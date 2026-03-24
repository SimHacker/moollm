# cursor-mirror (schemapedia: `cursor-mirror`)

**Introspection family.** Read **Cursor IDE** local state: chats, tool calls, thinking blocks, MCP traces—backed by **SQLite** and YAML model docs. The mirror CLI (`cursor_mirror.py`) exposes many commands for timeline and forensics.

## Why it matters here

Execution ([shell-orchestration](../shell-orchestration/README.md)) produces runs; **introspection** answers “what did the agent actually do?” without guessing. This mechanism is **Cursor-specific** but uses generic [sqlite](../sqlite/README.md) semantics for the data plane.

## What’s distinctive

- **Delegate**: [`cursor-mirror`](../../../../cursor-mirror/SKILL.md) skill; script [`cursor_mirror.py`](../../../../cursor-mirror/scripts/cursor_mirror.py).
- **Canonical model YAML**: `CURSOR-SQLITE-MODEL.yml`, `DATA-SCHEMAS.yml`, `tables.yml`—paths in [`MECHANISM.yml`](./MECHANISM.yml).
- **OS paths** vary; see skill’s `reference/reverse-engineered/storage` notes.

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [sqlite](../sqlite/README.md) | Same SQL engine; gateway `cursor-mirror-to-sqlite`. |
| [shell-orchestration](../shell-orchestration/README.md) | Typical sequence: run pipeline → inspect mirror. Gateway: `shell-then-mirror`. |

## Learn more (prioritized)

| Kind | URL |
|------|-----|
| Product | [Cursor](https://cursor.com/) |
| SQLite | [SQLite](https://www.sqlite.org/) |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Skill: [`../../../../cursor-mirror/SKILL.md`](../../../../cursor-mirror/SKILL.md)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
