# ⏰ Time

> Time flows as the story requires

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Simulation turns vs LLM iterations — **they're not the same!** One LLM response might be 0, 1, or many turns.

## Turn Definition

| Action | Turns |
|--------|-------|
| GO NORTH | 1 |
| PAT TERPIE | 1 |
| LOOK | 0 |
| INVENTORY | 0 |
| Pet all 8 kittens | 8 |
| Take a nap | ~10 |

## Duration Types

- **Turns** — X simulation turns (primary unit)
- **Conditional** — Until condition met
- **While present** — While in location/with item
- **Permanent** — Until explicitly removed
- **Natural language** — "5 minutes", "forever", "randomly 50%"

## Commands

| Command | Effect |
|---------|--------|
| `PAUSE` | Stop time |
| `RESUME` | Restart time |
| `TICK [n]` | Force n turns |
| `WAIT [duration]` | Skip time |
| `UNDO` | Rewind via git |

## Related Skills

- [buff](../buff/) — buff durations in turns
- [needs](../needs/) — needs decay over turns
- [simulation](../simulation/) — time state lives here
