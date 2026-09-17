# SimObliterator Integration — Battle Plan

> Do NOT copy the repo into moollm. Write skills that know how to clone it, set up the environment, and call it from its own sister directory.

## Architecture: Sister Repo Pattern

```
~/GroundUp/Leela/git/
├── moollm/                    ← our repo (skills live here)
│   └── skills/
│       └── sim-obliterator/   ← the uber-skill (later refactored into sub-skills)
│           ├── GLANCE.yml
│           ├── CARD.yml
│           ├── SKILL.md
│           └── scripts/
│               ├── setup.sh           ← clone repo, create venv, install deps
│               ├── uplift.py          ← save file → CHARACTER.yml
│               ├── download.py        ← CHARACTER.yml → save file
│               └── inspect.py         ← read-only save file exploration
└── SimObliterator_Suite/      ← Jeff's repo (sister directory, mounted in Cursor)
    ├── src/
    ├── launch.py
    └── requirements.txt
```

The skill knows the sister repo path (configurable, default `../SimObliterator_Suite`). It clones if missing, creates a venv, installs deps, and calls SimObliterator's Python API from its own scripts.

## Phase 0: The Uber-Skill (Build First)

One skill that does everything. Refactor later. The uber-skill `skills/sim-obliterator/` handles:

### Methods

| Method | What | Priority |
|--------|------|----------|
| `SETUP` | Clone SimObliterator repo, create venv, install requirements, verify | P0 |
| `INSPECT` | Read-only: load save file, list families/characters/objects | P0 |
| `UPLIFT` | Convert one character from save file → CHARACTER.yml | P0 |
| `DOWNLOAD` | Convert CHARACTER.yml → write back to save file | P1 |
| `TRANSLATE` | Auto-internationalize STR# strings in an IFF object | P2 |
| `DISASSEMBLE` | BHAV disassembly/decompilation of SimAntics bytecode | P2 |
| `ALBUM` | Scrape family album from archive.org, parse to YAML Jazz | P3 |

### SETUP (build this first — everything depends on it)

```bash
#!/bin/bash
# skills/sim-obliterator/scripts/setup.sh
set -eu

SISTER_REPO="${1:-../SimObliterator_Suite}"
VENV_DIR="${SISTER_REPO}/.venv"

# Clone if missing
if [ ! -d "$SISTER_REPO" ]; then
    git clone https://github.com/DnfJeff/SimObliterator_Suite.git "$SISTER_REPO"
fi

# Create venv if missing
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi

# Install deps
"$VENV_DIR/bin/pip" install -r "$SISTER_REPO/requirements.txt" --quiet

# Verify
"$VENV_DIR/bin/python" -c "
import sys; sys.path.insert(0, '$SISTER_REPO/src')
from formats.iff.iff_file import IFFFile
print('SimObliterator ready')
"
```

### INSPECT (read-only exploration — safe starting point)

```python
# skills/sim-obliterator/scripts/inspect.py
"""Inspect a Sims 1 save file. Read-only.

Usage: python inspect.py <save-file> [--json]
"""
# Adds SimObliterator to sys.path, loads save, lists characters
# Outputs YAML Jazz or JSON with character names, traits, needs, relationships
```

### UPLIFT (the core operation — save file character → MOOLLM CHARACTER.yml)

```python
# skills/sim-obliterator/scripts/uplift.py
"""Uplift a Sims 1 character to MOOLLM CHARACTER.yml.

Usage: python uplift.py <save-file> <character-name> [--output <path>]

Reads PersonData from save file, maps to MOOLLM character format,
generates enrichment fields (emoji_identity, mind_mirror, dialogue)
via LLM, writes CHARACTER.yml.
"""
# Uses the field mapping from designs/sim-obliterator/BRIDGE.md
# Indices verified against PersonData.h (12/17/99):
# PersonData[2-7] → sims_traits (nice=2, active=3, generous=4, playful=5, outgoing=6, neat=7)
# PersonData[9-18] → skills (cleaning=9, cooking=10, charisma=11, mechanical=12, ..., logic=18)
# PersonData[56,57,63] → career (job_type, job_status, job_performance)
# PersonData[58,65,60,70] → demographics (age, gender, skin_color, zodiac)
# NOTE: Motives are NOT in PersonData — they are runtime state
# FamilyData.budget → gold
# NeighborData.relationships → relationships with LLM narrative
```

## Build Order

### Week 1: Foundation

1. **Create `skills/sim-obliterator/` directory** with GLANCE.yml, CARD.yml, SKILL.md
2. **Write `setup.sh`** — clone, venv, install, verify
3. **Write `inspect.py`** — read-only save file exploration
4. **Test with a real save file** — verify SimObliterator loads and parses correctly

