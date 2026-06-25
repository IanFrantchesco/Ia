import { useState, useRef } from "react";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { JOURNAL_LABELS, JOURNALS } from "@shared/journals";
import type { Article, ArticlesResponse, ProcessResponse, WhatsAppResponse } from "@/types";
import type { Journal } from "@shared/journals";

// ─── Constantes ───────────────────────────────────────────────────────────────

const DAYS_OPTIONS = [7, 14, 30] as const;
type DaysOption = (typeof DAYS_OPTIONS)[number];

const ALL_JOURNAL_OPTIONS: (Journal | "ALL")[] = ["ALL", ...JOURNALS];

// ─── API helper ───────────────────────────────────────────────────────────────

async function apiFetch<T>(path: string): Promise<T> {
  const res = await fetch(path);
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error((body as { error?: string }).error ?? `HTTP ${res.status}`);
  }
  return res.json() as Promise<T>;
}

// ─── Componente principal ─────────────────────────────────────────────────────

export default function Home() {
  const queryClient = useQueryClient();
  const [journal, setJournal] = useState<Journal | "ALL">("ALL");
  const [days, setDays] = useState<DaysOption>(7);
  const [showWpp, setShowWpp] = useState(false);
  const [copied, setCopied] = useState(false);
  const copyTimerRef = useRef<ReturnType<typeof setTimeout> | undefined>(undefined);

  // Artigos do banco
  const articlesQuery = useQuery({
    queryKey: ["articles", journal, days],
    queryFn: () => {
      const params = new URLSearchParams({ days: String(days) });
      if (journal !== "ALL") params.set("journal", journal);
      return apiFetch<ArticlesResponse>(`/api/articles?${params}`);
    },
  });

  // Mensagem WhatsApp (lazy — só carrega quando o painel é aberto)
  const wppQuery = useQuery({
    queryKey: ["whatsapp", days],
    queryFn: () => apiFetch<WhatsAppResponse>(`/api/whatsapp?days=${days}`),
    enabled: showWpp,
  });

  // Buscar e processar (CrossRef → Claude → banco)
  const processMutation = useMutation({
    mutationFn: () => {
      const params = new URLSearchParams();
      if (journal !== "ALL") params.set("journal", journal);
      return apiFetch<ProcessResponse>(`/api/process?${params}`);
    },
    onSuccess: () => {
      setDays(7);
      queryClient.invalidateQueries({ queryKey: ["articles"] });
      queryClient.invalidateQueries({ queryKey: ["whatsapp"] });
    },
  });

  // Agrupar artigos por periódico na ordem canônica
  const articles = articlesQuery.data?.articles ?? [];
  const sections = JOURNALS.flatMap((j) => {
    if (journal !== "ALL" && j !== journal) return [];
    const group = articles.filter((a) => a.journal === j);
    return group.length > 0 ? [{ journal: j, group }] : [];
  });

  function handleCopy() {
    const msg = wppQuery.data?.message;
    if (!msg) return;
    navigator.clipboard.writeText(msg).then(
      () => {
        setCopied(true);
        clearTimeout(copyTimerRef.current);
        copyTimerRef.current = setTimeout(() => setCopied(false), 2000);
      },
      () => { /* permissão negada ou contexto não seguro — sem feedback visual */ }
    );
  }

  const db = processMutation.data?.db;
  const failedCount = processMutation.data?.failedDois.length ?? 0;

  return (
    <main className="min-h-screen" style={{ backgroundColor: "var(--background)", color: "var(--foreground)" }}>
      {/* Cabeçalho */}
      <header className="px-8 pt-8 pb-6" style={{ borderBottom: "1px solid var(--border)" }}>
        <h1>CardioNews</h1>
        <p className="mt-2 text-sm" style={{ color: "var(--muted-foreground)" }}>
          Monitor de artigos cardiológicos — JAMA · Heart Rhythm · JCE · Circulation
        </p>
      </header>

      {/* Controles */}
      <div className="px-8 py-4 flex flex-wrap gap-3 items-center" style={{ borderBottom: "1px solid var(--border)" }}>
        {/* Filtro de periódico */}
        <div className="flex gap-2 flex-wrap">
          {ALL_JOURNAL_OPTIONS.map((j) => (
            <button
              key={j}
              onClick={() => setJournal(j)}
              className="text-sm px-3 py-1.5"
              style={{
                border: "1px solid",
                borderRadius: "var(--radius)",
                borderColor: journal === j ? "var(--primary)" : "var(--border)",
                backgroundColor: journal === j ? "var(--primary)" : "transparent",
                color: journal === j ? "var(--primary-foreground)" : "var(--foreground)",
                cursor: "pointer",
              }}
            >
              {j === "ALL" ? "Todos" : JOURNAL_LABELS[j]}
            </button>
          ))}
        </div>

        {/* Filtro de período */}
        <select
          value={days}
          onChange={(e) => setDays(Number(e.target.value) as DaysOption)}
          className="text-sm px-3 py-1.5"
          style={{
            border: "1px solid var(--border)",
            borderRadius: "var(--radius)",
            backgroundColor: "var(--background)",
            color: "var(--foreground)",
            cursor: "pointer",
          }}
        >
          {DAYS_OPTIONS.map((d) => (
            <option key={d} value={d}>{d} dias</option>
          ))}
        </select>

        {/* Botão de busca */}
        <button
          onClick={() => processMutation.mutate()}
          disabled={processMutation.isPending}
          className="ml-auto text-sm px-4 py-1.5"
          style={{
            border: "1px solid var(--accent)",
            borderRadius: "var(--radius)",
            backgroundColor: "var(--accent)",
            color: "var(--accent-foreground)",
            cursor: processMutation.isPending ? "not-allowed" : "pointer",
            opacity: processMutation.isPending ? 0.7 : 1,
          }}
        >
          {processMutation.isPending ? "Buscando…" : "↻ Buscar e processar"}
        </button>
      </div>

      {/* Banner de resultado */}
      {(db != null || processMutation.isError) && (
        <div
          className="px-8 py-2 text-sm"
          style={{
            borderBottom: "1px solid var(--border)",
            color: processMutation.isError ? "var(--destructive)" : "var(--muted-foreground)",
          }}
        >
          {processMutation.isError
            ? `Erro: ${(processMutation.error as Error).message}`
            : `✓ ${db!.inserted} novos · ${db!.skipped} já existentes${failedCount > 0 ? ` · ${failedCount} com falha de tradução` : ""}`}
        </div>
      )}

      {/* Lista de artigos */}
      <div className="px-8 py-8">
        {articlesQuery.isLoading && (
          <p style={{ color: "var(--muted-foreground)" }}>Carregando artigos…</p>
        )}
        {articlesQuery.isError && (
          <p style={{ color: "var(--destructive)" }}>
            Erro: {(articlesQuery.error as Error).message}
          </p>
        )}
        {articlesQuery.isSuccess && sections.length === 0 && (
          <p style={{ color: "var(--muted-foreground)" }}>
            Nenhum artigo nos últimos {days} dias.
          </p>
        )}

        {sections.map(({ journal: j, group }) => (
          <section key={j} className="mb-12">
            <h2>{JOURNAL_LABELS[j]}</h2>
            <div className="editorial-divider" />
            <div className="flex flex-col gap-6">
              {group.map((article) => (
                <ArticleCard key={article.doi} article={article} />
              ))}
            </div>
          </section>
        ))}
      </div>

      {/* Painel WhatsApp */}
      <div className="px-8 pb-12">
        <button
          onClick={() => setShowWpp((v) => !v)}
          className="text-sm px-4 py-2"
          style={{
            border: "1px solid var(--border)",
            borderRadius: "var(--radius)",
            backgroundColor: "transparent",
            color: "var(--foreground)",
            cursor: "pointer",
          }}
        >
          {showWpp ? "▲" : "▼"} Mensagem WhatsApp ({days}d)
        </button>

        {showWpp && (
          <div className="editorial-card mt-4">
            <div className="flex justify-end mb-3">
              <button
                onClick={handleCopy}
                disabled={!wppQuery.data || wppQuery.isFetching}
                className="text-xs px-3 py-1"
                style={{
                  border: "1px solid var(--border)",
                  borderRadius: "var(--radius)",
                  backgroundColor: "transparent",
                  color: "var(--foreground)",
                  cursor: wppQuery.data ? "pointer" : "not-allowed",
                }}
              >
                {copied ? "✓ Copiado" : "Copiar"}
              </button>
            </div>
            {(wppQuery.isLoading || wppQuery.isFetching) && (
              <p style={{ color: "var(--muted-foreground)" }}>Gerando mensagem…</p>
            )}
            {wppQuery.isError && (
              <p style={{ color: "var(--destructive)" }}>Erro ao gerar mensagem.</p>
            )}
            {wppQuery.data && !wppQuery.isFetching && (
              <pre className="text-sm leading-relaxed whitespace-pre-wrap font-mono m-0">
                {wppQuery.data.message}
              </pre>
            )}
          </div>
        )}
      </div>
    </main>
  );
}

// ─── Card de artigo ───────────────────────────────────────────────────────────

function ArticleCard({ article }: { article: Article }) {
  const displayTitle = article.titlePt || article.title;
  return (
    <article className="editorial-card">
      <h3>{displayTitle}</h3>
      {article.pubDate && (
        <p className="text-xs mt-1" style={{ color: "var(--muted-foreground)" }}>
          {article.pubDate}
        </p>
      )}
      {article.summaryPt && (
        <p className="mt-4 leading-relaxed" style={{ fontSize: "0.95rem" }}>
          {article.summaryPt}
        </p>
      )}
      <a
        href={article.link}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-block mt-4 text-sm"
        style={{ color: "var(--primary)", textDecoration: "none" }}
      >
        Ler artigo →
      </a>
    </article>
  );
}
