---
name: workflow
description: Reusable procedures for MOOLLM. A workflow is a prototype of steps with actors, dependencies, verification, approval gates and parallel legs; running it clones the prototype into an instance directory and opens one task per step. Use when a sequence of work has been done the same way more than twice, when someone names a procedure to run, or when a finished run should improve the procedure.
allowed-tools: [read_file, write_file, run_terminal_cmd]
permissions: [read, write, terminal]
related: [task, cauldron, play-learn-lift, plan-then-execute, planning, prototype, speed-of-light]
benefits_from:
  - { skill: task, why: "instances are boards of tasks; STATUS is task FRONTIER" }
  - { skill: cursor-mirror, why: "LIFT and RETRO read what actually happened in past sessions" }
respects: [yaml-jazz, postel, robust-first]
license: MIT
tags: [moollm, procedure, workflow, orchestration]
credits: "Don Hopkins. Lineage: Papert's procedures, CI/GitHub Actions, Temporal durable execution, cauldron. Steve Yegge's Gas Town molecules/formulas for parallel legs and model tier hints; see README."
---

# Workflow 🔁

Part of MOOLLM · [This skill's directory](https://github.com/SimHacker/moollm/tree/main/skills/workflow)

A workflow is a procedure worth repeating. It says what the steps are, who or what does each
one, what each step needs first, how you know a step is done, where a human signs off, and what
can run in parallel.

The workflow file is a **prototype**. Running it clones the prototype into an instance
directory and opens one [task](../task/) per step. **The tasks carry all run state. The
workflow never does.** That's what makes a run resumable: a new session, a new model, or a
different person runs FRONTIER over the instance and picks up where things stand.

## Do it by hand three times, then lift it

Don't design workflows up front. Do the work by hand, as tasks, and keep the histories. When
the same sequence shows up the third time, LIFT it: diff the histories, keep the common steps
in their common order, turn the parts that varied into inputs. This is the LIFT phase of
[play-learn-lift](../play-learn-lift/) applied to work.

A workflow designed before anyone has done the work describes how somebody imagined it would
go.

## Schema

```yaml
workflow:
  id: release
  parent: null                 # inherit steps from another workflow (Self-style delegation)
  inputs:
    version: "semver of the release"
    platforms: "list: [mac, linux, windows]"
  steps:
    - id: test
      does: "Run the full test suite on main"
      actor: tool
      verify: "make test"

    - id: build
      does: "Build {{version}} for {{leg}}"
      actor: tool
      fan_out: { over: platforms, step: build }   # one task per platform, in parallel
      requires: [test]
      verify: "test -f dist/{{version}}-{{leg}}.tar.gz"

    - id: notes
      does: "Draft release notes from PRs merged since the last tag"
      actor: skill:thoughtful-commitment
      requires: [test]
      model: fast
      verify: "test -s dist/NOTES-{{version}}.md"

    - id: approve
      does: "Read the notes and the build list; approve or send back"
      actor: human
      gate: approval
      requires: [build, notes]   # requiring a fan_out step waits for every leg: the join

    - id: publish
      does: "Tag and publish"
      actor: tool
      requires: [approve]
      verify: "git rev-parse v{{version}}"
      on_fail: escalate
  lessons: []
```

### Step fields

- **`does`** — one imperative sentence. `{{slots}}` fill from inputs and the fan_out leg.
- **`actor`** — `tool`, `skill:<id>`, `llm`, or `human`. These are cauldron's three delegation
  tiers (tool, other skill, the LLM itself) plus people. Naming the actor matters: a tool step
  is cheap and deterministic, an LLM step needs judgment, a human step waits.
- **`requires`** — step ids. Becomes the step task's `requires:` with the upstream task's
  `done_when` as the verify.
- **`verify`** — becomes the step task's `done_when`. Required, except on human steps, which
  must say what the human checks.
- **`gate: approval`** — the step's dependents stay unready until a human appends an `approved`
  event. This is [plan-then-execute](../plan-then-execute/) inside a workflow.
- **`fan_out`** — one task per item in an input list. Any step that requires the fan_out step
  waits for every leg, which makes it the join.
- **`model`** — a hint, not a binding: `fast`, `deep`, or a model id. See cauldron's
  [MODEL-ROUTING](../cauldron/protocols/MODEL-ROUTING.yml).
- **`on_fail`** — `scry` (default: read the failing guard, fix the work or the guard, re-run),
  `retry:N`, or `escalate`. Never skip silently ([robust-first](../robust-first/)).

## Methods

**DEFINE** — write a prototype to `workflows/<id>.yml`, or inside a skill as
`skills/<skill>/workflows/<id>.yml`. Refuse steps with no verify unless the actor is human and
the step says what gets checked.

**LIFT** — from three or more task histories or [cursor-mirror](../cursor-mirror/) sessions,
extract the common steps and order; variations become inputs. Show the diff before writing.

**INSTANTIATE** — create the instance directory with a `WORKFLOW.yml` whose `parent:` is the
prototype and whose inputs are filled. OPEN one task per step (one per leg for fan_out) with
edges and guards. Report the frontier. The instance's identity is its directory: copy it to fork
a run, move it to rename it.

Refuse to instantiate if any rendered `does` or `verify` still contains `{{`. An unfilled slot
is an error, not text for the executor to interpret. Gas Town's renderer passed
`{{#if dry_run}}--dry-run{{/if}}` through verbatim, so a purge command meant to be rehearsed has
always run live ([#4909](https://github.com/gastownhall/gastown/issues/4909)). If a step's
safety depends on an input such as a dry-run flag, put that flag in the step's `verify` so a
dropped flag fails the guard.

**STATUS** — task FRONTIER over the instance. Done, ready, blocked, and the first failing guard.

**AMEND** — change one run without changing the procedure: skip a step, add one, swap an actor.
Edit the instance's tasks and append the reason to the instance's `WORKFLOW.yml`.

**RETRO** — after a run, read the task histories: released notes, failed guards, amendments,
human gate rejections. Propose edits to the prototype and append what was learned to
`lessons:`. Lessons are append-only; the prototype's steps change, the record of why doesn't.

**FREEZE** — mark an instance so none of its tasks become ready until a human approves the
whole plan. Use when steps touch untrusted input or production.

## Simulate or spawn

Fan-out legs that are small and share context can run as simulated workers in one call
([speed-of-light](../speed-of-light/)); an aspect analysis over five perspectives is an
[adversarial-committee](../adversarial-committee/) session, not five processes. Legs that need
their own checkout, a long build, or a different model go to separate sessions, the way
cauldron gives one playbook to one executor chat. The instance tasks are identical either way,
so the choice can change mid-run.

## Workflows already in MOOLLM

These skills are workflows that predate this one. They keep their own protocols; this skill
names the shape they share.

| Skill | Shape |
|---|---|
| [cauldron](../cauldron/) | MELT → STIR × N → LADLE → ANCHOR → LINK → TASTE → SERVE, SCRY loops inside |
| [plan-then-execute](../plan-then-execute/) | PLAN → REVIEW → APPROVE (gate) → EXECUTE |
| [play-learn-lift](../play-learn-lift/) | PLAY → LEARN → LIFT |
| [experiment](../experiment/) | configure → run → score → compare |
| [thoughtful-commitment](../thoughtful-commitment/) | read the thinking → draft → commit |

Cauldron is the one-off case: a single large plan melted and ladled into playbooks. A workflow
is the repeated case. When the third cauldron brew of the same kind of plan follows the same
playbook outline, LIFT the outline.

## Worked example

[workflows/add-skill.yml](workflows/add-skill.yml) is the procedure for adding a MOOLLM skill,
lifted from adding this one, `task`, `copy-that` and `no-ai-humansplaining`. It has a fan_out
over related skills for reverse links, a skill-snitch step, and a human approval gate at the end.

## Related skills

- [task](../task/) — what instances are made of.
- [cauldron](../cauldron/) — the large one-off plan engine; its playbooks are tasks.
- [play-learn-lift](../play-learn-lift/) — where workflows come from.
- [plan-then-execute](../plan-then-execute/) — FREEZE and approval gates.
- [planning](../planning/) — a living plan is a workflow instance without a prototype yet.
- [prototype](../prototype/) — `parent:` delegation.
- [speed-of-light](../speed-of-light/), [adversarial-committee](../adversarial-committee/),
  [action-queue](../action-queue/), [cursor-mirror](../cursor-mirror/).

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/workflow/](https://github.com/SimHacker/moollm/tree/main/skills/workflow)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
