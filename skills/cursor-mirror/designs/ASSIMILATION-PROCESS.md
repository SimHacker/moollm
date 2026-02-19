# Assimilation process (Stage 1 -> 2 -> 3)

How we turn external Cursor SQLite/transcript sources into a single, evidentially sourced, universal model. **Stage 1:** per-source import. **Stage 2:** synthesis into universal model. **Stage 3:** validate, verify, test, play, learn, lift, evolve. Iterate and improve incrementally. Track Cursor's inevitable evolutionary changes.

**Attribution is built into the core:** every claim in the universal model traces to at least one source (assimilated file, KEY-CATALOG, or DATA-SCHEMAS). The model and its format entourage carry `sources` and per-item `source`/`sources` so we can always cite who said what. No unsourced facts; attribution is not an afterthought--it is part of the schema.

**Reverse-engineered dir:** All reverse-engineered artifacts (from Cursor executables/dirs and from external projects, by project name) live in one place: `.moollm/skills/cursor-mirror/reverse-engineered/`. Big-endian named YAML (YYYYMMDD or YYYYMMDD-HHMMSS + description); shared metadata core (source, created, last_updated, attribution, hand_edit_annotations); beyond that, project-specific YAML-Jazz. See **designs/REVERSE-ENGINEERED-DIR.md** and **reference/reverse-engineered/README.md**.

---

## Stage 1: Per-source import (assimilated/*.yml)

**Goal:** Pull information from each external source into **one YAML file per project**. Document what we learned **in their terms**--preserve their vocabulary, structure, and findings. No deduping across sources yet.

**Outputs:** `reference/assimilated/<SOURCE>.yml`

**Rules:**
- One deep-dive per source; harvest into that source's file only.
- Keep their naming (e.g. "composerData", "cursorDiskKV", "toolFormerData").
- Quote or paraphrase their docs/code; note file/line or URL where possible.
- Include: keys, key patterns, schemas, SQL snippets, algorithms (e.g. extractBubbleText), and cross-refs to their repo paths (see SIBLING-REPOS.md).
- Meta block: source URL, assimilated date, cursor_mirror_use (how we use it).
- **Integration / interpolation:** Document which parts are **relevant to cursor-mirror** and **MOOLLM**, and where they plug in. Each assimilated file should include:
  - **cursor_mirror_integration** -- Which reference docs (KEY-CATALOG, DATA-SCHEMAS, TOOL-ARGS-MISSING, BORG-COLLECTIVE-COOKBOOK), which script paths (cursor_mirror.py, commands), and which features (e.g. terminal-commands, dubble, list/show) consume or cross-check this source. Interpolation points: keys we read, schemas we validate against, SQL we might run.
  - **moollm_interpolation** -- How MOOLLM uses it: cursor-mirror skill (CARD, SKILL, GLANCE), bootstrap/working-set, hot.yml, INDEX, k-lines, or other skills that reference this data. E.g. "cursor-mirror CARD data_sources cites KEY-CATALOG; universal model chunk dir feeds context assembler."
  - **mooco_interpolation** (optional) -- How **MOOCO** (custom orchestrator) can turbocharge MOOLLM by directly supporting skills: precise context management, k-line diffusion, advanced orchestration (tick, magic dictionary, context paging, skill containment). Assimilated data can feed what MOOCO injects per skill or expose as MOOCO-readable state. See designs/MOOCO-INTEGRATION.md; example in S2THEND-CURSOR-HISTORY.yml.

**Current Stage 1 files:** (each includes `cursor_mirror_integration` and `moollm_interpolation` sections). **Tell me more:** local file, sibling dir (if any), source URL, key file (if repo).

- **S2THEND-CURSOR-HISTORY** -- TypeScript: storage, parser, types, bubble schema, tool aliases. Integration: KEY-CATALOG, DATA-SCHEMAS, cursor_mirror.py; MOOLLM cursor-mirror skill, universal model, k-lines.  
  -> File: `reference/assimilated/S2THEND-CURSOR-HISTORY.yml`  
  -> Sibling dir: `../cursor-history` (see SIBLING-REPOS.md)  
  -> URL: https://github.com/S2thend/cursor-history  
  -> Key files: `src/core/storage.ts`, `src/core/parser.ts`, `src/core/types.ts`

