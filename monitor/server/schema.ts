import { sqliteTable, text, integer, index } from "drizzle-orm/sqlite-core";
import type { Journal } from "../shared/journals.js";

export const articles = sqliteTable(
  "articles",
  {
    doi: text("doi").primaryKey(),
    title: text("title").notNull(),
    titlePt: text("title_pt").notNull().default(""),
    description: text("description").notNull().default(""),
    summaryPt: text("summary_pt").notNull().default(""),
    link: text("link").notNull(),
    pubDate: text("pub_date").notNull().default(""),
    journal: text("journal").notNull().$type<Journal>(),
    /** Unix timestamp (segundos) — quando o artigo foi inserido na base */
    createdAt: integer("created_at", { mode: "timestamp" }).notNull(),
  },
  (t) => [
    index("idx_articles_journal").on(t.journal),
    index("idx_articles_created_at").on(t.createdAt),
  ]
);

export type ArticleRow = typeof articles.$inferSelect;
export type InsertArticleRow = typeof articles.$inferInsert;
