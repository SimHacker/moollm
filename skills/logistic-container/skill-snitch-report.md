# Skill Snitch Report: logistic-container

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** ITEMS FLOW LIKE WATER THROUGH PIPES

---

## Executive Summary

**Factorio-style logistics boxes.**

Items flow automatically between providers and requesters.

"The factory grows. Items flow. The world runs itself."

---

## Box Types

| Type | Emoji | Behavior |
|------|-------|----------|
| **Passive Provider** | 📦🟡 | Take from me if you need it |
| **Active Provider** | 📦🔴 | I'm pushing these OUT |
| **Requester** | 📦🔵 | I WANT these items |
| **Storage** | 📦⬜ | General overflow |
| **Buffer** | 📦🟢 | Hold until needed |

---

## Grid Storage

```
warehouse/
  LOGISTIC-CONTAINER.yml
  iron-ore/
    CELL.yml    # count: 2500
  copper-ore/
    CELL.yml    # count: 1800
  magic-sword/
    CELL.yml    # instances: [...]
```

Auto-create cells for new item types.

---

## Item Handling

| Mode | For | Behavior |
|------|-----|----------|
| **Fungible** | Commodities | Just count them |
| **Instance** | Unique items | Each has state |
| **Auto** | Based on tags | Decide automatically |

---

## Methods

| Method | Purpose |
|--------|---------|
| **ADD** | Add item to container |
| **REMOVE** | Remove item |
| **TRANSFER** | Move between containers |
| **REQUEST** | Pull from providers |
| **PUSH** | Push from active-provider |
| **QUERY** | Check contents |
| **NAVIGATE** | Walk through grid cells |

---

## Security Assessment

### Concerns

1. **Item duplication** — counting errors
2. **Infinite loops** — push/pull cycles
3. **Overflow** — stack limits exceeded

### Mitigations

- Deterministic transfers
- Stack limits enforced
- Events logged

**Risk Level:** LOW — Factorio got this right

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Factorio** | Logistic network, chests, bots |
| **Minecraft** | Item stacking and storage |
| **The Sims** | Inventory management |

---

## Verdict

**AUTOMATION INFRASTRUCTURE. APPROVE.**

Items flow like water through pipes.

The factory grows.
