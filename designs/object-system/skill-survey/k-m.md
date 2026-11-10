# Skill survey: k–m

Date: 2026-10-29. Standard: `designs/object-system/SCHEMA.md`, constitution §15–16.

Listing of `skills/` directories whose names start with k, l, or m (21):

k-lines, knowledge-frames, leela-ai, lighthouse-log, logistic-container, mail-digest, manufacturing-intelligence, mapbox, markdown, memory-palace, micropolis, mind, mind-mirror, moo, mooco, mooco-mirror, moocroworld, moollm, mount, multi-presence, mythic.

Checked GLANCE.yml, CARD.yml, and SKILL.md (frontmatter plus schema-shaped body). README presence only. No `parents:`, `extends:`, or `parent:` inheritance keys in these GLANCE/CARD files. `inherits:` appears as the parent list in mind examples. No `schema:` block with an `id` anywhere in the shard. No `klines:` key.

## Counts

| Check | Holds | Does not |
|---|---|---|
| GLANCE + CARD + SKILL.md | 21 | 0 |
| README present | 17 | 4: knowledge-frames, mail-digest, mind, moocroworld |
| CARD flat (no `skill:` / `card:` envelope) | 19 | 2: leela-ai, manufacturing-intelligence (`skill:`) |
| CARD `methods:` is a map, where present | 11 maps, 0 string entries | `does:` on lighthouse-log and mail-digest; `invocation:` on mapbox; mind methods are `{signature}` only |
| GLANCE `methods:` is a map of maps | 0 | 8 GLANCE files store method values as strings: k-lines, logistic-container, mapbox, memory-palace, mind-mirror, moollm, mount, multi-presence |
| CARD `advertisements:` is a map of advertisement entries | 7 maps, all using `condition:` | mount: map of strings. leela-ai and manufacturing-intelligence: singular `advertisement:`. 8 cards have neither advertisements nor `invoke_when:` |
| `k_lines:` is a list of bare K-LINE strings on the CARD | 0 | see K-line notes |
| `type:` is one id | 0 of the cards that set it | 15 cards use a list. 6 set no `type:` (knowledge-frames, leela-ai, manufacturing-intelligence, markdown, moo, moocroworld) |
| Owns a shape and has `schema:` | 0 | shapes listed under Schemas to reify |

SKILL.md has no YAML frontmatter: moo, moocroworld, micropolis, mythic.

Copy disagreements between GLANCE and CARD: k-lines method names and tier; knowledge-frames version; memory-palace method names; mapbox method set; mount method set; mooco and mooco-mirror `k_lines` shape; manufacturing-intelligence readings versus its own CARD and versus leela-ai.

## Per skill

**k-lines.** Pyramid files present, plus `CULTURE-SHIP-NAMES.md` and the memo OCR. Flat. Directory is `k-lines`; CARD `id: protocol`, `name: Protocol`; SKILL frontmatter `name: protocol`. GLANCE/CARD `tier: 0`; SKILL frontmatter `tier: 1`. GLANCE methods are strings named `K_REF` and `SISTER_SCRIPT`. CARD methods are maps named `K-REF` and `SISTER-SCRIPT`. CARD advertisements `ACTIVATE-CAPABILITY` and `CREATE-PROTOCOL` use `condition:`. No `k_lines:` key. CARD stores the theory in `k-line-insight:`. `type:` is a list of three. The K-REF grammar is copied three ways (below). This skill owns that grammar and the protocol record, and has no `schema:` block.

**knowledge-frames.** No README. GLANCE has no `what:` / `why:` / `when:`; it has `description`, `when_to_use`, `related_skills`, `version: 1.0.1`. CARD has `summary`, `status: active`, `version: 1.0.0`, `interfaces.reads`. No methods, advertisements, or `k_lines`. No `id:`. It maps four layers onto other skills (k-lines, schema-mechanism, schema). It does not own a record.

