# Korz examples — a spectrum, not a syllabus

*Part of the [Korz cauldron](../../README.md). The
[README](../../README.md) and [design](../README.md) carry the pure,
serious explanation and stay self-contained. This directory is where
the rest of the fun lives.*

An ensemble of practical and whimsical examples of how Korz and
Korz′ apply to a wide range of problems. The pieces run along a
spectrum:

- **Self-contained** — everything you need is on the page; no repo
  mythology assumed. Read these cold.
- **MOOLLM-integrated** — worked against live objects in the
  [MOOLLM](https://github.com/SimHacker/moollm) repo: characters,
  skills, experiments, designs. These introduce their cast properly,
  then lean into the shared canon — in-jokes permitted, because the
  serious explanation already happened somewhere else.

Each example states which end of the spectrum it sits on, up front.

## The exhibits

| Example | Spectrum | What it teaches |
|---|---|---|
| [troll-blend.md](troll-blend.md) | Self-contained intro → MOOLLM-integrated | Ambiguity policy: sample vs blend; coordinates as distributions; dispatch mixtures worn as visible anatomy |
| [sims-advertisements.md](sims-advertisements.md) | Self-contained (shipped commercial software is the canon) | Dispatch as an auction: scored advertisements, find-best-N dither, why argmax over lies is being deterministically conned |
| [moody-temperature.md](moody-temperature.md) | MOOLLM-integrated | Temperature as a context dimension; environments that write the dispatch context; media broadcasting coordinates; virtual vs API heat 2D map |
| [margolus-rules.md](margolus-rules.md) · [`.yml`](margolus-rules.yml) | Self-contained (classic CA rules are the canon) | Korz as a configuration modeling language: dimensionally parameterized block rules, orbit guards under declared symmetry groups, iteration order and coherence as plug-in dimensions, and what each archetype forces a compiler to support |
| [layered-rules.md](layered-rules.md) · [`.yml`](layered-rules.yml) | MOOLLM-integrated (reads a specific shipped codebase) | Reading `CAM6.js` and taking it apart: how to spot a naming convention that is a missing dimension, layers as pipeline stages instead of `if` blocks inlined per engine, bank-and-selector as one component, and drawing tools as ordinary stages — source × region × blend, with the stage *position* as part of the physics |
| [grid-as-rooms.md](grid-as-rooms.md) · [`.yml`](grid-as-rooms.yml) | Self-contained (a CA and an adventure map, both already familiar) | The bridge between the two case studies: a lattice and a room graph are one structure at opposite ends of the *exit-wiring regularity* axis. Non-reciprocal exits, portals as small-world rewiring, exits as an editable plane — and the bill regularity was paying, with specialize-back as the acceptance test |
| [mfm-city.md](mfm-city.md) · [`.yml`](mfm-city.yml) | MOOLLM-integrated (reads a published system) | Translating someone else's shipped rules: Trent Small's self-routing MFM city. Bit budgets the compiler must do arithmetic about, swap vs. destructive write as distinct primitives, a saturating distance transform whose clip *is* the result, three published routing methods refactored into four axes — and a traffic light that turns out to be a polymorphic inline cache |
| [mtg-layers.md](mtg-layers.md) · [`.yml`](mtg-layers.yml) | Self-contained (the published rules are the canon) | The dispatcher that shipped to millions: Magic's CR 613 as ordered dimensions, base state vs projected state as E-Prime enforced by tournament rules, effects that **rewrite other effects' guards** (the wall Korz has not hit), and ambiguity resolved by legislated total order because a game in progress may not raise an exception — plus the largest prose-to-guard translation corpus in existence, with a judge program as its soft tier |
| [df-procedural-magic.md](df-procedural-magic.md) · [`.yml`](df-procedural-magic.yml) | Self-contained (a shipped game's announced design, in the developers' words) | **Generating the dimension lattice**: Dwarf Fortress deletes the privileged effect list the way Self deleted classes. Per-world magic fitted to a procedural creation myth, one coordinate unbinding mid-game so thousands of agents re-dispatch (the paper's assertions trick with a body count), affordance advertisements as generated Sims auctions, three modes gathering one world along different axes — and an O(n²) opinion dispatch whose fix was a cache |
| [fluxx-nomic.md](fluxx-nomic.md) · [`.yml`](fluxx-nomic.yml) | Self-contained (published rules and the designers' own words) | **The context, made physical**: Fluxx's tableau *is* a Korz context — Draw, Play, Limit, Other as dimensions, one coordinate bound each, rebinding as the only operation, so conflict is unrepresentable and no layer system is needed. Overrides physically cover the slot they shadow; the win predicate is a coordinate that starts *unmentioned*. Behind it, Suber's Nomic (1982, Hofstadter's column) poses the self-amendment fixpoint as jurisprudence — with a failure literature |
| [purpose-dimension.md](purpose-dimension.md) · [`.yml`](purpose-dimension.yml) | MOOLLM-integrated | **The dimension that answers *why***: `rcvr` is the *what*, and the paper's four axes never say what a call is *for*. Ambient propagation is exactly what a setpoint needs, so Wiener's 1943 move lands in the guard lattice whole — reference signal as coordinate, pursuit as dispatch, error reduction as specificity. One `explain()` with four guards instead of a mode flag; a fridge that advertises nothing during an evacuation; a bare-name guard that refuses to run without a why. And the three breakages: a normative tie is a dilemma rather than a compile error (so it deopts and gets logged), goals are simultaneous while a context binds one coordinate per dimension, and whoever binds it at the top owns the telos underneath — which is fine when the binding is a coordinate you can print, and is a loss function when it is not |

The Margolus set is the runnable companion the
[cellular automata case study](../../case-cellular-automata.md) was waiting
for; it crystallizes into the
[CAM Construction Set](../../../cellular-automata/cam-construction-set.md) back end.
`grid-as-rooms` joins that case study to the
[Zork](../../case-zork.md) one, which had already named them siblings, and
`mfm-city` is the specimen that claim was asking for — a room graph
painted into a lattice, in published code.

`sims-advertisements`, `mtg-layers`, `fluxx-nomic` and
`df-procedural-magic` are the **shipped-system set**: mass-market games
that arrived at dimensioned dispatch with no reference to programming
language theory, which makes them evidence rather than illustration.
They split the mechanism cleanly. Magic is the *dispatch* half — a slot
sea with a legislated total order. Fluxx is the *context* half — one
coordinate bound per dimension, rebinding as the only move, conflict
unrepresentable. The Sims scores and samples; Dwarf Fortress generates
the dimensions and flips them mid-play.

Read together they replace the obvious question ("does it have
dimensions?") with a better one: **when is the lattice authored, and by
whom?** — design time, press time, play time by rebinding, play time by
amendment, or world-gen. `fluxx-nomic` carries that table, and it puts
Korz at the most static end of a spectrum whose other end has been
commercially successful since 1997.

Dwarf Fortress also settles `grid-as-rooms`'s open bet a second time:
it does not sit in the middle of the regularity axis, it serves *both
ends over one world*.

`purpose-dimension` is the odd one out, and deliberately: it is the
only example proposing a dimension the paper does not have, rather
than recognizing one in somebody's shipped system. Its evidence comes
from the other direction — [case-mystery-and-art/](../../case-mystery-and-art/)
reads narrative genres as dispatch configurations and finds that the
**whydunit**, the form with every coordinate bound except the motive,
is the one audiences find least bearable to leave open. Several
thousand years of people optimizing for whether an audience can follow
a configuration is a strange corpus for language design, and it is
still a corpus.

More are planned as the case studies mature — the
[Zork](../../case-zork.md) case study still
wants a fully runnable companion here, and the
[korz-eval experiment](../experiments/korz-eval/EXPERIMENT.md)
generates trial seas that double as teaching examples.

## House rules

1. **Introduce your cast.** If an example uses a repo character or
   design, it explains who and what that is in its own opening — a
   cold reader never needs the shared canon to follow the mechanics.
2. **Mechanics first, mythology second.** The Korz concept being
   taught is stated plainly before any costume goes on.
3. **Link out, don't assume.** Deep lore gets a link and a
   one-clause gloss, not a bare name.
