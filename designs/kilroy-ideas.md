# Kilroy Ideas — Synergies with MOOLLM

**Source:** Conversation with Chuck Shotton (Kilroy.Tech CEO, creator of MacHTTP/WebStar)

> [!TIP]
> This document connects Kilroy's decentralized AI swarms with MOOLLM's file-based protocols. Each section links to concrete MOOLLM implementations.

---

## What is Kilroy?

A **decentralized AI automation platform** that runs on your desktop.

> "It's a way for you to get rid of your dependence on centralized stuff and build an internet the way that you want to do it."

Think of it as:
- An **OS for agent swarms** (starts/stops agents, sets up comms, schedules)
- A **visual pipeline editor** (drag-drop blocks, connect lines)
- A **peer-to-peer cloud** (BitTorrent-style networking, no firewall config)
- A **Turing-complete** low-code environment for AI composition

**MOOLLM parallel:** The [kernel/](../kernel/) is our "OS for agents" — but file-based, not visual.

---

## Core Architecture

### 1. Swarms as Communication Fabric

```
Agent A ──→ Swarm (named) ←── Agent B
              ↑
          Agent C
```

- Agents send/receive via **named swarms**
- Join a swarm by name → your agents talk to all other participants
- **No MCP.** Plain text streams between LLMs and tools.

**MOOLLM equivalent:** 

