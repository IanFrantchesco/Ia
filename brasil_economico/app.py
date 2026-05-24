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

DB_PATH  = Path(__file__).parent / "output" / "brasil_economico.db"
STATIC   = Path(__file__).parent / "static"

app = FastAPI(title="Brasil Político")

# ── helpers ────────────────────────────────────────────────────────────────

def conn():
    c = sqlite3.connect(DB_PATH)
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


# ── static (deve ser o último mount) ───────────────────────────────────────
app.mount("/", StaticFiles(directory=str(STATIC), html=True), name="static")
