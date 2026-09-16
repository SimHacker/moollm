# Margolus block rules in Korz — designing the engine by its hardest examples

*Part of the [Korz cauldron](../../README.md), and the runnable companion the
[cellular automata case study](../../case-cellular-automata.md) asked for.
**Spectrum: self-contained intro → MOOLLM-integrated.** The mechanics stand alone; the last
section connects to a build in progress.*

**What it teaches:** orbit guards versus point guards, derived coordinates as a second
species of dimension, reversibility as a property of a slot *set*, and why writing the
classic rules first is how you find out what your engine actually has to support.

Guard algebra lives in the companion [`margolus-rules.yml`](margolus-rules.yml). This page
is the argument.

## The cast, briefly

**The Margolus neighborhood** (Norman Margolus, in Toffoli & Margolus's *Cellular Automata
Machines*, MIT Press 1987) partitions a grid into 2×2 **blocks** updated as units, with the
block boundaries shifting by one cell on alternate ticks. Its defining oddity: **a block has
no center.** Four sites go in, four come out, and none of them is the one being updated.
That is what makes reversible, momentum-conserving CA physics possible.

**[Korz](../../README.md)** (David Ungar, Harold Ossher, Doug Kimelman, IBM Research, Onward!
2014) is a language with no objects — only **slots** guarded by **dimensions**, dispatched by
matching a whole **context** symmetrically, with no privileged receiver. The most specific
matching slot runs.

Put those together and the joke tells itself: **a Margolus rule is a Korz send that was
running in silicon in 1987.** No receiver, dispatch on the joint state of everything in the
window, one atomic result. The case study already makes that argument. This page does the
exercise — write the classic rules out as slots, invent a few more, and see what breaks.

## The frame is dimensionally parameterized

Write it for `d` dimensions and the 2D case stops looking special:

- A block is **2^d sites**. It is even, therefore centerless, therefore receiverless. The
  no-privileged-receiver property is a *parity fact*, not a design choice.
- The partition needs **one spatial parity dimension per axis, plus time**: `T`, and `P₁..P_d`.
  In 2D those are the familiar `T`, `V`, `H`. In 3D you add one and everything else stands.
- The block-relative coordinates `C`, `CW`, `CCW`, `OPP` are **derived** — permutations of
  the compass rose indexed by which corner you occupy and which tick it is. This is why
  CAM-6 could run the Margolus neighborhood on plain Moore hardware: it's a change of basis,
  not new silicon.

And one generalization falls straight out of writing it this way: **`T` does not have to be
a parity.** Two alternating offsets is the classic scheme, not the definition. A cycle of `k`
offsets is equally well-formed — that's the invented `escher` rule below, and it turns the
partition schedule into a plugin.

## Two species of derived dimension

The case study flags an open question for David, and this exercise sharpens it into two
clearly distinct things:

- **Aggregates.** Life's `live_neighbors` is a *sum over* dimensions. Population and energy
  are the same species — reduce many coordinates to one.
- **Coordinate transforms.** `CW` is a *permutation of* dimensions, **indexed by other
  dimensions**. Which physical neighbor is clockwise from you depends on your corner and the
  tick.

The second species is strictly more powerful and it's the one Margolus rules run on. If Korz
has only aggregates, none of the rules below can be written without enumerating the phase
cases by hand — which is exactly the boilerplate the neighborhood exists to eliminate.

## Symmetry is declared, not enumerated

Every rule states a **group**, and its guards match **orbits** rather than points. `tron`
doesn't list sixteen block patterns; it says `arrangement: uniform` under `D4`, which is one
equivalence class. `billiard_ball` says `population: 1` under `C4`, which is four patterns
collapsed to one slot.

The important part is that **`E`, the trivial group, has to be available.** `sand` needs it:
gravity is a rule that *refuses* rotational symmetry. If the engine assumes symmetry, the
anisotropic rules can't be expressed; if it assumes no symmetry, every symmetric rule pays a
4× or 8× authoring tax. So the quotient is a parameter, which then means it can also be
**dispatched on** — see `chirality`, where handedness is read from a plane and the rotation
direction becomes data.

## The archetypes, and what each one costs the compiler

The classics aren't a list of rules. They're a **coverage suite** — each one is the simplest
thing that forces a distinct piece of machinery to exist.

