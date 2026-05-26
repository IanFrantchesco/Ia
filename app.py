"""
Backend FastAPI — Brasil Político
Dashboard comparativo de presidentes (1930-2024)
"""

import logging
import os
import sqlite3
from collections import defaultdict
from contextlib import contextmanager
from pathlib import Path
from typing import List

import anthropic
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, field_validator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
log = logging.getLogger(__name__)

DB_PATH      = Path(__file__).parent / "output" / "brasil_economico.db"
DB_BACT_PATH = Path(__file__).parent / "database" / "patologias_bacterianas_br.sqlite"
STATIC       = Path(__file__).parent / "static"

app = FastAPI(title="Brasil Político + Patologias Bacterianas")

_cache: dict = {}

EVIDENCIA_SCORE = {"A": 100, "B": 75, "C": 50, "D": 25}
LINHA_SCORE     = {1: 100, 2: 60, 3: 30}

CAMPOS_ANALISE = {
    "presidente", "ano_inicio", "ano_fim", "partido",
    "media_crescimento_pib", "media_pib_per_capita", "media_inflacao",
    "media_desemprego", "media_selic", "media_cambio", "media_divida_pib",
    "media_resultado_primario", "media_reservas", "media_exportacoes",
    "media_importacoes", "media_balanca_comercial", "media_ied",
    "media_fbcf", "media_gini", "media_idh", "media_pobreza",
    "media_esperanca_vida", "media_mortalidade", "media_salario_min",
}

# ── helpers ────────────────────────────────────────────────────────────────

@contextmanager
def conn():
    db = sqlite3.connect(DB_PATH, timeout=10)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA busy_timeout=5000")
    try:
        yield db
    finally:
        db.close()


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
    for path, name in [
        (DB_PATH,      "brasil_economico"),
        (DB_BACT_PATH, "patologias_bacterianas"),
    ]:
        if path.exists():
            log.info("DB ok: %s", path.name)
        else:
            log.error("DB não encontrado: %s", path)


# ── endpoints ──────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {
        "status": "ok",
        "dbs": {
            "brasil_economico":       DB_PATH.exists(),
            "patologias_bacterianas": DB_BACT_PATH.exists(),
        },
    }


@app.get("/api/presidentes")
def list_presidentes():
    if "presidentes" not in _cache:
        with conn() as db:
            rows = db.execute("""
                SELECT DISTINCT presidente, partido, fase,
                       MIN(ano) as ano_inicio, MAX(ano) as ano_fim
                FROM indicadores_brasil
                GROUP BY presidente
                ORDER BY MIN(ano)
            """).fetchall()
        _cache["presidentes"] = [dict(r) for r in rows]
    return _cache["presidentes"]


@app.get("/api/resumo/{presidente}")
def get_resumo(presidente: str):
    with conn() as db:
        row = db.execute("""
            SELECT
                presidente, partido, fase,
                MIN(ano) as ano_inicio, MAX(ano) as ano_fim,
                ROUND(AVG(crescimento_pib_real_pct),   2) as media_crescimento_pib,
                ROUND(AVG(pib_per_capita_usd),         0) as media_pib_per_capita,
                ROUND(AVG(inflacao_pct),               2) as media_inflacao,
                ROUND(AVG(taxa_desemprego_pct),        2) as media_desemprego,
                ROUND(AVG(selic_pct),                  2) as media_selic,
                ROUND(AVG(cambio_brl_usd),             4) as media_cambio,
                ROUND(AVG(divida_bruta_pib_pct),       2) as media_divida_pib,
                ROUND(AVG(resultado_primario_pib_pct), 2) as media_resultado_primario,
                ROUND(AVG(reservas_internacionais_bi_usd), 2) as media_reservas,
                ROUND(AVG(exportacoes_bi_usd),         2) as media_exportacoes,
                ROUND(AVG(importacoes_bi_usd),         2) as media_importacoes,
                ROUND(AVG(balanca_comercial_bi_usd),   2) as media_balanca_comercial,
                ROUND(AVG(ied_entrada_bi_usd),         2) as media_ied,
                ROUND(AVG(fbcf_pib_pct),               2) as media_fbcf,
                ROUND(AVG(coeficiente_gini),           4) as media_gini,
                ROUND(AVG(idh),                        4) as media_idh,
                ROUND(AVG(taxa_pobreza_extrema_pct),   2) as media_pobreza,
                ROUND(AVG(esperanca_vida_anos),        2) as media_esperanca_vida,
                ROUND(AVG(mortalidade_infantil_por_mil), 2) as media_mortalidade,
                ROUND(AVG(salario_minimo_real_brl),    0) as media_salario_min
            FROM indicadores_brasil
            WHERE presidente = ?
            GROUP BY presidente
        """, (presidente,)).fetchone()
    if not row:
        raise HTTPException(404, "Presidente não encontrado")
    return dict(row)


class AnaliseRequest(BaseModel):
    presidentes: List[dict]

    @field_validator("presidentes")
    @classmethod
    def valida_presidentes(cls, v):
        if not v:
            raise ValueError("Ao menos 1 presidente é obrigatório")
        if len(v) > 3:
            raise ValueError("Máximo de 3 presidentes por análise")
        for p in v:
            invalidos = set(p.keys()) - CAMPOS_ANALISE
            if invalidos:
                raise ValueError(f"Campos não permitidos: {invalidos}")
        return v