**leela-ai.** Pyramid files present. CARD is wrapped in `skill:` (`id`, `name`, `version`, `tier: meta`, `entry: README.md`). Singular `advertisement:` with `provides`, `wants`, `motives_satisfied`. `k_lines:` is a map: `activates` is a list of one-key maps (`minsky: "…"`, lowercase), `connects-to` is another list. No methods. GLANCE `tier: meta` (a string). SKILL.md contains Drescher `schema:` examples; those belong to schema-mechanism.

**lighthouse-log.** Pyramid files present. Flat. `type:` list. `k_lines: {activates, related}` with bare tokens (`LIGHTHOUSE-LOG`, `ONE-LIGHT`, `FOR-THE-ONE-WHO-COMES-AFTER`, …). `invoke_when:` list of five, no advertisements. Methods are maps whose body key is `does:`. SKILL.md specifies the house as a directory tree (`CREW.yml`, `LOG.md`, `HANDOFF.md`, `crew/<member>/ME.yml`) in prose.

**logistic-container.** Pyramid files present. Flat. GLANCE methods are strings; CARD methods are maps with the same seven names (`ADD`, `REMOVE`, `TRANSFER`, `REQUEST`, `PUSH`, `QUERY`, `NAVIGATE`). Advertisements are a map using `condition:`. `type:` list. No `k_lines`. `LOGISTIC-CONTAINER.yml.tmpl` and `CELL.yml.tmpl` are the records, each wrapped in a single key (`logistic-container:`, `cell:`).

**mail-digest.** No README. Flat. `type:` list. `status: active`. `k_lines: {activates, related}` with four bare tokens. Methods `DEDUP`, `DIGEST-PRIVATE`, `HARVEST-PUBLIC` use `does:`. No advertisements. `rules:` is a list of policy sentences.

**manufacturing-intelligence.** Pyramid files present. CARD wrapped in `skill:` like leela-ai. Singular `advertisement:` (`provides`, `wants`, `motives-satisfied` — hyphen). `k_lines.activates` is eight one-key maps (`papert`, `minsky`, `drescher`, `chomsky`, `dweck`, `leela`, `k-line`, `simulator-effect`); `connects-to` includes the key `k_lines` as a link target. GLANCE uses a different key, `k_lines_activated:`, a list of `"token — gloss"` strings, and a different seven readings than the CARD and than leela-ai (Dedup).

**mapbox.** Pyramid files present. Flat. GLANCE methods are six strings. CARD methods are seven maps (`ROUTE`, `DIAGNOSE`, `KEYS`, `SURFACE`, `MEASURE`, `WHERE`, `SNITCH`); `WHERE` is only on the CARD; several use `invocation:` rather than `signature:`. No advertisements, no `k_lines`. `type:` list. Indexes upstream Mapbox skills; it does not own their schemas.

**markdown.** Pyramid files present. CARD has `name`, `version`, `one_liner`, `when_to_use`, no `id`, no methods, no advertisements, no `k_lines`. GLANCE has `what:` and `when:`.

**memory-palace.** Pyramid files present, plus `MAP.yml.tmpl`, `ROOM.md.tmpl`, `ENTRY.md.tmpl`. Flat. GLANCE methods are strings named `CREATE_PALACE`, `ADD_ROOM`, `PLACE`, `WALK`, `RECALL`. CARD methods are maps named `CREATE-PALACE`, `ADD-ROOM`, and the same three verbs, with `description`, `parameters`, `output`, `effect`, `invoked_by`. Advertisements use `condition:`. No `k_lines`. `type:` list. The map template wraps a `palace:` key and stores `rooms` as a list.

**micropolis** (this repo). Pyramid files present. Flat. GLANCE `status: designing`, no `tier`, no methods. CARD `tier: 1`, `type:` list of four, `status:` is a map (`phase`, `next`). Activation is `activates:` (seven bare tokens), not `k_lines:`. `invoke_when:` list of five. `related:` entries are `{ref, relation}`. No methods. `artifacts/role-sheets.yml` is a catalog record (`id`, `status: designing`, `absolute_url`, `path`, `organelle`, `roles`, `experience`, `album`, …). Compared with MicropolisCore under Dedup.

