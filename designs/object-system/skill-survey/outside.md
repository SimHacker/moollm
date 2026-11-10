# Outside skills

Compared to `designs/object-system/SCHEMA.md` (2026-10-29) and to `moollm/skills` of the same name. Writers emit flat files, `inherits:` as a list (cross-repo: `moollm://github/<owner>/<repo>/<path>/`), `methods:` and `advertisements:` as maps, `k_lines:` as a list, a `schema:` block on the skill that owns a shape, and `moollm_compatible` where a repo declares compatibility. Views are GLANCE then CARD then the object. A CARD copies important slots; it does not invent a second parent.

## Skills found

| Repo | Skill | Pyramid |
|---|---|---|
| amsterdank/skills | coffeeshop | GLANCE, CARD, SKILL, plugins BUDTENDERS GHOSTS SURVEY GEOTOKING. No README. |
| MicropolisCore/skills | micropolis | GLANCE, CARD, SKILL, README |
| MicropolisCore/skills | micropolis-command-bus | GLANCE, CARD, SKILL, README |
| MicropolisCore/apps/screen-angel/skills | screen-angel | GLANCE, CARD, SKILL, README |
| WillWrightShowForFood/skills | repo-show | GLANCE, CARD, SKILL, README |
| WillWrightShowForFood/skills | ebike-safari | GLANCE, CARD, SKILL, README (all short) |

Also present, not skills: amsterdank `skills/INDEX.yml`; WillWrightShowForFood `skills/GLANCE.yml`, `skills/INDEX.yml`, `skills/README.md`, `skills/repo-show-format.yml` (pointer at `process/repo-show-format.yml`).

`RepoShow` exists and has no `skills/` directory. `SimObliterator_Suite` exists and has no `skills/` directory.

Same-name skill in `moollm/skills`: `micropolis` only. No `coffeeshop`, `screen-angel`, `repo-show`, `ebike-safari`, or `micropolis-command-bus`. `urban-safari` is the pipeline `ebike-safari` restates.

`schema:` appears in none of these six.

## Per skill

### coffeeshop

`amsterdank/skills/coffeeshop`. `moollm_compatible: true` on `skills/INDEX.yml` and on `SKILL.md` frontmatter. No prototype file.

`inherits: [room, place]` on GLANCE and CARD, bare ids. The SKILL body example is `inherits: [coffeeshop, room, place]`. INDEX `consumed` lists `place`, `room`, `budtender`, `character`, `yaml-jazz` as `https://github.com/SimHacker/moollm/tree/main/skills/...`. That URL form is a legacy spelling of `moollm://github/SimHacker/moollm/skills/<id>/`.

GLANCE opens with `skill: coffeeshop`. CARD opens with a `card:` envelope around identity, then flat `tools`, `tier`, `inherits`, `fields`, `methods`, `advertisements`. `k_lines` on GLANCE is a list: COFFEESHOP, GEDOOGLIJST, AHOJG, MENU-ONTOLOGY, BUDTENDER, TENANCY. CARD has no `k_lines`.

`methods` is a map: READ-BOARD, PROJECT, COMPARE, ASK-BUDTENDER, GEDOOG-CHECK, with `description`, `parameters`, `effect`. READ-BOARD uses `invoked-by` and a `refuses` string. `advertisements` is a list of `{action, to, when}`: VISIT, READ-BOARD, ASK-BUDTENDER, EXPLAIN.

Jurisdiction stays here: gedoog, AHOJG-I, afficheren, the board's own categories, units as sold (`gram | bag | piece | joint`), `weight_g` only when the board states it.

Inherit, and delete the restatement:

