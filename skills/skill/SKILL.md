---
name: skill
description: "A skill is documentation that learned to do things."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
related: [moollm, prototype, incarnation, play-learn-lift, sister-script, sniffable-python, plain-text, speed-of-light, constructionism, empathic-templates]
tags: [moollm, meta, program, capability, anthropic]
credits:
  - "David Ungar & Randall Smith — Self language (1987)"
  - "Seymour Papert — Constructionism"
  - "Marvin Minsky — K-lines, Society of Mind"
  - "Anthropic — Skills model foundation"
---

# SKILL

> **"A skill is documentation that learned to do things."**

The meta-protocol: how skills work, how they evolve, how they compose, and how MOOLLM advances the state of the art.

---

## Foundation: What We Share with Anthropic

MOOLLM skills build on Anthropic's excellent Skills model foundation:

| Anthropic Principle | MOOLLM Implementation | Shared Why |
|---------------------|----------------------|------------|
| **Documentation-first** | `README.md` + `SKILL.md` | Explain before automating |
| **Tool definitions** | YAML frontmatter + `CARD.yml` | Machine-readable specs |
| **Composability** | Prototype inheritance + dovetails | Complex from simple |
| **Human gates** | `PLAN-THEN-EXECUTE` protocol | Trust but verify |
| **Skill libraries** | `skills/` directory | Central, shareable |

**The foundation is sound.** What MOOLLM adds is **instantiation, inheritance, K-lines, empathic templates, and proven speed-of-light simulation**.

---

## MOOLLM's Unique Contributions

### 1. Skills as Prototypes (Self-like Inheritance)

> *"Objects all the way down."* — David Ungar

Traditional skills are static documentation. **MOOLLM skills are prototypes that create instances:**

```yaml
# Prototype (the skill)
skills/adventure/
├── SKILL.md           # The documentation
├── CARD.yml           # The interface
└── *.tmpl             # The templates

# Instance (created BY the skill)
examples/adventure-4/
├── ADVENTURE.yml      # Instantiated from template
├── characters/        # Populated during play
├── pub/               # A room instance
└── sessions/          # State over time
```

**Why this matters:**
- Skills aren't just docs — they're **factories**
- Instances inherit from prototypes but can override
- State lives in instances, behavior in prototypes
- Changes to prototypes automatically enhance all instances

See: [delegation-object-protocol.md](./delegation-object-protocol.md)

---

### 2. Cards: Playable Capability Bundles

Skills become **cards** that can be played, traded, collected:

```yaml
# CARD.yml — The interface contract
card:
  id: adventure
  name: "Text Adventure"
  type: [skill, game, narrative]
  emoji: 🎲
  rarity: rare
  
methods:
  EXPLORE: { description: "Move to adjacent room" }
  EXAMINE: { description: "Look at something" }
  TAKE: { description: "Pick up an object" }
  
advertisements:
  NARRATIVE-EXPLORATION:
    score: 90
    condition: "Want interactive fiction"
```

**Why this matters:**
- Clear interface contract
- Advertised capabilities (like Sims objects!)
- Can be played, stacked, combined
- Machine-readable for orchestration

---

### 3. K-lines: Names as Activation Vectors

> *"A K-line is a wire-like structure that attaches to whichever mental agencies are active when you solve a problem."* — Marvin Minsky

When you invoke a skill by name, you activate its **entire knowledge context**:

```markdown
> Apply YAML-JAZZ to this configuration.

# This single name activates:
# - The semantic commenting philosophy
# - The specific syntax patterns
# - The examples and anti-patterns
# - The emotional tone (jazzy, improvisational)
# - Related concepts (POSTEL, soul-chat)
```

**When you instantiate a character, their name becomes their K-line.** "Palm" activates everything about Palm — history, personality, goals, relationships, the incarnation story.

**Why this matters:**
- Names are more than labels — they're **semantic activations**
- Context flows from invocation
- Related concepts automatically available
- The LLM's associative memory works FOR us

---

### 4. Empathic Templates: Smart Instantiation

> *"Templates that understand what you mean, not just what you wrote."*

Traditional templates: `{{name}}` → literal substitution
Empathic templates: `{{describe_character}}` → **intelligent generation**

```yaml
# Template
description: |
  {{describe_appearance_based_on_species_and_personality}}

# Context
species: "Golden Retriever mix"
personality: ["enthusiastic", "loyal", "goofy"]

# Generated
description: |
  Biscuit is a fluffy, perpetually happy Golden Retriever mix with
  eyes that sparkle with boundless enthusiasm. His tail is in a
  constant state of wagging, a furry metronome of joy.
```

