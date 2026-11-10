# M11 — "interest" survey

Searched `skills/`, `kernel/`, `designs/object-system/`, and `PROTOCOLS.yml` for `interest` (case-insensitive). No files were renamed. `ALIGNMENT-PLAN.md` was not edited.

Dispatch sense: NeWS event dispatch, a behavior offer, a directory listing as an index of offers, or a gate on those offers. That word in moollm is advertisement.

English sense: curiosity, a topic, aesthetic or narrative "interesting", consent state `interested`, Sims personality interests, a proper name, a quoted source, finance, or an HCI term (Furnas degree-of-interest, Shneiderman object of interest, region of interest). No rename.

## The three named targets

| Plan target | Live file | Dispatch word left? |
|---|---|---|
| `INTEREST-GATES.yml` → `ADVERTISEMENT-GATES.yml` | `kernel/ADVERTISEMENT-GATES.yml` | No. Header is "Standard activation gates for advertisements of objects, skills, characters and actions". `INTEREST-GATES` occurs only as a citation. |
| `directories_as_interests` | `skills/skill/CARD.yml:119` `directories_as_advertisements`; body line 121 "VIRTUAL ADVERTISEMENTS". Same key on `skills/skill/GLANCE.yml:40`, `skills/yaml-jazz/GLANCE.yml:52`, `kernel/NAMING.yml`, `kernel/naming/NAMING.yml:173`. `skills/yaml-jazz/CARD.yml:43` `directories-as-advertisements`: "Directory listings ARE the advertisement index". | The key is gone. Two prose leftovers below. |
| event-handler wording | `skills/adventure/events/INDEX.yml:4` already: "Each handler advertises which event types it handles." | `skills/adventure/events/README.md:92` still shouts INTEREST. |

`skills/skill/` contains no `interest`. `skills/advertisement/` contains no `interest`. `kernel/ADVERTISEMENT-GATES.yml` contains no `interest`.

## Dispatch — rename these

### `skills/yaml-jazz/skill-snitch-report.md:54`

Sense: dispatch. The CARD already uses the new principle name. The snitch table is stale.

```
| directories-as-interests | Directory listings ARE the interest index |
```

Rename to:

```
| directories-as-advertisements | Directory listings ARE the advertisement index |
```

### `skills/no-ai-ideology/CONTRIBUTING.md:262` and `:264`

Sense: dispatch. Directory listing as the advertisement index. The rest of that section does not use the word.

`:262` `## How Directories Work as Interests` → `## How Directories Work as Advertisements`

`:264` `When an LLM lists a directory, it reads interests:` → `When an LLM lists a directory, it reads advertisements:`

### `skills/adventure/events/README.md:92`

Sense: dispatch. Event-handler wording. INDEX.yml is already recast; this quote is the leftover.

```
>   They advertise INTEREST in certain events.
```

Rename to:

```
>   They advertise which event types they handle.
```

### `kernel/naming/NAMING-CONSTELLATIONS.yml:36`

Sense: dispatch. Fifth member of the adventure constellation, beside room, object, and character. The skill directory is `skills/advertisement/`.

```
The constellation: [adventure, room, object, character, interest]
```

Rename to:

```
The constellation: [adventure, room, object, character, advertisement]
```

### `kernel/REVIEW.2026-04-21.claude-opus-4.7.yml:98`

Sense: dispatch. Tension slug still named for the old gates file. `side_a` already says `ADVERTISEMENT-GATES.yml`. `side_b` is score/condition/effect and does not say interest. The markdown review of the same date does not contain the word.

```
  - name: interest-gates-vs-advertisements
```

Rename to:

```
  - name: advertisement-gates-vs-scored-advertisements
```

Leave `side_a`, `side_b`, and `my_take` as they are.

### `designs/object-system/ANNOTATED-BIBLIOGRAPHY.md:128` and `:139`

Sense: dispatch. The key in the same paragraph is already `directories_as_advertisements`. The heading and the gloss still say interests. `skills/skill/CARD.yml:121` says "VIRTUAL ADVERTISEMENTS".

`:128` `## skill CARD — directories as interests, and the eight extensions` → `## skill CARD — directories as advertisements, and the eight extensions`

`:138-139` `directory listings are *virtual` / `interests* for the LLM:` → `directory listings are *virtual` / `advertisements* for the LLM:`

