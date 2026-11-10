# Skill survey: d–i

Standard: 2026-10-29, `designs/object-system/SCHEMA.md`, constitution §15–16. Pyramid is GLANCE, CARD, SKILL.md, README. Files are flat. `methods:` is a map of `{description, signature, parameters, effect, invoked_by, body}`. `advertisements:` is a map; `score_if:` on cards. `k_lines:` is a list of strings. `inherits:` is a list. `schema:` only where this skill owns a schema, in the schema-file shape (`id`, `applies_to`, `keys`). K-line level-band is the middle. Coherence domains: location, inventory, relationships (existence reciprocal, contents not), buffs, references.

## Counts

26 skill directories: data-flow, datasette, debate, debugging, design-sense, dog, economy, emacs, empathic-expressions, empathic-templates, evaluator, example-curator, exit, experiment, fictional, file-system-object, format-design, github, goal, groceries, hero-story, historical, honest-forget, image-mining, incarnation, inventory.

| Alignment | n |
|---|---|
| aligned | 0 |
| partial | 13 |
| drifted | 13 |

All 26 have GLANCE.yml, CARD.yml, and SKILL.md. README.md is missing on emacs and example-curator. No `condition:` remains on these GLANCE or CARD files. Where an advertisement entry exists it uses `score_if:`, except design-sense (`trigger` + `score_hint`), datasette and image-mining (string or list values), and emacs (a list of strings). `type:` is a list on 20 cards; one id on exit (`primitive`), goal (`primitive`), and example-curator (`worker-pattern`). design-sense, format-design, and groceries have no top-level `type:`.

Partial means the card is flat and advertisements, when present, are a map of `score` / `score_if`, but `type:` is a list and/or a schema block is still `required` / `optional` / `compiled` and/or methods omit `signature` while using `description`, `parameters`, `effect`, `invoked_by`, `output`. Drifted means the shape is still a legacy form: envelope, advertisement list or non-entries, `k_lines` map, `inherits` map, `invoke_when` as the activation list beside a broken k-line, or method fields `does` / `summary` / `customers`.

## Per skill

### data-flow — partial

Drifted keys: `type: [skill, programming, pipeline]`. State keys `room-inbox` and `room-outbox`. Pattern keys `rooms-are`, `exits-are`, `objects-are`.

Methods THROW, RECEIVE, CONNECT, PIPELINE have `description`, `parameters`, `effect`, `invoked_by`, `output` and no `signature`. Advertisements BUILD-PIPELINE and ROUTE-OBJECTS are `score` / `score_if`. No `k_lines`.

Schema candidate keys: `pattern`, `state` (`room_inbox`, `room_outbox`). SKILL.md also commands INBOX, NEXT, PEEK, STAGE, FLUSH, which the card does not copy.

Overlap with exit. data-flow `what:`:

```
Rooms as processing nodes. Exits as edges.
Objects THROWN through exits are messages.
Build Factorio-like pipelines in adventure world.
```

THROW `effect:` is `Object appears in destination room's inbox` — a location write and a contents write in one line.

### datasette — drifted

Drifted keys: `related_skills: [sqlite, cursor-mirror, schema]`. `type:` list. Advertisements are not entries:

```yaml
advertisements:
  when: ["datasette", "SQLite web", "canned queries", "crossdb"]
  load: GLANCE.yml
```

Methods SERVE, CROSSDB, CURSOR_MIRROR have `description`, `parameters`, `output`, `invoked_by` and no `effect` or `signature`. GLANCE methods are SERVE, METADATA, EXPORT_THEN_SERVE; the card has no METADATA or EXPORT_THEN_SERVE.

Schema candidate keys: none owned here. Metadata YAML (`databases` / `tables` / `queries`) is Datasette's foreign file, described in SKILL.md § Metadata. Do not reify it as a MOOLLM `schema:`.

### debate — partial

Drifted keys: `type:` list. Top-level `data-flow:` (hyphen).