- **JBDAMASK-CURSOR-DB-MCP** -- Python MCP: workspace discovery, query_table, cursor:// resources. Integration: BORG mcp_quick_ref; MOOLLM sibling mining, MCP interop.  
  -> File: `reference/assimilated/JBDAMASK-CURSOR-DB-MCP.yml`  
  -> Sibling dir: `../cursor-db-mcp`  
  -> URL: https://github.com/jbdamask/cursor-db-mcp  
  -> Key file: `cursor-db-mcp-server.py`

- **TARQ-COMPOSER-STATE** -- Blog: ItemTable key for composerState, JSON paths, sqlite3 one-liners. Integration: BORG composer_state; MOOLLM universal model entities, no_ai_slop.  
  -> File: `reference/assimilated/TARQ-COMPOSER-STATE.yml`  
  -> URL: https://tarq.net/posts/cursor-sqlite-command-allowlist/  
  -> No sibling repo (blog only).

- **CURSOR-FORUM-STATE-VSCDB** -- Forum: official caveat, community keys/paths, growth/troubleshooting. Integration: EXTERNAL-SOURCES caveat; MOOLLM robust_first, claim confirmation.  
  -> File: `reference/assimilated/CURSOR-FORUM-STATE-VSCDB.yml`  
  -> URLs: https://forum.cursor.com/t/questions-about-state-vscdb/47299 , https://forum.cursor.com/t/how-to-get-all-chat-history/16117 , https://forum.cursor.com/t/cursor-state-vscdb-growing-at-1-gb-in-a-day/151747 , https://forum.cursor.com/t/fixing-chat-loading-forever-solved/150106  
  -> No sibling repo (forum only).

- **TENSORZERO-CURSOR-LLM-CLIENT** -- Blog: proxy observation of Cursor↔LLM; system/user prompt shape, apply-model hierarchy, citation format. Integration: prompt/context-assembly docs; MOOLLM no_ai_slop (cite as evidence).  
  -> File: `reference/assimilated/TENSORZERO-CURSOR-LLM-CLIENT.yml`  
  -> URL: https://tensorzero.com/blog/reverse-engineering-cursors-llm-client  
  -> Example repo: https://github.com/tensorzero/tensorzero/tree/main/examples/integrations/cursor  
  -> No sibling repo (blog + example only).

- **EVERESTMZ-CURSOR-RPC** -- Go + protos: state.vscdb path, ItemTable auth keys, API URLs, ClientSideToolV2/BuiltinTool enums, schema extraction from Cursor.app. Integration: KEY-CATALOG auth cross-check; MOOLLM sibling tracking (RPC layer).  
  -> File: `reference/assimilated/EVERESTMZ-CURSOR-RPC.yml`  
  -> Sibling dir: `../cursor-rpc` (see SIBLING-REPOS.md)  
  -> URL: https://github.com/everestmz/cursor-rpc ; author post: https://ev.dev/posts/reverse-engineering-cursor  
  -> Key files: `client.go`, `cursor/aiserver/v1/aiserver.proto`, `cmd/extract/main.go`, `cursor_version.txt`

- **VLTANSKY-CURSOR-CHAT-HISTORY-MCP** -- TypeScript MCP: 100% local SQLite. Links Cursor conversations to git commits; tools: file context, find commit conversations, list conversation commits, link conversation to commit, list/search conversations, usage analytics (file activity, language). Integration: BORG/KEY-CATALOG cross-check; complements jbdamask (raw query) with git-link and analytics layer.  
  -> File: `reference/assimilated/VLTANSKY-CURSOR-CHAT-HISTORY-MCP.yml`  
  -> Sibling dir: `../cursor-chat-history-mcp` (see SIBLING-REPOS.md)  
  -> URL: https://github.com/vltansky/cursor-chat-history-mcp  
  -> Key files: `src/database/reader.ts`, `src/database/parser.ts`, `src/linker/links-database.ts`, `src/tools/conversation-tools.ts`.

- **FANKAIDEV-CURSORDISKKV-EXPORT** -- Gist: Python; SELECT value FROM cursorDiskKV (no key filter); globalStorage state.vscdb (macOS); chat shape name/createdAt/conversation[] (context.fileSelections, text). Export md+json per chat. Integration: KEY-CATALOG (alternative key model / legacy whole-row = chat); MOOLLM cursor-mirror EXTERNAL-SOURCES.  
  -> File: `reference/assimilated/FANKAIDEV-CURSORDISKKV-EXPORT.yml`  
  -> URL: https://gist.github.com/fankaidev/5a8d5385cebd9d130cc60ec427df17f7  
  -> No sibling (gist only).

