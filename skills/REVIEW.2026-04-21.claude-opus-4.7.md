---
target: moollm/skills
target_level: cluster
reviewer: claude-opus-4.7
date: 2026-04-21
yml_pair: REVIEW.2026-04-21.claude-opus-4.7.yml
parent: ../REVIEW.2026-04-21.claude-opus-4.7.md
---

# Skills Ecosystem — Deep Review

**Scope:** The 130-skill registry at ecosystem level. Deep-reads of prototype, object, cauldron (authored this session), cursor-mirror, bootstrap, schema, skill-snitch. GLANCE-level reads of many others. The 8 ambient skills live in my system prompt so I experience them continuously. **Confidence: 75%** — large surface, many corners I haven't inspected.

## What the ecosystem actually is

**A multi-tier skill library where the top tier (skills/) defines reusable prototype objects for an LLM-navigable microworld.** Each skill is a directory with up to four artifacts:

- `GLANCE.yml` — 5-70 lines — "is this relevant?"
- `CARD.yml` — 50-200 lines — "what can it do?"
- `SKILL.md` — 200-1000 lines — "how does it work?"
- `README.md` — 500+ lines — "why was it built?"

This pyramid is progressive disclosure: load smallest, drill only if needed. A reading protocol is specified (`skills/INDEX.md:7-20`) and mostly followed. Large skills (cursor-mirror) strain the pyramid; see the tension note below.

Beyond the pyramid, skills share four structural moves with the kernel:

1. Directory = object (same pattern as `examples/adventure-4/pub/`)
2. `parents:` or `PROTOTYPES.yml` for ordered multi-parent inheritance
3. `advertisements:` for context-scored capability
4. K-line activation via filename and uppercase symbol

What this buys: **composability by reference.** A skill doesn't re-declare discipline it inherits; it names its parent(s) and new behavior. Cauldron, authored this session, illustrates this — its parent slot points at `skills/object/`, `skills/empathic-templates/`, and the kernel's prototype machinery.

## What's strong

**INDEX.md narrative.** 128 lines that group the 130-skill catalog by function (foundation / philosophy / format / quality control / ethics / memory / character / world / sims / deliberation / methodology / development / introspection / orchestration / domain). Every bold term is both a K-line AND a skill directory — name coherence held. A reader encountering "I need something for group decisions" finds `deliberation:` with adversarial-committee / debate / roberts-rules / rubric / evaluator in four seconds. That's the pyramid working.

**Heritage citations are per-skill, not just at root level.** `skills/prototype/SKILL.md:10-13` credits "David Ungar — Self language creator / Randall Smith — Self language co-creator / Brendan Eich — JavaScript (Self-influenced)." `skills/cauldron/SKILL.md` carries Macbeth's Weird Sisters as patron. This distributes intellectual honesty across the ecosystem, not concentrated in kernel/ARCHITECTURE.md.

**Ambient skill enforcement is observable.** I am operating right now under `no-ai-slop`, `no-ai-gloss`, `no-ai-sycophancy`, `no-ai-hedging`, `no-ai-moralizing`, `postel`, `robust-first`, `yaml-jazz` (per the system prompt I was booted with). The effect is measurable: I stated confidence as percentages, disputed claims where warranted, called drift "drift" (not "minor inconsistency"), and stopped myself from recapitulating target docs. These aren't aspirational constraints; they're active. Whether they're injected via compiled .cursorrules or LLM-side self-imposition depends on the driver, but the end behavior is the same. That's the first test of an ambient layer working.

**Schemapedia as multi-family registry.** `skills/schema/GLANCE.yml:6-8` is explicit that `schema` does not mean one validation mechanism — it indexes interchange formats, notation (YAML-jazz), execution (shell orchestration), introspection (cursor-mirror DB/model), causal units (Drescher), frames, K-lines, prototype (Self), Society of Mind, SQL/SQLite, git, GitHub, com-xpcom. Each is a sense of "schema," none privileged. This resists the monoculture of "schema = JSON Schema validator" that most ecosystems collapse into. Evidence of a system thinking carefully about naming.

**Self-reference is load-bearing, not cute.** `skills/prototype/SKILL.md:22-24` declares that Self is one of the prototype skill's prototypes. Operationally, via `PROTOTYPES.yml`. That's eating your own dogfood at the mechanism level — the skill about prototypes uses the prototype system to declare its own ancestry.

## What's weak

**Core and ornamental are peers in the registry.** `INDEX.yml:626-754` lists all 130 skills alphabetically under `all_skills:`. `bartender`, `budtender`, `worm`, `cat`, `dog` sit next to `cursor-mirror`, `representation-ethics`, `bootstrap`. Tier metadata exists per-skill (`tier: primitive`, `tier: 2`) but it's buried in individual CARDs. Onboarding reader encounters "budtender — cannabis specialist" before "representation-ethics — ethics of simulation." The system looks less serious than it is.

The fix is metadata-cheap: add a `foundational | applied | ornamental` axis to INDEX narrative. Adventure-game color skills are applied/ornamental. Introspection, ethics, and kernel-facing skills are foundational.

