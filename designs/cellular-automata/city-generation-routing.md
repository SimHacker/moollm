# The city that routes itself

### Trent R. Small — *Local Routing in a new Indefinitely Scalable Architecture*

This is the paper behind Don's favorite party trick: the
[**Distributed City Generation** demo](https://www.youtube.com/watch?v=XkSXERxucPc)
in Dave Ackley's [Movable Feast Machine](https://movablefeastmachine.org/). The
video is gorgeous on its own — a city that grows itself from a single seed of
street — but the [YouTube description quietly links a paper](https://www.cs.unm.edu/~ackley/papers/paper_tsmall1_11_24.pdf)
that explains how the thing actually *works*, and it's fascinating. Here's the
short version, with the paper mirrored in this repo.

- **Paper (local copy):** tsmall-local-routing-mfm.pdf
- **Full text (accessible MD):** sources/tsmall-local-routing-mfm/full-text.md
- **Paper (author's host):** [cs.unm.edu/~ackley/papers/paper_tsmall1_11_24.pdf](https://www.cs.unm.edu/~ackley/papers/paper_tsmall1_11_24.pdf)
- **The demo video:** [Robust-first Computing: Distributed City Generation](https://www.youtube.com/watch?v=XkSXERxucPc) — transcript & notes
- **The whole MFM demo playlist:** [Movable Feast Machine demos](https://www.youtube.com/playlist?list=PLm5k2NUmpIP8qwttAS5Batnd7u2UpBtaL)
- **Source code:** [github.com/sixstring982/MFMv2-city](https://github.com/sixstring982/MFMv2-city) — an open fork of Movable Feast Machine v2
- Author: **Trent R. Small** (University of New Mexico), advised by **Dave Ackley**; funded by Google.

---

## The problem: routing with no map and no address

The [Movable Feast Machine](https://en.wikipedia.org/wiki/Cellular_automaton)
(Ackley, Cannon & Williams, 2013) is a spatially distributed, **indefinitely
scalable** architecture: computation lives *in place* on a grid of tiles, and any
data that moves has to physically travel across the machine, one small
neighborhood at a time. That's exactly what makes it robust — a fault in one
region doesn't sever the rest — but it breaks the comfortable assumptions of a
[Von Neumann machine](https://en.wikipedia.org/wiki/Von_Neumann_architecture):

- **No global state.** Each event sees only a tiny **Event Window** — 41 sites,
  ~96 bits each — so nothing can "look at the whole city."
- **No absolute addressing.** Memory *is* location; you can't name a destination
  by address, only find it by moving toward it.

So the paper asks a wonderfully concrete question: *how do you route a packet
across a computer that works like a city where nobody has a map?*

The answer is to **build an actual city** and steal the tricks real cities use.

## The city grows itself

The generation is pure bottom-up cellular automata — the same "grow from a seed"
move you see in Don's CAM6 rules, but producing urban form. From a single
`CITY_STREET` atom:

1. **Streets** copy themselves in a direction, laying **sidewalks** perpendicular
   as they go.
2. Streets occasionally spawn **intersections** (tuned by an "intersection odds"
   parameter); intersections spawn more streets. The grid fills fast.
3. Sidewalks wait, then raise **buildings** on the far side — each with one of
   **24 building types**.
4. Buildings emit **cars**, each seeking a *type* of destination (not an address).
   Mismatched blocks that don't line up are detected locally and filled with
   **parks**.

Nothing is coordinated globally. Sprawl, repair, and infill all happen as local
reactions — which is the whole robust-first point: *if a disaster wipes out a
chunk of city, the ability to rebuild was never lost, just unused.*

## Routing: three ways to find a building you can't address

Cars can't be told where to go, so the city has to guide them. The paper compares
three local strategies:

| Method | How it works | Cars arriving | Avg. gas (events) |
|--------|--------------|:-------------:|:-----------------:|
| **Random** | Intersections send cars down a random road they didn't arrive from | ~91% | 29.4 |
| **Sidewalk-Only** | Sidewalks keep a small map — distance in blocks to each building *type* — and intersections steer cars toward the nearest matching block | 98.2% | 20.05 |
| **Intersection-Canalization** | Adds memory: each intersection remembers the last direction it sent each car type, avoiding repeated dead-ends | 98.22% | **17.7** |

The punchline is the humility built into it. **Random routing already works 91% of
the time** just because dense cities keep similar buildings close together. A
sidewalk that can only remember distances *3 blocks* out (2 bits per building type,
because that's all the atom bits allow) gets you to 98%. Canalization barely
improves *accuracy* (+0.02%) but cuts *fuel* another 15% by not wandering into
dead-ends twice. Correctness is cheap; efficiency is the hard-won part — a very
robust-first moral.

## Why Don loves it

This is [Will Wright's SimCity](https://github.com/SimHacker/MicropolisCore)
turned inside out: instead of a person zoning a city top-down, the city zones
*itself* bottom-up, and then solves its own traffic as a side effect of growing.
It's the cleanest possible bridge between the two halves of Don's world — cellular
automata and city simulation — and it's why, when cyberpunk author
[Rudy Rucker](https://en.wikipedia.org/wiki/Rudy_Rucker) got buried in Ackley
links and begged for *"a video with pretty pictures of CAs, and not a guy
talking,"* this is the one Don sent. The design constraints Small lists —
*local mapping; fast, accurate, simple, flexible; favor robustness over
correctness* — are the robust-first credo written as a city-planning brief.

The paper even notes that UN-Habitat city planners had started using tile-based
software to plan real cities (Parker, *NYT*, 2014) — the toy and the tool
converging, again.

---

*The rules are translated into Korz slots as a design exercise in
[`mfm-city.md`](../korz/korz-prime/examples/mfm-city.md) — which is where the bit budget turns into
a type check, Algorithm 1 turns out to be a saturating Bellman-Ford whose clip is the actual result,
and intersection canalization turns out to be a polymorphic inline cache.*

*Part of the CA correspondence story. Paper by Trent
R. Small; mirrored here with attribution. Portrayal standards.*
