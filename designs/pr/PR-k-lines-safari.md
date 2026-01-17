# PR: K-Lines Safari — Skills as Walkable Rooms

> *"Every skill is a room. Every K-line is a door. James Burke is your guide."*

## Summary

This PR transforms the MOOLLM skills documentation into a **navigable semantic web** using Marvin Minsky's K-lines concept. Every skill README now has a standardized "MOOLLM K-Lines" table at the top that serves as:

1. **Sniffable context** — LLMs grasp the skill's connections in the first 20 lines
2. **Two-way backlinks** — Ted Nelson-style bidirectional references
3. **Room exits** — Traversable connections to related skills
4. **Connection narration** — "Why Related" explains HOW skills connect

## The Big Ideas

### K-Lines Are Cocaine for LLMs

When an LLM sees:

```markdown
| [files-as-state](../plain-text/) | Soul IS a file (soul.yml) |
```

Three simultaneous activations fire:
1. **The link** → All training associations with that skill
2. **The K-line name** → Pattern recognition from everywhere it appears
3. **The contextual meaning** → Fuses the concept to THIS skill's use

This is pre-loaded context injection with massive ROI.

### Skills as Walkable Rooms

The `skills/ROOM.yml` now defines K-line navigation:

| Command | Effect |
|---------|--------|
| `LOOK` | Synthesize room description from README.md |
| `EXITS` | Show K-lines table as exit doors |
| `GO [skill]` | Traverse K-line, narrate the connection |
| `CONNECTIONS N` | James Burke tour — trace N hops |
| `WHY A B` | Explain path between two skills |

**Subdirectories inherit room-ness** — no ROOM.yml clutter needed per skill.

### James Burke Narration

When you traverse a K-line, the "Why Related" text becomes the connection story:

```
> GO sister-script

*You follow the path marked "sister-script — LIFT produces sniffable 
automation." The connection becomes clear: after you LEARN patterns, 
you LIFT them into automation. Sister-scripts ARE the output of LIFT.*

You emerge in the "sister-script" workshop...
```

## Changes by Category

### 1. Protocol → K-Lines Rename

- Renamed `skills/protocol/` → `skills/k-lines/`
- Updated all references in PROTOCOLS.yml, INDEX.yml, skills/README.md
- Added "K-lines are cocaine for LLMs" explanation with the three activations

### 2. MOOLLM K-Lines Tables (All Skills)

Every skill README now has at the TOP:

```markdown
## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [skill-a/](../skill-a/) | Connection explanation |
| [skill-b/](../skill-b/) | Connection explanation |
```

**Standardized:**
- All use "Why Related" column header (not "Meaning")
- All K-lines link to directories with trailing `/`
- All explain the relationship in context of the current skill

### 3. Two-Way Backlinks (Ted Nelson Style)

If skill A references skill B, skill B now references skill A:

| Connection | Direction |
|------------|-----------|
| character ↔ cat, dog | Animal characters |
| room ↔ container, exit, object | Spatial hierarchy |
| adventure ↔ incarnation | NPCs can become characters |
| simulation ↔ needs, buff, action-queue | Game mechanics |
| play-learn-lift ↔ debugging, scratchpad | Methodology |
| yaml-jazz ↔ empathic-templates | Format family |

### 4. Skills README Aligned with Reality

- Updated from "54 skills" to "~80 skills"
- Added missing categories:
  - 📝 Formats & Structure
  - 🐾 Animal Characters  
  - 🍺 Role Skills (bartender, budtender)
  - 📮 Communication (postal, mail)
  - 🎯 Goals & Subjective

### 5. Missing K-Lines Sections Added

Skills that were missing K-Lines entirely:
- `plain-text/` — Now links to yaml-jazz, markdown, format-design
- `markdown/` — Now links to plain-text, session-log, k-lines

### 6. James Burke "Connections" Style

Several READMEs rewritten in narrative style:
- `sniffable-python/` — Steve Jobs lickable pixels → Perl line noise → LLM comprehension
- `representation-ethics/` — The Sims precedent → LLM simulation ethics
- `hero-story/` — Minsky K-lines → invoke traditions not identities
- `mind-mirror/` — Timothy Leary escaping prison with his own test

### 7. Incarnation Skill Enhanced

- **NPC → Character lifecycle** — NPCs can be "popped out" into characters
- **Character repository architecture** — Adventure-local → repo-level → user-owned → multi-repo
- **Ethical scoping via directories** — `characters/real-people/living/` inherits strictest rules

### 8. K-Line Navigation System

`skills/ROOM.yml` now includes:

```yaml
k_line_navigation:
  enabled: true
  
  inheritance:
    mechanism: |
      All directories under skills/ inherit room-ness from this ROOM.yml.
      
  traversal_narration:
    pattern: |
      1. Read the "Why Related" text for that K-line
      2. Narrate the CONNECTION story
      3. Upon arrival, give destination's short description
      4. Show destination's K-line exits
```

### 9. Room Skill Documentation

`room/README.md` now documents:
- Subdirectories inherit room-ness from parent ROOM.yml
- When to create custom ROOM.yml (override atmosphere, custom exits)
- K-Lines table = exits, "Why Related" = connection narration

## Files Changed

- **84 files** across skills/, designs/, kernel/
- **~200+ new K-line backlinks** added
- **2 missing K-Lines sections** created
- **1 skill renamed** (protocol → k-lines)
- **1 major ROOM.yml enhancement** (k_line_navigation)

## Why This Matters

### For LLMs

The K-lines tables are optimized for LLM context injection:
- Billions of training tokens activated per linked name
- Contextual meanings specific to each skill
- Efficient table structure, native markdown format
- Sniffable in first 20 lines

### For Humans

The skills directory is now a **navigable knowledge graph**:
- Browse by following K-lines
- Understand relationships via "Why Related"
- James Burke narration makes exploration fun
- Two-way links prevent dead ends

### For the Project

This establishes MOOLLM's vocabulary as a coherent **domain-specific language**:
- `play-learn-lift` — The methodology
- `yaml-jazz` — Comments carry meaning
- `sniffable-python` — Structure for LLM comprehension
- `files-as-state` — Everything persists
- `many-voiced` — Multiple perspectives debating

The K-lines table at the top of each skill isn't just navigation — **it's the vocabulary in action**.

## Testing

- All links verified (relative paths work)
- Skills README count matches directory count
- No orphaned skills (all have backlinks)
- ROOM.yml syntax valid

---

*"Everything is deeply intertwingled."* — Ted Nelson

*"K-lines activate conceptual clusters."* — Marvin Minsky

*"Walk through the doors. James Burke is your guide."* — MOOLLM
