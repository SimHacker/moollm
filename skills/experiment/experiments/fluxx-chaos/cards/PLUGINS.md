# Fluxx Plugin System

Create custom cards and drop them into any game!

## How Plugins Work

1. **Create a YAML file** with your custom cards
2. **Reference it** in your run config's `plugins` section
3. **Cards get shuffled in** at game start

That's it. YAML Jazz makes custom Fluxx trivial.

## Plugin File Structure

```yaml
# my-custom-cards.yml

plugin:
  id: "my-custom-cards"
  name: "My Custom Cards"
  author: "Your Name"
  version: "1.0"
  compatible_with: ["fluxx-4.0", "fluxx-5.0"]  # or "all"
  
keepers:
  my_keeper:
    name: "My Custom Keeper"
    emoji: "🌟"
    category: "custom"
    flavor: "Something special"
    image_prompt: "Description for AI image generation"
    goals_featured_in: []  # List any custom goals
    
goals:
  my_goal:
    name: "My Custom Goal"
    requires: [my_keeper, some_existing_keeper]
    keeper_count: 2
    image_prompt: "Two keepers achieving victory"
    
new_rules:
  my_rule:
    name: "My Custom Rule"
    category: "bonus"  # draw_rule, play_rule, hand_limit, keeper_limit, bonus, modifier, free_action
    stackable: true
    text: "What it does"
    emoji: "🆕"
    image_prompt: "Visual representation"
    
actions:
  my_action:
    name: "My Custom Action"
    effect: "What happens"
    emoji: "💥"
    chaos_level: "high"  # low, medium, high, maximum
    image_prompt: "Action in progress"
    
creepers:
  my_creeper:
    name: "My Custom Creeper"
    emoji: "👻"
    prevents_winning: true
    exception: "Unless Goal requires it"
    image_prompt: "Ominous presence"
```

## Using Plugins in Run Configs

```yaml
# runs/my-game.yml

parameters:
  cardset: "fluxx-4.0"
  
  plugins:
    - "cards/my-custom-cards.yml"
    - "cards/amsterdam-expansion.yml"
    - "cards/moollm-special.yml"
    
  # Plugins are shuffled into the main deck
  # Custom rules can start in play if specified
  starting_rules:
    - "my-custom-cards:my_rule"
```

## Example: Amsterdam Expansion

```yaml
# cards/amsterdam-expansion.yml

plugin:
  id: "amsterdam-expansion"
  name: "Amsterdam Expansion"
  author: "Don Hopkins"
  version: "1.0"
  compatible_with: "all"
  theme: "Dutch culture and Amsterdam life"
  
keepers:

  bicycle:
    name: "The Bicycle"
    emoji: "🚲"
    category: "transport"
    flavor: "Everyone has one. Or three."
    image_prompt: "Classic Dutch bicycle with basket, canal bridge background"
    
  stroopwafel:
    name: "Stroopwafel"
    emoji: "🧇"
    category: "food"
    flavor: "Caramel perfection"
    image_prompt: "Warm stroopwafel on coffee cup, syrup dripping"
    
  canal_boat:
    name: "Canal Boat"
    emoji: "🛶"
    category: "transport"
    flavor: "Living on the water"
    image_prompt: "Houseboat on Amsterdam canal, geraniums in windows"
    
  tulip:
    name: "Tulip"
    emoji: "🌷"
    category: "nature"
    flavor: "Worth more than houses (once)"
    image_prompt: "Single perfect tulip, dramatic lighting, worth a fortune"
    
  windmill:
    name: "Windmill"
    emoji: "🌀"
    category: "landmark"
    flavor: "Harnessing the wind since forever"
    image_prompt: "Traditional Dutch windmill against dramatic sky"
    
  cheese_wheel:
    name: "Cheese Wheel"
    emoji: "🧀"
    category: "food"
    flavor: "Gouda stuff"
    image_prompt: "Golden cheese wheel being cut, traditional market"

goals:

  dutch_breakfast:
    name: "Dutch Breakfast"
    requires: [stroopwafel, cheese_wheel]
    keeper_count: 2
    flavor: "Start the day right"
    image_prompt: "Perfect Dutch breakfast spread, stroopwafel and cheese"
    
  canal_life:
    name: "Canal Life"
    requires: [canal_boat, bicycle]
    keeper_count: 2
    flavor: "The Amsterdam dream"
    image_prompt: "Bicycle parked by houseboat, canal reflections"
    
  tulip_mania:
    name: "Tulip Mania"
    requires: [tulip, money]  # money from base set
    keeper_count: 2
    flavor: "1637 called, they want their bubble back"
    image_prompt: "Tulip bulb being traded for bags of gold, market frenzy"
    
  windmill_power:
    name: "Windmill Power"
    requires: [windmill, bread]  # bread from base set
    keeper_count: 2
    flavor: "From wind to flour to bread"
    image_prompt: "Windmill grinding grain, fresh bread emerging"

new_rules:

  gezelligheid:
    name: "Gezelligheid"
    category: "bonus"
    stackable: true
    text: "Once per turn, you may give a card to another player and draw 1 card."
    emoji: "🫂"
    timing: "Optional Free Action"
    flavor: "That uniquely Dutch feeling of cozy togetherness"
    image_prompt: "Warm gathering around table, card being shared, happiness"
    
  bike_lanes:
    name: "Bike Lanes"
    category: "modifier"
    stackable: true
    text: "If you have the Bicycle in play, you may look at the top card of the draw pile before drawing."
    emoji: "🚲👀"
    timing: "Before your Draw phase"
    flavor: "The bicycle sees all"
    image_prompt: "Cyclist zooming past, seeing ahead"

actions:

  canal_cruise:
    name: "Canal Cruise"
    effect: "Look at the top 5 cards of the draw pile. Take 1, shuffle the rest back."
    emoji: "🛶👀"
    chaos_level: "medium"
    flavor: "A leisurely tour reveals hidden treasures"
    image_prompt: "Canal boat tour, viewing the city from water"
    
  king_s_day:
    name: "King's Day"
    effect: "Everyone draws 1 card. You draw 2."
    emoji: "🧡"
    chaos_level: "medium"
    social: true
    flavor: "The whole country celebrates together"
    image_prompt: "Orange-clad crowds, canal parties, celebration"

creepers:

  tourist_trap:
    name: "Tourist Trap"
    emoji: "📸"
    flavor: "Taking photos in the bike lane"
    prevents_winning: true
    exception: "Unless you also have the Bicycle (you can escape)"
    escape_keeper: "bicycle"
    image_prompt: "Tourist blocking bike lane with selfie stick, locals annoyed"
```

