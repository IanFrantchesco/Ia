import Database from "better-sqlite3";
import type { Database as SQLiteDatabase } from "better-sqlite3";
import { drizzle, type BetterSQLite3Database } from "drizzle-orm/better-sqlite3";
import { migrate } from "drizzle-orm/better-sqlite3/migrator";
import { dirname, join, resolve } from "path";
import { mkdirSync } from "fs";
import { fileURLToPath } from "url";
import * as schema from "./schema.js";

export type Db = BetterSQLite3Database<typeof schema> & { $client: SQLiteDatabase };

const __dirname = dirname(fileURLToPath(import.meta.url));
const DB_PATH = process.env["DB_PATH"] ?? "./cardio.db";
// Em dev: <monitor>/server/../drizzle = <monitor>/drizzle
// Em prod (node dist/server/index.js): <monitor>/dist/server/../drizzle = <monitor>/dist/drizzle
const MIGRATIONS_PATH = process.env["MIGRATIONS_PATH"] ?? join(__dirname, "../drizzle");

function createConnection(path: string): Db {
  // Garante que o diretório pai existe (necessário quando DB_PATH aponta para volume externo, ex: /data/cardio.db)
  mkdirSync(dirname(resolve(path)), { recursive: true });
  const sqlite = new Database(path);
  sqlite.pragma("journal_mode = WAL");
  sqlite.pragma("foreign_keys = ON");
  return drizzle(sqlite, { schema });
}

export const db: Db = createConnection(DB_PATH);

/** Aplica todas as migrações pendentes. Chamar uma vez na inicialização do servidor. */
export function initDb(database: Db = db, migrationsFolder: string = MIGRATIONS_PATH): void {
  migrate(database, { migrationsFolder });
  console.log(`[db] migrações aplicadas — ${migrationsFolder}`);
}

/** Cria uma conexão in-memory isolada para testes. */
export function createTestDb(): Db {
  const sqlite = new Database(":memory:");
  sqlite.pragma("foreign_keys = ON");
  const testDb = drizzle(sqlite, { schema });
  migrate(testDb, { migrationsFolder: MIGRATIONS_PATH });
  return testDb;
}
