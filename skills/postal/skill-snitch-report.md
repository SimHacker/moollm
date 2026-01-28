# Skill Snitch Report: postal

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** MAIL GOES EVERYWHERE

---

## Executive Summary

**Complete messaging infrastructure: letters, texts, goals, rewards, attachments.**

Any character can send/receive. Goals come from anyone, not just Mom.

**UNIVERSAL ADDRESSING:** Mail goes anywhere pointers go.
Send a letter to a function, a YAML key, a line of code.

---

## The Core Insight

> "Mail goes anywhere pointers go."

If you can point to it, you can mail to it.

---

## Address Types

| Type | Example |
|------|---------|
| **Reserved** | `player`, `party`, `narrator` |
| **Character** | `characters/don-hopkins/` |
| **Room** | `pub/` |
| **Object** | `start/mailbox.yml` |
| **YAML section** | `config.yml#settings.notifications` |
| **JSON path** | `package.json#/dependencies/svelte` |
| **MD heading** | `README.md#installation` |
| **Function** | `src/lib/utils.ts#fetchData` |
| **Line number** | `engine.cpp:142` |
| **Line range** | `auth.py:45-67` |

> "Not all addresses make sense. They're all valid anyway."

---

## Message Types

| Type | Delivery | Attachments | Goals |
|------|----------|-------------|-------|
| **Letter** | Queued (3 turns) | Any | Can create |
| **Text** | Instant | Photos only | Rarely |

---

## Delivery Methods

| Method | Time | Cost | Features |
|--------|------|------|----------|
| Text | 0 | 0 | Instant, photos only |
| Letter | 3 | 1 | Standard |
| Express | 1 | 5 | Fast, tracking |
| Freight | 10 | 0.5/kg | Heavy items |
| Courier | 2 | 10 | Guaranteed |

---

## Attachment Types

| Type | Actions |
|------|---------|
| Object | Send, give, copy, reference |
| Gold | Send |
| Image | Copy, generate, reference |
| Buff | Apply |
| Room | Unlock, reference |
| Message | Forward |

---

## Goal Integration

```yaml
# Any character can assign goals!
letter:
  from: bartender
  to: player
  creates_goal:
    name: "Restock the cellar"
    reward: 50 gold
```

Not just Mom. Anyone can give you quests.

---

## It's 2026 — Everyone Has a Phone

```yaml
phone:
  always_available: true
  capabilities: [mail, text, notifications, camera, maps]
```

Modern adventure game assumption.

---

## Deterministic Routing

```
Resolution order:
1. Reserved keywords (player, party, narrator)
2. Relative paths
3. Absolute paths
4. Object paths
```

No LLM needed for routing. Simulator handles it.

---

## In-Transit State

```yaml
world.skills.postal.in_transit:
  - turns_remaining: 2
    from: don
    to: palm
    method: letter
```

Mail ticks down. Arrives when zero.

---

## Operations

| Command | Purpose |
|---------|---------|
| CHECK_PHONE | See notifications |
| READ_MAIL | Read inbox |
| READ_MESSAGE | Read specific |
| COMPOSE | Write new |
| REPLY | Respond |
| ATTACH | Add attachment |
| SEND | Dispatch letter |
| TEXT | Instant message |

---

## Security Assessment

### Concerns

1. **Universal addressing** — can mail to any pointer
2. **Goal injection** — anyone can assign goals
3. **Attachment transfer** — moves objects

### Mitigations

- "Not all addresses make sense" — that's OK
- Goals are visible, player can ignore
- Attachments use inventory protocol

**Risk Level:** MEDIUM — powerful but transparent

---

## Relationship to Inventory

Postal shares pointer syntax with inventory:

- Same addressing scheme
- Attachments use inventory transfer
- Location-as-pointer works both ways

---

## Verdict

**UNIVERSAL MESSAGING. APPROVE.**

Mail goes anywhere pointers go. That's the insight.

Want to send a bug report to line 142? Address it to `engine.cpp:142`.

Absurd but consistent.