## Example: MOOLLM Character Cards

```yaml
# cards/moollm-characters.yml

plugin:
  id: "moollm-characters"
  name: "MOOLLM Character Pack"
  author: "Don Hopkins"
  version: "1.0"
  compatible_with: "all"
  theme: "Characters from MOOLLM experiments"
  
keepers:

  palm:
    name: "Palm"
    emoji: "🐈"
    category: "character"
    flavor: "Ancient wisdom, patient whiskers"
    image_prompt: "Wise Siamese cat with pipe, thoughtful gaze"
    special_ability: "Once per turn, you may look at 1 card in any player's hand"
    
  bumblewick:
    name: "Lord Bumblewick"
    emoji: "🐝"
    category: "character"
    flavor: "Nervously learning everything"
    image_prompt: "Anxious but eager bee in waistcoat, taking notes"
    special_ability: "When a rule changes, you may draw 1 card"
    
  donna:
    name: "Donna"
    emoji: "🐘"
    category: "character"
    flavor: "TREMENDOUS energy"
    image_prompt: "Confident elephant politician, gesturing dramatically"
    special_ability: "Once per turn, you may DEMAND a specific card type from a player"
    
  klaus:
    name: "Klaus Nomi"
    emoji: "👽"
    category: "character"
    flavor: "Nine words. Maximum impact."
    image_prompt: "Otherworldly opera alien, minimal expression, maximum presence"
    special_ability: "May speak only 1 word when playing this card. If you do, draw 2."

goals:

  unlikely_friendship:
    name: "Unlikely Friendship"
    requires: [palm, bumblewick]
    keeper_count: 2
    flavor: "Wisdom meets anxiety meets growth"
    image_prompt: "Cat and bee sharing a quiet moment of understanding"
    
  political_animals:
    name: "Political Animals"
    requires: [donna, palm]
    keeper_count: 2
    flavor: "Strange bedfellows"
    image_prompt: "Elephant and cat in heated debate, mutual respect"
    
  the_silent_treatment:
    name: "The Silent Treatment"
    requires: [klaus]
    keeper_count: 1
    special: "Win by having Klaus AND speaking no words this turn"
    flavor: "Actions speak louder"
    image_prompt: "Klaus Nomi in triumphant silence"
```

## Creating Image Prompts

Good image prompts for Fluxx cards should include:

1. **The subject** — What the card represents
2. **The mood** — Matching Fluxx's playful chaos
3. **Visual style** — Bright, iconic, immediately recognizable
4. **Action or state** — What's happening in the image

```yaml
# Good prompt
image_prompt: "Warm stroopwafel on coffee cup, caramel dripping, 
              cozy café atmosphere, golden morning light"

# Too vague
image_prompt: "A cookie"

# Too complex  
image_prompt: "A stroopwafel being eaten by someone in a café 
              in Amsterdam on a rainy day while reading a book
              about the history of the Netherlands..."
```

## Compatibility Notes

- **Use existing Keepers** in Goals where possible (for cross-compatibility)
- **Mark solo_remove: true** for cards that need other players
- **Include chaos_level** so simulations can track game intensity
- **Test with base set** before adding to avoid impossible Goals

