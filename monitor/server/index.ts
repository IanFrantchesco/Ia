import express from "express";
import cors from "cors";
import { resolve, dirname } from "path";
import { existsSync } from "fs";
import { fileURLToPath } from "url";
import { scrapeAllArticles, scrapeJournal, JOURNAL_CONFIGS, type Journal, type ScrapedArticle } from "./scraper.js";
import { processArticles } from "./article-processor.js";
import { initDb } from "./db.js";
import { upsertArticles, getArticles } from "./repository.js";
import { generateWhatsappMessage } from "./whatsapp.js";

const __dirname = dirname(fileURLToPath(import.meta.url));
// __dirname em produção = dist/server/ → dois níveis acima = monitor/
// Serve o frontend quando os assets compilados existem (não depende de NODE_ENV,
// que no Railway faz o npm install pular as devDependencies necessárias ao build).
const clientDist = resolve(__dirname, "../../dist/client");
const serveStatic = existsSync(clientDist);

try {
  initDb();
} catch (err) {
  console.error("[db] falha ao aplicar migrações:", err);
  process.exit(1);
}

const rawPort = process.env.PORT ? Number(process.env.PORT) : 3000;
const PORT = Number.isFinite(rawPort) && rawPort > 0 ? rawPort : 3000;

const app = express();

// CORS apenas em desenvolvimento — em produção o frontend é servido pelo Express
if (!serveStatic) {
  app.use(cors({ origin: "http://localhost:5173" }));
}

app.use(express.json());

// ─── Helpers ──────────────────────────────────────────────────────────────────

function parseDays(raw: unknown, defaultDays: number): number {
  const n = Number(raw);
  return typeof raw === "string" && Number.isFinite(n) && n > 0 ? n : defaultDays;
}

// ─── Rotas ────────────────────────────────────────────────────────────────────

app.get("/api/health", (_req, res) => {
  res.json({ ok: true, ts: new Date().toISOString() });
});

const VALID_JOURNALS = new Set(Object.values(JOURNAL_CONFIGS).map((c) => c.journal));

/**
 * GET /api/scrape?journal=ALL|JAMA|HR|JCE|CAH
 * Busca artigos dos últimos 7 dias diretamente do CrossRef.
 * Sem cache, sem banco — resultado bruto para validação.
 */
app.get("/api/scrape", async (req, res) => {
  const raw = req.query["journal"];
  const journalParam = typeof raw === "string" ? raw.toUpperCase() : "ALL";

  try {
    if (journalParam === "ALL") {
      const result = await scrapeAllArticles();
      res.json({ count: result.articles.length, articles: result.articles, errors: result.errors });
      return;
    }

    if (!VALID_JOURNALS.has(journalParam as Journal)) {
      res.status(400).json({ error: `journal inválido: ${journalParam}` });
      return;
    }

    const articles = await scrapeJournal(journalParam as Journal);
    res.json({ count: articles.length, articles });
  } catch (err) {
    console.error("[/api/scrape] erro:", err);
    res.status(500).json({ error: "falha na busca" });
  }
});

/**
 * GET /api/process?journal=ALL|JAMA|HR|JCE|CAH
 * Busca artigos do CrossRef e traduz/resume com Claude em PT-BR.
 * Requer ANTHROPIC_API_KEY configurada.
 */
app.get("/api/process", async (req, res) => {
  const raw = req.query["journal"];
  const journalParam = typeof raw === "string" ? raw.toUpperCase() : "ALL";

  try {
    let articles: ScrapedArticle[];
    let scrapeErrors: { journal: Journal; message: string }[] = [];

    if (journalParam === "ALL") {
      const scraped = await scrapeAllArticles();
      articles = scraped.articles;
      scrapeErrors = scraped.errors;
    } else {
      if (!VALID_JOURNALS.has(journalParam as Journal)) {
        res.status(400).json({ error: `journal inválido: ${journalParam}` });
        return;
      }
      articles = await scrapeJournal(journalParam as Journal);
    }

    const result = await processArticles(articles, scrapeErrors);

    const { inserted, skipped } = upsertArticles(result.articles);
    console.log(`[/api/process] persistidos: ${inserted} novos, ${skipped} já existentes`);

    res.json({
      count: result.articles.length,
      articles: result.articles,
      failedDois: result.failedDois,
      scrapeErrors: result.scrapeErrors,
      db: { inserted, skipped },
    });
  } catch (err) {
    console.error("[/api/process] erro:", err);
    const message = err instanceof Error ? err.message : "";
    // Expõe apenas erro de configuração próprio — erros do SDK Anthropic são mascarados
    if (message.includes("ANTHROPIC_API_KEY")) {
      res.status(503).json({ error: message });
    } else {
      res.status(500).json({ error: "falha no processamento" });
    }
  }
});

/**
 * GET /api/articles?journal=ALL|JAMA|HR|JCE|CAH&days=30
 * Retorna artigos armazenados no banco de dados.
 */
app.get("/api/articles", (req, res) => {
  const rawJournal = req.query["journal"];
  const rawDays = req.query["days"];

  const journalParam = typeof rawJournal === "string" ? rawJournal.toUpperCase() : "ALL";
  const days = parseDays(rawDays, 30);

  if (journalParam !== "ALL" && !VALID_JOURNALS.has(journalParam as Journal)) {
    res.status(400).json({ error: `journal inválido: ${journalParam}` });
    return;
  }

  try {
    const rows = getArticles({
      journal: journalParam === "ALL" ? undefined : (journalParam as Journal),
      days,
    });
    res.json({ count: rows.length, articles: rows });
  } catch (err) {
    console.error("[/api/articles] erro:", err);
    res.status(500).json({ error: "falha ao consultar artigos" });
  }
});

/**
 * GET /api/whatsapp?days=7
 * Retorna mensagem formatada para WhatsApp com os artigos do banco dos últimos N dias.
 */
app.get("/api/whatsapp", (req, res) => {
  const days = parseDays(req.query["days"], 7);

  try {
    const now = new Date();
    const rows = getArticles({ days });
    const message = generateWhatsappMessage(rows, now);
    res.json({ count: rows.length, message });
  } catch (err) {
    console.error("[/api/whatsapp] erro:", err);
    res.status(500).json({ error: "falha ao gerar mensagem" });
  }
});

// ─── Produção: serve assets do Vite ──────────────────────────────────────────

if (serveStatic) {
  app.use(express.static(clientDist));
  // Catch-all SPA: rotas não-API devolvem index.html
  app.use((_req, res) => res.sendFile(resolve(clientDist, "index.html")));
}

app.listen(PORT, () => {
  console.log(`[server] http://localhost:${PORT}`);
});
