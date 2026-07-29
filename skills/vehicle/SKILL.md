---
name: vehicle
description: Movable room a character can inhabit — horse, coach, wagon, TARDIS, RV
license: MIT
tier: 1
related: [room, mount, party, inventory, container, character, soul, adventure]
tags: [moollm, vehicle, portable-room, embark, drive, caravan]
---

# Vehicle

> A vehicle is a **movable room** (or room-tree) a character can inhabit.

**Not** [`mount`](../mount/) — that skill is NFS-style: overlay a skill on a
directory, or compose virtual trees of GitHub repo slices. Colloquial English
says “mount a horse”; in MOOLLM that horse is a **vehicle** and you `EMBARK` /
`RIDE` it.

Spatial base: [`room`](../room/) — vehicles are a room type (`is_vehicle: true`).

Ethics: [ETHICS.md](ETHICS.md) — Dorothy’s house landed on a witch and killed her.
Movable rooms are not morally null; name pilots, victims, and aftermath.

## Core operations

| Method | Effect |
|--------|--------|
| EMBARK / RIDE | Enter / get on — inhabit the vehicle |
| DISEMBARK | Exit to the vehicle’s current world location |
| DRIVE | Relocate vehicle and all occupants |
| HITCH / UNHITCH | Nest pullable storage vehicles (wagon, trailer) |
| STOW | Cargo in/on vehicle inventory or nested rooms |
| STATUS | Position, occupants, hitchlings, cargo |

```yaml
room:
  name: "Research Tent"
  is_vehicle: true
  world_position: { x: 5, y: 12 }  # changes when you DRIVE
```

## Horses are vehicles

A steed moves through world-space; a rider inhabits it (or rides *on* it as
the occupied locus). It may carry packs (inventory) or **pull** other vehicles
(wagons, caravans). Same pattern as a motorcoach that tows a trailer.

```text
horse (vehicle)
  └── hitch → wagon (vehicle, storage-first)
                └── hitch → second wagon …
caravan := ordered nest traveling as one DRIVE
```

## Nesting and parties

- **Party** — multiple souls/characters sharing one vehicle ([party](../party/))
- **Nested rooms** — FMC lounge/cockpit/bedroom; TARDIS bigger-on-inside
- **Vehicle-as-character** — study/RV with its own CHARACTER.yml (Bartle study,
  FMC #898) — still a vehicle; may also be a soul with minds

## Worked examples (adventure-4)

| Example | Path |
|---------|------|
| FMC Motorcoach #898 | [`don-hopkins/fmc-898/`](../../examples/adventure-4/characters/real-people/don-hopkins/fmc-898/) |
| Richard’s study (TARDIS office) | [`richard-bartle/study/`](../../examples/adventure-4/characters/real-people/richard-bartle/study/) |
| Bakfiets of holding | [`acme-bakfiets-of-holding.yml`](../../examples/adventure-4/street/lane-neverending/w1/acme-bakfiets-of-holding.yml) |
| Logo turtle | room SKILL “Riding the Turtle” |

## Disambiguation

| Word | Skill | Means |
|------|-------|--------|
| mount | [mount](../mount/) | Attach skill / compose virtual repo tree (NFS) |
| vehicle | **this** | Movable inhabitable room (horse, coach, wagon, TARDIS) |
| RIDE / EMBARK | this | Get on/in a vehicle — not `MOUNT skill on X` |

## Part of MOOLLM

[README](../../README.md) · [skills/](../) · [room](../room/) · [INDEX.yml](../INDEX.yml)
