import express from "express";
import cors from "cors";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const PORT = Number(process.env.PORT ?? 3000);
const isProd = process.env.NODE_ENV === "production";

const app = express();

// CORS apenas em desenvolvimento — em produção o frontend é servido pelo Express
if (!isProd) {
  app.use(cors({ origin: "http://localhost:5173" }));
}

app.use(express.json());

app.get("/api/health", (_req, res) => {
  res.json({ ok: true, ts: new Date().toISOString() });
});

if (isProd) {
  // Em produção: dist/ está 2 níveis acima de dist/server/
  const clientDist = resolve(__dirname, "../../dist/client");
  app.use(express.static(clientDist));
  // Catch-all para SPA — qualquer rota não-API devolve o index.html
  app.use((_req, res) => res.sendFile(resolve(clientDist, "index.html")));
}

app.listen(PORT, () => {
  console.log(`[server] http://localhost:${PORT}`);
});
