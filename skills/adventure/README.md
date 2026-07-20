# ⚔️ Adventure

> *"Every directory is a room. Every file is a clue. Navigation is investigation."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [room/](../room/) | Adventure IS room + narrative framing |
| [character/](../character/) | Player and NPC management |
| [incarnation/](../incarnation/) | NPCs can be popped out into characters |
| [simulation/](../simulation/) | Adventure extends simulation |
| [card/](../card/) | Companions on the quest |
| [memory-palace/](../memory-palace/) | Spatial knowledge organization |
| [world-generation/](../world-generation/) | Questions create places |
| [debugging/](../debugging/) | Investigation as adventure |
| [sniffable-python/](../sniffable-python/) | Linter feedback loop drives generation |
| [examples/adventure-4/](../../examples/adventure-4/) | Live world with 36 rooms |

**Full Protocol:** [SKILL.md](SKILL.md) | **Interface:** [CARD.yml](CARD.yml)

**Core Protocols:**
- [SUMMON-PROTOCOL.md](SUMMON-PROTOCOL.md) — Distributed character instantiation
- [PSIBER-PROTOCOL.md](PSIBER-PROTOCOL.md) — Step inside any data structure

## Overview

Transform exploration into narrative investigation. Directories become rooms, files become clues, and the LLM dungeon-masters you through the quest.

**Lineage:** Colossal Cave, Zork, LambdaMOO, The Sims.

