"""
Backend FastAPI — Patologias
Painel clínico: bacterianas, virais, fúngicas, parasitárias e crônicas.
Critérios diagnósticos, tratamento padrão-ouro, posologia e interações.
"""

import logging
import re
import sqlite3
from collections import defaultdict
from contextlib import contextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
log = logging.getLogger(__name__)

DB_BACT_PATH = Path(__file__).parent / "database" / "patologias_bacterianas_br.sqlite"
STATIC       = Path(__file__).parent / "static"

app = FastAPI(title="Patologias — Painel Clínico")

_cache: dict = {}

EVIDENCIA_SCORE = {"A": 100, "B": 75, "C": 50, "D": 25}
LINHA_SCORE     = {1: 100, 2: 60, 3: 30}

# ── helpers ────────────────────────────────────────────────────────────────

@contextmanager
def conn_bact():
    db = sqlite3.connect(DB_BACT_PATH, timeout=10)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA busy_timeout=5000")
    try:
        yield db
    finally:
        db.close()


# ── startup ────────────────────────────────────────────────────────────────

@app.on_event("startup")
def startup_check():
    if DB_BACT_PATH.exists():
        log.info("DB ok: %s", DB_BACT_PATH.name)
    else:
        log.error("DB não encontrado: %s", DB_BACT_PATH)


# ── endpoints ──────────────────────────────────────────────────────────────

@app.get("/")
def root():
    return FileResponse(STATIC / "patologias.html")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "dbs": {
            "patologias_bacterianas": DB_BACT_PATH.exists(),
        },
    }


# ══════════════════════════════════════════════════════════════════════════
# PATOLOGIAS POR AGENTE (bacterianas · virais · fúngicas · parasitárias)
#
# Os quatro domínios compartilham exatamente a mesma lógica de detalhe,
# listagem e categorias — diferindo apenas nos nomes de tabelas/colunas.
# Toda a configuração que muda entre eles fica em AGENT_DOMAINS; a lógica
# vive uma única vez em _agent_detalhe / _patologias / _categorias.
# ══════════════════════════════════════════════════════════════════════════


class AgentDomain:
    """Configuração de um domínio de patologia baseada em agente etiológico.

    Todos os identificadores aqui são constantes confiáveis (nunca entrada
    do usuário), portanto sua interpolação em SQL via f-string é segura.
    """

    def __init__(self, **kw):
        self.__dict__.update(kw)


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

def _fetch_patologia(db, patologia_id):
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


def _fetch_clinical(db, patologia_id):
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

def _categorias(cfg):
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


def _patologias(cfg, categoria_id):
    key = f"{cfg.route}:patologias:{categoria_id}"
    if key not in _cache:
        sql = f"""
            SELECT DISTINCT p.id, p.nome, p.cid10, p.prevalencia_br, p.mortalidade_br,
                   p.notificacao_compulsoria, p.tipo_notificacao,
                   c.nome AS categoria
            FROM patologias p
            JOIN categorias_patologias c ON c.id = p.categoria_id
            JOIN {cfg.junction} j ON j.patologia_id = p.id
        """
        params = []
        if categoria_id:
            sql += " WHERE p.categoria_id = ?"
            params.append(categoria_id)
        sql += " ORDER BY p.nome"
        with conn_bact() as db:
            rows = db.execute(sql, params).fetchall()
        _cache[key] = [dict(r) for r in rows]
    return _cache[key]


# ── detalhe (genérico) ──────────────────────────────────────────────────────

def _agent_detalhe(cfg, patologia_id):
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

        def _pos_int_single(aid):
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

        def enrich(r):
            ev  = EVIDENCIA_SCORE.get(r["nivel_evidencia"] or "D", 25)
            ln  = LINHA_SCORE.get(r["linha_tratamento"] or 3, 30)
            seg = max(0.0, 100.0 - (r["resistencia_br_pct"] or 0.0))
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
                    "eficacia":       round(r["eficacia_pct"] or 0, 1),
                    "seguranca":      round(seg, 1),
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

    return result


# ── rotas finas (uma linha cada) ────────────────────────────────────────────

@app.get("/api/bacterias/categorias")
def bact_categorias():
    return _categorias(AGENT_DOMAINS["bacterias"])


