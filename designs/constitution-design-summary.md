# Constitution Design Summary
## Key Ideas from the LLM Orchestrator Architecture Discussion

*Extracted from a ChatGPT conversation exploring how to build a SvelteKit app
with an LLM orchestrator, tools, and interactive embedded components.*

---

## 🎯 The Core Insight

> **"The LLM is a pure function. The orchestrator is the operating system."**

The LLM does not plan, remember, or execute. It predicts tokens. Everything
else — memory, planning, agency, tools — is **orchestrator behavior**.

---

## 1. The Shared Mental Model

All modern LLM systems (Claude Code, Cursor, ChatGPT) converge on the same pattern:

```
1. Host gives LLM a catalog of callable tools (schemas)
2. LLM emits structured tool calls (name + args)
3. Host executes and returns results into context
4. Repeat until done
```

**MCP (Model Context Protocol)** standardizes this as the "POSIX layer" —
portable, declarative, boring (in a good way).

---

## 2. Planning is Emergent, Not Internal

**There is no planner in the model.**

Planning emerges from:
- **The prompt** (static bias toward plan-shaped text)
- **External state** (conversation history, tool results, artifacts)
- **Re-prompting** (the loop creates temporal glue)
- **Selection pressure** (orchestrator filters invalid trajectories)

> *"Planning is not something the LLM has. It is something the system does, moment by moment."*

**Implication:** You don't need a "planning module." You need:
- Explicit state
- Visible artifacts
- Resumable steps
- Tool logs
- UI feedback
- Guardrails

---

## 3. The "Everything is Files" Paradigm

**Treat the filesystem as the LLM's memory.**

| Cognitive Metaphor | Filesystem Primitive |
|--------------------|---------------------|
| Memory palace | Directory hierarchy |
| Room | Folder |
| Object/evidence | File |
| Note on wall | `.md` file |
| Post-it | `.meta.yml` sidecar |
| Mind map node | Directory with links |
| Timeline | Filenames / `events.jsonl` |
| Forgetting | De-prioritization |
| Recall | Search / traversal |

**Benefits:**
- Perfect audit trail
- Human-readable state
- Git version control
- LLM can browse with file tools
- No mystical "hidden scratchpad"

---

## 4. The Agent Directory Structure

```
.agent/
  constitution.md          # The DNA - rules, tools, output formats
  runtime.yml              # Machine-readable config
  
  sessions/
    <session-id>/
      chat.md              # Full transcript
      output.md            # User-visible output (APPEND-ONLY)
      events.jsonl         # Tool calls/results (APPEND-ONLY)
      working-set.yml      # What's in context right now
      hot.yml              # "Keep this in cache"
      cold.yml             # "Summarize/evict this"
      
      plans/               # Explicit plan artifacts
      tool/                # Tool outputs by category
        fs/
        terminal/
        python/
        js/
      artifacts/           # Generated outputs
      summaries/           # Compressed wisdom
      
  memory/                  # Cross-session persistence
    facts.md
    glossary.md
    decisions.md
    
  index/                   # Search infrastructure
    vector/
    lexical/
```

---

## 5. The Tool Contract: Require `why`

Every tool call MUST include a `why` parameter:

```yaml
fs.read:
  path: string
  range: optional
  why: string  # REQUIRED - forces intentionality

terminal.run:
  cmd: string[]
  cwd: string
  timeout_ms: number
  why: string  # REQUIRED
```

**Benefits:**
- Self-documenting traces
- Improved recall of intention
- Better audit trails
- Reduces aimless exploration

---

## 6. Memory Management Protocols

### Working Set Manifest
```yaml
# working-set.yml
context_budget_tokens: 28000
files:
  - path: ".agent/constitution.md"
    priority: 1.0
  - path: "src/routes/+page.svelte"
    priority: 0.7
```

The orchestrator assembles prompt context by reading this manifest,
truncating by priority until budget fits.

