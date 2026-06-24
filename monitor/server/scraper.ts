/**
 * Busca artigos via CrossRef API para 4 periódicos de eletrofisiologia/cardiologia.
 * Fonte: api.crossref.org — API pública, sem autenticação, polite pool via User-Agent.
 *
 * Dois filtros ativos por artigo:
 *   1. Títulos editoriais/administrativos (correction, retraction, etc.) → descartados
 *   2. Campo "created" mais antigo que maxCreatedAgeDays → descartado
 *      HR: usa created−1 dia como data de publicação (Elsevier deposita 1 dia depois)
 */

// ─── Constantes ─────────────────────────────────────────────────────────────

const CROSSREF_API = "https://api.crossref.org/works";
const CONTACT_EMAIL = process.env["CONTACT_EMAIL"] ?? "cardionews@example.com";
const USER_AGENT = `CardioMonitor/1.0 (mailto:${CONTACT_EMAIL})`;
const MAX_PER_JOURNAL = 10;
const MAX_CROSSREF_ROWS = MAX_PER_JOURNAL * 5; // margem para descartes editoriais
const REQUEST_TIMEOUT_MS = 25_000;
const MAX_RETRIES = 3;
const RETRY_BASE_WAIT_MS = 1_500;
const RATE_LIMIT_WAIT_MS = 3_000;

// ─── Tipos públicos ───────────────────────────────────────────────────────────

export type Journal = "JAMA" | "HR" | "JCE" | "CAH";

export interface ScrapedArticle {
  title: string;
  link: string;
  /** "YYYY-MM-DD" se dia disponível, "YYYY-MM" se apenas mês, "YYYY" se apenas ano, "" se ausente */
  pubDate: string;
  description: string;
  doi: string;
  journal: Journal;
}

// ─── Tipos internos da API CrossRef ──────────────────────────────────────────

export type DateParts = [number, number?, number?];

export interface CrossRefDate {
  /** CrossRef sempre retorna 1 elemento, tipado como array para compatibilidade JSON */
  "date-parts": DateParts[];
}

export interface CrossRefItem {
  title?: string[];
  DOI?: string;
  abstract?: string;
  "published-online"?: CrossRefDate;
  published?: CrossRefDate;
  created?: CrossRefDate;
}

interface CrossRefResponse {
  message?: { items?: CrossRefItem[] };
}

// ─── Configuração por periódico ───────────────────────────────────────────────

export interface JournalConfig {
  issn: string;
  journal: Journal;
  /** Delay antes do request — evita burst simultâneo nos 4 periódicos */
  delayMs: number;
  /** Janela de busca em dias (from-pub-date ou from-created-date) */
  windowDays: number;
  /**
   * HR usa from-created-date: a Elsevier deposita no CrossRef 1 dia após
   * a publicação online, então created−1 = data real de disponibilidade.
   */
  useCreatedDate: boolean;
  /** Artigos com "created" mais antigo que isso são descartados */
  maxCreatedAgeDays: number;
  /**
   * Ajuste em dias aplicado ao campo "created" para obter a data de publicação real.
   * HR = -1: a Elsevier deposita no CrossRef 1 dia após a publicação online.
   * 0 para todos os demais.
   */
  pubDateOffsetDays: number;
}

export const JOURNAL_CONFIGS: Record<Journal, JournalConfig> = {
  JAMA: { issn: "2380-6583", journal: "JAMA", delayMs: 0,    windowDays: 7, useCreatedDate: false, maxCreatedAgeDays: 30, pubDateOffsetDays: 0  },
  HR:   { issn: "1547-5271", journal: "HR",   delayMs: 1500, windowDays: 7, useCreatedDate: true,  maxCreatedAgeDays: 7,  pubDateOffsetDays: -1 },
  JCE:  { issn: "1045-3873", journal: "JCE",  delayMs: 4500, windowDays: 7, useCreatedDate: false, maxCreatedAgeDays: 30, pubDateOffsetDays: 0  },
  CAH:  { issn: "0009-7322", journal: "CAH",  delayMs: 6000, windowDays: 7, useCreatedDate: false, maxCreatedAgeDays: 30, pubDateOffsetDays: 0  },
};

// ─── Padrões editoriais/administrativos ──────────────────────────────────────

const EDITORIAL_PATTERNS = [
  /peer\s+reviewers?/i,
  /\bcorrection\b/i,
  /\bretraction\b/i,
  /\berratum\b/i,
  /\bcorrigendum\b/i,
  /\baddendum\b/i,
  /^editors?\b/i,
  /editorial\s+board/i,
  /^table\s+of\s+cont/i,
  /^cover\s+image/i,
  /^issue\s+information/i,
  /^masthead/i,
  /^graphical\s+abstract/i,
  /^in\s+memoriam/i,
  /^acknowledgements?$/i,
] as const;