**Why this matters:**
- Not string substitution — **semantic generation**
- LLM adds value during instantiation
- Context informs content
- Results are coherent, not mechanical

See: [../empathic-templates/](../empathic-templates/)

---

### 5. Three-Tier State Persistence

Skills persist state at three levels (this is unique to MOOLLM):

| Tier | Location | Lifespan | Use |
|------|----------|----------|-----|
| **Platform** | Cursor session | Ephemeral | Working memory |
| **Narrative** | `LOG.md`, `TRANSCRIPT.md` | Read-mostly | Data islands, events |
| **State** | `*.yml` files | Read-write | Characters, rooms, inventory |

**Data Islands:** Objects embedded in logs with `#object-id` addressing:

```yaml
# LOG.md embedded object — addressable as LOG.md#session-artifact
id: session-artifact
type: skill-output
patterns_found:
  - "API requires auth header"
```

**Promotion Pattern:** If you need to edit it, promote to `.yml` file.

**Why this matters:**
- Right persistence for right data
- Logs stay read-only (audit trail)
- State files are mutable (world state)
- Efficient context management

---

### 6. Speed of Light: PROVEN Multi-Agent Simulation

> *"Many turns in one call. Instant communication. No round-trips."*

This isn't theoretical. **We've demonstrated it:**

| Demonstration | Turns | Agents | Proof |
|---------------|-------|--------|-------|
| **Stoner Fluxx game** | 33 | 8+ characters | Full game state, card draws, rule changes |
| **Cat midnight prowl** | 21 | 10 cats | Parallel paths, territorial marking, reunification |
| **Palm's incarnation** | 1 | 1 + tribunal | Full character creation with committee debate |

```yaml
# 33 turns of Stoner Fluxx in ONE LLM call:
# - Andy and Kristin Looney playing their own game
# - Rule changes (Hand Limit 2, Draw 3, Play All)
# - Goal cards (Peace, 420, Get the Munchies)
# - Keeper management across 8 players
# - Natural conversation and jokes
# - Consistent state throughout
```

**Why this matters:**
- External multi-agent systems: Agent A → API → Agent B → API → ...
- MOOLLM: Single call simulates all agents debating, deciding
- **10x faster, 10x cheaper, perfect consistency**
- Adversarial committees, ensemble inference, real deliberation

See: [../speed-of-light/](../speed-of-light/)

---

### 7. Ethical Framing: Room-Based Context Inheritance

> *"The room defines the performance. Everything inside inherits its framing."*

When you enter a space, you inherit its ethical and performative context:

```yaml
# pub/ROOM.yml
room:
  name: The Rusty Lantern
  
  framing:
    mode: [performance, celebration, tribute]
    inherits_to_children: true
    
    description: |
      This is a PLACE OF PERFORMANCE AND CELEBRATION.
      Everything within these walls is understood as:
      - Social play
      - Entertainment and expression
      - TRIBUTE PERFORMANCE — honoring those we admire
      
    what_this_means:
      debates: "Arguments are sport, not war"
      performances: "The stage is open, judgment is kind"
      tributes: "We invoke those we admire as loving simulations"
```

**Why this matters:**
- Characters in the pub automatically inherit "performance mode"
- Tribute impersonations are framed as celebration, not deception
- Ethical context flows from rooms to all children
- No need to repeat framing in every sub-room

**Example:** When Palm performs as Andy Looney in the pub, the room's framing makes it explicitly a *tribute* — celebrated fan performance, not deceptive impersonation.

See: [../representation-ethics/](../representation-ethics/)

---

### 8. Skills as Rooms, Characters, and Objects

In MOO tradition, everything can manifest in multiple ways. A MOOLLM skill is **triadic**:

**As Room (Space to Explore):**
```
> enter the adventure skill
You are in the Adventure Workshop.
Exits: pub, maze, character-gallery
Objects: room-templates, npc-catalog, puzzle-designs
```

**As Character (Expert to Consult):**
```
> ask adventure-expert about puzzle design
"Consider the lock-and-key pattern: player finds key in
room A, uses it to unlock door in room B..."
```

**As Object (Tool to Use):**
```
> take the room-builder
You now have the room-builder.
> use room-builder on forest-clearing
Creating forest-clearing/ with ROOM.yml template...
```