**mind.** No README. Flat. `type:` list. `k_lines: {activates, related}` with `MIND`, `CUP`, `WELL`, `ORGANELLE`, and one more token. `invoke_when:` list. Methods `CREATE`, `INHERIT`, `DELTA`, `MUTE`, `SPEAK`, `ORGANELLE`, `BRIDGE` each carry only `signature:`. SKILL.md examples use `inherits:` and a `kind:` enum, and a nested `schema:` slot for an organelle's game DNA. `foundational_for: [society-of-mind, mind-mirror]`.

**mind-mirror.** Pyramid files present, plus `ETHICS.md`, `SIMS-STATS.yml`, `SIMS-STATS.md`, `ZODIAC.yml`, `ZODIAC.md`, `EXTENSIONS.yml`, `HALLS-AND-ROOMS.md`. Flat. GLANCE methods are strings; CARD methods are maps (`REFLECT`, `ANALYZE`, `MODIFY`, `COMPARE`, `PREDICT`) with `description`, `parameters`, `output`, `effect`, `invoked_by`. Advertisements use `condition:`. No `k_lines` on the CARD. `type:` list. GLANCE calls it an organelle schema on mind. The Sims tables and the circumplex are not under `schema:`.

**moo.** Pyramid files present, plus `MOONUAL.md`, `MOOGLANCE.md`, `MOOGLANCE-commands.md`, `MOOGLANCE-env.md`, `MOOGLANCE-moorl.md`, `moo.py`. CARD is flat and thin: `name`, `tagline`, `description`, `layout`, `cache`, `commands`, `env`, `related`, `tier`. No `id`, no methods, no advertisements, no `k_lines`. SKILL.md is eleven lines, no frontmatter, and points at `MOONUAL.md` for the command and moorl reference. GLANCE `related` is a one-entry map pointing at moocroworld.

**mooco.** Pyramid files present. Flat. GLANCE `k_lines:` is a list of eight `"TOKEN — gloss"` strings. CARD `k_lines:` is `{activates, related}` with eleven bare tokens (adds `MOOCO`, `SHARED-CORE`, `SKILL-INTAKE` to the GLANCE set). No methods, no advertisements. `type:` list. GLANCE `related` is a map of skill → sentence; CARD `related` is a list of `{ref, relation}` under `k_lines`.

**mooco-mirror.** Pyramid files present. Flat. GLANCE `k_lines:` is a map of three names to sentences (`MOOCO_MIRROR`, `CROSS_MIRROR`, `TRACE_DIFF` — underscores). CARD `k_lines.activates` is the hyphenated tokens `MOOCO-MIRROR`, `CROSS-MIRROR`, `TRACE-DIFF`, plus `related`. No methods, no advertisements. `type:` list. GLANCE `when:` names `TRACE-DIFF`, `MOOCO-MIRROR`, `CROSS-MIRROR`.

**moocroworld.** No README. SKILL.md has no frontmatter (about 21k). CARD has no `id`. No methods, no advertisements, no `k_lines` of its own; `related.k_lines` is a link. GLANCE carries `moo_role` and `moo_cli`, a second copy of moo's job, plus moorl addressing. `REPOS.yml` entries are `{github, description, default_type}` with auth notes. `ATTENTION-TREE.example.yml` is a separate shape.

**moollm.** Pyramid files present. Flat. GLANCE methods are nine strings; CARD methods are nine maps with the same names (`HELP`, `WHAT-AM-I`, `PHILOSOPHY`, `SKILLS`, `RECOMMEND`, `CONSTITUTION`, `NAVIGATE`, `ORIENT`, `MOOPMAP`). Advertisements `CONFUSED`, `WHAT-CAN-I-DO`, `UNDERSTAND-MOOLLM`, `FIND-SKILL` use `condition:`. No `k_lines`. `type:` list of four. `tier: 0` on both views.

