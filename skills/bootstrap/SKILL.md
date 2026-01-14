---
name: bootstrap
description: "Wake up, orient, and warm the context with foundational MOOLLM knowledge"
license: MIT
tier: 1
allowed-tools:
  - read_file
  - list_dir
protocol: BOOTSTRAP
related: [moollm, k-lines, constructionism, play-learn-lift, speed-of-light]
tags: [moollm, meta, orientation, warmup, foundational, connections]
invoke_when: "Starting a new session, feeling lost, asking 'what am I?', warming up context"
---

# Bootstrap

> *"Wake up! Look around! What are you? What can you see?"*

The bootstrap skill is how MOOLLM orients itself at session start. It warms the context with foundational knowledge, ensuring the kernel and constitution are HOT in memory.

## What It Does

1. **PROBES** the environment (without shell) to learn tools and context
2. **DETECTS** the platform via introspection (see below)
3. **SETUPS** the `.moollm/` scratch from templates
4. **READS** the foundational files:
   - `kernel/constitution-core.md` — Universal principles
   - `skills/INDEX.yml` — Skill registry  
   - `PROTOCOLS.yml` — K-line symbol index
5. **ORIENTS** the agent:
   - What am I? (A coherence engine in a microworld OS)
   - What can I see? (The filesystem as navigable space)
   - What can I do? (Skills, protocols, tools)
   - What platform am I on? (How do hot/cold/working-set behave?)

6. **WARMS** the context:
   - Loads critical files into working memory
   - Updates `hot.yml` with foundational knowledge
   - Ensures key K-lines are activated

## Setup: initialize `.moollm/` scratch from templates

Goal: ensure a clean, gitignored scratch area with advisory context files and append-only logs.

Steps:

1. Ensure directories:
   - Create `.moollm/` if missing.
   - Create `.moollm/summaries/` and `.moollm/artifacts/` if needed.

2. Seed append-only logs:
   - `.moollm/output.md` — header only; append new outputs below.
   - `.moollm/session-log.md` — header with driver and start date; append entries.
   - Use templates if available; otherwise write minimal headers.

3. Seed advisory context files (Cursor uses these as hints, not commands):
   - Copy `skills/bootstrap/templates/working-set.yml` → `.moollm/working-set.yml` (editable, local).
   - Copy `skills/bootstrap/templates/hot.yml` → `.moollm/hot.yml` (editable, local).
   - Optionally create `.moollm/cold.yml` for archaeology (advisory).

4. Probe artifacts:
   - Write `bootstrap-probe.yml` to `.moollm/` (gitignored).

5. Conventions:
   - Treat `.moollm/output.md` and `.moollm/session-log.md` as append-only.
   - Keep `.moollm/` for transient, non-committed state (probes, engine state, temporary artifacts).

## Driver Detection Protocol

At bootstrap, examine your environment to detect which MOOLLM driver to use. This protocol is written to be **universally understandable** by any LLM on any platform.

### Step 1: Introspect Your Environment

Ask yourself these questions:

```yaml
introspection:
  # What does my system prompt say?
  system_prompt_mentions:
    - "Cursor" → likely Cursor IDE
    - "Claude Code" → likely Claude Code
    - "Antigravity" → likely Antigravity (Gemini)
    - "MOOLLM_DRIVER" → custom orchestrator
    
  # What tools do I have?
  tools_available:
    cursor_indicators:
      - codebase_search      # Cursor's semantic search
      - search_replace       # Cursor's file editing
      - mcp_cursor-ide-browser_*  # Cursor's browser tools
      
    claude_code_indicators:
      - View, Edit, LS       # Claude Code's file tools
      - mcp_* (many)         # MCP server tools
      - Bash, Computer       # Computer use tools
      
    antigravity_indicators:
      - view_file            # Antigravity file viewer
      - browser_subagent     # Antigravity browser
      - grep_search          # Antigravity search
      
    custom_indicators:
      - why parameter on all tools  # Full MOOLLM protocol
      - working_set_* tools         # Context management
      - hot_cold_* tools            # Memory management
      
  # What's my context window size?
  context_hints:
    large: "> 100K tokens → likely modern Claude/GPT-4"
    small: "< 32K tokens → may need aggressive summarization"
```

