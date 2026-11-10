# Skill survey: o–r

Shard confirmed by directory listing, 29 skills, none whose names start with s:

object, ontology, party, persona, place, plain-text, plan-then-execute, planning, play-learn-lift, postal, postel, postgres, postgres-optimization, probability, procedural-rhetoric, protocol, prototype, quora-harvest, real-being, representation-ethics, research-notebook, return-stack, reward, roberts-rules, robot, robust-first, room, rubric, runtime.

Standard: pyramid (GLANCE, CARD, SKILL, copies agree), flat slots, `methods:` map, `advertisements:` map, `k_lines:` list, `inherits:` not `parents:`, and a `schema:` block only when this skill owns a schema (SCHEMA.md "Schema files", constitution §15–16). `type:` is one id. Card `condition:` is `score_if:`. Method `does:` / `call:` / `params:` are aliases. UPPERCASE method names use hyphens (`CALL-TO-ORDER`), not underscores.

## Counts

| Check | Result |
|---|---|
| GLANCE + CARD + SKILL.md | 29/29 |
| README.md | 27/29. Missing: place, quora-harvest |
| Flat cards (no `skill:` / `card:` / `object:` envelope) | 29/29 |
| `methods:` map on the card | 21. Absent: object, ontology, plain-text, postal, real-being, robot, room, runtime |
| `methods:` list or string entries on a card | 0 |
| Advertisement map, every entry a map | 21 |
| Advertisement map, entries not advertisements | 2: representation-ethics (three strings), postgres (`when:` list, `load:` string) |
| Advertisement list | 1: place (`action` / `to` / `when`) |
| Advertisements absent | 5: object, plain-text, postal, quora-harvest, runtime |
| `condition:` left on a card advertisement | 0. `score_if:` on 65 entries. `guard:` on 0 card entries |
| `k_lines:` list | 4 files, none of them a card except by absence. place/GLANCE.yml (6), postel/CHARACTER.yml (9), procedural-rhetoric/CHARACTER.yml (9), prototype/CHARACTER.yml (10) |
| `k_lines:` map `{activates, related}` | 4 cards: protocol, quora-harvest, room, representation-ethics (`related` only) |
| `parents:` / `parent:` in non-example YAML | 0 |
| `inherits:` | object card `[skills/prototype/]`, prototype card `[{ref, why}]`, place card and glance `[]`, plus the three CHARACTER.yml files |
| `type:` one id | 3: object `primitive`, postal `infrastructure`, runtime `system` |
| `type:` a list | 25 |
| `type:` absent | 1: plain-text |
| `invoke_when:` still on the card | 6: ontology, protocol, real-being, representation-ethics, robot, room |
| `schema.id` owned here | 2: `method` (object/OBJECT.yml), `representation` (representation-ethics/REPRESENTATION.yml) |
| `schema:` present but not a schema file | object CARD and GLANCE (`required` / `optional`), prototype CARD (prose map), rubric GLANCE (field sketch). representation-ethics CARD uses `representation_schema:` and still sets `id:` |

`output:` is a string on most method entries. `output: file + chat` is the accepted joined-list spelling. Values outside the enum `chat | state-change | file` include `terminal` (postgres APPLY_DDL), `yaml` (prototype DESIGN), `DDL` (postgres-optimization VIRTUAL-COLUMN), `internal-dialogue`, `increased-intensity`, `internal-tension` (persona).

Glance method names disagree with the card in ontology, persona, postgres, postgres-optimization, protocol, return-stack, and roberts-rules.

Unparseable: room/TOPOLOGY.yml (the compass diagram breaks the literal block).

## Per skill

### object

Pyramid is complete. CARD and GLANCE are flat. The card has no `methods:` and no `advertisements:`. OBJECT.yml is the prototype: `methods: {}` and `advertisements: {}` are slots, and `schema:` under them is not a slot.

