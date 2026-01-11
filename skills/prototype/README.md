# 🧬 Prototype

> *"Objects all the way down. No classes. Just clones and delegation."*

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [skill/](../skill/) | Contains Delegation Object Protocol |
| [character/](../character/) | Characters as prototype instances |
| [card/](../card/) | Cards as cloneable capabilities |
| [constructionism/](../constructionism/) | Learning by cloning and modifying |
| [skill/delegation-object-protocol.md](../skill/delegation-object-protocol.md) | Self-like inheritance |

The philosophy behind Self, JavaScript prototypes, and MOOLLM inheritance.

## The Core Insight

**Classes are blueprints. Prototypes are examples.**

Instead of defining an abstract "Cat class" and instantiating it, you:
1. Create one concrete cat (the prototype)
2. Clone it to make new cats
3. Modify the clone as needed
4. The clone delegates to its prototype for anything it doesn't override

## Why This Matters for MOOLLM

MOOLLM uses prototype-based inheritance everywhere:

| Thing | Prototype | Instance |
|-------|-----------|----------|
| Skill | `skills/room/` | `examples/adventure-4/pub/` |
| Character | `skills/character/` | `characters/bumblewick/` |
| Card | `skills/card/CARD.yml` | `pub/pie-table.yml` |

## The Self Language

Created by **David Ungar** and **Randall Smith** at Xerox PARC (1987), later Stanford and Sun.

Key ideas:
- **Everything is an object** (including methods)
- **No classes** — objects inherit from other objects
- **Slots** — named references that can hold data or code
- **Delegation** — "I don't know, ask my parent"
- **Clone and modify** — the only way to create

> *"Self is a network, not a node."* — David Ungar


## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [skills/](../) |
| 📜 Protocol | [delegation-object-protocol.md](../skill/delegation-object-protocol.md) |
| 🎴 Card | [CARD.yml](./CARD.yml) |

---

*"The best message is no message."* — David Ungar