```yaml
data-flow:
  description: "Debate can be part of a data flow network"
  inputs:
    - topic (from problem definition)
    - perspectives (from committee)
  outputs:
    - transcript (to evaluator)
    - decision (to action system)
```

`inherits: [adversarial-committee, roberts-rules]` is a list, on both GLANCE and CARD. Advertisements are `score` / `score_if`. Nine methods use `description`, `parameters`, `effect`, `invoked_by`, `output`, no `signature`. GLANCE method names are `CREATE_DEBATE`, `ADD_SIDE`; the card uses `CREATE-DEBATE`, `ADD-SIDE`.

Schema candidate keys: `formats` (oxford, roundtable, panel), `states: [setup, opening, main, closing, voting, complete]` on the GLANCE, and `DEBATE.yml.tmpl` / `SIDE.yml.tmpl` / `TRANSCRIPT.md.tmpl`.

### debugging — partial

Drifted keys: `type:` list. Eight methods match debate's field set (no `signature`). Advertisements FIX-BUG, INVESTIGATE-MYSTERY, SYSTEMATIC-SEARCH are `score` / `score_if`. No `k_lines`, no `invoke_when`.

Schema candidate keys: `session_states: [investigating, narrowing, fixing, verifying, resolved, abandoned]` and `strategies`. `DEBUG.yml.tmpl` is the instance file.

### design-sense — drifted

Drifted keys: `skill:` envelope (`id`, `emoji`, `tagline`, `type: ambient-socket`, `registries`). No top-level `id`. Methods use `does` and `dispatch` (`LOAD-LENSES` also `note`; `GERMINATE` also `gate`). `plugin_schema` is the alias of `schema:`. Advertisement entries use `trigger` and `score_hint`, not `score_if` and a numeric `score`.

```yaml
advertisements:
  LOAD-LENSES:
    trigger: "designing or critiquing any interactive surface (menu, HUD, gesture, dialog, sim UI)"
    score_hint: high
```

Child objects `lenses/`, `methods/`, `masters/`, `seeds/` each have GLANCE and CARD. `lenses/CARD.yml` advertisements use `offer` and `load`, not `score` / `score_if`.

Schema candidate keys: `plugin_schema.lens_or_method_file`, `plugin_schema.master_file`. SKILL.md § Authoring a plugin is the same shape in prose.

### dog — drifted

Drifted keys: `inherits` is a map, not a list. `k_lines` is a map (`activates`, `related`). `invoke_when`. `documentation`. `type:` list. Methods are `signature` plus `output` or `note`, no `description`.

```yaml
inherits:
  from: skills/animal
  gets: [PAT, FEED, OBSERVE, SNIFF, GREET, CUDDLE, VOCALIZE, FOLLOW, FLEE]
  overrides: [SNIFF, GREET, PAT]
```

GLANCE has `inherits: skills/animal` (a string). Advertisement entries are `score` / `score_if`.

Schema candidate keys: `buffs`, `special_buffs`, `loyalty`, `ontology` (`default_tags`, `species`). Buff magnitudes are restated, not an advertisement and not `skills/buff`. GLANCE keys are `PAT`, `BELLY_RUB`, `GOOD_BOY`; CARD keys are `PAT-success`, `BELLY-RUB-success`, `GOOD-BOY-success`. GLANCE `unconditional_love` vs CARD `unconditional-love`.

`related` inside `k_lines` points at `buff` with `relation: "interactions grant buffs"`.

### economy — partial

Drifted keys: `type: [skill, game, trade]`. Methods BUY, SELL, TRADE, BALANCE, PRICE, CONVERT have `description`, `parameters`, `effect`, `invoked_by`, `output` (CONVERT also `note`), no `signature`. Advertisements MAKE-PURCHASE and SELL-ITEM are `score` / `score_if`. No `k_lines`.