## Dispatch-shaped — do not rename the word

Replacing the dispatch word with advertisement would erase a ban, a citation, or a decision.

| File | Line | Why it stays |
|---|---|---|
| `designs/object-system/SCHEMA.md` | 211 | Never-column: other offer keys are `reactions:`, `interests:`, `provides:`. The legal key in the same row is already `advertisements:`. Renaming `interests:` here would ban `advertisements:`. Leave the retired spelling in the ban. |
| `designs/object-system/readings/2026-07-14-object-system-readme-reading.md` | 154 | "NeWS called them event interests" names NeWS's word, then the section uses advertisements. Recasting it would misname NeWS. |
| `designs/object-system/CARD-ANALYSIS.md` | 252, 254, 259–261, 263–265, 307 | Section 6 is the decision record. The three "Where" cells quote paths and sentences that are no longer in the live files (`kernel/INTEREST-GATES.yml` does not exist; `directories_as_interests` does not exist; INDEX.yml no longer says "expresses INTEREST"). Leave the before-quotes. The work list is stale; the leftovers are the six renames above, not those three paths. |
| `designs/object-system/tasks/objsys-001-reconcile-vocabularies.yml` | 78 | Decision note, 2026-10-29: "'interest' means advertisement". The sentence is the mapping. |
| `designs/object-system/ALIGNMENT-PLAN.md` | 206 | M11 work order. Not edited. Cites the three old forms. Consent hits on 62, 64, and 351 are the English consent state, below. |

`designs/object-system/readings/2026-07-14-object-system-readme-reading.md:209` ("an interesting Hacker News discussion") is ordinary English. No rename.

## English — no rename

Consent state `interested` (wants to take part; governs nothing until `granted`):

| File | Lines |
|---|---|
| `PROTOCOLS.yml` | 790, 829 |
| `kernel/constitution-core.md` | 311 |
| `skills/character/CHARACTER.yml` | 223, 228 |
| `skills/representation-ethics/REPRESENTATION.yml` | 67, 72 |
| `skills/prototype/scripts/layers_lint.py` | 106 |
| `skills/prototype/scripts/test_layers_lint.py` | 439, 442, 445, 450, 452, 459, 461 |
| `designs/object-system/ALIGNMENT-PLAN.md` | 62, 64, 351 |
| `designs/object-system/skill-survey/o-r.md` | 203, 205, 319 |
| `designs/object-system/skill-survey/outside.md` | 43 |

Sims personality interests, and character topic scores (CARD-ANALYSIS already keeps these):

| File | Lines | What it is |
|---|---|---|
| `skills/mind-mirror/SIMS-STATS.yml` | 253, 254, 257, 260 | PersonData interest categories |
| `skills/mind-mirror/SIMS-STATS.md` | 81 | "interesting failure" (English, Wright) |
| `skills/mind-mirror/README.md` | 48 | conventional interests |
| `skills/mind-mirror/ETHICS.md` | 46 | conventional interests |
| `skills/mind-mirror/SKILL.md` | 83 | Interests: forestry, gardening |
| `skills/mind-mirror/HALLS-AND-ROOMS.md` | 219, 544 | Furnas degree-of-interest; 242 is English "interesting" |
| `skills/adventure/ADVENTURE-COMPILER.md` | 1405, 1421, 1472, 1473, 1493, 2298, 2365, 2514, 2521, 2635, 2640, 2692, 2695, 2696, 2716, 2725, 2731, 2843, 2844, 2851, 2884, 3061 | `subject.interests.*`, `philosophy_interest`, `interesting_book`, FAQ topic scores, "Which interests you" |
| `skills/representation-ethics/examples/smallville-style-simulation.yml` | 67, 128 | `interests:` topic list; `mutual_interest_expressed` is social |
| `skills/hero-story/CARD.yml` | 95 | parameter `interest:` "What aspect interests you" |
| `skills/no-ai-overlord/archetypes/ROOM.yml` | 95 | `reveal: interests` — "what this archetype is about" |
| `skills/adventure/dist/prototypes.js` | 72 | `interests: archetype.utility \|\| archetype.interests` under the comment "What this archetype is about" |
| `skills/adventure/engine.js` | 1748, 1749 | buyer item-type preferences; "isn't interested in" |
| `skills/simulation/examples/urban-safari-ride-game.yml` | 39 | `project_interests` in a memory loop, beside `suggest_poi` |

