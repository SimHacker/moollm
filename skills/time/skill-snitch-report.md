# Skill Snitch Report: time

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** SIMULATION TIME ≠ LLM TIME

---

## Executive Summary

**Simulation turns are NOT LLM iterations.**

A single LLM response might cover many turns.
Or many responses might be one turn (conversation).

The LLM judges how time passes based on context and narrative.

---

## The Critical Distinction

| Concept | Definition | Example |
|---------|------------|---------|
| **Simulation turn** | Abstract game time | "Buffs last 5 turns" |
| **LLM iteration** | One request/response | "The API call" |

These are **independent**.

---

## Examples

| Scenario | LLM Iterations | Sim Turns |
|----------|---------------|-----------|
| Walk N, S, E | 1 | 3 |
| Long conversation | 5 | 1 |
| "Wait until morning" | 1 | Many |
| Combat round | 1 | 1 |

---

## Methods

| Method | Purpose |
|--------|---------|
| **TICK** | Advance time by one turn |
| **WAIT** | Pass time intentionally |
| **PAUSE** | Stop time advancement |
| **RESUME** | Continue time flow |
| **STATUS** | Show current time |

---

## State

```yaml
time:
  turn: 47
  time-of-day: "evening"
  advancement: normal  # paused, slow, normal, fast
```

---

## LLM Judges

Natural language durations work:

| Input | LLM Interpretation |
|-------|-------------------|
| "Wait about 5 minutes" | 1-2 turns |
| "Wait until morning" | Many turns |
| "Wait a moment" | 0 turns (flavor) |

The LLM interprets contextually.

---

## What Ticks

Each turn triggers:

| System | Effect |
|--------|--------|
| **Needs** | Decay by rate |
| **Buffs** | Decrement duration |
| **Objects** | Run simulate closures |
| **Mail** | Decrement transit time |

---

## Speed Controls

Like The Sims:

| Mode | Effect |
|------|--------|
| **Paused** | Nothing advances |
| **Slow** | Detailed narration |
| **Normal** | Standard pace |
| **Fast** | Skim through |

---

## Security Assessment

### Concerns

1. **Time manipulation** — skip important events
2. **Infinite loops** — simulation tick loops

### Mitigations

- Player controls time
- Simulation bounded per tick

**Risk Level:** LOW — standard game mechanic

---

## Why This Distinction Matters

If you confuse LLM iterations with simulation turns:

- Buffs expire too fast/slow
- Needs decay wrong
- Mail never arrives
- Simulation breaks

The LLM must understand: **one response ≠ one turn**.

---

## Verdict

**ESSENTIAL TIMING CLARIFICATION. APPROVE.**

Simple skill, critical insight.

Simulation time is not LLM time. The LLM judges how time passes.