### Week 2: Uplift

5. **Write `uplift.py`** — single character → CHARACTER.yml
6. **Implement field mapping** from BRIDGE.md (PersonData → sims_traits, needs, skills)
7. **Add LLM enrichment** — emoji_identity, mind_mirror, dialogue.greetings
8. **Test round-trip** — uplift a character, load into MOOLLM adventure, have a conversation

### Week 3: Download

9. **Write `download.py`** — CHARACTER.yml → write back to save file
10. **Implement reverse mapping** — use SimObliterator's `set_sim_*()` methods
11. **Test round-trip** — modify character in MOOLLM, download, verify in game

### Week 4: Refactor into Sub-Skills

12. **Extract `skills/sim-obliterator/inspect/`** — read-only save file exploration
13. **Extract `skills/sim-obliterator/uplift/`** — character → MOOLLM
14. **Extract `skills/sim-obliterator/download/`** — MOOLLM → character
15. **Extract `skills/sim-obliterator/translate/`** — auto-internationalization
16. **Extract `skills/sim-obliterator/bhav/`** — SimAntics bytecode analysis

## Key Design Decisions

### 1. Sister repo, not embedded

SimObliterator has its own git history, its own CI, its own release cycle. Don't copy it. Reference it. The setup script clones it. Updates are `git pull` in the sister directory.

### 2. Venv isolation

SimObliterator has specific Python dependencies (DearPyGUI, Flask, Pillow, etc.). Keep them in a venv inside the SimObliterator directory, not polluting MOOLLM's environment.

### 3. sys.path injection

The uplift/download/inspect scripts add SimObliterator's `src/` to `sys.path` at runtime. This is the cleanest way to use it as a library without installing it as a package.

### 4. CWD-independent

All scripts take explicit paths. The sister repo location is configurable (default `../SimObliterator_Suite`, overridable via environment variable or CLI arg). Works regardless of where you run from.

### 5. MOOLLM-native output

The uplift script outputs MOOLLM CHARACTER.yml, not some intermediate format. The character is immediately usable in the adventure engine, adventure compiler, and any MOOLLM skill that reads CHARACTER.yml.

## CARD.yml Sketch

```yaml
card:
  id: sim-obliterator
  name: "The Sims ↔ MOOLLM Bridge"
  type: [skill, tool, bridge, sims]
  emoji: "🏠"
  tier: 2
  tagline: "Drag a 25-year-old save file in. Watch the character wake up."

  description: |
    Two-way bridge between The Sims 1 save files and MOOLLM.
    Characters step between a 26-year-old game VM and an LLM universe.
    Uses SimObliterator Suite (sister repo) for binary parsing.

advertisements:
  UPLIFT-SIM:
    score: 95
    condition: "Have a Sims 1 save file and want to talk to the characters"
  INSPECT-SAVE:
    score: 85
    condition: "Want to explore what's in a Sims save file"
  DOWNLOAD-SIM:
    score: 90
    condition: "Want to send a MOOLLM character back into The Sims"

tools:
  required: [read_file, write_file, run_terminal_cmd]
  
related:
  - character      # The character format we export to
  - incarnation    # Gold-standard character creation
  - needs          # Sims motive system
  - adventure      # Room-based world the character enters
  - visualizer     # Skin regenesis
  - image-mining   # Family album analysis
```

## What Success Looks Like

```
> SETUP sim-obliterator
SimObliterator cloned, venv created, 276 tests passing.

> INSPECT ~/Sims/UserData/Neighborhoods/Neighborhood001.iff
Found 8 families, 23 characters:
  Goth Family: Mortimer (neat:9, outgoing:2), Bella (outgoing:9, active:7)
  Pleasant Family: Jeff (playful:8), Diane (neat:7)
  ...

> UPLIFT ~/Sims/UserData/Neighborhoods/Neighborhood001.iff "Bella Goth"
Uplifted Bella Goth → characters/bella-goth/CHARACTER.yml
  Traits: outgoing:9, active:7, playful:5, nice:3, neat:1
  Needs: social:high, fun:medium, energy:low
  Job: Politician level 5
  Gold: §23,400
  Relationships: Mortimer (♥ 87/92), Cassandra (♥ 95/95)
  
> Talk to Bella
Bella adjusts her hair and gives you a look that says she has places to be.
"Another visitor? Fine. But make it quick — I have a campaign event tonight."
```

---

*"What would your Sims say if they could finally talk to you?" — now we find out.*
