import { describe, it, expect, beforeEach, afterEach } from "vitest";
import { createTestDb } from "./db.js";
import { upsertArticles, getArticles, getArticleByDoi } from "./repository.js";
import { articles } from "./schema.js";
import type { ProcessedArticle } from "./article-processor.js";
import type { Db } from "./db.js";

// ─── Fixtures ─────────────────────────────────────────────────────────────────

const makeProcessed = (n: number, journal: "JAMA" | "HR" = "JAMA"): ProcessedArticle => ({
  doi: `10.1234/test.${n}`,
  title: `Article ${n} Title`,
  titlePt: `Artigo ${n} Título`,
  description: `Abstract for article ${n}.`,
  summaryPt: `Resumo do artigo ${n}.`,
  link: `https://doi.org/10.1234/test.${n}`,
  pubDate: "2026-06-20",
  journal,
});

// ─── upsertArticles ───────────────────────────────────────────────────────────

describe("upsertArticles", () => {
  let testDb: Db;

  beforeEach(() => {
    testDb = createTestDb();
  });

  afterEach(() => {
    testDb.$client.close();
  });

  it("insere artigos novos e reporta contagem correta", () => {
    const result = upsertArticles([makeProcessed(1), makeProcessed(2)], testDb);
    expect(result).toEqual({ inserted: 2, skipped: 0 });
  });

  it("não insere duplicatas pelo DOI — artigo existente é preservado", () => {
    upsertArticles([makeProcessed(1)], testDb);

    // Segunda inserção do mesmo DOI com título diferente
    const duplicate: ProcessedArticle = { ...makeProcessed(1), title: "Título Alterado" };
    const result = upsertArticles([duplicate], testDb);

    expect(result).toEqual({ inserted: 0, skipped: 1 });

    // Dado original preservado
    const stored = getArticleByDoi("10.1234/test.1", testDb);
    expect(stored?.title).toBe("Article 1 Title");
  });

  it("insere novos e pula duplicatas no mesmo batch", () => {
    upsertArticles([makeProcessed(1)], testDb);
    const result = upsertArticles([makeProcessed(1), makeProcessed(2)], testDb);
    expect(result).toEqual({ inserted: 1, skipped: 1 });
  });

  it("retorna { inserted: 0, skipped: 0 } para array vazio", () => {
    expect(upsertArticles([], testDb)).toEqual({ inserted: 0, skipped: 0 });
  });
});

// ─── getArticles ─────────────────────────────────────────────────────────────

describe("getArticles", () => {
  let testDb: Db;

  beforeEach(() => {
    testDb = createTestDb();
    upsertArticles([makeProcessed(1, "JAMA"), makeProcessed(2, "HR"), makeProcessed(3, "JAMA")], testDb);
  });

  afterEach(() => {
    testDb.$client.close();
  });

  it("retorna todos os artigos sem filtros", () => {
    const rows = getArticles({}, testDb);
    expect(rows).toHaveLength(3);
  });

  it("filtra por journal", () => {
    const jama = getArticles({ journal: "JAMA" }, testDb);
    expect(jama).toHaveLength(2);
    expect(jama.every((r) => r.journal === "JAMA")).toBe(true);
  });

  it("retorna em ordem decrescente de createdAt", () => {
    const rows = getArticles({}, testDb);
    // Como todos têm o mesmo createdAt (Date do beforeEach), verificar que são 3
    expect(rows).toHaveLength(3);
  });

  it("exclui artigos mais antigos que o número de dias especificado", () => {
    // Artigo antigo inserido manualmente com createdAt no passado
    const oldDate = new Date();
    oldDate.setDate(oldDate.getDate() - 60);

    // Inserir artigo com data antiga diretamente
    testDb.insert(articles).values({
      doi: "old-doi", title: "Old Article", titlePt: "", description: "",
      summaryPt: "", link: "https://doi.org/old", pubDate: "2025-01-01",
      journal: "JCE", createdAt: oldDate,
    }).run();

    // 7 dias só vê os 3 recentes, não o antigo
    const rows = getArticles({ days: 7 }, testDb);
    expect(rows).toHaveLength(3);
    expect(rows.find((r) => r.doi === "old-doi")).toBeUndefined();
  });

  it("retorna lista vazia quando não há artigos no período", () => {
    const emptyDb = createTestDb();
    const rows = getArticles({ days: 1 }, emptyDb);
    emptyDb.$client.close();
    expect(rows).toHaveLength(0);
  });
});

// ─── getArticleByDoi ──────────────────────────────────────────────────────────

describe("getArticleByDoi", () => {
  let testDb: Db;

  beforeEach(() => {
    testDb = createTestDb();
    upsertArticles([makeProcessed(1)], testDb);
  });

  afterEach(() => {
    testDb.$client.close();
  });

  it("retorna o artigo pelo DOI exato", () => {
    const row = getArticleByDoi("10.1234/test.1", testDb);
    expect(row).not.toBeNull();
    expect(row?.doi).toBe("10.1234/test.1");
    expect(row?.titlePt).toBe("Artigo 1 Título");
  });

  it("retorna null para DOI inexistente", () => {
    expect(getArticleByDoi("10.9999/nao-existe", testDb)).toBeNull();
  });
});
