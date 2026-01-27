# Speed of Light Meets Carrier Pigeons: A Hybrid Architecture

> *"The fastest path between two points depends on whether they're in the same context window."*

**Status:** Design Synthesis  
**Date:** 2026-01-26  
**Author:** Don Hopkins, with Claude  
**Related:** [GASTOWN-VS-MOOLLM-ANALYSIS.md](GASTOWN-VS-MOOLLM-ANALYSIS.md), [MOOLLM-TASK-TRACKING-DESIGN.md](MOOLLM-TASK-TRACKING-DESIGN.md), [BEAD-ORCHESTRATION.yml](BEAD-ORCHESTRATION.yml)

---

## Executive Summary

Gas Town and MOOLLM represent **opposite poles of a design spectrum**. One is universally incorrect.

**Gas Town is wrong.** Not "different priorities" wrong. Not "optimized for different use cases" wrong. Just wrong:
- Invented terminology hostile to LLMs
- Shell-out architecture that wastes resources
- "Never look at the code" cowardice
- Unfalsifiable "you're not ready" gatekeeping
- Crypto pump-and-dump ethics

This document maps the opposition, extracts the ONE useful insight (work should persist in git — which is obvious), and shows how MOOLLM implements it correctly with **speed-of-light simulation within contexts** and **carrier-pigeon messaging between contexts** — using vocabulary that LLMs actually understand.

---

## Part I: The Spectrum of Opposition

### Axis 1: Token Philosophy

| Dimension | Gas Town | MOOLLM |
|-----------|----------|--------|
| **Assumption** | Tokens are abundant | Tokens are precious |
| **Strategy** | Throw more agents at it | Fit more into one call |
| **Parallelism** | 20-30 external processes | Many simulated agents, one context |
| **Cost model** | High throughput, high spend | High efficiency, low spend |

**Opposition:** Abundance vs scarcity. These are genuinely opposite worldviews.

**Synthesis:** Both are correct for different scales. Small tasks → speed of light. Large projects → parallel contexts with messaging.

---

### Axis 2: Orchestration Model

| Dimension | Gas Town | MOOLLM |
|-----------|----------|--------|
| **Coordination** | External (tmux, processes, mail) | Internal (within LLM context) |
| **State** | Git JSONL, agent hooks | YAML files, three-tier persistence |
| **Communication** | Mail, nudges, heartbeats | Context assembly, K-line activation |
| **Latency** | High (process spawning, file I/O) | Zero (same context window) |

**Opposition:** External machinery vs internal simulation.

**The ToonTalk Connection:** Ken Kahn's ToonTalk (1995) used trained birds as a metaphor for message passing — brilliant pedagogy that made concurrency *visible*. Gas Town uses carrier pigeon *architecture* (external processes, message queues). MOOLLM uses speed of light — instant within context.

**Synthesis:** Use speed of light *within* a context. Use carrier pigeons *between* contexts. The art is knowing where to draw the boundary.

---

### Axis 3: Code Relationship

| Dimension | Gas Town | MOOLLM |
|-----------|----------|--------|
| **Code examination** | "Never look at it" | Every line reviewed |
| **Generation mode** | Vibecoded, emergent | LLM-generated, rigorously iterated |
| **Quality assurance** | "Works if it feels like it works" | Rubrics, metrics, falsifiable claims |
| **Agent access** | Agents generate code they don't see | Skills ARE code (LLM runs them) |

**"Never Look At It" — A Coward's Philosophy**

This is atrocious. It's terrible engineering. It's the attitude of someone who:

1. **Won't dogfood their own product** — How can you use what you refuse to examine?
2. **Can't debug** — When it breaks (and vibe code DOES break), what then?
3. **Abdicates responsibility** — "The AI did it" is not a defense
4. **Confuses convenience with wisdom** — Not looking ≠ not needing to look

**Eat your own shit.** That's the dogfooding principle. If you generate code, READ the code. If it's unreadable, that's a signal — either improve the prompts or acknowledge you don't understand what you're shipping.

