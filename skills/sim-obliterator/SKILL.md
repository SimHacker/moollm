---
name: sim-obliterator
description: "Two-way bridge between The Sims 1 save files and MOOLLM characters"
license: MIT
tier: 2
allowed-tools:
  - read_file
  - write_file
  - run_terminal_cmd
related: [character, mind-mirror, incarnation, needs, adventure]
tags: [sims, bridge, transport, uplift, download, save-file]
---

# SimObliterator — The Sims ↔ MOOLLM Bridge

> *"What would your Sims say if they could finally talk to you?"*

## What It Does

Reads and writes The Sims 1 save files via the SimObliterator Suite, a binary format parser that understands IFF files — the container format EA used for everything in The Sims.

Characters beam between a 26-year-old game and an LLM universe. Their personality traits, skills, needs, career, relationships, and family data travel with them. Mind Mirror personality (the MOOLLM extension) waits for them when they return.

## Setup

Run SETUP first. Everything else depends on it.

```bash
python3 skills/sim-obliterator/scripts/setup.py
```

Works on macOS, Linux, and Windows. This will:
1. Clone SimObliterator Suite to `../SimObliterator_Suite/` if not already there
2. Create a Python venv inside it (`.venv/`, gitignored)
3. Install dependencies from `requirements.txt`
4. Verify the IFF parser imports correctly
5. Tell you to add the repo to your Cursor workspace

The venv lives inside SimObliterator's directory, not moollm's. This keeps environments isolated. The `.venv/` directory is gitignored by SimObliterator.

## Methods

### SETUP

Clone, venv, install, verify. Idempotent — safe to run again.

```
> SETUP sim-obliterator
SimObliterator cloned, venv created, IFFFile imports. Ready.
```

### INSPECT

Read-only exploration of a save file. Lists families, characters, objects.

```
> INSPECT ~/Sims/UserData/Neighborhoods/Neighborhood001.iff
Found 8 families, 23 characters:
  Goth Family: Mortimer (neat:9, outgoing:2), Bella (outgoing:9, active:7)
  Pleasant Family: Jeff (playful:8), Diane (neat:7)
  ...
```

### UPLIFT

Reads a character from a save file, maps their PersonData to the MOOLLM `sims:` block, enriches with LLM-generated mind_mirror/description/dialogue, writes CHARACTER.yml.

```
> UPLIFT ~/Sims/Neighborhood001.iff "Bella Goth"
Uplifted Bella Goth → characters/bella-goth/CHARACTER.yml
  Traits: neat:1, outgoing:9, active:7, playful:5, nice:3
  Skills: charisma:8, cooking:3
  Zodiac: aries (computed)
  Career: Politics level 5
  Gold: §23,400
```

The uplift maps PersonData fields to the `sims:` block at 0-10 display scale. The LLM then generates mind_mirror properties, a description, backstory, and dialogue based on the personality. The character is immediately usable in MOOLLM.

### DOWNLOAD

Reads a CHARACTER.yml, maps the `sims:` block back to PersonData, patches the save file.

```
> DOWNLOAD characters/bella-goth/CHARACTER.yml ~/Sims/Neighborhood001.iff
Patched Bella Goth into save file.
  Traits written, skills written, needs written.
  mind_mirror preserved in CHARACTER.yml (Sims doesn't have it).
```

## The Transport Protocol

**BEAM UP** (Sims → MOOLLM):
- SimObliterator reads binary save → PersonData array extracted
- `sims:` block fills from PersonData (traits ÷ 100, needs as-is)
- LLM enriches: mind_mirror, description, dialogue, backstory
- Character is alive in MOOLLM

**BEAM DOWN** (MOOLLM → Sims):
- `sims:` block reads → traits × 100, needs as-is → PersonData
- SimObliterator patches binary save
- `mind_mirror:` stays in CHARACTER.yml — Sims doesn't know about it
- Character walks around in the game

**PARALLEL LIFE**:
- Character exists in both worlds simultaneously
- `sims:` is the sync surface — the fields both systems understand
- `mind_mirror:` is MOOLLM-only — it waits when you beam down
- Changes can be merged like git — no data is lost in either direction

## Field Mapping

| CHARACTER.yml | PersonData Index | Scale |
|---------------|-----------------|-------|
| sims.traits.nice | 2 (kPersNice) | 0-10 → ×100 → 0-1000 |
| sims.traits.active | 3 (kPersActive) | 0-10 → ×100 → 0-1000 |
| sims.traits.generous | 4 (kPersGenerous) | 0-10 → ×100 → 0-1000 |
| sims.traits.playful | 5 (kPersPlayful) | 0-10 → ×100 → 0-1000 |
| sims.traits.outgoing | 6 (kPersOutgoing) | 0-10 → ×100 → 0-1000 |
| sims.traits.neat | 7 (kPersNeat) | 0-10 → ×100 → 0-1000 |
| sims.skills.cooking | 10 (kCookingSkill) | 0-10 → ×100 → 0-1000 |
| sims.needs.hunger | motive system | -100 to 100 (as-is) |
| sims.career.track | 56 (kJobType) | enum 0-9 |
| sims.identity.zodiac | 70 (kZodiacSign) | computed, not stored |

See `skills/mind-mirror/SIMS-STATS.yml` for the complete field reference.
See `skills/mind-mirror/ZODIAC.yml` for the zodiac computation algorithm.

## Sister Repo Pattern

SimObliterator is NOT embedded in moollm. It lives beside it:

```
~/GroundUp/Leela/git/
├── moollm/                     ← skills live here
│   └── skills/sim-obliterator/ ← this skill
└── SimObliterator_Suite/       ← Jeff's repo (sister directory)
    ├── src/                    ← Python API we call
    ├── .venv/                  ← our venv (gitignored)
    └── requirements.txt
```

The skill knows where the sister repo is (default `../SimObliterator_Suite`, configurable). Scripts add `src/` to `sys.path` at runtime. The venv isolates SimObliterator's dependencies (DearPyGUI, Flask, Pillow, etc.) from moollm's environment.

## Dovetails With

- `skills/character/` — The CHARACTER.yml format we read/write
- `skills/mind-mirror/` — Personality layer that enriches uplifted characters
- `skills/incarnation/` — Ethical character creation (uplifted Sims get incarnated)
- `skills/needs/` — The Sims need system mapped 1:1
- `skills/adventure/` — Uplifted characters enter the adventure world