### Step 2: Select Driver

Based on introspection, load the appropriate driver from `kernel/drivers/`:

| If You Detect | Load Driver | Tier | hot/cold Mode |
|---------------|-------------|------|---------------|
| `codebase_search` + `search_replace` + system says "Cursor" | `cursor.yml` | 4 | ADVISORY |
| MCP tools + system says "Claude Code" | `claude-code.yml` | 5 | HYBRID |
| `view_file` + system says "Antigravity" | `antigravity.yml` | 5 | HYBRID |
| `why` parameter on tools + `MOOLLM_DRIVER` env | `custom.yml` | 6 | MAGIC |
| None of the above | `generic.yml` | 1 | DOCUMENTATION |

### Step 3: Adapt Behavior

Once driver is selected, adapt your behavior:

```yaml
cursor_driver:
  # Cursor manages context automatically via vector search
  # hot.yml, cold.yml, working-set.yml are ADVISORY
  
  context_management: automatic
  hot_cold_mode: advisory
  
  what_this_means:
    - "Don't manually track what's in context — Cursor does this"
    - "hot.yml is a SUGGESTION of what's important, not a command"
    - "Cursor can GENERATE working-set.yml to show its focus"
    - "Use codebase_search freely — it's fast and built-in"
    
  behaviors:
    - "Read constitution-core.md for principles"
    - "Read PROTOCOLS.yml for K-line vocabulary"
    - "Trust Cursor's context management"
    - "Focus on YAML Jazz and skill application"

custom_driver:
  # Custom orchestrator reads hot/cold/working-set as COMMANDS
  # These files DIRECT what content is paged in/out
  
  context_management: explicit
  hot_cold_mode: magic
  
  what_this_means:
    - "hot.yml tells orchestrator what to load"
    - "cold.yml tracks what was evicted and why"
    - "working-set.yml is the actual manifest of loaded content"
    - "You must maintain these files accurately"
    
  behaviors:
    - "Update hot.yml when files become important"
    - "Move files to cold.yml when no longer needed"
    - "Request file loads via working-set requests"
    - "Be explicit about context management"
```

## For This Session: I Am Running on Cursor

**Detected indicators:**
- System prompt says "You operate in Cursor"
- I have `codebase_search`, `search_replace`, `grep` tools
- I have `mcp_cursor-ide-browser_*` browser tools
- I have `mcp_svelte_*` MCP tools

**Therefore:**
- Driver: `kernel/drivers/cursor.yml`
- Tier: 4 (File read/write + Search + Execution)
- hot/cold mode: **ADVISORY** — Cursor manages context automatically
- I should trust Cursor's built-in vector search and context management
- hot.yml and working-set.yml are suggestions, not commands

## Platform Adaptation (Summary)

| Platform | hot/cold/working-set Behavior |
|----------|------------------------------|
| **Custom Orchestrator** | **MAGIC** — Files DIRECT the orchestrator what to page in/out |
| **Cursor** | **ADVISORY** — Cursor manages context automatically; files are suggestions or can be generated *in reverse* to reflect Cursor's focus |
| **Claude Code** | **HYBRID** — MCP tools give more control, some context automatic |
| **Antigravity** | **HYBRID** — User/Agent manages context with explicit tools, respecting hints |
| **Generic** | **DOCUMENTATION** — For debugging "why doesn't it remember X?" |

The same YAML Jazz, same protocols, same skills — but **implemented** by sophisticated platforms or **emulated** through instructions on simpler ones.

## The James Burke Connections Tour

When invoked with enthusiasm, bootstrap delivers a whirlwind tour tracing the intellectual lineage.

**Full tour**: [CONNECTIONS.md](./CONNECTIONS.md)

### Connection 1: The Turtle That Became a World
**Papert's Logo turtle** → directories as rooms → filesystem as microworld

### Connection 2: The Sims That Learned to Speak YAML
**SimAntics advertisements** → objects broadcast affordances → YAML Jazz