// ─── Funções puras (exportadas para testes) ───────────────────────────────────

/** Retorna true se o título indica artigo editorial/administrativo. */
export function isEditorialArticle(title: string): boolean {
  return EDITORIAL_PATTERNS.some((p) => p.test(title));
}

/**
 * Extrai a data de publicação de um item CrossRef.
 * Prioridade: published-online > published > created.
 * Retorna "YYYY-MM-DD" se dia disponível, "YYYY-MM" se apenas mês, "YYYY" se apenas ano.
 * Retorna "" se nenhum campo de data estiver presente no item.
 */
export function extractPublicationDate(item: CrossRefItem): string {
  const dateParts =
    item["published-online"]?.["date-parts"]?.[0] ??
    item["published"]?.["date-parts"]?.[0] ??
    item["created"]?.["date-parts"]?.[0];

  if (!dateParts || dateParts[0] === undefined) {
    return "";
  }

  const [year, month, day] = dateParts;
  if (month !== undefined && day !== undefined) {
    return `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
  }
  if (month !== undefined) {
    return `${year}-${String(month).padStart(2, "0")}`;
  }
  return String(year);
}

/**
 * Extrai a data do campo "created" como objeto Date.
 * Retorna null se o campo estiver ausente, malformado, ou sem mês.
 */
export function getCreatedDate(item: CrossRefItem): Date | null {
  const parts = item["created"]?.["date-parts"]?.[0];
  if (!parts || parts[0] === undefined || parts[1] === undefined) return null;
  const [year, month, day] = parts;
  return new Date(year, month - 1, day ?? 1);
}

/**
 * Remove tags XML/HTML do abstract (CrossRef usa JATS: <jats:p>, <jats:italic>…).
 * Normaliza espaços extras resultantes da remoção.
 */
export function cleanAbstract(abstract?: string): string {
  if (!abstract) return "";
  return abstract
    .replace(/<[^>]+>/g, " ")
    .replace(/&(?:[a-z]+|#\d+|#x[\da-f]+);/gi, " ")
    .replace(/\s+/g, " ")
    .trim();
}

/**
 * Constrói a URL de acesso ao artigo.
 * CAH (Circulation/AHA): usa PubMed como proxy — site da AHA tem Cloudflare.
 * Demais: doi.org (padrão universal).
 */
export function buildArticleLink(journal: Journal, doi: string): string {
  if (journal === "CAH") {
    return `https://pubmed.ncbi.nlm.nih.gov/?term=${encodeURIComponent(doi)}`;
  }
  return `https://doi.org/${doi}`;
}

