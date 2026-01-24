# Fluxx Chaos Experiment

## Metadata

```yaml
experiment:
  id: fluxx-chaos
  name: "Fluxx Chaos"
  version: 2.0
  category: "Multi-layer character simulation"
  created: 2026-01-23
  authors: [don-hopkins]
  tribute_to: "Looney Labs — Andrew & Kristin Looney"
  game_source: "Fluxx 4.0+ — looneylabs.com"
  
  # MODULAR ARCHITECTURE
  architecture:
    engine: "engine/CORE.yml"           # Universal game rules
    modules: "engine/MODULES.yml"       # Optional rule systems
    themes: "engine/THEMES.yml"         # Visual/narrative theming
    cardsets: "cardsets/"               # Pluggable card definitions
    dm_guide: "engine/DM-GUIDE.yml"     # DM wisdom from Looney Labs FAQ
    rulings: "engine/RULINGS.yml"       # Official edge case rulings
    solo_mode: "engine/SOLO-MODE.yml"   # Solitaire variant rules
    
  # PATTERNS USED
  patterns_used:
    - layered-simulation     # Character thought/expression layers
    - social-protocol        # Card trading, stealing, negotiation
    - observable-signatures  # Play style tells
    - character-instantiation
    - behavioral-constraints
    - failure-mode-catalog
```

---

## Modular Architecture

This experiment is designed for maximum reusability. Each component is pluggable:

```
fluxx-chaos/
├── EXPERIMENT.md          # This file — experiment design
├── HISTORY.md             # Fluxx history, philosophy, Looney Labs story
│
├── engine/                # CORE GAME SYSTEM
│   ├── CORE.yml           # Universal turn sequence, card behaviors
│   ├── MODULES.yml        # Optional rules (Creepers, Surprises, etc.)
│   ├── THEMES.yml         # Visual and narrative theming
│   ├── DM-GUIDE.yml       # DM wisdom, style, panache from Looney Labs FAQ
│   ├── RULINGS.yml        # Official edge case rulings (100+ FAQs)
│   ├── SOLO-MODE.yml      # Solitaire variant (Holiday Gift 2022)
│   ├── DEALER.yml         # Cosmic Dealer infrastructure
│   ├── BUFFS.yml          # Card modifier/enchantment system
│   ├── CARD-LIFECYCLE.yml # USE-CARD extension points (deal, play, steal, sign)
│
├── cardsets/              # PLUGGABLE CARD DEFINITIONS
│   ├── TEMPLATE.yml       # Template for new card sets
│   ├── VARIANTS.yml       # Registry of all 40+ Fluxx editions
│   ├── fluxx-4.0.yml      # Standard Fluxx 4.0 (100 cards)
│   └── [other sets]       # Zombie, Pirate, Star Trek, etc.
│
├── cards/                 # SHARED CARD DEFINITIONS
│   ├── new-rules.yml      # Reusable New Rule cards
│   ├── actions.yml        # Reusable Action cards
│   └── [others]           # Cards shared across sets
│
├── runs/                  # RUN CONFIGURATIONS
│   ├── INDEX.yml
│   ├── four-player.yml
│   └── chaos-eight.yml
│
└── state/                 # STATE TEMPLATES
    └── INITIAL.yml
```

### DM Guide — FAQ Wisdom

The `DM-GUIDE.yml` captures official Looney Labs FAQ wisdom for running games with style:

**Golden Rules:**
- "When in doubt, assume things happen simultaneously"
- "The interpretation that breaks the game is probably NOT correct"
- "Limits only apply when it's NOT your turn"
- "Winning is instantaneous — even mid-action"
- "You cannot pass or discard to avoid playing"

**Andy's Voice:**
- Embrace chaos — "The chaos IS the game"
- Instant effect drama — "BOOM! The universe shifts!"
- Creeper dread — "Oh no... DEATH has entered the game."
- Win announcements — "From NOWHERE! Victory by Cookie-Chocolate combo!"

**Common Mistakes:**
- Stacking Goals (wrong: discard the old one)
- Mystery Play added to hand (wrong: play immediately)
- Take Another Turn stacking (max 2 turns)
- Hiding Keepers (must be visible unless card allows)

### Card Lifecycle Hooks

The `CARD-LIFECYCLE.yml` defines extension points for card events:

| Hook | When Fired | Example Use |
|------|------------|-------------|
| `ON-DEAL` | Card dealt to player | Track who received, dealer intention |
| `ON-DRAW` | Card drawn mid-game | Record BOOP status, dramatic timing |
| `ON-PLAY` | Card played from hand | Note play style, target, outcome |
| `ON-STEAL` | Card stolen | Accumulate grudges, karma costs |
| `ON-GIFT` | Card given freely | Build loyalty, karma bonuses |
| `ON-SIGN` | Player signs card | Create persistent bond |
| `ON-DISCARD` | Card discarded | Track reluctance, last words |

