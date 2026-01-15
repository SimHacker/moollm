# World Generation 🌱

> Dynamic world creation — questions create places.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [room/](../room/) | Generated rooms follow room patterns |
| [character/](../character/) | Generated NPCs follow character patterns |
| [incarnation/](../incarnation/) | NPCs can become full characters |
| [container/](../container/) | Containers organize generated regions |
| [adventure/](../adventure/) | World generation serves the adventure |
| [party/](../party/) | Questions about companions create them |
| [constructionism/](../constructionism/) | Exploration creates understanding |
| [empathic-templates/](../empathic-templates/) | Smart generation of content |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

World Generation creates places on demand. Nothing exists until you ask about it. Questions expand reality.

```
Player: "What's north of here?"
DM: *north now exists*
```

**Motto:** *"The world grows where curiosity leads."*

## Quick Start

```
"Create a new area connected to the tavern"
"Expand the dungeon to the west"
"What's beyond the mountains?"
```

## Core Principle

**Don't pre-generate everything. Generate on demand.**

- Infinite worlds in finite storage
- Every playthrough unique
- Player choices shape reality

## Generation Triggers

| Trigger | Example |
|---------|---------|
| **Questions** | "Where did the grue come from?" → generates homeland |
| **Statements** | "There must be a library!" → maybe creates one |
| **Actions** | DIG → tunnel, CLIMB → passage |
| **Quests** | Objective generates its location |
| **Exploration** | Walking past known areas |

## Methods

| Method | Effect |
|--------|--------|
| **CREATE** | Generate new place from seed |
| **EXPAND** | Add adjacent area to existing place |
| **CONNECT** | Link two areas together |

## Directory Inheritance

Parent directories carry defaults that children inherit:

| Directory | Character |
|-----------|-----------|
| `maze/` | Dark, twisty, grue-friendly |
| `tower/` | Height, wind, views |
| `dungeon/` | Cells, guards, escape |
| `garden/` | Outdoor, weather, life |
| `library/` | Books, quiet, knowledge |

## Topology Patterns

| Pattern | Use |
|---------|-----|
| **Twisty maze** | Challenge, getting lost |
| **Grid** | Cities, chessboards |
| **Star** | Hub and spokes |
| **Loop** | Racing, time cycles |
| **Dead ends** | Treasure, boss rooms |

## Integration

| Skill | How It Integrates |
|-------|-------------------|
| **room** | Generated places are rooms |
| **adventure** | Serves the adventure narrative |
| **character** | NPCs generated with locations |
| **worm** | Worms can trigger generation |

## Files

| File | Purpose |
|------|---------|
| `CARD.yml` | Interface, methods |
| `SKILL.md` | Protocol documentation |
| `README.md` | This file |

## See Also

- [room](../room/) — What gets generated
- [adventure](../adventure/) — Generation in context
- [character](../character/) — NPCs with places
