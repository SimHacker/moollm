# 🎴 Card

> *"Portable tokens of capability, identity, and access."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [skill/](../skill/) | Cards ARE skills |
| [prototype/](../prototype/) | Cards clone from prototypes |
| [room/](../room/) | Cards activate in rooms |
| [character/](../character/) | Characters can be cards |
| [party/](../party/) | Cards as companions |
| [soul-chat/](../soul-chat/) | Cards can speak |
| [adventure/](../adventure/) | Cards as quest companions |
| [multi-presence/](../multi-presence/) | Same card, many rooms |
| [advertisement/](../advertisement/) | Cards advertise abilities |
| [return-stack/](../return-stack/) | Activation records as continuations |
| [visualizer/](../visualizer/) | Pure state prompt clusters |
| [hero-story/](../hero-story/) | Hero cards invoke traditions |

**Full Spec:** [SKILL.md](SKILL.md)

## Overview

Cards are portable capability tokens you can carry, play, and activate. They're **templates** — put them in play in a [room](../room/) to create live instances.

**Origin:** HyperCard + Magic: The Gathering + Fluxx + K-lines + Hewitt Actors.

## The Card Lineage

Cards are *natural*. The metaphor appears independently across computing history:

### HyperCard (1987)
Bill Atkinson's revolution. Cards and stacks. Navigation by linking. Scripting with HyperTalk.
- Inspired the World Wide Web (Tim Berners-Lee cited it)
- Created the wiki concept
- Launched Myst and countless experiences
- Put programming in hands of artists and designers
- *Deeply embedded in LLM training data*

HyperCard cards have a **front** (visible interface) and **back** (hidden script). MOOLLM cards mirror this: `CARD.yml` is the sniffable interface, `SKILL.md` is the deeper content.

**HyperTalk event handlers ARE our lifecycle hooks:**

| HyperCard | MOOLLM | When |
|-----------|--------|------|
| `on openCard` | `ON-DRAW` | Card enters view |
| `on closeCard` | `ON-DISCARD` | Card leaves |
| `on mouseUp` | `ON-PLAY` | Card activated |
| `on mouseEnter` | `ON-ENTER-HAND` | Card arrives |
| `on mouseLeave` | `ON-LEAVE-HAND` | Card departs |

Same pattern. Same idea. Bill Atkinson figured this out in 1987.

### Magic: The Gathering (1993)
Richard Garfield's collectible card game introduced:
- Cards as portable, tradeable capabilities
- Activation costs and timing
- Stack-based resolution (the "stack")
- Cards that modify other cards

### Fluxx (1996)
Looney Labs' meta-card game where cards change the rules:
- No fixed rules — rules are cards
- Goals change mid-game
- Perfect chaos testing for simulations
- See [experiment/fluxx-chaos/](../experiment/experiments/fluxx-chaos/)

### Why Cards Work

| Property | Benefit |
|----------|---------|
| **Discrete** | Clear boundaries, easy to reason about |
| **Portable** | Can be carried, traded, given |
| **Composable** | Stack, combine, interact |
| **Two-sided** | Interface vs implementation |
| **Collectible** | Build decks, create ensembles |

The same pattern, different eras, all deeply understood by models trained on human knowledge.

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
