# Snap! — first-class everything

**Go there:** [snap.berkeley.edu](https://snap.berkeley.edu/about) ·
[Snap! source](https://github.com/jmoenig/Snap) ·
[BJC](https://bjc.berkeley.edu/)

---

## The hook

Snap! extends Scratch-class accessibility with Scheme-class power: first-class **lists**,
**procedures**, AND **continuations** — enough to build the [Y combinator](y-combinator-in-blocks.md)
out of blocks — plus prototype-based objects. Brian's design input and documentation keep it
teachable; Jens's [Morphic.js](morphic-js.md) implementation keeps it live in the browser with no install.

## What "first-class" means here

| Feature | Scratch-class | Snap! addition |
|---------|---------------|----------------|
| Lists | Fixed primitives | **First-class lists** — data structures you pass and return |
| Procedures | Fixed blocks only | **Build Your Own Blocks** — user-defined reporters & commands |
| Control flow | Limited | **Continuations** — `call w/continuation`, pause/resume stories |
| Objects | Sprites only | **Prototype-based** objects inside the blocks world |
| Environment | Closed IDE | **Morphic.js** — malleable live substrate |

Former name: **BYOB** (Build Your Own Blocks) — the rename to Snap! signaled Scheme-class ambition
without abandoning beginners.

## Why Don cares

Don's 2018 thread with Brian and Jens assumed learners should *reprogram the simulator they're
studying* — Micropolis, CAM6, modifiable simulators. Snap! is the blocks language honest enough
to carry that constructionist bet. See
Micropolis × Snap! (Jens angle).

## Show hooks

- **First-class everything live** — build the Y combinator on air.
- **How far blocks go without losing beginners** — Jens's design answer.
- **Pair with Brian** — pedagogy (books) meets implementation (Snap!).

## Deeper links

| Topic | Where |
|-------|--------|
| Y combinator stunt | [y-combinator-in-blocks.md](y-combinator-in-blocks.md) |
| Rings, macros, AST | [Brian's macros digest](snap-macros-metaprogramming.md) |
| BJC curriculum | [Brian's BJC digest](logo-and-cs-education/beauty-and-joy-of-computing.md) |
| Morphic.js | [morphic-js.md](morphic-js.md) |
| Micropolis integration | micropolis-snap-2018.md |
| Pair show | snap-logo-brian-jens |

↑ [Snap! index](README.md)