@app.post("/api/analise")
def gerar_analise(req: AnaliseRequest):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(
            503,
            detail="ANTHROPIC_API_KEY não configurada. "
                   "Defina a variável de ambiente para ativar a análise por IA."
        )

    linhas = []
    for p in req.presidentes:
        linhas.append(
            f"\n### {p.get('presidente')} ({p.get('ano_inicio')}–{p.get('ano_fim')}) | {p.get('partido')}"
        )
        campos = [
            ("Crescimento médio PIB real", "media_crescimento_pib", "%"),
            ("PIB per capita médio", "media_pib_per_capita", "USD"),
            ("Inflação média", "media_inflacao", "%"),
            ("Desemprego médio", "media_desemprego", "%"),
            ("SELIC média", "media_selic", "%"),
            ("Dívida bruta/PIB média", "media_divida_pib", "%"),
            ("Resultado primário/PIB médio", "media_resultado_primario", "%"),
            ("Reservas internacionais médias", "media_reservas", "bi USD"),
            ("Balança comercial média", "media_balanca_comercial", "bi USD"),
            ("IED médio", "media_ied", "bi USD"),
            ("FBCF/PIB médio", "media_fbcf", "%"),
            ("IDH médio", "media_idh", ""),
            ("Gini médio", "media_gini", ""),
            ("Pobreza extrema média", "media_pobreza", "%"),
            ("Esperança de vida média", "media_esperanca_vida", "anos"),
            ("Mortalidade infantil média", "media_mortalidade", "/mil"),
            ("Salário mínimo real médio", "media_salario_min", "R$"),
        ]
        for label, key, unit in campos:
            val = p.get(key)
            if val is not None:
                linhas.append(f"- {label}: {val} {unit}".strip())

    dados = "\n".join(linhas)
    prompt = f"""Você é um economista especialista em história econômica do Brasil.

Analise comparativamente os governos abaixo com base nos dados econômicos e sociais.
Seja objetivo, equilibrado e contextualizado historicamente.
Considere que comparações entre períodos pré e pós Plano Real (1994) requerem contexto histórico especial.

{dados}

Estruture sua resposta assim:

## Análise Individual dos Governos
Para cada governo: destaque 2-3 realizações e 1-2 desafios, contextualizados.

## Comparação Direta
Compare os governos nos 5 indicadores mais relevantes para o contexto histórico.

## Legado Econômico e Social
Síntese do legado de cada governo (3-4 linhas por governo).

Use markdown com **negrito** para destacar números importantes.
Seja baseado em dados, equilibrado politicamente e historicamente contextualizado.
Responda em português brasileiro."""

    client = anthropic.Anthropic(api_key=api_key)
    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system="Você é economista especialista em história econômica do Brasil. Responda sempre em português brasileiro.",
        messages=[{"role": "user", "content": prompt}],
    )
    return {"analise": msg.content[0].text}


# ══════════════════════════════════════════════════════════════════════════
# PATOLOGIAS BACTERIANAS – endpoints
# ══════════════════════════════════════════════════════════════════════════

@app.get("/api/bacterias/categorias")
def bact_categorias():
    if "categorias" not in _cache:
        with conn_bact() as db:
            rows = db.execute(
                "SELECT id, nome, sistema FROM categorias_patologias ORDER BY nome"
            ).fetchall()
        _cache["categorias"] = [dict(r) for r in rows]
    return _cache["categorias"]