Schema candidate keys: `currencies`, `parallel_currencies`, `moolah_conversions`, `defaults`. A currency is closer to a fungible inventory item than to a new schema; see inventory.

### emacs — drifted

Drifted keys: `advertisements` is a list of three strings. Methods use `summary` (ACTIVATE, EVAL, INTENT, STRUCTURAL, RAW_ELISP, ONESHOT, MACRO, SPEAK, TARGET, URL). `state_schema` is the alias of `schema:`. `type:` list. No README.

```yaml
advertisements:
  - "Persistent structured editing beats unique-string replace"
  - "emacs:// URLs address buffer + structure for LLM round-trips"
  - "Play-learn-lift: oneshots + macros + logs"
```

`what:` calls the whole environment one K-line (see K-line notes).

Schema candidate keys: `state_schema` (`daemon`, `current_target`, `open_buffers`, `modified_count`, `last_effects`). MACRO's summary says keyboard macros become schema candidates; that queue is not a schema block.

### empathic-expressions — partial

Drifted keys: `type:` list. Hyphen top-level keys `languages-supported`, `generous-interpretation`, `clarification-protocol`, `code-switching`, `llm-as-code-processor`, `used-in`. Five methods have `description`, `output`, `parameters` only. Advertisements are `score` / `score_if`.

Schema candidate keys: none. The card is a pipeline description. Pair with empathic-templates; the `what:` lines are different (see Dedup).

### empathic-templates — partial

Drifted keys: `type:` list. `anti-patterns`. Hyphen keys `template-syntax`, `front-matter-pattern`, `relationship-to-inheritance`. Four methods have `description`, `output`, `parameters` only. Advertisements are `score` / `score_if`.

Schema candidate keys: SKILL.md § Templates as Schemas says the `.tmpl` file is the schema (required / optional / computed in comments). That is the exit/goal shape, not `schema.keys`. `relationship-to-inheritance` is the inherits story under another name.

### evaluator — partial

Drifted keys: `type:` list. `adversarial-loop`. GLANCE `evaluation_schema` is not `schema:`. Four methods have `description`, `parameters`, `effect`, `invoked_by`, `output`, no `signature`. Advertisements are `score` / `score_if`.

```yaml
evaluation_schema:
  output_ref: "What was evaluated"
  rubric_ref: "Criteria used"
  scores: "Per-criterion scores"
  total_score: "Weighted sum"
  status: "[pending, approved, rejected, revision-needed]"
  critique: "Feedback if not approved"
```

`status` here is a work state. SCHEMA.md says work state is not stored; `done_when` / `fail_when` belong to goal.

### example-curator — drifted

Drifted keys: no `id`. `version: 0.1.0` (retired). `related_skills`. No `advertisements`, no `methods`, no `k_lines`. No README. `type: worker-pattern` is one id.

`process.find_patterns.methods` and `process.evolve_canonical.actions` are lists of one-key maps (`cluster_similar`, `PROMOTE`, `MERGE`, `ABSTRACT`), not the methods map. `input.timestamped_examples.location` is a directory glob, not the location domain.

Schema candidate keys: `input`, `output`, `process`. ABSTRACT says "Concrete catches → general schema" and does not define one.

### exit — partial

`type: primitive`. Flat. `inherits: [skills/prototype/]` is a list. No advertisements, no methods, no `k_lines`.

Drifted keys: `schema:` is `required` / `optional` / `computed`, with no `id` and no `keys:`. GLANCE and CARD disagree. GLANCE `compiled: [guard_js, guard_py]` and optional stops at `one_way`, `metaphysical`. CARD `computed:` is the same two fields, and optional adds `lock_message`, `note`, `hint`.

`contained_by: room` and `points_to: room`. `destination` is a reference. `one_way: true` is the non-reciprocal edge; the card does not create the return exit. That matches contents-not-reciprocal for the edge: the reverse is another exit, not a mirror of this one.

