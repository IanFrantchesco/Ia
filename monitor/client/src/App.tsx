import { useQuery } from "@tanstack/react-query";

export default function App() {
  const { data, isLoading } = useQuery({
    queryKey: ["health"],
    queryFn: () => fetch("/api/health").then((r) => r.json()),
  });

  return (
    <main style={{ padding: "2rem" }}>
      <h1>Monitor de Artigos Cardiológicos</h1>
      <p style={{ marginTop: "1rem", color: "var(--muted-foreground)" }}>
        {isLoading
          ? "Verificando servidor..."
          : data?.ok
          ? `Servidor OK — ${data.ts}`
          : "Servidor indisponível"}
      </p>
    </main>
  );
}
