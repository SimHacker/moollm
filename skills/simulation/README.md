# 🎮 Simulation

> Abstract base for runtime state — concrete types inherit from this

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

**Abstract base** for runtime state management. Concrete simulation types inherit from this:

| Concrete Type | File | Purpose |
|--------------|------|---------|
| [Adventure](../adventure/) | `ADVENTURE.yml` | Narrative exploration |
| City Sim | `CITY.yml` | Urban simulation |
| Ecosystem | `ECOSYSTEM.yml` | Population dynamics |

> [!IMPORTANT]
> **Don't create `SIMULATION.yml` directly.** Use a concrete type like `ADVENTURE.yml` which includes all simulation properties plus type-specific ones.

## What Simulation Provides

All concrete types inherit:

- **Turn tracking** — `simulation.turn`, `TICK`, `PAUSE`
- **Parameters** — git, display, gameplay settings
- **Party/Selection** — who's playing, who commands go to
- **World state** — flags, active buffs
- **Git time machine** — commits = undo points

## Concrete Type: Adventure

The most common concrete type. `ADVENTURE.yml` includes:

```yaml
# Simulation properties (inherited)
simulation:
  turn: 47
  paused: false
  
parameters:
  git: { auto_commit: true }
  display: { narration_level: normal }
  
player:
  character: characters/don-hopkins/
  location: pub/
  
# Adventure-specific properties (added)
adventure:
  name: "Quest for Knowledge"
  objective: "Find the truth"
  
navigation:
  current_room: pub/
  rooms_visited: [start/, maze/]
```

## Commands

| Command | Effect |
|---------|--------|
| `PAUSE` / `RESUME` | Stop/start time |
| `TICK [n]` | Advance n turns |
| `REWIND [n]` | Go back n turns (via git) |
| `SET [param] [value]` | Configure parameter |

## Related Skills

- [adventure](../adventure/) — concrete type for narrative exploration
- [time](../time/) — turn mechanics
- [party](../party/) — party and selection state
- [character](../character/) — player entities
