# 🎮 Simulation

> The simulation is the world. The world is the simulation.

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Central hub for simulation state management. Everything about the current game state lives in `SIMULATION.yml`.

## Key Concepts

- **SIMULATION.yml** — Source of truth for "now"
- **Global parameters** — Configurable via chat
- **Git time machine** — Commits = deterministic undo
- **Turn tracking** — Increments on significant actions

## Global Parameters

### Time Control
| Command | Effect |
|---------|--------|
| `PAUSE` / `RESUME` | Stop/start time |
| `TICK [n]` | Advance n turns |
| `REWIND [n]` | Go back n turns (via git) |

### Git Automation
| Command | Effect |
|---------|--------|
| `SET AUTO COMMIT on` | Commit each turn |
| `SET AUTO PUSH on` | Push after commits |

### Output
| Command | Effect |
|---------|--------|
| `SET NARRATION [level]` | minimal/normal/verbose |
| `SET TRANSCRIPT [path]` | Where narrative goes |

## Related Skills

- [time](../time/) — turn mechanics
- [party](../party/) — party and selection state
- [adventure](../adventure/) — simulation as adventure
