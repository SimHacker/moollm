# Neuro-symbolic: the divide, and why it was never a divide

**Companion to [`AXES-NOT-CAMPS.md`](AXES-NOT-CAMPS.md)**, which argues that the
famous design dichotomies name real choices and fake tribes. This is the same
argument applied to the one that is still being fought in public: symbols
against networks.

**Companion to
[`ongoingness/CURIOSITY-SCHEMA-LINEAGE.md`](ongoingness/CURIOSITY-SCHEMA-LINEAGE.md)**,
which traces the constructive line — Piaget → Papert → Minsky → Drescher →
Leela AI — and states the operational synthesis. That document is the *how*.
This one is the *why the framing is wrong*, plus the two histories in enough
detail to argue with someone who only knows one of them.

## The one-line thesis

Every system that has actually worked at anything hard has been a hybrid, and
the people usually cited as founders of the two camps were **both arguing
against single-mechanism theories in the first place.** The divide is a
retrospective invention, maintained mostly by people defending a position rather
than building something.

## The two histories, side by side

| | Symbolic line | Connectionist line |
|---|---|---|
| 1943–58 | McCulloch–Pitts; Turing's "Computing Machinery" | Rosenblatt's perceptron (1958), Mark I hardware |
| 1969 | Minsky & Papert, *Perceptrons* | the same book, read as a death sentence |
| 1970s | Minsky's frames; Schank's scripts; Lenat's AM | quiet |
| 1980s | Cyc begins (1984); Eurisko; expert systems | backprop popularized (Rumelhart, Hinton & Williams 1986) |
| 1986–91 | *Society of Mind* (1986); Drescher's *Made-Up Minds* (1991) | connectionism ascendant, then stalls on data and compute |
| 2009–12 | knowledge engineering seen as a bottleneck | "Unreasonable Effectiveness of Data" (2009); ImageNet (2012) |
| 2014–17 | | attention (Bahdanau et al. 2014); the transformer (Vaswani et al. 2017) |
| 2016– | search, proof, verification as components | scale, pretraining, finetuning, RLHF |
| now | tool use, hooks, deterministic checks | the substrate everything else is built on |

`verified: standard citations; dates are the well-known ones. Confirm any
specific claim before quoting it in public — this table is a map, not a source.`

## *Perceptrons* is the most misremembered book in the field

Because it is the load-bearing exhibit for the whole "the symbolists killed
neural networks" story, and the story does not survive reading it.

**What Minsky and Papert actually proved** was about a specific, limited object:
the single-layer perceptron. Parity — of which XOR is the two-input case —
cannot be computed by one. Connectedness cannot be computed by perceptrons
whose receptive fields are limited in diameter or in order. These are real
theorems about a real machine, and they are correct.

**What they did not prove** was that layered networks cannot learn. They said
that the extension to multi-layer machines had not been shown to overcome the
limits, which in 1969 was true, and the 1988 expanded edition returned to the
question directly rather than pretending it had not moved.

So the honest summary is uncomfortable for both sides: **a genuine mathematical
result about a weak model was read as a verdict on a research programme**, by a
field that wanted a verdict. Whether the book caused the funding collapse or
was recruited to justify one is a question about sociology, not about the
theorems.

`verified: needs-check before publishing the strong version — the parity and
connectedness results are secure; the causal claim about the funding winter is
contested in the literature and should be stated as contested.`

### And Minsky was never the anti-network figure the story needs

This is the part that dissolves the divide, and it is the most useful thing in
this document.

Minsky's objection to the perceptron and his objection to unified theories of
mind are **the same objection.** *Society of Mind* is an argument that a mind is
many mechanisms — agents, agencies, K-lines, frames, censors — with no single
principle at the bottom and no one representation that does all the work. A
person holding that view will object to *any* proposal that one elegant
mechanism suffices. In 1969 the candidate was a layer of weighted sums. Later
candidates got the same treatment.

Read that way, the man cited as the symbolic camp's founder is the field's most
consistent opponent of camps. Papert has the matching irony: co-author of the
book that constrained networks, and author of the constructionist programme that
says knowledge is built by the learner rather than installed — which is the
learning-side intuition, not the engineering-side one.

`See` [`../skills/design-sense/masters/marvin-minsky.md`](../skills/design-sense/masters/marvin-minsky.md)
`and` [`../skills/design-sense/masters/seymour-papert.md`](../skills/design-sense/masters/seymour-papert.md).

## Lenat: the maximal symbolic bet, and what it actually taught

Worth taking seriously precisely because it is the position most people think
was simply refuted.

**AM** (1976) searched for interesting mathematical concepts using heuristics.
**Eurisko** went further and let the heuristics modify heuristics, which is the
part that still reads as radical — a system editing its own search policy. Then
**Cyc**, from 1984, made the largest bet available: that commonsense reasoning
needed millions of hand-asserted axioms, and that somebody had to sit down and
assert them.

