# Snap! as the Visual Front End — CAM6, VitaMoo, Micropolis, Bounce

*Don's design + funding vision. Four real engines, one visual programming host. Each is a standalone
**fundable goal**; together they're a constructionist play-and-learn platform.*
Portrayal standards ·
Trail: visual-programming-patch-cord

## The insight

Inspired by **eToys → Scratch → Snap! → Sandspiel Studio**, the temptation is to build a brand-new
visual cellular-automata programming language from scratch. But there's a better move: **just
integrate the engine with [Snap!](https://snap.berkeley.edu/)** — **that is the BEST solution.**

Snap! (Jens Mönig & Brian Harvey, UC Berkeley) is:
- **JavaScript, in the browser** — the same runtime as my CAM6.js, VitaMoo (WebGL), and Micropolis
  (WASM/JS). No impedance mismatch.
- **Extensible** — custom blocks + JS-primitive extensions, so an engine becomes a **block palette**.
- **Real language, not a toy** — first-class procedures, lists, and continuations (Scheme semantics
  under Lego-brick blocks); lambda, higher-order blocks, recursion.
- **Live and reified** — click a block, watch it run; the program is an object you can inspect.
- **Open source, huge reach** — the engine behind *The Beauty and Joy of Computing*; TurtleStitch and
  many others already extend it.

So I get the editor, palette, sprites, live-coding, and sharing **for free**, and spend my effort on
the **engine blocks** — not reinventing a whole IDE. Snap! is the front end; the lookup-table /
simulation engine is the back end.

## Two visual paradigms, both worth having

I've lived in both halves of the visual-programming taxonomy
(control-flow vs data-flow):

- **Snap! — blocks** (control flow + reified procedures, Scheme semantics). Great for *authoring
  rules and behavior*: define a CA rule, a Sim's action, a city policy as composable blocks.
- **Bounce — patch-cords** (objects on wires, data flow; David
  Levitt's Hookup → Body Electric → Bounce lineage). Great for *wiring live media and simulation
  streams* together — and a fundable reincarnation in its own right.

They're complementary. A mature platform could **bridge** them: Snap! blocks author the rules; a
Bounce-style patch-cord layer wires the running engines/streams together (zero-copy where it counts —
see streams-of-streams / zero-copy).

## The four engines — each a fundable goal

Each stands alone as a milestone with its own audience and funder story; a Snap! front end is the
common multiplier.

### 1. CAM6 — cellular automata (new modular version)
The rebuilt, modular CAM6 (much better than the old monolith) exposed as **Snap! blocks**: define
rules and neighborhoods, compile to lookup tables, paint and run live. **Norman Margolus has already
blessed turning book chapters into interactive playgrounds** — Snap! is how a chapter becomes a
palette a student can remix.
Bigger than a rule palette: the **[CAM Construction Set](../cellular-automata/cam-construction-set.md)** exposes the
**machine** as components — cell planes, neighborhood formers, the address assembler, the lookup
table itself, phase generators, instruments — so you snap together a historically accurate CAM-6
and then rewire it. That design is also where the blocks-vs-patch-cords question below gets
settled: rules are control flow (Snap!), the datapath is data flow (Bounce).
- Audience/funders: science + retrocomputing + CS education; the Margolus/Toffoli legacy.
- Docs: [CAM Construction Set](../cellular-automata/cam-construction-set.md) ·
  the CAM6 demo for Norman ·
  transcript + glossary ·
  [CAM6 writeup](../cellular-automata/cam6-cellular-automata-machine.md)

### 2. VitaMoo — Sims character animation
**Don Hopkins'** **VitaMoo** (WebGL Sims-1 character renderer; clean-room VitaBoy lineage, TS port of
Don's Unity3D C#) driven from **Snap! blocks**: pose, animate, and script Sims characters visually —
the soul mover made playable. Save/object tooling stack inspired by Jeff Adkins's
**SimObliterator**.
- Audience/funders: the huge Sims community + game preservation (VGHF-adjacent); content creators.
- Ties: Jeff Adkins (SimObliterator; accepted guest), Will Wright's data-portability grail.

### 3. Micropolis — city simulator
The open-source **Micropolis** (SimCity) engine as **Snap! blocks**: build, zone, and script the
city; expose the sim's variables and policies for constructionist play — the through-line to
**Doreen Nelson**'s Design-Based Learning and the **OLPC/Sugar** SimCity curriculum.
- Audience/funders: constructionist education; the SimCity-in-the-classroom lineage.
- Ties: constructionist lineage (Cynthia Solomon, Ken Kahn, Alan Kay), Doreen Nelson, Will Wright.

### 4. Bounce — objects-on-wires dataflow
A merciful **TypeScript reincarnation** of **David Levitt**'s Bounce (Pascal → mangled C → TS), the
patch-cord/data-flow complement to Snap!'s blocks — and a live-media wiring layer for the other three.
The reincarnation has a home: **Rebounce** — check in the source
and rewrite it together (hand + AI), seeded by David, Don, and **Jaron Lanier**.
- Audience/funders: media/VR heritage (VPL/Body Electric), realtime-media artists.
- Docs: Rebounce ·
  Body Electric / Bounce VR stack ·
  Levity / Bounce / Space Seed.

## Why "fundable, each"

- **Independent milestones.** Any one can ship and demo on its own; no big-bang dependency.
- **Distinct funders.** Education/constructionism (Micropolis + Snap!), game preservation + a large
  fan community (VitaMoo), science/retrocomputing (CAM6), media-art heritage (Bounce).
- **Shared multiplier.** Snap! integration amortizes across all four — build the bridge once.
- **Public dev stage.** Each is a natural **Repo Show** arc: build it live, in the open, with the
  people who made the originals.

## Collaborators & shows

- **Snap!:** Jens Mönig + Brian Harvey —
  integration partners and dream co-hosts for the visual-CA episode (they already have a headline show
  seed: snap-logo-brian-jens).
- **Bounce:** David Levitt — Hookup/Body Electric/Bounce; TS reincarnation.
- **CAM6:** Norman Margolus — chapter playgrounds (permission granted).
- **VitaMoo:** Don Hopkins — Sims character rendering/animation. **SimObliterator:** Jeff Adkins.
- **Micropolis / constructionism:** Will Wright,
  Cynthia Solomon, Ken Kahn,
  Alan Kay, Doreen Nelson.

## Status / next

- **Decision:** integrate engines with **Snap!** rather than build a new visual language from scratch.
- **First build:** CAM6-in-Snap! (rules → lookup tables → live paint), because the modular rebuild +
  Norman's chapter-playground blessing make it the cleanest first slice.
- **Then:** VitaMoo blocks, Micropolis blocks, Bounce TS — in whatever order the funding/energy lands.

*Status: firsthand vision — direction set, engines real, integrations not yet built. Fundraising
framing is Don's; no funder is committed.*