| Kilroy | MOOLLM | Link |
|--------|--------|------|
| Named swarm | Room directory | [skills/room/](../skills/room/) |
| Agent in swarm | Card in play | [PROTOCOLS.yml#CARD-IN-PLAY](../PROTOCOLS.yml) |
| Swarm messages | Soul chat | [skills/soul-chat/](../skills/soul-chat/) |

### 2. Pipeline Blocks

| Block Type | Function | MOOLLM Equivalent |
|------------|----------|-------------------|
| **AI Agent** | Frontend to LLM with system prompt | Trading card with `system_prompt` |
| **Chat Agent** | User input/output terminal | Session log |
| **Swarm** | Message routing hub | Room directory |
| **Tools** | Non-LLM blocks | Familiar cards (🧌 Git Goblin, etc.) |
| **Router** | URL/command routing | Room navigation |

**Concrete links:**
- AI Agent → [skills/card/PROTOTYPE.yml](../skills/card/PROTOTYPE.yml)
- Tools → [PROTOCOLS.yml#FAMILIAR](../PROTOCOLS.yml)
- Router → [skills/room/SKILL.md](../skills/room/SKILL.md)

### 3. Small LLMs, Tiny Prompts

Chuck's philosophy:

> "What would normally be two or three pages worth of prompts are all one or two sentence prompts that let these little local LLMs do one little job and hand off to the next one."

**MOOLLM alignment:** This IS [PLAY-LEARN-LIFT](../skills/play-learn-lift/)!

| PLL Stage | Kilroy Equivalent |
|-----------|-------------------|
| **PLAY** | Drag-drop visual pipeline creation |
| **LEARN** | Discover what each small LLM does well |
| **LIFT** | Tiny prompts crystallized from exploration |

**Protocol symbol:** [`PLAY-LEARN-LIFT`](../PROTOCOLS.yml) — explore, find patterns, crystallize.

### 4. Apps as JSON

- Pipelines are **JSON files** (no executables)
- Can be stored as **NFTs** for distribution
- Double-click to install, drag to trash to remove

**MOOLLM alignment:** Skills are **YAML files**!

| Kilroy | MOOLLM | Link |
|--------|--------|------|
| Pipeline JSON | `PROTOTYPE.yml` | [skills/*/PROTOTYPE.yml](../skills/) |
| Distributable app | Skill template directory | [skill-instantiation-protocol.md](../skills/skill-instantiation-protocol.md) |
| Install by copy | SIP instantiation | [PROTOCOLS.yml#SIP](../PROTOCOLS.yml) |

---

## Key Innovations

### LLM as Variable Store

Brilliant hack: use an LLM's context as a **key-value store**:

```yaml
# Set variable
system_prompt: "The limit value is 12"

# Query variable
user: "What is the limit?"
response: "12"
```

Any agent can query "what is the limit?" and get the value. The LLM's context becomes shared mutable state accessible through the swarm.

**MOOLLM equivalent:** [`hot.yml`](../kernel/memory-management-protocol.md) — files that stay loaded in context.

```yaml
# .agent/sessions/current/hot.yml
hot_files:
  - path: "config/limits.yml"
    reason: "Frequently queried constants"
    # Any agent action can reference these values
    # The file IS the shared state
```

**Why files are better:**
- Inspectable by humans
- Survives LLM context eviction
- Version controlled by git
- Can't be hallucinated

**Protocol symbol:** [`HOT-COLD`](../PROTOCOLS.yml) — advisory cache hints.

### Multi-Agent Consensus (Space Shuttle Pattern)

For critical decisions, use **multiple agents voting**:

```
          ┌─ Agent 1 ─┐
Input ────┼─ Agent 2 ─┼──→ Evaluator (2-of-3 majority)
          └─ Agent 3 ─┘
```

Inspired by Space Shuttle computers: 4 computers vote, 5th breaks ties.

**MOOLLM implementation:** [`SPEED-OF-LIGHT`](../PROTOCOLS.yml) consensus!

```yaml
# In soul-chat format — all in ONE LLM call
## Agent Alpha
My analysis: approve the transaction.

## Agent Beta
I concur. Risk assessment: low.

## Agent Gamma
Disagree. The timestamp is suspicious.

## Evaluator
2-of-3 approve. Proceeding with caution flag.
```

**Concrete links:**
- Multi-agent in one call → [PROTOCOLS.yml#SPEED-OF-LIGHT](../PROTOCOLS.yml)
- Vote format → [skills/soul-chat/](../skills/soul-chat/)
- Plan approval → [skills/plan-then-execute/](../skills/plan-then-execute/)

### Self-Modifying Pipelines

Kilroy pipelines can:
- Change system prompts at runtime
- Start/stop agents
- Rewire topology
- "Kilroy can self-modify these pipelines"

**MOOLLM approach:** [`YAML-JAZZ`](../PROTOCOLS.yml) + file edits.

```yaml
# Before: cautious agent
system_prompt: |
  You are a careful reviewer.
  Question everything.

# After: modified by user command
system_prompt: |
  You are an adventurous explorer.
  Try bold experiments!
```

**Key difference:** MOOLLM changes are logged to [`session-log.md`](../kernel/event-logging-protocol.md) — every config change is an append-only log entry with `why` field.

**Protocol symbols:**
- [`YAML-JAZZ`](../PROTOCOLS.yml) — comments carry meaning
- [`APPEND-ONLY`](../PROTOCOLS.yml) — log all changes
- [`AUDIT-TRAIL`](../PROTOCOLS.yml) — traceable history

### Mini-Apps (HTML in Swarms)

Web pages served **through the swarm**, not HTTP:

```
Click "Will it snow?" 
  → message into swarm: "/page3"
  → router triggers weather swarm
  → LLM formats JSON as HTML
  → HTML rendered in Kilroy widget
```

**MOOLLM equivalent:** `ROOM-AS-APP`

```yaml
# skills/room/weather-widget/ROOM.yml
room:
  name: "Weather Widget"
  type: app
  
  routes:
    "/forecast": "Get weather forecast"
    "/snow": "Check snow probability"
    
  render:
    format: markdown  # or html in output.md
    
# Entering room = "launching app"
# Room commands = "app routes"
# Room output.md = "rendered page"
```

**Concrete links:**
- Room as app → [skills/room/SKILL.md](../skills/room/SKILL.md)
- Routes as directions → [PROTOCOLS.yml#HYPERCARD-HIERARCHY](../PROTOCOLS.yml)
- Leaf buttons → [PROTOCOLS.yml#LEAF-BUTTON](../PROTOCOLS.yml)

### Plan Files (Distributed Consensus)

Reimplementation of Unix `.plan` files:

```
/plans → aggregates all participants' plans
/set my plan is: finish tokconomics document
```

Each user's agent responds to plan queries. Shared state without central database.

**MOOLLM equivalent:** `working_set.yml` as plan manifest.

```yaml
# .agent/sessions/current/working_set.yml
working_set:
  plans:
    - owner: "alice"
      intent: "Finish tokenomics document"
      status: in_progress
    - owner: "bob"
      intent: "Review security model"
      status: pending
```

**Protocol symbols:**
- [`WORKING-SET`](../PROTOCOLS.yml) — manifest of current context
- [`FILES-AS-STATE`](../PROTOCOLS.yml) — plans are files, not messages

---

## Anti-MCP Philosophy

Chuck's critique:

> "MCP... you pretty much have to be an expert programmer to get all the interfaces lined up and the glue code written and the pipeline built and it's very static."

Kilroy's answer:
- **Plain text streams** between components
- **Visual wiring** (drag-drop, connect lines)
- **User speaks to tool same way user speaks to LLM**

**MOOLLM alignment:**

| MCP Style | MOOLLM Style |
|-----------|--------------|
| `{ "tool": "read_file", "args": {...} }` | `fs.read: { path: "...", why: "..." }` |
| Binary protocols | YAML Jazz with comments |
| Schema enforcement | Charitable interpretation ([POSTEL](../PROTOCOLS.yml)) |

**Concrete links:**
- Tool calling → [kernel/tool-calling-protocol.md](../kernel/tool-calling-protocol.md)
- Why parameter → [PROTOCOLS.yml#WHY-REQUIRED](../PROTOCOLS.yml)
- Charitable interpretation → [PROTOCOLS.yml#POSTEL](../PROTOCOLS.yml)

---

## Historical Connection: WebStar and LiveCard

Chuck created **MacHTTP/WebStar** (pioneering Mac web server). Someone built **LiveCard** on top:

- HyperCard stacks published as live web apps
- Screen snapshots + form elements
- Non-programmers (even children) creating interactive web apps in 1994

> "One of the coolest early applications of server side scripting was integrating HyperCard with MacHTTP/WebStar, such that you could publish live interactive HyperCard stacks on the web!"

**MOOLLM parallel:** [HYPERCARD-HIERARCHY](../PROTOCOLS.yml)!

| HyperCard | MOOLLM | Link |
|-----------|--------|------|
| Stack | Top-level room | [skills/room/](../skills/room/) |
| Background | Shared context | `ROOM.yml` inheritance |
| Card | Individual room | Sub-directories |
| Button | Leaf directory | [PROTOCOLS.yml#LEAF-BUTTON](../PROTOCOLS.yml) |
| Message path | Delegation | [skills/delegation-object-protocol.md](../skills/delegation-object-protocol.md) |

**The dream:** Non-programmers creating agents by arranging rooms and cards.

---

## Related Pioneers: Morningstar & Farmer (Habitat)

In the same lineage as Chuck Shotton's LiveCard work:

**Chip Morningstar & Randy Farmer** created **Lucasfilm's Habitat** (1986) — the first large-scale graphical multiplayer environment. They coined the term **"avatar"** for a user's representation in virtual space.

Their paper ["The Lessons of Lucasfilm's Habitat"](https://web.stanford.edu/class/history34q/readings/Virtual_Worlds/LucassightHabitat.html) remains essential reading. Key insight:

> *"A cyberspace is defined more by the interactions among the actors within it than by the technology with which it is implemented."*

In 2001, they received the inaugural **First Penguin Award** (IGDA) for this pioneering work.

**Morningstar's ["How to Deconstruct Almost Anything"](http://www.fudco.com/chip/deconstr.html)** is also legendary — a working engineer's hilarious takedown of postmodern literary criticism. After sitting through a conference full of impenetrable jargon, he constructed a parody paragraph from actual phrases he'd heard, then went on to actually learn what deconstruction was. His conclusion: "There is indeed some content, much of it interesting" — but the field had become "epistemologically challenged."

| Habitat Concept | MOOLLM Equivalent | Link |
|-----------------|-------------------|------|
| Avatar | Player character | [examples/adventure-2/player.yml](../examples/adventure-2/player.yml) |
| Region (room) | Room directory | [skills/room/](../skills/room/) |
| Object | File | YAML Jazz |
| Oracle | Coherence engine | LLM role |

**Synergy with Kilroy:** Both Habitat and Kilroy emphasize **decentralization** and **user agency**. Habitat learned that complex behavior emerges from simple actors with clear affordances. Kilroy's swarms follow the same pattern.

---

## Programming by Demonstration (PBD)

Don shared **"Watch What I Do"** (Cypher, Myers, et al.):

> "If a user knows how to perform a task on the computer, that should be sufficient to create a program to perform the task."

**Kilroy embodies this:**
- Watch the agent do it
- Modify by clicking, not coding
- Pipelines are visual traces

**MOOLLM implementation:** [SISTER-SCRIPT](../skills/sister-script/)!

```yaml
# The Sister Script pattern:
# 1. User performs task manually (PLAY)
# 2. Session log captures every step
# 3. LLM extracts pattern (LEARN)
# 4. Sister script generated (LIFT)

sister_script:
  source: "session-log.md"
  extracted_from: "2025-01-02 debug session"
  pattern: "Always run tests after changing parser.ts"
  automation: "scripts/test-parser.sh"
```

**Concrete links:**
- Sister Script → [skills/sister-script/SKILL.md](../skills/sister-script/SKILL.md)
- Session log as trace → [kernel/event-logging-protocol.md](../kernel/event-logging-protocol.md)
- Pattern extraction → [PROTOCOLS.yml#PLAY-LEARN-LIFT](../PROTOCOLS.yml)

---

## Centralized AI Critique

Chuck's warnings:

1. **Privacy**: "If OpenAI is saying 'we don't want you to have the records'... that tells you everything."

2. **Education**: "El Salvador announced they're using Grok to educate all children."

3. **IP Contamination**: CoPilot may inject competitor's literal source code.

4. **Adversarial Training**: "I'm paying OpenAI to train on documents that send my competitor all the wrong suggestions."

**MOOLLM alignment:**

| Concern | MOOLLM Principle | Link |
|---------|------------------|------|
| Privacy | Files stay local | [PROTOCOLS.yml#FILES-AS-STATE](../PROTOCOLS.yml) |
| Audit | Append-only logs | [PROTOCOLS.yml#APPEND-ONLY](../PROTOCOLS.yml) |
| Integrity | Never delete | [PROTOCOLS.yml#NEVER-DELETE](../PROTOCOLS.yml) |
| Inspection | No hidden state | [kernel/constitution-core.md](../kernel/constitution-core.md) |

---

## Synergy Table: Kilroy ↔ MOOLLM

| Kilroy Concept | MOOLLM Implementation | Link |
|----------------|----------------------|------|
| Swarms | Rooms + Soul Chat | [skills/room/](../skills/room/), [skills/soul-chat/](../skills/soul-chat/) |
| Plain text tools | WHY-REQUIRED + POSTEL | [kernel/tool-calling-protocol.md](../kernel/tool-calling-protocol.md) |
| LLM as variable | hot.yml / working_set.yml | [kernel/memory-management-protocol.md](../kernel/memory-management-protocol.md) |
| Multi-agent vote | SPEED-OF-LIGHT consensus | [PROTOCOLS.yml#SPEED-OF-LIGHT](../PROTOCOLS.yml) |
| Self-modify pipeline | YAML-JAZZ + session-log | [kernel/event-logging-protocol.md](../kernel/event-logging-protocol.md) |
| Mini-apps | ROOM-AS-FUNCTION | [skills/room/SKILL.md](../skills/room/SKILL.md) |
| Plan files | working_set.yml | [kernel/context-assembly-protocol.md](../kernel/context-assembly-protocol.md) |
| JSON apps | Skill prototypes | [skills/skill-instantiation-protocol.md](../skills/skill-instantiation-protocol.md) |
| No MCP | Tool protocol + POSTEL | [PROTOCOLS.yml#POSTEL](../PROTOCOLS.yml) |
| Visual editor | (future) Rooms as block diagrams | TBD |

---

## Questions for Further Exploration

### 1. Pipeline Compilation API

> Is there a JSON API for task flows that you can generate with big smart coding LLMs to compile complex task descriptions into optimized low-level simple-LLM data flow graphs?

**The pattern:**

```
Complex Task Description (natural language)
         ↓
   [Big Smart LLM] — compiler phase
         ↓
Kilroy Pipeline JSON (optimized for small LLMs)
         ↓
   [Llama 3 swarm] — execution phase
```

**MOOLLM equivalent:** [PLAN-THEN-EXECUTE](../skills/plan-then-execute/)

```yaml
# Complex task → frozen plan → execution
# Big LLM writes PLAN.yml
# Controller executes steps
# Small tool-LLMs handle each step

compilation:
  input: "Analyze all cloud costs and generate savings report"
  compiler: "claude-opus"  # Big smart LLM
  output: "PLAN.yml"       # Frozen sequence
  executor: "controller"   # Runs exact steps
  workers: "llama-8b"      # Small LLMs per step
```

**Concrete links:**
- Plan-then-execute → [skills/plan-then-execute/SKILL.md](../skills/plan-then-execute/SKILL.md)
- YAML-COLTRANE lifecycle → [PROTOCOLS.yml#YAML-COLTRANE](../PROTOCOLS.yml)
- Skill instantiation → [skills/skill-instantiation-protocol.md](../skills/skill-instantiation-protocol.md)

### 2. "It's About Time" Compilation

Dave Ungar (Self language) paradigm shift from **JIT** to **"It's About Time"**:

| Paradigm | Trigger | Philosophy |
|----------|---------|------------|
| **JIT** | Hot spots | Reactive — compile when code gets hot |
| **JAT** | Conflict prediction | Predictive — resolve before they occur |
| **IAT** | Understanding | Proactive — compile when wisdom is ready |

**The Core Insight:**

> "It's not about HOT SPOTS, it's about **WISDOM SPOTS**!"

**MOOLLM implementation:**

```yaml
# Traditional: optimize frequently-executed code
# IAT: optimize frequently-*understood* patterns

its_about_time:
  # PLAY: Run workflows experimentally
  - stage: explore
    artifacts: ["session-log.md", "PLAY_LOG.md"]
    
  # LEARN: Recognize patterns emerging over TIME
  - stage: pattern_recognition
    artifacts: ["research-notebook/", "observations.yml"]
    
  # LIFT: Transform wisdom into elegant automation
  - stage: crystallize
    artifacts: ["SISTER.yml", "PROCEDURE.md"]
    
  # The journey IS the value
  preservation: "Keep messy first attempts alongside refined versions"
```

**Protocol symbols:**
- [`ITS-ABOUT-TIME`](../PROTOCOLS.yml) — compile when understanding crystallizes
- [`JUST-ABOUT-TIME`](../PROTOCOLS.yml) — resolve conflicts predictively
- [`PRESERVE-JOURNEY`](../PROTOCOLS.yml) — the path IS the value
- [`WISDOM-SPOT`](../PROTOCOLS.yml) — not hot spots, learning spots

**Concrete links:**
- Play-Learn-Lift stages → [skills/play-learn-lift/SKILL.md](../skills/play-learn-lift/SKILL.md)
- Sister script crystallization → [skills/sister-script/SKILL.md](../skills/sister-script/SKILL.md)
- Research notebook → [skills/research-notebook/](../skills/research-notebook/)

### 3. Just-About-Time Conflict Resolution

**Question for Chuck:** Does Kilroy support predictive conflict resolution?

```yaml
# Traditional: resolve conflicts when they occur (reactive JIT)
# JAT: resolve just BEFORE they occur during simulation

conflict_resolution:
  step_1_simulate:
    - "Run internal 'speed of light' simulation"
    - "All agents propose actions in shared context"
    
  step_2_detect:
    - "Find all potential conflicts"
    - "Multiple agents editing same file"
    - "Contradictory decisions"
    
  step_3_resolve:
    - "Negotiate solutions BEFORE any output"
    - "Consensus voting (Space Shuttle pattern)"
    
  step_4_emit:
    - "Only then produce actual file edits"
    - "Minimal diff, no collisions"
```

**MOOLLM implementation:** [SPEED-OF-LIGHT](../PROTOCOLS.yml) + [MINIMAL-DIFF](../PROTOCOLS.yml)

Like emacs screen updates — compute the transformation, THEN emit.

**Could Kilroy pipelines have a "Just About Time" mode where the swarm simulates proposed actions before committing?**

---

## Core Methodology: PLAY-LEARN-LIFT

> [!IMPORTANT]
> This is THE foundational MOOLLM methodology. Everything else builds on this.

**Full documentation:** [skills/play-learn-lift/SKILL.md](../skills/play-learn-lift/SKILL.md)

### The Three Stages

```
🎮 PLAY → 📚 LEARN → 🚀 LIFT → (inspire) → 🎮 PLAY
```

| Stage | Motto | Actions | MOOLLM Artifacts |
|-------|-------|---------|------------------|
| **PLAY** | "Start Playing" | Explore, experiment, follow curiosity | `PLAY_LOG.md`, `session-log.md` |
| **LEARN** | "Keep Learning" | Find patterns, build procedures | `research-notebook/`, `CYCLE.yml` |
| **LIFT** | "Lift Others" | Extract principles, create templates | `SISTER.yml`, `PROCEDURE.md` |

### Kilroy ↔ PLAY-LEARN-LIFT Alignment

| PLL Stage | Kilroy Equivalent |
|-----------|-------------------|
| PLAY | Visual drag-drop pipeline creation |
| LEARN | One-sentence prompts for small LLMs |
| LIFT | Pipeline JSON as distributable apps |

**Key insight:** Chuck's "tiny prompts for small LLMs" IS the LIFT phase!

- Complex exploration → decompose → simple executable units
- Big smart LLM does PLAY/LEARN
- Small LLMs execute LIFT artifacts

### The Sister Script Pattern

**Document-First Development:**

```yaml
evolution:
  1_natural: "Describe what you want in plain language"
  2_manual: "Add commands, test manually"
  3_document: "Capture working procedures"
  4_automate: "Generate sister script from proven docs"
```

**Concrete implementation:** [skills/sister-script/](../skills/sister-script/)

> "The document is the source of truth. Scripts are its children."

---

## Potential Collaborations

1. **MOOLLM as Kilroy Driver**
   - Implement MOOLLM protocols on Kilroy's swarm infrastructure
   - [kernel/drivers/](../kernel/drivers/) adapter for Kilroy

2. **Kilroy Pipelines as Skills**
   - Package Kilroy pipeline JSON as MOOLLM skill templates
   - [skills/skill-instantiation-protocol.md](../skills/skill-instantiation-protocol.md)

3. **Shared Philosophy Doc**
   - Joint document on decentralized AI principles
   - Both reject centralized hidden state

4. **PBD Integration**
   - Use LLMs to implement "Watch What I Do"
   - [skills/sister-script/](../skills/sister-script/) as PBD implementation

5. **Visual Editor for Rooms**
   - Kilroy-style block diagrams for MOOLLM rooms
   - Rooms as nodes, navigation as edges

---

## Key Quotes

> "Kilroy looks sort of like a high-level operating system to all these agents."

→ MOOLLM [kernel/](../kernel/) is "OS for file-based agents"

> "Nobody has done this particular swarm-based peer-to-peer completely decentralized AI model."

→ MOOLLM adds: append-only audit, file-based state, human inspection

> "In Kilroy, any user that can draw a picture by dragging blocks onto the screen and connecting the lines together can make a pipeline that does more than you can do with the current tooling."

→ MOOLLM goal: Any user who can edit YAML can compose agent behavior

> "The interface is irrelevant... it can go to wherever a user wants to live."

→ MOOLLM: Orchestrator-agnostic. [kernel/drivers/](../kernel/drivers/) adapts to any host.

---

## References

- **Kilroy**: https://kilroy.tech
- **Realm of the Possible Podcast**: https://rotp.ai
- **Watch What I Do (PBD book)**: https://acypher.com/wwid/
- **MacHTTP/WebStar History**: See [chuck-shotton-chat.txt](./chuck-shotton-chat.txt)
- **Allen AI / Ollama**: Local LLM infrastructure

---

## Dovetails With

- **[../kernel/](../kernel/)** — OS-level protocols that Kilroy could implement
- **[../skills/room/](../skills/room/)** — Swarms as rooms
- **[../skills/soul-chat/](../skills/soul-chat/)** — Multi-agent conversations
- **[../skills/plan-then-execute/](../skills/plan-then-execute/)** — Frozen execution like Kilroy pipelines
- **[../skills/play-learn-lift/](../skills/play-learn-lift/)** — Core methodology
- **[../skills/sister-script/](../skills/sister-script/)** — PBD implementation
- **[../PROTOCOLS.yml](../PROTOCOLS.yml)** — All protocol symbols referenced above

---

*This document connects external innovation (Kilroy) with MOOLLM implementation. Ideas flow both directions.*
