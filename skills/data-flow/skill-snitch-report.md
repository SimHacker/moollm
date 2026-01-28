# Skill Snitch Report: data-flow

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** ROOMS AS PROCESSING NODES

---

## Executive Summary

**Kilroy-style data flow programming in the filesystem.**

Rooms are processing nodes. Exits are edges. Objects THROWN through exits are messages.

Build Factorio-like pipelines in the adventure world.

---

## The Core Pattern

```
Room A        Exit         Room B
┌──────┐    ─────────►    ┌──────┐
│      │                  │ INBOX│ ← objects land here
│OUTBOX│ ← objects wait   │      │
└──────┘                  └──────┘
   │         THROW           │
   └─────────────────────────┘
```

---

## Metaphor Mapping

| Concept | Maps To |
|---------|---------|
| **Processing node** | Room |
| **Edge** | Exit |
| **Message** | Object |
| **Input buffer** | Inbox |
| **Output buffer** | Outbox |
| **Pipeline** | Connected room sequence |

---

## Methods

| Method | Purpose |
|--------|---------|
| **THROW** | Send object through an exit |
| **RECEIVE** | Process incoming objects from inbox |
| **CONNECT** | Create data flow edge between rooms |
| **PIPELINE** | Define multi-stage processing pipeline |

---

## The THROW Operation

```yaml
THROW cookie-jar N
# cookie-jar appears in northern room's inbox
```

Objects don't move instantly — they land in the destination's inbox, waiting for RECEIVE.

---

## Room Processing

Each room can have rules:

```yaml
room:
  on_receive:
    - "If object is ingredient, transform to dish"
    - "If object is raw, send to oven room"
    - "If object is finished, send to serving room"
```

The room transforms objects and routes them onward.

---

## Pipeline Example

```yaml
pipeline:
  name: "Cookie Factory"
  stages:
    - name: mixing-room
      receives: [ingredients]
      produces: [dough]
    - name: oven-room
      receives: [dough]
      produces: [cookies]
    - name: packaging-room
      receives: [cookies]
      produces: [boxed-cookies]
```

---

## Security Assessment

### Concerns

1. **Object routing** — could send dangerous objects
2. **Processing rules** — room transforms objects
3. **Pipeline automation** — unattended processing

### Mitigations

- Rooms visible and auditable
- Processing rules are natural language
- Pipelines explicit

**Risk Level:** LOW — transparent, inspectable

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Kilroy** | Room-based data flow |
| **Factorio** | Factory automation |
| **Unix pipes** | Data transformation |

---

## Why This Matters

Traditional adventures: objects are static.
Data-flow adventures: **objects move through processing**.

A factory becomes explorable. A workflow becomes navigable.

You can LOOK at the bottleneck. You can EXAMINE the transformation.

---

## Verdict

**FACTORIO MEETS TEXT ADVENTURES. APPROVE.**

Rooms as nodes. Exits as edges. Objects as messages.

The filesystem becomes a factory you can walk through.
