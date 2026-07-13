"""Testes de contrato da API (smoke/regressão).

Verifica status HTTP e a estrutura (chaves de topo) das respostas — não faz
"golden snapshot" de valores, que seria frágil e quebraria a cada ajuste legítimo
de dado. Varre TODOS os IDs de patologia de cada domínio para dar cobertura ampla.
"""
import sqlite3

import pytest

import app as app_module

# Domínios "por agente" → valor esperado de `dominio` no detalhe.
AGENT_DOMINIOS = {
    "bacterias": "bacteriana",
    "virais": "viral",
    "fungicos": "fungico",
    "parasitos": "parasitario",
}

# Chaves de topo que todo detalhe (agente e crônico) deve conter.
DETALHE_KEYS = {
    "dominio",
    "patologia",
    "agentes",
    "top3_medicamentos",
    "tratamento_padrao",
    "sintomas",
    "criterios_diagnosticos",
    "escores_diagnosticos",
}


def test_health(client):
    # Readiness real: 200 e a contagem de patologias (banco abre e tem dados).
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["patologias"] > 0


def test_health_503_com_banco_inacessivel(monkeypatch, tmp_path):
    # Banco ausente/quebrado deve dar 503 (para o Railway não promover o deploy).
    from fastapi.testclient import TestClient

    monkeypatch.setattr(app_module, "DB_BACT_PATH", tmp_path / "inexistente.sqlite")
    with TestClient(app_module.app, raise_server_exceptions=False) as c:
        r = c.get("/health")
    assert r.status_code == 503
    assert r.json()["status"] == "error"


