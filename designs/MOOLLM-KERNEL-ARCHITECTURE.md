# MOOLLM Kernel Architecture

> *"The orchestrator is the Operating System. The LLM is the Coherence Engine. The Repo is the Microworld."*

---

## Overview

This document captures the **philosophy and design rationale** behind the MOOLLM kernel. The kernel itself (`kernel/`) contains lean operational files; this document explains *why* they work the way they do.

**See also:**
- `kernel/README.md` — Kernel quick reference
- `kernel/drivers/README.md` — Driver structure
- `skills/skill/SKILL.md` — How skills relate to kernel

---

## The Three Layers

```
┌─────────────────────────────────────────────────────┐
│  USERLAND (skills/)                                 │
│  Soul chat, rooms, cards, advertisements, games     │
│  → Semantic meaning, application logic              │
├─────────────────────────────────────────────────────┤
│  KERNEL (kernel/)                                   │
│  Tools, context assembly, memory, repair, logging   │
│  → Infrastructure, plumbing, adaptation             │
├─────────────────────────────────────────────────────┤
│  HARDWARE (LLM + Orchestrator)                      │
│  Stateless token predictor + context management     │
│  → Raw computation, I/O                             │
└─────────────────────────────────────────────────────┘
```

The kernel provides **infrastructure**, not **semantics**. It doesn't know what "rooms" or "soul chat" mean — that's userland's job.

---

## Orchestrator Types: Smart vs Generic

### The Core Distinction

**Generic Orchestrators** (like Cursor, ChatGPT):
- Cannot parse MOOLLM-specific files
- Don't understand CARD.yml advertisements
- Can't inject ambient skills automatically
- The LLM must manually manage context

**Smart Orchestrators** (like MOOCO, custom implementations):
- Parse CARD.yml advertisements directly
- Inject ambient skills invisibly into context
- Manage hot/cold/working-set operationally
- Keep administrative infrastructure out of LLM's context window

### The Magic Dictionary Analogy

Smart orchestrators work like **NeWS PostScript magic dictionaries**:

In NeWS (Network extensible Window System), PostScript dictionaries like `processes`, `canvases`, and `events` appeared to be normal data structures but were actually backed by the window system. Reading from them triggered system queries; writing to them triggered system calls. The code didn't need to know — it just manipulated dictionaries.

Similarly, a smart MOOLLM orchestrator:
- Reads `CARD.yml` advertisements and activates matching skills
- Watches `hot.yml` / `working-set.yml` for context hints
- Injects ambient skills without the LLM explicitly requesting them
- Makes edits to these files "magically effect" orchestrator behavior

The **same skill files work on both orchestrator types** — the mechanism adapts:
- On generic orchestrators: LLM reads files manually, self-manages context
- On smart orchestrators: Orchestrator reads files, injects automatically

### Advisory Mode vs Operational Mode

| Feature | Generic (Advisory) | Smart (Operational) |
|---------|-------------------|---------------------|
| `hot.yml` | Documentation of what SHOULD be prioritized | Actually loaded into context |
| `cold.yml` | Breadcrumbs for archaeology | Actually evicted from context |
| `working-set.yml` | Self-documentation | Active context manifest |
| Ambient skills | LLM must manually load | Injected invisibly |
| CARD advertisements | Read on demand | Parsed and activated |

### Reverse Generation Pattern

On generic orchestrators, these files can work **in reverse**:
- Instead of commanding what to load, they **document what Cursor loaded**
- Generate them to reflect what the orchestrator's attention is focused on
- The files become **mirrors** rather than **commands**

---

## Driver Architecture

### What Drivers Do

Drivers adapt the MOOLLM constitution to specific orchestrators — like OS drivers adapt to different hardware.

A driver specifies:
1. **Detection** — How to identify this orchestrator
2. **Capabilities** — What features are available
3. **Tools** — Mapping abstract operations to concrete tool names
4. **Paths** — Where to store session files
5. **Adaptations** — Fallbacks for unsupported features
6. **Limits** — Token limits, file limits, etc.

