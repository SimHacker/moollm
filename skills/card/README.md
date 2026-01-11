# 🎴 Card

> *"Portable tokens of capability, identity, and access."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [room/](../room/) | Cards activate in rooms |
| [soul-chat/](../soul-chat/) | Cards can speak |
| [adventure/](../adventure/) | Cards as quest companions |
| [advertisement/](../advertisement/) | Cards advertise abilities |
| [return-stack/](../return-stack/) | Activation records as continuations |
| [visualizer/](../visualizer/) | Pure state prompt clusters |
| [hero-story/](../hero-story/) | Hero cards invoke traditions |

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Cards are portable capability tokens you can carry, play, and activate. They're **templates** — put them in play in a [room](../room/) to create live instances.

**Origin:** Magic: The Gathering + K-lines + Hewitt Actors.

## Quick Example

```yaml
card:
  name: "Git Goblin"
  type: familiar
  emoji: "🧌"
  
  ability:
    name: "Bisect"
    effect: "Binary search for bug introduction"
    
  advertisements:
    - action: BISECT
      score: 90
```

## Card Types

| Type | Examples |
|------|----------|
| `person` | Dave Ungar, Seymour Papert (Hero-Story) |
| `familiar` | Git Goblin 🧌, Index Owl 🦉 |
| `tool` | fs.read, search.vector |
| `concept` | POSTEL, YAML-JAZZ |

## Activation Records

**Playing a card = creating an activation record.** Like Self, cards have multiple methods:

```yaml
# design-room/architect-task-001.activation
card: architect.card
method: generate_proposal
state:
  iteration: 3
  status: awaiting_vote
```

Cards can also be **pure state** (prompt clusters, context bundles) that other cards reference.

## Commands

| Command | Effect |
|---------|--------|
| `PLAY [card]` | Activate in room |
| `PLAY [card].[method]` | Activate specific method |
| `COLLECT [card]` | Add to collection |
| `DECK [name]` | Build/select deck |

## Templates

| File | Purpose |
|------|---------|
| [CARD.yml.tmpl](CARD.yml.tmpl) | Individual card |
| [COLLECTION.yml.tmpl](COLLECTION.yml.tmpl) | Card collection |


## Tools Required

- `file_read` — Read card definitions
- `file_write` — Create cards and collections

---

*See [SKILL.md](SKILL.md) for complete specification.*
