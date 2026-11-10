# Skill survey: a–b

Judged 2026-10-29 against `designs/object-system/SCHEMA.md`, constitution §15–16, and the skill, k-lines, and coherence-engine designs.

Directories confirmed under `skills/` (skipping `archive/`):

`abstract`, `action-queue`, `adventure`, `adversarial-committee`, `advertisement`, `animal`, `artifactory`, `bartender`, `biome`, `bootstrap`, `budtender`, `buff`.

`skills/archive/` has no a–b children.

## Counts

12 skills. Alignment: 1 aligned, 7 partial, 4 drifted.

| Alignment | Skills |
|---|---|
| aligned | advertisement |
| partial | abstract, action-queue, adversarial-committee, artifactory, bartender, budtender, buff |
| drifted | adventure, animal, biome, bootstrap |

Every skill has `GLANCE.yml`, `CARD.yml`, `SKILL.md`, and `README.md`. One `CARD.yml` per object. No `ADVERTISEMENTS.yml`, `METHODS.yml`, or `K-LINES.yml` beside a card. `advertisement/ADVERTISEMENT.yml` is the schema file, not a second card. `biome/biomes/*/` are daughter objects, each with its own card.

No `skill:` or `card:` envelope on a live `CARD.yml`. The `card:` envelope appears in an animal example. No `parents:`, `extends:`, or `prototype:` used as the inheritance key on a card. No `+20` score bonus in this shard. `score_if` false bidding 0 is stated only on the advertisement schema.

`condition:` (the card alias of `score_if:`) is on 10 cards. `invoke_when:` is on abstract, animal, biome (and six daughters), and bootstrap. `k_lines:` as a map of `activates` / `related` is on adventure, bootstrap, biome, and the six daughter cards. `type:` is a list on 11 cards. advertisement is the only card with `type:` as one id plus `tags:`.

GLANCE entries that repeat a method as one line of prose are concentrated copies. They are not counted as defects. Places where the glance spelling disagrees with the card are counted.

## Per skill

### abstract

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md
- alignment: partial — advertisements are a name-keyed map, and the triggers are still `invoke_when:` plus `condition:`
- drifted keys: `type: [skill, ontology, ethics]`; `invoke_when:`; advertisement `condition:`
- schema in prose: `types:` entries (`concept`, `mascot`, `document`, `room`, `collective`) each state `description`, `examples`, `voice`. Unsure this is an instance schema. It reads as a catalog of personifications.
- overlap: none

### action-queue

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md
- alignment: partial — methods are a name-keyed map with `description`, `parameters`, `effect`, `invoked_by`; advertisements still use `condition:`; `type:` is a list; method entries omit `signature` and `body`
- drifted keys: `type: [skill, scheduling, game]`; advertisement `condition:`
- schema in prose: queue state under `state:` — `action-queue` (list), `queue-state.paused`, `queue-state.current-index`, `queue-state.mode` (`manual`, `autonomous`). Method parameters already name the step fields `action` and `target`.
- overlap: none. GLANCE says a claimed task pushes its next step here. That is a handoff, not the same job as task.
- unsure: `object-hooks:` (`on-action-blocked`, `on-resource-needed`) sits beside `advertisements:` as another way objects offer behavior

### adventure

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md, plus protocol docs (`SUMMON-PROTOCOL.md`, `PSIBER-PROTOCOL.md`, `ADVENTURE.yml.tmpl`, and others). One card.
- alignment: drifted — `k_lines` is a map, two advertisements are bare strings, and method entries are `{signature}` only
- drifted keys: `type: [skill, game, simulation, narrative]`; `k_lines: { activates, related }` with `related: [room, character, inventory, party, simulation]`; advertisements `start_or_resume: "Start or resume an adventure session"` and `codebase_archaeology: "Explore a codebase as a dungeon"`; remaining ads use `condition:`; method names `PSIBER_ENTER`, `PSIBER_EXIT`; `EXPORT.md` example `prototype: moollm://github/SimHacker/moollm/skills/no-ai-overlord/archetypes/doctor-no.yml`
- schema in prose: `ADVENTURE.yml.tmpl` states `simulation.turn`, `simulation.paused`, `parameters.time.advancement`, `parameters.git`, `parameters.display`, `parameters.debug`. The template says these are simulation properties. Unsure the owner is adventure rather than simulation. Room and character keys in the card belong to those skills. `characters_cache.tracks: [location, party, doing, mood, goals]` is a lookup cache, not a second coherence engine.
- overlap: none
- `inherits: [simulation]` is the canonical key. `MOOST-MULTIPLAYER.md` `inherits:` is a list of file paths in an example, not a card envelope.

