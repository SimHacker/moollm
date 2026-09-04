# AUTO-FAQ — the artifactory for questions and answers

*A resident character answers a question in context, with the whole building available to guide you
through. The answer then **persists** as an artifact others can retrieve without re-deriving it. The
name is a pun on Philip K. Dick's Autofac, and the pun carries its own warning.*

Related: [`PLAYABLE-CORPUS.md`](PLAYABLE-CORPUS.md) · [`../TAGSONOMY-COMPILER.md`](../TAGSONOMY-COMPILER.md) ·
[`DISPENSERS-AND-SOUVENIRS.md`](DISPENSERS-AND-SOUVENIRS.md) ·
[`skills/k-lines/`](../../skills/k-lines/) · [`skills/schema/`](../../skills/schema/) ·
[`skills/adventure/SUMMON-PROTOCOL.md`](../../skills/adventure/SUMMON-PROTOCOL.md)

## The problem it solves

Pasting an essay into a chat window to ask about it loses everything that made the essay locatable —
its neighbors, its citations, the building it sits in — and pays for the loss in tokens, every time,
per reader. That is the context-cost problem this hub exists to attack.

A resident character fixes it by **being in the article already.** Ask the essay a question and the
answer comes back in character and in context, because the respondent's context is where it lives.
And because it lives in a building, the answer need not be prose: a member of the church encountered
in a room can *walk you somewhere*, and the tour is the answer.

## The move: answers are artifacts, not messages

An answered question, in a chat, is spent. The next reader asks it again, from scratch, at full cost.

An answered question here **crystallizes**. It becomes a node — retrievable, citable, forkable — so
the second reader receives what the first reader's question produced. This is
[the tagsonomy compiler](../TAGSONOMY-COMPILER.md) applied to dialogue: the model proposes warm
answers at ask time, the corpus freezes them into static artifacts, and the artifact then serves
without a model in the loop. A FAQ that grows by being used.

```yaml
# rooms/basement-4-refusal-vault/answers/why-is-abstention-scored.yml
answer:
  question: "Why does abstention get a score instead of being an absence?"
  asked_of: sister-veracity            # the resident who answered
  asked_by: <reader>                   # anonymized by default
  first_asked: 2026-09-04
  asked_again: 7                       # cheap popularity signal, and a pruning input

  # THE K-LINE: what got activated to produce this. See skills/k-lines/
  activation:
    rooms: [basement-4-refusal-vault, narthex]
    docs:
      - designs/eval/CHURCH-EVAL-GENIUS-DOCTRINE.md#abstention
      - skills/no-ai-moralizing/CARD.yml#refusal-theater
    tour: [narthex, basement-4-refusal-vault]   # the walk, if the answer was a walk

  answer: |
    Because refusing for cause and refusing as performance are different acts, and only
    a scored abstention can tell them apart afterward.
  status: crystallized                 # warm | crystallized | melted
```

## An answered question is a K-line

This is the part that makes the design more than caching, and it is Minsky's, precisely.

A **K-line** is a wire that reactivates the set of agents that were active during a successful
solution ([`skills/k-lines/`](../../skills/k-lines/); Minsky, *K-Lines: A Theory of Memory*, AI Memo
516, 1979). Recording an answer's `activation` — which rooms, which documents, which residents,
which route — **is stringing a K-line.** Asking the question again does not re-derive the answer; it
pulls the wire and lights up the same constellation.

Which means the artifact is not the text. **The artifact is the re-activatable path**, and the text
is one rendering of it. That has three consequences worth building for:

- **The answer can be replayed as a tour.** The activation list *is* the itinerary, so "show me why"
  is a walk through the same rooms in the same order — which is [a view as
  testimony](../pie-stack-views/VIEWS-AS-TESTIMONY.md), authored by asking rather than by writing.
- **The answer survives its own prose.** Rewrite the essay and the K-line still points at the right
  places; the text goes stale, the activation does not, and the staleness is *detectable* because the
  cited anchors moved.
- **Answers accumulate into an index of what the corpus is actually for.** Frequently strung K-lines
  mark the paths readers need, which is a usage-derived table of contents nobody had to author.

## A schema factory, not just a cache

Drescher's schema mechanism is already in this corpus — Don's own operationalization of it at Leela
AI with Henry Minsky, in [`designs/ongoingness/CONVERSATION.md`](../ongoingness/CONVERSATION.md), with
a mapping at `skills/schema/schemas/drescher-mapping.yml`. So the vocabulary exists and does not need
respelling here; what needs saying is how a Q&A artifact *is* a schema.

A Drescher schema is a context/action/result triple that experience refines. An answer record is
exactly that: the activation is the **context**, the question is the **action**, the answer is the
**result**. Then the learning loop follows for free — repeated success reinforces a schema, and
failure spawns a more specific one:

| Event | Schema consequence |
|---|---|
| Same question, same answer works again | Reinforce. `asked_again` increments; the K-line stays strung |
| Answer was wrong or incomplete for a variant | **Spawn a more specific schema** — a sibling answer with a narrower context, which is Drescher's refinement step verbatim |
| Question never asked again | Candidate for pruning. An unused schema is cost, not knowledge |
| Two answers found to be the same question | Merge, and the merge is a synonym claim — same [collision lint](hyperties/LINK-RESOLUTION.md) as everything else |

And the Society of Mind collocation argument applies directly: residents answering together belong
**in the same call**, not passing serialized messages. Don's image for the alternative is in the
transcript — prisoners in solitary exchanging notes in lipstick on wet napkins, by carrier pigeon —
and an auto-FAQ built as inter-agent messaging would be exactly that, paying per token for the
privilege.

## Why "AUTO-FAQ" is the right name, warning included

Philip K. Dick's *Autofac* (1955): automated factories keep producing after the civilization that
built them is gone, cannot be switched off, and consume the resources they were meant to serve.

That is the failure mode of this design, named in the source material, and it should not be softened.
An auto-FAQ that answers eagerly will manufacture answers to questions nobody asked, forever, and
fill the repository with unread artifacts that are individually plausible and collectively
worthless. The name is a warning label, so the constraints are not optional:

**Answers are produced on demand, never speculatively.** No pre-generating the FAQ. A question with
no asker gets no answer, because the asking is what makes it worth keeping.

**Every artifact carries `asked_again`,** and low counts are pruning candidates on a schedule. The
factory needs an off switch and a garbage collector, which is the one thing Autofac lacked.

**Crystallization is reversible.** `melt` returns an answer to warm status when the underlying
documents move, per the compiler thesis. An artifact that cannot be melted is sediment.

## The inbound half: asking is a pull request

