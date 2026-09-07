---
name: stone
description: "The one-page tier: distill a whole system onto a single dense legible page whose star is the relationships"
license: MIT
tier: 1
protocol: STONE
allowed-tools: []
related: [card, prototype, moollm, design-sense, yaml-jazz, representation-ethics]
tags: [moollm, one-page, resolution-tier, documentation, diagram, prototype, design]
credits:
  - "Stone Librande — one-page designs (GDC); this skill is named for him and imitates them by being one"
  - "Will Wright — make the complex graspable without oversimplifying"
  - "Chaim Gingold — reverse-diagram lineage"
moollm:
  seed: examples/STONE.md
  defined_by: instance
---

# STONE

> **"If you only read one page, read this one."**

## Read the seed first

This file is not the authority. [`examples/STONE.md`](examples/STONE.md) is.

That file is three things at once: a STONE (its subject is Stone Librande), the
tribute page it needs to be to earn the name, and **the prototype every other
STONE clones.** The protocol below was *read off* that instance rather than
imposed on it, which is the [`prototype`](../prototype/) way — instance precedes
class. If this file and the seed ever disagree, the seed wins and this file is
stale.

So the shortest possible use of this skill is: **open the seed, copy it, swap the
subject.** Everything below is commentary on what you will find there.

## Why the tier exists

Stone Librande's question is the whole argument:

> 💬 "Why create a document with more than one page if most people only read the
> first page anyway?" — Stone Librande

And its companion, which is the part people skip:

> 💬 "Diagrams make relationships visible. Words make them invisible." — Stone Librande

MOOLLM already had tiers above and below this one. A `GLANCE` answers *is this
relevant*; a `CARD` answers *what can it do*; a `README` answers *why was it
built* and is read by almost nobody. The gap was the page you would keep if you
could keep only one — dense enough to be the real thing, short enough to
actually get read.

`GLANCE` → `CARD` → `DESCRIPTION` → **`STONE`** → `README` → directory

**Lower tiers tease; the README sprawls; the STONE is the keeper.**

## The four properties

A file is a STONE when it has all four. Three out of four is a nice document
with the wrong name.

| Property | The test |
|---|---|
| **One page** | You stopped. Denser than a DESCRIPTION, shorter than a README. |
| **Relationships are the star** | There is an actual arrows block, not prose that mentions connections. |
| **Made from understanding** | You could not have drawn those arrows without knowing the system. |
| **The read-one-page view** | If every other tier were deleted, this one would still serve. |

### One page means stopping

The hard property, because every other one is additive and this one is
subtractive. The page is finished when the next true sentence would push it to
two pages and you leave that sentence out. **A two-page STONE is a README with a
haircut.**

What makes this affordable rather than lossy is that the other tiers exist. You
are not throwing the detail away, you are putting it where it belongs and
linking to it. A STONE that tries to be complete has misunderstood which
document it is.

### The arrows are structural, not decorative

"X influenced Y" inside a paragraph is invisible; the reader has to assemble the
graph in their head and mostly will not. A relationships block hands them the
graph. From the seed:

```
Will Wright ──"make the complex graspable, don't oversimplify"──▶┐
Chaim Gingold ──reverse-diagram lineage─────────────────────────▶┤
                                              🪨 Stone Librande ──┤── one-page designs
                                                                  ├──▶ Don Hopkins — one-page UIs & control panels for Micropolis
                                                                  └──▶ STONE — this very skill / resolution tier (named for him)
```

Label the edges. An unlabeled arrow asserts that a relationship exists while
concealing what it is, which is the prose failure in ASCII form.

### Earned, which is why it cannot be faked

You cannot draw a correct arrows block for a system you have not understood.
This is the property that makes the tier trustworthy: a STONE is **evidence of
comprehension**, not merely a claim of it. It is also why "summarize this to one
page" is the wrong instruction to give yourself — summarizing what you do not
understand produces a legible lie, which is worse than sprawl because it reads
as authoritative.

## Making one

```
STONE [subject]
  1. CLONE examples/STONE.md beside the subject
  2. set parents: [ moollm://…/skills/stone/examples/STONE.md ]
  3. ARROWS  — draw the relationships block first, before the prose
  4. write the page around the arrows
  5. AUDIT   — check the four properties; cut until one page is true
```

**Draw the arrows before writing the prose.** Doing it in that order surfaces
what you do not yet understand while it is still cheap to go find out. Doing it
in the other order produces prose that gets diagrammed, which is decoration.

Front matter carries `is_a`, `parents`, and — when the subject is a real person
— `representation:` with a consent level per
[`representation-ethics`](../representation-ethics/). The seed demonstrates all
of it.

## The prototype clause

The seed **governs by example, not by decree.** Improve the seed and every clone
inherits the improvement; the rules in this file are a description of what the
seed does, so improving the seed makes this file wrong rather than making the
clone wrong. That is the intended direction of authority.

Practically: if you find a better way to lay out a STONE, change
`examples/STONE.md` and update this file to match. Do not add a rule here that
the seed does not demonstrate.

## Ornament

Density is not permission to decorate. A STONE runs against
[`no-decorative-comments`](../../.cursorrules) like everything else — no rules of
repeated dashes, no visual filler. But the tier is also the one place where
earned ornament pays: emoji as rungs, an arrows block that is pleasant to look
at, a quote placed where it lands. Clear the ground first; then what you add is
legible against it.

## Methods

| Method | Signature | Does |
|---|---|---|
| `STONE` | `STONE [subject]` | Full pipeline: clone, arrows, page, audit |
| `CLONE` | `CLONE [seed] FOR [subject]` | Copy the seed and reparent it |
| `AUDIT` | `AUDIT [file]` | Report which of the four properties fail |
| `ARROWS` | `ARROWS [subject]` | The relationships block alone |
| `LADDER` | `LADDER [file]` | Recommend a resolution tier for a document |

`LADDER` is the one that gets used most and it usually answers *not a STONE*.
Most documents want a `CARD`. The tier is for systems whose relationships are
the interesting part.

## Part of MOOLLM

A skill in [MOOLLM](../../README.md) — see [`skills/`](../README.md) for the
ecosystem. The tier sits inside the semantic pyramid described in the repo root
rules; its nearest neighbour with a skill of its own is [`card`](../card/), one
rung down. `GLANCE.yml` is a file convention rather than a skill.
