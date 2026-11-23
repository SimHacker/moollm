# Censors: Memo 603 on the schema mechanism, runnable

Minsky's AI Memo 603 says minds keep "censors" that suppress unproductive
mental states. It doesn't say how they're learned. Drescher's schema
mechanism does. The theory is in
[`../../no-ai-joking/MINSKY-JOKES.md`](../../no-ai-joking/MINSKY-JOKES.md)
and the [soul model](../../soul-city/SOUL-MODEL.md#minds-all-the-way-down--minsky-to-drescher).
The long explanation, for students and for anyone being modeled, is
[`designs/CENSORS-ON-SCHEMAS.md`](../../../designs/CENSORS-ON-SCHEMAS.md).
This directory runs it: [`../scripts/censor_sim.py`](../scripts/censor_sim.py).

## What it implements

| Memo 603 / *Made-Up Minds* | In the simulator |
|---|---|
| Schema: context → action → result | `schemas:`; the agent picks the open action with the best predicted value |
| Censor = schema with the sign bit flipped | `censors:` with `harm:`; response is veto, not do |
| Type (ii), "Don't even think that!": precursor censors work "before the problems that they evade actually arise" | `kind: precursor` vetoes an action before it runs |
| "no noticeable mental phenomenology" | the veto goes only to the OBSERVER trace; the agent sees its `cover:` sentence as its reason |
| Type (i), "Stop thinking that!": suppressor | `kind: suppressor` re-files a forbidden state (`refile:`), frame substitution |
| B-brain watching A-brain | the observer trace |
| Marginal attribution (extended context) | after repeated pain, mint a precursor on the positive schema's context plus every item where P(pain \| ON) − P(pain \| OFF) ≥ 0.5 |
| "humor might serve to mediate the process in which the censors learn" | `joke:` makes a censor visible, discounts it, and can install a `lesson:` |
| "positive general principles need always to be supplemented by negative, anecdotal censors" | a `lesson:` is an anecdotal censor; it outranks the general censors it patches |

A censor the agent can see and no longer trusts (below 0.6 reliability) can
be overridden. A censor whose harms have already happened stops firing. A
precursor censor that vetoes an action also stops that action's trials, so
it starves its own evidence. That's why statistics alone rarely unlearn one,
and why a one-shot channel (a joke, an anecdote) matters.

## The CLI: the engine never calls an LLM

Same shape as the [adventure compiler](../../adventure/README.md): the tool
describes what it found and what it can't compute; whoever has the context
answers. The loop lives outside the tool.

| Stream | Carries |
|---|---|
| stdout | the data you asked for: `--format text\|md\|yaml\|json` (`dot` for `export`) |
| stderr | one JSON event per line: `REQUEST`, `ERROR`, `WARNING`, `INFO`, `RESULT`, `TELEMETRY` |
| exit | 0 ok · 1 errors · 2 test failed · 3 requests open (`--strict`) |

Request ids are hashes of what's being asked, so the same open question has
the same id in every invocation. Each request carries a `patch`: the YAML
layer that would answer it. Write the patch to a file, fill it in, and pass
it back with `--layer`, or merge it into a file with `apply`.

| Command | |
|---|---|
| `resolve FILE...` | merge files and layers; print the result |
| `lint FILE` | unknown items, unoffered actions, template words in a real person's mouth |
| `run FILE [--run NAME]` | inner and observer traces |
| `test FILE` | exit 2 unless each factual run fits its record and its `expect:` block |
| `ablate FILE` | drop each censor; warn about the ones the record doesn't need |
| `sweep FILE --n N` | perturb value weights ±50%: do the conclusions depend on the numbers? |
| `bench FILE --n N` | simulations per second |
| `diff A B` | shared logic, different priorities, which censors each mind has |
| `where FILE PATTERN` | which layer defines what matches |
| `export FILE [--format dot]` | resolved model, or a censor graph for Graphviz |
| `import TEXT` | split a message thread into skeleton events, one request per message |
| `apply PATCH --into FILE` | merge a patch layer into a file |

Every command takes `--layer FILE` (repeatable), `--who k=v`, `--set
path=value` (lists by id: `censors.too-long.cover=...`), and `-` for stdin.

```bash
S=../scripts/censor_sim.py
python3 $S run examples/dentist-letter.yml 2>events.jsonl          # one cover request
jq -c 'select(.type=="REQUEST") | {id, msg, patch}' events.jsonl   # the open threads
python3 $S run examples/dentist-letter.yml \
        --layer examples/dentist-letter.answers.yml                # answered: deterministic, free
python3 $S resolve examples/beekeepers.yml --set agent.values.informed=12 \
  | python3 $S sweep - --n 5000                                    # compose in pipes
```

## Personality modules

A scenario inherits modules: `inherits: [file, ...]`, relative and
recursive. Dicts merge, `id`ed lists (schemas, censors) merge by id, events
merge by `t`, `drop: true` deletes. `who:` fills `{ally}`-style
placeholders.

| Module | |
|---|---|
| [`personalities/principled-skeptic.yml`](personalities/principled-skeptic.yml) | Shared logic only: facts first. Two people who inherit it agree on every schema and can still act differently |
| [`personalities/loyalty-censors.yml`](personalities/loyalty-censors.yml) | Five censors that keep "my ally said bigoted things" from forming. Template covers |
| [`personalities/status-guard.yml`](personalities/status-guard.yml) | Standing that depends on seeing what's expected |

## Examples (all fictional)

| Scenario | Shows |
|---|---|
| [`examples/dentist-letter.yml`](examples/dentist-letter.yml) ([output](examples/dentist-letter.RUN.md), [answers](examples/dentist-letter.answers.yml)) | A censor learned by marginal attribution, invisible from inside; a joke exposes it and leaves an exception. In 30% of weightings no censor forms at all: the values already avoid the letter |
| [`examples/beekeepers.yml`](examples/beekeepers.yml) | The real-person workflow on people who don't exist: inherit, cast, replace every cover with the character's words, fit the record (6/6), ablate (`tone` isn't needed: the story never offers it) |
| [`examples/emperors-new-clothes.yml`](examples/emperors-new-clothes.yml) | Andersen, 1837. The ablation says the Emperor's censor isn't needed: his values alone explain the praise. He's calculating, not repressing, which matches the story |

## Modeling a real person

The quotes are theirs, the censors are yours, and you label which is
which. Set `real_person: true`; `lint` then fails on any cover that isn't
their own words with a `source:`. Real quotes print only when the model's
action matches what the person did, so a counterfactual can't put words in
their mouth. Keep the model private until they've seen it, and let them
change it: under the
[portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md),
a model of a living person's mind needs their consent before it's public.
