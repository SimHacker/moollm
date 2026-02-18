# Format entourage: machine-readable model and tooling

The universal Cursor SQLite model is represented in a **format entourage**: one canonical form plus deterministic exports to a **directory of chunks**, YAML, JSON, JSONB, SQLite, CSV, and TXT. Python (or TS) tools can **load → validate → process → eval → apply** against any of these with the same in-memory schema.

**Preferred layout:** Pure data chunks in **individual files** and **subdirs**, **semantic names** (clear, obvious, domain nomenclature; e.g. `meta.yml`, `paths.yml`, `keys/workspace-itemtable.yml`, `sql/full-session.sql`). No numeric prefixes unless a fixed sequence is required. Tools operate on chunk files without parsing a surrounding container. Git-friendly: gitignore, regenerate, or check in; tools **import/export** between chunk dirs and single-file containers. See **DATA-LAYOUT.md** in this directory.

---

## Roles per format

| Format | Role | Use case |
|--------|------|----------|
| **Chunk dir** | Preferred source/export | `model/meta.yml`, `model/keys/*.yml`, `model/sql/*.sql`; semantic names; no container parsing; git-friendly; assemble ↔ explode. |
| **YAML** | Canonical single-file authoring | Comments (YAML Jazz), block structure; can be exploded to chunk dir or assembled from it. |
| **JSON** | APIs, pipelines, no comments | Strict schema; deterministic round-trip from YAML (strip comments). |
| **JSONB** | Postgres storage/query | Same as JSON; store in `jsonb` column for SQL queries over keys/entities. |
| **SQLite** | Queryable catalog | Normalized tables: `meta`, `paths`, `keys`, `entities`, `sql`, `sources`. Run JOINs, filter by source. |
| **CSV** | Flat lists, spreadsheets, diffs | One table per concept: e.g. `keys.csv`, `sql.csv`, `entity_fields.csv`. |
| **TXT** | Line-oriented, copy-paste, logs | Key-per-line, SQL block per section, or key=value; grep-friendly. |

---

## Canonical schema (in-memory / JSON)

The **logical model** that all formats map to. Python loads any format into this; exports from this.

```yaml
# Minimal top-level keys (all optional except meta for versioning)
meta:       { version, updated, schema_version, sources_consumed }
paths:      { darwin: {...}, win32: {...}, linux: {...}, workspace_db, workspace_json, folder_uri_to_path }
tables:     { ItemTable: { schema, where }, cursorDiskKV: { schema, where } }
keys:       # workspace_itemtable, global_itemtable, cursor_disk_kv_catalog
entities:   # bubble, composer_meta, composer_state, tool_result_parse, tool_param_aliases
sql:        # named snippets: list_sessions_workspace, full_session, composer_state, ...
sources:    # list of { name, url, assimilated_into } for evidence
```

- **keys**: Nested by namespace. Each key entry: `pattern` or literal, `note`, optional `sources: []`.
- **entities**: Nested by entity name; each has `fields: {}` or list, optional `sources`.
- **sql**: Map of `id` → `{ body: string, usage?: string, sources?: [] }`.
- **sources**: List of source identifiers used in evidence tags elsewhere.

**Attribution is first-class:** the canonical schema and every export in the entourage preserve a top-level **sources** list and optional **source**/sources per key, entity, or SQL snippet. Validation should require attribution for any exported fact (no unsourced keys or snippets). Comments and evidence tags exist only in YAML; JSON/JSONB/SQLite/CSV/TXT carry data only via the `sources` array and per-item `source`/`sources` fields.

---

## Deterministic processing pipeline

1. **Load** — Read from one of: **chunk dir** (e.g. `model/`), single `.yml`, `.json`, SQLite DB, CSV set, or `.txt` (key-list or structured blocks). Parse into canonical in-memory dict/list. Chunk dir: walk files (semantic names); merge in deterministic order (e.g. by path).
2. **Validate** — Check required `meta`, `schema_version`; required sections present; key patterns well-formed; SQL is string.
3. **Process** — Transform: filter by source, merge with another model, resolve references.
4. **Eval** — Evaluate against live Cursor DBs: run `sql.*` snippets with params, compare key lists to actual DB keys.
5. **Apply** — Emit: write back to any format (chunk dir, single YAML with comments from template, JSON, SQLite, CSV, TXT). Chunk dir: write one file per logical unit; semantic names (clear, domain-aligned).

Round-trip: **YAML → JSON → YAML** (comment-stripped) should be idempotent for data. **YAML → SQLite → CSV → JSON** should reproduce the same logical content (modulo comment loss).

**Future:** Once the model is complete and validated, the same pipeline can target **Cursor’s live state.vscdb** as output: quit Cursor → read → transform (including LLM) → write back. Full import/export. See **reference/INPUT-OUTPUT-PIPELINE.md**.

---

## File naming and placement

| Output | Path (under cursor-mirror) | Notes |
|--------|----------------------------|--------|
| **Chunk dir** | `reference/universal/model/` | Preferred: `meta.yml`, `paths.yml`, `keys/*.yml`, `sql/*.sql`; semantic names; git-friendly; see DATA-LAYOUT.md. |
| Canonical YAML | `reference/universal/CURSOR-SQLITE-MODEL.yml` | Single file; full YAML Jazz, evidence; can be assembled from or exploded to chunk dir. |
| JSON export | `reference/universal/CURSOR-SQLITE-MODEL.json` | No comments; schema-safe. |
| SQLite catalog | `reference/universal/cursor-sqlite-catalog.db` | Tables: meta, paths, keys, entities, sql, sources. Can be gitignored or regenerated. |
| CSV set | `reference/universal/csv/keys.csv`, `sql.csv`, … | One file per logical table; regenerated from model. |
| TXT key list | `reference/universal/cursor-sqlite-keys.txt` | One key pattern per line. |
| TXT SQL bundle | `reference/universal/cursor-sqlite-sql.txt` | Named blocks for copy-paste. |
| Audit / logs | `reference/universal/audit/` or gitignored dir | Timestamped chunk dirs or exports; optional check-in. |

---

## Python tooling contract

Tools in this skill (or in a dedicated `tools/` under cursor-mirror) should:

- **Input**: Path to a file or dir in the entourage: **chunk dir** (e.g. `model/`), single `.yml`, `.json`, `.db`, `.csv` dir, or `.txt`; or a `--format` flag.
- **Output**: Stdout or out path in a requested format; exit 0 on success.
- **Determinism**: Same input + same schema version → same output. No timestamp or random in exported data unless explicitly requested.
- **Validation**: `--validate` mode: load and validate only; exit 1 if invalid.

Example verbs: `load`, `validate`, `export` (to another format), **`assemble`** (chunk dir → single file), **`explode`** (single file → chunk dir), `eval-sql`, `keys-diff`.

---

## CSV table shapes (minimal)

- **keys.csv**: `namespace, key_or_pattern, note, sources`
- **sql.csv**: `id, body, usage, sources`
- **paths.csv**: `platform, key, value` (e.g. darwin, base, "~/Library/...")
- **entities.csv**: `entity, field, type_or_note, sources`

Optional: **sources.csv** with `name, url, assimilated_into`.

---

## Summary

One logical schema, many formats. **Preferred:** chunk dir (semantic names, no numeric prefixes; no container parsing; git-friendly; see DATA-LAYOUT.md). Single-file YAML/JSON and other exports remain supported. Python (and TS) can deterministically load, validate, process, eval, and apply the same metadata and content; **assemble** (chunk dir → container) and **explode** (container → chunk dir) for round-trip.
