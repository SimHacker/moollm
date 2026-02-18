# External projects: comparison, relation to us, and what's next

One document: prioritized list of external projects (Cursor SQLite/transcript/API/proxy ecosystem), how each relates to MOOLLM and MOOCO, what we have already assimilated, and what to analyze next. Use with EXTERNAL-SOURCES.md (inventory), SIBLING-REPOS.md (clone/mine), ASSIMILATION-PROCESS.md (Stage 1→2→3), and IDEAS-TODO.yml (ordered pipeline).

---

## Where we are: what we've already borged

**Assimilated:** 14 Stage 1 artifacts in `reference/assimilated/`. One is our own synthesis (BORG-COLLECTIVE-COOKBOOK); the rest are per-source YAMLs. Stage 2 (universal CURSOR-SQLITE-MODEL) is designed but not yet fully populated.

| # | Source | Assimilated file | Focus |
|---|--------|------------------|--------|
| 1 | S2thend/cursor-history | S2THEND-CURSOR-HISTORY.yml | Storage keys, CHAT_DATA_KEYS, parser, bubble schema, tool aliases, extractBubbleText |
| 2 | jbdamask/cursor-db-mcp | JBDAMASK-CURSOR-DB-MCP.yml | MCP: workspace discovery, query_table, cursor:// resources |
| 3 | tarq.net (blog) | TARQ-COMPOSER-STATE.yml | ItemTable composerState, YOLO/modes, sqlite3 one-liners |
| 4 | Cursor Forum (4 threads) | CURSOR-FORUM-STATE-VSCDB.yml | Official caveat, keys, paths, growth/recovery |
| 5 | TensorZero (blog) | TENSORZERO-CURSOR-LLM-CLIENT.yml | Prompt shape, apply-model hierarchy (proxy layer) |
| 6 | everestmz/cursor-rpc | EVERESTMZ-CURSOR-RPC.yml | Protobuf RPC, auth keys, API URLs, ClientSideToolV2 |
| 7 | somogyijanos/cursor-chat-export | SOMOGYIJANOS-CURSOR-CHAT-EXPORT.yml | Python CLI, workspace discovery, ItemTable aichat, Markdown export |
| 8 | fankaidev (gist) | FANKAIDEV-CURSORDISKKV-EXPORT.yml | cursorDiskKV whole-table, globalStorage, legacy chat shape |
| 9 | dav-ell/blink (skills) | DAV-ELL-BLINK-CURSOR-SKILLS.yml | Auth, 40+ models, IDE vs cursor-agent DB, composer/bubble 69+ fields |
| 10 | vltansky/cursor-chat-history-mcp | VLTANSKY-CURSOR-CHAT-HISTORY-MCP.yml | MCP: git-link commits↔chats, search, usage analytics |
| 11 | ton-ai-core/unlimite-context | TON-AI-CORE-UNLIMITE-CONTEXT.yml | TypeScript: auto-detect DB, composerData:*, cursor-composers export |
| 12 | HamedMP/CursorLens | HAMEDMP-CURSORLENS.yml | Next.js proxy: log chat/completions to PostgreSQL (tokens, cost) |
| 13 | markelaugust74/Cursor-history-MCP | MARKELAUGUST74-CURSOR-HISTORY-MCP.yml | FastAPI, Ollama embeddings, LanceDB RAG over aiService.prompts |
| — | cursor-mirror synthesis | BORG-COLLECTIVE-COOKBOOK.yml | Copy-paste SQL and key reference from multiple sources |

**Fed into:** KEY-CATALOG.yml, DATA-SCHEMAS.yml, TOOL-ARGS-MISSING, designs (MOOCO-INTEGRATION, ASSIMILATION-PROCESS), IDEAS-TODO ideas/protocols.

**Not yet done:** Stage 2 universal model (CURSOR-SQLITE-MODEL.yml) full synthesis; Stage 3 validation suite runs; a few HTTP-only sources (Monish, recovery guides, SpecStory) summarized but not deep-assimilated; TensorZero example repo not mined.

---

## Prioritized list: potential projects to analyze next

