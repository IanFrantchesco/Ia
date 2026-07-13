"""
Backend FastAPI — Patologias
Painel clínico: bacterianas, virais, fúngicas, parasitárias e crônicas.
Critérios diagnósticos, tratamento padrão-ouro, posologia e interações.

Arquitetura
-----------
Os quatro domínios "por agente" (bacteriano, viral, fúngico, parasitário)
compartilham a mesma lógica, parametrizada por ``AGENT_DOMAINS`` e servida por
``_agent_detalhe``. O domínio crônico tem fluxo próprio (não há agente
etiológico). Os dados vêm de um único SQLite read-only, montado no build por
``database/build_db.py``; respostas de listagem são memoizadas em ``_cache``.
"""

import logging
import re
import sqlite3
import threading
from collections import defaultdict
from contextlib import asynccontextmanager, contextmanager
from pathlib import Path

from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
log = logging.getLogger(__name__)

APP_VERSION  = "1.0.0"
DB_BACT_PATH = Path(__file__).parent / "database" / "patologias_bacterianas_br.sqlite"
STATIC       = Path(__file__).parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Ciclo de vida do app (substitui o ``@app.on_event`` deprecated).

    O código antes do ``yield`` roda no startup; o de depois, no shutdown. É aqui
    que, no futuro, a conexão com o banco de clientes (persistente) será
    inicializada — por ora, apenas confirma a presença do banco read-only.
    """
    if DB_BACT_PATH.exists():
        # Diagnóstico de boot: journal_mode real (confirma se WAL ativou no FS de
        # produção) + contagem de patologias por domínio (sanidade: 0 = build do
        # banco falhou). Transforma o startup num autodiagnóstico útil no log.
        with conn_bact() as db:
            modo = db.execute("PRAGMA journal_mode").fetchone()[0]
            total = db.execute("SELECT count(*) FROM patologias").fetchone()[0]
            por_dominio = {
                rota: db.execute(
                    f"SELECT count(DISTINCT patologia_id) FROM {cfg.junction}"
                ).fetchone()[0]
                for rota, cfg in AGENT_DOMAINS.items()
            }
        log.info("app v%s | DB %s | journal_mode=%s | patologias=%d | por_dominio=%s",
                 APP_VERSION, DB_BACT_PATH.name, modo, total, por_dominio)
        if total == 0:
            log.critical("ALERTA: 0 patologias no startup — build do banco falhou")
    else:
        log.critical("DB AUSENTE no startup: %s — deploy ficará unhealthy "
                     "(provável falha de build). App sobe, mas /health dará 503.",
                     DB_BACT_PATH)
    yield
    # (shutdown: nada a liberar por enquanto)


# docs_url/redoc_url/openapi_url = None: desativa a documentação interativa e o
# schema OpenAPI públicos. Reduz a divulgação da superfície da API (API9) — num
# produto a ser comercializado, não convém expor toda a lista de endpoints e seus
# schemas. Podem ser reativados/protegidos por auth quando/se fizer sentido.
app = FastAPI(
    title="Patologias — Painel Clínico",
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

# ── Compressão Gzip ──────────────────────────────────────────────────────────
# Comprime respostas JSON grandes (>500 bytes) quando o cliente aceita gzip —
# reduz o egress ~60–80% e corta custo, sem alterar o conteúdo (o navegador
# descomprime). Registrado ANTES do SlowAPIMiddleware de propósito: o SlowAPI é
# um BaseHTTPMiddleware que "streamifica" a resposta; se o Gzip ficasse por fora
# dele, veria um stream e comprimiria até respostas minúsculas, ignorando o
# minimum_size. Como o Gzip fica por dentro, ele vê a resposta original e
# respeita o limite (respostas pequenas como /health não são comprimidas).
app.add_middleware(GZipMiddleware, minimum_size=500)

# ── Rate limiting (limite de requisições) ────────────────────────────────────
# Limita cada visitante (identificado pelo IP) a 120 requisições por minuto.
# Protege contra sobrecarga do servidor (DoS) e cópia em massa do banco
# (scraping). O SlowAPIMiddleware aplica esse limite a TODAS as rotas
# automaticamente — não é preciso decorar cada endpoint. Quem ultrapassa o
# limite recebe a resposta HTTP 429 ("Too Many Requests") em vez dos dados.
limiter = Limiter(key_func=get_remote_address, default_limits=["120/minute"])
app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded, _rate_limit_exceeded_handler  # type: ignore[arg-type]
)  # incompatibilidade de tipagem conhecida entre o stub do Starlette (espera
   # handler para Exception genérica) e o handler do slowapi (tipado para
   # RateLimitExceeded); comportamento em runtime correto — Python não impõe
   # os tipos, e o FastAPI despacha por tipo de exceção registrado.
app.add_middleware(SlowAPIMiddleware)


# ── Handler global de erros inesperados ──────────────────────────────────────
# Garante que uma exceção não tratada NUNCA vaze detalhe interno/stack trace ao
# cliente: o detalhe completo vai só para o log do servidor; o cliente recebe um
# 500 genérico. Não intercepta HTTPException (404/422) nem o 429 do slowapi —
# esses são tipos distintos e seguem pelos handlers próprios.
@app.exception_handler(Exception)
async def handle_unexpected(request, exc):
    log.exception("Erro não tratado em %s %s", request.method, request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Erro interno do servidor"})

# ── Headers de segurança ─────────────────────────────────────────────────────
# Cabeçalhos HTTP de hardening aplicados a toda resposta. A CSP é "pragmática":
# permite 'unsafe-inline' em script/style porque o frontend atual é fortemente
# inline (blocos <script>/<style> e onclick=). Uma CSP estrita exigiria refatorar
# todo o frontend — fica para depois. 'img-src data:' cobre os ícones SVG inline.
# HSTS é seguro: o Railway serve HTTPS na borda; navegadores ignoram HSTS em HTTP.
SECURITY_HEADERS = {
    "Content-Security-Policy": (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline'; "
        "style-src 'self' 'unsafe-inline'; "
        "img-src 'self' data:; "
        "connect-src 'self'; "
        "font-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "frame-ancestors 'none'"
    ),
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
}


@app.middleware("http")
async def add_security_headers(request, call_next):
    """Injeta os headers de segurança em toda resposta (sem sobrescrever existentes)."""
    response = await call_next(request)
    for name, value in SECURITY_HEADERS.items():
        response.headers.setdefault(name, value)
    return response


# Cache em memória do processo para listagens/categorias/detalhes (read-only).
# Limitação consciente: não expira e não é compartilhado entre workers — após
# reconstruir o banco, reinicie o processo para refletir os novos dados.


class _BoundedCache(dict):
    """``dict`` com teto de tamanho, seguro sob concorrência.

    Ao inserir uma chave nova com o cache cheio, descarta a entrada mais antiga
    (``dict`` preserva a ordem de inserção). Evita crescimento indefinido de
    memória sob uso amplo. Todas as gravações ``_cache[k] = v`` já existentes
    passam por aqui — nenhum call site muda.

    As rotas ``def`` do FastAPI rodam no threadpool (até 40 threads), todas
    escrevendo neste objeto. O ``check-then-act`` (checar tamanho → evictar →
    inserir) roda sob um ``Lock``, tornando-o atômico: sem corrida na evicção
    (nada de ``RuntimeError``/``KeyError`` a engolir) e o teto é respeitado com
    exatidão. A seção crítica são poucas operações de ``dict`` (~µs), então a
    contenção é desprezível frente ao tempo das queries. As leituras
    (``k in cache``, ``cache[k]``) não precisam do lock — são atômicas sob o GIL.
    """

    def __init__(self, max_size):
        super().__init__()
        self._max = max_size
        self._lock = threading.Lock()

    def __setitem__(self, key, value):
        with self._lock:
            if key not in self and len(self) >= self._max:
                dict.__delitem__(self, next(iter(self)))
            dict.__setitem__(self, key, value)


_cache = _BoundedCache(max_size=2048)

# Normalização 0–100 para o gráfico radar dos medicamentos.
# EVIDENCIA_SCORE: nível de evidência (A = ECR … D = consenso de especialistas).
# LINHA_SCORE: linha de tratamento (1ª escolha pesa mais que 3ª).
EVIDENCIA_SCORE = {"A": 100, "B": 75, "C": 50, "D": 25}
LINHA_SCORE     = {1: 100, 2: 60, 3: 30}

# ── helpers ────────────────────────────────────────────────────────────────

@contextmanager
def _connect(db_path, *, read_only=True):
    """Abre uma conexão SQLite configurada e a fecha ao sair do bloco.

    O ``journal_mode`` NÃO é setado aqui: WAL é persistente no header do arquivo
    (definido uma única vez em ``build_db.py``), então cada conexão apenas o herda.
    ``busy_timeout`` dá tolerância a lock momentâneo; ``row_factory=Row`` dá acesso
    às colunas por nome. Quando ``read_only`` (padrão), aplica ``PRAGMA
    query_only=ON``, que impede qualquer escrita acidental — reforço para o banco
    de patologias, que é só de leitura. O parâmetro prevê o futuro banco de
    clientes: esse será read-write (num Volume persistente) e abrirá com
    ``read_only=False``.
    """
    db = sqlite3.connect(db_path, timeout=10)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA busy_timeout=5000")
    if read_only:
        db.execute("PRAGMA query_only=ON")
    try:
        yield db
    finally:
        db.close()


@contextmanager
def conn_bact():
    """Conexão com o banco de patologias (só leitura). Wrapper fino de ``_connect``."""
    with _connect(DB_BACT_PATH, read_only=True) as db:
        yield db


# ── endpoints ──────────────────────────────────────────────────────────────

@app.get("/")
def root():
    """Porta de entrada: serve o painel clínico (patologias.html)."""
    return FileResponse(STATIC / "patologias.html")


@app.get("/health")
def health():
    """Readiness check: 200 só se o banco abre, responde e tem dados; senão 503.

    O Railway usa o STATUS HTTP do healthcheckPath — 503 impede a promoção de um
    deploy quebrado (banco ausente, corrompido ou vazio), mantendo a versão
    anterior saudável no ar. Um `exists()` não bastaria: não valida que o arquivo
    realmente abre nem que tem dados.
    """
    try:
        with conn_bact() as db:
            n = db.execute("SELECT count(*) FROM patologias").fetchone()[0]
    except Exception as e:  # arquivo ausente/corrompido/travado
        log.error("healthcheck falhou ao consultar o banco: %s", e)
        return JSONResponse(status_code=503, content={"status": "error"})
    if n == 0:  # abre mas está vazio → build do banco falhou
        return JSONResponse(status_code=503, content={"status": "degraded", "patologias": 0})
    return {"status": "ok", "patologias": n}


# Agrupa as rotas de dados sob um único router com prefixo /api. Puramente
# estrutural (nenhuma lógica de autenticação hoje): quando a assinatura entrar,
# proteger todos os dados vira uma linha (`dependencies=[Depends(auth)]` aqui),
# em vez de editar cada rota. "/", "/health" e o mount de estáticos ficam DE
# PROPÓSITO fora do router — precisam continuar acessíveis sem login (a tela de
# entrada, e o healthcheck do Railway, que não pode ficar atrás de auth).
api = APIRouter(prefix="/api")


# ══════════════════════════════════════════════════════════════════════════
# PATOLOGIAS POR AGENTE (bacterianas · virais · fúngicas · parasitárias)
#
# Os quatro domínios compartilham exatamente a mesma lógica de detalhe,
# listagem e categorias — diferindo apenas nos nomes de tabelas/colunas.
# Toda a configuração que muda entre eles fica em AGENT_DOMAINS; a lógica
# vive uma única vez em _agent_detalhe / _patologias / _categorias.
# ══════════════════════════════════════════════════════════════════════════


# Identificadores de tabela/coluna válidos: só letras minúsculas, dígitos e "_".
_IDENT_RE = re.compile(r"^[a-z_][a-z0-9_]*$")

# Campos de AgentDomain que são interpolados como IDENTIFICADORES em SQL (nomes
# de tabela/coluna via f-string). São validados na construção contra _IDENT_RE.
_SQL_IDENT_FIELDS = frozenset({
    "junction", "agent_table", "agent_fk",
    "drug_table", "drug_class_table", "drug_fk",
    "efficacy_table", "treatment_table", "treatment_principal",
    "posology_table", "interactions_table", "agent_out_key",
})


class AgentDomain:
    """Configuração de um domínio de patologia baseada em agente etiológico.

    Todos os identificadores aqui são constantes confiáveis (nunca entrada do
    usuário), portanto sua interpolação em SQL via f-string é segura. Para
    transformar essa disciplina em **garantia de código** (o código vai crescer),
    o ``__init__`` valida na construção que cada identificador interpolado em SQL
    casa com ``_IDENT_RE`` — um valor fora do padrão faz o app **falhar no boot**,
    não em runtime.

    Os atributos são anotados no corpo da classe (sem valor) só para o mypy
    enxergá-los — quem de fato os define é ``__dict__.update(kw)`` no ``__init__``;
    isso não muda nenhum comportamento em runtime.
    """

    dominio: str
    route: str
    junction: str
    agent_table: str
    agent_fk: str
    agent_cols: tuple[str, ...]
    drug_table: str
    drug_class_table: str
    drug_fk: str
    efficacy_table: str
    treatment_table: str
    treatment_principal: str
    posology_table: str
    interactions_table: str
    agent_out_key: str
    categorias_filtered: bool
    extra_agent_key: str | None

    def __init__(self, **kw):
        self.__dict__.update(kw)
        for field in _SQL_IDENT_FIELDS:
            val = kw.get(field)
            if val is not None and not _IDENT_RE.match(val):
                raise ValueError(
                    f"AgentDomain: identificador SQL inválido em {field!r}: {val!r}"
                )
        for col in kw.get("agent_cols", ()):
            if not _IDENT_RE.match(col):
                raise ValueError(
                    f"AgentDomain: coluna inválida em agent_cols: {col!r}"
                )


AGENT_DOMAINS = {
    "bacterias": AgentDomain(
        dominio="bacteriana", route="bacterias",
        junction="patologia_bacteria", agent_table="bacterias", agent_fk="bacteria_id",
        agent_cols=("nome_cientifico", "nome_comum", "gram",
                    "aerobiose", "formato", "resistencia_natural"),
        drug_table="antibioticos", drug_class_table="classes_antibioticos",
        drug_fk="antibiotico_id", efficacy_table="eficacia_antibiotico",
        treatment_table="tratamento_padrao_ouro", treatment_principal="antibiotico_principal",
        posology_table="posologia", interactions_table="interacoes_medicamentosas",
        agent_out_key="bacteria", categorias_filtered=False, extra_agent_key="bacterias",
    ),
    "virais": AgentDomain(
        dominio="viral", route="virais",
        junction="patologia_virus", agent_table="virus", agent_fk="virus_id",
        agent_cols=("nome_cientifico", "nome_comum", "tipo_acido_nucleico",
                    "envelope", "transmissao_principal"),
        drug_table="antivirais", drug_class_table="classes_antivirais",
        drug_fk="antiviral_id", efficacy_table="eficacia_antiviral",
        treatment_table="tratamento_padrao_ouro_viral", treatment_principal="antiviral_principal",
        posology_table="posologia_viral", interactions_table="interacoes_antivirais",
        agent_out_key="agente", categorias_filtered=True, extra_agent_key=None,
    ),
    "fungicos": AgentDomain(
        dominio="fungico", route="fungicos",
        junction="patologia_fungo", agent_table="fungos", agent_fk="fungo_id",
        agent_cols=("nome_cientifico", "nome_comum", "tipo",
                    "transmissao_principal", "reservatorio"),
        drug_table="antifungicos", drug_class_table="classes_antifungicos",
        drug_fk="antifungico_id", efficacy_table="eficacia_antifungico",
        treatment_table="tratamento_padrao_ouro_fungico", treatment_principal="antifungico_principal",
        posology_table="posologia_fungica", interactions_table="interacoes_antifungicos",
        agent_out_key="agente", categorias_filtered=True, extra_agent_key=None,
    ),
    "parasitos": AgentDomain(
        dominio="parasitario", route="parasitos",
        junction="patologia_parasito", agent_table="parasitos", agent_fk="parasito_id",
        agent_cols=("nome_cientifico", "nome_comum", "tipo",
                    "ciclo_hospedeiro", "vetor"),
        drug_table="antiparasitarios", drug_class_table="classes_antiparasitarios",
        drug_fk="antiparasitario_id", efficacy_table="eficacia_antiparasitario",
        treatment_table="tratamento_padrao_ouro_parasitario",
        treatment_principal="antiparasitario_principal",
        posology_table="posologia_parasitaria", interactions_table="interacoes_antiparasitarios",
        agent_out_key="agente", categorias_filtered=False, extra_agent_key=None,
    ),
}


# ── helpers compartilhados (usados também pelo domínio crônico) ──────────────

def _fetch_patologia(db: sqlite3.Connection, patologia_id: int) -> sqlite3.Row:
    """Cabeçalho da patologia; levanta 404 se não existir."""
    pat = db.execute(
        """SELECT p.id, p.nome, p.cid10, p.descricao,
                  p.prevalencia_br, p.mortalidade_br, p.populacao_risco,
                  p.notificacao_compulsoria, p.tipo_notificacao,
                  c.nome AS categoria, c.sistema,
                  fo.sigla AS fonte_sigla, fo.nome AS fonte_nome
           FROM patologias p
           JOIN categorias_patologias c ON c.id = p.categoria_id
           LEFT JOIN fontes_oficiais fo ON fo.id = p.fonte_epidemio_id
           WHERE p.id = ?""",
        (patologia_id,),
    ).fetchone()
    if not pat:
        raise HTTPException(404, "Patologia não encontrada")
    return pat


def _fetch_clinical(
    db: sqlite3.Connection, patologia_id: int
) -> tuple[list[dict], list[dict], list[dict]]:
    """Sintomas, critérios diagnósticos e escores — idênticos em todo domínio."""
    sintomas = db.execute(
        """SELECT s.nome, s.sistema, s.tipo,
                  ps.frequencia, ps.onset_texto, ps.severidade, ps.ordem
           FROM patologia_sintoma ps
           JOIN sintomas s ON s.id = ps.sintoma_id
           WHERE ps.patologia_id = ?
           ORDER BY ps.ordem, s.nome""",
        (patologia_id,),
    ).fetchall()
    criterios = db.execute(
        """SELECT nome, categoria, tipo, descricao, valor_referencia, fonte, ordem
           FROM criterios_diagnosticos
           WHERE patologia_id = ?
           ORDER BY ordem, nome""",
        (patologia_id,),
    ).fetchall()
    escores = db.execute(
        """SELECT nome_escore, descricao, interpretacao, fonte
           FROM escores_diagnosticos
           WHERE patologia_id = ?
           ORDER BY ordem""",
        (patologia_id,),
    ).fetchall()
    return (
        [dict(s) for s in sintomas],
        [dict(c) for c in criterios],
        [dict(e) for e in escores],
    )


# ── listagem e categorias (genéricas) ───────────────────────────────────────

def _categorias(cfg: "AgentDomain") -> list[dict]:
    """Categorias (sistemas corporais) do domínio.

    ``categorias_filtered=True`` (viral, fúngico) restringe às categorias que
    de fato têm patologias no domínio; bacteriano e parasitário retornam todas
    por decisão histórica de produto.
    """
    key = f"{cfg.route}:categorias"
    if key not in _cache:
        if cfg.categorias_filtered:
            sql = f"""SELECT DISTINCT c.id, c.nome, c.sistema
                      FROM categorias_patologias c
                      JOIN patologias p ON p.categoria_id = c.id
                      JOIN {cfg.junction} j ON j.patologia_id = p.id
                      ORDER BY c.nome"""
        else:
            sql = "SELECT id, nome, sistema FROM categorias_patologias ORDER BY nome"
        with conn_bact() as db:
            rows = db.execute(sql).fetchall()
        _cache[key] = [dict(r) for r in rows]
    return _cache[key]


def _patologias(cfg: "AgentDomain", categoria_id: int | None) -> list[dict]:
    """Lista as patologias do domínio, opcionalmente filtradas por categoria.

    O cache é indexado por uma chave **fixa por domínio** (a listagem completa),
    e o filtro por ``categoria_id`` é feito em memória. Antes, a chave incluía
    ``categoria_id`` — controlado pelo cliente —, o que permitia inflar o cache
    com entradas-lixo (categorias inexistentes cacheavam ``[]``) e evictar as
    entradas legítimas. Filtrar ~350 linhas em memória é trivial.
    """
    key = f"{cfg.route}:patologias"
    if key not in _cache:
        # inclui p.categoria_id apenas para o filtro em memória (removido da saída)
        sql = f"""
            SELECT DISTINCT p.id, p.categoria_id, p.nome, p.cid10, p.prevalencia_br,
                   p.mortalidade_br, p.notificacao_compulsoria, p.tipo_notificacao,
                   c.nome AS categoria
            FROM patologias p
            JOIN categorias_patologias c ON c.id = p.categoria_id
            JOIN {cfg.junction} j ON j.patologia_id = p.id
            ORDER BY p.nome
        """
        with conn_bact() as db:
            rows = db.execute(sql).fetchall()
        _cache[key] = [dict(r) for r in rows]
    todas = _cache[key]
    filtradas = [p for p in todas if not categoria_id or p["categoria_id"] == categoria_id]
    # remove o FK interno da resposta (mantém o contrato de saída idêntico)
    return [{k: v for k, v in p.items() if k != "categoria_id"} for p in filtradas]


# ── detalhe (genérico) ──────────────────────────────────────────────────────

def _agent_detalhe(cfg: "AgentDomain", patologia_id: int) -> dict:
    """Detalhe completo de uma patologia por agente etiológico.

    Os "top 3 medicamentos" seguem uma estratégia em três níveis, do dado mais
    forte ao mais fraco:
      1. eficácia comparativa específica da patologia (tabela ``eficacia_*``);
      2. se ausente, eficácia genérica do agente principal (fallback);
      3. se ainda ausente, cards sintéticos a partir da diretriz padrão-ouro
         (marcados com ``is_fallback=True``).
    Posologias e interações dos cards reais são buscadas em lote para evitar o
    problema N+1. Os identificadores interpolados no SQL vêm sempre de ``cfg``
    (constantes confiáveis); os valores continuam parametrizados com ``?``.

    O resultado é memoizado em ``_cache`` por (domínio, patologia): como este é o
    endpoint mais pesado (~10 consultas por chamada) e os dados são read-only,
    guardar a resposta pronta evita refazer todo o trabalho a cada acesso.
    """
    cache_key = f"{cfg.route}:detalhe:{patologia_id}"
    if cache_key in _cache:
        return _cache[cache_key]

    with conn_bact() as db:
        pat = _fetch_patologia(db, patologia_id)

        agent_select = ", ".join(f"ag.{c}" for c in cfg.agent_cols)
        agentes = db.execute(
            f"""SELECT {agent_select}, j.papel, j.frequencia_pct
                FROM {cfg.junction} j
                JOIN {cfg.agent_table} ag ON ag.id = j.{cfg.agent_fk}
                WHERE j.patologia_id = ?
                ORDER BY j.papel, j.frequencia_pct DESC""",
            (patologia_id,),
        ).fetchall()

        eff_cols = f"""
            a.id AS {cfg.drug_fk},
            a.nome_generico, a.nome_comercial, a.via_administracao, a.disponivel_sus,
            ca.nome AS classe,
            ag.nome_cientifico AS {cfg.agent_out_key},
            e.eficacia_pct, e.linha_tratamento, e.nivel_evidencia,
            e.resistencia_br_pct, e.consideracoes,
            fo.sigla AS fonte, fo.nome AS fonte_nome, fo.ano AS fonte_ano"""
        eff_from = f"""
            FROM {cfg.efficacy_table} e
            JOIN {cfg.drug_table} a ON a.id = e.{cfg.drug_fk}
            JOIN {cfg.drug_class_table} ca ON ca.id = a.classe_id
            JOIN {cfg.agent_table} ag ON ag.id = e.{cfg.agent_fk}
            LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id"""

        meds = db.execute(
            f"""SELECT {eff_cols} {eff_from}
                WHERE e.patologia_id = ?
                ORDER BY e.eficacia_pct DESC, e.linha_tratamento ASC
                LIMIT 3""",
            (patologia_id,),
        ).fetchall()

        # Fallback: eficácia genérica do agente principal (sem patologia específica)
        if not meds and agentes:
            principal = agentes[0]["nome_cientifico"]
            agent_id_row = db.execute(
                f"SELECT id FROM {cfg.agent_table} WHERE nome_cientifico = ?",
                (principal,),
            ).fetchone()
            if agent_id_row:
                meds = db.execute(
                    f"""SELECT {eff_cols} {eff_from}
                        WHERE e.{cfg.agent_fk} = ? AND e.patologia_id IS NULL
                        ORDER BY e.eficacia_pct DESC, e.linha_tratamento ASC
                        LIMIT 3""",
                    (agent_id_row["id"],),
                ).fetchall()

        tratamento = db.execute(
            f"""SELECT t.{cfg.treatment_principal}, t.combinacao,
                       t.regime_resumido, t.duracao_resumida, t.justificativa,
                       t.alternativa_alergia, t.alternativa_resistencia,
                       t.obs_especiais, t.grau_recomendacao, t.nivel_evidencia,
                       t.ano_diretriz,
                       fo.sigla AS fonte_sigla, fo.nome AS fonte_nome
                FROM {cfg.treatment_table} t
                LEFT JOIN fontes_oficiais fo ON fo.id = t.fonte_id
                WHERE t.patologia_id = ?""",
            (patologia_id,),
        ).fetchone()

        def _pos_int_single(aid: int) -> tuple[list[dict], list[dict]]:
            pos = [dict(r) for r in db.execute(
                f"""SELECT po.populacao, po.dose_unitaria, po.frequencia, po.via,
                           po.duracao_min_dias, po.duracao_max_dias, po.duracao_texto,
                           po.ajuste_renal, po.ajuste_hepatico, po.observacoes,
                           fo.sigla AS fonte
                    FROM {cfg.posology_table} po
                    LEFT JOIN fontes_oficiais fo ON fo.id = po.fonte_id
                    WHERE po.{cfg.drug_fk} = ?
                      AND (po.patologia_id = ? OR po.patologia_id IS NULL)
                    ORDER BY po.patologia_id DESC, po.populacao""",
                (aid, patologia_id),
            ).fetchall()]
            ints = [dict(r) for r in db.execute(
                f"""SELECT i.medicamento_interagente, i.classe_interagente,
                           i.mecanismo, i.gravidade, i.efeito_clinico, i.conduta,
                           fo.sigla AS fonte
                    FROM {cfg.interactions_table} i
                    LEFT JOIN fontes_oficiais fo ON fo.id = i.fonte_id
                    WHERE i.{cfg.drug_fk} = ?
                    ORDER BY CASE i.gravidade
                      WHEN 'contraindicada' THEN 1 WHEN 'grave' THEN 2
                      WHEN 'moderada' THEN 3 WHEN 'leve' THEN 4 END""",
                (aid,),
            ).fetchall()]
            return pos, ints

        # Cards sintéticos a partir da diretriz quando não há dados de eficácia
        synthetic = []
        if not meds and tratamento:
            drug_names = [n for n in (
                tratamento[cfg.treatment_principal],
                tratamento["alternativa_alergia"],
                tratamento["alternativa_resistencia"],
            ) if n][:3]
            ev = EVIDENCIA_SCORE.get(tratamento["nivel_evidencia"] or "D", 25)
            for nome in drug_names:
                first_word = nome.split()[0]
                drow = db.execute(
                    f"""SELECT a.id, a.nome_generico, a.nome_comercial,
                               a.via_administracao, a.disponivel_sus,
                               ca.nome AS classe
                        FROM {cfg.drug_table} a
                        LEFT JOIN {cfg.drug_class_table} ca ON ca.id = a.classe_id
                        WHERE LOWER(a.nome_generico) LIKE LOWER(?)
                        LIMIT 1""",
                    (first_word.lower() + "%",),
                ).fetchone()
                sus = 100 if (drow and drow["disponivel_sus"]) else 0
                aid = drow["id"] if drow else None
                pos_s, int_s = _pos_int_single(aid) if aid else ([], [])
                synthetic.append({
                    "nome_generico":      drow["nome_generico"] if drow else nome,
                    "nome_comercial":     drow["nome_comercial"] if drow else None,
                    "via":                drow["via_administracao"] if drow else None,
                    "disponivel_sus":     bool(drow["disponivel_sus"]) if drow else False,
                    "classe":             drow["classe"] if drow else None,
                    cfg.agent_out_key:    None,
                    "eficacia_pct":       None,
                    "linha_tratamento":   1,
                    "nivel_evidencia":    tratamento["nivel_evidencia"],
                    "resistencia_br_pct": None,
                    "consideracoes":      tratamento["regime_resumido"],
                    "fonte":              tratamento["fonte_sigla"],
                    "fonte_nome":         tratamento["fonte_nome"],
                    "fonte_ano":          None,
                    "is_fallback":        True,
                    "radar": {
                        "eficacia":       0,
                        "seguranca":      100,
                        "evidencia":      ev,
                        "primeira_linha": 100,
                        "acesso_sus":     sus,
                    },
                    "posologias":         pos_s,
                    "interacoes":         int_s,
                })

        # Posologias e interações em lote (elimina N+1: 2 queries em vez de 2×N)
        drug_ids = [r[cfg.drug_fk] for r in meds]
        posologias_by_id: defaultdict = defaultdict(list)
        interacoes_by_id: defaultdict = defaultdict(list)

        if drug_ids:
            ph = ",".join("?" * len(drug_ids))
            for row in db.execute(
                f"""SELECT po.{cfg.drug_fk}, po.populacao, po.dose_unitaria,
                           po.frequencia, po.via, po.duracao_min_dias,
                           po.duracao_max_dias, po.duracao_texto,
                           po.ajuste_renal, po.ajuste_hepatico, po.observacoes,
                           fo.sigla AS fonte
                    FROM {cfg.posology_table} po
                    LEFT JOIN fontes_oficiais fo ON fo.id = po.fonte_id
                    WHERE po.{cfg.drug_fk} IN ({ph})
                      AND (po.patologia_id = ? OR po.patologia_id IS NULL)
                    ORDER BY po.{cfg.drug_fk}, po.patologia_id DESC, po.populacao""",
                (*drug_ids, patologia_id),
            ).fetchall():
                d = dict(row)
                posologias_by_id[d.pop(cfg.drug_fk)].append(d)

            for row in db.execute(
                f"""SELECT i.{cfg.drug_fk}, i.medicamento_interagente,
                           i.classe_interagente, i.mecanismo, i.gravidade,
                           i.efeito_clinico, i.conduta, fo.sigla AS fonte
                    FROM {cfg.interactions_table} i
                    LEFT JOIN fontes_oficiais fo ON fo.id = i.fonte_id
                    WHERE i.{cfg.drug_fk} IN ({ph})
                    ORDER BY i.{cfg.drug_fk},
                      CASE i.gravidade
                        WHEN 'contraindicada' THEN 1
                        WHEN 'grave'          THEN 2
                        WHEN 'moderada'       THEN 3
                        WHEN 'leve'           THEN 4
                      END""",
                drug_ids,
            ).fetchall():
                d = dict(row)
                interacoes_by_id[d.pop(cfg.drug_fk)].append(d)

        def enrich(r: sqlite3.Row) -> dict:
            """Monta o card de um medicamento real, com o radar normalizado 0–100.

            ``resistencia_br_pct`` e ``eficacia_pct`` distinguem None (dado clínico
            desconhecido) de 0.0 (medido como zero) — usar ``or 0`` aqui misturaria
            os dois (ex.: resistência desconhecida viraria "segurança 100%"). O
            radar propaga None; o frontend (Chart.js) já trata null como "sem
            dado" (ponto pulado), sem renderizá-lo como zero.
            """
            ev  = EVIDENCIA_SCORE.get(r["nivel_evidencia"] or "D", 25)
            ln  = LINHA_SCORE.get(r["linha_tratamento"] or 3, 30)
            resistencia = r["resistencia_br_pct"]
            seg = None if resistencia is None else max(0.0, 100.0 - resistencia)
            sus = 100 if r["disponivel_sus"] else 0
            aid = r[cfg.drug_fk]
            return {
                "nome_generico":      r["nome_generico"],
                "nome_comercial":     r["nome_comercial"],
                "via":                r["via_administracao"],
                "disponivel_sus":     bool(r["disponivel_sus"]),
                "classe":             r["classe"],
                cfg.agent_out_key:    r[cfg.agent_out_key],
                "eficacia_pct":       r["eficacia_pct"],
                "linha_tratamento":   r["linha_tratamento"],
                "nivel_evidencia":    r["nivel_evidencia"],
                "resistencia_br_pct": r["resistencia_br_pct"],
                "consideracoes":      r["consideracoes"],
                "fonte":              r["fonte"],
                "fonte_nome":         r["fonte_nome"],
                "fonte_ano":          r["fonte_ano"],
                "radar": {
                    "eficacia":       None if r["eficacia_pct"] is None else round(r["eficacia_pct"], 1),
                    "seguranca":      None if seg is None else round(seg, 1),
                    "evidencia":      ev,
                    "primeira_linha": ln,
                    "acesso_sus":     sus,
                },
                "posologias": posologias_by_id[aid],
                "interacoes": interacoes_by_id[aid],
            }

        sintomas, criterios, escores = _fetch_clinical(db, patologia_id)

        result = {
            "dominio":                cfg.dominio,
            "patologia":              dict(pat),
            "agentes":                [dict(a) for a in agentes],
            "top3_medicamentos":      synthetic if synthetic else [enrich(r) for r in meds],
            "tratamento_padrao":      dict(tratamento) if tratamento else None,
            "sintomas":               sintomas,
            "criterios_diagnosticos": criterios,
            "escores_diagnosticos":   escores,
        }
        # Bacterianas mantêm a chave histórica "bacterias" além de "agentes"
        if cfg.extra_agent_key:
            result[cfg.extra_agent_key] = [dict(a) for a in agentes]

    _cache[cache_key] = result
    return result


# ── rotas finas (uma linha cada) ────────────────────────────────────────────

@api.get("/bacterias/categorias")
def bact_categorias():
    return _categorias(AGENT_DOMAINS["bacterias"])


@api.get("/bacterias/patologias")
def bact_patologias(categoria_id: int | None = None):
    return _patologias(AGENT_DOMAINS["bacterias"], categoria_id)


@api.get("/bacterias/patologia/{patologia_id}")
def bact_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["bacterias"], patologia_id)


@api.get("/virais/categorias")
def virais_categorias():
    return _categorias(AGENT_DOMAINS["virais"])


@api.get("/virais/patologias")
def virais_patologias(categoria_id: int | None = None):
    return _patologias(AGENT_DOMAINS["virais"], categoria_id)


@api.get("/virais/patologia/{patologia_id}")
def virais_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["virais"], patologia_id)


@api.get("/fungicos/categorias")
def fungicos_categorias():
    return _categorias(AGENT_DOMAINS["fungicos"])


@api.get("/fungicos/patologias")
def fungicos_patologias(categoria_id: int | None = None):
    return _patologias(AGENT_DOMAINS["fungicos"], categoria_id)


@api.get("/fungicos/patologia/{patologia_id}")
def fungicos_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["fungicos"], patologia_id)


@api.get("/parasitos/categorias")
def parasitos_categorias():
    return _categorias(AGENT_DOMAINS["parasitos"])


@api.get("/parasitos/patologias")
def parasitos_patologias(categoria_id: int | None = None):
    return _patologias(AGENT_DOMAINS["parasitos"], categoria_id)


@api.get("/parasitos/patologia/{patologia_id}")
def parasitos_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["parasitos"], patologia_id)


# ══════════════════════════════════════════════════════════════════════════
# PATOLOGIAS CRÔNICAS – endpoints
# ══════════════════════════════════════════════════════════════════════════

@api.get("/cronicas/categorias")
def cronicas_categorias():
    if "cronicas:categorias" not in _cache:
        with conn_bact() as db:
            rows = db.execute(
                "SELECT id, nome, sistema FROM categorias_patologias ORDER BY nome"
            ).fetchall()
        _cache["cronicas:categorias"] = [dict(r) for r in rows]
    return _cache["cronicas:categorias"]


@api.get("/cronicas/patologias")
def cronicas_patologias(categoria_id: int | None = None):
    # Mesma correção de _patologias: chave de cache fixa + filtro em memória, para
    # não permitir inflar o cache com categoria_id controlado pelo cliente.
    key = "cronicas:patologias"
    if key not in _cache:
        sql = """
            SELECT DISTINCT p.id, p.categoria_id, p.nome, p.cid10, p.prevalencia_br,
                   p.mortalidade_br, p.notificacao_compulsoria, p.tipo_notificacao,
                   c.nome AS categoria
            FROM patologias p
            JOIN categorias_patologias c ON c.id = p.categoria_id
            JOIN tratamento_padrao_ouro_cronico tpc ON tpc.patologia_id = p.id
            ORDER BY p.nome
        """
        with conn_bact() as db:
            rows = db.execute(sql).fetchall()
        _cache[key] = [dict(r) for r in rows]
    todas = _cache[key]
    filtradas = [p for p in todas if not categoria_id or p["categoria_id"] == categoria_id]
    return [{k: v for k, v in p.items() if k != "categoria_id"} for p in filtradas]


@api.get("/cronicas/patologia/{patologia_id}")
def cronicas_detalhe(patologia_id: int):
    """Detalhe de patologia crônica.

    Diferente dos domínios por agente: não há agente etiológico. Os
    medicamentos (até 3) saem da própria diretriz — principal, combinação e
    alternativa — e cada nome é resolvido na tabela ``medicamentos`` por busca
    em cascata (``_lookup_med``).

    Como nos domínios por agente, a resposta é memoizada em ``_cache`` (dados
    read-only) para não refazer as consultas a cada acesso à mesma patologia.
    """
    cache_key = f"cronicas:detalhe:{patologia_id}"
    if cache_key in _cache:
        return _cache[cache_key]

    # GRAU_SCORE espelha EVIDENCIA_SCORE de propósito: grau de recomendação e
    # nível de evidência são eixos distintos, ainda que a escala coincida aqui.
    GRAU_SCORE = {"A": 100, "B": 75, "C": 50, "D": 25}

    def _extract_first_drug(text: str | None) -> str | None:
        """Extrai o nome do fármaco de um texto que pode conter dose e combinações."""
        if not text:
            return None
        # Só o primeiro fármaco, antes de qualquer separador + / &
        part = re.split(r"\s*[+/&]\s*", text)[0].strip()
        # Remove a informação de dose ao final (dígito ou parêntese)
        name = re.split(r"\s+\d|\s+\(", part)[0].strip()
        return name or None

    def _lookup_med(db: sqlite3.Connection, nome_raw: str | None) -> sqlite3.Row | None:
        """Busca em cascata na tabela ``medicamentos``: exata → case-insensitive → prefixo."""
        if not nome_raw:
            return None
        for query, param in [
            ("WHERE m.nome_generico = ?", nome_raw),
            ("WHERE LOWER(m.nome_generico) = LOWER(?)", nome_raw),
            ("WHERE LOWER(m.nome_generico) LIKE LOWER(?) LIMIT 1",
             nome_raw.split()[0].lower() + "%"),
        ]:
            row = db.execute(
                f"""SELECT m.id, m.nome_generico, m.nome_comercial,
                           m.via_administracao, m.disponivel_sus,
                           cm.nome AS classe
                    FROM medicamentos m
                    LEFT JOIN classes_medicamentos cm ON cm.id = m.classe_id
                    {query}""",
                (param,),
            ).fetchone()
            if row:
                return row
        return None

    def _build_card(
        db: sqlite3.Connection,
        nome_raw: str | None,
        role_label: str,
        tratamento: sqlite3.Row,
        grau_score: dict[str, int],
        patologia_id: int,
        linha: int,
    ) -> dict | None:
        """Monta um card de medicamento para patologia crônica; None se ``nome_raw`` vazio."""
        nome_clean = _extract_first_drug(nome_raw)
        if not nome_clean:
            return None
        med_row = _lookup_med(db, nome_clean)

        radar = {
            "evidencia":    EVIDENCIA_SCORE.get(tratamento["nivel_evidencia"] or "D", 25),
            "recomendacao": grau_score.get(tratamento["grau_recomendacao"] or "D", 25),
            "acesso_sus":   100 if (med_row and med_row["disponivel_sus"]) else 0,
        }

        posologias, interacoes = [], []
        if med_row:
            mid = med_row["id"]
            posologias = [
                {k: v for k, v in dict(r).items() if k != "medicamento_id"}
                for r in db.execute(
                    """SELECT po.medicamento_id, po.populacao, po.dose_unitaria,
                              po.frequencia, po.via, po.duracao_texto,
                              po.ajuste_renal, po.ajuste_hepatico,
                              po.meta_terapeutica, po.observacoes,
                              fo.sigla AS fonte
                       FROM posologia_cronica po
                       LEFT JOIN fontes_oficiais fo ON fo.id = po.fonte_id
                       WHERE po.medicamento_id = ?
                         AND (po.patologia_id = ? OR po.patologia_id IS NULL)
                       ORDER BY po.patologia_id DESC, po.populacao""",
                    (mid, patologia_id),
                ).fetchall()
            ]
            interacoes = [
                {k: v for k, v in dict(r).items() if k != "medicamento_id"}
                for r in db.execute(
                    """SELECT i.medicamento_id, i.medicamento_interagente,
                              i.classe_interagente, i.mecanismo, i.gravidade,
                              i.efeito_clinico, i.conduta, fo.sigla AS fonte
                       FROM interacoes_medicamentos i
                       LEFT JOIN fontes_oficiais fo ON fo.id = i.fonte_id
                       WHERE i.medicamento_id = ?
                       ORDER BY CASE i.gravidade
                         WHEN 'contraindicada' THEN 1 WHEN 'grave' THEN 2
                         WHEN 'moderada' THEN 3 WHEN 'leve' THEN 4 END""",
                    (mid,),
                ).fetchall()
            ]

        # Sem posologia estruturada: usa o texto do regime para a aba não ficar vazia
        if not posologias and tratamento["regime_resumido"]:
            posologias = [{"regime_texto": tratamento["regime_resumido"]}]

        return {
            "nome_generico":      med_row["nome_generico"] if med_row else nome_clean,
            "nome_comercial":     med_row["nome_comercial"] if med_row else None,
            "via":                med_row["via_administracao"] if med_row else None,
            "disponivel_sus":     bool(med_row["disponivel_sus"]) if med_row else False,
            "classe":             med_row["classe"] if med_row else None,
            "agente":             None,
            "eficacia_pct":       None,
            "linha_tratamento":   linha,
            "nivel_evidencia":    tratamento["nivel_evidencia"],
            "resistencia_br_pct": None,
            "consideracoes":      tratamento["regime_resumido"] if linha == 1 else nome_raw,
            "role_label":         role_label,
            "fonte":              tratamento["fonte_sigla"],
            "fonte_nome":         tratamento["fonte_nome"],
            "fonte_ano":          None,
            "is_fallback":        med_row is None,
            "radar":              radar,
            "posologias":         posologias,
            "interacoes":         interacoes,
        }

    with conn_bact() as db:
        pat = _fetch_patologia(db, patologia_id)

        tratamento = db.execute(
            """SELECT t.medicamento_principal, t.combinacao,
                      t.regime_resumido, t.duracao_resumida, t.justificativa,
                      t.alternativa_alergia, t.alternativa_resistencia,
                      t.obs_especiais, t.grau_recomendacao, t.nivel_evidencia,
                      t.ano_diretriz,
                      fo.sigla AS fonte_sigla, fo.nome AS fonte_nome
               FROM tratamento_padrao_ouro_cronico t
               LEFT JOIN fontes_oficiais fo ON fo.id = t.fonte_id
               WHERE t.patologia_id = ?""",
            (patologia_id,),
        ).fetchone()

        top3_medicamentos = []
        if tratamento and tratamento["medicamento_principal"]:
            candidates = [
                (tratamento["medicamento_principal"], "Medicamento Principal",      1),
                (tratamento["combinacao"],            "Em Combinação",              2),
                (tratamento["alternativa_alergia"],   "Alternativa / 2ª Escolha",  3),
            ]
            for nome_raw, role_label, linha in candidates:
                card = _build_card(
                    db, nome_raw, role_label, tratamento, GRAU_SCORE, patologia_id, linha
                )
                if card:
                    top3_medicamentos.append(card)

        sintomas, criterios, escores = _fetch_clinical(db, patologia_id)

        result = {
            "dominio":                "cronico",
            "patologia":              dict(pat),
            "agentes":                [],
            "top3_medicamentos":      top3_medicamentos,
            "tratamento_padrao":      dict(tratamento) if tratamento else None,
            "sintomas":               sintomas,
            "criterios_diagnosticos": criterios,
            "escores_diagnosticos":   escores,
        }

    _cache[cache_key] = result
    return result


app.include_router(api)

# ── static (deve ser o último mount) ───────────────────────────────────────
# Catch-all de arquivos estáticos (patologias.html, bacterias.html, chart.umd.min.js).
# Precisa vir DEPOIS das rotas /api e da rota "/" para não capturá-las primeiro.
app.mount("/", StaticFiles(directory=str(STATIC), html=True), name="static")