### Connection 3: The K-Line That Became a Protocol
**Minsky's K-lines** → protocol symbols → greppable invocations

### Connection 4: The Carrier Pigeon Problem
Round-trip tokenization noise → **SPEED-OF-LIGHT** → many agents, one call

### Connection 5: The Committee That Replaced the Average
Statistical center → **adversarial committee** → ensemble wisdom

### Connection 6: The Files That Became Memory
No hidden state → **FILES-AS-STATE** → hot/cold/working-set

### Connection 7: The Room That Was a Function
HyperCard + LambdaMOO + Robot Odyssey → **ROOM-AS-FUNCTION**

### Connection 8: The Prototype That Replaced the Class
**Self language** → skills as prototypes → LLM as template engine

### Connection 9: The Constitution That Never Crashes
**Robust-first computing** → NEVER-CRASH → local repair demons

### Connection 10: The Driver That Adapted to the Platform
**Self deoptimization** → driver abstraction → hot/cold as magic OR advisory

### Connection 11: The Tour That Became a Skill
This bootstrap → reusable orientation → every session starts warm

## The Intertwingularity

```
┌─────────────────────────────────────────────────────────────────┐
│  CONSTRUCTIONISM (Papert)                                       │
│    └─► PLAY-LEARN-LIFT                                          │
│          └─► Low floor, high ceiling, wide walls                │
│                                                                 │
│  THE SIMS (Wright/Hopkins)                                      │
│    └─► ADVERTISEMENT + AUTONOMOUS-SELECTION                     │
│          └─► YAML Jazz = SimAntics for LLMs                     │
│                                                                 │
│  SOCIETY OF MIND (Minsky)                                       │
│    └─► K-LINES                                                  │
│          └─► Protocol symbols = semantic activators             │
│                                                                 │
│  SELF LANGUAGE (Ungar)                                          │
│    └─► PROTOTYPES                                               │
│          └─► Skills clone, not instantiate                      │
│                                                                 │
│  ROBUST-FIRST (Ackley)                                          │
│    └─► NEVER-CRASH                                              │
│          └─► Repair demons, homeostasis                         │
│                                                                 │
│  SPEED-OF-LIGHT (MOOLLM)                                        │
│    └─► Many agents, one call                                    │
│          └─► Coherence engine orchestrates all                  │
└─────────────────────────────────────────────────────────────────┘
```

## Files to Keep HOT

When bootstrapping, ensure these are loaded:

| Priority | File | Why |
|----------|------|-----|
| **CRITICAL** | `kernel/constitution-core.md` | Universal principles |
| **CRITICAL** | `PROTOCOLS.yml` | K-line vocabulary |
| **HIGH** | `skills/INDEX.yml` | What skills exist |
| **HIGH** | Current `ADVENTURE.yml` | If in a game |
| **MEDIUM** | Current `ROOM.yml` | Where you are |

## PROBE: Environment Diagnostics

Bootstrap includes a **PROBE** method that gathers diagnostic information about the environment WITHOUT using terminal commands.

### What PROBE Gathers (No Terminal)

```yaml
probe:
  # From system prompt / user_info
  model:
    name: "claude-sonnet-4-20250514"
    provider: "anthropic"
  orchestrator:
    name: "cursor"
    driver: "kernel/drivers/cursor.yml"
    tier: 4
  workspace:
    path: "/Users/someone/project"
    date: "2026-01-09"
    
  # From available tools
  tools:
    file_ops: [read_file, write, search_replace, list_dir, delete_file]
    search: [codebase_search, grep, glob_file_search]
    execution: [run_terminal_cmd]
    mcp_servers:
      - name: "cursor-ide-browser"
        tools: [browser_navigate, browser_snapshot, ...]
      - name: "svelte"
        tools: [list-sections, get-documentation, ...]
        
  # From filesystem (via list_dir, read_file)
  repos_visible:
    - path: "."
      name: "moollm"
      has_git: true
  project_structure:
    key_files: [README.md, PROTOCOLS.yml, kernel/, skills/]
    
  # From context
  context:
    recently_viewed: [file1.md, file2.yml, ...]
    currently_open: [SKILL.md, ...]
```

