# The CAM Construction Set — the machine itself, rewireable 🔲🧩

*Don's design. The step past "CA rules as a block palette": expose the **datapath**, so the
emulator is something you assemble on screen and the historically accurate CAM-6 is one
particular way of wiring it up.*
Portrayal standards ·
Strategy: Snap! visual engines / fundable goals

> **On the name.** **Construction Set**, deliberately — after
> **Bill Budge's Pinball Construction Set** (1983), which this repo
> already calls the archetype of the genre and already pays tribute to with the
> Faceball Construction Set.
> PCS is the exact precedent: parts you drag together, and the machine runs *immediately*,
> with no compile step and no distinction between building it and playing it. Budge is
> upstream of Will Wright, so the name puts this where it belongs in the family. Short handle:
> **the CAM Set**.

## The move

Most CA toys give you rules and hide the machine. The book doesn't — *Cellular Automata
Machines* teaches the **architecture**, and the architecture is the interesting part.
Toffoli and Margolus's whole insight is a hardware insight: don't evaluate the rule in the
inner loop, precompute every answer into a **lookup table** and let the table be the
program.

So build the machine out of visible parts. **Every functional block of the CAM-6 becomes a
Snap! component with wires going in and out** — cell planes, neighborhood formers, the
address assembler, the rule table, the phase generator, the color map, the instruments. You
snap them together. Wired one way you get a historically accurate CAM-6. Rewired, you get
things no CAM-6 could do, and you can see exactly which wire you moved to get there.

**The lookup table stops being an implementation detail and becomes a component on the
canvas** — a thing with an address bus arriving and a value leaving, which you can inspect,
hand-edit, or fill from a rule. That single piece of exposed plumbing is the whole lesson
the book teaches and nearly every modern CA toy hides.

## The move has a name: partial evaluation (and one more thing)

Worth saying out loud, because naming it connects the hardware trick to forty years of
compiler theory and tells us what the Construction Set's back end should do.

**Partial evaluation** (Ershov; Futamura; Jones, Gomard & Sestoft) takes a program `f(s, d)`
and a known static input `s`, and produces a specialized residual program `f_s(d)` that
computes the same answers with the static work already done. The CAM-6 rule pipeline has a
textbook **binding-time division**: the rule's parameters — which rule, which planes are
wired to which address bits, thresholds, phase assignments — are **static**, fixed when you
load the rule. The **neighborhood is dynamic**, different for every cell on every tick.
Precomputing the table specializes the rule with respect to everything known in advance. That
is exactly partial evaluation, and it's the right name for the first half.

**The second half is exhaustive tabulation**, and it's the half that makes it a *hardware*
insight. Normally a partial evaluator emits residual *code*. CAM-6 doesn't — it emits the
**graph of the function**, every input paired with its answer, because the residual
function's domain is finite and small enough to enumerate. A 9-bit Moore address is 512
entries; CAM-6's assembled 16-bit address is 64K. You can afford the whole truth table, so
you buy it and never compute anything again.

That's a move with relatives everywhere once you see it:

- **DFA transition tables.** `lex` compiles a regex into a table and runs a fixed driver
  loop. The table is the program; the driver never changes. Structurally identical.
- **FPGA logic cells.** A *k*-input LUT is literally a 2^*k* SRAM truth table, because any
  combinational function of *k* bits **is** a ROM. Xilinx shipped the XC2064 in 1985 and the
  CAM book landed in 1987 — contemporaneous expressions of the same trade, logic for memory,
  made available by memory getting cheap. No influence claimed in either direction.
- **Rule numbers.** Wolfram's "rule 30" is that same table read as an integer. A rule number
  is an **address in the space of residual programs**.

### The Futamura projections, in CA terms

This is the part that's architecturally useful rather than merely satisfying:

1. **The interpreter** is a general engine that reads a rule description and evaluates it per
   cell. Correct, flexible, slow.
2. **First projection** — specialize the interpreter to one rule. You get that rule's lookup
   table, or its generated shader. *This is the CAM-6 move.*
3. **Second projection** — specialize the specializer to the interpreter. You get a **rule
   compiler**. CAM-6 had one: Forth in, tables out. Ours is Korz-style guards in, WebGPU out.
4. **Third projection** — a **compiler generator**: hand it a new neighborhood scheme or rule
   language and get back a compiler for it. Aspirational, but it's the honest description of
   what the Construction Set becomes if the front end is data rather than code.

And it retroactively justifies **believing in the JIT**: an optimizing JIT *is* a partial
evaluator, specializing code against values it observes at runtime. Generating
straightforward JavaScript and letting V8 specialize it is not giving up on the CAM-6 move —
it's delegating the same move to a machine that does it continuously and with better
information than we have at build time.

### Where the table stops being the answer

The decision rule for the back end falls straight out, and it's the same one the
[selector/bank](#one-pattern-four-scales) discussion arrives at from the other side:

**Materialize the table when the address space is small. Emit specialized code when it
isn't.** Both are partial evaluation; only the first is tabulation.

Tabulation dies quickly. A Movable Feast Machine event window has 41 sites — 2^41 entries,
and that's before multiple states. Large neighborhoods, many states, real-valued parameters
like `ising`'s temperature: all beyond enumeration. Meanwhile a totalistic rule has a tiny
residual domain even on a big neighborhood, because `popcount` is one GPU instruction and the
table behind it has nine entries. So the compiler's real question isn't "table or code" — it's
**how much of the address can be computed cheaply, and how much has to be looked up.**

### The third option: approximate the table

There's a rung below "emit specialized code," and it's worth naming because it's the only answer to
the 2^41 case. A table of 2¹⁶ entries is a function from sixteen bits to eight. **A small neural net
is also a function from sixteen bits to eight** — so the table and the net are the same object at
two points on one tradeoff:

| | Table | Net |
|---|---|---|
| Exactness | exact | approximate |
| Size | 64K entries | a few hundred weights |
| Generalization | none, by construction | to inputs never seen |
| Cost | one memory read | dozens of FLOPs |

Which makes the ladder four rungs, not three: **evaluate per cell → tabulate → compile the
tabulator → fit the table you can't build.** And the fourth rung earns its place in exactly one
place: **where the address space is too large to enumerate.** You cannot tabulate an MFM event
window. You can fit it.

Three things follow that are better than the compression story:

**The space between rules becomes traversable.** Train with a rule-ID embedding as an extra input
and you can slide continuously between `Life` and `Brain` instead of switching. That's this
document's whole complaint about `Life_Echo` — that the region between the named points should be
reachable — solved by a latent space instead of by a parameter. It's a [Turn
Table](turn-tables.md) with a learned space behind it.

**Continuous output is free fuzziness.** An output in [0,1] is a probability, so stochastic rules
stop being a special engine. But note the sting in the tail: an 8-bit cell means quantizing that
output, and *how* you quantize is a dither decision, which lands right back on the error-diffusion
carry and its [scheduling consequences](schedulers.md).

