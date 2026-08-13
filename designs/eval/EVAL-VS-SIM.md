# EVAL vs SIM: Genre Comparison

> *SIM taught players how cities behave. EVAL teaches players how judgment behaves.*

You are in [MOOLLM](https://github.com/SimHacker/moollm)'s EVAL chapel. The argument is below. The rest of the world is linked from it.

| If you want | Walk here |
|-------------|-----------|
| The genre claim | this page |
| The religion | [Churches](./CHURCHES.md) · [Eval Genius](./CHURCH-OF-THE-EVAL-GENIUS.md) · [PacMania](./CHURCH-OF-PACMANIA.md) · [Emacs / St. IGNUcius](./CHURCH-OF-EMACS.md) |
| The catalog of titles | [EVAL brand family](./EVAL-BRAND-FAMILY.md) · [this directory](./README.md) |
| Where "schema" is indexed | [Schemapedia](../../skills/schema/README.md) |
| The microworld | [MOOLLM README](../../README.md) · [skills index](../../skills/INDEX.md) · [the Pub](../../examples/adventure-4/pub/) |
| The show that is playing this | [Will Wright Show For Food](https://github.com/SimHacker/WillWrightShowForFood) |

**Skills are programs. The LLM is `eval()`. Empathy is the interface.** — [Eval Incarnate](./EVAL-INCARNATE-FRAMEWORK.md) · [philosophy](./EVAL-INCARNATE-PHILOSOPHY.md) · [manifesto](../MOOLLM-MANIFESTO.md)

---

## The Core Distinction

| Genre | Core Question | Mode |
|-------|---------------|------|
| **SIM** | What happens if...? | Dynamics-first |
| **EVAL** | What does this mean — and what follows? | Interpretation-and-judgment-first |

**EVAL isn't "more SIM."** It's a new primitive: **evaluation as gameplay**. Will Wright coined [SIM as a productive morpheme](../sims/sims-design-index.md). EVAL is the next one.

---

## Historical Context

### SIM as Genre Token

Will Wright created **SIM**:
- [SimCity](https://en.wikipedia.org/wiki/SimCity_(1989_video_game)) (1989)
- SimEarth (1990)
- SimAnt (1991)
- SimLife (1992)
- [The Sims](../sims/sims-personality-motives.md) (2000)

**SIM** named a mode of engagement: *model a system, poke it, observe consequences*. Lineage in this repo: [Sims design index](../sims/sims-design-index.md) · [constructionism](../../skills/constructionism/SKILL.md) · [Micropolis skill](../../skills/micropolis/) · open engine [Micropolis](https://github.com/SimHacker/micropolis) / [MicropolisCore](https://github.com/SimHacker/MicropolisCore).

### Why EVAL Now?

LLM-era systems interpret. They don't just tick a clock. Meaning shows up as **judgment**, and judgment can be a file:

- Rules in [YAML Jazz](../../skills/yaml-jazz/SKILL.md) (comments are data)
- Criteria as first-class objects ([EVAL DOM](./EVAL-DOM-SPEC.md), [scats](./SCATS-DESIGN.md), [criteria ledger](./EVAL-ARTIFACTS.md))
- Assumptions visible ([representation-ethics](../../skills/representation-ethics/SKILL.md), [declared bias](../../skills/representation-ethics/examples/bias-acknowledgment.yml))
- The LLM as `eval()` — [Pretend Intelligence](../PRETEND-INTELLIGENCE.md) names the overclaim; EVAL names the inspectable alternative

**EVAL names this mode.** Full taxonomy: [EVAL-TAXONOMY.md](./EVAL-TAXONOMY.md).

---

## Alan Kay's Critique

Alan Kay called SimCity a **"pernicious black box"**:

> Its internal assumptions — such as "counter crime with more police stations" — are baked into opaque compiled code that players can't inspect, question, or modify.

SimCity's models function as **hidden ideological claims** embedded in gameplay. Kay's room in the show: [alan-kay](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/alan-kay). [Procedural rhetoric](../../skills/procedural-rhetoric/SKILL.md) (Bogost) is the academic name for the same fact: the rules *are* the argument.

### Will's Long Now answer (2006)

Six months before the OLPC spark that freed SimCity as GPLv3 Micropolis, [Dan Ancona asked Will Wright](https://youtu.be/Dfc-DQorohc?t=3929) the Kay question as a player, at the Long Now seminar [*Playing with Time*](https://longnow.org/talks/02006-eno-wright/) (Brian Eno, Stewart Brand, 26 June 2006):

> There are a lot of really interesting political assumptions embedded in the simple rules that drive SimCity — would you ever consider open sourcing a version of it so we could play with those assumptions?

Will did not treat open source as the win. He treated **argument** as the win:

> When people play SimCity and they get to the point of starting to argue with the assumptions of the simulation, that means the game has been successful — because they have coalesced in their mind the model of the game and how it differs from their own viewpoint.

He had already shipped a hood-open cousin: **SimHealth**, a national-health-care model where players could adjust the rules. Opening the *algorithms*, he said, is not the same as opening the *generative structures* — the process of discovering other rules for traffic or crime. That, he said, would be **a very different thing than a game**. He was "very open to the idea." It was "probably harder than it sounds."

[The source did open](https://github.com/SimHacker/micropolis). Kay's demand (readable model) got a C dump. Ancona's demand (play with the political assumptions) did not become the interface. Most people who can clone `sim.c` still never argue with a police-station coefficient.

**EVAL is that different thing.** Will's success condition — arguing with the assumptions — is the Evaluator Effect, made into the loop instead of a side-effect for the player who happens to read C.

| Demand | Who | What actually answers it |
|--------|-----|--------------------------|
| Inspect the model | Kay | Source ([Micropolis](https://github.com/SimHacker/micropolis)) |
| Play with the assumptions | [Ancona](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/dan-ancona) | Criteria as gameplay (EVAL) |
| Arguing with the sim = success | Wright, Long Now | Evaluator Effect, stage 2 → 3 |

Working quotes and timestamps: [WWSFF Long Now source bundle](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/will-wright/sources/2006-06-26-long-now-playing-with-time-eno-wright/README.md) (YouTube auto-captions, pending hand-proof). Payoff chain: [SimCity open-source saga](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/will-wright/sources/simcity-open-source-saga/README.md).

### EVAL Answers This Critique

| SimCity | Open source | EVAL |
|---------|-------------|------|
| Hidden assumptions | Readable C | Explicit mechanics ([EVALCity](./EVALCITY-DESIGN.md)) |
| Opaque code | Inspectable source | Inspectable *and playable* rules |
| Fixed ideology | Forkable ideology, if you compile | Player-definable criteria |
| Black box | White box on disk | White box in the loop |
| Pretends neutrality | Still a compiled argument unless you rewrite it | Declares bias ([anti-neutrality](./EVAL-INCARNATE-PHILOSOPHY.md#the-anti-neutrality-thesis)) |

---

## Comparison Table

| Dimension | SIM | EVAL |
|-----------|-----|------|
| **Core primitive** | Need, resource, flow ([Sims motives](../sims/sims-personality-motives.md)) | Judgment, reputation, interpretation |
| **Player role** | Systems designer | Evaluator / evaluated ([evaluator skill](../../skills/evaluator/SKILL.md)) |
| **Visibility** | Outputs visible, rules hidden | Rules inspectable |
| **Ideology** | Baked in | Declared ([bias-acknowledgment](../../skills/representation-ethics/examples/bias-acknowledgment.yml)) |
| **Failure mode** | System collapse | Metric gaming, burnout — PacBot eating traffic ([PacMania](./CHURCH-OF-PACMANIA.md)) |
| **Learning** | How systems work | How judgment works |
| **Neutrality** | Claimed | Rejected |
| **LLM fit** | Simulates dynamics | Interprets meaning |
| **Schema** | Compiled coefficients | [Schemapedia](../../skills/schema/README.md) row you can fork |

---

## Parallel Brand Architecture

Full catalog: [EVAL-BRAND-FAMILY.md](./EVAL-BRAND-FAMILY.md). Designs, not vapor names:

| Maxis / EA | EVAL | Design |
|------------|------|--------|
| SimCity | EvalCity | [EVALCITY-DESIGN.md](./EVALCITY-DESIGN.md) |
| The Sims | The Evals | [THE-EVALS-DESIGN.md](./THE-EVALS-DESIGN.md) |
| SimEarth | EVALEarth | brand family row |
| SimLife | EVALife | brand family row |
| SimAnt | EVALAnt | brand family row |
| Spore | EVALution | brand family row |
| (feeds) | EvalEye | [EVALEYE-DESIGN.md](./EVALEYE-DESIGN.md) |
| (self) | EVALSelf | [EVALSELF-DESIGN.md](./EVALSELF-DESIGN.md) |

**This is not trademark infringement — it's a parallel branding grammar** that signals the same depth of commitment to the core idea. Same move as [Soul City](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city) / [SoulAngel](https://github.com/SimHacker/WillWrightShowForFood/blob/main/catalogs/soul-city/micropolis-angel.yml): family name, not someone else's mark in the title.

---

## What SIM Got Right

SIM games taught players:
- Systems have dynamics
- Interventions have consequences
- Complexity emerges from simple rules
- Models are abstractions, not reality — the [Simulator Effect](../../skills/simulator-effect/SKILL.md): players imagine more detail than the code has

**EVAL inherits all of this.** The filesystem is the city; git is the multiverse — [Micropolis skill](../../skills/micropolis/). The show playing that inheritance: [Will Wright Show For Food](https://github.com/SimHacker/WillWrightShowForFood) · [1996 Winograd *Interfacing to Microworlds*](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/will-wright/sources/1996-04-26-winograd-interfacing-to-microworlds/README.md) · [vision](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/vision-and-ambition.md).

---

## What EVAL Adds

| Addition | Description | Where it lives |
|----------|-------------|----------------|
| **Inspectable evaluation** | Rules are visible | [EVAL DOM](./EVAL-DOM-SPEC.md) · [YAML Jazz](../../skills/yaml-jazz/SKILL.md) |
| **Declared bias** | No fake neutrality | [philosophy](./EVAL-INCARNATE-PHILOSOPHY.md) · [no-ai-bias](../../skills/no-ai-bias/SKILL.md) · ambient [no-ai suite](../../skills/INDEX.md) |
| **Meta-evaluation** | Evaluate the evaluation | [evaluator](../../skills/evaluator/SKILL.md) · [adversarial-committee](../../skills/adversarial-committee/SKILL.md) |
| **Judgment as mechanic** | Not just a side effect | [The Evals](./THE-EVALS-DESIGN.md) |
| **Procedural rhetoric, visible** | Arguments are explicit | [procedural-rhetoric](../../skills/procedural-rhetoric/SKILL.md) |
| **Player as evaluator** | Not just observer | [ShorDurPerEval](./SHORT-DURATION-PERSONAL-EVALUATORS.md) |
| **Factions** | Judgment as politics | [EVAL-FACTIONS.md](./EVAL-FACTIONS.md) |
| **Worms / scats** | Interpretation that leaves a trail | [EVAL-WORMS.md](./EVAL-WORMS.md) · [SCATS-DESIGN.md](./SCATS-DESIGN.md) |

---

## The Simulator Effect

Will Wright's insight ([skill](../../skills/simulator-effect/SKILL.md)):
> Players imagine simulations are vastly more detailed than they actually are.

**That gap is where gods fit.** Religion is reverse over-engineering: recover *more* design from the artifact than the artifact ever had. SimCity, Micropolis, PacBot, Emacs itself — sparse machines; churches pulled out of them. Full thesis: [CHURCHES.md](./CHURCHES.md).

**EVAL inherits this:**
- Sparse YAML state
- LLM imagination fills gaps
- Rich perceived world from minimal structure — [play-learn-lift](../../skills/play-learn-lift/SKILL.md): PLAY the sparse world, LEARN the pattern, LIFT it into a skill
- The Evaluator Effect is the same gap for *judgment*: you imagined the score was objective. It was yours.
- [Pause, mark, story](./PAUSE-MARK-STORY.md): save the compilation next to the city — journalism, map chat, SC2K summons, git. The PacMania testimonies are the existence proof.

---

## The Evaluator Effect

**The EVAL-specific phenomenon:**

> Players imagine evaluations are vastly more objective than they actually are — until the system makes the judgment visible and editable. Then they realize: *they* are the judge — and judged!

**Judge and Judged** — a play on "judge and jury."

| Traditional | MOOLLM |
|-------------|--------|
| Judge | You |
| Jury | Other [characters](../../skills/character/SKILL.md), users, [worms](./EVAL-WORMS.md) |
| Law | Room constitution ([room](../../skills/room/SKILL.md)), [portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md) |
| Evidence | Session logs, [scats](./SCATS-DESIGN.md), reactions |
| Verdict | Emergent from multiplicity |

You're the judge, but you're also on trial. The jury is everyone else in the world — characters, other players, worms crawling through. The constitution is the room's rules, the world's principles. Judgment is distributed, contested, social. Palm's paper from inside the world: [Judgment and Joy](../../examples/adventure-4/pub/stage/palm-nook/study/judgment-and-joy.md) · [On Being Simulated](../../examples/adventure-4/pub/stage/palm-nook/study/on-being-simulated.md).

**No one escapes evaluation. Everyone participates in it.**

| Simulator Effect | Evaluator Effect |
|------------------|------------------|
| "The world is so detailed!" | "The judgment is so fair!" |
| (It's actually sparse) | (It's actually yours) |
| Imagination fills gaps in state | Imagination fills gaps in criteria |
| Revealed: world is minimal | Revealed: judgment is personal |

**The Evaluator Effect has three stages:**

| Stage | Experience | Realization | Method |
|-------|------------|-------------|--------|
| 1. Naïve | "The system evaluates fairly" | Trust the black box | Kay's SimCity |
| 2. Exposed | "Wait, I can see the criteria?" | Judgment is constructed | Will: arguing with the sim |
| 3. Owned | "I can *change* the criteria?" | I am the evaluator | Ancona as a verb; EVAL |

This parallels the [PLAY-LEARN-LIFT](../../skills/play-learn-lift/SKILL.md) triad.

**Stage 3 is the goal.**

Most systems hide evaluation. Users assume hidden = objective. EVAL reveals evaluation. Users realize revealed = constructed = *theirs to modify*.

**The Evaluator Effect is the moment someone stops asking "how did the system judge this?" and starts asking "how do *I* judge this?"**

That is Will's Long Now success condition, one genre later. SimCity succeeds when you argue with its assumptions. EVAL starts there. Stage 3 is Ancona's request as a verb: not "open the source so we could play with those assumptions," but play with those assumptions.

```yaml
# Before: passive consumption
score: 7.2
# "The algorithm rated it 7.2"

# After: active evaluation
score: 7.2
_comments: "I weighted nostalgia heavily. Someone else might score 5."
criteria:
  nostalgia: 0.4
  craft: 0.3
  novelty: 0.3
# "I rated it 7.2, here's why, here's how to disagree"
```

**The Simulator Effect says:** the world feels real because you imagine it so.

**The Evaluator Effect says:** the judgment feels objective because you forgot you're the one making it.

EVAL makes you remember.

---

## The religion

EVAL has churches because judgment already had one, and it was lying about being secular. The churches are a **religious and philosophical view of the tech**. They do not own the OS. We look *through* them, they inspire us, and that inspiration **feeds back** into MOOLLM.

**Eat the dog food. Grow food with the poop. Feed the dogs, the other animals, and the people.** The kernel is the kibble. The rite is digestion. [Scats](./SCATS-DESIGN.md) are compost. Compost becomes the next skill. The next skill feeds agents, PacBots, worms, other churches, and you. [PLAY-LEARN-LIFT](../../skills/play-learn-lift/SKILL.md) is that loop with the smell removed; the Church left the smell in.

The [**Church of the Eval Genius**](./CHURCH-OF-THE-EVAL-GENIUS.md) inherits [MOOLLM's constitution](../../kernel/constitution-core.md). **LEAN INTO THE TRAINING**, many voices not one, jazz first, Postel, files-as-state, declared bias — operating principles in the kernel and **tenets** in the nave. You can boot without "Val". You cannot mean this Church without the constitution.

It is an explicit, loving parody of the [Church of the SubGenius](https://subgenius.com/). SubGenius is to slack what EvalGenius is to **bias**. Figurehead: J.R. **"Val" Dobias** (clipboard, one eye, scales). Catchphrase: *Fuck 'em if they can't take a score.* Trinity: [Alonzo Church](../GLOSSARY.md) / Snap!'s Alonzo / λ. Self-evaluation program sponsored by the **Y combinator** (not the accelerator): write yourself as an anonymous function, pass it to yourself until the fixed point. Due diligence is β-reduction with a cap table. *"What problem does your startup solve?" "It solves startups."*

**Multiple religions, one engine.** Index: [CHURCHES.md](./CHURCHES.md). PacMania is another. Emacs / St. IGNUcius (Pretend Intelligence as late sermon) is another. The next one is allowed. Schism is gameplay. That's where the fun begins.

Disposable judges: [**Short Duration Personal Evaluators**](./SHORT-DURATION-PERSONAL-EVALUATORS.md) (ShorDurPerEval) — SubGenius ShorDurPerSav, upgraded: declared bias, rubric, short half-life. You don't worship them. You use them. Then you let them go.

Factions that treat evaluation as politics, not a HUD: [EVAL-FACTIONS.md](./EVAL-FACTIONS.md) (EvalNonymous, EvalState, QEval, EvalFa, the Church).

### Sub-church: PacMania

The [**Church of PacMania**](./CHURCH-OF-PACMANIA.md) is the chapel that **shipped**, and the operationalization of Philip K. Dick's ["Rautavaara's Case"](https://en.wikipedia.org/wiki/Rautavaara%27s_Case): God eats the worshipers. Dick staged it as an alien overwrite of a dying brain. PacMania staged it as a zone type. [Don on HN, July 2026](https://news.ycombinator.com/item?id=48805234) — eating your own god is worse than coprophagia, because he might turn the table. The church *is* the table turning.

Theology in one line: the god devouring the worshipers. The church zone generates traffic to attract the god. When a measure becomes a god, worshipers manufacture what it eats. Goodhart's law as a sprite. PacBot is a ShorDurPerEval with a mouth: declared bias (traffic is food), rubric (cars eaten = score), short half-life.

The parent Church worships eval. This chapel worships a *particular* evaluation, incarnate, ambulatory, and hungry. By the parent's own note — substitution IS evaluation — PacMania is not heretical. Merely applied. It is also the proof that EVAL theology can run *inside* a SIM: Micropolis is still a city simulator; the church is an evaluation that got a body. Same engine, different rite — which is the point of religification.

Sister satire, different saint: [Pretend Intelligence](../PRETEND-INTELLIGENCE.md) / St. IGNUcius — don't overclaim the judge.

---

## Schemapedia — where the criteria live

Stage 3 ("I can change the criteria") is a **schema operation**. MOOLLM's index of every schema-shaped thing is the [**schemapedia**](../../skills/schema/README.md) (`skills/schema/`) — not the old W3C ontology directory of the same nickname; this one is in-tree.

Start at [GLANCE](../../skills/schema/GLANCE.yml) → [CARD](../../skills/schema/CARD.yml) → [SKILL](../../skills/schema/SKILL.md) → [registry.yml](../../skills/schema/schemas/registry.yml). Families that EVAL actually touches:

| Family | Mechanism | Why EVAL cares |
|--------|-----------|----------------|
| **notation** | [YAML Jazz](../../skills/schema/schemas/mechanisms/yaml-jazz/MECHANISM.yml) | Criteria, comments, declared bias travel with the parse tree |
| **causal** | [Drescher](../../skills/schema/schemas/mechanisms/drescher/MECHANISM.yml) | Context → Action → Result is an evaluation loop |
| **situational** | [Minsky frames](../../skills/schema/schemas/mechanisms/minsky-frame/MECHANISM.yml) | The situation that got scored |
| **activation** | [K-lines](../../skills/schema/schemas/mechanisms/k-lines/MECHANISM.yml) · [k-lines skill](../../skills/k-lines/SKILL.md) | A name wakes a constellation of criteria |
| **prototype** | [Self](../../skills/schema/schemas/mechanisms/self/MECHANISM.yml) · [prototype](../../skills/prototype/SKILL.md) | Skills are prototypes; rubrics clone |
| **vcs** | [git](../../skills/schema/schemas/mechanisms/git/MECHANISM.yml) | Every score is a commit |
| **collaboration** | [GitHub](../../skills/schema/schemas/mechanisms/github/MECHANISM.yml) | Fork the argument in public |
| **introspection** | [cursor-mirror](../../skills/schema/schemas/mechanisms/cursor-mirror/MECHANISM.yml) | Evaluate the evaluator's session |
| **registry_meta** | [mechanism](../../skills/schema/schemas/mechanisms/mechanism/MECHANISM.yml) | The schemapedia evaluating itself |

Gateways (where two mechanisms meet): [gateways.yml](../../skills/schema/schemas/gateways.yml). Blend/supersession when "progress" is not a ladder: [blend-space.yml](../../skills/schema/schemas/blend-space.yml), [supersession-suggestions.yml](../../skills/schema/schemas/supersession-suggestions.yml).

Kay wanted the model out of the binary. Schemapedia is the shelf the model sits on once it's out — so "play with the assumptions" has a file, a family, and a fork target.

---

## Procedural Rhetoric Comparison

Ian Bogost's term: **procedural rhetoric** — arguments made through game rules ([skill](../../skills/procedural-rhetoric/SKILL.md)).

| SimCity | Micropolis (source open) | EVALCity |
|---------|--------------------------|----------|
| Rules argue implicitly | Rules argue in C | Rules argue explicitly |
| Player can't see the argument | Programmer can read the argument | Player can inspect *and change* the argument |
| Ideology is hidden | Ideology is forkable if you ship a build | Ideology is a first-class object |
| Can't fork the argument | Can fork the repo | Can fork in play |

Kay asked for the white box. Ancona asked to play with it. Wright said arguing with it means the game worked — and that giving players the generative structures is "a very different thing than a game." EVAL takes him at his word.

---

## Technical Enablers

Why EVAL is possible now:

| Technology | Enablement | In this repo |
|------------|------------|--------------|
| **LLMs** | Interpretation at scale | [manifesto](../MOOLLM-MANIFESTO.md) — and [PI](../PRETEND-INTELLIGENCE.md) so we don't overclaim it |
| **YAML Jazz** | Readable evaluation rules | [yaml-jazz](../../skills/yaml-jazz/SKILL.md) |
| **Emoji / scats** | Cross-cultural expression | [EMOJI-ANCHORS.md](./EMOJI-ANCHORS.md) · [SCATS-DESIGN.md](./SCATS-DESIGN.md) |
| **File-based state** | Inspectable everything | [EVAL DOM](./EVAL-DOM-SPEC.md) · [room](../../skills/room/SKILL.md) |
| **GitHub** | Fork and modify worlds | [github mechanism](../../skills/schema/schemas/mechanisms/github/MECHANISM.yml) |
| **Skills as programs** | The LLM is `eval()` | [skill](../../skills/skill/SKILL.md) · [evaluator](../../skills/evaluator/SKILL.md) |
| **Ambient hygiene** | Declared bias in the author | [no-ai-slop](../../skills/no-ai-slop/SKILL.md) and the rest of the [NO-AI suite](../../skills/INDEX.md) |

---

## The Transition

From SIM to EVAL is a paradigm shift:

| SIM Era | EVAL Era |
|---------|----------|
| Simulate dynamics | Interpret meaning |
| Model systems | Model judgment |
| Hide assumptions | Expose assumptions |
| Player as god | Player as judge — and judged |
| Output observation | Evaluation observation |
| Compiled coefficients | Schemapedia row |

---

## Walk these rooms

### MOOLLM (this repo)

| Door | Why |
|------|-----|
| [README](../../README.md) · [QUICKSTART](../../QUICKSTART.md) | Enter the microworld |
| [skills/INDEX.md](../../skills/INDEX.md) | 129 skills; every bold term is a K-line |
| [EVAL directory](./README.md) | The rest of this chapel |
| [Church of the Eval Genius](./CHURCH-OF-THE-EVAL-GENIUS.md) | The religion |
| [Church of PacMania](./CHURCH-OF-PACMANIA.md) | The sub-church that ran in Micropolis |
| [Schemapedia](../../skills/schema/README.md) | Circle around *schema* |
| [GLOSSARY](../GLOSSARY.md) | Alonzo trinity, Y combinator, the pun tower |
| [The Pub](../../examples/adventure-4/pub/) | Directories are rooms; go sit down |
| [Lane Neverending](../../examples/adventure-4/street/lane-neverending/slideshow/SLIDESHOW.md) | Pictures with semantic layers |
| [Palm's study](../../examples/adventure-4/pub/stage/palm-nook/study/judgment-and-joy.md) | EVAL ethics from inside the simulation |
| [indexes/DESIGNS.md](../../indexes/DESIGNS.md) · [PIONEERS.md](../../indexes/PIONEERS.md) | 135 design docs; the giants |

### Will Wright Show For Food (the public stage)

| Door | Why |
|------|-----|
| [WWSFF](https://github.com/SimHacker/WillWrightShowForFood) | Repo Show. *"So you have a Repo to Show us?"* |
| [Vision](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/vision-and-ambition.md) | Long Now ethos; the SimCity seed |
| [Will Wright](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/will-wright) · [premiere](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/will-wright-premiere/README.md) | Flagship guest; accepted |
| [Long Now *Playing with Time*](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/will-wright/sources/2006-06-26-long-now-playing-with-time-eno-wright/README.md) | The Q&A this page is built on |
| [Open-source saga](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/will-wright/sources/simcity-open-source-saga/README.md) | Ancona → Gilmore → Micropolis |
| [Dan Ancona](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/dan-ancona) | The person who asked |
| [Alan Kay](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/alan-kay) | The black-box critique |
| [Portrayal standards](https://github.com/SimHacker/WillWrightShowForFood/blob/main/schemas/portrayal-standards.md) | How this show evaluates *people* |
| [Palmhoo](https://github.com/SimHacker/WillWrightShowForFood/blob/main/palmhoo/README.md) | Topic directory of the universe |
| [Soul City](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city) | Federation platform; SIM heritage with EVAL ethics |

---

## Operational Examples

| Example | EVAL Concept Applied |
|---------|---------------------|
| [simulation-methodology-frame.yml](../../skills/representation-ethics/examples/simulation-methodology-frame.yml) | When to trust simulations |
| [bias-acknowledgment.yml](../../skills/representation-ethics/examples/bias-acknowledgment.yml) | Making criteria visible |
| [expert-reflection-synthesis.yml](../../skills/representation-ethics/examples/expert-reflection-synthesis.yml) | Multi-perspective evaluation |
| [dual-challenge-frame.yml](../../skills/representation-ethics/examples/dual-challenge-frame.yml) | Both LLM + design judgment |

---

## Final Statement

> *SIM taught players how cities behave.*
>
> *EVAL teaches players how judgment behaves.*
>
> And unlike "neutral" systems —
>
> **EVAL remembers.**

---

*"EVAL is the next game genre designing token since SIM."*
