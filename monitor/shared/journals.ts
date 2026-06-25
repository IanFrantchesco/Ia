export type Journal = "JAMA" | "HR" | "JCE" | "CAH";

/** Rótulos canônicos dos periódicos — única fonte de verdade para server e client. */
export const JOURNAL_LABELS: Record<Journal, string> = {
  JAMA: "JAMA Cardiology",
  HR:   "Heart Rhythm",
  JCE:  "J. Cardiovasc. Electrophysiol.",
  CAH:  "Circulation",
};

/** Ordem canônica dos periódicos nas mensagens e na UI. */
export const JOURNALS: Journal[] = ["JAMA", "HR", "JCE", "CAH"];
