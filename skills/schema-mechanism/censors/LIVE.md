# Live events: modeling the news as it happens

A model fitted to a record it has already seen proves little, because it
was built to fit. The test is the next event. This page is the loop for
modeling a public figure while the record is still being written, so each
new event first tests the model, then becomes part of its record.

## The loop

1. **Forecast.** Before anything happens, run `predict` on the kinds of
   event you expect, and write the result into the character's
   `predictions.yml`. Commit and push. The commit date is the
   preregistration: anyone can check the forecast came first.

   ```bash
   S=skills/schema-mechanism/scripts/censor_sim.py
   python3 $S predict on-stage.yml --offers apologize,amplify \
     --set-item accusation-heard=on --set-item power-at-risk=on --n 1000
   ```

   `predict` adds one event after the last one and runs every hypothesis
   in the file over N random weightings (±50%). It reports how often each
   hypothesis picks each action. A forecast is only useful where the
   hypotheses disagree.

2. **Record.** When the event happens, add it to `record.yml` with his
   words verbatim and a source. If it documents a cost to his business or
   access, set `power-at-risk: on` in the stage file. That item is
   observed, not inferred: no source, no cost.

3. **Score.** Add the observed action to the stage file and fill in
   `outcome:` and `scored:` in `predictions.yml`. Don't edit the old
   forecast; it's the evidence. Run `test`, `sweep` and `ablate` again. A
   hypothesis that keeps missing gets demoted in the README; it doesn't get
   quietly reweighted until it fits.

4. **Dispute.** If he, or anyone, says the record is wrong, file it in
   `disputes.yml` next to the record: his words, other readings, what we
   claim, and what evidence would settle it. Corrections with evidence
   change the record. Denials without evidence are recorded, not
   litigated ([portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md#public-power)).

## Learning contexts from the record

Hand-written schemas fit because someone wrote them to fit. `induce` does
what Drescher's extended context does with experience: for every action the
person was offered, it compares how often he took it with each item on and
with it off, and a large gap proposes a schema with that item in its
context. It learns only from items that were set and choices that were
observed, never from the weights.

```bash
python3 $S induce on-stage.yml
#  amplify    power-at-risk  -1.00  on 0/5  off 7/7
#  apologize  power-at-risk  +1.00  on 3/3  off 0/4
```

On the Musk record it finds the cost hypothesis without being told. That
doesn't prove the hypothesis; it shows the record carries it. Three cases
is the minimum (`--min-trials`); fewer, and coincidences propose schemas.

A positive gap is a context: the item makes the action likelier. A negative
gap on an action he otherwise takes is Drescher's overriding condition, an
item that stops a schema that usually works, and that is what a Minsky
censor looks like from outside. `induce --patch` writes each overriding
condition the model lacks as a precursor censor with `learned_from:`
filled in and `cover:` left blank. The cover has to be the person's own
words, with a source, or nothing.

On the Musk record the learned censor ("don't amplify when a cost is
documented") fits all 16 choices in every weighting, with no new value.
The hand-written `power-pays` hypothesis fits the same 16. They differ only
when he has a third move, going quiet, so `predict` with that offer is the
test to commit.

## Fit over time

A total hides change. A hypothesis that fit his first ten choices and
missed his last three is worse than 10/13 says, because people change and
the next choice is closer to the last ones. `drift` weights each hit by
recency (halving every `--half-life` choices back, default 4), shows where
each run's unbroken hits at the end begin, and prints a strip:

```bash
python3 $S drift on-stage.yml
#  power-pays         16/16  1.00    t=1    ################
#  doesnt-know        11/16  0.54    -      #.#######..###..
```

Rank hypotheses by `recent`, not by the total, when forecasting.

## Arguments, simulated first

Drescher's mechanism checks a plan by running it in the model before
acting. `argue` does that for arguments. Each argument is a kind of case,
written as an event (`say`, `set`, a `joke`), and is dropped in just
before the next choice, from a starting situation set with `--set-item`.
For every run it reports how often he takes the goal action, with the same
weightings for every argument, so the rows differ only in the argument.
An argument the runs disagree about is a test of them; one that moves no
run is, in the model, a waste of breath.

```bash
python3 $S argue on-stage.yml --args ../../arguments.yml \
  --offers apologize,amplify --goal apologize \
  --set-item accusation-heard=off --set-item power-at-risk=off
#  argument         doesnt-know  knows-and-agrees  power-pays  learned-censor
#  moral-case            0%           1%              0%            0%
#  documented-cost       0%           0%             71%          100%
```

On the Musk record no argument on the merits moves any run; only a
documented cost does. The arguments are hypothetical kinds, never messages
to send to a real person, and the result is about the model: it says which
situation the record makes him respond to, not what would persuade him.

## Latent items: what the record doesn't show

`induce` can only find items someone recorded. When a choice changes and
nothing recorded changed with it, Drescher's answer is a synthetic item:
if a schema works for a while and then stops, and stays stopped, some
state nobody observes switched in between. `propose` looks for exactly
that. For each action, it finds the one point in time that best splits
the record into "took it" and "didn't", and proposes a latent item there
when that split fits better than any item we observe. Items the choice
itself sets don't count as explanations, since they're its results.

```bash
python3 $S propose examples/quiet-secretary.yml
#  defend-ally  stops between t=4 and t=5: fits 8/8, best observed 4/8 (no item), 1 flip(s)
```

It raises a `latent` request asking what happened in that window. Its
patch adds the item, an event at the midpoint that turns it on, and a
precursor censor gated on it, with `say:`, `cover:` and `source:` blank.
The answer names the item for what it was and cites it, or says nothing is
known, and then the latent item stays a labeled hypothesis. In the
fictional example, the secretary stops defending the treasurer after she
sees a bank statement she never mentions
([answers](examples/quiet-secretary.answers.yml)), and the fit goes from
4/8 to 8/8.

One flip is the local consistency Drescher asks of a synthetic item. A
choice that flips back and forth isn't one hidden switch, so `propose`
reports the number of flips, and `--min-run` (default 2) sets how many
choices each side needs. None of the public-figure records trigger it yet:
each of their changes lines up with an item already recorded, which is
what a short, well-sourced record should look like.

## Jokes

Memo 603 makes jokes training data for censors. A joke either makes a
forbidden connection visible (`exposes:` a censor, which discounts it) or
teaches one (a `lesson:` with no `exposes:` installs a hidden censor in
whoever laughs along). So each joke, his or about him, is filed in
`jokes.yml` with the censor it works on and the audience it worked on. To
test one, drop it into an event as `joke:` and run `ablate`: the record
says whether the joke did anything.

## Arguments

An argument is two minds taking turns on one record. The sim runs one
mind at a time, so the argument is a loop outside it: A's response at
t becomes an event `say:` for B at t+0.1, and so on. Each side's censors
decide what it can hear. The interesting runs are the ones where a move
changes the other side's choice; most moves don't, and the model says why
(a paid defense, a censor the move doesn't expose). Write each exchange
as events so it's a record like any other, sourced where it really
happened and labeled hypothetical where it didn't.

## Worked example

[Elon Musk](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/elon-musk):
applause alone fits 11 of his 16 choices. The five misses are regrets and
retractions, and each followed a documented cost (advertisers in 2023,
Trump's threat to $18 billion in contracts in 2025, a lost midterm in
2026). One latent weight, `power-safe`, fits all 16 in 67% of weightings
(perturbing `power-safe` itself; before 2026-11-24 the sweep left a run's own
weights fixed and said 72%).
Its forecast for the next cost event, committed in `predictions.yml`, is a
regret or retraction; the other hypotheses say he doubles down.
