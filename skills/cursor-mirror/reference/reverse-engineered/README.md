# Reverse-engineered artifacts

Canonical index and examples for the **reverse-engineered** directory convention. Full spec: [designs/REVERSE-ENGINEERED-DIR.md](../../designs/REVERSE-ENGINEERED-DIR.md).

**Live dir (writes go here):** `.moollm/skills/cursor-mirror/reverse-engineered/` — gitignored; scripts and hand edits create big-endian named YAML files there.

**This dir:** Checked-in convention and example. Optional: mirror canonical docs here or keep only the example so the layout is clear.

## Naming

- Big-endian: `YYYYMMDD-<description>.yml` or `YYYYMMDD-HHMMSS-<description>.yml`
- By project: subdirs like `cursor-app/`, `everestmz-cursor-rpc/`, `S2thend-cursor-history/` with same naming inside

## Required metadata (every doc)

- `meta.source` — URL or path
- `meta.source_type` — project | executable | directory | forum | …
- `meta.created` / `meta.last_updated` — ISO timestamps
- `meta.attribution` — list of { name, url?, note? }
- `meta.hand_edit_annotations` — optional

Beyond that, YAML-Jazz and project-specific content; each source can diverge.

## Example

See [EXAMPLE-METADATA-CORE.yml](EXAMPLE-METADATA-CORE.yml) for the shared metadata core plus a minimal project-specific block.