The standard verdict is that this failed and scale won. The more useful reading:

- **The diagnosis was right.** Lenat and Feigenbaum's "threshold of knowledge"
  argument — that competence requires an enormous quantity of background
  knowledge, not a better inference engine — is exactly what the last decade
  confirmed. It is *why* pretraining on the internet works.
- **The acquisition method was wrong**, and this is the whole lesson. Hand
  assertion does not reach internet scale, ever, and the bottleneck was never
  representation. It was intake.
- **So an LLM is a solution to Lenat's problem**, arrived at by a route he
  rejected. It is the knowledge acquisition step done statistically. What it
  does not supply is the thing Cyc had and LLMs lack: **a persistent, inspectable
  store you can query, check, and correct.**

Which is the argument for hybrids stated without any appeal to what is
fashionable: one line solved intake and cannot do bookkeeping; the other solved
bookkeeping and could not do intake.

## The strongest case against hybrids, stated properly

Any document arguing for both sides owes the reader the best argument that this
is a mistake, and there is a good one.

**Sutton's "bitter lesson":** the history of AI shows that general methods
which scale with available computation beat methods that build in human
knowledge, repeatedly, in domain after domain, and researchers keep failing to
learn it because the knowledge-engineering approach feels like progress and
gives better short-term results. On this account, every symbolic scaffold is a
crutch that will be removed by the next order of magnitude, and building
carefully around today's model's weaknesses is the classic error.

`verified: characterization of Sutton's 2019 essay; quote it from the source
before attributing wording.`

**This is not answerable by assertion, and it should not be dismissed.** Two
observations that bound it rather than refute it:

1. **It is an argument about where capability comes from, not about where
   *guarantees* come from.** Scale produces competence; it does not produce
   auditability, determinism, or a record. A test that must pass, a permission
   that must hold, a citation that must resolve — those are not capability
   problems and no amount of compute converts a probability into a guarantee.
2. **The scaffolding that gets removed is the scaffolding that encodes
   knowledge.** The scaffolding that encodes *policy* does not, which is the
   same distinction argued in
   [`RULES-INJECTION-CONUNDRUM.md`](RULES-INJECTION-CONUNDRUM.md): a skill that
   restates documentation decays with every release, and a skill that says *how
   we do it here* does not, because it is not a fact about the world.

So the honest position is narrow: **use the model for competence, use symbols
for commitments.** Anything you would want to prove, log, diff, or be held to
belongs on the symbolic side, not because the model is weak but because
guarantees are a different kind of thing than skill.

## The hybrids that actually work, as evidence

Not a wish list. These shipped and won.

- **AlphaGo and AlphaZero.** Neural policy and value networks inside Monte
  Carlo tree search. The network proposes and evaluates; the search verifies by
  playing it out. Neither half is sufficient and nobody describes this as a
  compromise.
- **AlphaGeometry.** A language model proposes auxiliary constructions; a
  symbolic deduction engine proves. The neural half supplies the intuition that
  search cannot enumerate; the symbolic half supplies the proof the network
  cannot certify. `verified: needs-check on the reported IMO problem count.`
- **DreamCoder and program synthesis generally.** A network guides search over
  programs, and the programs are the artifact — inspectable, runnable, and
  correct or not correct independent of the network's confidence.
- **Tool use and function calling, which is the everyday case.** The moment a
  model calls a calculator, runs a query, executes a test, or reads a file, it
  is a neuro-symbolic system, and this is now the normal way of working. Most
  people using it do not call it that, which is the clearest evidence that the
  divide has stopped being real in practice while remaining live in argument.
- **Hooks and mandatory checks.** The least glamorous and possibly the most
  important: a deterministic gate the model cannot talk its way past. See
  `Determinishtic` in
  [`../skills/no-ai-parrot/corpus/CORRECTIONS.md`](../skills/no-ai-parrot/corpus/CORRECTIONS.md)
  for the coinage.

One framing to use carefully: **System 1 and System 2 is a metaphor, not an
architecture.** It is useful for explaining the shape to someone in one
sentence and it licenses no design decisions. Reaching for it as though it
specified an interface is how a good analogy becomes a bad plan.

## Where this repository stands, concretely

MOOLLM is a neuro-symbolic system in the plainest sense, and the parts map
cleanly onto the two histories:

| Component | Which side | Doing what |
|---|---|---|
| The model | neural | Coherence, retrieval, proposal, natural-language interface |
| Skills, cards, GLANCE/CARD/SKILL | symbolic | Persistent, inspectable, diffable structure with declared interfaces |
| K-lines | symbolic, Minsky's | Activators — reassemble a context by name |
| Advertisements and auctions | symbolic, Wright's | Candidate affordances, scored, so choice is explicable |
| Schemas | symbolic, Drescher's | `context → action → expected result`, with prediction error as the learning signal |
| Hooks, tests, the compiler-as-linter | deterministic | The gates. Not persuadable |
| The filesystem | symbolic | The store Cyc had and a context window does not |