**mount.** Pyramid files present. Flat. GLANCE methods are four strings (`MOUNT`, `UNMOUNT`, `LIST_MOUNTS`, `COMPATIBILITY`). CARD methods contain only `MOUNT`. CARD advertisements `modify_character`, `create_zone`, `try_affliction` are strings. `invoke_when:` list of five. `type:` list. No `k_lines`. Modes `grant` / `afflict` and targets `character` / `room` sit under `concepts:`.

**multi-presence.** Pyramid files present. Flat. GLANCE methods are strings; CARD methods are maps (`SPLIT`, `SYNC`, `MERGE`, `STATUS`). Advertisements use `condition:`. No `k_lines`. `type:` list. GLANCE `presence_schema:` is four prose fields: `source_card`, `location`, `local_state`, `siblings`. CARD has hyphenated `use-cases:`.

**mythic.** Pyramid files present. SKILL.md has no frontmatter. Flat. `is_tag: true` and `protocol: MYTHIC` on the GLANCE. No methods key. Advertisements `INVOKE`, `RETELL`, `ADAPT`, `CREATURE` use `condition:`, and `invoke_when:` is also a list of four. `type:` list. `sensitivity_levels:` is a four-way table (gods, legendary, folklore, creatures). No `k_lines`.

## Dedup

Five names, five jobs.

- **moo** — "The moo CLI is the "moo virtual machine" — user-space file tools over GitHub branches (read, write, list, resolve moorls). Each branch is a moo (ClassName_ObjectID). Repos live in moocroworld (REPOS.yml); moo owns its own ephemeral cache in .moollm/skills/moo/cache/."
- **moocroworld** — "Typed objects stored as orphan branches in a git repo. Each branch is a self-contained actor (Hewitt) with its own state (file tree), history (git log), address (branch name), and semantic interface (GLANCE → CARD → instance data). The main branch is the "main world" with rooms and shared structure. Moocroworlds orbit outside it — independent existences paged into context on demand by mooco."
- **mooco** — "Custom orchestrator designed to host MOOLLM skills. Explicit context control. Safe tool execution. Skills remain portable across orchestrators."
- **mooco-mirror** — "Parallel introspection for MOOCO sessions. Inspects events, compares with Cursor-mirror. Reveals divergence, improves portability."
- **moollm** — "The spirit and constitution of MOOLLM itself. Top-level help: explain system, navigate, articulate philosophy. When confused, invoke this skill."

moo is the CLI. moocroworld is the branch-actor model that CLI runs; its GLANCE also restates `moo_role` and `moo_cli`. mooco is the skill host. mooco-mirror diffs mooco sessions against cursor-mirror. moollm is the help and constitution skill. Not one job. The moo pair and the mooco pair are each a tool plus the thing it operates on.

**mind** — "Resident agency — usually inside (or beside) a soul. First-class; soul-as-container is organizational, not metaphysical. May host sub-minds, sub-souls, intervening containers. Blank, cloned, inherited, stub, zombie, organelle, …. Default: shares the soul's map pin."

**mind-mirror** — "Deep personality modeling via Timothy Leary's Interpersonal Circumplex. An organelle schema on a mind — needs mind; usual host soul. Four Thought Planes capture motivation, not just behavior. Complements Sims traits (behavior) with WHY."

Not the same job. mind is the agency. mind-mirror is one organelle that requires a mind. mind's CARD lists mind-mirror in `foundational_for`.

**leela-ai** and **manufacturing-intelligence** share a slogan and are not the same job. leela-ai: "MOOLLM principles applied to industrial AI. Neural-symbolic computer vision. Causal reasoning. Minsky, Papert, Drescher on factory floors." manufacturing-intelligence: "The K-line that activates them all. "Manufacturing Intelligence" — seven readings. Sparse phrase, rich conceptual activation." The seven readings have drifted. manufacturing-intelligence's seven are industrial, process, constructionism (Papert), society of mind (Minsky), manufacturing consent (Chomsky), growth mindset (Dweck), etymology (manu factus). leela-ai's slogan readings are industrial, process, constructionism, personal dynamic media (Kay), society of mind, manufacturing consent, growth mindset. Kay is only on leela-ai. Etymology is only on manufacturing-intelligence. Chomsky and Dweck swap order.