`schema.id: method` is the method schema SCHEMA.md points at. Reified there, with `shape`, `default`, `meaning`, `compiles`, `aliases`, and `example`: `description`, `signature`, `parameters` (map), `effect`, `output`, `returns`, `invoked_by`, `satisfies`, `body`, `from`. Conventions reified: map form, string form (`NAME: "prose"` means `{body}`), deprecated list form, name case, signature notation, list-of-one, joined list, compiled siblings, graduated effect keys, run order (`body_js`, else `effect_js`, else graduated keys, else the LLM). Examples reified: LOOK, consume_fuel, OPEN.

SCHEMA.md "The other keys" names the same method fields except `from`:

> `methods:` map keyed by name, each `{description, signature, parameters, effect, output, returns, invoked_by, satisfies, body}`

OBJECT.yml adds `from` as the interface file a card copied the method from, which SCHEMA.md also describes under Views ("copied methods sit in the card's `methods:` with `from: <file>`"). The card's `method_schema:` and the SKILL.md methods table both drop `from`. Those two copies otherwise match the schema: same aliases (`does`, `summary`, `doc`, `syntax`, `call`, `invocation`, `params`, `args`, `input`, `customers`, `invoked-by`) and the same case-dependent `invoked_by` default.

What is still only prose, or a block that is not a schema file:

- Instance slots (`id`, `name`, `description`, `examine`, `emoji`, `tags`, `takeable`, `container`, `locked`, `contains`, `hidden`, `disabled`, `capacity`, `simulate`, `location`, food and logistics keys) are comments on OBJECT.yml, a table in SKILL.md "Object Properties", and a different `schema:` on the card (`required` / `optional` / `computed`). There is no `schema.id: object`.
- The card's `advertisement_schema` is a second shape (`required: [description]`, optional `params`). Advertisements are owned by the advertisement schema. `params` is a method alias, not an advertisement key. SCHEMA.md's behavior row says `parameters`.
- `compile_events` on the card is a list of compiler events, not keys of the method schema.
- GLANCE `schema.compiled` is a shorter list than the card's `computed` list (`methods_js.*` versus `methods.*.body_js`).
- Simulate, resilience, and the SimCity zone pattern are SKILL.md prose. `simulate` is a prototype comment, not a schema key.

The card `inherits: [skills/prototype/]`. `type: primitive` is one id. `related:` is a list of bare ids, not `{id, role, when, why}`.

### ontology

Card is flat, `type` is a list, `invoke_when` remains. No `methods:` on the card. Glance methods are strings: TAG, CHECK_ETHICS, COMPOSE. The card's advertisements are the same three offers, with CHECK-ETHICS hyphenated, each `{score, score_if, effect, parameters}` and CHECK-ETHICS and COMPOSE also carrying a string `output`. Tag index (`tags.real-being` and the rest) is the skill's actual content. No schema block. "Most restrictive wins" is the same rule representation-ethics reifies as `conventions.most_restrictive_wins`.

### party

Card methods FORM, JOIN, LEAVE, STATUS, SPLIT, REUNITE are a map and match the glance names. Each entry has `description`, `parameters` (map), `output` (joined string), `effect`, `invoked_by`. Advertisements MANAGE-GROUP and COORDINATE-ACTIONS are `{score, score_if}`. No `k_lines`, no `inherits`, `type` is a list. No schema.

### persona

Card methods (SUMMON, DISMISS, CREATE, SOUL_CHAT, NEGOTIATE, DEFER, AMPLIFY, CONFLICT, MODULATE) and glance methods (WEAR, REMOVE, CREATE, PREVIEW, INSTANTIATE-SHELL) share only CREATE. SOUL_CHAT is underscore. Advertisements are `{score, score_if}`. `output` values include `internal-dialogue`, `increased-intensity`, `internal-tension`. No schema. The persona tree and state-machine keys are prose structure on the card, not a `schema:` block.

### place

GLANCE, CARD, SKILL.md only. No README. No PLACE.yml. Glance `files.templates/PLACE.yml.tmpl` names a file that is not in the directory.

Flat. `inherits: []` on both glance and card, with a comment showing how instances should inherit (`[coffeeshop, room, place]`). `k_lines` is a list, on the glance only: PLACE, TENANCY, SURVEY, OSM, PROVENANCE, GEDOOGLIJST. The card has no `k_lines`. Glance also has `skill: place` and `one_line`.