The two claims worth making about that arrangement:

**The LLM supplies exactly what the symbolic architectures lacked, and vice
versa.** Drescher's schemas needed grounded symbols and had empty Lisp atoms;
the model arrives with billions of grounded associations. The model needs
persistence, identity over time, and an audit trail; the filesystem and the
skill tree are that. This is argued at length in
[`ongoingness/CURIOSITY-SCHEMA-LINEAGE.md`](ongoingness/CURIOSITY-SCHEMA-LINEAGE.md),
including the observation that **schemas pointing at schemas, K-lines
reactivating agents, and attention pointing at latent representations are one
pattern on three substrates** — symbolic in the 1980s, developmental in the
1990s, differentiable now.

**Grounding is three different things and conflating them causes most of the
confusion.** Relational and social grounding come from the model, imperfectly.
*Operational* grounding — concepts bound to persistent objects with state,
affordances, consequences and history — comes from a microworld, and that is
what this repository is for. The model's common sense is **a prior, not an
oracle**: it proposes plausible structure and the world corrects it.

### Leela AI is firmly in the "both" camp, and the roster is the argument

Not a hedge and not a synthesis proposed from outside — **an explicit
programme**, reimagining a specific body of work rather than reacting to a
trend:

- **Minsky's Society of Mind** — many mechanisms, no single principle, agents
  all the way down
- **K-lines** — reactivating a mental state by name, which is what a skill
  invocation is
- **Papert's microworlds** — a bounded world with real consequences, so concepts
  can be *operationally* grounded rather than merely described
- **Constructionist programming** — you learn the thing by building the thing;
  see [`../skills/design-sense/`](../skills/design-sense/) on Papert
- **Drescher's schemas, and the schema factories** — `context → action →
  expected result`, with prediction error as the learning signal, and machinery
  that builds new schemas out of old ones
- **Learning algorithms** — the connectionist half, doing the work it is
  actually good at

**Every one of these hit a wall, and it was the same wall: grounding.** The
symbols were empty. Drescher's atoms had no content, Cyc's assertions had no
sensorimotor purchase, and the microworld's concepts stopped at the microworld's
edge. That is the honest reason the programme stalled, and it should be conceded
before claiming anything for the revival.

**What changed is that LLMs arrive pre-grounded in exactly the currency those
architectures were short of.** Billions of relational and linguistic
associations, available as a prior. So the old structures are not merely
rehabilitated, they are *more* fruitful than they were: a schema whose terms
mean something can generalize; a K-line that names a rich latent region
activates something real; a microworld whose objects the model already
understands does not need its ontology hand-built.

**And the line runs through actual people rather than a literature search.**
Papert and Minsky to Drescher's thesis and *Made-Up Minds*, then implemented in
Lisp and Python at Leela AI with **Henry Minsky as CTO and Drescher advising** —
so the grounding wall is a remembered engineering experience rather than a
historical anecdote. That is the same lesson as
[`AXES-NOT-CAMPS.md`](AXES-NOT-CAMPS.md): the ideas travel in people, and the
camps get drawn afterwards by people who were not there.

## How the label goes wrong

"Neuro-symbolic" is now also a fashion word, and it fails the same test as every
other label in the companion document: **does a claim follow it?**

- **Empty use:** calling a system neuro-symbolic because it has a network and
  also some `if` statements.
- **Real use:** naming which half supplies capability, which half supplies
  guarantees, and what happens at the boundary when they disagree.

The boundary is the entire design problem. Everything above is preamble to it,
and the answer this repository gives is: **the deterministic side wins ties,
because the point of having it is that it cannot be argued with.**

## See also

- [`AXES-NOT-CAMPS.md`](AXES-NOT-CAMPS.md) — the general form: real axes, fake
  tribes, and why the geography never worked
- [`ongoingness/CURIOSITY-SCHEMA-LINEAGE.md`](ongoingness/CURIOSITY-SCHEMA-LINEAGE.md)
  — the constructive lineage and the integrated decision loop
- [`RULES-INJECTION-CONUNDRUM.md`](RULES-INJECTION-CONUNDRUM.md) — policy
  survives model improvement; knowledge does not
- [`ADVERTISEMENT-AUCTION.md`](ADVERTISEMENT-AUCTION.md) — the Sims mechanism
  as the symbolic half of action selection
- [`../skills/no-ai-parrot/corpus/CANON.md`](../skills/no-ai-parrot/corpus/CANON.md)
  — Minsky 1982, "Why People Think Computers Can't," which answered the genre
  forty years early
