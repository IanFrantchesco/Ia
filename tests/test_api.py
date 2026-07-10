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
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert "patologias_bacterianas" in body["dbs"]


def test_root_serves_html(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "text/html" in r.headers["content-type"]


def test_limiter_presente():
    # A proteção de rate limit deve existir (o comportamento 429 é validado à
    # parte, manualmente, por depender de janela de tempo).
    assert hasattr(app_module, "limiter")


@pytest.mark.parametrize("rota", list(AGENT_DOMINIOS))
def test_categorias(client, rota):
    r = client.get(f"/api/{rota}/categorias")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


@pytest.mark.parametrize("rota", list(AGENT_DOMINIOS))
def test_patologias(client, rota):
    r = client.get(f"/api/{rota}/patologias")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


@pytest.mark.parametrize("rota,dominio", list(AGENT_DOMINIOS.items()))
def test_detalhe_todos_os_ids(client, rota, dominio):
    ids = [p["id"] for p in client.get(f"/api/{rota}/patologias").json()]
    assert ids, f"nenhuma patologia para {rota}"
    for pid in ids:
        r = client.get(f"/api/{rota}/patologia/{pid}")
        assert r.status_code == 200, f"{rota}/{pid} -> {r.status_code}"
        body = r.json()
        assert DETALHE_KEYS.issubset(body), f"faltam chaves em {rota}/{pid}"
        assert body["dominio"] == dominio
    # Bacterianas mantêm a chave histórica extra "bacterias".
    if rota == "bacterias":
        assert "bacterias" in client.get(f"/api/bacterias/patologia/{ids[0]}").json()


def test_cronicas(client):
    assert client.get("/api/cronicas/categorias").status_code == 200
    ids = [p["id"] for p in client.get("/api/cronicas/patologias").json()]
    assert ids, "nenhuma patologia cronica"
    for pid in ids:
        r = client.get(f"/api/cronicas/patologia/{pid}")
        assert r.status_code == 200
        body = r.json()
        assert DETALHE_KEYS.issubset(body)
        assert body["dominio"] == "cronico"
        assert body["agentes"] == []


def test_detalhe_404(client):
    assert client.get("/api/bacterias/patologia/99999999").status_code == 404


@pytest.mark.parametrize("url", ["/", "/health", "/api/bacterias/categorias"])
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


def test_gzip_em_resposta_grande(client):
    # Uma resposta JSON grande (detalhe) deve vir comprimida quando o cliente aceita.
    pid = client.get("/api/bacterias/patologias").json()[0]["id"]
    r = client.get(
        f"/api/bacterias/patologia/{pid}", headers={"Accept-Encoding": "gzip"}
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


def test_conn_bact_e_read_only():
    # A conexão de patologias permite leitura, mas rejeita escrita (query_only).
    with app_module.conn_bact() as db:
        assert db.execute("SELECT COUNT(*) FROM patologias").fetchone()[0] > 0
        with pytest.raises(sqlite3.OperationalError):
            db.execute("CREATE TABLE _proibido (x)")
