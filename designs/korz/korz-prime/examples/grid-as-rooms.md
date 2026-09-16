# Grids are room graphs that got regular

*Part of the [Korz cauldron](../../README.md). **Spectrum: self-contained** — the cast is a cellular
automaton and an adventure game, and you already know both. Structured data and every ⚠️ in
[`grid-as-rooms.yml`](grid-as-rooms.yml).*

**What it teaches:** that the two Korz case studies already named as siblings are the same data
structure at opposite ends of one axis, what the empty middle of that axis contains, and why a tidy
unification has to pay a bill before it's allowed to stand.

## The two case studies were always one

[`case-zork.md`](../../case-zork.md) works out symmetric dispatch over five frozen dimensions in an
irregular graph of hand-authored rooms. [`case-cellular-automata.md`](../../case-cellular-automata.md)
works out the same dispatch where every guard is decidable and every dimension is frozen. It closes
by calling the two siblings, which is right and stops one step short:

> A cellular automaton and an adventure map are the same data structure at opposite ends of one
> axis, and the axis is **regularity of the exit wiring**.

At the CA end, every node has identical exits wired by a formula — so implicit that nobody calls it
a graph. At the Zork end, every node has exits placed by an author, and the wiring *is* the content.
The middle is empty, and that's where the interesting systems live.

This isn't an analogy someone had to build, either. The vocabulary already collided: **`c`, `n`,
`s`, `e`, `w`, `ne`, `nw`, `se`, `sw`** is simultaneously a Moore neighborhood, a RISCA opcode set,
an eight-item pie menu, and an adventure game's exit list. Zork adds up, down, in, out — so a 3-D CA
is a room graph with an up staircase, and **the neighborhood former is an exit table.**

## What the room model buys the automaton

**Topology stops being a switch statement.** Torus, Klein bottle, projective plane, sphere,
hyperbolic tiling — each is just a different exit wiring. The `topology` dimension that
[`layered-rules.yml`](layered-rules.yml) declares once and shares between grid, tool, and knob turns
out to *be* the exit table, rather than a parameter with special cases hiding behind it.

**Non-reciprocal exits.** A lists B as a neighbor; B doesn't list A. Every CA engine assumes
reciprocity, and Zork's twisty little passages never did. Information then flows one way, which
buys diodes, ratchets, and one-way membranes — structures you cannot build on a symmetric lattice.
It also breaks something: the interference graph becomes **directed**, so the conflict-coloring
machinery needs a directed version, and ⚠️ it's worth checking whether the (r+1)^d coloring argument
survives at all.

**Portals.** An exit that leads somewhere far away is a long-range connection, and a lattice plus a
few random long edges is a **small-world network** — where synchronization, spreading, and mixing
time all shift qualitatively (⚠️ Watts–Strogatz; verify before printing specifics). So a magic word
in an adventure game is a rewiring experiment with a literature behind it, and the rewiring
probability is a single knob that traverses the entire regularity axis from pure lattice to random
graph.

**Exits as data.** Make the exit table a *plane* and the wiring becomes editable by rules and by
hand. That generalizes moveable RISCA directly: the direction field names an exit, so
[a turtle walks a graph](../../../cellular-automata/schedulers.md) instead of a grid. And you get
self-modifying space — a CA that rewires its own connectivity, which is the honest version of what
"programs are painted" was reaching toward.

**Rooms contain things.** An adventure room holds objects and state; a cell holds bits. Same slot,
different budget. The useful end of that is a room whose contents are an entire sub-grid running its
own rules — hierarchical CA, and exactly the meta-iterator's "a particle can be an engine."

## What the automaton gives back

The arrow has to point both ways or the unification isn't real, and it does.

**Schedulers.** Zork has exactly one: turn-based, with daemons and fuses. `case-zork.md` already
notes that daemons and fuses become slots guarded on a time dimension — and the priority-queue
policy in [`schedulers.yml`](../../../cellular-automata/schedulers.yml) *is* a fuse queue. So an adventure
engine inherits the whole palette: asynchronous rooms, event windows, rooms that tick while you're
somewhere else.

**Measurement.** The domain-wall and compression instruments
apply to a room graph too — which regions of a game world are predictable, and which carry
structure.

One asymmetry worth admitting: the CA side is the one with a compiler, and the adventure side is the
one with forty-five years of players as an oracle.

