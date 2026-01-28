# Skill Snitch Report: needs

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** SIMS IN YOUR YAML

---

## Executive Summary

**Sims-style dynamic motivations that decay over time and drive behavior.**

Hunger, energy, fun, social, hygiene, bladder, comfort, room.

Objects advertise based on which needs they satisfy.

---

## The Original Eight

From The Sims (2000):

| Need | Decay/Turn | What Satisfies It |
|------|------------|-------------------|
| **Hunger** | 5 | Food, cooking |
| **Energy** | 3 | Sleep, rest |
| **Fun** | 4 | Games, entertainment |
| **Social** | 2 | Conversation, groups |
| **Hygiene** | 2 | Shower, sink |
| **Bladder** | 4 | Toilet |
| **Comfort** | 1 | Good furniture |
| **Room** | 1 | Nice surroundings |

---

## Thresholds

| Level | Value | Motivation |
|-------|-------|------------|
| **Full** | 100 | None |
| **Satisfied** | 75 | Low |
| **Moderate** | 50 | Normal |
| **Low** | 25 | Strong |
| **Critical** | 10 | Desperate |

---

## Methods

| Method | Purpose |
|--------|---------|
| **CHECK** | View character's current needs |
| **SATISFY** | Fulfill a need (source: object/buff) |
| **DECAY** | Reduce needs over time |
| **URGENT** | Find most pressing need |

---

## The Advertising Loop

```
1. Needs decay over time
2. Low needs increase motivation
3. Objects advertise based on needs they satisfy
4. Autonomous agents queue highest-scoring actions
5. Actions satisfy needs
6. Loop
```

---

## False Advertisements

> "False advertisements can be used for good and evil."

The **Food Chain** pattern:

```
Fridge → advertises food
  ↓
Ingredients → advertise cooking
  ↓
Stove → advertises cooking
  ↓
Counter → advertises prep
  ↓
Table → advertises eating
```

Each step hands off to the next. The carrot in front of the donkey.

---

## Bed Relationship Learning

> "Bed advertisement score modulated by relationship with bed, which increases with use so you learn to sleep in the same place."

The more you use a bed, the higher it scores for you. Learned preference.

---

## Security Assessment

### Concerns

1. **Behavior manipulation** — needs drive autonomous action
2. **False advertisements** — can mislead agents
3. **Decay rates** — can be tuned to extremes

### Mitigations

- Needs are transparent
- Advertisements auditable
- Player always has override

**Risk Level:** LOW — The Sims has run for 25 years

---

## Why This Matters

Needs create **emergent behavior** without scripting:

1. Don't script "go eat"
2. Let hunger decay
3. Let fridge advertise
4. Agent figures it out

The Sims insight: **motivation drives behavior**.

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **The Sims** | Original 8 needs (2000) |
| **Will Wright** | Needs-driven autonomous behavior |

---

## Verdict

**25 YEARS OF PROVEN DESIGN. APPROVE.**

Will Wright solved autonomous agent behavior in 2000. This is that system.

Needs decay. Objects advertise. Agents act. Emergent behavior.
