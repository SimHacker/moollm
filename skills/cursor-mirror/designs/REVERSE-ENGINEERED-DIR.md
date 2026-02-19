# Reverse-engineered directory: one place for all reversed artifacts

One directory holds **all reverse-engineered documents** from Cursor (executables, install dirs, state DBs) and from **external projects** (by project name). YAML-Jazz, shared metadata core, and per-source attribution. Beyond the core, each project or source can use its own schema and vocabulary.

**Canonical location:** All curated reverse-engineered content lives **inside the skill**, checked in. Nothing canonical goes in a private or gitignored dir.

---

## Paths

- **Curated/canonical:** `skills/cursor-mirror/reference/reverse-engineered/` (checked in). This is the **only** canonical location for reverse-engineered artifacts. Subdirs by topic or project (e.g. `storage/`, `cursor-app/`, `S2thend-cursor-history/`).
- **Ephemeral (optional):** Scripts may write drafts or extracts to `.moollm/skills/cursor-mirror/reverse-engineered/` (gitignored) for local use only. Promote to `reference/reverse-engineered/` when ready to keep; do not rely on .moollm for anything you do not want to lose.

---

## Naming: descriptive; attribution and dates in files

**Do not use timestamp prefixes in filenames.** Use short, descriptive, filesystem-safe names (lowercase, hyphens). Examples: `cursor-state-db-keys.yml`, `mac-storage-map.yml`, `S2thend-storage-ts-keys.yml`.

**Put attribution and dates inside the file:** every document must include the shared metadata core with `meta.created`, `meta.last_updated`, and `meta.attribution`. That is where timestamps and who-to-cite live, not in the filename.

**By project or topic:** use subdirs under `reference/reverse-engineered/` when useful:

- `reference/reverse-engineered/storage/` -- platform storage maps (macOS, Windows, Linux, Cursor.app, ~/.cursor)
- `reference/reverse-engineered/cursor-app/` -- from Cursor binary, install dir, etc.
- `reference/reverse-engineered/S2thend-cursor-history/` -- from that repo
- `reference/reverse-engineered/forum/` -- from Cursor forum threads

Flat is fine if you prefer one level.

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

- **source** -- URL (repo, blog, forum thread) or path (e.g. Cursor.app extensionHostProcess.js). Required.
- **source_type** -- project | executable | directory | forum | doc | other. Helps consumers filter.
- **created** / **last_updated** -- ISO-ish timestamp. Required so we know freshness.
- **attribution** -- list of { name, url?, note? }. Required; no unsourced reverse-engineered docs.
- **hand_edit_annotations** -- optional list of places where a human edited or annotated (e.g. `{ at: "keys section", note: "Added key from 0.44" }`).

---

## Beyond the core: project-specific content

After the shared core, the rest of the file is **free-form YAML-Jazz**. Each project or source can define its own:

- Key names, table names, schema fragments
- Code snippets, SQL, proto excerpts
- Structural notes (e.g. "storage.ts lines 40--80")
- Cross-references to other reverse-engineered docs or to assimilated files

Preserve the **source's vocabulary** (e.g. "composerData", "toolFormerData"). Use comments to document meaning and origin. No single global schema beyond the metadata core; per-project "language" is expected and encouraged.

---

## Relation to assimilated and universal model

- **reference/assimilated/*.yml** -- One file per external project: our harvest in their terms. Curated, one-per-source.
- **reference/reverse-engineered/** -- All reverse-engineered artifacts in one place: from Cursor itself (binaries, dirs, storage maps) and from projects (by project name). Descriptive filenames; shared metadata core; content can be raw or semi-raw dumps. This dir is the **evidence pool**; nothing canonical lives in a private or gitignored dir.
- **Universal model (Stage 2)** -- Synthesizes from assimilated + KEY-CATALOG + DATA-SCHEMAS; attribution flows from there. Assimilated and universal model cite reverse-engineered where useful.

---

## Summary

| Aspect | Rule |
|--------|------|
| Path | `reference/reverse-engineered/` (canonical, in skill, checked in). Ephemeral only in .moollm if needed. |
| Naming | Descriptive filenames only; **no** timestamp prefixes. Put created/updated/attribution in meta inside the file. |
| Metadata core | source, source_type, created, last_updated, attribution, hand_edit_annotations (optional) |
| Content | YAML-Jazz; beyond core, project-specific; preserve source vocabulary; comments as data |
| Attribution | Required; every doc cites source and when it was created/updated (in meta, not in filename) |
