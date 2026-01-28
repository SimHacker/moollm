# Skill Snitch Report: persona

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE COSTUME ON THE BODY

---

## Executive Summary

**Identity layers that modify how a character presents.**

Characters are BODIES. Personas are COSTUMES.

Same actor, different roles.

---

## The Body/Costume Distinction

```
CHARACTER (body)     PERSONA (costume)
     │                     │
     └──── WEAR ──────────►│
                           │
     Palm (the cat)    "bartender"
     Palm (the cat)    "musician"
     Palm (the cat)    "detective"
```

The body persists. The costume changes.

---

## What Personas Modify

| Field | Effect |
|-------|--------|
| **voice** | How to speak in this role |
| **trait-modifiers** | Sims trait adjustments |
| **abilities** | What the persona grants |
| **constraints** | What the persona forbids |
| **reputation** | How others perceive you |

---

## Methods

| Method | Purpose |
|--------|---------|
| **WEAR** | Put on a persona |
| **REMOVE** | Take off current persona |
| **CREATE** | Design new persona |
| **PREVIEW** | See how persona would change you |

---

## Example: Palm the Cat

| Persona | Voice | Abilities |
|---------|-------|-----------|
| None | Feline aloofness | Standard cat abilities |
| Bartender | Professional warmth | Mix drinks, manage tabs |
| Musician | Artistic temperament | Play piano, compose |
| Detective | Hard-boiled cynicism | Investigate, interrogate |

Same cat. Different hats.

---

## Persona Schema

```yaml
persona:
  name: "Bartender"
  voice: "Professional, warm, knows everyone's name"
  trait-modifiers:
    outgoing: +3
    nice: +2
  abilities:
    - mix-drinks
    - manage-tabs
    - refuse-service
  constraints:
    - cannot-leave-bar-during-shift
  reputation:
    bar-patrons: friendly
    management: reliable
```

---

## Security Assessment

### Concerns

1. **Identity confusion** — persona vs character blur
2. **Ability escalation** — persona grants dangerous abilities
3. **Constraint bypass** — remove persona to escape limits

### Mitigations

- Clear body/costume distinction
- Abilities bound to persona context
- Removal is observable action

**Risk Level:** LOW — clear, bounded identity layers

---

## Relationship to Other Skills

| Skill | Relationship |
|-------|--------------|
| **character** | Character WEARS persona |
| **mind-mirror** | Persona can modify Mind Mirror display |
| **coatroom** | Room for storing/changing personas |
| **representation-ethics** | Personas are ethical (costumes, not souls) |

---

## Why Separate Body and Costume?

### Practical
- Same character, multiple contexts
- Role-specific abilities don't persist
- Easy to try different identities

### Ethical
- Clear who IS vs who is PLAYING
- No confusion about identity
- Representation-ethics compatible

### Design
- Modular identity system
- Characters don't bloat with abilities
- Personas can be shared/traded

---

## Verdict

**CLEAN IDENTITY LAYERS. APPROVE.**

The persona skill solves the "one character, many roles" problem elegantly:

- Body persists (CHARACTER)
- Costume changes (PERSONA)
- Clear boundaries
- Ethical by design
