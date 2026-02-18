# Validation test suite (cursor-mirror)

Rigorous tests **validate assumptions** (keys, schemas, paths, SQL) and **detect Cursor changes** so the assimilation pipeline can re-mine and evolve. Structure tests (offline) and optional live DB drift tests; run via **skill-test** (per-skill config, runner in MOOLLM).

**Full design and cursor-mirror-specific validation layers, config example, and pipeline hook:** **skills/skill-test/designs/cursor-mirror/VALIDATION-SUITE.md**.

**Runner design (harness, config schema, relation to skill-snitch):** **skills/skill-test/designs/runner/RUNNER-DESIGN.md**.

**Refs:** designs/ASSIMILATION-PROCESS.md (Stage 3); reference/universal/FORMAT-ENTOURAGE.md (validation mode).
