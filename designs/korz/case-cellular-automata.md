# Case study: cellular automata — Korz at absolute zero

*Part of the [Korz cauldron](README.md). The
[design](korz-prime/README.md) puts a strict tier and a soft tier on one
semantics. A cellular automaton is what the strict tier looks like at
its logical extreme — every dimension frozen, every guard decidable,
the whole slot space crystallized into a lookup table.*

## Neighbors are dimensions

A cell's update rule dispatches on its neighborhood, and the
neighborhood is an implicit context: von Neumann is five named
dimensions (`c`, `n`, `s`, `e`, `w`), Moore is nine, a Moveable Feast
Machine event window is forty-one. The rule table is a set of guarded
slots over those dimensions — and it is **total and decidable**: every
context matches exactly one rule, zero ambiguity, nothing left latent.
A cellular automaton is the extreme strict tier — Korz fully
crystallized, the specificity lattice flattened into a complete lookup
table. **Korz at absolute zero**: Zork froze five dimensions
([case-zork.md](case-zork.md)), The Sims froze two, and the CA freezes
them all the way down to the compass rose.

There's a pronoun grammar hiding in that mapping, and it's the real
reason CAs land so neatly in Korz. Object-oriented programming is
**"this"** — first person singular, one privileged receiver, the world
sorted into me and them. A cellular automaton is **"us"**: I am at the
center, surrounded by neighbors, and the rule dispatches on all of us
at once — multiple dispatch as a way of life, no cell ever addressed
in the second person. And there's a gradient inside the "us": a Moore
rule reads all of us but writes only *me* — "I among us" — while the
Margolus block below removes even the center: reads us, writes us,
four receivers and four outputs, first person plural with no singular
left. Every cell is simultaneously the center of its own neighborhood
and a neighbor in eight others — perspectival symmetry, which is just
Korz's subjectivity said in grid coordinates.

## The classic rule families are guard algebra wearing lab coats

- **Totalistic rules guard on derived dimensions.** Life's B3/S23
  never looks at individual neighbors — it guards on their *sum*:
  `{center: dead, live_neighbors: 3} → born`. An aggregate of
  dimensions used as a dimension. (An open question for David: are
  derived dimensions ordinary dimensions, or a new kind of guard? The
  Margolus bullet finds a second species — coordinate transforms, not
  just aggregates. See [ask-david.md](ask-david.md).)

- **Rotational symmetry is guards quotiented by a group.** A symmetric
  rule doesn't enumerate four rotations; it matches the *orbit*, not
  the point — dispatch modulo group action, a symmetry declaration
  collapsing many contexts into one equivalence class.

- **The Margolus neighborhood is no-privileged-receiver in silicon.**
  A 2×2 block with *no center cell* — four sites dispatch
  symmetrically, none of them "the receiver" — and the alternating
  partition makes the block phase a **time-and-space parity
  dimension**: `T` decides which tick's partition you're in, `V` and
  `H` decide which corner of your block you are, so the same four
  cells match different slots on even and odd ticks *and* the block
  boundaries themselves shift under your feet. Reversible rules make
  the slot set bijective — `git revert` as physics.

  And here's the head-tilt: the Margolus neighborhood **isn't new
  hardware, it's a derived coordinate system**. The CAM-6 cellular
  automata machine (Toffoli & Margolus's 1987 hardware, which Don's
  [CAM6.js](../cellular-automata/cam6-cellular-automata-machine.md)
  simulates in the browser) implemented it on plain Moore-neighborhood
  machinery: the block-relative dimensions `C`, `CW`, `CCW`, `OPP` are
  *functions* of the compass rose (`N S E W NW NE SW SE`) plus three
  phase dimensions — `T` (time parity), `V` (vertical phase), `H`
  (horizontal phase). Which physical neighbor is "clockwise from you"
  depends on where you sit in the block and which tick it is — a
  **change of basis over dimensions you already had**. That sharpens
  the derived-dimensions question: Life's `live_neighbors` is an
  *aggregate* (sum of dimensions), but `CW` is a *coordinate
  transform* (permutation of dimensions indexed by other dimensions).
  Same machinery, second species.

  Worked out as actual Korz slots — the classic block rules (billiard
  ball, critters, TRON, HPP gas, sand, dendrite, two Isings) plus some
  invented ones chosen to break the compiler in instructive places — in
  [examples/margolus-rules.md](korz-prime/examples/margolus-rules.md) and its
  sidecar [examples/margolus-rules.yml](korz-prime/examples/margolus-rules.yml).

  The rules complete the no-privileged-receiver story, and the name
