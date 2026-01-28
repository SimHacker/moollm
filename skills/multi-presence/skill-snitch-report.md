# Skill Snitch Report: multi-presence

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** BE IN TWO PLACES AT ONCE. THREE EVEN.

---

## Executive Summary

**Same card instantiated in multiple rooms simultaneously.**

Each instance has its own state but shares identity.

Quantum superposition for adventure games.

---

## Methods

| Method | Purpose |
|--------|---------|
| **SPLIT** | Create presence in another room |
| **SYNC** | Synchronize state between presences |
| **MERGE** | Combine presences back into one |
| **STATUS** | Show all active presences |

---

## State Per Presence

```yaml
presence:
  source-card: characters/don/
  location: pub/bar/
  local-state:
    has_drink: true
    talking_to: palm
  siblings:
    - pub/games/
    - maze/room-3/
```

Each instance diverges. SYNC brings them together. MERGE collapses to one.

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Parallel exploration** | Scout multiple dungeon branches |
| **Distributed work** | Work on multiple files |
| **Consensus building** | Participate in debates in multiple rooms |
| **Hedge bets** | Try different approaches |

---

## The Merge Problem

When presences diverge, MERGE must decide:

- Which state wins?
- How to combine memories?
- What happens to contradictions?

The `primary` parameter determines which presence becomes the merged result.

---

## Security Assessment

### Concerns

1. **State divergence** — inconsistent world
2. **Resource multiplication** — duplicate items
3. **Identity confusion** — which is real?

### Mitigations

- Siblings tracked explicitly
- SYNC resolves divergence
- Primary presence defined

**Risk Level:** MEDIUM — powerful, but needs careful tracking

---

## Verdict

**QUANTUM ADVENTURE MECHANICS. APPROVE.**

Be in two places at once.

But remember to MERGE eventually.
