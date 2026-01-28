# Skill Snitch Report: card

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** PORTABLE TOKENS OF CAPABILITY

---

## Executive Summary

**The meta-skill for understanding and creating cards.**

Trading cards, playing cards, Magic cards, Tarot cards, business cards, key cards, receipts, tickets — all cards.

---

## Key Insight

> "Cards are ACTIVATION TRIGGERS, not handlers."

CARD.yml tells you IF to use. SKILL.md tells you HOW.

---

## Card Types

| Type | Description |
|------|-------------|
| **trading-card** | Hero-Story cards for real people |
| **playing-card** | Actions, abilities, spells |
| **fluxx-card** | Rule-changing cards |
| **skill-card** | Capabilities you can invoke |
| **character-card** | Summonable personas |
| **item-card** | Objects with effects |
| **key-card** | Access tokens |

---

## Methods

| Method | Signature |
|--------|-----------|
| **CREATE** | `CREATE [name] TYPE [types]` |
| **PLAY** | `PLAY [card] (IN [room])` |
| **COLLECT** | `COLLECT [card] TO [collection]` |
| **TRADE** | `TRADE [cards] WITH [character]` |
| **EXAMINE** | `EXAMINE [card]` |
| **ACTIVATE** | `ACTIVATE [card] [method]` |

---

## Card Structure (Recommended Order)

```
1. card: (id, name, emoji, tagline)
2. files: (index for context)
3. k-lines: (activation vectors)
4. advertisements: (PRIMARY — before methods!)
5. methods: (signatures only)
6. state: (brief)
7. documentation: (pointers)
```

Target: ~150-200 lines. Smell: >300 lines → move to SKILL.md.

---

## Sidecar Pattern

Any entity can have a CARD.yml sidecar:

- `pub/CARD.yml` — makes pub playable
- `characters/don/CARD.yml` — trading card
- `objects/lamp/CARD.yml` — item card

---

## Security Assessment

### Concerns

1. **Card creation** — can create capabilities
2. **PLAY effects** — cards do things
3. **FLUXX cards** — change rules

### Mitigations

- Cards are visible
- Effects bounded by type
- Room ethics apply

**Risk Level:** MEDIUM — powerful but transparent

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Magic: The Gathering** | Complex card interactions |
| **Fluxx** | Rule-changing cards |
| **Tarot** | Archetypal prompts |
| **Self language** | Cards as prototype objects |

---

## Verdict

**PORTABLE CAPABILITIES. APPROVE.**

Cards are tokens you carry, play, and activate.

The sidecar pattern lets anything become a card.
