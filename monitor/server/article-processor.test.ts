import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { processArticles } from "./article-processor.js";
import type { ScrapedArticle } from "./scraper.js";

// ─── Mock do SDK ──────────────────────────────────────────────────────────────

// vi.hoisted garante que mockCreate está disponível dentro do factory de vi.mock
const mockCreate = vi.hoisted(() => vi.fn());

vi.mock("@anthropic-ai/sdk", () => ({
  default: vi.fn().mockImplementation(() => ({
    messages: { create: mockCreate },
  })),
}));

// ─── Fixtures ─────────────────────────────────────────────────────────────────

const makeArticle = (n: number): ScrapedArticle => ({
  title: `Article ${n} Title`,
  link: `https://doi.org/10.1234/test.${n}`,
  pubDate: "2026-06-20",
  description: `Abstract for article ${n}. Contains medical content.`,
  doi: `10.1234/test.${n}`,
  journal: "JAMA",
});

const successResponse = (titlePt: string, summaryPt: string) => ({
  content: [
    {
      type: "tool_use",
      id: "tu_test",
      name: "translate_article",
      input: { titlePt, summaryPt },
    },
  ],
});

// ─── processArticles ──────────────────────────────────────────────────────────

describe("processArticles", () => {
  const originalEnv = process.env["ANTHROPIC_API_KEY"];

  beforeEach(() => {
    vi.clearAllMocks();
    process.env["ANTHROPIC_API_KEY"] = "sk-ant-test-key";
  });

  afterEach(() => {
    if (originalEnv === undefined) {
      delete process.env["ANTHROPIC_API_KEY"];
    } else {
      process.env["ANTHROPIC_API_KEY"] = originalEnv;
    }
  });

  it("retorna lista vazia sem chamar Claude para array vazio", async () => {
    const result = await processArticles([]);
    expect(result).toEqual({ articles: [], failedDois: [], scrapeErrors: [] });
    expect(mockCreate).not.toHaveBeenCalled();
  });

  it("lança erro quando ANTHROPIC_API_KEY não configurada", async () => {
    delete process.env["ANTHROPIC_API_KEY"];
    await expect(processArticles([makeArticle(1)])).rejects.toThrow(
      "ANTHROPIC_API_KEY não configurada"
    );
  });

  it("traduz artigo com sucesso e retorna campos titlePt e summaryPt", async () => {
    mockCreate.mockResolvedValueOnce(
      successResponse("Título em Português", "Resumo conciso do artigo.")
    );

    const result = await processArticles([makeArticle(1)]);

    expect(result.articles).toHaveLength(1);
    expect(result.articles[0]!.titlePt).toBe("Título em Português");
    expect(result.articles[0]!.summaryPt).toBe("Resumo conciso do artigo.");
    expect(result.failedDois).toHaveLength(0);
    expect(mockCreate).toHaveBeenCalledTimes(1);
  });

  it("preserva todos os campos originais do ScrapedArticle", async () => {
    const article = makeArticle(42);
    mockCreate.mockResolvedValueOnce(successResponse("Título PT", "Resumo PT."));

    const result = await processArticles([article]);
    const processed = result.articles[0]!;

    expect(processed.doi).toBe(article.doi);
    expect(processed.link).toBe(article.link);
    expect(processed.pubDate).toBe(article.pubDate);
    expect(processed.journal).toBe(article.journal);
    expect(processed.description).toBe(article.description);
  });

  it("propaga scrapeErrors recebidos sem modificação", async () => {
    const scrapeErrors = [{ journal: "HR" as const, message: "timeout" }];
    mockCreate.mockResolvedValueOnce(successResponse("Título PT", "Resumo."));

    const result = await processArticles([makeArticle(1)], scrapeErrors);
    expect(result.scrapeErrors).toEqual(scrapeErrors);
  });

  it("usa fallback em inglês quando Claude falha e registra DOI em failedDois", async () => {
    mockCreate.mockRejectedValueOnce(new Error("API rate limit"));

    const article = makeArticle(1);
    const result = await processArticles([article]);

    expect(result.articles).toHaveLength(1);
    // fallback: campos em inglês
    expect(result.articles[0]!.titlePt).toBe(article.title);
    expect(result.articles[0]!.summaryPt).toBe(article.description);
    expect(result.failedDois).toEqual([article.doi]);
  });

  it("processa artigos válidos mesmo quando um no batch falha", async () => {
    // 3 artigos: 1º falha, 2º e 3º succedem
    mockCreate
      .mockRejectedValueOnce(new Error("timeout"))
      .mockResolvedValueOnce(successResponse("Título 2 PT", "Resumo 2."))
      .mockResolvedValueOnce(successResponse("Título 3 PT", "Resumo 3."));

    const result = await processArticles([makeArticle(1), makeArticle(2), makeArticle(3)]);

    expect(result.articles).toHaveLength(3);
    expect(result.articles[0]!.titlePt).toBe("Article 1 Title"); // fallback
    expect(result.articles[1]!.titlePt).toBe("Título 2 PT");
    expect(result.articles[2]!.titlePt).toBe("Título 3 PT");
    expect(result.failedDois).toEqual(["10.1234/test.1"]);
  });

  it("divide em lotes de BATCH_SIZE=5 e chama Claude por artigo", async () => {
    // 7 artigos → lote1(5) + lote2(2)
    const articles = Array.from({ length: 7 }, (_, i) => makeArticle(i + 1));

    mockCreate.mockResolvedValue(successResponse("Título PT", "Resumo."));

    const result = await processArticles(articles);

    expect(mockCreate).toHaveBeenCalledTimes(7);
    expect(result.articles).toHaveLength(7);
    expect(result.failedDois).toHaveLength(0);
  });

  it("inclui tool_choice e model corretos na chamada ao Claude", async () => {
    mockCreate.mockResolvedValueOnce(successResponse("Título PT", "Resumo."));

    await processArticles([makeArticle(1)]);

    const callArgs = mockCreate.mock.calls[0]![0];
    expect(callArgs.tool_choice).toEqual({ type: "tool", name: "translate_article" });
    expect(callArgs.model).toBe("claude-haiku-4-5-20251001");
    expect(callArgs.tools[0].name).toBe("translate_article");
  });
});
