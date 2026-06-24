import express from "express";
import cors from "cors";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const PORT = Number(process.env.PORT ?? 3000);
const isProd = process.env.NODE_ENV === "production";

const app = express();

app.use(cors({ origin: "http://localhost:5173", credentials: true }));
app.use(express.json());

// Health check — valida que o servidor está de pé
app.get("/api/health", (_req, res) => {
  res.json({ ok: true, ts: new Date().toISOString() });
});

// Em produção serve os assets do Vite build
if (isProd) {
  const clientDist = resolve(__dirname, "../../dist/client");
  app.use(express.static(clientDist));
  app.get("*", (_req, res) =>
    res.sendFile(resolve(clientDist, "index.html"))
  );
}

app.listen(PORT, () => {
  console.log(`[server] rodando em http://localhost:${PORT}`);
});
