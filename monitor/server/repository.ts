/**
 * Camada de acesso a dados — artigos cardiológicos processados.
 * Todas as funções aceitam um parâmetro `database` opcional para injeção em testes.
 */

import { eq, desc, gte, and } from "drizzle-orm";
import { db as defaultDb, type Db } from "./db.js";
import { articles } from "./schema.js";
import type { ArticleRow, InsertArticleRow } from "./schema.js";
import type { ProcessedArticle } from "./article-processor.js";
import type { Journal } from "./scraper.js";

export type { ArticleRow };

// ─── Escrita ──────────────────────────────────────────────────────────────────

/**
 * Insere artigos novos; ignora DOIs já existentes (deduplicação por DOI).
 * Nunca deleta artigos existentes — corrige o bug do padrão delete-all-before-insert.
 */
export function upsertArticles(
  processed: ProcessedArticle[],
  database: Db = defaultDb
): { inserted: number; skipped: number } {
  const now = new Date();
  let inserted = 0;

  for (const article of processed) {
    const row: InsertArticleRow = {
      doi: article.doi,
      title: article.title,
      titlePt: article.titlePt,
      description: article.description,
      summaryPt: article.summaryPt,
      link: article.link,
      pubDate: article.pubDate,
      journal: article.journal,
      createdAt: now,
    };

    const result = database.insert(articles).values(row).onConflictDoNothing().run();
    if (result.changes > 0) inserted++;
  }

  return { inserted, skipped: processed.length - inserted };
}

// ─── Leitura ──────────────────────────────────────────────────────────────────

export interface ArticleFilters {
  journal?: Journal;
  /** Apenas artigos inseridos nos últimos N dias (padrão: 30) */
  days?: number;
}

/** Retorna artigos do banco, ordenados do mais recente para o mais antigo. */
export function getArticles(
  filters: ArticleFilters = {},
  database: Db = defaultDb
): ArticleRow[] {
  const { journal, days = 30 } = filters;

  const cutoff = new Date();
  cutoff.setDate(cutoff.getDate() - days);

  const conditions = [gte(articles.createdAt, cutoff)];
  if (journal) conditions.push(eq(articles.journal, journal));

  return database
    .select()
    .from(articles)
    .where(conditions.length === 1 ? conditions[0] : and(...conditions))
    .orderBy(desc(articles.createdAt))
    .all();
}

/** Retorna um artigo pelo DOI, ou null se não existir. */
export function getArticleByDoi(doi: string, database: Db = defaultDb): ArticleRow | null {
  const rows = database.select().from(articles).where(eq(articles.doi, doi)).limit(1).all();
  return rows[0] ?? null;
}
