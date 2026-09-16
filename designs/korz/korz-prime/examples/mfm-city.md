# The city that routes itself, as Korz slots

*Spectrum: **MOOLLM-integrated** — it reads a specific published system. Sidecar:
[`mfm-city.yml`](mfm-city.yml).*

The subject is Trent R. Small's self-generating, self-routing city, built on
Dave Ackley's **Movable Feast Machine** — a spatial computer with
no global state and no absolute addressing, where a program is a population of small typed agents
called *atoms* and every atom sees only a 41-site window around itself. The city grows from one
street atom into streets, sidewalks, buildings and cars, and then the cars find buildings they
cannot address. Paper ·
summary ·
[demo](https://www.youtube.com/watch?v=XkSXERxucPc). There's a browser reimplementation in
TypeScript, **[MFM-JS](https://github.com/walpolea/MFM-JS)** by Andrew Walpole, running at
[mfm.rocks](https://mfm.rocks) — which is the version you can actually poke at, and the one Don
corresponded with Andrew about.

## Why this one and not another Margolus rule

The [Margolus set](margolus-rules.md) is deterministic, synchronous, 2×2, and made of stateless
integer cells. The city is none of those things, and every property it breaks is a property this
design claims to have factored out:

| The city needs | Which axis |
|---|---|
| random asynchronous site selection | site selection |
| one exclusive event window at a time | coherence |
| a 41-site Manhattan disc | neighborhood as a declared shape |
| swap as the transport primitive | transport |
| typed objects with data members, not integers | the Korz object model |
| **a hard bit budget** | **nothing — this is the hole** |

Five of six were already there, which is the good news and also unsurprising, since
[`schedulers.yml`](../../../cellular-automata/schedulers.yml) was written partly *from* MFM. The sixth is
what the exercise was for.

## The bit budget has to be a type check

MFM gives an atom 96 bits, 71 of them general-purpose, and the paper does its arithmetic by hand:
24 building types × 2 bits of distance = 48 bits of sidewalk map, leaving 23 for everything else.
Two bits saturates at three blocks. The author names this as the study's central limitation and
notes that twenty more bits would have reached seven.

So the paper's main finding *is a bit-budget overflow*, discovered by reasoning. **A configuration
language for this architecture that cannot count bits has missed the architecture.** Slots need
declared widths, the compiler sums them per element, and blowing 71 bits is a build error with the
arithmetic shown — not a runtime surprise and not a comment. The second-order win is that once the
budget is a quantity the compiler holds, it can propose the trade: drop to twelve building types and
your map reaches seven blocks.

There's a coupling here worth noticing too. The canalization routing method adds a 24-entry table to
every intersection, so **changing the routing method changes the bit budget.** Those two knobs are
not independent, and a design that shows the dependency is telling you something a pair of
sliders wouldn't.

## Algorithm 1 is a saturating Bellman-Ford, and the saturation is the result

The sidewalk mapping rule — border a building, set your entry to zero; otherwise take the minimum
over your neighbors, and one more than the sidewalk across the street — is a local, asynchronous
**distance transform**, one scalar field per building type, relaxed in place.

The clip is the interesting part. Two bits means the field flattens at three blocks, and **a flat
gradient carries no information**, so beyond three blocks a car is routing at random. Which
reframes the results table: sidewalk routing isn't "better than random," it's *random except within
three blocks of the answer*, and getting 98.2% out of that is the actual achievement. The 91% random
baseline isn't a curiosity to be surprised by — it's the floor the whole system falls back to
whenever the gradient runs out.

Twenty-four scalar fields, relaxed locally, read by something that steers. That's
[procedural fields](layered-rules.md) and the direction field of moveable RISCA, reached from the
other side.

## Three routing methods is the `Life_Echo` problem again

The paper compares Random, Sidewalk-Only, and Intersection-Canalization: three named points with
nothing reachable between them. That's the same shape as
[`Life_Echo` and `Life_Heat`](layered-rules.md) — a naming convention standing in for a dimension.

Decomposed, it's four independent axes: gradient source (none / sidewalk map / anything else),
memory (none / last direction per type), **memory trust** (how often to re-evaluate rather than
believe the cache — a continuous knob the paper describes in prose and never varies), and U-turn
policy. The three published methods are three corners of that box, and the interior is unexplored.

Then the nice part: **Figure 3 is arrival rate and Figure 4 is gas.** Those are two meters. Ten runs
averaged into a bar chart becomes a live panel with a knob, and the paper's entire result turns into
a sweep you can feel with your hand — the same argument as the
two-meter ask, on a completely different subject.

## Canalization is a polymorphic inline cache

Each intersection remembers the last direction it sent a car *of each type*, and re-evaluates less
often, trusting its memory. Translated: the intersection is a call site, the car's destination type
is the receiver type, the outgoing direction is the cached target, there are 24 possible types, and
the invalidation policy is time-based and tunable.

That is a polymorphic inline cache. And the measured result is the inline-cache value proposition,
stated exactly: **+0.02% accuracy, −15% cost.** The cache doesn't change the answer, it changes the
work.

Which is a good coincidence, since inline caching is [Ungar's](../../README.md), this is his examples
directory, and the [CAM compiler](../../../cellular-automata/cam-construction-set.md) already names Self's
inline caches as its runtime for usually-but-not-always-constant parameters. Small was solving a
traffic problem and reinvented polymorphic inline caching in a traffic light, with a decay policy.
Neither literature noticed.

## The city is `grid-as-rooms` running, and it adds a case

[`grid-as-rooms`](grid-as-rooms.md) argued that a lattice and a room graph are one structure at
different exit-wiring regularities. The city is the specimen: intersections are nodes, streets are
edges, buildings are typed rooms, and a car seeking a building type is doing graph traversal over a
graph **embedded in** a lattice.

It also corrects that file's representation story. `grid-as-rooms` proposed shape-by-reference plus
an array of dicts, with connectivity living in the shape. Here the shape stays formulaic — it's an
MFM grid, uniformly wired — and the room graph is **painted into the cell contents**. So
connectivity isn't always structural; it can live in the payload. "Is this exit structural or is it
data?" turns out to be a real question with a performance answer rather than a philosophical one.

## What the exercise put on the design's todo list

New: **bit-budget arithmetic** as a build-time check; **two distinct transport primitives** (streets
overwrite, cars swap — and the type system shouldn't let you confuse them); **lifespans** (cars have
gas, sidewalks age before building) matching the fuse queue in `grid-as-rooms`; **local counting**
("buildings reproduce up to a maximum size" with no global count is a recurring MFM idiom that needs
a supported form); and **saturating fields**, where the clip is a designed parameter rather than an
accident.

Confirmed already present: random asynchronous scheduling, exclusive coherence, swap transport,
typed cells with members, and the decomposition of named variants into dimensions.

One discipline the translation forces: intersection odds, random routing, and random site selection
all want randomness, and an RNG stream destroys replay. It has to be `hash(x, y, event_count, seed)`
— the same purity rule as the [dither discipline](../../../cellular-automata/cam-construction-set.md). A
city that regrew differently is a bug report you can send someone.

---

*Paper by Trent R. Small (UNM), advised by Dave Ackley, funded by Google. Mirrored with attribution;
see portrayal standards.*
