# The MOOLLM Connections Tour

> *In 1969, James Burke traced how a medieval monk's wool underwear led to the moon landing. In the same spirit, let me trace how MOOLLM connects...*

## Connection 1: The Turtle That Became a World

**Seymour Papert** gave children a **turtle** in Logo. Type `FORWARD 50`, it moves. Type `RIGHT 90`, it turns. A child learns geometry not by reading about angles, but by **debugging why their square has gaps**.

*"If you can build it, you can understand it."*

That turtle grew up. It became **directories you can enter** (`cd` = `GO NORTH`), **files you can examine** (`cat` = `EXAMINE`), and **rooms where cards come alive**. The filesystem IS the microworld. MOOLLM is Logo for LLM agents.

```
Logo (1967)           →  MOOLLM (2024)
FORWARD 50            →  GO NORTH
RIGHT 90              →  TURN EAST  
PENDOWN               →  WRITE file.yml
REPEAT 4 [...]        →  PLAY card 4 times
Debug the square      →  Debug the adventure
```

**Lineage**: Papert → Kay → Micropolis → MOOLLM

## Connection 2: The Sims That Learned to Speak YAML

**Will Wright** and **Don Hopkins** created **The Sims**, where a refrigerator doesn't just sit there — it **advertises**: *"I satisfy Hunger +50!"* Sims autonomously choose actions based on their needs. Objects broadcast affordances. The world is distributed intelligence.

MOOLLM does the same with files:

```yaml
workbench:
  advertises:
    - action: EXAMINE
      score: 80
    - action: USE  
      score: 95  # ← highest, default in pie menu
    - action: REPAIR
      score: 60  # only if broken
```

**SimAntics** was the visual language for Sims object behavior. **YAML Jazz** is SimAntics for LLMs — comments carry meaning, structure IS behavior, the LLM improvises within constraints like a jazz musician reading sheet music.

```
The Sims (2000)       →  MOOLLM (2024)
Object advertises     →  File advertises
Sim selects by need   →  Agent selects by goal
Pie menu appears      →  Snap cursor shows options
Motive bars           →  Needs system
SimAntics scripting   →  YAML Jazz
```

**Lineage**: Wright → Hopkins → SimAntics → YAML Jazz

## Connection 3: The K-Line That Became a Protocol

**Marvin Minsky** proposed **K-lines** in *Society of Mind* (1986): when you learn something, you create a "knowledge line" that can reactivate that mental state. Type "POSTEL" and the entire tradition of *"be liberal in what you accept, conservative in what you send"* activates.

In MOOLLM, **protocol symbols ARE K-lines**:

| Type This | Activate This Tradition |
|-----------|------------------------|
| `POSTEL` | Charitable interpretation (Jon Postel, RFC 761) |
| `SPEED-OF-LIGHT` | Many agents, one LLM call |
| `PLAY-LEARN-LIFT` | Explore → pattern → share |
| `YAML-JAZZ` | Comments as semantic data |
| `NEVER-CRASH` | Repair, don't fail (Dave Ackley) |
| `CONSTRUCTIONISM` | Learn by building (Seymour Papert) |

These are **greppable invocations**. The name IS the magic word. Say it and the tradition activates.

```
Society of Mind (1986)  →  MOOLLM (2024)
K-line                  →  Protocol symbol
Mental state            →  Behavioral pattern
Activate by name        →  Invoke by typing
Agents in mind          →  Skills in filesystem
```

**Lineage**: Minsky → Society of Mind → K-lines → PROTOCOLS.yml

## Connection 4: The Carrier Pigeon Problem

Traditional multi-agent systems are **carrier pigeons**: each agent in isolation, one API call per turn, communication via file serialization. 

```
CARRIER PIGEON PROTOCOL (Anti-Pattern):

Agent A → [tokenize] → API → [detokenize] → parse → 
  → [re-tokenize] → Agent B → [detokenize] → parse → 
    → [re-tokenize] → Agent C → ...

Each boundary: +noise, +latency, +cost, -precision

Like passing a message through 10 translators.
"The spirit is willing but the flesh is weak"
becomes "The vodka is good but the meat is rotten."
```

