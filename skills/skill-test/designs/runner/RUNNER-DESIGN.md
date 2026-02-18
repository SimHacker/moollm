# RUNNER-DESIGN — skill-test harness and config

Single harness to discover and run tests for one or all skills. Per-skill test configuration; consistent contract. **Source:** moollm/designs (consolidated here).

---

## Interlocking layers

| Layer | Role |
|-------|------|
| **cursor-mirror** | Raw observability: tool calls, arguments, transcripts, DB. |
| **skill-snitch** | Audit skills in body and spirit; watch them run via cursor-mirror. |
| **skill-test** | Put skills to the test. Measure and validate using skill-snitch, cursor-mirror, git, YAML audit logs, LLMs. |

---

## Purpose

- **Single harness** — Discover and run tests for one or all skills.
- **Per-skill test config** — Each skill declares where its tests are and under what conditions (offline vs live, env vars).
- **Consistent contract** — Tests can live in-skill (e.g. `skills/cursor-mirror/tests/`) or reference a suite in the runner; runner invokes the same way.
- **Full-stack validation** — Tests can invoke skill-snitch (SCAN/AUDIT/SNITCH), cursor-mirror (tools, transcript, status), git, skill-log, YAML audit trail, LLMs.

---

## Placement (hybrid)

- **skill-test** — A skill under MOOLLM (e.g. `skills/skill-test/`) that implements the runner.
- **Per-skill config** — `skills/<name>/test.yml` or `skills/<name>/.skill-test.yml`.
- **Tests** — Can live **inside the skill** (e.g. `cursor-mirror/tests/`); runner discovers and runs them.

---

## Test config schema (minimal)

```yaml
# skills/<name>/test.yml or .skill-test.yml
suite: <skill-id>
description: optional

entrypoint: tests/          # dir or script path, relative to skill root
runner: pytest             # pytest | script

env:
  VAR_NAME: "default"      # passed when running tests

marks:
  <mark>: "description"    # e.g. structure: "offline"; drift: "live, needs DB"
```

Runner: resolve skill root, run entrypoint with runner, pass env. Marks filter (e.g. run only `structure` when no live DB).

---

## Relation to skill-snitch and cursor-mirror

| Concern | skill-snitch | skill-test |
|---------|--------------|------------|
| Focus | Security, trust; body and spirit | Correctness, regression |
| Trigger | SCAN, AUDIT, SNITCH | Run test suite |
| Input | Skill files, transcripts, tool calls | Test config + test code; can invoke snitch + mirror + git + LLM |
| Output | Findings, report | Pass/fail, drift report, measures |

---

## cursor-mirror use case

cursor-mirror has reference data (KEY-CATALOG, BORG, assimilated) and optional live checks against state.vscdb. Its config points at `tests/` and sets env (e.g. `CURSOR_VALIDATE_LIVE`, `CURSOR_DB_PATH`). Structure tests run everywhere; drift tests only when DB available. Full validation design: **designs/cursor-mirror/VALIDATION-SUITE.md**.

---

## Extensions

**Context benchmarks** — Run the same benchmark at different context levels: SKILL.md only, skill dir only, MOOLLM subsets (minimal, bootstrap, ambient, respects), or full ecosystem. Measure: do skills work when alone? how well? how much does MOOLLM improve performance? which subsets are sufficient? See **designs/runner/CONTEXT-BENCHMARKS.md**.

**Cost analysis** — cursor-mirror implements cost-analysis (model cost DB, context metadata, time cost, network). skill-test **performs** cost validation (budgets, SLAs). See skills/cursor-mirror/IDEAS-TODO.yml `extensions_todo.cost-analysis`.

---

## Implementation order

1. Define test-config schema and where runner looks (e.g. `skills/*/test.yml`).
2. Add skill-test runner: discover configs, run entrypoints, collect results.
3. Add per-skill configs (cursor-mirror first); add tests under each skill as needed.
4. Optional: CI or periodic job that runs skill-test for all skills (or subset).
5. Extension: cost analysis (cursor-mirror implements; skill-test validates).
