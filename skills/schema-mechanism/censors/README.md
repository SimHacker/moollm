# Censors — Memo 603 on the schema mechanism, runnable

Minsky's AI Memo 603 says minds keep "censors" that suppress unproductive
mental states. It doesn't say how they're learned. Drescher's schema
mechanism does. The theory is in
[`../../no-ai-joking/MINSKY-JOKES.md`](../../no-ai-joking/MINSKY-JOKES.md)
(skill commentary) and the
[soul model](../../soul-city/SOUL-MODEL.md#minds-all-the-way-down--minsky-to-drescher).
This directory runs it: [`../scripts/censor_sim.py`](../scripts/censor_sim.py).

```bash
python3 ../scripts/censor_sim.py examples/dentist-letter.yml --markdown
python3 ../scripts/censor_sim.py SCENARIO.yml --ablate
```

## What it implements

| Memo 603 / Made-Up Minds | In the simulator |
|---|---|
| Schema: context → action → result | `schemas:`; the agent picks the open action with the best predicted value |
| Censor = schema with the sign bit flipped | `censors:` with `harm:`; response is veto, not do |
| Precursor censor: works "before the problems that they evade actually arise" | `kind: precursor` vetoes an action before it runs |
| "no noticeable mental phenomenology" | the veto goes only to the OBSERVER trace; the agent sees its `cover:` sentence as its reason |
| Suppressor: disrupts a state after it forms | `kind: suppressor` re-files a forbidden state (`refile:`); frame substitution |
| Marginal attribution | after a painful result, count what was ON; when it repeats, mint a precursor censor on that context |
| "humor might serve to mediate the process in which the censors learn" | `joke:` makes a censor visible, discounts it, and can install a `lesson:` |
| "positive general principles need always to be supplemented by negative, anecdotal censors" | a `lesson:` is an anecdotal censor; it outranks the general censors it patches |

A censor the agent can see and no longer trusts (below 0.6 reliability) can
be overridden. A censor whose harms have already happened stops firing.

## Fitting a real record

Events can say what a real agent actually did (`observed:`) and quote them
(`response:`). The report scores the fit. `--ablate` removes each
hypothesized censor in turn: one the fit doesn't need is an invention the
data doesn't support. A real quote prints only when the model's action
matches what the person actually did, so a counterfactual run can't put
words in anyone's mouth. Mark those runs `counterfactual: true`.

That's the honesty rule for modeling people: the quotes are theirs, the
censors are yours, and you label which is which. Under the
[portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md),
a model of a living person's mind needs their consent before it's public.

## Examples

| File | What it shows |
|---|---|
| [`examples/dentist-letter.yml`](examples/dentist-letter.yml) ([output](examples/dentist-letter.RUN.md)) | A censor learned by marginal attribution, invisible from inside; a friend's joke exposes it and leaves an anecdotal exception |