@app.get("/api/bacterias/patologias")
def bact_patologias(categoria_id: int = None):
    key = f"patologias:{categoria_id}"
    if key not in _cache:
        sql = """
            SELECT p.id, p.nome, p.cid10, p.prevalencia_br, p.mortalidade_br,
                   p.notificacao_compulsoria, p.tipo_notificacao,
                   c.nome AS categoria
            FROM patologias p
            JOIN categorias_patologias c ON c.id = p.categoria_id
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


@app.get("/api/bacterias/patologia/{patologia_id}")
def bact_detalhe(patologia_id: int):
    with conn_bact() as db:
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

        bacterias = db.execute(
            """SELECT b.nome_cientifico, b.nome_comum, b.gram,
                      b.aerobiose, b.formato, b.resistencia_natural,
                      pb.papel, pb.frequencia_pct
               FROM patologia_bacteria pb
               JOIN bacterias b ON b.id = pb.bacteria_id
               WHERE pb.patologia_id = ?
               ORDER BY pb.papel, pb.frequencia_pct DESC""",
            (patologia_id,),
        ).fetchall()

        antibioticos = db.execute(
            """SELECT
                a.id AS antibiotico_id,
                a.nome_generico, a.nome_comercial, a.via_administracao,
                a.disponivel_sus,
                ca.nome AS classe,
                b.nome_cientifico AS bacteria,
                e.eficacia_pct, e.linha_tratamento, e.nivel_evidencia,
                e.resistencia_br_pct, e.consideracoes,
                fo.sigla AS fonte, fo.nome AS fonte_nome, fo.ano AS fonte_ano
               FROM eficacia_antibiotico e
               JOIN antibioticos a ON a.id = e.antibiotico_id
               JOIN classes_antibioticos ca ON ca.id = a.classe_id
               JOIN bacterias b ON b.id = e.bacteria_id
               LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id
               WHERE e.patologia_id = ?
               ORDER BY e.eficacia_pct DESC, e.linha_tratamento ASC
               LIMIT 3""",
            (patologia_id,),
        ).fetchall()

        if not antibioticos and bacterias:
            bact_principal = bacterias[0]["nome_cientifico"]
            bact_id_row = db.execute(
                "SELECT id FROM bacterias WHERE nome_cientifico = ?",
                (bact_principal,),
            ).fetchone()
            if bact_id_row:
                antibioticos = db.execute(
                    """SELECT
                        a.id AS antibiotico_id,
                        a.nome_generico, a.nome_comercial, a.via_administracao,
                        a.disponivel_sus,
                        ca.nome AS classe,
                        b.nome_cientifico AS bacteria,
                        e.eficacia_pct, e.linha_tratamento, e.nivel_evidencia,
                        e.resistencia_br_pct, e.consideracoes,
                        fo.sigla AS fonte, fo.nome AS fonte_nome, fo.ano AS fonte_ano
                       FROM eficacia_antibiotico e
                       JOIN antibioticos a ON a.id = e.antibiotico_id
                       JOIN classes_antibioticos ca ON ca.id = a.classe_id
                       JOIN bacterias b ON b.id = e.bacteria_id
                       LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id
                       WHERE e.bacteria_id = ? AND e.patologia_id IS NULL
                       ORDER BY e.eficacia_pct DESC, e.linha_tratamento ASC
                       LIMIT 3""",
                    (bact_id_row["id"],),
                ).fetchall()

        tratamento = db.execute(
            """SELECT t.antibiotico_principal, t.combinacao,
                      t.regime_resumido, t.duracao_resumida, t.justificativa,
                      t.alternativa_alergia, t.alternativa_resistencia,
                      t.obs_especiais, t.grau_recomendacao, t.nivel_evidencia,
                      t.ano_diretriz,
                      fo.sigla AS fonte_sigla, fo.nome AS fonte_nome
               FROM tratamento_padrao_ouro t
               LEFT JOIN fontes_oficiais fo ON fo.id = t.fonte_id
               WHERE t.patologia_id = ?""",
            (patologia_id,),
        ).fetchone()

        # Bulk-fetch posologias e interacoes (elimina N+1: 2 queries em vez de 2×N)
        atb_ids = [r["antibiotico_id"] for r in antibioticos]
        posologias_by_id: defaultdict = defaultdict(list)
        interacoes_by_id: defaultdict = defaultdict(list)

        if atb_ids:
            ph = ",".join("?" * len(atb_ids))
            for row in db.execute(
                f"""SELECT po.antibiotico_id, po.populacao, po.dose_unitaria,
                           po.frequencia, po.via, po.duracao_min_dias,
                           po.duracao_max_dias, po.duracao_texto,
                           po.ajuste_renal, po.ajuste_hepatico, po.observacoes,
                           fo.sigla AS fonte
                    FROM posologia po
                    LEFT JOIN fontes_oficiais fo ON fo.id = po.fonte_id
                    WHERE po.antibiotico_id IN ({ph})
                      AND (po.patologia_id = ? OR po.patologia_id IS NULL)
                    ORDER BY po.antibiotico_id, po.patologia_id DESC, po.populacao""",
                (*atb_ids, pat["id"]),
            ).fetchall():
                d = dict(row)
                posologias_by_id[d.pop("antibiotico_id")].append(d)

            for row in db.execute(
                f"""SELECT i.antibiotico_id, i.medicamento_interagente,
                           i.classe_interagente, i.mecanismo, i.gravidade,
                           i.efeito_clinico, i.conduta, fo.sigla AS fonte
                    FROM interacoes_medicamentosas i
                    LEFT JOIN fontes_oficiais fo ON fo.id = i.fonte_id
                    WHERE i.antibiotico_id IN ({ph})
                    ORDER BY i.antibiotico_id,
                      CASE i.gravidade
                        WHEN 'contraindicada' THEN 1
                        WHEN 'grave'          THEN 2
                        WHEN 'moderada'       THEN 3
                        WHEN 'leve'           THEN 4
                      END""",
                atb_ids,
            ).fetchall():
                d = dict(row)
                interacoes_by_id[d.pop("antibiotico_id")].append(d)

        def enrich_atb(r):
            ev  = EVIDENCIA_SCORE.get(r["nivel_evidencia"] or "D", 25)
            ln  = LINHA_SCORE.get(r["linha_tratamento"] or 3, 30)
            seg = max(0.0, 100.0 - (r["resistencia_br_pct"] or 0.0))
            sus = 100 if r["disponivel_sus"] else 0
            aid = r["antibiotico_id"]
            return {
                "nome_generico":      r["nome_generico"],
                "nome_comercial":     r["nome_comercial"],
                "via":                r["via_administracao"],
                "disponivel_sus":     bool(r["disponivel_sus"]),
                "classe":             r["classe"],
                "bacteria":           r["bacteria"],
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

        result = {
            "patologia":         dict(pat),
            "bacterias":         [dict(b) for b in bacterias],
            "top3_antibioticos": [enrich_atb(r) for r in antibioticos],
            "tratamento_padrao": dict(tratamento) if tratamento else None,
        }

    return result


# ══════════════════════════════════════════════════════════════════════════
# PATOLOGIAS VIRAIS – endpoints
# ══════════════════════════════════════════════════════════════════════════

@app.get("/api/virais/categorias")
def virais_categorias():
    if "virais_categorias" not in _cache:
        with conn_bact() as db:
            rows = db.execute(
                """SELECT DISTINCT c.id, c.nome, c.sistema
                   FROM categorias_patologias c
                   JOIN patologias p ON p.categoria_id = c.id
                   JOIN patologia_virus pv ON pv.patologia_id = p.id
                   ORDER BY c.nome"""
            ).fetchall()
        _cache["virais_categorias"] = [dict(r) for r in rows]
    return _cache["virais_categorias"]


@app.get("/api/virais/patologias")
def virais_patologias(categoria_id: int = None):
    key = f"virais_patologias:{categoria_id}"
    if key not in _cache:
        sql = """
            SELECT DISTINCT p.id, p.nome, p.cid10, p.prevalencia_br, p.mortalidade_br,
                   p.notificacao_compulsoria, p.tipo_notificacao,
                   c.nome AS categoria
            FROM patologias p
            JOIN categorias_patologias c ON c.id = p.categoria_id
            JOIN patologia_virus pv ON pv.patologia_id = p.id
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