Ordered by value to cursor-mirror + MOOLLM + MOOCO: high (clone/deep-mine) → medium (HTTP or light clone) → lower (document only).

### Empirical measurement vs behavioral inference

**Cursor-mirror (and proxy/RPC) enable real measurement.** We have state.vscdb (bubbles, composerData, tool calls), agent-transcripts (tool args and results), and—with TensorZero/CursorLens-style proxy or cursor-rpc—we can observe what context was actually sent per request (prompt contents, cited files, token counts). That is reproducible, instrumented evidence.

**Behavioral-inference posts (e.g. Monish Gosar)** vary inputs (cursor position, selection, recency), ask questions, and infer a “context priority stack” from when Cursor’s answers change. No access to prompt dumps, no schema, no counts. “Strong, repeatable” is qualitative; it’s hypothesis-generating, not proof. Useful as a list of claims to *test* with mirror/proxy data, not as empirical truth.

### Tier 1 — High value (deep-mine or clone)

| Priority | Project | Why |
|----------|---------|-----|
| 1 | **TensorZero example repo** (cursor integration) | We have the blog (TENSORZERO-CURSOR-LLM-CLIENT); their GitHub has an example integration. Mine for actual proxy code, request/response shapes, and citation handling. Complements CursorLens (proxy) and MOOCO-in-the-middle. **Empirical:** proxy shows what actually went into each request. |
| 2 | **legel — Cursor chat export gist** | Export chat to .md from SQL; “context feed-back” use case. Small; different key/query pattern than fankaidev/somogyijanos. HTTP enough; add to EXTERNAL-SOURCES and optionally one-page assimilated note. |
| 3 | **Jack Youstra — Cursor settings location** | state.vscdb locations (macOS/Windows/Linux), ItemTable as key-value JSON. Short blog; cross-check paths with BORG and KEY-CATALOG. HTTP only. |
| 4 | **Doug Silkstone — Editing notepads with SQLite** | LinkedIn note on notepad storage and SQLite hacks. Niche but may reveal extra keys or tables. HTTP only. |

### Tier 2 — Medium value (document, optional clone)

| Priority | Project | Why |
|----------|---------|-----|
| 5 | **Monish Gosar — Cursor context management** | Blog: black-box behavioral inference (cursor locality, recency, selection override). **Not empirical:** no prompt dumps, no instrumentation; infers “context priority stack” from when answers change. Use as **hypotheses to test** with cursor-mirror + proxy (what actually went into context). HTTP only. |
| 6 | **SpecStory** | Cursor extension; auto-save to .specstory/history/; share link; AI rules from history. Different UX (in-IDE vs CLI). Document as alternative; .specstory path convention for MOOCO export alignment. HTTP only (docs + marketplace). |
| 7 | **Recovery guides (Dre Dyson, Cursor docs)** | state.vscdb paths, chat-history.json, state.vscdb-wal, recovery steps, official export/shared transcripts. User-facing; cursor-mirror recovery/orphan docs can cite. HTTP only. |
| 8 | **cursordocs.com — export tutorial** | How to export Cursor chat history (2025); mentions cursor-chat-export, unlimite-context, SpecStory. Single reference for “what users read.” HTTP only. |

### Tier 3 — Lower priority (when filling gaps)

| Priority | Project | Why |
|----------|---------|-----|
| 9 | **Han / sheikheddy — Forum export guide** | Classic Datasette + ItemTable query; 22k views. Already covered by Forum harvest; optional one-pager “community export patterns.” |
| 10 | **Other forum threads** (metadata storage, rich export, Docker/remote) | FORUM-HARVEST.md lists them. Assimilate as needed when building orphan cleanup, rich export, or remote-path features. |

---

## Per-project comparison: description, relation, same/different, benefits, unique, notes

### Already assimilated (brief)

