/**
 * Traduz títulos e resume abstracts de artigos cardiológicos usando Claude.
 * Processa em lotes paralelos com fallback gracioso por artigo.
 *
 * Modelo padrão: claude-haiku-4-5-20251001 (custo-eficiente para tradução em série).
 * Troque por claude-sonnet-4-6 se precisar de maior fidelidade em terminologia.
 */

import Anthropic from "@anthropic-ai/sdk";
import type { ScrapedArticle, Journal } from "./scraper.js";

// ─── Constantes ───────────────────────────────────────────────────────────────

const CLAUDE_MODEL = "claude-haiku-4-5-20251001";
const BATCH_SIZE = 5;
const BATCH_DELAY_MS = 1_000;

// ─── Tipos públicos ───────────────────────────────────────────────────────────

export interface ProcessedArticle extends ScrapedArticle {
  /** Título traduzido para português brasileiro */
  titlePt: string;
  /** Resumo do abstract em português brasileiro (≤ 3 frases) */
  summaryPt: string;
}

export interface ProcessResult {
  articles: ProcessedArticle[];
  /** DOIs de artigos que falharam na tradução (mantidos com conteúdo em inglês como fallback) */
  failedDois: string[];
  /** Periódicos que falharam na busca CrossRef (propagado do ScrapeResult) */
  scrapeErrors: { journal: Journal; message: string }[];
}

// ─── Tool definition ─────────────────────────────────────────────────────────

const TRANSLATE_TOOL: Anthropic.Messages.Tool = {
  name: "translate_article",
  description:
    "Traduz o título e resume o abstract de um artigo científico de cardiologia para português brasileiro.",
  input_schema: {
    type: "object",
    properties: {
      titlePt: {
        type: "string",
        description: "Título do artigo traduzido para português brasileiro",
      },
      summaryPt: {
        type: "string",
        description: "Resumo conciso do abstract em português brasileiro (máximo 3 frases)",
      },
    },
    required: ["titlePt", "summaryPt"],
  },
};

// ─── Core ────────────────────────────────────────────────────────────────────

const sleep = (ms: number) => new Promise<void>((r) => setTimeout(r, ms));

async function translateArticle(
  client: Anthropic,
  article: ScrapedArticle
): Promise<ProcessedArticle> {
  const userContent = [
    "Traduza o título e resuma o abstract abaixo para português brasileiro.",
    "O resumo deve ter no máximo 3 frases, direto e claro para cardiologistas.",
    "",
    `Título: ${article.title}`,
    `Abstract: ${article.description || "(sem abstract disponível)"}`,
  ].join("\n");

  const response = await client.messages.create({
    model: CLAUDE_MODEL,
    max_tokens: 512,
    tools: [TRANSLATE_TOOL],
    tool_choice: { type: "tool", name: "translate_article" },
    messages: [{ role: "user", content: userContent }],
  });

  const toolBlock = response.content.find((b) => b.type === "tool_use");
  if (!toolBlock || toolBlock.type !== "tool_use") {
    throw new Error(`resposta inesperada do Claude — DOI ${article.doi}`);
  }

  const { titlePt, summaryPt } = toolBlock.input as { titlePt: string; summaryPt: string };
  return { ...article, titlePt, summaryPt };
}

async function translateBatch(
  client: Anthropic,
  batch: ScrapedArticle[]
): Promise<{ results: ProcessedArticle[]; failedDois: string[] }> {
  const settled = await Promise.allSettled(batch.map((a) => translateArticle(client, a)));

  const results: ProcessedArticle[] = [];
  const failedDois: string[] = [];

  settled.forEach((outcome, i) => {
    const article = batch[i]!;
    if (outcome.status === "fulfilled") {
      results.push(outcome.value);
    } else {
      const msg =
        outcome.reason instanceof Error ? outcome.reason.message : String(outcome.reason);
      console.error(`[processor] tradução falhou — ${article.doi}: ${msg}`);
      // fallback: artigo mantido com conteúdo em inglês
      results.push({ ...article, titlePt: article.title, summaryPt: article.description });
      failedDois.push(article.doi);
    }
  });

  return { results, failedDois };
}

// ─── API pública ──────────────────────────────────────────────────────────────

export async function processArticles(
  articles: ScrapedArticle[],
  scrapeErrors: { journal: Journal; message: string }[] = []
): Promise<ProcessResult> {
  const apiKey = process.env["ANTHROPIC_API_KEY"];
  if (!apiKey) throw new Error("ANTHROPIC_API_KEY não configurada");

  if (articles.length === 0) {
    return { articles: [], failedDois: [], scrapeErrors };
  }

  const client = new Anthropic({ apiKey });

  console.log(`[processor] iniciando tradução — ${articles.length} artigos, modelo ${CLAUDE_MODEL}`);

  const allResults: ProcessedArticle[] = [];
  const allFailedDois: string[] = [];
  const totalBatches = Math.ceil(articles.length / BATCH_SIZE);

  for (let i = 0; i < articles.length; i += BATCH_SIZE) {
    if (i > 0) await sleep(BATCH_DELAY_MS);

    const batchNum = Math.floor(i / BATCH_SIZE) + 1;
    const batch = articles.slice(i, i + BATCH_SIZE);

    console.log(`[processor] lote ${batchNum}/${totalBatches}: ${batch.length} artigos…`);
    const { results, failedDois } = await translateBatch(client, batch);

    allResults.push(...results);
    allFailedDois.push(...failedDois);
  }

  console.log(
    `[processor] concluído: ${allResults.length} traduzidos, ${allFailedDois.length} com fallback`
  );

  return { articles: allResults, failedDois: allFailedDois, scrapeErrors };
}
