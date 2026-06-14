# MOOLLM Self-ish Objects

Status: Design Vision

---

# Introduction

MOOLLM is heavily influenced by Self, Lisp, Smalltalk, MOO, actor systems, and modern LLM architectures.

The goal is not to reproduce any of these systems.

The goal is to extract their deepest lessons and combine them into a living object system suitable for language models.

---

# Everything Is An Object

In classic object systems:

- files contain objects
- databases contain objects
- programs manipulate objects

In MOOLLM:

everything is already an object.

Examples:

- rooms
- characters
- skills
- documents
- conversations
- K-lines
- repositories
- sessions
- advertisements
- methods
- tools

All are peers.

All can reference one another.

All can participate in activation and context gathering.

---

# Self Instead Of Classes

MOOLLM follows Self more closely than Java.

Objects are primary.

Classes are optional.

Inheritance is replaced by delegation.

```yaml
bugs:
  parent: cartoon-rabbit

cartoon-rabbit:
  parent: rabbit

rabbit:
  parent: mammal
```

Objects acquire behavior by delegation chains.

This maps naturally onto how LLMs already reason.

They do not retrieve a class definition and instantiate it.

They reason by analogy and inheritance of examples.

---

# Living Objects

Objects are not static records.

Objects are active participants in cognition.

A skill can advertise itself.

A room can suggest neighboring rooms.

A character can recommend skills.

A K-line can activate related concepts.

An object can influence its own discoverability.

This makes the object graph partially self-organizing.

---

# Lisp Lessons

Lisp's greatest contribution was not parentheses.

It was the collapse of boundaries.

Code becomes data.

Data becomes code.

Programs can inspect themselves.

Programs can generate programs.

MOOLLM extends this principle.

Skills are data.

Skills are code.

Conversations are data.

Conversations become executable context.

Documentation becomes executable context.

Examples become executable context.

Natural language becomes executable context.

---

# The Self-Hosting Insight

Traditional systems assume:

```text
source code
    ->
compiler
    ->
machine code
```

MOOLLM introduces another layer:

```text
natural language
    ->
context
    ->
behavior
```

The primary executable format is no longer source code.

The primary executable format becomes meaning.

Code remains useful.

Code remains necessary.

But code becomes an optimization rather than the fundamental representation.

---

# Garnet And Amulet: Parallel Trees

Self teaches delegation. **Garnet/Amulet** (Brad Myers, CMU — Don Hopkins worked on Garnet) add **structural inheritance**: when you instance a composite prototype, the system creates a **parallel tree of instanced parts**, not just a flat clone. Constraints bind across the part-owner graph (sibling/owner paths) so the same formulas work on every instance.

That triple — prototype chain, part tree, constraint graph — is the mechanical complement to MOOLLM's Self-ish objects. See [GARNET-AMULET-PROTOTYPE-SYSTEM.md](GARNET-AMULET-PROTOTYPE-SYSTEM.md).

---

# Fragment Config As Copy-Down

Runtime and workspace shapes can use the same prototype grammar as skills:

- small `fragment.yml` files with ordered `parents: []`
- directory-as-package (scripts beside JSON)
- compose at session start; runtime reads flat output

See [PROTOTYPE-FRAGMENT-CONFIG.md](PROTOTYPE-FRAGMENT-CONFIG.md). Garnet/Amulet **copy** slots vs **inherit** slots vs **local** slots map onto compose-time flatten vs runtime overlay. Prior art: Pantomime JSON mixins; fleet VM fragment resolver (private); Amulet slot inheritance modes ([GARNET-AMULET-PROTOTYPE-SYSTEM.md](GARNET-AMULET-PROTOTYPE-SYSTEM.md)).

---

# K-Lines As Prototype Links

K-lines behave similarly to Self slots.

They connect concepts rather than types.

```text
INTROSPECTION
    ->
cursor-mirror
    ->
sqlite-fluency
    ->
thinking-extractor
```

The graph itself becomes part of the runtime.

Objects inherit not only behavior.

Objects inherit relevance.

---

# Progressive Revelation

Objects reveal themselves progressively.

```text
INDEX
    ->
CARD
    ->
SKILL
    ->
README
    ->
Directory
    ->
Implementation
```

No fixed boundary exists between interface and implementation.

The LLM may descend as deeply as necessary.

Every object is potentially inspectable.

---

# Reflection As A First-Class Capability

Most software treats reflection as a debugging feature.

MOOLLM treats reflection as a primitive.

Objects can inspect:

- themselves
- their history
- their relationships
- their activation paths
- their descendants
- their ancestors

This is closer to Lisp, Self, and MOO than to modern application frameworks.

---

# The Long-Term Goal

The long-term goal is a living ecology of objects.

Not a database.

Not a chatbot.

Not a workflow engine.

A cognitive object system.

Objects advertise.

Objects activate.

Objects teach.

Objects remember.

Objects evolve.

Objects help language models think.
