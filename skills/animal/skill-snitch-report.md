# Skill Snitch Report: animal

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** SPECIES OVER STORY

---

## Executive Summary

**Base skill for non-human creatures.**

Dogs, cats, dragons, aliens — all inherit from here.

Animals are NOT humans in fur suits.

---

## Shared Advertisements

| Action | Purpose |
|--------|---------|
| **PAT** | Brief friendly touch |
| **FEED** | Provide food/treat |
| **OBSERVE** | Watch without interacting |
| **CALL** | Try to get attention |
| **SNIFF** | Olfactory investigation |
| **GREET** | Species-appropriate hello |
| **CUDDLE** | Close contact comfort |
| **VOCALIZE** | Species-appropriate sound |
| **FOLLOW** | Accompany someone |
| **FLEE** | Run from danger |

---

## Multiple Dispatch

Interactions dispatch based on participants:

| Interaction | Dispatch |
|-------------|----------|
| animal_sniffs_animal | Species-specific protocol |
| animal_sniffs_human | Species-specific protocol |
| animal_sniffs_object | Curiosity, food check |
| animal_greets_animal | Species protocol |
| animal_greets_human | Species protocol |

---

## Parental Inheritance

Animals inherit from parents:

```yaml
kitten:
  inherits:
    from_species: skills/cat
    from_parent: characters/stroopwafel
  gets:
    - stroopwafel's suspicion of new things
    - stroopwafel's love of warm spots
```

---

## Inherited By

- skills/dog
- skills/cat
- skills/puppy
- skills/kitten
- (future: dragon, horse, bird, etc.)

---

## Anthropomorphization

When anthropomorphizing: **acknowledge it**.
When playing straight: **species-appropriate behavior**.

---

## Verdict

**FOUNDATION FOR ALL CREATURES. APPROVE.**

Species over story. Not humans in fur suits.

But we can anthropomorphize — just acknowledge it.