- **S2thend/cursor-history** — TypeScript CLI + library; list/show/export; workspace ItemTable + global cursorDiskKV; bubble types, toolFormerData, thinking; tool param aliases; backup. **Same:** We both read Cursor SQLite and export. **Different:** They focus on Node/TS and user-facing CLI; we add Python, agent-transcripts, KEY-CATALOG, universal model, MOOCO. **MOOLLM/MOCO benefit:** Canonical key order (CHAT_DATA_KEYS), extractBubbleText algorithm, MessageType enum; BORG and DATA-SCHEMAS cite them. **Unique:** Most complete public bubble/session schema and parsing in one codebase.
- **jbdamask/cursor-db-mcp** — Python MCP; query_table(ItemTable|cursorDiskKV); cursor://projects|chat|composers. **Same:** Same DB, same keys. **Different:** MCP server vs our CLI + reference docs. **Benefit:** MCP surface for “query Cursor state” from another agent; MOOCO could expose or proxy. **Unique:** cursor:// URI scheme and workspace discovery via workspace.json.
- **tarq.net** — Single post: ItemTable key for composerState (reactiveStorage...applicationUser), YOLO allowlist/denylist, mcpAllowedTools, sqlite3 one-liners. **Same:** ItemTable. **Different:** Composer *settings* only, not chat bubbles. **Benefit:** BORG composer_state section; no-ai-slop / skill gating can use allowlist. **Unique:** Only public doc of that exact key and JSON paths.
- **Cursor Forum** — Official caveat (unsupported, subject to change); keys workbench.panel.aichat, aiService.prompts; growth, recovery threads. **Same:** Community dependency on same DB. **Different:** Policy and user reports, not code. **Benefit:** EXTERNAL-SOURCES caveat; robust_first; path-based orphan/recovery ideas. **Unique:** Only “official” stance on 3rd party use.
- **TensorZero** — Blog: proxy Cursor↔LLM; system/user prompt ~642 tokens; citation format startLine:endLine:filepath; apply-model hierarchy. **Same:** Interest in what Cursor sends to LLMs. **Different:** Traffic layer, not SQLite. **Benefit:** Prompt/context-assembly docs; MOOCO-in-the-middle can mirror this observation layer. **Unique:** Public prompt-structure breakdown.
- **everestmz/cursor-rpc** — Go + protobuf; IDE↔server RPC; auth from state.vscdb; api2.cursor.sh, repo42; ClientSideToolV2/BuiltinTool. **Same:** Same app, same auth store. **Different:** Protocol layer, not chat storage. **Benefit:** MOOCO-in-the-middle Act path (StreamChat, tools); KEY-CATALOG auth cross-check. **Unique:** Only reverse-engineered Cursor RPC proto we know of.
- **somogyijanos/cursor-chat-export** — Python; config.yml paths; workspace discovery; ItemTable workbench.panel.aichat; export to Markdown. **Same:** Read SQLite, export. **Different:** Workspace-only (legacy), no cursorDiskKV; archived. **Benefit:** Config paths and discover logic; completes “export trio” with S2thend + unlimite-context. **Unique:** Explicit multi-OS workspace paths in config.
- **fankaidev gist** — Python; SELECT value FROM cursorDiskKV (no key filter); globalStorage; chat shape name/createdAt/conversation[]. **Same:** cursorDiskKV. **Different:** Whole-table = one blob per chat; legacy/simple. **Benefit:** KEY-CATALOG “alternative key model”; migration story ItemTable→cursorDiskKV. **Unique:** Minimal cursorDiskKV-only reader.
- **dav-ell/blink (Cursor skills)** — cursor-internals (Auth, 40+ models, API), cursor-db (IDE globalStorage vs cursor-agent store.db, composer _v:10, bubble _v:3, 69+ fields). **Same:** Reverse-engineered Cursor internals. **Different:** Skill docs only, no code that reads DB. **Benefit:** Authoritative IDE vs CLI and bubble schema; universal model can cite. **Unique:** Single installable “Cursor internals” skill; store.db meta+blobs.
- **vltansky/cursor-chat-history-mcp** — TypeScript MCP; 100% local; link conversations to git commits; list/search conversations; full content; usage analytics (file activity, language). **Same:** Read Cursor SQLite. **Different:** Separate SQLite for git links; MCP tools for commit↔conversation. **Benefit:** MOOCO can expose “conversations for this commit” as K-line; play-learn-lift from discussions. **Unique:** Only project tying Cursor chats to git commits and analytics.
- **ton-ai-core/unlimite-context** — TypeScript; auto-detect state.vscdb (Linux/macOS/Win + cursor-dev); composerData:*; export to cursor-composers/ (main + details). **Same:** Same keys, export. **Different:** Project filter by identifier; one file per dialog; no agent-transcripts. **Benefit:** Cross-platform path logic; cursor-composers convention; FullConversationLog/Bubble/CodeBlockDetails. **Unique:** npx one-liner, all-OS path detection.
- **HamedMP/CursorLens** — Next.js proxy; catch-all chat/completions; log to PostgreSQL (method, url, body, response, tokens, cost); forward to OpenAI/Anthropic. **Same:** Observe Cursor↔LLM. **Different:** No Cursor SQLite; proxy in front. **Benefit:** MOOCO-in-the-middle Record: same idea (log stream); we add state.vscdb for full picture. **Unique:** Production proxy + Prisma schema for cost/tokens.
- **markelaugust74/Cursor-history-MCP** — Python; workspaceStorage scan; ItemTable aiService.prompts (list of {text}); Ollama nomic-embed-text; LanceDB; FastAPI /search_chat_history. **Same:** Read Cursor state. **Different:** Prompts only (no full bubbles); vectorize + RAG. **Benefit:** “Chat as vectors” pattern; MOOCO could add semantic search over mirror data (pgvector). **Unique:** Minimal RAG-over-prompts pipeline.