**micropolis** in this repo versus `skills/micropolis` in MicropolisCore (`github.com/SimHacker/MicropolisCore`). They diverge.

This repo: "Micropolis as constructionist educational platform. A nurturing environment, not a killer app. Open source SimCity → WebAssembly → SvelteKit → MOOLLM. AI tutors. School-owned repos. Game state as git-controlled files." Status `designing`. CARD tier 1, tagline "The filesystem is the city. Git is the multiverse." Activation key is `activates:`. Tokens: `MICROPOLIS`, `SIMCITY`, `CONSTRUCTIONISM`, `MICROWORLD`, `GIT-MULTIVERSE`, `NURTURING-ENVIRONMENT`, `METHOD-OF-LOCI`. No methods. The card is the Soul City vision.

MicropolisCore: "Parent MicropolisCore skill for humans, LLMs, CLI users, browser UI, content tools, and adapters that need to inspect, analyze, visualize, simulate, edit, render, package, or command Micropolis worlds." Status `implementing`. CARD is wrapped in `card:`, tier 2, tagline "The engine is the microworld. The CLI is the public gate." Activation is `k_lines.activates` plus `invoke_when:`. Tokens: `MICROPOLIS`, `MICROPOLIS-ENGINE`, `SIMCITY`, `CITY-FILE`, `CTY-FORMAT`, `MICROPOLIS-CLI`, `MICROPOLIS-RENDERER`, `CONTENT-CATALOG`, `CLIENT-RENDERED-PREVIEW`, `MICROWORLD`, `CONSTRUCTIONISM`. The card is the engine, save files, CLI, and renderers, with a checked command list. Shared tokens: `MICROPOLIS`, `SIMCITY`, `MICROWORLD`, `CONSTRUCTIONISM`.

## K-line notes

Read: `skills/k-lines/GLANCE.yml`, `CARD.yml`, and the schema-shaped parts of `SKILL.md` (naming convention, PROTOCOLS.yml example, K-REF format, location table, symbol table).

### Level-band

SKILL.md, from AI Memo 516: attach only to an intermediate band. Too low "would impose false perceptions and conceal the real details of the present problem." Too high "would make us hallucinate the present problem as already solved." Restore the middle of the pyramid (structure). Leave the top free for the current goal and the bottom free for current facts. Weak fringes lose cross-exclusion to whatever the present situation asserts, so they behave as defaults.

GLANCE compresses that to: attach the middle; too low imposes stale detail; too high hallucinates the problem as solved; weak fringes are defaults. `CULTURE-SHIP-NAMES.md`, via the GLANCE: "Warship" is too high, a spec sheet is too low, a disposition is the middle.

The band is a property of a K-line definition, not of every card that names it. A card's `k_lines:` stays a list of tokens. `band` lives on the definition (the PROTOCOLS.yml entry).

### K-REF grammar

Three productions in the skill, and they disagree.

GLANCE `k_ref_format` and CARD method `K-REF.format`:

```
PATH[:LINE[-END]][#anchor][?search] # TYPE - DESC
```

The worked example under that production is `/path/file.txt:42:10-46 # secret 🔴`, which is line, column, end-column, and a severity icon, and does not match `[:LINE[-END]]` or `TYPE - DESC`.

SKILL.md, first sketch:

```
/path/to/file.md:42-58 # section_type | preview text
```

SKILL.md, "K-REF Format":

```
PATH[:LINE[-END]][#ANCHOR][?SEARCH] # TYPE [LABEL] SEVERITY - DESCRIPTION
  EXCERPT or MASKED_VALUE
```

The location table adds a fourth shape the compact production does not cover: `/path/file:42:10-46` (line 42, columns 10–46), plus whole file, `:LINE`, `:LINE-END`, `#anchor`, `?search`, and `#anchor?search`. Anchor forms named in prose: markdown heading slug, YAML dot-path (`/CARD.yml#methods.K-REF`), code symbol (`#def:`, `#class:`), HTML id. Search is literal, or regex if prefixed with `~`.