for it is **multiple dispatch**. Single dispatch picks the method
from one privileged receiver (`cell.update(...)`); multiple dispatch
(CLOS, Cecil — and Kaleida's ScriptX, whose CLOS-like multimethods
Dan Bornstein implemented, as Don
recalls it) picks it from the joint types of *all* the arguments;
  and Korz goes one step further — dispatch on the whole **context**,
  where "arguments" and "environment" are just dimensions, and nothing
  is the receiver. A Margolus rule is exactly that: a generic function
  whose method is selected by the **joint state of all four sites plus
  the phase dimensions** — not `nw.update(ne, sw, se)` but
  `update{a, b, c, d, T, V, H}`, written **once, rotationally
  symmetric (dispatch modulo the rotation group), with four receivers
  and four outputs**. Every site is simultaneously an argument to
  dispatch and a result of it; the block updates as one atomic
  multimethod call. Korz's symmetric, receiverless message send was
  running in silicon in 1987. The crystallization pipeline shipped
  there too: CAM-6 rules were written in Forth and *compiled into
  lookup tables* — expressive description down to total dispatch
  table, exactly the Zork-compiler movement. The compiler-theory name
  for that movement is **partial evaluation**: the rule's parameters
  are static, the neighborhood is dynamic, and the table is the
  residual program. Crystallizing a Korz sea is the same operation
  with the guards as the static input — which means the strict tier
  isn't a separate mechanism, it's what a specializer leaves behind
  ([the arithmetic of when tabulation
  works](../cellular-automata/cam-construction-set.md#the-move-has-a-name-partial-evaluation-and-one-more-thing)).

- **The Moveable Feast Machine is the soft tier's physics.** Dave
  Ackley's MFM abandons the synchronous total table: events fire
  asynchronously and stochastically, and an element's behavior
  function acts on *whatever its event window actually contains* —
  including noise, decay, and corruption. That is deopt-not-segfault
  as a physical law: robust-first, survive > heal > function, guards
  written to tolerate partial matches instead of erroring on them. The
  MFM sits exactly on the tier boundary — strict elements, soft
  scheduling — and its indefinite scalability comes from refusing the
  strict tier's global synchrony the same way the soft tier refuses
  its global decidability.

The soft tier adds one more reading: a neighborhood can be a *pattern
coordinate* instead of per-site dimensions — `neighborhood:
glider-head` is a K-line guard, which is how humans actually talk
about Life (nobody says "dead cell with three live neighbors
northeast"; they say *glider*). Pattern names are the semantic
compression the strict table can't express and the soft tier gets
free.

## Minsky demolished the same receiver in a different substrate

["Why People Think Computers Can't"](https://doi.org/10.1609/aimag.v3i4.376)
(*AI Magazine*, 1982;
[full text](http://www.sci.brooklyn.cuny.edu/~sklar/teaching/f05/alife/papers/minsky-computerscantthink.pdf))
takes apart what Minsky calls the **"Single Agent" theory** — "that
deep inside each mind resides a special, central 'self' that does the
real mental work for us, a little person deep down there to hear and
see and understand what's going on," an idea that "underlies all
principles of law, work, and morality" no matter "how ridiculous it
may seem, scientifically." Most of what our "consciousness" reveals,
he says in the same breath, is just "made up" — so our minds are
**made up** in both senses: confabulated, and then decided, closed
around the confabulation.

Single dispatch is the Single Agent theory frozen into syntax —
`cell.update(...)` posits a little person deep down inside the object
who does the real work — and receiverless dispatch is *The Society of
Mind* stated as a calling convention: no agent in the society is "the
self," and the behavior lives in the joint state. Fitting that the
same man coined the K-lines this whole design runs on
([epistemics.md](korz-prime/epistemics.md)). He dissolved the privileged receiver
of folk psychology decades before Korz dissolved the one in message
sends.

The same Single Agent demolition earned Minsky a villain's role in the
LaRouche movement's 2001 "Cult of Artificial Intelligence" polemic,
which quotes these very lines as proof of degeneracy — one text, two
readers, opposite verdicts, which is itself a dispatch-on-context demo:
archived with commentary.

And Minsky wrote the capstone himself, in the same section: "In every
field, as Scientists we're always forced to recognize that what we see
as single things — like rocks or clouds, or even minds — must
sometimes be described as made of other kinds of things. We'll have to
understand that Self, itself, is not a single thing." Read that with
2026 eyes and a capital S: it names Ungar's language and predicts its
dissolution in one sentence, eleven years before Self shipped and four
decades before Korz. Ungar simplified objects to their bare essentials
by removing classes, and got Self — the JIT lineage that made Java,
JavaScript, and Lua fast. Then he removed the objects themselves. Or
rather, self itself: **Selfless self**, a sea of slots that assemble
themselves into virtual objects depending on how you look at them —
where "how you look at them" is the context binding, said in plain
English. Rocks, clouds, minds, objects: none of them are single
things; all of them are dispatch. The de-objectification of
object-oriented programming, in one motto: **there are more dimensions
than Self** — the language, the ego, and the guard list, all at once;
`rcvr` demoted to one dimension among place, time, mood, world.

## Crystallization targets — compile Korz to kernels

CAM-6 already proved the movement: Forth descriptions compiled into
total lookup tables. Generalize the back end and Korz becomes a
**source language for GPU kernels**. The soft tier (an LLM) reads a
Korz spec — dimensions, guards, neighborhood declarations, symmetry
quotients — and lowers it to:

- **PyTorch** — wildly specialized CA and image-processing flows as
  tensor programs, including **training and generation**: make the
  rule table differentiable and you're in neural-CA territory
  (Mordvintsev's growing CAs), where the crystallized table is the
  *result* of gradient descent instead of hand enumeration. Korz
  guards in, learned physics out.

- **WebGPU TypeScript** — better, because it runs where the audience
  is: in the browser, with `getUserMedia` putting the **video camera
  in the loop**. Camera → compute shader pipeline → canvas → camera:
  Jim Crutchfield's 1984 video-feedback paper proposed exactly this as
  its "variation (6)" — insert a digital computer into the feedback
  loop via a video frame buffer
  (his papers, annotated) —
  running live in a tab, forty-two years later. The 1984 control knobs
  map straight onto shader uniforms: rotation, zoom, and pan choose
  *which cells are your neighbors*, focus is the diffusion radius —
  dimension guards you turn with a slider instead of a lens ring.

The pipeline is the same in both cases: **describe in Korz, ask the
soft tier to crystallize, run the strict artifact on the GPU** — and
when a guard needs renegotiating, melt it back up a tier and
recompile. Zork-compiler movement, hot loop edition.

---

*Sibling case study: [case-zork.md](case-zork.md). The philosophical
thread continues in the [design](korz-prime/README.md) and the open questions in
[ask-david.md](ask-david.md).*