### Not yet assimilated (prioritized)

- **Monish Gosar — Cursor context management** — Blog ([reverse-engineering Cursor context management](https://blog.gomonish.com/blog/reverse-engineering-cursor-context-management)): black-box experiments (vary cursor position, selection, file recency; ask questions; infer “context priority stack” from when Cursor’s answers change). **Not empirical:** no instrumentation, no prompt dumps, no measurement of what actually went into context; “strong, repeatable” is qualitative. **Relation:** Hypotheses about locality, recency, selection override—testable with cursor-mirror + proxy. **Different:** We can measure (bubbles, transcripts, and with proxy the actual request payload); he infers from outputs only. **Benefit:** Use his reconstructed stack as a checklist to validate or refute with real data. **Note:** Document as “behavioral-inference / hypothesis-generating”; priority for assimilation is low compared to sources that give us schema or instrumentation.
- **TensorZero example repo** — Code for Cursor integration (proxy). **Relation:** Implements what the blog describes. **Same:** Proxy observation. **Different:** We have cursor-mirror (DB + transcript) and MOOCO (orchestrator); they do proxy only. **Benefit:** Concrete request/response shapes; MOOCO-in-the-middle Watch can align. **Unique:** Example code for Cursor proxy. **Note:** Clone optional; mine for schema and citation handling.
- **legel gist** — Export chat to .md from SQL; context feed-back. **Relation:** Another export + “use context elsewhere.” **Same:** Export, SQL. **Different:** Unknown key set; small. **Benefit:** Extra key/query idea; user story “feed back into context.” **Note:** Short assimilated note or row in EXTERNAL-SOURCES.
- **Jack Youstra** — state.vscdb locations, ItemTable key-value. **Relation:** Paths and high-level structure. **Same:** Paths. **Different:** No key catalog. **Benefit:** Cross-check BORG paths (macOS/Windows/Linux). **Note:** One-page or BORG footnote.
- **SpecStory** — Extension; .specstory/history/; share link; AI rules from history. **Relation:** Alternative to CLI export; in-IDE. **Same:** Persist chat/composer. **Different:** Extension vs our CLI/skill; different path. **Benefit:** Document .specstory convention; MOOCO export could offer compatible layout. **Unique:** Only Cursor extension we list for “save history.”
- **Recovery guides** — Paths, WAL, recovery, official export. **Relation:** User-facing recovery and official export. **Same:** state.vscdb. **Different:** How-to, not schema. **Benefit:** cursor-mirror recovery/orphan docs; cite official export. **Note:** Section in EXTERNAL-SOURCES or recovery doc.

---

## Same vs different (across all)

**Same across ecosystem:** Cursor’s state.vscdb (workspace + global); ItemTable and cursorDiskKV; composer/composerData/bubbles; migration trend toward cursorDiskKV for full content; need to handle Cursor format changes.

**Different:**  
- **Data source:** SQLite (most) vs proxy/traffic (TensorZero, CursorLens).  
- **Output:** CLI export (S2thend, somogyijanos, unlimite-context, fankaidev), MCP (jbdamask, vltansky, markelaugust74), extension (SpecStory), proxy log (CursorLens), skill docs (dav-ell).  
- **Scope:** Full bubbles (S2thend, vltansky, unlimite-context) vs prompts only (markelaugust74) vs settings (tarq) vs auth/API (everestmz, dav-ell).  
- **Stack:** TypeScript (S2thend, vltansky, unlimite-context, CursorLens), Python (jbdamask, somogyijanos, fankaidev, markelaugust74), Go (everestmz), docs only (tarq, Forum, dav-ell, TensorZero blog).

**Where we sit:** cursor-mirror is the only one that (1) merges agent-transcripts (.txt) with SQLite bubbles, (2) maintains KEY-CATALOG + BORG + universal model with attribution, (3) feeds MOOLLM skills and MOOCO (context, K-lines, in-the-middle). We assimilate others into that model; we don’t replace their tools—we cite them and interoperate (e.g. MCPs, export conventions).

---

## How MOOLLM and MOOCO benefit and learn

- **MOOLLM:** Assimilated data backs KEY-CATALOG, DATA-SCHEMAS, BORG, and (when done) universal model. Skills (cursor-mirror, bootstrap, k-lines) and INDEX/hot/working-set use this for “what Cursor stores and where.” Ideas (play-learn-lift, path-based recovery, export conventions) come from Forum and projects. no-ai-slop / robust_first get “official caveat” and migration story.
- **MOOCO:** Watch = cursor-mirror + state.vscdb (bubbles, thinking, tools). Act = cursor-rpc + same auth (StreamChat, ClientSideToolV2). Record = PostgreSQL (time-series + pgvector); CursorLens-style logging plus our DB+transcript. Assimilated sources inform: which keys to read, which MCPs to expose (jbdamask, vltansky), how to align proxy behavior (TensorZero, CursorLens), and how to add RAG/semantic (markelaugust74) or git-link (vltansky) as K-lines.
- **Learning:** S2thend = bubble parsing and tool aliases. vltansky = git-link and analytics. everestmz = RPC for Act. dav-ell = IDE vs CLI and bubble schema. markelaugust74 = vectorize prompts. CursorLens = proxy log schema. TensorZero = prompt shape (proxy = empirical). Monish = hypotheses about context hierarchy (behavioral inference only; we can test with mirror + proxy). Each fills a different slice; we synthesize and attribute.

---

## What’s next (concrete)

1. **Stage 2:** Run synthesis from all assimilated YAMLs + KEY-CATALOG + DATA-SCHEMAS → CURSOR-SQLITE-MODEL.yml (and format entourage). Attribution in core; YAML Jazz.
2. **Stage 3:** Run validation suite (skill-test/cursor-mirror); verify against live DBs; play-learn-lift; track siblings for Cursor changes.
3. **Tier 1 pending:** Mine TensorZero example repo for proxy code (empirical context capture); add legel, Jack Youstra, Doug Silkstone as short notes or EXTERNAL-SOURCES rows. Optionally document Monish as “hypotheses to test” (low priority; his post is inference, not measurement).
4. **Tier 2:** Document SpecStory (convention + alternative); recovery guides (cite in cursor-mirror recovery); cursordocs.com (reference).
5. **MOOCO:** Use this doc and assimilated files when designing MOOCO-in-the-middle Watch/Act/Record and when exposing MCP or proxy layers.

Cross-references: EXTERNAL-SOURCES.md, SIBLING-REPOS.md, IDEAS-TODO.yml, ASSIMILATION-PROCESS.md, FORUM-HARVEST.md, PENDING-SOURCES-CLONE-VS-HTTP.md, designs/MOOCO-INTEGRATION.md.