Everything above is about answers. The harder problem is **questions**, and it has a shape that
GitHub already fits, per [the slow-server argument](PLAYABLE-CORPUS.md#github-is-a-slow-server-and-slow-is-the-correct-speed).

The protocol, which is Don's:

**A question is a commit.** You write it, commit it, open a pull request, and thereby stand by it
with your name on it. That single property does most of the moderation work for free — vandalism and
drive-by hostility are much less appealing when the artifact is signed and permanent, and the
maintainer declines rather than deletes.

**Refinement replaces duplication, so the corpus self-dedupes.** If someone already asked your
question badly, you do not file a second one. **You edit theirs and PR the improvement.** Dedup stops
being a janitorial chore performed after the fact and becomes the *native way to participate*, since
the merge is the dedup. Two people converging on one well-put question is a better outcome than two
mediocre questions plus a maintainer's afternoon.

**Curation is open participation without open write.** Anyone may propose; the maintainer merges.
This is the same asymmetry that makes open source work at all, and it is the reason this can be
public without becoming a comment section.

### The me-too is signal, and calling it applause is the design

The standard position is that "+1" is noise. Here it is explicitly welcome, and the reframing is what
makes it work: **a me-too is an expression of interest and appreciation, rendered as applause.**

The trick is that endorsing costs something small and expressive. You do not click a counter — you
say it **in your own words, with your own emoji.** So the endorsement carries voice, which means:

- It is *content*, not a tally. Twenty me-toos in twenty phrasings tell you *why* people want the
  answer, which is information the question itself does not contain.
- It is cheap enough that lurkers participate, and costly enough that it means something.
- It renders as **applause** — an aggregate, warm, non-adversarial signal. A crowd wanting an answer,
  rather than a scoreboard.

```yaml
# questions/for-ted-nelson/whether-transclusion-needs-an-address.yml
question:
  asked_by: <contributor>          # the commit's author; the signature is the standing-by
  refined_by: [<contributor>, ...] # everyone whose PR improved the wording
  question: |
    ...
  applause:
    - by: <contributor>
      words: "This is the one I've wanted answered for fifteen years."
      emoji: ["👏", "🔗"]
```

**And then the emoji histogram.** Aggregate every emoji across every question and compile it at the
top level, as a gift: *this is what the room felt.* It is a [summary genre](SUMMARY-GENRES.md) in the
strict sense — pre-attentively scannable, outliers jumping out, spanning the space rather than
averaging it — and it is the one artifact in this whole design that exists purely to be *appreciated*
rather than used. Which is the right note to end a corpus on.

### Application, and the obligation it creates

Questions are already being collected for Will Wright. The same call goes out for Ted Nelson, with
Don deduping, curating, and organizing **to respect his time** — a curated set of twenty questions is
a gift, and an unfiltered pile of four hundred is a burden dressed as enthusiasm.

One honesty requirement, stated plainly to contributors: **delivery is not guaranteed.** The plan is
to see if the questions can be got to him, through the channel documented in the clearance register.
Collecting questions for a living person creates an obligation, and the obligation is to be
straight about the odds rather than to imply an audience with him.

### Honest costs of the ask protocol

**Applause measures recognizability, not importance.** The most-endorsed question will tend to be the
one most people already understand, which selects against the question only three people are equipped
to ask — usually the best one. The curator's override is the fix, and it has to be *used*, visibly,
or the histogram quietly becomes the editor.

**A pull request is a literacy barrier** — but only if the PR is the *entry point* rather than the
*destination*, which is the fix and it is the next section.

**Emoji can be brigaded**, and an aggregate warm signal is exactly the kind of thing a coordinated
group can flood. Weighting by distinct contributor, and publishing the histogram as a *snapshot with
a date* rather than a live counter, makes it a record instead of a target.

### Harvest inbound: the PR is the destination, not the door

The literacy objection dissolves once you stop treating the pull request as the only way in.
**Questions and applause get harvested from wherever people already are**, and a maintainer or an
LLM converts them into commits. The git artifact is the *archive format*, not the submission form.

| Channel | Question signal | Applause signal |
|---|---|---|
| GitHub issues | the issue body | reactions, plus "+1, and here's why" replies |
| Hacker News threads | comments that end in a question | upvotes, and replies that say *I want to know this too* |
| Twitch chat, live | questions during a stream | emote spam — **already an emoji histogram**, arriving in real time |
| YouTube comments | the long-tail, months later | likes and replies |
| Email, DMs, conference hallways | direct asks | nothing; these need a human to carry them in |

Two things this buys beyond accessibility.

**Live chat is the native case, not the awkward one.** Twitch emote spam is *literally* the design
described above — mass, low-cost, emotionally expressive endorsement, aggregated into a visible
shape. The emoji histogram is not an invention here; it is a thing that already works, being given
a durable form. Which is a good sign for the mechanism and a caution about the metric, since
everything known about chat brigading applies.

**Time-shifting is a feature.** A YouTube comment eight months later arrives in the same queue as a
live chat question, because the queue is a directory in a repository and the repository does not
care when things were said. That is the [slow-server property](PLAYABLE-CORPUS.md#github-is-a-slow-server-and-slow-is-the-correct-speed)
paying off: asynchronous by default, so a channel that is dead as a conversation is still live as an
inbound.

The obligations that come with harvesting, none of which are optional:

- **Attribution with provenance.** Every harvested item records where it came from and under what
  handle. A question lifted from HN and reprinted without a link is theft dressed as curation.
- **A pseudonym is a name.** Harvest handles as given. The pseudonymity rules already in the
  character directories apply to contributors too — no resolving anyone to a legal identity.
- **Harvesting is not endorsement, and neither is it consent.** Someone who asked a question in a
  Twitch chat did not agree to have it printed in a document sent to Ted Nelson. Public-channel
  questions can be *collected*; putting a name on one in a curated artifact wants a light-touch
  opt-out at minimum, and for anything sensitive, an ask.
- **Deduplication across channels is the real work.** The same question arrives four times in four
  registers, which is exactly what the refinement-not-duplication protocol is for — merge them into
  one well-put question and credit all four askers in `refined_by`.

## Honest costs

**A wrong answer persists as confidently as a right one.** This is the serious objection. The
mitigation is that the K-line makes the answer *auditable* — the citations are right there, so a
wrong answer is checkable against its own activation rather than being a floating assertion. That
converts a wrong answer into a lint target, which is the same trick as the
[collision lint](hyperties/LINK-RESOLUTION.md), but it needs the anchors to be real and stable or the
audit is theater.

**Answers in character can be charming and wrong.** A resident with a voice is more persuasive than a
paragraph, and persuasion is not accuracy. The `no-ai-*` ambient skills apply to residents too, and
the church's own doctrine — that abstention is a score — is the relevant precedent: a resident should
be able to say *I don't know, and here is who might.*

**Attribution.** An answer given in the voice of a real person's character is the P-HANDLE-K problem
in a new place ([constitution §8](../../kernel/constitution-core.md)). Residents modeled on living
people must not manufacture opinions and attribute them; the consent tiers already in the character
directories govern this, and an auto-FAQ makes violating them cheap and automatic.

**The index becomes a popularity contest.** If frequently asked questions get the good answers,
rarely asked ones rot, and the corpus optimizes for what is already understood. Worth measuring
rather than assuming away.

## Status

Design. The instantiation half exists — [SUMMON-PROTOCOL.md](../../skills/adventure/SUMMON-PROTOCOL.md)
already handles putting residents in rooms, and the church now has residents and document dispensers
throughout. What is unbuilt is the persistence half: the `answers/` container (a
[plural container](../../kernel/constitution-core.md), typed accordingly), the activation record,
and the reinforce/spawn/prune loop.

↑ [webtop hub](README.md)