Schema candidate keys: `direction`, `destination`, `guard`, `locked`, `unlock_with`, `hidden`, `one_way`, `metaphysical`, `guard_js`, `guard_py`. This skill owns the exit schema.

### experiment — drifted

Drifted keys: `k_lines` map with `activates`, `activation_clusters`, and `related`. `invoke_when`. `type:` list. `inherits:` is a proper list (`simulation`, `evaluator`, `rubric`, `speed-of-light`), also on the GLANCE.

`activation_clusters` puts parent skills inside the K-line:

```yaml
EXPERIMENT: [simulation, evaluator, rubric, speed-of-light, character]
```

`related` entries use `ref` and `relation`, and several say `inherits —`. Inheritance is already the `inherits:` list.

Sixteen methods have `signature` and `description`; several add `activity`, `example`, `note`, `output`, `steps`. No `parameters`, `effect`, or `invoked_by`. Advertisements RUN, DEFINE, COMPARE, LIST are `score` / `score_if`.

Schema candidate keys: SKILL.md § Experiment Definition Structure. The sample is an `experiment:` envelope (`id`, `name`, `version`, `category`, `created`, `authors`) plus `character_slots`. `version` and `created` are file metadata SCHEMA.md leaves to git.

### fictional — partial

Drifted keys: `type: [skill, ontology, ethics]`. `invoke_when` duplicates the advertisement `score_if` lines. No `k_lines`. Advertisements CREATE, PLAY, TRANSFORM, CROSSOVER have `score`, `score_if`, `effect`.

Schema candidate keys: `ontology` (`is_tag`, `tag_name: fictional`, `applies_to`, `directory_mirror`), `ethics`, `combinations`. This is the tag for `status: fictional`, not a second character schema.

`what:`

```
Ontological tag for invented entities.
Created by imagination. Creator has authority.
Full creative control within ethical bounds.
```

SKILL.md world integration does not say an existence link is stored on both sides. `combinations.with_real_being` says HERO-STORY is required.

### file-system-object — drifted

Drifted keys: `k_lines:` is null. `activates:` and `related:` are siblings at the same indent, so they are top-level keys. `invoke_when`. `type:` list. Methods are `signature` + `category` (`parse`, `declare`, `validate`, `promote`, `enumerate`, `instantiate`, `lift_template`, `nest_subskill`). Advertisement prose is `what_to_do`, not `effect`. Entries also use `satisfies`, `note`, `see`.

```yaml
k_lines:
activates:
  - FILE-SYSTEM-OBJECT
  - UPPERCASE-MARKER
  ...
related:
  - { ref: skill, relation: "SKILL.md is an interface export under this grammar" }
```

`related` uses `ref` / `relation`. BRANCH-AS-OBJECT `see:` is a relative path that leaves this repo.

GLANCE.yml is 171 lines. The grammar is copied down; the glance is not the top of the pyramid.

Schema candidate keys: `naming`, `participation_levels`, `canonical_interfaces`, `skill_lookup`. SKILL.md § Skill Lookup and Inheritance Through Tree Containment treats containment as how a bare `inherits:` name resolves. Containment is not `inherits:`, and contents are not reciprocal. The 16-item `activates` list runs from the grammar down to `CURSOR-WORKSPACE-ROOTS` and `QUACK-QUACK-DUCK-TYPING` (see K-line notes).

### format-design — drifted

Drifted keys: no `id`. `version: 1.0.0`. `one_liner`. No `advertisements`, no `methods`, no `k_lines`. `protocol: FORMAT-DESIGN` sits where a k-line would.

`what:`

```
How to design formats that succeed.
Formats win through simplicity, timing, community —
not technical superiority.
```

Not a schema owner. The checklist is advice. SKILL.md § Designing for MOOLLM does not define `schema.keys`.

### github — drifted

Drifted keys: `k_lines` map (`activates`, `related` with `ref` / `relation`). Methods use `customers` (26 of them) plus `signature` and `satisfies`. Advertisement entries use `score_if` and also `customers` and `methods`. `type:` list. `inherits: [postel, robust-first, code-review]` is a list.

