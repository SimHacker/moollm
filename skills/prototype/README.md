# 🧬 Prototype

> *"Objects all the way down. No classes. Just clones and delegation."*

## The long chain

At **Xerox PARC** and **Stanford**, **Self** stripped objects down to **slots** and **delegation**—no classes, only networks of concrete things that clone and point upward. That minimal machine turned out to be **universal**: you can **simulate** class tables, **host** **COM**-shaped binary contracts, or sit beside **CLOS**-style generic functions and **Dylan**/**ScriptX**-era multimethod stories without *being* any of them. The **web** inherited the idea when **JavaScript** borrowed prototype chains for the browser. **JSON** became the world’s interchange for object-shaped data; **YAML** added a human layer; **YAML Jazz** (in MOOLLM) adds a **parallel comment channel**—notation, not the same as the Self kernel, but **living on the same files** the agent walks. **MOOLLM** pushes the thread one step further: **directories** are objects, **skills** are **prototypes**, **`PROTOTYPES.yml`** is an ordered parent list, and an **LLM** resolves behavior by **path**—not by dispatching a vtable, but by **following the same delegation story** Self told in the 1980s. The **future** here is not “one winning object system”; it is **one bedrock** (prototype delegation) with **many** hosted disciplines registered honestly beside it—see **[`self` in schemapedia](../schema/schemas/mechanisms/self/README.md)** and **[`SKILL.md`](./SKILL.md)** for the full stack.

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [skill/](../skill/) | Contains Delegation Object Protocol |
| [room/](../room/) | Rooms as prototype instances |
| [container/](../container/) | Containers inherit like prototypes |
| [character/](../character/) | Characters as prototype instances |
| [card/](../card/) | Cards as cloneable capabilities |
| [simulation/](../simulation/) | Abstract → concrete inheritance |
| [constructionism/](../constructionism/) | Learning by cloning and modifying |
| [return-stack/](../return-stack/) | Self's dynamic deoptimization |
| [debugging/](../debugging/) | Stack traces on demand |
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

Created by **David Ungar** and **Randall Smith** at Stanford (1987), continued at Sun Microsystems.

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
