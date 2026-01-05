---
name: skill
description: "A skill is documentation that learned to do things."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
---

# SKILL

> **"A skill is documentation that learned to do things."**

The meta-protocol: how skills work, how they evolve, how they live everywhere.

---

## What Is a Skill?

A skill is a **documented capability** that can be instantiated, composed, and automated.

```
Documentation → Procedure → Script → Tool
     ↑              ↑         ↑        ↑
   PLAY           LEARN     LIFT  SISTER-SCRIPT
```

Skills are **Programming by Demonstration** made systematic. You show the LLM how to do something. It watches, learns patterns, crystallizes them into reusable procedures.

---

## Parallels with Anthropic Skills

MOOLLM skills directly parallel [Anthropic's emerging Skills model](https://docs.anthropic.com/):

| Anthropic Skills | MOOLLM Skills | Shared Philosophy |
|------------------|---------------|-------------------|
| Documentation-first | `README.md` + `SKILL.md` | Explain before automating |
| Tool definitions | `PROTOTYPE.yml` | Machine-readable capability spec |
| Composable tools | Skill inheritance + composition | Build complex from simple |
| Human approval gates | `PLAN-THEN-EXECUTE` | Trust but verify |
| Skill libraries | `skills/` directory | Central, shareable |

**The key insight:** Skills start as prose. They become procedures. They crystallize into scripts. The documentation remains the source of truth.

---

## Where Skills Live

### Central Skills (`skills/` directory)

Shared, reusable, general-purpose:

```
skills/
├── room/            # Spatial navigation
├── card/            # Instantiable capabilities  
├── adventure/       # Text adventure CLI
├── play-learn-lift/ # The methodology itself
├── skill/           # This meta-skill (you are here!)
└── ...
```

### Local Skills (in rooms and characters)

Context-specific, specialized, emergent:

```
examples/adventure-1/
├── player.yml              # Character with local skills
│   skills:
│     - maze-mapping        # Learned from playing
│     - grue-avoidance      # Emerged from dying
│     
├── kitchen/
│   └── ROOM.yml            # Room with local skills
│       skills:
│         - food-prep       # Context-specific
│         - appliance-use   # Local knowledge
```

---

## Instantiation Modes

**Skills don't always need to be instantiated.** They can exist in multiple forms:

### 1. Just Mentioned (Lightest)

Simply name the skill in conversation:

```markdown
> Let's apply YAML-JAZZ to this configuration.
> Use POSTEL when interpreting that command.
```

The name activates the tradition. No files created. Ephemeral.

### 2. Modeled in Chat (Ephemeral)

The skill shapes behavior within a conversation:

```markdown
User: PLAY-LEARN-LIFT this new API

LLM: Starting PLAY phase...
- Exploring endpoints
- Trying different parameters
- Noting what works

Moving to LEARN phase...
- Pattern: all endpoints need auth header
- Pattern: pagination uses cursor, not offset
```

Lives in chat history only. Guides behavior but leaves no files.

### 3. Embedded in Soul-Chat (Documentary)

Skills can be discussed in their design conversation:

```markdown
# yaml-jazz-symposium.md

## YAML-JAZZ (concept)

I am the principle that comments carry meaning.
When you write `# This is semantic`, I ensure it's read.

## A Skeptic

But parsers strip comments!

## YAML-JAZZ

LLMs read comments. The parser is not the only reader.
```

The skill is **embedded in the document about itself**. Meta but useful. 

Embedding skill definitions and examples in design documents and discussions is Knuth's Literate Programming.

### 4. Instantiated in Room (Persistent)

Full materialization with state:

```
skills/adventure/
├── README.md           # Documentation
├── PROTOTYPE.yml       # Machine-readable spec
├── template/           # Templates for instances
└── ...

examples/adventure-1/   # ← An INSTANCE of the skill
├── player.yml         # Skill state
├── start/ROOM.yml     # Skill structure
└── ...
```

The skill has been **instantiated** — it has files, state, persistence.

### Summary Table

| Mode | Files? | Persistent? | Use Case |
|------|--------|-------------|----------|
| Mentioned | No | No | Quick invocation in chat |
| Modeled | No | Chat only | Guided exploration |
| Embedded | Document | Document | Design discussions |
| Instantiated | Yes | Yes | Running instances |

---

### Skill Acquisition Through Interaction

**Interacting with objects AND characters can teach skills.** Characters carry learned skills with them:

```yaml
# Player interacts with the costume racks...
> COMBINE astronaut WITH pirate AS Klaes Ashford FROM The Expanse

# Now player.yml gains:
skills:
  - costume-combining:
      learned_from: "coatroom/costume-racks"
      learned_when: "2026-01-03"
      proficiency: "novice"

# This skill travels with the character!
# Later, in another room with costumes, they already know how.
```

**Skill-granting objects:**
- **Books** teach knowledge skills
- **Tools** teach craft skills  
- **Characters** teach social skills
- **Puzzles** teach problem-solving
- **Practice** improves proficiency

The coatroom doesn't just dress you — it teaches you costume-combining and skill-mixing!

### Skill Inheritance

Local skills can inherit from central skills:

```yaml
# In player.yml
skills:
  - inherits: play-learn-lift  # From central
    local_additions:
      - maze-mapping           # Learned locally
      - costume-combining      # From coatroom
```

---

## The PLAY-LEARN-LIFT Lifecycle

Every skill evolves through three phases:

### PLAY: Explore by Doing

```yaml
# No skill yet — just doing things manually
- "Entered maze room A"
- "Dropped cheese"  
- "Went north, ended up in room C"
- "Hmm, dropped bread here..."
```

### LEARN: Notice Patterns

```yaml
# Pattern emerges:
maze_mapping:
  technique: "drop food items as markers"
  works_because: "each room needs unique marker"
  discovered_by: "trial and error + dying a lot"
```

### LIFT: Extract Reusable Skill

```yaml
# Now it's a skill others can use:
skill:
  name: maze-mapping
  protocol: MAZE-MAP
  
  procedure:
    - "Drop unique item in each room"
    - "Track which items in which rooms"
    - "Build mental map from markers"
    
  sister_script: maze-mapper.py  # Automated version
```

---

## Skill Anatomy

Every skill directory contains:

| File | Purpose | Required |
|------|---------|----------|
| `README.md` | Human-readable overview | ✓ |
| `SKILL.md` | Full protocol documentation | Optional |
| `PROTOTYPE.yml` | Machine-readable definition | ✓ |
| `template/` | Templates for instantiation | Optional |

### PROTOTYPE.yml Structure

```yaml
skill:
  name: "skill-name"
  protocol: SKILL-SYMBOL
  tier: 1  # Capability tier required
  
  description: "One-line summary"
  
  invokes:  # K-lines activated
    - "tradition-name"
    - "another-tradition"
    
  requires:  # Dependencies
    - room
    - card
    
  provides:  # What this skill enables
    - capability-a
    - capability-b
    
  commands:  # Chat commands
    - SKILL-DO-THING
    - SKILL-OTHER-THING
```

---

## Skill Composition

Skills compose like functions:

```yaml
# A complex skill built from simple ones
skill:
  name: "adventure-exploration"
  
  composes:
    - room           # Navigation
    - card           # Inventory
    - soul-chat      # NPC dialogue
    - action-queue   # Agent behavior
    
  orchestrates:
    - "Use room for movement"
    - "Use card for items"
    - "Use soul-chat for conversations"
    - "Use action-queue for autonomy"
```

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

---

## Commands

| Command | Action |
|---------|--------|
| `SKILL [name]` | Invoke or describe a skill |
| `SKILLS` | List available skills |
| `LEARN-SKILL [name]` | Begin learning a new skill |
| `LIFT-SKILL [name]` | Extract local skill to central |
| `COMPOSE-SKILLS [a] [b]` | Combine skills |

---

## Protocol Symbols

| Symbol | Meaning |
|--------|---------|
| `SKILL` | Invoke this meta-skill |
| `PLAY-LEARN-LIFT` | The development lifecycle |
| `SISTER-SCRIPT` | Documentation that became code |
| `SKILL-INSTANTIATION` | Create instance from prototype |

---

## Dovetails With

- **[../protocol/](../protocol/)** — The UPPER-CASE naming convention for skills and concepts
- **[../play-learn-lift/](../play-learn-lift/)** — The methodology for skill development
- **[../sister-script/](../sister-script/)** — When skills become automated scripts
- **[../room/](../room/)** — Skills live in rooms
- **[../card/](../card/)** — Skills can be cards
- **[../constructionism/](../constructionism/)** — Building skills by doing
- **[../soul-chat/](../soul-chat/)** — Skills embedded in design conversations
- **[../../kernel/](../../kernel/)** — Core skill infrastructure
- **[../delegation-object-protocol.md](../delegation-object-protocol.md)** — Skill inheritance

---

## The Anthropic Connection

Anthropic's Skills model and MOOLLM skills share DNA:

1. **Documentation-first**: Write what it does before how
2. **Composable**: Complex capabilities from simple building blocks
3. **Evolvable**: Skills improve through use
4. **Auditable**: You can see what a skill does
5. **Human-in-the-loop**: Approval gates where needed

The difference: MOOLLM skills live in the filesystem, can be local to rooms/characters, and evolve through PLAY-LEARN-LIFT. They're not just tool definitions — they're **living documents that learned to do things**.

---

*"Start with jazz, end with standards."*
