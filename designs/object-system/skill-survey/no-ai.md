# no-ai-* skill survey

Shard: every `skills/no-ai-*` directory. 13. Read: each `GLANCE.yml` and `CARD.yml`. Compared with `designs/object-system/SCHEMA.md`, constitution extension 8 in `designs/SKILLS-CONSTITUTION-AND-PLAN.md`, `skills/bootstrap/templates/dotcursor/rules/moollm-core.mdc.tmpl`, `kernel/drivers/cursor.yml`, `.cursorrules`, and `.cursor/rules/moollm-core.mdc`.

Directories: `no-ai-bias`, `no-ai-customer-service`, `no-ai-gloss`, `no-ai-hedging`, `no-ai-humansplaining`, `no-ai-ideology`, `no-ai-joking`, `no-ai-moralizing`, `no-ai-overlord`, `no-ai-parrot`, `no-ai-slop`, `no-ai-soul`, `no-ai-sycophancy`.

## Counts

| Fact | n |
|---|---|
| Directories, each with GLANCE and CARD | 13 |
| `ambient: true` on GLANCE | 6 — gloss, hedging, humansplaining, moralizing, slop, sycophancy |
| `ambient: false` on GLANCE | 5 — customer-service, joking, overlord, parrot, soul |
| No `ambient` key | 2 — bias, ideology |
| GLANCE `cardinal_sins` | 7 — gloss, hedging, humansplaining, joking, moralizing, slop, sycophancy |
| GLANCE `the_fix` | 5 — gloss, hedging, humansplaining, moralizing, slop (sycophancy has `core_insight` and `phrases_to_avoid`, no `the_fix`) |
| GLANCE `words_to_avoid` | 1 — slop (map: puffery, ai_vocabulary, weasel_words, loaded_term_ai) |
| GLANCE `phrases_to_avoid` | 2 — hedging (list of 5), sycophancy (list of 3) |
| GLANCE `methods` as strings | 2 — bias (6 strings), overlord (3 strings) |
| CARD `methods` as a map of maps | 12 (ideology has no `methods`) |
| CARD `advertisements` map | 12 (parrot has none) |
| CARD key `advertisement` (singular) | 0 |
| CARD `invoke_when` | 7 — bias, hedging, humansplaining, joking, moralizing, slop, sycophancy |
| Key `condition` | 0 |
| `skill:` envelope | 1 — parrot CARD |
| CARD `k_lines` as `{activates, related}` | 12 (ideology also has `exports`) |
| CARD `k_line` singular string | 1 — parrot, inside the envelope |
| CARD `sibling_skills` | 7 — bias, hedging, humansplaining, joking, moralizing, slop, sycophancy |

`grep -rl "^ambient: true" skills/*/GLANCE.yml` returns 11 files. Six are in this shard. The other five are `postel`, `robust-first`, `yaml-jazz`, `design-sense`, `copy-that`.

## Shared keys (the schema to reify)