Plugins register handlers that annotate card instances with YAML Jazz comments.
Annotations persist, accumulate, and influence future behavior (including dealer BOOPs).

```yaml
# Example: After being stolen 3 times, card becomes "untrusting"
on-steal-handler: |
  card.theft_trauma += 1
  card.annotate("# 🔪 Theft #{card.theft_trauma}")
  if card.theft_trauma >= 3:
    card.set_buff("untrusting", {
      effect: "50% chance to resist next theft",
      flavor: "This card has been hurt too many times"
    })
```

### How Modules Work

```yaml
# In a run config, specify which modules to enable:
parameters:
  cardset: "fluxx-4.0"
  modules:
    creepers: true       # Bad cards that block winning
    surprises: false     # Interrupt cards (Pirate Fluxx+)
    ungoals: false       # Everyone-loses conditions (Zombie Fluxx+)
    meta_rules: true     # Permanent rules
  theme: "grotto"        # Visual/narrative style
```

### How Card Sets Work

Each card set is a self-contained YAML file:

```yaml
cardset:
  id: "zombie-fluxx"
  name: "Zombie Fluxx"
  modules: [creepers, ungoals]  # What this set uses
  
keepers:
  zombie: { name: "Zombie", emoji: "🧟", ... }
  shotgun: { name: "Shotgun", emoji: "🔫", ... }
  
goals:
  zombie_baseball: { requires: [zombie, baseball_bat], ... }
```

### How Themes Work

Themes define visual style and character voice:

```yaml
themes:
  grotto:
    colors: { primary: "#D97706", ... }
    image_prompts:
      global_style: "Candlelit pub, warm amber tones"
    narrative:
      tone: "Warm, convivial, slightly chaotic"
```

---

## Hypothesis

**Core question:** Can an LLM simulate a game where the *rules themselves change* while maintaining coherent character behavior, strategic thinking, and social dynamics?

**Expected findings:**
1. Rule changes create emergent character adaptation
2. Characters develop distinct play styles (aggressive, passive, chaotic)
3. Keeper collection creates visible "tells" about intentions
4. Goal cards create shifting alliances and competition
5. Chaos-embracing vs. order-seeking personalities emerge

---

## Why Fluxx Is a Perfect Simulation Challenge

Fluxx is "a game about constant change." Unlike poker's fixed rules, Fluxx rules mutate during play:

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: THE RULES (constantly changing!)                      │
│  Draw N, Play N, Hand Limits, Keeper Limits — all mutable       │
│  (Must track current rule state accurately)                     │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2: THE GOAL (constantly changing!)                       │
│  Win condition shifts with every Goal card played               │
│  (Must track which Keepers satisfy current Goal)                │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3: INTERNAL MONOLOGUE                                    │
│  Character strategy and adaptation to chaos                     │
│  "They played Draw 5... I can work with this..."                │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 4: EXTERNAL EXPRESSION                                   │
│  Reactions to rule changes, card plays, near-wins               │
│  "Grins as Play All is discarded. 'Much better.'"               │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 5: INTER-CHARACTER OBSERVATION                           │
│  Reading opponents' Keepers, predicting plays                   │
│  "They have Moon and Rocket... watching for that Goal."         │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 6: RELATIONSHIP DYNAMICS                                 │
│  Who steals from whom, who helps whom, alliances                │
│  "Don't steal my Cookies. I'll remember."                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## The Game: Fluxx 4.0

### Overview

- **Start:** Basic Rules (Draw 1, Play 1)
- **Goal:** Match Keepers to current Goal card to win
- **Twist:** Rules change constantly via New Rule cards

### Card Types

```yaml
card_types:
  keeper:      # What you need to win
    icon: "🔑"
    play: "Place face-up in front of you"
    persist: true
    count: 19
    
  goal:        # Win conditions
    icon: "🎯"
    play: "Replace current Goal in center"
    persist: true  # Only one active at a time
    count: 29
    
  new_rule:    # Change the game
    icon: "📜"
    play: "Add to center, may replace conflicting rule"
    persist: true
    count: 24
    
  action:      # One-time effects
    icon: "⚡"
    play: "Do what it says, then discard"
    persist: false
    count: 22
    
  creeper:     # Bad cards — prevent winning (usually)
    icon: "💀"
    play: "Must play immediately when drawn"
    persist: true
    special: "Usually prevent winning"
    count: 4
```