### adversarial-committee

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md, SELECTION.md
- alignment: partial — methods are a name-keyed map with `description`, `parameters`, `effect`, `invoked_by`; advertisements use `condition:`; `type:` is a list; entries omit `signature` and `body`
- drifted keys: `type: [skill, decision, ensemble, debate]`; advertisement `condition:`
- schema in prose: committee instance under `state.committee` (`name`, `purpose`, `members`, `protocol`) and `state.session` (`status`, `current-motion`, `votes`, `transcript`) plus `decisions`. Roster members state `propensity`, `surfaces`, `voice`.
- overlap: none inside this shard. See Dedup for debate.

### advertisement

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md, ADVERTISEMENT.yml (`schema.id: advertisement`)
- alignment: aligned — flat card, `type: skill` with `tags:`, advertisements use `score_if` and `method`, methods are a name-keyed map with `description`, `parameters`, `effect`, and the card's `schema:` is a concentrated copy (`canonical: ADVERTISEMENT.yml#schema`, no `id`)
- drifted keys: none on the card. `condition`, `params`, `score_hint`, and the other old spellings live under `schema.aliases`, which is where old spellings belong. GLANCE repeats the key list as `ad_schema:` rather than `schema:`.
- schema in prose: already reified. `ADVERTISEMENT.yml` `score_if` says a false condition bids 0 and the advertisement stays available. No `+20`.
- method entries omit `signature`, `invoked_by`, and `body`
- unsure: the card has `name: ADVERTISEMENT` and no `id:`
- overlap: none

### animal

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md
- alignment: drifted — inheritance is `inherits_from`, triggers are `invoke_when:`, and the species-creation example wraps a card in `card:`
- drifted keys: `type: [skill, character, base]`; `invoke_when:`; advertisement `condition:`; `inherits_from: null`; SKILL.md example `card:` / `inherits_from: [skills/animal]`
- the parental example is also the legacy value-map form:

```yaml
inherits:
  from_species: skills/cat
  from_parent: characters/stroopwafel
```

- schema in prose: none owned here. Shared behavior is advertisements (`PAT`, `FEED`, `OBSERVE`, `CALL`, `SNIFF`, `GREET`, `CUDDLE`, `VOCALIZE`, `FOLLOW`, `FLEE`) with a `dispatch:` extension. That extension is YAML Jazz on an advertisement, not a second schema.
- methods `PAT`, `FEED`, `SNIFF` have `description`, `parameters`, `output`, and omit `effect`, `signature`, `invoked_by`, `body`
- overlap: none

### artifactory

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md
- alignment: partial — methods are a name-keyed map with `description`, `parameters`, `effect`, `invoked_by`; advertisements use `condition:`; `type:` is a list
- drifted keys: `type: [skill, foundational, tool, meta]`; advertisement `condition:`
- schema in prose: `state.session-schema` states `building`, `targets`, `provenance`, `branch`, `stop_condition`. Provenance is described as author, source, reviewed_by, timestamp.
- `INSTANTIATE`'s parameter is named `prototype`. That is a parameter name, not the inheritance key `prototype:`.
- overlap: none. GLANCE calls `skills/skill` an artifactory-factory. The jobs differ: this skill builds artifacts; skill builds skills.

### bartender

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md
- alignment: partial — the card's methods are a name-keyed map with `description`, `parameters`, `effect`, `invoked_by`; advertisements use `condition:`; `type:` is a list. `inherits: []` is the canonical key.
- drifted keys: `type: [skill, role, service]`; advertisement `condition:`; `can-be-inherited-by:`
- glance/card disagree: GLANCE `methods` groups are lists, and the names use underscores (`TAKE_ORDER`, `REFUSE_SERVICE`, `OPEN_TAB`, `KNOW_REGULAR`). The card uses hyphens (`TAKE-ORDER`, `REFUSE-SERVICE`, `OPEN-TAB`, `KNOW-REGULAR`).
- schema in prose: role state `station`, `tabs` (customer_id → balance), `regulars`, `banned`, `secrets`
- overlap: none. budtender inherits this skill.

