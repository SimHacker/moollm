# Sims ↔ MOOLLM Bridge (SimObliterator Integration)

> *"What would your Sims say if they could finally talk to you?"*

Two-way bridge between [The Sims 1](https://en.wikipedia.org/wiki/The_Sims_(video_game)) save files and [MOOLLM](https://github.com/SimHacker/moollm). Characters, objects, and pets step between a 26-year-old game VM and an LLM-powered universe, retaining and synchronizing their parallel existences.

## RETIRED — read the current documents instead

**This corpus is historical.** It describes a Python prototype that has since been rewritten in
TypeScript, and it uses vocabulary the project has since replaced. Nothing here should be linked
from a front door, and none of it is the place to start.

Where each idea now lives, in current vocabulary:

| This directory | Current home |
|---|---|
| The protocol for crossing a save-file border | moollm [`skills/soul-city/SOUL-BRIDGES.md`](../../../skills/soul-city/SOUL-BRIDGES.md) — two gates, conservation, fork-and-sync |
| `PSYCHOPOMP-AND-THE-BIFROST.md` — the crossing, the guide, fork-and-sync | [`SOUL-BRIDGES.md` §6](../../../skills/soul-city/SOUL-BRIDGES.md) and the psychopomp section of [`skills/soul-city/README.md`](../../../skills/soul-city/README.md) |
| `THE-UPLIFT.md` — the pipeline and the story | MicropolisCore [soul-city-uplift-roadmap.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/soul-city-uplift-roadmap.md), Phase 0 onward |
| `BRIDGE.md` — field-level Sims ⇄ soul mapping | MicropolisCore [`packages/sims-io/`](https://github.com/SimHacker/MicropolisCore/tree/main/packages/sims-io) (TypeScript, tested) |
| `IFF-LAYERS.md` — multi-resolution resource layers | MicropolisCore [`packages/vitamoo/`](https://github.com/SimHacker/MicropolisCore/tree/main/packages/vitamoo) and its [layered stack](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/vitamoo/OBLITERATOR-TYPESCRIPT.md) |
| `THE-PET-SHOP.md` — the guinea pig demo | MicropolisCore [pet-shop-soul-surgery.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/pet-shop-soul-surgery.md) |
| `ANGEL-EVENT-BUS.md` — objects calling outward | MicropolisCore [`screen-angel/MEDIAFLOW.yml`](https://github.com/SimHacker/MicropolisCore/blob/main/apps/screen-angel/MEDIAFLOW.yml), which deliberately **rejects** a push event bus as the core abstraction, and [the-computer-as-portal.md](https://github.com/SimHacker/MicropolisCore/blob/main/documentation/designs/the-computer-as-portal.md) |
| `BATTLE-PLAN.md` — sister-repo scripts shelling out to Python | Nothing shells out to Python anymore; the I/O runs in browser and Node |
| The vocabulary itself (import/export, cargo) | Replaced: **transmigration**, travelers and refugees, `measure` / `drain` / `squirt`. See [`GLOSSARY.md`](../../../skills/soul-city/GLOSSARY.md) |

**The credit stands.** [Jeff Adkins](https://github.com/DnfJeff/SimObliterator_Suite) wrote the
Python suite that proved the core move — reach into a twenty-six-year-old VM, read a character
as editable state, write it back changed — and that idea is now the definition of a soul in
[`skills/soul-city/`](../../../skills/soul-city/). Retiring the code is not retiring the parent.

Everything below this line is kept for provenance. It is not current.

## Design Documents

| Document | What It Covers |
|----------|---------------|
| **[THE-UPLIFT.md](THE-UPLIFT.md)** | The vision, the story arc, family album archaeology, skin regenesis, literary precedent, feasibility study |
| **[THE-PET-SHOP.md](THE-PET-SHOP.md)** | Heal the sick guinea pig (and you!) by editing their soul in the save file — the LLM-superpowered Unleashed pet shop; names your pet, hands you a coffee-table maintenance book, and (audaciously) can generate a bespoke named guinea pig object and hot-patch it in — the polymorphic-inline-cache trick on a save file |
| **[BRIDGE.md](BRIDGE.md)** | Technical field mappings (Sims ↔ MOOLLM), SimObliterator architecture, auto-internationalizer, Transmogrifier modernization, phased roadmap |
| **[IFF-LAYERS.md](IFF-LAYERS.md)** | Multi-resolution resource layer architecture (6 layers from binary to narrative), compilation directions, TMog comparison, gap analysis |
| **[PSYCHOPOMP-AND-THE-BIFROST.md](PSYCHOPOMP-AND-THE-BIFROST.md)** | The mythological framing — SimObliterator as the Bifrost bridge, and the psychopomp character who guides souls across it |
| **[BATTLE-PLAN.md](BATTLE-PLAN.md)** | Integration architecture — the sister-repo pattern (clone, don't copy) and the uplift / download / inspect scripts |
| **[ANGEL-EVENT-BUS.md](ANGEL-EVENT-BUS.md)** | *(new, 1 Sep 2026)* Objects make "system calls" to the angel by creating invisible message objects; the angel reads the save, acts, and writes replies the objects consume and delete. A low-frequency event bus for minting custom content from actual gameplay — idiomatic, because the Sims VM is already 100% event-driven. Includes the **"Take a Rest" / "Finish Resting"** session model, where saving and quitting becomes diegetic and the rest screen doubles as the one-writer-at-a-time lock; plus the instance/class editor split and the **authoritative engine rules for class edits** (grow attribute counts, never shrink them) |

YAML data sources: [THE-UPLIFT.yml](THE-UPLIFT.yml) · [BRIDGE.yml](BRIDGE.yml) · [IFF-LAYERS.yml](IFF-LAYERS.yml)

## The One-Line Version

Drag a 25-year-old Sims save file in. Watch the character wake up. Have a conversation with them. Send them home changed.

## Adventure Compiler

This is the Sims equivalent of the [MOOLLM Adventure Compiler](https://github.com/SimHacker/moollm/tree/main/skills/adventure). One adventure map — characters, rooms, objects, stories — compiles to multiple targets: web browser (JS + WebGL), Python server, The Sims (IFF objects + save files + family albums), and dev tools (YAML + git). Like Rug-O-Matic and Don's tombstone server, but generalized: any MOOLLM object description becomes a playable Sims artifact. Full architecture in [BRIDGE.md](BRIDGE.md#adventure-compiler-moollm--multi-target-export).

## Why It's Trivial

MOOLLM already has [`sims_traits`](https://github.com/SimHacker/moollm/tree/main/skills/character) as a native personality system — the **same 5 traits**, same 25-point budget as The Sims. [SimObliterator](https://github.com/DnfJeff/SimObliterator_Suite) already parses the full `person_data` array from save files. The bridge is a `to_moollm_yaml()` method. The reverse is `set_sim_skill()`. See [BRIDGE.md](BRIDGE.md) for the complete field mapping.

## Literary Precedent

[**"The Wedding Album"**](https://en.wikipedia.org/wiki/The_Wedding_Album_(short_story)) by David Marusek (1999). [Sturgeon Award](https://en.wikipedia.org/wiki/Theodore_Sturgeon_Award) winner, [Nebula](https://en.wikipedia.org/wiki/Nebula_Award) finalist. Virtual copies of newlyweds become aware they're recordings and fight for the right to live in **"Simopolis."** We're building that place — in MOOLLM it's called **Soul City**. [$2.99 on Kindle](https://www.amazon.com/dp/B0073NQC7W). Read it.

## Key Links

| Resource | URL |
|----------|-----|
| SimObliterator Suite (Jeff Adkins) | https://github.com/DnfJeff/SimObliterator_Suite |
| MOOLLM (Don Hopkins) | https://github.com/SimHacker/moollm |
| VitaBoy Unity — character animation (Don Hopkins) | https://donhopkins.com/home/VitaBoyUnity.zip |
| SimAntics VM Design Document (Don Hopkins) | https://donhopkins.com/home/TheSimsDesignDocuments/VMDesign.pdf |
| "The Wedding Album" — Wikipedia | https://en.wikipedia.org/wiki/The_Wedding_Album_(short_story) |
| "The Wedding Album" — Kindle | https://www.amazon.com/dp/B0073NQC7W |
| MOOLLM Character Skill | https://github.com/SimHacker/moollm/tree/main/skills/character |
| MOOLLM Incarnation Skill | https://github.com/SimHacker/moollm/tree/main/skills/incarnation |
| MOOLLM Semantic Image Pyramid | https://github.com/SimHacker/moollm/tree/main/skills/bootstrap |
| ZombieSims (HN discussion) | https://news.ycombinator.com/item?id=34485103 |
| Sims modding (HN thread) | https://news.ycombinator.com/item?id=43065985 |
