# Cursor SQLite/transcript: sibling repos to mount

Clone these as **siblings of the moollm repo** so you can open them in Cursor alongside moollm. Cursor-mirror assimilates from them; local clones allow cross-check and deeper mining.

**Parent directory:** `Leela/git/` (same level as `moollm/`).  
**Process:** ASSIMILATION-PROCESS.md (Stage 1 → 2 → 3; tell-me-more pointers in "Current Stage 1 files").

| Repo | Path (sibling of moollm) | Why |
|------|--------------------------|-----|
| **S2thend/cursor-history** | `../cursor-history` | TypeScript: storage keys, parser, bubble schema, extractBubbleText, tool param aliases. |
| **jbdamask/cursor-db-mcp** | `../cursor-db-mcp` | Python MCP: workspace discovery, query_table, cursor:// resources. |
| **everestmz/cursor-rpc** | `../cursor-rpc` | Protobuf RPC layer (IDE↔server). Different from SQLite but same ecosystem. |
| **vltansky/cursor-chat-history-mcp** | `../cursor-chat-history-mcp` | TypeScript MCP: git-link conversations to commits, list/search/analytics; cursorDiskKV reader; hooks, links DB. |
| **ton-ai-core/unlimite-context** | `../unlimite-context` | TypeScript: composerData:* (ItemTable then cursorDiskKV); project filter; export to cursor-composers; Bubble/ToolCallData/codeBlockData. |

## Clone commands (run from `Leela/git/`)

```bash
cd /Users/a2deh/GroundUp/Leela/git

git clone https://github.com/S2thend/cursor-history.git
git clone https://github.com/jbdamask/cursor-db-mcp.git
git clone https://github.com/everestmz/cursor-rpc.git
git clone https://github.com/vltansky/cursor-chat-history-mcp.git
git clone https://github.com/ton-ai-core/unlimite-context.git
```

## Recommended next (clone + mount for assimilation)

| Repo | Path (sibling of moollm) | Why |
|------|--------------------------|-----|
| **dav-ell/blink** | `../blink` | Cursor Internals skill: Auth, API catalog, 40+ models, cursorDiskKV/ItemTable schema. Worth cloning (PENDING-SOURCES). |
| **somogyijanos/cursor-chat-export** | `../cursor-chat-export` | Python CLI; workspace discovery, config paths, export to Markdown; completes export-tool trio with S2thend + unlimite-context. |
| **HamedMP/CursorLens** | `../CursorLens` | Proxy that logs AI generations/usage (traffic layer). Optional if you want proxy schema. |
| **markelaugust74/Cursor-history-MCP** | `../Cursor-history-MCP` | Python MCP; FastAPI, LanceDB, Ollama, RAG over chat history. Small; how they read/vectorize. |

```bash
cd /Users/a2deh/GroundUp/Leela/git

# Recommended next (high value)
git clone https://github.com/dav-ell/blink.git
git clone https://github.com/somogyijanos/cursor-chat-export.git

# Optional (proxy / RAG layer)
git clone https://github.com/HamedMP/CursorLens.git
git clone https://github.com/markelaugust74/Cursor-history-MCP.git
```

After cloning, add the sibling folders to your Cursor workspace so the agent can read them. Not cloneable: tarq.net (blog), Cursor Forum, TensorZero/Monish/recovery (articles).

**Deep dives (2026-02-18):** All 10 sibling repos were mined; each assimilated YAML in reference/assimilated/ now has a `deep_dive` (or `deep_dive_repo`) section with file refs, exact keys, and code notes from the clone. TensorZero repo Cursor example (examples/integrations/cursor/feedback/src/cursor.rs) added to TENSORZERO-CURSOR-LLM-CLIENT.yml.

---

## Track Cursor changes (constitutional)

