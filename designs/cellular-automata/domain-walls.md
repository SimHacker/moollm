# Reading the anneal boundary

*How to recognize and measure the Life ⟺ Brain transition across an anneal boundary. Structured
data and every ⚠️ in [`domain-walls.yml`](domain-walls.yml).*

The question has an existing answer, and it's a good one: this is **Hanson and Crutchfield's
computational mechanics of cellular automata**. Better, the version here is *easier* than the one
they solved. They had to discover the domains inside a spacetime diagram that looked like noise.
Here the domains are known in advance, because the anneal selector assigned them and you painted
the regions. The hard half is already done. What's left is instrumentation.

## What the method is

A **domain** is a region whose spacetime pattern is describable by a regular language — an
ε-machine. Build that machine, then run it as a **transducer** over the spacetime diagram:
conforming cells map to blank, violations get marked. What survives the filter is the walls, the
defects, and the particles. The domains were the background all along, and subtracting them is what
makes the structure visible.

Then you catalog the survivors — each wall type by its velocity and profile — and tabulate the
interactions: α + β → γ. At which point the thing you're looking at is a CA *computing* by
transporting and colliding particles, which is intrinsic computation made visible by subtraction
rather than by argument. (⚠️ Get the exact Hanson & Crutchfield papers and years before any of this
is said on air.)

## Start with the exact measure, not the statistical one

**The allegiance field.** For each cell, run *both* rules on the local patch and compare each
prediction against what actually happened next. Four outcomes: Life predicted correctly and Brain
didn't, Brain and not Life, both agreed (common — the rules coincide on many neighborhoods), or
neither. That last set is the walls.

This should be built first because it's *exact* rather than statistical, and it's about ten lines of
code. No estimation, no threshold, no training, no tuning. And it comes with a free bonus nobody had
in 1993: the anneal selector already knows each cell's **intended** allegiance, so comparing
intended against behavioral gives you a discrepancy field — cells assigned to Life that are behaving
like Brain. That measurement only exists because you painted the domains.

## Flux

Which is what you actually asked for, and it's a small family:

- **Global area flux** — the derivative of the Life-allegiance cell count. One signed number, so one
  meter, and the sign tells you which rule is winning.
- **Local flux density** — cells converted per unit boundary length per tick, as a field rendered
  onto the wall itself.
- **Boundary velocity** — per segment, by cross-correlating consecutive frames, giving a velocity
  field along the interface.

The interesting experiment falls out of the first one: find the parameter values where global flux
crosses **zero** and you've found the composition at which the two rules are in equilibrium. That's
a phase-boundary hunt, and it's the same shape of experiment as sweeping the Ising temperature —
which means it shares a front panel with something already on the build list.

## Foaminess is a measurement, not an impression

"Anti-Life just makes it foamier" is a statement about **interfacial roughness and domain-size
distribution**, and it's testable in an afternoon:

- **Domain-size distribution** — connected components on the allegiance field, histogrammed.
  Foamier means more domains, smaller.
- **Coarsening exponent** — mean domain area against time. Curvature-driven coarsening classically
  goes as t^½; whether CA anneal domains obey it is exactly the open question.
- **Interfacial width** — w(L) against segment length L, giving a roughness exponent under
  Family–Vicsek scaling. ⚠️ Don't claim a KPZ universality class without measuring it.
- **Von Neumann–Mullins** — in 2-D soap froth and grain growth, a bubble's area changes linearly
  with (n − 6), where n is its number of sides. ⚠️ That's borrowed from a different physical system
  on purpose, and testing whether anneal domains obey it is a real result either way.

So the observation is a hypothesis with an obvious measurement attached, which is the best kind.

## The two meters, but scoped to a region

Here's the design requirement this whole question produces. Entropy rate and statistical complexity
computed **globally** cannot see any of this, because the domains dominate the area and drown the
walls. The prediction worth testing is that domains are low-h_μ and low-C_μ while the walls carry
the structure — and testing it requires computing the meters over a **mask**.

Which means measurement stages need a **region**, exactly the way drawing tools do — the same
`source × region × blend` factoring, with meters as one more consumer of the region dimension. That
turns the two-meter ask from a request for two readouts
into a request for two readouts *with a region input*, which is a more specific and more useful
thing to build.

## Brute force is genuinely an option now, and here's where to spend it

