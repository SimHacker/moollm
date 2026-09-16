# Snap! rings, AST metaprogramming, and macros

Brian Harvey — design and Reference Manual; Jens Mönig — implementation.

**Primary sources:** Snap! Reference Manual
[Procedures as Data](https://docs.snap.berkeley.edu/procedures-as-data/) ·
[Metaprogramming](https://docs.snap.berkeley.edu/metaprogramming/) ·
[Continuations](https://docs.snap.berkeley.edu/continuations/) —
forum threads [hygienic macros](https://forum.snap.berkeley.edu/t/hygienic-macros/3258) ·
[script builder library](https://forum.snap.berkeley.edu/t/script-builder-library-part-1/3361) ·
[do macros actually work?](https://forum.snap.berkeley.edu/t/do-macros-actually-work-in-snap/14431) —
Snap!Con 2022: Brian Harvey, *A History of Metaprogramming* (Logo/Scheme → Snap! 8).
**Live code:** [Snap! itself](https://github.com/jmoenig/Snap) — the whole IDE is one repo.

---

## The hook

Snap! carries Scheme-class ideas in a visual language: gray **rings** are essentially **quote**;
**split by blocks** / **join** / **define** (v8+) treat blocks as AST data; **macros** follow the
Lisp-family model (unevaluated inputs, expand in the caller's environment) — not C preprocessor
text — but hygiene and the block-editor macro checkbox are still unfinished. Brian documented the
pedagogy; Jens ships the interpreter.

## Two layers, two chapters

| Layer | Chapter | What | Mechanism |
|-------|---------|------|-----------|
| **Procedures as data** | [Ch. 6](https://docs.snap.berkeley.edu/procedures-as-data/) | First-class functions — lambda, HOFs, closures | Gray ring / ringify; `call` (reporters) and `run` (commands) |
| **Metaprogramming proper** | [Ch. 11](https://docs.snap.berkeley.edu/metaprogramming/) (since Snap! 8.0) | Manipulate block syntax trees — what you see on screen IS the data | `split by blocks`, `join`, `define`, `set _ of block`, `definition of`, `attribute of block`, `delete block` |

The ring = quote: evaluation does not pass through until explicit invocation. Brian's own claim
(Karlstrom 2025): **anonymous procedures — the gray rings — are his main Snap! code
contribution.** And the two layers are genuinely distinct: AST manipulation is not the same thing
as procedure values.

## The ring as visual syntax

The insulating gray oval with a gap is deliberate pedagogy: enclosed blocks are **data**, not
orders to run now. Invocation (`call`/`run`, or a higher-order function) reaches through at the
**call site**.

- **Command ring** — jigsaw interior · **Reporter ring** — oval interior · **Predicate ring** — hexagonal interior
- **Invisible rings:** C-shaped control slots (unevaluated scripts — Scratch already used this)
  and `Any (unevaluated)` inputs (special forms; look like white rectangles, delay evaluation
  like macro arguments)
- **Special forms:** a reporter if-then-else that doesn't infinite-loop on factorial —
  unevaluated branches + `call` inside the implementor, while the user sees Scratch-normal UI.

## The macro model — Lisp family, not C preprocessor

1. A macro call **looks like** a procedure call.
2. Macro inputs are **not pre-evaluated**.
3. The macro **reports a ringed script or expression**.
4. The result is **evaluated in the CALLER's environment** — spliced at the call site.

Why you need this: declare script variables in the caller; change caller control flow
(report/stop from a macro expansion); derived special forms (COND → nested IFs) — things a normal
procedure cannot do.

**The canonical example — "script list variables."** A helper that declares script variables
`a, b, c` initialized to `[]` binds them in the *helper*, not the caller. The macro fix: report a
ringed script; that script runs inside the caller where the macro was invoked. The gray ring
remembers the macro's own environment for its free variables (e.g. the input list `VARS`) — the
closure and the splice cooperate.

**Ship state (v8, partial):** caller context via the `of` block (run code in another context,
like `tell sprite to`); the fizzbuzz `if _ report _ caller _` pattern reports from inside `map`.
The Manual itself admits: caller context should become an invisible input (a future checkbox in
the make-a-block dialog); command-macro vs reporter-macro notation is still TBD; macro/caller
variable name collisions are possible; and hygienic macros are **not** implemented — "one
substantial Scheme feature we don't yet implement." Brian on the forum, 2020: no macros at all
yet — "one big hole"; continuations already there; leaning FEXPR first. By 2023, users
[couldn't distinguish a macro from an ordinary call of a ring](https://forum.snap.berkeley.edu/t/do-macros-actually-work-in-snap/14431);
Brian hoped for a Snap!Con cleanup.

## Why it's hard — blocks aren't S-expressions

Lisp's advantage: the code surface IS lists, so quote/quasiquote are trivial. Snap!'s obstacle
(pre-v8): scripts were first-class but *atomic* — no inspectable interior. Open AST design
questions: variable refs (special AST nodes vs niladic variable blocks?), block headers (the
title is spread across the UI, not one symbol like `(define foo …)`), the command-macro shape
(stacks like a command, reports a script like a reporter), and caller splice (a call/cc
workaround was discussed; the shipped answer is the `of` caller-context primitive).

**Trajectory:** 2020 [script-builder library](https://forum.snap.berkeley.edu/t/script-builder-library-part-1/3361)
(community AST hack; Brian wanted `SLOT OF` and programmatic `define`) → Snap! 8.0 primitives
(`split`/`join`/`define` + partial caller-context macros) → future: macro checkbox in the block
editor, possibly a macro library atop the primitives. Brian's target: the
[*Computer Science Logo Style*](logo-and-cs-education/computer-science-logo-style.md) chapters on program-as-data and
macros — **Logo lineage, not only SICP**.

## Hygiene and FEXPR — Brian's position

- He was reading comp.lang.scheme **when hygienic macros were invented**; he knows the arguments.
- FEXPR-style is **simpler for learners** — teach the name-capture danger explicitly.
- Hygiene is the compile-time analogue of lexical scope; FEXPR is the dynamic-scope analogue.
- Ship FEXPR first; hygiene after the AST layer is debugged.
- On syntax-rules pattern matching: a poor fit for blocks — "they're blocks, not S-expressions."

Jens's 2020 pushback: dynamic scope is horror for learners and abstraction — a separate thread
from macros, which leads to…

## The dynamic binding controversy 🔥

**Brian's most controversial take:** he wishes Snap! used **dynamic binding** (at least for
learners) — grounded in decades teaching Logo to kids, not industry programmers.

**For (Brian):** in Logo without lambda, the dynamic environment is a superset of the lexical —
more caller variables visible. Name capture is unlikely unless you have multiple programmers and
no modules — kids write one-off helpers. Sometimes you *want* capture: Logo `MAP` + `?` — the
callee reads a variable set in the caller (`scale 3 [4 5 6]`). Logo debugging: the REPL uses the
same language, and all relevant locals are visible at the error — no special debug dialect.
Helpers meant for 1–3 specific callers can assume the caller's environment.

**Against (acknowledged):** Jens — blocks must be **interchangeable**; dynamic scope means the
same block behaves differently per caller. Jens — interpreter cost: shallow binding and tail-call
elimination break Brian's hybrid-scope fix. Purists — name-capture bugs at scale. Snap!'s actual
answer to HOF caller-variables: gray rings + hyperblocks, not dynamic scope.

**Brian's unshipped proposals:** full dynamic scope; hybrid scope (dynamic lookup only when no
lexical/global match, 2020); a `DYNAMIC VARIABLES` block (like `SCRIPT VARIABLES` but permitting
dynamic reference when there's no lexical candidate).

**Jens's position:** lexical only. Dynamic scope has no benefits except trivial implementation
(which Snap! would still pay for if done efficiently). Kids deserve interchangeable blocks.
Debugging may need dynamic-flavored access — but that's not a license for dynamic binding in the
language.

**What Snap! actually has:** lexical scope (global, sprite-local, script variables); special
forms (`Any (unevaluated)`, C-slots — delayed evaluation, not dynamic binding); closures (rings
remember the defining environment); a debugging exception (pause all → watchers for suspended
scripts' variables — Brian: "Jens does understand you need dynamic scope for debugging"); the
`of` caller-context block; and `self` in `my` blocks (Don's RISC-for-OOP metaphor —
sprites are first-class). **Not** in Snap!: fluid-let, full dynamic scope, hybrid scope, the
`DYNAMIC VARIABLES` primitive.

→ This is Palm's question 3
on the pair show: Brian states for/against on air; Jens says what shipped vs what was argued.
One atomic primitive, or a pile of special cases?

## Dataflow vs CPS (forum Sep 2020)

**spdegabrielle** (health developer, not CSE): Snap! is light-years ahead of Blockly/Scratch;
macros was curiosity not a proposal; **dataflow** (Pure Data fan) feels more natural than scope or
macros; mentions an unnamed hybrid-scope language.

**Brian:** thanks; asks which hybrid-scope language; has thought about dataflow but gets hung up on
**conditional evaluation without explicit continuation-passing style** — though it fits the visual
metaphor; will look into more.

**Don's counterexample:** Bounce / Body Electric
(David Levitt) — **switch** (pure dataflow `? :`), **enable line** (gate + sequence), **while
encapsulation** (telescoping loop) — partial order from wires, no CPS. Full design notes in
`mediaflow-design-comments.md` § "Bounce control flow vs Max".

## The honest SICP scorecard

| Status | Feature |
|--------|---------|
| ✅ Yes | Functional style, recursion, HOFs · Closures via rings + environment · Continuations (`call w/continuation`, `catch`/`throw`, experimental limits) · Quote / delayed eval (rings, special forms, unevaluated inputs) · Program-as-data (block AST since 8.0) |
| 🟡 Partial | Macros — caller-context expansion via `of`; UI incomplete; user confusion reported 2023 |
| ❌ Not yet | Hygienic `define-syntax` / `syntax-rules` · Full metacircular evaluator chapter out-of-box (pieces exist via AST) |

**Calibrating the HN claim:** "Everything you can do with Scheme in Snap!" is directionally right
for BJC/SICP *ideas* but oversells macro polish. Safer: functional programming + continuations +
metaprogramming AST + the Lisp-family macro *model* (partial implementation).

## Show beats

**Brian:** draw the ring on a whiteboard — quote, gap, call/run as eval · special forms (why
Scratch `if`/`forever` already had invisible rings) · FEXPR vs hygiene pedagogy · the dynamic
binding take · dataflow vs CPS — Bounce switch/enable/while · which CSLS macro examples still can't be done faithfully.
**Jens:** `split`/`join`/`define` live — hexagon from square block · interpreter cost of caller
context (`of` internals) · what's blocked on the macro checkbox and command-macro notation · the
2020 scope debate vs the lexical commitment.
**Pair:** Logo disguised as Scratch → lambda made it Scheme disguised as Scratch · Palm's Theo
turtle meets the ring — code you can see and touch.

## Deeper into the multiverse

- Palm's audience questions — the ring-as-quote lead question, the scorecard, the controversy
- [Karlstrom address digest](snapcon-2025/karlstrom-address-brian.md) — lambda as Brian's contribution, in his own words · [full transcript](snapcon-2025/karlstrom-address-transcript.md)
- [*Computer Science Logo Style*](logo-and-cs-education/computer-science-logo-style.md) · [*Simply Scheme*](logo-and-cs-education/simply-scheme.md) — the textbook lineage
- [Jens — first-class everything](snap-first-class-everything.md) · [the Y combinator in blocks](y-combinator-in-blocks.md)
- [Snap! source](https://github.com/jmoenig/Snap) · [Snap! IDE](https://snap.berkeley.edu/) · [Reference Manual](https://snap.berkeley.edu/snap/help/SnapManual.pdf)
- [Palm's worm field notebook](https://github.com/SimHacker/moollm/blob/main/examples/adventure-4/pub/stage/palm-nook/study/palm-on-worms-fieldnotes.md) — Theo the Logo Turtle, rings as insulation
- Pair show

↑ [Snap! index](README.md)
