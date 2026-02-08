# /proc/mooco/*

> *The other orchestrator. Proc sees both.*

When MOOLLM runs on [MOOCO](https://github.com/SimHacker/mooco) (the custom orchestrator with explicit context control) instead of Cursor, this directory replaces `/proc/cursor/*` as the IDE-layer view. MOOCO-mirror provides the equivalent introspection.

| Virtual File | What It Shows |
|-------------|---------------|
| `/proc/mooco/context` | MOOCO's explicit context assembly — what was loaded and why |
| `/proc/mooco/traces` | Execution traces — tool calls, state transitions |
| `/proc/mooco/diff` | Comparison with Cursor traces (mooco-mirror vs cursor-mirror) |
| `/proc/mooco/budget` | Token budget tracking — what's spent, what's left |

## Cursor vs MOOCO

Cursor is the current primary platform. MOOCO is the custom alternative. Both expose their internals through Proc's procfs interface. The `diff` virtual file compares traces between the two orchestrators — same MOOLLM skills, different orchestration, what changes?

This is how Proc sees which orchestrator behaviors are platform-specific and which are fundamental to the skills themselves.

## See Also

- [mooco skill](../../../../../skills/mooco/) — The custom orchestrator
- [mooco-mirror skill](../../../../../skills/mooco-mirror/) — MOOCO introspection
- [cursor-mirror skill](../../../../../skills/cursor-mirror/) — Cursor introspection
- [`/proc/cursor/`](../cursor/) — The Cursor-side equivalent
