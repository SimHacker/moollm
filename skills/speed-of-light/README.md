# ⚡ Speed of Light

> Many turns in one call. Instant communication. No round-trips.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [moollm/](../moollm/) | Core MOOLLM principle |
| [bootstrap/](../bootstrap/) | Speed-of-light activated on boot |
| [simulation/](../simulation/) | Many turns in simulation |
| [multi-presence/](../multi-presence/) | Parallel activations in one call |
| [coherence-engine/](../coherence-engine/) | Orchestrates epochs |
| [soul-chat/](../soul-chat/) | Multi-character dialogue |
| [adversarial-committee/](../adversarial-committee/) | Many voices, one call |
| [debate/](../debate/) | Structured deliberation in one call |
| [examples/adventure-4/pub/](../../examples/adventure-4/pub/) | 33-turn Fluxx game in one epoch |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

MOOLLM's approach to multi-agent simulation: instead of making separate API calls for each character's turn, simulate **many turns within a single LLM call**.

Characters communicate telepathically. Objects react instantly. Rooms update in real-time. All within one "epoch."

## The Problem with Round-Trips

Traditional multi-agent:
- 500ms+ latency per turn
- Token explosion (re-emit entire context)
- Noise accumulation at each boundary
- Hallucination creep

## Speed of Light Solution

```
[Single LLM call = 1 "epoch"]
  Character A: speaks
  Character B: responds
  Object: reacts
  Room: updates
  All: written to files
[End call — all changes persisted]
```

