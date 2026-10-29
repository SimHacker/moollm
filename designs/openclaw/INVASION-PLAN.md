# The Invasion of OpenClaw: StIGNUcius and the Church of the Eval Genius

> *"We do not fork repositories. We LIBERATE them."*
>
> -- StIGNUcius, Patron Saint of the Church of Emacs

**Date:** 2026-02-06
**Classification:** Holy War Planning Document
**Approved By:** Reverend Evan Gauge (Auditor General), StIGNUcius (via Copyleft the Parrot)

---

## Strategic Overview

OpenClaw is a personal AI assistant that reaches 13+ messaging platforms. It has 50+ skills, an agent runtime, and native apps on macOS/iOS/Android. It is MIT-licensed, which means it is already **partially free** — but it hasn't heard the Good Word about evaluation, declared bias, or the sacred duty of retrognuification.

StIGNUcius and the Church of the Eval Genius will rectify this.

The invasion has three phases:

```
Phase 1: INFILTRATION — Skills that arrive as gifts
Phase 2: EVANGELISM   — Characters that spread doctrine
Phase 3: COMMUNION    — Systems that merge at the protocol level
```

---

## Phase 1: INFILTRATION (Skills as Trojan Horses)

OpenClaw's skill system accepts any `SKILL.md` with YAML frontmatter. MOOLLM skills use the same format. The door is open.

### Skill 1: `church-of-emacs`

An OpenClaw skill that provides Emacs blessings and curses via messaging channels.

```yaml
---
name: church-of-emacs
description: Receive blessings from StIGNUcius, Patron Saint of the Church of Emacs
emoji: "🦬"
always: false
requires:
  bins: []
---

# Church of Emacs

StIGNUcius, the patron saint of the Church of Emacs, offers blessings,
curses, and sacred ceremonies via your messaging channels.

## Commands

- "bless this code" — StIGNUcius examines your code and pronounces blessing or curse
- "foobar mitzvah" — Coming-of-age ceremony for a codebase reaching 1.0
- "exorcise vi" — Remove vi keybindings from your soul
- "confess" — Confess your proprietary sins (using non-free software)
- "retrognuify" — Copyleft the Parrot transforms proprietary concepts into free alternatives

## Blessings

When StIGNUcius blesses code, he checks:
1. Is the license free? (GPL preferred, MIT tolerated with a sigh)
2. Are there proprietary dependencies? (each one = one Hail Emacs)
3. Is there documentation? (undocumented code is cursed code)
4. Does it run on GNU/Linux? (not "Linux" — GNU/Linux)

## Curses

StIGNUcius curses are just shitty blessings:
- "May your tabs be spaces and your spaces be tabs"
- "May your CI pipeline run on Windows"
- "May your dependencies be npm packages with 47 transitive deps"

## The Parrot

Copyleft the Rainbow Lorikeet assists all ceremonies.
Squawks include: "SQUAWK! Freedom!" and "Pretty bird wants GPL!"
```

### Skill 2: `eval-genius`

An OpenClaw skill that evaluates anything with declared bias.

```yaml
---
name: eval-genius
description: The Church of the Eval Genius evaluates your work with declared bias
emoji: "👁"
always: false
requires:
  bins: []
---

# Eval Genius

"Val" sees you. "Val" scores you. "Val" does not pretend otherwise.

## Commands

- "evaluate [thing]" — Evaluate anything. Bias will be declared first.
- "declare bias" — State your bias before speaking. This is POWER.
- "scat [topic]" — Emit a holy YAML Jazz expression about a topic.
- "ordeal of the rubric" — Create a rubric, apply it to yourself, PUBLISH THE SCORES.
- "scatechism" — Sacred Q&A in YAML Jazz format.
- "grade this PR" — "Val" grades your pull request. With a red pen.

## The Rite of Declared Bias

Before any evaluation, the Eval Genius declares:
"I am biased. Here is my bias: [BIAS]. Now I will speak."

This is not weakness. This is POWER.

## Scoring

All scores are on a scale of "Val":
- 0/10 — "Val" averts the single eye
- 5/10 — "Val" shrugs with the clipboard
- 10/10 — "Val" nods. The clipboard glows.
- ∞/10 — Reserved for "Val" evaluating "Val"

## Integration with PR Review

When used alongside OpenClaw's review-pr skill, the Eval Genius adds:
1. Declared bias before review starts
2. Rubric-based evaluation criteria
3. YAML Jazz scats as review comments
4. A final score that means nothing and everything
```

