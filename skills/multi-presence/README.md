# 🔀 Multi-Presence

> The same card, active in many rooms at once

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [card/](../card/) | What gets multi-instantiated |
| [room/](../room/) | Where activations live |
| [coherence-engine/](../coherence-engine/) | Orchestrates all instances |
| [speed-of-light/](../speed-of-light/) | Parallel in one call |

**Quick Links:**
- [Full Specification](SKILL.md) — complete actor model docs

## Overview

**Multi-Presence** allows a single card (character, tool, skill) to be instantiated in multiple rooms simultaneously, each instance with its own state.

Like running the same program in multiple terminals. Same code, different contexts, parallel execution.

## Actor Model

| Actor Model | Multi-Presence |
|-------------|----------------|
| Actor | Card activation |
| Mailbox | Room's inbox |
| Message | Thrown object |
| Spawn | PLAY card |
| State | Instance YAML |

## Blocking States

| Status | Meaning |
|--------|---------|
| `active` | Running, process this epoch |
| `blocked` | Waiting for tool result, skip |
| `ready` | Tool returned, resume |
| `paused` | User paused, skip until resumed |
| `completed` | Done, can be cleaned up |

## Commands

- `PLAY card IN room` — Create activation
- `INSTANCES card` — List all activations
- `BROADCAST message TO card` — Send to all instances
- `MERGE instance-1 instance-2` — Combine findings