- `moollm://github/SimHacker/moollm/skills/place/` for address-as-subject, tenancy, `site_history`, survey, OSM, provenance, absence-versus-closure. GHOSTS and SURVEY re-explain those slots. GLANCE `k_lines` repeats place's TENANCY, SURVEY, GEDOOGLIJST.
- `moollm://github/SimHacker/moollm/skills/room/` for interior, contents, exits, advertisements.
- `moollm://github/SimHacker/moollm/skills/budtender/` for RECOMMEND-STRAIN and the counter role. ASK-BUDTENDER is the local method that passes this board.
- `moollm://github/SimHacker/moollm/skills/representation-ethics/` for consent. BUDTENDERS.md defines tiers 0–4 (declined, role, named, character, self-authored). `REPRESENTATION.yml` retired numeric `consent_level` and uses `consent.state` (`not_asked`, `asked`, `interested`, `granted`, `declined`, `revoked`, `unverified`), `authored_by`, `speaks_as`. The robot, the house mascot, and the pet are those keys on a character, plus `inherits: [character]`.
- `moollm://github/SimHacker/moollm/skills/character/` for the person file.
- `yaml-jazz` and `postel`, already named under `respects`.

`fields:` on the CARD is an instance schema (gedoog, status, menu, shared_vocabulary, amenities, vibe, staff) with no `schema:` id. Plugins name parents that are not skills: `item`, `purchase`, `spot`, `episode`, `assessment`, `robot-budtender`, `mascot`, `pet`.

### micropolis

`MicropolisCore/skills/micropolis`. Same name as `moollm/skills/micropolis`. No `inherits`, no `moollm_compatible`, no `methods`, no `advertisements`, no `schema`.

Both copies use a pyramid and then diverge. moollm status is `designing`; tagline "The filesystem is the city. Git is the multiverse." MicropolisCore status is `implementing`; tagline "The engine is the microworld. The CLI is the public gate."

MicropolisCore GLANCE and CARD wrap identity in nothing on GLANCE (`what`, `why`, `status`) and in `card:` on CARD. `k_lines` is a map `activates:` on both files, different lists. CARD adds `invoke_when`, `commands` (shell strings grouped introspection/city/visualize/sim/bus/content), `workflows` (step lists), `delegation`, `rules`, `formats`, `evidence`, `files`. SKILL.md frontmatter has `allowed-tools`, `related`, `protocol: MICROPOLIS-ENGINE`.

moollm's copy is also pre-schema: top-level `activates` and `invoke_when`, `related: [{ref, relation}]`, no `inherits`, no `methods` map, no `advertisements` map. Its CARD still lists the older `micropolis.js` commands (`city dump/info/export/analyze`, `visualize ascii/emoji/filtered`).

MicropolisCore should declare:

```yaml
inherits:
  - moollm://github/SimHacker/moollm/skills/micropolis/
  - moollm://github/SimHacker/moollm/skills/constructionism/
  - moollm://github/SimHacker/moollm/skills/github/
  - moollm://github/SimHacker/moollm/skills/experiment/
  - moollm://github/SimHacker/moollm/skills/sister-script/
  - moollm://github/SimHacker/moollm/skills/character/
  - moollm://github/SimHacker/moollm/skills/advertisement/
  - moollm://github/SimHacker/moollm/skills/room/
  - moollm://github/SimHacker/moollm/skills/object/
```

and keep the implemented gate: `apps/micropolis` CLI (`about`, `api`, `city`, `visualize`, `sim`, `bus`), WASM loaders, renderer plugins, sidecar and computed-layer roadmap. Soul City, DreamScape lineage, nurturing-environment essay, school repos, and the GitHub-as-civic-space protocol are the parent's text. MicropolisCore SKILL § GitHub MMORPG Protocol and § Semantic Layer Protocol restate them (branch names `city_<id>`, `issue_<id>`, `proposal_<id>`, `experiment_<id>`; layers raw bytes → resource tree → decoded YAML → authoring YAML → annotations → CHARACTER/OBJECT/city package). `file-system-object` already owns directories-as-objects and UPPERCASE interfaces. `github` owns issues, PRs, branches. `experiment` owns simulate/evaluate loops. Delegation entries that only name those skills are `inherits` / `related`, not a second protocol.