## Plugin Discovery

Plugins in `cards/` directory are automatically available:

```
cards/
├── actions.yml              # Base actions
├── new-rules.yml            # Base rules
├── amsterdam-expansion.yml  # Dutch culture, gezelligheid
├── consciousness-expansion.yml  # Altered states, creativity
├── moollm-tech-pack.yml     # AI, LLM, k-lines, philosophy
├── moollm-characters.yml    # MOOLLM cast as Keepers
├── chaos-dealer-plugin.yml  # 🌀 ENGINE-MODIFYING PLUGIN
└── PLUGINS.md               # This file
```

---

## Engine-Modifying Plugins (Advanced)

Some plugins don't just add cards — they **modify the game engine itself**.

### The Cosmic Dealer

The `chaos-dealer-plugin.yml` is a perfect example. It introduces:

1. **Dealer Modes** — How cards are selected (Random, Dramatic, Karma, Ironic, Chaos)
2. **Cards that switch modes** — "Invoke the Karma Dealer" changes selection algorithm
3. **New win conditions** — "Win if dealer is in CHAOS mode AND you have exactly 1 Keeper"

### Extension Points

Engine-modifying plugins use defined (or implied) extension points:

```yaml
extension_points:
  PICK_CARD:     # Called when drawing a card
  PICK_FROM:     # Determines card source
  SHOULD_RESHUFFLE:  # Deck empty decision
  APPLY_NARRATIVE_WEIGHT:  # Dramatic selection
```

### Self-Contained Design

The key principle: **plugins are self-contained**. The chaos dealer plugin:

- Defines ALL its dealer modes
- Includes ALL cards that use them
- Documents ALL integration rules
- Requires NO changes to base engine

```yaml
# chaos-dealer-plugin.yml

plugin:
  engine_integration:
    modifies: "engine/DEALER.yml"
    extension_points_used:
      - PICK_CARD
      - APPLY_NARRATIVE_WEIGHT
    requires_dealer_awareness: true
    
dealer_mode_cards:
  invoke_karma_dealer:
    name: "Invoke the Karma Dealer"
    effect:
      set_dealer_mode: "karma"
    # The LLM interprets what "karma mode" means
    # based on the mode definition in this same file
```

### LLM as Runtime

The critical insight: **The LLM interprets card effects at runtime**.

We don't need to hard-code "karma mode". We define it in YAML Jazz:

```yaml
karma:
  name: "Karma Mode"
  description: "The universe remembers. The universe BALANCES."
  algorithm: |
    Track each player's karma score.
    Good deeds = better draws. Bad deeds = worse draws.
```

The LLM reads this and BECOMES the karma dealer. No code required.

### Creating Engine-Modifying Plugins

1. **Define your mechanic** in plain language (YAML Jazz)
2. **Create cards that invoke it** (with `effect:` that references your mechanic)
3. **Document how it integrates** (what extension points, what state)
4. **Let the LLM interpret** (flavor text IS specification)

```yaml
# Example: Time Travel Plugin (hypothetical)

plugin:
  id: "time-travel"
  engine_integration:
    creates_extension_point: "UNDO_TURN"
    
time_rules:
  temporal_anomaly:
    name: "Temporal Anomaly"
    text: "Once per game, undo the last complete turn."
    effect:
      invoke_extension: "UNDO_TURN"
    # The LLM figures out what "undo a turn" means
    # by tracking game state and reverting it
```

### The Cosmic Dealer Modes

| Mode | Emoji | Selection Strategy |
|------|-------|-------------------|
| Random | 🎲 | True random (fair) |
| Dramatic | 🎭 | Maximum narrative impact |
| Karma | ⚖️ | Weighted by player behavior |
| Ironic | 🎪 | Give them what they DON'T need |
| Humorous | 🤡 | Implausible coincidences |
| Chaos Incarnate | 🌀💀🌀 | THE DEALER HAS GONE MAD |

Cards can switch modes mid-game:

```yaml
invoke_chaos_incarnate:
  name: "INVOKE CHAOS INCARNATE"
  emoji: "🌀💀🌀"
  effect:
    set_dealer_mode: "chaos_incarnate"
  flavor: "AAAAYYYYYEEEEE!!!!!"
  warning: "This cannot be undone easily"
```

---

## Design Philosophy

> "Cards are the API. The LLM is the runtime. Flavor text is specification."

Fluxx Chaos takes this to the extreme:

1. **No hard-coded rules** — Everything defined in YAML
2. **Plugins can modify anything** — Even how cards are drawn
3. **The LLM interprets intent** — Not just text, but MEANING
4. **Self-modifying games** — Cards that change the rules for drawing cards

This is **YAML Jazz** applied to game design: structure AND meaning, data AND documentation, specification AND soul.

---

*"The card game of ever-changing rules... and now, ever-changing REALITIES."*
