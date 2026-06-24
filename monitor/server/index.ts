import express from "express";
import cors from "cors";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";
import { scrapeAllArticles, scrapeJournal, JOURNAL_CONFIGS, type Journal, type ScrapeResult } from "./scraper.js";

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
      const result: ScrapeResult = await scrapeAllArticles();
      res.json({ count: result.articles.length, articles: result.articles, errors: result.errors });
      return;
    }

    if (!VALID_JOURNALS.has(journalParam as Journal)) {
      res.status(400).json({ error: `journal inválido: ${journalParam}` });
      return;
    }

    const articles = await scrapeJournal(journalParam as Journal);
    res.json({ count: articles.length, articles, errors: [] });
  } catch (err) {
    console.error("[/api/scrape] erro:", err);
    res.status(500).json({ error: "falha na busca" });
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