### biome

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md, `biomes/convention.yml`, `biomes/families.yml`, and six daughter objects (`aws`, `azure`, `cloudflare`, `gcp`, `github`, `tailscale`), each with GLANCE.yml and CARD.yml
- alignment: drifted — `k_lines` is a map, triggers are `invoke_when:`, method entries are `{signature, category}`, and advertisements use `command:` and `satisfies:` with no `score_if`
- drifted keys: `type: [skill, meta, mother, prototype]`; `k_lines: { activates, related }` where `related` entries are `{ref, relation}` maps; `invoke_when:`; method names `instantiate`, `declare_child`, `register`, `add_bridge`, `validate`; advertisement keys `command:`, `note:`. `inherits: [skill, prototype]` is canonical. The same `k_lines` map and `invoke_when:` repeat on each daughter card. Daughter `type:` is `[skill, biome]`.
- schema in prose: `biomes/convention.yml` under `biome_convention:` (not `schema:`). Keys: `inheritance.declared_in`, `core_files`, `required_subdirs`, and:

```yaml
required_card_fields:
  - card.id
  - card.name
  - card.character
  - card.microworld_scope
  - card.biome
  - card.family
```

Daughter cards are flat (`id`, `name`, `character`, `family`, `biome` at the root). No daughter card contains `microworld_scope` or a `card:` envelope. The convention still spells the envelope.
- overlap: none. The skill names schemapedia as a structural ancestor. The job is platform descriptors, not schema mechanisms.

### bootstrap

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md, CONNECTIONS.md, PROBE.yml.tmpl
- alignment: drifted — `k_lines` is a map, triggers are `invoke_when:`, and method entries are `signature` plus `note` rather than `description` / `parameters` / `effect` / `invoked_by` / `body`
- drifted keys: CARD `type: [skill, meta, orientation]`; `k_lines: { activates, related }` with `related` entries `{ref, relation}`; CARD `invoke_when:`; SKILL.md frontmatter `invoke_when: "Starting a new session, feeling lost, asking 'what am I?', warming up context"`; advertisement `condition:`; method field `note:`. GLANCE `type: skill` is one id, and it disagrees with the card's list.
- GLANCE has no `what:`. Relevance is `description:`.
- schema in prose: `PROBE.yml.tmpl` roots a document at `probe:` with `timestamp`, `model` (`name`, `provider`, `context_window`), `orchestrator` (`name`, `driver`, `tier`, `hot_cold_mode`), `workspace`, `tools`. Here `orchestrator` is the IDE. It is not a second coherence engine.
- overlap: none

### budtender

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md
- alignment: partial — `inherits: [skills/bartender]` is canonical; methods are a name-keyed map with `description`, `parameters`, `effect`, `invoked_by`; advertisements use `condition:`; `type:` is a list
- drifted keys: `type: [skill, role, service, cannabis]`; advertisement `condition:`
- glance/card disagree: GLANCE `inherits: bartender` (bare name) and GLANCE method lists use underscores (`RECOMMEND_STRAIN`, `EXPLAIN_TERPENES`, `ROLL_JOINT`, `CHECK_ID`, `ASSESS_STATE`, `TALK_DOWN`, `HANDLE_WHITEOUT`, `SUGGEST_CBD`). The card uses hyphens (`RECOMMEND-STRAIN`, and the rest likewise).
- schema in prose: adds `strain_inventory`, `customer_preferences`, `session_tracking` on top of the bartender state keys. Terpene rows state `aroma` and `effect`.
- overlap: none

### buff

- files present: GLANCE.yml, CARD.yml, SKILL.md, README.md, plus design notes (`EFFECTIVE-VALUES.md`, `SELF-KORZ.md`, `CONSEQUENCE-LOOP.md`, `BUFF-IN-TIME-COMPILER.md`, `buffopedia/`). One card.
- alignment: partial — methods are a name-keyed map with `description`, `parameters`, `effect`, `invoked_by`; advertisements use `condition:`; `type:` is a list; the buff instance is described in prose and examples, not a `schema:` block
- drifted keys: `type: [skill, effects, game]`; advertisement `condition:` and `hint:`; method name `REMOVE_BY_TAG` beside hyphenated siblings (`FIND-BY-TAG`, `HAS-TAG`). SKILL.md examples wrap instances in `buff:` and an animate place in `room:`.
- schema in prose: `state.buff-schema` and the Hosts section. Keys: `name`, `host`, `hosts`, `source`, `effect`, `duration`, `expires`, `tick`, `stacks`, `max-stacks`, `polarity`, `tags`, `category`, `spawns_after`, `grants_immunity`, `start`, `start_js`, `simulate`, `simulate_js`, `is_finished`, `is_finished_js`, `cancels`, `boosts`, `replaces`, `merges_with`, `blocked_by`, `counters`, `countered_by`, `radiates`, `buff_policy.allowed_hosts`, `buff_policy.on_violation`.
- `standard-properties` (`needs`, `mind`, `combat`, `room`) are the stats a buff modifies. Unsure those tables belong to buff rather than character or needs.
- relationship hosts carry a direction (`from` / `to`) and do not equalize the other party's cell. That matches coherence: existence is reciprocal, contents are not.
- overlap: none