**Card Structure for Triadic Skills:**

```yaml
card:
  name: adventure
  
  as_room:
    description: "A workshop for building text adventures"
    exits: [pub, maze, templates]
    objects: [room-builder, npc-factory, puzzle-kit]
    
  as_character:
    description: "An expert in interactive fiction design"
    expertise: [puzzle-design, pacing, atmosphere]
    personality: "Creative, playful, encouraging"
    
  as_object:
    description: "Tools for creating adventure games"
    verbs: [create-room, spawn-npc, design-puzzle]
    portable: true
```

---

### 9. Codebase as Navigable World

Modern IDEs like Cursor can mount multiple repositories. Each codebase becomes a navigable world:

- **Directories are rooms** — enter `@central/apps/insights/pyleela/brain/`
- **Files are objects** — examine `Schema.py`, see its classes and functions
- **Functions are chambers** — enter `createSyntheticItemIfNeeded` to focus there
- **Characters have code locations** — `location: "@repo/path/file.py:142"`
- **Parties explore together** — multi-expert code review in one LLM call

**Location path syntax:**
```
@repo/path/to/file.py       # File
@repo/path/to/file.py:42    # Specific line
@repo/path/to/file.py:42-67 # Line range
@repo/path/dir/             # Directory (room)
```

**See:**
- [room/](../room/) — Directories as rooms, files as objects with chambers
- [character/](../character/) — Code locations, party-based review

---

## The Play-Learn-Lift Cycle

Every skill evolves through three phases:

```
┌─────────────────────────────────────────────────────┐
│                    PLAY                              │
│  Do it manually. Explore. Make mistakes.            │
│  "Dropped cheese in room A..."                      │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│                    LEARN                             │
│  Notice patterns. Document them.                    │
│  "Each room needs a unique marker..."              │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│                    LIFT                              │
│  Extract reusable skill. Share it.                  │
│  skill: maze-mapping                                │
│  procedure: "Drop unique item in each room"        │
└─────────────────────────────────────────────────────┘
```

**Documentation → Procedure → Script → Tool**

This is **Programming by Demonstration** made systematic.

See: [../play-learn-lift/](../play-learn-lift/)

---

## Skill Anatomy (Required Structure)

Every skill directory contains:

```
skills/
  my-skill/
    README.md         # Human entry point (GitHub renders)
    SKILL.md          # Full spec with YAML frontmatter
    CARD.yml          # Machine-readable interface
    *.tmpl            # Templates at root level (optional)
```

| File | Purpose | Required |
|------|---------|----------|
| `README.md` | Human-friendly landing page | ✓ |
| `SKILL.md` | Full spec with YAML frontmatter | ✓ |
| `CARD.yml` | Interface: methods, tools, state, advertisements | ✓ |
| `*.tmpl` | Templates for instantiation | Optional |
| `*.py` | Sister scripts for automation | Optional |

### Why README.md (Disagreeing with Anthropic)

Anthropic recommends against `README.md` in skills. We respectfully disagree:

- **GitHub renders README.md** as the landing page
- **Humans browse skills** before invoking them
- **Play-Learn-Lift** starts with exploration
- **Two audiences**: humans (README) and LLMs (SKILL.md + CARD.yml)

**Keep both.** README is for discovery, SKILL.md is for execution.

---

## Flat-to-Structured Growth

Skills can start simple and grow organized:

### Phase 1: Flat Start
```
skills/my-skill/
├── README.md
├── SKILL.md
├── CARD.yml
└── helper.py
```

### Phase 2: Add Structure As Needed
```
skills/my-skill/
├── README.md
├── SKILL.md
├── CARD.yml
├── scripts/           # When you have multiple scripts
│   └── helper.py
├── templates/         # When you have multiple templates
│   └── INSTANCE.yml.tmpl
└── references/        # When you have supporting docs
    └── algorithm.md
```

### Phase 3: Instance Library Pattern

**Skills can have a sub-directory for reusable instances!**

```
skills/buff/
├── README.md
├── SKILL.md
├── CARD.yml
├── BUFF.yml.tmpl      # Template for new buffs
└── buffs/             # ← LIBRARY of reusable instances!
    ├── fire-resistance/   # Instance as directory
    │   └── BUFF.yml
    ├── haste.yml          # Instance as single file
    └── INDEX.yml          # Multiple instances bundled
```

**Three organization styles (all valid, mix freely):**

