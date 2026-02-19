# Universal model design (Stage 2 output)

**Purpose:** One canonical, evidentially sourced, human/LLM/machine-readable model of Cursor SQLite and transcript data. Synthesized from all assimilated per-source YAMLs.

**Target path:** `reference/universal/CURSOR-SQLITE-MODEL.yml` (to be created when we run Stage 2 synthesis).

**Format entourage:** The same model is emitted as YAML (canonical), JSON, JSONB, SQLite, CSV, and TXT for deterministic Python/TS tooling (load → validate → process → eval → apply). See **FORMAT-ENTOURAGE.md** and **cursor-sqlite-model-schema.json** in this directory.

---

## Principles

1. **Evidence on every claim** — Block and inline comments cite source (e.g. `# S2thend storage.ts`, `# tarq.net`, `# KEY-CATALOG`). No unsourced facts.
2. **Attribution in the core model** — Attribution is not an afterthought; it is part of the schema. The model has a top-level `sources` array (name, url, assimilated_into) and optional `source` or `sources` on each key entry, entity, and SQL snippet. Exports (JSON, SQLite, CSV) preserve these so every consumer can cite who said what. YAML comments add human-readable origin; the `sources` / `source` fields make attribution machine-readable and round-trip safe.
3. **YAML Jazz** — Comments are first-class: origin, meaning, and usage. Block comments for sections; end-of-line for fields and values.
4. **Factored by concept** — Group by: paths, tables, key namespaces (workspace ItemTable, global ItemTable, cursorDiskKV), entities (bubble, composer, tool_call, composerState), algorithms (extractBubbleText, tool result parse), and cross-cutting (legacy vs new, MCP).
5. **Deduped and cross-validated** — Same key or schema from multiple sources appears once, with multiple source tags. Conflicts resolved or documented with alternatives.
6. **Machine-readable** — Consistent structure so Python/TS can parse and use it (e.g. key patterns, field lists, SQL templates).

---

## Suggested sections (to refine when synthesizing)

- `meta` — version, updated, sources_consumed, schema_version.
- `sources` — top-level list of { name, url, assimilated_into } for attribution; every key/entity/sql entry may carry optional source or sources.
- `paths` — darwin/win32/linux; global_db, workspace_storage, folder_uri_to_path.
- `tables` — ItemTable, cursorDiskKV; where each is used.
- `keys` — workspace_itemtable (session_list_priority, prompts, generations); global_itemtable (composer_state_key, notable); cursor_disk_kv (bubbleId, composerData, agentKv, checkpointId, …) with patterns and source tags.
- `entities` — bubble (type, text, codeBlocks, toolFormerData, thinking, …); composer meta; composerState (YOLO, modes4, defaultMode2); tool_call / tool_result.
- `algorithms` — extractBubbleText priority; tool result parsing (terminal, read_file, edit/write, error); tool param aliases.
- `sql` — Copy-paste queries with inline source and usage comments.
- `legacy_vs_new` — Key priority; raw_chat_data vs composer.composerData; chatSessions vs allComposers.
- `mcp` — cursor:// resources, query_table signature (for cursor-db-mcp).
- `cross_refs` — Pointers to KEY-CATALOG, DATA-SCHEMAS, assimilated files for deep dives.

---

## Relationship to existing docs

- **BORG-COLLECTIVE-COOKBOOK.yml** — Current consolidated cookbook; will feed Stage 2 but the universal model will be more comprehensive and fully commented with evidence.
- **KEY-CATALOG.yml** — Discovered key inventory; absorbed into universal model with source tags.
- **DATA-SCHEMAS.yml** — Bubble/composer/tool schemas; merged into universal model with origins.
- **assimilated/*.yml** — Primary Stage 1 inputs; every fact in the universal model should trace back to one or more of these (or KEY-CATALOG/DATA-SCHEMAS with their own provenance).

When the universal model exists, BORG-COLLECTIVE-COOKBOOK can become a "quick ref" extract from it, or we keep both: cookbook for copy-paste, universal for full accuracy and evidence.

**See also:** UNIVERSAL-MODEL-PLAN.md — gaps, inconsistencies, parallels, trends, patterns, categories, and step-by-step generation plan for the universal model and chunk dir.
