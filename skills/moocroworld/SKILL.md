# Moocroworld

Each branch is an actor. Crows fly between them.

A moocroworld is a typed object stored as an orphan git branch. The repo's main branch is the "main world" with shared rooms and structure. Moocroworlds orbit outside it — independent existences paged into context on demand by mooco.

## Lineage

- **Hewitt** (1973) — Actor model: independent processes, message passing, no shared mutable state. Each moocroworld branch is an actor.
- **Kahn** — Concurrent actors in computational media. Ken Kahn's programming actors realized in git: each branch-actor receives messages (commits from any agent), processes them (file tree evolves), and can communicate with other actors (cross-references, merge actions, issue comments).
- **Papert** — Microworlds: small, complete universes to think with. Each branch is a microworld you can enter, explore, and manipulate.
- **Minsky** — K-lines, society of mind. Branch names are K-lines (activators). The repo is a society of branch-actors; behavior emerges from their interactions.

MOO (MOOLLM) + crow (intelligent agent) + microworld (Papert) = moocroworld.

## The main world and moocroworlds

A git repo has one main branch (the "main world") and any number of orphan branches (moocroworlds). They coexist in the same repo but do not share git history.

**Main branch:** Shared structure. Config, skill definitions, room layouts, navigation, indexes. Directories are rooms (see: room skill). This is the world everyone enters first.

**Moocroworlds:** Independent branches named `ClassName_ObjectID`. Each has its own file tree, its own git log, its own MOOLLM interface (GLANCE → CARD → instance data). Created when an object is born, grows as agents act on it, archived when the object is done.

The main branch may reference moocroworlds (an index file, a room with links to branches), but the moocroworld's data lives entirely on its own branch. The mooco orchestrator pages moocroworlds into context on demand — bring it in when relevant, release it when done.

## Branch naming: ClassName_ObjectID

```
Issue_abc123           # alert event
Issue_0                # prototype alert (the schema IS the example)
Definition_Motion      # alert definition
Camera_BADHOEVEDORP_1  # camera config
Character_Rocky        # adventure character
Report_2026-02-weekly  # generated report
Session_abc123         # chat session archive
```

ClassName is the type. ObjectID is the instance. `git branch --list 'ClassName_*'` lists all instances of a type. The prefix prevents collisions between object types and makes the branch list self-documenting.

## Addressing: moo:// and moollm://

A moo is a top-level typed object mounted in the local mooco VM. It can come from anywhere — a GitHub repo, a local git repo, a database, an API. Two URL schemes:

**`moo://`** — local namespace. What's mounted in the VM right now, regardless of origin. Like a Unix mount or a Python import: the agent sees `moo://Issue_0/ALERT.yml`, not the full repo path. The mount abstracts the origin.

**`moollm://`** — origin namespace. The full path to where a moo actually lives: `moollm://repo/ClassName_ObjectID/path`. Used for cross-repo references, mounting, and provenance.

```
moo://Issue_0/ALERT.yml                        ← local (mounted)
moollm://leela-alerts/Issue_0/ALERT.yml        ← origin (where it lives)

moo://Character_Rocky/CARD.yml                 ← local
moollm://moollm/Character_Rocky/CARD.yml       ← origin

moo://Camera_BADHOEVEDORP_1/GLANCE.yml         ← local
moollm://central/Camera_BADHOEVEDORP_1/GLANCE.yml ← origin
```

Mooco mounts moos into the `moo://` namespace on demand:

```
mount: moo://Issue_0      ← from moollm://leela-alerts/Issue_0
mount: moo://Issue_abc123 ← from moollm://leela-alerts/Issue_abc123
mount: moo://Character_Rocky ← from moollm://moollm/Character_Rocky
```

Once mounted, every agent addresses them the same way. The agent doesn't need to know (or care) whether the moo came from `leela-alerts` or `moollm` or a customer repo. This is the same abstraction as LambdaMOO's `#123` — a local object number that doesn't encode where the object was defined. The `moo://` scheme is the MOOLLM equivalent of `#`.

## MOOLLM interface (per moocroworld)

Every moocroworld has at minimum:

| File | Purpose |
|------|---------|
| `GLANCE.yml` | 5-line summary. Always read first. |
| `CARD.yml` | Machine-readable overview with links to everything. |
| `INSTANCE_DATA.yml` | Skill instance data, named by skill (e.g. `ALERT.yml`, `CHARACTER.yml`). ALL_CAPS convention. |

Recommended: `README.md` (human-readable narrative, auto-generated). Optional: `evidence/`, `actions/`, `analysis/`, `data/` — whatever the object type needs.

The semantic image pyramid (GLANCE → CARD → full data) works per-branch. A crow landing on a branch reads GLANCE first. If it needs more, CARD. If it needs the full state, the instance data file.

## Crows (agents)

Agents that fly between branches are called crows. They are intelligent, social, persistent, and they use tools.

| Crow type | Examples |
|-----------|---------|
| Human | Reviewer, editor, admin — acts via UI, GitHub, or CLI |
| LLM | Vision model, reviewer agent, analysis agent |
| Bot | GitHub bot, webhook handler, automation script |
| System | Alert server, orchestrator, pipeline |

A crow's lifecycle on a branch:

1. **Land** — Read GLANCE → CARD → specific files as needed.
2. **Act** — Add evidence, run analysis, approve/reject, update state.
3. **Commit** — Write changes to the branch (new files, updated GLANCE/CARD).
4. **Fly** — Move to the next branch (or return to the main world).

A crow never nests permanently on one branch. It visits, acts, and moves on.

## GitHub integration

When the repo is on GitHub, a moocroworld branch can be paired with a GitHub Issue. The issue is the conversation layer (comments, labels, notifications); the branch is the data layer (structured files, images, analysis). They complement each other:

- Issue body generated from the branch's README.md.
- Issue comments correspond to branch `actions/` entries.
- Issue labels track state (severity, review status).
- A bot watches issue comments for commands and commits to the branch.
- Webhooks sync actions between the issue and the branch in both directions.

## Applications

### Leela Alerts (first application)

Alert events stored as `Issue_` branches in `leela-ai/leela-alerts`. Each alert is a moocroworld with `ALERT.yml`, evidence (video frames, dashboards), analysis (vision/LLM, human reviewer), actions (approve, reject, escalate, resolve), and delivery log. `Issue_0` is the prototype alert — the null alert, the schema-as-example.

Design: `leela-ai/central` `apps/alerts/doc/ALERTS-NODE-POSTGRES-DESIGN.md` §13.

### Other candidates

- **Adventure characters** — each character as a `Character_` branch with their own soul file, inventory, history, mind mirror.
- **Chat sessions** — `Session_` branches archiving complete conversations with context.
- **Experiment runs** — `Experiment_` branches with parameters, results, analysis.
- **Model versions** — `Model_` branches with weights metadata, training data references, evaluation results.

## Part of MOOLLM

- Repository: https://github.com/leela-ai/moollm
- Skills index: `skills/INDEX.yml`
- Related skills: room, incarnation, mooco, adventure, object, yaml-jazz, k-lines, society-of-mind