GLANCE `advertisements` are five strings (RUNNER-OPS, GIT-ARCHAEOLOGY, CONTEXT-GATHERING, SIMULATION-OPS, PR-REVIEW-OPS). GLANCE `k_lines` is a list, lowercase, including `delegate-to-me`. The card's `activates` list is the uppercase version of those words plus `VERSION-CONTROL`.

Schema candidate keys: none. `capabilities` restates the method names.

### goal — partial

`type: primitive`. Flat. No advertisements, no methods, no `k_lines`. `inherited_by: task` is the canonical key. `states` are marked computed, never stored. `accepts` reads `complete_when` and `research_complete_when` as `done_when`, and a stored `status:` as events. That matches SCHEMA.md.

Drifted keys: `schema:` is `required` / `optional` / `computed`, no `id`, no `keys:`. Optional includes `parent` beside `children`. CARD optional adds `fail_message`, `progress`, `location`, which the GLANCE optional list does not have. GLANCE says `compiled: [done_when_js, fail_when_js]`; CARD says `computed` and adds the `_py` siblings plus `state`.

```yaml
optional: [priority, reward, fail_when, parent, children, requires, blocks, given_by, history]
```

`parent` / `children` is the goal tree. SKILL.md also says `skills/task` inherits this skill, which is the other meaning of parent. Both are in the file; the card does not use `inherits:`.

`location` on the card schema is the location domain sitting on a goal. SKILL.md completion example writes `world.player.inventory.includes('treasure')`, which is the inventory domain inside `done_when_js`.

Schema candidate keys: `id`, `name`, `description`, `done_when`, `fail_when`, `priority`, `reward`, `requires`, `blocks`, `given_by`, `history`, `done_when_js`, `fail_when_js`. This skill owns the goal schema. `progress` is a stored fraction beside events; SKILL.md § Status Is Computed does not list it as derived.

### groceries — drifted

Drifted keys: `skill:` envelope (`name`, `version: 1.0.0`, `emoji`, `tagline`, `config_dir`, `description`). No top-level `id`. `allowed_tools` is a list. `invoke_when`. GLANCE has no `what:`; it has `use_when` and `glance:`.

Advertisements SEARCH, BONUS, MEAL-PLAN, ANALYZE, LIST-SYNC are `score` / `score_if` at the top level, outside the envelope. Methods have `description`, `parameters`, `returns` (`returns` is a standard method field); five also have `auth`. No `signature`, `effect`, or `invoked_by`. `parameters` values are type words (`string`, `enum`, `object`, `array`).

GLANCE `contents:` is the directory listing (`scripts`, `examples`, `templates`), not a container's contents. CARD `related` lists `inventory` for pantry tracking. `templates/pantry.yml.tmpl` is a personal inventory file.

### hero-story — partial

Drifted keys: `type:` list. GLANCE `hero_card_schema` is not `schema:`. Eight methods have `description`, `parameters`, `effect`, `invoked_by`, `output`, no `signature`. Advertisements are `score` / `score_if`. No `k_lines`, no `invoke_when`.

```yaml
hero_card_schema:
  name: "Card name (not person's name)"
  honors: "Who this card honors"
  tradition: "What they represent"
  invocations: "Ways to activate"
  not_for: "What NOT to use for"
```

`what:`

```
Safe K-line references to real people's traditions.
YAML-Coltrane isn't John Coltrane — it activates the
jazz improvisation tradition Coltrane represents.
```

That is the references domain: a K-line points at a tradition. It does not store the person.

### historical — partial

Drifted keys: `type:` list. `invoke_when`. `ethics.inherits_from: skills/real-being` beside `inherits: [skills/real-being]`. Advertisements HONOR, CHANNEL, TEACH, LEGACY have `score`, `score_if`, `effect`; CHANNEL also `disclosure`. No `k_lines`.

