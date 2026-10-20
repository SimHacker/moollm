---
name: task
description: Durable work items that outlive the chat. A task has an id, a title, and a done_when guard you can run; it can be claimed by a human, an LLM character, or a tool. Events are stored append-only; ready, blocked, stale and urgent are computed from guards and buffs. Use when work must survive the session, when someone asks what to do next, or when handing work between people, agents, or sessions.
allowed-tools: [read_file, write_file, run_terminal_cmd, grep]
permissions: [read, write, terminal]
related: [goal, cauldron, workflow, action-queue, buff, advertisement, planning, return-stack, postal, github]
benefits_from:
  - { skill: cauldron, why: "playbooks are tasks; TREE computes the frontier from their guards" }
  - { skill: buff, why: "stale, waiting-on and deadline live on the task and advertise" }
  - { skill: workflow, why: "reusable procedures that spawn tasks with edges" }
respects: [yaml-jazz, postel, robust-first, no-ai-sycophancy]
license: MIT
tags: [moollm, tracking, work, dependencies, tech-tree]
credits: "Don Hopkins. Lineage: The Sims action queue and advertisements, issue trackers, tech trees. Steve Yegge's Beads/Gas Town for the git-persistence point; see README for where MOOLLM departs."
---

# Task ✅

Part of MOOLLM · [This skill's directory](https://github.com/SimHacker/moollm/tree/main/skills/task)

A task is durable work someone can claim, do, and prove done. It outlives the session that
opened it. It lives in whatever container suits the project: a YAML file, a cauldron playbook's
frontmatter, a block in a markdown ledger, or a GitHub issue. The fields are the same in all of
them.

A task inherits [goal](../goal/). A goal is a state of the world someone wants and nobody
claims; a task is a goal someone has claimed. `done_when`, `fail_when`, `requires`, `priority`,
children and the guard compiler come from goal. Owner, judge, CLAIM/RELEASE and the hand-off to
the [action-queue](../action-queue/) are task's own. An action is one step of the work, minutes
long, in one worker's queue; that is the Sims meaning of the word, and MOOLLM keeps it.

## The one rule

**Store what happened. Compute what is possible.**

A task stores events: opened, claimed, released, done, failed, cancelled, reopened, split. The list is
append-only. Everything else is derived at read time:

- **ready** and **blocked** come from running the guards in `requires:`
- **done** comes from running `done_when`, confirmed by a `done` event with evidence
- **stale**, **waiting-on**, **deadline** are buffs hosted on the task
- the board, the kanban columns, the dependency picture are projections, never saved

A hand-typed `status: blocked` is a flag somebody has to remember to clear. Nobody does, and
then the board lies. The same goes for a hand-maintained NEXT-STEPS list. This is the rule
from [designs/TECH-TREE.md](../../designs/TECH-TREE.md) applied to work.

## Schema

```yaml
id: moollm-042                   # prefix-as-owner, big-endian
title: "Add task buffs to the buff library"
why: "Stale tasks need to ask for attention without a patrol agent"
# Reasoning that doesn't fit a field goes in comments. They are data.
done_when: "rg -q '^  stale:' skills/buff/buffs/INDEX.yml"
requires:
  - { task: moollm-040, verify: "test -f skills/task/SKILL.md" }
unlocks:
  - { feature: "boards that flag their own stale work", why: "stale buff advertises CHECK-ON-ME" }
priority: normal                 # an input to scoring, not a queue position
owner: null                      # set by CLAIM
source: "designs/gastown/GASTOWN-VS-MOOLLM-ANALYSIS.md"
links: { github: null, workflow: null }
history:
  - { at: 2026-10-20, event: opened, by: don }
```

Files are flat: the file is the task, so there is no `task:` wrapper. In a markdown ledger each
fenced block is one task.

Required: `id`, `title`, `done_when`. A task without a definition of done is a wish.
`complete_when` (goal's older spelling) and `research_complete_when` (cauldron's) are read as
`done_when`.

`done_when` is either a shell command (exit 0 means done) or prose. Prose is allowed because
plenty of real work has no test: "the README reads well to someone who has never seen MOOLLM".
Prose `done_when` needs a `judge:` — a human, the `evaluator` skill, or a named `rubric`. The
worker who did the job does not certify its own prose guard.

### Accepting other people's status words

Liberal in, conservative out. On input:

| You wrote | Stored as |
|---|---|
| pending, open, todo, backlog | `opened` |
| in_progress, doing, active, hooked | `claimed` |
| done, closed, complete | `done` (after the guard passes) |
| failed | `failed` (after `fail_when` holds, or with a reason) |
| cancelled, wontfix, abandoned | `cancelled` |
| blocked | not stored; becomes a `requires` edge, or a `waiting-on` buff with a reason |

## Methods

**OPEN** — write the task with `history: [{event: opened}]`. Refuse without `done_when`, or
record a prose guard with a judge.

**CLAIM** — append `claimed` with the owner. Then push the first concrete step into the owner's
[action-queue](../action-queue/). The task is days; the action is minutes.

**RELEASE** — append `released` with a required note: what was learned, what is half-done, what
to try next. The next claimant reads it before anything else.

**CHECK** — run every `requires[].verify` and `done_when`; report done, ready, or blocked, and
for blocked, **the first failing guard**, which is the real next step. This is cauldron's
[SCRY](../cauldron/protocols/SCRY.yml) loop: the guard reports, the LLM decides. A guard that
fails for a boring reason (wrong directory, missing tool) is a bug in the guard. Fix the guard;
don't mark the task blocked.

**CLOSE** — run `done_when`. On pass, append `done` with evidence: commit sha, PR, run file, or
the judge's verdict. Then run FRONTIER and say what just became possible. The reward for
finishing is the pointer to what's next, in the same breath.

**CANCEL** — append `cancelled` with the reason. Keep the file. Abandoned work explains later
decisions.

**SPLIT** — open child tasks with `parent:`. The parent's `done_when` becomes "all children
done" unless it already said more.

**FRONTIER** — over a board (a directory, a ledger file, or a cauldron `playbooks/`), partition
into DONE, READY, BLOCKED by running guards. For a cauldron tree this is
[TREE FRONTIER](../cauldron/protocols/TREE.yml); same algorithm.

**BOARD** — render a list, kanban columns, a DAG, or a by-owner view. Projection only; never
written back.

**HANDOFF** — send a [postal](../postal/) letter whose payload is the task reference and a note.
Delivery appends `released` by the sender; the recipient CLAIMs.

**SYNC** — mirror to a GitHub issue with `gh issue create/edit/close`, store the number in
`links.github`. GitHub is a fine place for humans to see and discuss tasks. It is a mirror;
the guard is still the definition of done.

## Where tasks live

Pick whichever fits; a board may mix them.

- **One file per task**: `tasks/moollm-042-task-buffs.yml`. Big-endian names make the directory
  listing the index.
- **A markdown ledger**: one file, one fenced YAML block per task. Loads a whole small backlog
  in one read. [designs/gastown/TASKS-2026-01.md](../../designs/gastown/TASKS-2026-01.md) is the
  January 2026 MOOLLM backlog in this form.
- **Cauldron playbooks**: each `PB-NN-*.md` is a task; `requires:`/`unlocks:` frontmatter per
  TREE; completions append to `playbooks/COMPLETED.yml`.
- **GitHub issues** via SYNC.

Cursor's TodoWrite list is not a place tasks live. It is a session-scoped view of the frontier
of whatever you're working on, and it dies with the chat. Use it for the next ten minutes; open
a task for anything that should exist tomorrow.

Work that won't outlive the session goes in [scratchpad](../scratchpad/). Don't open tasks
for it.

## Status effects are buffs

A task is a host like any other ([buff](../buff/) hosts are open). The library entries are in
[skills/buff/buffs/INDEX.yml](../buff/buffs/INDEX.yml):

- **stale** — no event for N days while claimed or ready. Advertises `CHECK-ON-ME` to the owner
  and anyone viewing the board. Expires on any new event.
- **waiting-on** — the owner names an external wait (review, a person, a vendor). Expires when
  the condition holds, or after N days spawns `stale`.
- **deadline** — ticks the score up as the date approaches; spawns `overdue` if the date passes.
- **flaky-guard** — a guard failed for an uninteresting reason. Advertises `FIX-THE-GUARD`.

Because a buff carries its own advertisements, a stuck task asks for help by itself. Nothing has
to poll for it. Gas Town runs a Witness agent and a Deacon daemon on patrol cycles to find stuck
work; here the stuck work raises its hand.

No buff closes a task. Age is not evidence that work is done. Gas Town's reaper closed five live
bug reports in one day because they were old
([#4911](https://github.com/gastownhall/gastown/issues/4911)). A stale task gets attention. It
only closes when its guard passes, or when someone CANCELs it with a reason.

## Who picks up what

A ready task advertises `WORK-ON-ME` to workers. Score is priority × fit to the worker's skills ×
freshness, plus whatever buffs add. The owner's own claimed task scores highest for that owner,
so a worker who wakes up into a new session goes back to what it claimed. That is the whole of
Gas Town's "if there's work on your hook, run it", and it's how a Sim decides to eat:
advertisements and scores, not a principle with an acronym.

Workers can be humans, LLM characters in one context, or separate executor sessions. When the
tasks are small and share context, simulate several workers in one call
([speed-of-light](../speed-of-light/)). When tasks need separate checkouts, long tool runs, or
different models, give each to its own session, the way cauldron hands one playbook to one
executor chat. Each task file works the same either way.

## Interruptions

Urgent work arrives mid-task: [return-stack](../return-stack/) PUSH the current task with a
one-line note of where you were, action-queue URGENT the new work, POP when it's done. The
pushed task gets no event, so if the interruption runs long, `stale` will notice.

## Commits

[thoughtful-commitment](../thoughtful-commitment/) cites task ids in commit messages; CLOSE
takes the resulting sha as evidence. A cursor-mirror session id in `links.session` lets anyone
trace from the task to the reasoning that closed it.

## Related skills

- [goal](../goal/) — the parent: the condition keys, dependencies and guard compiler.
- [cauldron](../cauldron/) — the big-plan engine; its playbooks are tasks and TREE is the graph.
- [workflow](../workflow/) — reusable procedures that spawn tasks.
- [action-queue](../action-queue/) — what a claimed task turns into, minute by minute.
- [buff](../buff/) — status effects with clocks.
- [advertisement](../advertisement/) — how ready tasks find workers.
- [planning](../planning/) / [plan-then-execute](../plan-then-execute/) — decomposition and
  approval gates above the task level.
- [postal](../postal/), [github](../github/), [return-stack](../return-stack/),
  [evaluator](../evaluator/), [rubric](../rubric/), [scratchpad](../scratchpad/).

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/task/](https://github.com/SimHacker/moollm/tree/main/skills/task)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
