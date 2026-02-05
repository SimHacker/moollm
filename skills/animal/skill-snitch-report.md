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

## 🔄 DUAL-USE & BIAS ANALYSIS

**Profile**: IMPLICIT — prototype inheritance demonstrates dual-use through species specialization

| Check | Result |
|-------|--------|
| Bias declared | NO — animals have SPECIES, not bias |
| Invertibility | YES (implicit) — species behaviors invert across the inheritance tree |
| Inheritance chain | animal → cat, animal → dog (same base, opposite temperaments) |
| Multi-purpose | YES — game NPCs, emotional modeling, species education |

**Multi-purpose classification** (4 purposes):
1. **Game NPCs** — companion animals with species-appropriate behavior
2. **Emotional modeling** — trust mechanics (cat), loyalty mechanics (dog) model real relationships
3. **Species education** — "not humans in fur suits" teaches species-appropriate thinking
4. **Prototype inheritance demonstration** — animal is the textbook example of MOOLLM inheritance

**Key dual-use insight**: Animal is the PARENT PROTOTYPE. Cat and dog inherit from it but specialize in OPPOSITE DIRECTIONS. Same PAT method, different response. Same GREET method, opposite behavior. The animal skill doesn't have dual-use — it has FORKED use. The fork happened at speciation. The dual-use IS the inheritance tree.

**Anthropomorphization**: Documented as possible but requiring acknowledgment. "We can anthropomorphize — just acknowledge it." This is representation-ethics applied to non-human entities.

---

## Verdict

**FOUNDATION FOR ALL CREATURES. APPROVE.**

Species over story. Not humans in fur suits.

But we can anthropomorphize — just acknowledge it.
