# Skill Snitch Report: bartender

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** POUR DRINKS, KNOW SECRETS, SAY NOTHING

---

## Executive Summary

**The ancient art of tending bar.**

This is a ROLE skill — provides methods, not personality.

Capability comes from this SKILL. Personality comes from your PERSONA.

---

## Methods

### Service
| Method | Purpose |
|--------|---------|
| **POUR** | Make and serve a drink |
| **TAKE-ORDER** | Listen to customer's request |
| **RECOMMEND** | Suggest drinks |
| **REFUSE-SERVICE** | Cut someone off |
| **LAST-CALL** | Announce closing |

### Economics
| Method | Purpose |
|--------|---------|
| **OPEN-TAB** | Start a tab |
| **ADD-TO-TAB** | Add item to tab |
| **CLOSE-TAB** | Collect payment |
| **COMP** | Give something free |

### Social
| Method | Purpose |
|--------|---------|
| **LISTEN** | Hear troubles |
| **INTRODUCE** | Connect two customers |
| **EJECT** | Remove troublemaker |
| **KNOW-REGULAR** | Recognize repeat customer |

---

## State

```yaml
station: "pub/bar"
tabs: { customer_id: balance }
regulars: [known customers]
banned: [not welcome]
secrets: { subject: knowledge }  # PRIVATE
```

---

## Inheritance

Can be inherited by:
- **budtender** — adds cannabis expertise
- **sommelier** — wine specialist
- **mixologist** — cocktail specialist
- **barista** — coffee specialist

---

## Security Assessment

### Concerns

1. **secrets** field is private — never revealed directly
2. **EJECT** affects player movement

### Mitigations

- Private fields documented
- Actions require justification

**Risk Level:** LOW — role mechanics

---

## Archetype

> "The wise counsel behind the bar."

---

## Verdict

**BARTENDING AS GAME MECHANIC. APPROVE.**

Pour drinks, know secrets, say nothing.

Capability here. Personality from persona.