**Discover Cursor changes by tracking these projects.** They track Cursor at different rates (repos: code/keys; forum: reports; blog: posts). Run a pipeline: `git pull` in each sibling; check forum and blog for new content. When a source changes (e.g. cursor-history adds support for a new key), re-mine → update assimilated → Stage 2/3. By design: we use the ecosystem as a change-detection network, not Cursor changelogs alone. See ASSIMILATION-PROCESS.md "Track Cursor changes by tracking sources."

---

## Key files to mine (cursor-mirror assimilation)

When siblings are mounted, these are the files that feed KEY-CATALOG, BORG-COLLECTIVE-COOKBOOK, and assimilated docs.

### cursor-history (TypeScript)

| Path | Purpose |
|------|---------|
| `src/core/storage.ts` | DB paths, CHAT_DATA_KEYS, cursorDiskKV queries, extractBubbleText, formatToolCallWithResult |
| `src/core/parser.ts` | RawChatData, ComposerData, ComposerHead, GenerationEntry, bubble parsing |
| `src/core/types.ts` | MessageType, ToolCall, TokenUsage, SessionUsage |
| `src/core/database/*.ts` | Registry, drivers (node-sqlite, better-sqlite3) |
| `src/core/backup.ts` | Backup manifest schema |
| `src/cli/commands/list.ts`, `show.ts`, `export.ts` | How session list and full session are read |
| `package.json` | Deps (e.g. better-sqlite3), scripts |

Config/tooling: `.prettierrc`, `eslint.config.js`, `vitest.config.ts`, `tsconfig.json`, `CLAUDE.md`, `README.md`. Specs: `specs/`, `examples/`, `docs/`.

### cursor-db-mcp (Python)

| Path | Purpose |
|------|---------|
| `cursor-db-mcp-server.py` | MCP server: workspace discovery, query_table, cursor:// resources, ItemTable/cursorDiskKV keys |
| `install.py` | Install / config |
| `test_mcp_server.py` | How DB paths and queries are used |
| `requirements.txt` | FastMCP, sqlite3 |

Other: `README.md`, `LICENSE`, `img/` (if present).

### cursor-rpc (Go)

| Path | Purpose |
|------|---------|
| `client.go` | RPC client entry |
| `cursor/aiserver/v1/aiserver.proto` | Protobuf: IDE↔server API surface |
| `cursor/gen/aiserver/v1/*.go` | Generated Go from proto |
| `cmd/extract/main.go`, `preprocess.js`, `postprocess.js` | Extraction pipeline (from minified Cursor) |
| `cmd/example/main.go` | Example usage |
| `Makefile`, `go.mod`, `cursor_version.txt` | Build and version |

Different layer than SQLite: use for protocol shape, not keys or bubbles.

### cursor-chat-history-mcp (TypeScript)

| Path | Purpose |
|------|---------|
| `src/database/reader.ts` | CursorDatabaseReader, cursorDiskKV, connect/query, legacy vs modern |
| `src/database/parser.ts` | Bubble/conversation parsing |
| `src/database/types.ts` | CursorConversation, Legacy/Modern, BubbleMessage |
| `src/linker/links-database.ts` | Git links SQLite (CursorChatHistory/links.sqlite) |
| `src/linker/linker-tools.ts` | MCP tools: get_file_context, get_commit_conversations, link_conversation_commit |
| `src/linker/commands/install-cursor-hook.ts` | ~/.cursor/hooks.json, git post-commit hook |
| `src/tools/conversation-tools.ts` | list_conversations, get_conversation, search_conversations |
| `src/tools/analytics-tools.ts` | get_conversation_analytics (files, languages, temporal) |
| `docs/SPEC.md` | Git linker specification |
| `package.json` | @modelcontextprotocol/sdk, better-sqlite3, zod; bin server + linker/cli |

DB locations: README (Cursor state.vscdb vs CursorChatHistory/links.sqlite per OS). Context files: ~/.cursor-chat-history/context/conversations/<id>.md.

### unlimite-context (TypeScript)

