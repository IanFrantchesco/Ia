import express from "express";
import cors from "cors";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";
import { scrapeAllArticles, scrapeJournal, type Journal } from "./scraper.js";

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

const VALID_JOURNALS = new Set<Journal>(["JAMA", "HR", "JCE", "CAH"]);

/**
 * GET /api/scrape?journal=ALL|JAMA|HR|JCE|CAH
 * Busca artigos dos últimos 7 dias diretamente do CrossRef.
 * Sem cache, sem banco — resultado bruto para validação.
 */
app.get("/api/scrape", async (req, res) => {
  const journalParam = (req.query["journal"] as string | undefined)?.toUpperCase() ?? "ALL";

  try {
    const articles =
      journalParam === "ALL"
        ? await scrapeAllArticles()
        : VALID_JOURNALS.has(journalParam as Journal)
        ? await scrapeJournal(journalParam as Journal)
        : null;

    if (articles === null) {
      res.status(400).json({ error: `journal inválido: ${journalParam}` });
      return;
    }

    res.json({ count: articles.length, articles });
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