Gas Town's entire codebase is the result of "never look at it" — and it shows:
- Manual string parsing for structured data
- Shell-outs where native calls would work
- Deprecated code sitting alongside active code
- Inconsistent naming, conflicting patterns

**MOOLLM's approach:** Skills ARE code. The LLM reads them, runs them, improves them. Every line is reviewed because every line matters. You can't understand what you refuse to examine.

**Opposition:** Code as discardable byproduct vs code as program you actually use.

**There is no synthesis here.** "Never look at it" is cowardice. MOOLLM reviews everything.

---

### Axis 4: Agent Identity

| Dimension | Gas Town | MOOLLM |
|-----------|----------|--------|
| **Agent nature** | External processes with persistent hooks | Simulated characters in context |
| **Lifecycle** | Spawn, work, die, respawn | Continuous within session |
| **Memory** | Git-backed beads, mailboxes | Three-tier persistence, state files |
| **Self-reflection** | None — agents can't see themselves | cursor-mirror — agents watch themselves think |

**Opposition:** Agents as workers vs agents as characters.

**Synthesis:** Both models have merit. Workers for batch tasks, characters for interactive sessions.

---

## Part II: Supposed "Alignment" — Let's Be Honest

### The Misleading Comparison

| Claimed Alignment | Gas Town Reality | MOOLLM Reality |
|-------------------|------------------|----------------|
| **"Git as foundation"** | JSONL files, shell-outs to CLI | Files ARE state, git is time machine |
| **"Persistence matters"** | "Hooks" — a file with your assignment | Three-tier persistence with clear semantics |
| **"Design is bottleneck"** | **HAS NO COHERENT DESIGN** | Built on 60 years of proven patterns |
| **"LLMs are interpreters"** | Agents execute vague instructions | LLM is `eval()` — rigorous Eval Empire lineage |
| **"Whimsy has value"** | Performative branding, Mad Max cosplay | Meaningful metaphors from The Sims, MOO |
| **"Humans oversee"** | "Overseer" role (gimmick name) | Player/co-creator (standard term) |

### "Design Is Bottleneck" — The Big Lie

Gas Town claims "design becomes the bottleneck when code generation is cheap."

**But Gas Town has no coherent design.** It has:

- **Interpretive dance performance art** — Novel terms that sound cool but mean nothing
- **Gimmickry and branding** — Mad Max theming, animal names, invented acronyms
- **No intellectual lineage** — Vague gestures at "Kubernetes" and "Temporal"
- **No falsifiable claims** — "It works if you're Stage 7+"

**MOOLLM has actual design:**

| Foundation | Source | Training Data Presence |
|------------|--------|----------------------|
| Prototype delegation | **Self** (Ungar & Smith, 1987) | Deep — became JavaScript |
| Rooms and objects | **LambdaMOO** (Curtis, 1990) | Deep — MUD communities |
| Advertisement-based coordination | **The Sims** (Wright, 2000) | Deep — $5B+ franchise |
| K-lines and activation | **Minsky** (Society of Mind, 1986) | Deep — AI foundations |
| Directories as places | **Unix filesystem** | Ubiquitous |
| YAML with comments | **Kubernetes, CI/CD** | Massive |

**Every MOOLLM pattern is PROVEN and DEEPLY REPRESENTED in training data.**

Gas Town's patterns are invented, untested, and hostile to LLM comprehension.

### What Actually Aligns (Minimally)

1. **Work should persist in git** — But this is obvious, not novel
2. **Tasks can have dependencies** — Standard graph structure
3. **Agents need assignments** — Trivial observation

That's it. Everything else is divergence.

---

## Part III: The In-Between Zone

### Patterns That Could Go Either Way

| Pattern | Gas Town Approach | MOOLLM Approach | Hybrid Potential |
|---------|-------------------|-----------------|------------------|
| **Multi-agent simulation** | External processes | Single-call internal | Federated contexts |
| **Workflow templates** | TOML formulas, molecules | Skills with methods | Either works |
| **Progress tracking** | Bead status + labels | Task status + reasoning | YAML Jazz wins |
| **Role specialization** | 7+ distinct agent types | Characters with methods | Flexible roles |
| **Merge coordination** | Refinery agent | N/A (not needed) | Use when parallelizing |