Schema candidate keys: `ontology` (`is_tag`, `tag_name: historical`, `applies_to`, `examples`). Same tag shape as fictional.

`what:`

```
Ontological tag for deceased real beings.
Extends real-being with additional considerations.
They cannot consent — extra care required.
```

GLANCE says "Extends". The card's `inherits:` list is the standard spelling of that sentence.

### honest-forget — partial

Drifted keys: `type:` list. `metadata-pattern`. GLANCE `forget_schema` is a prose blob, not `schema:`. Four methods have `description`, `parameters`, `effect`, `invoked_by`, `output`, no `signature`. Advertisements are `score` / `score_if`.

```yaml
forget_schema: |
  original-path: archive/session-42.md
  summary: "Session 42: Found the key"
  forgotten-at: 2026-01-28T14:30:00Z
  reason: "Context overflow"
```

`forgotten-at` is a timestamp SCHEMA.md would put in a sidecar or leave to git. The pointer (`original-path`) is the references domain: the summary stays, the body lives elsewhere. That is the middle of the pyramid, not a copy of the forgotten text.

### image-mining — drifted

Drifted keys: `invoke_when`. `references` (alias of `see_also`). `k_lines` map. `type:` list. Advertisements are strings:

```yaml
advertisements:
  extract_resources: "Turn pixels into structured observations"
  multi_lens: "Apply multiple analytical lenses to one image"
```

```yaml
k_lines:
  activates: [IMAGE-MINING, VISUAL-EXTRACTION, YAML-JAZZ, THIRD-EYE]
  related: [visualizer, slideshow]
```

Methods are `signature` + `output` only. CARD is 59 lines; SKILL.md is 3332. The card does not carry the protocol. GLANCE is 76 lines and lists twelve methods; the card lists five.

Schema candidate keys: `outputs`, `concepts`. EXIF fields live on the GLANCE (`exif_fields`) and are not on the card.

### incarnation — drifted

Drifted keys: `k_lines` map (`activates`, `related` with `ref` / `relation`). `invoke_when`. `documentation`. `type:` list. Eleven methods are `signature` + `output`, three also `note`. Advertisements are `score` / `score_if` (nine entries).

GLANCE `ontology` keys: `character`, `soul`, `mind`, `persona`, `ethics`, `stack`, `examples`. That is a schema of being-parts. Existence of a character is granted here; the card does not say the relation is written on both sides. `related` names `character`, `soul`, `mind`, `persona`, `society-of-mind`.

### inventory — drifted

Drifted keys: `k_lines` map (`activates`, `related` with `ref` / `relation`). `invoke_when`. `documentation`. `type:` list. Twenty-four methods are `signature` plus `note` or `modes`. Advertisements are `score` / `score_if`.

This skill owns location, inventory, and references. The card has no `schema:`.

SKILL.md § Pickup Modes, TAKE REF:

```
1. Create pointer in your inventory
2. Object stays where it is
3. Object's `location` field updates: `location: "characters/don/inventory"`
```

The object stays, and its location becomes the holder's inventory. Those two sentences cannot both be the location domain.

DROP INTO:

```
1. Target file has a list (contents, items, inventory)
2. Your item inserted into that list
3. No new file created
4. Packed storage in existing file
```

Contents are written. Location of the item is not mentioned. The sample container is an `object:` envelope:

```yaml
object:
  name: "Treasure Chest"
  contents:
    - { id: gold-coins, proto: economy/gold.yml, count: 100 }
    - ref: magic-scroll.yml
```

§ Unified Addressing says the pointer is the reference, and inventory stores it as `refs:`. A rich ref uses `condition: "good"` for wear. That spelling is the legacy advertisement/guard key.

Boxing: "When dropped, items get BOXED into YAML files with their own existence." Existence of the new file is not a reciprocal link. `k_lines.related` says rooms are implicit containers and references point to prototypes.

`what:`

