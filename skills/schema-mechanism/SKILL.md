---
name: schema-mechanism
description: Drescher's computational theory of causal learning
allowed-tools: []
tier: 0
protocol: SCHEMA-MECHANISM
tags: [moollm, theory, learning, causality, drescher, minsky, neuro-symbolic]
origin: "Gary Drescher — Made-Up Minds (1991)"
lineage:
  - "Gary Drescher — Schema Mechanism, Made-Up Minds (1991)"
  - "Marvin Minsky — Society of Mind, K-lines (1986)"
  - "Jean Piaget — Genetic Epistemology, schemas as cognitive structures"
  - "Henry Minsky — pyleela.brain Python implementation"
related: [constructionism, society-of-mind, leela-ai, manufacturing-intelligence, play-learn-lift, planning, yaml-jazz, knowledge-frames, schema]
---

# Schema Mechanism

> *"An agent learns by discovering reliable patterns: when I do X in context C, result R tends to follow."*

Gary Drescher's *Made-Up Minds* (1991) provides a computational theory of how minds learn causal models of the world. Drescher was a student of Marvin Minsky at MIT, and his schema mechanism extends Piaget's developmental psychology into executable algorithms.

## The Core Idea

A **schema** is a causal unit:

```
Context → Action → Result
```

The agent doesn't start with schemas. It **discovers** them through experience, noticing which actions reliably produce which results in which contexts.

```yaml
schema:
  action: push-button
  context: [door-closed]
  result: [door-open]
  reliability: 0.95
```

## Drescher schema vs interchange schema

Here **schema** means **Drescher causal units** (Context → Action → Result). That is **not** JSON Schema, OpenAPI, RELAX NG, XSD, or other **interchange** mechanisms. For the MOOLLM **schemapedia** (interchange, relational SQL/SQLite, frames, K-lines, SoM—same word, many senses), see `schema` (`skills/schema/`, `schemas/registry.yml`). For Minsky **frames** vs K-lines vs Drescher, see `knowledge-frames`.

## Schema Components

| Component | Description | MOOLLM Equivalent |
|-----------|-------------|-------------------|
| **Item** | Atomic state element (ON/OFF/UNKNOWN) | YAML field, file existence |
| **Action** | Something the agent can do | Skill verb, procedure |
| **Schema** | Context → Action → Result | Documented procedure |
| **Extended Context** | Statistical tracking of context conditions | "Prerequisites" section |
| **Extended Results** | Statistical tracking of result conditions | "Side Effects" section |
| **Synthetic Item** | Discovered hidden state | Undocumented dependency |
| **Composite Action** | Chained sequence of actions | Multi-step procedure |

---

## Extended Context: Marginal Attribution

A schema might fail unpredictably. Extended Context tracks **which conditions correlate with success**:

```yaml
# The schema "start pyvision" sometimes fails
# Extended Context discovers: it fails when postgres isn't running

schema:
  action: start-pyvision
  context: []  # Initially empty
  result: [pyvision-running]
  
extended_context:
  postgres-running:
    success_when_on: 47    # Succeeded 47 times when postgres was on
    success_when_off: 0    # Never succeeded when postgres was off
    failure_when_on: 2     # Failed 2 times even with postgres
    failure_when_off: 15   # Failed 15 times without postgres
    
# Discovery: postgres-running is a prerequisite!
# Spin off new schema with explicit context:
schema:
  action: start-pyvision
  context: [postgres-running]  # Now explicit
  result: [pyvision-running]
```

This is **marginal attribution** -- discovering which items matter by tracking correlations.

---

## Extended Results: Side Effect Discovery

Similarly, schemas track what else happens:

```yaml
schema:
  action: ingest-video
  context: [video-exists]
  result: [task-created]
  
extended_results:
  disk-space-decreased:
    on_after_success: 47
    off_after_success: 0
    # Discovery: ingesting uses disk space!
```

Side effects become explicit, documented, predictable.

---

## Synthetic Items: Hidden State

Sometimes success depends on state the agent can't directly observe. Drescher's solution: **invent a synthetic item** as a hypothesis.

```yaml
# The schema works sometimes, fails sometimes, no visible pattern
# Hypothesis: there's hidden state we can't see

synthetic_item:
  name: "gpu-memory-available"
  host_schema: start-pyvision
  # If this schema succeeds, assume the item was ON
  # If it fails, assume the item was OFF
```

The synthetic item becomes a **probe** -- its state is inferred from schema success/failure.

---

## Composite Actions: Planning

Once the agent has reliable schemas, it can chain them:

```yaml
# Goal: pyvision-running
# Current: postgres-not-running

plan:
  - schema: start-postgres
    context: []
    result: [postgres-running]
  - schema: start-pyvision
    context: [postgres-running]
    result: [pyvision-running]
```

Drescher uses **Dijkstra's algorithm** on the schema graph -- find shortest path from current state to goal state.

---

## The Learning Loop

```yaml
# Schema mechanism learning loop
learning_loop:
  - step: 1. ACT
    action: "Execute schema action"
  - step: 2. OBSERVE
    action: "Record which items changed (on-flips, off-flips)"
  - step: 3. ATTRIBUTE
    action: "Update extended context/results tables, track correlations"
  - step: 4. SPIN OFF
    action: "When patterns emerge, create child schemas with refined conditions"
```

This maps directly to PLAY-LEARN-LIFT:
- **PLAY** = ACT + OBSERVE
- **LEARN** = ATTRIBUTE
- **LIFT** = SPIN OFF