### The Rule of Five

Gas Town adopted Jeffrey Emanuel's discovery: forcing agents to review work 4-5 times leads to convergence and superior outcomes.

**MOOLLM equivalent:** The **[adversarial-committee skill](../skills/adversarial-committee/)** and **[debate skill](../skills/debate/)** — multiple perspectives in single call.

**Synthesis:** Self-review is valuable. Whether it's 5 external agents or 5 simulated perspectives, the pattern works.

---

## Part IV: The Hybrid Architecture

### Core Insight: Factoring by Locality

The key question: **What benefits from being in the same context?**

| Same Context Benefits | Different Context Benefits |
|-----------------------|---------------------------|
| Zero-latency communication | Parallel execution |
| Shared state without serialization | Isolation (no interference) |
| Coherent narrative | Fresh perspectives |
| Multi-perspective simulation | Resource scaling |
| No tokenization decay | Error containment |

### The Factory Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                         MOOLLM FEDERATION                           │
│                                                                     │
│  ┌───────────────────┐      ┌───────────────────┐                  │
│  │   Context A       │      │   Context B       │                  │
│  │   (Speed of Light)│      │   (Speed of Light)│                  │
│  │                   │      │                   │                  │
│  │  ┌─────┐ ┌─────┐ │      │  ┌─────┐ ┌─────┐ │                  │
│  │  │Agent│ │Agent│ │      │  │Agent│ │Agent│ │                  │
│  │  │  1  │ │  2  │ │      │  │  3  │ │  4  │ │                  │
│  │  └──┬──┘ └──┬──┘ │      │  └──┬──┘ └──┬──┘ │                  │
│  │     │       │     │      │     │       │     │                  │
│  │     └───┬───┘     │      │     └───┬───┘     │                  │
│  │         │         │      │         │         │                  │
│  │    [Instant]      │      │    [Instant]      │                  │
│  │                   │      │                   │                  │
│  └─────────┬─────────┘      └─────────┬─────────┘                  │
│            │                          │                             │
│            │    ┌──────────────┐      │                             │
│            └────┤ Carrier      ├──────┘                             │
│                 │ Pigeon       │                                    │
│                 │ (Git/Mail)   │                                    │
│                 └──────────────┘                                    │
│                                                                     │
│            Within context: SPEED OF LIGHT (instant)                │
│            Between contexts: CARRIER PIGEON (async, persisted)     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Factoring Principles

#### Principle 1: Maximize Locality

**Group into same context:**
- Agents that need to converse rapidly
- Characters in the same "scene"
- Tasks with tight dependencies
- Multi-perspective debate on same question

**Separate into different contexts:**
- Independent work streams
- Different codebases
- Parallel batch tasks
- Conflict-prone changes

#### Principle 2: Minimize Crosstalk

**Crosstalk costs:**
- Serialization/deserialization overhead
- Context window consumption for messages
- Latency waiting for responses
- State synchronization complexity

