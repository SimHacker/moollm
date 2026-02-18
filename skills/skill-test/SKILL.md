# skill-test

Validation test runner for MOOLLM skills. **Status: DESIGN** — harness and per-skill config to be implemented.

- **Runner:** Discovers skills with `test.yml` or `.skill-test.yml`; runs entrypoint (pytest or script); passes env; reports pass/fail and drift.
- **Per-skill:** Each skill declares entrypoint, runner type, env, marks. Tests can live inside the skill (e.g. `cursor-mirror/tests/`).
- **Relation:** skill-snitch = audit/security; skill-test = validation/regression. Both use cursor-mirror for observability.

Design docs (k-lines, source-grouped) live in **designs/**:

| K-line | Path | Content / source |
|--------|------|-------------------|
| RUNNER-DESIGN | designs/runner/RUNNER-DESIGN.md | Harness, config schema, placement, relation to snitch/mirror |
| CURSOR-MIRROR-VALIDATION-SUITE | designs/cursor-mirror/VALIDATION-SUITE.md | What to validate for cursor-mirror; layers; example config; pipeline hook |

See **designs/README.md** for full index.
