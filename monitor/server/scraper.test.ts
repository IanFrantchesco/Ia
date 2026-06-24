import { describe, it, expect } from "vitest";
import {
  isEditorialArticle,
  extractPublicationDate,
  getCreatedDate,
  cleanAbstract,
  buildArticleLink,
} from "./scraper.js";

// ─── isEditorialArticle ───────────────────────────────────────────────────────

describe("isEditorialArticle", () => {
  it("descarta artigos de revisão de pares", () => {
    expect(isEditorialArticle("JAMA Cardiology Peer Reviewers in 2025")).toBe(true);
    expect(isEditorialArticle("Peer Reviewer Acknowledgment")).toBe(true);
  });

  it("descarta correções e retrações", () => {
    expect(isEditorialArticle("Correction: Original Article Title")).toBe(true);
    expect(isEditorialArticle("Retraction Notice")).toBe(true);
    expect(isEditorialArticle("Erratum for Article X")).toBe(true);
    expect(isEditorialArticle("Corrigendum")).toBe(true);
    expect(isEditorialArticle("Addendum to Previous Study")).toBe(true);
  });

  it("descarta conteúdo editorial/administrativo", () => {
    expect(isEditorialArticle("Table of Contents")).toBe(true);
    expect(isEditorialArticle("Table Of Content")).toBe(true);
    expect(isEditorialArticle("Cover Image")).toBe(true);
    expect(isEditorialArticle("Issue Information")).toBe(true);
    expect(isEditorialArticle("Masthead")).toBe(true);
    expect(isEditorialArticle("Graphical Abstract")).toBe(true);
    expect(isEditorialArticle("In Memoriam")).toBe(true);
    expect(isEditorialArticle("Editorial Board")).toBe(true);
    expect(isEditorialArticle("Acknowledgements")).toBe(true);
    expect(isEditorialArticle("Editor's Note on Recent Changes")).toBe(true);
  });

  it("mantém artigos científicos reais", () => {
    expect(isEditorialArticle("Catheter Ablation for Atrial Fibrillation in Adults")).toBe(false);
    expect(isEditorialArticle("Risk Factors for Ventricular Fibrillation")).toBe(false);
    expect(isEditorialArticle("How Many CPVT Patients Need an ICD?")).toBe(false);
    expect(isEditorialArticle("Evidence-Based Imaging Pathway for AF")).toBe(false);
    expect(isEditorialArticle("QT Interval Prolongation in Athletes")).toBe(false);
  });

  it("trata capitalização mista", () => {
    expect(isEditorialArticle("CORRECTION: Some Article")).toBe(true);
    expect(isEditorialArticle("peer REVIEWERS 2025")).toBe(true);
  });
});

// ─── extractPublicationDate ───────────────────────────────────────────────────

describe("extractPublicationDate", () => {
  it("retorna YYYY-MM-DD quando dia disponível em published-online", () => {
    const item = { "published-online": { "date-parts": [[2026, 5, 17] as [number, number, number]] } };
    expect(extractPublicationDate(item)).toBe("2026-05-17");
  });

  it("retorna YYYY-MM quando apenas mês disponível", () => {
    const item = { published: { "date-parts": [[2026, 5] as [number, number]] } };
    expect(extractPublicationDate(item)).toBe("2026-05");
  });

  it("prioriza published-online sobre published", () => {
    const item = {
      "published-online": { "date-parts": [[2026, 6, 1] as [number, number, number]] },
      published: { "date-parts": [[2026, 5, 1] as [number, number, number]] },
    };
    expect(extractPublicationDate(item)).toBe("2026-06-01");
  });

  it("faz fallback para created quando outros campos ausentes", () => {
    const item = { created: { "date-parts": [[2026, 4, 10] as [number, number, number]] } };
    expect(extractPublicationDate(item)).toBe("2026-04-10");
  });

  it("pad com zero em mês e dia de um dígito", () => {
    const item = { "published-online": { "date-parts": [[2026, 1, 9] as [number, number, number]] } };
    expect(extractPublicationDate(item)).toBe("2026-01-09");
  });
});

// ─── getCreatedDate ───────────────────────────────────────────────────────────