| Rule | Archetype | What it forces the engine to support |
|---|---|---|
| `rotate` | the group action itself | nothing — the baseline every other rule deviates from |
| `tron` | degeneracy | orbit guards; and the proof that **reversible ≠ conserving** |
| `billiard_ball` | reversible logic | bijectivity checking, and running a slot set backwards |
| `critters` | reversible without conservation | the same bijection machinery with population *not* invariant |
| `hpp_gas` | conservation laws | invariants as a checkable obligation, not a comment |
| `diffusion` | stochastic dispatch | a **random dimension** — the soft tier's foot in the door |
| `sand` | symmetry breaking | the ability to **decline** the quotient (`group: E`) |
| `dendrite` | absorbing states | non-bijective sets, guards that read another plane, and **delegation** |
| `swap_on_diagonal` | pure permutation | the minimal case — information moves, nothing is made or lost |
| `ising` | energy-guarded | real-valued derived dimensions, and a coordinate from **outside the grid** |

Two of those deserve a second look.

**`dendrite` is the layering archetype.** Diffusion-limited aggregation (the book's §15.7
Margolus-dendrite) isn't written from scratch — it's a rule whose *default case delegates to
`diffusion` underneath it*. Get `defer_to` right and rules compose instead of forking, which
is the difference between a plugin system and a directory of near-duplicates.

**`ising` breaks the closed world.** Its temperature isn't on the grid. It comes from the
environment, which means the strict tier has to accept a coordinate supplied by something
else — a slider, a clock, an audio envelope, a
[Turn Table](../../../cellular-automata/turn-tables.md). That's the seam where a deterministic CA
becomes an instrument you can play, and it's worth noticing that the oldest statistical-
mechanics rule in the set is the one that demands it.

## The invented ones

Made up to force the remaining machinery, on the principle that a made-up rule that exposes a
missing feature is worth more than a faithful one that doesn't.

**`chirality`** — handedness read from a plane, so the rotation direction is per-cell data.
*Forces:* the symmetry group to be dispatchable, not just declarable. Paint a left-handed
region and watch the boundary.

**`recombinase`** — the block permutation is selected by an **opcode stored in the cells**.
*Forces:* a derived coordinate whose source is cell *content*, plus an open bank of emissions
supplied as plugins. This is RISCA meeting Margolus: painted programs that update as atomic
reversible blocks. It is also the closest thing in this set to a Movable Feast Machine atom,
where the atom's type selects its behavior.

**`tollbooth`** — a permission plane gates transport across block boundaries. *Forces:*
guards over **layers** rather than sites, which turns the layer stack into part of the
dispatch context.

**`escher`** — `k` partition offsets in a cycle rather than two. *Forces:* `T`'s arity to be
a parameter, and reversibility to be re-derived per schedule. This is the sharpest available
demonstration that **iteration order is part of the rule**, not an implementation detail.

## Why write these before the engine

Because the union of what they demand *is* the specification:

orbit guards · derived coordinates as permutations · bijectivity checking · invariant
checking · a stochastic dimension · real-valued guards fed from outside · delegation between
layered rules · an open emission bank · a parameterized partition schedule

Every item is machinery the [CAM Construction Set](../../../cellular-automata/cam-construction-set.md)
needs anyway. Designing from `life` gives you an engine that runs `life`. Designing from this
set gives you one that runs the reversible physics, the lattice gases, the stochastic growth
models, and the ones nobody has written yet — and the classics become the **regression
suite**, with the book's own printed figures as the answer key.

Then crystallize, per the case study's pipeline: **lookup table where the rule fits, generated
code where it doesn't**, same front end either way.

## Honest status

The **shape** of each rule is the claim — its guards, its group, its archetype, what it costs
the compiler. The **bit-exact tables are not**: entries marked ⚠️ in the YAML need checking
against Toffoli & Margolus (1987) before anyone runs them and reports a result. Norman
Margolus can settle every one of them in a sitting, which is a good reason for the
conversation rather than an obstacle to it.

## See also

- [`../case-cellular-automata.md`](../../case-cellular-automata.md) — the case study this completes
- [`margolus-rules.yml`](margolus-rules.yml) — the guard algebra
- [`../../../don-hopkins/cam-construction-set.md`](../../../cellular-automata/cam-construction-set.md) — the engine these are the spec for
- [`../../../don-hopkins/turn-tables.md`](../../../cellular-automata/turn-tables.md) — where `ising`'s temperature comes from
- `../../../norman-margolus/the-cam6-demo-for-norman.md` — the letter; Norman is the answer key
- `../../../dave-ackley/README.md` — the soft tier: asynchronous event windows
