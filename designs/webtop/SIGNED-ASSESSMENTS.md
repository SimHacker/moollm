# Signed assessments: rating as a compiled tagsonomy

**The unit is a signed assessment record, and its vocabulary is a tagsonomy the build compiles.**
Everything else here — reader-turnable knobs, question ledgers, overlay views — is a rendering of
that one record type over that one vocabulary.

This is the same machinery as [`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md), pointed at
judgments instead of subjects. There, freehand utterances get tags, synonyms and definitions
proposed by a model, confirmed by a human, and crystallized at build time into a static index with
no runtime resolution cost. Here the same pipeline runs on *what people think about claims*, and it
buys the same three things: comparability, countability, and compilability.

| Tagsonomy concept | Assessment concept |
|---|---|
| parent tag | **dimension** — `truth`, `evidence`, `argument`, `stance`, `novelty` |
| child tags under a parent | **rungs** — the closed, ordered value set for that dimension |
| alias interned to one object | **freehand input mapped to a rung** — "this seems sketchy" → `truth: speculation` |
| tag applied to a node | **assessment** — but *signed*, which is the one thing tags usually are not |
| build crystallizes the index | **static aggregate index**, so the corpus renders with no backend |
| collision lint | **distinctness lint** — two rungs that no rater separates in practice are one rung |

An assessment has **author, target, dimension, value, date, evidence.** Everything in this document
follows from that shape, and the sections below are: why it must be signed, why the vocabulary must
be closed, how it compiles, how it renders, and where it fails.

## Why the record is signed, and there is no universal layer

Gwern.net puts a confidence tag at the top of a page. The tag is an annotation *about* the document,
sitting outside it, doing nothing.

**Certainty is not a property of a proposition.** It is a relation over *knower × claim × evidence ×
assumptions × time*. A page-level tag flattens five dimensions to one scalar and attaches it to the
wrong object. And if there is a knower in the relation, **an unsigned confidence field is a category
error**: a `know:` value on an object with no author claims to be a fact about the world, which is
the one thing epistemic metadata can never be.

So the unit is not a field on a node. It is an **assessment record**: authored, owned, dated, aimed
at a target, optionally carrying evidence, and free to conflict with the assessment sitting next to
it.

**This is where the analogy to ordinary tagging breaks, and the break is the point.** A tag is a
claim about a thing. An assessment is a claim about a thing *by somebody*. Tagsonomies normally
collapse raters — `#dubious` is `#dubious` whoever applied it — and collapsing raters is exactly the
failure this document exists to prevent. So the compiler is inherited and the anonymity is not:
every leaf carries its author, and the aggregate is a view over authors rather than a replacement
for them.

### The two models, side by side

| Wrong model | Right model |
|---|---|
| `know: plausible` on the node | *This person* assessed *this span* as `plausible` on *this date*, citing *this* |
| One value, universal | Many values, attributed, in disagreement |
| Confidence is metadata | Confidence is a **position somebody holds** |
| Unowned, so unaccountable | Owned, so answerable |

**The target needs a durable anchor**, which is the same span problem as transclusion — and the W3C
Web Annotation Data Model already solved it with `TextQuoteSelector`, which stores an exact quote
plus a prefix and suffix so the anchor survives edits that a character offset would not. Same
standard supplies `creator` for the signature and `motivation` for the kind of act — *assessing*,
*questioning*, *commenting*, *endorsing*, *moderating* — which is itself a constrained vocabulary,
already specified, already implemented by Hypothesis.

### The vocabulary is closed, and that is the whole trick

Free-text annotation fragments: forty spellings of the same objection, none of them commensurable.
Unbounded numeric scales invite fake precision — `0.73` is a lie with a decimal point in it. So each
dimension gets **a small closed set of named values**, and votes within a dimension become
comparable, countable, and compilable.

The receipt is **Slashdot**, which shipped
*typed* moderation in the late nineties — Insightful, Informative, Interesting, Funny, Redundant,
Offtopic, Flamebait, Troll, Overrated, Underrated — a fixed keyword set where the *kind* of judgment
was part of the vote. Stack Exchange does the same with its closed set of close reasons. Wikipedia's
inline templates (`{{citation needed}}`, `{{dubious}}`, `{{who?}}`) are a closed vocabulary too, and
their flaw is instructive: **the objection is visible in the text but the objector is not**, recorded
only in the revision history. Signed, they would be assessments.

Dimensions worth separating, because one scalar conflates them:

| Dimension | Closed value set | Asks |
|---|---|---|
| `truth` | fiction · rumor · speculation · plausible · likely · supported · established | Is it so? |
| `evidence` | none · anecdote · cited · reproduced · executable | What backs it? |
| `argument` | fallacious · weak · sound · rigorous | Does it follow? |
| `stance` | oppose · doubt · neutral · agree · endorse | Where do *you* stand? |
| `novelty` | restatement · synthesis · new-to-me · new | Have I seen it before? |

`evidence` is the axis Don is pointing at with *supported by objective evidence*: an assessment that
links a source, a computation, or **a test that runs** is checkable rather than merely counted, which
is the difference between reviewing and voting.

This closed vocabulary is not a separate mechanism from the rest of the corpus — it is exactly what
[`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md) compiles, and the LLM's job is the same one it
does for synonyms: map somebody's freehand "this seems sketchy" onto `truth: speculation` and let the
human confirm.

## The first rendering: the Know Knob, and the button both knobs came from

**A button at a science fiction convention dealer's table read QUESTION AUTHORITY.** Don read it as
an honorific — *this man is an authority on questions, so go ahead and ask him some, he'll give you
authoritative answers* — and only later worked out it was a call to action.

Both parses are grammatical. `question` is a verb and `authority` its object, or `question` modifies
`authority` and the phrase names a role. The button is a Necker cube for syntax, and it is stable in
neither reading for long.

**Keep both.** They name the two non-assertive motivations, and the misreading is the half nobody
builds.

| Parse | Reads as | Rendering | Motivation |
|---|---|---|---|
| Imperative verb + object | *Go question authority.* | **Know Knob** | contest |
| Noun-noun compound | *An authority on questions.* | **Wonder Knob** | inquire |

Assertion is the third motivation and the only one the web ships. **Assert, contest, inquire** — one
record type, three values in its `motivation` field, which is the vocabulary the W3C model already
uses.

Turning a knob is then a precise operation rather than a vague one: **select a rung on an ordinal
dimension, and choose an assessor set.** The document re-renders through it:

1. clean narrative
2. certainty markers and attribution
3. assumptions, provenance, dates
4. expanded counterarguments
5. full audit — sources, revision history, executable tests

It is a knob rather than a filter because the rungs are ordinal: there is a *more* and a *less*, so
the control is a position on a ladder rather than a set of checkboxes.

### So the knob has a second axis: whose knowledge

Once assessments are signed, depth is not the only thing to turn. **You can also choose the assessor
set** — mine, the author's, people I have chosen to trust, everyone, or one specific named person.
Reading the corpus through Ted Nelson's assessments and then through gwern's is a different act than
reading it through an average, and neither is "the" view. This is reader agency considerably past a
tag at the top of a page, and it is the epistemic form of multi-userness rather than the presence
form.

Gwern's own tag survives all of this unchanged in content and improved in honesty: it becomes
**gwern's assessment, signed gwern**, which is what it always actually was.

### Aggregation must bridge, not count

Counting votes produces a leaderboard, and a leaderboard is the failure mode this document is about.
The state of the art is **bridging-based aggregation**, as in Community Notes: a note gains standing
when it is rated helpful by raters who *usually disagree with each other*, so agreement across a
divide counts for more than volume within a faction. Brigading a bridged score requires manufacturing
consensus among opponents, which is expensive in a way that manufacturing upvotes is not.

Precise claim, since the mechanism is easy to overstate: bridging raises the cost of capture. It does
not eliminate it.

### Where the records live, given no server

Assessments are objects, so they live where objects live: a `type_id` branch or a pull request, per
[CURSOR-STORAGE.md](CURSOR-STORAGE.md). The **build compiles them into a static aggregate index**, so
the published corpus renders knobs with no backend, no key, and no model in the loop — and melting
back up to re-aggregate is a rebuild. Live where liveness matters, git where permanence does, exactly
as in [PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md).

### Disagreement is the normal state, not an error

Two signed assessments in opposition are the system working. The renderer must **show the split
rather than resolve it** — which is the one place this design can implement contestability instead of
merely claiming it. An averaged score that hides a bimodal distribution is a lie no single assessor
told.

**Which means the point is to take a position, loudly, in a namespace that is yours.** Don's
intended use of this machinery is to plant a flag on emacs versus vi, tabs versus spaces, and every
other hill worth dying on — in his own public repo, signed, under his own name. That is not a misuse
of an epistemics feature; it is the feature. An assessment layer whose only permitted register is
cautious hedging has smuggled a personality in through the back door, and a boring one.

It also separates two kinds of disagreement that a single score conflates. `truth` and `evidence`
disputes are **evidentiary** — more evidence can move them, and bridging is meaningful there.
`stance` disputes are often **taste**, and no amount of evidence will settle tabs versus spaces
because there is nothing to settle. Averaging stances is meaningless; averaging truth assessments at
least aspires to something. So a renderer should present taste dimensions as **a map of who believes
what**, never as a consensus number, and the dimensions table exists so the machinery knows which
kind it is holding.

### The generalization is Leary's Mind Mirror

**Mind Mirror** (Timothy Leary, Electronic Arts, 1985) already did the load-bearing half of this,
and did it on people rather than claims: you rated a subject along **graded scales** to produce a
profile, and the tool's central act was **overlaying two profiles and looking at the difference.**
It never claimed to measure anyone truly. A Mind Mirror profile was, by construction, *somebody's
rating of somebody* — signed, subjective, and interesting precisely because it could be compared with
a different rating of the same subject.

That is the whole argument of this section, shipped as a consumer product in 1985. What is
generalized here is only the target: **swap the subject from a person to a claim**, keep the graded
scales, keep the signature, and keep profile comparison as the primary view rather than a fallback.

Two consequences worth taking:

- **Render the rungs as gradations, not labels.** `fiction · rumor · speculation · plausible ·
  likely · supported · established` is an ordinal ladder, so it can be drawn as a position on a
  scale — Mind Mirror's bars — rather than as a badge. That keeps the *distance* between two
  assessments visible, which a categorical chip discards. Named rungs remain the storage format
  because `0.73` is still a lie with a decimal point in it; the gradation is a rendering of the
  ladder, not a replacement for it.
- **Overlay is the default view.** "Whose knowledge" stops being a filter and becomes a
  **comparison**: my profile of this claim against yours, with the gap as the object of interest.
  Which is the same move as showing the split rather than resolving it, arrived at from the
  interface side.

Existing coverage of Mind Mirror in this repo is about representation ethics — simulation is not
impersonation — in [`../ethics/MIND-MIRROR-FOUNDATION.md`](../ethics/MIND-MIRROR-FOUNDATION.md) and
[`../../skills/mind-mirror/`](../../skills/mind-mirror/). This is a second, independent debt to the
same product: its **rating mechanics**, not its disclaimer.

**The recursion is what makes this more than display.** Simulation rules can be assessed too, and by
their own author first: a population-growth rule whose author signs it *plausible, short-term,
fails-when resource-limited* stops impersonating natural law — and anyone who has run the model can
attach a competing assessment with the run as evidence, which is the `evidence: reproduced` rung
doing real work. Turn the knob on a running world and the floorboards go
transparent: this is observation, that is assumption, that one is a guess, this is ideology, and that
is a joke somebody left in. A microworld that can show its own epistemic frame is a different kind of
artifact than one that cannot.

Prior art worth crediting, because it shipped: **GreaterWrong's theme tweaker** gave readers control
over presentation years ago. Reader-controlled rendering is not a new claim; extending it from
typography to epistemics is the move.

## The second rendering: the Wonder Knob, ignorance as an object

Low confidence cannot say *I don't know.* Zero means **certainly false**. Fifty percent can mean a
well-understood balance of evidence, which is knowledge, not ignorance. The scale has no cell for the
thing you have not looked into.

So the second knob measures **question volume**: a `?` that grows with curiosity, plus an ask switch
that broadcasts *answers wanted* and specifies what kind is welcome — evidence, estimates,
speculation, personal experience, someone willing to run the experiment. Ignorance becomes a visible,
addressable, socially actionable object instead of a blank. The asker turns it down as things
resolve, and **the history of having wondered survives the resolution**, because that history is the
interesting part.

**A question is the same record with a different motivation.** Author, target, dimension, value,
date, evidence — a question fills in author and target, leaves the value open, and names what kind of
evidence would close it. So *assert, contest, inquire* are not three subsystems but three motivations
on one signed record, which is the vocabulary the W3C model already uses (`assessing`, `questioning`,
`commenting`). One store, one anchor mechanism, one aggregation pass, three verbs.

And a signed question is answerable in a way an unsigned one is not: you know who wants to know,
which is most of what determines whether answering is worth anyone's time.

Don's misreading names the role this creates. Someone with the knob turned up *is* a question
authority: their standing comes from the quality of what they have not settled. That is not a joke
about humility. In a corpus, an inventory of well-formed open questions is more useful than another
confident summary, and much rarer.

It is also the fuel for [AUTO-FAQ.md](AUTO-FAQ.md). A question broadcast in context, answered in
context, and kept as an artifact is the compiler thesis applied to dialogue.

### The Wonder Knob is also a doubt-manufacturing machine, and here is why it isn't

**"Some people are saying." "Questions are being raised." "We're just asking questions."** This is
the interrogative smear, and it works because **a question's presuppositions survive the question
form.** *Why did X do Y?* asserts that X did Y while committing the speaker to nothing — the
assertion's effect without the assertion's accountability. Pair it with the agentless passive and the
asker disappears too: *questions are being raised* deletes whoever raised them. Fox's house
formulation is the best-known instance; the technique is much older and belongs to nobody.

A feature that makes broadcasting questions cheap and gives status to question volume is a doubt
factory with a nice interface. Saying so is not optional.

**Three properties of this design break the move, and they are not add-ons — they are the same
properties that make assessments accountable in the first place:**

1. **There are no unsigned questions.** The move's entire force comes from the anonymous plural.
   *Some people are asking* cannot be expressed as a signed record; the record type demands an
   author, so it renders as *Don is asking*, which is a position he can be held to. The smear
   requires a crowd that cannot be enumerated, and this store cannot represent one.
2. **A question must name what would answer it.** The `evidence` field on an inquiry says what kind
   would close it — a citation, a computation, a run, an experiment someone is willing to do. A
   question engineered never to close refuses to name its closing conditions, because naming them
   forfeits the move. So **make it required, and a question with no answering conditions is malformed
   and fails the lint.** That single field is a mechanical distinction between inquiry and
   insinuation, and it costs nothing.
3. **Resolution history is kept.** The JAQ move depends on questions being re-askable forever in a
   medium with no memory. Here the history of having wondered survives the resolution, so a question
   that was asked, answered, and asked again is visibly that — and *who* keeps re-asking it after it
   closed is itself a fact on the record.

**Where it is legitimately useful, surgically.** The speech act is not inherently corrupt; four cases
earn it:

- **A hypothesis you cannot yet support but think matters** — signed, with what would settle it. That
  is ordinary science and the reason the inquire motivation exists.
- **Reporting real question volume, with the names attached.** *These forty signed people are asking
  X* is a fact about the corpus rather than a rhetorical device, and it is a fact precisely because
  the forty are enumerable.
- **Socratic exposure** — asking what you already know the answer to so the reader derives it. Sound
  pedagogy, but it pollutes the question-volume metric with performed ignorance, so it needs its own
  value: `rhetorical` versus `genuine`, declared by the asker.
- **Asking because asserting is unsafe.** Someone with real exposure may be able to ask what they
  cannot afford to claim. This is the one case where reduced attribution is the point, and it should
  be served deliberately through the unverified tier in
  [CONTRIBUTION-BOT.md](CONTRIBUTION-BOT.md) rather than arrived at by accident.

**The residual hole, which is real and not fixable inside the system.** All three defenses work on
our surface and none of them survive export. **Aggregation deletes authorship, which is exactly what
the propaganda move requires** — so any count we publish is a ready-made *some people are saying* for
somebody else's purposes, and a screenshot strips the signatures for free.

The mitigation is a rule about rendering, and it is the strongest concrete thing on this page:
**never render a count without its signature list.** No bare *N people are asking.* If the names do
not fit, the number does not ship. That makes our own aggregates harder to weaponize and, more
usefully, makes it obvious when someone has stripped them.

And the honest cost: `rhetorical` versus `genuine` is self-reported, so it is gameable by anyone
willing to lie about their own curiosity. There is no fix. Keep the ledger, and note that a corpus
where somebody's questions never close is information about that person.

## The badge trap, which is real

**Ian Bogost built Cow Clicker as a satire of social games and it acquired sincere fans who liked
clicking the cow.** He had to stage an apocalypse to end it. The lesson generalizes: a critical
artifact placed inside the system it critiques gets consumed as content.

The button is that lesson in miniature. Worn on a jacket at a convention, QUESTION AUTHORITY is a
status token that **costs nothing to display** and requires no questioning of anything. The signal
detaches from the act, and once detached it can be collected.

Every mechanism on this page has the same failure mode waiting for it. Confidence rungs become a
leaderboard the moment high certainty reads as high status. *Answers wanted* becomes an engagement
feed. Question volume becomes a metric, and a metric becomes a quota. At which point the honest name
is not gamification — per Bogost's [*Gamification Is
Bullshit*](https://bogost.com/writing/blog/gamification_is_bullshit/) it is **exploitationware**, and
he is right about that.

### The mitigation: make the display be the work

A badge fails because it is a token *standing for* an act. The fix is to display the act itself.

- **An open-question ledger cannot be pinned on.** It shows actual questions, dated, attributed, each
  naming what kind of answer would satisfy it, sitting in public next to its resolution or its
  continued absence. You cannot wear that without having wondered.
- **Signing does most of the work.** A count is gameable because the vote detaches from the voter; an
  assessment carries its author, its date, and its evidence link, so a bad one is *attributable* and
  a hollow one is inspectable. Add bridging aggregation and the cheap attack — volume within a
  faction — stops paying.
- **Invert the status gradient.** Standing accrues to exposed ignorance rather than asserted
  certainty — which is Socratic, is the opposite of what a confidence leaderboard rewards, and is
  cheap to implement because the ledger is already the artifact.
- **Publish the audit next to the feature.** Write down what the mechanism argues *procedurally*, in
  a critic's voice, and ship it with the mechanism.

Running that audit is what forced the signing model above, so here is the result. **An unsigned
confidence dial argues that certainty is a reader preference and disagreement is a settings
question** — a claim nobody would defend in prose, asserted structurally by the interface. Signed
assessments argue something else: *certainty is a position somebody holds, for reasons you can
inspect, and other people hold different ones.* That is a procedural argument worth making, and the
difference between the two is a design change rather than a disclaimer.

### What the mitigation does not do

It does not confer immunity, and claiming otherwise would be the same move it warns about. A ledger
is countable, and anything countable is gameable: an institution can absolutely require ten questions
a week. The claim is narrower — **a hollow question is more expensive than a hollow badge**, because
it must be answerable-shaped, it sits in public beside its non-resolution, and a reputation for
asking empty questions is itself legible. That is a friction field, not a wall. Bogost's hazard is
permanent and the correct posture is to keep re-running his analysis on ourselves rather than to
declare it handled.

## Honest costs

- **Two knobs is one more control than most readers want.** Both must default to off and stay
  invisible until asked for, or the corpus reads as instrumentation rather than prose.
- **Authoring burden is real.** An assessment on every object is not going to happen by hand. The LLM
  can propose values at build time and a human confirms — the same arrangement as synonym generation
  in [hyperties/ARTICLE-SCHEMA.md](hyperties/ARTICLE-SCHEMA.md), and it fails the same way if nobody
  reviews it. **An LLM-proposed assessment must be signed by the model and the run**, never laundered
  into an unattributed value, or the whole signing discipline is for nothing.
- **Cold start is the hard problem.** Almost every span will have zero assessments, and a knob with
  no data behind it is furniture. The author's own signed assessments are the bootstrap, which is why
  gwern's existing per-page tag matters: it is a real corpus of real assessments already written, and
  it only needs a name attached.
- **Signing needs identity, and the static tier has no accounts.** GitHub identity is the cheap
  answer, since assessments arrive as commits or pull requests and are therefore already signed by
  the substrate. Pseudonyms are fine — a stable pen name is a knower — but *anonymous* assessment
  breaks the model, because an unattributed value is the universal-metadata error wearing a
  disguise.
- **Named rungs still invite false precision.** *Supported* versus *likely* will be argued about, and
  the argument is mostly not worth having. Fewer rungs is probably better than more.
- **Inheriting the compiler means inheriting its failure mode.** A rung collision fails the same way
  a synonym collision does — **silently, by resolving to a plausible wrong value** — and it is worse
  here, because two raters who mean different things by *supported* produce an aggregate that looks
  clean and means nothing. So the distinctness lint is not optional: measure whether raters actually
  separate two adjacent rungs in practice, and **merge the pair when they do not.** A rung nobody
  distinguishes is not a fine distinction, it is noise with a name.
- **A public ignorance ledger is a privacy surface.** What you have not looked into is information
  about you. Same three gates as the path grammar: local by default, share by act, redact by pass.

## Related

- [AUTO-FAQ.md](AUTO-FAQ.md) — questions answered in context and kept as re-activatable artifacts
- [PLAYABLE-CORPUS.md](PLAYABLE-CORPUS.md) — the room that has someone in it to ask
- [OBJECTIONS.md](OBJECTIONS.md) — the strongest case against all of it, which is where Bogost belongs
- [READING-CURSORS.md](READING-CURSORS.md) — who is asking, and from where
- [SUMMARY-GENRES.md](SUMMARY-GENRES.md) — same rung, different register
- [`skills/no-ai-hedging/`](../../skills/no-ai-hedging/) — the ambient version already in force: state confidence as a number, then make the claim plainly

↑ [webtop hub](README.md)