describe("getCreatedDate", () => {
  it("extrai data do campo created", () => {
    const item = { created: { "date-parts": [[2026, 5, 13] as [number, number, number]] } };
    const date = getCreatedDate(item);
    expect(date).not.toBeNull();
    expect(date!.getFullYear()).toBe(2026);
    expect(date!.getMonth()).toBe(4); // 0-indexed
    expect(date!.getDate()).toBe(13);
  });

  it("retorna null quando created ausente", () => {
    expect(getCreatedDate({})).toBeNull();
  });

  it("retorna null quando date-parts malformado", () => {
    // Apenas year, sem month — campo insuficiente
    const item = { created: { "date-parts": [[2026] as [number]] } };
    expect(getCreatedDate(item)).toBeNull();
  });

  it("usa dia 1 quando dia ausente", () => {
    const item = { created: { "date-parts": [[2026, 5] as [number, number]] } };
    const date = getCreatedDate(item);
    expect(date).not.toBeNull();
    expect(date!.getDate()).toBe(1);
  });

  it("filtra artigo antigo (created > 60 dias) corretamente", () => {
    const cutoff = new Date();
    cutoff.setDate(cutoff.getDate() - 60);

    const oldDate = new Date();
    oldDate.setDate(oldDate.getDate() - 90);
    const oldItem = {
      created: {
        "date-parts": [[oldDate.getFullYear(), oldDate.getMonth() + 1, oldDate.getDate()] as [number, number, number]],
      },
    };
    expect(getCreatedDate(oldItem)! < cutoff).toBe(true);

    const recentDate = new Date();
    recentDate.setDate(recentDate.getDate() - 10);
    const recentItem = {
      created: {
        "date-parts": [[recentDate.getFullYear(), recentDate.getMonth() + 1, recentDate.getDate()] as [number, number, number]],
      },
    };
    expect(getCreatedDate(recentItem)! < cutoff).toBe(false);
  });
});

// ─── cleanAbstract ────────────────────────────────────────────────────────────

describe("cleanAbstract", () => {
  it("remove tags JATS XML", () => {
    const raw = "<jats:p>This is a <jats:italic>test</jats:italic> abstract.</jats:p>";
    expect(cleanAbstract(raw)).toBe("This is a test abstract.");
  });

  it("remove entidades HTML comuns", () => {
    // &amp; vira espaço; o texto entre &lt;...&gt; é preservado pois não é tag real
    expect(cleanAbstract("Heart &amp; Vessels")).toBe("Heart Vessels");
    expect(cleanAbstract("Study A &amp; Study B")).toBe("Study A Study B");
  });

  it("normaliza múltiplos espaços", () => {
    const raw = "<p>Text   with    spaces</p>";
    expect(cleanAbstract(raw)).toBe("Text with spaces");
  });

  it("retorna string vazia para entrada ausente", () => {
    expect(cleanAbstract(undefined)).toBe("");
    expect(cleanAbstract("")).toBe("");
  });

  it("mantém texto limpo sem modificação", () => {
    const clean = "Normal abstract text without any tags.";
    expect(cleanAbstract(clean)).toBe(clean);
  });
});

// ─── buildArticleLink ─────────────────────────────────────────────────────────

describe("buildArticleLink", () => {
  it("usa doi.org para JAMA", () => {
    expect(buildArticleLink("JAMA", "10.1001/jamacardio.2026.1234")).toBe(
      "https://doi.org/10.1001/jamacardio.2026.1234"
    );
  });

  it("usa doi.org para HR", () => {
    expect(buildArticleLink("HR", "10.1016/j.hrthm.2026.01.001")).toBe(
      "https://doi.org/10.1016/j.hrthm.2026.01.001"
    );
  });

  it("usa doi.org para JCE", () => {
    expect(buildArticleLink("JCE", "10.1111/jce.15000")).toBe(
      "https://doi.org/10.1111/jce.15000"
    );
  });

  it("usa PubMed para CAH (Circulation — AHA tem Cloudflare)", () => {
    const doi = "10.1161/CIRCULATIONAHA.126.123456";
    expect(buildArticleLink("CAH", doi)).toBe(
      `https://pubmed.ncbi.nlm.nih.gov/?term=${encodeURIComponent(doi)}`
    );
  });
});