| Style | When to Use | Example |
|-------|-------------|---------|
| **Directory** | Complex instance with assets | `buffs/fire-resistance/BUFF.yml` |
| **Single file** | Simple standalone instance | `buffs/haste.yml` |
| **INDEX.yml** | Many small related instances | `buffs/INDEX.yml` with 20 buffs |

**The pattern applies to many skills:**

```
skills/buff/buffs/              # Buff library
skills/character/characters/    # Character prototypes
skills/room/rooms/              # Room templates
skills/object/objects/          # Object prototypes
skills/image-mining/images/     # Mineable images
skills/adventure/adventures/    # Adventure templates
```

**INDEX.yml bundling example:**

```yaml
# skills/buff/buffs/INDEX.yml
# Multiple instances in one file

buffs:
  fire-resistance:
    name: "Fire Resistance"
    duration: 10
    effect: "Immune to fire damage"
    
  haste:
    name: "Haste"
    duration: 5
    effect: "+2 speed, extra action"
    
  invisibility:
    name: "Invisibility"
    duration: 8
    effect: "Cannot be seen unless attacking"
    breaks_on: ["attack", "cast_spell"]
```

**Referencing library instances:**

```yaml
# From anywhere in the world
character:
  buffs:
    - ref: skills/buff/buffs/fire-resistance.yml
    - ref: skills/buff/buffs/INDEX.yml#haste
```

**Why this matters:**
- Skills are FACTORIES that produce instances
- Instance libraries are CATALOGS of pre-made products
- Users can browse, copy, or reference existing instances
- The skill teaches by example (Play-Learn-Lift!)

**Rule:** Top-level `SKILL.md` references ALL files, regardless of nesting. No hierarchical hunting.

---

## Front-Matter Sniffing

LLMs can efficiently understand skills by reading the first ~50 lines:

```yaml
# === SKILL HEADER (lines 1-15) ===
---
name: my-skill
description: "One-line summary"
tier: 1
allowed-tools: [read_file, write_file]
related: [room, card, character]
---

# === PURPOSE (lines 16-25) ===
# My Skill
> One-liner philosophy

## What It Does
Brief explanation...

# === FILE MAP (lines 26-40) ===
## Files in This Skill
- `README.md` — Landing page
- `CARD.yml` — Interface definition
- `scripts/helper.py` — Automation tool
- `templates/INSTANCE.yml.tmpl` — Instantiation template
```

**Why this matters:**
- LLMs don't need to read everything
- Front-matter summarizes capability
- File map shows what's available
- 50 lines = context-efficient discovery

---

## Python Scripts: Dual-Audience Structure

When skills include Python, structure for both humans and LLMs:

```python
#!/usr/bin/env python3
"""my-skill: Brief description.

This docstring becomes --help AND is visible to the LLM.

Usage: python my-skill.py [command]
"""

# === IMPORTS (lines 8-15) ===
import click
from pathlib import Path

# === CONSTANTS (lines 17-25) ===
DEFAULT_ROOM = "start"
VALID_COMMANDS = ["explore", "examine", "take"]

# === CLI STRUCTURE (lines 27-50) ===
@click.group()
def cli():
    """Main entry point."""
    pass

@cli.command()
@click.argument("target")
def examine(target: str):
    """Look at something in detail."""
    ...

# === IMPLEMENTATION (lines 52+) ===
# LLM only reads this far if it needs implementation details
```

| Consumer | What They Read |
|----------|----------------|
| **Human** | `./tool.py --help` |
| **LLM** | First 50 lines (imports, constants, CLI structure) |

**DRY:** Command structure written once as code. No duplicate documentation.

---

## Instantiation Modes

Skills don't always need full instantiation:

| Mode | Files? | Persistence | When to Use |
|------|--------|-------------|-------------|
| **Mentioned** | No | None | Quick invocation: "Apply POSTEL here" |
| **Modeled** | No | Chat only | Guided exploration in conversation |
| **Embedded** | In doc | Document | Design discussions (literate programming) |
| **Instantiated** | Yes | Full | Running instances with state |

**Start light, instantiate when needed.**

---

## Skill Composition

Skills compose like functions:

```yaml
skill:
  name: "adventure-exploration"
  
  composes:
    - room           # Navigation
    - card           # Inventory
    - soul-chat      # NPC dialogue
    - action-queue   # Agent behavior
    - speed-of-light # Multi-agent simulation
    
  orchestrates:
    - "Use room for movement"
    - "Use card for items"
    - "Use soul-chat for conversations"
    - "Use speed-of-light for ensemble scenes"
```

