# Data layout: chunks out, semantic names, git- and LLM-friendly

**Preference:** Pull **pure data chunks** (e.g. YAML embedded in markdown or text) out into **individual files** in **subdirs**. Use **clear, obvious names** that tell you what is inside; fit MOOLLM, Cursor, and domain nomenclature; be **consistent**. Use **big-endian naming** only when there is an actual need for ordering—e.g. category-first so lexical sort groups naturally (`keys-workspace-itemtable.yml` not `workspace-keys-itemtable.yml`)—not numeric prefixes that impose a single importance order. Tools operate on these files directly without parsing a container. **Git-friendly:** paths can be gitignored, regenerated, or checked in. **LLM-friendly:** orchestrator, context assembler, virtual memory, moomap; GLANCE-level (e.g. `meta.yml`, dir listing) then CARD/SKILL-level chunks. Tools **import/export** between chunk dirs and containers.

---

## Principles

1. **Chunks out** — No data buried inside prose or mixed content. Each logical unit (meta, paths, a key namespace, one SQL snippet, one entity) lives in its own file. Pure YAML or JSON; no "here is the yaml:" wrapper.
2. **Subdirs** — Group by concept. One top-level dir per model or export (e.g. `model/`, `csv/`, `audit/`). Nested subdirs for large namespaces (e.g. `keys/`, `sql/`, `entities/`).
3. **Semantic names** — Clear, obvious, tell you what is inside. Fit MOOLLM and Cursor and domain nomenclature; consistent. Use **big-endian naming** only when ordering is needed: put the category first so sort groups by concept (e.g. `keys-workspace-itemtable.yml`, `entities-bubble.yml`, `sql-list-sessions-workspace.sql`). No numeric prefixes (00-, 01-) unless there is a real need for a fixed sequence; names should not encode a universal importance judgement.
4. **Tool-only parsing** — Tools read/write these files. No need to parse a parent markdown or single monolithic YAML to get one key list or one SQL snippet. Each file is self-contained and schema-bound.
5. **Git-friendly** — Any of: **gitignored** (e.g. generated exports, local overrides), **regenerated** from a single source (dir → container or container → dir), or **checked in** as source of truth or audit logs. Diffs are per-file; merges are straightforward.
6. **Import/export** — Tools can **assemble** a directory of chunks into a single container (one .yml, .json, or .md with embedded chunks). And **explode** a container into a directory of chunks. Round-trip preserves data; comments/evidence live in chunk files or in a template used when assembling.
7. **LLM-friendly** — **Orchestrator / context assembler / virtual memory / moomap** can treat the chunk dir as a **detail hierarchy**: load GLANCE-level first (e.g. `meta.yml`, directory listing, or INDEX/GLANCE.yml that points to chunks), then pull in CARD- or SKILL-level chunks as needed. Same layout works for human, tool, and LLM context management; no need to parse a monolithic container to decide what to load.

---

## Canonical chunk dir: universal model

Suggested layout for the Cursor SQLite universal model as a **directory of chunks** (first-class; can be the source of truth instead of one big YAML).

```
reference/universal/model/
  meta.yml
  paths.yml
  tables.yml
  sources.yml
  keys/
     workspace-itemtable.yml
     global-itemtable.yml
     cursor-disk-kv.yml
  entities/
     bubble.yml
     composer-meta.yml
     composer-state.yml
     tool-result-parse.yml
     tool-param-aliases.yml
  sql/
     list-sessions-workspace.sql
     full-session.sql
     list-composers-global.sql
     composer-state.sql
     agent-kv-for-composer.sql
     ...
```

- **.yml** chunks: pure YAML; one top-level key or a small dict. No surrounding markdown.
- **.sql** chunks: pure SQL; optional first line `-- id: list_sessions_workspace` or filename = id. Tools can inject `-- usage: ...` and `-- sources: ...` when exporting to a container.
- **Naming:** Clear, obvious, domain-aligned. Category-first where it helps sort (e.g. `keys/`, `entities/`, `sql/`); no numeric prefixes unless a fixed sequence is required.

---

## LLM / context management

The chunk dir is **orchestrator- and context-assembler-friendly**:

- **Detail hierarchy** — Top-level files (`meta.yml`, `paths.yml`, …) and subdirs (`keys/`, `sql/`, `entities/`) form a clear pyramid. An LLM or context assembler can load a **GLANCE** (e.g. one small INDEX or `meta.yml` + dir listing) to decide relevance, then load only the chunks needed for the current task (CARD/SKILL level).
- **Virtual memory / moomap** — Chunk paths are stable keys; "what’s in context" can be a set of chunk paths. Hot/cold or working-set policies can include/exclude by path or by prefix (e.g. all of `keys/`).
- **GLANCE.yml-style** — Optional: add a `GLANCE.yml` or `INDEX.yml` at the root of the chunk dir that lists chunk names and one-line descriptions (like MOOLLM skill GLANCE). The orchestrator reads GLANCE first, then pulls only the chunks it needs. No parsing of full content to answer "is this relevant?"

---

## Containers vs chunk dirs

| Source of truth | Export / regeneration |
|-----------------|------------------------|
| Chunk dir `model/` | → Single file: `CURSOR-SQLITE-MODEL.yml` (assembled), `CURSOR-SQLITE-MODEL.json`, or `.md` with embedded YAML blocks. |
| Single file `CURSOR-SQLITE-MODEL.yml` | → Chunk dir: explode into `model/meta.yml`, `model/keys/…`, `model/sql/…`, etc. |

- **Audit / logs:** A subdir (e.g. `audit/` or `exports/`) can hold timestamped or versioned chunk dirs or flat files; can be gitignored or checked in.
- **Regenerated:** e.g. `csv/` or `cursor-sqlite-catalog.db` generated from `model/`; put in `.gitignore` or commit as build artifacts.

---

## Embedded chunks in text/markdown

When the **source** is prose (e.g. a doc with “```yaml … ```” blocks):

1. **Extract** — Tool finds fenced blocks or structured sections; writes each to a chunk file (semantic name, category-first if ordering helps) in a subdir.
2. **Edit** — Humans or tools edit the chunk files.
3. **Re-embed** (optional) — Tool reassembles the doc from chunk files, replacing or inserting the blocks. Single source of truth can remain the chunk dir; the doc is generated.

Same for YAML embedded in markdown: extract to `*.yml` in a subdir; tools operate on the .yml; optionally regenerate the .md.

---

## Summary

- Prefer **pure data in individual files**, **subdirs**, **semantic names** (clear, obvious, domain nomenclature; big-endian/category-first only when ordering is needed, no numeric prefixes).
- Tools work on chunk files **without parsing** a container.
- **Git-friendly**: ignore, regenerate, or check in; **import/export** between chunk dirs and single-file (or .md) containers.
- **LLM-friendly**: detail hierarchy (GLANCE → CARD/SKILL); orchestrator/context assembler/virtual memory/moomap can load by chunk path; optional GLANCE.yml/INDEX.yml for "is this relevant?" without parsing full content.
- Universal model can live as **reference/universal/model/** (chunk dir) and be assembled into **CURSOR-SQLITE-MODEL.yml** when needed.

---

## Git

- **Chunk dir `model/`** — Check in as source of truth, or gitignore and regenerate from single-file.
- **Generated** — e.g. `*.db`, `csv/`, `*.json`, `cursor-sqlite-keys.txt`: add to `.gitignore` in that tree or commit as audit/build artifacts.
- **Audit dirs** — `audit/` or `exports/`: typically gitignored; optionally check in for history.
