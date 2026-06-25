/**
 * Camada de acesso a dados — artigos cardiológicos processados.
 * Todas as funções aceitam um parâmetro `database` opcional para injeção em testes.
 */

import { eq, desc, gte, and } from "drizzle-orm";
import { db as defaultDb, type Db } from "./db.js";
import { articles } from "./schema.js";
import type { ArticleRow } from "./schema.js";
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
  if (processed.length === 0) return { inserted: 0, skipped: 0 };

  const now = new Date();
  const inserted = database.transaction((tx) => {
    let count = 0;
    for (const article of processed) {
      const result = tx
        .insert(articles)
        .values({ ...article, createdAt: now })
        .onConflictDoNothing()
        .run();
      if (result.changes > 0) count++;
    }
    return count;
  });

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
    .where(and(...conditions))
    .orderBy(desc(articles.createdAt))
    .all();
}

/** Retorna um artigo pelo DOI, ou null se não existir. */
export function getArticleByDoi(doi: string, database: Db = defaultDb): ArticleRow | null {
  const rows = database.select().from(articles).where(eq(articles.doi, doi)).limit(1).all();
  return rows[0] ?? null;
}