`commands:` and `workflows:` are shell recipes. The bus verbs belong on `micropolis-command-bus` as `methods`.

### micropolis-command-bus

`MicropolisCore/skills/micropolis-command-bus`. No moollm skill of this name. No `inherits`, no `moollm_compatible`, no `schema`.

CARD is inside `card:`. Methods are a map, the closest of the Micropolis pair to the method schema: LIST, PREVIEW, PROPOSE, DISPATCH, APPROVE, REJECT, each with `signature`, `description`, `output`, `tool`. `output` is the slot; the method schema's alias list does not include it (`returns` is the returns slot). `tool` is a shell line, a local extension. Advertisements are a map: ROUTE-ACTION, LLM-PROPOSE, EXPORT-MCP, BUILD-PIE-MENU, SNIFF-DIRECT-MUTATIONS, with `score`, `condition`, `effect`, sometimes `methods` or `delegate: {skill, reason}`. On a CARD, `condition` is the alias of `score_if`. GLANCE `k_lines.activates` is a map. CARD spells `k-lines` and nests `activates` plus `related: [{ref, relation}]`. `state.command`, `state.proposal`, `state.risk` (`safe | reversible | destructive | external`), and `policies` are the object, written as prose and a TypeScript literal in SKILL.md.

GLANCE `see_also` points at `moollm/skills/micropolis/CARD.yml` and at its own directory. CARD `see_also` uses absolute checkout paths for `action-queue` and `advertisement`.

Inherit:

- `moollm://github/SimHacker/moollm/skills/micropolis/` as the domain parent (the MicropolisCore one, once that one inherits moollm).
- `moollm://github/SimHacker/moollm/skills/advertisement/` for pie-menu offers. BUILD-PIE-MENU already delegates there; the advertisement entries should be advertisement objects, not a parallel `delegate:` shape.
- `moollm://github/SimHacker/moollm/skills/action-queue/` for queued proposals. action-queue methods are DO, NEXT, QUEUE, URGENT, CANCEL, CLEAR. They do not define preview, propose, approve, or risk. The bus should inherit the queue and add the gate methods.
- `moollm://github/SimHacker/moollm/skills/card/` for the interface file.
- `moollm://github/SimHacker/moollm/skills/github/` for external-risk commands.
- `skill-snitch` for SNIFF-DIRECT-MUTATIONS.

The command record (`id`, `label`, `icon`, `context`, `enabled`, `run`, `preview`, `undo`, `policy.risk`) is the schema this skill invents. Every surface (pie, key, button, chat, MCP, CLI, model) dispatches one id, and risk decides dispatch versus proposal. That parent does not exist under `moollm/skills`.

### screen-angel

`MicropolisCore/apps/screen-angel/skills/screen-angel`. `moollm_compatible: true` on CARD and on SKILL frontmatter (`ecosystem: false`). No moollm skill of this name. No `inherits`, no `methods`, no `advertisements`, no `k_lines`, no `schema`.

CARD is flat: `name`, `tagline`, `description`, then `layout`, `model`, `commands`, `global_flags`, `selectors`, `boundaries`, `failure_modes`, `python`, `respects`, `composes_with`, `related`. SKILL frontmatter uses `allowed-tools`, `permissions`, `benefits_from`, `respects`, `supports`, `composes_with`. The pyramid is copied into GLANCE, CARD, SKILL, and README.

`commands` is a map of verbs (info, permissions, windows, focused, query, tree, at, show, highlight, say, overlay, watch, mcp) with `args`, `what`, and occasional `returns`, `call_first`, `macos_caveat`, `empty_titles`. That is a methods map under another key, missing `description` / `signature` / `parameters` / `effect`.

Inherit `moollm://github/SimHacker/moollm/skills/sister-script/`, `sniffable-python/`, `postel/`, `yaml-jazz/`, and `card/`. The skill already says the CLI is the spec, selectors are accepted loosely, JSON is emitted strictly, and CARD is the interface. Those sentences are the parents. `related` should be `{id, role, when, why}` entries, or `inherits` when behavior is actually taken.

