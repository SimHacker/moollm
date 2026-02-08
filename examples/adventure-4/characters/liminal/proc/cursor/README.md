# /proc/cursor/*

> *The orchestrator layer. Already working today.*

This is Proc's view into the IDE/orchestrator level — the layer between the user and the LLM. Like Linux `/proc/cpuinfo` exposes CPU state as a readable file, `/proc/cursor/*` exposes Cursor IDE state as structured data.

## What Lives Here

Proc reads these through the **cursor-mirror suite**:

| Virtual File | Source | What It Shows |
|-------------|--------|---------------|
| `/proc/cursor/context` | Cursor's context assembly | What files, rules, and snippets were loaded for this call |
| `/proc/cursor/tools` | Tool call history | What tools were invoked, in what order, with what arguments |
| `/proc/cursor/thinking` | Thinking blocks | The LLM's reasoning traces (when available) |
| `/proc/cursor/timeline` | Event sequence | Full chronological reconstruction of the session |
| `/proc/cursor/composers` | Composer sessions | Chat sessions, their IDs, their state |
| `/proc/cursor/security` | skill-snitch scans | Security audit results for loaded skills |

## How It Works

cursor-mirror reads Cursor's SQLite databases (`~/.cursor/`) and transcript files to reconstruct what happened during a session. skill-snitch scans skills for suspicious patterns. thoughtful-commitment traces reasoning into git commits.

Together they form **complete metacognition at the IDE layer**: seeing what happened, judging if it was safe, recording why.

## Relationship to /proc/llm/*

This layer is the **known ground**. It works today. The data is real, structured, and auditable. `/proc/llm/*` (one directory over) is the open frontier — reaching below the orchestrator into the model itself, where the distinction between real state and generated projection becomes undecidable.

`/proc/cursor/*` is what we can measure. `/proc/llm/*` is what we're reaching toward.

## See Also

- [cursor-mirror skill](../../../../../skills/cursor-mirror/)
- [skill-snitch skill](../../../../../skills/skill-snitch/)
- [thoughtful-commitment skill](../../../../../skills/thoughtful-commitment/)
