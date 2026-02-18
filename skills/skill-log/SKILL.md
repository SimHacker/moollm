# skill-log: Protocol for skill logging

Any skill can log structured events into its own directory under `.moollm/skills/<skill-name>/logs/`. Filenames are **time-big-endian** so directory sort is chronological. One file per entry; body is YAML.

---

## Contract

- **Log directory:** `.moollm/skills/<skill_name>/logs/`
  - `<skill_name>` = skill id (e.g. `cursor-mirror`, `skill-snitch`, `skill-test`). Use the same name as in `skills/<name>/`.
  - Resolve `.moollm` from env `MOOLLM_ROOT` or by walking up from cwd until a directory named `.moollm` exists. If not found, use cwd and create `.moollm/skills/<skill_name>/logs/` there.
- **Filename:** `YYYYMMDD-HHMMSS-<description_slug>.yml`
  - Time: local, big-endian (year, month, day, hour, minute, second). Sortable.
  - `<description_slug>`: short, filesystem-safe (lowercase, hyphens for spaces/special; e.g. `run-started`, `snitch-scan-done`). Collision in same second: add suffix (e.g. `run-started-1`) or rely on slug variety.
- **Body (YAML):** At least `timestamp` (ISO or same as filename) and `description` (human string). Rest is free-form `payload` or top-level keys. Comments allowed (YAML Jazz).

---

## Body schema (minimal)

```yaml
timestamp: "2026-02-17T14:30:00"   # ISO or YYYYMMDD-HHMMSS
description: "run started"          # human-readable
# optional: any key-value; nested OK
payload: {}
# or top-level keys: event, result, duration, ...
```

---

## Usage

### Python (script or from another skill)

From repo root or any dir under MOOLLM:

```python
# Option A: run the script
# python skills/skill-log/scripts/skill_log.py <skill_name> <description_slug> [key=value ...]

# Option B: import and call (if skill_log is on path)
from skill_log import log_entry
log_entry("cursor-mirror", "export-done", {"format": "json", "count": 42})
```

### CLI

```bash
# One entry; payload as key=value pairs (optional)
python skills/skill-log/scripts/skill_log.py cursor-mirror export-done format=json count=42

# Or set MOOLLM_ROOT and run from anywhere
MOOLLM_ROOT=/path/to/moollm python skills/skill-log/scripts/skill_log.py skill-snitch scan-done skill=cursor-mirror
```

### From another skill

- **skill-snitch:** After SCAN or AUDIT, log to `.moollm/skills/skill-snitch/logs/` with slug e.g. `scan-done`, `audit-done`; payload can include skill path, finding count.
- **skill-test:** After a test run, log to `.moollm/skills/skill-test/logs/` with slug e.g. `suite-done`, `test-failed`; payload can include suite name, pass/fail, duration.
- **cursor-mirror:** Optional: log export or tail events to `.moollm/skills/cursor-mirror/logs/`.

All use the same convention so snitch/test/mirror can read each other’s logs or aggregate under `.moollm/logs/` later if desired.

---

## TAIL (read recent entries)

The script can support `tail` subcommand: list or cat recent files from a skill’s log dir (sort by filename = time order). Implement in same script or a separate one; protocol is “same dir, same filename format.”

---

## Relation to session-log

- **session-log** — Audit trail for the session (LOG/VIEW/SEARCH); often one shared stream or file.
- **skill-log** — Per-skill, file-per-event, time-big-endian filenames. Skills opt in; no central stream. Use for skill-specific traces, test runs, snitch reports. session-log and skill-log can coexist; tools can aggregate both.

---

## Future

- **MCP / API:** Expose LOG and TAIL as MCP tools or HTTP so non-Python callers can log.
- **Aggregation:** A viewer that reads `.moollm/skills/*/logs/` and merges by time for a single timeline.
- **Rotation:** Optional max files per skill or age-based cleanup; keep protocol simple first.