```
Universal protocol for carrying, storing, transferring objects.
Applies to ANY container: characters, bags, rooms, vehicles.
Pointers (free) vs values (weight). Boxing creates identity.
```

## Dedup

Same graph sentence, two skills. data-flow `what:` "Rooms as processing nodes. Exits as edges." exit `what:` "Rooms are nodes. Exits are edges. The adventure world is a directed graph." data-flow adds "Objects THROWN through exits are messages." Keep both: exit is the edge, data-flow is the inbox on the room.

Same tag frame. fictional `what:` "Ontological tag for invented entities." historical `what:` "Ontological tag for deceased real beings." historical `what:` also says "Extends real-being with additional considerations." They share `ontology.is_tag` / `tag_name` / `applies_to`. They are different tags.

hero-story `what:` "Safe K-line references to real people's traditions." historical CARD `related` lists `skills/hero-story`. fictional `combinations.with_real_being` says "HERO-STORY required". The hero-story line is a reference to a tradition, not a tag for the being.

empathic-expressions `what:` "Intent-based code interpretation across ALL languages. One pipeline. Many syntaxes." empathic-templates `what:` "Smart templates with semantic understanding. Not string substitution — intelligent content generation." Each card's `see_also` names the other. Not the same skill. Templates claim to be the schema; expressions claim to be the compiler.

evaluator `what:` "Independent assessment without debate context. Scores output against rubric." debate `what:` "Structured multi-perspective deliberation. Oxford, roundtable, panel formats." debate `data-flow` outputs a transcript to evaluator. experiment `inherits` lists evaluator and its `what:` is "SIMULATE → EVALUATE → ITERATE → ANALYZE." Three skills, one pipeline.

groceries has no `what:`. GLANCE `glance:` is "Smart grocery shopping for Dutch supermarkets." inventory `what:` is the carrying protocol quoted above. groceries `related` lists inventory for pantry tracking. Pantry files are inventory instances, not a second inventory skill.

format-design `what:` "How to design formats that succeed." design-sense `what:` "The working designer's head as an ambient skill" and "Never tells you what colors to use." format-design `why` includes "Worse is better principle." design-sense `registries.methods` includes "worse-is-better". The `what:` lines do not match.

## K-line notes

The level-band is the middle: a K-line reopens structural names, leaves the current goal out, and leaves raw facts and tool spellings out. The file shape is a list of those names. `related` is navigation, not part of the K-line.

Map form (`activates` plus `related`, sometimes more), which stores the neighbors inside the K-line:

- dog — activates DOG, CANINE, PUPPY, PACK-DYNAMICS, LOYALTY; related is cat, buff, character, animal
- experiment — activates eight names and `activation_clusters` pulls in simulation, evaluator, rubric, speed-of-light, character, debate
- github — activates GITHUB through CONTEXT-GATHERING; related is customer skills. GLANCE list is lowercase and adds `delegate-to-me` (a goal, upper band) and `gh-cli` (a tool spelling, lower band)
- image-mining — activates IMAGE-MINING, VISUAL-EXTRACTION, YAML-JAZZ, THIRD-EYE; related is visualizer, slideshow
- incarnation — activates INCARNATION, CHARACTER-AUTONOMY, SOUL-AUTHORSHIP, MIND-AUTHORSHIP, ARCHITECTURE-AUTHORSHIP
- inventory — activates INVENTORY, TAKE, DROP, CARRY, BOXING

file-system-object: `k_lines:` parses as null. `activates` is a top-level list of 16 names from FILE-SYSTEM-OBJECT through CURSOR-WORKSPACE-ROOTS, CARD-ONLY-DISPATCH, and QUACK-QUACK-DUCK-TYPING. That is every level. `related` is already a sibling, which is where those links belong, once `ref` / `relation` are `id` / `why`.

emacs `what:` "Not a buffer tool — the whole environment is one big K-line." A K-line that is the whole environment is the case the level-band refuses.

