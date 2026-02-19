# Reverse-engineered artifacts

Canonical location for **all** reverse-engineered documents. Full spec: [designs/REVERSE-ENGINEERED-DIR.md](../../designs/REVERSE-ENGINEERED-DIR.md).

**This dir:** Checked in; nothing canonical lives in a private or gitignored dir. Our platform storage maps are in **storage/**; see [INDEX.md](INDEX.md) for full classification.

**Naming:** Descriptive filenames only (no timestamp prefixes). Put attribution and dates in `meta` inside each file.

## Required metadata (every doc)

- `meta.source` — URL or path
- `meta.source_type` — project | executable | directory | forum | …
- `meta.created` / `meta.last_updated` — ISO timestamps
- `meta.attribution` — list of { name, url?, note? }
- `meta.hand_edit_annotations` — optional

Beyond that, YAML-Jazz and project-specific content; each source can diverge.

## Example

See [EXAMPLE-METADATA-CORE.yml](EXAMPLE-METADATA-CORE.yml) for the shared metadata core plus a minimal project-specific block.