## The representation, which already agrees with the argument

The form is a layer that **points to a shape** and carries **an array of dicts**:

```json
{ "shape": "<ref>", "cells": [ {...}, {...}, ... ] }
```

(⚠️ Provenance unclear — this is either shipped code not yet located or the proposal. Worth settling
before it's cited as existing.)

The split is the thesis. `shape` is the connectivity — the exit table, shared by reference. `cells`
is the contents. And **a lattice and a room graph differ only in what `shape` says**, with the cell
array byte-identical in both. When shape reads "2-D torus, 256×256" the exit table is formulaic and
the compiler specializes back to fixed offsets; when it's an explicit adjacency list you have rooms;
when it's formulaic *plus an exception list* you have portals, which is the specialize-back story
with a small table beside it. The unification doesn't have to be argued into the representation —
it's already the representation's natural shape.

**Two different shapes are hiding in one word,** and they get specialized by different machinery:
the *layer's* shape (connectivity between sites) and a *cell's* shape (the set of keys its dict
carries). Call the second one the cell's **archetype**, borrowing the games-industry term, so they
stop colliding.

**"Points to the shape" makes shape a prototype** — one object, many layers referencing it, Self and
Korz semantics of shared structure with per-instance state. Which has a concrete consequence:
**layers that share a shape are register-compatible and can be cross-wired.** Shape sharing isn't a
storage optimization, it's what makes the layer bus — the ganged CAM-6 cards — well-typed. The
hazard on the other side is that editing a shared shape rewires everything pointing at it, which
wants to be deliberate.

### The trap: array-of-dicts is an authoring format

It's the right *source* representation and the wrong *runtime* one. Hand-editable, diffable, sparse,
heterogeneous, readable by all three audiences — and completely wrong for a shader, which wants one
tightly packed typed array per field.

That transform has a name and this repo already specified its output: **AoS to SoA, where "one typed
array per field" is exactly the plane algebra** in [`layered-rules.md`](layered-rules.md). The planes
*are* the compiled form of the cell dicts. Which makes this the same pattern as everything else here
— declarative source, specialized runtime, compiler in between. Rules to tables, Korz to WGSL, dicts
to planes.

The mature vocabulary for the heterogeneous-versus-packed problem is **ECS**: components stored as
arrays, entities as indices, systems iterating over archetypes. The games industry solved this and
named it; borrowing beats reinventing. The compiler's choice then falls out — dense and homogeneous
cells become planes; sparse or heterogeneous rooms become archetype tables; and the common mixed
case packs the shared fields into planes and keeps the rare ones in a side table.

One rule to hold the line: **JSON must not become canonical.** It has no comments, and in this repo
comments are semantic data, so a round trip through JSON silently deletes meaning. yaml-jazz is the
source of truth and JSON is a lossy export for the wire and the runtime — never source → JSON →
source.

## The bill

A tidy unification shouldn't be allowed to quietly delete the performance story, so: **regularity
was buying six things** — fixed-offset addressing, table indexing, tiling, space-filling curves, GPU
coalescing, and static conflict coloring. An arbitrary graph destroys all six. There's no lattice to
skew, no Morton index, no (r+1)^d coloring.

So grid-as-rooms is a **semantic** unification and not an implementation strategy, and it's only
allowed to stand if the compiler **specializes back**: recognize a uniform exit table and emit the
lattice code with fixed offsets; recognize uniform-plus-a-few-portals and emit lattice code with an
exception list. That's [partial
evaluation](../../../cellular-automata/cam-construction-set.md#the-move-has-a-name-partial-evaluation-and-one-more-thing)
again, applied to connectivity rather than to rules.

The acceptance test is strict, and it should be: **if the uniform case doesn't compile to exactly
the code the lattice engine would have emitted, the unification cost something and should be
rejected.**

## See also

- [`../case-zork.md`](../../case-zork.md) — the irregular end, and where the five frozen dimensions come from
- [`../case-cellular-automata.md`](../../case-cellular-automata.md) — the regular end
- [`margolus-rules.md`](margolus-rules.md) — the rules that run on the lattice this generalizes
- [`layered-rules.md`](layered-rules.md) — where `topology` is declared once for grid, tool, and knob
- [`schedulers.md`](../../../cellular-automata/schedulers.md) — the menagerie whose nine names are exit names, and the fuse queue Zork already had