### Driver Tiers

| Tier | Description | Example |
|------|-------------|---------|
| 1 | Minimal — bare essentials | `generic.yml` |
| 2 | Basic — read/write/terminal | Basic CLI |
| 3 | Standard — search, some MCP | ChatGPT |
| 4 | Advanced — full file ops, MCP | Cursor |
| 5 | Premium — custom tools, full MCP | Claude Code, Antigravity |
| 6 | Custom — full kernel control | MOOCO |

### Capability Graceful Degradation

When a feature isn't available, drivers specify fallbacks:

| Feature | Full Support | Fallback |
|---------|-------------|----------|
| `why` parameter | Include in tool call | Document intent in response |
| Append-only | Enforced by orchestrator | Convention only |
| Event logging | Structured YAML | Markdown narrative |
| Vector search | `SemanticSearch` | Grep/manual scan |
| Sandboxed exec | Isolated container | Trust-based |

---

## Context Assembly

### The Problem

LLMs are stateless — they don't remember previous turns unless you include them in the prompt. The orchestrator must **assemble context** from:
- Conversation history
- File contents
- Search results
- Tool outputs
- Session state

### MOOLLM's Approach

The kernel provides **context assembly protocol** (`kernel/context-assembly-protocol.md`):

1. **Working Set** — Files currently relevant
2. **Hot Cache** — High-priority items to keep loaded
3. **Cold Cache** — Items recently evicted (breadcrumbs)
4. **Summaries** — Compressed representations of large content

On generic orchestrators, these are **advisory** — the LLM consults them to remind itself what to load. On smart orchestrators, they're **operational** — the orchestrator reads them and assembles context automatically.

---

## Memory Management

### Hot/Cold Model

Inspired by CPU cache hierarchies:

```
┌─────────────────────────────────────────┐
│  CONTEXT WINDOW (~30K tokens)           │
│  What the LLM can see RIGHT NOW         │
├─────────────────────────────────────────┤
│  HOT CACHE (.moollm/hot.yml)            │
│  High-priority items to keep loaded     │
│  "Page these in frequently"             │
├─────────────────────────────────────────┤
│  WARM (working-set.yml)                 │
│  Currently relevant files               │
│  "These are my focus right now"         │
├─────────────────────────────────────────┤
│  COLD CACHE (.moollm/cold.yml)          │
│  Recently evicted items                 │
│  "I used to care about these"           │
├─────────────────────────────────────────┤
│  REPO (files on disk)                   │
│  Everything else                        │
│  "I can page this in if needed"         │
└─────────────────────────────────────────┘
```

### Resolution Hints

Skills can declare **resolution levels** in their CARD.yml:
- `activation_only` — Just check if skill applies
- `summary` — Read CARD.yml header
- `interface` — Read CARD.yml fully
- `implementation` — Read SKILL.md
- `full` — Read everything including README.md

This lets the LLM (or orchestrator) know how deep to page in.

---

## Ambient Skills

### What Are Ambient Skills?

Skills that should be **always present** in context, continuously influencing behavior. Examples:
- `no-ai-slop` — Suppress filler language
- `yaml-jazz` — Treat YAML comments as semantic data
- `representation-ethics` — Guidelines for simulating real people

### The Injection Problem

On generic orchestrators, the LLM must:
1. Know that ambient skills exist
2. Remember to load their CARD.yml
3. Keep them in hot.yml for persistence
4. Re-load them if context is cleared

On smart orchestrators:
1. Orchestrator parses CARD.yml advertisements
2. Finds skills with `type: AMBIENT`
3. Injects them into every context assembly
4. LLM never has to think about it

### Same Files, Different Mechanism

The beauty: **same CARD.yml works both ways**:

