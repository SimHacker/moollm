---
name: protocol
description: "Protocol names ARE K-lines."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
related: [yaml-jazz, skill, coherence-engine]
---

# PROTOCOL

> **"Protocol names ARE K-lines."**

MOOLLM protocol symbols are Minsky's K-lines made concrete and greppable.

---

## Protocol Names = K-Lines

A **K-line** (Minsky, *Society of Mind*) is a mental structure that, when activated, reactivates an entire constellation of knowledge, skills, and associations.

**Protocol names are exactly this:**

```
YAML-JAZZ         ← Activates: semantic comments, jazz interpretation, LLM-as-musician
POSTEL            ← Activates: charitable interpretation, robustness, collaboration
PLAY-LEARN-LIFT   ← Activates: exploration, pattern-finding, crystallization, sharing
COHERENCE-ENGINE  ← Activates: consistency, constraints, orchestration, referee, simulation, DM
```

Type the name → activate the tradition → invoke the behavior.

The UPPER-CASE-HYPHENATED format makes these K-lines **findable**.

---

## Naming Convention

| Rule | Example | Why |
|------|---------|-----|
| ALL CAPS | `YAML-JAZZ` not `yaml-jazz` | Stands out in prose |
| Hyphen-separated | `PLAY-LEARN-LIFT` not `PLAY_LEARN_LIFT` | Shell-friendly, readable |
| No colons | `POSTEL` not `WP:POSTEL` | Cleaner than Wikipedia |
| Semantic | `ROBUST-FIRST` not `RF` | Self-documenting |

---

## Why This Convention?

### 1. Grep-Friendly

```bash
# Find all uses of a protocol
grep -r "YAML-JAZZ" .

# Find all protocol definitions
grep -r "^[A-Z-]*:" PROTOCOLS.yml

# Find all mentions in docs
grep -rn "POSTEL\|PLAY-LEARN-LIFT" skills/
```

### 2. Vector-Search Friendly

The UPPER-CASE format creates **distinct embeddings**. When you search for "YAML-JAZZ", you get:
- The protocol definition
- Files that reference it
- Examples that demonstrate it

Not general YAML documentation.

### 3. Human-Scannable

In prose, protocols pop:

> When parsing user input, apply POSTEL (charitable interpretation).
> If the command is ambiguous, use YAML-JAZZ to infer intent.

You can't miss them.

---

## Protocol Layers

### Kernel Protocols (Low-Level)

Defined in `kernel/`, fundamental to operation:

| Protocol | Purpose | Location |
|----------|---------|----------|
| `FILES-AS-STATE` | Everything is files | kernel/constitution-core.md |
| `WHY-REQUIRED` | Tool calls need reasons | kernel/tool-calling-protocol.md |
| `APPEND-ONLY` | Never modify logs | kernel/constitution-template.md |
| `MINIMAL-DIFF` | Change only what's needed | kernel/constitution-core.md |

### Skill Protocols (Mid-Level)

Defined in `skills/`, behavioral patterns:

| Protocol | Purpose | Location |
|----------|---------|----------|
| `PLAY-LEARN-LIFT` | The methodology | skills/play-learn-lift/ |
| `SOUL-CHAT` | Everything speaks | skills/soul-chat/ |
| `POSTEL` | Charitable interpretation | skills/postel/ |
| `YAML-JAZZ` | Comments carry meaning | skills/yaml-jazz/ |

### Ad-Hoc Protocols (Emergent)

Mentioned in conversations, examples, documents:

```markdown
# In a soul-chat document
We should apply KITCHEN-RULES here — no running,
always clean up, respect the fridge contents.

# In an adventure room
This room follows GRUE-SAFE protocol — magically lit.
```

These don't need formal definitions. **Naming them makes them real.**

---

## Where Protocols Live

### Central Registry

**[PROTOCOLS.yml](../../PROTOCOLS.yml)** — The master list:

```yaml
YAML-JAZZ:
  meaning: "Comments carry meaning. Data is interpreted."
  location: kernel/constitution-core.md §3
  invoke_when: "Writing or reading YAML with semantic intent"
```

### Embedded in Files

Protocols can be defined inline where they're used:

```yaml
# In a room's ROOM.yml
protocols:
  DARK-ROOM:
    meaning: "No light source = grue danger"
    applies_when: "player enters without lit lamp"
```

### Referenced in Prose

Just mention them:

> This adventure follows REINCARNATION protocol —
> death returns you to start, inventory preserved.

The name IS the definition until someone formalizes it.

---

## Protocol Lifecycle

```
Mentioned → Documented → Formalized → Skill
    ↓            ↓            ↓          ↓
  "Let's       Entry in     Directory   Full
   try          PROTOCOLS    in          PROTOTYPE
   FOOD-CHAIN"  .yml         skills/     + templates
```

Most protocols stay informal. Only crystallize when needed.

---

## Commands

| Command | Action |
|---------|--------|
| `PROTOCOL [name]` | Describe or invoke a protocol |
| `PROTOCOLS` | List defined protocols |
| `DEFINE-PROTOCOL [name]` | Add to PROTOCOLS.yml |
| `GREP-PROTOCOL [name]` | Find all references |

---

## Protocol Symbols

| Symbol | Meaning |
|--------|---------|
| `PROTOCOL` | This meta-protocol |
| `K-LINE` | Minsky's concept — name activates tradition |
| `GREPPABLE` | Easy to find with text search |
| `UPPER-CASE` | The naming convention itself |

---

## Dovetails With

- **[../skill/](../skill/)** — Protocols can become skills
- **[../../PROTOCOLS.yml](../../PROTOCOLS.yml)** — The central registry
- **[../../kernel/](../../kernel/)** — Low-level protocols
- **[../yaml-jazz/](../yaml-jazz/)** — Protocol for semantic YAML
- **[../postel/](../postel/)** — Protocol for charitable interpretation

---

## The Power of Naming

> *"In the beginning was the Word."*

When you name something, you can:
- **Find it** — grep, vector search, memory
- **Invoke it** — type the name, activate the tradition
- **Compose it** — combine named things into new things
- **Teach it** — names are handles for concepts

MOOLLM protocols are handles on ideas. The UPPER-CASE convention makes them **impossible to miss, trivial to find**.

---

*"Name it, grep it, use it."*
