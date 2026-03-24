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
4. The clone delegates upward for anything it doesn't override—but **to whom?** Not necessarily a single parent.

**Self (the language) is not JavaScript:** a Self object can delegate to **several** **parents** at once—**multiple prototypes** in an **ordered** chain (whatever you want to call them: parents, supers, traits, mix-ins, “classes” simulated on top—**more than one slot**). **JavaScript** (in the usual story) gives each object **one** internal `[[Prototype]]` link; **multiple inheritance** there is awkward, faked, or library-shaped. **Self** made **multi-parent delegation** a **first-class** capability. **MOOLLM** mirrors that: **`PROTOTYPES.yml`** lists **many** parent skills in order—**first match wins** across **all** of them.

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
- **Delegation** — "I don't know, ask my parent**s**" (yes, **plural**—**multiple** prototype links, ordered)
- **Clone and modify** — the only way to create

## Navigation

| Direction | Destination |
|-----------|-------------|
| ⬆️ Up | [skills/](../) |
| 📜 Protocol | [delegation-object-protocol.md](../skill/delegation-object-protocol.md) |
| 🎴 Card | [CARD.yml](./CARD.yml) |

---

## Real quotes (primary sources)

**Ungar & Smith — *Self: The Power of Simplicity*** (OOPSLA ’87; also *Lisp and Symbolic Computation* 4(3), June 1991). From the **abstract**:

> *Self is an object-oriented language for exploratory programming based on a small number of simple and concrete ideas: prototypes, slots, and behavior.*

[Bibliography](http://bibliography.selflanguage.org/self-power.html) · [PDF](http://bibliography.selflanguage.org/_static/self-power.pdf)

**Smith & Ungar — *Programming as an Experience: The Inspiration for Self*** (ECOOP ’95, Aarhus). From the **abstract**:

> *The language semantics embed the programmer in a uniform world of simple objects that can be modified without appealing to definitions of abstractions.*

> *Although we see areas that fall short of the vision, on the whole, the language, interface, and implementation conspire so that the Self programmer lives and acts in a consistent and malleable world of objects.*

[Bibliography](http://bibliography.selflanguage.org/programming-as-experience.html) · [PDF](http://bibliography.selflanguage.org/_static/programming-as-experience.pdf)

**Pavel Curtis — *LambdaMOO Programmer’s Manual*** (March 1997; for LambdaMOO 1.8.0p6). From the **Introduction** (object-oriented programming as the medium of a shared world):

> *LambdaMOO is a network-accessible, multi-user, programmable, interactive system well-suited to the construction of text-based adventure games, conferencing systems, and other collaborative software.*

> *The database contains representations of all the objects in the virtual reality, including the MOO programs that the server executes to give those objects their specific behaviors.*

> *Thus, programming in the MOO language is a central part of making non-trivial extensions to the database and thus, the virtual reality.*

From **MOO value types** / objects:

> *Objects are the backbone of the MOO database and, as such, deserve a great deal of discussion…*

[LambdaMOO Programmer's Manual](https://www.hayseed.net/MOO/manuals/ProgrammersManual.html) (same text as other mirrors of the canonical manual).

**Self and LambdaMOO** are different mechanisms (prototype language vs. networked MOO object database), but they share a **PARC-era** thread: **objects** as the center of a **programmable** **reality**—Self’s **malleable world of objects** and LambdaMOO’s **virtual reality** made of **objects** and **verbs**.