**Exhaustive tabulation.** Enumerate every k×k×τ spacetime patch and count its frequency inside each
domain, then classify by likelihood ratio. A 3×3×2 binary patch is 2¹⁸ = 262,144 patterns, which is
nothing. Worth noticing what that is: it's the *same move the rule engine is built on* — the
analyzer gets to use the CAM-6's own
[partial-evaluation trick](cam-construction-set.md#the-move-has-a-name-partial-evaluation-and-one-more-thing)
against the CAM-6's output.

**Automatic particle cataloging.** Filter to walls, connected-component them, track them over time,
cluster the trajectories by velocity and profile, and the particle zoo and its interaction table
come out generated instead of hand-compiled. This is a great deal of compute spent stupidly, which
is precisely what's cheap now and wasn't in 1993 — and it's the strongest argument that the old
method deserves a new instrument.

**Learned classifiers, honestly placed.** A CNN on patches would work, and for *this* problem it
would be worse than the predictor test, because the rules are known and the exact answer is cheaper
than the approximate one. Spend the learning budget where the answer isn't known: on **discovering
domains nobody declared.** Hanson and Crutchfield found that walls between domains can themselves be
domains — a third phase living inside the interface. A classifier allowed to find a category you
didn't paint is looking for exactly that, and that's the result worth chasing.

## The compression bench

Running deterministic Life beside progressively fuzzier copies is entertainment, and it's also a
**bifurcation diagram in the noise parameter** — you get to watch the melting point, the noise level
where gliders stop surviving and structure dissolves. That question has a framework behind it:
noise-stability of CAs is a real subject, and its canonical result is that **Toom's rule**
(North-East-Center majority) survives small random perturbation because it has the eroder property,
while plain 2-D majority voting does not (⚠️ verify the attribution and the exact statement). So
"which rules survive dithering" is a measurable property with prior art, and the thing to plot is
structure-survival against noise level, one curve per rule, with the knee as the transition.

### Compression is an entropy-rate estimator, and that's the trap

Compressed size per cell per tick is a crude but genuine estimate of the **entropy rate** — the
brute-force version of the meter this whole project has been asking Crutchfield for, computable
today with zlib and no theory at all. A live "bits per cell per tick under gzip" readout costs
nothing and already separates a still life from a random soup.

Then you hit the wall, and it's the best thing about the question: **random noise is
incompressible.** Sort the rule catalog by compression ratio and pure noise comes out on top. Which
means compression alone reproduces precisely the confusion — random mistaken for complex — that
computational mechanics was built to correct.

That's good news rather than bad. **The compression question arrives at the two-meter ask on its
own.** Nobody has to be talked into believing one number is insufficient; you discover it the first
time you sort the zoo by gzip ratio and find noise at the top. That's a far better argument than a
theoretical preference, and it's an experiment anyone can run this afternoon.

The second axis comes cheaply and from the same data. Estimate the block entropy H(L) over a range
of block sizes L, and **one table gives you both numbers**: the *slope* is the entropy rate, the
randomness; the *intercept* is the **excess entropy**, the computable practical cousin of statistical
complexity. Same exhaustive tabulation already proposed for domain classification, reused for the
meters. (⚠️ Excess entropy and statistical complexity coincide in some cases and not others — don't
conflate them in print.)

### Anneal is the extreme case, and the reason is the interesting part

The suspicion is right, in the *low* direction. Anneal builds large uniform domains separated by thin
walls, so the bulk costs almost nothing to describe and the entropy rate falls toward zero as domains
coarsen.

Which has a consequence worth stating on its own: **if the domains compress to nothing, all the
information is in the walls.** Total compressed size then scales with *boundary length* rather than
area — so the compression meter is secretly measuring interfacial length, and its time derivative is
the coarsening rate.

So zooming in on the edges isn't an optional refinement. It's where the entire signal lives, and the
high-frequency detail at the boundary is the *same measurement* as the interfacial-width exponent
above — arrived at from compression instead of from metallurgy. Two routes, one number, which is
usually a sign the number is real.

One methodological caution: ⚠️ anneal is **non-stationary** while it coarsens, and entropy-rate
estimation assumes stationarity. Report the curve over time; never a single number.

### What to build

Run every rule in the catalog, log spacetime, report both estimates as curves over time. The
artifact is a compressibility catalog for the rule zoo, which no rule catalog currently ships. And
the interesting cells of that table are the **combinations** Don asked for — Life against Brain under
the anneal selector — because combinations are where walls exist to be measured at all. As before,
the meters need to be region-scoped, which is the same requirement this page reached from the other
direction.

## The contour slice, and the dance at the edge of it

There's a technique already in `CAM6.js` that doesn't seem to be written down anywhere. The colormap
is a smooth gray sweep with a **high-contrast black/white discontinuity dropped into the middle**, at
the 127/128 boundary. The smooth part shows almost nothing; the discontinuity renders anything
straddling it at maximum contrast. And `frob` — the DC offset added to every cell — slides the whole
field up and down *through* that discontinuity, on the mouse wheel.

So it's an **isoline visualizer built from a colormap discontinuity plus a DC offset**: no contour
algorithm, no extra pass, full frame rate, and you hunt for the interesting level by hand. That's the
violin, and it's a [Turn Table](turn-tables.md) — a rotational control sweeping a continuous
parameter. (⚠️ Reconstructed from Don's description; confirm the colormap details against the running
app.)

### The dancing patterns are the scheduler made visible

Don's own sharpening of this is the important part: **that texture is not a cellular automaton
artifact, by definition.** A CA is a uniform local rule applied as a function of a fixed neighborhood,
independent of position and update order. The dither carry threads through cells *in scan order*, so
the pattern depends on where a cell sits in the update sequence and not only on its neighborhood.

Which makes it the display this whole project needed and didn't know it had.
[`schedulers.md`](schedulers.md) argues at length that iteration order is part of the rule and is
invisible in every engine. This is **the instrument that makes it visible** — built years before the
argument for it.

### "Language and syntax" is literal

The patterns an error-diffusion dither can produce at a given residual form a *constrained set* of
configurations — a shift space defined by forbidden words. That's a formal language in the exact
technical sense, and the "syntax" is its transition structure. Which means the right tool is an
**ε-machine of the dither**, whose statistical complexity measures how much memory the dance carries.

And the one-dimensional case has a name that makes the whole thread click shut. A 1-D DDA's step
sequence — which axis moves on each tick — is a **Sturmian sequence**: aperiodic with minimal factor
complexity, the cutting sequence of a line of irrational slope, the symbolic dynamics of an irrational
circle rotation. Sturmian sequences have **zero entropy rate and nonzero excess entropy**.

Low h_μ, real C_μ. That is *exactly* the structured-but-not-random corner the two meters exist to
find — which means **the dither texture is a naturally occurring specimen of the phenomenon this
entire project is asking Crutchfield about**, generated for free inside Don's own engine, and found
beautiful before anyone supplied the theory. It's the same DDA the
[Bresenham turtles](schedulers.md) run on, seen from the other end.

⚠️ The 1-D statement is solid; 2-D error diffusion with a distributed kernel is richer than Sturmian,
and that structure is the open and more interesting question.

Two things follow immediately. First, it's a **calibration source**: a meter needs a signal with a
known answer, and the 1-D case has a theoretical entropy rate of zero, so if the estimator doesn't
report near zero the estimator is broken. Free, exactly-known test signal, produced by the machine
being instrumented.

Second, and against the obvious: **don't train a net on it — reconstruct the machine.** For a process
with a genuine finite-state syntax, ε-machine reconstruction yields an exact interpretable automaton
where a net yields weights that describe it worse. This is the specific case where the classical
method beats the fashionable one, and it happens to be the method of the person this repo is writing
to. A net still earns its place in three places: the 2-D case where spatial machine reconstruction is
hard, the "which scheduler produced this texture" classifier, and demodulation near edges where local
constancy fails.

That last one is worth its own note, because the texture is **an analog signal encoded in a binary
image** — local dither density reads out the fractional part of the underlying value, which is the
sigma-delta face of the [Bresenham identity](schedulers.md). So you can recover sub-LSB precision by
box-filtering, which is oversampling rather than magic and needs no model at all. And automating the
wheel — sweeping `frob` through the whole range and stacking the contours — reconstructs a
higher-precision field from a stack of binary level sets, beating the cell's own bit depth. A hand
technique for finding the interesting slice becomes, once automated, a measurement instrument.

## The loop this closes

Analyzers are pipeline **stages that emit fields**, and `CAM6.js` already has an `analyzer`
`defineType` to hang them on. But if a meter emits a field, and
[every parameter can consume a field](../korz/korz-prime/examples/layered-rules.md), then **a meter
is a source.** Drive the anneal selector from the measured flux and the boundary regulates itself:
the instrument's measurement becomes part of its physics.

Which is worth building and worth labeling, because measurement-driven rules are feedback loops and
they can oscillate.

## See also

- [`cam-construction-set.md`](cam-construction-set.md) — the machine this instruments
- [`schedulers.md`](schedulers.md) — the measured field depends on iteration order too, so a flux number without a named schedule is incomplete
- [`korz/korz-prime/examples/layered-rules.md`](../korz/korz-prime/examples/layered-rules.md) — anneal as a selector rather than an engine, and `both_life`'s polarity
- `../jim-crutchfield/positive-feedback.md` — the two-meter ask this makes specific
- jim-crutchfield — computational mechanics and ε-machines