@app.get("/api/bacterias/patologias")
def bact_patologias(categoria_id: int = None):
    return _patologias(AGENT_DOMAINS["bacterias"], categoria_id)


@app.get("/api/bacterias/patologia/{patologia_id}")
def bact_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["bacterias"], patologia_id)


@app.get("/api/virais/categorias")
def virais_categorias():
    return _categorias(AGENT_DOMAINS["virais"])


@app.get("/api/virais/patologias")
def virais_patologias(categoria_id: int = None):
    return _patologias(AGENT_DOMAINS["virais"], categoria_id)


@app.get("/api/virais/patologia/{patologia_id}")
def virais_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["virais"], patologia_id)


@app.get("/api/fungicos/categorias")
def fungicos_categorias():
    return _categorias(AGENT_DOMAINS["fungicos"])


@app.get("/api/fungicos/patologias")
def fungicos_patologias(categoria_id: int = None):
    return _patologias(AGENT_DOMAINS["fungicos"], categoria_id)


@app.get("/api/fungicos/patologia/{patologia_id}")
def fungicos_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["fungicos"], patologia_id)


@app.get("/api/parasitos/categorias")
def parasitos_categorias():
    return _categorias(AGENT_DOMAINS["parasitos"])


@app.get("/api/parasitos/patologias")
def parasitos_patologias(categoria_id: int = None):
    return _patologias(AGENT_DOMAINS["parasitos"], categoria_id)


@app.get("/api/parasitos/patologia/{patologia_id}")
def parasitos_detalhe(patologia_id: int):
    return _agent_detalhe(AGENT_DOMAINS["parasitos"], patologia_id)


# ══════════════════════════════════════════════════════════════════════════
# PATOLOGIAS CRÔNICAS – endpoints
# ══════════════════════════════════════════════════════════════════════════

@app.get("/api/cronicas/categorias")
def cronicas_categorias():
    if "cronicas:categorias" not in _cache:
        with conn_bact() as db:
            rows = db.execute(
                "SELECT id, nome, sistema FROM categorias_patologias ORDER BY nome"
            ).fetchall()
        _cache["cronicas:categorias"] = [dict(r) for r in rows]
    return _cache["cronicas:categorias"]


@app.get("/api/cronicas/patologias")
def cronicas_patologias(categoria_id: int = None):
    key = f"cronicas:patologias:{categoria_id}"
    if key not in _cache:
        sql = """
            SELECT DISTINCT p.id, p.nome, p.cid10, p.prevalencia_br, p.mortalidade_br,
                   p.notificacao_compulsoria, p.tipo_notificacao,
                   c.nome AS categoria
            FROM patologias p
            JOIN categorias_patologias c ON c.id = p.categoria_id
            JOIN tratamento_padrao_ouro_cronico tpc ON tpc.patologia_id = p.id
        """
        params = []
        if categoria_id:
            sql += " WHERE p.categoria_id = ?"
            params.append(categoria_id)
        sql += " ORDER BY p.nome"
        with conn_bact() as db:
            rows = db.execute(sql, params).fetchall()
        _cache[key] = [dict(r) for r in rows]
    return _cache[key]


@app.get("/api/cronicas/patologia/{patologia_id}")
def cronicas_detalhe(patologia_id: int):
    GRAU_SCORE = {"A": 100, "B": 75, "C": 50, "D": 25}

    def _extract_first_drug(text: str) -> str | None:
        """Return the drug name from a text that may include dose and combinations."""
        if not text:
            return None
        # Take only the first drug before any + / & separator
        part = re.split(r"\s*[+/&]\s*", text)[0].strip()
        # Strip trailing dose info (digit, parenthesis)
        name = re.split(r"\s+\d|\s+\(", part)[0].strip()
        return name or None

    def _lookup_med(db, nome_raw):
        """3-step cascade lookup in the medicamentos table."""
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

    def _build_card(db, nome_raw, role_label, tratamento, grau_score, patologia_id, linha):
        """Build one drug card for a chronic pathology; returns None if nome_raw is blank."""
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

        # When posologia is missing, fall back to the regime text so the tab isn't empty
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

    return result


# ── static (deve ser o último mount) ───────────────────────────────────────
app.mount("/", StaticFiles(directory=str(STATIC), html=True), name="static")