The selector language (combinators, predicates, role vocabulary, omitted sibling combinators), the socket location, the read-versus-act split, and `failure_modes` (NotRunning, empty tree when permissions are missing, `truncated`, `path` is not identity) belong in this skill as `schema:` on a prototype. They are not a second card schema. Nothing here types or clicks; that boundary stays in the skill body.

### repo-show

`WillWrightShowForFood/skills/repo-show`. No moollm skill of this name. No `inherits`, no `moollm_compatible`, no `advertisements`, no `schema`.

GLANCE `k_lines` is a list. CARD `k_lines` is `activates:` only, a shorter list, so the two views disagree. CARD is inside `card:`. `methods` is a map whose entries are mostly a `signature` string: ORIENT, FIND-GUEST, FIND-SHOW, SEED, PLANT, HARVEST. HARVEST has `delegate: SimHacker/moollm/skills/cauldron` (owner/repo/path, legacy for `moollm://`). `compose_with` is a list of the same path shape. `inheritance.rule` is a sentence ("every file under repo-shows/ inherits SHOW implicitly"), not `inherits:`.

SKILL.md proposes a GLANCE/CARD split and says to promote it into `skills/card` and `skills/glance` when it proves out. SCHEMA already states that split: GLANCE and CARD are views, `subject*: ..`, `format*: glance|card`, navigation is `related` / `see_also`, behavior is `methods` and `advertisements`, and a CARD is one file. There is no `skills/glance` directory. The format parent is the latent GLANCE until that skill exists. repo-show should follow the view rule and stop carrying a second navigation theory.

Inherit:

- `moollm://github/SimHacker/moollm/skills/cauldron/` for HARVEST (MELT, SCOOP, ladle into `skills/`).
- `moollm://github/SimHacker/moollm/skills/character/` and `representation-ethics/` for guests. Portrayal standards already extend `representation` from `WillWrightShowForFood/schemas/`; the skill should `inherits` that layer, not restate consent.
- `moollm://github/SimHacker/moollm/skills/play-learn-lift/`, `thoughtful-commitment/`, `cursor-mirror/`, `experiment/`, `rubric/` for the show's cited upstream. INDEX `upstream_moollm` lists them as `SimHacker/moollm/skills/...`.
- `moollm://github/SimHacker/moollm/skills/card/` for the interface view.

Rituals, TicketPR layout, rig classes, and branding stay in this repo's `process/` files. The skill CARD should point at them with `related`, not copy the lifecycle into GLANCE, CARD, SKILL, and README. GLANCE and README use SEED, PLANT, ELABORATE, INVITE, TEND, ANNOUNCE, AIR, HARVEST, RESEED. CARD `lifecycle.order` and the SKILL body insert PROPOSE and PRODUCE.

SHOW as an object (seed file `repo-shows/<name>.yml`, planted directory, phase list) is the schema this repo invents. It is the parent a planted show should `inherits`, written once as a prototype with `schema:`.

### ebike-safari

`WillWrightShowForFood/skills/ebike-safari`. No moollm skill of this name. No `inherits`, no `moollm_compatible`, no `methods`, no `advertisements`, no `k_lines`, no `schema`.

CARD opens with `skill:` (`name`, `version`, `type: ebike-gps-pipeline`, `status`). Behavior is `provides:` (a list) and `quick_start`. SCHEMA forbids `provides:` as an offer key; offers are `advertisements:`. SKILL.md then tables the same phases as `urban-safari`: SYNC `sync_flow_trips.py`, BUILD `build_web_assets.py`, INSPECT `inspect_fit.py`, SYNC_VIDEO `sync_video.py`, MAP_TRANSCRIPT `map_transcript.py`, plus the same `pipeline.py --sync` line and the same FIT → GeoJSON + series + manifest contract. moollm `urban-safari` GLANCE lists `methods: [SYNC, BUILD, INSPECT, SYNC_VIDEO, MAP_TRANSCRIPT, MATCH]` (a list, so that parent is itself legacy) and CARD `provides` the same Bosch Flow / GeoJSON / ffprobe stack, including the XOSS adapter this copy drops.

