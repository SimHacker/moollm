# Skill Snitch Report: buff

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** CURSES ARE JUST SHITTY BUFFS

---

## Executive Summary

**Temporary effects system.** Numeric modifiers (+2 energy), semantic vibes ("feeling lucky"), or behavior changes.

Key insight: **Curses are just negative buffs. No separate system needed.**

---

## The Unified Model

```yaml
buff:
  name: "Slightly Cursed"
  polarity: negative      # <-- This is what makes it a curse
  effect: "bad luck"
  duration: 10
```

One system. One signature. Positive, negative, neutral — all buffs.

---

## Target Rule

**BUFFS ONLY TARGET CHARACTERS.**

If a room needs buffs, create a "room spirit" character.

This keeps the system simple:
- One target type (character)
- One signature
- Room effects via room-spirit character

---

## Buff Schema

| Field | Type | Description |
|-------|------|-------------|
| **name** | string | Display name |
| **source** | string | What granted it |
| **effect** | object/string | Stat mods OR semantic prompt |
| **duration** | int/string | Turns, "forever", "50% per turn" |
| **polarity** | enum | positive, negative, neutral |
| **tags** | array | Searchable keywords |
| **stacks** | bool | Can apply multiple times? |
| **max-stacks** | int | Stacking limit |

---

## Buff Types

| Type | Description | Example |
|------|-------------|---------|
| **numeric** | Stat modifiers | `{energy: +2, focus: +1}` |
| **semantic** | Arbitrary vibes | "cats seem to like you today" |
| **conditional** | Trigger effects | "Next roll is critical success" |

---

## Duration Types

| Type | Example |
|------|---------|
| **turns** | 10 (integer) |
| **forever** | Permanent buff |
| **percentage** | "50% per turn" — random decay |
| **condition** | "until you eat" |
| **natural-language** | "about 5 minutes" — LLM judges |

---

## Methods

| Method | Purpose |
|--------|---------|
| **APPLY** | Add buff to character |
| **REMOVE** | Remove specific buff |
| **TICK** | Advance all durations by one turn |
| **LIST** | Show active buffs |
| **FIND-BY-TAG** | Find buffs with tag |
| **REMOVE-BY-TAG** | Remove all buffs with tag |
| **HAS-TAG** | Check if has buff with tag |
| **CLEANSE** | Remove all negative buffs |

---

## Buff Interactions

Buffs can interact with each other:

| Interaction | Description |
|-------------|-------------|
| **cancels** | Remove buffs with these tags |
| **boosts** | Increase buffs with these tags |
| **replaces** | Remove old, add this |
| **merges_with** | Combine into new buff |
| **blocked_by** | Prevent application |
| **counters** | Weaken other buffs |

Example: `{tags: ["fire", "ice"], result: "steam-burst"}`

---

## Lifecycle Hooks

Natural language → compiled to JS closures:

| Hook | When |
|------|------|
| **start** | Buff activates |
| **simulate** | Each tick |
| **is_finished** | Check if should end |

Signature: `(world, subject, verb, object) => { ... }`

---

## Standard Properties

Buffs modify these standard stats:

### Needs (Sims-style, 0-100)
hunger, energy, social, hygiene, bladder, fun, comfort

### Mind (cognitive/emotional)
focus, mood, stress, creativity, confidence, patience, curiosity

### Combat
hp, damage, armor, speed, luck

### Room Spirit
production_speed, error_rate, mood_influence, comfort_bonus

---

## Tag Examples

| Tag | Use |
|-----|-----|
| **combat** | Affects fighting |
| **social** | Affects interactions |
| **terpene** | From terpene kittens |
| **curse** | Negative effect |
| **dispellable** | Can be removed by spells |
| **embarrassing** | Social consequences |

---

## Security Assessment

### Concerns

1. **State modification** — buffs change character state
2. **JS compilation** — lifecycle hooks compile to closures
3. **Stacking** — could accumulate unbounded effects

### Mitigations

- All changes logged
- Max-stacks limits
- Cleanse method available
- Polarity marking (curses visible)

**Risk Level:** LOW — bounded, observable effects

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **D&D** | Buff/debuff spells |
| **World of Warcraft** | Buff stacking |
| **The Sims** | Moodlets |

---

## Verdict

**ELEGANT UNIFIED SYSTEM. APPROVE.**

The insight that curses are just negative buffs eliminates an entire subsystem.

One type. One signature. Infinite variety.
