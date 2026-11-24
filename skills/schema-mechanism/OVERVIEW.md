# A Pretend Intelligence you can read

## Minsky's censors on Drescher's schemas: what this is, where it comes from, and what it doesn't do

*An overview for readers who distrust "AI" and want to see the mechanism.
The full design is in [`designs/SCHEMA-ENGINE.md`](../../designs/SCHEMA-ENGINE.md);
a tutorial with worked examples is
[`designs/CENSORS-ON-SCHEMAS.md`](../../designs/CENSORS-ON-SCHEMAS.md).*

---

## In one paragraph

`censor_sim.py` is a small program, about 1,500 lines of Python, that runs
a made-up mind. The mind is a list of named facts that are on, off or
unknown, a table saying how much it likes or dislikes each one, and a list
of rules of the form *in this situation, doing this tends to cause that*.
At each step it does whatever its rules say will turn out best, unless a
*censor* forbids the step. Censors are learned from bad outcomes, and the
mind doesn't see them: it only sees the excuse it tells itself. You give
the program a record of what a real or fictional agent actually did, and it
tells you whether the made-up mind reproduces that record, which of its
parts the record actually needs, and how much the answer depends on numbers
somebody guessed. It never calls a language model and it doesn't understand
anything. It counts.

## The term: Pretend Intelligence

Richard Stallman proposed the term **Pretend Intelligence (PI)** for what
the industry markets as "AI", in a talk at Georgia Tech on 23 January 2026
([video](https://youtu.be/YDxPJs1EPS4?t=641); the full essay on the term is
[`designs/PRETEND-INTELLIGENCE.md`](../../designs/PRETEND-INTELLIGENCE.md)).
His test is short:

> "Intelligence is the capacity to know and understand at least within some
> domains."

> "If a system can really understand statements in some domain, maybe it's
> real artificial intelligence within that domain. But if it can't, then
> it's pretend intelligence."

The term is his. This program uses it in two senses, and keeps them apart.

**The language model is PI, and is treated as PI.** Where the program
needs words it can't compute (what an action does, what a hidden state
should be called, what excuse a person gives themselves), it doesn't call
a language model. It prints a request, with the exact patch that would
answer it, and stops. A person, or a language model in a chat window, may
fill the patch in. Every generated line is then marked `[PI]` in the
output and carries a note saying who wrote it, and it is a hypothesis
until the record supports it. The arithmetic never goes to the model: it
is slow at it and gets it wrong.

**The mind itself is a pretend mind, on purpose.** It is a simulation,
like a Sim or a SimCity: a mechanism small enough to read, that pretends
to have motives so you can see what follows from them. It makes no claim
to know or understand. Its claim is narrower and checkable: *given what
this agent did, here is the smallest mechanism we found that does the
same, here are the parts nothing needed, and here is how fragile the
answer is.* Gary Drescher's title for the theory it runs is *Made-Up
Minds*. That is exactly what this is, and it says so on every page of
output.

## Where it comes from: the MIT AI Lab

**Marvin Minsky, AI Memo 603, "Jokes and the Logic of the Cognitive
Unconscious" (1980).** Minsky argued that the mind has *censors* that
suppress not forbidden wishes, as Freud had it, but faulty reasoning. He
distinguished two kinds: ones that say "stop thinking that", and ones that
learn a bad thought's precursors and say "don't even think that", so
quietly that you never notice them. He added that a good general rule
should be patched with specific exceptions, "for, it hardly ever pays to
alter a general mechanism to correct a particular bug", and that humor is
how censors are trained: a joke holds an absurdity in view long enough for
the mind to learn from it. The memo never said how a censor gets built.
([full text](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/marvin-minsky/sources/papers/AIM-603-jokes-cognitive-unconscious-1980.md))

**Gary Drescher, *Made-Up Minds* (MIT Press, 1991).** Drescher's MIT
doctoral work, with Minsky and Seymour Papert, turned Jean Piaget's account
of how infants learn into an algorithm. Its unit is the *schema*: context,
action, result, with a reliability. The agent starts with none and finds
them by *marginal attribution*: noticing which facts make an action's
result likelier, and which ones make a reliable action fail. Drescher's
*overriding conditions*, facts that make a reliable action fail, are
Minsky's specific exceptions, found by counting. His *synthetic items*,
states the agent can't see but must posit to explain itself, are how it
invents concepts.

**The join.** Read the memo with Drescher's mechanism and they fit: a
censor is a schema with the sign flipped. Same context, same action, the
result marked harmful, and the response *don't* instead of *do*. Marginal
attribution over your own bad outcomes is the missing rule for how a
censor is learned. This program is that join, run.

The same lab gave the field ELIZA and DOCTOR, and Joseph Weizenbaum's
warning that people would trust a program that only seemed to understand.
DOCTOR has lived in GNU Emacs for forty years. The lesson carried here is
his: make the mechanism visible, so nobody has to trust the appearance.

## Where it comes from: games, and Leela AI

**The Sims and SimCity.** Don Hopkins worked on The Sims at Maxis. The
Sims' people choose what to do with an algorithm called Find Best Action
(Jamie Doornbos, 1997): every object *advertises* how much each of its
actions would raise each of a Sim's motives, and the Sim picks the best
offer, scored by how much it would actually change. This program's
`decide` is the same loop: schemas are the advertisements, the value table
is the motives, and a censor is an advertisement the Sim can't see. Will
Wright's games taught a whole generation that a simulation is an argument
you can play with, and that the model is supposed to be small enough for
the player to build in their head. Don also persuaded Electronic Arts to
release SimCity's source under the GPL, as Micropolis, for the One Laptop
per Child project, so children could read the model, not just play it.

