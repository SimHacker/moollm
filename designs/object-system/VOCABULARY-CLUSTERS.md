# Vocabulary clusters

MOOLLM's YAML grew organically. One concept often has three spellings, and one spelling
sometimes carries two concepts. This document groups the keys by the concept they express,
counts how each is actually used, names where each dialect came from, and lays out the options
for reconciling them. It is the working map for the refactor tracked in
[tasks/objsys-001-reconcile-vocabularies.yml](tasks/objsys-001-reconcile-vocabularies.yml).

Counts are top-level keys across 2,539 YAML objects outside `temp/` (an archived import), plus
the frontmatter of the 121 `skills/*/SKILL.md` files, taken on 2026-10-20. Regenerate them:

```bash
python3 skills/prototype/scripts/vocab_survey.py --examples        # every cluster
python3 skills/prototype/scripts/vocab_survey.py --cluster delegation
python3 skills/prototype/scripts/resolve.py lint --strict -v        # delegation only, with file list
```

Shapes: `path` (contains `/`), `id` (one lowercase word), `KLINE` (`ALL-CAPS-HYPHENATED`),
`prose` (anything with spaces), `url`, `map{keys}`, `list[shapes]`.

## Why there are dialects

Each cluster's vocabulary comes from a different ancestor, and the ancestors disagree:

| Ancestor | Contributed | Its word for "where missing things come from" |
|---|---|---|
| Self, JavaScript | slots, parents, clone | parent slot `parent*` |
| LambdaMOO | `location`, `contents`, verbs, player-wizards | `parent` (single) |
| The Sims | `advertisements`, scores, motives | object definition, semi-globals |
| Minsky, *K-lines* (1980) | `k-lines`, `activates` | (none; activation, not delegation) |
| OpenLaszlo `<node>`, CSS | `CONTAINER.yml`, cascade | "inherits" — values flowing *down* |
| Anthropic Agent Skills | `name`, `description`, `allowed-tools` | (none) |
| Dublin Core | `title`, `source`, `relation`, `type`, `subject` | `relation` (not inheritance) |

Reconciling is mostly deciding which ancestor owns each word. The worst collisions are where two
ancestors used the same word for opposite things (CSS's "inherits" flows down, Self's flows
up).

