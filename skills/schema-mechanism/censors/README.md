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
| `predict FILE --offers A,B [--set-item K=on]` | forecast the next event under every hypothesis; commit it before it happens ([LIVE.md](LIVE.md)) |
| `induce FILE [--run R]` | Drescher's extended context over the record: which items made each observed choice likelier; flags ones the model lacks |
| `suite PATH... [--ablate]` | Lint and test every scenario under the paths (each with its `.answers.yml`), one line each; `--ablate` lists the censors each run doesn't need. Exit 2 on any failure |
| `argue FILE --offers A,B --goal A --args ARGS [--set-item K=V]` | Plan validation by simulation: each argument (an event of `say`/`set`/`joke`) before the next choice, P(goal) under every run, and which arguments the runs disagree about |
| `drift FILE [--half-life N]` | Fit over time: hits weighted toward recent choices, where each run's unbroken hits begin, and a `#.#` strip of hits and misses |
| `propose FILE [--run R]` | Drescher's synthetic items over the record: a choice that switched once with nothing observed to explain it; proposes a latent item and asks what it was (`--patch` for the layer) |
| `plan FILE --goal G [--run R] [--at start\|end] [--set-item K=V]` | Drescher's planner (Dijkstra over schemas, cost 1 − log reliability) with Minsky's censors in the search: the plan the agent can think of, the plan an observer sees, and the censor that hid each missing step |
| `learn FILE [--run R] [--rounds N] [--patch]` | Drescher's learner over the record: replays what the person did with result and context spinoffs on, proposes each learned schema, keeps it only if the fit improves, and asks the other tier what each kept one means. `--patch` writes the kept ones as a layer |
| `try FILE --layer L [--run R]` | The gate for any proposal, from `learn`, a person or a language model: rejects a layer that makes a run fit worse or adds a lint error |
| `duet FILE [--n N] [--test]` | Two minds on one stage. Each turn is one seat's choice or the world changing; `effects` make one mind's move the other's news, and `when` skips turns the world never reached. With `--n`, each seat's weights are drawn independently and the outcomes tallied. `suite` runs duets too |
| `bench FILE --n N` | simulations per second |
| `diff A B` | shared logic, different priorities, which censors each mind has |
| `where FILE PATTERN` | which layer defines what matches |
| `lineage FILE` | the parts a mind is built from, in merge order, each once |
| `export FILE [--format dot]` | resolved model, or a censor graph for Graphviz |
| `import TEXT` | split a message thread into skeleton events, one request per message |
| `apply PATCH --into FILE` | merge a patch layer into a file |

