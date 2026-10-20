# Workflow 🔁

Reusable procedures for MOOLLM. Protocol: [SKILL.md](SKILL.md). Interface: [CARD.yml](CARD.yml).
Quick look: [GLANCE.yml](GLANCE.yml). Example: [workflows/add-skill.yml](workflows/add-skill.yml).

## Why

Half the skills in MOOLLM are workflows already. Cauldron sequences seven phases with loops and
branches. Plan-then-execute has an approval gate. Play-learn-lift has three phases. Each of them
wrote its own state machine in its own CARD. That's fine for those skills, and they keep their
protocols. What was missing was a way to write a *new* procedure without inventing a new skill:
"this is how we release", "this is how we add a skill", "this is how we review a PR".

The workflow skill is that way. A workflow is a small YAML prototype. Running it opens tasks.
Everything about the run lives in the tasks, so the workflow file stays a clean description of
the procedure and improves with each RETRO.

## Lineage

- **Papert's procedures.** Logo taught kids to name a procedure, run it, watch it fail, and debug
  it. A workflow is a procedure for work, and RETRO is the debugging.
- **CI and GitHub Actions.** Steps, `needs:`, matrices, manual approvals. Every model has read
  thousands of these files, which is why the step fields look the way they do.
- **Temporal and durable execution.** Run state as an event log; resume by replaying. Here the
  event log is the task histories and replay is FRONTIER.
- **Cauldron.** The three delegation tiers (tool, skill, LLM), SCRY loops, model routing per
  phase, identity through location. Workflow generalizes them from one big plan to any
  repeated procedure.
- **Self.** A workflow can set `parent:` and inherit another workflow's steps, overriding the
  ones that differ. No class hierarchy; just delegation.

## Gas Town's molecules and formulas

Gas Town has a workflow layer too, and it's worth being specific about what it does well.

**What we took.**

- **Parallel legs with a synthesis step.** Gas Town's "convoy" formula type runs legs in parallel
  and then synthesizes. That's `fan_out` plus a join step here.
- **A model tier hint per step.** Gas Town's `MoleculeStep` has a `Tier` field. Good idea; cauldron
  had already arrived at the same place with model routing per phase. Here it's `model:`.
- **Durable chains.** A molecule survives agent restarts because its state is on disk. Same here,
  because the state is in task files.

**Where we part ways.**

- **Four formula types for one shape.** Gas Town distinguishes convoy, workflow, expansion and
  aspect formulas, in TOML. Here they are all one schema: sequential is `requires:`, parallel
  is `fan_out`, expansion is INSTANTIATE with inputs, and aspect analysis is a committee, which
  can run in a single call instead of as separate agents.
- **Names.** Molecule, protomolecule, formula, wisp, convoy. The procedure is a workflow. The
  model knows the word, and so does everyone who has opened `.github/workflows/`.
- **Who checks the work.** Gas Town keeps the pipeline moving by throwing more agents at it
  until things converge. Here every step has a `verify`, a failing step returns the failing
  guard, and human gates are explicit. Retries are fine when "done" is something you can run.
- **Reading it.** A workflow is a short YAML file you read before you run it. You can't improve
  a procedure you've never looked at.

The longer argument is in [designs/gastown/](../../designs/gastown/).

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/workflow/](https://github.com/SimHacker/moollm/tree/main/skills/workflow)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
