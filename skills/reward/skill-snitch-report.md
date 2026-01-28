# Skill Snitch Report: reward

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE TREASURE MATCHES THE QUEST

---

## Executive Summary

**Dynamic achievement rewards — thematically appropriate.**

Slay a dragon, get dragon stuff. Complete a quest, get quest-related boons.

---

## Reward Types

| Type | Description |
|------|-------------|
| **Items** | Physical objects |
| **Gold** | Currency |
| **Buffs** | Temporary effects |
| **Titles** | Reputation markers |
| **Abilities** | New capabilities |
| **Access** | Keys, permissions |
| **Knowledge** | Secrets revealed |

---

## Methods

| Method | Purpose |
|--------|---------|
| **GRANT** | Give a reward |
| **GENERATE** | Auto-generate thematic reward |

---

## Thematic Matching

```
Achievement: "Slay the dragon"
Context: "Fire dragon's lair"

Generated rewards:
- Dragon scales (armor material)
- Fire resistance buff
- Dragon's hoard gold
- Title: "Dragonslayer"
```

The reward fits the deed.

---

## Security Assessment

### Concerns

1. **Inflation** — too many rewards
2. **Inappropriate rewards** — don't match achievement
3. **Balance** — rewards too powerful

### Mitigations

- Thematic matching enforced
- DM controls GRANT
- Economy skill manages value

**Risk Level:** LOW — standard RPG mechanic

---

## Verdict

**THEMATIC REWARDS. APPROVE.**

The treasure matches the quest.

Dragon-related achievements → dragon-related rewards.