def test_root_serves_html(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "text/html" in r.headers["content-type"]


def test_limiter_presente():
    # A proteção de rate limit deve existir (o comportamento 429 é validado à
    # parte, manualmente, por depender de janela de tempo).
    assert hasattr(app_module, "limiter")


def test_rotas_de_dados_agrupadas_sob_api_router():
    # Preparação para auth/tier futuros: todas as 15 rotas de dados devem estar
    # sob um único APIRouter com prefixo /api/v1, para que protegê-las vire uma
    # linha (`dependencies=[...]`) em vez de editar cada rota.
    api_paths = {r.path for r in app_module.api.routes}
    assert app_module.api.prefix == "/api/v1"
    assert len(api_paths) == 15
    assert all(p.startswith("/api/v1/") for p in api_paths)


def test_saude_e_raiz_fora_do_api_router(client):
    # "/" e "/health" precisam continuar acessíveis sem passar pelo router de
    # dados: "/" é a porta de entrada; "/health" é o healthcheck do Railway, que
    # não pode ficar atrás de uma futura autenticação.
    api_paths = {r.path for r in app_module.api.routes}
    assert "/" not in api_paths
    assert "/health" not in api_paths
    assert client.get("/health").status_code == 200


@pytest.mark.parametrize("rota", list(AGENT_DOMINIOS))
def test_categorias(client, rota):
    r = client.get(f"/api/v1/{rota}/categorias")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


@pytest.mark.parametrize("rota", list(AGENT_DOMINIOS))
def test_patologias(client, rota):
    r = client.get(f"/api/v1/{rota}/patologias")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


@pytest.mark.parametrize("rota,dominio", list(AGENT_DOMINIOS.items()))
def test_detalhe_todos_os_ids(client, rota, dominio):
    ids = [p["id"] for p in client.get(f"/api/v1/{rota}/patologias").json()]
    assert ids, f"nenhuma patologia para {rota}"
    for pid in ids:
        r = client.get(f"/api/v1/{rota}/patologias/{pid}")
        assert r.status_code == 200, f"{rota}/{pid} -> {r.status_code}"
        body = r.json()
        assert DETALHE_KEYS.issubset(body), f"faltam chaves em {rota}/{pid}"
        assert body["dominio"] == dominio
    # Bacterianas mantêm a chave histórica extra "bacterias".
    if rota == "bacterias":
        assert "bacterias" in client.get(f"/api/v1/bacterias/patologias/{ids[0]}").json()


def test_cronicas(client):
    assert client.get("/api/v1/cronicas/categorias").status_code == 200
    ids = [p["id"] for p in client.get("/api/v1/cronicas/patologias").json()]
    assert ids, "nenhuma patologia cronica"
    for pid in ids:
        r = client.get(f"/api/v1/cronicas/patologias/{pid}")
        assert r.status_code == 200
        body = r.json()
        assert DETALHE_KEYS.issubset(body)
        assert body["dominio"] == "cronico"
        assert body["agentes"] == []


def test_radar_distingue_none_de_zero(client):
    # PEP8/idiom review: `campo or 0` misturava "desconhecido" (None) com "medido
    # como zero" no radar dos cards REAIS (via enrich(), is_fallback=False). Varre
    # os domínios de agente procurando um card assim com eficacia_pct/
    # resistencia_br_pct None e confirma que o radar propaga None (não 0/100
    # enganoso). Cards sintéticos (is_fallback=True) usam radar hardcoded por
    # design (fora de escopo desta correção) e são ignorados aqui.
    encontrou_algum = False
    for rota in AGENT_DOMINIOS:
        for pid in [p["id"] for p in client.get(f"/api/v1/{rota}/patologias").json()]:
            det = client.get(f"/api/v1/{rota}/patologias/{pid}").json()
            for m in det["top3_medicamentos"]:
                if m.get("is_fallback"):
                    continue
                if m.get("eficacia_pct") is None:
                    assert m["radar"]["eficacia"] is None
                    encontrou_algum = True
                if m.get("resistencia_br_pct") is None:
                    assert m["radar"]["seguranca"] is None
                    encontrou_algum = True


def test_card_real_define_is_fallback_explicito(client):
    # S20: enrich() (cards reais) agora define "is_fallback": False
    # explicitamente -- mesma forma que os cards sintéticos e os de crônicas,
    # que sempre definem a chave. Antes a chave ficava ausente nesse caminho.
    encontrou_algum = False
    for rota in AGENT_DOMINIOS:
        for pid in [p["id"] for p in client.get(f"/api/v1/{rota}/patologias").json()]:
            det = client.get(f"/api/v1/{rota}/patologias/{pid}").json()
            for m in det["top3_medicamentos"]:
                assert "is_fallback" in m, f"{rota}/{pid}: card sem a chave is_fallback"
                if not m["is_fallback"]:
                    encontrou_algum = True
    assert encontrou_algum, "nenhum card real (is_fallback=False) encontrado nos fixtures"
    assert encontrou_algum, "nenhum card real com dado ausente encontrado nos fixtures"


def test_detalhe_404(client):
    assert client.get("/api/v1/bacterias/patologias/99999999").status_code == 404


@pytest.mark.parametrize("url", ["/docs", "/redoc", "/openapi.json"])
def test_docs_publicas_desabilitadas(client, url):
    # Redução de superfície (API9): a documentação/schema não devem estar públicos.
    assert client.get(url).status_code == 404


def test_app_funciona_sem_docs(client):
    # Desabilitar as docs não afeta a aplicação em si.
    assert client.get("/").status_code == 200
    assert client.get("/health").status_code == 200
    assert client.get("/api/v1/bacterias/categorias").status_code == 200


def test_erro_inesperado_nao_vaza_detalhe(monkeypatch):
    # Um erro não tratado deve responder 500 genérico, sem vazar detalhe interno
    # (o stack trace/senha vai só para o log do servidor).
    from fastapi.testclient import TestClient

    def boom(cfg):
        raise RuntimeError("segredo interno: senha=abc123")

    monkeypatch.setattr(app_module, "_categorias", boom)
    with TestClient(app_module.app, raise_server_exceptions=False) as c:
        r = c.get("/api/v1/bacterias/categorias")
    assert r.status_code == 500
    # S24: envelope RFC 9457 (type/title/status/detail) -- mesma garantia de
    # segurança do S13, só a forma da resposta mudou.
    body = r.json()
    assert body["status"] == 500
    assert body["detail"] == "Erro interno do servidor"
    corpo = r.text
    assert "abc123" not in corpo
    assert "RuntimeError" not in corpo
    assert "Traceback" not in corpo


_ENVELOPE_KEYS = {"type", "title", "status", "detail"}


def test_erro_404_usa_envelope_rfc9457(client):
    r = client.get("/api/v1/bacterias/patologias/99999999")
    assert r.status_code == 404
    body = r.json()
    assert _ENVELOPE_KEYS <= body.keys()
    assert body["status"] == 404
    assert body["detail"] == "Patologia não encontrada"
    assert r.headers["content-type"] == "application/problem+json"


def test_erro_422_usa_envelope_rfc9457(client):
    r = client.get("/api/v1/bacterias/patologias/abc")
    assert r.status_code == 422
    body = r.json()
    assert _ENVELOPE_KEYS <= body.keys()
    assert body["status"] == 422
    # a lista de erros do Pydantic vira campo de extensão, nao o detail em si
    assert isinstance(body["errors"], list) and body["errors"]


def test_erro_429_usa_envelope_rfc9457():
    # Precisa de um TestClient próprio com o limiter ligado (a fixture global
    # desliga o limiter para não atrapalhar os outros testes).
    from fastapi.testclient import TestClient

    app_module.limiter.enabled = True
    try:
        with TestClient(app_module.app, raise_server_exceptions=False) as c:
            codigos = [c.get("/api/v1/bacterias/categorias").status_code for _ in range(125)]
            assert 429 in codigos, "limite de 120/min não disparou em 125 tentativas"
            r = c.get("/api/v1/bacterias/categorias")
            assert r.status_code == 429
            body = r.json()
            assert _ENVELOPE_KEYS <= body.keys()
            assert body["status"] == 429
    finally:
        app_module.limiter.enabled = False


def test_erros_compartilham_o_mesmo_envelope(client):
    # O ponto central do S24: 404/422/500 (e o 429, testado à parte) devem ter
    # exatamente o mesmo CONJUNTO de chaves de topo -- antes, cada um tinha uma
    # forma diferente ({"detail": str} vs {"detail": [...]} vs {"error": str}).
    r404 = client.get("/api/v1/bacterias/patologias/99999999")
    r422 = client.get("/api/v1/bacterias/patologias/abc")
    assert set(r404.json().keys()) >= _ENVELOPE_KEYS
    assert set(r422.json().keys()) >= _ENVELOPE_KEYS
    # ambos concordam nas 4 chaves-base (extensões como "errors" podem variar)
    assert {k: r404.json()[k] for k in ("type",)} == {k: r422.json()[k] for k in ("type",)}


def test_listagem_nao_infla_cache_por_categoria_id(client):
    # Fix API4: iterar categoria_id (controlado pelo cliente) não deve criar uma
    # entrada de cache por valor — a chave agora é fixa por domínio.
    before = len(app_module._cache)
    for cid in range(900000, 900050):
        assert client.get(f"/api/v1/bacterias/patologias?categoria_id={cid}").status_code == 200
    # no máximo 1 entrada nova (a listagem completa de bacterias), nunca 50
    assert len(app_module._cache) - before <= 1


def test_listagem_filtra_por_categoria_sem_vazar_fk(client):
    # O filtro por categoria continua funcionando e o FK interno não vaza.
    todas = client.get("/api/v1/bacterias/patologias").json()
    assert todas and all("categoria_id" not in p for p in todas)
    cid = client.get("/api/v1/bacterias/categorias").json()[0]["id"]
    filtradas = client.get(f"/api/v1/bacterias/patologias?categoria_id={cid}").json()
    assert len(filtradas) <= len(todas)


def test_cronicas_listagem_nao_infla_cache_por_categoria_id(client):
    # S22: cronicas_patologias agora delega a _patologias_lista, o mesmo helper
    # de bacterias/virais/etc -- confirma que a proteção do S11 (antes só
    # testada para bacterias) vale igual para o domínio crônico.
    before = len(app_module._cache)
    for cid in range(900000, 900050):
        assert client.get(f"/api/v1/cronicas/patologias?categoria_id={cid}").status_code == 200
    assert len(app_module._cache) - before <= 1


def test_cronicas_listagem_filtra_por_categoria_sem_vazar_fk(client):
    todas = client.get("/api/v1/cronicas/patologias").json()
    assert todas and all("categoria_id" not in p for p in todas)
    cid = client.get("/api/v1/cronicas/categorias").json()[0]["id"]
    filtradas = client.get(f"/api/v1/cronicas/patologias?categoria_id={cid}").json()
    assert len(filtradas) <= len(todas)


@pytest.mark.parametrize("url", ["/", "/health", "/api/v1/bacterias/categorias"])
def test_headers_de_seguranca(client, url):
    h = client.get(url).headers
    assert "content-security-policy" in h
    assert h["x-content-type-options"] == "nosniff"
    assert h["x-frame-options"] == "DENY"
    assert "strict-transport-security" in h
    # a CSP pragmática precisa permitir inline (frontend inline) e data: (ícones SVG)
    csp = h["content-security-policy"]
    assert "script-src 'self' 'unsafe-inline'" in csp
    assert "img-src 'self' data:" in csp


def test_cache_control_em_dados_de_sucesso(client):
    # Dados sob /api/v1/* só mudam a cada deploy (novo processo) — devem levar
    # Cache-Control para evitar rebusca desnecessária de conteúdo que o
    # cliente já sabe, por contrato, que não muda durante a vida do processo.
    r = client.get("/api/v1/bacterias/categorias")
    assert r.headers["cache-control"] == "public, max-age=3600"

    pid = client.get("/api/v1/bacterias/patologias").json()[0]["id"]
    r_det = client.get(f"/api/v1/bacterias/patologias/{pid}")
    assert r_det.headers["cache-control"] == "public, max-age=3600"


def test_cache_control_ausente_fora_do_api(client):
    # "/" e "/health" não são "dados" versionados — não devem ganhar o
    # Cache-Control de 1h (health precisa refletir o estado real a cada chamada
    # do healthcheck do Railway; "/" serve sempre o mesmo HTML estático).
    assert "cache-control" not in {k.lower() for k in client.get("/").headers}
    assert "cache-control" not in {k.lower() for k in client.get("/health").headers}


def test_cache_control_ausente_em_erro(client):
    # Respostas de erro (404/422/429/500) nunca devem ser cacheadas.
    r404 = client.get("/api/v1/bacterias/patologias/99999999")
    r422 = client.get("/api/v1/bacterias/patologias/abc")
    assert "cache-control" not in {k.lower() for k in r404.headers}
    assert "cache-control" not in {k.lower() for k in r422.headers}


def test_gzip_em_resposta_grande(client):
    # Uma resposta JSON grande (detalhe) deve vir comprimida quando o cliente aceita.
    pid = client.get("/api/v1/bacterias/patologias").json()[0]["id"]
    r = client.get(
        f"/api/v1/bacterias/patologias/{pid}", headers={"Accept-Encoding": "gzip"}
    )
    assert r.status_code == 200
    assert r.headers.get("content-encoding") == "gzip"


def test_gzip_ignora_resposta_pequena(client):
    # Resposta pequena (< minimum_size) NÃO deve ser comprimida (evita inflar bytes).
    r = client.get("/health", headers={"Accept-Encoding": "gzip"})
    assert r.status_code == 200
    assert r.headers.get("content-encoding") != "gzip"


def test_cache_limitado():
    # O cache não cresce além do teto; ao encher, descarta as entradas mais antigas.
    c = app_module._BoundedCache(max_size=3)
    for i in range(10):
        c[f"k{i}"] = i
    assert len(c) == 3
    assert "k9" in c and "k8" in c and "k7" in c  # mantém as mais recentes
    assert "k0" not in c and "k6" not in c        # descartou as mais antigas
    # sobrescrever chave existente não conta como nova nem estoura o teto
    c["k9"] = 99
    assert len(c) == 3 and c["k9"] == 99


def test_cache_seguro_sob_concorrencia():
    # 40 threads (o tamanho do threadpool do FastAPI) martelam o cache ao mesmo
    # tempo: nenhuma exceção deve escapar e o teto deve ser respeitado (o Lock
    # torna o check-then-act atômico).
    import threading

    c = app_module._BoundedCache(max_size=64)
    errors = []
    start = threading.Barrier(40)

    def hammer(tid):
        start.wait()  # largada simultânea, maximiza a corrida
        for i in range(1500):
            try:
                c[f"k{tid}-{i}"] = tid  # chaves novas → evicção constante
            except Exception as e:  # noqa: BLE001 — o teste é justamente pegar qualquer uma
                errors.append(repr(e))

    threads = [threading.Thread(target=hammer, args=(t,)) for t in range(40)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert errors == []          # nenhuma exceção escapou do __setitem__
    assert len(c) <= 64          # teto respeitado, sem overage
    assert len(c) == len(list(c.keys()))  # dict íntegro


def _agentdomain_kwargs(**overrides):
    # AgentDomain é @dataclass com todos os campos obrigatórios (S20) -- monta um
    # conjunto completo e válido, sobrescrevendo só o(s) campo(s) sob teste.
    base = dict(
        dominio="x", route="x", junction="x", agent_table="x", agent_fk="x",
        agent_cols=(), drug_table="x", drug_class_table="x", drug_fk="x",
        efficacy_table="x", treatment_table="x", treatment_principal="x",
        posology_table="x", interactions_table="x", agent_out_key="x",
        categorias_filtered=False, extra_agent_key=None,
    )
    base.update(overrides)
    return base


def test_agentdomain_valida_identificadores_sql():
    # Blindagem de injeção: identificadores interpolados em SQL devem casar com
    # [a-z0-9_]; um valor fora do padrão falha na construção (no boot), não em runtime.
    with pytest.raises(ValueError):
        app_module.AgentDomain(**_agentdomain_kwargs(junction="patologia; DROP TABLE x"))
    with pytest.raises(ValueError):
        app_module.AgentDomain(**_agentdomain_kwargs(agent_cols=("nome", "col invalida")))
    # identificadores válidos não levantam
    app_module.AgentDomain(
        **_agentdomain_kwargs(junction="patologia_bacteria", agent_cols=("nome_cientifico",))
    )


def test_agentdomain_e_dataclass_com_campos_obrigatorios():
    # S20: AgentDomain virou @dataclass com todo campo obrigatório -- construir
    # sem um deles (o próprio TypeError do Python, verificado à parte via mypy
    # com "call-arg") deve falhar em runtime também, não só silenciosamente
    # deixar o atributo ausente.
    with pytest.raises(TypeError):
        app_module.AgentDomain(junction="patologia_bacteria")


def test_conn_bact_e_read_only():
    # A conexão de patologias permite leitura, mas rejeita escrita (query_only).
    with app_module.conn_bact() as db:
        assert db.execute("SELECT COUNT(*) FROM patologias").fetchone()[0] > 0
        with pytest.raises(sqlite3.OperationalError):
            db.execute("CREATE TABLE _proibido (x)")


@pytest.mark.parametrize("texto,esperado", [
    ("Metformina 500mg", "Metformina"),
    ("Metformina + Sitagliptina", "Metformina"),
    ("Losartana/Hidroclorotiazida", "Losartana"),
    ("Enalapril & Anlodipino", "Enalapril"),
    ("Amoxicilina (500mg 8/8h)", "Amoxicilina"),
    ("  Ibuprofeno  ", "Ibuprofeno"),
    (None, None),
    ("", None),
    ("   ", None),
])
def test_extract_first_drug(texto, esperado):
    # S21: _extract_first_drug foi promovida de dentro de cronicas_detalhe para
    # função de módulo -- é pura (sem banco/estado externo), então já era
    # testável isoladamente; só estava aninhada por convenção. Cobre os casos
    # de combinação (+, /, &), dose numérica, dose entre parênteses e vazio/None.
    assert app_module._extract_first_drug(texto) == esperado


def test_lookup_med_none_e_vazio():
    # _lookup_med recebe db como parâmetro (nunca capturou nada por closure) --
    # promovida no S21. nome_raw None/vazio retorna None sem tocar o banco.
    with app_module.conn_bact() as db:
        assert app_module._lookup_med(db, None) is None
        assert app_module._lookup_med(db, "") is None


def test_lookup_med_cascata_no_banco_real():
    with app_module.conn_bact() as db:
        nome_real = db.execute("SELECT nome_generico FROM medicamentos LIMIT 1").fetchone()[0]

        # nome exato
        r = app_module._lookup_med(db, nome_real)
        assert r is not None and r["nome_generico"] == nome_real

        # case-insensitive
        r = app_module._lookup_med(db, nome_real.upper())
        assert r is not None and r["nome_generico"] == nome_real

        # prefixo (primeira palavra + "%")
        prefixo = nome_real.split()[0][: max(1, len(nome_real.split()[0]) - 1)]
        r = app_module._lookup_med(db, prefixo)
        assert r is not None

        # inexistente
        assert app_module._lookup_med(db, "medicamento-que-nao-existe-xyz") is None