Methods MATCH, CLAIM, RESOLVE, OSM-RECONCILE, PROPOSE-EDIT, SURVEY are a map with `description`, sometimes `parameters`, `effect`. Advertisements are still a list:

```yaml
- { action: VISIT,   to: [rider, tourist], when: "within 200 m and open" }
- { action: SURVEY,  to: [surveyor],       when: "review.priority is high or paired" }
- { action: COUCH,   to: [tour],           when: "author is building a route" }
- { action: EXPLAIN, to: [anyone],         when: "always — the bare guard, per Korz" }
```

`action` / `to` / `when` are the legacy list spelling. The field catalog under `fields:` (address, coordinate claims, osm, tenancies, site_history, survey, review) is the place schema in prose. It is the thing a `schema.id: place` would reify. Glance states the split with room in one line: a room has exits and contents; a place has latitude.

### plain-text

Card has no `id`, no `type`, no methods, no advertisements, no `k_lines`. It has `version: 1.0.0` and `one_liner`. `protocol: PLAIN-TEXT` is a symbol, not `inherits`. Flat aside from a leading document marker. No schema.

### plan-then-execute

See the pair under Dedup. Card methods PLAN, REVIEW, APPROVE, EXECUTE, ABORT match the glance and are a map (`description`, `parameters`, string `output`, `invoked_by`; no `effect`). Advertisements SAFE-AUTOMATION and AUDIT-TRAIL are `{score, score_if}`. `type` is a list. No `k_lines`. SKILL.md frontmatter uses `allowed-tools` (foreign spelling, allowed). The plan template is wrapped in `plan:` and stores `status` and `created`.

### planning

Card methods PLAN, DECOMPOSE, PROGRESS, STATUS, REVISE match the glance. Same method shape as plan-then-execute, plus `effect`. Advertisements COMPLEX-TASK and TRACK-PROGRESS are `{score, score_if}`. Same template problems: `plan:` envelope, `status`, `created`. The SKILL.md example is a different document than PLAN.yml.tmpl (`goal` / `tasks` / `status: in_progress` versus `objective` / `steps` / `status: not_started`).

### play-learn-lift

Methods PLAY, LEARN, LIFT, STAGE match the glance. Map entries include `effect` and `invoked_by`. Advertisements START-EXPLORATION, CRYSTALLIZE-LEARNING, CREATE-SKILL are `{score, score_if}`. No `k_lines`. No schema. Stages live in `methodology` prose and CYCLE.yml.tmpl.

### postal

Messaging infrastructure. `type: infrastructure` is one id. Card has templates, endpoint types, routing, delivery, and operations, and no methods, advertisements, or `k_lines`. Not the Postel skill. No schema block; the message templates (LETTER, MESSAGE, INBOX, OUTBOX, TEXT) are the would-be schema, still templates.

### postel

Ambient. Card methods INTERPRET and CLEAN are a map and match the glance strings. Advertisements include AMBIENT plus three offers, all `{score, score_if}` (AMBIENT also has `scope`, `resolution`, `rationale`). Hyphen keys on the card: `command-parser`, `ask-if-unsure`. CHARACTER.yml has `inherits` and a `k_lines` list of nine. No `schema.id`. The principle is prose, which is what this skill is.

### postgres

Card methods CONNECT, APPLY_DDL, LIST_EXTENSIONS, INTROSPECT, DELEGATE_OPTIMIZATION. Glance methods CONNECT, EXTENSIONS, TIMESCALE, PGVECTOR, DELEGATE. Only CONNECT is shared. Names are UPPER_SNAKE. APPLY_DDL `output: terminal` is outside the enum. `related_skills:` is the legacy key; SCHEMA.md says `related:`.

Advertisements are not advertisements:

```yaml
advertisements:
  when: ["postgres", "psql", "postgres", "timescale", "pgvector", "DATABASE_URL"]
  load: GLANCE.yml
```