The dialects also survive for the reason Alan Kay gave in an email to Don about MVC: "Things
seem to hang on in computing just because they work a little bit"
([HN 7755759](https://news.ycombinator.com/item?id=7755759)). A key the LLM can read never
fails loudly, so nothing forces it out.

## Principles for every cluster

1. **One meaning per key.** A key may have several accepted spellings; a spelling may not have
   several meanings.
2. **Postel.** Readers (the resolver, the adventure compiler, the LLM) accept every spelling
   listed here. Writers emit the canonical one. Nothing breaks on the day a decision lands.
3. **The majority spelling wins unless it collides.** Usage is evidence of what reads naturally.
4. **Code that already reads a key outranks prose that mentions it.** `skills/adventure/adventure.py`
   declares `inherits: list[str]`; that settles more than any vote.
5. **Comments stay.** A comment on a parent line ("`- skills/animal  # predator instincts`") is a
   modulating clause the LLM tier reads. Structure is added only where a tool must act on it.
6. **Measured.** Every cluster that gets a decision gets a lint count that goes to zero.
7. **Facts, not verdicts.** An object states facts about itself. A judgment that depends on
   another object's concerns belongs to that other object. A room says how it is lit; the grue
   decides whether that's dark enough to hunt. Kay's "watchers" in the same email: views that
   don't affect what they view. A verdict stored on the wrong object goes stale the moment
   something else changes the facts, as when a player carries a lamp into a dark room.

## 1. Delegation: where missing slots come from

| Spelling | Uses | Shapes |
|---|---:|---|
| `inherits:` | 94 (+3 frontmatter) | 56 list[path], 21 list[id], 7 list[KLINE,path], 4 path |
| `prototype:` | 11 | 10 path, 1 wrapper map (not a parent) |
| `meta.inherits:` | 8 | list[path], all `moollm/skills/...` (skill CHARACTER.yml files) |
| `parent:` | 5 | path |
| `extends:` | 1 | id (`skills/historical`: `extends: real-being`) |
| `inherits: {from, gets, overrides}` | 2 | `skills/cat`, `skills/dog` |
| `name*:` (Self named parent) | 1 | the lookup fixture only |
| `parents:` | 0 | (the docs' word, unused in the wild) |
| `prototypes: [list]` | 0 | the prototype SKILL documents it; no object uses it |

The reference grammar inside those values has five forms, all in use:

| Form | Example | Resolves to |
|---|---|---|
| repo path | `skills/animal` | file; 233 refs resolve |
| relative path | `../characters/fictional/grue/CHARACTER.yml` | file |
| bare id | `simulation`, `real-being` | registry lookup (`skills/<id>`, `characters/<id>`) |
| K-line | `EDITH-BUNKER`, `NORM-CHEERS`, `GUINAN-TNG` | latent; the LLM knows them (12 today) |
| prose | `"Garfield, the comic-strip cat"` | latent |
| `moollm/` prefixed path | `moollm/skills/character` | file, after stripping the prefix (8) |
| URL | none yet | remote; latent until fetched |

Broken: 8 path-shaped refs name skills that don't exist (`skills/game`, `skills/turtle`,
`skills/narrator`, `skills/creature`, `skills/companion`). Each is either a skill to write or a
latent parent to respell as a K-line.

Options:

- **A. `inherits:` canonical**, everything else accepted. Matches 94 of ~120 uses and the
  compiler's dataclass. Self's vocabulary survives in named parents (`traits*:`) and in the
  docs.
- **B. `parents:` canonical**, matching Self and the prose in SELF-AND-MOOLLM. Zero current uses;
  churns ~120 files and the compiler.
- **C. Split by relationship**: `inherits:` for delegation, `prototype:` for "cloned from, then
  diverged". MOOLLM instances keep only their differences and delegate the rest, so clone and
  delegate are the same operation here; the split would encode a distinction the runtime
  doesn't make.

**Decided: A.** Modulating clauses, in order of how much structure they need:
a comment on the line; `{ref, why}`; `{ref, gets, overrides, except}` when a tool must check
which methods come from where; `{ref, but}` for latent parents ("`EDITH-BUNKER`, but Dutch and
younger"); `{ref, as}` to name a role, equivalent to `as*: ref`.

## 2. Cascade: values flowing down to contents

| Spelling | Uses | Notes |
|---|---:|---|
| `container.inherits:` | 1 | `examples/adventure-4/maze/CONTAINER.yml`; documented throughout `skills/container` |
| `defaults:` | 4 | container schema lists it beside `inherits:` with the same description |
| `ambient:` | 21 | 18 are a boolean on GLANCE (skill is always-on), 3 are sensory effects |
| `provides:` | 1 | unrelated prose list |

The collision: in `skills/container`, `inherits:` means "children get these values". Everywhere
else it means "I get my parents' slots". Same word, opposite direction. The container also
merges differently (deep-merge maps, concatenate arrays, override scalars), where delegation is
first match wins.

Options:

- **A. Rename to `defaults:`** — already in the container schema with the same meaning; one word
  fewer.
- **B. Rename to `provides:`** — says the direction; collides with nothing used structurally.
- **C. Rename to `cascade:`** — names the CSS lineage and the merge rule.

**Decided: A, `defaults:`.** The container's `defaults:` and `inherits:` sections merge into
one. Separately, `ambient:` is two concepts: the GLANCE boolean (skill loading) and the
room's sensory atmosphere. The boolean probably wants `ambient_skill: true` or to live only in
skill frontmatter.

## 3. Placement: where an object is, and what it holds

| Spelling | Uses | Shapes |
|---|---:|---|
| directory nesting | implicit, everywhere | the primary containment |
| `location:` | 123 | 84 path, 13 prose, 4 id, 3 map{address,building,street} |
| `home:` | 11 | 5 prose, 5 path, 1 id |
| `exits:` | 115 | map{direction: target} |
| `objects:` | 30 | 17 list[id], prose mixed in |
| `contents:` | 22 | map{card,skill,...} (a file listing) or list[prose] |
| `characters:` | 19 | 4 different shapes |
| `residents:` | 6 | 4 different shapes |
| `contains:` | 5 | prose, list, map |

LambdaMOO had exactly two builtins here: `location` (one object) and `contents` (a list,
maintained by the server). MOOLLM has the directory tree as the server-maintained truth, and
`location:` for things that are somewhere other than where their file lives (characters who
travel, multi-presence).

Options: keep directory nesting authoritative; `location:` a path when it can be, prose only
for real-world addresses (put those under `address:`); retire `contains`/`objects`/`residents`/
`characters` lists in favor of what the directory listing already says, or keep them as
*hints* the lint checks against the directory. `contents:` currently means a file listing in
skill ROOM.yml files, which belongs to cluster 11.

Leaning: directory is truth, `location:` path-or-`address:` (75%). Listing keys: undecided.

## 4. Activation: names that wake the object up

| Spelling | Uses | Shapes |
|---|---:|---|
| `k-lines:` | 60 | 35 map{activates,related}, 11 list[id], 6 list[KLINE] |
| `k_lines:` | 47 | 31 list[KLINE], 9 map{activates,related} |
| `klines:` | 1 | map{activates,triggered_by} |
| `when:` | 156 | 140 list[prose] (GLANCE: when to load this) |
| `invoke_when:` | 54 (+3 frontmatter) | list[prose] (CARD: same idea) |
| `use_when:`, `triggers:` | 3 | |
| `what:` / `why:` | 162 / 150 | GLANCE prose |

Two shapes compete inside `k-lines`: a flat list of names, and `{activates, related}` where
`related` duplicates cluster 5. `when:` (GLANCE) and `invoke_when:` (CARD) mean the same thing
at two pyramid levels.

Options: canonical `k_lines:` (schema keys use underscores) as a list of K-LINE
names this object answers to; move `related` out to the association cluster; keep
`when:` in GLANCE and `invoke_when:` in CARD as the same concept at two resolutions, or merge to
`when:`. Leaning `k_lines:` flat list (80%); `when:`/`invoke_when:` undecided.

## 5. Association: related, but not a parent

| Spelling | Uses | Shapes |
|---|---:|---|
| `related:` | 144 (+118 frontmatter) | 91 list[id], 10 list[KLINE], 9 list[path] |
| `see_also:` | 74 | list[id,path], prose |
| `see-also:` | 61 | 59 list[path] |
| `references:` | 38 | map{design_docs,related_examples,skill_docs} |
| `benefits_from:` | 6 frontmatter | soft dependency, part of the skill publishing policy |
| `requires:` | 3 | |

None of these delegate. `related:` is navigation (Dublin Core `relation`). `benefits_from:` is
"works better if loaded"; `requires:` is "won't work without".

Options: `related:` for skill-to-skill and object-to-object links (ids or paths, the resolver
can check both); `see_also:` for documents; `references:` folded into `see_also:`.
Leaning: two keys, `related:` and `see_also:` (70%). Spelling follows "Spelling of compound
keys" below.

## 6. Behavior: what the object can do

| Spelling | Uses | Shapes |
|---|---:|---|
| `methods:` | 259 | map{NAME: {signature, ...}}, some list[KLINE] |
| `advertisements:` | 182 | map{NAME: {...}} and list[{...}] (13), and two unrelated uses |
| `actions:` | 31 | map{VERB: ...} on rooms and objects |
| `commands:`, `operations:`, `interactions:` | 19 | |
| `protocol:` | 31 (+48 frontmatter) | 23 KLINE — the skill's own K-line name, not behavior |

`methods:` are things you can ask the object to do. `advertisements:` are Sims-style offers: a
method plus a guard and a score, so the simulation can choose among them (compiled to
`guard_js`/`score_if_js`/`effect_js` closures over `world` in `skills/adventure/adventure.js`).
`actions:` on rooms are methods by another name.

Options: `methods:` (map, canonical) and `advertisements:` (map, each entry names the method it
offers and adds guard/score); `actions:` and `commands:` read as `methods:`. Advertisements as a
list should become a map so a child can override one by name; lists can only be appended to.
`protocol:` belongs to identity (cluster 9). Leaning (75%).

## 7. Envelope: wrapping the slots in a type key

| Spelling | Uses | In |
|---|---:|---|
| `object:` | 349 | object YAML files |
| `card:` | 212 | CARD.yml (148 of them) |
| `room:` | 178 | ROOM.yml |
| `character:` | 80 | CHARACTER.yml |
| `meta:` | 202 | 20+ unrelated shapes |
| `instance:` | 11 | instances beside `prototype:` |
| `metadata:` | 35 | 28 are image-mining frame data |
| `container:` | 1 | CONTAINER.yml |

Two styles coexist: flat (GLANCE, most skill CARDs) and wrapped (`room: {name, ...}`). The
adventure engine already tolerates both (`engine.js` looks inside `object:` and `prototype:`
when a key isn't found at top level). Wrapping repeats the filename (ROOM.yml already says
"room") and pushes slots one level down, so `inherits:` at top level and slots inside
`room:` are siblings of different kinds.

Options: **A** flat everywhere, the filename is the type; **B** keep wrappers, define lookup as
"top level, then the envelope named by the file"; **C** keep wrappers only where a file holds
more than one object. **Decided: A, flat.** The wrapper does no work: 125 of 175 wrapped
ROOM.yml files have nothing else at the top level, 329 of 349 `object:` files likewise, and
where something does sit beside the wrapper, the same slot ends up at two depths across files
(`exits` inside `room:` 154 times, outside 16). Every reader already falls back to the flat
form (`data.get('room', data)`). Embedded objects and mixed collections declare what they are
with `inherits:`, so they don't need wrappers either; see [SCHEMA.md](SCHEMA.md). `meta:` needs splitting by what's in it: inheritance (cluster 1), invocation
(cluster 4), mining provenance (cluster 10).

## 8. Classification: what kind of thing this is

| Spelling | Uses | Shapes |
|---|---:|---|
| `type:` | 282 (+5) | 244 id, 35 list[id] |
| `tier:` | 276 (+110) | 212 int, 64 id (`system`, names) |
| `species:` | 106 | 75 id, 30 prose |
| `ontology:` | 72 | map{species, tags, role, nature, origin} |
| `tags:` | 20 (+115) | list[id] |
| `role:`, `nature:`, `archetype:` | 15 | |

Classification never delegates. A `type: cat` does not give the object a cat's methods; an
`inherits: [skills/cat]` does. That line has to stay sharp, because LLM readers will happily
treat a tag as a parent.

`tier:` is two things: a skill's load tier (int 0–3) and a character's tier (a name).
`ontology:` already bundles `species`, `tags`, `role`, `nature`, so top-level copies are
duplicates.

Options: `tags:` (list) for free classification, Dublin Core `subject`; `type:` one id naming the
interface (`skill`, `room`, `character`, `object`, `container`) and nothing else; `tier:` int,
skills only; character attributes inside `ontology:`. Leaning (70%).

## 9. Identity

| Spelling | Uses | Notes |
|---|---:|---|
| `name:` | 319 (+121) | 233 prose display names, 84 ids |
| `id:` | 171 | |
| `emoji:` / `emoji_identity:` | 73 / 158 nested | `emoji_identity` lives inside envelopes, never top level |
| `title:`, `aliases:`, `aka:`, `also_called:` | 14 | |

`name:` is a display name for characters and an id for skills (frontmatter requires the id).
Options: `id:` the machine name (defaults to the directory name), `name:` display, `aliases:`
the one list of other names. Leaning (80%).

## 10. Provenance: where the idea came from (not where slots come from)

| Spelling | Uses | Shapes |
|---|---:|---|
| `lineage:` | 108 (+6) | list[prose], list[{name, source}], prose |
| `sources:` | 112 | 87 list[path] (mined-image provenance) |
| `credits:` | 66 (+24) | map{inspiration, methodology}, list[prose] |
| `source:` | 53 | prose, maps from Sims imports |
| `origin:` | 21 (+9) | |
| `inspiration:` | 4 | |

`lineage:` is intellectual ancestry ("Self, OpenLaszlo, CSS"); it must never be read as
`inherits:`. The prototype skill's own GLANCE lists Ungar, Smith, Kay, Curtis, Eich and Yegge
in `lineage:` and has no `inherits:`, which is correct: it learned from them, it doesn't
delegate to them.

Options: `lineage:` (ideas, list of `{name, source}` or prose), `credits:` (people),
`sources:` (files this was made from). Map `credits` → Dublin Core `creator`/`contributor`,
`sources` → `source`. Leaning (65%).

## 11. Interface: which files make up the object

| Spelling | Uses | Notes |
|---|---:|---|
| marker files | everywhere | GLANCE.yml, CARD.yml, SKILL.md, README.md, ROOM.yml, CHARACTER.yml, CONTAINER.yml |
| `files:` | 112 | 59 list[id] — a listing |
| `interface:` / `interfaces:` | 10 | each a different meaning |
| `contents:` in skill ROOM.yml | 8 | map{card, skill, examples} |

The interface is the set of marker files present, COM QueryInterface by `ls`. That needs no
key. `files:` lists are hints for readers who can't list directories, and they drift.

Options: no interface key; the resolver reports which markers exist; `files:` kept only where
order or annotation matters, and linted against the directory. Leaning (80%).

### Views: GLANCE, CARD, INDEX are sub-objects that summarize their container

Every UPPERCASE file is an instance of the skill its name implies (`ROOM.yml` → `skills/room`).
The resolution files follow the same rule: they are *view* objects, instances of view skills
that define the level of detail and the schema for that level. What sets a view apart is its
subject: a view summarizes the object that contains it.

A view has two parents, which is what named parent slots are for:

```yaml
# implied for pub/GLANCE.yml; nothing needs to be written
format*: skills/glance     # how long, which keys, what a glance is for
subject*: ..               # the thing it summarizes: the directory that holds it
```

Lookup on a view: its own slots, then `subject*`, then `format*`. A glance that doesn't have the
answer falls through to the object it summarizes before the view skill. The reading rule "never load a lower level
without the level above" is then a delegation order: GLANCE, then CARD, then the object itself.

| View | Skill | Summarizes | Status |
|---|---|---|---|
| `GLANCE.yml` | `skills/glance` | the container, in 5–70 lines | skill doesn't exist yet; the format is described in `skills/skill/SKILL.md` |
| `CARD.yml` | `skills/card` | the container's interface: methods, advertisements | exists; already owns the "CARD.yml sidecar on any entity" pattern, alongside trading and playing cards |
| `INDEX.yml` | `skills/index` | the container's *contents*, one entry each | skill doesn't exist yet |
| `foo-metadata.yml` | `skills/summarize` | its stem sibling `foo.yml`, not its directory | exists |

`skills/summarize` is the common parent of all four: a view is a summary with a known subject.

GLANCE files are settled per subject type, not across them. Census on 2026-10-20:

| Subject | GLANCE files | Keys in ≥85% of them | Median lines |
|---|---:|---|---:|
| skill | 150 | `what`, `when`, `why`, `tier` | 49 |
| room | 100 | `name`, `type`, `description`, `exits` | 20 |
| character | 60 | `name`, `description` (and `location` 81%) | 24 |
| other | 33 | none | 38 |

Plus 15 GLANCE files that don't parse. Each subject type has a core; the rest is YAML Jazz:
whatever about this particular object helps a reader who sees only the glance decide whether to
open the CARD, the README, or the directory. So the core keys belong to the subject's skill,
not to `skills/glance`: the room skill says a room's glance carries name, type, description and
exits. `skills/glance` says what every glance is for, its line budget, and how it points deeper.
The view's two parents already give that split: `format*` (glance) and `subject*` (the room).

Consequences:

- **No second family of UPPERCASE files.** Interfaces and views use one rule; views just have a
  subject.
- **A view is a cache of its subject, so it can go stale.** Git is the record: a view is stale
  when its subject has a later commit or uncommitted changes. Views carry no hashes or dates;
  `resolve.py stale` asks git. On 2026-10-20, 315 of 639 views were older than something they
  summarize. That's commit-granular (a typo fix in SKILL.md flags its CARD), so it's a prompt
  to look, not a gate.
- **The lint can check views.** Line budgets per level, required keys per level, and that a
  view's claims (method names, exits, file lists) match its subject.
- **Two subject rules.** Container for UPPERCASE views; stem sibling for `-metadata.yml`
  sidecars. Keep both, or make sidecars `foo/GLANCE.yml` when `foo` grows into a directory.

## 12. State: what changes at runtime

`state:` (101; 16 are empty maps), `status:` (58; 23 id, 22 KLINE, 9 prose), `inventory:`,
`memory:`. The prototype rule ("state never inherits; it is always local") has no lint behind
it. Options: `state:` holds everything mutable; `status:` is one id inside it; the resolver
refuses to look up `state.*` through parents. Leaning (70%).

### Verdicts stored as facts: `grue_safe`

`grue_safe:` is on 179 ROOM.yml files (109 true, 69 false, 1 `forever`). Neither engine reads
it. It mostly restates `lighting:`: 36 rooms are `lighting: none` and unsafe, 25 are lit and
safe. Where the two disagree, the cause is somewhere else: `maze/room-h` is dark but safe
because The Thing That Watches lives there, and the grue's own CHARACTER.yml already says
"being SEEN repels it even more than light". `dim` rooms go both ways, and 77 rooms have no
`lighting:` at all. The maze's CONTAINER.yml adds `is_dark`, `light_level` and
`grue_rules.safe_with_light`, more spellings of the same question.

**Decided:** rooms state their lighting; the grue owns the predicate. Its guard reads the
room's `lighting`, any lit light source in the room or carried by someone there, and anything
present that watches. `grue_safe:` and the container's `grue_rules` go away. The room keeps
its flavour in a comment: `lighting: 6  # warm, reflected off bottles`. `lighting:` is a level
from 0 (pitch black) to 10 (full sun); the comment modulates it, as a comment modulates a
parent: `lighting: 4  # one bare bulb, swinging: 1..7, Hitchcock`. The same key on an object is
the light it gives while lit (the brass lamp is 6). A room with no `lighting:` gets it from its
container's `defaults:` (the maze says 0) or counts as lit. The grue hunts at 2 or below.
The same rule applies wherever another verdict is stored as a fact.

Done on 2026-10-20: 129 ROOM and room GLANCE files got a level (the old word kept as the
comment; `grue_safe` used as evidence to put a room on the right side of 2), `grue_safe`,
`requires_light` and `ambient_light` removed, the Eye says `watches: true`, the grue's
CHARACTER.yml holds the guard. `lighting:` maps on artwork and slideshow MINING files are a
different concept (how a picture is lit) and were left alone.

## 13. Work: goal, task, action

| Spelling | Uses | In |
|---|---:|---|
| `complete_when:` | 16 files | goal, postal letters, adventure compiler |
| `done_when:` | 17 files | task, the object-system task files |
| `research_complete_when:` | 4 files | cauldron TREE, playbook template, TECH-TREE |
| `status:` stored | goal, the January ledger | pending/active/complete/failed, hand-typed |

Three skills each grew a word for "this condition means finished", and "action" was proposed as
the name for durable work. The words separate by lifetime. A **goal** is a state someone wants;
nobody claims it, and it lasts until the world matches. A **task** is a goal someone has
claimed; it lasts until someone proves it done. An **action** is one step in one worker's
queue, minutes long, the Sims meaning and the one `advertisement` and `action-queue` already
use. **Decided:** `skills/task` `inherits: [skills/goal]` (in task's CARD.yml); the condition
key is `done_when:` everywhere, with `fail_when:` beside it; goals store events and compute
state, as tasks do. `complete_when:` and `research_complete_when:` are read as `done_when:` and
reported by `lint`. This also argues for cluster 6's leaning: `actions:` on rooms reads as
`methods:`, so "action" keeps the one meaning.

## Spelling of compound keys

The repo has `k-lines` 60 / `k_lines` 47, `see-also` 61 / `see_also` 74, `allowed-tools`
(Anthropic, fixed), `invoke_when`, `benefits_from`, `emoji_identity`. A single rule saves
re-deciding per key. Hyphens match the Anthropic frontmatter and most K-line style; underscores
are valid identifiers in JS and Python, which matters because `adventure.js` compiles slots into
`world.*` accessors and `context` uses `world.skills.<name_with_underscores>`.

Across all YAML outside `temp/`, keys with underscores occur 41,857 times (17,887 distinct) and
keys with hyphens 3,398 times (2,080 distinct). Most hyphenated keys are not schema words at
all: they are names of things used as map keys (`yaml-jazz`, `no-ai-slop`, `real-people`,
`kitten-myrcene`). The hyphenated schema words are few: `invoked-by` (294 uses, 59 files),
`k-lines` (88, 75), `see-also` (61, 61), then a tail of local vocabulary.

**Decided:**

1. **Keys the schema defines are identifiers, with underscores:** `done_when`, `k_lines`,
   `see_also`, `invoked_by`, `score_if`. The name in the file is the name in running code
   (`world.k_lines`, `done_when_js`), so one grep finds data, compiler and engine. A slot has
   one name, as in Self.
2. **Names of things are slugs, with hyphens:** skill, room, file and directory names, ids,
   used as values or as keys of maps indexed by name. Where a slug becomes an identifier (the
   skills namespace, `world.skills.action_queue`), `-` becomes `_` at that one boundary.
3. **Foreign schemas keep their own spelling.** `allowed-tools` belongs to Anthropic's
   frontmatter, as HTTP headers belong to HTTP.

`resolve.py lint` reports `k-lines`, `klines`, `see-also` and `invoked-by` (the named
renames). Other hyphenated keys are left to the census, which separates local vocabulary from
names.

## Decisions

| Question | Decision (2026-10-20) |
|---|---|
| Delegation key | `inherits:`; Self-style `name*:` for named parent roles |
| Container's downward values | `defaults:` |
| Envelopes | none: files are flat, the filename is the interface |
| Compound keys | schema keys use underscores (`k_lines`, `done_when`); names of things use hyphens; foreign schemas keep theirs |
| Interface skills | an UPPERCASE file implies its skill, found in enclosing scopes first, latent if none |
| Views | GLANCE, CARD, INDEX: `subject*` the container, then `format*` the view skill |
| File metadata | git; a `-metadata.yml` sidecar only for what git can't hold |
| Verdicts | facts on the object, judgments on the judge: rooms have `lighting:`, the grue decides; no `grue_safe:` |
| Work vocabulary | goal (wanted state) ← task (claimed goal) → actions (queued steps); `done_when:` is the one condition key |

The canonical form is written up in [SCHEMA.md](SCHEMA.md).

Still open:

1. The five broken `skills/...` parents: write those skills, or respell as K-lines?
2. Should `tier:` mean anything outside skills?
3. Placement listing keys (`objects:`, `characters:`, `residents:`, `contains:`): retire, or keep as
   hints linted against the directory?
4. `when:` (GLANCE) and `invoke_when:` (CARD): one key or two?

## Related

- [SELF-AND-MOOLLM.md](SELF-AND-MOOLLM.md): the lookup semantics these keys feed.
- [DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md](DUBLIN-CORE-AND-THE-ADVENTURE-COMPILER.md): the
  metadata vocabulary clusters 5, 8, 9 and 10 can map onto.
- [skills/prototype/scripts/resolve.py](../../skills/prototype/scripts/resolve.py): the
  deterministic lookup, `lint --strict` meter for cluster 1.
- [skills/container/](../../skills/container/): the cascade in cluster 2.
- [skills/adventure/adventure.py](../../skills/adventure/adventure.py): the compiler's
  `Object.inherits` field.
