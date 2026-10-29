# The object schema

The canonical form of a MOOLLM object. Readers accept the older spellings listed at the end;
writers emit only what's on this page. Why each choice was made, and the usage counts behind
it, are in [VOCABULARY-CLUSTERS.md](VOCABULARY-CLUSTERS.md). The deterministic implementation
is [skills/prototype/scripts/resolve.py](../../skills/prototype/scripts/resolve.py); its
`lint --strict` is the enforcement.

## Objects

There are three sizes of object, and lookup treats them the same:

| Object | Address | Slots |
|---|---|---|
| directory | `examples/adventure-4/pub` | its interface files' top-level keys, merged (not its views), plus its files and subdirectories |
| file | `examples/adventure-4/maze/grue.yml` | its top-level keys |
| embedded | `garden/ROOM.yml#objects.bench` | the keys of that map |

An embedded object that grows can move into its own directory (`garden/bench/OBJECT.yml`)
without changing any lookup result.

## Files hold content

A file holds the object's content and nothing about the file. Git already records who
changed it and when, so files carry no `created:`, `updated:` or `timestamp:` about
themselves. Metadata that git can't supply goes in a sidecar named by suffix
(`wine-rack.yml`, `wine-rack-metadata.yml`), which sorts next to its subject in a directory
listing without being inside it.

Files are flat: slots at the top level. There's no envelope key repeating the filename
(`room:` inside ROOM.yml) and no generic `object:` wrapper.

## Interfaces

An UPPERCASE file is an interface: `ROOM.yml`, `CHARACTER.yml`, `RUN.yml`. Unlike a COM
vtable it holds the data that belongs to that interface, and it can see everything else in its
directory: the other interfaces, the files, the subdirectories. Those are shared; what the
interface owns goes in its file.

- **A directory has as many interfaces as it has interface files.** A talking room is a
  directory with `ROOM.yml` and `CHARACTER.yml`. Character slots don't go in ROOM.yml.
- **An interface that needs files of its own** gets a subdirectory named after it, with its
  interface file and the related files inside (`troll/stomach/STOMACH.yml`). That
  subdirectory is the slot `stomach` of the troll, an object in its own right.
- **Any other subdirectory is a child.** A sub-room is a subdirectory with its own `ROOM.yml`.
- **A data slot must not share a name with a child directory.** If the troll has a `stomach/`
  directory, CHARACTER.yml doesn't also define a `stomach:` map. It can point at it
  (`stomach: stomach/`) or leave it out. The lint reports collisions.

## Parents

```yaml
inherits:
  - skills/animal                 # repo path
  - ../characters/fictional/grue  # relative path
  - real-being                    # bare id: nearest skills/<id>, characters/<id>, ...
  - EDITH-BUNKER                  # K-line: latent, the model knows it
  - "Garfield, the comic-strip cat"   # prose: latent
  - aisle-e/PROTOTYPES.yml#prototypes.wine-rack   # an embedded object
  - { ref: skills/cat, gets: [PAT, FEED], overrides: [PAT], why: "a cat with opinions" }
  - { ref: EDITH-BUNKER, but: "Dutch, and forty years younger" }
traits*: skills/cat               # named parent: a role that can be reassigned
mood*: moods/sleepy
```

`inherits:` is a list, most specific first. Each entry is a reference string or a map with
`ref:` plus modulating clauses:

| Clause | Means | Read by |
|---|---|---|
| a comment on the line | which aspect is inherited | the LLM |
| `why:` | the same, as data | the LLM, reports |
| `gets:` / `overrides:` / `except:` | which methods come from this parent, which are redefined here, which are refused | the LLM; no script checks them yet |
| `but:` | how this object differs from a latent parent | the LLM |
| `as:` | a role name; same as writing `role*: ref` | lookup |

A reference that names no file is latent. That's legitimate for K-lines and prose; a
path-shaped reference that names no file is a broken link.

**Cross-repo references.** A parent in another repo is written
`moollm://github/<owner>/<repo>/<path>[#slot.path]`, a directory ending in `/`. The resolver
([refs.py](../../skills/prototype/scripts/refs.py)) maps it to a sibling checkout
(`<root>/<repo>/<path>`, roots from `$MOOLLM_ROOTS`, else the directory holding moollm), else to
its GitHub URL, where it is a `remote` parent: real, just not loaded. The form carries no
branch; a GitHub URL on another branch parses and loses it. Layers in different repos that
inherit from each other use this form, so a copy keeps working.

