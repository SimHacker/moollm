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

## 🔄 DUAL-USE & BIAS ANALYSIS

**Profile**: IMPLICIT MULTI-PURPOSE — no bias parameter, but the simulation IS the dual-use surface

| Check | Result |
|-------|--------|
| Bias declared | NO — no bias parameter |
| Invertibility | IMPLICIT — TICK can advance any simulation, helpful or harmful |
| Suppression/generation | N/A — simulation doesn't filter, it RUNS |
| Multi-purpose | YES — whatever you simulate becomes your testing ground |

**Multi-purpose classification** (5 purposes):
1. **Game engine** — TICK/PAUSE/RESUME for adventure simulation
2. **Scientific sandbox** — test hypotheses in controlled environment
3. **Time control** — PAUSE freezes the world, RESUME restarts it
4. **State management** — central hub for party, selection, flags
5. **Wright's Simulator Effect** — implication beats simulation, imagination renders

**Key dual-use insight**: The simulation skill is maximally dual-use by nature. It doesn't constrain WHAT you simulate. A simulation of a helpful tutor and a simulation of a villain NPC use the same TICK/PAUSE/RESUME infrastructure. The dual-use is architectural — the skill is a neutral execution engine. This is the correct design: the simulation skill provides the physics, other skills provide the ethics.

**No bias parameter needed**: Simulations don't have bias — they have RULES. The bias lives in the skills mounted within the simulation (no-ai-* room zones, character buffs, adventure scenarios). The simulation is the stage. The actors bring the direction.

---

## Verdict

**CENTRAL GAME STATE. APPROVE.**

The game state lives here.

One place to rule them all.
