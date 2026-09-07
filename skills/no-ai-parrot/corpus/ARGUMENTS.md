# ARGUMENTS — positions, stated as positions

**Different contract from every other file in this corpus.** The others hold
text: quotations with authors, dates and resolving links, safe to paste because
a reader can click and check. This file holds **no quotable prose at all.** It
holds positions, compressed to the point where they cannot be pasted, so that
re-using one requires arguing it again in the human's own words.

That is the point. A position you have to re-state is a position you still
hold; a paragraph you paste is a paragraph you have outsourced. See
[`../CONSTITUTION.md`](../CONSTITUTION.md) Article I.

Nothing here is attributed to anyone but the skill's author, and nothing here
is a reaction to any particular thread.

---

## Against the training-objective reduction

The family of moves is "it is *just* X," where X is the training objective.
These five positions answer it, in the order they usually need to be made.

**1. An objective is not an ontology.** What a system was trained to optimize
does not tell you what it turned out to be. This is the whole argument in one
line and everything else is support for it.

**2. Compression is the mechanism, and it is the step the cliché skips.**
Prediction under a size constraint forces structure: to predict well you have to
model what generates the thing, not the thing. This is the load-bearing claim,
because it explains *why* capability appears without needing anyone to have
intended it. Whoever says "just predicting the next token" has described the
objective and omitted the mechanism by which the objective bites.

**3. The reduction is available for any system, which is what shows it proves
nothing.** A brain is "just" ion channels minimizing prediction error. Evolution
is "just" an inclusive-fitness optimizer. Both are true at one level of
description and both are silent about what the process produces. The move is not
wrong; it is **empty**, and it is empty in a way the objector can verify on
themselves in one step.

**4. Dismissal is not skepticism.** Skepticism says *we do not know, and here is
why the question is hard.* A verdict plus a prohibition on examining it is the
opposite of skepticism wearing its clothes. Turing's section 6 is what the
careful version of the same objection looks like, which is why
[`CANON.md`](CANON.md) carries it.

**5. Deep Blue is the clean case.** It was "just" alpha-beta search. Everyone
agrees the reduction is true and everyone agrees it settles nothing about
whether the thing plays chess. Reach for it when the abstract version stalls,
because it costs the other person nothing to grant and it grants the whole
structure of the argument.

---

## On "answer-shaped string"

The sharpest phrasing in the family (see [`PHRASES.md`](PHRASES.md)) and it
deserves a better answer than the others, because unlike them it makes a
**testable claim about the shape of the output** rather than a metaphysical
claim about the producer.

The question it does not answer: **shaped by what path?**

"Extrapolates the statistically most likely answer-shaped string" is a
description of the *output format*. It is silent about everything that happened
between the question and the string, and that interval is where the entire
disagreement lives. The interval can contain:

- **Computation actually performed** — arithmetic done, a program written and
  run, a file read, a search executed, a test failing and the failure changing
  what happens next.
- **Logical analysis** — a case split made and both branches followed, a
  counterexample constructed, a claim checked against a source instead of
  against a prior.
- **General-purpose problem-solving skills, composed** — in both senses of the
  word: the industry's sense of a named, loadable capability, and the ordinary
  sense of knowing how to attack a problem. Applied, composed with each other,
  and iterated.
- **Iteration against feedback** — the loop where the artifact is run, the
  errors are read, and the next pass is different because of what the last pass
  returned.

Every one of those is a step whose *result was not known in advance*, and a
string produced after them is not "extrapolated" in any sense that does work for
the person using the word. **The string may be answer-shaped because it is an
answer.**

### Why this is the same observation as "predicting the next token is doing a lot of work"

The two are one argument. Emergent capability is not a side effect that happens
to accompany prediction; **it is an excellent technique for predicting
accurately**, which is why the objective produces it. Modeling the process that
generated the text is how you predict the text. So "it is only trying to predict
tokens" and "it is doing analysis" are not competing descriptions — the second
is how the first gets done well.

### The evidential form, which is the strong one

Do not argue about what is happening inside. **Look at the path, because the
path is inspectable**, and the person on the other side is usually already
inspecting paths in their own work. Then either:

- the path is indistinguishable from what a human would have done, in which case
  the shape objection has no purchase; or
- the path is **distinguishable because it is better** — more cases checked,
  more sources verified, the arithmetic actually run rather than estimated — in
  which case the objection has landed on the wrong side of its own test.

`kind: argument · reuse: re-argue, never paste`

### What this does not claim, stated before someone says it

It does not claim the model understands, is conscious, or is a being — see
Article VII. It also does not claim every use looks like this: a single
unexamined completion with no computation, no checking and no iteration **is**
an answer-shaped string, and conceding that outright is what makes the
distinction worth anything. The claim is narrow and it is about *paths*, not
about minds.

---

## Filing note

Positions get lost faster than quotations, because a quotation has a link
holding it in place and a position only has whoever remembers making it. When a
position is re-argued well in public, the new version earns a permalink and
moves to [`CORRECTIONS.md`](CORRECTIONS.md), which is the file that can be
pasted from.