Scoring options on `agent:`: `score: earned` (default; a result pays every
time, as if the motive had decayed back) or `score: change` (only what the
action changes, as The Sims' Find Best Action scores the delta), and
`losses_hurt: true` to count losing a valued item as pain when learning.
`learn_schemas: true` lets a mind start from bare schemas and spin off what
its actions do from what follows them, as Drescher's agent does.

Tests: `python3 ../scripts/test_censor_sim.py` checks the engine's own rules;
`suite` checks the models against their records; `python3
../scripts/regen_runs.py --check` fails if a generated `RUN.md` is stale.

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

A scenario inherits modules: `inherits: [file, ...]`, relative, recursive
and multiple (a shared parent merges once). Dicts merge, `id`ed lists
(schemas, censors) merge by id, events merge by `t`, `drop: true` deletes.
`who:` fills `{ally}`-style placeholders.

The modules are a construction kit, down to one censor per file:
**[`BRAINBALL.md`](BRAINBALL.md)** covers the parts in [`parts/`](parts/), the
archetypes in [`archetypes/`](archetypes/), single-trait `imports:`, and how to compose a person.

| Module | |
|---|---|
| [`personalities/principled-skeptic.yml`](personalities/principled-skeptic.yml) | Shared logic only: facts first. Two people who inherit it agree on every schema and can still act differently |
| [`personalities/loyalty-censors.yml`](personalities/loyalty-censors.yml) | Bundle of five censor parts that keep "my ally said bigoted things" from forming. Template covers |
| [`parts/crowd-logic.yml`](parts/crowd-logic.yml) | Shared logic for a crowd around a figure: belonging pays with every defense |
| [`personalities/status-guard.yml`](personalities/status-guard.yml) | Standing that depends on seeing what's expected |
| [`parts/credit-logic.yml`](parts/credit-logic.yml) | Shared logic, both seats, for a goal only an opponent can sign: offer him the credit or don't; take it, or keep the veto |
| [`archetypes/the-credit-giver.yml`](archetypes/the-credit-giver.yml) | Goal over credit, plus one anecdotal censor, `play-the-ball`: when he signals, don't refuse because it's him. Swap in `drive-the-taunt` for the stunt reading; `drive-name-on-it` is the target's side |

## Examples (all fictional)

| Scenario | Shows |
|---|---|
| [`examples/learning-toddler.yml`](examples/learning-toddler.yml) | Drescher's learner from bare schemas: cries, is scolded, learns *cry → scolded*; asks, gets a snack, learns *ask → snack*, then *when the parent is home*. The learning mind fits 7/7, the same mind without learning 2/7; `learn` from outside reaches 5/7, because only a learner fits a learner's early mistakes |
| [`examples/dentist-letter.yml`](examples/dentist-letter.yml) ([output](examples/dentist-letter.RUN.md), [answers](examples/dentist-letter.answers.yml)) | A censor learned by marginal attribution, invisible from inside; a joke exposes it and leaves an exception. In 30% of weightings no censor forms at all: the values already avoid the letter |
| [`examples/beekeepers.yml`](examples/beekeepers.yml) ([output](examples/beekeepers.RUN.md)) | The real-person workflow on people who don't exist: inherit, cast, replace every cover with the character's words, fit the record (6/6), ablate (`tone` isn't needed: the story never offers it) |
| [`examples/beekeepers-second-round.yml`](examples/beekeepers-second-round.yml) | The principled ally's second round: the witness discounted ("never said that to me"), the friend's story kept (confidential), and a loyalty debt that makes the scope censor unnecessary. Two accounts, both 8/8 |
| [`examples/beekeepers-open-skeptic.yml`](examples/beekeepers-open-skeptic.yml) | The open skeptic in Ruth's seat: same logic, none of her censors, four anecdotal patches. Asks Tom, asks the Hive Watch, checks Tom's story, believes Mags, in every weighting, and ends with both conflicts conscious |
| [`examples/unrepentant-beekeeper.yml`](examples/unrepentant-beekeeper.yml) | The accused's side: out of context, the context never named. Repressing (six censors, all needed) and face-first (none) both fit 7/7; a joke exposing the out-of-context move separates them |
| [`examples/quiet-secretary.yml`](examples/quiet-secretary.yml) ([answers](examples/quiet-secretary.answers.yml)) | A record with something missing. Four defenses, then four silences, and nothing observed changes: the model fits 4/8, `induce` finds nothing, `propose` finds the switch and asks what it was. Answered, it fits 8/8 |
| [`examples/emperors-new-clothes.yml`](examples/emperors-new-clothes.yml) ([output](examples/emperors-new-clothes.RUN.md)) | Andersen, 1837. The ablation says the Emperor's censor isn't needed: his values alone explain the praise. He's calculating, not repressing, which matches the story |
| [`examples/name-on-the-clinic.yml`](examples/name-on-the-clinic.yml) | A reformer offers the mayor she mocked his name on a free clinic. The offer fits the goal reading and the stunt reading; what she does after he bites splits them (4/4 against 2/4). The censor is needed only in the mind that despises him |
| [`examples/mayor-thorne.yml`](examples/mayor-thorne.yml) | The other seat: the mayor offered the credit. His spokesman attacked the offer and he shared it himself; the vain and indifferent readings each fit one of those (2/3) |
| [`examples/name-on-the-clinic.duet.yml`](examples/name-on-the-clinic.duet.yml) | Both seats at once. The clinic gets signed only if she means it and he wants his name on it; a taunting reformer stalls after he bites, an indifferent mayor attacks and nothing follows. 78% of 2,000 joint weightings end signed |
| [`examples/baron/`](examples/baron/) ([output](examples/baron/RUN.md)) | Six followers of a fictional platform baron, built from archetypes, on one record. The friend's censors can't keep him; the crowd's belonging keeps everyone else with no censor needed; a crusader and a convert act identically and differ only in what they know. See [`BRAINBALL.md`](BRAINBALL.md#the-barons-crowd) |

## Modeling a real person

The quotes are theirs, the censors are yours, and you label which is
which. Set `real: [self]` (or `real_person: true`); `lint` then fails on any
cover that isn't their own words with a `source:`. With `real: [ally]`, a
real public figure in the center seat, `lint` fails on any event without a
`source:`. Real quotes print only when the model's
action matches what the person did, so a counterfactual can't put words in
their mouth. Keep the model private until they've seen it, and let them
change it: under the
[portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md),
a model of a living person's mind needs their consent before it's public.