```yaml
# In any skill's CARD.yml
advertisements:
  - trigger: "*"           # Matches everything
    score: 0.3             # Low but always present
    type: AMBIENT          # Smart orchestrators auto-inject
    resolution: summary    # Just the header
```

- Generic orchestrator: LLM reads this, knows to keep it loaded
- Smart orchestrator: Parses this, auto-injects skill

---

## Introspection

### cursor-mirror Skill

The `skills/cursor-mirror/` skill enables **meta-cognition** — the LLM watching itself think.

```bash
cursor-mirror status          # Quick health check
cursor-mirror tree            # Navigate sessions
cursor-mirror thinking @1     # Watch reasoning blocks
cursor-mirror tools @1        # Trace tool calls
cursor-mirror deep-snitch     # Security audit
```

This is especially powerful on Cursor, where the skill can:
- Read conversation history from LevelDB
- Analyze boot sequences
- Track tool call patterns
- Debug context assembly

### Introspection on Other Orchestrators

The same introspection **concept** applies everywhere, but implementation varies:
- Cursor: Deep LevelDB access via cursor-mirror
- Claude Code: MCP history access
- Custom: Whatever the orchestrator exposes

---

## The Coherence Engine

The LLM isn't just generating text. It's:

1. **Computing Dependencies** — Figuring out what depends on what
2. **Cross-Checking State** — Verifying consistency against rules
3. **Refereeing Conflicts** — Resolving parallel agent disagreements
4. **Orchestrating Simulations** — Running many characters per call
5. **Maintaining Consistency** — Keeping the microworld coherent

The kernel provides the **infrastructure** for this; skills provide the **semantics**.

---

## Design Principles

### From Unix

- Simple tools that compose
- Text as universal interface
- Convention over configuration

### From Self Language

- Prototypes and delegation
- Objects clone, not instantiate
- Everything is mutable

### From Robust-First Computing (Dave Ackley)

- Missing state → repair, not crash
- Local information, global behavior
- Homeostatic maintenance

### From Kay/Papert

- Microworld as operating system
- The repo IS the world
- Learning through exploration

### From NeWS

- Magic dictionaries as system interface
- Code that doesn't know it's talking to the system
- Same API, different backing implementation

---

## File Organization

```
kernel/
├── README.md                    # Quick reference
├── constitution-core.md         # Universal principles
├── constitution-template.md     # Full constitution template
├── context-assembly-protocol.md # How context is built
├── memory-management-protocol.md# Hot/cold/working-set
├── event-logging-protocol.md    # Append-only logging
├── self-healing-protocol.md     # Repair and recovery
├── tool-calling-protocol.md     # How tools work
├── NAMING.yml                   # Naming conventions
├── naming/                      # Detailed naming docs
│   ├── NAMING-K-LINES.yml       # Names as K-lines
│   ├── NAMING-RELATIONSHIPS.yml # See-also annotations
│   └── ...
├── drivers/
│   ├── README.md                # Driver docs
│   ├── cursor.yml               # Cursor IDE adapter
│   ├── claude-code.yml          # Claude Code adapter
│   ├── antigravity.yml          # Antigravity adapter
│   ├── generic.yml              # Fallback adapter
│   └── custom.yml               # Full-control template
└── ...
```

---

## See Also

| Topic | Location |
|-------|----------|
| Kernel quick reference | `kernel/README.md` |
| Driver structure | `kernel/drivers/README.md` |
| Skill architecture | `skills/skill/SKILL.md` |
| CARD.yml format | `skills/card/CARD.yml` |
| Advertisement system | `skills/advertisement/CARD.yml` |
| Context assembly | `kernel/context-assembly-protocol.md` |
| Memory management | `kernel/memory-management-protocol.md` |
| cursor-mirror skill | `skills/cursor-mirror/CARD.yml` |
| MOOCO orchestrator | `designs/MOOCO-ARCHITECTURE.md` (in mooco repo) |

---

*"Make the kernel boring so the skills can be exciting."*
