# Reverse-engineered directory: one place for all reversed artifacts

One directory holds **all reverse-engineered documents** from Cursor (executables, install dirs, state DBs) and from **external projects** (by project name). Big-endian naming, YAML-Jazz, shared metadata core, and per-source attribution. Beyond the core, each project or source can use its own schema and vocabulary.

---

## Paths

- **Live/generated:** `.moollm/skills/cursor-mirror/reverse-engineered/` (gitignored). Scripts, extractors, and hand edits write here. One big dir; optional subdirs by project.
- **Curated/canonical (optional):** `reference/reverse-engineered/` (checked in). Canonical examples and index; can mirror or link to the same convention.

Resolve `.moollm` via `MOOLLM_ROOT` (workspace root) or walk up from cwd; see skill-log and bootstrap.

---

## Naming: big-endian + description

Filenames are **time-big-endian** so directory sort is chronological. Use one of:

- `YYYYMMDD-<description-slug>.yml` — one file per day or per logical snapshot
- `YYYYMMDD-HHMMSS-<description-slug>.yml` — one file per run or event

Description slug: short, filesystem-safe (lowercase, hyphens). Examples: `cursor-state-db-keys`, `everestmz-rpc-auth`, `S2thend-storage-ts-keys`.

**By project:** use subdirs under `reverse-engineered/` when useful:

- `reverse-engineered/cursor-app/` — from Cursor binary, install dir, extensionHostProcess.js, etc.
- `reverse-engineered/everestmz-cursor-rpc/` — from that repo or extract
- `reverse-engineered/S2thend-cursor-history/` — from that repo
- `reverse-engineered/forum/` — from Cursor forum threads

Inside each subdir, same big-endian naming. Flat is fine if you prefer one level.

---

## Shared metadata core (required)

Every document in this dir must include the following. YAML-Jazz: comments are semantic; keep them.

```yaml
# --- Shared metadata core (required) ---
meta:
  source: "<url or identifier>"           # Where this came from (repo, blog, binary path)
  source_type: "project | executable | directory | forum | ..."
  created: "YYYY-MM-DDTHH:MM:SS"          # When this doc was first created
  last_updated: "YYYY-MM-DDTHH:MM:SS"     # Last time content was updated
  attribution:                             # Who/what to cite
    - name: "Project or author"
      url: "https://..."
      note: "optional"
  hand_edit_annotations: []                # Optional: list of { at: "section or line", note: "..." }
  # Optional: project name for grouping (e.g. everestmz-cursor-rpc, S2thend-cursor-history)
  project: "optional-project-slug"
```

- **source** — URL (repo, blog, forum thread) or path (e.g. Cursor.app extensionHostProcess.js). Required.
- **source_type** — project | executable | directory | forum | doc | other. Helps consumers filter.
- **created** / **last_updated** — ISO-ish timestamp. Required so we know freshness.
- **attribution** — list of { name, url?, note? }. Required; no unsourced reverse-engineered docs.
- **hand_edit_annotations** — optional list of places where a human edited or annotated (e.g. `{ at: "keys section", note: "Added key from 0.44" }`).

---

## Beyond the core: project-specific content

After the shared core, the rest of the file is **free-form YAML-Jazz**. Each project or source can define its own:

- Key names, table names, schema fragments
- Code snippets, SQL, proto excerpts
- Structural notes (e.g. "storage.ts lines 40–80")
- Cross-references to other reverse-engineered docs or to assimilated files

Preserve the **source’s vocabulary** (e.g. "composerData", "toolFormerData"). Use comments to document meaning and origin. No single global schema beyond the metadata core; per-project "language" is expected and encouraged.

---

## Relation to assimilated and universal model

- **reference/assimilated/*.yml** — One file **per external project**: our **harvest** in their terms, with cursor_mirror_integration and moollm_interpolation. Curated, one-per-source.
- **reverse-engineered/** — **All** reverse-engineered artifacts in one place: from Cursor itself (binaries, dirs) and from projects (by project name). Big-endian named; can be many files per source (e.g. one per extract run, one per executable). Shared metadata core; content can be raw or semi-raw dumps, not only summaries.
- **Universal model (Stage 2)** — Synthesizes from assimilated + KEY-CATALOG + DATA-SCHEMAS; attribution flows from there. Reverse-engineered dir is the **evidence pool**; assimilated and universal model cite it where useful.

---

## Summary

| Aspect | Rule |
|--------|------|
| Path | `.moollm/skills/cursor-mirror/reverse-engineered/` (live); optional `reference/reverse-engineered/` (curated) |
| Naming | Big-endian: `YYYYMMDD-<slug>.yml` or `YYYYMMDD-HHMMSS-<slug>.yml`; optional subdirs by project |
| Metadata core | source, source_type, created, last_updated, attribution, hand_edit_annotations (optional) |
| Content | YAML-Jazz; beyond core, project-specific; preserve source vocabulary; comments as data |
| Attribution | Required; every doc cites source and when it was created/updated |