/** Formata Date como "YYYY-MM-DD" usando componentes locais — evita shift UTC do toISOString(). */
function toLocalISODate(date: Date): string {
  return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`;
}

// ─── HTTP ────────────────────────────────────────────────────────────────────

const sleep = (ms: number) => new Promise<void>((r) => setTimeout(r, ms));

const FETCH_HEADERS = { "User-Agent": USER_AGENT, Accept: "application/json" } as const;

async function fetchWithRetry(url: string): Promise<Response> {
  for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
    try {
      const res = await fetch(url, {
        headers: FETCH_HEADERS,
        signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS),
      });

      if (res.status === 429) {
        if (attempt < MAX_RETRIES) {
          console.warn(`[scraper] rate limited — aguardando ${RATE_LIMIT_WAIT_MS * attempt}ms`);
          await sleep(RATE_LIMIT_WAIT_MS * attempt);
        }
        continue;
      }

      // Erros 5xx são transientes — retentar com backoff (4xx não são, retornar imediatamente)
      if (res.status >= 500 && attempt < MAX_RETRIES) {
        console.warn(`[scraper] HTTP ${res.status} — retry ${attempt}/${MAX_RETRIES}`);
        await sleep(RETRY_BASE_WAIT_MS * attempt);
        continue;
      }

      return res;
    } catch (err) {
      if (attempt === MAX_RETRIES) throw err;
      await sleep(RETRY_BASE_WAIT_MS * attempt);
    }
  }

  throw new Error("CrossRef: max retries exceeded");
}

// ─── Query principal ──────────────────────────────────────────────────────────

async function queryByISSN(config: JournalConfig): Promise<ScrapedArticle[]> {
  if (config.delayMs > 0) await sleep(config.delayMs);

  const fromDate = new Date();
  fromDate.setDate(fromDate.getDate() - config.windowDays);
  const fromDateStr = toLocalISODate(fromDate);

  const dateFilter = config.useCreatedDate
    ? `from-created-date:${fromDateStr}`
    : `from-pub-date:${fromDateStr}`;

  const sortField = config.useCreatedDate ? "created" : "published";

  const url =
    `${CROSSREF_API}?filter=issn:${config.issn},${dateFilter}` +
    `&sort=${sortField}&order=desc&rows=${MAX_CROSSREF_ROWS}` +
    `&mailto=${encodeURIComponent(CONTACT_EMAIL)}`;

  console.log(`[scraper] ${config.journal}: buscando últimos ${config.windowDays} dias…`);

  const res = await fetchWithRetry(url);
  if (!res.ok) throw new Error(`CrossRef HTTP ${res.status} para ${config.journal}`);

  let data: CrossRefResponse;
  try {
    data = (await res.json()) as CrossRefResponse;
  } catch {
    throw new Error(`CrossRef resposta não-JSON para ${config.journal} (HTTP ${res.status})`);
  }
  const items = data.message?.items ?? [];

  const createdCutoff = new Date();
  createdCutoff.setDate(createdCutoff.getDate() - config.maxCreatedAgeDays);

  const articles: ScrapedArticle[] = [];

  for (const item of items) {
    if (!item.title?.[0] || !item.DOI) continue;

    // CrossRef inclui tags HTML (<i>, <b>, <sub>…) e entidades (&amp;, &#8220;…) em títulos
    const title = item.title[0]
      .replace(/<[^>]+>/g, " ")
      .replace(/&(?:[a-z]+|#\d+|#x[\da-f]+);/gi, " ")
      .replace(/\s+/g, " ")
      .trim();

    // Filtro 1: descartar artigos editoriais/administrativos
    if (isEditorialArticle(title)) {
      console.log(`[scraper] ${config.journal}: editorial — "${title.slice(0, 60)}"`);
      continue;
    }

    const createdDate = getCreatedDate(item);

    // Filtro 2: sem "created" ou mais antigo que maxCreatedAgeDays → descartado
    if (!createdDate || createdDate < createdCutoff) {
      if (createdDate) {
        console.log(`[scraper] ${config.journal}: created antigo (${toLocalISODate(createdDate)}) — descartado`);
      }
      continue;
    }

    // pubDate: periódicos com pubDateOffsetDays != 0 ajustam o campo created (ex: HR = −1 dia)
    let pubDate: string;
    if (config.pubDateOffsetDays !== 0) {
      const adjusted = new Date(createdDate);
      adjusted.setDate(adjusted.getDate() + config.pubDateOffsetDays);
      pubDate = toLocalISODate(adjusted);
    } else {
      pubDate = extractPublicationDate(item);
    }

    articles.push({
      title,
      link: buildArticleLink(config.journal, item.DOI),
      pubDate,
      description: cleanAbstract(item.abstract),
      doi: item.DOI,
      journal: config.journal,
    });
  }

  const limited = articles.slice(0, MAX_PER_JOURNAL);
  console.log(`[scraper] ${config.journal}: ${articles.length} após filtros → ${limited.length} retornados`);
  return limited;
}

// ─── Exports públicos ─────────────────────────────────────────────────────────

export interface ScrapeResult {
  articles: ScrapedArticle[];
  /** Periódicos que falharam durante a busca (rede, API indisponível, etc.) */
  errors: { journal: Journal; message: string }[];
}

export async function scrapeAllArticles(): Promise<ScrapeResult> {
  console.log(`[scraper] iniciando busca — ${new Date().toISOString()}`);

  const cfgs = Object.values(JOURNAL_CONFIGS);
  const settled = await Promise.allSettled(cfgs.map((cfg) => queryByISSN(cfg)));

  const articles: ScrapedArticle[] = [];
  const errors: ScrapeResult["errors"] = [];

  settled.forEach((result, i) => {
    const journal = cfgs[i]!.journal;
    if (result.status === "fulfilled") {
      articles.push(...result.value);
    } else {
      const message = result.reason instanceof Error ? result.reason.message : String(result.reason);
      console.error(`[scraper] ${journal}: erro — ${message}`);
      errors.push({ journal, message });
    }
  });

  console.log(`[scraper] total: ${articles.length} artigos, ${errors.length} falhas`);
  return { articles, errors };
}

export async function scrapeJournal(journal: Journal): Promise<ScrapedArticle[]> {
  return queryByISSN({ ...JOURNAL_CONFIGS[journal], delayMs: 0 });
}
