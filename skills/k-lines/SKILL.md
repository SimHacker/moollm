---
name: protocol
description: "Protocol names ARE K-lines."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
related: [moollm, leela-ai, manufacturing-intelligence, society-of-mind, skill, bootstrap, yaml-jazz, markdown, postel, play-learn-lift, sniffable-python, plain-text, knowledge-frames, schema-mechanism, schema]
tags: [moollm, k-lines, minsky, memory, activation, society-of-mind]
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

## Activation: scene and stance, not only a pointer

A K-line is **not** only a compact reference to a concept. In Minsky’s account, activating a K-line tends to **re-instantiate a configuration** that worked before: which sub-skills, tone, and moves to bring online. Henry Minsky put it in terms of a **whole state of mind** (or “scene”) bound to a name—closer to a **re-enterable closure** than to a bare pointer.

That matters in MOOLLM because:

- **Shared index** — `PROTOCOLS.yml`, `skills/INDEX.yml`, and prior turns give the same symbol the same load-bearing role. Without that, a name is noise.
- **Embodied triggers** — A photo, a warning sign, a vocal cue can act like a K-line if the culture around it is shared: they snap attention to a **lived** situation, not a map coordinate.

**Linguistic analogy (not Minsky’s wording, but useful):** In some languages, *am Bahnhof Zoo* vs bare *Bahnhof Zoo* shifts from bare reference toward **situated, insider scene**—the way *the 405* in Los Angeles is not “a highway” but **that** corridor of life. Same mechanism in spirit: **name → thick situation**, not only **name → fact**.

**Optional cultural example:** Nina Hagen’s *Berlin Zoo* (1982) is often read as **performative** activation—noise, animal theatre, West Berlin grit—not as zoology. The track works as a **charged name** for a subculture-tinted “zoo” of people and noise. A zoo sign about a lion spraying urine through bars is thematically on that wavelength: blunt, bodily, public—**scene-first**, not taxonomy-first.

**Contrast:** **Frames** (Minsky) describe the **shape** of a situation (slots, defaults). **Drescher schemas** (see `schema-mechanism`) describe **learned causality** (Context → Action → Result). **Schemapedia** (see `schema`, `schemas/registry.yml`) indexes interchange, causal, frames, activation, relational SQL/SQLite, and SoM—each family with its own delegate skills. **Protocol symbols** here describe **which competence bundle to load**. See `knowledge-frames` for the full map.

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

## K-REFs: File Pointers as K-Lines

A **K-REF** is a K-line that points to a specific location in a file with optional metadata:

```
/path/to/file.md:42-58 # section_type | preview text
```

### K-REF Format

```
PATH[:LINE[-END]][#ANCHOR][?SEARCH] # TYPE [LABEL] SEVERITY - DESCRIPTION
  EXCERPT or MASKED_VALUE
```

Components:
- **PATH** — Absolute file path (if no line number, refers to whole file)
- **LINE** — Line number (1-based), optionally with column `:LINE:COL`. Omit for whole file.
- **END** — Optional end line or column for ranges
- **#ANCHOR** — Jump to heading/section (like URL fragments)
- **?SEARCH** — Find first match of pattern (like URL query)
- **TYPE** — What was found (uuid, secret, user_prompt, tool_call, etc.)
- **LABEL** — Optional redact label like `[SSH_KEY]`
- **SEVERITY** — Icon: 🔴 critical, 🟠 high, 🟡 medium, 🔵 low, ℹ️ info
- **DESCRIPTION** — Human-readable explanation
- **EXCERPT** — Surrounding context or masked value

### Location Specifiers

| Format | Meaning | Example |
|--------|---------|---------|
| `/path/file` | Whole file | `/etc/config.yml` |
| `/path/file:42` | Line 42 | `/src/main.py:42` |
| `/path/file:42-58` | Lines 42-58 | `/src/main.py:42-58` |
| `/path/file:42:10-46` | Line 42, cols 10-46 | `/src/main.py:42:10-46` |
| `/path/file#section` | Anchor/heading | `/docs/API.md#authentication` |
| `/path/file?pattern` | Search for pattern | `/src/main.py?def process_data` |
| `/path/file#section?pattern` | Section + search | `/docs/API.md#errors?401` |