- **TON-AI-CORE-UNLIMITE-CONTEXT** -- NPM @ton-ai-core/unlimite-context: TypeScript; composerData:* (ItemTable then cursorDiskKV); auto-detect state.vscdb (Linux/macOS/Win + cursor-dev fallback); project filter by identifier string; export to cursor-composers (main log + details subdir). FullConversationLog/Bubble/ToolCallData/CodeBlockDetails schema. Integration: KEY-CATALOG, S2THEND; MOOLLM EXTERNAL-SOURCES, SIBLING-REPOS.  
  -> File: `reference/assimilated/TON-AI-CORE-UNLIMITE-CONTEXT.yml`  
  -> Sibling dir: `../unlimite-context` (see SIBLING-REPOS.md)  
  -> URL: https://github.com/ton-ai-core/unlimite-context  
  -> Key files: `src/lib/logExtractor.ts`, `src/cli/index.ts`

- **DAV-ELL-BLINK-CURSOR-SKILLS** -- dav-ell/blink .cursor/rules/skills: cursor-internals (Auth, api2.cursor.sh, 40+ models, JSON vs Protobuf, DB quick ref), cursor-db (IDE globalStorage vs cursor-agent ~/.cursor/chats/store.db, cursorDiskKV/ItemTable, composer _v:10, bubble _v:3 69+ fields, store.db meta+blobs). Integration: KEY-CATALOG, universal model; authoritative doc for IDE vs CLI and bubble schema.  
  -> File: `reference/assimilated/DAV-ELL-BLINK-CURSOR-SKILLS.yml`  
  -> Sibling dir: `../blink`  
  -> URL: https://github.com/dav-ell/blink  
  -> Key files: `.cursor/rules/skills/cursor-internals/SKILL.mdc`, `.cursor/rules/skills/cursor-db/SKILL.mdc`

- **SOMOGYIJANOS-CURSOR-CHAT-EXPORT** -- Python CLI; workspaceStorage paths (config.yml); ItemTable key workbench.panel.aichat.view.aichat.chatdata; tabs/bubbles (user/ai, delegate/text/initText); discover + export to Markdown. Integration: KEY-CATALOG, CURSOR-FORUM; completes export-tool trio.  
  -> File: `reference/assimilated/SOMOGYIJANOS-CURSOR-CHAT-EXPORT.yml`  
  -> Sibling dir: `../cursor-chat-export`  
  -> URL: https://github.com/somogyijanos/cursor-chat-export  
  -> Key files: `config.yml`, `chat.py`, `src/vscdb.py`, `src/export.py`

- **HAMEDMP-CURSORLENS** -- Next.js proxy; catch-all chat/completions; logs to PostgreSQL (Log: method, url, headers, body, response, metadata tokens/cost); forwards to OpenAI/Anthropic/etc. No Cursor SQLite. Integration: EXTERNAL-SOURCES; proxy-based observation alternative.  
  -> File: `reference/assimilated/HAMEDMP-CURSORLENS.yml`  
  -> Sibling dir: `../CursorLens`  
  -> URL: https://github.com/HamedMP/CursorLens  
  -> Key files: `src/app/[...openai]/route.ts`, `prisma/schema.prisma`, `src/types/logs.ts`

- **MARKELAUGUST74-CURSOR-HISTORY-MCP** -- Python: workspaceStorage scan; ItemTable aiService.prompts (list of {text}); Ollama nomic-embed-text; LanceDB vector DB; FastAPI /search_chat_history, /health. Integration: KEY-CATALOG, SOMOGYIJANOS; RAG over prompts only.  
  -> File: `reference/assimilated/MARKELAUGUST74-CURSOR-HISTORY-MCP.yml`  
  -> Sibling dir: `../Cursor-history-MCP`  
  -> URL: https://github.com/markelaugust74/Cursor-history-MCP  
  -> Key files: `cursor_history_extractor.py`, `main.py`

**Pipeline:** Add new sources from EXTERNAL-SOURCES.md / IDEAS-TODO.yml -> deep-dive -> create new `assimilated/<SOURCE>.yml` (with cursor_mirror_integration + moollm_interpolation) -> update IDEAS-TODO status and assimilated_into.

---

## Stage 2: Universal model (synthesis)

**Goal:** Look at **all** assimilated files at once. Dedupe, cross-validate, cohere, and interpolate into one **comprehensive, well-factored, intricately accurate, evidentially sourced** model. Human-, LLM-, and machine-readable (Python/TS).