Inherit `moollm://github/SimHacker/moollm/skills/urban-safari/`. Keep the WWSFF facts: app lives at `apps/ebike-safari/`, Urban Safari (SFC, 2008–2011) is amber and not to be extended, MapLibre is the planned viewer, show hooks under `repo-shows/ebike-safari/`. `legacy: {name: urban-safari, status: amber}` should be `inherits` plus a `but:` (new FIT/GeoJSON stack; do not extend the SFC code), not a second pipeline description.

## Duplication with moollm

**micropolis, same name.** Two skills, two jobs, one id. moollm holds the platform essay, Soul City, lineage, and a CLI chapter aimed at `MicropolisCore/micropolis/scripts/micropolis.js`. MicropolisCore holds the unified `pnpm run micropolis` gate and restates the essay: Git branches as timelines, issues as civic discussion, PRs as merging futures, constructionist microworld, AI tutors, semantic layers down to CHARACTER.yml / OBJECT.yml, city dump/info/analyze/export and ascii/emoji visualize. The implementing skill should inherit the designing skill and own only what the binary does now (bus, sim smoke, WASM, renderer plugins, content upload after approval). Inheriting today's moollm `micropolis` does not supply a methods map or an advertisements map; that parent still uses `activates` and `invoke_when`. The outside copy duplicated the old card shape and then grew `commands` and `workflows` beside it.

**ebike-safari and urban-safari.** Different ids, same protocol table, same script names, same quick-start flags (`--sync`, `--trips-dir`, `--out`, `--home-lat`, `--home-lon`). urban-safari also has MATCH, XOSS, and a privacy rule for raw FIT. ebike-safari adds a design cauldron path and an amber label. `provides:` on both CARDs is the offer list SCHEMA replaced with `advertisements`.

**coffeeshop and place / room / budtender / representation-ethics.** Declared in prose and in INDEX `consumed`, written as bare `inherits: [room, place]` and as GitHub `tree/main` URLs. The CARD's advertisement list matches place's CARD list shape (`{action, to, when}`, VISIT and EXPLAIN). Closure-by-cause, survey-at-the-door, site history, image-plus-sidecar, and "absence is unknown" are place slots (`tenancies.cause`, `survey`, `site_history`, `review.reasons`) plus the schema's `-metadata.yml` sidecar. Consent tiers 0–4 are a numeric scale `REPRESENTATION.yml` already retired. The budtender skill already has the strain methods; coffeeshop's ASK-BUDTENDER is the delegation.

**repo-show and cauldron / card.** HARVEST is defined as "delegate cauldron" and then specified again (melt, SCOOP into `skills/`, implement in packages and apps, RESEED). The GLANCE-versus-CARD ownership note proposes an upstream change SCHEMA already made. `compose_with` paths duplicate `related`. Lifecycle text is copied across GLANCE, CARD, SKILL, and README and the phase lists differ.

**micropolis-command-bus and advertisement / action-queue.** Composition table in SKILL.md names both. Advertisements on the CARD use `condition` and a `delegate` map. Proposals are described as action-queue entries without `inherits`. Risk policy and PREVIEW/PROPOSE/APPROVE are new; the rest is the parents.

**screen-angel and sister-script / postel / card.** The pyramid paragraph is the card/skill view rule, repeated in four files. `moollm_compatible: true` is the one declaration of the six that sits on the CARD. `benefits_from` and `composes_with` name the parents without `inherits`.

**Shared legacy spellings across the outside set.** `card:` or `skill:` envelopes (coffeeshop, micropolis, command-bus, repo-show, ebike-safari). `k_lines: {activates}` or `k-lines` (micropolis, command-bus, repo-show CARD). Advertisements as a list (coffeeshop). `invoke_when` (micropolis). `provides:` (ebike-safari). `https://github.com/.../tree/main/...` and `SimHacker/moollm/skills/...` where a parent reference should be `moollm://github/SimHacker/moollm/skills/.../`. `relation:` where `related` entries use `role`. Absolute checkout paths in command-bus `see_also`.