No schema. Connection, DDL, Timescale, and pgvector live in SKILL.md and EXTENSIONS.md. The card's own description delegates index and EXPLAIN depth to postgres-optimization.

### postgres-optimization

Card methods are hyphenated and match the glance `when:` lines: ANALYZE-QUERY, CHECK-CONSTRAINTS, LOWER-CARDINALITY, HASH-UNIQUE, CHOOSE-INDEX-TYPE, DIAGNOSE-INDEX-USAGE, plus VIRTUAL-COLUMN, COMPARE-INDEXES, EXPLAIN-INDEX-INTERNALS. The glance `methods:` map still uses underscores (ANALYZE_QUERY, …) and omits the three extra card methods. Eleven advertisements, each `{score, score_if}` only. Card `see_also` includes `skills/postgres`. Glance `related` is `[debugging, plan-then-execute]` and does not name postgres. VIRTUAL-COLUMN `output: DDL`. No schema. Techniques are prose plus INDEXES.md. SKILL.md frontmatter `inputs` / `outputs` is a second interface beside `methods`.

### probability

Methods CALCULATE and RESOLVE match the glance. Map with `effect` and `invoked_by`. One advertisement, RESOLVE-UNCERTAINTY. No `k_lines`, no schema. The no-RNG rule is prose on glance and card.

### procedural-rhetoric

Methods ANALYZE, DESIGN, CRITIQUE match the glance. Advertisements INTENTIONAL-DESIGN and UNDERSTAND-IDEOLOGY. CHARACTER.yml has `inherits` and a `k_lines` list of nine. No schema. Bogost's rule ("rules are arguments") stays prose, which is the skill.

### protocol

Card is the K-line skill and stores `k_lines` as the legacy map:

```yaml
k_lines:
  activates: [PROTOCOL, K-LINE, K-REF, SISTER-SCRIPT, SEMANTIC-ACTIVATION]
  related:
    - { ref: k-lines, relation: "naming conventions" }
```

SCHEMA.md legacy table: `k_lines: {activates, related}` becomes `k_lines: [list]` plus `related:`. `invoke_when` is still there, and the four advertisements already repeat it as `score_if`. Methods INVOKE, DEFINE, LIST, K-REF are `{signature, description}`. Glance also lists SISTER-SCRIPT as a method; the card makes it an advertisement only. `k_ref_format` is prose. No schema file. PROTOCOLS.yml is outside this directory.

### prototype

GLANCE, CARD, SKILL, README, CHARACTER.yml, and `scripts/resolve.py`. The card `inherits: [{ref: skills/schema/schemas/mechanisms/self, why: ...}]`, which is the canonical entry shape. Methods EXPLAIN, DESIGN, TRACE, LINT, COMPARE are a map; glance `when:` names the same five. DESIGN `output: yaml` is outside the enum. Advertisements are `{score, score_if}`. CHARACTER.yml `k_lines` is a list of ten. The card has no `k_lines`.

The card key `schema:` is not a schema file. It is six prose lines (`inherits`, `named_parent`, `implied_parent`, `view_parents`, `embedded`, `not_parents`, `never_inherited`) and has no `id`. SKILL.md "Declaring parents", "Lookup", "Views", "Objects", and "Older spellings" are a concentrated copy of SCHEMA.md. The parent example matches, including latent K-lines, `but:`, `gets` / `overrides` / `except`, and `traits*:`. That copy is allowed. A second `schema.id` here would split ownership with SCHEMA.md and resolve.py. `gets` / `overrides` / `except` are still unchecked by any script, as both texts say.

### quora-harvest

No README. Card `k_lines` is the legacy map (`activates` / `related`). `status: active` is a stored work status. Methods EXPAND, SNIPPET, HARVEST-PAGE, HARVEST-PROFILE, RECAP are a map. Four of them carry `call:` beside `signature:`; `call` is an alias of `signature`. `returns:` is a map of typed fields, not prose. No advertisements. No schema. The expander label list is data on the card (`expansion_labels`), a graduated key, not under `schema:`.

### real-being

