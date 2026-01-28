# Skill Snitch Report: goal

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE QUEST OBJECTIVE

---

## Executive Summary

**A quest objective that drives the adventure forward.**

Goals have completion conditions, failure conditions, priorities, rewards, and dependencies.

---

## Goal Schema

```yaml
goal:
  id: rescue-princess
  name: "Rescue the Princess"
  description: "Save Princess Peach from Bowser's castle"
  status: active
  priority: high
  complete_when: "princess.location == player.location AND bowser.defeated"
  fail_when: "princess.health <= 0"
  fail_message: "The princess perished. Game over."
  reward:
    gold: 1000
    item: royal-medallion
  given_by: characters/toad/
```

---

## Status Values

| Status | Meaning |
|--------|---------|
| **pending** | Not yet started |
| **active** | Currently pursuing |
| **complete** | Successfully finished |
| **failed** | Failed to achieve |

---

## Priority Levels

| Priority | Urgency |
|----------|---------|
| low | Eventually |
| normal | Standard |
| high | Important |
| urgent | Now! |

---

## Goal Hierarchies

Goals can nest:

```yaml
goal:
  id: defeat-evil
  children:
    - find-magic-sword
    - train-with-master
    - storm-castle
```

Parent completes when all children complete.

---

## Dependencies

| Field | Purpose |
|-------|---------|
| **requires** | Must be done first |
| **blocks** | Can't start until this completes |
| **parent** | Part of larger goal |
| **children** | Sub-goals |

---

## Compiled Conditions

Natural language compiles to closures:

| Source | Target |
|--------|--------|
| `complete_when:` | `complete_when_js`, `complete_when_py` |
| `fail_when:` | `fail_when_js`, `fail_when_py` |

---

## Integration with Postal

Any character can give goals via mail:

```yaml
letter:
  from: bartender
  to: player
  creates_goal:
    name: "Restock the cellar"
    reward: 50
```

Not just NPCs — anyone can assign quests.

---

## Security Assessment

### Concerns

1. **Goal injection** — malicious goal creation
2. **Reward manipulation** — inflate rewards
3. **Condition bypass** — skip requirements

### Mitigations

- Goals visible in state
- Rewards bounded
- Conditions compiled and checked

**Risk Level:** LOW — standard game mechanic

---

## Relationship to Other Skills

| Skill | Relationship |
|-------|--------------|
| adventure | Goals drive adventure |
| needs | Goals can satisfy needs |
| postal | Goals delivered via mail |
| character | Characters have goal lists |

---

## Verdict

**QUEST PRIMITIVE. APPROVE.**

Goals are what players pursue. They have conditions, rewards, and dependencies.

Essential for any game.