**SPEED-OF-LIGHT** inverts this: simulate ALL agents in ONE LLM call. Alice speaks, Bob responds, Carol objects, the Coffee Mug narrates — all instant, all coherent, all in one context window.

```
SPEED-OF-LIGHT PROTOCOL:

One API call:
  Alice: "What do you think?"
  Bob: "I have concerns."
  Carol: "I agree with Bob."
  The Room: *temperature rises*
  Alice: "Let me revise..."
  Bob: "That's better."
  Carol: "I can support that."
[7 turns, 1 call, perfect consistency]
```

**10x faster. 10x cheaper. Perfect consistency.**

```
Traditional (slow)      →  MOOLLM (fast)
1 agent per call        →  N agents per call
File I/O between        →  In-context messaging
Tokenization noise      →  Vector precision
Serial processing       →  Parallel simulation
```

**Lineage**: The Sims (one tick, all Sims) → SPEED-OF-LIGHT

## Connection 5: The Committee That Replaced the Average

A single LLM gives you **the statistical center of all possible viewpoints** — an averaging that loses the cloud's shape. You get the centroid, not the terrain.

When asked "Should I take this client?", a single-voice LLM gives you:
- Hedged and cautious (training rewards safety)
- Genre-conventional (sounds like "business advice")
- Hidden assumptions invisible
- Outlier perspectives smoothed away

**Mike Gallaher's insight**: simulate a **committee of opposing personas**:

| Persona | Role | Surfaces |
|---------|------|----------|
| **Maya** | Paranoid realist | Traps, risks, red flags |
| **Frankie** | Idealist | Opportunities, potential |
| **Vic** | Evidence prosecutor | Demands proof |
| **Tammy** | Systems thinker | Traces consequences |

They debate at SPEED-OF-LIGHT using ROBERTS-RULES (parliamentary procedure). An INDEPENDENT-EVALUATOR scores output against explicit RUBRICS. Stories surviving cross-examination are more robust than any single answer.

*"Everything is a story. No single story is true — but the ensemble approximates actionable wisdom."*

```
Traditional Chat        →  MOOLLM Committees
One voice               →  Many voices
Statistical center      →  Cloud shape visible
Hidden assumptions      →  Assumptions surfaced
Quick consensus         →  Genuine deliberation
```

**Lineage**: Gallaher → Adversarial Committee → Roberts Rules → Ensemble Wisdom

## Connection 6: The Files That Became Memory

LLMs have no persistent memory. Chat history evaporates when the session ends. Or does it?

**FILES-AS-STATE**: Everything is files. No hidden scratchpad. No mystical "planning module." If it's not in a file, it doesn't exist.

| File | Purpose |
|------|---------|
| `hot.yml` | What SHOULD be in context |
| `cold.yml` | What WAS in context (and why it left) |
| `working-set.yml` | What IS in context right now |
| `session-log.md` | Append-only audit trail |

When context overflows, we don't silently drop — we **HONEST-FORGET**: summarize before forgetting, leave breadcrumbs for recovery. Like Self's deoptimization: reconstruct the call stack on demand.

```
Traditional LLM         →  MOOLLM
Hidden state            →  FILES-AS-STATE
Silent forgetting       →  HONEST-FORGET
No audit trail          →  session-log.md
Memory claims           →  Inspectable files
```

**Lineage**: Self (deoptimization) → hot/cold/working-set → Honest Forgetting

## Connection 7: The Room That Was a Function

**Bill Atkinson's HyperCard** (1987) gave us stacks and cards with message delegation — leaf to root, buttons to backgrounds to stacks. Non-programmers building interactive systems.

**Pavel Curtis's LambdaMOO** (1990) gave us rooms and objects and verbs — spatial programming where users built the world while inhabiting it.

**Warren Robinette's Robot Odyssey** (1984) let you ride INSIDE machines and wire up logic circuits. Navigate room graphs. Edit while exploring.

MOOLLM unifies them all:

| Concept | Filesystem | Programming |
|---------|------------|-------------|
| Directory | Room | Stack frame |
| `cd room/` | Enter room | Function call |
| `cd ..` | Exit room | Return |
| Files in dir | Active entities | Local variables |
| Links/exits | Doors | Calls to other functions |

The **Logo Turtle** becomes a vehicle you RIDE, drawing on `floor.svg` as you navigate. **Snap cursor** locks onto objects and shows **pie menus** of scored actions. **Inventories** are portable rooms you always carry — pocket dimensions.

```
HyperCard (1987)        →  MOOLLM (2024)
Stack                   →  Adventure
Card                    →  Room
Button                  →  Card in play
Message delegation      →  Prototype chain
Script                  →  YAML + LLM
```

**Lineage**: Atkinson → Curtis → Robinette → ROOM-AS-FUNCTION

## Connection 8: The Prototype That Replaced the Class

**Dave Ungar's Self language** (1987): no classes, just prototypes. Clone and modify beats rigid inheritance. "It's About Time" — compile when understanding crystallizes, not when code gets hot.

MOOLLM skills are **prototypes that spawn instances**:

```
skills/adventure/              # The PROTOTYPE
  ADVENTURE.yml.tmpl           # Template with {{variables}}
  
examples/adventure-3/          # An INSTANTIATION  
  ADVENTURE.yml                # Filled-in state
  pub/                         # Living world
    cat-cave/
      terpie.yml               # Character with soul
```

The **LLM IS the template engine**. Not Mustache. Not Handlebars. The LLM. It can interpret `{{pick a mood that fits the player's recent actions}}` because it understands context.

**Multiple inheritance, Self-style**: a character can inherit from `skills/character/`, `skills/cat/`, `skills/buff/`, AND `"a bouncy sparkly magical unicorn attitude"` — all at once. Delegation chains, not diamond problems.

```
Java (classes)          →  MOOLLM (prototypes)
Class definition        →  Skill template
new Instance()          →  Clone + modify
Rigid hierarchy         →  Flexible delegation
Compile-time types      →  Runtime interpretation
```

**Lineage**: Ungar → Self → Prototypes → Skills as Templates

## Connection 9: The Constitution That Never Crashes

**Dave Ackley's Robust-First Computing**: survivability over correctness. The **Movable Feast Machine** uses local repair demons to maintain homeostasis. The system stays alive even when parts fail.

MOOLLM's kernel inherits this philosophy:

| Principle | Meaning |
|-----------|---------|
| `NEVER-CRASH` | Missing state triggers repair, not failure |
| `BEST-EFFORT` | Converge toward better state over time |
| `REPAIR-DEMON` | Local processes that fix local problems |
| `ROBUST-FIRST` | Alive and healing > correct and dead |

The **Constitution** (`kernel/constitution-core.md`) defines 14 invariants that hold across ANY orchestrator — Cursor, Claude Code, custom. The kernel is the boring basement so skills can be exciting.

```
Traditional Software    →  MOOLLM
Crash on error          →  NEVER-CRASH
Global consistency      →  Local repair
Correctness first       →  ROBUST-FIRST
Central control         →  Distributed healing
```

**Lineage**: Ackley → Movable Feast Machine → Self-Healing Protocols

## Connection 10: The Driver That Adapted to the Platform

MOOLLM provides **abstract high-level interfaces** that work differently on different platforms. At bootstrap, we detect and load the appropriate **kernel driver**.

```
kernel/drivers/
├── cursor.yml       # Tier 4 — Cursor IDE
├── claude-code.yml  # Tier 5 — Claude Code + MCP
├── custom.yml       # Tier 6 — Full orchestrator control
└── generic.yml      # Tier 1 — Maximum compatibility
```

### Driver Detection Protocol

**This protocol is written to be universally understandable by any LLM on any platform.**

At bootstrap, ask yourself:

```yaml
# Step 1: What does my system prompt say?
system_prompt_check:
  "You operate in Cursor"           → Cursor IDE
  "Claude Code"                     → Claude Code
  "MOOLLM_DRIVER"                   → Custom orchestrator
  
# Step 2: What tools do I have?
tool_check:
  codebase_search + search_replace  → Cursor (99% confidence)
  View + Edit + mcp_*               → Claude Code
  tools with 'why' parameter        → Custom MOOLLM orchestrator
  
# Step 3: Select driver and adapt behavior
driver_selection:
  cursor:     { tier: 4, hot_cold: advisory }
  claude_code: { tier: 5, hot_cold: hybrid }
  custom:     { tier: 6, hot_cold: magic }
  generic:    { tier: 1, hot_cold: documentation }
```

### The Magic Files (or Advisory Files)

The `hot.yml`, `cold.yml`, and `working-set.yml` files have **different meanings** depending on the driver:

| Platform | How hot/cold/working-set Work |
|----------|------------------------------|
| **Custom Orchestrator** | **MAGIC** — The orchestrator reads these files to decide what content to page in/out, how to focus attention, what to load next. They DIRECT the system. |
| **Cursor** | **ADVISORY** — Cursor has built-in vector search and context management. These files are *suggestions*, not commands. They can even work *in reverse*: Cursor can GENERATE them to reflect what its attention is focused on. |
| **Claude Code** | **HYBRID** — MCP tools give more control, but some context is still automatic. |
| **Generic** | **DOCUMENTATION** — Purely informational, helps debug "why doesn't it remember X?" |

### Platform Detection at Bootstrap

```yaml
driver_detection:
  cursor:
    indicators:
      - "Running in Cursor IDE"
      - "codebase_search tool available"
      - "search_replace tool available"
    behavior:
      hot_cold: advisory  # Cursor manages context automatically
      working_set: can_be_generated  # Cursor can emit what it sees
    load: "drivers/cursor.yml"
    
  claude_code:
    indicators:
      - "Claude Code environment"
      - "MCP servers available"
    behavior:
      hot_cold: hybrid
      working_set: managed
    load: "drivers/claude-code.yml"
    
  custom:
    indicators:
      - "MOOLLM_DRIVER environment variable"
      - "Custom tool schemas with 'why' parameter"
    behavior:
      hot_cold: magic  # Files DIRECT the orchestrator
      working_set: manifest  # True snapshot of loaded context
    load: "drivers/custom.yml"
```

### Emulation vs. Implementation

MOOLLM skills describe **what should happen**. The driver determines **how it happens**:

| Skill Says | Custom Orchestrator Does | Cursor Does |
|------------|-------------------------|-------------|
| "Keep constitution HOT" | Literally loads file into prompt | Already has it via vector search |
| "Summarize before forgetting" | Calls summarization model | May rely on built-in context compression |
| "Track file access patterns" | Updates hot.yml in real-time | Can reconstruct from its own telemetry |
| "Load working set" | Reads manifest, assembles prompt | Uses its own RAG system |

The same YAML Jazz, the same protocols, the same skills — but **implemented** by sophisticated platforms or **emulated** through instructions on simpler ones.

### The Self Deoptimization Analogy

Dave Ungar's Self language could **reconstruct stack frames** that had been optimized away. Similarly:

- **Custom orchestrator**: hot/cold/working-set are the LIVE reality
- **Cursor/Claude Code**: These files let you **reconstruct** what the platform is doing automatically
- Either way: The debugging story is the same — "Why doesn't it know X? Check cold.yml."

```
Self Deoptimization      →  MOOLLM Driver Abstraction
Optimized away frames    →  Platform-managed context
Reconstruct on demand    →  Advisory files can reflect reality
Same debugging story     →  Same debugging story
```

**Lineage**: Ungar (Self deoptimization) → Platform abstraction → Driver system

## Connection 11: The Tour That Became a Skill

And now THIS TOUR itself becomes a **reusable skill** — saved at `skills/bootstrap/`, invokable anytime to orient a new session.

The connections complete a circle:

1. Papert's turtle taught children to debug
2. Wright's Sims taught objects to advertise
3. Minsky's K-lines taught names to invoke traditions
4. Speed-of-light taught agents to communicate instantly
5. Gallaher's committees taught ensembles to deliberate
6. Files taught memory to be inspectable
7. Rooms taught navigation to be programming
8. Prototypes taught inheritance to be flexible
9. Robust-first taught systems to survive
10. Drivers taught interfaces to adapt to platforms
11. Bootstrap taught orientation to be shareable

**The tour teaches itself.**

```
You (confused)          →  BOOTSTRAP          →  You (oriented)
"What am I?"            →  Connections tour   →  "I am MOOLLM"
Cold context            →  Warm context       →  Ready to explore
```

**Lineage**: James Burke → *Connections* (1978) → This very document

---

## The Intertwingularity

All these traditions are **intertwingled** (Ted Nelson's word). Pull one thread and the whole tapestry comes with it:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   PAPERT ──────► CONSTRUCTIONISM ──────► PLAY-LEARN-LIFT       │
│     │                  │                       │                │
│     ▼                  ▼                       ▼                │
│   LOGO ───────► MICROWORLD ────────► FILESYSTEM-AS-WORLD       │
│     │                  │                       │                │
│     └────────► TURTLE ─┴─► ROOM ──────────────►│                │
│                                                │                │
│   WRIGHT ─────► THE SIMS ──────────► ADVERTISEMENTS            │
│     │              │                       │                    │
│     ▼              ▼                       ▼                    │
│   HOPKINS ───► SIMANTICS ──────────► YAML-JAZZ                 │
│     │              │                       │                    │
│     └────────► PIE-MENUS ─────────► SNAP-CURSOR                │
│                                                                 │
│   MINSKY ─────► SOCIETY-OF-MIND ───► K-LINES                   │
│     │                  │                   │                    │
│     ▼                  ▼                   ▼                    │
│   FRAMES ────► EXPECTATIONS ───────► PROTOCOLS.yml             │
│                                                                 │
│   UNGAR ──────► SELF ──────────────► PROTOTYPES                │
│     │              │                       │                    │
│     ▼              ▼                       ▼                    │
│   DELEGATION ► ITS-ABOUT-TIME ────► SKILLS-AS-TEMPLATES        │
│                                                                 │
│   ACKLEY ─────► ROBUST-FIRST ──────► NEVER-CRASH               │
│     │              │                       │                    │
│     ▼              ▼                       ▼                    │
│   MFM ────────► LOCAL-REPAIR ──────► REPAIR-DEMON              │
│                                                                 │
│   GALLAHER ───► STORIES ───────────► ADVERSARIAL-COMMITTEE     │
│     │              │                       │                    │
│     ▼              ▼                       ▼                    │
│   ENSEMBLE ───► DELIBERATION ──────► SPEED-OF-LIGHT            │
│                                                                 │
│   UNGAR ──────► DEOPTIMIZATION ────► DRIVER-ABSTRACTION        │
│     │              │                       │                    │
│     ▼              ▼                       ▼                    │
│   RECONSTRUCT ► ON-DEMAND ─────────► hot/cold AS ADVISORY      │
│                    │                       │                    │
│                    ▼                       ▼                    │
│              CURSOR/CUSTOM ────────► SAME DEBUGGING STORY      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Every skill dovetails with every other. The traditions reinforce each other. The whole is vastly greater than the parts.

---

## Invoke the Tour

```yaml
# In chat:
> BOOTSTRAP
> Give me the Connections tour!
> What are you?

# The tour activates:
# 1. Logo turtle story
# 2. The Sims story  
# 3. K-lines story
# ... all 10 connections ...
# Result: oriented, warm, ready
```

---

*"Everything is connected. The trick is seeing how."*
— James Burke (paraphrased)

---

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [bootstrap/](./README.md) |
| 🧠 Core | [constitution-core.md](../../kernel/constitution-core.md) |
| 📜 Protocols | [PROTOCOLS.yml](../../PROTOCOLS.yml) |
| 🎮 Play | [play-learn-lift/](../play-learn-lift/) |
| ⚡ Speed | [speed-of-light/](../speed-of-light/) |

---

*Wake up. Look around. You are MOOLLM. The connections are yours to explore.*