Tag skill. Card says `ontology.is_tag: true`. `invoke_when` remains. No `methods:` map. SKILL.md headings PORTRAY, TRIBUTE, and IMAGINE-RESPONSE use `inputs` / `process` / `output`, not the method schema. The card advertisements of those three, plus QUOTE, are maps: `score`, `score_if`, `effect`, and extra keys `ethics`, `requirement`, `disclosure`.

The ethics block is the retired spelling:

```yaml
ethics:
  protocol: HERO-STORY
  skill_reference: skills/hero-story/
```

REPRESENTATION.yml `governed_by.value_aliases` maps `HERO-STORY` to the real-being and representation-ethics refs. This card still stores the alias as if it were the protocol. Combination rules (animal, robot, fictional) repeat ontology's composition rule in prose. No `k_lines`, no `schema:`. Portrayal facts belong on `representation:`, which this skill does not own.

### representation-ethics

Pyramid is complete, plus ETHICS.md, REPRESENTATION.yml, and examples/. The card is flat. `type` is a list. `invoke_when` remains beside advertisements that are three strings, not maps:

```yaml
advertisements:
  ethics_check: "Check consent, disclosure, and framing"
  choose_abstraction: "Pick a safer representation level"
  stack_map: "See ETHICS.md for cross-skill integration"
```

Methods CHECK and FRAME are `{signature}` only. `k_lines` is `{related: [{ref, relation}]}`.

`schema.id: representation` in REPRESENTATION.yml is the schema SCHEMA.md names ("the `representation:` block of real-being layers"). Reified, each with shape, default, and meaning: `authored_by`, `public_figure`, `consent` (nested `state`, `scope`, `date`, `evidence`, `note`), `governed_by`, `may`, `must_not`, `speaks_as`, `subject_rights` (nested `right_to_correct`, `right_to_object`, `contact`, `note`), `parody` (nested `target`, `sources`), `disclaimer`, `note`. Also reified: `conventions` (list-of-one, facts-not-verdicts, narrow-not-widen, most-restrictive-wins, life facts live on the character), `value_aliases` (`not_yet_asked` → `not_asked`, and the invitation-status spellings), `governed_by.aliases: [protocol]`, `rules` with full `may` / `must_not` lists (memorial, self_authored, consented, public_figure, private), and `retired.consent_level`.

SCHEMA.md already says the same things this file now stores. Overlaps, file against file:

Legacy table, SCHEMA.md: "`protocol:` (representation) → `representation.governed_by:`". REPRESENTATION.yml: `governed_by.aliases: [protocol]`, and `value_aliases.HERO-STORY` expands to the two `moollm://` refs. That part agrees.

SCHEMA.md schema-file rules: "A concentrated copy in a CARD names its `canonical:` and carries no `id`." The card's copy is `representation_schema:` and still has `id: representation`. It has no `canonical:`.

Consent states in the schema:

> `values: [not_asked, asked, interested, granted, declined, revoked, unverified]`

with `interested`: "wants to take part; planning the time, medium and scope. Governs nothing until granted: the rule falls through as for asked".

SKILL.md key table omits it:

> `not_asked` · `asked` · `granted` · `declined` · `revoked` · `unverified`

The card enum omits it too: `values: [not_asked, asked, granted, declined, revoked, unverified]`.

`consent.scope` default in the schema is "participate in the show, in any medium and on any timeline the subject chooses". SKILL.md says the default is none. The card says `default: null`.

`parody` is a key in the schema (public-figure rule, punch up, no private life). It does not appear in the SKILL.md key table or the card's `representation_schema.keys`.

`governed_by` shape is a list. Default is both real-being and representation-ethics. The SKILL.md example is one string, and it drops real-being:

> `governed_by: moollm://github/SimHacker/moollm/skills/representation-ethics/`

Rules' `may` and `must_not` lists are data in the schema. The card and the SKILL.md table collapse each rule to one sentence. That is a legal smaller copy only where the sentence is the rule; the lists themselves are not on the card, so a reader who stops at the card cannot apply narrow-not-widen.