**Complex capabilities from simple building blocks.**

---

## Local Skill Emergence

Skills can emerge from gameplay and be captured:

```yaml
# In player.yml after playing
learned_skills:
  - name: grue-avoidance
    learned_from: "dying 7 times"
    technique: "always check lamp before entering dark rooms"
    could_lift_to: skills/grue-avoidance/
    
  - name: vendor-haggling  
    learned_from: "buying lamp oil"
    technique: "buy in bulk, check gold first"
    local_only: true  # Too specific to generalize
```

**Characters carry learned skills.** Objects and NPCs can teach skills.

---

## Commands

| Command | Action |
|---------|--------|
| `SKILL [name]` | Invoke or describe a skill |
| `SKILLS` | List available skills |
| `LEARN-SKILL [name]` | Begin learning a skill |
| `LIFT-SKILL [name]` | Extract local skill to central |
| `INSTANTIATE [skill] [location]` | Create instance from prototype |

---

## Protocol Symbols

| Symbol | Meaning |
|--------|---------|
| `SKILL` | Invoke this meta-skill |
| `PLAY-LEARN-LIFT` | The development lifecycle |
| `SKILL-INSTANTIATION` | Create instance from prototype |
| `PROTOTYPE` | Self-like inheritance |
| `EMPATHIC-TEMPLATES` | Smart semantic instantiation |

---

## The Proof: What We've Demonstrated

This isn't theory. MOOLLM has demonstrated:

### 1. Autonomous Character Creation
- **Palm the monkey**: Full incarnation with tribunal debate, self-chosen name, home, traits, goals
- **Biscuit the dog**: Autonomous naming, species selection, home placement

### 2. Extended Multi-Agent Simulation
- **33-turn Stoner Fluxx**: 8+ characters, rule changes, consistent game state
- **21-turn Cat Prowl**: 10 cats in parallel, territorial marking, coordinated return

### 3. Complex Narrative Consistency
- **Session logs**: 6000+ lines of consistent narrative
- **World state**: Rooms update with markings, characters remember interactions
- **Relationships**: Evolving bonds between characters

### 4. Speed of Light Deliberation
- **Tribunal debates**: Multiple personas cross-examining simultaneously
- **Ensemble inference**: Diverse perspectives in single call

**The architecture works. The results prove it.**

---

## Dovetails With

- **[../prototype/](../prototype/)** — Self-like inheritance philosophy
- **[../k-lines/](../k-lines/)** — K-line naming convention
- **[../play-learn-lift/](../play-learn-lift/)** — Skill development methodology
- **[../empathic-templates/](../empathic-templates/)** — Smart instantiation
- **[../empathic-expressions/](../empathic-expressions/)** — Intent interpretation
- **[../speed-of-light/](../speed-of-light/)** — Multi-agent simulation
- **[../room/](../room/)** — Skills live in rooms (triadic: as_room)
- **[../card/](../card/)** — Skills become cards (triadic: as_object)
- **[../character/](../character/)** — Skills become experts (triadic: as_character)
- **[../constructionism/](../constructionism/)** — Learning by building, Drescher's schema mechanism

### Protocol Documents (in this directory)

- **[delegation-object-protocol.md](./delegation-object-protocol.md)** — Self-like inheritance
- **[skill-instantiation-protocol.md](./skill-instantiation-protocol.md)** — How skills become instances

---

## Summary: MOOLLM Advances the Art

| Feature | Anthropic Foundation | MOOLLM Contribution |
|---------|----------------------|---------------------|
| Documentation | ✓ | + README.md for discovery |
| Tool definitions | ✓ | + CARD.yml with advertisements |
| Composability | ✓ | + Prototype inheritance (Self) |
| Stateless | — | **Three-tier persistence** |
| Single-agent | ✓ | **Speed-of-light multi-agent** |
| String templates | ✓ | **Empathic templates** |
| Static skills | ✓ | **Instantiable prototypes** |
| Names | ✓ | **K-lines (activation vectors)** |
| Single aspect | ✓ | **Triadic: room/character/object** |
| Isolated skills | ✓ | **Codebase as navigable world** |

**We stand on excellent foundations and warmly invite others to join us. We add instantiation, inheritance, empathy, triadic manifestation, and proven multi-agent simulation.**

---

*"Start with jazz, end with standards. But never stop playing."*
