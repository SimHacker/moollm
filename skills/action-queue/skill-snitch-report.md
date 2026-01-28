# Skill Snitch Report: action-queue

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** QUEUE UP WHAT TO DO NEXT

---

## Executive Summary

**The Sims-inspired task scheduler.**

Queue actions, execute in order. Objects can push prerequisites. Urgent tasks jump the line.

---

## The Sims Pattern

In The Sims, characters don't execute actions immediately. They **queue** them:

```
Queue: [eat, shower, sleep]
       ↓ NEXT
Executing: eat
Queue: [shower, sleep]
```

---

## Methods

| Method | Purpose |
|--------|---------|
| **DO** | Add action to end of queue |
| **NEXT** | Execute next queued action |
| **QUEUE** | Show current action queue |
| **URGENT** | Insert action at front (jump line) |
| **CANCEL** | Remove action from queue |
| **CLEAR** | Empty entire queue |
| **REORDER** | Move action to new position |
| **PAUSE** | Stop executing, keep queue |
| **RESUME** | Continue executing |

---

## Queue State

```yaml
action-queue:
  - eat
  - shower
  - sleep
queue-state:
  paused: false
  current-index: 0
  mode: autonomous  # or manual
```

---

## Object Push Pattern

Objects can push prerequisites:

```
Player: EAT
Fridge: "Wait, you need food first"
        → URGENT: GET-FOOD
        → Then: EAT

Queue becomes: [GET-FOOD, EAT]
```

**The Sims insight:** Objects know what they need.

---

## Autonomous vs Manual Mode

| Mode | Behavior |
|------|----------|
| **Manual** | Player says NEXT to advance |
| **Autonomous** | Agent auto-executes queue |

---

## The Workbench Example

```
Player: CRAFT sword
Workbench: "Need materials"
           → URGENT: GET-IRON
           → URGENT: GET-COAL
           → Then: CRAFT sword

Queue: [GET-IRON, GET-COAL, CRAFT sword]
```

Objects guide multi-step processes.

---

## Security Assessment

### Concerns

1. **Queue manipulation** — add dangerous actions
2. **URGENT abuse** — always jump the line
3. **Autonomous mode** — unattended execution

### Mitigations

- Queue visible
- PAUSE available
- Player can CANCEL anything

**Risk Level:** LOW — transparent, interruptible

---

## Relationship to Other Skills

| Skill | Relationship |
|-------|--------------|
| **return-stack** | Past (history) vs future (queue) |
| **advertisement** | Objects suggest what to queue |
| **needs** | Motivates which actions to queue |
| **coherence-engine** | Orchestrates execution |

---

## Verdict

**THE SIMS TASK SCHEDULER. APPROVE.**

Queue up what to do. Objects push prerequisites. Execute in order.

Simple but essential. This is how autonomous agents work.
