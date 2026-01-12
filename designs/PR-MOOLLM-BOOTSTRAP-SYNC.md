# PR Plan: MOOLLM bootstrap + advisory cleanup

## Summary
- Add a concise MOOLLM repo manifest (YAML + short MD) to declare world metadata, driver, indices, and adventure.
- Standardize advisory context files: tracked templates under `skills/bootstrap/templates/`, runtime copies in gitignored `.moollm/` (working-set, hot, cold, logs, probe).
- Update bootstrap flow and docs to reflect advisory mode on Cursor, platform-neutral naming, and K-line conventions for advertisements.

## Key changes
- Added `MOOLLM.yml` (microworld manifest) and `MOOLLM.md` (narrative pointer).
- Added templates: `skills/bootstrap/templates/{working-set.yml,hot.yml,cold.yml}`; runtime `.moollm/{working-set.yml,hot.yml,cold.yml}` with append-only logs/probe already in `.moollm/`.
- Bootstrap SETUP (CARD/SKILL) now copies templates into `.moollm/` and optionally creates `cold.yml`.
- Updated self-review to:
  - Mark implemented items DONE (advertisements YAML, advisory files moved to `.moollm/`, bootstrap order).
  - Remove nonstandard `.cursorpriority`; reinforce platform-neutral guidance and use of `.cursorrules` + `.moollm/`.
  - Document advisory-mode status and template-based workflow.
- Kept advertisements K-line style (UPPER-CASE with dashes) and YAML `advertisements:` field as the preferred, greppable pattern.

## Status
- Code/doc updates are applied locally; `.moollm/` remains gitignored (runtime/advisory only).
- No tests run (doc/config-only changes).

## Risks / Notes
- Ensure any future skills align their `advertisements:` keys to K-line form.
- If desired, add a brief README note pointing to `MOOLLM.yml` for discoverability.
- Optional: flesh out the Indirection Pattern in the self-review with the new `.moollm/` breadcrumbs.

## Testing
- Not run (documentation and configuration updates only).
