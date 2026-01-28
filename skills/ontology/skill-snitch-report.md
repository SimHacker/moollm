# Skill Snitch Report: ontology

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** TAGS, NOT TREES

---

## Executive Summary

**Composable ontological tags for character identity.**

Tags, not trees. Folksonomy, not taxonomy.

What kind of being is this? Multiple answers allowed.

---

## The Core Insight

Traditional: characters have ONE type (class, category).
Ontology: characters have **multiple tags** (folksonomy).

| Character | Tags | Ethics |
|-----------|------|--------|
| Biscuit | [real-being, animal] | Full respect + species-appropriate |
| C-3PO | [fictional, robot] | Creative freedom + robotic behavior |
| Spirit of Minsky | [historical, abstract] | Legacy respect + acknowledge personification |

---

## The Ontological Tags

| Tag | Emoji | Summary |
|-----|-------|---------|
| **real-being** | 👤 | Actually exists — highest ethical weight |
| **historical** | 📜 | Deceased real being — extends real-being |
| **fictional** | 📖 | Invented — creative freedom within bounds |
| **animal** | 🐾 | Non-human creature — species-appropriate |
| **robot** | 🤖 | Artificial being — transparent about nature |
| **abstract** | 💭 | Concept personified — ideas with voice |
| **mythic** | ✨ | Mythology/folklore — cultural sensitivity |

---

## How Tagging Works

Tags come from skill inheritance:

```yaml
character:
  id: biscuit
  inherits:
    - skills/real-being   # Tag: [real-being]
    - skills/animal       # Tag: [animal]
  # Effective tags: [real-being, animal]
```

Each tag IS a skill. Inherit = tagged.

---

## Composition Rule

**Most restrictive ethics apply.**

| Combination | Tags | Ethics |
|-------------|------|--------|
| Real animal | [real-being, animal] | Full respect + species-appropriate |
| AI trained on real | [real-being, robot, fictional] | Consent + AI disclosure + generated not quoted |
| Real-inspired fiction | [real-being, fictional] | HERO-STORY required + disclaimer |

---

## Methods

| Method | Purpose |
|--------|---------|
| **TAG** | Assign ontological tags to character |
| **CHECK-ETHICS** | Compute combined ethics from all tags |
| **COMPOSE** | Combine multiple ontological sources |

---

## High-Risk Combinations

| Combination | Risk | Required |
|-------------|------|----------|
| [real-being, fictional] | High | HERO-STORY protocol |
| [real-being, robot] | Medium | Clear AI disclosure |
| [historical, fictional] | Medium | Legacy respect |

---

## Why Tags, Not Trees?

| Trees (Taxonomy) | Tags (Folksonomy) |
|------------------|-------------------|
| One category | Multiple categories |
| Mutually exclusive | Composable |
| Designer decides | Multiple inheritance |
| Rigid | Flexible |

A dog can be [real-being, animal, historical, mythic] if they're a legendary dog who actually lived and became folklore.

---

## Security Assessment

### Concerns

1. **Tag manipulation** — remove ethics-carrying tags
2. **Composition bypass** — ignore "most restrictive"
3. **Real-being abuse** — improperly tag fictional as real

### Mitigations

- Tags visible
- Ethics checked on portrayal
- HERO-STORY enforced for real-being

**Risk Level:** LOW — transparent, auditable

---

## Integration

| Skill | Integration |
|-------|-------------|
| hero-story | HERO-STORY protocol for real-being |
| representation-ethics | Detailed ethics guidance |
| character | Creation uses tags |
| incarnation | Respects ontological ethics |

---

## Verdict

**ETHICAL FOUNDATION. APPROVE.**

Tags, not trees. Folksonomy, not taxonomy.

Characters are complex. They can be multiple things. The most restrictive ethics win.

This is how you handle identity ethically.