### Spellings of the key

Inside k-lines:

| Spelling | Where |
|---|---|
| `k-lines` | directory name; SKILL frontmatter `tags` |
| `K-LINE`, `K-line`, `K-lines` | prose and the symbol table |
| `k-line-insight` | CARD slot, prose, not a list |
| `wikipedia_urls_are_k_lines`, `culture_ship_names_are_k_lines` | GLANCE slots, prose |
| `activates` | parameter name on method `DEFINE` ("What it invokes"), not a top-level key |
| `invoke_when` | field on the PROTOCOLS.yml example entry |
| `K_REF` / `K-REF`, `SISTER_SCRIPT` / `SISTER-SCRIPT` | GLANCE method names versus CARD and SKILL |

The skill never uses `k_lines:`, `k-lines:` as a key, or `klines:`.

Across this shard:

| Spelling | Where | Value shape |
|---|---|---|
| `k_lines:` list | mooco GLANCE | 8 strings, each `TOKEN — gloss` |
| `k_lines: {activates, related}` | lighthouse-log, mail-digest, mind, mooco CARD, mooco-mirror CARD | `activates` is bare uppercase tokens; `related` is `{ref, relation}` |
| `k_lines: {activates, connects-to}` | leela-ai, manufacturing-intelligence | `activates` entries are one-key maps, names lowercase |
| `k_lines:` map of commands | mooco-mirror GLANCE | `MOOCO_MIRROR`, `CROSS_MIRROR`, `TRACE_DIFF` → sentences |
| `k_lines_activated:` | manufacturing-intelligence GLANCE | list of `token — gloss` |
| `activates:` | micropolis CARD | 7 bare tokens. Same role as `k_lines` |
| `k-line-insight:` | k-lines CARD | prose |
| `klines:` | none | |

Bare tokens that are already K-LINEs, sitting under the wrong envelope: lighthouse-log, mail-digest, mind, mooco CARD, mooco-mirror CARD, micropolis (`activates:`). mooco GLANCE and manufacturing-intelligence GLANCE are the same tokens with a gloss glued on. leela-ai and manufacturing-intelligence CARDs are not tokens; they are lowercase topic labels with a sentence.

`related` inside `k_lines` is navigation. SCHEMA already sends it to top-level `related:`. `connects-to` is the same slot under another name.

### Proposed k-line schema keys

Two schemas. The card key `k_lines` is a list of ids of the first. Aliases the linter reports: `k-lines`, `klines`, `activates` (when the value is a list of tokens), `k_lines_activated`, and the map forms `{activates, related}` and `{activates, connects-to}` (split into `k_lines` plus `related`).

```yaml
schema:
  id: k-line
  applies_to: "each definition of a protocol symbol (PROTOCOLS.yml and inline protocol entries). A card's k_lines: is a list of these ids."
  keys:
    id:
      shape: string
      required: true
      meaning: "UPPER-CASE-HYPHENATED. All caps, hyphens, no colon, no underscore. The name is the activator. PLAY-LEARN-LIFT, not PLAY_LEARN_LIFT, not yaml-jazz, not RF."
      example: YAML-JAZZ
    meaning:
      shape: prose
      required: true
      meaning: "What re-instantiates when the name is said: the competence bundle, not a fact."
    location:
      shape: ref
      meaning: "Where the tradition is written. File, skill, or section."
    band:
      shape: enum
      values: [low, middle, high]
      default: middle
      meaning: "Level band of attachment. middle restores structure. low imposes stale detail and hides the present. high treats the problem as already solved."
```

`invoke_when` on today's PROTOCOLS.yml example is an advertisement (`score_if:`), not a key of k-line.

