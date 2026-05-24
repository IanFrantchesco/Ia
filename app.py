"""
Backend FastAPI — Brasil Político
Dashboard comparativo de presidentes (1930-2024)
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
import sqlite3
import os
from pathlib import Path

DB_PATH      = Path(__file__).parent / "output" / "brasil_economico.db"
DB_BACT_PATH = Path(__file__).parent / "database" / "patologias_bacterianas_br.sqlite"
STATIC       = Path(__file__).parent / "static"

app = FastAPI(title="Brasil Político + Patologias Bacterianas")

# ── helpers ────────────────────────────────────────────────────────────────

def conn():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c

def conn_bact():
    c = sqlite3.connect(DB_BACT_PATH)
    c.row_factory = sqlite3.Row
    return c

# ── endpoints ──────────────────────────────────────────────────────────────

@app.get("/api/presidentes")
def list_presidentes():
    with conn() as db:
        rows = db.execute("""
            SELECT DISTINCT presidente, partido, fase,
                   MIN(ano) as ano_inicio, MAX(ano) as ano_fim
            FROM indicadores_brasil
            GROUP BY presidente
            ORDER BY MIN(ano)
        """).fetchall()
    return [dict(r) for r in rows]


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


@app.post("/api/analise")
def gerar_analise(req: AnaliseRequest):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(
            503,
            detail="ANTHROPIC_API_KEY não configurada. "
                   "Defina a variável de ambiente para ativar a análise por IA."
        )

    import anthropic

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

EVIDENCIA_SCORE = {"A": 100, "B": 75, "C": 50, "D": 25}
LINHA_SCORE     = {1: 100, 2: 60, 3: 30}


@app.get("/api/bacterias/categorias")
def bact_categorias():
    with conn_bact() as db:
        rows = db.execute(
            "SELECT id, nome, sistema FROM categorias_patologias ORDER BY nome"
        ).fetchall()
    return [dict(r) for r in rows]


@app.get("/api/bacterias/patologias")
def bact_patologias(categoria_id: int = None):
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
    return [dict(r) for r in rows]


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

        # Top 3 antibióticos mais eficazes para esta patologia
        antibioticos = db.execute(
            """SELECT
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

        # Se não encontrou por patologia_id, busca pela bactéria principal
        if not antibioticos and bacterias:
            bact_principal = bacterias[0]["nome_cientifico"]
            bact_id_row = db.execute(
                "SELECT id FROM bacterias WHERE nome_cientifico = ?",
                (bact_principal,),
            ).fetchone()
            if bact_id_row:
                antibioticos = db.execute(
                    """SELECT
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

    def score_atb(r):
        ev  = EVIDENCIA_SCORE.get(r["nivel_evidencia"] or "D", 25)
        ln  = LINHA_SCORE.get(r["linha_tratamento"] or 3, 30)
        seg = max(0.0, 100.0 - (r["resistencia_br_pct"] or 0.0))
        sus = 100 if r["disponivel_sus"] else 0
        return {
            "nome_generico":    r["nome_generico"],
            "nome_comercial":   r["nome_comercial"],
            "via":              r["via_administracao"],
            "disponivel_sus":   bool(r["disponivel_sus"]),
            "classe":           r["classe"],
            "bacteria":         r["bacteria"],
            "eficacia_pct":     r["eficacia_pct"],
            "linha_tratamento": r["linha_tratamento"],
            "nivel_evidencia":  r["nivel_evidencia"],
            "resistencia_br_pct": r["resistencia_br_pct"],
            "consideracoes":    r["consideracoes"],
            "fonte":            r["fonte"],
            "fonte_nome":       r["fonte_nome"],
            "fonte_ano":        r["fonte_ano"],
            "radar": {
                "eficacia":   round(r["eficacia_pct"] or 0, 1),
                "seguranca":  round(seg, 1),
                "evidencia":  ev,
                "primeira_linha": ln,
                "acesso_sus": sus,
            },
        }

    return {
        "patologia": dict(pat),
        "bacterias": [dict(b) for b in bacterias],
        "top3_antibioticos": [score_atb(r) for r in antibioticos],
    }


# ── static (deve ser o último mount) ───────────────────────────────────────
app.mount("/", StaticFiles(directory=str(STATIC), html=True), name="static")
