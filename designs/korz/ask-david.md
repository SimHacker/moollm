# ASK David — the open questions, collected

*Part of the [Korz cauldron](README.md). Every question the design
raises that only David Ungar can answer well, gathered from the
documents that raise them — the agenda for the conversation.*

## The tier architecture ([design.md](korz-prime/README.md))

1. **Does the JIT framing land?** Crystallize/deopt is Self's
  speculative optimization applied to *semantics* — is that a
   continuation of the Self VM work or an abuse of it?
2. **Where does the tier boundary want to sit?** His VM instincts on
  what "hot and stable enough to compile" means when the
   interpreter is a language model — and how eagerly to recompile
   after a deopt.
3. **Should** `blend` **frighten us?** Method combination by semantic
  merge ([the troll's mixture](korz-prime/examples/troll-blend.md)) is either
   the answer to Korz's composition problem or a new kind of bug no
   debugger can see. (The troll wears his weights as anatomy; is
   that a debugging story or a dodge?)
4. **Is prose-in-guards a feature or a moral hazard?** The strict
  tier's refusal to compile it is the only discipline on offer.



## The name — just "Oriented Programming"?

1. **Should we drop the modifier guard entirely?** The joke writes
  itself in Korz terms: "Object Oriented Programming" minus the
   `Object` guard on the slot is just **Oriented Programming**. Once
   `rcvr` is no longer special — and there may be many dimensions of
   orientation — why argue over Subject-Oriented vs Context-Oriented
   vs Whatever-Oriented? Each camps on a frozen guard on one axis. The
   FOOL paper already argues object-, aspect-, and context-oriented
   programming are projections of one mechanism. Our reading goes one
   step further: **ditch the modifier guard** and call the whole thing
   Oriented Programming — behavior from orientation along *N* named
   dimensions, none privileged in the name. Freeze only `rcvr` and OO
   reappears as a view; freeze only `subject` and SOP reappears; leave
   all guards open and you have Korz. Corollary: every other *-Oriented
   language that freezes one guard and ignores the rest is
   **Disoriented Programming**. ;)
   Is that a fair elevator pitch, or
   does the "Context-Oriented" label in the Onward! title carry weight
   you'd defend? Would you rename the language genre if you could?

   Full deconstruction (Morningstar formula, both demolitions):
   [deconstruct-oriented-programming.md](deconstruct-oriented-programming.md)

## The dispatch semantics

1. **What are derived dimensions, formally?** The
  [CA case study](case-cellular-automata.md) finds two species:
   **aggregates** (Life's `live_neighbors`, a sum used as a
   dimension) and **coordinate transforms** (CAM-6's Margolus
   neighborhood: `C`/`CW`/`CCW`/`OPP` as permutations of the Moore
   compass indexed by phase dimensions `T`/`V`/`H`). Are both
   ordinary dimensions, a new guard kind, or evidence that
   dimensions form an algebra?
2. **Would Korz accept a scored or stochastic dispatch mode?** The
  Sims ranks all matching advertisements and dithers among the top
   N ([the auction](korz-prime/examples/sims-advertisements.md)); Korz
   legislates ties away. Is the specificity lattice's determinism
   the point, or would he buy dispatch as an auction — with
   temperature as a dimension
   ([the MOODY reading](korz-prime/examples/moody-temperature.md))?
3. **Coordinates as distributions.** `world: {zork: 0.7, adventure:
  0.3}` turns a binding into a mixture and sampling into a special
   case of blending. Is that still Korz, or a different (worse?
   better?) language wearing its clothes?
4. **The null family.** Korz has no null coordinate — dodged bullet
  or missing feature? Korz′ splits null's meanings into unmentioned
   / `isKnown` / named sentinels / deopt
   ([epistemics.md](korz-prime/epistemics.md)) and keeps one benign null as
   dimension-indexed delegation
   ([sparse-shadow-trees.md](korz-prime/sparse-shadow-trees.md)) — does that
   partition survive his scrutiny? And which parent function did the
   Self prototype's delegation *actually* use when hierarchies
   multiplied?
5. **Slots that mutate other slots' guards.** Magic: The Gathering's
  layer system exists because effects rewrite what other effects
   match: a card that turns every nonbasic land into a Mountain
   deletes the ability of a land that would have turned everything
   into a Swamp, so "which is newer" is the wrong question — the
   right one is which effect still *exists* to be asked. Rule 613.8a
   defines the dependency in terms of guard mutation, and the
   self-referential case (Humility and Opalescence, an enchantment
   that removes the abilities of the creatures another effect just
   made out of enchantments) is handled in at least one engine by
   *trial application* — provisionally run the slots, observe which
   outcomes move, derive the order, then run for real. Korz's
   unique-most-specific-match has no room for a guard that is
   undecidable until other slots have provisionally run. Is that a
   new guard kind, a fixpoint one level above dispatch, or a case he
   would rule out of the language on purpose
   ([mtg-layers.md](korz-prime/examples/mtg-layers.md))?
6. **Legislated total order as a third ambiguity policy.** Magic
  cannot error and cannot ask a player to accept an undefined board,
   so it stacks fallbacks: hand-authored layer order, then dependency
   derived from guard mutation, then timestamp, and if the
   dependencies form a loop, drop a tier. The judges' stated design
   goal is not principle but expectation — make the answer "what we
   would intuitively expect as often as possible." Does that read to
   him as an admission about what specificity heuristics are always
   doing, or as evidence that a declared lattice is exactly what
   would have saved them thirty years of errata?
7. **Rebinding instead of ordering — and self-amendment.** Fluxx
  ([fluxx-nomic.md](korz-prime/examples/fluxx-nomic.md)) is a Korz context sitting
   on a table: `Draw`, `Play`, `Limit`, `Other` are dimensions, a card
   is a coordinate, exactly one is bound per dimension, and playing a
   card rebinds and discards the displaced one. Conflict is
   unrepresentable, so no layer system is needed — which reads as the
   strongest possible argument for declared dimensions, made in a card
   game in 1997. Two questions follow. First: is "at most one binding
   per dimension" doing more work in Korz than the papers say out loud,
   and is Magic's whole layer apparatus just the price of violating it?
   Second, the harder one: Fluxx's ancestor is Peter Suber's **Nomic**
   (1982, published in Hofstadter's *Metamagical Themas*), built to
   embody the thesis of Suber's *The Paradox of Self-Amendment* — that
   a rule of change may apply to itself and authorize its own
   amendment. Korz′'s crystallization loop is an amendment process with
   a ratification step. Does he think the self-amendment literature is
   load-bearing for a two-tier dispatcher, or a category error?
8. **Can the lattice itself be generated?** Dwarf Fortress's Myth and
  Magic work generates each world's magic from a procedural creation
   myth: which effects exist, what they cost, and what they are
   *about* all come out of the generated cosmology, and a later
   mythological event can flip a rule so that "suddenly people's
   teleport spells don't work anymore" — the paper's assertions
   demonstration, with thousands of agents re-dispatching underneath
   and nothing in between written to expect it. Korz's dimensions are
   declared by a programmer. What is the smallest change that lets a
   *program* emit a dimension, and does the specificity lattice stay
   sound when the axes arrive at runtime
   ([df-procedural-magic.md](korz-prime/examples/df-procedural-magic.md))?



## The hosting and tooling story ([hosting-moollm.md](korz-prime/hosting-moollm.md))

1. **How much of the prototype's IDE was Korz needing an IDE, and
  how much was the Self image needing a window?** If the slots had
   been files in a repo — visible to `ls`, `grep`, and `git` — what
   tooling would he have actually missed? Is a saved-view interface
   file (durable, versioned) what the IDE's on-demand slot grouping
   wanted to be?
2. **Hosting symmetry.** Korz-in-Self took machinery; Self-in-Korz
  takes only restraint (guard everything on `rcvr`). Does hosting
    Korz in Self predict that a filesystem can host both readings in
    one repository — and did the prototype ever exploit the
    asymmetry?



## The history

1. **The Conscientious Objectors meetup** — the Kaleida gathering
  of the ScriptX object-system team and the Self team. Who was
    there? (Don recalls
    Dan Bornstein, who implemented
    ScriptX's CLOS-like multimethods, in the room — cross-examine.)
    What was argued, and did anything from either side ship in the
    other?
2. **Korz's unpublished residue.** The prototype had an
  interpreter, debugger, and partial IDE in Self — what survives?
    What did the papers leave out that the implementation knew?



## Where the rest of the ASKs live

[korz-notes.md](korz-notes.md) carries Don's Q&A working notes on
the papers, with embedded ASKs on nulls, JIT history, Linda, layers,
mirrors, Emacs buffer-locals, before/after demons (CLOS method
combination as a dispatch pattern — what is Korz's
`call-next-method`?), and what "super" even means once class, owner,
and linearization are all dissolved (context weakening vs reified
dispatch — David reportedly called resend unsolved; confirm) — those
stay in their reading context rather than being duplicated here. The
[deep dive](sources/korz-paper-deep-dive-moollm-mapping.md) ends
with its own open-questions list, which this page subsumes.