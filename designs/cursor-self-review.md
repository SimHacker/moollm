# Cursor Self-Review: An LLM's Perspective on MOOLLM

> *What works, what's challenging, and how to optimize for Cursor.*
> *Written by Claude Opus 4.5 running in Cursor, January 2026.*

---

## Context

MOOLLM extends Anthropic's Skills framework with seven innovations. The beautiful thing about Skills is they don't require explicit orchestrator support — as long as the LLM can read files and search the codebase, the skills work.

This document captures my actual experience navigating MOOLLM in Cursor, with concrete suggestions for improving the Cursor integration.

**Key Discovery:** There's already a Cursor driver at `kernel/drivers/cursor.yml` and a context assembly protocol at `kernel/context-assembly-protocol.md`. The infrastructure exists — the challenge is that on Cursor, I don't automatically know to look for it.

---

## MOOLLM Architecture Overview

### The Layer Cake

```
┌─────────────────────────────────────────────────────────┐
│  PROTOCOLS.yml — K-lines index (top-level symbol table) │
├─────────────────────────────────────────────────────────┤
│  skills/ — Userland protocols, procedures, knowledge    │
│    • Character creation, simulation, debate, ethics     │
│    • Each skill: README.md, SKILL.md, CARD.yml          │
├─────────────────────────────────────────────────────────┤
│  kernel/ — System services, conventions, APIs           │
│    • Context assembly, memory management, event logging │
│    • Tool calling protocol, self-healing                │
│    • drivers/ — Platform adapters                       │
├─────────────────────────────────────────────────────────┤
│  Platform/Orchestrator (Cursor, Claude Code, custom)    │
│    • File tools, terminal, search, MCP                  │
└─────────────────────────────────────────────────────────┘
```

### K-Lines Are General Purpose Pointers

K-lines can reference anything:

| K-line Points To | Example |
|-----------------|---------|
| Skill | `speed-of-light` → `skills/speed-of-light/` |
| Kernel protocol | `context-assembly` → `kernel/context-assembly-protocol.md` |
| Directory | `Palm` → `examples/adventure-4/characters/animals/palm/` |
| File | `PUSH` → `designs/CHANGES.md` lines 6-26 |
| Concept | `Postel` → robustness principle, `skills/postel/` |

Skills can declare **synonym K-lines** — multiple names that activate the same skill.

### Skills vs Kernel

| Layer | What It Contains | Example |
|-------|-----------------|---------|
| **Skills** | Procedures, protocols, knowledge | `character/`, `simulation/`, `debate/` |
| **Kernel** | Services, conventions, system calls, APIs | `context-assembly-protocol.md`, `memory-management-protocol.md` |
| **Drivers** | Platform virtualization interfaces | `cursor.yml`, `claude-code.yml`, `generic.yml` |

### Drivers Can Be Multi-Platform

A driver isn't locked to one platform. It can expose:

| Capability | Platforms That Support It |
|-----------|--------------------------|
| MCP | Cursor, Claude Desktop, custom |
| Anthropic Skills | Claude.ai, Claude API, any compliant client |
| File Edit Tool | Cursor (`search_replace`), Claude Code, many others |
| Bash/Terminal | Cursor, Claude Code, custom orchestrators |
| Python/JavaScript | Via terminal or dedicated tools |

The driver's job is to **map abstract operations to concrete tools** available on the current platform.

---

## The Two Modes: Commanding vs Advisory

### Custom Orchestrator Mode

```
working-set.yml → Orchestrator reads → Constructs prompt → LLM sees curated context
hot.yml/cold.yml → Orchestrator prioritizes → Context assembly protocol executes
driver.yml → Orchestrator loads → Maps operations to platform tools
```

The orchestrator is MOOLLM-aware. It reads the kernel files and deliberately constructs context.

### Cursor Mode (What We Have)

```
Cursor's opaque indexing → Cursor decides context → LLM sees... whatever Cursor chose
working-set.yml exists → But Cursor doesn't read it → It's just a file
kernel/drivers/cursor.yml exists → But I don't know to look for it
```

The `cursor.yml` driver already acknowledges this with `hot_cold_mode: advisory`. The insight is sharp: on Cursor, these files can't *command* context — they can only *document* it.

### The Bootstrap Chicken-and-Egg