**Implied parents.** Every interface file implies the skill its name names: `ROOM.yml` implies
`room`, `RUN.yml` implies `run`. What an instance gets from the skill is the skill's
**prototype file**, a concrete object named for the interface (`skills/room/ROOM.yml`): the
defaults and methods every room has. The skill's GLANCE, CARD and README describe the skill and
are not inherited. A skill without a prototype file gives its instances nothing but its name. The skill is looked up in enclosing scopes first, so an
experiment can own a `run` skill (`experiment/skills/run/`) that its runs inherit before any
repo-wide one. If no scope defines it, the parent is the latent K-line `RUN`: the model's own
idea of a run, until somebody writes the skill. An embedded object implies the skill of its
collection key (`objects:` → `object`, `exits:` → `exit`). Implied parents come after the
declared ones, because they're the most generic.

**Lookup.** Own slots; then each declared parent in order, depth-first; then container
defaults (see Cascade); then implied parents; first match wins. A dotted slot
(`stomach.contents`) descends through maps and into child objects. A cycle is skipped and
reported. When two unrelated parents both define a slot, MOOLLM takes the first and
`lookup --all` reports it, because Self 4 would call it ambiguous.

## Layers

One being can have a layer per purpose and repo (constitution §15). Each layer states the core
keys of [skills/character/CHARACTER.yml](../../skills/character/CHARACTER.yml) `schema:` itself,
so it runs alone. Three keys relate layers:

| Key | Relation | Read by |
|---|---|---|
| `inherits:` | lookup: missing slots come from that layer | lookup |
| `derived_from:` | authoring: `[{ref, transform, copies}]`; the copied keys must agree | `resolve.py layers` |
| `layers:` | navigation: `{layer: ref or [refs]}` | readers; linted against disk |

`inherits:` never points from a public repo into a private one; a public layer may name a
private one in `derived_from:` or `layers:` by ref. Facts that disagree across layers
(consent state, public figure, life facts) go to `designs/object-system/tasks/ALIGNMENT-REVIEW.yml` for a
person to decide.

## Views

`GLANCE.yml`, `CARD.yml` and `INDEX.yml` are views: instances of a view skill, summarizing
the object that contains them. Each view has two implied named parents:

```yaml
subject*: ..       # the directory it summarizes
format*: glance    # skills/glance when it exists; the latent GLANCE until then
```

Views are not slots of the directory they summarize: a room's slots come from ROOM.yml, not
from its GLANCE. A view that lacks a slot falls through to its subject first, then to its format, so reading GLANCE, then CARD, then the
object is a delegation chain. GLANCE and CARD summarize the object; INDEX summarizes its
contents, one entry per child.

Views are concentrated, not DRY (constitution §15). A skill's CARD is the one file that says
what the skill and its objects do, so it copies down the most important slots and methods of
its prototype file: the room CARD lists LOOK, ENTER, EXIT and the keys every room has, even
though `skills/room/ROOM.yml` is canonical for instances. Fall-through covers what a view
leaves out; it is never a reason to leave out what matters at that size. A copy that
disagrees with its source is a lint finding, fixed by updating the copy. A CARD is one file:
all of a directory's interfaces feed it, and it is never split into aspect files
(`ADVERTISEMENTS.yml`, `METHODS.yml`). Its keys keep standard shapes so orchestrators can
filter and project many cards at once.

The card schema is the `schema:` section of [skills/card/CARD.yml](../../skills/card/CARD.yml).
A card names the interface files it summarizes in `interfaces:`, keyed by path, with the slots
it copies; copied methods sit in the card's `methods:` with `from: <file>`.

A view is a cache, so it can go stale. Git says when: a view is stale when anything it
summarizes has a later commit, or uncommitted changes. `resolve.py stale` lists them. Views
carry no hashes or dates.

## Embedded objects

```yaml
# garden/ROOM.yml
name: The Garden
exits:
  north: ../pub
objects:                   # map keyed by id: addressable as ROOM.yml#objects.bench
  bench:
    description: Worn oak, carved initials.
  gnome:
    inherits: [../cat]
contents:                  # a list only when order matters; each item has an id
  - { id: sign, inherits: [skills/object], text: "No grues" }
```

Collections are maps keyed by id, so a child can override one entry by name. Lists are for
order (slideshow frames, runs), and each item carries `id:`. In a mixed collection each item
says what it is with `inherits:`.

## Cascade (containers)

A `CONTAINER.yml` passes values down to everything inside it:

```yaml
defaults:
  room:
    lighting: 0      # pitch black; whether a grue hunts is the grue's call
```