## Schemas to reify

Own in moollm, then let the outside skill `extends` or `inherits` them. Each needs a `schema:` block (`id`, `applies_to`, `keys`) on the skill that owns it, not a CARD `fields:` dump.

1. **Command / operator.** Parent missing. Shape is the command-bus `state.command` plus `policy.risk` enum `safe | reversible | destructive | external`, and methods LIST, PREVIEW, PROPOSE, DISPATCH, APPROVE, REJECT. `action-queue` owns ordering. `advertisement` owns the offer. The gate (preview, proposal, approval, risk) is the part moollm does not have, and the Micropolis bus is the worked instance. `condition` on those ads migrates to `score_if`. `delegate:` migrates to `inherits` or to the advertisement's method.

2. **Show.** Parent missing. Seed file versus planted directory, phase id list, implicit SHOW parent for `repo-shows/`. One ordered list. HARVEST's body is cauldron's. WWSFF rituals stay local. repo-show's GLANCE/CARD split does not need a new view schema.

3. **Place without an address (`spot`).** place's one idea is that the address is the subject. GEOTOKING.md says a bench has no street number and keys `identity.osm`, a coordinate claim, and a local name, `inherits: [spot, place]`. That exception belongs on place (osm id or coordinate claim as identity when `address` is absent), not as an unowned parent name.

4. **Local ontology projected at a closed vocabulary.** coffeeshop `menu.categories.<slug>.projects_to` and `shared_vocabulary.terms` (`flower`, `hash`, `preroll`, `edible`, `drink`, `vape`, `seed`, `accessory`, `other`), with the shared list unauthorable. The coffeeshop terms stay in amsterdank. The keys `projects_to` and the closed-vocabulary rule are the general shape (verbatim local labels, coarse query terms, no writing the coarse list by hand). place and room do not have it.

5. **Do not reify consent tiers.** Map BUDTENDERS tiers onto `representation`: tier 0 → `consent.state: declined` and the robot (`speaks_as: false`, `is_a_person: false`); tier 1–3 → `granted` with `scope`; tier 4 → `authored_by` the subject. `REPRESENTATION.yml` `retired.consent_level` already records why a 1..5 rank was removed.

6. **micropolis content layers.** The six-layer stack in MicropolisCore SKILL § Semantic Layer Protocol (raw bytes, resource tree, decoded fields, authoring YAML, annotations, MOOLLM package) is `file-system-object` plus `object` / `character` prototypes plus git. It should be a short `inherits` of those, with Micropolis tile and `.cty` specifics as extensions (`owner:` the Micropolis skill). It should not be a second pyramid beside GLANCE/CARD.

7. **FIT pipeline.** Already `urban-safari`. ebike-safari adds no new keys that need an id. Migrate both CARDs off `provides:` onto `advertisements` when urban-safari grows a `schema:`.

8. **Screen Angel selector and verb list.** Own them on the screen-angel skill as `schema: id: screen-angel`, `methods` for the verbs, keys for combinators and failure modes. moollm core should not absorb CSS-subset selectors. The outside CARD's `commands` / `what` / `args` keys should become method `signature`, `description`, `parameters`.

9. **Cross-repo parent spelling and compatibility flag.** INDEX files already try to declare this (`moollm_compatible`, `consumed`, `upstream_moollm`, `compose_with`) in three shapes. One `inherits` list of `moollm://` URIs replaces `consumed`, `compose_with`, `benefits_from`, and `respects` when the relationship is inheritance. `related` remains for links that are not parents. `moollm_compatible: true` belongs once per repo INDEX, which amsterdank already does, and on each skill that is not part of moollm, which only coffeeshop and screen-angel do.
