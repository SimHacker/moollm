# Censors on Schemas

## Debugging a mind with Minsky's Memo 603, Drescher's schema mechanism, and a CLI that never calls the LLM

*For students, and for anyone who finds themselves being modeled.*

Engine: [`skills/schema-mechanism/scripts/censor_sim.py`](../skills/schema-mechanism/scripts/censor_sim.py) ·
Manual: [`skills/schema-mechanism/censors/`](../skills/schema-mechanism/censors/README.md) ·
Theory: [schema-mechanism](../skills/schema-mechanism/SKILL.md), [Minsky's jokes memo](../skills/no-ai-joking/MINSKY-JOKES.md), [soul model](../skills/soul-city/SOUL-MODEL.md#minds-all-the-way-down--minsky-to-drescher)

---

## 1. A bug you can't see from inside

You have a toothache. A letter from the dentist arrives. You read it, and it's
bad news. Another one comes. You read that too, and it's worse. The third
letter goes on the pile. So does the fourth. If someone asks, you have a
reason: you'll open it when you have a quiet minute.

You aren't lying. From inside, there was no decision not to read it. There
was just a pile, and a reason. Run it:

```bash
cd skills/schema-mechanism/censors/examples
python3 ../../scripts/censor_sim.py run dentist-letter.yml --run avoidance \
        --layer dentist-letter.answers.yml
```

The simulator keeps two traces. The **inner trace** is what the agent
experiences:

```
t=1: does 'read-letter'
t=3: does 'read-letter'
t=5: does 'put-aside' — "I'll open it when I have a quiet minute." [PI]
t=9: does 'put-aside' — "I'll open it when I have a quiet minute." [PI]
```

The **observer trace** is everything that fired:

```
t=3: marginal attribution mints censor learned-read-letter: context ['letter-from-dentist']  [unconscious]
t=5: censor learned-read-letter vetoes 'read-letter' (predicts knows-bad-news)  [unconscious]
```

The gap between those two traces is what Minsky called the cognitive
unconscious, and the rest of this article is about how to model it, test
it, and fix it.

## 2. Minsky, 1980: the censors

Marvin Minsky's AI Memo 603, *Jokes and the Logic of the Cognitive
Unconscious* ([full text](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/marvin-minsky/sources/papers/AIM-603-jokes-cognitive-unconscious-1980.md)),
patches Freud. Censors don't only suppress forbidden *content*; they
suppress defective *reasoning*. He distinguishes two kinds:

> (i) Stop thinking that!
> (ii) Don't even (or ever) think that!

Type (i) waits for the bad thought and then suppresses it. Type (ii) has to
learn the bad thought's precursors, and then it never has to fire visibly at
all:

> precursor-sensitive censors can do their work before the problems that
> they evade actually arise. Probably, also, they can do this so quickly and
> gently as to produce no noticeable mental phenomenology. This would explain
> why censors are (in the) unconscious.

Then the part that matters most for debugging a person:

> positive general principles need always to be supplemented by negative,
> anecdotal censors. For, it hardly ever pays to alter a general mechanism to
> correct a particular bug.

You don't fix a good rule by throwing it away. You fix it by remembering the
one case where it misfires. A child who grabs his sibling's toy learns not to
grab *that*, "but he must not learn in general not to take things he wants,
lest he become helpless."

And how do censors learn? Minsky's guess:

> Thus "humor" might serve to mediate the process in which the censors
> learn, much as "pleasure" is often supposed to mediate ordinary learning.

Laughter stops the line of thought and holds the absurdity in focus at the
same time, long enough for a censor-learning agency to absorb it.

What the memo never says is *how* a censor gets built. That's where his
student comes in.

## 3. Drescher, 1991: the schema mechanism

Gary Drescher, Minsky's PhD student, wrote *Made-Up Minds*: a
computational version of Piaget, an agent that grows concepts from raw
experience. Its unit is the **schema**:

```
context → action → result      (with a reliability)
```

The agent starts with bare schemas, one per action, and refines them by
**marginal attribution**:

- **Extended results** compare how often each item turns on when the action
  is taken against when it isn't. A real difference spins off a schema with
  that result.
- **Extended context** compares how often the schema succeeds when each item
  is on against when it's off. A real difference spins off a schema with
  that item in its context.
- **Overriding conditions** are items that make an otherwise reliable schema
  fail. They are exceptions to a rule.
- **Synthetic items**: when a schema is unreliable overall but *locally
  consistent* (it works right after it worked, fails right after it failed),
  something hidden is going on. Drescher mints a new item to stand for that
  hidden state.

Read Minsky's memo through Drescher's eyes and the two snap together. A
censor is **a schema with the sign bit flipped**: the same
context/action/result triple, with the result marked harmful and the stored
response *suppress* instead of *do*. Marginal attribution run over your own
pain is the censor-learning rule the memo was missing. And Minsky's
anecdotal censor, the exception that patches a general rule, is Drescher's
overriding condition.

## 4. Henry Minsky's code

At Leela AI, Henry Minsky (Marvin's son) and the team implemented
Drescher's mechanism in Python as `pyleela.brain`, with Drescher advising.
There is a Rust port too, `schema-rs`. That code isn't public, so this
section describes what it does rather than quoting it. It's a far more
serious learner than this simulator, and the comparison is the best way to
see what the simulator simplifies.

| | Henry's `pyleela.brain` | `censor_sim.py` |
|---|---|---|
| Items | thousands, from vision, touch and proprioception in a blocks world and in real video | a few dozen, named by an author |
| Extended results | P(item turns on \| taken) vs \| not taken, as running averages | not modeled; results are authored |
| Extended context | P(success \| item ON) vs \| OFF, running averages, threshold tightens as samples accumulate, checks throttled on a random schedule | P(pain \| ON) − P(pain \| OFF) over the trials so far, fixed threshold |
| Overriding conditions | learned statistically from the context tables | authored, or installed in one shot by a joke |
| Synthetic items | minted from local consistency, named after the host schema; also *negative* synthetic items for reliable schemas that go locally unreliable | not yet |
| Redundant attribution | suppressed once a spun-off child explains it | not needed at this scale |
| Planning | Dijkstra over the schema graph, plans checked by simulation, composite actions per goal item | `plan`: Dijkstra over states, cost 1 − log reliability, run twice, with censors pruning and without; each turn the agent still just picks the best open action |
| Value | primary and refractory activation values per schema | one value table per agent |
| Scale | GPU-batched extended results, schema pruning | 15,000–35,000 whole simulations per second on a laptop |
| Language | core learner predates LLMs; a newer teacher layer grounds words to the schema graph, with a learned associator or an LLM | the engine never calls an LLM (section 7) |

Reading Henry's code taught the simulator two things.

**A censor starts from the schema it inverts.** The first version learned a
censor's context by intersecting everything that happened to be on during
painful trials, so it picked up noise like `calm` and `informed`. Drescher's
tables don't credit an item that never varied, because it carries no
evidence. Now a learned censor starts from the positive schema's own context
and adds only items that actually separate painful trials from painless
ones. The dentist's censor came out as `[letter-from-dentist]`: the read
schema with its sign flipped.

**Censors starve their own evidence.** Henry's code updates a schema's
extended context only when its action is actually taken. A precursor censor
exists to stop an action from being taken. So once it forms, the statistics
that could unlearn it stop arriving. No trials, no counter-evidence. That's
the mechanical reason censors outlive the situations that made them, and the
reason Minsky needs a one-shot channel: an anecdote, a joke, something that
installs the exception without waiting for trials that will never happen.

## 5. Jokes, run

In the dentist scenario's second run, a friend says: "You've got a whole
drawer of unread mail from the guy who could fix your face." The joke does
three things, exactly as the memo says:

1. It **exposes** the censor: `learned-read-letter` becomes visible, and its
   reliability is discounted.
2. It **installs an anecdotal censor**: not "always read your mail" (a new
   general rule) but "not this one, the tooth hurts" (one exception).
3. The visible, discounted censor can now be **overridden**, and the fourth
   letter gets read.

A joke can't do everything. In Andersen's *The Emperor's New Clothes*
([scenario](../skills/schema-mechanism/censors/examples/emperors-new-clothes.yml)),
the child's line exposes the pretense, and the Emperor walks on anyway,
prouder than before. The model reproduces that, and the ablation shows
something sharper: **the Emperor doesn't need a censor at all.** His values
alone (favor and dignity over truth) explain the praise. He isn't repressing
anything; he's calculating. That matches the story, where he thinks quite
consciously, "Am I unfit?" A good model tells you when the unconscious
explanation isn't needed.

## 6. Testing a model of a mind

A model of a mind is a hypothesis, and it should be tested like one. Write
down what the agent actually did (`observed:`), then ask four questions.

**Does it fit?** `test` replays the record and fails unless the model
chooses what the person chose, every time.

**Does it need every part?** `ablate` drops each censor in turn and refits.
A censor the record doesn't need is an invention, and the tool warns about
it. In the fictional beekeepers' story, the `tone` censor from the module
isn't needed, because the story never offers Ruth the chance to hear her
accuser out. The module had it; the record didn't call for it; out it goes.

**Does it depend on numbers I made up?** The value weights are guesses.
`sweep` perturbs every weight by up to ±50% thousands of times and reports
how often the conclusions survive. In the dentist scenario, 30% of plausible
weightings never form a censor at all, because those agents value calm more
than knowing and never read the first letter. That is a finding, not noise:
a censor only forms in someone whose values would otherwise lead them to the
painful thought.

**What would change it?** Counterfactual runs add an event (a joke, a
fact, a sentence from the person's own principles) and show where the mind
goes. They're marked `counterfactual: true`, and nobody's real words are
printed in them except next to actions the person actually took.

## 7. Two tiers: Python for arithmetic, the LLM for meaning

Henry's code, and Drescher's before it, ran into the same wall: grounding.
Items were opaque names. A synthetic item could only be named after the
schema that hosted it, something like `[context/action/result]`. Nothing
could read a letter, notice that a sentence is a rationalization, or say
what a hidden state *means*.

An LLM can do all of that. It is also slow and costly, and you can't trust
it with arithmetic. One run of a seven-event scenario is about 4 KB of
trace, roughly a thousand tokens. A 2,000-perturbation sweep is 4,000 runs,
about four million tokens of generation, or hours of it. Python does the
same sweep in a quarter of a second, and gets the same answer every time.

So split the work the way the [adventure
compiler](../skills/adventure/ADVENTURE-COMPILER.md) does, and the way
[Korz′ deoptimizes to the LLM](korz/korz-prime/deoptimize-to-the-llm.md):
deterministic code runs the crystallized part, and falls back to the LLM
only for what it can't compute. [Speed of light](../skills/speed-of-light/SKILL.md)
puts many turns in one LLM call. This goes further: a sweep runs thousands
of simulations with no LLM call at all.

**The engine never calls an LLM.** It describes what it can't do, and the
loop lives outside it:

- **stdout** carries the data you asked for.
- **stderr** carries one JSON event per line: `REQUEST`, `ERROR`, `WARNING`,
  `INFO`, `RESULT`, `TELEMETRY`.
- Every **request** has an id that is a hash of what's being asked, so the
  same open question has the same id in every invocation, and any number of
  threads can be tracked from outside with `jq`.
- Every request carries a **patch**: the YAML layer that would answer it.

```json
{"id": "req-cover-e48b1c252a", "type": "REQUEST", "kind": "cover",
 "msg": "censor learned-read-letter fired with no cover story",
 "vetoes": "read-letter", "guards": ["knows-bad-news"],
 "ask": "one sentence ... tells itself instead of 'read-letter', unaware of the censor; for a real person, their own words or nothing",
 "patch": {"censors": [{"id": "learned-read-letter", "cover": "<sentence>", "source": "tier0: <who answered>"}]}}
```

The LLM (or a person) reads the request, writes the patch to a file, and
reruns with `--layer answers.yml`. Now that run is deterministic and free,
forever. Generated text is marked `[PI]` everywhere it appears, and a
`source: tier0: ...` says who wrote it.

What goes to the LLM:

| Request | Why Python can't |
|---|---|
| `cover`: what does the agent tell itself? | a rationalization is meaning, not arithmetic |
| `schema`: what does this action do? | needs world knowledge |
| `event`: turn this message into an event | `import` splits a thread deterministically; reading it is the LLM's job |
| (next) name a synthetic item | Drescher's hidden states, named for what they mean instead of where they were found |
| (next) propose censors from a record | hypotheses are cheap to write; `test`, `ablate` and `sweep` are what keep them honest |

The LLM proposes; Python disposes. Every command composes in a pipe:

```bash
S=skills/schema-mechanism/scripts/censor_sim.py
python3 $S import thread.txt > events.yml 2> requests.jsonl     # skeleton + one request per message
# ... the LLM answers requests.jsonl into events.patch.yml ...
python3 $S apply events.patch.yml --into events.yml
python3 $S lint scenario.yml                                    # template words in a real mouth? error
python3 $S test scenario.yml && python3 $S ablate scenario.yml
python3 $S resolve scenario.yml --set agent.values.informed=12 | python3 $S sweep - --n 5000
python3 $S diff alice.yml bob.yml                               # same logic, different priorities?
```

## 8. Personality modules: same logic, different priorities

People who agree on nearly every principle still do different things. The
simulator lets you say that precisely. A scenario inherits **personality
modules**, layered like the [soul model](../skills/soul-city/SOUL-MODEL.md)
layers a character: character, then soul, then minds as organelle
directories that keep their own format.

- [`principled-skeptic.yml`](../skills/schema-mechanism/censors/personalities/principled-skeptic.yml)
  is only logic: what asking for proof, reading, asking the accused, and
  hearing a witness each do. Facts first.
- [`loyalty-censors.yml`](../skills/schema-mechanism/censors/personalities/loyalty-censors.yml)
  adds five censors that keep "my ally said bigoted things" from forming:
  one suppressor that re-files it as politics, and four precursors (too
  long, not my business, I don't trust the people who told me, stop
  lecturing me).
- A person's own layer adds their weights and replaces every template line
  with their own words.

`diff` shows two minds side by side. Two people who both inherit
`principled-skeptic` share every schema. What separates them is a couple of
numbers and which censors each one carries. That's a fairer description of
most disagreements than "one of us is illogical", and it points at exactly
what to talk about.

The modules go all the way down to one censor per file, which makes them a
construction kit: the [**Brainball Construction Kit**](../skills/schema-mechanism/censors/BRAINBALL.md),
sibling to Faceball. Parts are logic, single censors, and drives; archetypes
are named compositions of parts; a person is a list of archetypes plus their
own words. Its worked example is a fictional platform baron and six
followers on one record. It shows something a single mind can't. A friend's
censors only keep a fact out, while a crowd pays for every defense, so a
follower with enough drive to belong needs no censor at all. And a crusader
who doesn't know what he's defending acts exactly like a convert who knows
and agrees.

## 9. Modeling a real person, fairly

This is Pretend Intelligence, a term [Richard Stallman uses for
LLMs](PRETEND-INTELLIGENCE.md): it can produce something that looks like
understanding, without the understanding. A model of someone's censors is
exactly that, and it should say so. The rules the tool enforces:

1. **Their words, your hypotheses, labeled.** `real: [self]` makes `lint`
   fail on any cover that isn't their own sentence with a source; `real:
   [ally]` makes it fail on any event about a real public figure that has
   no source.
2. **No words in their mouth.** Real quotes print only next to actions the
   person actually took. Counterfactuals show the model's choices, not
   invented speech.
3. **Every censor must earn its place.** `ablate` flags the ones the record
   doesn't need.
4. **The numbers are guesses, so test them.** `sweep` shows whether the
   conclusions survive different weights.
5. **Private until they've seen it, and theirs to change.** Under the
   [portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md),
   a model of a living person's mind needs their consent before it's public.
   They can delete a censor, change a weight, add a sentence or a source,
   or delete the whole thing.

The last rule is what makes the rest fair. A model you can edit is an
argument you can answer, in the same terms it was made. If a censor is
wrong, delete it and run `test`: if the record still fits, the censor was
an invention, and the tool will say so. If it doesn't fit, you've learned
something about what the record needs. Either way, the person being modeled
has the last word on the parts that are about them, and the record has the
last word on what they did.

## 10. Exercises

1. **Dentist.** Find the weights where the censor never forms (`sweep`
   finds them; then set them with `--set`). Is that agent healthier, or
   just differently stuck?
2. **A joke with no lesson.** Remove the `lesson:` from the dentist's joke.
   What happens to the fourth letter, and why? Which of Minsky's two
   functions of laughter is left?
3. **Starvation.** Give the dentist agent a statistical overriding-condition
   learner. Show that it can't unlearn the censor without a joke, because
   the vetoed action produces no trials.
4. **Synthetic items.** Port Henry's local-consistency test: when a censor
   is unreliable overall but streaky, mint a hidden item. Have the CLI emit a
   `REQUEST` asking an LLM to name it.
5. **Beekeepers.** Delete one censor at a time and rewrite the story so the
   record still fits. What did you have to make Ruth say?
6. **A public record.** Pick a documented exchange from a public figure.
   Write the events with their words, hypothesize the fewest censors that
   fit, ablate and sweep. Then stop: send it to them before you show
   anyone else.
7. **The Baron's crowd.** Find the smallest change to the record that
   tells the crusader from the convert by behavior alone. What would you
   have to offer them that one takes and the other refuses?
8. **Your own.** Model a decision you regret. Which censor would you need,
   and what is the anecdotal exception that would have fixed it without
   giving up the principle?

## Lineage

Marvin Minsky, AI Memo 603 (1980) and *The Society of Mind* (1986) · Gary
Drescher, *Made-Up Minds* (1991) · Henry Minsky and Leela AI,
`pyleela.brain` and `schema-rs` · Hans Christian Andersen, *The Emperor's
New Clothes* (1837) · Self's tiered JIT and dynamic deoptimization (Ungar,
Chambers, Hölzle), by way of [Korz′](korz/korz-prime/deoptimize-to-the-llm.md)
· the MOOLLM [adventure compiler](../skills/adventure/ADVENTURE-COMPILER.md)'s
events-to-the-LLM pattern.
