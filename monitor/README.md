# CardioMonitor

Monitor de artigos cardiológicos. Busca publicações recentes de 4 periódicos via CrossRef, traduz títulos e resume abstracts para português brasileiro com Claude AI, armazena em SQLite e exibe numa interface React.

## Periódicos monitorados

| Código | Periódico |
|--------|-----------|
| JAMA | JAMA Cardiology |
| HR | Heart Rhythm |
| JCE | J. Cardiovasc. Electrophysiol. |
| CAH | Circulation |

## Requisitos

- Node.js 18+
- Chave de API Anthropic (`ANTHROPIC_API_KEY`)

## Configuração

```bash
cd monitor
npm install
```

Crie um arquivo `.env` na pasta `monitor/`:

```env
ANTHROPIC_API_KEY=sk-ant-...

# Opcionais
PORT=3000
DB_PATH=./cardio.db
CONTACT_EMAIL=seuemail@exemplo.com
CLAUDE_MODEL=claude-haiku-4-5-20251001
```

## Desenvolvimento

```bash
npm run dev
```

Inicia o servidor Express na porta 3000 e o cliente Vite na porta 5173 simultaneamente. Acesse `http://localhost:5173`.

## Produção

```bash
npm run build
npm start
```

O build compila o servidor TypeScript para `dist/server/`, copia as migrations para `dist/drizzle/` e compila o cliente React para `dist/client/`. O servidor Express serve os assets estáticos do cliente em produção.

Acesse `http://localhost:3000`.

## Deploy no Railway

1. Crie conta em [railway.app](https://railway.app) e conecte ao GitHub
2. **New Project → Deploy from GitHub repo** → selecione `IanFrantchesco/Ia`
3. Em **Settings → Root Directory**, defina: `monitor`
4. Em **Settings → Volumes**, crie um volume em `/data` para persistir o banco SQLite entre deploys
5. Em **Variables**, adicione:

| Variável | Valor |
|----------|-------|
| `ANTHROPIC_API_KEY` | `sk-ant-...` |
| `CONTACT_EMAIL` | seu email |
| `DB_PATH` | `/data/cardio.db` |

6. Railway detecta o `railway.toml` e faz o build automaticamente
7. Acesse a URL gerada pelo Railway de qualquer dispositivo

> O volume `/data` é necessário para que os artigos salvos não sejam perdidos a cada novo deploy.

## Testes

```bash
npm test
```

## Como usar

### Buscar e processar artigos

1. Selecione o periódico (ou "Todos")
2. Clique em **↻ Buscar e processar**
3. O sistema busca os artigos dos últimos 7 dias no CrossRef, traduz e resume com Claude, e salva no banco

O banner abaixo dos controles confirma quantos artigos foram inseridos e quantos já existiam.

### Filtrar artigos

- **Periódico**: filtra por journal específico ou exibe todos
- **Período**: 7, 14 ou 30 dias (contados pela data de inserção no banco)

### Mensagem WhatsApp

Clique em **▼ Mensagem WhatsApp** para gerar um texto formatado com todos os artigos do período. Use o botão **Copiar** e cole diretamente num grupo do WhatsApp. O markdown `*negrito*` é renderizado nativamente no app.

## Estrutura

```
monitor/
├── shared/
│   └── journals.ts          # Fonte de verdade: Journal type, labels, ordem canônica
├── server/
│   ├── scraper.ts           # Busca artigos via CrossRef API
│   ├── article-processor.ts # Tradução e resumo com Claude AI
│   ├── schema.ts            # Schema Drizzle (SQLite)
│   ├── db.ts                # Conexão e migrações
│   ├── repository.ts        # Leitura e escrita no banco
│   ├── whatsapp.ts          # Gerador de mensagem formatada
│   └── index.ts             # Servidor Express + rotas
├── client/
│   └── src/
│       ├── Home.tsx          # Interface principal
│       ├── types.ts          # Tipos compartilhados com o servidor
│       └── main.tsx          # Entry point React
├── drizzle/                  # Migrations SQL
└── package.json
```

## Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/api/health` | Status do servidor |
| GET | `/api/process?journal=ALL\|JAMA\|HR\|JCE\|CAH` | Busca CrossRef + traduz + salva no banco |
| GET | `/api/articles?journal=...&days=30` | Artigos armazenados no banco |
| GET | `/api/whatsapp?days=7` | Mensagem formatada para WhatsApp |
| GET | `/api/scrape?journal=...` | Busca bruta no CrossRef (sem banco, para validação) |

## Variáveis de ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `ANTHROPIC_API_KEY` | — | Obrigatória. Chave da API Anthropic |
| `PORT` | `3000` | Porta do servidor Express |
| `DB_PATH` | `./cardio.db` | Caminho do arquivo SQLite |
| `CONTACT_EMAIL` | `cardionews@example.com` | Email para o polite pool do CrossRef |
| `CLAUDE_MODEL` | `claude-haiku-4-5-20251001` | Modelo Claude para tradução |
| `MIGRATIONS_PATH` | `<dist>/drizzle` | Caminho das migrations (sobrescrever em testes) |
