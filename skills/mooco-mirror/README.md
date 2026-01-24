# MOOCO Mirror

Parallel introspection for a custom orchestrator that can observe itself and, when helpful, watch a parallel Cursor environment side by side.

This skill mirrors the spirit of `cursor-mirror` while targeting MOOCO‑hosted sessions. It is designed for “parallel mooniverses”: MOOCO running locally, Cursor running in the IDE, and a shared lens that compares context assembly, tool usage, and event emissions across both.

In this pairing, Cursor is the IDE for mooniverses, and MOOCO is the language‑server‑like runtime and live execution environment for portable skills, context, and code. Develop in parallel, then publish a standalone mooniverse for production.

## What It Does

- Inspect MOOCO session logs and event streams
- Compare MOOCO context assembly with Cursor’s observed context
- Trace tool calls and sister‑script invocations
- Surface divergences between orchestration decisions

## Use Cases

- Debug context drift between development and production
- Validate orchestration decisions before release
- Improve skill portability by exposing hidden assumptions

## Why It Matters

Parallel systems drift. A mirror keeps them coherent by turning invisible orchestration decisions into explicit data.

## Relationship to Cursor‑Mirror

- Cursor‑mirror reads Cursor’s SQLite state and tooling traces
- MOOCO‑mirror reads MOOCO’s session events and context bundles
- Together they allow side‑by‑side introspection and debugging
