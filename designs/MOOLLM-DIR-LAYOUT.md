# .moollm directory layout (gitignored)

The `.moollm/` tree is gitignored. It holds local runtime state, session logs, and secrets. This doc describes the **intended layout** so bootstrap and skills know where to read/write. On first boot, bootstrap creates missing files from templates.

## Root (bootstrap expects these)

| File | Purpose |
|------|---------|
| hot.yml | Priority file list (advisory). From skills/bootstrap/templates/hot.yml if missing. |
| cold.yml | Deprioritized list (optional). |
| working-set.yml | Current focus. From template if missing. |
| output.md | Append-only session output. |
| session-log.md | Boot log. Append-only. |
| bootstrap-probe.yml | Probe output. Written by bootstrap. |
| INDEX.md | Local index of what lives where (optional; created by organize). |

## secrets/ — Credentials only

- **api-keys.yml** — API keys (OpenAI, Google, Anthropic, etc.). Never commit. Formerly model-keys.yml at root.
- README.md — Explains that this dir is for credentials only.

Scripts that expect the old path `model-keys.yml` at root can use a symlink or be updated to `secrets/api-keys.yml`.

## reports/ — Scan and audit output (archived)

Past run reports from skill-snitch, deep-snitch, cursor-mirror. Use descriptive names (e.g. skill-snitch-moollm-86-skills-2026-01-15.md, deep-snitch-transcript-profanity-scan-2026-01-15.md). Nothing here is committed.

## session-context/ — Task context (session scratch)

One-off context docs for specific tasks (e.g. micropolis-js-review-and-wasm.md). Not templates.

## skills/ — Per-skill runtime

- **skills/skill-log/logs/** — skill-log run entries (timestamped YAML).
- **skills/cursor-mirror/transcripts/** — cursor-mirror export output.
- **skills/cursor-mirror/reports/** — cursor-mirror test/session reports (optional).
- **skills/skill-snitch/** — User config (config.yml, ignore.yml, trust-overrides.yml, scan-history.yml), custom patterns/, surfaces/, analyzers/. Last-run reports may be written here; archives can live in reports/.

## What stays in the repo

Templates live in **skills/bootstrap/templates/** (hot.yml, working-set.yml, etc.). Skill code and docs live in **skills/\<name\>/** in the repo. Example reports, if desired, go in **skills/skill-snitch/examples/** or **designs/** and must be sanitized (no secrets, no machine-specific paths).
