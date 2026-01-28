# Skill Snitch Report: subjective

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** FIRST-PERSON CODE — THE "I" SHIFTS

---

## Executive Summary

**Subjective-Oriented Programming.**

`i_have("key")` instead of `world.has("key")`.

The "I" shifts based on who is speaking.

---

## Who Can Be "I"?

| Subject | Context |
|---------|---------|
| **player** | In player action handlers |
| **object** | In object simulate() |
| **npc** | In NPC dialogue/behavior |
| **room** | In room descriptions |

---

## Core i_ Functions

### Inventory
- `i_have` — Do I have this?
- `i_give` — Give to someone
- `i_take` — Take from somewhere
- `i_drop` — Drop item
- `i_has_tag` — Tag check
- `i_find_by_tag` — Find by tag

### State
- `i_am` — Set state flag
- `i_am_not` — Clear state flag
- `i_get` — Get property
- `i_set` — Set property

### Buffs
- `i_have_buff` — Check buff
- `i_add_buff` — Add buff
- `i_remove_buff` — Remove buff

### Location
- `i_am_in` — Location check
- `i_can_see` — Visibility check
- `i_go` — Move

### Communication
- `i_say` — Speak
- `i_emote` — Action
- `i_think` — Inner thought
- `i_emit` — Broadcast

---

## Subject Resolution

Priority order:
1. **object** — if world.object is set
2. **npc** — if world.npc is set
3. **player** — default fallback

---

## The Insight

> "First-person code reads naturally and shifts perspective automatically."

When an NPC's simulate() runs, `i_have` checks the NPC's inventory.
When a player action runs, `i_have` checks the player's inventory.

Same code, different subject.

---

## Security Assessment

### Concerns

1. **Subject confusion** — whose "I" is this?
2. **Scope leakage** — wrong subject active

### Mitigations

- Clear resolution priority
- Context sets subject explicitly

**Risk Level:** LOW — elegant abstraction

---

## Verdict

**ELEGANT PERSPECTIVE SHIFT. APPROVE.**

First-person code. The "I" shifts.

`i_have("key")` works for anyone.