### Anchor Types

```
# Markdown headings (slugified)
/README.md#installation
/SKILL.md#k-ref-format

# YAML keys (dot-path)
/config.yml#server.port
/CARD.yml#methods.K-REF

# Code symbols (function/class)
/main.py#def:process_data
/main.py#class:AuditRunner

# HTML-style id
/page.html#footer
```

### Search Patterns

```
# Literal string (default)
/file.py?def main

# Regex (prefix with ~)
/file.py?~def\s+\w+\(

# First match of pattern
/transcript.txt?user: 

# Combine with line context
/file.py?def main # function - Jump to main()
```

### Examples

```
/path/to/config.yml # config - Whole file reference
/path/to/SKILL.md#k-refs # section - Jump to K-REFs section
/path/to/main.py?def audit # search - Find audit function
/path/transcript.txt:91:12-48 # uuid ℹ️
  fe18ce96-5200-4e15-acd3-190695de6295

/path/transcript.txt:7528:18-45 # private_key ([PRIVATE_KEY]) 🔴 - Private key header
  ********** ******* ********

/path/config.json:15 # password ([PASSWORD]) 🟠 - Database password
  ************
```

### Images Work Too!

Cursor (and other orchestrators) can read absolute file paths directly — **INCLUDING IMAGES**!

```
/Users/me/Screenshots/error.png # screenshot - Analyze this error
/tmp/architecture-diagram.jpg # diagram - Explain this system
/path/to/chart.png # data - What trends do you see?
```

No line numbers for images (obviously). Just the absolute path.

**This is powerful:**
- Point to any image on disk
- Cursor reads and analyzes it
- Works with screenshots, diagrams, charts, photos
- Supports: jpeg, png, gif, webp

**Security note:** Cursor can read ANYWHERE on your disk, not just the workspace. Powerful, but be aware.

### Sister Script Methodology

**Problem**: LLMs have limited context windows. Dumping entire files wastes tokens.

**Solution**: Sister scripts emit K-REFs (pointers) instead of full content:

```yaml
# Sister script → K-REF → LLM flow
kref_flow:
  source: "cursor-mirror (sister script)"
  produces: "K-REFs (pointers)"
  consumer: "LLM reads only what it needs"
```

1. **Scan** — Script searches large data (transcripts, databases)
2. **Emit** — Output K-REFs pointing to relevant sections
3. **Read** — LLM selectively reads only the referenced ranges

This is **reference by pointer, not by value** — parsimonious context.

### K-REF Output Modes

| Mode | Command | Use Case |
|------|---------|----------|
| K-REF | `--emit-kref` | Human/LLM navigation |
| REDACT | `--emit-redact` | Pipe to masking tool |
| JSON | `--json` | Programmatic processing |

### Example: cursor-mirror as Sister Script

```bash
# Emit K-REFs for secrets (LLM reads just the pointers)
cursor-mirror audit --patterns secrets --emit-kref

# Output:
# /path/file.txt:42:10-46 # openai_key ([OPENAI_KEY]) 🔴 - OpenAI API key
#   sk-proj-****...(48 chars)...****

# LLM can then selectively read context around line 42
```

## Commands

| Command | Action |
|---------|--------|
| `PROTOCOL [name]` | Describe or invoke a protocol |
| `PROTOCOLS` | List defined protocols |
| `DEFINE-PROTOCOL [name]` | Add to PROTOCOLS.yml |
| `GREP-PROTOCOL [name]` | Find all references |
| `K-REF [path:line]` | Navigate to a K-REF location |

---

## Protocol Symbols

| Symbol | Meaning |
|--------|---------|
| `PROTOCOL` | This meta-protocol |
| `K-LINE` | Minsky's concept — name activates tradition |
| `K-REF` | K-line as file pointer: path:line + metadata |
| `SISTER-SCRIPT` | Tool emits K-REFs, LLM reads selectively |
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