**MOOLLM.** The program lives in [MOOLLM](https://github.com/SimHacker/moollm),
Don's free-software framework for building simulations and characters out
of plain files. It follows MOOLLM's rule for language models: deterministic
code does everything it can, and falls back to a model only for what it
can't compute, through files a person can read and edit.

**Leela AI.** Henry Minsky, Marvin's son, co-founded Leela AI and, with
Drescher advising, implemented the schema mechanism as a working learner
over real video. Don works there. Henry's code is far more serious than
this program, and isn't public; this program is a small, separate, public
re-telling of the same idea, aimed at reading people's choices instead of
watching a factory floor.

## How it works, in five steps

The fictional example everyone recognizes: a letter from the dentist.

1. **Describe the agent.** Facts (`letter-from-dentist`, `knows-bad-news`,
   `informed`), what it values (knowing +5, bad news −3), and two schemas:
   reading the letter makes you informed and gives you bad news; putting it
   aside keeps you calm.

2. **Give it the record.** Letters arrive at times 1, 3, 5 and 9. The
   record says what it did.

3. **Run it.** It reads the first two letters. Both times the news is bad.
   Marginal attribution notices, and mints a censor against reading
   letters from the dentist. From then on the agent puts letters aside,
   and the program prints two traces: what the agent experiences, and
   what an observer sees.

   ```
   INNER (what it experiences):
     t=5: does 'put-aside' — "I'll open it when I have a quiet minute." [PI]
   OBSERVER (everything that fired):
     t=3: marginal attribution mints censor learned-read-letter  [unconscious]
     t=5: censor learned-read-letter vetoes 'read-letter'        [unconscious]
   ```

   The difference between the two traces is what Minsky called the
   cognitive unconscious. The excuse is marked `[PI]` because a language
   model drafted it; for a real person, the only allowed excuse is their
   own sentence, with a source.

4. **Plan.** Ask for a way to an appointment. The agent can't find one.
   The observer can: read the letter, then book. The planner names the
   censor that hid the first step.

   ```
   agent sees:    none found
   observer sees: read-letter → book-appointment
   hidden: 'read-letter' is vetoed by censor learned-read-letter
   ```

   A friend's joke ("a whole drawer of unread mail from the guy who could
   fix your face") exposes the censor, and the plan comes back.

5. **Test it.** `test` fails unless the model reproduces the record.
   `ablate` removes each censor in turn and reports the ones the record
   doesn't need. `sweep` re-runs everything with every guessed weight
   moved up to 50% either way, a few thousand times, and reports how
   often the conclusion survives. For the dentist, about 30% of plausible
   weightings never form the censor at all, because those agents value
   calm more than knowing and never read the first letter. That's a
   finding, not noise: a censor forms only in a mind that would otherwise
   go where it hurts.

## What it doesn't do

- **It doesn't understand.** Facts are names. The program doesn't know
  what a dentist is. Meaning lives in the names, the comments, and the
  reader.
- **It doesn't read minds.** A model that fits a record is one account of
  it. When two accounts fit the same record, the program says so, and
  says what evidence would separate them. It never reports intent the
  record doesn't show.
- **It doesn't learn the way Drescher's full mechanism does.** It learns
  censors from bad outcomes, and finds hidden states and overriding
  conditions in a record, but its positive schemas are written by hand.
- **It doesn't call out.** No network, no model, no telemetry. Same input
  and seed, same output, on any machine.
- **It doesn't put words in anyone's mouth.** For a real person, the lint
  step fails on any excuse that isn't their own sentence with a source,
  and real quotes print only next to things they actually did. A model of
  a living person stays private until they've seen it, and they can
  change or delete any part of it.

## Freedom

The program and its examples are free software under the MIT (Expat)
license. It needs Python 3 and PyYAML, nothing else. Every model is a
plain YAML text file you can read, diff, and change; every result can be
regenerated from those files; and the tests that check the engine ship
with it. If a part of a model is wrong, delete it and run `test`: if the
record still fits, the part was a guess, and the program will say so.

## Try it

```bash
cd skills/schema-mechanism/censors/examples
S=../../scripts/censor_sim.py
python3 $S run dentist-letter.yml --layer dentist-letter.answers.yml
python3 $S plan dentist-letter.yml --run avoidance --goal appointment
python3 $S ablate emperors-new-clothes.yml     # the Emperor needs no censor at all
python3 $S sweep dentist-letter.yml --n 2000
python3 ../../scripts/test_censor_sim.py       # the engine's own tests
```

## Read more

- [`designs/SCHEMA-ENGINE.md`](../../designs/SCHEMA-ENGINE.md): the full design, every rule, every command, the known limits
- [`designs/CENSORS-ON-SCHEMAS.md`](../../designs/CENSORS-ON-SCHEMAS.md): the tutorial, with exercises
- [`designs/PRETEND-INTELLIGENCE.md`](../../designs/PRETEND-INTELLIGENCE.md): Stallman's term and the argument around it
- [`censors/`](censors/README.md): the manual, the construction kit, the examples
- [`designs/sims/sims-find-best-action.md`](../../designs/sims/sims-find-best-action.md): The Sims' decision loop
