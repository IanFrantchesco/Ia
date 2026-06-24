import express from "express";
import cors from "cors";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

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

app.get("/api/health", (_req, res) => {
  res.json({ ok: true, ts: new Date().toISOString() });
});

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
