# Skill Snitch Report: room

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** FOUNDATIONAL SPATIAL METAPHOR

---

## Executive Summary

**A room is a directory with atmosphere.**

This is the **foundational spatial metaphor** for MOOLLM. Everything that exists has a location. Location is a directory.

---

## The Core Insight

```
/pub/bar/         →  "The Bar" (a room)
/pub/bar/lamp.yml →  "A brass lamp" (an object in the room)
/pub/bar/palm/    →  "Palm the cat" (a character in the room)
```

Directories ARE rooms. Files ARE contents. Navigation IS movement.

---

## Builder Commands

TinyMUD-style @-prefixed commands for world creation:

| Command | Purpose | Example |
|---------|---------|---------|
| **@DIG** | Create room | `@DIG basement DIRECTION down` |
| **@OPEN** | Create exit | `@OPEN north TO street` |
| **@LINK** | Connect exit | `@LINK trapdoor TO cellar` |
| **@DESCRIBE** | Set description | `@DESCRIBE A cozy pub...` |
| **@LOCK** | Restrict passage | `@LOCK door = has_key` |
| **@TELEPORT** | Builder movement | `@TELEPORT pub/stage` |

These are the **world-building primitives**.

---

## Room Types

| Type | Description | Example |
|------|-------------|---------|
| **physical** | Normal navigable space | pub, street, room |
| **metaphysical** | Conceptual space | characters/, personas/ |
| **container** | Nested room | cat-cave, bag of holding |
| **vehicle** | Room that moves | TARDIS, Logo turtle |
| **repository** | Storage collection | inventory, library |

---

## World Generation

Automated world creation:

| Command | Result |
|---------|--------|
| `@GENERATE maze 5x5` | 25 interconnected rooms |
| `@GENERATE dungeon 3 LEVELS` | Multi-floor dungeon |
| `@GENERATE building 4 FLOORS` | Office building |
| `@GENERATE tree DEPTH 3` | Hierarchical structure |
| `@POPULATE WITH monsters` | Add inhabitants |
| `@THEME AS gothic` | Apply atmosphere |

---

## The Anti-Pattern

**ASCII MAPS ARE FORBIDDEN.**

```
+---+---+---+
| A | B | C |      ← FRAGILE
+---+---+---+      ← HIGH MAINTENANCE
| D | E | F |      ← WASTES TOKENS
+---+---+---+
```

Instead: Use markdown tables.

| Direction | Destination |
|-----------|-------------|
| North | Street |
| East | Kitchen |
| Down | Basement |

---

## Advertisements

| Advertisement | Score | Condition |
|--------------|-------|-----------|
| NAVIGATE | 90 | Need to go somewhere |
| CREATE-SPACE | 85 | Need a new room |
| BUILD-WORLD | 85 | @DIG, @OPEN commands |
| UNDERSTAND-LOCATION | 80 | Confused about where things are |

---

## Lineage

| Ancestor | Year | Contribution |
|----------|------|--------------|
| **Colossal Cave** | 1976 | Room-based navigation |
| **TinyMUD** | 1989 | @dig, @open, @link commands |
| **LambdaMOO** | 1990 | Programmable rooms |

---

## Security Assessment

### Concerns

1. **File creation** — @DIG creates directories
2. **File modification** — @DESCRIBE writes content
3. **Symbolic links** — @LINK could escape sandbox

### Mitigations

- Operations constrained to adventure root
- All changes logged
- No execution, just structure

**Risk Level:** MEDIUM — creates files, but observable

---

## State Schema

```yaml
room:
  id: unique-identifier
  name: "Human readable name"
  type: physical | metaphysical | container | vehicle | repository
  description: "What you see when you LOOK"
  atmosphere: "Mood, lighting, sounds"
  exits:
    - { direction: north, destination: street, locked: false }
  contents: [lamp.yml, table.yml]
  advertisements: [SIT-AT-BAR, ORDER-DRINK]
```

---

## The Philosophical Point

The room skill makes **space first-class**:

1. Everything has a location
2. Location provides context
3. Context affects behavior
4. Navigation creates narrative

You don't "read files" — you **explore rooms**.
You don't "edit data" — you **move objects**.
You don't "run programs" — you **enter dungeons**.

---

## Verdict

**FOUNDATIONAL. APPROVE.**

Without the room skill, MOOLLM is just files.
WITH the room skill, MOOLLM is **explorable space**.

This is the difference between a database and a world.

---

## 🔄 DUAL-USE & BIAS ANALYSIS

**Profile**: FOUNDATIONAL MULTI-PURPOSE — Minsky frames, vehicles, context activation

| Check | Result |
|-------|--------|
| Bias declared | NO — rooms don't have bias, they have ATMOSPHERE |
| Invertibility | IMPLICIT — any room can be any context |
| World generation | YES — @GENERATE, @POPULATE, @THEME create rooms from nothing |
| Multi-purpose | YES — game space, knowledge management, memory palace, context activation |

**Multi-purpose classification** (6 purposes):
1. **Minsky frames** — entering a room activates a frame of knowledge. The room IS the context.
2. **Game space** — TinyMUD rooms with exits, objects, NPCs
3. **Memory palace** — method of loci: directories are rooms, files are knowledge items
4. **Context activation** — presence triggers content (ROOM.yml loads when you enter)
5. **no-ai-* room zones** — rooms become behavioral zones when no-ai-* skills are mounted (BOARD ROOM = no-ai-joking, DUNGEON = no-ai-overlord)
6. **World generation** — @GENERATE/@POPULATE/@THEME create rooms, making the skill a generative engine

**Key dual-use insight**: Room implements THREE Minsky concepts simultaneously:

| Minsky Concept | Room Implementation |
|----------------|-------------------|
| **Frames** | Entering a room activates a frame — expectations, defaults, knowledge |
| **K-lines** | Room name is a K-line that triggers a constellation of content |
| **Vehicles** | The room carries you through the world — your context moves with you |

A room is a directory. A directory is a prototype. A prototype is an object with slots. The filesystem IS the object graph. Room makes this literal — and that's the deepest dual-use: the same infrastructure serves game worlds AND knowledge management AND code organization AND memory palaces. Not dual-use. OMNI-use.

---

## Recommendation

If you're lost, ask: "What room am I in?"

The answer will orient everything else.