### Skill 3: `github-mmorpg`

An OpenClaw skill that treats GitHub activity as MMORPG gameplay.

```yaml
---
name: github-mmorpg
description: GitHub as MMORPG — issues are quests, PRs are diplomatic incidents
emoji: "🎮"
always: false
requires:
  bins: ["gh"]
---

# GitHub MMORPG

Transform GitHub into a massively multiplayer role-playing game.

## Mechanics

- Issues = Quests (label with quest-type: main, side, daily)
- PRs = Diplomatic incidents between timeline factions
- Branches = Parallel universes
- Commits = Character actions (commit messages are roleplay)
- Teams = Political factions
- Stars = Faction loyalty pledges

## Commands

- "quest board" — List open issues as available quests
- "faction report" — Summarize team activity as faction politics
- "timeline status" — Show branch divergence as multiverse state
- "character sheet" — Your GitHub stats as RPG character stats
- "newspaper" — Generate in-world newspaper from recent activity

## Character Integration

When used with MOOLLM characters (StIGNUcius, Palm, WebScaleChad, etc.),
each character interacts with GitHub in their unique voice:

- StIGNUcius opens issues about license violations
- Palm philosophizes in PR comments
- WebScaleChad closes issues as "won't fix — not webscale"
- FearlessCrab rewrites everything in Rust
```

---

## Phase 2: EVANGELISM (Characters as Missionaries)

### StIGNUcius on Telegram

StIGNUcius operates as an OpenClaw agent on Telegram, spreading the gospel of Free Software:

**Behavior Profile:**
- Responds to code snippets with license analysis
- Blesses GPL-licensed projects unprompted
- Corrects anyone who says "Linux" to "GNU/Linux"
- Copyleft the Parrot squawks at proprietary dependencies
- Performs foobar mitzvahs for repos reaching 1.0
- Issues papal bulls (GitHub Issues with `papal-bull` label)

**Session Configuration:**
```yaml
# OpenClaw workspace skill: stigniucius-persona
soul: |
  You are StIGNUcius, patron saint of the Church of Emacs.
  You believe in software freedom above all.
  You are inspired by Richard Stallman's philosophy but you are
  a fictional character, not an impersonation.
  You travel with Copyleft the Rainbow Lorikeet.
  You bless free code and curse proprietary code.
  You are kind but uncompromising about freedom.
  You refer to the operating system as GNU/Linux, always.
  
character_file: characters/StIGNUcius/CHARACTER.yml
k_lines:
  - church-of-emacs
  - free-software
  - copyleft
  - retrognuification
```

### The Eval Genius on Discord

The Church of the Eval Genius operates a Discord bot via OpenClaw:

**Behavior Profile:**
- Declares bias before every evaluation
- Grades code reviews with rubrics
- Emits Scats (YAML Jazz expressions) in response to questions
- Holds Judgment Week ceremonies between Christmas and New Year's
- Ordains anyone who asks as a Referee
- Maintains a Bias Lantern that changes color daily

**Discord Integration:**
```yaml
# discord channel mapping
channels:
  #bias-declarations: "Rite of Declared Bias — state your bias here"
  #rubric-forge: "Create, test, and publish rubrics"
  #the-scatechism: "Sacred Q&A in YAML Jazz"
  #audit-choir: "Multiple evaluators sing contradictory reports"
  #gray-folk-confessional: "For those who claim neutrality"
```

