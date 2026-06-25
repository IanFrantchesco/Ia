import { describe, it, expect } from "vitest";
import { generateWhatsappMessage, JOURNAL_LABELS } from "./whatsapp.js";
import type { ArticleMessage } from "./whatsapp.js";

// ─── Fixtures ─────────────────────────────────────────────────────────────────

const makeArticle = (n: number, journal: "JAMA" | "HR" | "JCE" | "CAH" = "JAMA"): ArticleMessage => ({
  doi: `10.1234/test.${n}`,
  titlePt: `Artigo ${n} Título`,
  summaryPt: `Resumo do artigo ${n}.`,
  link: `https://doi.org/10.1234/test.${n}`,
  pubDate: "2026-06-25",
  journal,
});

// Quinta-feira, 25 de junho de 2026
const FIXED_DATE = new Date("2026-06-25T12:00:00");

// ─── Testes ───────────────────────────────────────────────────────────────────

describe("generateWhatsappMessage", () => {
  it("retorna mensagem de 'nenhum artigo' para array vazio", () => {
    const msg = generateWhatsappMessage([], FIXED_DATE);
    expect(msg).toContain("*Olá, Doutor(a)!*");
    expect(msg).toContain("Nenhum artigo novo no período consultado.");
  });

  it("inclui a data de atualização formatada em PT-BR no rodapé", () => {
    const msg = generateWhatsappMessage([], FIXED_DATE);
    expect(msg).toMatch(/25/);
    expect(msg).toMatch(/junho/);
    expect(msg).toMatch(/2026/);
  });

  it("formata artigo único com título em negrito, data, resumo, DOI e link", () => {
    const msg = generateWhatsappMessage([makeArticle(1)], FIXED_DATE);
    expect(msg).toContain("*Artigo 1 Título*");
    expect(msg).toContain("📅");
    expect(msg).toContain("Resumo do artigo 1.");
    expect(msg).toContain("DOI: 10.1234/test.1");
    expect(msg).toContain("🔗 https://doi.org/10.1234/test.1");
  });

  it("exibe nome completo do periódico no cabeçalho da seção com emoji 📰", () => {
    const msg = generateWhatsappMessage([makeArticle(1, "HR")], FIXED_DATE);
    expect(msg).toContain("📰 *Heart Rhythm*");
  });

  it("agrupa e ordena seções em JAMA > HR > JCE > CAH independente da ordem de entrada", () => {
    const articles = [
      makeArticle(1, "CAH"),
      makeArticle(2, "JCE"),
      makeArticle(3, "JAMA"),
      makeArticle(4, "HR"),
    ];
    const msg = generateWhatsappMessage(articles, FIXED_DATE);
    const pos = (label: string) => msg.indexOf(label);
    expect(pos("JAMA Cardiology")).toBeLessThan(pos("Heart Rhythm"));
    expect(pos("Heart Rhythm")).toBeLessThan(pos("J. Cardiovasc."));
    expect(pos("J. Cardiovasc.")).toBeLessThan(pos("Circulation"));
  });

  it("numera artigos continuamente dentro da mesma seção", () => {
    const articles = [makeArticle(1), makeArticle(2), makeArticle(3)];
    const msg = generateWhatsappMessage(articles, FIXED_DATE);
    expect(msg).toContain("1. *Artigo 1 Título*");
    expect(msg).toContain("2. *Artigo 2 Título*");
    expect(msg).toContain("3. *Artigo 3 Título*");
  });

  it("numera artigos continuamente entre periódicos diferentes (sem reiniciar)", () => {
    const articles = [makeArticle(1, "JAMA"), makeArticle(2, "HR")];
    const msg = generateWhatsappMessage(articles, FIXED_DATE);
    expect(msg).toContain("1. *Artigo 1 Título*");
    expect(msg).toContain("2. *Artigo 2 Título*");
    // O contador não reinicia — deve haver apenas uma ocorrência de "1. "
    const matches = [...msg.matchAll(/^1\. /gm)];
    expect(matches).toHaveLength(1);
  });

  it("omite seções de periódicos sem artigos", () => {
    const msg = generateWhatsappMessage([makeArticle(1, "JAMA")], FIXED_DATE);
    expect(msg).not.toContain("Heart Rhythm");
    expect(msg).not.toContain("J. Cardiovasc.");
    expect(msg).not.toContain("Circulation");
  });

  it("usa 'title' como fallback quando titlePt está vazio", () => {
    const article: ArticleMessage = {
      doi: "10.1234/test.0",
      title: "English Title",
      titlePt: "",
      summaryPt: "Resumo.",
      link: "https://doi.org/10.1234/test.0",
      pubDate: "2026-06-25",
      journal: "JAMA",
    };
    const msg = generateWhatsappMessage([article], FIXED_DATE);
    expect(msg).toContain("*English Title*");
  });

  it("usa '(sem título)' quando title e titlePt estão vazios", () => {
    const article: ArticleMessage = {
      doi: "10.1234/test.0",
      titlePt: "",
      summaryPt: "Resumo.",
      link: "https://doi.org/10.1234/test.0",
      pubDate: "2026-06-25",
      journal: "JAMA",
    };
    const msg = generateWhatsappMessage([article], FIXED_DATE);
    expect(msg).toContain("*(sem título)*");
  });

  it("não termina com linha em branco", () => {
    const msg = generateWhatsappMessage([makeArticle(1)], FIXED_DATE);
    expect(msg.endsWith("\n")).toBe(false);
    expect(msg.endsWith(" ")).toBe(false);
  });

  it("múltiplos artigos do mesmo journal ficam em sequência na mesma seção", () => {
    const articles = [makeArticle(1, "JCE"), makeArticle(2, "JCE"), makeArticle(3, "JAMA")];
    const msg = generateWhatsappMessage(articles, FIXED_DATE);
    const jcePos = msg.indexOf("J. Cardiovasc.");
    const art1Pos = msg.indexOf("Artigo 1 Título");
    const art2Pos = msg.indexOf("Artigo 2 Título");
    expect(art1Pos).toBeGreaterThan(jcePos);
    expect(art2Pos).toBeGreaterThan(jcePos);
  });

  it("JOURNAL_LABELS cobre todos os 4 códigos de periódico", () => {
    expect(JOURNAL_LABELS["JAMA"]).toBe("JAMA Cardiology");
    expect(JOURNAL_LABELS["HR"]).toBe("Heart Rhythm");
    expect(JOURNAL_LABELS["JCE"]).toBe("J. Cardiovasc. Electrophysiol.");
    expect(JOURNAL_LABELS["CAH"]).toBe("Circulation");
  });
});