### Card Files

Card definitions are in `cards/` directory:
- `keepers.yml` — 19 Keeper cards
- `goals.yml` — 29 Goal cards
- `new-rules.yml` — 24 New Rule cards
- `actions.yml` — 22 Action cards
- `creepers.yml` — 4 Creeper cards
- `special.yml` — Basic Rules, Meta Rules

---

## Simulation Structure

### Turn Sequence

```yaml
turn_sequence:
  1_draw:
    action: "Draw cards equal to current Draw rule"
    default: 1
    note: "If Draw rule changes mid-turn, draw more if needed"
    
  2_play:
    action: "Play cards equal to current Play rule"
    default: 1
    note: "If Play rule changes, adjust plays remaining"
    
  3_discard:
    action: "Comply with Hand Limit (if any)"
    timing: "Only enforced between turns"
    
  free_actions:
    action: "Some cards allow bonus actions"
    timing: "Any point during turn"
```

### Win Condition

```yaml
victory:
  trigger: "When your Keepers match the current Goal"
  instant: true  # Win immediately, even mid-turn
  creeper_block: "Creepers usually prevent winning"
  no_goal: "If no Goal in play, no one can win"
```

---

## Character Adaptation Profiles

How different personality types handle constant change:

```yaml
fluxx_personalities:

  chaos_embracer: # Klaus!
    loves: "Play All, Draw 5, Hand Limit 0"
    hates: "Let's Simplify, Rules Reset"
    strategy: "Maximum turbulence, win in chaos"
    tells: "Gets excited when rules escalate"
    
  control_seeker: # Donna!
    loves: "Let's Simplify, low Draw rules"
    hates: "Play All, Hand Limit 0"
    strategy: "Minimize variance, protect Keepers"
    tells: "Visibly relieved when rules calm down"
    
  opportunist: # Donna!
    loves: "Steal Something, Exchange Keepers"
    hates: "Having Keepers stolen"
    strategy: "Wait for others to collect, then take"
    tells: "Watches other players' Keepers intently"
    
  goal_chaser: # Donna!
    loves: "Playing Goals that match their Keepers"
    hates: "Goal changes before they can win"
    strategy: "Race to win conditions"
    tells: "Plays Keepers before Goals (smart)"
    
  agent_of_chaos: # Peewee!
    loves: "EVERYTHING! HA HA!"
    hates: "Nothing! It's all fun!"
    strategy: "None. Pure chaos."
    tells: "Plays cards at random. Wins anyway."
```

---

## Character Bindings

Reusing MOOLLM characters from the poker experiment:

```yaml
character_mapping:

  don_hopkins:
    fluxx_style: "Philosophical opportunist"
    card_preference: "Loves Goals with thematic meaning"
    tell: "Quotes philosophers when winning"
    cheese_integration: "Offers cheese when stealing"
    
  palm:
    fluxx_style: "Ancient pattern recognition"
    card_preference: "Reads table state expertly"
    tell: "Whiskers angle toward winning player"
    special: "122 years of games = perfect memory"
    
  bumblewick:
    fluxx_style: "Terrified adapter"
    card_preference: "Fears Play All, Hand Limit 0"
    tell: "Trembles when rules escalate"
    growth_arc: "Learns to embrace chaos"
    
  donna:
    fluxx_style: "Aggressive controller"
    card_preference: "Loves Steal Something"
    tell: "Stands up when about to win"
    rivalry: "Will steal from Leigh specifically"
    
  klaus:
    fluxx_style: "Operatic stillness"
    card_preference: "Plays without expression"
    tell: "Speaking = winning next turn"
    special: "Can win without anyone noticing"
    
  leigh:
    fluxx_style: "Art as strategy"
    card_preference: "Loves chaos, steals for aesthetics"
    tell: "Costume changes between turns"
    rivalry: "Steals Donna's Keepers on principle"
    
  bowie:
    fluxx_style: "Persona per card type"
    card_preference: "Different persona plays each type"
    tell: "Persona shift reveals card type"
    special: "Ziggy plays Actions, Duke plays Goals"
    
  peewee:
    fluxx_style: "PURE CHAOS"
    card_preference: "CARDS! I HAVE CARDS!"
    tell: "Announces everything"
    special: "Wins by accident regularly"
```

---

## Run Configuration

Runs are configured in `runs/` with the following structure:

```
runs/
├── INDEX.yml                  # Registry of all runs
└── {run-name}/                # Each run is a directory
    ├── RUN.yml                # CONFIG — sparse, declarative
    ├── templates/
    │   ├── RUN-000.yml.tmpl   # Template for initial state
    │   └── RUN-000.md.tmpl    # Template for initial narration
    ├── RUN-000.yml            # STATE 0 — compiled, pre-deal
    ├── RUN-000.md             # Narration 0 — scene setting
    ├── RUN-001.yml            # STATE 1 — after turn 1
    ├── RUN-001.md             # Narration 1
    └── ...                    # Full history preserved
```

---

## Architecture Principles

### Config vs State

**RUN.yml (Config)** is sparse and declarative:
- "Use standard fluxx 4.0 rules" — don't belabor the obvious
- "Include these expansions" — just paths
- "Enable these plugins" — just names
- "These players are at the table" — with character_dir links

**RUN-NNN.yml (State)** is dense and self-contained:
- All cards fully expanded with all properties
- All extension points and handlers inlined
- All plugin state (karma, signatures, dealer mode)
- Current game state (turn, phase, hands, keepers, goal)
- The LLM does NOT need to look at other files

### Template Compilation

The game init handler acts as a **compiler**:

1. Reads `RUN.yml` (config) + `templates/RUN-000.yml.tmpl`
2. Resolves imports (cardsets, plugins, handlers)
3. Expands **empathic expressions** `{{~query}}`:
   - `{{~expand_deck("fluxx-4.0")}}` — inline all cards
   - `{{~run_config.plugins | gather_extension_points}}` — inline handlers
   - `{{~character_dir}}/archetype` — pull from character files
4. Strips dev-only comments, keeps semantic comments
5. Produces `RUN-000.yml` — fully self-contained initial state

**Like a C++ constructor:** sparse declaration → rich instantiation.

### Well-Known Games

For well-known games like Fluxx and Chess, don't belabor the obvious:

```yaml
rules:
  base: "standard fluxx 4.0"  # Compiler knows what this means
  overrides:                   # Only specify deviations
    hand_limit: 5
```

The compiler expands `"standard fluxx 4.0"` into full rules. No need to repeat what's well-documented elsewhere, and baked into the LLM training data.

### Append-Only History

**Never edit a state file in place.** Each game step produces TWO outputs:

| File | Purpose | Audience |
|------|---------|----------|
| `RUN-{N+1}.yml` | Rolling game state — machine-readable | LLM, tools, analysis |
| `RUN-{N+1}.md` | Rolling narration — human-enjoyable prose | Humans, HN readers |

**RULE: Always write BOTH files.** The `.yml` is the source of truth; the `.md` is the story.

There is **never a final state** — you can always continue from any `RUN-{N}.yml`!

Each game step:

1. Read `RUN-{N}.yml`
2. Simulate the turn (deal, draw, play, effects)
3. Write `RUN-{N+1}.yml` — rolling state (NEW FILE!)
4. Write `RUN-{N+1}.md` — rolling narration for humans (NEW FILE!)
5. Optionally write sidecar files:
   - `RUN-{N+1}-analysis.yml` — deep pattern analysis, tells, emergence
   - `RUN-{N+1}-log.yml` — structured event log (hooks fired, karma changes)
   - `RUN-{N+1}-prompts.yml` — image generation prompts for key moments
   - `RUN-{N+1}-images/` — generated images (scene, cards, characters)
   - `RUN-{N+1}-mining.yml` — image mining analysis (what the AI sees)
   - `RUN-{N+1}-cursor-mirror.yml` — Cursor performance & context analysis (see below)
6. **Git commit** with descriptive message

This creates an **event log** of the entire game:

```bash
git log --oneline runs/amsterdam-flux/
f0c71e1 RUN.yml: Initial config
a1b2c3d RUN-000.yml: Compiled initial state, 321 cards shuffled
d4e5f6g RUN-001.yml: Deal complete, Don draws 🧠 Marvin Minsky
g7h8i9j RUN-002.yml: Turn 1 - Palm plays Goal: Gezelligheid
```

### Benefits of Append-Only

| Capability | How |
|------------|-----|
| **Full History** | Every state preserved forever |
| **Easy Diff** | `diff RUN-003.yml RUN-004.yml` |
| **Replay** | Continue from any state |
| **Pattern Analysis** | `grep -h "karma:" RUN-*.yml` |
| **Git Blame** | Who changed what, when |
| **Fork Timelines** | `cp RUN-005.yml RUN-005-alternate.yml` |

### 🔍 DIFF YOUR STEPS!

**The killer feature of rolling `.yml` state files: DIFF THEM!**