`defaults:` is keyed by what the child is: its interface lowercased (`room`, `character`,
`run`), `object` for a plain file, the singular of the collection for an embedded object. A
container covers what's inside its directory, not the directory itself.

Lookup order for a slot: own slots, then declared parents (`inherits:`, `role*:`) and what they
inherit, then the defaults of enclosing containers, then implied skill parents. Defaults beat
the implied skill because the maze knows more about its rooms than the generic room skill does.
Across nested containers, maps deep-merge, lists concatenate nearest first, and the nearest
scalar wins. `resolve.py lookup` applies this; the adventure compiler doesn't yet.

## The other keys

| Concept | Key | Never |
|---|---|---|
| names that activate it | `k_lines:` list of K-LINES | parents |
| navigation links | `related:` entries `{id, role, when, why}`; `see_also:` documents | parents; `sibling_skills:`, `composes_with:` |
| intellectual ancestry | `lineage:` | parents |
| classification | `tags:`; `type:` one id | dispatch |
| behavior | `methods:` map keyed by name, each `{description, signature, parameters, effect, output, returns, invoked_by, satisfies, body}` ([skills/object/OBJECT.yml](../../skills/object/OBJECT.yml) `schema:`), UPPERCASE names are commands, lowercase are functions or protocol steps, `effect:`/`body:` compile to `_js`/`_py` inside the entry; `advertisements:` map, each with score, guard, score_if, parameters, effect, optionally the method it runs; prose keys compile to `_js`/`_py` siblings (constitution §16) | lists; other keys for offers (`reactions:`, `interests:`, `provides:`) |
| mutable state | `state:` | inherited through parents |
| finished, or impossible | `done_when:`, `fail_when:` (goal; task inherits goal) | stored as a `status:` |
| about the file | git; else a `-metadata.yml` sidecar | inside the file |
| card face | `emoji`, `tier` 0..3, `rarity`, `tagline`, `t_shirt`, `tools: {required, optional}`, `files` | `one_liner`, `allowed_tools` |
| copy-down | `interfaces:` map of file → `{role, slots, methods}` | aspect files beside a CARD |
| being's layers | `layer:` the layer's role; `type:` the being's kind; `inherits:`, `derived_from:`, `layers:` (see Layers) | `type: invitation` |

Keys the schema defines use underscores, so the key in the file is the name in code
(`k_lines:` is `world.k_lines`). Names of things (skills, rooms, files, ids) use hyphens.
Foreign schemas keep their own spelling (`allowed-tools`).

`status:` on a being states a life fact (`living`, `deceased`, `fictional`) and is allowed;
the rule against stored status is about work.

## Schema files

Each standard schema is a YAML Jazz file in the skill that owns it, read by the linters and by
models: `skills/advertisement/ADVERTISEMENT.yml`, `skills/object/OBJECT.yml` (methods),
`skills/card/CARD.yml` (card schema section), `skills/character/CHARACTER.yml`,
`skills/representation-ethics/REPRESENTATION.yml` (the `representation:` block of real-being layers). Where the file is also a prototype, the schema sits
under a top-level `schema:` key so it is not inherited as slots. Its shape:

```yaml
schema:
  id: advertisement
  applies_to: "each entry of an advertisements: map, in any object or CARD"
  extends: []                     # other schema ids whose keys this one includes
  extensions: "object-specific keys are allowed; never reuse a standard key with another meaning"
  conventions:                    # rules shared by every key unless the key says otherwise
    list_of_one: "a bare string where a list is expected is a list of one"
    any_all_not: "a list means any; { all: [...] } every; { not: [...] } none"
  keys:
    score:
      shape: number               # string | prose | number | bool | enum | ref | list | map
      range: [0, 100]             # optional; enum uses values: [...]
      of: null                    # element shape for list/map, e.g. of: ref, or of: advertisement
      default: 50                 # what an omitted key means; null means "absent, nothing happens"
      meaning: "how much the advertiser wants to be chosen, before score_if"
      compiles: false             # true for prose keys that get _js/_py siblings
      aliases: [score_hint]       # older spellings; lint reports them, migrations rewrite them
      example: 80
```

`prose` is natural language a model reads; with `compiles: true` it also gets `<key>_js` and
`<key>_py` siblings. `lookup` never returns a top-level schema block as a slot; `FILE#schema.keys` reaches it.
A linter treats a value equal to the default as removable, an alias as a
finding, and an unknown key as YAML Jazz unless it collides with an alias.