@app.get("/api/virais/patologia/{patologia_id}")
def virais_detalhe(patologia_id: int):
    with conn_bact() as db:
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

        agentes = db.execute(
            """SELECT v.nome_cientifico, v.nome_comum, v.tipo_acido_nucleico,
                      v.envelope, v.transmissao_principal,
                      pv.papel, pv.frequencia_pct
               FROM patologia_virus pv
               JOIN virus v ON v.id = pv.virus_id
               WHERE pv.patologia_id = ?
               ORDER BY pv.papel, pv.frequencia_pct DESC""",
            (patologia_id,),
        ).fetchall()

        antivirais = db.execute(
            """SELECT a.id AS antiviral_id,
                      a.nome_generico, a.nome_comercial, a.via_administracao,
                      a.disponivel_sus,
                      ca.nome AS classe,
                      v.nome_cientifico AS agente,
                      e.eficacia_pct, e.linha_tratamento, e.nivel_evidencia,
                      e.resistencia_br_pct, e.consideracoes,
                      fo.sigla AS fonte, fo.nome AS fonte_nome, fo.ano AS fonte_ano
               FROM eficacia_antiviral e
               JOIN antivirais a ON a.id = e.antiviral_id
               JOIN classes_antivirais ca ON ca.id = a.classe_id
               JOIN virus v ON v.id = e.virus_id
               LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id
               WHERE e.patologia_id = ?
               ORDER BY e.eficacia_pct DESC, e.linha_tratamento ASC
               LIMIT 3""",
            (patologia_id,),
        ).fetchall()

        if not antivirais and agentes:
            virus_principal = agentes[0]["nome_cientifico"]
            virus_id_row = db.execute(
                "SELECT id FROM virus WHERE nome_cientifico = ?",
                (virus_principal,),
            ).fetchone()
            if virus_id_row:
                antivirais = db.execute(
                    """SELECT a.id AS antiviral_id,
                              a.nome_generico, a.nome_comercial, a.via_administracao,
                              a.disponivel_sus,
                              ca.nome AS classe,
                              v.nome_cientifico AS agente,
                              e.eficacia_pct, e.linha_tratamento, e.nivel_evidencia,
                              e.resistencia_br_pct, e.consideracoes,
                              fo.sigla AS fonte, fo.nome AS fonte_nome, fo.ano AS fonte_ano
                       FROM eficacia_antiviral e
                       JOIN antivirais a ON a.id = e.antiviral_id
                       JOIN classes_antivirais ca ON ca.id = a.classe_id
                       JOIN virus v ON v.id = e.virus_id
                       LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id
                       WHERE e.virus_id = ? AND e.patologia_id IS NULL
                       ORDER BY e.eficacia_pct DESC, e.linha_tratamento ASC
                       LIMIT 3""",
                    (virus_id_row["id"],),
                ).fetchall()

        tratamento = db.execute(
            """SELECT t.antiviral_principal, t.combinacao,
                      t.regime_resumido, t.duracao_resumida, t.justificativa,
                      t.alternativa_alergia, t.alternativa_resistencia,
                      t.obs_especiais, t.grau_recomendacao, t.nivel_evidencia,
                      t.ano_diretriz,
                      fo.sigla AS fonte_sigla, fo.nome AS fonte_nome
               FROM tratamento_padrao_ouro_viral t
               LEFT JOIN fontes_oficiais fo ON fo.id = t.fonte_id
               WHERE t.patologia_id = ?""",
            (patologia_id,),
        ).fetchone()

        av_ids = [r["antiviral_id"] for r in antivirais]
        posologias_by_id: defaultdict = defaultdict(list)
        interacoes_by_id: defaultdict = defaultdict(list)

        if av_ids:
            ph = ",".join("?" * len(av_ids))
            for row in db.execute(
                f"""SELECT po.antiviral_id, po.populacao, po.dose_unitaria,
                           po.frequencia, po.via, po.duracao_min_dias,
                           po.duracao_max_dias, po.duracao_texto,
                           po.ajuste_renal, po.ajuste_hepatico, po.observacoes,
                           fo.sigla AS fonte
                    FROM posologia_viral po
                    LEFT JOIN fontes_oficiais fo ON fo.id = po.fonte_id
                    WHERE po.antiviral_id IN ({ph})
                      AND (po.patologia_id = ? OR po.patologia_id IS NULL)
                    ORDER BY po.antiviral_id, po.patologia_id DESC, po.populacao""",
                (*av_ids, pat["id"]),
            ).fetchall():
                d = dict(row)
                posologias_by_id[d.pop("antiviral_id")].append(d)

            for row in db.execute(
                f"""SELECT i.antiviral_id, i.medicamento_interagente,
                           i.classe_interagente, i.mecanismo, i.gravidade,
                           i.efeito_clinico, i.conduta, fo.sigla AS fonte
                    FROM interacoes_antivirais i
                    LEFT JOIN fontes_oficiais fo ON fo.id = i.fonte_id
                    WHERE i.antiviral_id IN ({ph})
                    ORDER BY i.antiviral_id,
                      CASE i.gravidade
                        WHEN 'contraindicada' THEN 1
                        WHEN 'grave'          THEN 2
                        WHEN 'moderada'       THEN 3
                        WHEN 'leve'           THEN 4
                      END""",
                av_ids,
            ).fetchall():
                d = dict(row)
                interacoes_by_id[d.pop("antiviral_id")].append(d)

        def enrich_med_viral(r):
            ev  = EVIDENCIA_SCORE.get(r["nivel_evidencia"] or "D", 25)
            ln  = LINHA_SCORE.get(r["linha_tratamento"] or 3, 30)
            seg = max(0.0, 100.0 - (r["resistencia_br_pct"] or 0.0))
            sus = 100 if r["disponivel_sus"] else 0
            aid = r["antiviral_id"]
            return {
                "nome_generico":      r["nome_generico"],
                "nome_comercial":     r["nome_comercial"],
                "via":                r["via_administracao"],
                "disponivel_sus":     bool(r["disponivel_sus"]),
                "classe":             r["classe"],
                "agente":             r["agente"],
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

        result = {
            "dominio":           "viral",
            "patologia":         dict(pat),
            "agentes":           [dict(a) for a in agentes],
            "top3_medicamentos": [enrich_med_viral(r) for r in antivirais],
            "tratamento_padrao": dict(tratamento) if tratamento else None,
        }

    return result


# ══════════════════════════════════════════════════════════════════════════
# PATOLOGIAS FÚNGICAS – endpoints
# ══════════════════════════════════════════════════════════════════════════

@app.get("/api/fungicos/categorias")
def fungicos_categorias():
    if "fungicos_categorias" not in _cache:
        with conn_bact() as db:
            rows = db.execute(
                """SELECT DISTINCT c.id, c.nome, c.sistema
                   FROM categorias_patologias c
                   JOIN patologias p ON p.categoria_id = c.id
                   JOIN patologia_fungo pf ON pf.patologia_id = p.id
                   ORDER BY c.nome"""
            ).fetchall()
        _cache["fungicos_categorias"] = [dict(r) for r in rows]
    return _cache["fungicos_categorias"]


@app.get("/api/fungicos/patologias")
def fungicos_patologias(categoria_id: int = None):
    key = f"fungicos_patologias:{categoria_id}"
    if key not in _cache:
        sql = """
            SELECT DISTINCT p.id, p.nome, p.cid10, p.prevalencia_br, p.mortalidade_br,
                   p.notificacao_compulsoria, p.tipo_notificacao,
                   c.nome AS categoria
            FROM patologias p
            JOIN categorias_patologias c ON c.id = p.categoria_id
            JOIN patologia_fungo pf ON pf.patologia_id = p.id
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


@app.get("/api/fungicos/patologia/{patologia_id}")
def fungicos_detalhe(patologia_id: int):
    with conn_bact() as db:
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

        agentes = db.execute(
            """SELECT f.nome_cientifico, f.nome_comum, f.tipo,
                      f.transmissao_principal, f.reservatorio,
                      pf.papel, pf.frequencia_pct
               FROM patologia_fungo pf
               JOIN fungos f ON f.id = pf.fungo_id
               WHERE pf.patologia_id = ?
               ORDER BY pf.papel, pf.frequencia_pct DESC""",
            (patologia_id,),
        ).fetchall()

        antifungicos = db.execute(
            """SELECT a.id AS antifungico_id,
                      a.nome_generico, a.nome_comercial, a.via_administracao,
                      a.disponivel_sus,
                      ca.nome AS classe,
                      f.nome_cientifico AS agente,
                      e.eficacia_pct, e.linha_tratamento, e.nivel_evidencia,
                      e.resistencia_br_pct, e.consideracoes,
                      fo.sigla AS fonte, fo.nome AS fonte_nome, fo.ano AS fonte_ano
               FROM eficacia_antifungico e
               JOIN antifungicos a ON a.id = e.antifungico_id
               JOIN classes_antifungicos ca ON ca.id = a.classe_id
               JOIN fungos f ON f.id = e.fungo_id
               LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id
               WHERE e.patologia_id = ?
               ORDER BY e.eficacia_pct DESC, e.linha_tratamento ASC
               LIMIT 3""",
            (patologia_id,),
        ).fetchall()

        if not antifungicos and agentes:
            fungo_principal = agentes[0]["nome_cientifico"]
            fungo_id_row = db.execute(
                "SELECT id FROM fungos WHERE nome_cientifico = ?",
                (fungo_principal,),
            ).fetchone()
            if fungo_id_row:
                antifungicos = db.execute(
                    """SELECT a.id AS antifungico_id,
                              a.nome_generico, a.nome_comercial, a.via_administracao,
                              a.disponivel_sus,
                              ca.nome AS classe,
                              f.nome_cientifico AS agente,
                              e.eficacia_pct, e.linha_tratamento, e.nivel_evidencia,
                              e.resistencia_br_pct, e.consideracoes,
                              fo.sigla AS fonte, fo.nome AS fonte_nome, fo.ano AS fonte_ano
                       FROM eficacia_antifungico e
                       JOIN antifungicos a ON a.id = e.antifungico_id
                       JOIN classes_antifungicos ca ON ca.id = a.classe_id
                       JOIN fungos f ON f.id = e.fungo_id
                       LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id
                       WHERE e.fungo_id = ? AND e.patologia_id IS NULL
                       ORDER BY e.eficacia_pct DESC, e.linha_tratamento ASC
                       LIMIT 3""",
                    (fungo_id_row["id"],),
                ).fetchall()

        tratamento = db.execute(
            """SELECT t.antifungico_principal, t.combinacao,
                      t.regime_resumido, t.duracao_resumida, t.justificativa,
                      t.alternativa_alergia, t.alternativa_resistencia,
                      t.obs_especiais, t.grau_recomendacao, t.nivel_evidencia,
                      t.ano_diretriz,
                      fo.sigla AS fonte_sigla, fo.nome AS fonte_nome
               FROM tratamento_padrao_ouro_fungico t
               LEFT JOIN fontes_oficiais fo ON fo.id = t.fonte_id
               WHERE t.patologia_id = ?""",
            (patologia_id,),
        ).fetchone()

        af_ids = [r["antifungico_id"] for r in antifungicos]
        posologias_by_id: defaultdict = defaultdict(list)
        interacoes_by_id: defaultdict = defaultdict(list)

        if af_ids:
            ph = ",".join("?" * len(af_ids))
            for row in db.execute(
                f"""SELECT po.antifungico_id, po.populacao, po.dose_unitaria,
                           po.frequencia, po.via, po.duracao_min_dias,
                           po.duracao_max_dias, po.duracao_texto,
                           po.ajuste_renal, po.ajuste_hepatico, po.observacoes,
                           fo.sigla AS fonte
                    FROM posologia_fungica po
                    LEFT JOIN fontes_oficiais fo ON fo.id = po.fonte_id
                    WHERE po.antifungico_id IN ({ph})
                      AND (po.patologia_id = ? OR po.patologia_id IS NULL)
                    ORDER BY po.antifungico_id, po.patologia_id DESC, po.populacao""",
                (*af_ids, pat["id"]),
            ).fetchall():
                d = dict(row)
                posologias_by_id[d.pop("antifungico_id")].append(d)

            for row in db.execute(
                f"""SELECT i.antifungico_id, i.medicamento_interagente,
                           i.classe_interagente, i.mecanismo, i.gravidade,
                           i.efeito_clinico, i.conduta, fo.sigla AS fonte
                    FROM interacoes_antifungicos i
                    LEFT JOIN fontes_oficiais fo ON fo.id = i.fonte_id
                    WHERE i.antifungico_id IN ({ph})
                    ORDER BY i.antifungico_id,
                      CASE i.gravidade
                        WHEN 'contraindicada' THEN 1
                        WHEN 'grave'          THEN 2
                        WHEN 'moderada'       THEN 3
                        WHEN 'leve'           THEN 4
                      END""",
                af_ids,
            ).fetchall():
                d = dict(row)
                interacoes_by_id[d.pop("antifungico_id")].append(d)

        def enrich_med_fungico(r):
            ev  = EVIDENCIA_SCORE.get(r["nivel_evidencia"] or "D", 25)
            ln  = LINHA_SCORE.get(r["linha_tratamento"] or 3, 30)
            seg = max(0.0, 100.0 - (r["resistencia_br_pct"] or 0.0))
            sus = 100 if r["disponivel_sus"] else 0
            aid = r["antifungico_id"]
            return {
                "nome_generico":      r["nome_generico"],
                "nome_comercial":     r["nome_comercial"],
                "via":                r["via_administracao"],
                "disponivel_sus":     bool(r["disponivel_sus"]),
                "classe":             r["classe"],
                "agente":             r["agente"],
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

        result = {
            "dominio":           "fungico",
            "patologia":         dict(pat),
            "agentes":           [dict(a) for a in agentes],
            "top3_medicamentos": [enrich_med_fungico(r) for r in antifungicos],
            "tratamento_padrao": dict(tratamento) if tratamento else None,
        }

    return result


# ══════════════════════════════════════════════════════════════════════════
# PATOLOGIAS PARASITÁRIAS – endpoints
# ══════════════════════════════════════════════════════════════════════════

@app.get("/api/parasitos/categorias")
def parasitos_categorias():
    if "parasitos:categorias" not in _cache:
        with conn_bact() as db:
            rows = db.execute(
                "SELECT id, nome, sistema FROM categorias_patologias ORDER BY nome"
            ).fetchall()
        _cache["parasitos:categorias"] = [dict(r) for r in rows]
    return _cache["parasitos:categorias"]


@app.get("/api/parasitos/patologias")
def parasitos_patologias(categoria_id: int = None):
    key = f"parasitos:patologias:{categoria_id}"
    if key not in _cache:
        sql = """
            SELECT p.id, p.nome, p.cid10, p.prevalencia_br, p.mortalidade_br,
                   p.notificacao_compulsoria, p.tipo_notificacao,
                   c.nome AS categoria
            FROM patologias p
            JOIN categorias_patologias c ON c.id = p.categoria_id
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


@app.get("/api/parasitos/patologia/{patologia_id}")
def parasitos_detalhe(patologia_id: int):
    with conn_bact() as db:
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

        agentes = db.execute(
            """SELECT ps.nome_cientifico, ps.nome_comum, ps.tipo,
                      ps.ciclo_hospedeiro, ps.vetor,
                      pp.papel, pp.frequencia_pct
               FROM patologia_parasito pp
               JOIN parasitos ps ON ps.id = pp.parasito_id
               WHERE pp.patologia_id = ?
               ORDER BY pp.papel, pp.frequencia_pct DESC""",
            (patologia_id,),
        ).fetchall()

        antiparasitarios = db.execute(
            """SELECT a.id AS antiparasitario_id,
                      a.nome_generico, a.nome_comercial, a.via_administracao,
                      a.disponivel_sus,
                      ca.nome AS classe,
                      ps.nome_cientifico AS agente,
                      e.eficacia_pct, e.linha_tratamento, e.nivel_evidencia,
                      e.resistencia_br_pct, e.consideracoes,
                      fo.sigla AS fonte, fo.nome AS fonte_nome, fo.ano AS fonte_ano
               FROM eficacia_antiparasitario e
               JOIN antiparasitarios a ON a.id = e.antiparasitario_id
               JOIN classes_antiparasitarios ca ON ca.id = a.classe_id
               JOIN parasitos ps ON ps.id = e.parasito_id
               LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id
               WHERE e.patologia_id = ?
               ORDER BY e.eficacia_pct DESC, e.linha_tratamento ASC
               LIMIT 3""",
            (patologia_id,),
        ).fetchall()

        if not antiparasitarios and agentes:
            parasito_principal = agentes[0]["nome_cientifico"]
            parasito_id_row = db.execute(
                "SELECT id FROM parasitos WHERE nome_cientifico = ?",
                (parasito_principal,),
            ).fetchone()
            if parasito_id_row:
                antiparasitarios = db.execute(
                    """SELECT a.id AS antiparasitario_id,
                              a.nome_generico, a.nome_comercial, a.via_administracao,
                              a.disponivel_sus,
                              ca.nome AS classe,
                              ps.nome_cientifico AS agente,
                              e.eficacia_pct, e.linha_tratamento, e.nivel_evidencia,
                              e.resistencia_br_pct, e.consideracoes,
                              fo.sigla AS fonte, fo.nome AS fonte_nome, fo.ano AS fonte_ano
                       FROM eficacia_antiparasitario e
                       JOIN antiparasitarios a ON a.id = e.antiparasitario_id
                       JOIN classes_antiparasitarios ca ON ca.id = a.classe_id
                       JOIN parasitos ps ON ps.id = e.parasito_id
                       LEFT JOIN fontes_oficiais fo ON fo.id = e.fonte_id
                       WHERE e.parasito_id = ? AND e.patologia_id IS NULL
                       ORDER BY e.eficacia_pct DESC, e.linha_tratamento ASC
                       LIMIT 3""",
                    (parasito_id_row["id"],),
                ).fetchall()

        tratamento = db.execute(
            """SELECT t.antiparasitario_principal, t.combinacao,
                      t.regime_resumido, t.duracao_resumida, t.justificativa,
                      t.alternativa_alergia, t.alternativa_resistencia,
                      t.obs_especiais, t.grau_recomendacao, t.nivel_evidencia,
                      t.ano_diretriz,
                      fo.sigla AS fonte_sigla, fo.nome AS fonte_nome
               FROM tratamento_padrao_ouro_parasitario t
               LEFT JOIN fontes_oficiais fo ON fo.id = t.fonte_id
               WHERE t.patologia_id = ?""",
            (patologia_id,),
        ).fetchone()

        ap_ids = [r["antiparasitario_id"] for r in antiparasitarios]
        posologias_by_id: defaultdict = defaultdict(list)
        interacoes_by_id: defaultdict = defaultdict(list)

        if ap_ids:
            ph = ",".join("?" * len(ap_ids))
            for row in db.execute(
                f"""SELECT po.antiparasitario_id, po.populacao, po.dose_unitaria,
                           po.frequencia, po.via, po.duracao_min_dias,
                           po.duracao_max_dias, po.duracao_texto,
                           po.ajuste_renal, po.ajuste_hepatico, po.observacoes,
                           fo.sigla AS fonte
                    FROM posologia_parasitaria po
                    LEFT JOIN fontes_oficiais fo ON fo.id = po.fonte_id
                    WHERE po.antiparasitario_id IN ({ph})
                      AND (po.patologia_id = ? OR po.patologia_id IS NULL)
                    ORDER BY po.antiparasitario_id, po.patologia_id DESC, po.populacao""",
                (*ap_ids, pat["id"]),
            ).fetchall():
                d = dict(row)
                posologias_by_id[d.pop("antiparasitario_id")].append(d)

            for row in db.execute(
                f"""SELECT i.antiparasitario_id, i.medicamento_interagente,
                           i.classe_interagente, i.mecanismo, i.gravidade,
                           i.efeito_clinico, i.conduta, fo.sigla AS fonte
                    FROM interacoes_antiparasitarios i
                    LEFT JOIN fontes_oficiais fo ON fo.id = i.fonte_id
                    WHERE i.antiparasitario_id IN ({ph})
                    ORDER BY i.antiparasitario_id,
                      CASE i.gravidade
                        WHEN 'contraindicada' THEN 1
                        WHEN 'grave'          THEN 2
                        WHEN 'moderada'       THEN 3
                        WHEN 'leve'           THEN 4
                      END""",
                ap_ids,
            ).fetchall():
                d = dict(row)
                interacoes_by_id[d.pop("antiparasitario_id")].append(d)

        def enrich_ap(r):
            ev  = EVIDENCIA_SCORE.get(r["nivel_evidencia"] or "D", 25)
            ln  = LINHA_SCORE.get(r["linha_tratamento"] or 3, 30)
            seg = max(0.0, 100.0 - (r["resistencia_br_pct"] or 0.0))
            sus = 100 if r["disponivel_sus"] else 0
            aid = r["antiparasitario_id"]
            return {
                "nome_generico":      r["nome_generico"],
                "nome_comercial":     r["nome_comercial"],
                "via":                r["via_administracao"],
                "disponivel_sus":     bool(r["disponivel_sus"]),
                "classe":             r["classe"],
                "agente":             r["agente"],
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

        result = {
            "dominio":           "parasitario",
            "patologia":         dict(pat),
            "agentes":           [dict(a) for a in agentes],
            "top3_medicamentos": [enrich_ap(r) for r in antiparasitarios],
            "tratamento_padrao": dict(tratamento) if tratamento else None,
        }

    return result


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
            SELECT p.id, p.nome, p.cid10, p.prevalencia_br, p.mortalidade_br,
                   p.notificacao_compulsoria, p.tipo_notificacao,
                   c.nome AS categoria
            FROM patologias p
            JOIN categorias_patologias c ON c.id = p.categoria_id
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

    with conn_bact() as db:
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
            med_row = db.execute(
                """SELECT m.id, m.nome_generico, m.nome_comercial,
                          m.via_administracao, m.disponivel_sus,
                          cm.nome AS classe
                   FROM medicamentos m
                   LEFT JOIN classes_medicamentos cm ON cm.id = m.classe_id
                   WHERE m.nome_generico = ?""",
                (tratamento["medicamento_principal"],),
            ).fetchone()

            if med_row:
                med = dict(med_row)
                med_id = med["id"]

                posologias_rows = db.execute(
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
                    (med_id, patologia_id),
                ).fetchall()

                interacoes_rows = db.execute(
                    """SELECT i.medicamento_id, i.medicamento_interagente,
                              i.classe_interagente, i.mecanismo, i.gravidade,
                              i.efeito_clinico, i.conduta, fo.sigla AS fonte
                       FROM interacoes_medicamentos i
                       LEFT JOIN fontes_oficiais fo ON fo.id = i.fonte_id
                       WHERE i.medicamento_id = ?
                       ORDER BY CASE i.gravidade
                         WHEN 'contraindicada' THEN 1
                         WHEN 'grave'          THEN 2
                         WHEN 'moderada'       THEN 3
                         WHEN 'leve'           THEN 4
                       END""",
                    (med_id,),
                ).fetchall()

                posologias = [
                    {k: v for k, v in dict(r).items() if k != "medicamento_id"}
                    for r in posologias_rows
                ]
                interacoes = [
                    {k: v for k, v in dict(r).items() if k != "medicamento_id"}
                    for r in interacoes_rows
                ]

                radar = {
                    "evidencia":    EVIDENCIA_SCORE.get(tratamento["nivel_evidencia"] or "D", 25),
                    "recomendacao": GRAU_SCORE.get(tratamento["grau_recomendacao"] or "D", 25),
                    "acesso_sus":   100 if med["disponivel_sus"] else 0,
                }

                top3_medicamentos = [{
                    "nome_generico":      med["nome_generico"],
                    "nome_comercial":     med["nome_comercial"],
                    "via":                med["via_administracao"],
                    "disponivel_sus":     bool(med["disponivel_sus"]),
                    "classe":             med["classe"],
                    "agente":             None,
                    "eficacia_pct":       None,
                    "linha_tratamento":   1,
                    "nivel_evidencia":    tratamento["nivel_evidencia"],
                    "resistencia_br_pct": None,
                    "consideracoes":      None,
                    "fonte":              None,
                    "fonte_nome":         None,
                    "fonte_ano":          None,
                    "radar":              radar,
                    "posologias":         posologias,
                    "interacoes":         interacoes,
                }]

        result = {
            "dominio":           "cronico",
            "patologia":         dict(pat),
            "agentes":           [],
            "top3_medicamentos": top3_medicamentos,
            "tratamento_padrao": dict(tratamento) if tratamento else None,
        }

    return result


# ── static (deve ser o último mount) ───────────────────────────────────────
app.mount("/", StaticFiles(directory=str(STATIC), html=True), name="static")
