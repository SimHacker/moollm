# Vocabulary for work: task, workflow, action, goal

The rule: use the word the model has read most often for the thing you mean. When two traditions
offer a word, pick the one that matches what the reader is doing. Mint a new word only when
nothing existing fits, and make it decompress on sight.

Gas Town did the opposite, which makes it a handy checklist. This file settles the words MOOLLM
uses for work, now implemented in [skills/task/](../../skills/task/) and
[skills/workflow/](../../skills/workflow/).

## The settled vocabulary

| Word | Means | Lives in | Where the word comes from |
|---|---|---|---|
| **task** | Durable work with a `done_when` guard; days to weeks | [task](../../skills/task/) | Every to-do list and tracker; GitHub calls it an issue |
| **action** | One entry in a character's queue; seconds to minutes | [action-queue](../../skills/action-queue/) | The Sims |
| **goal** | A state to reach, with `done_when`; nobody claims it. A task is a claimed goal | [goal](../../skills/goal/) | Minsky (a difference to reduce), every game |
| **workflow** | A reusable procedure that spawns tasks | [workflow](../../skills/workflow/) | CI, GitHub Actions; Papert's *procedure* |
| **plan** | A living decomposition, not yet worth reusing | [planning](../../skills/planning/) | Everyday |
| **playbook** | A task with numbered steps for one PR, ladled from a cauldron | [cauldron](../../skills/cauldron/) | Ops runbooks, sports |
| **owner** | Who claimed a task | task `owner:` | Everyday; GitHub says assignee |
| **frontier** | What's ready now, computed from guards | task FRONTIER, cauldron TREE | Tech trees |
| **ledger** | Append-only history | task `history:`, `COMPLETED.yml` | Bookkeeping |
| **buff** | A status effect with a clock, on any host | [buff](../../skills/buff/) | MMOs, The Sims moodlets |
| **advertisement** | An object bidding to be chosen | [advertisement](../../skills/advertisement/) | The Sims |

### Why task and not action or goal

"Action" is the obvious Sims word, but in The Sims, in [advertisement](../../skills/advertisement/)
and in [action-queue](../../skills/action-queue/) an action is a short runtime step in one
worker's queue. The useful distinction is durable versus runtime. A task is "fix the auth bug".
The actions under it are "open the file", "run the test", "commit". One word each.

"Goal" is closer: it has the condition, the dependencies and the hierarchy. What it lacks is a
claimant. A goal is a state somebody wants and nobody owns; a task is a goal somebody has
claimed. So [task](../../skills/task/) inherits [goal](../../skills/goal/), both spell the
condition `done_when`, and the three words are three lifetimes: the goal holds until the world
changes, the task until someone proves it done, the action until it runs.

### Why owner and not slot

"Slot" was suggested for Gas Town's "hook" because Self calls every field a slot. True, but that
makes it too general: every field is a slot, so the word tells you nothing. "Owner" says what it
holds.

### Why workflow and not procedure

Papert's "procedure" is the deeper idea, and the workflow skill credits it. But "workflow" is
what the people running these things call them, and the model has read every
`.github/workflows/*.yml` on GitHub. The step fields (`requires`, `verify`, `gate`, `fan_out`)
look like CI because that's where the model expects them.

### Why not project or milestone for a batch

"Project" is too big and too vague. A batch of related tasks is a workflow instance when it came
from a procedure, and a GitHub milestone when it's a release. Both words already exist.

## Gas Town's words

| Gas Town | Is | MOOLLM word |
|---|---|---|
| bead | an issue ("used interchangeably", per their README) | task |
| hook, pinned bead | assignment | owner |
| GUPP | "if work is on your hook, run it" | advertisement scoring |
| molecule, protomolecule, formula | workflow, workflow template | workflow |
| convoy | batch | workflow instance, milestone |
| wisp | ephemeral task (deprecated in their own code) | scratchpad |
| polecat | worker | executor, worker |
| refinery | merge queue | merge queue |
| deacon, witness, dogs | supervisors on patrol timers | buffs on the task |
| rig | project or repo | repo |
| seance | asking a previous session what it did | [cursor-mirror](../../skills/cursor-mirror/) |
| MEOW | "Molecular Expression of Work" | nothing; delete |

The pattern: every Gas Town word is a costume on a concept with an ordinary name. The
costume costs explanation tokens every session and pulls in the wrong priors (polecats are
ferrets, molecules are chemistry, hooks are git hooks).

## The traditions MOOLLM draws from

These are where MOOLLM's other words come from, for reference. Each one brings a coherent set of
related words the model already associates with each other.

- **Minsky, Society of Mind** — agent, K-line, frame, goal. Agents are many, simple, and in one
  mind.
- **Papert, Logo** — procedure, microworld, bug (as something to learn from), turtle.
- **Kay, Smalltalk** — message, method, object.
- **Ungar and Smith, Self** — prototype, slot, clone, delegation, parent.
- **Wright, The Sims** — motive, advertisement, action, queue, autonomy, routing slot.
- **LambdaMOO and MUDs** — room, exit, verb, property, object, wizard.
- **GitHub** — issue, assignee, label, milestone, workflow, pull request, review.

When MOOLLM needs a word for work, it takes it from GitHub if the reader is doing software
delivery, and from the Sims if the reader is playing. Usually both are available, and the files
can carry both: a task can SYNC to a GitHub issue and still advertise to a Sim.
