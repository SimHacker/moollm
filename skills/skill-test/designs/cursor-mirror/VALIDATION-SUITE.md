# CURSOR-MIRROR-VALIDATION-SUITE — what to validate and how

Rigorous tests to **validate assumptions** (keys, schemas, paths, SQL) and **detect Cursor changes** so the cursor-mirror assimilation pipeline can re-mine and evolve. **Source:** skills/cursor-mirror/designs (moved here; summary + ref kept in cursor-mirror).

---

## Goals

1. **Validate assumptions** — KEY-CATALOG, BORG, assimilated YAML, universal model have required structure; SQL runnable; key lists well-formed.
2. **Detect Cursor changes** — With live `state.vscdb`: compare expected vs actual (tables, ItemTable keys, cursorDiskKV prefixes). Report drift so we re-mine and re-run Stage 2/3.
3. **Pipeline integration** — Stage 3 (cursor-mirror assimilation) runs these tests. Optional: after Stage 2 synthesis or when tracking sibling repos. See cursor-mirror designs/ASSIMILATION-PROCESS.md.

---

## What to validate (layers)

| Layer | Offline (no DB) | Live (with state.vscdb) |
|--------|------------------|--------------------------|
| **Structure** | KEY-CATALOG has `meta`, `cursorDiskKV`, `ItemTable`; BORG has `paths`, `tables`, `sql_*`; assimilated have `cursor_mirror_integration` | — |
| **Keys** | Extract expected ItemTable and cursorDiskKV from catalog/BORG | Compare to actual: sqlite_master; ItemTable keys; cursorDiskKV prefixes |
| **SQL** | Parse and sanity-check (no destructive; valid SQLite) | Run each `sql_*` with safe params; assert no exception |
| **Paths** | BORG paths match platform keys (darwin, win32, linux) | Optional: resolve darwin path, assert DB exists when CURSOR_VALIDATE_LIVE=1 |

Live tests **opt-in** (env or path); **skipped** when no DB so CI without Cursor passes.

---

## cursor-mirror test configuration

When skill-test exists, cursor-mirror declares:

```yaml
# skills/cursor-mirror/test.yml (or .skill-test.yml)
suite: cursor-mirror
description: "Assimilation model structure and optional Cursor DB drift"

entrypoint: tests/
runner: pytest  # or: script (e.g. scripts/validate_cursor_model.py)

env:
  CURSOR_VALIDATE_LIVE: "0"   # set 1 to run live DB tests
  CURSOR_DB_PATH: ""         # optional; default darwin global path

marks:
  structure: "offline, fast"
  drift: "live, requires state.vscdb"
```

Structure tests always run; drift tests when `CURSOR_VALIDATE_LIVE=1` and optionally DB path set.

---

## Pipeline hook

- **Stage 3 (cursor-mirror ASSIMILATION-PROCESS):** After "validate model → verify against live DBs → test tooling", run this validation suite (structure always; live when configured). If drift reported → "Cursor may have changed" → re-mine assimilated, re-run Stage 2/3.
- **Track Cursor changes:** Periodically run suite with live DB; if drift, trigger re-assimilation or document delta.

---

## Implementation order (cursor-mirror)

1. skill-test harness exists (designs/runner/RUNNER-DESIGN.md).
2. Add cursor-mirror test config (`test.yml` or `.skill-test.yml`) pointing at `tests/` and env.
3. Implement structure validation (load KEY-CATALOG, BORG, assimilated; assert required sections).
4. Optional drift tests (expected keys/prefixes vs actual when DB available).
5. Wire "run skill-test for cursor-mirror" into Stage 3 and any CI or "track Cursor changes" job.

---

## References

- **cursor-mirror designs/ASSIMILATION-PROCESS.md** — Stage 3 validate → evolve.
- **cursor-mirror reference/universal/FORMAT-ENTOURAGE.md** — Load → validate → process; validation mode.
- **skill-test designs/runner/RUNNER-DESIGN.md** — Harness and config schema.
