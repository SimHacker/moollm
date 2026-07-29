---
name: soul-city
description: Liminal place prototype — rooms, shops, tools, objects; souls walk here
license: MIT
tier: 1
related: [soul, mind, character, persona, room, object, vehicle, adventure, micropolis, incarnation, party, inventory, memory-palace]
tags: [moollm, soul-city, prototype, place, city, map, rooms, roads, shops]
---

# Soul City

Reusable **place** prototype — rooms, roads, shops, tools, objects, plazas,
vehicles. Souls walk here ([soul](../soul/)).

Human entry: [SOUL-MODEL.md](SOUL-MODEL.md)

## Grain

```text
skills/soul/               ← continuity body (0+ minds; free-form)
skills/soul-city/          ← place (rooms, shops, tools, …)
    ↓ INSTANTIATE / COMPOSE
instance map               ← concrete rooms, roads, plazas, shops
    ↓ inhabit
soul + mind[] + character  ← bridges to other games OK
```

## Contents

- **Rooms, roads, maps, plazas** — spatial index
- **Shops, tools, objects** — city affordances
- **Vehicles** — movable inhabitables
- **Souls** — citizens and visitors; each authors its mind graph
- **Parties** — multi-soul travel

## Cross-game

Souls may bridge to characters, personas, and minds in other games. Each game
keeps its own organization. [incarnation](../incarnation/) — grant and author architectures.

## Instances

| Instance | Role |
|----------|------|
| [`examples/adventure-4/`](../../examples/adventure-4/) | Bootstrap walkable seed |
| [`examples/soul-city/`](../../examples/soul-city/) | Sims-citizen seed |
| [MicropolisCore](https://github.com/SimHacker/MicropolisCore) | Product compose |
| [WWSFF catalogs/soul-city](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city) | Platform catalog |

## Parker / public entry

[SOUL-MODEL.md](https://github.com/SimHacker/moollm/blob/main/skills/soul-city/SOUL-MODEL.md)

## Part of MOOLLM

[README](../../README.md) · [skills/](../) · [INDEX.yml](../INDEX.yml)
