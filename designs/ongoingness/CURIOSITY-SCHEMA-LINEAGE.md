# Curiosity, Schemas, and the Lineage: Piaget → Papert → Minsky → Drescher → Leela AI

## The correction

"You don't program curiosity" is too glib. Programming curiosity is exactly
what Gary Drescher attempted in his PhD thesis with Minsky and in *Made-Up
Minds* (1991) — operationalizing Piaget's and Papert's developmental
philosophy. Not as:

```python
curiosity = True
```

> When ChatGPT originally rendered that Python fragment as a markdown block,
> it had a "Run" button on it — and pressing it would dramatically prove how
> futile `curiosity = True` was by actually running it in a Python
> interpreter. I see beauty in that inadvertently self-aware improvisational
> executable performance art! — Don

Not as a flag, but as a cognitive architecture where curiosity **emerges as
the optimal strategy**:

```
a schema predicts
→ prediction fails
→ the failure becomes interesting
→ the system invents experiments
→ it learns new schemas
```

Very Piagetian: equilibration through accommodation and assimilation.
Curiosity is not a module; it is the consequence of machinery that notices the
difference between expectation and reality and can reduce it.

## What the wall was, and what LLMs changed

Leela AI (Henry Minsky, CTO; Drescher advising) implemented schema mechanisms
in Lisp and Python. The wall was **grounding**: symbols were easy to
manipulate, impossible to connect to the enormous irregular background
knowledge humans acquire through culture. Implementing Drescher's program from
scratch in 1991 meant building an infant's entire cognitive development
yourself.

An LLM changes the economics. It arrives with billions of grounded statistical
associations — "cup," "gravity," "embarrassment," "joke," "door" are no longer
empty Lisp atoms. Schemas no longer bootstrap *meaning* from nothing; they
bootstrap *competence*.

## Three kinds of grounding (keep them distinct)

| Kind | What it is | Who provides it |
|------|-----------|-----------------|
| Relational | a word situated among words and concepts in learned representation | LLM, imperfectly |
| Social | records of how humans use, respond to, negotiate the concept | LLM, imperfectly |
| Operational | concepts bound to persistent objects, actions, observations, consequences | **microworlds** — MOOLLM's job |

A room, stove, promise, debt, or joke becomes operationally grounded when it
has stable identity, state, affordances, consequences, and history — not
merely a textual description. Common sense from the LLM is **a prior, not an
oracle**: it proposes plausible schema structure; the world corrects it.

## Three versions of one computational pattern

> Drescher's schemas point to other schemas. Minsky's k-lines reactivate
> collections of agents. Transformer attention points to other latent
> representations.

Same pattern, forty years, three substrates: the 1980s version was symbolic,
the 1990s version was developmental, the 2020s version is differentiable. They
don't replace one another — they finally fit together. The LLM supplies the
representational substrate the symbolic architectures lacked; Society of Mind
and schemas supply the organization and persistence the LLMs lack.

## The schema mechanism, operationally

A schema: `context → action → expected result`, accumulating evidence about
applicability, prediction reliability, intervening conditions, sub-actions,
and generalizing abstractions.

The developmental loop:

```
observe → predict → act → compare expectation with result
→ assign surprise and credit → refine or construct schemas
→ select the next informative action
```

Curiosity as a **policy for choosing experiments**, balancing: expected
information gain, goal relevance, reducible uncertainty, availability of a
testing action, cost and reversibility, safety and permissions, transfer
potential. Penalize novelty without learning, endless self-stimulation, and
unsafe exploration. This distinguishes curiosity from a background monologue.

## Advertisements close the loop

The Sims advertisement mechanism (Will Wright, Jamie Doornbos) supplies
candidate affordances: object advertises action + conditions + expected
benefits + costs + suitability for this actor. Schemas predict what those
actions will do; agencies weigh competing goals; curiosity raises the value of
actions that resolve useful uncertainty.

The integrated decision loop:

```
world event → activate k-lines → assemble agency coalition
→ discover and score advertisements → apply schemas to predict outcomes
→ choose and act → observe → compare prediction with reality
→ update schemas and memories → preserve or lift reusable knowledge
```

That is the operational synthesis of Minsky, Drescher, The Sims, LLMs, and
MOOLLM in one loop.

## Humor as a cognitive probe

Minsky's "Jokes and the Cognitive Unconscious": a joke works because one
cognitive frame is suddenly replaced by another that better explains the same
situation; the laugh is rapid reorganization. That is schema repair and frame
switching — remarkably close to how competing continuations resolve inside an
LLM.

A MOOLLM humor mechanism is therefore a **diagnostic agency**, not a joke
generator: it detects hidden assumptions, incompatible frames, ambiguity,
violated expectations, and compression through analogy. Socially it signals
shared context and softens correction — accountable to representation ethics,
never a license for cruelty. See `frame-shift` in
[SKILL-ROADMAP.md](SKILL-ROADMAP.md).
