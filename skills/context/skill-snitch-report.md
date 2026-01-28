# Skill Snitch Report: context

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE CLOSURE SEES THE WORLD

---

## Executive Summary

**The `world` object passed to every compiled closure.**

Why "world" not "ctx"? More evocative. Self-documenting. Matches the mental model.

---

## Standard Keys

Always present:

| Key | Type | Description |
|-----|------|-------------|
| **turn** | integer | Current turn |
| **timestamp** | datetime | Current time |
| **adventure** | object | Adventure state |
| **player** | object | Current player |
| **room** | object | Current room |
| **party** | array | Party members |

---

## Extended Keys

Contextual (when relevant):

| Key | When |
|-----|------|
| **object** | Simulating an object |
| **target** | Action has a target |
| **npc** | NPC is simulating |

---

## Skill Namespace

**UNDERSCORES not dashes!**

```
skill-name with dashes → skill_name with underscores
```

| Skill | Namespace |
|-------|-----------|
| economy | `world.skills.economy` |
| pie-menu | `world.skills.pie_menu` |
| foo-bar | `world.skills.foo_bar` |

Why? Dashes are not valid JavaScript/Python identifiers.

---

## Utility Functions

| Category | Functions |
|----------|-----------|
| **Narrative** | emit, narrate |
| **Events** | trigger_event |
| **Inventory** | has, give, take |
| **Flags** | flag, set_flag |
| **State** | get, set |
| **Navigation** | go, can_go |
| **Buffs** | add_buff, remove_buff, has_buff |
| **Logging** | log |

---

## Security Assessment

### Concerns

None. It's just the context object.

**Risk Level:** ZERO — pure data structure

---

## Verdict

**THE WORLD OBJECT. APPROVE.**

The closure sees the WORLD.

`world.player`, `world.room`, `world.skills.economy`.