Still only prose, in SKILL.md and on the glance, with no schema key: owned versus disowned self-authored personae (St. Ignucius, plannedchaos), the framing spectrum, the robot-rule emoji disclosure, distance-sets-the-license, and lotion-on-the-skin. `schema.rules.self_authored` covers "authored_by is the subject". It does not cover a persona the subject invented and then owned or disowned.

### research-notebook

Methods START, QUESTION, SOURCE, FINDING, DECIDE match the glance. Advertisement RESEARCH-SOMETHING. No `k_lines`, no schema. NOTEBOOK.yml.tmpl and SOURCES.yml.tmpl are the unimplemented schema. Card has no copy of that template's keys.

### return-stack

Card methods PUSH, POP, BACK, HISTORY, GOTO, TRACE, WHY, BLAME are a map. Glance `methods` is two lists under `navigation` and `deoptimization`, not those names. Card key `dynamic-deoptimization` is hyphenated. Advertisements are `{score, score_if}`. No schema.

### reward

Methods GRANT and GENERATE match the glance. One advertisement. Card key `reward-types` is hyphenated. No schema.

### roberts-rules

Card methods are hyphenated and match the procedure: CALL-TO-ORDER, MINUTES, MOTION, SECOND, DEBATE, CALL-QUESTION, VOTE, ADJOURN. Glance methods use CALL_TO_ORDER and CALL_QUESTION. Card key `forcing-function` is hyphenated. Advertisements STRUCTURED-DELIBERATION and PREVENT-RAILROADING. No schema. The sequence is prose; the method map is the interface.

### robot

Same tag-card shape as real-being: `invoke_when`, `ontology.is_tag`, an `ethics` prose block, advertisements IDENTIFY, ASSIST, EXECUTE, REPORT as `{score, score_if, effect}`, `combinations`, `incarnation`. No methods map, no `k_lines`, no schema. Not a duplicate of real-being. It is the other ontological tag, and ontology's card already points at both.

### robust-first

Ambient. Methods ASSESS and DEGRADE match the glance. Advertisements AMBIENT, ERROR-HANDLING, DESIGN-FOR-FAILURE. Glance has `vs_postel`. No `k_lines` on the card (the principle is the skill). No schema.

### room

ROOM.yml is the prototype every ROOM.yml implies. Slots reified as data: `type: room`, `hidden: false`, `lighting: 6`, `exits: {}`, `advertisements: {}`, and `objects: []`. SCHEMA.md says a collection is a map keyed by id. The empty list is the wrong shape, and the comment still allows embedded objects as `{id, name}` inside that list.

Methods on the prototype still use the `does:` alias:

```yaml
LOOK:      { signature: "LOOK (AT [thing])", does: "describe the room, or one thing in it" }
ENTER:     { signature: "ENTER [room]" }
EXIT:      { signature: "EXIT [direction]", does: "follow an exit; its guard decides" }
CONTENTS:  { signature: "CONTENTS", does: "list objects, stacks and who is here" }
ADVERTISE: { signature: "ADVERTISE", does: "list the actions offered by the room and everything in it" }
```

`builder_commands` uses `usage` and `does`, not `signature` and `description`. That key is not in the method schema.

The card does not copy LOOK, ENTER, EXIT, CONTENTS, ADVERTISE or the builder commands. A comment says they live in ROOM.yml. §15 says the card copies the important methods down. `k_lines` is the legacy map (`activates` plus `related`). `invoke_when` remains. Advertisements NAVIGATE, CREATE-SPACE, BUILD-WORLD, UNDERSTAND-LOCATION are `{score, score_if}`. `state.own` / `state.inherited` is a sketch of the prototype, not `schema.id: room`. Glance `related_skills` is the legacy key. TOPOLOGY.yml does not parse. ETHICS.md is venue framing, a different subject from representation-ethics, and the card points at it.

### rubric