**Primary source (readable world model):** Knuth's CWEB recasting of Crowther/Woods Adventure 1.0 —
study room + MOOLLM/Repo Show analysis in WillWrightShowForFood:
[`characters/donald-knuth/sources/adventure-knuth/`](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/donald-knuth/sources/adventure-knuth)
([CREAM](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/donald-knuth/sources/adventure-knuth/CREAM.md) ·
[ANALYSIS](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/donald-knuth/sources/adventure-knuth/ANALYSIS.md)).
Upstream: [Knuth Programs — ADVENT](https://www-cs-faculty.stanford.edu/~knuth/programs.html#advent).
SHRDLU/WUMPUS trail: [advent-shrdlu-wumpus-lineage.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/donald-knuth/sources/advent-shrdlu-wumpus-lineage.md).

## Quick Commands

| Command | Effect |
|---------|--------|
| `QUEST objective` | Start adventure |
| `ENTER room` | Go to directory |
| `LOOK` | Describe room |
| `EXAMINE object` | Study file |
| `COLLECT clue` | Add evidence |
| `SELECT character` | Control who |
| `CYCLE` | Next character |
| `SUMMON character` | Instantiate character at current location |
| `ENTER moollm://path` | Enter PSIBER mode (explore data as room) |
| `CHANGE key TO value` | Edit data in PSIBER mode |
| `WHAT IS key` | Ask about a key's purpose |

## When to Use

- **Codebase archaeology** — "Find where the auth bug was introduced"
- **Onboarding** — "Understand this project's structure"
- **Bug hunting** — "Follow the evidence trail"
- **Documentation diving** — "What does this system actually do?"

## Room Narrative Levels

Rooms are described in progressive detail:

- **glance** — one‑line entry for lists and maps  
- **look** — first impression on entry (glance + more)  
- **examine** — architectural detail plus an extra beat, like a song drifting in from outside

Rooms read from `ROOM.yml` plus local `README.md`. Objects and characters
describe themselves; rooms avoid re‑describing artifacts with their own
YAML/MD files.

## Roadmap

Planned expansions:

- **Description alternatives** — allow arrays of strings for glance/look/examine,
  with engine rotation that avoids recent repeats.
- **Dialog tree schema** — descriptions, expressions, and utterances become
  interactive trees with state and consequences: creating or destroying objects,
  currency exchange, summoning or incarnating characters, generating rooms
  and maps, triggering buffs, and reshaping world state.

## Templates

| File | Purpose |
|------|---------|
| [ADVENTURE.yml.tmpl](./events/ADVENTURE.yml.tmpl) | Quest state & evidence |
| [LOG.md.tmpl](./events/LOG.md.tmpl) | Narrative journal |

## Tools Required

- `file_read` — Read rooms and clues
- `file_write` — Update adventure state
- `list_directory` — Survey rooms

## Browser Runtime with Speech

The `dist/` directory contains a publishable browser runtime with **text-to-speech**:

```
dist/
├── speech.js          # Voice synthesis library
├── adventure-speech.js # Speech integration
├── index.html         # Demo page
└── README.md          # API documentation
```

**Features:**
- 🔊 Speaks room descriptions, responses, and dialogue
- 🎭 Character-specific persistent voices
- 🤖 Robot voices for AI/machine characters
- ✨ Effect voices for magical events
- 🌍 Multi-language support (67+ voices on macOS)

```javascript
const engine = createSpeakingAdventure('adventure', {
    speechEnabled: true,
    speakRooms: true
});

engine.load(adventureJSON);
engine.speak("Welcome to NO AI TOWER!", { voiceType: 'robot' });
```

See [dist/README.md](dist/README.md) for full API.

---

# Deep Background

> The following sections are for humans who want to understand the vision, history, and future plans. LLMs running the simulation don't need this context unless specifically consulting the README.

## adventure.py — The CLI Uplift Plan

**Vision:** A Python CLI that validates, lints, and compiles adventures into standalone browser experiences.

```bash
$ adventure.py lint quest/           # Validate schemas, suggest fixes
$ adventure.py compile quest/ -o dist/  # Generate standalone HTML/JS
$ adventure.py serve quest/          # Live preview with hot reload
```

### The Pipeline

```
1. AUTHOR    — Write empathic YAML in Cursor
2. LINT      — adventure.py lint quest/ → outputs events for LLM
3. COMPILE   — LLM generates: HTML + CSS + JSON + JavaScript
4. BROWSER   — engine.js evaluates expressions, escalates to LLM for complex situations
```

### Key Principles

- **Linter does NOT auto-fix** — outputs events for LLM to read and correct (LLM has context)
- **Empathic expressions → static data** — LLM compiles behavior into executable JSON
- **Python for precision, LLM for poetry**

### Runtime Expressions

Objects can have embedded JavaScript expressions for runtime evaluation:

```yaml
compiled_behavior:
  expressions:
    wander_delay: "2 + Math.random() * 3"
    flee_chance: "player.intimidation > 5 ? 0.8 : 0.3"
    damage_roll: "roll('1d6') + this.strength"
```

---

## Inspiration: Scott Adams, Don Hopkins & Memory Palaces

This system is directly inspired by a [Hacker News conversation (Nov 2021)](https://news.ycombinator.com/item?id=29316066) between **Scott Adams** (creator of *Adventureland*, 1978) and **Don Hopkins** (SimCity, The Sims, pie menus).

### The Method of Loci Connection

Don Hopkins asked Scott Adams:

> *"How do you think Adventure games are like the Method of Loci, or Memory Palaces, in that they can help you remember and retrieve vast amounts of information geographically?"*

**Adventure games ARE memory palaces.** The rooms, objects, and spatial relationships create lasting mental maps.

### Pie Menus = Room Navigation

```
      N
      ↑
  NW ↖ ↗ NE
 W ←  ●  → E     Pie menu = Room exits = Memory palace navigation
  SW ↙ ↘ SE
      ↓
      S
```

Don Hopkins realized: *"4-item and 8-item pie menus are the essential elements of an Adventure map, as long as you think of 'menus' as rooms in a map with two-way links."*

### Code as Buildings

Don Hopkins visualizes code as memory palaces:

> *"Each function is a little building like an office or a shop, which has a sign out front telling what services or products it sells, and contains everything inside you need to solve some kind of problem."*

### The Vision: Archives as Adventures

Both Scott Adams and Don Hopkins want to publish their papers, articles, emails, and biographies as **interactive adventures**. This system is one iteration of that vision.

### The Banned Magic

The Method of Loci was **banned by the Puritans in 1584** for evoking "bizarre and irrelevant" imagery. We're bringing it back. 🏰✨

---

## lloooomm Heritage — The Crown Jewels

The Shneiderman Owl Simulation demonstrates the architecture:

```yaml
# owl.yml (YAML definition)
name: "Nightwatch-7"
type: owl
behaviors: [patrol, hunt, drone]
stats:
  energy: 100
  catches: 0
```

↓ **Compiles to** ↓

```javascript
class Owl {
    constructor(id, timezone) {
        this.id = id;
        this.position = { x: 0, y: 0, z: 50 };
        this.energy = 100;
    }
    patrol(owls) { /* 3D flocking (boids) */ }
    hunt(mice) { /* predator-prey behavior */ }
}
```

**The Projection:** Browser version is a deterministic shadow of the full LLM simulation. Simple interactions run locally. Complex situations escalate to LLM.

---

*See [SKILL.md](SKILL.md) for complete runtime specification.*