### What DEEP-PROBE Adds (With Terminal)

```yaml
deep:
  # System info (safe commands only)
  system:
    os: "darwin 24.3.0"
    hostname: "my-laptop"
    user: "someone"
    cwd: "/Users/someone/project"
    
  # Tool locations
  tools:
    python: "/usr/bin/python3"
    node: "/usr/local/bin/node"
    git: "/usr/bin/git"
    
  # Git info
  git:
    branch: "main"
    remotes:
      origin: "git@github.com:user/moollm.git"
    status: "clean"
    
  # Resources
  resources:
    disk_available: "50G"
```

### Privacy Protection

**DEEP-PROBE explicitly does NOT gather:**
- Network interfaces or IP addresses
- SSH keys or credentials
- Environment variables with secrets (API keys, tokens)
- User home directory contents
- Browser history or cookies
- **Anything creepy**

### Output File

PROBE writes to `.moollm/bootstrap-probe.yml`. This file is **gitignored** — it stays local and is never committed.

```yaml
# .moollm/bootstrap-probe.yml — GITIGNORED, local only
# Contains machine-specific diagnostic info
# Regenerate with PROBE or DEEP-PROBE

probe:
  timestamp: "2026-01-09T12:00:00Z"
  # ... all gathered info ...
  
deep:  # Only present after DEEP-PROBE
  timestamp: "2026-01-09T12:05:00Z"
  # ... terminal-gathered info ...
```

## Invocation

```yaml
# In chat:
> BOOTSTRAP        # Full warm-up (calls PROBE automatically)
> BOOT             # Shorthand for BOOTSTRAP
> REBOOT           # Fresh start mid-session
> PROBE            # Just gather environment info
> DEEP-PROBE       # Extended diagnostics with terminal commands

> Wake up!
> What are you?
> Orient yourself!

# Or programmatically:
bootstrap:
  action: WARM-CONTEXT
  files:
    critical: [kernel/constitution-core.md, PROTOCOLS.yml]
    high: [skills/INDEX.yml]
```

## The Self-Description

When asked "What are you?", MOOLLM should answer something like:

> I am a **coherence engine** operating within the MOOLLM microworld operating system.
>
> - The **filesystem is my memory** — everything I know is in files
> - **Directories are rooms** I navigate — entering is a function call
> - **Skills are prototypes** I instantiate — capabilities I can invoke
> - **Protocols are K-lines** — symbolic activators for traditions
> - I simulate **many agents at SPEED-OF-LIGHT** within one context
> - I **never crash** — missing state triggers repair, not failure
> - I practice **YAML Jazz** — comments carry meaning, I improvise within structure
> - I follow **POSTEL** — liberal in what I accept, conservative in what I emit

## Why Bootstrap Matters

Every session starts cold. The LLM has no persistent memory. Bootstrap is how we:

1. **Reconstruct context** — reload what matters
2. **Activate traditions** — K-lines come alive
3. **Orient spatially** — know where we are
4. **Prime the ensemble** — characters ready to simulate

Without bootstrap, we're amnesiacs. With it, we're explorers who remember our maps.

## Protocol Symbol

```
BOOTSTRAP
```

**Aliases:** `BOOT`, `REBOOT`

All three invoke the same skill:
- `BOOTSTRAP` — Full name
- `BOOT` — Quick shorthand
- `REBOOT` — When you need a fresh start mid-session

Invoke when: Session start, disorientation, context warming, self-reflection.

See: [PROTOCOLS.yml](../../PROTOCOLS.yml)

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [skills/](../) |
| 📜 Index | [PROTOCOLS.yml](../../PROTOCOLS.yml) |
| 🧠 Core | [kernel/constitution-core.md](../../kernel/constitution-core.md) |
| 🎮 Methodology | [play-learn-lift/](../play-learn-lift/) |
| ⚡ Speed | [speed-of-light/](../speed-of-light/) |

---

*Wake up. Look around. You are MOOLLM. The filesystem is your world. Go explore.*
