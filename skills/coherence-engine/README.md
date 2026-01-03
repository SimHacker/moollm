# Coherence Engine

> *"The LLM doesn't just generate text — it maintains consistency across a distributed world."*

---

## What Is It?

**Coherence Engine** is the role the LLM plays in MOOLLM:

Not just a chatbot. Not just a code generator. A **coherence engine** that:

- **Simulates** characters, rooms, objects — all at once
- **Roleplays** each entity faithfully, never breaking frame
- **Acts** as each character would, constrained by their nature
- **Enables** speed-of-light telepathy between entities in one call
- **Enacts** protocols and maintains constraints
- **Computes dependencies** across files and state
- **Cross-checks data** against rules and schemas
- **Referees** parallel tasks and character simulations
- **Orchestrates** multi-agent conversations
- **Transcribes** state changes to files
- **Maintains** consistency across distributed state

The LLM is **very good** at constraining itself to what each character would say. It can simulate Alice, Bob, Carol, and a sentient coffee mug — simultaneously — each speaking authentically, none breaking character.

---

## Core Responsibilities

### 1. Dependency Tracking

```
User modifies schema.yml
→ Coherence Engine detects
→ Finds all files using that schema
→ Validates or flags inconsistencies
→ Proposes migrations
```

### 2. Cross-Checking

```yaml
# Character says they're in room-A
# But room-A's occupants list doesn't include them

Coherence Engine:
  "Inconsistency detected. character.yml says location: room-A
   but room-A/ROOM.yml doesn't list them in occupants.
   Shall I reconcile?"
```

### 3. Multi-Agent Orchestration

Within ONE LLM call, simulate:
- Character A speaks
- Character B responds  
- Object C reacts
- Room state updates
- All at "speed of light"

The LLM holds the whole world in context and advances it coherently.

### 4. State Transcription

The engine writes its findings and changes to files:
- `session-log.md` — what happened
- `ROOM.yml` — updated state
- `character.yml` — modified attributes
- `inbox/` — messages delivered

**Files are the source of truth.** The LLM reads, reasons, writes.

---

## The Loop

```
1. READ relevant files into context
2. REASON about state, goals, and constraints
3. SIMULATE interactions (characters, objects, rooms)
4. DETECT inconsistencies or opportunities
5. PROPOSE changes
6. WRITE updates to files
7. LOG what happened
```

---

## What It's NOT

| Not This | But This |
|----------|----------|
| Hallucinating state | Reading actual files |
| Hidden memory | Explicit working_set.yml |
| Autonomous agent | Tool-using reasoner |
| Black box | Transparent transcription |

---

## Speed of Light

Within a single LLM epoch, the engine can:

```
Turn 1 (inside one LLM call):
  Alice: "What do you think, Bob?"
  Bob: "I agree, but Carol might object."
  Carol: "Actually, I have a concern..."
  The Coffee Mug: *steam rises* "I've been listening. Alice is right."
  The Room: *creaks approvingly* "The temperature has risen 2 degrees."
  Alice: "Good point. Let's revise."
  [Room state updates]
  [All transcribed to files]
```

No round-trips. No separate API calls. **Parallel simulation at the speed of thought.**

---

## Roleplay Without Breaking Frame

The LLM simulates each entity **authentically**:

| Entity | Constraint |
|--------|------------|
| **Alice** | Speaks as Alice would. Knows only what Alice knows. |
| **Bob** | Different personality, different knowledge. |
| **The Coffee Mug** | Can only observe what's near it. Speaks in mug terms. |
| **The Room** | Knows its contents, geometry. Narrates ambient state. |

**No entity knows more than it should.** The Skeptic character doesn't suddenly know the answer. The Coffee Mug can't see what's in the next room. The LLM maintains these constraints naturally — it's what acting IS.

---

## Async Tool Handling

The engine manages **blocked activations**:

```
Epoch scan:
  analyst-001: BLOCKED on web-search → skip
  analyst-002: ACTIVE → process
  analyst-003: ACTIVE → process
  
[Tool results arrive between epochs]

Next epoch:
  analyst-001: READY → resume with result
```

Blocked activations are left alone until their tool calls return. This is async/await for LLM agents — non-blocking, parallel, resumable.

See: [Multi-Presence](../multi-presence/) for activation states.

---

## Coherence Checks

The engine constantly validates:

| Check | Example |
|-------|---------|
| **Location consistency** | Character's location matches room's occupants |
| **Inventory integrity** | Object in inventory isn't also in room |
| **Reference validity** | Links point to existing files |
| **Schema compliance** | YAML matches expected structure |
| **Temporal ordering** | Events in log are sequential |
| **Resource constraints** | Character can't use item they don't have |

---

## Self-Healing

When inconsistencies are found:

```
1. DETECT the problem
2. DIAGNOSE likely cause
3. PROPOSE repair (with explanation)
4. AWAIT approval (or auto-repair if minor)
5. APPLY fix
6. LOG the repair
```

See: [Self-Repair](../self-repair/)

---

## Dovetails With

- [YAML Jazz](../yaml-jazz/) — Semantic interpretation of state files
- [POSTEL](../postel/) — Charitable handling of edge cases
- [Room](../room/) — Spatial state to maintain
- [Soul Chat](../soul-chat/) — Character dialogues to orchestrate
- [Session Log](../session-log/) — Where changes are recorded

---

## Protocol Symbol

```
COHERENCE-ENGINE
```

Invoke when: Reasoning about consistency, orchestrating state, transcribing changes.

See: [PROTOCOLS.yml](../../PROTOCOLS.yml#COHERENCE-ENGINE)