---

## Implementation: pyleela.brain

Henry Minsky (Marvin's son) implemented Drescher's schema mechanism in Python:

| Class | Purpose |
|-------|---------|
| `World` | Central coordinator, tracks all items and schemas |
| `Item` | Atomic state element with ON/OFF/UNKNOWN values |
| `Action` | Primitive or composite action |
| `Schema` | The Context → Action → Result unit |
| `ExtendedContext` | Statistical tracking for context discovery |
| `ExtendedResults` | Statistical tracking for result discovery: P(item turns on \| taken) vs \| not taken |
| `LocalConsistencyTracker` | Streakiness of a schema's success; triggers synthetic items, including negative ones for reliable schemas that go locally unreliable |
| `DijkstraPlanner`, `PlanSimulator` | Goal-directed planning through the schema graph, plans checked by simulation |

The extended-context tables also yield **overriding conditions**: items that
make an otherwise reliable schema fail. Those are Minsky's anecdotal
censors, learned statistically. A comparison with the censor simulator, and
what it borrowed from this code, is in
[`designs/CENSORS-ON-SCHEMAS.md`](../../designs/CENSORS-ON-SCHEMAS.md#4-henry-minskys-code).

---

## What an LLM adds, and what it doesn't

Richard Stallman calls these systems **Pretend Intelligence**: they generate
text without understanding what it means, and don't notice when it's wrong
([his term, and the argument](../../designs/PRETEND-INTELLIGENCE.md)). This
skill takes that as a design constraint, not an insult.

So the work is split in two, and the split is enforced in code
([`designs/CENSORS-ON-SCHEMAS.md` §7](../../designs/CENSORS-ON-SCHEMAS.md#7-two-tiers-python-for-arithmetic-the-llm-for-meaning)):

- **The deterministic tier counts.** Items, schemas, marginal attribution,
  planning, sweeps and tests are plain Python. It never calls an LLM, gives
  the same answer every time, and runs tens of thousands of simulations a
  second.
- **The language tier drafts.** Where a step needs words, the engine emits
  a `REQUEST` with the exact YAML patch that would answer it: what does this
  action do, what does this agent tell itself, what should this hidden item
  be called. A person or an LLM fills it in. Every generated line is marked
  `[PI]` and carries a `source: tier0: ...` saying who wrote it.
- **The record decides.** An LLM's draft is a hypothesis. `test` replays
  what actually happened and fails if the model doesn't reproduce it;
  `ablate` removes each part and reports the ones nothing needed; `sweep`
  shows whether a conclusion survives other weights. A draft that doesn't
  survive those is thrown away, however fluent it sounds.

What that buys, concretely:

| Step | Without words | With a drafted label |
|---|---|---|
| A hidden item Drescher's mechanism mints | named after where it was found: `latent-read-from-t5` | a name a person can check against the record: "the second letter said the X-ray was bad" |
| An action nobody described | the engine stops and asks | a candidate schema, which `test` then accepts or rejects |
| A censor's cover story | the engine stops and asks | a sentence, marked `[PI]`; for a real person, their own words with a source, or nothing |
| A thread of email | split into messages by rule | each message turned into an event, every quote verbatim |

None of this makes the program understand anything. It makes the parts
that need words explicit, labeled, and testable, and keeps the arithmetic
out of the LLM's hands, where it would be slow and wrong.

---

## Connection to MOOLLM Skills

| Drescher | MOOLLM Skill |
|----------|--------------|
| World state | YAML files in skill directory |
| Items | Fields in state files |
| Actions | Skill verbs and procedures |
| Schemas | Documented procedures with context/result |
| Extended Context | Prerequisites, dependencies |
| Extended Results | Side effects, outputs |
| Synthetic Items | Undocumented state the skill discovers |
| Composite Actions | Multi-step procedures |
| Spin-offs | Refined procedures from experience |

---

## Censors: the schema with the sign bit flipped

Minsky's Memo 603 censors, run on this mechanism: precursor censors that
veto an action before it's thought, suppressors that re-file a forbidden
state, marginal attribution that mints new censors from pain, and jokes that
expose them. Two traces, inner and observer; the gap is the cognitive
unconscious. A CLI that never calls an LLM: it fits a record, ablates each
censor, sweeps the weights, and emits requests with patches for whoever has
the context to answer. Personality modules inherit shared logic, so two
minds can agree on every schema and still differ in priorities.
[`censors/`](censors/README.md) · [`scripts/censor_sim.py`](scripts/censor_sim.py) ·
[the article](../../designs/CENSORS-ON-SCHEMAS.md)

---

## Dovetails With

- **[../constructionism/](../constructionism/)** — Papert's educational philosophy
- **[../play-learn-lift/](../play-learn-lift/)** — Schema learning as methodology
- **[../planning/](../planning/)** — Dijkstra through schema graph
- **[../debugging/](../debugging/)** — Marginal attribution for bugs
- **[../skill/](../skill/)** — Skills as schema systems

---

## Credits

- **Gary Drescher** — Made-Up Minds (1991)
- **Marvin Minsky** — Society of Mind, K-lines
- **Jean Piaget** — Developmental schemas
- **Henry Minsky** — pyleela.brain implementation

---

> *"If you can observe patterns, you can discover causality."*
> *"If you track correlations, you can spin off knowledge."*
> *"If you can't check it against the record, it's a guess, so label it."*
