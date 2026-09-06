# A Fitts' Law optimizer

**Once the cursor is virtual, the terms of Fitts' law stop being constraints and become control
variables.** That is the sentence this whole cluster has been circling.

$$MT = a + b\log_2\!\left(\frac{2D}{W}\right)$$

Movement time depends on distance to the target and the target's width. In pixel space both are
fixed: the button is where it is and as big as it is. In **motor space** — the space the hand
actually moves through, which a drawn cursor and a transfer function jointly define — both are free.
Every mechanism in this cluster turns out to be a term in that expression.

The lens version of the law, with the CHI '88 receipt and Tog's menu bar, is
[`skills/design-sense/lenses/fitts.md`](../../skills/design-sense/lenses/fitts.md). This document is
the *active* version: not "obey the law" but **operate it**.

## Every mechanism here is a term

| Mechanism | Term it moves | How |
|---|---|---|
| **Warping** | `D → 0` | Put the pointer on the target. Browsers refuse this, which is why the cursor must be drawn — see [FRICTION-FIELDS.md](FRICTION-FIELDS.md) |
| **Pie menu** | `D` small and constant; `W` grows with radius | Direction replaces travel; further out is *more* forgiving, not less |
| **Screen or window edge** | `W → ∞` in one axis | You cannot overshoot it. Corners are infinite in two |
| **Friction strip / detent** | `W` wide in motor space, unchanged in pixels | Motion zeroes near the value, so a one-pixel target acquires like a fat one |
| **Precision damping** | `W` magnified locally | Reduce gain and the same hand motion covers fewer pixels; the target grows under the hand |
| **Groove or dock** | `W → ∞` along the line | [GROOVES-AND-SPIKES.md](GROOVES-AND-SPIKES.md) already says it: drawing a groove draws a Fitts wall |
| **Snap-dragging** | `W` per construction | Gravity toward meaningful geometry rather than toward pixels |
| **Multiple cursors** | `D → 0` without any warp | The nearest parked cursor acts. Cheapest optimization available |
| **Vehicle** | changes the metric itself | When you must tack against the wind, distance is no longer Euclidean and `D` is the wrong variable |

Two of those are worth stating as the general moves. **The target can come to the pointer** — Fitts
assumes a stationary target and nothing requires it. And **the pointer can go to the target** — which
is warping, and is the reason the virtual cursor is load-bearing rather than decorative.

## This is a real literature, and it should be cited rather than reinvented

| Work | Contribution |
|---|---|
| **Semantic pointing** — Blanch, Guiard, Beaudouin-Lafon, CHI 2004 | The canonical formulation: decouple motor space from visual space and give important targets more motor space than pixels. Our friction strips are this, arrived at from the snap-dragging side |
| **Bubble cursor** — Grossman & Balakrishnan, CHI 2005 | Dynamically resize the cursor's activation area to capture the nearest target; Voronoi partition means *no empty space at all*, and it is provably optimal in that sense |
| **Area cursors** — Kabbash & Buxton, CHI 1995 | The cursor as a region rather than a point |
| **Sticky icons** — Worden et al., CHI 1997 | Gain reduction over targets, motivated by older adults; the accessibility case for the same trick |
| **Snap-dragging** — Bier & Stone, SIGGRAPH 1986 | Gravity toward constructed geometry, which is where the `W → ∞` groove comes from |
| **Pie menus** — Callahan, Hopkins, Weiser, Shneiderman, CHI 1988 | 15% faster with fewer errors: the radial claim, measured |

The distinctive thing left to do is not another gain trick. It is **giving the optimizer an objective
and a target list**, which is where this stops being a bag of interaction hacks.

## What makes it an optimizer: it needs to know the targets, and it can

A gain curve tuned by hand is a trick. An optimizer needs to know **what the targets are and which
ones matter**, and this design already has both, from two directions:

- **The build knows the geometry.** Motor-space warps can be precomputed per context at compile time,
  the same move as the tagsonomy compiler — the expensive analysis happens once, the runtime reads a
  table. See [`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md).
- **The LLM can rank the candidates.** Ranked method resolution and Sims-style advertisements already
  produce a likelihood ordering over what you probably want next. Feed that ordering into `W`
  allocation and **likely targets get wider motor space than unlikely ones**, while every target
  stays exactly where it looks. Selker's dwell-time prediction is the same idea with a slower clock,
  and it shipped.

That is the version worth building: **predicted intent as the weighting function of a Fitts
optimizer.** Not "make the button bigger," which changes the layout, but "make the *likely* button
cheaper to hit," which changes nothing you can see.

## Multiple cursors are the cheapest optimizer, and Engelbart got there first

Parking a cursor costs nothing. Switching to it is a single act. So with several cursors resident in
several places, **`D` collapses without any motor-space manipulation at all** — the acquisition
problem is replaced by a selection-among-few problem, which is a pie menu, which is itself the radial
Fitts win. The optimization composes with itself.

The lineage is **Engelbart's NLS**, and the framing that matters is Bret Victor's. The 1968 demo
included a live shared-screen session with a colleague thirty miles away, both parties working in the
same document — two cursors, two people, one artifact, in 1968. Victor's argument in *A few words on
Doug Engelbart* (2013) is that reading NLS as an ancestor of present-day systems misses it, because
the collaborative purpose was **constitutive rather than featural**: Engelbart was building a system
for people to solve urgent complex problems *together*, and augmenting collective intelligence was
the point rather than a groupware checkbox screwed onto the side of a personal productivity tool.
*(Paraphrase — verify wording before quoting.)*

Which is the correct reading of multi-cursor here too. Cursors are plural because a corpus is worked
on by several parties — including agents — not because multiplayer is a feature to add later. The
body-plan argument is in [READING-CURSORS.md](../webtop/READING-CURSORS.md); the presence-only
version, shipped and enjoyed, is
[Cursor Camp](../webtop/PLAYABLE-CORPUS.md#cursor-camp-the-whole-model-shipped-for-a-mass-audience-with-no-characters).

## Honest costs

- **Distractors break gain-based tricks.** Semantic pointing degrades when the path to the target
  crosses other targets, each grabbing as you pass. Bubble cursor's Voronoi partition handles this
  and pure gain reduction does not, so a real implementation needs the partition, not just friction.
- **Nulling returns.** Motor and visual space diverging is the mechanism; the cursor drifting from
  where the hand believes it is, is the cost. Buxton's nulling problem, already documented in
  [WINDOW-RESIZE-PIE.md](WINDOW-RESIZE-PIE.md).
- **Never snap ahead of the gesture.** Don's rule, and it is not negotiable: hold the position for a
  distance while relative-dragging, so that every value in between remains selectable. Eager snapping
  makes near-but-not-equal values unreachable, which is a worse failure than a slow acquisition.
- **Speed is not always the objective, and this is the important one.** Fitts measures acquisition
  time. A corpus often wants *deliberation* — a knob that is trivially easy to turn gets turned
  thoughtlessly, which is the badge problem from [`../webtop/SIGNED-ASSESSMENTS.md`](../webtop/SIGNED-ASSESSMENTS.md) expressed
  in the motor channel. So consequential and destructive actions should be optimized **against**:
  deliberately distant, deliberately narrow, deliberately effortful. An optimizer without a signed
  objective just makes everything fast, and *fast* is not the same as *good*.
- **Accessibility is not optional.** Every optimization here is a pointing optimization, so every
  operation it accelerates must also have a discrete named command reachable from the keyboard — the
  invariant in [`../webtop/TREE-NAVIGATION.md`](../webtop/TREE-NAVIGATION.md), where it is a lint
  rather than a taste.

## Related

- [FRICTION-FIELDS.md](FRICTION-FIELDS.md) — transfer functions, vehicles, virtual cursors, the Cursor Camp receipt
- [WINDOW-RESIZE-PIE.md](WINDOW-RESIZE-PIE.md) — the acquisition problem that started it, and the mile-high menu bar generalized
- [GROOVES-AND-SPIKES.md](GROOVES-AND-SPIKES.md) — constraints you can draw, and docking as an infinite-width target
- [`skills/design-sense/lenses/fitts.md`](../../skills/design-sense/lenses/fitts.md) — the lens, with the CHI '88 measurement
- [`skills/design-sense/lenses/foveation.md`](../../skills/design-sense/lenses/foveation.md) — where the eye goes, as against where the hand can cheaply go
- [`../webtop/READING-CURSORS.md`](../webtop/READING-CURSORS.md) — why cursors are plural in the first place

↑ [pie-stack-views](README.md)
