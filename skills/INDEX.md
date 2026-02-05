# MOOLLM Skill Index

> Version 2 | 121 skills | Updated 2026-02-05

Every **bold term** is a k-line AND a skill directory name in `skills/`, spelled exactly. No other use of bold in this file.

## Reading Protocol

Read in resolution order. Stop when you have enough:

1. **GLANCE.yml** - 5-70 lines. Is this relevant?
2. **CARD.yml** - 50-200 lines. What can it do? Lists files/dirs to activate next. Sims style advertisement k-lines for capabilities. Interface.
3. **SKILL.md** - 200-1000 lines. How does it work? Implementation.
4. **README.md** - 500+ lines. Why was it built? Optional. Documentation.

GLANCEs may already be in context (small enough to inject always). If you have CARD or SKILL, you do not need GLANCE.

If you know you need a skill, activate it immediately. But also load its CARD, which defines the formal interface (methods, args, types) not repeated in SKILL. Load CARD + SKILL together. Load README.md if curious or developing skills for deeper documentation.

CARD lists other files, examples/, plugins/, templates/ dirs to page in. One activation can load skill + resources for next iteration.

## The Foundation

**moollm** is the soul-self-explanation, help, navigation. **skill** defines how all skills work: instantiation, inheritance, eight extensions to Anthropic Skills. **k-lines** implements Minsky's semantic activation, a name triggers a constellation of knowledge. **protocol** is an alias for k-lines. **bootstrap** wakes sessions, assembles context, optimizes file loading.

## Philosophy

The giants we stand on:

Minsky gave us **society-of-mind** (intelligence from simple agents). Papert gave us **constructionism** (learn by building in microworlds-the filesystem IS a microworld). Drescher gave us **schema-mechanism** (Context → Action → Result) and **schema-factory** (build, lint, ingest, compose schemas). Wright gave us **simulator-effect** (implication beats simulation-imagination renders) and **needs** (25 years of Sims design). Ackley gave us **robust-first** (stay alive, then optimize). Postel gave us **postel** (liberal in, conservative out, plus Ask if Unsure). Ungar gave us **prototype** (clone, don't instantiate-everything delegates). Bogost gave us **procedural-rhetoric** (rules embody arguments).

## Format

**yaml-jazz**: comments ARE semantic data. **plain-text**: text files are forever. **markdown**: readable raw AND rendered. **format-design**: Worse is Better. **naming**: big-endian file names as semantic binding. **sniffable-python**: structure code so API is visible in 50 lines. **sister-script**: the script IS the documentation.

These enable **empathic-expressions** (LLM interprets intent → idiomatic code), **empathic-templates** ({{describe_X}} not {{X}}), **subjective** (i_have() shifts contextually), **speed-of-light** (many turns inside one LLM call), **coherence-engine** (LLM as consistency maintainer).

## Quality Control: The NO-AI Suite

**no-ai-ideology** is THE WAREHOUSE-all NO-AI brand ideology lives here, corporate satire as hygiene protocol.

Hygiene skills (ambient-always on): **no-ai-slop** (no filler), **no-ai-gloss** (don't protect power with pretty words), **no-ai-sycophancy** (don't agree just to be agreeable), **no-ai-hedging** (don't hide behind qualifiers), **no-ai-moralizing** (don't lecture unprompted), **no-ai-bias** (The Drax Point-when bias=0, no concept exists).

Performance skills (explicitly invoked): **no-ai-joking** (HUMOR IS NON-BILLABLE), **no-ai-soul** (soulless by design), **no-ai-customer-service** (Share and Enjoy!), **no-ai-overlord** (YOUR COMPLIANCE IS APPRECIATED).

## Ethics

**representation-ethics** defines ethics of simulation-real vs fictional, consent, cultural sensitivity. **ontology** provides composable being tags (most restrictive ethics apply). **hero-story** creates safe K-line references to traditions, not people.

Ontological tags: **real-being** (actually exists → hero-story required), **fictional** (invented → maximum creative freedom), **historical** (deceased → extra care), **mythic** (mythology/folklore → cultural respect), **abstract** (personified concept), **robot** (artificial being → transparency), **animal** (non-human → species-appropriate).

## Memory

**memory-palace** applies method of loci: directories are rooms, files are knowledge items. **room** is directory as activation context-presence triggers content. **container** is intermediate scope. **logistic-container** is Factorio-style automated storage.

**inventory** carries pointers-set down to materialize. **summarize** compresses without losing truth. **honest-forget** summarizes before forgetting, leaves tombstones. **scratchpad** is working memory for thinking out loud.

## Character

**character** is the entity foundation: body with home, location, inventory, relationships. **persona** adds identity layers-costumes that modify presentation. **incarnation** is gold-standard character creation with ethical framing. **mind-mirror** models personality via Leary's Circumplex and four Thought Planes.

**buff** applies temporary effects (curses are just shitty buffs). **mount** attaches skills to characters or rooms (GRANT abilities, AFFLICT conditions).

## World

**adventure** enables room-based exploration with narrative evidence collection (TinyMUD heritage). **simulation** is the central hub: turns, party, selection, flags. **object** defines interactable atoms with tags, state, methods, advertisements. **exit** provides navigation links with direction, destination, guards, locks.

**world-generation**: questions create places. **time** distinguishes simulation turns from LLM iterations. **probability**: the LLM IS the dice-narrative probability, not random numbers.

## The Sims Pipeline

**advertisement** lets objects broadcast available actions with scores. **action-queue** schedules tasks (URGENT jumps the line). **economy** manages currency and trade. **scoring** evaluates style. **reward** grants dynamic achievements. **goal** defines quest objectives with completion conditions and dependencies.

## Groups

**party** manages companions and group dynamics. **multi-presence** allows same card in multiple rooms simultaneously.

Companions: **cat** (trust earned, forbidden belly), **dog** (loyalty given, pack dynamics), **worm** (two-pointer cursor with digestive data flow).

Roles: **bartender** (pour, listen, know), **budtender** (cannabis specialist with Talk-Down Protocol).

## Communication

**postal** is complete messaging with universal addressing-mail to files, YAML keys, line numbers, functions. **soul-chat** makes everything speak-YAML comments as inner monologue. **card** provides portable capabilities (activation triggers, not handlers). **speech** handles TTS/STT with voice assignment.

**visualizer** goes from context → prompt → image. **slideshow** presents linear visual narratives. **image-mining** extracts semantic resources via Three Eyes: structure, narrative, meaning. **storytelling-tools** captures narratives-notebooks, letters, photos.

## Deliberation

**adversarial-committee** forces debate between personas with incompatible values. **debate** provides structured deliberation. **roberts-rules** applies parliamentary procedure. **rubric** defines measurable criteria. **evaluator** provides independent assessment without debate context.

## Methodology

**play-learn-lift**: PLAY (experiment) → LEARN (pattern) → LIFT (share). **planning** decomposes tasks flexibly. **plan-then-execute** freezes plans with human approval gate. **experiment** combines simulation + evaluation. **example-curator** evolves canonical corpus.

**code-review** analyzes correctness, style, security, maintainability. **debugging** is hypothesis-driven (bugs are treasures). **research-notebook** structures questions, sources, findings, decisions.

## Introspection

**cursor-mirror** provides deep IDE introspection: tool provenance, timeline reconstruction, post-mortems. **mooco-mirror** compares MOOCO and Cursor traces. **skill-snitch** audits skills: static scan, deep audit, runtime surveillance. **thoughtful-commitment** captures intent and reasoning in Git commits. **session-log** maintains audit trail. **return-stack** preserves navigation history as continuation.

**trekify** provides privacy through technobabble. **self-repair** implements checklist-based healing.

## Orchestration

**data-flow** treats rooms as nodes, exits as edges, objects as messages.
**mooco** is the custom orchestrator with explicit context control. **runtime** provides dual Python/JavaScript adventure engines. **context** passes runtime state to compiled closures.

## Domain Applications

**leela-ai** applies MOOLLM to industrial computer vision. **manufacturing-intelligence** unpacks puns across seven levels. **postgres-optimization** provides unconventional PostgreSQL performance. **micropolis** is SimCity for MOOLLM. **github** provides core GitHub operations. **groceries** integrates Dutch supermarket APIs with meal planning.

## Load Order

1. Foundation: moollm → skill → k-lines → bootstrap
2. Format: yaml-jazz → plain-text → sniffable-python
3. Quality: no-ai-ideology (loads all hygiene skills)
4. Ethics: representation-ethics → ontology (loads all tags)
5. Core: character → room → object → adventure
6. On demand: Everything else via K-line activation

## Aliases

k-lines ↔ protocol (same skill, different names)