A key may be the alias of two canonical keys when the meaning depends on where it appears
(`condition:` is `guard:` in world objects and `score_if:` in CARDs); a comment on the alias
says which, and the migration decides by location. `enum` keys list `values: [...]`. The map
key of a collection entry is its `id:`; a schema that replaces a legacy list form lists the old
name field (`action:`, `name:`) as an alias of `id`.

A key whose old spellings changed values as well as names lists them in `value_aliases:`, a map
from old value to canonical value (`not_yet_asked: not_asked`); `null` means the old value carried
nothing and is dropped. A map-shaped key may give its own `keys:` in the same form. A schema may
add tables its keys refer to, such as `rules:` in REPRESENTATION.yml, where each portrayal rule
holds the `may` and `must_not` lists that are the defaults for those keys. A repo standard that
adds to a moollm schema names it in `extends:` (WillWrightShowForFood
`schemas/portrayal-standards.yml` extends `representation`). Keys inside `aliases:` and
`value_aliases:` maps are old spellings on purpose and lint does not report them.

A map- or list-shaped key whose entries have their own keys defines them with a nested `keys:`
(or `entry_keys:`) in the same form; `of: <schema id>` instead names another schema for its
entries (the card schema's `advertisements:` is `of: advertisement`). `extends:` includes
another schema's keys at the same level and is not used for entry shapes. A key may also carry
`required: true` (no default; every instance states it), `values:` with `value_meanings:`, and
`owner:` (a schema in another repo that defines its values). A dotted key
(`representation.consent.state`) names a key inside a map. A default may be computed from other
keys or from where the file is; the schema says how in prose, and the linter applies it before
treating a value as removable. Optional top-level sections: `retired:` (key → where its content
goes now) and `projection:` (the keys an orchestrator may filter on).

[schema_lint.py](../../skills/prototype/scripts/schema_lint.py) (`resolve.py lint --schema`)
discovers every `skills/*/*.yml` whose `schema:` has an `id`; a concentrated copy in a CARD
names its `canonical:` and carries no `id`.

## Accepted legacy forms

`lint --strict` counts these; the migration in
[tasks/objsys-001](tasks/objsys-001-reconcile-vocabularies.yml) removes them.

| Legacy | Canonical |
|---|---|
| `room:` in ROOM.yml, `card:`, `character:`, `object:` wrappers | flat |
| `parents:`, `parent:`, `extends:`, `prototype: <ref>`, `meta.inherits:` | `inherits:` |
| `prototype: {source: FILE, id: X}` | `inherits: [FILE#collection.X]` |
| `inherits: {key: value, ...}` (values, not parents) | plain slots, or `defaults:` on a container |
| `container.inherits:` | `defaults:` |
| `moollm/skills/x` inside moollm | `skills/x` |
| `moollm/x` or `<owner>/<repo>/x` from another repo | `moollm://github/<owner>/<repo>/x` |
| `https://github.com/<owner>/<repo>/tree/main/x` (also `blob/`, raw URLs) | `moollm://github/<owner>/<repo>/x` |
| `{repo, path, absolute_url, canonical_dir, character_url}` map | `moollm://github/<owner>/<repo>/<path>` |
| `character_ref:`, `moollm_source:`, `wwsff_local:`, `canonical_soul:`, `prototype_ref:`, `canonical_home:`, `moollm_home:` | `inherits:` |
| `upstream:` | `derived_from:` |
| `protocol:` (representation) | `representation.governed_by:` |
| `type:` naming a layer's role (`invitation`, `memorial`, `representational`) | `layer:` |
| `skill:` or `card:` wrapper in CARD.yml, `invoke_when:`, `k_lines: {activates, related}` | flat; advertisement `score_if:`; `k_lines: [list]` + `related:` |
| `k-lines:`, `klines:`, `see-also:`, `invoked-by:` | `k_lines:`, `see_also:`, `invoked_by:` |
| `complete_when:`, `research_complete_when:` | `done_when:` |
| method `does:`, `summary:`, `doc:` | `description:` |
| method `syntax:`, `call:`, `invocation:` | `signature:` |
| method `params:`, `args:`, `input:`, or a list of names | `parameters:` map |
| `customers:` | `invoked_by:` |
| `NAME: "prose"` method with sibling `methods_js:`/`methods_py:` | `NAME: { body: "prose" }`, `body_js:` inside the entry |
| `methods:` or `advertisements:` as a list | map keyed by name |

```bash
python3 skills/prototype/scripts/resolve.py lint --strict      # exit 0 when clean
python3 skills/prototype/scripts/resolve.py stale              # views older than their subjects
python3 skills/prototype/scripts/resolve.py lookup examples/adventure-4/pub exits --all
```
