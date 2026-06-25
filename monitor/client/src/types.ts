export type Journal = "JAMA" | "HR" | "JCE" | "CAH";

export interface Article {
  doi: string;
  title: string;
  titlePt: string;
  description: string;
  summaryPt: string;
  link: string;
  pubDate: string;
  journal: Journal;
  createdAt: string;
}

export interface ArticlesResponse {
  count: number;
  articles: Article[];
}

export interface ProcessResponse {
  count: number;
  articles: Article[];
  failedDois: string[];
  scrapeErrors: Array<{ journal: Journal; message: string }>;
  db: { inserted: number; skipped: number };
}

export interface WhatsAppResponse {
  count: number;
  message: string;
}
