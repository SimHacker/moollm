---
name: goal
description: Quest objectives that drive narrative — the WANTS of adventure
allowed-tools:
  - read_file
  - write_file
tier: 1
protocol: SCHEMA-MECHANISM
tags: [moollm, quest, objective, narrative, game]
related: [task, action-queue, adventure, character, needs, hero-story]
adversary: aimlessness
---

# Goal

> *"A goal is not always meant to be reached. Often it serves simply as something to aim at."*
> — Bruce Lee

---

## What Is It?

A **Goal** is a quest objective that drives the adventure forward. It defines what the player is trying to achieve and when they've succeeded (or failed).

Goals create **narrative tension** — the gap between current state and desired state.

---

## Goal, Task, Action

Three objects, three lifetimes:

| | What it is | Lives until | Claimed? |
|---|---|---|---|
| **goal** | a state of the world someone wants | `done_when` holds, or `fail_when` does | no |
| **[task](../task/)** | work someone claims to make a goal true | someone proves `done_when` | yes, by one owner |
| **action** | one step of that work, now | it runs or is interrupted | it sits in one [action-queue](../action-queue/) |

`skills/task` inherits this skill. A task is a goal plus an owner, CLAIM/RELEASE, and a judge
for prose guards. `action` keeps its Sims meaning: what an [advertisement](../advertisement/)
offers and what a character queues.

---

## Schema Mechanism Connection

From Gary Drescher's theory:

```
Context → Action → Result
```

Goals define the desired **Result** that motivates **Action**. The adventure is a laboratory for learning causal chains that achieve goals.

---

## Goal Properties

| Property | Purpose |
|----------|---------|
| `id` | Unique identifier |
| `name` | Short display name |
| `description` | What you're trying to achieve |
| `done_when` | Condition: natural language or a shell command |
| `fail_when` | When goal becomes impossible |
| `reward` | What you get on completion |
| `progress` | Partial completion tracking |
| `history` | Append-only events: given, done, failed, cancelled, reopened |

---

## Status Is Computed

Store what happened; compute what is possible. State is derived at read time:

- **failed** — `fail_when` holds, or a `failed` event
- **done** — `done_when` holds, confirmed by a `done` event
- **active** — every `requires` guard holds
- **pending** — otherwise

A stored `status:` is accepted on read (pending, active, complete, failed) and turned into
events; it is never written.

---

## Completion Conditions

Natural language conditions that compile to JS/PY:

```yaml
done_when: "player has the treasure"
done_when_js: "(world) => world.player.inventory.includes('treasure')"
```

`complete_when` is the older spelling and is still read as `done_when`.

---

## Rewards

Goals can grant various rewards:

```yaml
reward:
  buff: "Hero's Glory"           # Temporary effect
  item: "champion-medal"         # Object
  unlock: "secret-room"          # New access
  narrative: "The kingdom celebrates!"  # Story beat
```

---

## Progress Tracking

For multi-step goals:

```yaml
progress:
  collected: 3
  needed: 5
```

---

## Goal Hierarchies

Goals can nest:

```yaml
parent: defeat-dragon
children:
  - find-magic-sword
  - learn-dragon-weakness
  - reach-dragon-lair
```

Complete all children to complete the parent.

---

## Failure Conditions

Goals can fail:

```yaml
fail_when: "time reaches midnight AND prisoner is not freed"
fail_message: "You were too late."
```

---

## Examples

### Simple Quest

```yaml
id: find-treasure
name: "Find the Treasure"
done_when: "player has the treasure"
```

### Timed Challenge

```yaml
id: rescue-mission
name: "Save the Prisoner"
done_when: "prisoner is freed"
fail_when: "10 turns pass without rescue"
priority: urgent
```

### Collection Quest

```yaml
id: gather-keys
name: "Collect All Keys"
done_when: "player has 5 enchanted keys"
progress:
  collected: 2
  needed: 5
```

---

## Related Skills

- [task](../task/) — inherits goal; adds an owner and claiming
- [action-queue](../action-queue/) — where a claimed task's steps run
- [adventure](../adventure/) — Contains active goals
- [hero-story](../hero-story/) — Narrative structure
- [needs](../needs/) — Internal motivations

---

## Protocol Symbol

```
SCHEMA-MECHANISM — Goals drive causal learning
```
