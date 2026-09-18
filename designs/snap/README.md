# Snap! — first-class everything, in blocks

Snap! is Brian Harvey and Jens Mönig's block language: Scratch's shape with
Scheme's semantics underneath. First-class procedures, first-class lists,
first-class continuations, metaprogramming on the blocks themselves — and a child
can drag them.

That combination is why it keeps turning up in MOOLLM's designs. It is the
existence proof that a frontier idea can be brought all the way home without
being watered down: the thing children play with is the real mechanism, not a
diagram of it. See
[revolutionary-chess/BRINGING-IT-HOME.md](../revolutionary-chess/BRINGING-IT-HOME.md)
for the argument and [skills/constructionism](../../skills/constructionism/) for
the tradition it belongs to.

Each `.md` has a `.yml` sidecar carrying the same material as structured data.

## The language

| Doc | What it is |
|---|---|
| [moollm-integration.md](moollm-integration.md) | **Start here for the MOOLLM connection.** What Snap! and MOOLLM share — constructionism, first-class everything, a system that explains itself — and how they could integrate, including with Micropolis |
| [snap-first-class-everything.md](snap-first-class-everything.md) | The design claim: procedures, lists, continuations, sprites and costumes all first class, in a language you drag |
| [y-combinator-in-blocks.md](y-combinator-in-blocks.md) | The Y combinator built out of blocks — recursion without a name to recurse on, made visible |
| [snap-macros-metaprogramming.md](snap-macros-metaprogramming.md) | Brian on macros, unevaluated inputs, and blocks that build blocks |
| [morphic-js.md](morphic-js.md) | Jens' Morphic in JavaScript: the live direct-manipulation object world Snap! is built on, from Self through Squeak |
| [../MORPHIC-LINEAGE.md](../MORPHIC-LINEAGE.md) | The whole Morphic family tree Snap! sits in: Self, Squeak, Tweak, Cuis's Morphic 3, Lively's three generations, GP/MicroBlocks, and the Common Lisp attempts |
| [gp-alan-kay-lineage.md](gp-alan-kay-lineage.md) | GP, and the line back through Alan Kay's group — John Maloney, Yoshiki Ohshima |
| [sap-research-and-snap.md](sap-research-and-snap.md) | Jens' day job and how the research work relates to Snap! |

## SnapCon 2025

Brian Harvey's Karlström Award address, with Jens' introduction — the talk this
material keeps quoting.

| Doc | What it is |
|---|---|
| [snapcon-2025/karlstrom-address-transcript.md](snapcon-2025/karlstrom-address-transcript.md) | The transcript, where the quotes come from |
| [snapcon-2025/karlstrom-address-brian.md](snapcon-2025/karlstrom-address-brian.md) | Digest of the address |
| [snapcon-2025/karlstrom-intro-jens.md](snapcon-2025/karlstrom-intro-jens.md) | Jens' introduction |

## Snap! meets a simulator

Wiring blocks to a live city. The 2018 thread has two write-ups because there
were two sides to it.

| Doc | What it is |
|---|---|
| [micropolis-snap-2018-brian-thread.md](micropolis-snap-2018-brian-thread.md) | Don's 2018 thread with Brian and Jens: driving Micropolis and CAM6 from Snap! blocks |
| [micropolis-snap-2018-jens-build-side.md](micropolis-snap-2018-jens-build-side.md) | The same thread from the build side — what it would take to wire blocks to live simulation parameters |
| [micropolis-svelte-snap-constraint-bridge.md](micropolis-svelte-snap-constraint-bridge.md) | The three bindings of a glass-box city: WASM engine authoritative, Svelte runes for the HUD, Snap! blocks for student-authored rules |
| [snap-visual-engines-fundable-goals.md](snap-visual-engines-fundable-goals.md) | Visual engines as fundable goals, and who the pieces belong to |

## Logo and CS education

Brian Harvey's other line of work, which is the same argument one generation
earlier.

| Doc | What it is |
|---|---|
| [logo-and-cs-education/computer-science-logo-style.md](logo-and-cs-education/computer-science-logo-style.md) | *Computer Science Logo Style* — Logo as a serious language |
| [logo-and-cs-education/simply-scheme.md](logo-and-cs-education/simply-scheme.md) | *Simply Scheme* — the on-ramp to SICP |
| [logo-and-cs-education/berkeley-logo-and-cs61a.md](logo-and-cs-education/berkeley-logo-and-cs61a.md) | Berkeley Logo, and CS61A |
| [logo-and-cs-education/beauty-and-joy-of-computing.md](logo-and-cs-education/beauty-and-joy-of-computing.md) | BJC — the Snap!-based curriculum |

## Related

- [teaching-complicated-systems-without-a-manual.md](../teaching-complicated-systems-without-a-manual.md)
  — the pedagogy essay this material is evidence for
- [cellular-automata/](../cellular-automata/) — the other simulator Snap! was
  pointed at
- [korz/](../korz/) — subjective dispatch; Morphic and Self are the shared ancestry
- [VISUAL-PROGRAMMING-LINEAGE.md](../VISUAL-PROGRAMMING-LINEAGE.md)