Proper names, quoted sources, finance, HCI, stakes:

| File | Lines | What it is |
|---|---|---|
| `skills/no-ai-overlord/CARD.yml` | 124, 300 | TV title "Person of Interest" |
| `skills/no-ai-overlord/SKILL.md` | 46 | same title |
| `skills/no-ai-overlord/README.md` | 63 | same title |
| `skills/no-ai-overlord/skill-snitch-report.md` | 48 | same title |
| `skills/no-ai-overlord/archetypes/the-machine.yml` | 1 | same title |
| `skills/no-ai-overlord/archetypes/samaritan.yml` | 1 | same title |
| `skills/no-ai-overlord/archetypes/INDEX.yml` | 82 | same title |
| `skills/k-lines/sources/aim-516-k-lines-1979-ocr.txt` | 969 | Minsky OCR, "of interest that" |
| `skills/persona/CARD.yml` | 182 | "Technical debt has interest" (finance); 372 "Load if interested" is curiosity |
| `designs/object-system/HOMOICONICITY.md` | 386, 599, 607, 614 | Perlis epigram "nothing of interest is easy" and the English around it |
| `PROTOCOLS.yml` | 1862 | "regions of interest" (annotation) |
| `PROTOCOLS.yml` | 2299 | "less interesting" |
| `skills/design-sense/lenses/direct-manipulation.md` | 8 | Shneiderman, objects of interest |
| `skills/design-sense/seeds/2026-08-22-wwsff-corpus.md` | 52, 77 | same term; 77 is English "interesting failure" |
| `skills/design-sense/masters/ben-shneiderman.md` | 16, 34 | object of interest |
| `skills/design-sense/masters/don-hopkins.md` | 24 | object of interest |
| `skills/no-ai-parrot/corpus/CORRECTIONS.md` | 80 | "points of interest"; 48 is English "interesting" |
| `skills/adventure/dist/README.md` | 1328 | `persons_of_interest` |
| `skills/no-ai-gloss/SKILL.md` | 166, 220, 261, 343 | business interests, conflict of interest |
| `skills/no-ai-gloss/skill-snitch-report.md` | 57 | conflict of interest |
| `skills/no-ai-gloss/examples/2026-01-24-register-switch-oligarch-critique.yml` | 23 | business interests |
| `skills/no-ai-ideology/examples/enemy-fake-objectivity.yml` | 45 | "Whose interests" |
| `skills/skill-snitch/catalog/awesome-agent-skills/CATALOG.md` | 15 | column "Interest for MOOLLM" (relevance) |
| `skills/cursor-mirror/reference/EXTERNAL-PROJECTS-COMPARISON.md` | 79 | "Interest in what Cursor sends" (curiosity) |
| `skills/leela-ai/reference/society-of-llms.yml` | 31, 33 | `when_interesting:` hindsight samples |

Ordinary English (curiosity, aesthetic, narrative, "the interesting part"). No rename. One line each unless noted:

`skills/animal/SKILL.md:79`, `skills/buff/BUFF-IN-TIME-COMPILER.md:105`, `skills/buff/SELF-KORZ.md:104`, `skills/buff/SKILL.md:198,296,641`, `skills/buff/buffs/INDEX.yml:1105`, `skills/buff/buffopedia/interchange.yml:104`, `skills/buff/buffopedia/observations.yml:611`, `skills/buff/buffopedia/registry.yml:126`, `skills/buff/buffopedia/systems/equipment-inventory/SYSTEM.yml:55`, `skills/buff/buffopedia/systems/lambdamoo/SYSTEM.yml:22`, `skills/buff/buffopedia/systems/simprov/SYSTEM.yml:221,296`, `skills/buff/buffopedia/systems/spore/SYSTEM.yml:188`, `skills/cat/CARD.yml:198,224`, `skills/cat/SKILL.md:189`, `skills/cauldron/META-PLAN.md:74`, `skills/cauldron/REVIEW.2026-04-21.claude-opus-4.7.yml:108`, `skills/cauldron/protocols/SCRY.yml:47`, `skills/cauldron/protocols/TREE.yml:81`, `skills/cursor-mirror/REVIEW.2026-04-21.claude-opus-4.7.md:66`, `skills/cursor-mirror/characters/i-beam/CHARACTER.yml:85,206,222,291,344,378`, `skills/cursor-mirror/characters/i-beam/README.md:144,283`, `skills/cursor-mirror/lib/commands/status_cmd.py:296`, `skills/cursor-mirror/scripts/cursor_mirror_old.py:5739`, `skills/debate/SIDE.yml.tmpl:84`, `skills/design-sense/masters/john-conway.md:38`, `skills/design-sense/masters/scott-kim.md:36`, `skills/design-sense/methods/failure-as-entertainment.md:8`, `skills/dog/SKILL.md:352`, `skills/fictional/SKILL.md:187`, `skills/groceries/examples/voyager-neelix.yml:97`, `skills/image-mining/SKILL.md:2354`, `skills/INDEX.yml:703`, `skills/mapbox/CAULDRON.md:3,86`, `skills/mapbox/README.md:12,139,178`, `skills/mapbox/skill-snitches/findings.yml:195,339`, `skills/mapbox/skill-snitches/mapbox-location-grounding/skill-snitch-report.md:16`, `skills/mapbox/skill-snitches/mapbox-token-security/skill-snitch-report.md:79`, `skills/markdown/SKILL.md:440`, `skills/micropolis/artifacts/connections.yml:195,247`, `skills/micropolis/artifacts/education.yml:275`, `skills/micropolis/artifacts/unfulfilled-dreams.yml:190`, `skills/no-ai-gloss/examples/2026-02-20-documented-violence-to-fantasy-laundering.yml:211`, `skills/no-ai-humansplaining/examples/2026-08-02-hn-humansplaining-gastowning.yml:187`, `skills/no-ai-joking/examples/minsky-ultimate-machine.yml:817`, `skills/no-ai-joking/skill-snitch-report.md:119,165`, `skills/no-ai-moralizing/examples/2026-01-24-refusal-theater-historical-fiction.yml:23`, `skills/no-ai-overlord/archetypes/hannibal-chew.yml:156`, `skills/no-ai-overlord/archetypes/i-beam.yml:19`, `skills/no-ai-overlord/archetypes/q.yml:35,68`, `skills/no-ai-overlord/examples/patronizing.yml:122`, `skills/no-ai-overlord/examples/sealioning.yml:48`, `skills/no-ai-parrot/CONSTITUTION.md:331`, `skills/no-ai-parrot/corpus/CANON.md:457`, `skills/no-ai-slop/HUMAN-SLOP.md:21,87`, `skills/no-ai-soul/CARD.yml:72`, `skills/no-ai-soul/facets/INDEX.yml:141`, `skills/no-ai-soul/facets/creativity.yml:46`, `skills/no-ai-soul/facets/presence.yml:62`, `skills/no-ai-sycophancy/CARD.yml:153,291`, `skills/no-ai-sycophancy/CONTRIBUTING.md:44`, `skills/no-ai-sycophancy/SKILL.md:161,275`, `skills/no-ai-sycophancy/examples/2026-01-24-great-question-any-question.yml:48`, `skills/no-ai-sycophancy/skill-snitch-report.md:161`, `skills/place/GLANCE.yml:5`, `skills/place/SKILL.md:100,108`, `skills/play-learn-lift/PLAY_LOG.md.tmpl:44`, `skills/return-stack/SKILL.md:88,89,96,206` (bookmark name `interesting-spot`), `skills/robot/README.md:33`, `skills/robot/SKILL.md:47,48,64,117`, `skills/skill-snitch/catalog/README.md:68`, `skills/skill-snitch/catalog/anthropic/CATALOG.md:3`, `skills/skill-snitch/catalog/anthropic/mcp-builder-development.md:20`, `skills/skill-snitch/catalog/mcp-servers/CATALOG.yml:13`, `skills/skill-snitch/catalog/reviewed/soul-md-persona.yml:2,20`, `skills/soul-city/CHARACTER-ENDOSYMBIOSIS.md:111`, `skills/soul-city/GLOSSARY.md:235`, `skills/soul-city/README.md:25,40,77`, `skills/soul-city/SOUL-BRIDGES.md:308`, `skills/stone/SKILL.md:160`, `skills/task/CARD.yml:94,152`, `skills/task/SKILL.md:164`, `skills/visualizer/profiles/INDEX.yml:60`, `skills/visualizer/visualize.py:273`, `skills/adventure/PSIBER-PROTOCOL.md:469`, `skills/adventure/SKILL.md:364`, `skills/adventure/SUMMON-PROTOCOL.md:176`, `skills/adventure/skill-snitch-report.md:136`.

