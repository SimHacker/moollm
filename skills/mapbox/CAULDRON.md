# eval-harness — cauldron (parked, not adopted)

Status: **parked 2026-09-20.** Interesting, not scheduled. Harvested here because this is
where the pattern was found — Mapbox ships it and moollm does not. Lives in `skills/mapbox/`
until it either graduates into its own skill or gets thrown out. Registered as
`planned: eval-harness` in `skills/INDEX.yml` so it is findable without reading this file.

## What the pattern is

`mapbox/mapbox-agent-skills` ships an `evals/evals.json` inside every skill: hard questions
with graded rubrics, plus a runner that grades a model's answers with a second model.

Each item carries a `prompt` (a realistic hard question), an `expected_output` in prose,
optional `files` for context, and `expectations` — a list of specific things a good answer
must contain. The runner concatenates `SKILL.md` and every file in `references/`, sends the
prompt with that as context, then hands prompt, response and expectations to a judge model
which scores **each expectation 0–3** (`FULL`, `PARTIAL`, `MINIMAL`, `MISS`) with a written
reason. Totals roll up per skill into `evals/baseline.json`; `--diff` compares a fresh run
against the stored baseline; `--update-baseline` re-baselines.

Measured in their repo on 2026-09-20: **89 eval items, 386 graded expectations, 20 skills.**
The committed baseline is older and smaller — 51 evals at 672/684, or 98.2%, judged by
Sonnet 4 on 2026-03-30. Machinery is `scripts/eval.js` plus `run-evals.js`, about 500 lines,
`@anthropic-ai/sdk`, concurrency 10, model and judge set by `EVAL_MODEL` and
`EVAL_JUDGE_MODEL`. Their `metrics/` directory is unrelated — GitHub traffic stats.

## Why moollm would want it

Because of the **ambient eleven**. Every ambient skill makes a falsifiable behavioural
claim: `no-ai-sycophancy` prevents softened disagreement, `no-ai-hedging` eliminates
qualifier stacking, `no-ai-slop` fires a CLAIM-LEDGER gate on every user claim. Those claims
are currently untested. Ambient status is described in the CARD as permission to live in
context rent-free, granted on trust — and trust is exactly what a harness would replace with
a number.

The rubric scale already exists in the repo. `no-ai-sycophancy`'s calibration ladder —
exceptional, good, adequate, flawed, wrong — is a 0–3 judge rubric with one extra rung.

## The upgrade they do not have: an ablation arm

Their runner always loads the skill. There is no without-skill control, so the baseline is
**temporal** — it answers "did my edit make this worse?" and cannot answer "does this skill
do anything at all?"

For Mapbox that is the right question. For moollm's ambient skills it is the wrong one. The
useful design runs each prompt twice, with and without the skill in context, and reports the
delta. An ambient skill whose delta is zero is spending context for nothing, and that is a
result you can act on — unlike a regression number on a suite already scoring 98.2%, which
has almost no headroom to detect improvement.

## The composed stack: harness + mirrors + monitors

The ablation arm above is one upgrade. The larger one is that **an eval grades output, and output is
the least informative thing about a skill.** moollm already has the other two instruments; the point
is that they are separate tools over one shared substrate, and the substrate is the transcript.

| Axis | Instrument | Question it answers | Blind to |
|---|---|---|---|
| Output | `evals/evals.json` + judge | Did the answer satisfy N expectations? | Whether the skill had anything to do with it |
| Process | `cursor-mirror` (per harness) | Was the skill opened? Which files? What did it cost? | Whether the answer was any good |
| Safety | `skill-snitch` (SCAN / AUDIT / SNITCH) | Should this skill be trusted to run at all? | Both of the above |

### Attribution: the failure an output-only harness cannot see

A `FULL` score has at least three causes and the harness cannot tell them apart:

1. The skill supplied the knowledge. *(what you wanted to measure)*
2. The base model already knew, and the skill was decoration.
3. The skill was **never read** — the runner concatenated it into context and the model answered from
   priors without attending to it.

Ablation separates 1 from 2 statistically, over a suite. `cursor-mirror` separates 3 mechanically, per
run, by reading the actual tool calls: `tools <composer>` shows whether the file was opened,
`timeline` shows when, `thinking` shows whether it was reasoned over or skimmed past. **"Correct answer,
skill never consulted" is a passing eval measuring the base model** — and it is invisible without
process data, which is why a green suite is weaker evidence than it looks.

The cost dimension arrives free with the same data. A skill that scores `FULL` while burning 40k
tokens of context has a result the rubric has no column for, and for ambient skills — which pay rent
continuously — that column matters more than the score.

### Why "mirrors" is plural, and why Mapbox specifically should care