### Hot/Cold Cache Hints
```yaml
# hot.yml - Model suggests what to keep
keep:
  - path: ".agent/constitution.md"
    why: "Defines tool schemas and output protocol"

# cold.yml - Model suggests what to evict
evict:
  - path: ".../tool/terminal/log-009.txt"
    why: "Old build log, no longer relevant"
```

**Key principle:** Model ADVISES memory management, orchestrator DECIDES.

### Summarization as a Tool
```yaml
memory.summarize:
  target_paths: ["..."]
  into_path: ".agent/summaries/tool_state.md"
  why: "Need condensed view for next steps"
  style: "bullet|narrative|schema"
  keep_refs: true
```

Summaries become files → searchable, browsable, indexable.

---

## 7. Sidecar Metadata: Post-it Notes for Files

Every important file can have a `.meta.yml` sidecar:

```yaml
# path/to/file.meta.yml
title: "Vector index schema"
summary: "Defines embedding model, chunking, ranking knobs."
tags: ["index", "retrieval", "core"]
hotness: 0.92
pin: true
last_used: "2025-12-30T12:41:02Z"
provenance:
  created_by: tool:terminal.run
  session: 2025-12-30T12-04-17Z
links:
  - .agent/constitution.md
```

**Benefits:**
- Directory listings become informative
- LLM can browse metadata without reading full files
- Vector index can ingest summaries + tags
- "Sticky note layer" for the filesystem

---

## 8. Skills as Userland Protocols

**Skills are NOT orchestrator code — they're conventions the model follows.**

A skill is:
- A protocol document (constitution)
- A directory template
- Naming rules
- `.meta.yml` conventions
- Hot/cold conventions

**Skill Tiers:**
1. **Tier 0**: Pure cognitive (no tools) — writing styles, reasoning patterns
2. **Tier 1**: File-only — memory palaces, adventure maps, research notebooks
3. **Tier 2**: File + search — recall, navigation
4. **Tier 3**: File + shell — build, test, data processing
5. **Tier 4**: External systems — databases, APIs (MCP-backed)

> *"If a skill can be expressed using only file tools, do that."*

---

## 9. Skill Instantiation Protocol (SIP)

Skills as **activation record templates**:

```
.skills/
  ui_embed/
    SKILL.md                # Description + rules
    PROTOTYPE.yml           # Identity + version
    template/               # Files to copy
      overrides/
      state/
      CHECKLIST.md
      TASK.yml.tmpl
```

**Instantiation:**
1. Create instance dir: `.agent/sessions/<sid>/instances/<skill>-NNNN/`
2. Copy template files
3. Render `.tmpl` → concrete files
4. Write `INSTANCE.yml` and `PROTOTYPES.yml`
5. Mark status: active

**Lifecycle:** boot → run → finalize → garbage collect

---

## 10. Delegation Object Protocol (DOP)

**Self-like prototype/delegation adapted for LLMs.**

Instead of class inheritance, use **ordered delegation**:

```yaml
# PROTOTYPES.yml in an instance
prototypes:
  - path: ".skills/ui_embed"
    version: "0.3.1"
  - path: ".skills/memory_palace"
    version: "0.2.0"
resolution:
  strategy: "first-match-wins"
```

**Resolution Rule:**
1. Check local `overrides/`
2. Check each prototype in order
3. First match wins

**Why this works for LLMs:**
- Explicit, textual resolution rules
- Navigable via file browsing
- No algorithmic MRO
- Conflicts documented, not hidden

---

## 11. Robust-First / MFM-Inspired Design

Inspired by **Dave Ackley's Robust-First Computing** and **Movable Feast Machine**:

> *"Systems should continue operating under local faults, partial outages,
> and uncertainty — prioritizing survivability over fragile correctness."*

**Self-Healing Protocol:**
- At session start, check canonical files exist
- If missing, create minimal placeholders
- Record repairs in `events.jsonl`
- Never crash on missing scaffolding — converge

