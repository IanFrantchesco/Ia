import { JOURNAL_LABELS, JOURNALS } from "../shared/journals.js";
import type { Journal } from "../shared/journals.js";

export { JOURNAL_LABELS };

// ─── Tipos ───────────────────────────────────────────────────────────────────

/** Subconjunto mínimo necessário para formatar a mensagem — aceita ProcessedArticle ou ArticleRow. */
export interface ArticleMessage {
  doi: string;
  title?: string;
  titlePt: string;
  summaryPt: string;
  link: string;
  pubDate: string;
  journal: Journal;
}

// ─── Constantes ───────────────────────────────────────────────────────────────

const JOURNAL_ORDER = JOURNALS;

const DIVIDER = "━━━━━━━━━━━━━━━━━━━━";

const INSTAGRAM_LINK =
  "https://www.instagram.com/arritmia.update?igsh=bWJpa2JnbzN0c3Iy&utm_source=qr";

// ─── Helpers ──────────────────────────────────────────────────────────────────

function formatDate(date: Date): string {
  return date.toLocaleDateString("pt-BR", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

function formatPubDate(pubDate: string): string {
  const parts = pubDate.split("-");
  const year = Number(parts[0]);
  const month = Number(parts[1]);
  const day = Number(parts[2]);
  if (!year || !month || !day) return pubDate;
  // noon UTC evita off-by-one causado por diferenças de fuso
  const d = new Date(Date.UTC(year, month - 1, day, 12));
  return d.toLocaleDateString("pt-BR", {
    day: "numeric",
    month: "long",
    year: "numeric",
    timeZone: "UTC",
  });
}

// ─── Geração da mensagem ──────────────────────────────────────────────────────

/**
 * Gera mensagem formatada para WhatsApp com os artigos agrupados por periódico.
 * Usa markdown do WhatsApp: *negrito*, separadores ━ e emojis.
 * Numeração é contínua entre todos os periódicos.
 */
export function generateWhatsappMessage(
  articles: ArticleMessage[],
  date: Date = new Date()
): string {
  const lines: string[] = [
    "*Olá, Doutor(a)!*",
    "",
    "Seguem as atualizações dessa semana, selecionadas diretamente das edições mais recentes dos principais periódicos internacionais de cardiologia. Esperamos que sejam úteis para a sua prática clínica.",
    "",
    "*Arritmia Update*",
    INSTAGRAM_LINK,
  ];

  if (articles.length === 0) {
    lines.push("", "Nenhum artigo novo no período consultado.");
    lines.push("", DIVIDER);
    lines.push(`📆 Atualização: ${formatDate(date)}.`);
    return lines.join("\n");
  }

  // Agrupa preservando a ordem canônica; ignora journals sem artigos
  const byJournal = new Map<Journal, ArticleMessage[]>();
  for (const journal of JOURNAL_ORDER) {
    const group = articles.filter((a) => a.journal === journal);
    if (group.length > 0) byJournal.set(journal, group);
  }

  let counter = 1;

  for (const [journal, group] of byJournal) {
    lines.push("");
    lines.push(DIVIDER);
    lines.push(`📰 *${JOURNAL_LABELS[journal]}*`);
    lines.push(DIVIDER);

    for (const article of group) {
      const displayTitle = article.titlePt || article.title || "(sem título)";
      lines.push("");
      lines.push(`${counter}. *${displayTitle}*`);
      if (article.pubDate) lines.push(`📅 ${formatPubDate(article.pubDate)}`);
      lines.push(article.summaryPt);
      lines.push(`DOI: ${article.doi}`);
      lines.push(`🔗 ${article.link}`);
      counter++;
    }
  }

  lines.push("");
  lines.push(DIVIDER);
  lines.push(`📆 Atualização: ${formatDate(date)}.`);

  return lines.join("\n");
}