**Differentiability means you can go backwards.** If the rule is differentiable you can optimize
*toward a target behavior* — "find me a rule with entropy rate near 0.3 and high statistical
complexity." That's the inverse problem CA research has always attacked by search, and it's the
direct descendant of the genetic-algorithm work Mitchell, Hraber and Crutchfield did on evolving
CAs for density classification. Neural Cellular Automata (⚠️ Mordvintsev et al., Distill 2020 —
verify) is the established modern form.

And the objections, which matter more than the enthusiasm:

- **Exactness was the point.** An approximation of Life is not Life. A glider that decays after four
  hundred steps is a bug. So a fitted rule must **never silently replace a table** — same discipline
  as substituting a dither: it appears in the UI as a *different rule*, not as a performance
  setting.
- **Reversibility dies.** A learned approximation of a reversible rule is almost certainly not
  reversible, which puts nets at odds with the entire Margolus branch unless the architecture is
  constrained to be invertible (⚠️ coupling-layer designs exist; unverified here).
- **It isn't obviously faster.** A 64K table is one memory read; an MLP is dozens of operations. On
  a GPU the MLP may genuinely win, because compute is cheaper than bandwidth and the table may not
  fit in cache — but that's an empirical claim and should be measured before it's believed.

### Does MFM robustness cover for a net's mistakes?

Partly, and the part it doesn't cover is the part that matters.

**What it genuinely does buy.** Ackley's elements are written on the assumption that things go
wrong — damaged atoms, missing neighbors, arbitrary asynchronous interleaving, a whole tile dying.
An approximation error arrives looking exactly like "an unexpected neighborhood configuration,"
which is the fault class those rules are already built to survive. And in a system with restoring
dynamics — a sorter that re-sorts, a crystal that regrows — occasional wrong outputs get repaired by
subsequent right ones instead of accumulating. So a fuzzy substrate is *viable* under
robust-first design in a way it simply isn't under a reversible Margolus
rule. That's a real result, and it's the strongest version of the argument.

**Why it isn't enough.** Robustness of that kind is protection against **noise**, and a neural net's
errors are **bias**. MFM tolerates faults that are independent and uncorrelated; a net fails *the
same way on the same input every time*, and the healing pass is running the same broken
approximation that caused the damage. A random fault kills one glider in a hundred. A systematic
one kills that glider phase every time it ever occurs.

Three consequences worth stating plainly:

- **The errors land exactly where the interest is.** Most of a grid is background, so a training set
  is dominated by the common case and the net will be superb at reproducing emptiness and worst at
  the rare configurations — gliders, walls, defects — that are the entire point. The loss function
  and the phenomenon are misaligned.
