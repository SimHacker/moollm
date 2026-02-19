# Universal model: analysis and generation plan

Read-over of all reverse-engineered and assimilated files to find gaps, inconsistencies, parallels, trends, patterns, and categories; then a concrete plan to generate the universal virtual model (Stage 2).

**Inputs:** reference/assimilated/*.yml (14 files), KEY-CATALOG.yml, DATA-SCHEMAS.yml, BORG-COLLECTIVE-COOKBOOK.yml, designs (UNIVERSAL-MODEL-DESIGN.md, FORMAT-ENTOURAGE.md, DATA-LAYOUT.md), cursor-sqlite-model-schema.json.

**Target:** reference/universal/model/ (chunk dir) and CURSOR-SQLITE-MODEL.yml (assembled); format entourage (JSON, SQLite, CSV, TXT) as needed.

---

## 1. Gaps (missing or single-source coverage)

| Gap | Who covers it | Universal model action |
|-----|----------------|------------------------|
| **Agent-transcript format** (`.txt` under agent-transcripts/) | cursor-mirror only (CARD, TOOL-ARGS-MISSING, code). No external assimilated source. | Add `entities.agent_transcript` with schema (Tool call, Tool result, Thinking blocks); source = cursor-mirror skill. |
| **cursor-agent store.db** (CLI headless) | Blink cursor-db only. Path ~/.cursor/chats/<hash>/<id>/store.db; meta+blobs; schema "unknown". | Add `paths.cursor_agent` and `tables.store_db` with single source DAV-ELL-BLINK; note "schema not fully documented". |
| **Global vs workspace for prompts/generations** | DATA-SCHEMAS says aiService.prompts/generations in workspace; S2thend uses workspace ItemTable for session list, global for bubbles. Blink says "chat only in global" (bubbles). | Resolve: session list and aiService.prompts/generations can live in **workspace** ItemTable; **full bubble content** only in **global** cursorDiskKV. Document both; tag workspace keys with "session list / prompts cache". |
| **codeBlockPartialInlineDiffFates, inlineDiffUndoRedo** | KEY-CATALOG only (counts, pattern). No assimilated parser. | Include in keys.cursor_disk_kv with source KEY-CATALOG; no entity schema beyond pattern. |
| **messageRequestContext** value shape | KEY-CATALOG + DATA-SCHEMAS ref; no rich field list from code. | Keep pattern + schema_ref; sources KEY-CATALOG, DATA-SCHEMAS. |
| **Proxy / traffic layer** | TensorZero (blog + repo cursor.rs), CursorLens (Prisma). Not SQLite. | Universal model stays SQLite/transcript-focused. Add short `cross_refs.proxy_and_traffic` pointing to TENSORZERO-CURSOR-LLM-CLIENT, HAMEDMP-CURSORLENS for "what Cursor sends to LLM" and "how to log traffic". |
| **RAG / vector / git-link** | markelaugust74 (prompts only), vltansky (git-link DB). | Not part of core schema. cross_refs.rag_and_git_link → assimilated files. |

---

## 2. Inconsistencies (resolve or document)

| Inconsistency | Sources | Resolution |
|---------------|---------|------------|
| **"Chat only in globalStorage"** vs **workspace ItemTable has chat keys** | Blink: "workspace state.vscdb do NOT contain chat data." Somogyijanos, markelaugust74: read workspace ItemTable for workbench.panel.aichat, aiService.prompts. | **Resolve:** "Full chat content (bubbles) = global cursorDiskKV only. Session list and legacy/cache data (composer.composerData metadata, workbench.panel.aichat, aiService.prompts) can appear in **workspace** ItemTable; canonical session list and full messages come from global." State both in legacy_vs_new and paths. |
| **composer.composerData location** | S2thend: workspace ItemTable for composer.composerData (session list). jbdamask: same. Unlimite: ItemTable then cursorDiskKV for composerData:*. | **Resolve:** Session list = workspace ItemTable key composer.composerData (allComposers[]). Full composer blob per id = global cursorDiskKV composerData:{id}. No conflict. |
| **Bubble field list length** | DATA-SCHEMAS: many fields. Blink: "69+ fields". S2thend: type, text, codeBlocks, toolFormerData, thinking. | **Resolve:** One canonical entity.bubble with required/core vs optional; cite blink for "69+", DATA-SCHEMAS and S2THEND for core set. |
| **Tool param aliases** | S2thend has one list; BORG has slightly different wording. | Dedupe; use S2thend as primary (from code); add BORG as source. |

---

## 3. Parallels (same concept, different wording — unify)

| Concept | Parallels | Universal name / section |
|---------|------------|--------------------------|
| Session list keys | CHAT_DATA_KEYS (S2thend), workspace_chat_keys (BORG), keys_priority (KEY-CATALOG), get_composer_ids (jbdamask) | keys.workspace_itemtable.session_list_priority |
| Full session read | cursorDiskKV bubbleId:*, composerData:* (S2thend, vltansky, BORG); "full content from global" | sql.full_session, entities.bubble, entities.composer_meta |
| Composer state (YOLO, modes) | tarq composerState key; BORG composer_state_schema; KEY-CATALOG global_itemtable | keys.global_itemtable.composer_state, entities.composer_state |
| Discovery (workspace → project name) | jbdamask folder URI → project_name; S2thend workspace.json; BORG folder_uri_to_path | paths.workspace_json, paths.folder_uri_to_path, discovery.project_name_from_uri |
| extractBubbleText | S2thend parser/storage; BORG extract_bubble_text | algorithms.extract_bubble_text |
| Tool result parsing | S2thend result_parse; BORG tool_result_parse | entities.tool_result_parse |
| cursor:// and query_table | jbdamask only | mcp.resources, mcp.tools |

---

## 4. Trends (document in universal model)

| Trend | Evidence | Section |
|-------|----------|---------|
| **Migration: ItemTable → cursorDiskKV for chat** | Forum, fankaidev gist, S2thend (session list in ItemTable, bubbles in cursorDiskKV). | legacy_vs_new.migration |
| **Legacy keys still present** | workbench.panel.aichat, workbench.panel.chat; chatSessions/tabs in raw JSON. | legacy_vs_new.legacy_keys, keys.workspace_itemtable |
| **New format: composer.composerData + allComposers** | S2thend, jbdamask, unlimite-context, blink. | legacy_vs_new.new_primary |
| **Two storage systems: IDE vs cursor-agent** | Blink only. | paths.cursor_agent, tables.store_db |
| **Multi-source tracking** | ASSIMILATION-PROCESS: track siblings/forum to detect Cursor changes. | meta.track_sources (optional) |

---

## 5. Patterns (recurring structures)

| Pattern | Where | Use in universal model |
|---------|--------|-------------------------|
| **Key pattern** `{namespace}:{id}:{suffix}` | bubbleId:composerId:index; agentKv:composerId:toolCallId; messageRequestContext:composerId:requestId | keys.cursor_disk_kv.*.pattern |
| **Try keys in order** | CHAT_DATA_KEYS priority; workspace chat key fallback | keys.workspace_itemtable.session_list_priority (ordered list) |
| **Table check before cursorDiskKV** | S2thend, BORG sql_has_cursor_disk_kv | sql.table_check_cursor_disk_kv |
| **ORDER BY rowid** for message order | S2thend, BORG | sql.*.usage note |
| **folder URI → path** | file:// strip, %20 → space | paths.folder_uri_to_path |
| **Workspace = path-based** | workspaceStorage id ≠ project path; workspace.json has folder URI | paths.workspace_json, discovery |

---

## 6. Categories (sections of the universal model)

Aligned with UNIVERSAL-MODEL-DESIGN.md and DATA-LAYOUT.md:

| Category | Content | Primary sources |
|----------|---------|------------------|
| **meta** | version, updated, schema_version, sources_consumed | — |
| **sources** | List of { name, url, assimilated_into } for every source used | All assimilated + KEY-CATALOG, DATA-SCHEMAS, BORG |
| **paths** | darwin/win32/linux base, global_db, workspace_storage, workspace_db, workspace_json, folder_uri_to_path; cursor_agent (store.db) | BORG, S2thend, jbdamask, blink |
| **tables** | ItemTable, cursorDiskKV (schema, where); store_db (cursor-agent, minimal) | BORG, KEY-CATALOG, blink |
| **keys** | workspace_itemtable (session_list_priority, prompts, generations); global_itemtable (composer_state_key, auth, notable); cursor_disk_kv_catalog (all KEY-CATALOG patterns with counts/percent) | KEY-CATALOG, BORG, S2thend, tarq, jbdamask |
| **entities** | bubble (core + optional fields, type 1/2); composer_meta; composer_state; tool_result_parse; tool_param_aliases; agent_transcript (cursor-mirror) | DATA-SCHEMAS, S2thend, BORG, blink |
| **algorithms** | extract_bubble_text; tool result parsing (terminal, read_file, edit_write, error) | S2thend, BORG |
| **sql** | list_sessions_workspace, full_session, list_composers_global, composer_state, table_check, agent_kv_for_composer, search_keys_prefix, list_itemtable_keys, count_bubbles | BORG, S2thend, jbdamask |
| **legacy_vs_new** | new_primary, legacy_keys, migration (ItemTable→cursorDiskKV), raw_session vs composer_head | BORG, S2thend, fankaidev, Forum |
| **mcp** | cursor:// resources, query_table signature, workspace_chat_key | jbdamask |
| **discovery** | list_workspaces, project_name_from_uri | jbdamask, BORG |
| **cross_refs** | KEY-CATALOG, DATA-SCHEMAS, assimilated files; proxy/traffic (TensorZero, CursorLens); RAG/git (markelaugust74, vltansky) | — |

---

## 7. Source → section mapping (attribution)

| Section | Sources to cite |
|---------|-----------------|
| paths | BORG, S2THEND (storage.ts getGlobalStoragePath), JBDAMASK (get_default_cursor_path), DAV-ELL (cursor-db paths), KEY-CATALOG |
| tables | BORG, KEY-CATALOG (cursorDiskKV counts), DAV-ELL (store.db) |
| keys.workspace_itemtable | S2THEND (CHAT_DATA_KEYS, PROMPTS_KEY, GENERATIONS_KEY), KEY-CATALOG, JBDAMASK, SOMOGYIJANOS (aichat_query), MARKELAUGUST74 (aiService.prompts) |
| keys.global_itemtable | TARQ (composer_state key), KEY-CATALOG (auth, feature, memories, etc.) |
| keys.cursor_disk_kv | KEY-CATALOG (full catalog), BORG, S2THEND, VLTANSKY, TON-AI-CORE |
| entities.bubble | DATA-SCHEMAS, S2THEND, BORG, DAV-ELL (69+), TON-AI-CORE (Bubble interface) |
| entities.composer_meta | BORG, S2THEND, DATA-SCHEMAS |
| entities.composer_state | TARQ, BORG |
| entities.tool_result_parse, tool_param_aliases | S2THEND, BORG |
| entities.agent_transcript | cursor-mirror (TOOL-ARGS-MISSING, CARD) — skill itself |
| sql.* | BORG (primary), S2THEND (exact queries from storage.ts), JBDAMASK (execute_query semantics) |
| legacy_vs_new | BORG, S2THEND, CURSOR-FORUM, FANKAIDEV |
| mcp | JBDAMASK |
| discovery | JBDAMASK, BORG |

---

## 8. Generation plan (step-by-step)

### Phase 1: Chunk dir as source of truth

1. **Create directory** `reference/universal/model/` with subdirs: `keys/`, `entities/`, `sql/`.
2. **sources.yml** — Build list from all assimilated files + KEY-CATALOG, DATA-SCHEMAS, BORG. Each entry: name, url (or path), assimilated_into (file path).
3. **meta.yml** — version (e.g. 1.0), updated (date), schema_version (e.g. 2026-02), sources_consumed (list of filenames).
4. **paths.yml** — Merge BORG paths + S2thend/JBDAMASK/DAV-ELL; add cursor_agent from blink; tag each line with source.
5. **tables.yml** — ItemTable, cursorDiskKV from BORG/KEY-CATALOG; store_db from blink (minimal).
6. **keys/workspace-itemtable.yml** — Session list priority, prompts, generations; sources S2THEND, KEY-CATALOG, SOMOGYIJANOS, MARKELAUGUST74.
7. **keys/global-itemtable.yml** — Composer state key (tarq), auth, notable from KEY-CATALOG.
8. **keys/cursor-disk-kv.yml** — Full catalog from KEY-CATALOG (pattern, count, percent, note); add sources KEY-CATALOG, BORG.
9. **entities/bubble.yml** — Core fields from DATA-SCHEMAS + S2THEND + blink 69+ note; type 1/2; sources.
10. **entities/composer-meta.yml** — From BORG, DATA-SCHEMAS.
11. **entities/composer-state.yml** — From TARQ, BORG.
12. **entities/tool-result-parse.yml** — From S2THEND, BORG.
13. **entities/tool-param-aliases.yml** — From S2THEND, BORG.
14. **entities/agent-transcript.yml** — Schema from cursor-mirror docs; source = cursor-mirror skill.
15. **algorithms/extract-bubble-text.yml** — From S2THEND, BORG.
16. **sql/** — One file per BORG snippet: list-sessions-workspace.sql, full-session.sql, list-composers-global.sql, composer-state.sql, table-check-cursor-disk-kv.sql, agent-kv-for-composer.sql, search-keys-prefix.sql, list-itemtable-keys.sql, count-bubbles.sql. Each file: optional `-- id:`, `-- usage:`, `-- sources:` header; then SQL body.
17. **legacy-vs-new.yml** — New primary, legacy keys, migration; sources BORG, S2THEND, Forum, FANKAIDEV.
18. **mcp.yml** — cursor:// resources, query_table; source JBDAMASK.
19. **discovery.yml** — list_workspaces, project_name_from_uri, folder_uri_to_path; sources JBDAMASK, BORG.
20. **cross-refs.yml** — Pointers to KEY-CATALOG, DATA-SCHEMAS, assimilated/*; proxy (TensorZero, CursorLens); RAG/git (markelaugust74, vltansky).

### Phase 2: Resolve and tag

21. **Resolve workspace vs global** — In paths and keys, add one short "authoritative note" block: full bubbles only in global cursorDiskKV; session list and prompts/generations (and legacy panel state) in workspace ItemTable where present.
22. **Attribution pass** — Every key, entity, and sql chunk has a `sources:` list (or inline comment). No unsourced fact.
23. **Validation** — Run schema validation (cursor-sqlite-model-schema.json) against assembled model; fix any missing required or malformed fields.

### Phase 3: Assemble and export

24. **Assemble** — From model/ (chunk dir) → single CURSOR-SQLITE-MODEL.yml. Preserve YAML Jazz (comments) from chunk files or inject from a template.
25. **Export** — Generate CURSOR-SQLITE-MODEL.json (strip comments); optionally cursor-sqlite-catalog.db, csv/*, *.txt per FORMAT-ENTOURAGE.md.
26. **GLANCE/INDEX** — Optional: add model/GLANCE.yml or INDEX.yml listing chunk names and one-line descriptions for context assembler.

### Phase 4: BORG and docs

27. **BORG** — Either (a) keep BORG as quick-ref extract and add a note "Full model: universal/model/ and CURSOR-SQLITE-MODEL.yml", or (b) generate BORG from universal model (sql + key summary only).
28. **Update ASSIMILATION-PROCESS** — Stage 2 "Pipeline" step: point to this plan and to model/ as output.
29. **Update UNIVERSAL-MODEL-DESIGN** — Add "See UNIVERSAL-MODEL-PLAN.md for gaps, inconsistencies, and generation steps."

---

## 9. Order of work (recommended)

1. sources.yml + meta.yml (so every other chunk can reference source names).
2. paths.yml, tables.yml (foundation).
3. keys/* (workspace, global, cursor_disk_kv) — largest merge from KEY-CATALOG + BORG.
4. entities/* (bubble, composer_meta, composer_state, tool_result_parse, tool_param_aliases, agent_transcript).
5. algorithms/extract-bubble-text.yml.
6. sql/* (copy from BORG, add -- sources).
7. legacy-vs-new.yml, mcp.yml, discovery.yml, cross-refs.yml.
8. Resolve workspace/global in paths + keys; attribution pass.
9. Validate; assemble; export.
10. BORG note + doc updates.

---

## 10. Summary

- **Gaps:** agent_transcript, cursor-agent store.db, proxy/RAG as cross-refs only; workspace vs global clarified.
- **Inconsistencies:** workspace vs global resolved by stating "full content = global; session list and prompts/cache = workspace where present."
- **Parallels:** Unified names for session list keys, full session read, composer state, discovery, extractBubbleText, tool parsing.
- **Trends:** Migration ItemTable→cursorDiskKV, legacy keys, two storage systems (IDE vs CLI).
- **Patterns:** Key patterns, try-in-order, table check, ORDER BY rowid, folder URI.
- **Categories:** meta, sources, paths, tables, keys, entities, algorithms, sql, legacy_vs_new, mcp, discovery, cross_refs.
- **Plan:** Build chunk dir first (model/), then assemble to CURSOR-SQLITE-MODEL.yml, then export; attribution on every fact; optional BORG from model.
