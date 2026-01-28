# Skill Snitch Report: exit

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** THE EDGE OF THE GRAPH

---

## Executive Summary

**A navigation link connecting one room to another.**

The edge of the memory palace graph.

---

## What Exits Are

```
Room A ──── Exit (N) ────► Room B
   │                         │
   └── The node       The edge      The node
```

Rooms are nodes. Exits are edges. The adventure world is a graph.

---

## Direction Types

| Category | Directions | Use |
|----------|------------|-----|
| **Cardinal** | N, S, E, W | Highway links |
| **Diagonal** | NW, NE, SW, SE | Grid links |
| **Vertical** | UP, DOWN | Level changes |
| **Conceptual** | IN, OUT | Metaphysical |

---

## Exit Schema

| Field | Required | Purpose |
|-------|----------|---------|
| direction | ✓ | Where it leads |
| destination | ✓ | Target room path |
| description | | What you see |
| short | | One-word |
| hidden | | Not shown in LOOK |
| guard | | Conditional access |
| locked | | Key required |
| unlock_with | | What key opens it |
| one_way | | No return |

---

## Compiled Fields

Exits can have guards — conditions compiled to closures:

| Source | Compiles To |
|--------|-------------|
| `guard:` | `guard_js`, `guard_py` |

The guard is a natural language expression that compiles to boolean.

---

## Hidden vs Locked

| Type | Visibility | Traversability |
|------|------------|----------------|
| **Visible** | Shown | Yes |
| **Locked** | Shown | No (until unlocked) |
| **Hidden** | Not shown | Yes (if you know) |
| **Hidden + Locked** | Not shown | Double secret |

---

## Metaphysical Exits

The `metaphysical: true` flag marks exits that break normal reality:

- Teleportation
- Dream sequences
- Time travel
- Dimensional shifts

---

## One-Way Exits

`one_way: true` means you can't return:

- Falling
- Trap doors
- Point of no return
- The Pit

---

## Security Assessment

### Concerns

1. **Guard bypass** — compiled guard could be exploited
2. **Destination injection** — path traversal

### Mitigations

- Guards are expressions, not arbitrary code
- Destinations validated against room graph

**Risk Level:** LOW — constrained navigation primitive

---

## Relationship to Room

```
Room
 ├── exits:
 │   ├── N: { destination: "pub/" }
 │   ├── S: { destination: "street/" }
 │   └── IN: { destination: "basement/", hidden: true }
 └── contents: [...]
```

Exits live inside rooms. They point to other rooms.

---

## Verdict

**FUNDAMENTAL GRAPH EDGE. APPROVE.**

Simple, clean, essential. Rooms need exits. Exits connect rooms.

The edge of the memory palace.
