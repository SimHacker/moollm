# Interface files, the object model, and simulation ticks

How a MOOLLM folder says what it is, how scripts find and read such folders without understanding
their contents, how linters talk back to the LLM, and how a whole world advances one tick at a
time.

This is the MOOLLM-level convention. The orchestration side (skill compiler, script tool, hooks,
scheduler, dispatch, budgets) is in mooco's private design doc `MOOCO-SKILL-JIT-AND-SCHEDULER.md`
in the mooco repo. Related here: [DIRECTORY-AS-IUNKNOWN.md](./DIRECTORY-AS-IUNKNOWN.md),
[P-PYRAMID.md](./P-PYRAMID.md), [SKILL-SNITCH-EXTENSIBILITY.md](./SKILL-SNITCH-EXTENSIBILITY.md),
[SIMULATION-AS-SERVICE.md](./SIMULATION-AS-SERVICE.md).

Status: **design**.

## 1. Interface files: mounting a skill on a folder

A folder implements an interface by containing that interface's file:

```
characters/alice/CHARACTER.yml     # alice implements CHARACTER; this file is her CHARACTER state
characters/alice/NPC-DIALOG.yml    # and NPC-DIALOG too, with its own state
skills/character/CARD.yml          # the prototype: declares the interface
skills/character/SKILL.md          # the behaviour
```

COM and OLE, done with files. A folder may implement any number of interfaces. Each interface file
holds the state that belongs to that interface; the folder's other files and subfolders are shared
by all of them.

The skill folder is the prototype. Its `CARD.yml` declares:

```yaml
interface:
  file: CHARACTER.yml          # the file name that marks an instance; declared, never guessed
  schema: ./character.schema.json
  after: [ROOM]                # tick ordering, see §5
  methods: [describe, speak, move]
  properties: { mood: neutral, location: null }   # defaults for every instance
```

Two rules, fixed early:

- **The prototype declares the file name.** A `CHARACTER.yml` that no `CARD.yml` claims is
  ordinary data, so interface files cannot collide with data files of the same name.
- **Names map deterministically.** Upper-case interface names map to the lower-case, hyphenated
  skill names the harnesses require: `NPC-DIALOG` ↔ `npc-dialog`.

Lookup goes instance file → parent folders → prototype `CARD.yml`. That is Self's selfish
inheritance, with the path as the parent chain.

## 2. Paths are context

A path costs a few tokens and activates a lot. The names of the folders along the path carry
meaning before any file is read:

- a plural container folder names the skill that handles its contents by default:
  `characters/` → `character`, `rooms/` → `room`;
- interface file names declare membership outright;
- any name can be a k-line that pulls in other folders, files and skills.

The plural-folder-to-skill table belongs in the top-level index, so the rule is written down and
not only latent. Harnesses can enforce it natively: the compiler turns it into Claude skills'
`paths:` globs and Copilot instructions' `applyTo` globs (see the mooco doc).

## 3. The semantic pyramid index

Skill discovery is ours to define. The harness gives a flat skill list and a root file
(`AGENTS.md` or `CLAUDE.md`); everything below that is a path we lay down from the root. The index
that lays it down follows [P-PYRAMID.md](./P-PYRAMID.md):

| Level | What | Budget |
|---|---|---|
| L0 | The root `AGENTS.md`, including the folder-to-skill table | one screen |
| L1 | An `INDEX.md` per area: skills, worlds, kernel, drivers | a page |
| L2 | Per skill `CARD.yml` / `GLANCE` | a few lines each |
| L3 | `SKILL.md` | as written |
| L4 | Supporting files, scripts, examples | read on demand |

Rules:

1. **Generated, never hand-maintained.** Hand-written indexes drift from the tree.
2. **Pointers and stable keys, not copied content**, so `rg` and `yq` can query it cheaply.
3. **One source, many views.** The same tree generates a different L0 and L1 per world or
   workflow. The harness's own skill list is one of the levels, and its budget is spent on
   purpose.

## 4. The object model library

One small library, TypeScript with a thin Python twin, that every script uses instead of walking
paths itself:

| Call | Does |
|---|---|
| `objects(root, iface)` | every folder under `root` that implements `iface`, found by file name alone |
| `resolve(obj, key)` | a property, looked up instance → parent folders → prototype |
| `schema(iface)` | Dublin Core base fields plus the interface's JSON Schema from `CARD.yml` |
| `id(obj)` | a stable identifier (Dublin Core `identifier`), so references survive moves and renames |

A script written against this works on any world, any layout and any mix of repos. It needs to
know the schemas, not the meanings. Extension schemas compose: a folder implementing `CHARACTER`
and `NPC-DIALOG` validates against both.

`objects()` is Smalltalk's `allInstances`. The cheap implementation is
`rg --files -g '**/CHARACTER.yml'`; an orchestrator can keep a live index up to date with inotify.

## 5. Simulation ticks

Mounting a skill on folders means the skill can enumerate its instances and step each of them.
A tick:

| Step | Who | Deterministic |
|---|---|---|
| Enumerate | `objects(root, iface)` | yes |
| Order | a partial order from `after:` in `CARD.yml`, or read and write sets in instance files, grouped into levels whose members can run in any order | yes |
| Group | the skill's strategy: per object, per type, per room with all its characters, in batches | yes |
| Fit context | pack instance files and neighbours into a token budget | yes |
| Step | decide what happens | **no: the LLM** |
| Check | linters on the outputs, diagnostics back to the LLM (§6) | yes |
| Commit | one git commit for the tick | yes |

Only the step needs an LLM. Everything around it is ordinary scripting, which is also exactly the
Play → Learn → Lift boundary.

The grouping strategy belongs to the skill, not the engine. "Each character alone", "every
character in a room together", "all rooms in one batch" are all valid, and a skill can switch
between them.

### Rules that make ticks safe

- **Double buffering.** Steps read state as of tick N and write tick N+1. Order within a level
  stops mattering, and batches can run in parallel. The cellular-automaton discipline: CAM-6 for
  characters.
- **Each object writes only its own interface file.** Effects on other objects are messages into
  the target's mailbox (`alice/inbox/`), applied by the target on the next tick. Kay's messaging
  between objects, and two steps can never collide on one file.
- **One commit per tick.** The git history is the simulation's timeline. A branch is an alternate
  timeline.
- **A budget per tick**, in tokens and time, so a big world degrades gracefully rather than
  expensively. Enforcement is the orchestrator's job.

Where the step runs (inline, in a forked subagent, or in a separate session) is a dispatch choice
made by the skill's script per tick or per batch. See the mooco doc.

## 6. Diagnostics: the linter in a loop

Every MOOLLM linter, validator and cross-checker emits **LSP-shaped diagnostics**:

```json
{ "file": "characters/alice/CHARACTER.yml",
  "range": { "start": { "line": 12, "character": 2 }, "end": { "line": 12, "character": 9 } },
  "severity": "warning",
  "code": "MOO-CHAR-007",
  "source": "character-lint",
  "message": "location 'pub/back-room' is not a ROOM",
  "fix": { "kind": "replace", "text": "pub" } }
```

The same output feeds:

| Consumer | How |
|---|---|
| VS Code | a tiny language server, or a task with a problem matcher. Agents' existing "read errors" tools then see MOOLLM warnings with no new tool. |
| Harness hooks | after each edit, lint the file and return a compact summary as extra context. A stop hook refuses "done" while errors remain. |
| CI | SARIF from the same checks, shown on pull requests |

Keep them cheap in tokens:

- grouped by `code`, deduplicated, top N with counts;
- `moo explain <code>` prints the long explanation only when asked;
- automatic fixes are applied mechanically, so the LLM only sees what needs judgement.

This is the adventure compiler pattern generalised: a linter in a loop with an LLM that fixes
warnings, checks generated code, and reads run output.

## 7. Play → Learn → Lift, measured

Stable diagnostic codes turn crystallising into bookkeeping:

1. **Play.** The LLM handles a problem by judgement.
2. **Learn.** The same kind of fix recurs, logged against an ad hoc code or none.
3. **Lift.** Write a check for it. If the fix is deterministic, add an automatic fix too. The LLM
   never sees that case again.

Counting fixes by code says which judgements recur most, and so which to lift next. The LLM's
share of the work shrinks to what genuinely needs judgement. The checks double as tests: run them
across every world to keep worlds consistent with their prototypes.
