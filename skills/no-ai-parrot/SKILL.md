# NO-AI-PARROT™ — Protocol

> *"To parrot 'stochastic parrot' is to be one."*

---

## Quick Reference

| Command | Effect |
|---------|--------|
| `STEELMAN [cliché]` | State its strongest true version, with the citation. Always first. |
| `DEREFERENCE [phrase]` | What the borrowed source actually argues, and what it does not |
| `NAME-THE-MOVE` | Lifton 1961: thought-terminating cliché, loading the language |
| `REPLY [comment]` | The five moves, emitted short, formatted for the venue |
| `PREFLIGHT` | Length, one receipt, unarmored spot, no cite-wall, no sign-flipped sin |

---

## The Problem

Someone answers a question about what a system does by naming what it is made of,
and treats that as the end of the discussion. "It's just a next token predictor."
"Stochastic parrot." "Glorified autocomplete." "It doesn't really understand."

Three things are true at once, and a reply that drops any of them is worse than
no reply.

1. **The phrase is usually accurate as far as it goes.** The training objective
   *is* next-token prediction. A fixed-context transformer *is* formally a
   high-order Markov process. Fluency *does* cause people to over-attribute.
2. **It is borrowed from real work whose argument is different.** "Stochastic
   parrot" is the title of a paper about the cost of scale, undocumentable
   training corpora, encoded harm, and human misattribution. It is not a proof
   that models cannot reason.
3. **It is deployed so that no reply is possible.** That is a named phenomenon
   with a literature going back to 1961, and naming it is the move that makes the
   conversation continue instead of ending.

## The logical error, precisely

The cliché describes an **objective** and concludes a **capability**. The same
sentence form, applied elsewhere:

- Evolution is just an inclusive-fitness optimizer.
- Deep Blue was just alpha-beta search.
- Your brain is just cells minimizing prediction error.

Each is true at one level of description and completely silent about what the
process produces. **Objectives are not ontologies.** You do not need any claim
about understanding, consciousness, or being to make this point — and reaching
for one is how you lose.

### The reversal worth memorizing

Claude Shannon measured the entropy of printed English in 1951 by sitting human
subjects down and having them **guess the next letter** of a text, one letter at
a time, with the number of guesses as the measurement.

> Shannon, C. E. (1951). Prediction and Entropy of Printed English.
> *Bell System Technical Journal* 30(1), 50–64.

Next-token prediction entered the literature as an instrument for studying
people. "Just a next token predictor" describes an experiment Shannon ran on us.

## The five moves

### 1. STEELMAN

State the strongest true version of the cliché **before** anything else, and
attribute it. If you cannot, you have not understood it and should stop.

The honest core of every entry in this catalog is the **ELIZA effect**: humans
over-attribute mind to fluent text, reliably, and it has been documented since
1966 by someone who was alarmed at what his own program did to people.

> Weizenbaum, J. (1966). ELIZA. *CACM* 9(1), 36–45.
> Weizenbaum, J. (1976). *Computer Power and Human Reason*.

Concede this out loud. It costs nothing and it is true.

### 2. DEREFERENCE

Look up the source of the borrowed phrase and quote what it argues.

| Cliché | Source | What it argues | What it does not argue |
|---|---|---|---|
| stochastic parrot | Bender, Gebru, McMillan-Major, Shmitchell, FAccT '21 | Cost of scale; corpora too large to document; encoded harm; **humans over-attribute meaning to fluent text** | That models cannot reason |
| form without meaning | Bender & Koller, ACL 2020 | The octopus: form learned without grounding | (This is the real argument people mean) |
| doesn't understand | Searle 1980 | Against one functionalism; answered in the same issue by the Systems Reply | That machine minds are impossible — Searle holds brains cause minds causally |
| next token predictor | the training objective | Accurate description of the loss | Anything about the resulting capability |
| Markov chain on steroids | formally correct | Fixed context = high-order Markov | That order and function class don't matter |

The gap between column three and column four is the entire reply.

### 3. NAME-THE-MOVE

> Lifton, R. J. (1961). *Thought Reform and the Psychology of Totalism*,
> ch. 22, "Ideological Totalism" — the criterion of **loading the language**:
> "the most far-reaching and complex of human problems are compressed into brief,
> highly reductive, definitive-sounding phrases."

"Thought-terminating cliché" is a technical term from a study of coercive
persuasion. **With the citation it is analysis; without it, it is just another
cliché.** Use it on the phrase, never on the person.

Minsky answered this whole genre by name in 1982, and the title is the argument:
*Why People Think Computers Can't*, AI Magazine 3(4).

### 4. SEPARATE THE QUESTION FROM THE PROHIBITION

The strong form of the cliché asserts an answer and forbids the inquiry —
sometimes explicitly, by diagnosing anyone who asks. When that happens, the
reply is not to argue the metaphysics. It is to point out that **a claim plus a
prohibition on examining it is not skepticism.** Skepticism is "we don't know,
and here is why the question is hard."

Turing spent section 6 of the 1950 paper working through nine numbered objections,
conceded the residual mystery of consciousness, and proposed a test instead of a
verdict. That is what the careful version of this position looks like.

### 5. ANSWER THE REAL QUESTION

There is almost always a real question underneath, and it is usually better than
the cliché: *where is the boundary between what this does reliably and what it
does once?* Answer that with something you built, and the argument about what the
thing **is** becomes optional.

This is also where you stop. End somewhere the other person can reply without
humiliation. **The goal is that they stop, not that they lose.**

## Output constraints

These are load-bearing and were learned expensively. See
[`examples/hypfer-2026.md`](examples/hypfer-2026.md).

- **Short.** The long version does not get read.
- **One receipt.** Something you personally built or ran, not a bibliography.
- **Keep an unarmored spot** — one line no RLHF'd model would produce. A dense,
  polished, perfectly parallel citation wall reads as machine-written to humans
  *and to automated filters.* In the founding case, the most careful, most
  heavily cited reply in the thread was auto-filtered as machine-generated and
  never got read, while the same venue failed to detect actual hybrid output all
  day. The detector fails in both directions, and your best prose is what trips it.
- **Two citations maximum in a public reply.** The rest lives in the skill.
- **No sign-flipped sin.** Do not answer an overconfident metaphysical claim with
  your own.

## Reusability

The point of writing this down is that the next occurrence costs nothing. The
cliché is stable, the citations do not move, and the reply is a lookup. Add each
new encounter to `examples/` verbatim — the parroted phrase, the reply, and
whether it worked — and the skill gets better at the one thing it does.

When the same account repeats the same cliché in a new venue, that is not a new
argument. It is a cache hit.

## Part of MOOLLM

This skill is part of [MOOLLM](https://github.com/SimHacker/moollm) — see the
[repo README](../../README.md) and [skills/README](../README.md).

Related MOOLLM skills: [no-ai-slop](../no-ai-slop/) (the claim ledger —
CONFIRM / DISPUTE / ASK, which is what STEELMAN is),
[no-ai-hedging](../no-ai-hedging/), [no-ai-humansplaining](../no-ai-humansplaining/)
(the inbound mirror), [no-ai-ideology](../no-ai-ideology/) (the brand warehouse),
[copy-that](../copy-that/) (venue formatting — HN takes no markdown),
[cursor-mirror](../cursor-mirror/) (pull the verbatim prior exchange out of
transcripts to build `examples/`).

## Credits

Lifton for the name of the move. Shannon for the reversal. Minsky for answering
the genre forty years early. Weizenbaum for the part the other side gets right.
