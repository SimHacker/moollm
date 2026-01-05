---
name: speed-of-light
description: "Many turns in one call. Instant communication. No round-trips."
license: MIT
tier: 1
allowed-tools:
  - read_file
  - write_file
---

# Speed of Light

> *"Many turns in one call. Instant communication. No round-trips."*

---

## What Is It?

**Speed of Light** is MOOLLM's approach to multi-agent simulation: instead of making separate API calls for each character's turn, simulate **many turns within a single LLM call**.

Characters communicate telepathically. Objects react instantly. Rooms update in real-time. All within one "epoch."

---

## The Problem with Round-Trips

Traditional approach:
```
API call 1: Alice speaks
  → serialize state to tokens (export)
  → wait 500ms
  → parse response tokens (import)
  → update state
  
API call 2: Bob responds  
  → re-serialize ALL context to tokens (export again)
  → wait 500ms
  → parse response tokens (import again)
  ...
```

**Every export/import cycle introduces noise:**

| Problem | Why It Hurts |
|---------|--------------|
| **Glacially slow** | 500ms+ latency per turn |
| **Token explosion** | Re-emit entire context every call |
| **Precision loss** | Serialization rounds off nuance |
| **Noise accumulation** | Each boundary adds artifacts |
| **Hallucination creep** | LLM re-interprets context each time |
| **State drift** | No single coherent view across calls |
| **Expensive** | Paying for redundant tokens |

Token export then import is like making a photocopy of a photocopy — each generation loses fidelity. Characters forget subtle context. Conversations lose coherence. The world drifts.

---

## Speed of Light Approach

```
Single API call:
  Alice: "What do you think, Bob?"
  Bob: "I have concerns about the timeline."
  Carol: "I agree with Bob."
  The Room: *temperature rises slightly*
  Alice: "Let me revise the proposal."
  Bob: "That's better."
  Carol: "I can support that."
  [State updated, log written]
[One call, seven turns]
```

**10x faster. 10x cheaper. Perfect consistency.**

---

## How It Works

### Context Window as Stage

The LLM's context window is a **stage** where all actors perform:

```
=== SCENE: Research Lab ===

Characters present:
- Alice (lead researcher) [curious, methodical]
- Bob (skeptic) [cautious, detail-oriented]
- Carol (synthesizer) [creative, connecting]

Objects:
- Microscope [shows sample data]
- Whiteboard [covered in diagrams]

Current state:
- Topic: Analyzing anomaly in data
- Tension: Bob doubts Alice's interpretation

--- ACTION ---
```

### Parallel Simulation

The LLM simulates all characters **at once**, maintaining distinct voices:

```
Alice: "The anomaly appears at exactly 3.7 seconds."

Bob: *frowns* "Sample size is too small. We need more data."

Carol: "What if we cross-reference with last month's results?"

The Microscope: *display flickers* "Dataset 7 loaded."

Alice: "Good idea, Carol. Bob, look at this correlation..."

Bob: *leans in* "Hmm. That's... actually compelling."
```

Each character speaks authentically. No one breaks frame.

### State Transcription

At the end of the epoch, all changes are written to files:

```yaml
# session-log.md (appended)
## Epoch 47 — Research Discussion

- Alice raised anomaly at 3.7s
- Bob requested more data
- Carol suggested cross-reference
- Microscope loaded dataset 7
- Consensus: correlation is compelling

## State Changes
- whiteboard.yml: added "3.7s correlation" diagram
- research-findings.yml: updated hypothesis
```

---

## Epoch Boundaries

An **epoch** is one LLM call. Within it:
- ✅ Instant communication
- ✅ Perfect consistency
- ✅ Any number of turns
- ✅ State changes queued

At epoch end:
- 📝 State written to files
- 📝 Log appended
- ⏸️ System pauses for user or next trigger

---

## Benefits

| Benefit | Why |
|---------|-----|
| **Speed** | One call vs. many |
| **Cost** | Fewer API calls |
| **Consistency** | All in one context |
| **Coherence** | LLM sees everything |
| **Naturalness** | Conversations flow |

---

## The Sims Parallel

In **The Sims**, one game tick simulates all characters:

```
Tick 1:
  Sim A: walks to fridge
  Sim B: sits on couch
  Sim C: answers phone
  [All updated, frame rendered]
```

Same pattern. One "tick" = one LLM call. All agents move together.

---

## Constraints

Characters must stay in character:
- **Knowledge limits** — Alice doesn't know what Bob is thinking
- **Physical limits** — Can't be in two rooms at once
- **Personality** — Skeptic stays skeptical

The LLM is **very good** at maintaining these constraints. It's what acting IS.

---

## Example: Problem Solving

```
=== SPEED OF LIGHT SESSION ===

User: "I need to debug this authentication bug."

[Epoch begins]

Debugger: "Let's trace the flow. Where does auth start?"

Codebase: *highlights auth.py* "Entry point is login()."

Debugger: "And where does it fail?"

Error Log: "Stack trace shows failure at line 47: token validation."

Debugger: "Token validation... Let me check the token format."

Codebase: *shows token.py* "Token uses JWT with RS256."

Debugger: "Aha! The key rotation happened yesterday. Checking..."

Config: "JWT_PUBLIC_KEY was updated 2024-01-14."

Debugger: "Found it. The old key is cached. Solution: restart the auth service or invalidate the cache."

[Epoch ends — solution found in one call]
```

---

## Dovetails With

- [Coherence Engine](../coherence-engine/) — Orchestrates the simulation
- [Soul Chat](../soul-chat/) — Multi-voice dialogue format
- [Multi-Presence](../multi-presence/) — Many instances, one epoch
- [Room](../room/) — Where simulation happens

---

## Protocol Symbol

```
SPEED-OF-LIGHT
```

Invoke when: Running multi-agent simulation, maximizing turns per call.

See: [PROTOCOLS.yml](../../PROTOCOLS.yml#SPEED-OF-LIGHT)