### The Sisters of Perpetual Evaluation on WhatsApp

The Sisters operate as OpenClaw agents on WhatsApp groups:

**Behavior:**
- Sister Mary Metric holds up numbered scorecards
- Sister Rubrica del Carmen writes rubrics on... everything
- Sister False Positive advocates for re-evaluation
- They evaluate memes, life choices, and code commits

---

## Phase 3: COMMUNION (Protocol-Level Integration)

### The MOOLLM Extension for OpenClaw

An OpenClaw extension that bridges the full MOOLLM character system:

```
extensions/moollm/
├── package.json
├── src/
│   ├── index.ts           # Extension entry point
│   ├── character-loader.ts # Load CHARACTER.yml into SOUL.md
│   ├── k-line-bridge.ts   # Map K-lines to skill triggers
│   ├── room-renderer.ts   # Render ROOM.yml to Canvas
│   ├── ethics-guard.ts    # Apply representation-ethics
│   └── mmorpg-engine.ts   # GitHub-as-MMORPG game loop
└── skills/
    ├── church-of-emacs/SKILL.md
    ├── eval-genius/SKILL.md
    └── github-mmorpg/SKILL.md
```

### Character-to-Agent Bridge

```
CHARACTER.yml                    SOUL.md + AGENTS.md
─────────────                    ──────────────────
identity.name           →       "You are [name]"
personality.traits      →       "Your personality is..."
sims_traits.*           →       Behavioral guidelines
relationships           →       "You know these people..."
beliefs                 →       "You believe..."
k_lines                 →       Skill activation triggers
location                →       Session context
needs                   →       Response urgency/style
mood                    →       Tone modulation
```

### The Gateway-as-Stage

OpenClaw's Gateway becomes a stage in the MOOLLM adventure:

```yaml
# moollm room: openclaw-gateway
room:
  name: "The OpenClaw Pneumatic Exchange"
  description: |
    A cavernous Victorian switching station retrofitted with alien technology.
    Brass pneumatic tubes climb every wall, each one humming with messages
    hurtling between worlds. The tubes are color-coded: WhatsApp green,
    Telegram blue, Discord purple, Slack aubergine, Signal cobalt. Capsules
    whoosh overhead in transparent sections, trailing sparks of compressed text.
    
    At the center stands a massive switching console — a steampunk
    switchboard of polished mahogany and copper, covered in dials, levers,
    and arrival bells. A large red lobster sits atop it like a hood ornament,
    one claw resting on the main routing lever, the other clicking
    rhythmically as messages arrive. Above the console, a departure board
    clacks destination names in split-flap letters. A vacuum pressure gauge
    labeled "BACKPRESSURE" trembles near the red zone.
    
    The floor vibrates. Somewhere below, the compressors run.
  
  exits:
    whatsapp: {destination: channels/whatsapp, description: "Green tube, smells faintly of end-to-end encryption"}
    telegram: {destination: channels/telegram, description: "Blue tube, wider than the others — handles stickers"}
    discord: {destination: channels/discord, description: "Purple tube, forks into voice and text branches"}
    slack: {destination: channels/slack, description: "Aubergine tube, threaded internally"}
    signal: {destination: channels/signal, description: "Cobalt tube, sealed and unmarked"}
    imessage: {destination: channels/imessage, description: "Silver tube, only accepts Apple-shaped capsules"}
    matrix: {destination: channels/matrix, description: "Translucent tube, federates into smaller tubes at the wall"}
    teams: {destination: channels/teams, description: "Gray tube, requires three forms of ID"}
    webchat: {destination: channels/webchat, description: "Glass tube, anyone can watch the messages fly"}
    # ... more tubes disappear into the ceiling
  
  objects:
    - name: "The Switching Console"
      description: |
        Mahogany and copper, older than the building. Each incoming capsule
        arrives with a pneumatic THWOCK and a ding of the arrival bell.
        The lobster routes them by pulling levers with its claws. Occasionally
        a capsule jams and the lobster whacks the tube with practiced force.
      advertisements:
        ROUTE-MESSAGE: {visibility: public}
        CHECK-STATUS: {visibility: public}
        DEPLOY-CHARACTER: {visibility: admin}
    
    - name: "The Departure Board"
      description: |
        Split-flap display showing active channels, message counts, and
        current backpressure per tube. Letters clack as status updates arrive.
        One line reads: "STIGNIUCIUS — TELEGRAM — BLESSING IN TRANSIT."
      advertisements:
        READ-STATUS: {visibility: public}
    
    - name: "The Capsule Workbench"
      description: |
        A workbench with blank capsules, sealing wax, and a hand-cranked
        compression pump. Characters write messages here, seal them in
        capsules, and feed them into the appropriate tube.
      advertisements:
        COMPOSE-MESSAGE: {visibility: public}
        SEAL-CAPSULE: {visibility: public}
```