**Reduce crosstalk by:**
- Factor work into independent chunks
- Use async messaging (fire-and-forget when possible)
- Batch messages (don't send one at a time)
- Design for eventual consistency

#### Principle 3: Serialize at Boundaries Only

```yaml
# GOOD: Speed of light within, serialize at edges
context_a:
  internal_state: [agent_1, agent_2, shared_memory]  # Fast
  output_to_b: "Summary message"                      # Serialized once

# BAD: Constant serialization
agent_1 → serialize → agent_2 → serialize → agent_3  # Slow
```

### Implementation: MOOLLM Cells

A **cell** is a MOOLLM context that:
- Runs speed-of-light internally
- Communicates externally via git-backed messages
- Has clear input/output boundaries

```yaml
# Cell definition
cell:
  id: design-review-cell
  
  # What's inside (speed of light)
  internal:
    agents: [architect, critic, implementer]
    shared_state: true
    simulation_style: adversarial-committee
    
  # How it connects (carrier pigeon)
  external:
    inbox: cells/design-review/inbox/
    outbox: cells/design-review/outbox/
    sync_mode: async  # or sync for blocking
    
  # Boundaries
  input_schema:
    - design_doc: markdown
    - constraints: list
  output_schema:
    - verdict: approve | reject | revise
    - feedback: markdown
    - action_items: list
```

### Message Protocol

Between cells, use simple git-backed messages:

```yaml
# cells/design-review/inbox/msg-001.yml
message:
  id: msg-001
  from: implementation-cell
  to: design-review-cell
  timestamp: 2026-01-26T15:30:00Z
  type: review-request
  
  payload:
    design_doc: |
      ## Feature X Design
      ...
    constraints:
      - Must be backward compatible
      - Performance target: <100ms
      
  # Reasoning travels with message
  context: |
    Implementation cell completed initial design.
    Requesting adversarial review before coding.
```

Response:

```yaml
# cells/implementation/inbox/msg-002.yml  
message:
  id: msg-002
  from: design-review-cell
  to: implementation-cell
  timestamp: 2026-01-26T15:45:00Z
  type: review-response
  in_reply_to: msg-001
  
  payload:
    verdict: revise
    feedback: |
      The caching strategy has a race condition.
      See attached analysis.
    action_items:
      - Add mutex around cache updates
      - Consider read-write lock for performance
```

---

## Part V: When to Use What

### Decision Matrix

| Scenario | Architecture | Why |
|----------|--------------|-----|
| **Single complex task** | One cell, speed of light | Coherence, instant communication |
| **Multi-perspective analysis** | One cell, multiple simulated agents | Same context enables rapid debate |
| **Parallel batch work** | Multiple cells, carrier pigeon | Independence, scaling |
| **Long-running project** | Cells with persistent state | Context limits require boundaries |
| **Code review** | One cell (reviewer + author) | Conversation needs shared context |
| **Large refactor** | Multiple cells by subsystem | Isolation reduces conflicts |
| **Interactive session** | Single cell | User needs coherent conversation |
| **Overnight batch** | Multiple cells + orchestrator | Parallelism, fault isolation |

### The Leela Factory Model

For Leela's manufacturing intelligence use case:

```
┌─────────────────────────────────────────────────────────────────┐
│                    LEELA MANUFACTURING MOOLLM                    │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  Vision Cell    │  │  Rules Cell     │  │  Query Cell     │ │
│  │                 │  │                 │  │                 │ │
│  │  [Camera 1]     │  │  [Safety Rules] │  │  [User Chat]    │ │
│  │  [Camera 2]     │  │  [Process Rules]│  │  [Explain]      │ │
│  │  [Detector]     │  │  [Alert Logic]  │  │  [Visualize]    │ │
│  │                 │  │                 │  │                 │ │
│  │  Speed of Light │  │  Speed of Light │  │  Speed of Light │ │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘ │
│           │                    │                    │           │
│           └────────────┬───────┴───────────────────┘           │
│                        │                                        │
│               ┌────────┴────────┐                               │
│               │   Event Bus     │                               │
│               │  (Carrier       │                               │
│               │   Pigeon)       │                               │
│               └─────────────────┘                               │
│                                                                 │
│  Cells communicate events: "Person detected in zone A"          │
│  Rules cell fires: "Alert: PPE violation"                       │
│  Query cell explains: "Worker without hardhat at timestamp T"   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Part VI: Reducing Crosstalk

### The Problem

When cells communicate too frequently:
- Messages pile up
- Serialization overhead dominates
- Latency increases
- Debugging becomes hard

### Factoring Strategies

#### Strategy 1: Batch Similar Work

```yaml
# BAD: One message per item
for item in items:
  send_message(item)  # N messages, N serializations

# GOOD: Batch into single message
batch = collect(items)
send_message(batch)   # 1 message, 1 serialization
```

#### Strategy 2: Fire and Forget

```yaml
# BAD: Request-response for everything
send(request)
wait(response)  # Blocking!

# GOOD: Fire and forget when possible
send(notification)  # Non-blocking
# Response comes later via inbox
```

#### Strategy 3: Eventual Consistency

```yaml
# BAD: Strong consistency between cells
lock(shared_resource)
update(shared_resource)
unlock(shared_resource)  # Coordination overhead

# GOOD: Eventual consistency
update(local_state)
broadcast(change_event)  # Others update when they can
```

#### Strategy 4: Smart Boundaries

Factor work so cells have **minimal interface surface**:

```yaml
# BAD: Cells constantly sharing fine-grained state
cell_a.variable_1 ↔ cell_b.variable_1
cell_a.variable_2 ↔ cell_b.variable_2
cell_a.variable_3 ↔ cell_b.variable_3  # Crosstalk!

# GOOD: Cells share coarse-grained summaries
cell_a.summary → cell_b.inbox  # One message
```

---

## Part VII: The GUPP Adaptation

Gas Town's GUPP: "If work is on your hook, YOU MUST RUN IT."

### MOOLLM Cell GUPP

```yaml
# Cell activation principle
cell_gupp:
  trigger: "Message in inbox"
  action: "Process immediately"
  
  rules:
    - "If inbox has messages, process them"
    - "If processing spawns work, do it (speed of light)"
    - "If work needs external input, send request to outbox"
    - "If done, write result to outbox"
    - "If stuck, escalate via outbox"
```

### Orchestrator Role

A lightweight orchestrator (could be a simple script or a Mayor-like agent):

```yaml
orchestrator:
  responsibilities:
    - Route messages between cells
    - Spawn new cells when needed
    - Monitor for stuck cells
    - Aggregate results
    
  does_not:
    - Examine cell internals
    - Make decisions about cell work
    - Manage cell internal state
    
  pattern: |
    while work_pending:
      for cell in cells:
        if cell.inbox.has_messages():
          cell.activate()  # GUPP
        if cell.outbox.has_messages():
          route(cell.outbox.messages)
```

---

## Part VIII: Comparison Summary

### Opposition Spectrum

```
           EXTERNAL                              INTERNAL
           (Gas Town)                            (MOOLLM)
               │                                     │
               ▼                                     ▼
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  Carrier Pigeons ◀─────────── HYBRID ──────────────▶ Speed of   │
│  (processes,                    │                     Light      │
│   mail,                         │                    (single     │
│   tmux)                         │                     context)   │
│                                 │                                │
│  High latency              Cells with                Zero        │
│  High parallelism          boundaries               latency      │
│  High cost                 Best of both             Low cost     │
│  Fault isolation           Factored locality        Coherence    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### When Each Approach Wins

| Context | Approach | Why |
|---------|----------|-----|
| **Complex conversation** | Speed of Light | Coherence, instant response |
| **Multi-agent debate** | Speed of Light | Same context, rapid exchange |
| **Parallel batch jobs** | Parallel Cells + Messages | Independence, BUT efficiency still matters |
| **Large codebase refactor** | Parallel Cells | Isolation, conflict avoidance |
| **Interactive session** | Speed of Light | User experience |
| **Long-running automation** | Parallel Cells | Fault tolerance |
| **Design review** | Speed of Light | Tight collaboration |
| **Overnight work** | Parallel Cells | Parallelism |

### Why Gas Town's Approach Fails Even For "Carrier Pigeon" Use Cases

**The fallacy:** "Abundant tokens" doesn't exist. Parallel work means costs multiply:

| Agents | Naive Cost | With Coordination | With Retries |
|--------|------------|-------------------|--------------|
| 1 | 1× | 1× | ~1.2× |
| 5 | 5× | ~7× | ~10× |
| 20 | 20× | ~40× | ~80× |
| 30 | 30× | ~70× | ~140× |

Gas Town's architecture **maximizes waste**:
- Shell-outs to Python CLI (overhead per operation)
- tmux session management (fragile, slow)
- Text injection for commands (parsing overhead)
- JSONL files parsed by hand (no caching)
- Redundant context loading per agent

**Efficient parallelism requires efficient cells**, not "throw more agents at it."

### The Synthesis

**MOOLLM Cells with Async Messaging:**

1. **Inside a cell:** Speed of light. Multiple simulated agents, instant communication, shared context. **This is where MOOLLM excels.**

2. **Between cells:** Async git-backed messages. But keep cells efficient! Don't shell out to CLI tools. Don't parse text by hand. Don't inject commands via tmux.

3. **Factoring principle:** Maximize locality within cells, minimize crosstalk between cells. **Factor for efficiency, not just parallelism.**

4. **Activation principle:** If inbox has work, process it. Don't wait. (This is the one good idea from GUPP.)

5. **Orchestrator:** Lightweight router, not a smart coordinator. Cells are autonomous. **No daemon hierarchy, no watchdog chains, no patrols.**

---

## Conclusion

Gas Town and MOOLLM aren't opposites to choose between — they're **endpoints of a spectrum** to position on based on the work.

| Principle | Application |
|-----------|-------------|
| **Speed of Light** | Use within a coherent task, conversation, or simulation |
| **Carrier Pigeon** | Use between independent work streams or parallel batches |
| **Factor for Locality** | Group tightly-coupled work in same cell |
| **Minimize Crosstalk** | Coarse-grained messages, eventual consistency |
| **GUPP for Cells** | Cells activate on inbox messages, process autonomously |

The future isn't "Gas Town vs MOOLLM" — it's **MOOLLM cells running at speed of light, connected by carrier pigeons when necessary**.

---

## Part IX: What NOT To Learn From Gas Town

### The Anti-Patterns

| Gas Town Pattern | Why It's Bad | MOOLLM Alternative |
|------------------|--------------|-------------------|
| **Shell-out to CLI** | 3 language hops to read a file | Direct file access |
| **tmux orchestration** | Fragile, unobservable, slow | LLM-native coordination |
| **Text injection commands** | Parsing overhead, errors | Structured state files |
| **JSONL storage** | No comments, no reasoning | YAML Jazz |
| **Novel jargon** | Hostile to LLM comprehension | Standard vocabulary |
| **Daemon hierarchies** | Complexity for complexity's sake | Simple activation rules |
| **"Stage N developer"** | Unfalsifiable escape hatch | Documented, testable patterns |

### The Code Smell Checklist

If your orchestration system has any of these, reconsider:

- [ ] Wraps CLI tools instead of direct access
- [ ] Parses text output from subprocesses
- [ ] Has deprecated packages still in the tree
- [ ] Requires tmux (or similar) for operation
- [ ] Uses invented acronyms (GUPP, MEOW, NDI)
- [ ] Claims to need "advanced developers" to use
- [ ] Has 11+ custom types for issue tracking
- [ ] Stores structured data in description fields

Gas Town checks all of these.

### The One Good Idea

**Persistent assignment**: Work should survive session death.

MOOLLM already has this via three-tier persistence. Gas Town's "hook" concept is just... a file that tracks what you're working on. We don't need a Mad Max metaphor for that.

---

## Conclusion

Gas Town and MOOLLM are NOT equal alternatives on a spectrum. They're:

- **MOOLLM**: Principled design, efficient implementation, standard vocabulary
- **Gas Town**: Interesting philosophy, vibe-coded implementation, hostile nomenclature

The hybrid architecture — MOOLLM cells with async messaging — takes the ONE useful pattern from Gas Town (persistent work tracking) and implements it properly.

Don't adopt Gas Town's architecture. Don't adopt its vocabulary. Don't adopt its shell-out patterns. Take the core insight (work persists in git) and implement it simply.

---

## References

- [GASTOWN-VS-MOOLLM-ANALYSIS.md](GASTOWN-VS-MOOLLM-ANALYSIS.md) — Original comparison
- [MOOLLM-TASK-TRACKING-DESIGN.md](MOOLLM-TASK-TRACKING-DESIGN.md) — Task vocabulary and harsh assessment
- [kernel/constitution-core.md](../kernel/constitution-core.md) — Speed of light principle
- [skills/adversarial-committee/](../skills/adversarial-committee/) — Multi-perspective in single call
- Ken Kahn, [ToonTalk](https://toontalk.com) (1995) — Carrier pigeon pedagogy (the original, pedagogically valuable version)