| Path | Purpose |
|------|---------|
| `src/lib/logExtractor.ts` | getDefaultDbPath (win/darwin/linux + cursor-dev fallback), ItemTable then cursorDiskKV, composerData:*, FullConversationLog/Bubble/ToolCallData/CodeBlockDetails, formatUserMessageV2/formatAiMessageV2, extractAndSaveCursorChatLogs |
| `src/cli/index.ts` | commander; saveDir = (saveToProject \|\| cwd)/cursor-composers; prints 5 newest + rest count |
| `package.json` | better-sqlite3, commander, fs-extra, uuid; bin unlimite-context → dist/cli/index.js |

Output: cursor-composers/ (main log + details subdir with tool_call_*.json, code_block_*). .gitignore: cursor-export-logs/. Assimilated: reference/assimilated/TON-AI-CORE-UNLIMITE-CONTEXT.yml.

### blink (dav-ell) — Cursor skills only

| Path | Purpose |
|------|---------|
| `.cursor/rules/skills/cursor-internals/SKILL.mdc` | Auth (Auth0, api2.cursor.sh), 40+ models, JSON vs Protobuf, DB quick ref, cursor-agent create-chat |
| `.cursor/rules/skills/cursor-db/SKILL.mdc` | IDE globalStorage vs cursor-agent ~/.cursor/chats/store.db; cursorDiskKV/ItemTable; composer _v:10, bubble _v:3 (69+ fields); store.db meta+blobs |
| `.cursor/rules/skills/cursor-db/EXAMPLES.mdc` | Examples |
| `.cursor/rules/skills/cursor-internals/EXAMPLES.mdc` | Examples |

No code in repo reads state.vscdb; skills are documentation. Assimilated: reference/assimilated/DAV-ELL-BLINK-CURSOR-SKILLS.yml.

### cursor-chat-export (somogyijanos)

| Path | Purpose |
|------|---------|
| `config.yml` | default_vscdb_dir_paths (Windows/Darwin/Linux workspaceStorage), aichat_query (ItemTable key) |
| `chat.py` | get_cursor_workspace_path, get_latest_workspace_db_path, discover, export (Typer CLI) |
| `src/vscdb.py` | VSCDBQuery, query_aichat_data (loads config query) |
| `src/export.py` | MarkdownChatFormatter (tabs/bubbles user/ai), ChatExporter, MarkdownFileSaver |

Assimilated: reference/assimilated/SOMOGYIJANOS-CURSOR-CHAT-EXPORT.yml.

### CursorLens (HamedMP)

| Path | Purpose |
|------|---------|
| `src/app/[...openai]/route.ts` | Catch-all POST chat/completions; getDefaultConfiguration; insertLog; forward to provider |
| `prisma/schema.prisma` | Log (method, url, headers, body, response, metadata), AIConfiguration, ModelCost |
| `src/types/logs.ts` | LogMetadata (tokens, cost), RequestBody, ResponseData |
| `src/lib/db.ts` | getDefaultConfiguration, insertLog |

Proxy only; no Cursor SQLite. Assimilated: reference/assimilated/HAMEDMP-CURSORLENS.yml.

### Cursor-history-MCP (markelaugust74)

| Path | Purpose |
|------|---------|
| `cursor_history_extractor.py` | workspaceStorage scan; ItemTable aiService.prompts; Ollama nomic-embed-text; LanceDB (vector, text, source_db, role) |
| `main.py` | FastAPI startup (Ollama + LanceDB); POST /search_chat_history, GET /health |

Assimilated: reference/assimilated/MARKELAUGUST74-CURSOR-HISTORY-MCP.yml.

### tensorzero (Cursor example)

| Path | Purpose |
|------|---------|
| `examples/integrations/cursor/feedback/src/cursor.rs` | Parse Cursor inference output (Ask vs Edit); system-message routing; code block regex ```lang:path; post-inference parsing, not proxy |

Assimilated: reference/assimilated/TENSORZERO-CURSOR-LLM-CLIENT.yml (blog + deep_dive_repo).
