import { useQuery } from "@tanstack/react-query";

export default function App() {
  const { data, isLoading, isError } = useQuery({
    queryKey: ["health"],
    queryFn: async () => {
      const res = await fetch("/api/health");
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      return res.json() as Promise<{ ok: boolean; ts: string }>;
    },
  });

  const status = isLoading
    ? "Verificando servidor..."
    : isError
    ? "Servidor indisponível"
    : `Servidor OK — ${data?.ts}`;

  return (
    <main className="p-8">
      <h1 className="text-4xl font-bold">Monitor de Artigos Cardiológicos</h1>
      <p className="mt-4 text-[var(--muted-foreground)]">{status}</p>
    </main>
  );
}
