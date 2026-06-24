import { defineConfig } from "vitest/config";
import { resolve } from "path";

export default defineConfig({
  test: {
    passWithNoTests: true,
    projects: [
      {
        // Testes do servidor — ambiente Node puro, sem DOM
        test: {
          name: "server",
          include: ["server/**/*.test.ts"],
          environment: "node",
        },
        resolve: {
          alias: {
            // No vitest server, @shared resolve via caminho relativo
            "@shared": resolve(__dirname, "shared"),
          },
        },
      },
      {
        // Testes do cliente — ambiente DOM (jsdom)
        test: {
          name: "client",
          include: ["client/src/**/*.test.{ts,tsx}"],
          environment: "jsdom",
        },
        resolve: {
          alias: {
            "@": resolve(__dirname, "client/src"),
            "@shared": resolve(__dirname, "shared"),
          },
        },
      },
    ],
  },
});
