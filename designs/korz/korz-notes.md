# Korz — Don's notes, questions, and answers

Working notes from reading the paper
([../sources/korz-2014-onward.pdf](https://dl.acm.org/doi/10.1145/2661136.2661147)) ahead of
the demo. Short answers here; the long arguments live in the
[deep dive](sources/korz-paper-deep-dive-moollm-mapping.md). Questions
still open for David are marked **ASK**. The constructive answer —
what a Korz redesigned for the LLM age looks like — is
[design.md](korz-prime/README.md): one semantics, two dispatchers,
crystallize/deopt between them.

## KORZ is an anagram of ZORK

Don's observation: the paper's Appendix A derives the name from
Korzybski (*Science and Sanity*, the map is not the territory), but the
same four letters spell **Zork**. A language of subjective objects and
implicit context, accidentally named for the adventure game — and it
*fits*: adventures and games are where subjective dispatch earns its
keep. The room you're in, the world you're from, the side you're on,
the mood in the air — all dimensions of an implicit context that every
action dispatches through. That's the thesis of
[GAME-PIECES](https://github.com/SimHacker/moollm/blob/main/designs/GAME-PIECES.md),
and the specimens already run: the
[Cross-Platform Troll](https://github.com/SimHacker/moollm/tree/main/examples/adventure-4/characters/fictional/troll)
dispatching on a `world` dimension (zork-mind vs adventure-mind — he's
a Korz subjective object *containing Zork*, the anagram closed into a
loop; he can front one mind or blend between them, mixing the minds
with different weights — and he's literally two-headed, head size
displaying the live weights — see the [troll-blend example](korz-prime/examples/troll-blend.md)),
[Revolutionary Chess](https://github.com/SimHacker/moollm/tree/main/skills/experiment/experiments/turing-chess/plugins/revolutionary-chess)
reparenting pieces mid-game, moody rooms writing dispatch temperature
([MOODY](https://github.com/SimHacker/moollm/blob/main/designs/MOODY.md)).
**ASK:** did anyone at IBM notice the anagram? (It's not a reversal —
Korz backwards is Zrok.)

## Korz is E-Prime for objects

The Korzybski lineage runs deeper than the name. His student D. David
Bourland Jr. formalized **E-Prime** in 1965 (*A Linguistic Note:
Writing in E-Prime*, General Semantics Bulletin): English minus every
form of "to be." The targets came straight from *Science and Sanity* —
the **is of identity** ("Don *is* a programmer": collapses a
multidimensional person into one label) and the **is of predication**
("the rose *is* red": projects the observer's perception onto the
object as an intrinsic property). Banning "be" also kills the English
passive ("was eaten"), so E-Prime structurally forces active sentences
with named actors. Robert Anton Wilson wrote *Quantum Psychology* in
it; Albert Ellis rewrote therapy books in it. Korzybski himself never
endorsed total elimination — auxiliary and existence uses he considered
harmless; Bourland took the critique to its limit.

Korz does to the object model what E-Prime does to the sentence: it
bans the is of identity. A Korz object *is* nothing absolutely — no
single objective identity, only behavior that emerges when a context
asks along particular dimensions. Subjectivity per viewer = no is of
predication either: "red" lives in the dispatch, not in the rose. "The
map is not the territory" and "the object is not its class" — same
slogan. **ASK:** did the E-Prime connection figure in the naming, or
just the map/territory line in Appendix A?

Footnote on the slogan itself: "is not" is not the is of identity — it
denies an identity rather than asserting one, prying the abstraction
levels apart instead of collapsing them, so Korzybski's own system
permits it (he kept auxiliary, existence, and negated uses). Bourland's
doesn't: E-Prime bans every form of "to be," so **E-Prime cannot state
"the map is not the territory."** The rewrite — "the map differs from
the territory," "no map captures its territory" — improves it in
classic E-Prime fashion by forcing you to say *how*. The student's
reform is too strict to express the teacher's premise.

## Q&A

**Does Korz handle null or empty dimensions gracefully?**
Absence is the mechanism, not an edge case. A guard takes one of three
stances per dimension: *unmentioned* (don't-care — matches whether the
context binds it or not; Appendix C draws a "−" position on every
axis), *bare name* (must be present, any value, bound into method scope
as a named implicit parameter), *constrained* (present and at least
that specific). Less context ⇒ only more-generic slots match, down to
the zero-dimensional procedural case. But there is **no null
coordinate**: you can't bind `location: none` to mask specific slots,
or guard on absence. The soft tier offers a third option beyond
null/absence: **graded presence** — with K-line referents the test is
not `isNull: bool` but `isKnown: float`, and guards can threshold on
it (see [epistemics.md](korz-prime/epistemics.md) §isNull becomes isKnown).
**ASK:** missing feature or dodged bullet — or a boolean shadow of a
continuous question?

**Is Korz a discipline for using Self multidimensionally, or a new
quark in Self's atom?**
New quark — the discipline test settles it. A discipline is what you
could follow in vanilla Self without changing semantics, and you
can't: Self's send is asymmetric in the metal (one privileged
receiver, lookup up its chain, slots contained in objects), while Korz
dispatches symmetrically over the whole context and keeps slots in a
global sea, guarded, not contained. The receiver survives only as
`{rcvr: stack1}` — **demoted to an ordinary dimension**, the same move
Self made on Smalltalk's classes, one level up (the paper says so:
"Just as Self reformulated the Smalltalk model…"). Future work pushes
the *selector* into a dimension too, with pattern-matching
specificity: the atom fully split. So the prototype needed machinery,
not manners: an interpreter, debugger, and partial IDE hosted on the
Self language, VM, and environment (Self-based syntax; the paper's
JavaScript-ish examples are cosmetic). And in Self everything is a
prototype, so "a prototype of Korz in Self" is the only kind of Korz
that Self could contain.

**Is the prototype metacircular — does it zoom into itself?**
Not yet, but the paper reaches for the zoom. The prototype is a
definitional interpreter (Korz-in-Self). Future work, verbatim: they
"have started to experiment with **dimensions that alter the behavior
of the interpreter**, such as handling failure or ambiguity" — the key
to method combination, e.g. an Ensembles dimension meaning "run every
slot for this message." Evaluator knobs surfacing as language
dimensions is metacircularity arriving sideways. Then the tantalizer:
if a slot's *contents* became one more component of its *guard*, the
contents/guard distinction dissolves — the sea of slots eating its own
structure. A full metacircular Korz needs a grounded bottom (3-Lisp's
tower ends in the ultimate machine) or "which interpreter applies?"
regresses forever. MOODY is the same experiment from the other end:
the room writing dispatch temperature *is* a dimension altering the
evaluator. **ASK:** how far did the interpreter-altering dimensions
get? What grounded the regress?

**Can you host Self in Korz once you're hosting Korz in Self?**
Yes, and cheaper than the reverse — the asymmetry is the insight.
Korz-in-Self took machinery (an interpreter). Self-in-Korz takes only
*restraint*: guard every slot on `rcvr` alone and you're writing Self
— the paper's own spectrum puts procedural at zero dimensions,
single-receiver OO at one. Self is a **subspace** of the sea of slots,
not an emulation, so the tower Self → Korz → Self doesn't stack, it
collapses: the inner Self is the outer Korz with discipline. Downward
hosting is discipline; upward hosting is machinery. Which inverts the
first question: Korz is not a discipline for using Self
multidimensionally — **Self is a discipline for using Korz
unidimensionally.**

**Is Korz optimizable with Self's JIT techniques, or does it need new
ones?**
The paper is nearly silent — one "efficient [Pirk07]" and Agesen cited
for tooling, not speed — so this is open territory, and his. Two
existence proofs cover the halves: Self proved the *dynamic* half
(inline caches, maps, customization, speculative inlining, deopt);
Julia — in the paper's references — proved the *symmetric multiple
dispatch* half (per-signature specialization, world-age
invalidation). Korz is Self's dynamism × Julia's dispatch, so the
toolbox transfers, but every technique needs translation:
maps/hidden classes become **context shapes** (nothing else recurs —
there's no object to attach a map to); inline caches become
**dimension-sliced PICs** keyed only on the dimensions any candidate
slot for that selector guards on; customization risks **combinatorial
explosion** across dimensions (Self had one dimension; this needs
lazy, profile-guided specialization — Ace's `$tradeoff` question,
answered automatically); deopt guards move to **context-extension
points** instead of every send; and the open sea needs an
**incremental discrimination DAG** per selector — the specificity
lattice compiled to a decision tree, patched on slot arrival, with
CHA-style invalidation. Genuinely new inventions required:
**dimension relevance analysis** (which dimensions can possibly
affect a selector — doesn't exist in Self or Julia because neither
has implicit context), explosion management, incremental lattice
compilation. And Korz′'s soft tier adds one with no precedent: the
model as interpreter tier, where profiling watches which
*improvisations* stabilize and compilation crystallizes them. Self's
JIT watched types recur; this one watches meanings recur. **ASK:**
where do his VM instincts put the cliff — context shapes, or the
discrimination lattice under mutation?

**Is the sea of slots a Linda tuple space?**
Close kin. Linda (Gelernter '85, generative communication) removed the
*recipient* from message passing: a tuple, once `out()`, floats free
of its producer, retrieved by content match. Korz removes the
*receiver* from dispatch: a slot floats free of any owner, retrieved
by guard match against the context. Both trade point-to-point
addressing for an associative commons — the sea of slots is a tuple
space where the tuples are behavior. The binding grammar converges
almost exactly: Linda's *actuals* (must equal) and *formals* (match
anything, **bind the value into the reader's scope**) are Korz's
*constrained* and *bare-name* guard stances (bare name binds the
coordinate into method scope as an implicit parameter); *unmentioned*
is the don't-care both share. The split is what happens on multiple
matches: Linda picks **arbitrarily** (it's a concurrency coordination
language; `in()` consumes the tuple and blocks — retrieval is
synchronization), Korz demands the **unique most-specific** (it's a
dispatch semantics; ambiguity is an error; slots persist, lookup never
takes), and the LLM **samples** a relevance-weighted distribution.
Arbitrary / error / sample — MOODY's dispatch temperature interpolates
between the last two. Punchline: transformer attention *is* a
differentiable tuple space — queries pattern-match keys, retrieve
values, `rd()` with "equals" relaxed to "resembles." Lineage: Linda →
blackboards → attention, with Korz as the branch where the retrieved
content executes. **ASK:** tuple spaces had their second life at IBM —
TSpaces, Almaden, late '90s; Ossher and Kimelman are IBM Research. Was
Linda in the room when the sea got named? Is a guard an anti-tuple?

**Layers aren't reified — the IDE restores them. What is a layer,
then?**
The paper's cited COP advantage is that layers are first-class and
visible in source; Korz declines to reify them and "relies on the IDE
to group slots as needed," presenting *different groupings as the user
needs them*. The analogy is the paper's own: Self showed objects could
play both instance and class; Korz shows guarded slot collections can
play both objects and layers — and in each case *IDE support restores
the higher-level abstractions* over a simpler, more malleable model.
Read structurally: a layer becomes a **saved view** — a query over the
sea, guarded by dimensions — not a language construct. Tables vs
views, with materialization on demand; you also duck the JOT paper's
layer-in-class vs class-in-layer dilemma entirely, because there is
nothing to put inside anything. This is Alan Kay's missing-HyperCard-
layer argument wearing a language-design hat: keep the kernel minimal,
and give *users* the authoring layer where they compose, save, and
share their own views — with **two-way** traffic, edits flowing back
through the view into the model (HyperCard cards, Morphic, Self 4.0's
outliners — his own environment already did this for objectness).
MOOLLM's version: the LLM *is* that IDE tier. Views are conversational
projections — ask for any grouping and it materializes; the
CARD/GLANCE/README pyramid is precompiled views at fixed resolutions;
directory listings are views; and prestoration proved the write-back
direction. **ASK David:** how much of Korz's usability burden did the
partial IDE prototype actually carry — and is layer-as-saved-query
enough, or do layers need identity for activation and ordering to
compose? What did Self 4.0's environment teach about restoring
abstractions the language refused to build in? **ASK Alan** (when the
memorial screen-share happens): is a user-composable, two-way view
layer over a slot soup the HyperCard layer he keeps saying is missing?

**How do mirrors work in Korz — disco ball or funhouse mirror?**
The paper defines no mirror API; the IDE is the reflective surface,
cutting subjective planes through the symmetric slot space. The model
forces the answer: a mirror on a subjective object must take a
**context as a parameter**, because the object doesn't exist until a
context gathers its slots. So: disco ball — many flat honest facets,
multiplicity in the ball, no distortion in the glass. A funhouse mirror
is one privileged image, warped. **ASK** (it's his mirrors paper,
Bracha & Ungar OOPSLA '04): what does a mirror reflect when the object
is subjective?

**How does COP relate to SOP?**
SOP (Harrison & Ossher '93, IBM) decomposes by *who is looking* —
composed perspectives, build time, symmetric. COP (Costanza &
Hirschfeld, ContextL) decomposes by *what is happening* — layers
activated at run time. Neither contains the other; the FOOL '14
position paper (local PDF)
argues both are projections of Korz: subject = viewer coordinate,
layer = guard, composition rules = dispatch specificity. **ASK:** still
hold that, ten years on?

**Is The Sims subject-oriented programming?**
Not in the IBM sense — one shared behavior tree per interaction, not
per-subject composed code. Grammatically subject-oriented (every tree
runs as a `me`), economically subjective (every Sim scores the same ads
differently; relationship matrices are one party's opinion),
compositionally shared. Korz diagnosis: `me` and `stackObject` are two
hardwired dispatch dimensions — a binary multimethod frozen in the VM;
Korz generalizes to N, addable later. The verb lives in the direct
object. And Zork got there first: ZIL dispatches every turn through
PRSA/PRSO/PRSI — verb, direct object, indirect object — plus WINNER
(the character; "ROBOT, PUSH BUTTON" rebinds it) and HERE (the
location; its action routine speaks first), with a fixed
action-routine cascade (room, indirect, direct, verb default). Five
hardwired dimensions and a frozen specificity order in the Z-machine,
1979 — and character + location are exactly the pair MOOLLM reifies
as directories. Full riff:
[case-zork.md](case-zork.md).
**ASK:** did the Korz team know they were generalizing two shipped
game VMs — and that one of them spells the language's name?

**Pronouns: this vs self vs me/it.**
`this` points at a thing (dehumanizing); `self` is the personhood word
(humanizing); The Sims went first-person `me` with the stack object as
grammatical direct object — "that" for the singular inanimate, "them"
when it deserves personhood. Korz's `rcvr` is convention plus
dot-notation sugar, nothing privileged: a Sims-shaped dialect with `me`
and `it` dimensions is fully within the model. The dimension names are
the language's pronoun system — choosing them is choosing who counts
as a subject.

**Named parent slots (Self) or a parent array (NeWS, MOOLLM)?**
Names buy directed disambiguation, mode-switch-by-role (Revolutionary
Chess reparents by role, not position), map-not-sequence mutation, and
keyed git diffs; order buys deterministic resolution. YAML dissolves
the tradeoff: maps preserve key order (named AND ordered), and Self's
trailing asterisk parses unquoted (`traits*:`) since YAML only reserves
leading `*` for aliases. Plus the **parents basket**: one `parents*`
slot holding an object whose slots are the parents — swap the basket,
swap the whole ancestry. A situation-chosen basket is a context; the
named parent slot looks like the proto-Korz-dimension. Full treatment:
[SELF-AND-MOOLLM §Named parent slots](https://github.com/SimHacker/moollm/blob/main/designs/object-system/SELF-AND-MOOLLM.md).
**ASK:** what did naming the parents buy Self in practice — and did
anyone use the basket idiom?

**Korz "context" vs LLM "context" — same word, same thing?**
Parallel, and the projection is load-bearing: bindings ↔ window
contents, decidable guards ↔ judged relevance, specificity ↔
attention, lookup ↔ sampling. Deterministic COP is the corner case at
`{temperature: 0, dimensions: enumerable, guards: decidable}` — which
is why the tiered-JIT thesis coheres. Going up opens latent-space
inheritance, semantic conflict resolution, generative miss handling,
and grounding for Drescher schemas. **ASK:** what would Korz look like
with an inferential dispatcher?

**Does Korz support dynamic and lexical binding?**
Both, split cleanly. Inside a method: ordinary lexical locals and
blocks (the paper declines to detail blocks). The implicit context is
the dynamic half — dimension bindings flow down the dynamic extent of
the call chain, rebind for sub-computations, revert after: Common Lisp
special variables, disciplined. The paper's related-work section names
it: prior work on "implicit arguments (or dynamic scoping)" *"did not
link implicit arguments to dynamic dispatch"* — that linkage is the
novelty. Dynamic binding answers "what value does `location` have
here?"; Korz also asks "which slot *exists*, given `location`?" No
Pascal-style nesting though: slots float flat in the sea, so lexical
scope lives only inside a method — there's no textual containment to
capture.

**Emacs buffer-locals: subjective objects in a text editor.**
Don's observation from years of Emacs programming-in-the-large:
`buffer` is a dimension. A buffer-local variable is a slot guarded
`{buffer ≤ thisBuffer}`; switching buffers rebinds one dimension and
the whole binding set — modes, syntax tables, keymaps — resolves
subjectively through it. Buffers-as-objects is subjective-objects
programming discovered independently: the "object" is gathered by the
current-buffer context, not owned by a container. It even worked in
UniPress (Gosling) Emacs Mocklisp — no lists, no dictionaries,
terribly lazy dynamic scoping — where buffers were the *only* object
system available, so the ambient context was the sole load-bearing
structure. And the detail too good to skip: since Emacs 24, elisp's
lexical binding is switched on by `lexical-binding: t` — **a
buffer-local variable**. The scoping regime itself is a context
dimension: the temperature-as-dimension move, shipped in an editor.

**The ambient-context catalog: the "current X" pattern, two flavors.**
The same shape recurs across systems programming: *binding stacks* —
PostScript's `gsave`/`grestore` graphics state and `begin`/`end`
dictionary stack (a literal dynamic scope for name lookup): push a
context, work, pop, structurally guaranteed to revert. Versus *raw
mutation* — OpenGL's state machine, Win32 GDI device contexts, MacApp
globals: the current X mutated in place, restoration by convention,
every bug a leaked binding. X11/NeWS server connections and token
tables sit between: per-connection context behind an explicit handle.
Korz's contribution to this old family is hygiene — context as
bindings per call chain, never global mutation, and dispatch reads the
same context that lookup does. **ASK:** does he read Emacs
buffer-locals as a Korz precedent? What's the design line between a
context dimension and a stateful API's "current X"?

**Before/after demons: language features become patterns.**
Don's observation: Korz lets you *wrap* minimal, essential methods in
**before and after demons** — slots that perform assertions, logging,
tracing, permission checks, anything cross-cutting — and then delegate
inward to the more essential method. The mechanics fall out of
dispatch: the demon slot guards one dimension more specifically than
the essential slot (a phase or aspect coordinate, or any extra
constraint), so it matches first; it does its demon work, then
re-sends with that dimension stripped or advanced, and the
next-most-specific slot — the essential method — runs. Stacking demons
is stacking dimensions; ordering comes from the specificity lattice,
not a combination DSL. What this buys is the point: **features of
other systems become patterns of a simpler system with fewer, more
essential features.** CLOS ships `:before`/`:after`/`:around` as
language features and needs the MOP — a protocol for designing *other*
object systems — to let you change them; AOP ships a weaver, with
pointcuts and advice as first-class machinery. In Korz the pointcut is
a guard, the advice is a slot, and method combination is something you
*write*, not something the language *is*. It's the same subtraction
run one more time: Self showed classes are a pattern of prototypes;
Korz shows objects are a pattern of guarded slots — and now CLOS's
flagship feature is a pattern of dispatch. The paper's own future work
gestures here from the interpreter side ("dimensions that alter the
behavior of the interpreter… the key to method combination, e.g. an
Ensembles dimension"); demons come at the same target from below, with
no interpreter change at all. And Ossher is the right co-author for
this conversation — subject-oriented programming and Hyper/J were IBM's
composition machinery; Korz makes the machinery an idiom. **ASK:** what
is Korz's `call-next-method` — is there a clean resend-to-next-most-
specific idiom for the demon's inward delegation, did the prototype
have one, and does demons-as-a-pattern make the Ensembles dimension
unnecessary — or is "run every matching slot" the one combination that
genuinely needs the interpreter?

**What does "super" even mean in Korz?**
Don's recollection (confirm with David): he named resend as an
unsolved — or at least unaddressed — problem of Korz. The history
explains why it goes hard here: every prior super was an anchor into
machinery the language hid, and Korz dissolved everything the anchors
held onto. Smalltalk's `super` is *static* — the compiler bakes the
method's defining class into the send; same receiver, lookup just
starts one level above where the method textually lives. Which already
gives the game away: super was never a different object, it was a
different *lookup position* — dispatch state wearing a keyword
costume. Self's `resend` anchors to the slot *holder* (and directed
resends name a parent explicitly). CLOS's `call-next-method` is
*dynamic interpreter state* — a closure over the remaining sorted
applicable-method list, handed to you mid-dispatch; the MOP even
exposes the list (`compute-applicable-methods`). So: defining class,
slot holder, linearization. Korz has none of them — no class, no
owner, and the specificity lattice is a **partial order**, so "next
most specific" inherits exactly the tie-ambiguity that Appendix B
legislates into errors, one level down. Two candidate meanings
survive the dissolution. (1) **Context weakening** — the demon
pattern's delegation: re-send with the discriminating dimension
stripped or generalized. Pure Korz, no interpreter reflection; but
semantically it is *re-dispatch from scratch*, not continue-from-here
— it can re-match the sender if the guard still passes (loop hazard),
and it answers "what would a poorer context see?" rather than "who is
below me?" (2) **Reified dispatch** — expose the matching computation
itself: the rest-of-the-lattice as a first-class value, a
`call-next-slot` closure the interpreter hands the winner. Honest,
and continuous with the paper's interpreter-altering-dimensions
future work — but it is precisely a **reflective function into the
interpreter**, and once dispatch position is data, the sea of slots
has a hidden second context ("where am I in the current send") that
the language's own contexts don't reify. That's the answer to Don's
question: yes — and it always was. Smalltalk just compiled the
reflection in statically; CLOS handed it to you as a closure; Korz,
having nothing left to hide it behind, would have to admit it's
reflection or define it away as weakening. Soft-tier coda: under LLM
dispatch "next most specific" becomes *resample, excluding the
previous draw* — super as rejection sampling — which suggests the
honest primitive was never "go up" but "try again, differently."
**ASK:** which did he mean by unsolved — that neither meaning is
right, or that both are and they don't coincide? And did the Self
prototype's interpreter keep a candidate list it *could* have exposed?

**Would Korz accept scored or stochastic dispatch?**
Korz argmaxes (most specific slot wins; Appendix B legislates ties).
The Sims auctioned all matching ads and dithered among the top N;
temperature could be a context dimension — `{temperature: 0}` recovers
classical Korz. And the auction is already running in this repo:
MOOLLM cards are bundles of Sims advertisements — guarded (`condition`)
and scored (`score`) — i.e. Korz slots with the precedence declared
numerically instead of derived structurally. See
[hosting-moollm.md §What are cards?](korz-prime/hosting-moollm.md). **ASK:** would he buy
dispatch as an auction?

**Can the LLM be the Korz interpreter, the way MOOLLM interprets Self?**
MOOLLM applies LLMs to executing Self with inferencing extensions:
inherit from latent space, smart context-sensitive method resolution.
The same move for Korz is [design.md](korz-prime/README.md) — one semantics,
two dispatchers: the VM compiles the decidable slots, the LLM
improvises over the rest (semantic coordinate match, prose guards,
sample-don't-error on ambiguity, fall through to latent space on a
miss), crystallize/deopt between the tiers. **ASK:** the Self JIT
watched types recur and compiled them; this one watches *meanings*
recur. Does the JIT analogy hold all the way up, or does inference
break some invariant the deopt safety net depended on?

**Filesystem: tree of Self objects, or soup of slots?**
MOOLLM views the file system as a tree of Self objects — directories
as prototypes, parent lists, delegation. Could it *also* view the same
files as a Korz sea of slots: semi-organized, but arbitrarily viewable
and groupable as subjective objects along parameterized dimensions?
Then the tree is just one saved view among many (see the layers
question above — layers as queries over the sea), and the LLM is the
IDE tier that materializes any grouping on demand. **ASK:** is the
Self reading and the Korz reading of the same directory a duality or a
hierarchy — and does the paper's "IDE restores the abstractions" line
predict that a filesystem never needed to *be* a tree, only to be
viewable as one?

**"Slot space" is a config system Don already runs in production.**
The paper: *"A body of Korz code is termed a slot space: a collection
of slots organized in a multidimensional space."* Chess shows the
shape — piece type, color, enumeration, behavior variant as composable
dimensions, one PAWN definition instead of a copy per combination
([GAME-PIECES](https://github.com/SimHacker/moollm/blob/main/designs/GAME-PIECES.md)).
And Don's **selfish configuration system** is the same thing with a
merge instead of a dispatch: JSON/YAML objects with parent reference
lists, deep-merged in order, deployed five times over —
machine-vision processor configs (live parent chains in production),
edgebox master configs (prototype-first, presence = enabled — note: no
null coordinate there either), cloud fleet ops (zones × SKUs ×
spot/on-demand as "a decidable cell space"), Pantomime's JSON
object/networking/build-target system, and MOOLLM's fragment config.
Receipts copied out:
[SELFISH-CONFIG-IN-PRODUCTION](https://github.com/SimHacker/moollm/blob/main/designs/SELFISH-CONFIG-IN-PRODUCTION.md)
and the full
[Fleet Weather design](https://github.com/SimHacker/moollm/blob/main/designs/FLEET-WEATHER-DESIGN.md).
**ASK:** config-merge at compose time vs dispatch at run time — same
slot space, two evaluation strategies. Did the Korz team think about
the compile-time projection?

## The pun shelf

Sea of slots → slot soup → the **Sea of Holes** (*Yellow Submarine*) —
one hole leads to the Sea of Green: follow an unbound dimension far
enough and you surface somewhere else entirely. Ringo kept a hole in
his pocket; every guard is a hole waiting for a context to fall
through it. And every don't-care is a hole the disco ball shines
through.

Related: [deep dive + MOOLLM mapping](sources/korz-paper-deep-dive-moollm-mapping.md) ·
chat guide ·
[his original Korz pointer](sources/2025-10-26-korz-email-hn-rollup.md) ·
[GAME-PIECES](https://github.com/SimHacker/moollm/blob/main/designs/GAME-PIECES.md) ·
[ENDOSYMBIOSIS](https://github.com/SimHacker/moollm/blob/main/designs/object-system/ENDOSYMBIOSIS.md)
