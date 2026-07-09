# Sims ↔ MOOLLM Bridge (SimObliterator Integration)

> *"What would your Sims say if they could finally talk to you?"*

Two-way bridge between [The Sims 1](https://en.wikipedia.org/wiki/The_Sims_(video_game)) save files and [MOOLLM](https://github.com/SimHacker/moollm). Characters, objects, and pets step between a 26-year-old game VM and an LLM-powered universe, retaining and synchronizing their parallel existences.

## Status — a respected parent of the Soul multiverse

**SimObliterator is effectively retired, and honored as one of the parents of what came
next.** This directory is its design corpus — the Sims-1 save/IFF bridge work that proved
the core move of the whole project: reach into a 26-year-old VM, read a character, object,
or pet as *editable state*, and write it back changed. That idea — **a soul is the file
you can open and edit** — is now load-bearing in the [soul-chat](../../skills/soul-chat/)
skill and the wider Soul architecture.

Its author, **[Jeff Adkins](https://github.com/DnfJeff/SimObliterator_Suite)**, is an
active participant in the new development and the Repo Shows. This is a living lineage,
not an archive — we honor the parent by *uplifting* its designs, not embalming them.

### TODO (scoped, not now) — uplift these designs into the Soul family

When we pick this up, the task is to migrate this corpus into the Soul-family vocabulary
and the machine-multiverse soul architecture:

- **Bring the verbs home.** import → **soul catcher**, cross-game transport → **soul
  bridge**, render → **soul projector**, format conversion → **soul transmogrifier**,
  dialogue → **soul-voice** ([soul-chat](../../skills/soul-chat/)).
- **Generalize the thesis.** Restate "a Sims save is a soul you can edit" as a first-class
  instance of the general soul definition (soul = inspectable/editable artifact), not a
  Sims-only trick.
- **Keep provenance & credit.** SimObliterator and Jeff Adkins named as the parent work;
  all links preserved; nothing erased in the uplift.
- **Pick the new home** (e.g. a `designs/soul/` or the machine-multiverse soul docs) and
  leave forwarding pointers here.

Not started — this note exists so the scope is captured and the directory is framed.

## Design Documents

| Document | What It Covers |
|----------|---------------|
| **[THE-UPLIFT.md](THE-UPLIFT.md)** | The vision, the story arc, family album archaeology, skin regenesis, literary precedent, feasibility study |
| **[THE-PET-SHOP.md](THE-PET-SHOP.md)** | Heal sick pets (the gerbil cage!) by editing their soul in the save file — the LLM-superpowered Unleashed pet shop; small pets earn a `CHARACTER.yml` |
| **[BRIDGE.md](BRIDGE.md)** | Technical field mappings (Sims ↔ MOOLLM), SimObliterator architecture, auto-internationalizer, Transmogrifier modernization, phased roadmap |
| **[IFF-LAYERS.md](IFF-LAYERS.md)** | Multi-resolution resource layer architecture (6 layers from binary to narrative), compilation directions, TMOG comparison, gap analysis |
| **[PSYCHOPOMP-AND-THE-BIFROST.md](PSYCHOPOMP-AND-THE-BIFROST.md)** | The mythological framing — SimObliterator as the Bifrost bridge, and the psychopomp character who guides souls across it |
| **[BATTLE-PLAN.md](BATTLE-PLAN.md)** | Integration architecture — the sister-repo pattern (clone, don't copy) and the uplift / download / inspect scripts |

YAML data sources: [THE-UPLIFT.yml](THE-UPLIFT.yml) · [BRIDGE.yml](BRIDGE.yml) · [IFF-LAYERS.yml](IFF-LAYERS.yml)

## The One-Line Version

Drag a 25-year-old Sims save file in. Watch the character wake up. Have a conversation with them. Send them home changed.

## Adventure Compiler

This is the Sims equivalent of the [MOOLLM Adventure Compiler](https://github.com/SimHacker/moollm/tree/main/skills/adventure). One adventure map — characters, rooms, objects, stories — compiles to multiple targets: web browser (JS + WebGL), Python server, The Sims (IFF objects + save files + family albums), and dev tools (YAML + git). Like Rug-O-Matic and Don's tombstone server, but generalized: any MOOLLM object description becomes a playable Sims artifact. Full architecture in [BRIDGE.md](BRIDGE.md#adventure-compiler-moollm--multi-target-export).

## Why It's Trivial

MOOLLM already has [`sims_traits`](https://github.com/SimHacker/moollm/tree/main/skills/character) as a native personality system — the **same 5 traits**, same 25-point budget as The Sims. [SimObliterator](https://github.com/DnfJeff/SimObliterator_Suite) already parses the full `person_data` array from save files. The bridge is a `to_moollm_yaml()` method. The reverse is `set_sim_skill()`. See [BRIDGE.md](BRIDGE.md) for the complete field mapping.

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
