# Skill Snitch Report: simulation

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE GAME STATE LIVES HERE

---

## Executive Summary

**Central hub for simulation state.**

Turns, time, party, selection, flags — all managed here.

Adventure skill inherits from this.

---

## What It Manages

| State | Purpose |
|-------|---------|
| **turn** | Current turn number |
| **paused** | Is simulation paused? |
| **time** | Time of day, advancement speed |
| **party** | References to party members |
| **selection** | Currently selected targets |
| **flags** | Game state flags |
| **git** | Auto-commit, auto-push settings |
| **output** | Log path, transcript path |

---

## Methods

| Method | Purpose |
|--------|---------|
| **TICK** | Advance one turn |
| **PAUSE** | Stop the simulation |
| **RESUME** | Continue simulation |
| **STATUS** | Show current state |
| **SELECT** | Set selection targets |
| **CONFIGURE** | Set parameters |

---

## What TICK Does

```
TICK
  ↓
Increment turn
  ↓
Tick buffs (decrement duration)
  ↓
Decay needs
  ↓
Run object simulations
  ↓
Deliver mail
```

One tick orchestrates all time-based effects.

---

## Security Assessment

### Concerns

1. **State corruption** — broken simulation
2. **Time manipulation** — skip important events
3. **Flag abuse** — cheat via flags

### Mitigations

- State visible in files
- TICK is auditable
- Flags explicit

**Risk Level:** LOW — transparent, central

---

## Verdict

**CENTRAL GAME STATE. APPROVE.**

The game state lives here.

One place to rule them all.