Card methods CREATE, SCORE, EXPLAIN match the glance strings. Advertisements DEFINE-QUALITY and SCORE-OUTPUT. The card has no schema copy. Glance `schema:` is four prose lines (`name`, `criteria`, `weights`, `threshold`) and says criteria are a list of `{name, weight, levels}`. RUBRIC.yml.tmpl and the SKILL.md example disagree with that and with each other: both wrap a `rubric:` envelope, criteria are a map keyed by id with `weight`, `scale`, `anchors`, and the template adds `version`, `created`, and `thresholds.accept/reject/review`. No `schema.id: rubric`. The card, which is the resolution that should carry this, carries none of it.

### runtime

`type: system` is one id. Card describes dual Python/JavaScript targets, `world_methods`, expression types, the simulation loop, and mail delivery. No methods map, no advertisements, no `k_lines`, no schema. The golden rule (generate both `_js` and `_py`) is the same compilation rule the method schema reifies as `compiles: true`. This skill does not own that schema.

## Dedup

**planning vs plan-then-execute.** Keep both. Each skill states the split: planning's plans change as you learn; plan-then-execute freezes a sequence behind approval so tool output cannot pick the next action. Method sets share only the name PLAN, and the two PLAN entries take different parameters. Shared neighbors (action-queue, task, workflow) are related skills, not a third copy of the protocol.

What is duplicated, and wrong in both, is the plan document. Both templates open with a `plan:` envelope and store `status` and `created`. SCHEMA.md forbids the envelope and forbids `created` inside the file. Work status belongs in `done_when` / `fail_when`, not `status`. planning's SKILL.md example (`goal`, `tasks`, `in_progress`) is a third shape beside its own template (`objective`, `steps`, `not_started`). plan-then-execute's template uses `actions` and `why`, which is closer to a method list, and its SKILL.md example uses `steps` and `tool_call` instead.

**postgres vs postgres-optimization.** Keep both. postgres is connection, DDL, extensions, backup vocabulary. postgres-optimization is index and EXPLAIN technique, and both texts say so. The link is one-sided at glance level: optimization's glance `related` omits postgres, while its card `see_also` includes it. postgres's card points back via `related_skills` and DELEGATE_OPTIMIZATION. Glance and card method names inside postgres do not match each other, and postgres's `advertisements` map is a trigger word list. That is the alignment debt, not the existence of two skills.

**real-being vs representation-ethics.** Do not merge. real-being is the tag (`is_tag: true`) meaning the subject exists apart from the fiction. representation-ethics owns `schema.id: representation` and the computed rules. The overlap is the ethics block on the real-being card: `protocol: HERO-STORY`, principles, and forbidden acts that the representation rules already state as `must_not` (no invented quotes, no speaking as them, consent for intimate portrayal). HERO-STORY is a value alias of `governed_by`, not a second protocol. PORTRAY, TRIBUTE, QUOTE, and IMAGINE-RESPONSE are advertisements on the tag. CHECK and FRAME are methods on the ethics skill. A portrayal layer should carry `representation:`, not a private `ethics:` map.

**ontology, robot, real-being.** ontology is the composer ("tags, not trees", most restrictive wins). robot and real-being are two tags with the same card skeleton (`invoke_when`, `ontology`, `ethics`, advertisements, `combinations`). The skeleton is undeclared. The content is not the same.

**room vs place.** place's glance draws the line: room has exits and contents, place has latitude, and a coffeeshop inherits both. place has no prototype file, so a PLACE.yml gets nothing but the latent name. Its advertisements are the last list in the shard.

**postal vs postel.** Homophones. postal moves messages. postel is the robustness principle. Nothing in either card inherits the other.

**protocol vs prototype.** protocol activates names. prototype resolves slots. prototype's CHARACTER.yml already uses a `k_lines` list. protocol's card, which is about K-lines, still uses the map form, and its `related` entry points at the k-lines skill.

**postel vs robust-first.** Both ambient, both say how they differ (`vs_postel` on the robust-first glance). Not duplicates.

**rubric vs the method schema.** CREATE / SCORE / EXPLAIN fit the method map. The rubric document they produce does not fit any schema in this shard.

## K-line notes

The list form exists in this shard only on place's glance and on three CHARACTER.yml files (postel, procedural-rhetoric, prototype). Those lists are lowercase or mixed words (`postel`, `ungar`, `PLACE`), not the card default of the id uppercased.