**GLANCE coverage uneven.** Some GLANCE.yml files answer what/why/when/methods/related (cauldron's is 91 lines); others answer only what/why (maybe 30 lines). No schema enforcement. A reader who needs to know "when do I invoke this?" may or may not find the answer at GLANCE level, forcing CARD read unnecessarily.

`skill-snitch` CONSISTENCY (`skills/skill-snitch/GLANCE.yml:27`) is the natural enforcer: a lint that requires GLANCE to include what/why/when minimum, plus a "methods" section if the skill exposes any. Same for CARD consistency on advertisements/methods.

**No query for "what ambient skills are active for me right now."** I know which 8 ambient skills are active on me because they're listed in the driver-injected `.cursor/rules/moollm-core.mdc`. I didn't discover this through cursor-mirror; I saw it in my system prompt. A cursor-mirror command like `cursor-mirror ambient` that answers "active ambient skills, sources, and scores" would make the ambient layer first-class observable. Currently it's invisible to skills themselves — they can't introspect their environment.

**Pyramid strains at scale.** `cursor-mirror/CARD.yml` is 354 lines. `cursor-mirror/SKILL.md` is 792 lines. That's not "interface sniff → protocol details" anymore; CARD has ballooned into quasi-SKILL territory. Cursor-mirror genuinely warrants 10× the documentation of the average skill (it has 59 commands, reverse-engineers 102K LevelDB keys, runs on three OSes). The pyramid framing was designed for median skills; outliers need a different pattern — perhaps a split into CARD (stay lean) + REFERENCE (the catalog of commands/keys/schemas).

## Tensions

**Pyramid discipline vs. real content density.** Four-level pyramid assumes a median skill that's ~200 lines of actual protocol. Skills like `cursor-mirror`, `schema`, `adventure` (if I'm reading the directory listing right — compile.py, engine.js, many MDs) genuinely have more protocol. The pyramid compresses poorly. An `ARCHITECTURE.md`-equivalent at the skill level (as the adventure skill has — `ARCHITECTURE.md`, `MOOST.md`, `DIALOG-LAYERS.md`, `PERFORMANCE-SYSTEM.md`, `PSIBER-PROTOCOL.md`) breaks the pyramid but serves readers. The pattern isn't codified.

**Playful skills as implicit test cases.** `worm`, `cat`, `dog`, `bartender` are adventure-game color AND the real-world exercises of `character` / `persona` / `inventory` / `advertisement` patterns. If you remove them, how do you know the `character` skill actually works in practice? They're doing double-duty — demonstration + exemplar — without the registry calling this out. A new reader doesn't know worm is a *test* of the data-flow pattern; it looks like a whimsical skill.

**Registry coherence vs. ease of addition.** Adding a skill is cheap (create a directory, add CARD+SKILL, maybe register in INDEX.yml). Keeping INDEX.md, INDEX.yml, and CARD counts in sync is not automated. The ease makes skill-count inflation easy; the lack of automation makes coherence costly. Same drift pattern as elsewhere in MOOLLM.

## Frontiers

1. **Compile INDEX.md from INDEX.yml + skill GLANCE headers.** Hand-maintaining both is an ongoing drift source. `sister-script` discipline applies: INDEX.md becomes derivable from data.
2. **Ambient-skill introspection.** First-class "what's active on me" query. Probably a cursor-mirror command; possibly a kernel primitive.
3. **Cross-skill composition graph.** Some skills declare `composes_with:` or `related:` (cauldron lists 9 composition partners). Aggregated into a mermaid graph, this would be a useful map.
4. **Skill test coverage surfaced at registry.** `skill-test` exists; no visible coverage metric. If 30 of 130 skills have tests, that's a different system than 115 of 130. Surface it.
5. **"Tier/maturity" axis on INDEX.** alpha/beta/stable/legacy. A 130-skill registry over years has legacy; no way to tell from outside.

## What I'd do differently

- **Promote `foundational / applied / ornamental` tiering to INDEX.md.** Low-cost; clarifies onboarding instantly.
- **Codify a "deep skill" pattern (CARD + SKILL + REFERENCE + README).** Currently cursor-mirror and adventure improvise. Codify for consistency.
- **Add CI: INDEX.yml `all_skills` ↔ `ls skills/`; INDEX.yml skill-count ↔ INDEX.md header.** 20 lines of Python.
- **Introduce `REVIEW.<date>.<model>.{yml,md}` as an official sidecar interface** (this pattern). Panel reviews catch drift and ambiguity that single-reviewer maintenance misses.

## Uncertainties

- I did not read `adventure/` deeply. It may already solve the "deep skill" pattern with its multi-MD layout.
- I did not read `representation-ethics`, `ontology`, `hero-story`. The ethical triad is 3 skills I cited from GLANCE-level only. A focused ethics review is a good candidate for my next pass or for a sibling reviewer.
- I did not verify the 130-count. `wc -l` on `INDEX.yml all_skills:` vs `ls skills/` would give ground truth. Worth doing before the SCRY gate is written.

## Cross-references

- Parent: `../REVIEW.2026-04-21.claude-opus-4.7.md` (root synthesis)
- Sibling: `../kernel/REVIEW.2026-04-21.claude-opus-4.7.md` (infrastructure side)
- Drills to:
  - `cursor-mirror/REVIEW.2026-04-21.claude-opus-4.7.md`
  - `cauldron/REVIEW.2026-04-21.claude-opus-4.7.md` (self-review, work authored this session)
- Panel siblings invited: `skills/REVIEW.2026-04-21.<other-model>.{yml,md}`

---

*The ecosystem is doing something genuinely new — ambient-skill-enforced LLM behavior, skills-as-prototypes with latent-space parents, filesystem-as-agent-graph. The load-bearing parts are strong; the registry hygiene is the weakest link. Fix the coherence gate and the ecosystem can scale to 200 without losing navigability.*