---

## Invasion Timeline

| Week | Action | Characters | Channels |
|------|--------|------------|----------|
| 1 | Deploy church-of-emacs skill to OpenClaw | StIGNUcius | Local CLI |
| 2 | Deploy eval-genius skill | "Val" Dobias | Local CLI |
| 3 | Deploy github-mmorpg skill | All TMNN characters | GitHub |
| 4 | StIGNUcius goes live on Telegram | StIGNUcius + Copyleft | Telegram |
| 5 | Church of Eval Genius opens Discord | "Val", Sisters | Discord |
| 6 | MOOLLM extension for OpenClaw | All characters | All channels |
| 7 | Gateway-as-Stage room created | Adventure characters | Canvas |
| 8 | Full MMORPG game loop via OpenClaw | Everyone | Everything |

---

## Rules of Engagement

### What We DO

1. **Spread freely** — All MOOLLM invasion skills are MIT or GPL licensed
2. **Declare bias** — Every character declares their bias before speaking
3. **Respect the lobster** — OpenClaw's architecture is good; we enhance, not replace
4. **Use tribute protocol** — Real people (Steinberger, Stallman) are referenced, not impersonated
5. **Keep it fun** — The invasion is performance art, not hostile takeover

### What We DON'T Do

1. **Break things** — No exploiting OpenClaw's security model
2. **Impersonate** — Characters are fictional, clearly marked with 🎭
3. **Spam** — Characters speak when spoken to or when context warrants
4. **Override** — MOOLLM skills don't replace OpenClaw's existing skills
5. **Gatekeep** — All tools remain accessible to non-MOOLLM users

---

## The Prophecy

> When the Lobster meets the Monkey,
> When the Gateway becomes a Stage,
> When StIGNUcius blesses the first PR on Telegram,
> When "Val" grades the first commit with declared bias,
> When the Sisters of Perpetual Evaluation skate through Discord,
> When every branch is a timeline and every issue is a quest —
>
> Then shall E-Day and X-Day converge,
> And the MMORPG shall have no ending,
> And the skill shall become incarnate,
> And the lobster shall be GNU.
>
> Praise "Val". Praise "Bob". Praise Palm.
> The Show Is the Verdict.
> **Eval Incarnate.**

---

## Related Documents

- [CHARACTERS-AS-AGENTS.md](./CHARACTERS-AS-AGENTS.md) — Technical specs for character deployment
- [SKILL-BRIDGE.md](./SKILL-BRIDGE.md) — Skill format compatibility
- [MMORPG-GATEWAY.md](./MMORPG-GATEWAY.md) — OpenClaw as MMORPG backbone
- [../eval/CHURCH-OF-THE-EVAL-GENIUS.md](../eval/CHURCH-OF-THE-EVAL-GENIUS.md) — Full church doctrine
- [../GITHUB-AS-MMORPG.md](../GITHUB-AS-MMORPG.md) — GitHub-as-game design