Four cards use the retired map. The activators buried in `activates:` that a list would surface:

- protocol: PROTOCOL, K-LINE, K-REF, SISTER-SCRIPT, SEMANTIC-ACTIVATION
- quora-harvest: QUORA-HARVEST, EXPAND-ALL-FOLDS, RECAP-A-THREAD
- room: ROOM, SPATIAL, NAVIGATION, DIRECTORY-AS-ROOM, BUILDER-COMMANDS, ETHICAL-FRAMING

representation-ethics has no `activates`, only `related` refs (soul, mind, character, room, incarnation, hero-story, ontology, persona, mind-mirror). Those are `related:` entries sitting under `k_lines`.

Everywhere else the card omits `k_lines`. The settled card default is the id uppercased, so omission is the default, not a hole, except where a glance or a character file already published a different list (place) and the card does not carry it.

Name-case collisions that will matter once these become one list: glance methods CALL_TO_ORDER versus card CALL-TO-ORDER; ANALYZE_QUERY versus ANALYZE-QUERY; CHECK_ETHICS versus CHECK-ETHICS. A K-line and a method that differ only by `_` / `-` are two activators for one command.

## Schemas to reify

Already reified, and the copies that disagree with them:

1. **method** (`skills/object/OBJECT.yml`, `schema.id: method`). Done. Repair the copies: add `from` to the card `method_schema` and the SKILL.md table; stop calling the card's `required`/`optional` block `schema` or give the instance-slot schema its own id; point `advertisement_schema` at the advertisement schema and replace `params` with `parameters`. ROOM.yml methods should emit `description`, not `does`.

2. **representation** (`skills/representation-ethics/REPRESENTATION.yml`, `schema.id: representation`). Done. Repair the copies, do not invent a second schema: card `representation_schema` should name `canonical: representation` and carry no `id`; add `interested` and `parody` to the SKILL.md table and the card; make `consent.scope`'s default the schema's sentence in both copies; make the SKILL.md `governed_by` example a list of two refs. real-being's `ethics.protocol: HERO-STORY` should become `representation.governed_by` by lookup, not a local protocol name.

Not yet a schema file:

3. **Object instance slots.** id, name, description, examine, tags, takeable, container, locked, contains, hidden, disabled, state, simulate, capacity, inherits, location. Today they are comments plus the card's nonstandard `schema:`. `simulate` compiling to `simulate_js` / `simulate_py` is prose and a `compile_events` list.

4. **Room slots, separate from method.** lighting, exits, objects-as-map, builder_commands. The prototype file exists; it is not a `schema:` block. `objects: []` contradicts the collection rule. Builder commands need `signature` / `description` or their own entry schema. The card should copy LOOK, ENTER, EXIT, CONTENTS, ADVERTISE with `from: ROOM.yml`.

5. **Place.** The card `fields:` map (address parts, coordinate claims, osm identity, tenancies, site_history, survey, review) is the schema. It needs `schema.id: place` and a PLACE.yml prototype. Advertisements become a map keyed by VISIT, SURVEY, COUCH, EXPLAIN. Glance's missing `templates/PLACE.yml.tmpl` should be that prototype or the pointer should go away.

6. **Rubric.** One `schema.id: rubric`: criteria as a map keyed by id, weight, scale, anchors, thresholds. Drop the `rubric:` envelope, `version`, and `created`. Glance currently says criteria are a list; the template says a map. The map matches the collection rule. The card should carry the keys.

7. **Plan document**, shared by planning and plan-then-execute. One schema, two advertised modes (living versus frozen), not two envelopes. Keys: goal, steps as a map or a list-with-id, `done_when`, approval as a fact with evidence for the frozen mode. Not `status`, not `created`, not a `plan:` wrapper. Until that exists, the two templates and planning's SKILL.md example are three prose shapes.

8. **Do not reify again.** Prototype inheritance stays in SCHEMA.md and resolve.py. Protocol K-lines stay a list plus `related:`, not a new schema id. Postal message types and quora `returns:` maps can wait; they are not the object-system schemas this standard names.
