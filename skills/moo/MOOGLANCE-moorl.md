# MOOGLANCE — Moorl (URLs, fragment, drill)

Dense. Top-level: MOOGLANCE.md. Full: MOONUAL.md §2.

## Forms

- `moo://branch/path` — Repo from MOO_REPO or --repo. Example: `moo://Issue_42/ALERT.yml`.
- `moollm://repo/branch/path` — Full. Example: `moollm://leela-ai/leela-alerts/Issue_42/ALERT.yml`.

## Fragment (#)

- **Navigation (drill):** `#key/key` or `#repos/0`. Slash path; future: JSONPath/dotted for JSON/YAML, XPath for HTML.
- **Line range:** `L3` or `L3-L10` (1-based). Combined: `#key/path:L3-L10`.
- **Query (?):** Reserved for transforms (sniff, skeleton, etc.). Not for navigation.

## Drill rules

- **# only** for drill (not / in path). Use `#key/key` or CLI `--key`.
- **Moorl only:** Drill defined for moo:// and moollm://. Not for https (no tree to split file vs key path).

## Resolve

`moo resolve <moorl>` → JSON: scheme, repo, branch, path, fragment_key_path, fragment_line_start, fragment_line_end, query.
