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

Human entry: [README.md](README.md) → [SOUL-MODEL.md](SOUL-MODEL.md)

Inspiration: Will Wright's 1996 Stanford lecture, where he named **data portability** as the
thing he was working on and then demoed an unreleased Dollhouse by loading a SimCity city into
it — [lecture notes](../../designs/sims/sims-will-wright-microworlds-1996.md).

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

Souls may bridge to characters, personas, and minds in other games. Each game keeps its own
organization — one mind per game, as an **organelle**, in that game's own format, unflattened.
[incarnation](../incarnation/) — grant and author architectures.

Two kinds of crossing at a save-file border, and they are different primitives:

| Gate | Who crosses | Received as |
|------|-------------|-------------|
| Hydraulics | A displaced population | Conserved quantity — `measure` / `drain` / `squirt` |
| Role gate | A named traveler | An office, a byline, a seat |

The act is **transmigration**, not import/export — souls are travelers, and most are refugees
(delisted games, retired servers, formats locked on purpose), so the statuses that apply are
the ones borders use: traveler, expat, immigrant, refugee. Never cargo.

Identity rule: **fork and sync, never transport.** Both sides stay alive; shared fields sync;
the soul is saved before any ending is played. Conservation means nobody vanishes at the border,
and no soul is returned to a world that can no longer hold it.

Protocol: [SOUL-BRIDGES.md](SOUL-BRIDGES.md) · terms: [GLOSSARY.md](GLOSSARY.md) ·
world-to-world (non-save-file) travel: [PORTABLE-NPCS.md](PORTABLE-NPCS.md).

## Instances

| Instance | Role |
|----------|------|
| [`examples/characters/robin/`](examples/characters/robin/) | Worked SOUL-MODEL character — body, persona, soul, three minds |
| [`examples/adventure-4/`](../../examples/adventure-4/) | Bootstrap walkable seed; three imported games interoperating |
| [`examples/soul-city/`](../../examples/soul-city/) | Sims-citizen seed |
| [MicropolisCore](https://github.com/SimHacker/MicropolisCore) | Design + implementation: product, roadmap, bridge SDK |
| [Soul City catalog](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city) | Platform layer — object shops, content pipeline, GUID registry, distribution and rights |

## Bound documents

MOOLLM-side architecture for the Sims bridge:
[THE-UPLIFT.md](../../designs/sim-obliterator/THE-UPLIFT.md) ·
[PSYCHOPOMP-AND-THE-BIFROST.md](../../designs/sim-obliterator/PSYCHOPOMP-AND-THE-BIFROST.md) ·
[BRIDGE.md](../../designs/sim-obliterator/BRIDGE.md) ·
[IFF-LAYERS.md](../../designs/sim-obliterator/IFF-LAYERS.md) ·
[THE-PET-SHOP.md](../../designs/sim-obliterator/THE-PET-SHOP.md)

MicropolisCore-side design + implementation:
[soul-city.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city.md) ·
[characters-as-hydrogen.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/characters-as-hydrogen.md) ·
[roadmap](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city-uplift-roadmap.md) ·
[role sheets](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/micropolis-role-sheets.md) ·
[peer games](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/federation-peer-games.md) ·
[soul-angel modules](https://github.com/SimHacker/MicropolisCore/tree/main/apps/screen-angel/modules/soul-angel)

Vocabulary mapping between the two repos: [README.md](README.md#one-vocabulary-two-repos).

## Public entry

[skills/soul-city/](https://github.com/SimHacker/moollm/tree/main/skills/soul-city)

## Part of MOOLLM

[README](../../README.md) · [skills/](../) · [INDEX.yml](../INDEX.yml)
