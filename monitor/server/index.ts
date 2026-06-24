import express from "express";
import cors from "cors";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";
import { scrapeAllArticles, scrapeJournal, JOURNAL_CONFIGS, type Journal } from "./scraper.js";
import { processArticles } from "./article-processor.js";

const __dirname = dirname(fileURLToPath(import.meta.url));
const isProd = process.env.NODE_ENV === "production";

const rawPort = process.env.PORT ? Number(process.env.PORT) : 3000;
const PORT = Number.isFinite(rawPort) && rawPort > 0 ? rawPort : 3000;

const app = express();

// CORS apenas em desenvolvimento — em produção o frontend é servido pelo Express
if (!isProd) {
  app.use(cors({ origin: "http://localhost:5173" }));
}

app.use(express.json());

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
    let articles;
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
    res.json({
      count: result.articles.length,
      articles: result.articles,
      failedDois: result.failedDois,
      scrapeErrors: result.scrapeErrors,
    });
  } catch (err) {
    const message = err instanceof Error ? err.message : "falha no processamento";
    console.error("[/api/process] erro:", err);
    const status = message.includes("ANTHROPIC_API_KEY") ? 503 : 500;
    res.status(status).json({ error: message });
  }
});

// ─── Produção: serve assets do Vite ──────────────────────────────────────────

if (isProd) {
  // __dirname em produção = dist/server/ → dois níveis acima = monitor/
  const clientDist = resolve(__dirname, "../../dist/client");
  app.use(express.static(clientDist));
  // Catch-all SPA: rotas não-API devolvem index.html
  app.use((_req, res) => res.sendFile(resolve(clientDist, "index.html")));
}

app.listen(PORT, () => {
  console.log(`[server] http://localhost:${PORT}`);
});
