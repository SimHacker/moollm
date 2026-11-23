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
2026). One latent weight, `power-safe`, fits all 16 in 72% of weightings.
Its forecast for the next cost event, committed in `predictions.yml`, is a
regret or retraction; the other hypotheses say he doubles down.