No `k_lines` key, so the default is the id in upper dashes: data-flow, datasette, debate, debugging, design-sense, economy, emacs, empathic-expressions, empathic-templates, evaluator, example-curator, exit, fictional, format-design, goal, groceries, hero-story, historical, honest-forget. Omission is the default, not a second spelling. `invoke_when` on dog, experiment, fictional, file-system-object, historical, image-mining, incarnation, inventory, groceries is the upper band (the current goal) written as a list. Those lines already match advertisement `score_if` on the cards that have both.

## Schemas to reify

Own a schema. The block should be `schema:` with `id`, `applies_to`, and `keys` in the schema-file shape. A concentrated copy on the CARD names `canonical:` and carries no second `id`.

| Skill | Now | Keys |
|---|---|---|
| exit | `schema.required` / `optional` / `compiled` or `computed`; GLANCE and CARD disagree | direction, destination, description, short, hidden, guard, locked, lock_message, unlock_with, one_way, metaphysical, guard_js, guard_py |
| goal | same shape; `parent` in optional; `location` only on the CARD | id, name, description, done_when, fail_when, priority, reward, requires, blocks, given_by, history, done_when_js, fail_when_js, done_when_py, fail_when_py |
| inventory | no `schema:`; the protocol is the SKILL | location, refs, contents, weight; pointer vs value vs box. TAKE REF writes location onto an object that "stays where it is". DROP INTO writes contents and does not say location. `condition` on a rich ref is wear, not `score_if` |
| fictional | `ontology` | is_tag, tag_name, applies_to. Pair with `status: fictional` |
| historical | `ontology`; `ethics.inherits_from` | same tag keys. `inherits: [skills/real-being]` stays the parent list |
| hero-story | `hero_card_schema` on the GLANCE only | name, honors, tradition, invocations, not_for |
| evaluator | `evaluation_schema` on the GLANCE only | output_ref, rubric_ref, scores, total_score, critique. `status` collides with the ban on stored work status |
| emacs | `state_schema` | daemon, current_target, open_buffers, modified_count, last_effects |
| design-sense | `plugin_schema` | lens_or_method_file, master_file. Child lens cards need `score` / `score_if` before they are the same advertisement schema |
| honest-forget | `forget_schema` prose | original path, summary, reason. `forgotten-at` is a timestamp |
| experiment | `experiment:` envelope inside SKILL.md | id, name, hypothesis, scenario, character_slots. Drop version, created |
| dog | `buffs`, `loyalty`, `ontology` | buff name, magnitude, duration; loyalty range and thresholds. Do not invent a second buff schema if `skills/buff` owns the keys. GLANCE and CARD buff names disagree |
| debate | `formats`, `states`, tmpl files | format id, states. Not a second data-flow schema |
| debugging | `session_states`, DEBUG.yml.tmpl | session state names |

Do not reify: datasette metadata YAML (foreign), format-design (checklist), example-curator (worker steps), groceries (API client; pantry files are inventory), file-system-object grammar (constitution §14; `naming` can be keys later, containment is not `inherits:`), data-flow inbox (room state plus exit), economy currencies (fungible inventory).

Coherence, as these files state it:

- Location and inventory are one pointer syntax in inventory SKILL.md ("The pointer is the reference") and two writes in TAKE REF.
- Contents are a list on the container (DROP INTO). The back-link is not another contents list. The skill never says the chest is inside the cookie.
- Existence: boxing creates a file "with its own existence." That is a new object, not a reciprocal relation. fictional and historical are tags, not existence edges.
- Exit `one_way` is the non-reciprocal location edge. `destination` is a reference. `contained_by: room` is containment.
- Buffs on dog are a local table, passive PRESENCE included, keyed differently on GLANCE and CARD.
- References: inventory `refs:`, hero-story tradition pointers, honest-forget `original-path`, exit `destination`, file-system-object `related.ref`. Goal `done_when_js` reaches into `player.inventory`.