```yaml
schema:
  id: k-ref
  applies_to: "a sister-script pointer. One line, optional excerpt line under it."
  conventions:
    grammar: "PATH[:LINE[:COLUMN][-END]][#anchor][?search] # TYPE [LABEL] SEVERITY - DESCRIPTION"
  keys:
    path:
      shape: string
      required: true
      meaning: "Absolute path. No line means the whole file. Images are a path and a TYPE, no line."
    line:
      shape: number
      meaning: "1-based. Omit for a whole file or an image."
    column:
      shape: number
      meaning: "Start column when the specifier is :LINE:COL-ENDCOL."
    end:
      shape: string
      meaning: "End line, or end column when column is set."
    anchor:
      shape: string
      meaning: "Fragment. Markdown slug, YAML dot-path, #def:name, #class:name, or HTML id."
    search:
      shape: string
      meaning: "First match. Regex if the pattern starts with ~."
    type:
      shape: string
      meaning: "What was found: section, secret, uuid, screenshot, …"
    label:
      shape: string
      meaning: "Optional redact label, written [SSH_KEY]."
    severity:
      shape: enum
      values: ["🔴", "🟠", "🟡", "🔵", "ℹ️"]
      meaning: "critical, high, medium, low, info."
    description:
      shape: prose
    excerpt:
      shape: string
      meaning: "Following line. Masked value or surrounding text."
```

The unified grammar is the SKILL.md full production, with `:LINE:COL-ENDCOL` from the location table added, and the pipe form (`section_type | preview`) dropped. Method name on the card is `K-REF` (hyphen, the command). Schema id is `k-ref`.

## Schemas to reify

No skill in this shard has a `schema:` block. These own a repeated record:

| Owner | id | Keys now living outside `schema:` |
|---|---|---|
| k-lines | `k-line`, `k-ref` | Protocol example `meaning`, `location`, `invoke_when`. K-REF productions above. `band` is only in prose. |
| logistic-container | `logistic-container`, `cell` | Templates wrapped in `logistic-container:` and `cell:`. Cell keys include `item_type`, `storage_mode` (`fungible`, `instance`, `auto`), `stack_limit`. |
| memory-palace | `palace` | `MAP.yml.tmpl`: `palace`, `entry_point`, `rooms` (a list; collections are maps), `landmarks`, `archive`. |
| multi-presence | `presence` | GLANCE `presence_schema`: `source_card`, `location`, `local_state`, `siblings`. |
| mind | `mind` | `kind` values in SKILL.md: blank, inherited, cup, organelle, stub, zombie, made-up, imported. Record fields in the examples: `inherits`, `organelle`, `bridge`. |
| mind-mirror | `mind-mirror`, `sims-trait`, `zodiac` | Planes and circumplex axes on the GLANCE. `SIMS-STATS.yml` trait entries: `index`, `range`, `display`, `pole_0`, `pole_10`, `affects`. `ZODIAC.yml`: `algorithm`, `signs`. `EXTENSIONS.yml`. |
| moocroworld | `moo-repo`, `moorl` | `REPOS.yml` entry: `github`, `description`, `default_type`. Branch name `ClassName_ObjectID`. moorl forms are prose on the GLANCE and in moo's `MOONUAL.md`. One schema, owned here; moo references it. |
| mount | `mount` | `concepts.modes` grant/afflict, `concepts.targets` character/room, `parameters.resolution_order`. |
| lighthouse-log | `crew` | House files named in SKILL.md (`CREW.yml`, log, handoff, `ME.yml`). Field lists are still prose. |
| micropolis | `role-sheet` | `artifacts/role-sheets.yml`: `roles`, `experience`, `album`, `organelle`, plus `absolute_url` and `path` (one ref, not a pair) and `status: designing`. |
| mythic | `mythic-tag` | `sensitivity_levels` (gods, legendary, folklore, creatures) and `protocol: MYTHIC`. |

Do not reify: knowledge-frames (it points at k-lines, schema-mechanism, and schema), leela-ai's Drescher examples (schema-mechanism), manufacturing-intelligence's seven readings (one slogan's content; the drifted copy is a dedup fix, not a schema), mapbox (upstream skills), markdown, mail-digest (`rules:` is policy), moo (the moorl schema lives with moocroworld), mooco, moollm.
