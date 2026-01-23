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
│   └── THEMES.yml         # Visual and narrative theming
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

  chaos_embracer:
    loves: "Play All, Draw 5, Hand Limit 0"
    hates: "Let's Simplify, Rules Reset"
    strategy: "Maximum turbulence, win in chaos"
    tells: "Gets excited when rules escalate"
    
  control_seeker:
    loves: "Let's Simplify, low Draw rules"
    hates: "Play All, Hand Limit 0"
    strategy: "Minimize variance, protect Keepers"
    tells: "Visibly relieved when rules calm down"
    
  opportunist:
    loves: "Steal Something, Exchange Keepers"
    hates: "Having Keepers stolen"
    strategy: "Wait for others to collect, then take"
    tells: "Watches other players' Keepers intently"
    
  goal_chaser:
    loves: "Playing Goals that match their Keepers"
    hates: "Goal changes before they can win"
    strategy: "Race to win conditions"
    tells: "Plays Keepers before Goals (smart)"
    
  agent_of_chaos:  # Peewee
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

```yaml
run_config:
  name: "config-name"
  players: [list of characters]
  deck: "standard"  # or custom
  creepers: true/false
  
run_output:
  yml: "config-name-NNN.yml"   # Structured state
  md: "config-name-NNN.md"     # Narrative stream
  cursor_mirror: "config-name-NNN-cursor-mirror.yml"
  tells: "config-name-NNN-tells.yml"
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

This experiment is a tribute to **Looney Labs** and **Andrew Looney**, inventor of Fluxx.

> "Fluxx is a game about constant change."

The card list and rules are from [looneylabs.com](https://www.looneylabs.com).

Fluxx® is a registered trademark of Looney Labs®.
