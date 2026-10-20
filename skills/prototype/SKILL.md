---
name: prototype
description: "MOOLLM's object model: objects delegate to parents listed in inherits:, Self-style, with no classes. How to declare parents, how lookup resolves a slot, and resolve.py to check it."
license: MIT
tier: 1
allowed-tools: [read_file, run_terminal_cmd]
permissions: [read, terminal]
related: [skill, room, container, character, card, glance, simulation, constructionism, return-stack, debugging]
benefits_from:
  - { skill: yaml-jazz, why: "a comment on an inherits: line says which aspect is inherited" }
  - { skill: k-lines, why: "a K-line in inherits: is a latent parent the model already knows" }
tags: [moollm, inheritance, self, delegation, clone, lookup]
protocol: PROTOTYPE
credits:
  - "David Ungar and Randall Smith: Self (1987), slots, parent slots, multiple parents"
  - "Henry Lieberman: delegation as the alternative to classes (1986)"
  - "Pavel Curtis: LambdaMOO, parented objects in a shared world"
  - "Brendan Eich: JavaScript prototypes (one parent per object)"
---

# PROTOTYPE

> **"Objects all the way down."**

Part of MOOLLM · [This skill's directory](https://github.com/SimHacker/moollm/tree/main/skills/prototype)

MOOLLM has no classes. Every object is concrete: a directory, a file, or a map inside a file.
An object that lacks a slot asks its parents, in order, and the first one that has it answers.
That's Self's model, applied to a filesystem an LLM walks.

## Self in one page

A Self object is a set of **slots**. Some hold data, some hold code, and some, marked with `*`,
are **parent slots**:

```
cat: (|
  name <- "Terpie".
  meow = (| | "Meow!" |).
  traits* = catTraits.
|)
```

Sending `meow` looks in the object's own slots, then in each parent, then in their parents.
First match wins. There can be several parent slots, and they can be reassigned at run time,
so an object can change what it is by pointing a parent somewhere else. New objects are made by
cloning an existing one and changing what differs. Classes, mixins, traits and generic
functions can all be built from this; none of them is needed to start.

The schemapedia describes Self as a mechanism ([`self`](../schema/schemas/mechanisms/self/README.md)); this skill's CARD inherits from it.

MOOLLM keeps that model and changes the storage: slots are YAML keys and files, objects are
directories, and lookup is something both a script and an LLM can do by following paths.

## Objects

| Object | Address | Slots |
|---|---|---|
| directory | `examples/adventure-4/pub` | the top-level keys of its interface files, merged, plus its files and subdirectories |
| file | `examples/adventure-4/maze/grue.yml` | its top-level keys |
| embedded | `garden/ROOM.yml#objects.bench` | the keys of that map |

Files are flat: slots at the top level, no wrapper key repeating the filename (`room:` inside
ROOM.yml) and no `object:` envelope. An UPPERCASE file (`ROOM.yml`, `CHARACTER.yml`, `RUN.yml`)
is an **interface**: it holds the slots that belong to that role, and a directory has as many
interfaces as it has interface files. A data slot must not share a name with a child directory.

## Declaring parents

```yaml
inherits:
  - skills/animal                     # repo path
  - ../characters/fictional/grue      # relative path
  - real-being                        # bare id: nearest skills/<id>, characters/<id>, ...
  - EDITH-BUNKER                      # K-line: latent, the model knows it
  - "Garfield, the comic-strip cat"   # prose: latent
  - aisle-e/PROTOTYPES.yml#prototypes.wine-rack   # an embedded object
  - { ref: skills/cat, gets: [PAT, FEED], overrides: [PAT], why: "a cat with opinions" }
  - { ref: EDITH-BUNKER, but: "Dutch, and forty years younger" }
traits*: skills/cat                   # named parent: a role that can be reassigned
mood*: moods/sleepy
```

`inherits:` is a list, most specific first. An entry is a reference string, or a map with
`ref:` and clauses:

| Clause | Means | Read by |
|---|---|---|
| a comment on the line | which aspect is inherited | the LLM |
| `why:` | the same, as data | the LLM, reports |
| `gets:` / `overrides:` / `except:` | methods taken from this parent, redefined here, refused | the LLM; no script checks them yet |
| `but:` | how this object differs from a latent parent | the LLM |
| `as:` | a role name; same as writing `role*: ref` | lookup |

A key ending in `*` is a **named parent**, Self's parent slot. Use one when the parent is a role
that changes (a mood, a costume, a current owner), so it can be reassigned without touching the
others. Named parents come after `inherits:` in lookup order, in the order they're written.

A reference that names no file is **latent**: the model's own knowledge stands in for the
file. That is legitimate for K-lines and prose. A path-shaped reference that names no file is
a broken link.

**Implied parents.** An interface file implies the skill its name names: `ROOM.yml` implies
`room`, `RUN.yml` implies `run`. The skill is looked up in enclosing scopes first, so an
experiment can own `experiment/skills/run/` and its runs inherit it before any repo-wide one.
If no scope defines it, the parent is the latent K-line `RUN` until somebody writes the skill.
An embedded object implies the skill of its collection key (`objects:` → `object`, `exits:` →
`exit`). Implied parents come last, because they're the most generic.

## Lookup

1. The object's own slots.
2. Each declared parent in order (`inherits:`, then named parents), depth-first.
3. `defaults:` of enclosing containers, nearest first (see Containers).
4. Implied parents, the most generic.
5. First match wins. A cycle is skipped and reported.
6. A dotted slot (`stomach.contents`) descends through maps and into child objects.
7. If two unrelated parents both define the slot, the first wins and `lookup --all` flags it,
   because Self 4 would call it ambiguous.

`state:` is never inherited. Each object keeps its own.

## Views

`GLANCE.yml`, `CARD.yml` and `INDEX.yml` summarize the object whose directory they sit in. Each
has two implied named parents:

```yaml
format*: glance    # the view skill: skills/glance, or the latent GLANCE until it exists
subject*: ..       # the directory it summarizes
```

A view that lacks a slot falls through to its subject, so reading GLANCE, then CARD, then the
object is one delegation chain. A view is a cache; git says when it's stale (`resolve.py stale`).

## Embedded objects and catalogs

```yaml
# garden/ROOM.yml
objects:              # a map keyed by id: garden/ROOM.yml#objects.bench
  bench:
    description: Worn oak, carved initials.
  gnome:
    inherits: [../cat]
```

Collections are maps keyed by id, so a child can override one entry by name; lists are for
order, and each item has an `id:`. An embedded object that grows moves into its own directory
without changing any lookup result.

A `PROTOTYPES.yml` is a **catalog**: a map of objects meant to be cloned (the Leela storage
aisles). It is not a parent list. To clone an entry, write a new object that inherits from it
and states only what differs:

```yaml
# pub/basement/wine-rack.yml
inherits:
  - "street/lane-neverending/leela-manufacturing/storage/aisle-e/PROTOTYPES.yml#*.wine-rack"
name: "Cobwebbed Wine Rack"
capacity: 24          # bottles
```

`#*.wine-rack` means the entry `wine-rack` in whichever collection of that file has it. This
is delegation, not Self's copy-on-clone: the instance keeps tracking its prototype, and its own
slots are its differences.

## Containers

A `CONTAINER.yml` passes values down to everything inside it:

```yaml
defaults:
  room:
    lighting: 0      # pitch black; whether a grue hunts is the grue's call
```

This is a cascade, not a parent. `defaults:` is keyed by what the child is (`room`,
`character`, `object` for a plain file). An object's own slots and declared parents win over
its containers' defaults; the defaults win over its implied skill. Across nested containers,
maps deep-merge, lists concatenate, and the nearest scalar wins. `resolve.py lookup` applies
it; the [container](../container/SKILL.md) skill has the details.

## Not parents

| Concept | Key |
|---|---|
| names that activate it | `k_lines:` |
| navigation | `related:`, `see_also:` |
| intellectual ancestry | `lineage:` |
| classification | `tags:`, `type:` |
| where it is | its directory |

A room is not a child of the room that contains it in the delegation sense; containment is
the directory. Writing `inherits: [../]` would make every sub-room inherit its container's
description.

## Older spellings

Readers accept these; writers emit `inherits:`. `resolve.py lint --strict` counts them.

| Older | Write |
|---|---|
| `parents:`, `parent:`, `extends:`, `prototype: <ref>`, `meta.inherits:` | `inherits:` |
| `prototype: {source: FILE, id: X}` | `inherits: ["FILE#*.X"]` |
| `inherits: {key: value}` (values, not parents) | plain slots, or `defaults:` on a container |
| `room:` / `card:` / `character:` / `object:` wrappers | flat |
| `moollm/skills/x` | `skills/x` |

## Two tiers

Lookup runs at two levels. **`scripts/resolve.py`** is the deterministic tier: it follows
files, reports which parent answered, and lists the latent parents it couldn't follow. The
**LLM** is the other tier: it reads the same chain, and where the chain reaches a K-line or a
prose parent, it answers from what it knows about that name, modulated by `but:` and comments.

```bash
python3 skills/prototype/scripts/resolve.py lookup  <object> <slot> [--all]
python3 skills/prototype/scripts/resolve.py parents <object>
python3 skills/prototype/scripts/resolve.py lint    [paths] [--strict] [-v]
python3 skills/prototype/scripts/resolve.py stale   [paths]
python3 skills/prototype/scripts/flatten.py <paths> [--name ROOM.yml] [--write]
```

`examples/lookup/` is a small object graph covering own slots, multiple and named parents,
latent parents, cycles, implied scoped skills, views and embedded objects; its README lists
each lookup and why it resolves the way it does.

## Methods

| Method | Does |
|---|---|
| EXPLAIN | Explain delegation to someone, from objects in front of them |
| DESIGN | Choose parents for a new object: what it inherits, what it overrides, what is latent |
| TRACE | Walk a lookup (`resolve.py lookup --all`) and say which parent answered and why |
| LINT | Run `resolve.py lint`; fix broken references and older spellings |
| COMPARE | Show a design as classes and as prototypes, and what each costs |

## History

| Year | Event |
|---|---|
| 1986 | Lieberman, "Using Prototypical Objects to Implement Shared Behavior" |
| 1986 | Ungar and Smith begin Self at Xerox PARC |
| 1987 | *Self: The Power of Simplicity*, OOPSLA |
| 1990 | LambdaMOO: parented objects, inherited properties and verbs |
| 1995 | JavaScript: prototype chains, one parent per object |
| 2008 | Yegge, "The Universal Design Pattern": property lists with parent links |
| 2024 | MOOLLM: directories as objects, delegation an LLM can follow |

## Further reading

- Ungar, D. & Smith, R. (1987). *Self: The Power of Simplicity*. [bibliography](http://bibliography.selflanguage.org/self-power.html), [PDF](http://bibliography.selflanguage.org/_static/self-power.pdf)
- Smith, R. B. & Ungar, D. (1995). *Programming as an Experience: The Inspiration for Self*. [bibliography](http://bibliography.selflanguage.org/programming-as-experience.html), [PDF](http://bibliography.selflanguage.org/_static/programming-as-experience.pdf)
- Lieberman, H. (1986). *Using Prototypical Objects to Implement Shared Behavior in Object-Oriented Systems*. OOPSLA '86.
- Yegge, S. (2008). [*The Universal Design Pattern*](http://steve-yegge.blogspot.com/2008/10/universal-design-pattern.html)
- Curtis, P. (1997). [*LambdaMOO Programmer's Manual*](https://www.hayseed.net/MOO/manuals/ProgrammersManual.html)
- [designs/object-system/SCHEMA.md](../../designs/object-system/SCHEMA.md): the same model as a design record, with the usage counts behind each choice in VOCABULARY-CLUSTERS.md

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/prototype/](https://github.com/SimHacker/moollm/tree/main/skills/prototype)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