A mirror is harness-specific: `cursor-mirror` reads Cursor's LevelDB, a Claude Code mirror reads its
JSONL, and the next host will store transcripts its own way. That looks like a chore and is actually
the interesting measurement, because **Mapbox ships the same `SKILL.md` into every host** —
`npx skills add` lands it in `~/.agents/skills` or `~/.claude/skills`, and each host has its own
loading rules, context budget, tool availability and description-matching for selection.

So a skill graded in one harness is **unverified in the others**, and nothing in the current design
would notice. Same twenty files, different behaviour per host, one baseline. A mirror per harness turns
"does this skill behave the same in Cursor as in Claude Code?" from a shrug into a diff.

### skill-snitch is supply-chain review, which no eval performs

A skill is instructions an agent will follow. Publishing twenty of them under MIT, installable by a
package manager, is shipping executable instructions into other people's agents — and evals grade
helpfulness, never whether a skill tells the agent to fetch, exfiltrate or run something it shouldn't.
`skill-snitch`'s three methods map onto three moments: SCAN before trusting, AUDIT before adopting,
SNITCH while running (via the mirror, which is why the integration already exists).

For a platform vendor this is not hypothetical housekeeping. Their repo is the trust anchor for a
namespace anyone can typosquat, and a consumer installing `mapbox-*` skills currently has no way to
check what they agreed to run.

### Harvesting beats authoring

Mapbox hand-wrote 89 eval items, which is the part that does not scale — authoring evals is slower than
writing the skill. But a mirror is sitting on a corpus of **real questions, with real answers, already
graded implicitly by whether the user accepted the result.** Every session is an unlabelled eval.

Which makes the pipeline: mirror harvests candidate prompts from real transcripts → judge grades them
against the skill's expectations → the ones that discriminate become committed evals. That inverts the
economics, and it is the same observation as
[`design-sense/lenses/interfaces-to-agency`](../design-sense/lenses/interfaces-to-agency.md)'s
demonstration argument pointed at testing instead of teaching: **use produces the corpus as a
byproduct.**

## The trap, with a worked example

**An eval locks in whatever its author believed.** It is a regression detector, not a truth
oracle, and it preserves errors faithfully.

Their `mapbox-token-security` eval id 2 grades five expectations, three of which reward
wildcard URL patterns:

```
- Recommends 'https://myapp.com/*' for production
- Recommends 'http://localhost:*' or 'http://127.0.0.1:*' for local development
- Warns against overly broad patterns like 'http://*' or '*.com/*'
```

The Mapbox console rejects wildcards outright: "Wildcard characters (*) are not supported in
URL restrictions." So their harness now scores a correct answer as a MISS and a wrong answer
as FULL, and the score stays green while the guidance is wrong. See `CARD.yml#measured` for
the probe.

Consequence for any moollm adoption: an expectation asserting external behaviour needs a
provenance field saying how it was verified and when, or the suite becomes a monument to a
belief. Expectations about *our own* conventions are safe; expectations about *the world*
rot.

## Open questions before graduating

- Where does the runner live — a `skills/eval-harness/` skill in sister-script shape, or
  repo infrastructure? Leaning skill: it should be usable against any skill, and be
  self-documenting.
- Does it fold into `evaluator` or `skill-snitch` instead of adding a 150th? Now leaning **no, and
  deliberately**: the three instruments above are orthogonal and share a substrate rather than a
  purpose. Keeping them separate is what lets them compose — snitch audits, mirror observes, harness
  grades, and each is useful without the others. One merged skill would be a worse version of all
  three. What they need is an agreed transcript shape to pass between them.
- Can the judge run against transcripts cursor-mirror already has, rather than fresh API calls? This
  is the highest-value open question, because it decides whether ablation is affordable and whether
  evals can be *harvested* rather than authored. The thing it turns on is whether a transcript records
  **which skills were in context**, not just which files were opened — and cursor-mirror already has
  `context`, `context-sources`, `request-context --message N`, `agent-tools` and `mcp-tools`, which is
  exactly where to look before writing anything. Probe those against a session known to have loaded a
  skill; if injected rule and skill text is recoverable per request, the ablation arm is nearly free in
  Cursor and the remaining work is one mirror per other harness.
- Cost at full coverage: two model calls per expectation, so roughly 772 calls for a
  386-expectation suite. Cheap per run, not free per iteration.
- Does an eval belong in the semantic image pyramid at all? It is not a lower rung — GLANCE,
  CARD, SKILL and README are all *description*, and an eval is *measurement*. Orthogonal
  axis, so the "never load a lower level without the level above" rule does not apply.

## Provenance

Harvested from `mapbox/mapbox-agent-skills` @ `aab3a6f` (2026-09-16, MIT), read at
`/Users/a2deh/GroundUp/git/mapbox-agent-skills`. Numbers counted from that checkout on
2026-09-20, not quoted from its documentation.
