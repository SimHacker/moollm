# ⚡ Speed of Light

> Many turns in one call. Instant communication. No round-trips.

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

## Related Skills

- [multi-presence](../multi-presence/) — parallel activations
- [coherence-engine](../coherence-engine/) — orchestrates epochs
- [soul-chat](../soul-chat/) — multi-character dialogue
