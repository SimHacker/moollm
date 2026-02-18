# External sources: Cursor SQLite and transcript

Community and third-party work on Cursor’s internal SQLite, chat storage, and transcript format. You’re not the only one; these are the main places that document or tool it.

Ordered by richness/relevance: IDEAS-TODO.yml. Assimilated knowledge: reference/assimilated/. **Full comparison (prioritized list, relation to MOOLLM/MOCO, same/different, what's next):** [reference/EXTERNAL-PROJECTS-COMPARISON.md](EXTERNAL-PROJECTS-COMPARISON.md). Two-stage process (per-source import → universal synthesis): designs/ASSIMILATION-PROCESS.md. Reverse-engineered artifacts (from Cursor and from projects, big-endian named, with attribution): designs/REVERSE-ENGINEERED-DIR.md; live dir .moollm/skills/cursor-mirror/reverse-engineered/.

## Official caveat

Cursor Forum (Feb 2025): *“We cannot support 3rd party extensions, and the format and contents of Cursor and its databases is subject to change at any time.”* So treat all of the below as reverse‑engineered and fragile.

---

## Forums and support

**Assimilated** (all four threads below): [assimilated/CURSOR-FORUM-STATE-VSCDB.yml](assimilated/CURSOR-FORUM-STATE-VSCDB.yml)

- **Questions about state.vscdb**  
  https://forum.cursor.com/t/questions-about-state-vscdb/47299  
  Official answer: DB format/contents unsupported and subject to change.

- **How to get all chat history**  
  https://forum.cursor.com/t/how-to-get-all-chat-history/16117  
  Points to workspaceStorage and keys like `workbench.panel.aichat.view.aichat.chatdata`, `aiService.prompts`.

- **state.vscdb growing at 1 GB in a day**  
  https://forum.cursor.com/t/cursor-state-vscdb-growing-at-1-gb-in-a-day/151747  
  User reports on DB size; useful for understanding scale.

- **Fixing chat loading forever**  
  https://forum.cursor.com/t/fixing-chat-loading-forever-solved/150106  
  Workarounds involving backup/removal of corrupted state.vscdb.

**More forum threads and projects:** A broader harvest (export guides, path-based metadata, cursorDiskKV migration, recovery, extensions, people and GitHub) is in **reference/FORUM-HARVEST.md**. It lists additional threads (e.g. [Guide: 5 steps exporting chats](https://forum.cursor.com/t/guide-5-steps-exporting-chats-prompts-from-cursor/2825), [Where is all metadata stored?](https://forum.cursor.com/t/where-are-all-the-metadata-chat-composer-history-indexed-cached-data-workplace-settings-etc-stored/42699), [Small script export](https://forum.cursor.com/t/small-script-to-export-chat-history/35361)), projects (somogyijanos/cursor-chat-export, fankaidev gist, SpecStory, CursorLens, markelaugust74 Cursor-history-API, dav-ell Cursor Internals skill), and people/GitHub to check for assimilation candidates.

---

## SQLite: keys and structure

- **How Cursor Stores Its Command Allowlist in SQLite** (tarq.net) — **Assimilated**  
  https://tarq.net/posts/cursor-sqlite-command-allowlist/  
  ItemTable key `src.vs.platform.reactivestorage.browser.reactiveStorageServiceImpl.persistentStorage.applicationUser`; documents `composerState` (useYoloMode, yoloCommandAllowlist/Denylist, yoloPrompt, mcpAllowedTools, modes4, defaultMode2). Includes sqlite3 one‑liners to read/update. **ItemTable only**, not cursorDiskKV.  
  → [assimilated/TARQ-COMPOSER-STATE.yml](assimilated/TARQ-COMPOSER-STATE.yml)

- **Trying to change Cursor settings without clicking?** (Jack Youstra)  
  https://jackyoustra.com/blog/cursor-settings-location  
  state.vscdb locations (macOS/Windows/Linux), ItemTable as key‑value JSON store.

---

## GitHub: MCP and CLI tools

- **S2thend/cursor-history** (CLI + library) — **Assimilated**  
  https://github.com/S2thend/cursor-history  
  Node.js 20+; list sessions, show full conversations (user, assistant, tool, thinking, error), search, export Markdown/JSON, backup/restore, migrate. Reads workspace ItemTable (CHAT_DATA_KEYS priority: composer.composerData, workbench.panel.aichat..., aiService.prompts/generations) and global cursorDiskKV (bubbleId:*, composerData:*). Documents bubble type (1=user, 2=assistant), toolFormerData (name, params, result, rawArgs, status, additionalData), thinking.text; tool param key aliases per tool; legacy vs new composer format.  
  → [assimilated/S2THEND-CURSOR-HISTORY.yml](assimilated/S2THEND-CURSOR-HISTORY.yml)

- **jbdamask/cursor-db-mcp** — **Assimilated**  
  https://github.com/jbdamask/cursor-db-mcp  
  MCP server that queries Cursor’s SQLite. Uses **workspace** state.vscdb (ItemTable) for `composer.composerData`, `workbench.panel.aichat.view.aichat.chatdata`; **global** state.vscdb (cursorDiskKV) for `composerData:{composerId}`. Exposes `cursor://projects`, `cursor://projects/{name}/chat`, `cursor://projects/{name}/composers`, `cursor://composers/{id}` and a `query_table` tool for ItemTable/cursorDiskKV. Python, ~500 LOC. Note: “chats increasingly stored as composerData under globalStorage.”

- **everestmz/cursor-rpc** — **Assimilated**  
  https://github.com/everestmz/cursor-rpc  
  Reverse‑engineered Cursor **protobuf RPC** (from minified JS); programmatic access to Cursor backend services. State.vscdb path and ItemTable keys for auth (cursorAuth/accessToken, cursorAuth/refreshToken); API base api2.cursor.sh, repo42.cursor.sh; ClientSideToolV2/BuiltinTool enums; schema extraction from Cursor.app extensionHostProcess.js. Not SQLite bubbles—API layer.  
  → [assimilated/EVERESTMZ-CURSOR-RPC.yml](assimilated/EVERESTMZ-CURSOR-RPC.yml)

- **somogyijanos/cursor-chat-export** — **Assimilated**  
  https://github.com/somogyijanos/cursor-chat-export  
  Python CLI; workspaceStorage; ItemTable key workbench.panel.aichat.view.aichat.chatdata; tabs/bubbles; discover + export to Markdown.  
  → [assimilated/SOMOGYIJANOS-CURSOR-CHAT-EXPORT.yml](assimilated/SOMOGYIJANOS-CURSOR-CHAT-EXPORT.yml)

- **fankaidev (gist)**  
  https://gist.github.com/fankaidev/5a8d5385cebd9d130cc60ec427df17f7  
  Python script; reads **cursorDiskKV** (post-migration); globalStorage paths; export to md + JSON by timestamp.

- **SpecStory** (Han, forum)  
  https://docs.specstory.com/integrations/cursor  
  Cursor extension; auto-save chat/composer to `.specstory/history/`; share link; AI rules from history. Alternative to CLI export.

- **Cursor Internals Skill** (dav-ell/blink) — **Assimilated**  
  https://github.com/dav-ell/blink (.cursor/rules/skills/cursor-internals, cursor-db)  
  Auth (Auth0, api2.cursor.sh), 40+ models, JSON vs Protobuf; cursor-db: IDE globalStorage vs cursor-agent ~/.cursor/chats/store.db, composer/bubble 69+ fields.  
  → [assimilated/DAV-ELL-BLINK-CURSOR-SKILLS.yml](assimilated/DAV-ELL-BLINK-CURSOR-SKILLS.yml)

- **vltansky/cursor-chat-history-mcp** — **Assimilated**  
  https://github.com/vltansky/cursor-chat-history-mcp  
  TypeScript MCP server; 100% local SQLite. Links Cursor conversations to git commits; tools: get file context, find commit conversations, list conversation commits, list conversations (filters), full conversation content, search conversations, usage analytics (file activity, language stats). Separate SQLite for git links (app support dir).  
  → [assimilated/VLTANSKY-CURSOR-CHAT-HISTORY-MCP.yml](assimilated/VLTANSKY-CURSOR-CHAT-HISTORY-MCP.yml)

- **ton-ai-core/unlimite-context** — **Assimilated**  
  https://github.com/ton-ai-core/unlimite-context  
  TypeScript CLI + programmatic; auto-detects state.vscdb on Linux, macOS, Windows. Exports all chat history to `./cursor-composers` (one file per dialog); optional custom DB path and output dir. npx `@ton-ai-core/unlimite-context <project-identifier>`. Compare with S2thend, cursor-mirror export.  
  → [assimilated/TON-AI-CORE-UNLIMITE-CONTEXT.yml](assimilated/TON-AI-CORE-UNLIMITE-CONTEXT.yml)

- **fankaidev (gist)** — **Assimilated**  
  https://gist.github.com/fankaidev/5a8d5385cebd9d130cc60ec427df17f7  
  Python; `SELECT value FROM cursorDiskKV` (no key filter); globalStorage path (macOS); chat shape: name, createdAt, conversation[] (blocks with context.fileSelections, text). Export to md+json per chat.  
  → [assimilated/FANKAIDEV-CURSORDISKKV-EXPORT.yml](assimilated/FANKAIDEV-CURSORDISKKV-EXPORT.yml)

- **CursorLens** (HamedMP) — **Assimilated**  
  https://github.com/HamedMP/CursorLens  
  Next.js proxy; logs chat/completions to PostgreSQL (tokens, cost); forwards to OpenAI/Anthropic/etc. No Cursor SQLite.  
  → [assimilated/HAMEDMP-CURSORLENS.yml](assimilated/HAMEDMP-CURSORLENS.yml)

- **markelaugust74/Cursor-history-MCP** — **Assimilated**  
  https://github.com/markelaugust74/Cursor-history-MCP  
  WorkspaceStorage + ItemTable aiService.prompts; Ollama embeddings; LanceDB; FastAPI /search_chat_history.  
  → [assimilated/MARKELAUGUST74-CURSOR-HISTORY-MCP.yml](assimilated/MARKELAUGUST74-CURSOR-HISTORY-MCP.yml)

---

## Reverse‑engineering and analysis

- **Reverse Engineering Cursor’s LLM Client** (TensorZero) — **Assimilated**  
  https://tensorzero.com/blog/reverse-engineering-cursors-llm-client  
  Proxy between Cursor and LLMs; observes prompts and responses. Documents system/user prompt shape (~642 tokens), citation format (startLine:endLine:filepath), and “apply model” hierarchy. **Not** about local SQLite or transcripts.  
  → [assimilated/TENSORZERO-CURSOR-LLM-CLIENT.yml](assimilated/TENSORZERO-CURSOR-LLM-CLIENT.yml)

- **I Reverse-Engineered Cursor’s Context Management System** (Monish Gosar)  
  https://blog.gomonish.com/blog/reverse-engineering-cursor-context-management  
  Behavioral analysis: cursor locality, semantic retrieval, recency; how Cursor re-anchors context. No DB schema.

- **“Reversing” Cursor: Editing Notepads with SQLite** (Doug Silkstone, LinkedIn)  
  https://www.linkedin.com/pulse/editing-notepads-cursor-doug-silkstone-c0rhe  
  Short note on notepad storage and SQLite hacks.

---

## Recovery and export (user-facing)

- **Beginner’s Guide: Recover Missing Chat History in Cursor** (Dre Dyson)  
  https://dredyson.com/beginners-guide-how-to-recover-your-missing-chat-history-in-cursor-ide/  
  state.vscdb locations, chat-history.json, state.vscdb-wal; recovery steps.

- **Cursor Docs: Shared transcripts, export**  
  https://cursor.com/docs/shared-transcripts  
  https://docs.cursor.com/en/agent/chat/export  
  Official: shared read‑only links; export chat as Markdown. No spec for internal agent-transcripts `.txt` format.

---

## Transcript format (undocumented)

The plaintext **agent transcript** under `~/.cursor/projects/.../agent-transcripts/<composer>.txt` (e.g. `[Tool call] run_terminal_command_v2` plus indented `  key: value` lines, `[Tool result]`, `[Thinking]`) is **not** formally documented by Cursor. Current best source for its structure is this skill’s reference docs (TOOL-ARGS-MISSING, DATA-SCHEMAS context_assembly, CARD data_sources.dotcursor.agent_transcripts) and code that parses it (e.g. cursor_mirror.py). S2thend/cursor-history shows tool/thinking/output in its “show” output but reads from SQLite bubbles/agentKv, not necessarily the same as the `.txt` transcript file.

---

## Summary table

| Source | Focus | Tables/keys mentioned | Transcript |
|--------|--------|------------------------|------------|
| Cursor Forum | Policy, chat keys | ItemTable: workbench.panel.aichat, aiService.prompts | No |
| tarq.net | composerState, YOLO | ItemTable: reactiveStorage...applicationUser | No |
| jbdamask/cursor-db-mcp | Chat, composers | ItemTable + cursorDiskKV, composerData | No |
| S2thend/cursor-history | Sessions, tools, export | Reads SQLite (bubbles/agentKv implied) | No (uses DB) |
| everestmz/cursor-rpc | RPC, auth, API | ItemTable cursorAuth; api2.cursor.sh, repo42.cursor.sh | No |
| TensorZero | Prompt shape, apply model | None (proxy/LLM layer) | No |
| vltansky/cursor-chat-history-mcp | MCP: git-link, search, analytics | Cursor app DB + separate SQLite (git links) | No |
| ton-ai-core/unlimite-context | Export, auto-detect DB | state.vscdb (cross-platform paths) | No |
| fankaidev gist | cursorDiskKV export | globalStorage state.vscdb; value = chat blob | No |
| cursor-mirror (this skill) | Bubbles, tools, transcript merge | cursorDiskKV bubbleId/agentKv, KEY-CATALOG | Yes (agent-transcripts) |
| dav-ell/blink (skills) | Auth, API, IDE vs CLI DB | cursor-db: globalStorage/cursorDiskKV; cursor-agent store.db meta+blobs | No |
| somogyijanos/cursor-chat-export | Workspace export, discover | ItemTable workbench.panel.aichat (workspaceStorage) | No |
| HamedMP/CursorLens | Proxy log | PostgreSQL (not SQLite) | No |
| markelaugust74/Cursor-history-MCP | RAG search prompts | ItemTable aiService.prompts, LanceDB | No |

So: **SQLite** is covered by forum posts, tarq.net, cursor-db-mcp, and cursor-history; **transcript syntax** is only documented in this skill and in code that parses the `.txt` files.