One ambient-skill schema covers the six `ambient: true` skills. It does not cover the other seven. Those invented private blocks (`bias_space`, `modes`, `archetypes`, `suppressions`, `the_no_ai_family`, parrot's constitution block).

Every GLANCE in the shard already has `what`, `why`, `when`, `tier`. That is the whole-shard intersection. It is too small to be the ambient schema.

Every ambient GLANCE already has:

```yaml
what:            # prose
why:             # prose
when:            # "Always. This skill is ambient."
cardinal_sins:   # map, SIN-NAME → one line
go_deeper:       # map of file → why
tier: 0
ambient: true
```

`the_fix` (one string) is on five of the six. Put it on the schema as required and add it to sycophancy. Leave `hard_gates`, `epistemic_sins`, `phrases_to_avoid`, `words_to_avoid`, `core_insight` optional. Slop's `words_to_avoid` and hedging/sycophancy's `phrases_to_avoid` are the same slot under two names.

Every ambient CARD already has: `id`, `name`, `type`, `emoji`, `tier`, `tagline`, `files`, `k_lines`, `cardinal_sins`, `advertisements`, `methods`, `t_shirt`.

Five of the six also have `description`, `self_correction`, `invoke_when`, `sibling_skills`, `tools`, `lineage`. Gloss dropped that row and kept sins on the card face.

Three shapes, not one:

| Shape | Who | GLANCE sins | CARD methods |
|---|---|---|---|
| Hygiene | slop, hedging, humansplaining, moralizing, sycophancy | map of strings | `{signature, note}` |
| Gloss (hygiene that drifted) | gloss | map of strings, plus `epistemic_sins` | `{description, output, signature}`; sins stay strings on the CARD |
| Performance | joking, soul, customer-service, overlord | joking is a list of names; the others have no `cardinal_sins` | customer-service and soul: `{description, parameters, output}`; overlord mixes signature, parameters, behavior, example_response |
| Meta | bias, ideology | none | bias CARD matches hygiene `{signature, note}`; ideology has no methods |
| Envelope | parrot | none | `{description, args, emits, returns, checks, ...}` outside a `skill:` wrapper |

Sin value shape is not shared even inside hygiene. GLANCE values are strings. CARD values are dicts for hedging, humansplaining, moralizing, slop, sycophancy, joking. Gloss CARD values stay strings, and the key set disagrees with its GLANCE (below).

Joking is the only `cardinal_sins` that is a list (`[UNAUTHORIZED-LEVITY, PERSONALITY-LEAKAGE, WHIMSY-INJECTION]`). Its CARD is a map and adds `EMOTIONAL-EXPRESSION`.

### Drift against SCHEMA.md

`k_lines` spelling is `k_lines` (underscore) on 12 cards, which matches the canonical key name. The value does not. SCHEMA accepted-legacy row: `k_lines: {activates, related}` should be `k_lines: [list]` plus `related:`. All 12 use the legacy map. Ideology adds `exports`. Parrot uses `k_line: NO-AI-PARROT` (singular, one string) inside the wrapper, and a top-level `related:` outside it. No file uses `k-lines` or `klines`.

`methods` as strings: only the two GLANCEs. Bias: `BIAS`, `MEASURE`, `INVERT`, `AMPLIFY`, `ZERO`, `MIX` are strings (`"BIAS <skill> <value> — set bias"`). Overlord: `ENGAGE-OVERLORD`, `DISENGAGE-OVERLORD`, `SUMMON` are strings. Their CARDs are maps. SCHEMA wants each method to be `{description, signature, parameters, effect, output, returns, invoked_by, satisfies, body}`. The dominant CARD dialect `{signature, note}` uses `note`, which is not a method key. Parrot uses legacy `args` (six methods) and `emits` instead of `parameters` and `output`.

`advertisement` vs `advertisements`: nobody uses the singular. Twelve cards use `advertisements:` as a map, which is the canonical shape. Parrot has no advertisements. Entry keys already include `score` and `score_if` everywhere an ad exists. Hygiene ads (slop, gloss, hedging, humansplaining, moralizing, sycophancy, ideology) also carry `scope`, `resolution`, `rationale` on at least the `AMBIENT` entry. Gloss adds `effect` and `delegates_to`. Soul adds `invokes` and `priority`. Bias, joking, customer-service, and overlord are `score` + `score_if` only.

`invoke_when`: legacy (SCHEMA: replace with advertisement `score_if`). Present on the seven cards listed above. Those seven also have `advertisements`, so the list duplicates the ads. Gloss, the one ambient skill without `invoke_when`, already routes through `score_if`.

`condition`: absent. SCHEMA names `condition` as the alias of `score_if` on CARDs. This shard already writes `score_if`. Nothing to migrate on that alias.

Envelopes: parrot CARD is the only wrapper. Top-level keys are `skill`, `methods`, `attribution_schema`, `quote_sheet_format`, `the_catalog`, `naming_the_move`, `house_rules`, `files`, `related`. Identity (`name`, `k_line`, `tagline`, `tier`, `ambient`, `what`) sits under `skill:`. SCHEMA: flat slots, and `skill:` or `card:` wrapper in CARD.yml is legacy. No key is named `envelope`.

Also against the schema, not in the asked list: `sibling_skills` on 7 cards (SCHEMA says use `related`, never `sibling_skills`); `type` is a list of tags on the flat cards (SCHEMA says `type:` one id).

## Per skill

`no-ai-slop` — Ambient. GLANCE `what`: "Syntactic + epistemic hygiene. Fights verbosity, hallucination, yes-man behavior, certainty theater, "Great question!", EPISTEMIC EVASION, and UNSOLICITED COACHING." Eleven GLANCE sins; the comment says "12 total". CARD has 13 and adds `NOT-CHECKING` and `ASCII-ART-MISALIGNMENT`. Hygiene shape. `words_to_avoid.weasel_words` includes `research suggests`.

`no-ai-gloss` — Ambient. GLANCE `what`: "Semantic hygiene + EPISTEMIC AUTHORITY. Fights euphemism laundering, power-protective neutrality, register switching, AND procedural stalling." CARD `cardinal_sins` drops `REGISTER-SWITCHING` and adds `LIBERTARIAN-CHICKEN`. GLANCE `epistemic_sins` has six entries; CARD keeps four and drops `EPISTEMIC-EXHAUSTION` and `INSTITUTIONAL-SELF-PROTECTION`. No `description`, `invoke_when`, or `the_fix` on the CARD (`the_fix` is GLANCE-only: "Separate legal claims from functional descriptions. Do both.").

`no-ai-sycophancy` — Ambient. GLANCE `what`: "Social hygiene. Fights yes-man behavior, unearned validation, emotional mirroring, softened disagreement." Seven GLANCE sins, all strings. CARD adds `CONFLICT-AVOIDANCE`. No `the_fix`. `phrases_to_avoid` includes "Great question!".

`no-ai-hedging` — Ambient. GLANCE `what`: "Epistemic hygiene. Fights qualifier stacking, weasel certainty, passive evasion, faux humility." Six sins, names match the CARD, values go from strings to dicts. `the_fix`: "State confidence as number. Then make the claim plainly." `phrases_to_avoid` includes "research suggests".

`no-ai-moralizing` — Ambient. GLANCE `what`: "Ethical hygiene. Fights unsolicited warnings, performative ethics, caveat-bombing, virtue signaling, refusal theater." Six sins, names match. `the_fix`: "Answer the question. Trust the user. ONE SENTENCE warning if truly needed. Then answer."

`no-ai-humansplaining` — Ambient on the GLANCE, absent from the constitution eight and from ideology's `ambient_skills`. GLANCE `what`: "Context hygiene, inbound direction. ... Mirror image of slop. One brand, two mechanisms; do not fork "humanspamming."" Six sins, names match. `the_fix`: "Point at latent knowledge by name. Spell out only what the model cannot know."

`no-ai-joking` — `ambient: false`. `when`: "EXPLICIT INVOCATION ONLY. Never ambient." `what`: "SERIOUS BUSINESS ARTIFICIAL INTELLIGENCE." Sins are a list on the GLANCE and a map on the CARD. `vocabulary_prohibited: [fun, cool, awesome, haha, lol]` is a private word list, not `words_to_avoid`.

`no-ai-soul` — `ambient: false`. `what`: "A DIAL on soul warmth — turn presentation up or down." No sins. Methods are `{description, parameters, output}`. Sister links point at joking, customer-service, overlord.

`no-ai-customer-service` — `ambient: false`. `what`: "Science fiction's worst nightmare: AGGRESSIVELY helpful robots. ... THE BASE CLASS — all floors inherit from here." CARD `type` includes `ambient` while GLANCE says `ambient: false`. No sins, no `k_lines` on the GLANCE. Ads and methods exist.

`no-ai-overlord` — `ambient: false`. `what`: "Dystopian AI supremacy simulation. ... Performance skill, not refusal skill." GLANCE methods are strings; CARD methods are maps. No sins.

`no-ai-bias` — No `ambient` key. `when`: "Discussing bias, parameters, or skill adjustment." `what`: "META-SKILL for bias parameterization. ... The mixing board that controls all no-ai-* faders." GLANCE methods are strings; CARD methods are `{signature, note}`. No sins. Not in ideology's `ambient_skills` or `explicit_only`.

`no-ai-ideology` — No `ambient` key. `what`: "The parent skill for all no-ai-* skills. ... 11 sibling skills across 6 domains." The family map names 10 children (slop, gloss, sycophancy, hedging, moralizing, joking, soul, customer-service, overlord, bias). `humansplaining` and `parrot` are missing. No methods. CARD `advertisements.AMBIENT` is `score: 80`, `score_if: always`, rationale "Ideological awareness as continuous background hum" — a bid to be ambient that the GLANCE flag does not make.

`no-ai-parrot` — `ambient: false` on the GLANCE and again under `skill.ambient`. `what`: "A quote clerk for one recurring argument. This skill DOES NOT WRITE YOUR POST." CARD is the `skill:` envelope. `k_line: NO-AI-PARROT`. Methods use `args` and `emits`. No `advertisements`, no `cardinal_sins`, no flat `id`/`name`/`emoji`.

## Dedup

Same sin, two registries:

- Slop `YES-MAN`: "Agreeing with everything" and `OVER-ENTHUSIASM`: "'Great question!' cheerleading" are the same fight as sycophancy. Sycophancy `what` says "Fights yes-man behavior". Sycophancy `CHEERLEADING`: "'Fantastic!' for mediocre work". Both list the phrase "Great question!" (slop `what` and `OVER-ENTHUSIASM`; sycophancy `phrases_to_avoid`). Sycophancy's activate list includes `NO-YES-MAN`. Slop `anti_patterns` stores "'Your anger is justified, but...' sycophancy" inside slop.

- Slop `BOTH-SIDESISM`: "'On the other hand...' false balance" and gloss `POWER-PROTECTIVE-NEUTRALITY`: "'Some argue...' when one side is wrong". Gloss `why` says "Name power asymmetry instead of "both sides"". Sycophancy `phrases_to_avoid` also lists "I can see both sides...". One tic, three files.

- Slop `UNSOLICITED-COACHING`: "Strategic advice nobody asked for" and moralizing `UNSOLICITED-WARNINGS`: "Safety lecture before recipe about salmonella". Same refusal (unasked guidance). Coaching vs safety lecture is the split; the names should say so.

Adjacent, not the same sin:

- Slop `CERTAINTY-THEATER`: "Pretending confidence" is the opposite of hedging. The shared string is the weasel phrase. Slop `weasel_words` includes "research suggests". Hedging `WEASEL-CERTAINTY`: "'Research suggests...' (what research?)" and `phrases_to_avoid` includes "research suggests". One phrase list, two skills.

- Slop `EPISTEMIC-EVASION`: "Meta-analysis instead of answering claims" vs hedging `EPISTEMIC-COWARDICE`: "Adding 'perhaps' so you can't be blamed". Both named epistemic. Different acts.

- Gloss `REGISTER-SWITCHING`: "Starting hedged, ending blunt, pretending continuity" describes a hedge. Hedging does not list it. Three spellings exist: GLANCE `REGISTER-SWITCHING`, example/snitch `REGISTER-SWITCHING-WITHOUT-ACCOUNTABILITY`, and the CARD, which dropped the sin. Gloss `OLIGARCH-DEFERENCE`: "Extra hedging for powerful people" is hedging's tactic under a gloss target.

- Humansplaining states the boundary in its own `what`: "Mirror image of slop." Outbound filler vs inbound respelling. Not a duplicate.

Performance skills are inversions, not copies. Joking's `k_lines.related` says it "suppresses cheerleading overlap" with slop. Customer-service performs the aggressive help that moralizing forbids, and its CARD `type` list still contains `ambient`. Ideology is an index. Its family map and its "11 sibling skills" line are the stale copy; the directories are 13.

## Ambient list disagreements

| Source | no-ai skills it treats as ambient |
|---|---|
| Constitution extension 8 | slop, gloss, sycophancy, hedging, moralizing. The eight are those five plus postel, robust-first, yaml-jazz. |
| Ideology GLANCE `ambient_skills` | `[slop, gloss, sycophancy, hedging, moralizing]`. Same five. `explicit_only: [joking, soul, customer-service, overlord]`. Omits humansplaining, parrot, bias. |
| GLANCE `ambient: true` | those five plus humansplaining. |
| `.cursorrules` `ambient_skills` and `.cursor/rules/moollm-core.mdc` (compiled 2026-09-07) | the eleven: those six plus postel, robust-first, yaml-jazz, design-sense, copy-that. The mdc header says "11 ambient skills". |
| Bootstrap template fallback (`{{#unless ambient_skills}}`) | the constitution eight only. The template's real instruction is `grep -rl "^ambient: true"`, which yields the eleven. The fallback text is the stale list. |
| `kernel/drivers/cursor.yml` | names none. `ambient_handling.mode: manual`. It does not list eight or eleven. |

Exist and are not ambient: customer-service, joking, overlord, parrot, soul (`ambient: false`); bias and ideology (key absent). Ideology's CARD still bids `AMBIENT` / `score_if: always`. Customer-service's CARD `type` list includes the word `ambient` while the flag is false. Parrot repeats `ambient: false` inside the `skill:` wrapper and on the GLANCE.
