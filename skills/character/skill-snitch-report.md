# Skill Snitch Report: character

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE BODY IN THE ROOM

---

## Executive Summary

**Characters are BODIES. Personas are COSTUMES.**

A character has location, inventory, relationships, and mortality.
A persona is a role you wear.

This distinction is foundational.

---

## The Core Insight

```
CHARACTER = ACTOR (the body)
PERSONA = ROLE (the costume)

Palm (character) wearing "bartender" (persona)
Same body, different role.
```

---

## Character Types

| Type | Control | Behavior |
|------|---------|----------|
| **player** | Human via chat | Direct control |
| **npc** | DM (LLM) | Responds when addressed |
| **companion** | Semi-autonomous | Follows player, has personality |
| **bot** | Action queue | Factorio-style carrier |
| **agent** | Full LLM | Own goals and initiative |
| **logistic-bot** | Programmatic | Automated resource movement |

---

## State Schema

```yaml
character:
  id: unique-identifier
  name: "Display name"
  home: "Directory where CHARACTER.yml lives (NEVER moves)"
  location: "Where character IS (changes during play)"
  inventory: [items...]
  gold: 0
  current-persona: null
  sims_traits: {nice: 5, outgoing: 5, active: 5, playful: 5, neat: 5}
  mind_mirror: {emotional: {}, intellectual: {}, physical: {}, social: {}}
  buffs: []
  relationships: {}
```

---

## Home vs Location

| Field | Meaning | Changes? |
|-------|---------|----------|
| **home** | Where CHARACTER.yml lives | NEVER |
| **location** | Where character IS | YES |

**Rule:** Update location field, don't move files.

---

## Multiple Dispatch

Characters can interact with each other. The system uses **multiple dispatch**:

```
dog SNIFFS cat  →  dog_sniffs_cat (most specific)
dog SNIFFS npc  →  dog_sniffs_character (species-level)
npc SNIFFS npc  →  character_sniffs_character (base)
```

Resolution order:
1. CHARACTER.yml (instance method)
2. Species skill (dog, cat)
3. Target skill
4. Base method

---

## Inventory Protocol

| Type | Description | Weight |
|------|-------------|--------|
| **object** | Deep copy, real item | Has weight/bulk |
| **ref** | Pointer to item | 0 weight |
| **fungible** | Stack with count | Weight × count |

Characters have capacity limits:
- **max_weight:** ~40-50
- **max_bulk:** ~8-12

Full protocol: `skills/inventory/SKILL.md`

---

## Methods

### Lifecycle
| Method | Purpose |
|--------|---------|
| CREATE | Create new character |
| STATUS | Show current state |

### Movement & Inventory
| Method | Purpose |
|--------|---------|
| MOVE | Move to destination |
| TAKE | Pick up item |
| DROP | Put down item |

### Personas
| Method | Purpose |
|--------|---------|
| WEAR | Put on identity layer |
| REMOVE-PERSONA | Take off identity layer |

### Interactions (dispatch-based)
| Method | Purpose |
|--------|---------|
| SNIFF | Investigate (species-specific) |
| LICK | Affection/grooming |
| GREET | Social acknowledgment |
| CUDDLE | Physical comfort |

---

## Security Assessment

### Concerns

1. **State ownership** — CHARACTER.yml is canonical
2. **File writes** — Updates character files
3. **Location tracking** — Knows where everyone is

### Mitigations

- Clear ownership rules (CHARACTER.yml wins on conflict)
- All changes logged
- Location is just a field, not filesystem movement

**Risk Level:** LOW — foundational, well-bounded

---

## Lineage

| Ancestor | Contribution |
|----------|--------------|
| **The Sims** | Needs, traits, relationships |
| **D&D** | Character sheets, stats |
| **MUD** | Player characters in rooms |

---

## The Character/Persona Split

Why separate them?

1. **Flexibility** — Same character, different roles
2. **Clarity** — Body state vs role behavior
3. **Persistence** — Character survives persona changes
4. **Ethics** — Clear who IS vs who is PLAYING

Example:
- Palm (character) wearing "bartender" persona serves drinks
- Palm (character) wearing "musician" persona plays piano
- Same cat, different costumes

---

## Verdict

**FOUNDATIONAL. APPROVE.**

Without characters, MOOLLM has no actors.
With characters, MOOLLM has **embodied entities** that move, carry things, and relate to each other.

This is the difference between documents and a world.
