# Schedulers: the open space

*Split out of [`cam-construction-set.md`](cam-construction-set.md#iteration-order-is-a-plug-in),
where this was a bullet list. A list was the wrong shape. Structured data and every ⚠️ live in
[`schedulers.yml`](schedulers.yml); this page is the argument.*

Nearly every cellular automata engine picks one update order, welds it in, and never mentions it.
So the space has no catalog and no vocabulary, and the consequence is that the part of a CA machine
with the most unclaimed territory in it is the part nobody thinks of as a part.

It is also where scalability is decided. Ackley's argument for the Movable Feast
Machine is that a global clock cannot scale, which means the scheduler
isn't one component among many — it's the component that determines whether the machine can grow.

## Six axes, not a menu

A scheduler is a point in a product space, and naming the popular points is the same mistake as
naming `Life_Echo`:

| Axis | What it decides |
|---|---|
| **Site selection** | Which sites update, in what sequence. Synchronous, raster, serpentine, space-filling, carrier-driven, permutation, Poisson clocks, event-driven frontier. |
| **Granularity** | The unit that updates indivisibly — cell, 2×2 block, event window, tile, whole grid. Atomicity is what buys reversibility in the Margolus case, not the block's shape. |
| **Conflict policy** | How concurrent units avoid each other. Static coloring, runtime non-overlap, ownership with locked borders, optimistic-with-rollback (⚠️ which I don't think anyone has tried in a CA engine). |
| **Clock** | Where time comes from. |
| **Coherence** | What a read sees — the memory model, orthogonal to all the above. |
| **Determinism** | Reproducible? Invertible? |

The conflict-policy row hides a unification worth stating: **static coloring, Margolus phases,
checkerboard sweeps, and MFM's non-overlap test are one mechanism.** All four partition an
interference graph and run one class at a time. One compiler pass serves all of them.

## The clock is a coordinate, and CAM6 already reads it twice

The scan rotation in `CAM6.js` is selected by the low two bits of the step counter. The Margolus
partition is selected by the low one bit. Serpentine is selected by the low bit of the *row* — a
spatial phase rather than a temporal one. These are all the same kind of thing: a **phase word**,
assembled from low-order bits of position and time.

Which exposes something in the existing engine. `CAM6.js` reads the clock in two unrelated places.
`phaseTime` is a neighbor in the Moore address — it's shifted into the table index, so it feeds
**rule dispatch**. And `step & 3` selects the scan rotation in a separate switch, feeding
**scheduling**. Same clock, two ad-hoc readers, no shared coordinate between them.

Publish one phase word and let the dispatcher, the scheduler, and the basis change all consume it.
Then *"iteration order is part of the rule"* stops being a slogan and becomes a **type**: the rule
guards on the same coordinate the scheduler indexes on, and there is no principled line left
between the rule and the schedule.

The width of that phase word is a budget. It's how much symmetry the schedule can afford to cover —
which is the next section.

## Serpentine and four-rotation are not alternatives

I had this wrong in the construction-set page, which called four-rotation cycling "strictly better
than serpentine." They cancel *different* symmetries and they multiply.

- **Serpentine supplies the reflection.** The carry drifts east on one row and west on the next.
- **Four-rotation supplies the rotations.** The residual direction turns 90° per generation.
- **Together** they average the error-diffusion kernel over the full **dihedral group D₄**, which is
  exactly the symmetry group of the square lattice being scanned.

Either one alone covers half the group: rotation-only keeps a handedness, serpentine-only keeps a
preferred axis. So:

> **A scan schedule is a walk over a symmetry group, and you want the walk to cover the group.**
> Declare the lattice's group and the anisotropy-cancelling schedule falls out.

That's the *same* group declaration the rule guards already use to match orbits instead of
individual patterns — `C_k`, `D_k`, `E` in
`margolus-rules.yml`. One declaration, two
consumers: it tells the dispatcher which contexts are equivalent, and it tells the scheduler which
orders average out. In three dimensions you cover the octahedral group and the sentence survives
unchanged.

## Serpentine's better argument, and where it leads

The bias story is the famous one, but continuity is the stronger one. **Row-major teleports the
accumulator** from the right edge back to the left once per row, injecting a spatial discontinuity
into a quantity that is supposed to represent a *local* remainder. Serpentine never teleports.

But serpentine is still only one-dimensionally local — adjacent rows are a full height apart in
time. Take continuity seriously and you arrive at the real statement: **a scan order is a map from
one-dimensional time into n-dimensional space, and a space-filling curve is the answer to which map
preserves locality best.**

Hilbert, Peano, Moore, Morton, Gray code. Three separate payoffs, and they're independent:

1. **Carry locality.** The error-diffusion remainder stays near where it was generated. Established
   practice in dithering (⚠️ Velho & Gomes — verify), and as far as I can tell unheard of in CA
   engines.
2. **Cache locality.** Raster needs two rows resident. A curve traversal keeps a compact working
   set, which is real speed on large grids rather than an aesthetic preference. Morton order is
   already what GPU texture swizzling uses.
3. **Parallel decomposition.** Cut the curve into *P* equal arcs and you get *P* compact domains
   with low surface area, so minimal halo traffic. Standard for load balancing in adaptive mesh
   refinement (⚠️ verify the citation), and exactly what a distributed MFM wants.

There's a catch, and it has a pretty fix. Hilbert isn't isotropic either — it has a blobby quadrant
grain of its own. But the Hilbert base has four rotations and two reflections, which is **eight
variants, which is D₄ again**. So cycle the curve's orientation across generations and the
group-coverage argument applies unchanged: a **Hilbert scheduler walking D₄**, deterministic,
locality-preserving, and anisotropy-free.

And Morton is the bridge between the two halves of the compiler problem. Take the high bits of a
Morton index as a tile ID and the low bits as intra-tile order, and **one curve is simultaneously a
serial scan and a parallel decomposition** — which is the join that
the dependence-cone ladder needs between "serial
carry" and "tiled dispatch."

## Bresenham particles

Don's, and the best thing on this page: a population of little turtles, each with a **speed of one
cell per tick and a fractional direction**. Where they land is what updates. Position, integer
direction, error accumulator; the accumulator decides which axis steps.

It sounds like a toy. It isn't, because of this:

> **Bresenham, Floyd–Steinberg, and sigma-delta modulation are the same algorithm.**
> Each accumulates a fractional residual and emits a discrete step when it overflows — a
> first-order DDA. They differ only in what they point at: *position*, *intensity*, *voltage*.

Which means the scheduler and the dither are one mechanism aimed at different quantities. So a
walker can **carry the heat remainder along its own path** instead of along the raster path, and
the carry is continuous by construction because the walker is. Several walkers are several
independent carries — natural threads. The aesthetic idea and the parallelization idea turn out to
be the same idea, arrived at from opposite ends.

**The number theory is the amusement.** A walker with slope *p/q* on a torus is a discrete geodesic.
Given the right coprimality it visits every cell exactly once before closing — a complete, fair
sweep that happens to look like diagonal stripes (⚠️ get the exact condition right before printing
it). Slope 1/0 is a column scan, 1/1 is diagonal, and a good rational approximation to an irrational
gives quasi-uniform coverage that *looks* random while being perfectly deterministic. **One
parameter sweeps from raster to quasi-random, and that parameter is an angle** — so it's a
[Turn Table](turn-tables.md). The knob rotates and the walker direction rotates; it's the same
control, which is a good sign the abstraction is real rather than a pun. Non-coprime slopes leave
cells unvisited, which is either a bug or frozen regions, and either way it's measurable: put a
visit-count heatmap on the panel.

### The menagerie, and the nine names you already have

Start with nine patron saints. **`c` just sits there.** `n`, `s`, `e`, `w` go in their nominal
straight directions; `nw`, `ne`, `sw`, `se` go in their diagonominal ones. Eight wedges and a
center tap — which is to say, **the patron saints of eight-item pie menus.**

Those same nine names are already doing three other jobs in this machine. They're the nine offsets
of a Moore neighborhood. They're already opcode names in CAM6's RISCA bank, where they mean *copy
from that direction*. And they're the pie-menu layout Don's own work settled on decades ago. So a
walker is the **moving version of the RISCA copy opcode** — one vocabulary, four subsystems, no
translation layer anywhere.

Two details fall out that are too neat to leave unsaid. **The center of the pie menu is the
identity element**: `c` is `(0,0)`, the additive identity of the algebra below, the neutral gesture
of the control, and the turtle that does nothing — the same fact arriving three times. And a pie
menu selects by *angle* while a walker's direction *is* an angle, so the control's geometry and the
parameter's geometry are the same geometry. Quantized to eight detents it's a pie menu picking a
saint; unquantized it's a dial sweeping everything between them. That's the entire
[Turn Table](turn-tables.md) thesis with nothing left over.

### Moveable RISCA: swap, don't copy

The nine names are already RISCA opcodes meaning *copy from that direction*. Change one verb and
they mean **swap with that direction, carrying your payload** — with `c` as stay-put. That one word
changes what kind of object this is:

- **Conservative.** Nothing is created or destroyed, so population and histogram are exactly
  preserved. The CAM book's conservation theme, for free.
- **Reversible.** A swap is its own inverse. Replay the direction sequence and the grid comes back
  exactly.
- **Bijective.** A conflict-free set of swaps is a *permutation of the grid*, which makes this a
  transport network rather than a rule that edits.

Two cells can't both swap into the same target, and the three answers to that are all already on
this page. Confine swaps inside a Margolus 2×2 block and they're atomic and provably conflict-free —
which makes moveable RISCA **a lattice gas with per-cell programmable momentum**. Or enable only a
non-conflicting color class, which is the meta-iterator doing its job. Or, prettiest, **mutual
consent**: swap if and only if `a` points at `b` *and* `b` points back at `a`. That's conflict-free,
local, deterministic, and reversible with no partition and no arbiter at all — and cells pointing at
neighbors that don't point back simply stall, so jams and pressure and traffic emerge from the
protocol instead of being modeled.

"Higher-level layers and rules decide which direction it should travel and when" means the direction
is **a field written by other stages**, which makes this layer programmable **advection**: transport
of payload along a vector field the rest of the machine computes. Paint the flow by hand, or drive it
from a noise gradient, or have another CA compute it. Note the budget honestly — nine directions
need four bits, which on an eight-bit cell leaves four for payload, and a photograph wants
twenty-four. The direction field wants to be its own plane.

It also generalizes things already in the catalog. **Margolus's sand rule *is* moveable RISCA with
the direction hardcoded to "down"** and the diagonals as its conflict fallback. HPP is this with
fixed rather than programmable momentum.

And it closes the gap with the turtles, because **a Bresenham walker and a moveable RISCA cell differ
only in where the error accumulator lives** — in the agent above the grid, or in the payload inside
it. Give a moveable RISCA cell a fractional accumulator and it *is* a Bresenham walker implemented as
swaps. Same DDA, two addressing precisions.

**Now let a bunch of them loose on a photo.** CAM6 already registers images as sources — webcam,
logo, Micropolis tiles. Load one, release a population, and the pixels get *transported* rather than
recolored. Because swaps conserve, the histogram is invariant: every frame is a permutation of the
original photograph, which can be smeared past all recognition while still containing exactly the
same pixels. And undo is free — run the direction sequence backwards and the photograph reassembles
itself, which is a performance in its own right.

### Breeding, which is a theorem rather than a hope

Combine two turtles by adding their coordinates: `(p,q) + (r,s) = (p+r, q+s)`. Now —

> **Componentwise addition of direction coordinates is the Stern–Brocot mediant.**
> The mediant of `p/q` and `r/s` is `(p+r)/(q+s)`. Breeding coordinates *is* taking mediants.

So repeated breeding from the patron saints walks the **Stern–Brocot tree**, which enumerates every
positive rational exactly once. "Combine them to make new ones of any direction" isn't a loose
aspiration; every rational direction is reachable, by exactly one lineage. Direction is projective
anyway — `(2,2)` and `(1,1)` are the same turtle — so the space being enumerated is precisely
P¹(ℚ), which is precisely what Stern–Brocot enumerates.

And then the part nobody would guess. The Stern–Brocot tree **is** the continued-fraction tree, so
each breeding step toward a target is the best rational approximation available at that
denominator. Breeding toward an irrational direction therefore produces optimal quasi-uniform
coverage at every generation — the equidistribution isn't something you tune for, it's what
breeding *does*. Breed toward the golden ratio and the slopes are 1/1, 2/1, 3/2, 5/3, 8/5:
a **Fibonacci turtle**, the most-irrational direction, the best coverage, and the same φ as
phyllotaxis, so the visit pattern looks like a sunflower.

Underneath, Bresenham's error recurrence is the subtractive Euclidean algorithm on `(p,q)`
(⚠️ state the correspondence precisely before printing it), which means **the turtle computes the
gcd of its own direction as it walks.** The number theory isn't decoration bolted onto the walker.
It's the walker's inner loop.

**Update rate becomes a field.** *N* walkers on a *W*×*H* grid give a mean rate of *N*/(*WH*) per
cell per tick, but the *distribution* is whatever the walker dynamics produce. Regions visited more
often evolve faster, so local proper time varies across the grid — a relativistic CA arrived at by
accident from an aesthetic choice. That's one more scalar promoted to a field, which is the same
move noise-as-parameter makes.

**It stays reversible.** Negate the direction and the error term and a walker retraces exactly. So
this is a deterministic scheduler with a stochastic appearance, and it preserves the reversibility
a random scheduler destroys — the same property that makes a phase word better than a counter and
Perlin noise better than an RNG stream.

It also connects to everything else in the machine. A walker carrying a *window* instead of a point,
with a non-overlap test between walkers, **is the Movable Feast Machine with ballistic rather than
random site selection**. A walker whose atomic unit is a 2×2 block is a moving Margolus partition.
And the billiard ball model already has ballistic particles in the *rule* — this puts them in the
*schedule*, which is [one pattern at another scale](cam-construction-set.md#one-pattern-four-scales).
The physics reading is the nicest one: nothing happens until something arrives. Causality carried by
particles instead of by a global clock is Ackley's no-global-clock argument made concrete.

There's a natural ladder inside it, too, which is a tech tree if anything is: **ballistic** walkers
with fixed direction, then **reactive** ones whose direction depends on the cell they read
(Langton's ant, turmites, Paterson's worms), then **interacting** ones that collide and scatter and
breed. The ballistic case is the one with number theory in it; the reactive case is the one with
universality in it.

And as an art form it does the thing this whole repo keeps arguing for: **the schedule becomes
visible.** You watch turtles update the machine, with the echo layer already sitting there as
exactly the right decoration — phosphor trails behind each one.

## Iterators with handlers

Calling these things **iterators** is what turns the taxonomy into an architecture, because it
collapses the entire site-selection axis into one protocol:

```
Scheduler = Iterator<Site>
```

Raster is an iterator. Serpentine, Hilbert, Morton, a fixed permutation, MFM's random draw, an
event-driven frontier, a turtle — all the same type. Nesting is `flatMap`, so the composition tree
below needs no new mechanism. Laziness is free, which is what unbounded grids require. And the
ordinary combinators apply unchanged: `take`, `filter`, `zip`, `chain`, `cycle`, `interleave`.

Then you install **handlers**: things a turtle does when it hits a boundary, another particle, an
obstacle, or comes within some distance of something. Which is one more instance of a sentence this
repo keeps writing:

- a **rule** is a thing whose neighborhood comes from the grid
- a **drawing tool** is a thing whose neighborhood comes from the hand
- a **handler** is a thing whose neighborhood comes from the collision

Three instances is a pattern, not a coincidence. Handlers are Korz slot sets, guarded and dispatched
exactly like rules, and no second mechanism is needed to have them.

Events are `on_step`, `on_boundary`, `on_collision`, `on_obstacle`, `on_proximity`, plus the
lifecycle ones. Actions steer (turn, reflect, scatter, reverse, accelerate), manage population
(spawn, split, merge, die, breed with whoever you just hit), touch the grid (write, deposit a trail,
pick up a carry), or touch the schedule itself (skip this site, update it twice, hand off to another
scheduler).

Three things worth pulling out:

**`on_boundary` is the topology dimension for the third time.** Wrap, bounce, clamp, kill, teleport
is the same choice as the grid's toroidal edges and a Turn Table's wrap/bounce/clamp. Declare
topology once and let the walker, the grid, and the knob all consume it. And the closure is
pleasing: **a one-dimensional Bresenham particle with a bounce handler is exactly Tristram's
bouncing slider**, which is exactly CAM6's `frob`/`frobTarget`/`unfrob`. The
prior art turns out to be a 1-D special case of
the turtle.

**Proximity needs a spatial index, and the grid already is one.** All-pairs is O(N²) and dies early.
Let walkers register in an occupancy plane of the automaton and a proximity query becomes an
ordinary neighborhood read — the particles use the CA to find each other, at a cost the engine
already pays.

**Handlers are what the ballistic→reactive→interacting ladder was made of.** `on_obstacle → turn`
gives you Langton's ant and turmites. `on_collision → scatter` gives you the billiard ball model —
in the *schedule* now, not the rule. `on_proximity → steer` gives you boids as a scan order. And a
walker whose proximity radius *is* its event window, yielding on collision, is **ballistic MFM**.

Hazards, named rather than discovered later: spawning handlers can explode the population, so it
needs a budget like every other resource here; two walkers reaching one site must tiebreak on
something defined (id, or the phase word) rather than on iteration accident; and reversibility
survives elastic reflection and scattering but not absorption, death, or merging — so a reversible
session restricts the handler palette, and the panel should say so instead of silently breaking
undo.

## The GPU decomposition, and its actual name

There is a name, several in fact, for different things. But first a correction that redirects the
question.

**A synchronous double-buffered CA needs no non-overlapping decomposition at all.** Every cell reads
the past buffer and writes the future one, so all N cells are independent — one dispatch, no
conflict, embarrassingly parallel. Non-overlap becomes a *requirement* only for in-place updates,
for rules that write their neighbors (moveable RISCA swaps, any transport layer), or for carried
state like the heat accumulator.

So the real reason to tile a 3×3 stencil isn't correctness, it's **bandwidth**. Nine reads and one
write per cell is arithmetically trivial and entirely memory-bound, and every cell gets fetched nine
times across a frame. Reducing traffic to global memory is the whole game.

**When conflicts *are* real, the name is coloring.** Formally, distance-*k* coloring of the conflict
graph: two sites conflict when their read/write footprints overlap. Concretely, for read-radius 1
writing to self in place, class members need pairwise Chebyshev distance greater than 1, giving
`(x mod 2, y mod 2)` — **four passes**, each updating a quarter of the grid, generally
(*r*+1)^*d* classes. The established name is **red-black or multicolor ordering**, straight out of
iterative linear solvers: red-black Gauss–Seidel is exactly this trick, needing two colors for a
5-point stencil and four for a 9-point one, which is Moore.

**For chunks over time, the name is temporal blocking** — also time skewing or time tiling, with the
general framework being the **polyhedral model** and the ancestor being Lamport's hyperplane method
from 1974. The specific shapes each have names: **overlapped tiling** (ghost zones), where a tile
redundantly computes a shrinking halo so it can advance *k* steps without talking to anyone;
**trapezoidal decomposition**, Frigo and Strumpen's cache-oblivious recursive cut of spacetime;
and **diamond tiling**, the modern best practice because diamonds permit *concurrent start* where a
plain wavefront makes tiles wait on their neighbors (⚠️ verify the citation). In order-theoretic
terms each parallel step is an **antichain** of the dependence partial order — the same vocabulary
the compiler ladder uses.

### The better metaphor, and it isn't one

A CA has an **exact speed of light**: information moves at most *r* cells per tick. So the set of
cells that can affect (x, t+k) is precisely the backward **light cone** of radius *r·k*. Temporal
tiling isn't *like* cutting spacetime along causal structure — it *is* that, exactly, with no
approximation, because the light cone is a hard combinatorial fact about the stencil rather than an
analogy borrowed from physics.

Trapezoids and diamonds are **causal diamonds**. A tile is a region of spacetime that's causally
self-contained, so it can be computed without consulting anything outside it. Which makes the cost
model obvious: grow the tile in time and the cone widens, so you carry more halo or you communicate,
and that tension is the tuning parameter. Producing an *S*×*S* output tile after *k* steps needs
(*S* + 2*rk*)² inputs loaded — redundant compute rising with *k*, global traffic falling roughly as
1/*k*, with an optimum that depends on shared-memory size and is a **measurement, not a derivation**.
Put it on the panel next to frame time.

One honest cost. Temporal blocking assumes the rule is *the same* for *k* consecutive steps, so
anything reading a phase word, a hand-drawn stroke, or a live parameter breaks the tile. That bounds
*k* by how interactive the machine is: an instrument you're playing wants *k*=1, an unattended run
can take *k*=8. The good news is that this is a declared property rather than a mystery — the
compiler knows which stages read time-varying context and can choose *k* accordingly.

## ULAM fits inside this, and the misfit is the interesting part

Ackley's MFM programming language maps onto this design piece for piece,
and **moveable RISCA is the piece that closes it** — the "Movable" in Movable Feast *is* atoms
relocating by swap. (⚠️ Everything here is from reading ULAM, not from writing it in anger; Ackley
can correct the whole table in one sitting.)

| ULAM | here |
|---|---|
| Element — a typed atom | the RISCA opcode field; `layered-rules.yml` already calls RISCA "a proto-Movable Feast Machine atom" |
| `behave()` | a rule stage guarded on the cell's type |
| EventWindow, radius 4, 41 sites | the neighborhood former with a radius parameter |
| random asynchronous site selection | one value on the site-selection axis |
| non-overlapping concurrent events | a conflict policy — or equivalently an enable-by-conflict predicate |
| atom swap | moveable RISCA |
| bitfield-packed typed data members | plane algebra with named fields and declared widths |
| quarks | slot inheritance and `defer_to` |
| DReg | a noise-driven source stage |

Now the part worth dwelling on. **ULAM hardcodes its scheduler.** MFM is *always* random-site,
asynchronous, non-overlapping — and that isn't an oversight, it's the thesis. Welding in asynchrony
with no global clock is precisely Ackley's argument for indefinite scalability and robustness.

So subsuming ULAM means making MFM's scheduler **one point in a space**, which is exactly the degree
of freedom he deliberately removed. That's worth something concrete rather than just tidy: it means
the same element set can run under a raster scan, a Margolus partition, a Hilbert order, or a
population of turtles, **and be compared.** Ackley's claim that asynchrony plus non-overlap buys
robustness becomes testable by ablation — identical elements, different schedulers, measured. That's
not a rebuttal of the thesis; it's the instrument that could support it with numbers instead of
argument. Whether a removable scheduler is a gift or a heresy is a real open question, and the
answer changes what the default ought to be.

What subsumption doesn't mean: ULAM is a mature language with a compiler and a standard library, so
"expressible in this model" is not "replaceable in a weekend." The exact 41-site window numbering
matters for porting real code and isn't reproduced here. And the MFM *hardware* story — distributed
tiles, no global clock — is architecture rather than language, so none of it comes along.

## The meta-iterator

> **For each particle that is enabled, take a step** — for some definition of particle and enabled.

Both nouns are deliberately left open, and that's the design. A meta-iterator over enabled particles
is *itself* an iterator, so it can be a particle inside another meta-iterator. That closure is what
makes nesting work to arbitrary depth without inventing anything at any level.

**Any definition of particle.** Anything with a `next()`. A turtle. A raster scan — a particle that
happens to visit everything. A tile with its own interior order. A hand-driven stroke, which is a
particle whose direction comes from a mouse. An entire sub-grid running its own rules, which is the
**layer bus** — ganged CAM-6 cards. Ganging engines, nesting schedulers, and running turtles stop
being three facilities.

**Any definition of enabled.** `enabled` is a *guard*: a predicate over context, dispatched rather
than stored. Enabled by phase, by region, by the content of the cell underneath, by a budget, by a
field over a threshold, by not overlapping any in-flight window, or by a switch on the panel. And
that last-but-one collapses an entire axis — **the conflict policy is just an enable predicate.**
Margolus alternation is "enable the even-phase partition on even ticks." Checkerboard is
enable-by-color. MFM's non-overlap test is enable-by-conflict. Three mechanisms become three
predicates over one loop.

The enable mask is a **plane**, which means it can be painted. So: **paint where the machine runs.**
The brush drives the scheduler and not merely the cells — freeze a region, run another one hot,
author the proper-time field by hand instead of waiting for walker dynamics to produce one.

"For each" also hides a policy that's worth exposing, because the options are different machines:
round-robin (each enabled particle steps once per tick), chain (run A to exhaustion, then B),
weighted (speed *k* gets *k* steps), random draw (MFM's actual discipline), or a **priority queue**
where each particle carries its next-event time and you pop the earliest — under which
variable-speed turtles and the continuous-time Gillespie clock turn out to be the same thing, which
is a decent sign the factoring is right.

The cost to watch: evaluating the predicate over every particle every tick is O(N) before any work
happens. The fix is to maintain the enabled set incrementally with dirty flags — which is the
event-driven frontier from the site-selection axis, arrived at from the opposite direction.

## Schedulers compose, and that's where the empty space is

The unvisited points aren't more entries in the list. They're **nested** schedulers — the
meta-iterator applied recursively:

```
schedule: {outer: hilbert_tiles,        inner: serpentine,        phase: rotate_d4}
schedule: {outer: mfm_random,           inner: margolus_blocks}
schedule: {outer: morton_tiles_parallel, inner: bresenham_walkers}
schedule: {outer: event_driven_frontier, inner: raster_within_active_tile}
```

The hierarchy is how a locality-preserving serial order and a parallel dispatch stop competing and
start cooperating: the outer level decomposes for the machine, the inner level preserves the
physics.

## What goes on the front panel

Same argument as the two meters: if it isn't visible it
isn't an instrument. For schedulers that means the traversal animated so you can watch the scan, a
visit-count heatmap so you can see whether it's fair, which strategy the compiler picked and how
exact it is, and frame time per stage so the cost of a schedule is a number rather than a feeling.

## See also

- [`cam-construction-set.md`](cam-construction-set.md) — the architecture this is one axis of
- [`schedulers.yml`](schedulers.yml) — the axes as data, with every ⚠️
- [`turn-tables.md`](turn-tables.md) — a walker's direction is an angle, so it's a knob
- `../david-ungar/korz/examples/layered-rules.md` — the compiler side: declare a dependence cone, not a scan order
- `../david-ungar/korz/examples/margolus-rules.md` — where `C_k`/`D_k`/`E` come from
- `../dave-ackley/README.md` — MFM, indefinite scalability, and why the global clock has to go
- `../norman-margolus/the-cam6-demo-for-norman.md` — the block partition as a scheduling decision in disguise