## Dedup

No pair in this shard has two `what:` lines that claim the same job.

Unsure, adjacent to debate (outside this shard):

- adversarial-committee: "Multiple personas with opposing propensities debate. Robert's Rules procedure. Independent evaluation. Surface blind spots through structured disagreement."
- debate: "Structured multi-perspective deliberation. Oxford, roundtable, panel formats. Cross-examination and audience voting."

Those are different procedures. Committee is a fixed roster plus Robert's Rules plus an outside evaluator. Debate is a set of formats.

action-queue and task are a handoff: the queue's GLANCE says a claimed task pushes its next step here. bartender and budtender are inheritance, not two copies of one job. artifactory and skill are constructor and skill-factory. biome names schema as an ancestor and describes platforms.

## K-line notes

Nine skills have no `k_lines` key. The directory name is the activator. Nothing in those files sits above or below the level band, because no extra names are declared.

Three cards, plus six biome daughters, store `k_lines` as `{activates, related}`. The canonical shape is a list of strings, with links in `related:`. None of the `related` values are K-REFs (`PATH[:LINE[-END]][#anchor][?search]`). Adventure's are bare ids. Bootstrap's and biome's are `{ref, relation}` maps.

Level band on the names that are declared:

- adventure `activates`: `ADVENTURE` and `TEXT-ADVENTURE` are the name. `DUNGEON-MASTER` is the role the model plays, still in the middle. `ROOM-NAVIGATION` is too low: it is one verb inside the adventure.
- bootstrap `activates`: `BOOTSTRAP` is the name. `BOOT` and `REBOOT` are aliases of that name (`aliases: [BOOT, REBOOT]` on the card). `WARM-CONTEXT` is too low: it is one step of the boot sequence. `ORIENTATION` is the same job as the name.
- biome `activates`: `BIOME` and `PLATFORM-DESCRIPTOR` are the middle. `MOTHER-SKILL`, `SISTER-SYMMETRY`, and `CROSS-BIOME-GATEWAY` are too high: they name the design claim as if saying it has already solved cross-biome exchange.
- gcp, inside biome, activates product names (`GCE`, `GKE`, `BIGQUERY`, `CLOUD-RUN`). Those wake a real product, which is the middle. Unsure about `FIREBASE-ADJACENT`: it does not name a product.

`related:` elsewhere in this shard is usually a list of `skills/...` paths (abstract, advertisement) or the job is done by `see_also:`. SCHEMA wants `related:` entries `{id, role, when, why}`. Unsure whether a path list should be rewritten now or left until `related` is migrated on its own. It is a separate question from the `k_lines` map.

## Schemas to reify

Already owned and present: advertisement (`ADVERTISEMENT.yml`, `schema.id: advertisement`). The card copy names `canonical:` and carries no `id`. Leave it.

Own a `schema:` block, keys already written in prose:

- buff — the buff entry. Keys listed under buff above. Examples should be flat slots, not a `buff:` or `room:` wrapper. `standard-properties` stays out of this schema until character or needs claims those stats. Unsure of that owner.
- biome — daughter biome, from `biome_convention`. Spell card fields flat (`id`, `name`, `character`, `family`, `biome`), matching the daughter cards. Drop `card.` and either require `microworld_scope` or stop listing it. `required_subdirs` and `inheritance.declared_in` belong in the same schema.
- action-queue — the queue. Keys: the step (`action`, `target`) and `paused`, `current-index`, `mode`.
- adversarial-committee — the committee. Keys: `name`, `purpose`, `members`, `protocol`, `status`, `current-motion`, `votes`, `transcript`, `decisions`, and roster `propensity`, `surfaces`, `voice`.
- bartender — the station. Keys: `station`, `tabs`, `regulars`, `banned`, `secrets`. budtender extends that set with `strain_inventory`, `customer_preferences`, `session_tracking`. Terpene rows (`aroma`, `effect`) can be a nested entry schema or stay data.
- bootstrap — the probe document. Keys under `probe:`: `timestamp`, `model`, `orchestrator`, `workspace`, `tools`. The template's `probe:` root can stay the document name if `schema.applies_to` says so.
- artifactory — session state. Keys: `building`, `targets`, `provenance`, `branch`, `stop_condition`.

Unsure:

- adventure `ADVENTURE.yml.tmpl` keys under `simulation:` and `parameters:`. The file says they are inherited from simulation. If simulation does not already own them, they belong there, not on adventure.
- abstract `types.*` (`description`, `examples`, `voice`). A catalog of voices, not clearly an instance schema.