**Protocol Demons (local repair agents):**
- **Checklist repairer**: Creates missing canonical files
- **Sticky-note maintainer**: Auto-creates `.meta.yml` stubs
- **Heat balancer**: Manages working set size
- **Membrane keeper**: Keeps agent state inside `.agent/`

**Homeostatic Goals:**
- Canonical files exist
- Every artifact has a sticky note
- Summaries exist for files above N KB
- Working set fits budget

---

## 12. The Constitution as Boot Header

Don't re-paste the DNA every turn. Use a pointer:

```
Root: .agent/
Constitution: .agent/constitution.md (v12, hash abc123)
Session: .agent/sessions/<id>/
Output sink: output.md (append-only)
Working set: working-set.yml
Cache hints: hot.yml, cold.yml
All tool calls require why
```

The model can read the constitution file when needed.

---

## 13. Orchestrator vs Skill Responsibilities

### Orchestrator (Kernel)
- Provide file tools (ls/read/append/patch)
- Provide search tools (lexical/vector)
- Provide sandboxed execution (terminal/python/js)
- Enforce sandbox boundaries
- Enforce append-only rules where needed
- Enforce resource limits
- Context assembly from `working-set.yml`
- Event logging to `events.jsonl`
- Indexing service

### Skills (Userland)
- Define canonical file sets
- Define checklists
- Define repair rules
- Define summarization conventions
- Define hot/cold heuristics
- Define output formats
- Define UI embed protocols

---

## 14. Key Architectural Quotes

> *"Memory is infrastructure, not cognition. The model is a consumer of
> memory, not its owner."*

> *"The model doesn't have to 'remember the protocol' — it can literally
> `ls` and follow the breadcrumbs."*

> *"LLMs don't understand inheritance — but they are very good at following
> explicit delegation protocols over navigable structures."*

> *"Robustness emerges from rules and structure, not heroic centralized control."*

> *"The LLM emits tokens. The orchestrator decides which tokens become reality."*

---

## 15. Integration with MOOLLM

This architecture maps beautifully to MOOLLM:

| Constitution Concept | MOOLLM Equivalent |
|---------------------|-------------------|
| `.agent/` root | Character directory |
| `constitution.md` | Soul file (`.yml`) |
| `sessions/` | Room activations |
| `working-set.yml` | Room context / attention |
| `hot.yml/cold.yml` | Memory breathing |
| `.meta.yml` sidecars | Soul chat metadata |
| Skills | Trading cards / protocols |
| Delegation/prototypes | Pet inheritance |
| Self-healing | Robust-first consciousness |

**See also:**
- `MOOLLM-PROTOCOLS.md` — Protocol compendium
- `MOOLLM-MANIFESTO.md` — Core philosophy
- `kernel/` — Low-level OS protocols
- `skills/` — Skill templates and examples

---

## Files Generated from This Analysis

```
01-Projects/moollm/
├── constitution-design-summary.md    # This file
├── kernel/
│   ├── README.md                     # Kernel overview
│   ├── constitution-template.md      # The actual constitution
│   ├── tool-calling-protocol.md      # Tool schemas + why
│   ├── context-assembly-protocol.md  # Working set management
│   ├── memory-management-protocol.md # Hot/cold, summaries
│   ├── self-healing-protocol.md      # MFM-inspired repair
│   └── event-logging-protocol.md     # Append-only audit
├── skills/
│   ├── README.md                     # Skills overview
│   ├── skill-instantiation-protocol.md  # SIP spec
│   ├── delegation-object-protocol.md    # DOP spec
│   └── templates/                    # Example skill templates
│       └── basic-skill/
└── schemas/
    ├── tool-schemas.yml              # Core tool definitions
    ├── working-set-schema.yml        # Working set format
    └── meta-sidecar-schema.yml       # .meta.yml format
```

---

*"The orchestrator is the operating system. The filesystem is the brain.
The protocols are the cognitive style. The LLM is a navigator, not a brain."*
