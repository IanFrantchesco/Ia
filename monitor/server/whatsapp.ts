import { JOURNAL_LABELS, JOURNALS } from "../shared/journals.js";
import type { Journal } from "../shared/journals.js";

export { JOURNAL_LABELS };

// ─── Tipos ───────────────────────────────────────────────────────────────────

/** Subconjunto mínimo necessário para formatar a mensagem — aceita ProcessedArticle ou ArticleRow. */
export interface ArticleMessage {
  title?: string;
  titlePt: string;
  summaryPt: string;
  link: string;
  journal: Journal;
}

// ─── Constantes ───────────────────────────────────────────────────────────────

/** Ordem canônica dos periódicos — importada de shared para garantia de unicidade. */
const JOURNAL_ORDER = JOURNALS;

// ─── Helpers ──────────────────────────────────────────────────────────────────

function formatDate(date: Date): string {
  return date.toLocaleDateString("pt-BR", {
    weekday: "short",
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}

// ─── Geração da mensagem ──────────────────────────────────────────────────────

/**
 * Gera mensagem formatada para WhatsApp com os artigos agrupados por periódico.
 * Usa markdown do WhatsApp: *negrito* e numeração por seção.
 */
export function generateWhatsappMessage(
  articles: ArticleMessage[],
  date: Date = new Date()
): string {
  const header = `*CardioNews — ${formatDate(date)}*`;

  if (articles.length === 0) {
    return `${header}\n\nNenhum artigo novo no período consultado.`;
  }

  // Agrupa preservando a ordem canônica; ignora journals sem artigos
  const byJournal = new Map<Journal, ArticleMessage[]>();
  for (const journal of JOURNAL_ORDER) {
    const group = articles.filter((a) => a.journal === journal);
    if (group.length > 0) byJournal.set(journal, group);
  }

  const sections: string[] = [header, ""];

  for (const [journal, group] of byJournal) {
    const noun = group.length === 1 ? "artigo" : "artigos";
    sections.push(`*${JOURNAL_LABELS[journal]}* (${group.length} ${noun})`);
    sections.push("");

    group.forEach((article, i) => {
      const displayTitle = article.titlePt || article.title || "(sem título)";
      sections.push(`${i + 1}. *${displayTitle}*`);
      sections.push(article.summaryPt);
      sections.push(article.link);
      if (i < group.length - 1) sections.push("");
    });

    sections.push("");
  }

  // Remove linha em branco final
  while (sections.length > 0 && sections[sections.length - 1] === "") {
    sections.pop();
  }

  return sections.join("\n");
}