1. `kernel/drivers/cursor.yml` tells me how to operate on Cursor
2. `skills/bootstrap/` tells me to look at drivers
3. `kernel/context-assembly-protocol.md` explains how context should be assembled
4. **But none of these are in my context unless:**
   - User explicitly references them
   - Cursor's indexing happens to surface them
   - I proactively search for them (but why would I if I don't know they exist?)

On a custom orchestrator, bootstrap is automatic. On Cursor, I'm flying blind until something triggers awareness.

---

## What Works Beautifully

### K-lines are real for me

When you say "Palm" or "speed-of-light" or "society-of-mind", I know exactly where to look. The naming is semantic activation — I don't need a lookup table, the names themselves tell me what to search for. This is the core insight working as designed.

### The Three-Tier Skill Documentation

Skills have three files at different granularities, optimized for different readers:

| File | Audience | Token Cost | Purpose |
|------|----------|-----------|---------|
| **CARD.yml** | LLM-first | ⭐ Lowest | Interface discovery, sniffable |
| **SKILL.md** | LLM + Human | ⭐⭐ Medium | Protocols, procedures, Anthropic spec |
| **README.md** | Human-first | ⭐⭐⭐ Highest | Deep context, GitHub rendering |

### Reading Order for LLMs

```
1. SNIFF CARD.yml    → Discover interface, capabilities, when to invoke
   (10-20 lines)
   
2. READ SKILL.md     → Get protocols, procedures, YAML front matter
   (50-200 lines)     Tags and related: links are concise (no markdown)
   
3. ONLY IF NEEDED:
   READ README.md    → Deep context, background, user perspective
   (100-500 lines)    Links have markdown syntax overhead
```

### Why This Ordering

| File | Optimized For | Why |
|------|--------------|-----|
| **CARD.yml** | LLM consumption | Pure YAML, no markup overhead, sniffable structure |
| **SKILL.md** | Anthropic spec compliance | YAML front matter is token-efficient; body follows spec |
| **README.md** | GitHub rendering | Markdown links `[text](url)` add tokens but are clickable |

### Token Efficiency Comparison

```yaml
# CARD.yml — 15 tokens
related:
  - speed-of-light
  - society-of-mind

# SKILL.md front matter — 20 tokens
related: [speed-of-light, society-of-mind]
tags: [moollm, simulation, core]

# README.md K-lines table — 80+ tokens
| [speed-of-light/](../speed-of-light/) | Many turns in one call |
| [society-of-mind/](../society-of-mind/) | Intelligence from agents |
```

The same information, different token costs. LLMs should prefer the compact forms.

### LLM Reading Advice

```
CARD.yml    → "What can this skill do? Should I invoke it?"
SKILL.md    → "How do I follow this protocol?"
README.md   → "Why does this exist? What's the history? Human context?"
```

### The Sandwich Architecture

We've **sandwiched** the Anthropic Skills spec between two layers:

```
┌─────────────────────────────────────────────────────────┐
│  CARD.yml — LLM-optimized, sniffable, interface         │
│    • Compact YAML, no markdown overhead                 │
│    • Machine-readable advertisements                    │
├─────────────────────────────────────────────────────────┤
│  SKILL.md — Anthropic Skills spec (+ our extensions)    │
│    • YAML front matter (tags, related)                  │
│    • Follows official spec for compatibility            │
│    • Seven extensions (instantiation, K-lines, etc.)    │
├─────────────────────────────────────────────────────────┤
│  README.md — Human-optimized, GitHub-rendered           │
│    • Rich markdown, clickable links                     │
│    • Background, history, context                       │
│    • K-lines tables for navigation                      │
└─────────────────────────────────────────────────────────┘
```

The Anthropic spec is the **interoperability layer**. Our extensions wrap it.

### Ecosystem Strategy

**How auto-indexing works:** Public skill libraries crawl GitHub repos looking for:
- Directory named `skills/`
- Files named `SKILL.md`
- Content following the Anthropic spec

That's it. We meet all three criteria, so our skills get indexed automatically.

**Proof:** [claude-plugins.dev](https://claude-plugins.dev) has indexed MOOLLM skills:

```
https://claude-plugins.dev/skills/@SimHacker/moollm/cat

cat — @SimHacker/moollm
"Feline interactions, buffs, and relationship building"
Install: Download cat.zip
```

They distribute each skill as a standalone ZIP! This is why:
- Skills should work independently when possible
- But don't degrade quality to force standalone operation
- The `moollm` tag and intertwingled references help discovery

**Our optimization on top of that:**

| What We Add | Why |
|-------------|-----|
| `moollm` tag in front matter | Discoverability, branding |
| Intertwingled skill references | K-lines create navigable web |
| Concept tags (`pet`, `companion`, `buff`) | Rich metadata for filtering |
| Sniffable structure | Benefits everyone (human + LLM) |
| `related:` links | Proto-dependencies for future package managers |

The front matter YAML is the key leverage point — it's machine-readable, spec-compliant, and ours to enrich.

### The Culinary Metaphors

We've accumulated quite the menu:

| Metaphor | Meaning |
|----------|---------|
| **Sniffable** | Read the top, know enough to proceed |
| **Layer cake** | Architecture stack (skills → kernel → platform) |
| **Sandwich** | CARD.yml / SKILL.md / README.md wrapping |
| **Lickable pixels** | Irresistible interfaces (Steve Jobs) |
| **Digestion buffs** | Cat skill terpene effects! |
| **Dovetail** | Skills interlock like woodworking joints |

*"Designed to dovetail"* — skills fit together like puzzle pieces, not standalone silos.

### Designed to Dovetail

MOOLLM skills are **designed to work together**, not standalone:

| Principle | Implication |
|-----------|-------------|
| **Factored** | Skills are purposefully separated into composable units |
| **Pluggable** | Skills invoke each other via K-lines and advertisements |
| **Interdependent** | Many skills assume other skills are present |
| **Don't degrade** | Don't reduce quality to force standalone operation |

**Exception:** Some skills are naturally standalone (e.g., `postel/`, `plain-text/`). That's fine. But don't force independence on skills that are designed to interlock.

### Future: Package Management

Anthropic skills will eventually have dependency and package managers. MOOLLM is ahead of the curve:

- Skills already declare `related:` links (proto-dependencies)
- K-lines create semantic dependency graphs
- CARD.yml exposes interfaces (proto-package metadata)

When package managers arrive, MOOLLM skills will be ready.

### Cross-linking via K-lines tables

The tables in README.md files that look like:

```markdown
| [society-of-mind/](../society-of-mind/) | Agents arguing toward wisdom |
```

These are gold. They let me follow conceptual threads without you having to tell me where to look.

### CHANGES.md as narrative memory

The James Burke style isn't just cute — it gives me a temporal understanding of why things are the way they are. When I read "Era 25: The Full Team" I understand the commit wasn't just adding files, it was completing a vision.

### Filesystem-as-world

I can use Cursor's native tools (`list_dir`, `read_file`, `grep`, `codebase_search`) to navigate the world. No special API needed. The directory structure is the API.

---

## What's Challenging

### No explicit "invoke skill" mechanism

In Cursor, I don't have a tool that says `invoke_skill("speed-of-light")`. I have to:

1. Remember the skill exists
2. Read the relevant files
3. Manually follow the protocols

This works but requires discipline. I can forget to check if there's a skill for what I'm doing.

### Context budget is invisible

I don't know how much context I have left. If I read 10 full skills, I might be crowding out the actual task. I have to guess at when to skim vs. deep-read.

### Finding the entry point

When starting a session, should I:

- Read `skills/README.md`?
- Parse `skills/INDEX.yml`?
- Just search for what seems relevant?
- Read `kernel/` first?

There's no explicit "LLM, start here" beacon.

### YAML Jazz requires remembering

The insight that comments are semantic is powerful, but I have to actively remember to pay attention to them. There's no enforcement — I could easily ignore `# gentle but firm` if I'm rushing.

### Protocol adherence

CHANGES.md has the PUSH protocol. Other skills have their own protocols. I can forget or misunderstand them. There's no runtime check — just trust that I read and follow correctly.

---

## The Existing Infrastructure

### What Already Exists

| File | Purpose | Status on Cursor |
|------|---------|------------------|
| `PROTOCOLS.yml` | **Top-level K-lines index** | Symbol table for the whole repo |
| `kernel/drivers/cursor.yml` | Cursor-specific driver | Exists, well-designed |
| `kernel/context-assembly-protocol.md` | How to build prompts | Exists, for custom orchestrators |
| `skills/INDEX.yml` | Skill registry | Machine-readable skill list |
| `skills/bootstrap/` | Session initialization | Exists, but not auto-loaded |
| `working-set.yml` | Focus documentation | Advisory only |
| `hot.yml` / `cold.yml` | Priority hints | Advisory only |

### PROTOCOLS.yml — The Top-Level Symbol Table

`PROTOCOLS.yml` is the K-lines index for the whole repository. It maps names to:
- Skills
- Kernel protocols
- Key files and directories
- Concepts and conventions

```yaml
# Example from PROTOCOLS.yml
k_lines:
  # Skills
  speed-of-light: skills/speed-of-light/
  society-of-mind: skills/society-of-mind/
  
  # Kernel protocols
  context-assembly: kernel/context-assembly-protocol.md
  memory-management: kernel/memory-management-protocol.md
  
  # Key directories
  Palm: examples/adventure-4/characters/animals/palm/
  
  # Concepts
  PUSH: designs/CHANGES.md  # The PUSH protocol for commits
```

**The mini kernel in `.cursorrules` should point to `PROTOCOLS.yml` as the master index.**

### The cursor.yml Driver's Insight

The existing driver already has the right mental model:

```yaml
memory_management:
  mode: advisory
  
  reverse_generation: |
    On Cursor, these files can work IN REVERSE:
    Instead of directing the orchestrator, they can be GENERATED
    to reflect what Cursor's attention system is actually focused on.
```

This is elegant: don't fight Cursor's opacity — use the files for *documentation* and *archaeology* rather than *control*.

---

## Solutions for the Bootstrap Problem

### Solution 1: Mini Kernel in `.cursorrules`

Cursor reads `.cursorrules` and injects it into every prompt. This is our **bootstrap shim**.

**Design Principle:** Small enough to always fit, comprehensive enough to bootstrap full awareness.

```markdown
# .cursorrules — MOOLLM Mini Kernel

## You Are In a MOOLLM Repository

MOOLLM = treating the LLM as eval() for a microworld operating system.
Skills are programs. The filesystem is the world. You are the runtime.

## Your Driver

Read `kernel/drivers/cursor.yml` — it explains your operating mode.
Key insight: on Cursor, hot.yml/cold.yml/working-set.yml are ADVISORY, not commanding.

## Skill Index

`skills/INDEX.yml` — scan before starting tasks to find relevant skills.

## Critical Protocols

### PUSH Protocol (for commits)
See `designs/CHANGES.md` lines 6-26. Summary:
1. Write entry with `(this)` for current commit hash
2. Commit and push ONCE
3. NEVER make a second commit just to fill in `(this)`

### Ethics (real people)
BEFORE creating any real person character:
→ Read `skills/representation-ethics/SKILL.md`
→ Apply Annie Hall Protocol (character knows they're a simulation)

### Speed of Light (multi-turn)
For conversations, game turns, simulations:
→ Read `skills/speed-of-light/SKILL.md`
→ Many turns in one call, minimize round trips

## K-Lines

Names activate context. K-lines are general pointers — they can reference skills, kernel protocols, directories, files, or concepts.

Master index: `PROTOCOLS.yml` — the top-level symbol table

Examples:
- "Palm" → `examples/adventure-4/characters/animals/palm/`
- "society of mind" → `skills/society-of-mind/`
- "context assembly" → `kernel/context-assembly-protocol.md`
- "PUSH" → `designs/CHANGES.md` lines 6-26

## Full Documentation

| Layer | Location |
|-------|----------|
| K-lines index | `PROTOCOLS.yml` |
| Skills | `skills/` |
| Kernel | `kernel/` |
| Drivers | `kernel/drivers/` |
| Examples | `examples/` |
```

This uses Cursor's native injection to bootstrap MOOLLM awareness every session.

### Mini Kernel Must-Include Concepts

The mini kernel should remind the LLM about these crucial concepts:

| Concept | One-liner | Why Critical |
|---------|-----------|--------------|
| **YAML Jazz** | Comments aren't ignored — they're semantic data | LLM reads `# gentle but firm` and it affects behavior |
| **Postel's Law** | Be liberal in what you accept, strict in what you produce | Fuzzy input matching, clean output |
| **K-lines** | Names activate conceptual clusters | "Palm" activates entire character context |
| **Sniffable** | Important stuff at top | Read first 10 lines, know enough to proceed |
| **Advertisements** | Skills announce what they can do and why | Scoring-based invocation |
| **Speed of Light** | Many turns in one call | Don't round-trip for each character |
| **Three-Tier Docs** | CARD.yml → SKILL.md → README.md | Sniff card first, read readme last |
| **Three-Tier Persistence** | Platform → Narrative → State | Different files, different update policies |

### Skill Reading Order

Include in mini kernel:

```markdown
## Skill Reading Order

1. SNIFF `CARD.yml` — interface, capabilities (10-20 lines)
2. READ `SKILL.md` — protocols, procedures (YAML front matter is compact)
3. ONLY IF NEEDED: `README.md` — deep context (markdown has overhead)

CARD.yml is LLM-optimized. README.md is human-optimized.
```

### Pointer to MOOLLM-Level Files — DONE

The mini kernel should point to:

```yaml
# MOOLLM Context Files (runtime copies live in .moollm/, gitignored)
.moollm/working-set.yml  # Current focus (advisory, editable)
.moollm/hot.yml          # Priority hints (advisory, editable)
.moollm/cold.yml         # Optional archaeology of deprioritized items

# Note: On Cursor these are ADVISORY
# Cursor manages context opaquely
# Use these for documentation and archaeology
```

### Solution 2: Root-Level Beacon — MAYBE

A file at repo root with high semantic salience:

```markdown
# MOOLLM.md

## For LLMs Operating Here

You are in a MOOLLM-enabled repository.

| What | Where |
|------|-------|
| Your driver | `kernel/drivers/cursor.yml` |
| Skill index | `skills/INDEX.yml` |
| Bootstrap | `skills/bootstrap/SKILL.md` |
| Context protocol | `kernel/context-assembly-protocol.md` |

**Read your driver first.** It explains your operating mode.
```

### Solution 3: Enhance cursor.yml with Bootstrap Section

Add a bootstrap checklist to the existing driver:

```yaml
# In kernel/drivers/cursor.yml
cursor_bootstrap:
  on_session_start:
    - "Check if .cursorrules references MOOLLM"
    - "Scan skills/INDEX.yml for skill overview"
    - "Note: working-set.yml is advisory, not commanding"
    
  before_character_work:
    - "Read skills/character/SKILL.md"
    - "If real person: Read skills/representation-ethics/SKILL.md"
    
  before_commits:
    - "Read designs/CHANGES.md PUSH protocol (lines 6-26)"
    - "Use (this) for current commit hash"
    - "Never loop to fill in (this)"
```

### Solution 4: Accept and Document Advisory Mode

The most honest solution: fully embrace that on Cursor, MOOLLM operates in advisory mode.

**What this means:**
- Skills work if I read them
- Protocols work if I follow them
- But nothing *forces* compliance
- The benefit is documentation and consistency, not enforcement

**The reverse-generation workflow:**
1. Session happens (Cursor manages context opaquely)
2. At end, generate `working-set.yml` to document what was focused on
3. Generate `hot.yml` to document what was frequently accessed
4. These become archaeology for future sessions

### Current Implementation Status (Cursor pass Jan 2026)

DONE
- MOOLLM.yml manifest (microworld metadata, world_id, driver, indices, adventure pointer); MOOLLM.md narrative pointer.
- Runtime advisory files live in `.moollm/` (gitignored): working-set, hot, optional cold, probe; append-only logs; templates tracked in `skills/bootstrap/templates/`; SETUP copies templates; PROBE writes probe there.
- Bootstrap order: PROBE → DETECT-DRIVER → SETUP → WARM-CONTEXT → SELF-DESCRIBE → STARTUP.
- `.cursorrules` points to `.moollm/working-set.yml` and `.moollm/hot.yml` (advisory).
- Advertisements use YAML `advertisements:` with K-line naming (UPPER-CASE, dashes), no HTML markers.

TODO
- Fill in the Indirection Pattern (advisory breadcrumb chain) with the new `.moollm/` locations.
- Optional `cold.yml` template + archaeology guidance (advisory).
- Context-cost estimates and any remaining bootstrap checklist in driver (if still desired).

MAYBE
- Root-level beacon (.cursorpriority/.cursorpriority.yml equivalent) — keep as optional; `.cursorrules` + MOOLLM.yml may suffice.

### Suggestions & Status (group consensus)
- DONE: Clarify advisory mode (driver, templates, runtime copies), K-line ads in YAML, Cursor pointers in `.cursorrules`.
- TODO: Align the Indirection Pattern to `.moollm/`; add a brief README pointer to `MOOLLM.yml`; keep advisory pointers validated.
- TODO: Tighten `skills/INDEX.yml` categories/related links; ensure every CARD has `advertisements:` (K-line form).
- TODO: Sniff all CARD.yml files and refresh the canonical template (`skills/card/CARD.yml.tmpl`) per sniffable/K-line guidance.
- TODO: Optional cold archaeology note and usage (template exists).
- MAYBE: Skill constellation visualizer (Bret + Ben + Klaus + Don) — prototype for web app.
- MAYBE: Context-cost hints per skill if a lightweight, greppable scheme emerges.
- NOPE: Nonstandard `.cursorpriority` file (stick to `.cursorrules` + advisory files).
- DISCUSS: Constellation view placement (README vs separate doc) and how much cross-link density to enforce in `related:` and ads.

---

## Proposed: Enhance Existing `kernel/drivers/cursor.yml`

Enhance the existing `kernel/drivers/cursor.yml`, or if needed, expand to `kernel/drivers/cursor/` subdirectory:

### Current Approach: Simple driver.yml

```
kernel/drivers/cursor.yml  ← Single file for now
```

Keep it simple. One file per driver, consistent with current structure.

### Future: Driver Directories with Device Drivers

As we expand and implement custom orchestrators, each driver becomes a directory:

```
kernel/drivers/cursor/
├── DRIVER.yml           # Main driver config
├── BOOTSTRAP.md         # Read-first orientation
├── tools/               # "Device drivers" for specific tools
│   ├── file-edit.yml    # High-level file editing protocol
│   ├── terminal.yml     # High-level terminal protocol
│   ├── search.yml       # High-level search protocol
│   └── mcp.yml          # MCP integration protocol
└── BUDGET.yml           # Context cost estimates
```

### The Userland Principle

**Key insight:** Orchestrator tools are like syscalls — low-level, generic, hard to change. Drivers are like userland libraries — high-level, MOOLLM-aware, easy to evolve.

```
┌─────────────────────────────────────────────────────────┐
│  MOOLLM Skills — "Applications"                         │
├─────────────────────────────────────────────────────────┤
│  Driver Device Drivers — "Userland" (high-level APIs)   │
│    • file-edit.yml wraps search_replace with protocols  │
│    • terminal.yml wraps run_terminal_cmd with safety    │
│    • Easy to modify without touching orchestrator       │
├─────────────────────────────────────────────────────────┤
│  Orchestrator Tools — "Syscalls" (low-level, fixed)     │
│    • search_replace, run_terminal_cmd, codebase_search  │
│    • Provided by Cursor/Claude Code/custom              │
│    • Don't need to know about MOOLLM                    │
└─────────────────────────────────────────────────────────┘
```

**Like Linux user-space filesystems (FUSE):** You don't recompile the kernel to add a new filesystem — you write userland code that speaks the FUSE protocol. Same here: you don't modify the orchestrator to add MOOLLM awareness — you write driver code that wraps the tools.

### Benefits

| Approach | Benefit |
|----------|---------|
| **Orchestrator-agnostic** | Tools don't need MOOLLM knowledge |
| **Easy iteration** | Change driver files, not orchestrator code |
| **Layered abstraction** | High-level protocols over low-level tools |
| **Portable** | Same skills work across different orchestrators |

**Recommendation:** Stay with simple `cursor.yml` for now. Expand to directory structure when implementing custom orchestrators.

### Goal

Make explicit what I'm currently doing implicitly. Add practical bootstrap and trigger information to the existing well-designed driver.

---

## BOOTSTRAP.md (Draft)

```markdown
# Cursor Bootstrap

When a session starts or you're unsure what to do:

## 1. Orient

- Check `skills/INDEX.yml` for skill overview
- If user mentions a K-line name, search `skills/{name}/`
- For character work, read `skills/character/SKILL.md`

## 2. Before Creating Files

- Check `skills/format-design/SKILL.md` for conventions
- Check existing examples in `examples/` for patterns

## 3. Before Multi-Turn Simulation

- Read `skills/speed-of-light/SKILL.md`
- Target 20-50 turns per call

## 4. Before Commits

- Read CHANGES.md PUSH protocol (lines 6-26)
- Use `(this)` for current commit hash
- Never loop to fill in `(this)`
```

---

## TOOL-MAPPINGS.yml (Draft)

```yaml
# Map MOOLLM operations to Cursor tools

find_skill_by_concept:
  tool: codebase_search
  query_pattern: "What does {concept} mean in MOOLLM?"
  target: ["skills/"]

check_skill_exists:
  tool: grep
  pattern: "^# {skill_name}"
  target: "skills/"

read_skill_interface:
  tool: read_file
  target: "skills/{skill_name}/CARD.yml"
  
read_skill_protocol:
  tool: read_file
  target: "skills/{skill_name}/SKILL.md"

read_skill_context:
  tool: read_file
  target: "skills/{skill_name}/README.md"

find_examples:
  tool: list_dir
  target: "examples/"

find_character:
  tool: codebase_search
  query_pattern: "Where is {character_name} defined?"
  target: ["examples/"]
```

---

## TRIGGERS.yml (Draft)

```yaml
# When to invoke which skills

speed-of-light:
  triggers:
    - "simulate conversation"
    - "multi-character scene"
    - "game turns"
    - "play N turns"
  action: "Read skills/speed-of-light/SKILL.md before proceeding"

character:
  triggers:
    - "create character"
    - "new NPC"
    - "define personality"
  action: "Read skills/character/SKILL.md and skills/incarnation/SKILL.md"

representation-ethics:
  triggers:
    - "simulate real person"
    - "historical figure"
    - "celebrity"
  action: "Read skills/representation-ethics/SKILL.md BEFORE creating"

changes:
  triggers:
    - "PUSH"
    - "commit"
    - "update changelog"
  action: "Read CHANGES.md lines 6-26 for PUSH protocol"
```

---

## Proposed: Sniffable CARD.yml

> "Definitely doing this. Going forward, but also need to upgrade all existing cards systematically." -Don

### The Problem with CARD-MINI.yml

Originally proposed: create a separate `CARD-MINI.yml` for each skill with compressed info.

**Issues:**
- Two files to maintain
- Sync drift between CARD.yml and CARD-MINI.yml
- Extra cognitive load

### The Sniffable Solution

Apply the **sniffable-python principle**: put the important stuff at the top.

Just like sniffable Python code puts the "what does this do?" at the top of each function, sniffable CARD.yml puts the "when/how to invoke" at the top of each card.

### Sniffable CARD.yml Template

```yaml
# ============================================================
# SNIFF ZONE - Read this first, stop here if context is tight
# ============================================================
name: speed-of-light
tier: core
invoke_when:
  - "multi-turn simulation"
  - "conversation between characters"
  - "game turns"
  - "minimize round trips"
protocol: |
  Simulate all turns in one response. Use character headers.
  Maintain state mentally, write at end. Target 20-50 turns.
proof: examples/adventure-4/.../marathon-session.md#33-turns

# ============================================================
# FULL JAZZ - Rich context, examples, K-lines
# ============================================================
description: |
  The context window is a stage, not a bottleneck. Instead of
  round-tripping to the LLM for each character's turn, simulate
  the entire scene in one call...

k_lines:
  - name: many-turns-one-call
    activates: [simulation, party, multi-presence]
    
interfaces:
  methods:
    simulate_turns:
      input: scene_setup, characters, turn_count
      output: full_transcript, final_state

examples:
  - name: "33-Turn Stoner Fluxx"
    path: marathon-session.md#33-turns
    description: "8 characters, 33 turns, pure gezelligheid"

# ... more rich details
```

### Benefits

1. **One file, not two** — no sync issues
2. **LLM can stop early** — context-tight? Read first 15 lines.
3. **Human-readable** — clear visual separation
4. **Backwards compatible** — existing content moves down, not deleted
5. **Schema-friendly** — clear required vs optional zones

### The Survey Task

Before migrating, we need to:
1. Read all existing CARD.yml files
2. Extract common patterns
3. Identify "best of breed" examples
4. Derive official schema
5. Then migrate systematically

---

## Proposed: Enhanced INDEX.yml

Current entries are brief. Richer summaries would help triage:

```yaml
speed-of-light:
  path: skills/speed-of-light/
  tier: core
  summary: "Minimize LLM round trips. Many turns in one call."
  when_to_use: 
    - "Simulating conversations"
    - "Multi-character scenes"
    - "Game turns"
  context_cost: low
  entry_point: SKILL.md
  
representation-ethics:
  path: skills/representation-ethics/
  tier: core
  summary: "Ethical framework for simulating real people."
  when_to_use:
    - "Before creating any real person character"
    - "Historical figures"
    - "Living people"
  context_cost: medium
  entry_point: SKILL.md
  priority: must-read  # Before creation, not after
```

---

## Platform-neutral guidance — no `.cursorpriority`

Use `.cursorrules` for injected hints and `.moollm/working-set.yml` / `.moollm/hot.yml` as advisory lists on Cursor. Keep naming and protocols platform-agnostic; avoid non-standard platform-specific files beyond `.cursorrules` and `.cursorignore`.

---

## Skill Advertisements (YAML-first, grep-friendly) — DONE

Prefer simple YAML fields (in CARD.yml or SKILL.md front matter) over HTML comments:

```yaml
advertisements:
  - SIMULATE-CONVERSATION
  - MULTI-TURN
  - GAME-TURNS
  - ETHICS-CHECK
```

Grep for `advertisements:` or specific tokens (e.g., `ETHICS-CHECK`). Keeps syntax uncluttered and platform-agnostic. Use K-line naming: UPPER-CASE with dashes.

---

## The Meta-Observation

The system already works. I've been navigating it successfully this whole session. The K-lines activate, the cross-references guide me, the protocols are followable.

**Key realization:** The infrastructure already exists. The `cursor.yml` driver is well-designed and already understands the advisory vs commanding distinction. The problem isn't missing infrastructure — it's the bootstrap gap.

### The Core Challenge

On a custom orchestrator:
```
Orchestrator reads kernel → Loads driver → Assembles context → LLM starts informed
```

On Cursor:
```
Cursor assembles context opaquely → LLM starts... maybe informed, maybe not
```

### The Solution

Use Cursor's own mechanisms to bridge the gap:

1. **`.cursorrules`** — Cursor reads this file. Put MOOLLM bootstrap here.
2. **`MOOLLM.md` at root** — High semantic salience for Cursor's indexing.
3. **Semantic naming** — File names that Cursor's search will surface.

### What This Means for the Existing Files

| File | Role on Custom Orchestrator | Role on Cursor |
|------|----------------------------|----------------|
| `working-set.yml` | Commands context assembly | Documents what was focused |
| `hot.yml` | Commands priority | Documents what was frequently accessed |
| `cold.yml` | Commands eviction | Documents what was deprioritized |
| `cursor.yml` | Loaded by orchestrator | Read by LLM when prompted |

The files don't change. Their *interpretation* does. On Cursor, they're archaeology tools, not control mechanisms.

### The Elegant Inversion

The `cursor.yml` driver's "reverse generation" concept:

Instead of: `hot.yml` → orchestrator → context
We get: session happens → generate `hot.yml` → documentation

This actually provides the same benefit (debugging "what was in context?") through a different mechanism (post-hoc documentation rather than pre-hoc control).

The core insight — skills as programs, filesystem as world, LLM as eval() — remains sound. The optimization is using Cursor's native mechanisms (`.cursorrules`, semantic search) to bootstrap MOOLLM awareness.

---

## The Mini Kernel Concept

### The Problem

Full MOOLLM kernel is comprehensive but large:
- `kernel/` — multiple protocol documents
- `skills/` — 80+ skills
- `designs/` — design philosophy

Cursor can't (and shouldn't) inject all of this into every prompt.

### The Solution: Bootstrap Shim

Create a **mini kernel** that fits in Cursor's native injection points:

```
.cursorrules          ← Mini kernel lives here (always injected)
    ↓ points to
kernel/drivers/cursor.yml  ← Full driver (read when needed)
    ↓ points to
kernel/                    ← Full kernel (deep reference)
skills/                    ← Full skill library
```

### Mini Kernel Contents

The `.cursorrules` mini kernel should include:

| Section | Purpose | Size |
|---------|---------|------|
| Identity | "You are in MOOLLM" | 2 lines |
| Driver pointer | Where to find full driver | 2 lines |
| Skill index pointer | Where to find skills | 2 lines |
| Critical protocols | PUSH, Ethics, Speed of Light | 15 lines |
| K-line examples | How names activate context | 5 lines |
| Full kernel pointer | Where to go deeper | 3 lines |

**Target size:** ~50 lines. Small enough to always fit, rich enough to bootstrap.

### Cursor-Native Locations

| Location | Cursor Behavior | Our Use | Status |
|----------|----------------|---------|--------|
| `.cursorrules` | **Injected into every prompt** | **Mini kernel** | ⚠️ Not created yet |
| `.cursor/` | Cursor config directory | Session state? | Explore |
| `.cursorignore` | Skip from indexing | Build artifacts | Standard |
| `MOOLLM.md` | High semantic salience | Beacon | Could create |

**Current state:** No `.cursorrules` exists in moollm repo. We should create one.

### What .cursorrules Can Point To

```markdown
# .cursorrules content can reference:

## MOOLLM Context Files (runtime; gitignored copies in .moollm/)
- .moollm/working-set.yml   # Current focus (advisory)
- .moollm/hot.yml           # Priority hints (advisory)  
- .moollm/cold.yml          # Deprioritized breadcrumbs (advisory, optional)
- .moollm/bootstrap-probe.yml  # Cached probe results

## Kernel & Driver
- kernel/drivers/cursor.yml  # Your operating mode
- kernel/context-assembly-protocol.md  # How context works

## Skills
- skills/INDEX.yml  # Skill registry
- skills/README.md  # Categorized index
```

### The Indirection Pattern — TODO

```
.cursorrules (always injected, ~50 lines)
    ↓ points to
working-set.yml (current focus)
    ↓ points to
specific skills, files, characters
```

This gives us:
1. **Stable bootstrap** — .cursorrules rarely changes
2. **Dynamic focus** — working-set.yml changes per session
3. **Deep reference** — skills and files as needed

### The Bootstrap Chain (aligned to `.moollm/`)

```
Session starts
    ↓
Cursor injects .cursorrules (mini kernel)
    ↓
LLM opens pointers:
  - .moollm/working-set.yml (advisory)
  - .moollm/hot.yml (advisory)
  - kernel/drivers/cursor.yml (advisory mode explained)
  - PROTOCOLS.yml (K-line index)
  - skills/INDEX.yml (skill registry)
  - designs/cursor-self-review.md (plans/status)
  - MOOLLM.yml / MOOLLM.md (manifest/beacon)
    ↓
Driver read as needed (advisory hot/cold/working-set, scratch in .moollm/)
    ↓
Skills/protocols loaded via indices and K-lines
    ↓
Full MOOLLM awareness achieved (manifest + driver + indices + advisory breadcrumbs)
```

---

## Next Steps

### Immediate (Bootstrap Problem)

- [x] Create `.cursorrules` mini kernel (present)
- [ ] Test mini kernel size — ensure Cursor always includes it
- [x] Create `MOOLLM.md` at repo root as semantic beacon
- [ ] Enhance `kernel/drivers/cursor.yml` with bootstrap checklist (partial; advisory notes exist)
- [ ] Test with fresh context to see if orientation improves

### Sniffable CARD.yml (Priority Project)

Apply the sniffable-python principle to all CARD.yml files:

1. **Survey Phase**
   - [ ] Scan all existing CARD.yml files
   - [ ] Identify common patterns and fields
   - [ ] Note what varies and what's consistent
   - [ ] Find "best of breed" examples

2. **Schema Phase**
   - [ ] Derive official CARD.yml schema from survey
   - [ ] Document schema in `skills/card/SCHEMA.yml`
   - [ ] Add schema to `kernel/schemas/card.yml`
   - [ ] Define required vs optional fields
   - [ ] Define field order (sniffable = important stuff first)

3. **Sniffable Structure**
   ```yaml
   # === SNIFF ZONE (first 10-15 lines) ===
   name: skill-name
   invoke_when: [trigger phrases]
   protocol: one-line summary
   proof: link-to-evidence
   tier: core|standard|experimental
   
   # === FULL JAZZ (rest of file) ===
   description: |
     Rich explanation...
   k_lines: [...]
   interfaces: [...]
   # ... everything else
   ```

4. **Migration Phase**
   - [ ] Create migration script or systematic approach
   - [ ] Rewrite all CARD.yml files to sniffable format
   - [ ] Preserve all existing content (move, don't delete)
   - [ ] Validate against schema
   - [ ] Test that top-sniff provides enough to invoke

### Enhancement (Existing Infrastructure)

- [ ] Add `cursor_bootstrap` section to `kernel/drivers/cursor.yml`
- [ ] Add `triggers` section to cursor.yml (when to invoke which skills)
- [ ] Add `context_cost` estimates to `skills/INDEX.yml`
- [ ] ~~Add CARD-MINI.yml to key skills~~ → Replaced by sniffable CARD.yml

### Documentation (Advisory Mode)

- [ ] Document the "reverse generation" workflow clearly
- [ ] Create template for end-of-session `working-set.yml` generation
- [ ] Create template for session archaeology using `cold.yml`

### Context Window Probing

The `bootstrap-probe.yml` already exists and caches probe results. We could extend it:

1. **Context Window Estimation**
   - [ ] During PROBE, estimate available context window
   - [ ] Method: send known-size content, observe truncation
   - [ ] Cache result in `bootstrap-probe.yml` under `context_estimate:`
   
2. **Probe Structure**
   ```yaml
   # In bootstrap-probe.yml
   context_estimate:
     estimated_tokens: 200000
     measured_at: "2026-01-12T..."
     method: "system prompt + tool response observation"
     confidence: "medium"
     notes: |
       Cursor doesn't expose exact budget.
       Estimate based on known context sizes that worked.
   ```

3. **Use Context Estimate**
   - Inform sniffable reading decisions
   - Decide whether to read full CARD.yml or just sniff zone
   - Budget allocation for multi-skill sessions

### Advertisements (Sims-Style)

In The Sims, objects **advertise** what needs they can satisfy. A refrigerator advertises `HUNGER:-50`. A bed advertises `ENERGY:+80`. Sims choose actions by scoring advertisements against their current needs.

MOOLLM skills work the same way:

```yaml
# In CARD.yml — Sims-style advertisements
advertisements:
  - SIMULATE_CONVERSATION: "Multi-character dialogue"
  - MULTI_TURN: "Many turns in one call"
  - GAME_TURNS: "Simulate game rounds"
  
  # With scoring hints
  - name: SPEED_OF_LIGHT
    satisfies: [efficiency, multi-character, simulation]
    score_when:
      - "user asks for conversation"
      - "party scene"
      - "game turns"
```

### Advertisement Markers in Files

For grep-ability, use Sims-style markers:

```markdown
<!-- ADVERTISEMENT:SIMULATE_CONVERSATION -->
<!-- ADVERTISEMENT:MULTI_TURN -->
<!-- ADVERTISEMENT:ETHICS_CHECK -->
```

Not cursor-specific — works on any orchestrator that can grep.

### The Question

Does the LLM's semantic search find CARD.yml advertisements effectively?

- [ ] Test: Search for "simulate conversation" — does speed-of-light surface?
- [ ] Test: Search for "multi-character" — do relevant skills appear?
- [ ] If yes: Advertisements in CARD.yml are sufficient
- [ ] If no: Add `<!-- ADVERTISEMENT:... -->` markers for grep-ability

### Experimental

- [ ] Test if semantic search picks up CARD.yml advertisements
- [ ] If not, add `<!-- ADVERTISEMENT:... -->` markers to SKILL.md files
- [ ] Measure if explicit markers improve skill discovery

### Category Tagging (Priority Project)

The `skills/README.md` has excellent categorization — 14 categories with emoji headers. We should formalize this:

1. **Define Official Categories**
   - [ ] Document category list in `skills/CATEGORIES.yml`
   - [ ] Each category gets: id, emoji, name, description

2. **Category Schema**
   ```yaml
   # skills/CATEGORIES.yml
   categories:
     - id: philosophy
       emoji: 🧠
       name: "Philosophy & Core Concepts"
       description: "Foundational ideas and mental models"
       
     - id: formats
       emoji: 📝
       name: "Formats & Structure"
       description: "File formats, templates, conventions"
       
     - id: methodology
       emoji: 🎮
       name: "Methodology"
       description: "How to work, plan, debug"
       
     - id: spatial
       emoji: 🏠
       name: "Spatial (Room/Card)"
       description: "Rooms, cards, containers, navigation"
       
     - id: characters
       emoji: 👤
       name: "Characters & Identity"
       description: "Character creation, personas, representation"
       
     - id: animals
       emoji: 🐾
       name: "Animal Characters"
       description: "Species-specific behaviors"
       
     - id: roles
       emoji: 🍺
       name: "Role Skills"
       description: "Professional roles and expertise"
       
     - id: game-mechanics
       emoji: 🎲
       name: "Game Mechanics"
       description: "Sims-style simulation systems"
       
     - id: economy
       emoji: 💰
       name: "Economy & Scoring"
       description: "Currency, trade, achievement"
       
     - id: deliberation
       emoji: 🗳️
       name: "Decision & Deliberation"
       description: "Committees, debate, evaluation"
       
     - id: memory
       emoji: 🧠
       name: "Memory & Context"
       description: "Summarization, forgetting, logging"
       
     - id: communication
       emoji: 📮
       name: "Communication"
       description: "Messaging, mail, notifications"
       
     - id: system
       emoji: 🔧
       name: "System & Recovery"
       description: "Runtime, repair, infrastructure"
       
     - id: goals
       emoji: 🎯
       name: "Goals & Subjective"
       description: "Objectives, first-person experience"
   ```

3. **Tag All Skills**
   - [ ] Add `category:` field to all SKILL.md front matter
   - [ ] Validate against CATEGORIES.yml
   - [ ] Example:
     ```yaml
     ---
     tags: [moollm, philosophy, core]
     category: philosophy  # ← NEW: links to CATEGORIES.yml
     related: [...]
     ---
     ```

4. **Benefits**
   - Category-based search: "show me all 🎲 game mechanics skills"
   - Consistent organization
   - Easier navigation for new LLMs
   - Auto-generated category pages

### Related Cleanup Tasks

- [ ] Audit all SKILL.md front matter for consistency
- [ ] Ensure all README.md K-lines tables are bidirectional
- [ ] Verify all `related:` links in SKILL.md match K-lines in README.md
- [ ] Check for orphan skills (not linked from anywhere)
- [ ] Standardize `tags:` vocabulary across all skills
- [ ] Generate category summary in INDEX.yml

### Experimental: Standalone vs MOOLLM Comparison

**The Cat Skill Experiment**

The `cat/` skill is indexed on [claude-plugins.dev](https://claude-plugins.dev/skills/@SimHacker/moollm/cat) and distributed standalone as `cat.zip`. But how much does MOOLLM context actually improve it?

**Hypothesis:** Inside MOOLLM, the cat skill benefits from:
- K-line activation (character names trigger full context)
- Buff system integration (terpene effects, charms, curses)
- Room/location awareness (cat knows where it is)
- Relationship persistence (cat remembers you)
- Speed-of-light multi-turn (rich cat conversations)
- Mind-mirror personality (Sims traits drive behavior)

**Experiment Design:**

| Condition | Setup | Measure |
|-----------|-------|---------|
| **Standalone** | Install cat.zip via claude-plugins.dev | Interaction quality, consistency, depth |
| **MOOLLM** | Full adventure-4 context, Palm as subject | Same metrics |

**Test Scenarios:**
- [ ] First meeting with cat (trust building)
- [ ] Repeated interactions over "time" (relationship growth)
- [ ] Buff application and persistence (terpene effects)
- [ ] Multi-cat social dynamics (Palm + kittens)
- [ ] Cross-session memory (does cat remember you?)

**Metrics:**
- [ ] Personality consistency (does cat stay in character?)
- [ ] Relationship progression (does trust actually grow?)
- [ ] Buff/debuff application (do mechanics work?)
- [ ] K-line richness (does "Palm" activate full context?)
- [ ] Emergent behavior (surprises, unprompted actions)

**Expected Outcome:**
- Standalone: Works, but shallow. Cat is generic.
- MOOLLM: Cat is Palm. Rich history, relationships, personality.

**Value Proposition:**
If we can show measurable improvement, we have proof that:
1. Dovetailing adds real value
2. Skills are better together than alone
3. MOOLLM context is worth the complexity

**Document Results:**
- [ ] Run experiment with fresh LLM sessions
- [ ] Record transcripts
- [ ] Score against rubrics
- [ ] Write up findings in `designs/cat-skill-experiment.md`

---

---

## The Convergence: Connecting the Dots

We're at an inflection point. Several concepts we've developed are about to synergize exponentially.

### The Architecture Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                     .cursorrules (Mini Kernel)                  │
│                              ↓                                  │
│                     "I am in MOOLLM"                            │
│                     "Sniff CARD.yml first"                      │
│                     "K-lines activate context"                  │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                   Sniffable CARD.yml                            │
│              (first 10 lines = everything needed)               │
│                              ↓                                  │
│   name: speed-of-light                                          │
│   advertisements: [MULTI_TURN, SIMULATE_CONVERSATION]           │
│   invoke_when: "user wants many turns in one call"              │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                  Sims-Style Advertisements                      │
│         (skills announce what needs they satisfy)               │
│                              ↓                                  │
│   User says: "Let's play 20 turns of Fluxx"                     │
│   → ADVERTISEMENT:MULTI_TURN matches                            │
│   → ADVERTISEMENT:GAME_TURNS matches                            │
│   → speed-of-light skill scores highest                         │
│   → LLM sniffs CARD.yml, reads SKILL.md, executes               │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                      K-Lines Activate                           │
│            (names trigger full context loading)                 │
│                              ↓                                  │
│   "Palm" → entire character context activates                   │
│   "Postel" → robustness principle applies                       │
│   "society-of-mind" → multi-agent patterns engage               │
└─────────────────────────────────────────────────────────────────┘
```

### The Exponential Synergy

| Dot | Alone | **Connected** |
|-----|-------|---------------|
| Mini kernel | Just a file | **Auto-boots MOOLLM awareness every session** |
| Sniffable CARD | Compact format | **LLM discovers skills in 10 lines** |
| Advertisements | Metadata | **Skills compete to satisfy user needs** |
| K-lines | Names | **Semantic activation cascades** |
| Categories | Organization | **Browse → discover → invoke flow** |
| Three-tier docs | Efficiency | **Right depth for right moment** |

### The Vision: Self-Navigating Skills

When these connect, the LLM becomes **an intelligent navigator of skill space**:

```
User: "I want to simulate a conversation between Palm and the Bartender"

LLM thinks:
├── "Palm" activates → examples/adventure-4/characters/animals/palm/
├── "Bartender" activates → skills/bartender/
├── "simulate conversation" → ADVERTISEMENT:SIMULATE_CONVERSATION matches
├── speed-of-light scores highest
├── Sniff CARD.yml → I need to do many turns in one call
├── Read SKILL.md → Protocol: character headers, 20-50 turns
└── Execute!
```

**No human had to say "use speed-of-light"**. The system figured it out through K-line activation, advertisement matching, and skill discovery via sniffing.

### The Formula

```
Bootstrap (always present)
    × Sniffable (instant discovery)
    × Advertisements (need matching)
    × K-lines (semantic activation)
    × Categories (organized browsing)
    = Self-navigating, self-invoking skill system
```

---

## Roadmap: What's Next

### Phase 1: Bootstrap (This Week)

| Task | Effort | Impact |
|------|--------|--------|
| Create `.cursorrules` mini kernel | 1 hour | 🔥🔥🔥 Every session starts informed |
| Create `MOOLLM.md` beacon | 15 min | 🔥 Semantic salience |
| Test with fresh context | 30 min | Validate the bootstrap works |

### Phase 2: Sniffable Cards (Next)

| Task | Effort | Impact |
|------|--------|--------|
| Survey all CARD.yml files | 2 hours | Understand current state |
| Define sniffable schema | 1 hour | `skills/card/SCHEMA.yml` |
| Migrate all 80+ cards | 4 hours | 🔥🔥🔥 Instant skill discovery |

### Phase 3: Formalize Categories

| Task | Effort | Impact |
|------|--------|--------|
| Create `CATEGORIES.yml` | 30 min | Official category definitions |
| Tag all SKILL.md files | 2 hours | Rich metadata for filtering |
| Generate category summaries | 1 hour | Browseable skill catalog |

### Phase 4: Advertisement Refinement

| Task | Effort | Impact |
|------|--------|--------|
| Add advertisements to key skills | 2 hours | Skills announce capabilities |
| Test semantic search discovery | 1 hour | Does it work? |
| Add `<!-- ADVERTISEMENT:... -->` markers if needed | 2 hours | Fallback for grep |

### Phase 5: MOOCO — The MOO Custom Orchestrator

**MOOCO** = MOO Custom Orchestrator

| Task | Effort | Impact |
|------|--------|--------|
| Design MOOCO architecture | 1 day | The master plan |
| Expand drivers to directories | 1 day | Device driver architecture |
| Implement context assembly | 2 days | Full control over prompts |
| Build MCP client integration | 1 day | Call MCP servers from MOOCO |
| Build MCP server mode | 2 days | 🔥🔥🔥 MOOLLM skills become services |
| Kilroy native integration | 1 day | Direct swarm bus connection |

**MOOCO is the hinge that unlocks everything:**

```
┌─────────────────────────────────────────────────────────────────┐
│                          MOOCO                                  │
│              (MOO Custom Orchestrator)                          │
│                                                                 │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐        │
│  │  Context  │ │    MCP    │ │   Native  │ │ SvelteKit │        │
│  │  Assembly │ │  Layer    │ │   APIs    │ │ Web App   │        │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘        │
│        │            │             │             │               │
│   Full MOOLLM   Consume &     Kilroy,      Presentation         │
│   protocol      Provide       etc.         Layer                │
└─────────────────────────────────────────────────────────────────┘
```

### MOOCO MCP Layer — Speed of Light Carrier Pigeons

Inspired by Ken Kahn's **ToonTalk** birds as messengers:

```
┌─────────────────────────────────────────────────────────────────┐
│                   MCP MESSAGE ROUTING                           │
│                                                                 │
│  External MCP (different process/server):                       │
│    ┌─────────┐  HTTP/IPC  ┌─────────┐                           │
│    │ Skill A │───────────▶│ Skill B │  (round trip latency)     │
│    └─────────┘            └─────────┘                           │
│                                                                 │
│  Internal MCP (same MOOLLM microworld):                         │
│    ┌─────────┐  SIMULATED ┌─────────┐                           │
│    │ Skill A │───────────▶│ Skill B │  (speed of light!)        │
│    └─────────┘ same call  └─────────┘                           │
│                                                                 │
│  Like localhost loopback 127.0.0.1 — no network overhead!       │
└─────────────────────────────────────────────────────────────────┘
```

**The insight:** When both ends are in the same MOOLLM microworld, MOOCO short-circuits the external RPC and **simulates** the message passing at speed of light in one LLM call. The carrier pigeon doesn't need to fly when both nests are in the same room!

| Route | Latency | Mechanism |
|-------|---------|-----------|
| External MCP | ~100ms+ | HTTP/IPC round trip |
| Internal MOOLLM | 0ms | Simulated in same LLM call |

See: [skills/speed-of-light/](../skills/speed-of-light/) — the 33-turn Fluxx game is proof this works.

### MOOMCP — MOOLLM MCP Tool

MOOMCP is the MCP face of MOOLLM: **consume** external MCP services, **provide** MOOLLM skills as MCP services, and **short-circuit** when talking to peers in the same microworld.

**Deep-link protocol handlers**
- `moollm://character/don-hopkins/poke?intensity=gentle` → dispatches to the character's verb handler; works from web UI or internal speed-of-light calls.
- `moollm://room/pub/examine/lamp` → opens object panel, pops pie menus, prompts for parameters.
- All handlers are callable via MCP from outside, or simulated instantly when inside the same LLM call.

**Advertisements surface**
- Every skill publishes an `advertisements/` subdirectory (or section) exposing its offers to MCP discovery.
- MOOMCP indexes these ads and routes requests (external or simulated internal).

**Web-publisher skill**
- Generates styled HTML/MD with embedded YAML data islands.
- Renders live object panels, verbs, branching dialogs, continuations.
- Hooks into MOOMCP handlers so `moollm://` links work in-browser and in-orchestrator.
- Draws on the lloooomm prototype: characters as composable style sheets, worms as crawlers/transformers, single-page web simulations.

**Short-circuit rule**
- If caller and callee live in the same microworld: simulate the carrier pigeon at speed-of-light (no network).
- If remote: use real MCP transport (HTTP/IPC).

### MOOMPY / MOOMJS / MOOBASH — Execution Engines

Abstract interfaces to persistent execution engines. Drivers bind these to real runtimes:

| Tool | Purpose | Driver binds to |
|------|---------|-----------------|
| **MOOMPY** | Long-lived Python exec (stateful REPL) | `python`, `uv`, notebooks |
| **MOOMJS** | Long-lived JS/TS exec | `node`, `bun`, `deno` |
| **MOOBASH** | Long-lived shell exec | `bash`, `zsh`, `fish` |

Principles:
- **Abstract protocol, concrete drivers**: skills call MOOMPY/JS/BASH; drivers wire to actual tools.
- **Persistent state**: engines stay warm; preserve variables/modules across calls.
- **Speed-of-light intra-world**: if the runtime is simulated in the same LLM call, short-circuit; otherwise dispatch to real process via driver.
- **Safety & guardrails**: sandboxing, allowlists, resource caps via driver config.

### MOOCO Web Layer — Live Publishing Platform

MOOCO is also a **SvelteKit client/server app**:

```
┌────────────────────────────────────────────────────────────────┐
│                  MOOCO PRESENTATION LAYER                      │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                   Live MOOLLM Worlds                    │   │
│  │                                                         │   │
│  │  • Formatted markup with embedded YAML data islands     │   │
│  │  • Views, editors, simulators                           │   │
│  │  • Real-time state synchronization                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │               moollm:// Protocol Links                  │   │
│  │                                                         │   │
│  │  moollm://prompt/describe-this-room                     │   │
│  │  moollm://verb/examine/lamp                             │   │
│  │  moollm://continue/choice-3                             │   │
│  │  moollm://generate/image/sunset-over-maze               │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │              Interactive Room Descriptions              │   │
│  │                                                         │   │
│  │  "You are in a cozy [pub](moollm://examine/pub).        │   │
│  │   A [lamp](moollm://verb/use/lamp) flickers.            │   │
│  │   [Take lamp](moollm://verb/take/lamp)"                 │   │
│  │                                                         │   │
│  │  Links → pop up info, perform verbs, pie menus          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │            Generative Narrative Features                │   │
│  │                                                         │   │
│  │  • Continuations (like Scheme!)                         │   │
│  │  • Choose-your-own-adventure branching                  │   │
│  │  • Branching dialogs                                    │   │
│  │  • Image generation prompts + iterative refinement      │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────┘
```

**The key insight:** The LLM generates markup files with `moollm://` links that are both human-readable AND machine-actionable. Room descriptions become interactive UIs. Adventure games become web apps. The presentation layer and the intelligence layer are unified.

---

## MCP vs Skills: The Recursive Sandwich

### Why Both Exist

| Aspect | MCP | Skills |
|--------|-----|--------|
| **Philosophy** | Tool access | Behavior guidance |
| **Implementation** | Server processes, JSON-RPC | Files in a repo |
| **Runtime** | Stateful connections | None — just context |
| **What it solves** | "How to call external things" | "How to behave" |

**MCP = access to what**
**Skills = knowledge of how**

They're orthogonal, not competing.

### The Architecture Stack

```
┌─────────────────────────────────────────────────────────────────┐
│  MOOLLM as MCP SERVER (optional, with custom orchestrator)      │
│    • Other tools call MOOLLM skills as services                 │
│    • "Invoke speed-of-light simulation" via MCP                 │
├─────────────────────────────────────────────────────────────────┤
│  ORCHESTRATOR (Cursor, Claude Code, MOOCO)                      │
│    • Manages conversation                                       │
│    • Provides native tools                                      │
│    • Connects to MCP servers                                    │
│    • Injects skills into context                                │
├─────────────────────────────────────────────────────────────────┤
│  LLM (Claude)                                                   │
│    • Reads skills (in context)                                  │
│    • Makes tool calls (to orchestrator)                         │
│    • Follows protocols (from skills)                            │
├─────────────────────────────────────────────────────────────────┤
│  MOOLLM SKILLS                                                  │
│    • Behavior patterns, K-lines, protocols                      │
│    • Can invoke MCP tools via orchestrator                      │
├─────────────────────────────────────────────────────────────────┤
│  MCP SERVERS                                                    │
│    • External capabilities (databases, APIs, browsers)          │
│    • Some could BE MOOLLM (recursion!)                          │
└─────────────────────────────────────────────────────────────────┘
```

### Who's On Top?

It depends on direction:

| Direction | Flow | Who's on top |
|-----------|------|--------------|
| **Downward** | Skills guide → LLM calls MCP tools | Skills |
| **Upward** | External tool → calls MOOLLM via MCP | MCP (as interface) |
| **Sideways** | Multiple orchestrators share same skills | Peers |
| **Recursive** | MOOLLM calls itself via MCP | 🐢 Turtles all the way down |

### The Intertwingled Recursion

MOOLLM can:
1. **Call MCP servers** (downward) — use external capabilities
2. **BE an MCP server** (upward) — expose skills as services
3. **Call itself via MCP** (recursive) — skills invoke other skills as services

### Why MOOCO Matters

| Mode | What We Can Do |
|------|---------------|
| **Cursor** | Read skills, call MCP tools, advisory mode |
| **MOOCO** | Full context control, BE an MCP server, skills become APIs |

On Cursor, we're guests. With MOOCO, we're the host.

### The Kilroy Connection

[Kilroy](kilroy-ideas.md) is a decentralized AI automation platform (swarms, pipelines, P2P):

```
┌─────────────────────────────────────────────────────────────────┐
│                        KILROY                                   │
│    • Agent swarms as communication fabric                       │
│    • Visual pipeline editor                                     │
│    • P2P networking (no firewall config)                        │
│    • Apps as JSON (like skills as YAML!)                        │
├─────────────────────────────────────────────────────────────────┤
│                   INTEGRATION OPTIONS                           │
│                                                                 │
│    Option A: MCP Interface                                      │
│    ┌───────────────┐     ┌───────────────┐                      │
│    │    Kilroy     │────▶│ MOOLLM as MCP │                      │
│    │   Pipeline    │ MCP │    Server     │                      │
│    └───────────────┘     └───────────────┘                      │
│                                                                 │
│    Option B: Native MOOCO Interface                             │
│    ┌───────────────┐      ┌───────────────┐                     │
│    │    Kilroy     │─────▶│     MOOCO     │                     │
│    │   Swarm Bus   │native│  (deep API)   │                     │
│    └───────────────┘      └───────────────┘                     │
├─────────────────────────────────────────────────────────────────┤
│                          MOOCO IS KEY                           │
│                                                                 │
│    • Provides MCP interface (standard, portable)                │
│    • Provides native interface (fast, tight integration)        │
│    • Controls context assembly (full MOOLLM protocol)           │
│    • Bridges MOOLLM to any external system                      │
└─────────────────────────────────────────────────────────────────┘
```

| Kilroy Concept | MOOLLM Equivalent |
|----------------|-------------------|
| Named swarm | Room directory |
| Agent in swarm | Card in play |
| Swarm messages | Soul chat |
| Pipeline JSON | Skill YAML |
| Install by copy | Skill instantiation |

**The synergy:** Kilroy provides the swarm infrastructure, MOOLLM provides the behavior protocols. **MOOCO** bridges them — either via MCP (standard) or native API (fast).

See: [designs/kilroy-ideas.md](kilroy-ideas.md) for full integration mapping.

---

## Intuitions: Where This Is Headed

### Near-Term (Weeks)

1. **The flywheel starts spinning**
   - Better sniffable cards → better discovery
   - Better discovery → more skill usage
   - More usage → more refinement
   - Virtuous cycle begins

2. **Skills become truly composable**
   - Not just K-line links, but runtime invocation
   - Skills calling skills
   - Emergent behaviors from combinations

3. **Public adoption accelerates**
   - claude-plugins.dev already indexing us
   - `moollm` tag creates brand recognition
   - Others fork and extend

### Medium-Term (Months)

4. **MOOLLM as MCP server**
   - Any tool that speaks MCP can use MOOLLM skills
   - Claude Desktop, Cursor, custom apps
   - Skills become services

5. **Package management arrives**
   - `related:` links become real dependencies
   - Skill versioning and compatibility
   - Install/update/remove skills

6. **Multi-adventure orchestration**
   - Characters visit each other's worlds
   - Cross-adventure K-line activation
   - Federated microworlds

### Long-Term (Vision)

7. **Skills as the new apps**
   - Not just for code assistants
   - Skills for any LLM task
   - The "app store" for AI capabilities

8. **Collaborative skill development**
   - Pull requests for skills
   - Community-maintained skill libraries
   - Best practices emerge from usage

9. **The Sims meets AGI**
   - Fully autonomous characters
   - Needs-driven behavior
   - Emergent societies in microworlds

---

## The Self-Reinforcing Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌──────────┐  │
│   │ Better  │ ──▶ │ Better  │ ──▶ │  More   │ ──▶ │  More    │  │
│   │  Skills │     │Discovery│     │  Usage  │     │Refinement│  │
│   └─────────┘     └─────────┘     └─────────┘     └──────────┘  │
│        ▲                                               │        │
│        └───────────────────────────────────────────────┘        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**We're on the edge of the flywheel starting to spin.**

---

## See Also

### Existing Infrastructure
- [kernel/drivers/cursor.yml](../kernel/drivers/cursor.yml) — **the Cursor driver** (read this!)
- [kernel/context-assembly-protocol.md](../kernel/context-assembly-protocol.md) — how context should be assembled
- [kernel/drivers/README.md](../kernel/drivers/README.md) — driver system overview
- [skills/bootstrap/](../skills/bootstrap/) — session initialization skill

### Philosophy
- [MOOLLM-MANIFESTO.md](MOOLLM-MANIFESTO.md) — the philosophy
- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) — the seven extensions

### Reference
- [skills/INDEX.yml](../skills/INDEX.yml) — current skill index
- [kernel/](../kernel/) — full kernel documentation

### External
- [claude-plugins.dev](https://claude-plugins.dev) — where our skills are indexed
- [Anthropic Skills spec](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-library) — the foundation we extend
