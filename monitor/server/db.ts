import Database from "better-sqlite3";
import { drizzle, type BetterSQLite3Database } from "drizzle-orm/better-sqlite3";
import { migrate } from "drizzle-orm/better-sqlite3/migrator";
import * as schema from "./schema.js";

export type Db = BetterSQLite3Database<typeof schema>;

const DB_PATH = process.env["DB_PATH"] ?? "./cardio.db";
const MIGRATIONS_PATH = process.env["MIGRATIONS_PATH"] ?? "./drizzle";

function createConnection(path: string): Db {
  const sqlite = new Database(path);
  sqlite.pragma("journal_mode = WAL");
  sqlite.pragma("foreign_keys = ON");
  return drizzle(sqlite, { schema });
}

export const db: Db = createConnection(DB_PATH);

/** Aplica todas as migrações pendentes. Chamar uma vez na inicialização do servidor. */
export function initDb(database: Db = db, migrationsFolder: string = MIGRATIONS_PATH): void {
  migrate(database, { migrationsFolder });
  console.log(`[db] migrações aplicadas — ${DB_PATH}`);
}

/** Cria uma conexão in-memory isolada para testes. */
export function createTestDb(): Db {
  const sqlite = new Database(":memory:");
  const testDb = drizzle(sqlite, { schema });
  migrate(testDb, { migrationsFolder: MIGRATIONS_PATH });
  return testDb;
}
