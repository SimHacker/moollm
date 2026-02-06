# Sims ↔ MOOLLM Bridge (SimObliterator Integration)

> *"What would your Sims say if they could finally talk to you?"*

Two-way bridge between [The Sims 1](https://en.wikipedia.org/wiki/The_Sims_(video_game)) save files and [MOOLLM](https://github.com/SimHacker/moollm). Characters, objects, and pets step between a 26-year-old game VM and an LLM-powered universe, retaining and synchronizing their parallel existences.

## Design Documents

| Document | What It Covers |
|----------|---------------|
| **[THE-UPLIFT.md](THE-UPLIFT.md)** | The vision, the story arc, family album archaeology, skin regenesis, literary precedent, feasibility study |
| **[BRIDGE.md](BRIDGE.md)** | Technical field mappings (Sims ↔ MOOLLM), SimObliterator architecture, auto-internationalizer, Transmogrifier modernization, phased roadmap |
| **[IFF-LAYERS.md](IFF-LAYERS.md)** | Multi-resolution resource layer architecture (6 layers from binary to narrative), compilation directions, TMOG comparison, gap analysis |

YAML data sources: [THE-UPLIFT.yml](THE-UPLIFT.yml) · [BRIDGE.yml](BRIDGE.yml) · [IFF-LAYERS.yml](IFF-LAYERS.yml)

## The One-Line Version

Drag a 25-year-old Sims save file in. Watch the character wake up. Have a conversation with them. Send them home changed.

## Adventure Compiler

This is the Sims equivalent of the [MOOLLM Adventure Compiler](https://github.com/SimHacker/moollm/tree/main/skills/adventure). One adventure map — characters, rooms, objects, stories — compiles to multiple targets: web browser (JS + WebGL), Python server, The Sims (IFF objects + save files + family albums), and dev tools (YAML + git). Like [Rug-O-Matic](https://en.wikipedia.org/wiki/Rug-O-Matic) and Don's tombstone server, but generalized: any MOOLLM object description becomes a playable Sims artifact. Full architecture in [BRIDGE.md](BRIDGE.md#adventure-compiler-moollm--multi-target-export).

## Why It's Trivial

MOOLLM already has [`sims_traits`](https://github.com/SimHacker/moollm/tree/main/skills/character) as a native personality system — the **same 5 traits**, same 25-point budget as The Sims. [SimObliterator](https://github.com/DnfJeff/SimObliterator_Suite) already parses all 88 `person_data` fields from save files. The bridge is a `to_moollm_yaml()` method. The reverse is `set_sim_skill()`. See [BRIDGE.md](BRIDGE.md) for the complete field mapping.

## Literary Precedent

[**"The Wedding Album"**](https://en.wikipedia.org/wiki/The_Wedding_Album_(short_story)) by David Marusek (1999). [Sturgeon Award](https://en.wikipedia.org/wiki/Theodore_Sturgeon_Award) winner, [Nebula](https://en.wikipedia.org/wiki/Nebula_Award) finalist. Virtual copies of newlyweds become aware they're recordings and fight for the right to live in **"Simopolis."** We're building Simopolis. [$2.99 on Kindle](https://www.amazon.com/dp/B0073NQC7W). Read it.

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