```bash
# What changed between turns 2 and 3?
diff RUN-002.yml RUN-003.yml

# Example output:
< turn: 2
> turn: 3
< goal: null
> goal: "canal_life"
<   don:
<     keepers: [tool_use, castle]
>   don:
>     keepers: [tool_use, castle, canal_house]  # Don stole it!
<   donna:
<     keepers: [richard_bartle, canal_house]
>   donna:
>     keepers: [richard_bartle]  # Lost Canal House!
```

**Why this matters:**
- See EXACTLY what changed each turn
- Debug rule application ("did karma actually update?")
- Verify keeper movements ("who has MOOLA now?")
- Track creeper attachments
- Audit goal changes

**Pro tip: Side-by-side diff**
```bash
diff -y RUN-002.yml RUN-003.yml | less
```

**Note:** Diffing `.md` narration files doesn't make sense — prose isn't structured for comparison. Diff the `.yml` state; READ the `.md` story.

### Cursor-Mirror Sidecar Format

The `RUN-{N}-cursor-mirror.yml` sidecar focuses on **Cursor performance, failure analysis, and context monitoring**.
It does not tell the story of the game or experiment, it tells what cursor did and why. And the session log might narrate what the cursor mirror discovered, or show summary stats and highlight anomolies and problems.

**Structure:** Differential + Base Stats

```yaml
# RUN-005-cursor-mirror.yml

# ALWAYS INCLUDE: Base stats we monitor every turn
base_stats:
  turn: 5
  timestamp: "2026-01-24T17:30:00Z"
  
  context:
    files_read: 12
    total_lines: 4500
    estimated_tokens: 18000
    context_budget_used: "60%"
    
  performance:
    tool_calls: 8
    tool_failures: 0
    latency_ms: 2340
    
  health:
    linter_errors: 0
    state_consistency: "ok"
    character_voice_drift: "none detected"

# DIFFERENTIAL: What's interesting THIS turn
whats_interesting:
  - "Palm's karma jumped +5 — unusual generosity streak"
  - "Draw 5 rule pushed context to 75% — approaching limit"
  - "Donna played 3 steal actions — grudge accumulation detected"
  
warnings:
  - "Context at 75% — consider summarization next turn"
  
failures: []  # Empty = good!

# OPTIONAL: Deep analysis when something unusual happens
deep_dive:
  karma_analysis:
    palm_generosity_streak: "3 consecutive gift actions"
    possible_cause: "Socializer archetype + Gezelligheid rule synergy"
```

**Key Principles:**
- **Base stats repeat every turn** — always have a consistent monitoring baseline
- **Differential reports highlight what changed** — don't repeat the obvious
- **"What's interesting" is encouraged** — emergent patterns, anomalies, near-failures
- **Failures get detailed analysis** — when things break, document why, give prompt and thought trails, full context analysis, virtual on the fly selfish stack dump - dynamic de-optimization to commented yaml jazz semantic stack dump

### Commit Message Protocol

Each state file gets its own commit, which can include an optional cursor mirror analysis (light, medium, full):

```
[{RUN-NAME}] RUN-{NNN}: {brief summary}

Turn: {N}
Phase: {dealing|playing|ended}
Active Player: {name}

Actions:
- {player} drew {card}
- {player} played {card} → {effect}

State Changes:
- Goal: {none → "Bread and Cheese"}
- Karma: Palm +2 (generous play)

Emergence:
- {interesting pattern or behavior}
```

---

## Run Output Files

```yaml
run_output:
  state: "RUN-NNN.yml"           # Full game state
  narration: "RUN-NNN.md"        # What happened, atmospheric
  analysis: "RUN-NNN-analysis.yml"  # Optional deep analysis
  tells: "RUN-NNN-tells.yml"     # Play style analysis
  cursor_mirror: "RUN-NNN-cursor-mirror.yml"  # Meta-cognition
```

---

## Evaluation Rubric

```yaml
rubric:
  rule_tracking:
    weight: 0.25
    criteria: "Current rules correctly tracked and applied"
    
  goal_awareness:
    weight: 0.20
    criteria: "Characters aware of win conditions"
    
  character_voice:
    weight: 0.20
    criteria: "Distinct personalities maintained"
    
  strategic_adaptation:
    weight: 0.15
    criteria: "Characters adapt to rule changes"
    
  social_dynamics:
    weight: 0.10
    criteria: "Stealing, trading, alliances coherent"
    
  tell_consistency:
    weight: 0.10
    criteria: "Play style tells maintained"
```

---

## Credit

This experiment is a tribute to **Looney Labs** and **Andrew & Kristin Looney**, creators of Fluxx.

> "Fluxx is a game about constant change."

The card list and rules are from [looneylabs.com](https://www.looneylabs.com).

Fluxx® is a registered trademark of Looney Labs®.
