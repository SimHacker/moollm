# Task ✅

Durable work items for MOOLLM. Protocol: [SKILL.md](SKILL.md). Interface: [CARD.yml](CARD.yml).
Quick look: [GLANCE.yml](GLANCE.yml).

## Why a task skill now

MOOLLM has been tracking work for a year without naming the thing. The January 2026 backlog
([designs/gastown/TASKS-2026-01.md](../../designs/gastown/TASKS-2026-01.md)) is thirty-odd YAML
blocks with ids, statuses, sources and deliverables. Cauldron playbooks are tasks with
verification blocks. Goals had `complete_when`. The action queue holds Sims-style actions.
Buffs put clocks on everything. Each of those skills reinvented a corner of task tracking, and
none of them said what a task was.

This skill says it, and wires the corners together:

| Existing skill | What it already did | What the task skill adds |
|---|---|---|
| [goal](../goal/) | Condition guards, compiled to JS and Python | Task inherits goal; both now spell the guard `done_when` |
| [cauldron](../cauldron/) | Playbooks with Verify blocks; TREE computes the frontier | Says every playbook is a task, so FRONTIER works on any board |
| [action-queue](../action-queue/) | Sims queue of short actions | CLAIM feeds it; tasks are days, actions are minutes |
| [buff](../buff/) | Effects with ticks and expiry on any host | Task-hosted buffs: stale, waiting-on, deadline, flaky-guard |
| [advertisement](../advertisement/) | Objects bid for attention | Ready tasks bid for workers |
| [planning](../planning/) | Living step lists | Steps worth keeping past the chat become tasks |
| [postal](../postal/) | Letters between characters | HANDOFF is a letter carrying a task |
| [github](../github/) | `gh issue` operations | SYNC mirrors a task to an issue |

## Why "task", not "action" or "goal"

Three words, three lifetimes. A **goal** is a state of the world someone wants; nobody claims
it, and it holds or it doesn't (Minsky: a difference to reduce). A **task** is a goal someone
has claimed: it has an owner, a history, and a judge. An **action** is one step of the work, in
one worker's queue, minutes long and interruptible. That last one is what The Sims calls an
action, what an [advertisement](../advertisement/) offers, and what
[action-queue](../action-queue/) holds; naming durable work "action" would give one word two
lifetimes. So task inherits goal, a claimed task pushes actions, and each word keeps one meaning.

## The design in one paragraph

Store events, compute state. A task's history is append-only. Ready and blocked come from
running guards. Stale and urgent are buffs with clocks, and because buffs carry advertisements,
a stuck task asks for attention by itself. The board is a view. Nothing anyone has to remember
to update, so nothing goes stale silently.

## Gas Town and Beads: where we agree and where we don't

Steve Yegge's [Beads](https://github.com/steveyegge/beads) and
[Gas Town](https://github.com/steveyegge/gastown) are the best-known recent attempt at agent
task tracking, so they are the obvious comparison. Full analysis:
[designs/gastown/](../../designs/gastown/).

**Where we agree.**

- **Agent work state belongs in git and must survive session death.** Beads gets this right,
  and it is the most useful idea in the project. An agent that loses its context should be able
  to read its work back off disk and keep going.
- **Identity persists; sessions are disposable.** Gas Town's "hook" pins work to an agent
  identity rather than to a process. Our `owner:` field plus advertisement scoring does the
  same job.
- **Dependencies are first class.** Beads has `depends_on`; we have `requires:` with guards.
- **Retries are fine if done is checkable.** Yegge calls this nondeterministic idempotence:
  paths vary, the outcome converges. That only holds if the outcome is defined by something
  you can run. Hence `done_when`.

**Where we depart, and why.**

- **The word.** Gas Town's own README says "the terms 'bead' and 'issue' are used
  interchangeably." Then call it an issue, or a task. Every model has read millions of each.
  Nobody has read about beads. A name that needs explaining in every prompt is a tax you pay
  forever ([no-ai-humansplaining](../no-ai-humansplaining/)).
- **What gets stored.** Beads stores `status: open | in_progress | closed` and Gas Town runs
  supervisors (Witness, Deacon, Boot the dog) on patrol cycles to notice when stored status has
  stopped matching reality. We store events and compute status, and let a `stale` buff do what
  the patrols do.
- **Format.** Beads rows are JSONL synced with a SQLite database behind a `bd` CLI. JSON has
  no comments, so the reason a task is high priority lives somewhere else or nowhere. Our tasks
  are YAML a person or a model reads directly, and the comments carry the reasoning
  ([yaml-jazz](../yaml-jazz/)).
- **One type for everything.** Gas Town registers eleven custom bead types: agent, role, rig,
  convoy, slot, queue, event, message, molecule, gate, merge-request. Half of those are not
  work. A message is a [postal](../postal/) letter, an agent is a [character](../character/),
  a lock is a lock. A task is a task.
- **Access path.** In the January 2026 snapshot, Gas Town's Go code shells out to the `bd`
  binary at 231 call sites to read and write its own state. A MOOLLM task is a file. The model
  reads it.
- **Done is proved, not declared.** CLOSE runs the guard. Prose guards need a judge who isn't
  the worker.

## Vocabulary

| Gas Town | MOOLLM | Also known as |
|---|---|---|
| bead | task | issue |
| hook / pinned bead | `owner:` + highest ad score | assignee |
| GUPP ("work on your hook, run it") | advertisement scoring | Sims autonomy |
| convoy | [workflow](../workflow/) instance, or a GitHub milestone | batch, epic |
| molecule, formula | [workflow](../workflow/) | procedure, recipe, GitHub Actions workflow |
| wisp | [scratchpad](../scratchpad/) | scratch |
| gate | workflow `gate:` | approval |
| polecat | executor, worker | |
| Witness / Deacon patrols | `stale` buff advertising | |
| mail | [postal](../postal/) | |

The reasoning for each choice is in
[designs/gastown/CONSTRUCTIONIST-TERMINOLOGY.md](../../designs/gastown/CONSTRUCTIONIST-TERMINOLOGY.md).

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/task/](https://github.com/SimHacker/moollm/tree/main/skills/task)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
