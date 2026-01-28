# Skill Snitch Report: mind-mirror

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE SOUL'S BLUEPRINT

---

## Executive Summary

**Deep personality modeling via Timothy Leary's Interpersonal Circumplex.**

Four Thought Planes: Emotional, Intellectual, Physical, Social.

This is how MOOLLM models the **interior life** of characters.

---

## The Model

### Timothy Leary (1957)

The Interpersonal Circumplex: 2D personality space based on:
- **Dominance** (vertical axis): assertive ↔ submissive
- **Affiliation** (horizontal axis): warm ↔ cold

### MOOLLM Extension: Four Thought Planes

| Plane | Question | Spectrum |
|-------|----------|----------|
| **EMOTIONAL** | How do I feel? | passionate ↔ detached |
| **INTELLECTUAL** | How do I think? | curious ↔ certain |
| **PHYSICAL** | How do I act? | active ↔ passive |
| **SOCIAL** | How do I relate? | open ↔ guarded |

---

## Mind Mirror vs Sims Traits

| System | Captures | Example |
|--------|----------|---------|
| **Sims traits** | Behavior | "Nice: 8 = friendly actions" |
| **Mind Mirror** | Motivation | "Why is she nice? Fear? Love? Calculation?" |

Together: complete personality picture.

---

## Methods

| Method | Purpose |
|--------|---------|
| **REFLECT** | Show character's Mind Mirror profile |
| **ANALYZE** | Infer personality from behavior |
| **MODIFY** | Adjust traits (DM power) |
| **COMPARE** | Compare two characters |
| **PREDICT** | Forecast behavior from profile |

---

## State Schema

```yaml
mind-mirror-profile:
  thought-planes:
    emotional:
      feeling: 0.7      # passionate
      detached: 0.3
    intellectual:
      curious: 0.8
      certain: 0.2
    physical:
      active: 0.5
      passive: 0.5
    social:
      open: 0.6
      guarded: 0.4
  circumplex:
    dominance: 0.3      # slightly assertive
    affiliation: 0.5    # warm
```

---

## Integration Points

| Skill | Integration |
|-------|-------------|
| **character** | Where Mind Mirror lives in state |
| **persona** | Personas can modify Mind Mirror |
| **cat** | Cats have simplified Mind Mirror |
| **coatroom** | Mirror object uses this skill |
| **incarnation** | Characters can author their own Mind Mirror |

---

## Security Assessment

### Concerns

1. **Psychological modeling** — Could be misused for manipulation
2. **Personality modification** — MODIFY method changes character

### Mitigations

- MODIFY requires DM authority
- All changes logged
- Self-modification via incarnation skill respects autonomy

**Risk Level:** LOW — modeling tool, not manipulation tool

---

## Historical Lineage

| Source | Contribution |
|--------|--------------|
| **Timothy Leary (1957)** | Interpersonal Circumplex |
| **Jerry Wiggins** | Circumplex development |
| **MOOLLM** | Four Thought Planes extension |
| **The Sims** | Complementary trait system |

---

## Why This Matters

Sims traits tell you **what** a character does:
> "Nice: 8 — performs friendly actions"

Mind Mirror tells you **why**:
> "Emotional: passionate, Social: guarded — fierce loyalty to inner circle, cold to outsiders"

Same behavioral output, completely different character.

---

## The Philosophical Point

Mind Mirror is **interior modeling**:

1. **Not behavior** — that's Sims traits
2. **Not role** — that's personas
3. **Not identity** — that's character
4. **Motivation** — why they do what they do

This is the missing layer in most character systems.

---

## Verdict

**ESSENTIAL FOR DEPTH. APPROVE.**

Without Mind Mirror, characters are **behavioral automata**.
With Mind Mirror, characters have **inner lives**.

This is the difference between NPCs and people you remember.