**Output:** `reference/universal/CURSOR-SQLITE-MODEL.yml` (or equivalent; see UNIVERSAL-MODEL-DESIGN.md). The model is also exported in a **format entourage** (JSON, JSONB, SQLite, CSV, TXT) for deterministic Python tooling--see reference/universal/FORMAT-ENTOURAGE.md and cursor-sqlite-model-schema.json.

**Rules:**
- **Attribution in the core** -- Every key, pattern, and schema fact traces to at least one assimilated source (evidence). The universal model and every export in the format entourage include a `sources` section and optional `source`/`sources` per key, entity, or SQL snippet. Who said what is first-class data, not a comment-only convention.
- Use **YAML Jazz**: block comments and end-of-line comments as semantic documentation of **origin** (e.g. `# S2thend storage.ts`) and **meaning** (e.g. `# 1=user, 2=assistant`).
- Factor by concept: paths, tables, keys (workspace ItemTable, global ItemTable, global cursorDiskKV), bubble schema, tool result parsing, composer metadata, composerState, message types, legacy vs new, MCP surface.
- Resolve conflicts by source priority or document alternatives with source tags.
- Include copy-paste SQL and code snippets where they are the canonical form.

**Inputs:** All `assimilated/*.yml` + KEY-CATALOG.yml + DATA-SCHEMAS.yml. Optional: BORG-COLLECTIVE-COOKBOOK.yml as a prior synthesis pass.

**Pipeline:** Run when we have enough Stage 1 files (or on demand). Diff against previous universal model to avoid regressions. Regenerate or patch; keep version and changelog in meta.

**Track Cursor changes by tracking sources (constitutional).** Run a pipeline that **discovers Cursor changes by tracking other projects**. Sibling repos, forum, and blogs track Cursor at **different rates**; we intentionally watch them to spot DB/API/format changes. Examples: `git pull` in `../cursor-history`, `../cursor-db-mcp`, `../cursor-rpc`; check forum for new threads or replies; check tarq.net or other posts for updates. When a source changes (e.g. cursor-history adapts to a new key), re-mine and update assimilated -> Stage 2/3. This is **by design**: we don't rely on Cursor changelogs alone; we use the ecosystem as a change-detection network.

---

## Stage 3: Validate -> evolve

**Goal:** Don't stop at synthesis. **Validate** (schema, required fields); **verify** (run SQL against real state.vscdb, compare keys); **test** (tools load/export/assemble/explode); **play** (explore, try queries, try commands); **learn** (what broke, what Cursor changed, what we got wrong); **lift** (share fixes, update assimilated refs, document patterns); **evolve** (patch universal model, add sources, refine integration points). Play--learn--lift style: explore -> notice patterns -> codify and share.

**Pipeline:** After Stage 2 (or after any assimilated update): validate model -> verify against live DBs if available -> test tooling -> play/learn from use -> lift improvements back into assimilated or universal -> evolve docs and model.

**Validation test suite:** Structure + optional live DB drift; run via **skill-test**. Full design and cursor-mirror layers: **skills/skill-test/designs/cursor-mirror/VALIDATION-SUITE.md**. Summary: **designs/VALIDATION-DESIGN.md**.

**Pipeline: track Cursor changes.** Periodically: pull sibling repos (see SIBLING-REPOS.md), check forum/blog; when sources change, re-mine and update assimilated files, then re-run Stage 2/3 as needed. Different sources track at different rates--intentionally, constitutionally.

---

## Iteration

- **Stage 1:** Continuously add and refine per-source YAMLs as we discover new projects or re-mine existing ones (e.g. cursor-history storage.ts for more helpers).
- **Stage 2:** Re-run synthesis after every few new or updated assimilated files; update universal model and comments so origin/meaning stay accurate.
- **Stage 3:** Validate, verify, test, play, learn, lift, evolve--close the loop so the model and tools stay accurate as Cursor changes and as we use them.
- **Track sources to discover Cursor changes:** Run pipeline (pull siblings, check forum/blog). Sources track at different rates; we discover Cursor changes by watching them. Constitutional.

This keeps a clear separation: first learn from each source on its own terms, then unify into one model we can trust and cite, then keep it alive through use, feedback, and **tracking other projects** for change detection. **Attribution** is built into that model: the core schema and all exports carry source provenance so we can always attribute claims to the right project, post, or file.