- **Conservation laws drift rather than degrade.** If a rule conserves particle count or energy, small
  violations accumulate monotonically because nothing restores a conserved quantity. Robustness
  offers no help here. The fix is architectural rather than statistical: have the net emit a *swap
  decision* or a permutation rather than a raw next state, so conservation is structural — which is
  [moveable RISCA's](schedulers.md) property, and it composes.
  There's already a worked example of this exact quantity in the engine, on purpose: **`frob` is a
  deliberate DC offset** added per cell into the heat error accumulator, spring-returning to
  `frobTarget` at rate `unfrob`, and playable live on a mouse wheel — which is a rotational control
  driving a continuous parameter, so it's a [Turn Table](turn-tables.md) that predates the name.
  A net's conservation violation is *the same mathematical object*: a small constant bias injected
  into an accumulator. The only difference between the instrument and the defect is whether it's
  declared, measured, and on a knob.

  Which suggests the honest treatment rather than the hopeful one. Measure the mean violation per
  tick, display it, and let a slow servo inject the opposing offset — an automatic `frob` that nulls
  the drift, with the residual it *can't* null shown as the real uncertainty. Give that correction a
  spring-return whose rest position is the servo's estimate and you can push against it by hand,
  which is how you'd find out whether the drift is constant or state-dependent.

  And the cautionary half, from this same codebase: the suspected heat-sum
  bug produces an
  *east* drift, and a playable drift knob sitting right next to it is an excellent place for such a
  thing to hide for years. A control that can mask a bias will mask a bias. Expose the measurement
  separately from the knob.

- **You lose the ability to tell surprise from hallucination.** This is the one that decides it. The
  machine exists to show behavior nobody predicted. If the substrate can invent, every surprising
  observation has two explanations and no way to separate them — and robustness makes this *worse*,
  because a robust system will smoothly absorb a hallucination into something that looks plausible.

### Dither converts the bias into noise, which is the fault class robustness *does* handle

This is the move, and it's the textbook one: **dithering decorrelates quantization error from the
signal.** It's why dither exists in audio and imaging — it turns deterministic, input-correlated
distortion (banding, contouring, harmonic distortion) into broadband noise with the right mean.

Applied here: the net emits a continuous value that has to be quantized to a discrete cell state. If
you threshold at 0.5, a neighborhood the net scores 0.48 becomes 0 *every time, forever* — that's the
bias. Compare instead against a per-cell, per-tick dither value and that neighborhood becomes 1 with
probability 0.48. The glider that always died now dies 52% of the time, and **that** is an
independent, uncorrelated fault, which is exactly what MFM robustness and restoring dynamics are
built to absorb. Errors cancel across healing passes instead of compounding.

Note what the dither source has to be: a hash of (x, y, t, seed), not an RNG stream — the same
[pure-function discipline](schedulers.md) that keeps replay and shareable patches working. Blue noise
beats an error-diffusion carry here, since carried error introduces its own spatial worming and a CA
will happily amplify it.

And it's the third appearance of the same mechanism in this design: heat's carry is error diffusion,
[Bresenham is the same DDA](schedulers.md), and now so is net-output quantization. The machinery is
already in the box.

Three limits, because this is a real improvement and not a fix:

- **Dither cures the quantizer, not the net.** If the continuous output is itself systematically
  wrong — 0.9 for a configuration whose true answer is 0 — you get the wrong answer 90% of the time
  instead of 100%. So the net's output has to be a **calibrated probability** rather than a score,
  which is an extra training step and not a free one.
- **Conservation improves from drift to random walk.** Zero-mean violations accumulate as √t rather
  than t. Better, still unbounded, so the structural fix — emit swap decisions rather than raw states
  — is still the one that actually works.
- **Different seeds are different physics.** Any single run stays exactly reproducible, which is what
  matters for diffing against the table, but the ensemble isn't one system.

That last limit is secretly the best feature. Run sixteen copies with different dither seeds and
**the variance across the ensemble is a direct measure of how much the net is guessing.** Where the
copies agree, the approximation is confident; where they diverge, it doesn't know. That's an
uncertainty field, it costs one more meter on the panel, and it's the honest answer to "can I trust
what I'm looking at" — which no exact table can give you either, because a table never tells you
what it doesn't cover.

So the rule that follows: **nets where the answer is unknown and approximate anyway; never where an
exact answer exists; never under conservation or reversibility; dithered and calibrated when used at
all; and always with the exact rule available to diff against.** That last clause is cheap, because the instrument for it is already
being built — the
allegiance field that asks "which rule predicted this cell" generalizes without
modification to "did the net agree with the table," and the flux measures turn disagreement into a
number on the panel.

One cheaper trick deserves mention alongside, because it's free and nobody uses it: **the GPU
already does fuzzy lookup tables in hardware.** A filtered texture fetch *is* an interpolated table
read. Store the rule table as a texture, sample it with interpolation, and you can rotate to
positions *between* entries with no net and no training — which is a fairly literal reading of what
a Turn Table is for.

## The component inventory

Blocks, grouped by what they are in the hardware. Each is a Snap! block with typed inputs
and outputs; each is independently swappable.

**Storage**
- **Cell plane** — a grid of cells, N bits deep. Multiple planes stack in the same cell
  site, which is what makes Echo and heat-under-CA possible.
- **Plane writer** — where a result lands (`>PLN0` and friends).
- **Plane shifter** — moves old state up a plane each step. This block *is* Echo (book §3.2).

**Neighborhood**
- **Neighborhood former** — the block that taps which cells feed the rule. Interchangeable
  variants: **Moore** (8 + center), **von Neumann** (4 + center), **Margolus** (2×2 blocks
  with the grid offsetting on alternate steps), and **custom** for anything you invent.
  Swapping this block is the single most instructive edit in the whole system.
- **Phase generator** — even/odd step, horizontal/vertical phase; what the Margolus
  neighborhood needs and what multiplexed rules ride on.

**The table path**
- **Address assembler** — concatenates the tapped neighbor bits into an index. Draw this
  wire bundle and the reader understands the machine.
- **Rule table** — the lookup memory itself. Inspectable as a real table, hand-editable,
  savable, diffable.
- **Rule compiler** — takes a rule *as a value* and runs it over every possible neighborhood
  to fill the table. In Snap! a rule can be a first-class procedure, so this is an ordinary
  higher-order block: `fill table from (rule)`.

**Output and instruments**
- **Color map** — value to color, editable live, with the notch/X-ray trick available.
- **Histogram**, **event counter**, **space-time diagram** (the 1+1D view for one-dimensional
  rules), **zoom views**, **X-ray slice**.
- **Input tools** — brushes, spray, line, randomize, image import, webcam.

**Between machines**
- **Layer bus** — one engine's output plane wired into another's input. This is *ganging
  CAM-6 cards*, which the hardware did physically and which the software version can do
  arbitrarily.

## The phase matrix — the component the marble rules were hiding

The most transferable thing in the existing monolith is buried inside the marble rules,
where it looks like knob-twiddling. It isn't. Don walks through it in detail from **15:45 to
22:14** of the demo,
and it generalizes into a component the whole Construction Set should have.

The rule holds a **bank of 16 convolution kernels**. What makes a world is not the bank —
it's **what selects from it, per cell, per step**. Those selectors can all run at once, each
with its own depth, and they sum:

| Selector | What it reads | What it does to the picture |
|---|---|---|
| **Phase offset** | nothing — a constant | Every cell uses one kernel. The whole field flows one direction. Don calls it *"the DC voltage."* |
| **Phase shift step** | the clock, at a chosen rate | The kernel advances over time — *"how fast do we stir it."* Slow bakes each effect in; fast is the wavy stuff that hurts your brain. |
| **Phase shift cell** | the cell's own value | Structure becomes its own cause. Pattern folds along its contour lines; a value change shows up as a visible crease — *"a wrinkle in phase."* |
| **Phase shift X** / **Y** | position, at independent frequencies per axis | Standing zigzags whose chunkiness you dial. Different X and Y frequencies beat against each other. |
| **Cell shift** | an irregular but **spatially coherent** source | Breaks up regularity without turning it into noise. |

Dial all to zero but one and you can see what each contributes — which is how Don teaches it
in the video, and it's the right default UI behavior. Run several and they interfere.

**That is a modulation matrix**, the architecture of a modular synthesizer: a small set of
**sources** routed with adjustable depth to a small set of **destinations**, where the
character lives in the routing rather than the parts. Sixteen kernels is a small bank; the
matrix is what makes it a large space.

So make it a **component, not a rule feature**. A phase matrix block takes any bank-selecting
input and drives it from the same source palette. Wire it to:

- **the kernel bank** — what the marble rules already do;
- **the rule table** — different lookup tables in different regions or at different times,
  which is the `RISCA` "paint programs onto the grid" idea reached from the other direction;
- **the neighborhood former** — Moore here, von Neumann there, switching on a clock;
- **the color map** — the X-ray notch sweeping under modulation.

And the source palette is open: the clock, the cell, position, noise — plus, once the
continuous half is on the same bus, an **audio envelope** (Don's *"synchronize it with the
music's time instead of the simulation's time"* at 22:14) or a **webcam-derived signal**,
which is exactly how WarpOMatic drove its feedback
parameters from the performer's own position and silhouette area. Same architecture, one
system apart.

## One pattern, four scales

The phase matrix isn't a special case. Once you write it out, **most of what the monolith
already does is the same component wearing different clothes**: a **bank** of behaviors plus
a **selector** that decides which one applies, here, now. The zoo collapses.

| Layer | The bank | What selects from it |
|---|---|---|
| **Marble / flow rules** | 16 convolution kernels | the phase matrix — constant, clock, cell value, X, Y, coherent noise |
| **Anneal arbiter** | two or more CA rules (Life here, Brian's Brain there) | a **third CA** — anneal's majority-with-near-tie-inversion vote, which partitions the space into domains and hands each domain to a different rule |
| **RISCA** | ~16 instructions | the **cell's own top four bits**, with the bottom four as the operand |
| **Echo / heat** | which bit planes route where | plane masks — a static selector, the degenerate case |

So the Construction Set needs **one** core component, parameterized, not four. A `bank` block
holding N behaviors and a `selector` input that resolves to an index. Everything else is
which selector you plug in and how many entries the bank has.

That's what makes it a construction set rather than a menu. And it means each of the
following is a wire change, not a new subsystem:

- Drive the **rule table** from the phase matrix and you get regime changes over time and
  space that RISCA reaches by a different route.
- Drive the **anneal arbiter** from a clock and the domains breathe.
- Let a RISCA opcode's operand be a **phase offset** and the painted program carries its own
  modulation depth.
- Nest them: a selector whose source is *another bank's output*. This is where it stops being
  a config format and starts being a language.

### RISCA, taken seriously

The Ridiculous Instruction Set deserves more than the joke, because it's the most radical
thing in the existing engine. Splitting the cell into **opcode field** and **operand field**
means **the rule a cell obeys is stored in the cell**. Consequences worth building on:

- **Programs are painted, and adjacency is the calling convention.** A patch of Life next to
  a heat diffuser next to a copy-northward region interact wherever they touch, with no
  wiring, no ports, no API. In the demo the "logic calculator" visibly sucks Life into
  itself. That's two hand-painted programs discovering each other at a boundary.
- **The eyedropper is a debugger.** Sample a cell, paint with it — you have copied behavior,
  not appearance.
- **Opcodes should be open.** Any layer in the Construction Set ought to be installable as an
  opcode, so the instruction set is user-extensible rather than a fixed sixteen.
- **Opcodes that write opcodes.** Self-modifying spatial code: a region that rewrites its
  neighbors' instruction fields is a constructor, and von Neumann's 29-state machine is
  sitting right there as the historical target.
- **Movement instructions already exist** — the demo's copy-in-a-direction opcodes slurp Life
  across the grid. Give those a proper operand and you have transport as a primitive.

And here's the bridge worth naming: **RISCA is a proto-Movable Feast Machine.** In
Dave Ackley's MFM, each **atom** carries a **type**, and the type
determines the code that runs on it. Don arrived at typed cells dispatching their own
behavior independently, from the paint-program side. Dave formalized it and asked what
happens when you also stop assuming a global clock — which is the next section.

## Iteration order is a plug-in

This is the axis nearly every CA system hardcodes and hides, and exposing it is the biggest
idea here after the lookup table itself.

**Iteration order is not a performance detail. It is part of the rule.** Life updated
asynchronously is a different system from Life updated synchronously — not slower, *different*,
with different attractors. Any engine that bakes in "synchronous, whole grid, row-major" has
silently fixed a parameter its users don't know exists. So make the scheduler a component with
a plug-in interface, and put the variants in the palette:

- **Synchronous whole-grid.** Read the old state everywhere, write the new state everywhere.
  The textbook default, and one option among several rather than the law.
- **Row-major scan.** Required the moment a rule carries state across cells — which
  **error diffusion** does, by handing the averaging remainder to the next cell instead of
  discarding it.
- **Serpentine scan.** Alternate direction each row — boustrophedon. It cancels the left/right
  bias, and better than that, it makes the scan a **single continuous path**: row-major teleports
  the accumulator from the right edge back to the left once per row, injecting a discontinuity
  into a quantity that is supposed to be a *local* remainder. Serpentine never teleports.
- **Four-rotation cycling.** Scan the grid rotated 0°, 90°, 180°, 270° on successive
  generations. Because a CA runs forever, the accumulated anisotropy **cancels over time**
  rather than merely being scrambled within one frame — an option available only because you're
  iterating rather than rendering one image. Without it, error diffusion's residual always drifts
  the same way and the "worming" artifacts acquire a permanent grain.
- **Both at once,** because they cancel *different* symmetries and multiply. Serpentine supplies
  the reflection, four-rotation supplies the rotations, and together they average the kernel over
  the full **dihedral group D₄** — exactly the symmetry group of a square lattice. Either alone
  covers half the group. Which generalizes: **a scan schedule is a walk over a symmetry group, and
  you want the walk to cover the group** — the same `C_k`/`D_k`/`E` declaration the
  rule guards use to match orbits instead of
  points, with the dispatcher and the scheduler as its two consumers.
- **Space-filling curves.** Take the continuity argument seriously and a Hilbert or Morton order
  keeps the carry local in *both* axes instead of only along rows.
- **Bresenham particles.** Turtles with a one-cell-per-tick speed and a fractional direction,
  where they land being what updates. An art form with number theory inside it, and the point
  where the schedule becomes something you watch.
- **Block-partitioned (Margolus).** Worth saying out loud: **the Margolus neighborhood is
  already an iteration-order plug-in** and everyone treats it as a neighborhood. Updating 2×2
  blocks atomically with the block grid offsetting on alternate steps is a *scheduling*
  decision, and it's the scheduling decision that buys reversibility and conservation. Once
  the scheduler is a visible component, that stops being folklore and becomes the obvious
  first example.
- **Random event windows (MFM).** Ackley's asynchronous model: pick a site at random, run the
  rule atomically on a window around it, no global clock at all. **Concurrent windows are safe
  when they don't overlap**, so parallelism falls out of spatial separation rather than
  barrier synchronization — which is what makes it **indefinitely scalable**: add hardware
  without redesigning the program. It's also **robust-first** in the strict sense, because
  there is no global synchrony left to lose when part of the machine fails.
- **Tiled parallel dispatch.** The GPU version of the same non-overlap argument, with
  workgroups instead of random draws.

That list is the shallow end. The scheduler turns out to be the widest unexplored space in the
machine, and it has its own page: [**Schedulers: the open space**](schedulers.md) — six orthogonal
axes rather than a menu, space-filling curves, Bresenham turtles and the breeding algebra that
generates every rational direction, iterators with collision handlers, and the meta-iterator ("for
each particle that is enabled") that all of the above turn out to be instances of.

### Where the clock comes from, and why it's one coordinate

The four-rotation scan is selected by the **low two bits of the step counter**. The Margolus
partition is selected by the low one bit. Serpentine is selected by the low bit of the *row* — a
spatial phase instead of a temporal one. Same kind of thing every time: a **phase word** assembled
from low-order bits of time and position, whose width is the budget for how much symmetry a
schedule can cover.

`CAM6.js` reads that clock in two unrelated places. `phaseTime` is shifted into the Moore table
index, so it feeds **rule dispatch**; `step & 3` selects the scan rotation in a separate switch, so
it feeds **scheduling**. One clock, two ad-hoc readers, no shared coordinate. Publish the phase word
once and let the dispatcher, the scheduler, and the basis change all consume it — at which point
*"iteration order is part of the rule"* stops being a slogan and becomes a **type**, because the
rule guards on the same coordinate the scheduler indexes on and there is no principled line left
between them.

### The second axis: what a read sees

The scheduler says **when** a site updates. It does not say **what the rule sees when it
reads a neighbor** — and that's a separate plug-in that almost every engine welds to the
first one and then forgets it did.

The question is whether there's a **past** to read. Double-buffering isn't a memory
optimization, it's a semantic commitment: it's the thing that makes "synchronous" mean
anything at all.

- **Past buffer.** Read generation *t*, write generation *t+1*, ping-pong. Every read sees
  the same past, so results are independent of visit order. Costs 2× memory and — the part
  that matters — **a global barrier every generation**.
- **In place.** Reads see whatever is currently there: some neighbors already updated this
  generation, some not. Scan order stops being cosmetic and becomes part of the definition,
  which is where "iteration order is part of the rule" bites hardest.
- **Locked window (MFM).** Take exclusive access to an event window, read and write in place
  inside it, release. No global buffer and no barrier, because **correctness comes from
  non-overlap in space rather than separation in time**. Ackley doesn't need a past state
  because he never has a global present — which is exactly the thing that makes the model
  indefinitely scalable, since a barrier is a global object and global objects are what
  don't scale.
- **Statically exclusive (Margolus).** Worth stating as the unification it is: **block
  partitioning is MFM locking with the conflict resolved at compile time instead of run
  time.** Same guarantee — a rule gets exclusive access to a disjoint region — bought by a
  static tiling rather than a runtime lock. Zero synchronization cost, less generality. Two
  points on one axis, not two unrelated traditions.
- **History of depth *k*.** Keep *k* past generations addressable. This is how you get
  **Fredkin's second-order construction** — `s(t+1) = f(neighborhood(t)) XOR s(t−1)`, which
  makes *any* rule reversible — and note what that means: **reversibility purchased from the
  memory model rather than from the rule.** It's also what echo, heat, and trail layers
  actually want instead of faking with a decay plane, and it's what
  [scrubbing backwards](turn-tables.md) needs when the rule isn't invertible.

**So rules declare, and the engine satisfies.** A rule states its requirement —
`reads: past` / `present` / `exclusive-window` / `history(k)` — and the engine picks the
cheapest implementation that honors it, the way a compiler picks a memory ordering. A
Margolus rule asking for `exclusive-window` gets the static partition with no locking. A
totalistic Moore rule asking for `past` on a tiled GPU dispatch gets halo exchange. An
in-place rule that never declared a scan order gets rejected, because it hasn't finished
saying what it is.

That also lets the engine **check the joint property nobody can check today**: reversibility
is not a property of the rule alone. It needs a bijective local update, **and** a schedule
whose application order can be run backwards, **and** enough history. Three plug-ins, one
theorem. Split them apart and each is checkable; leave them fused and the answer is folklore.

**The compile target has opinions, and should have to say so.** GPU ping-pong makes the past
buffer nearly free and makes locking nearly impossible — which is the real reason almost
every GPU cellular automaton in existence is synchronous. The hardware chose the semantics
and nobody was asked. Ackley's tile hardware runs the other way: distributed interlocking,
no global clock, no global address space. Making coherence an explicit component is what
keeps the compile target from silently picking the physics.

*(Historical note, pleasing if it holds up: Ingerson & Buvel's "Structure in Asynchronous
Cellular Automata" is ⚠️ also in* Physica D **10** *(1984) — the same volume as Toffoli's CAM
paper and Crutchfield's video feedback paper. The
asynchrony question was in the room too. Verify before repeating.)*

Two payoffs from making these components:

**The scheduler can be modulated like anything else.** Plug the phase matrix into the
iteration-order selector and the update discipline itself becomes a function of time,
position, or cell value. Synchronous in the calm regions, asynchronous where it's busy.

**Comparisons become one wire.** Run the same rule under four schedulers side by side and
watch which structures survive. That's a real experiment, it's a good show segment, and it's
the sort of thing that's currently a rewrite instead of a swap.

## Rewiring is the curriculum

The point of components is that the lesson plan is a sequence of patches, each one edit away
from the last:

1. **Life.** Moore former → address assembler → table → plane 0. The minimal machine.
2. **Life with trails.** Add a plane shifter. Nothing else changes. Echo is not a feature,
   it's a block you inserted.
3. **Billiard-ball logic.** Swap the Moore former for Margolus and add the phase generator.
   Same table path, reversible physics out the other end — and the reason *why* becomes
   visible, because you can see that the rule now rewrites a whole block at once.
4. **Ising, twice, side by side.** The book explains Ising models better than anything else
   I've read, and the reason it's a great station is that you can build the *same* model two
   ways and the difference is one wire.
   **Metropolis:** temperature is an **input you set** — a knob, an external random number,
   an open system that leaks.
   **Creutz demon:** a few bits per cell carry an energy currency, spins trade with it, and
   total energy is conserved *exactly* — so the model is closed, deterministic, and
   reversible, the heat bath lives inside the cell array, and **temperature becomes an output
   you measure**, fitted from the demon's energy histogram.
   The lesson is worth the whole station: **whether a quantity is an input or an output is a
   wiring choice, not a fact about the quantity.** It's also the cleanest possible warm-up for
   the argument that instruments belong on the front
   door — here's a panel where the same word is a
   knob on the left and a meter on the right.
   *(It also forces the partition into the open, since you can't flip interacting spins
   simultaneously — the checkerboard sweep and the Margolus block turn out to be the same
   move, a proper coloring of the interaction graph.)*
5. **Heat under CA.** Two engines sharing one cell array, split by bit plane, with a leak
   wire from the CA into the diffusion. The "heat pollution" from the demo, drawn.
6. **Ganged layers.** N engines in parallel with cross-wiring — what the hardware needed
   extra boards for.

Each of those is a chapter playground, which is the thing Norman gave permission for.

## That ladder is a tech tree, and this is a Factorio

Look at the list again: six stations, each **one component away from the last**, each unlocking a
verb you didn't have, each one making the next make sense. That isn't a lesson plan that happens to
resemble a progression game. **It is one**, and noticing that changes what to build, because
Factorio has already solved problems this design has.

| Factorio | CAM Construction Set |
|---|---|
| **Tech tree** | The component inventory. Start with one plane, a Moore former, a table. Unlock the plane shifter (echo), the phase generator (Margolus, and reversibility with it), the demon (Creutz), the selector (phase matrix), the opcode field (RISCA), the layer bus, asynchrony (MFM). |
| **Belts and inserters** | Wires between stages. The core verb in both is *routing* — Factorio routes material between machines, this routes bits between planes. |
| **Blueprints** | A painted RISCA region. The eyedropper already copies **behavior, not appearance**, and because binding is data, blueprints are savable, diffable, shareable. |
| **Pollution and biters** | `heatShiftPollution` is already a variable in the engine. The honest antagonist is **entropy**: chaotic neighbors eat your structures, stray gliders crash your logic, anneal domains encroach. Defending a hand-built machine against a chaotic region is real CA content, not a theme. |
| **Craft by hand → assembler → assemblers making assemblers** | The [Futamura ladder](#the-futamura-projections-in-ca-terms), exactly. |
| **Launch the rocket** | The ["historically accurate" test](#historically-accurate-as-a-test-not-a-claim) — a win condition with a **published answer key**, since the book prints the figures your machine has to reproduce. And as in Factorio the post-launch game is the real one: [break it on purpose](#then-break-it-on-purpose). |

### The scarcity is real, which is why it works as a game

Factorio is good because iron is genuinely limited and belts genuinely saturate. This has the same
property and usually hides it:

- **The cell is an inventory slot.** Eight bits. Echo wants one or two, heat wants four, a RISCA
  opcode wants four, Brain wants two, a Creutz demon wants a few, a
  [moveable-RISCA direction](schedulers.md) wants four. **You cannot have every layer at once**, and
  deciding what your cell is made of shows up on screen within one frame.
- **The address budget doubles per tap.** Nine bits is 512 entries and free; sixteen is 64K and the
  real CAM-6; forty-one is an MFM event window and no table exists. That's the
  [tabulate-or-approximate decision](#where-the-table-stops-being-the-answer) arriving as a resource
  constraint the player *feels* instead of a paragraph they skip.
- **Frame time is the belt.** Stages cost passes over the grid, fusion buys them back, and the meter
  is right there.

Three real budgets — bits, address space, milliseconds — trading against each other. That's a game
economy, and it happens to be the actual engineering.

### And the trap, named out loud

A tech tree is a lock, and **this document's whole complaint is that CA toys hide the machine.**
Gating the neighborhood former behind three hours of play is the same sin in a friendlier hat — the
same loss as [Electropaint shipping with the sliders
hidden](turn-tables.md#prior-art-and-its-better-than-what-i-specified).

So the tech tree is a **suggested path, never a gate**. A sandbox with every component sits on the
front door next to the campaign, available from the first second. Progression is opt-in —
homefun, not homework. An ordering is a gift; a lock is a tax.

Which is also the Will Wright answer. His games have no win condition:
they're toys with scenarios attached, not campaigns with a sandbox attached. Same content, opposite
default. Build it that way round and the whole Factorio structure is still there for anyone who
wants it.

## "Historically accurate" as a test, not a claim

The target is a configuration that **is** a CAM-6, and the way to make that mean something
is to make it falsifiable:

> Assemble the CAM-6 patch, load the **Forth rules printed in the book**, run them, and
> check the output against **the book's own figures**.

That's a real acceptance test with a published answer key, and it's the same contract the
existing `CAM6.js` already honors — book Forth rules compiled to lookup tables, imported
and matched. Passing it earns the word "accurate." Until then the honest phrasing is
"CAM-6-shaped."

**To verify before claiming fidelity:** the sub-array organization and plane depth, the exact
neighborhood tap sets and their address-line ordering, table width, the phase and event-
counter details, and how ganged boards actually exchanged data. Those come from the book and
from the CAM-6 Forth sources — not from memory, and not from this document. The
letter to Norman
already flags that its "8 bits in, 8 bits out" framing is the essential kernel rather than
the real datapath. Same caution applies here, and Norman is the person who can settle it in
one sitting.

## Then break it on purpose

Once the accurate configuration exists and passes, everything interesting is a modification
of a working reference:

- **Neighborhoods that never existed** — hexagonal, aperiodic, distance-2, or one wired from
  a picture.
- **Tables from anywhere** — hand-painted, learned, imported from an image, generated by
  another CA.
- **Instruments as plugins** — Jim Crutchfield's structural-complexity readouts (excess
  entropy, ε-machines) as a meter you clip onto the bus, next to the histogram.
- **Views as plugins** — cells as animated SimCity tiles, cells as sound grains
  (Musical Gas), 1+1D space-time diagrams.
- **The continuous half** — a warp/feedback engine on the same bus, which is where this
  meets WarpOMatic and the
  Crutchfield machine. §5 of Crutchfield's 1984
  paper argues video feedback and lookup-table CA are one family; a shared component bus is
  what that claim looks like when you build it.

And every patch is a document: shareable as a URL, diffable, forkable, with the wiring
visible rather than buried in a config file.

## Why this needs both visual paradigms

Worth stating plainly, because it settles an open question in the
Snap! engines doc, which lists blocks and patch
cords as complementary without saying where they meet. **This is where they meet.**

- **The rule is control flow.** "Count the neighbors, compare, decide" is a procedure, and
  Snap!'s first-class procedures are exactly right for authoring it and handing it to a
  compiler block as a value.
- **The machine is data flow.** Planes, formers, tables, and instruments are boxes on wires
  with data moving between them — Bounce-shaped, not
  block-shaped. Drawing a datapath as nested blocks would be a lie about its structure.

So the honest build is Snap! blocks for rules, hosted inside a patch-cord canvas for the
machine — which makes CAM-6-in-Snap! the first concrete reason to build the bridge, rather
than a nice idea deferred forever.

## Retire the XML. Generate the JavaScript. Believe in the JIT.

The monolith composes rules through a **commented XML string-templating system**. It works,
it got a lot done, and it should go. Its problems are structural rather than cosmetic:
it's stringly-typed, so nothing is checked until it runs; it has no composition semantics, so
"combine these two rules" isn't an operation, it's a paste; and meaning ends up in comments
the parser can't see, which makes the config a document pretending to be a program.

The replacement is **higher-order composition plus code generation**.

**Rules become values.** A rule is a function; a layer is a function; composing them is
function composition. In Snap! that's free — first-class procedures and lists are the
language, so `compose (rule) with (layer)` is an ordinary block that takes procedures as
inputs and returns one. In TypeScript it's just functions. Either way "combine these" becomes
an operation with a type, instead of template expansion with a prayer.

**Then emit JavaScript and let V8 compile it.** Don't interpret the composed structure per
pixel, and don't reach for WASM. **Generate specialized source for the exact configuration
that's currently wired up**, and hand it to the JIT:

- A disabled layer **disappears from the source**, rather than costing a branch per cell per
  frame.
- A constant phase offset **inlines its kernel**; the bank and the selector evaporate.
- The scheduler is **specialized** — the scan loop generated for four-rotation cycling is a
  different loop from the synchronous one, not the same loop with a mode flag.
- Everything downstream is straight-line, monomorphic code, which is exactly the shape a
  modern JIT is good at.

This is **Vanessa Freudenberg's** lesson from SqueakJS,
and the repo already states her principle: **target JS, not WASM** — generate source and
trust the JIT, because the JIT has decades of adaptive optimization in it that a
hand-written interpreter will never match. She was right, and it's the right call here for
the same reasons.

It also closes the loop the letter to Norman
opens. That section traces why `CAM6.js` runs fast — Self's inline caches and adaptive
optimization → Strongtalk → HotSpot → V8 — and asks *who JITs the jitter?* With codegen the
answer gets better: **the rule compiler and the JIT become two stages of one pipeline.**
Toffoli and Margolus's Forth compiled a readable rule down to a table that hardware executed;
now a block-composed rule compiles down to JavaScript that V8 executes. Same three-layer
architecture, one era later.

**And it generalizes the book's contract instead of abandoning it.** The lookup table is the
right target when the state is small and the neighborhood is finite — that's most of the
book, and those rules should still compile to tables and still match the book's figures. But
the table can't express many-state cells, continuous values, error diffusion carrying a
remainder across cells, or MFM event windows. So the compiler gets **two back ends**:

> **Table when it fits. Generated code when it doesn't. One front end either way.**

The user writes a rule once; the compiler picks the representation. That's the honest 2026
version of "don't evaluate the rule in the inner loop."

### Three binding times, not two

Stated as a pipeline: **JIT the machine into Korz, and JIT the Korz into JS and WebGPU shaders.**
That's right, and it's worth splitting because the two "JIT"s are different operations and there's a
third underneath doing most of the work.

| Stage | Operation | Binds at | Produces |
|---|---|---|---|
| 1 | **Reification** — the wired panel becomes declarative data | interaction time | a Korz spec: savable, diffable, postable, and readable by all three audiences |
| 2 | **Specialization + codegen** — data becomes source | patch-change time | JS for the serial parts, WGSL for the parallel ones |
| 3 | **The JIT you didn't write** — source becomes machine code | execution time | V8 and the shader compiler doing decades of adaptive optimization for free |

Stage 2 is the [first Futamura projection](#the-futamura-projections-in-ca-terms) performed at
runtime, which is why the ladder in this document isn't decoration. And stage 1 is what makes the
middle artifact exist at all — the reason a patch can be a file, the
[map can be the save file](#that-ladder-is-a-tech-tree-and-this-is-a-factorio), and an LLM can read
and write your machine.

**What triggers regeneration is the whole engineering problem.** A shader recompile costs
milliseconds to tens of milliseconds and must never happen per frame, so the Korz spec has to
separate **structural** bindings (adding a layer, rewiring a selector — regenerate) from **dynamic**
ones (`frob`, temperature — pass as a uniform, never regenerate). That separation is a binding-time
analysis, and `CAM6.js` already has a hand-written version of it in every rule's `paramsUsed`.

The interesting case is the middle: a parameter that's *usually* constant. Specialize on it
speculatively, guard the assumption, and deoptimize when it changes — which is exactly what a real
JIT does. Which means **the CA compiler should steal inline caches and dynamic deoptimization from
Self**, and Self is David Ungar's, sitting in the same repo as the
language stage 1 targets. Korz is his design; Self's implementation techniques are its natural
runtime.

Three consequences follow that are ordinary JIT engineering and should be built as such:

- **Tiered compilation.** Interpret immediately so the patch is live the instant you wire it, then
  promote to generated JS, then to WGSL, in the background as the patch stabilizes. You cannot
  create a WebGPU pipeline mid-frame without a visible hitch, so the compile must be async and the
  old pipeline keeps running until the new one is ready.
- **A code cache keyed on the spec's hash.** Same patch, same shader, no recompile — and precompiled
  shaders for the common configurations give you a warm start.
- **The JS/WGSL split is decided by declaration, not by guesswork.** Per-cell parallel stages with no
  carry go to WGSL; serial carries, small populations, and hand interaction stay in JS. The
  dependence-cone declarations exist precisely to
  make that partition mechanical rather than a judgment call.

### Ace: Gosling already built stage 2, for exactly this problem

**James Gosling** wrote **Ace** in 1989 to generate the bitblt and
vector routines in Sun's Shapes library, and it is the closest ancestor this compiler has. Not
*similar to* — the same problem. Ace specialized a graphics inner loop across pixel depth × all 16
rasterops × line orientation × plane mask × clipping; this machine wants to specialize a cell loop
across neighborhood × layer stack × scan order × coherence × wrap. **`Life_Echo` and `Life_Heat`
are hand-expanded bitblt cases**, and Ace is the tool that makes hand-expansion unnecessary. One
page of source in, twenty pages of tight special cases out.

It's a syntax-tree rewriter rather than a text macro processor — rules are `$replace pattern $with
replacement` over parsed C, with metavariables `$0 $1 $2` and a side-effect-free variant `$f0` for
patterns that may only match pure trees. That distinction is the whole reason it can reason about
the code instead of merely pasting it, and it's the same complaint this document makes about the
[commented-XML string templating](#the-configuration-language-goes-away) it replaces.

**The sentence that settles the tiered-compilation question** is Gosling's aside about `$pullout`,
which hoists a loop-invariant test out of a loop by duplicating the body:

> Eliminating this is a form of code motion that no compilers use since it leads to an exponential
> growth in code size, but in some cases it is justified.

That is the proof **stage 3 does not subsume stage 2.** V8 and the shader compiler will not pull
`if (wrap)` out of your per-cell loop, because a general-purpose optimizer cannot risk doubling code
size per hoisted test and has no idea the loop runs 65,536 times a frame. You know that. So the
specialization has to happen upstream, deliberately, by someone holding the domain knowledge — which
is the entire argument for generating source rather than interpreting a composed structure.

Five operators worth taking more or less as they are:

| Ace | What it does | What it becomes here |
|---|---|---|
| `$pullout(c)` | hoist a loop-invariant test, duplicating the body | `wrap`, `polarity`, a disabled layer — each pulled out of the cell loop |
| `$assume(c, body)` | compile `body` knowing `c` holds | the guard body after a speculative specialization succeeds |
| `$switchout(N, e, set)` | expand a switch over a declared finite value set | a **Korz dimension with finite values** — this is literally dimensional dispatch |
| `$tradeoff(fast, small)` | pick by estimated time vs. space | the answer to *which* configurations get specialized |
| `$repeat(n)` | emit the loop shape the target likes | Gosling's expanded to `do {…} while (--count != -1)` to hit a 68020 `dbra`; ours emits the shape the WGSL compiler vectorizes |

Two of those deserve more than a table row.

**`$assume` is user-defined, and that's the deep lesson.** Ace has no built-in knowledge of Boolean
algebra. DeMorgan's laws and the comparison negations (`!($0 < $1)` → `$0 >= $1`) are ordinary rules
in a library, `$assume` is defined on top of them via `$let`, and `$pullout` is defined on top of
`$assume`. So **the specializer's knowledge is data, extensible by whoever is writing the rules** —
which is the same argument as [rules as values](#the-configuration-language-goes-away) applied one
level up. The CA compiler's rewrite knowledge belongs in the Korz layer beside the rules, not
hardcoded in the generator.

**`$tradeoff` is a cost model, and it answers the code-cache explosion problem.** You annotate
branch probability with `$P(e)` and loop trip counts with `$trips(n)`, and two knobs decide: `pthresh`
(specialize when execution probability exceeds it) and `mingain` (…but only if the fast version wins
by that percentage). Which gives a principled answer to *what* to specialize rather than a vibe: a
256×256 grid is 65,536 trips and always earns the fast path; a hundred-cell tool stroke doesn't; a
rarely-selected rule variant takes the small version and stays out of the cache. That's exactly the
budget the [code cache keyed on spec hash](#three-binding-times-not-two) needs and doesn't otherwise
have.

**Ace and Self are the two halves, and this compiler wants both.** Ace specializes *statically* on
*declared* probabilities, aggressively, ahead of time. Self specializes *dynamically* on *measured*
feedback, speculatively, with deoptimization when the guess breaks. So: Ace's `$pullout` and
`$switchout` at patch-change time for the structural bindings, Ungar's
inline caches and deopt for the usually-but-not-always constants. The criterion for which mechanism
gets a given parameter is whether its value is *known* when the patch changes or only *observed*
while it runs.

Two engineering details from the manual page that every codegen system rediscovers painfully:
Ace's `-lnc` flag emits **line numbers as comments** so the debugger steps through generated code
while you can still find the source line it came from — and generated output was created mode `444`
to stop you editing the file that's about to be overwritten. Both belong in the
[readable-generated-source panel](#three-binding-times-not-two) below.

**The paper's large worked example is a Bresenham vector routine**, and its generated cases carry
comments like *"going right, x is the major axis, the line is neither horizontal nor vertical"* —
the same eight directions that [`schedulers.md`](schedulers.md) enumerates as Bresenham particles
and pie-menu patron saints. Same algorithm, same specialization axes. Which makes the specialized
cases in that paper a worked example of what a scheduler plug-in compiles to, already written down.
Ace's `$scanshape` is the other half: a **user-defined iterator that takes a code block as its
body**, which is `Iterator<Site>` with handlers, in 1989.

What doesn't transfer is the deployment. Ace was ahead-of-time source-to-source on C, with no
runtime and no JIT underneath. Generating JS and WGSL text at runtime is a far easier problem, and
the browser hands you the back end Gosling had to do without. **The technique transfers; the
plumbing got cheap.**

Two more reasons this is the right move for a *teaching* system specifically:

- **The generated source is readable, and should be shown.** Put it in a panel. You snap
  blocks together and watch the JavaScript for your machine appear, then set a breakpoint in
  it. A lookup table is opaque and a WASM blob is worse; generated source is the most
  inspectable artifact of the three, which matters more here than in a production engine.
- **It makes the pipeline itself a lesson.** Rule → composition → generated code → JIT →
  machine code is the same story as rule → Forth → table → TTL, and a student who has seen
  one can be shown the other.

**The honest caveats:** generated code has to be regenerated whenever the configuration
changes, so the edit-to-running latency needs watching in a live-coding context; and the hot
loops have to stay monomorphic or the JIT's help evaporates, which is a real constraint on
how clever the generator is allowed to be. Neither is a reason not to do it. Both are reasons
to measure.

### Pause is the identity rule, and the compiler makes it free

There's a rule already in the RISCA opcode set that does nothing: **`C`** — copy center to center.
Every layer set to `C` is a universe that keeps running and never changes. Which means **the
simulation never stops; stopping is just selecting the identity rule.** There is no paused state, no
`if (running)` in the loop, no second code path that has to be kept in sync with the first. The
engine has one mode.

And then the specializer deletes it. Identity's residual program is the *empty program* — the
degenerate case of `$pullout` where every stage that reads and writes the same thing evaporates and
the generated kernel is nothing at all. So **"paused costs zero" is a theorem the compiler proves,
not a feature anybody implements.** It's also the cheapest possible demonstration that the codegen
story is real: show the generated-source panel, set the rule to `C`, and watch the source go empty.

Three things follow that are more than tidiness.

**It justifies a claim made earlier on credit.** This document already says a disabled layer
*disappears from the source* rather than costing a branch per cell per frame. The reason that's
sound is that rules compose, composition has a neutral element, and **a disabled layer is that
neutral element** — identity is removable under composition by definition. So the empty slot, the
disabled layer, and the paused machine are one object with three names, and the optimization is
algebra rather than a special case in the generator.

**Time becomes an exponent.** Running rule `R` for *n* steps is `R^n`, and `R^0` is identity — so
pause is step zero, not a separate concept. On the reversible Margolus branch the group closes:
`R^-1` is the backward step, and a time slider is literally an integer exponent on a rule.

**The sharp edge is that "pause" has to say *which stages*.** The rule isn't the only thing in the
pipeline — there are drawing tools, analyzers, the
display, error-diffusion accumulators, and `frob`'s spring-return. Pausing the physics while the
brush stays live is exactly what you want when painting a pattern before you run it; pausing
everything including the meters is a different operation. So the pause button is **identity selected
per stage** — a mask over the stage list — which is the layered pipeline paying for itself again.
The bug it prevents is specific and the kind that hides for years: a `frob` that keeps
spring-returning toward `frobTarget` while you think you're paused hands you a different machine
when you unpause than the one you stopped.

**And elision is only sound when the clock is an input.** If sites are chosen by
`hash(x, y, t, seed)` and you delete the identity step, `t` must not advance as a side effect of
having run — because any surviving stage that reads `t` would then observe the step you optimized
away. That's the [pure-function discipline](schedulers.md) stated as a soundness condition rather
than a style preference: **the clock is data the stages read, never a side effect of running.**

Ackley's machine already takes this position, from the other end: in MFM, `Empty` is an *element*
with a behavior, not the absence of one. Sites are never missing; they hold something that does
nothing. Same design, arrived at because an indefinitely scalable machine can't afford a special
case for "nothing here" either.

## Show beats

1. **Assemble Life on air**, from empty canvas to running glider, naming each block as it
   goes down. Under five minutes if the components are right — and if it isn't, that's the
   design review.
1. **Same rule, four schedulers.** Synchronous, serpentine, Margolus blocks, and MFM random
   event windows, running side by side on identical seeds. Which structures survive is the
   whole argument for exposing iteration order, and it needs no explanation to be legible.
2. **One wire, different universe.** Swap Moore for Margolus live and let Norman explain why
   the physics changes.
3. **Open the table.** Show the actual lookup table filling up as the compiler runs, then
   hand-edit one entry and watch the universe change. Nobody ever gets to see this.
4. **Pause it and show the source vanish.** Set the rule to `C`, the identity, and let the
   generated-source panel go empty — the universe is still running, the compiler just proved that
   running it costs nothing. Three seconds, and it's the whole specialization argument made visible.
5. **Grade the fidelity.** Run the book's rules against the book's figures with Norman
   watching, and let him call out what's still wrong.
6. **Then break it.** Wire something the hardware could never have done, with the person who
   designed the hardware in the room.

## See also

- `../norman-margolus/the-cam6-demo-for-norman.md` — the letter; Act 2 is this
- `../norman-margolus/the-cam6-demo-transcript.md` — the demo transcribed, with the jargon defined
- [`cam6-cellular-automata-machine.md`](cam6-cellular-automata-machine.md) — the existing monolith and its lineage
- `snap-visual-engines-fundable-goals.md` — the four-engine strategy this is the first slice of
- `levity-bounce-space-seed.md` — the patch-cord half
- `../jens-monig/README.md` · `../brian-harvey/README.md` — Snap!, integration partners
- `../dave-ackley/README.md` — Movable Feast Machine: random event windows, asynchrony, indefinite scalability, robust-first
- `../vanessa-freudenberg/README.md` — SqueakJS; target JS not WASM, and believe in the JIT
- `../jim-crutchfield/positive-feedback.md` — why the continuous half belongs on the same bus: Physica D 10, §5
- `../jim-crutchfield/ideas.md` — the meters this front panel is supposed to carry, and the 1989 question that wanted them
- `../david-ungar/korz/examples/margolus-rules.md` — the rule catalog written as Korz slots; the front end this back end compiles
- `../david-ungar/korz/examples/layered-rules.md` — the same argument checked against `CAM6.js` line by line: echo/heat/anneal/RISCA as stages, drawing tools as a composition step, and a suspected heat-sum bug copied five times
- [`schedulers.md`](schedulers.md) · [`.yml`](schedulers.yml) — the iteration-order axis opened out: six dimensions, space-filling curves, Bresenham turtles and their breeding algebra, handlers, and the meta-iterator
- [`turn-tables.md`](turn-tables.md) — the control that drives every parameter above, including `ising_metropolis`'s temperature. A turtle's direction is an angle, so the knob and the walker are one control.
- `../rudy-rucker/README.md` — CA Lab / CelLab: the other rule catalog that escaped the CAM-6, and the other person who owned one

*Status: design, not built. The components are a proposal; the fidelity claims are
unverified pending a pass through the book with Norman.*