`skills/adventure/dist/world.json` is compiled narrative. Every hit is English: curiosity, character topics, points of interest, a financial "Interest rate", `tom_interest`, or "interesting" as a story beat. Lines: 485, 526, 870, 7745, 10281, 11345, 12019, 13411, 14414, 16861, 19154, 19233, 19296, 20095, 20134, 20153, 20162, 20220, 20764, 21848, 23342, 25288, 25289, 25504, 25505, 25935, 25984, 26314, 29911, 30682, 32279, 32587, 32613, 32623, 32659, 32680, 32683, 32686, 32724, 32730, 32767, 32768, 33481, 33496, 33941, 38846, 39996, 39997. The PostgreSQL "EVENT DISPATCH" examine text at 30682 uses "interesting" as English and does not call the queue an interest. No rename. Do not edit the dist file in place of its sources.

`skills/experiment/` is entirely the English sense: curiosity, aesthetic, visual composition, narrative, chess "with interest" (the recapture idiom), and "player interests" as stakes. Includes shouted `INTERESTING`. No rename. Case-sensitive file counts (shouted-only lines are the same sense): `experiments/turing-chess/runs/kasparov-deep-blue-1997/RUN-000.yml` 6, `plugins/revolutionary-chess/REVOLUTIONARY-CHESS.yml` 2, `DYNAMICS.md` 3, `house-rules/VANQUISHED-MERCY.yml` 1, `house-rules/THE-HAGUE.yml` 1, `PIECE-CONSCIOUSNESS.yml` 1, `NO-KINGS.md` 1, `games/opera-game-1858.yml` 1, `games/game-of-century-1956.yml` 1, `characters/alan-turing.yml` 3, `turing-chess/EXPERIMENT.md` 1, `fluxx-chaos/engine/DEALER.yml` 3, `CARD-INTERACTION.yml` 1, `PERFECT-CARD-GENERATOR.yml` 1, `cards/cosmic-dealers.yml` 1, `cards/moollm-inspirations.yml` 1, `cards/amsterdam-expansion.yml` 1, `runs/moollm-ultimate/RUN.yml` 5, `runs/amsterdam-flux/generated-cards.yml` 1, `artwork/SLIDESHOW.md` 1, `artwork/ARTWORK.md` 3, `artwork/06-love-mined.yml` 1, `artwork/03-moon-mined.yml` 1, `artwork/02-rocket-mined.yml` 1, `artwork/01-cookies-mined.yml` 3, `SCORE.md` 1, `RUN-017.yml` 1, `RUN-015.yml` 1, `RUN-015.md` 1, `RUN-012.yml` 1, `RUN-010.md` 1, `RUN-005.md` 1, `RUN-003.md` 1, `RUN-001.yml` 1, `RUN-001.md` 1, `RUN-000.yml` 1, `RUN-000.md` 1, `PROTOCOL.md` 1, `LETTER-TO-ANDY.md` 3, `fluxx-chaos/EXPERIMENT.md` 4, `APPRECIATION.md` 1, `emo-poker-face/runs/whacky-eight/RUN.yml` 2, `minimal-three/RUN.yml` 1, `four-player/RUN.yml` 1, `RUN-004.yml` 1, `RUN-003.yml` 3, `RUN-003.md` 2, `RUN-001.yml` 1, `RUN-001.md` 1, `RUN-001-cursor-mirror.yml` 1, `eight-player/RUN.yml` 1, `RUN-005-cursor-mirror.yml` 1, `RUN-004-cursor-mirror.yml` 1, `RUN-003-cursor-mirror.yml` 1, `RUN-002-cursor-mirror.yml` 1, `RUN-001.md` 1, `RUN-001-cursor-mirror.yml` 1, `RELATIONSHIPS.yml` 2, `emo-poker-face/EXPERIMENT.md` 2, `patterns/visual-prompt-synthesis.yml` 1, `patterns/observable-signatures.yml` 1, `patterns/layered-simulation.yml` 1, `skills/experiment/SKILL.md` 2, `skills/experiment/README.md` 1.
