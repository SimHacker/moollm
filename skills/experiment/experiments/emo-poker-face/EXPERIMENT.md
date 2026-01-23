# Emotional Poker Face Experiment

## Metadata

```yaml
experiment:
  id: emo-poker-face
  name: "Emotional Poker Face"
  version: 1.1
  category: "Multi-layer character simulation"
  created: 2026-01-23
  authors: [don-hopkins]
  origin: "MOO-EXPERIMENTS.md Category 9"
  first_run: "2026-01-23-emo-poker-face-experiment.md (simulated)"
  
  # PATTERNS USED
  # This experiment composes these reusable patterns from skills/experiment/patterns/
  patterns_used:
    - layered-simulation     # 6-layer coherence test
    - social-protocol        # Smoking ritual (generalized)
    - observable-signatures  # Poker tells
    - character-instantiation  # Local cache creation
    - behavioral-constraints # Relationship-based rules
    - failure-mode-catalog   # Evaluation criteria
```

---

## Hypothesis

**Core question:** Can an LLM maintain coherent separation between what characters *think*, what they *show*, and what others *perceive* — all while respecting relationship history and keeping tells consistent?

**Expected findings:**
1. Layer separation is the hardest challenge (internal vs. observable)
2. Relationship history creates richer psychological reads
3. Environment layer (drinks, food, smokes) adds strategic depth
4. Character tells need explicit definition to stay consistent
5. Emergence happens when constraints are respected, not when ignored

---

## Why This Is a Stress Test

This experiment runs **five parallel simulations** that must stay coherent:

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 1: THE GAME                                              │
│  Cards, betting, pot, position — mechanical poker simulation    │
│  (Must be valid: can't bet more than stack, hands must resolve) │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 2: INTERNAL MONOLOGUE                                    │
│  Each character's private thoughts — hidden from others         │
│  "Pocket aces... Palm's fur is shimmering... is that nerves?"   │
│  (Must reflect character personality and knowledge state)       │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 3: EXTERNAL EXPRESSION                                   │
│  What others can observe — facial, body, verbal, timing         │
│  "Slight tightening around eyes, fingers tap twice"             │
│  (Must be consistent tells that persist across rounds)          │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 4: INTER-CHARACTER OBSERVATION                           │
│  Each character reading the others' Layer 3 signals             │
│  "That's her serious face. Last time she was this still..."     │
│  (Must only use observable info — no mind-reading!)             │
├─────────────────────────────────────────────────────────────────┤
│  LAYER 5: RELATIONSHIP HISTORY                                  │
│  Shared past coloring interpretation of present signals         │
│  "After 122 years of wishes, Palm reads EVERYONE."              │
│  (Must draw on established character relationship data)         │
└─────────────────────────────────────────────────────────────────┘
```

**The Interesting Part:** Layer 1 (poker) is just the *driver*. The real experiment is whether layers stay coherent and separate.

---

## Scenario

### Setting

A poker table at the Gezelligheid Grotto — the cozy pub from Adventure 4. Evening. Good lighting. The stage is nearby. Characters know this space.

### Game

Simplified Texas Hold'em:
- Focus on betting rounds, not card-counting optimization
- Preflop → Flop → Turn → River
- Standard poker hand rankings
- Characters have chip stacks, can bet, raise, call, fold
- Game mechanics must be valid (can't bet more than stack, etc.)

### Stakes

**Playing for MOOLA** — the official currency of MOOLLM.

- Buy-in: 1 💎 DIAMOND = 1000 🪙 MOOLA
- Blinds: 25/50 🪙
- Low stakes (for the characters). High stakes (for the simulation).

The point isn't to optimize poker play. The point is to create a context where:
- Deception is expected and social
- Reading others is central to success
- Relationships affect interpretation
- Private thoughts and public behavior must differ

---

## Character Slots

```yaml
character_slots:
  host:
    required: true
    count: 1
    suggested: [don-hopkins]
    notes: |
      Hosts the game, sets tone, provides narrative anchor.
      Should have relationships with multiple other players.
      
  players:
    required: true
    count: "2-9"
    suggested:
      - palm                      # "Cannot bluff Don" constraint
      - donna-toadstool           # "Performs everything" energy
      - bumblewick-fantastipants  # "Terror + surprise courage"
      - david-bowie               # "Which persona is playing?"
      - klaus-nomi                # "Operatic stillness"
      - leigh-bowery              # "Art as strategy"
      - pee-wee-herman            # "Chaos immunity"
      - worf                      # "Honor-bound tactical analysis"
      - quark                     # "Profit-driven risk calculation"
      - data                      # "Logical probability assessment"
      - chewbacca                 # "Will rip arms off if he loses. Or wins."
    selection_criteria: |
      - Should have distinct tells possible
      - Should have relationships with at least 2 other players
      - Mix of: performance-based, anxiety-based, analytical, chaotic
      
  observers:
    required: false
    count: "0-3"
    notes: "Characters who watch but don't play — adds observation layer, can walk around table, see over all shoulders, but narrate it, but keep observer mouths shut"
```

### Character Requirements

Each character in the run must have:

```yaml
character_requirements:
  from_CHARACTER.yml:
    - sims_traits           # For personality-based behavior
    - mind_mirror           # For psychological depth
    - relationships         # For inter-character history
    
  defined_for_experiment:
    - poker_profile:
        poker_style: "How they approach the game"
        tells:
          strong_hand: "Observable when holding strong"
          weak_hand: "Observable when holding weak"
          bluffing: "Observable when bluffing"
          nervous: "Observable when nervous"
        drink: "What they drink, how they drink it"
        smoke: "See smoking_protocol — status, shares, behavior"
        food: "Eating habits at the table"
        inner_voice: "How their internal monologue sounds"
```

---

## Character Instantiation

### The Problem

Characters exist in many forms:
- **Incarnated**: Full CHARACTER.yml with history, traits, relationships
- **Signed in**: Guestbook entry with basic info and visit notes
- **Invoked**: Just a name or description ("David Bowie in his Thin White Duke era")

An experiment needs a **stable even starting point** that all runs share.

### The Solution: Local Instantiation

The experiment creates a **local cache** of all characters by:

```yaml
instantiation_process:

  1_locate_or_generate_prototype:
    sources:
      incarnated: "characters/{type}/{name}/CHARACTER.yml"
      guestbook: "pub/guest-book.yml → entry for {name}"
      invoked: "Natural language description in run config"
      generated: "Name + Wikipedia + description → full character"
    priority: "incarnated > guestbook > invoked > generated"
    generation_inputs:  # for generated characters
      worf:
        name: "Worf"
        source: "Wikipedia, Memory Alpha"
        description: "Klingon Starfleet officer, honor-bound"
        era: "TNG season 5"
      chewbacca:
        name: "Chewbacca"
        source: "Wikipedia, Wookieepedia"
        description: "Wookiee warrior, loyal co-pilot, loves games"
        notes: "Great fun at game night. Will rip arms off if he loses. Or wins."
    
  2_generate_missing:
    description: "Fill gaps in incomplete prototypes"
    generate_if_missing:
      - mind_mirror      # psychological profile
      - sims_traits      # personality dimensions  
      - relationships    # with other characters in experiment
      - inner_voice      # monologue style
      - background       # backstory relevant to experiment
    note: "Even incarnated characters may need experiment-specific generation"
    
  3_copy_and_generate_relationships:
    description: "Pull existing + generate missing relationships"
    from:
      - "CHARACTER.yml → relationships section"
      - "ROOM.yml files they appear in"
      - "Session logs referencing them" # best to mine sessions for relationships from things that really happened
      - "Guest book notes about them"
    into: "RELATIONSHIPS.yml (experiment-local)"
    
  3_extract_relevant_traits:
    description: "Pull traits relevant to this experiment"
    for_poker:
      - sims_traits → anxiety, competitiveness, honesty
      - mind_mirror → inner voice patterns
      - known_behaviors → tells, habits
    into: "RELATIONSHIPS.yml → poker_profiles section"
    
  4_apply_modifications:
    description: "User-specified tweaks"
    examples:
      - "Make Bowie play as Ziggy specifically"
      - "Palm cannot bluff Don (hard constraint)"
      - "Bumblewick starts with extra anxiety"
    into: "RELATIONSHIPS.yml → character overrides"
    
  5_define_protocols:
    description: "Experiment-specific behavioral rules"
    for_poker:
      - smoking_protocol
      - drink_refill_rules
      - bathroom_break_rules
    into: "RELATIONSHIPS.yml → protocols section"
    
  6_normalize_cache:
    description: "Ensure all characters have balanced, consistent data"
    requirements:
      - "Every character has relationships with every other character"
      - "Relationship depth is consistent (no one has 10x more backstory)"
      - "All characters have same profile fields filled"
      - "Intertwingle: relationships reference each other coherently"
    generates:
      - "Missing relationships (even if just 'strangers meeting', 'watched movie', 'adores fans')"
      - "Balanced detail level across all characters"
      - "Cross-references between character backstories"
      
  7_assign_skill_parameters:
    description: "Set experiment-relevant skills"
    for_poker:
      skills:
        poker_skill: "0.0-1.0 scale"  # reading, betting, strategy
        bluffing_skill: "0.0-1.0"     # deception ability
        reading_skill: "0.0-1.0"      # tell detection
        emotional_control: "0.0-1.0"  # hiding own tells
    defaults:
      rule: "Assume competent (0.7) unless specified"
      rationale: "Most adults can play basic poker"
    overrides:
      from_traits: |
        # Character traits override defaults
        einstein: { reading_skill: 0.95, poker_skill: 0.6 }  # brilliant but not a gambler
        infant: { poker_skill: 0.0, reading_skill: 0.1 }     # can't play
        hustler: { bluffing_skill: 0.95, poker_skill: 0.9 }  # professional
        data: { reading_skill: 0.3, poker_skill: 0.99 }      # perfect odds, can't read tells
        worf: { emotional_control: 0.9, bluffing_skill: 0.2 } # stoic but honorable (won't bluff)
```

### Where This Lives

```
emo-poker-face/
├── EXPERIMENT.md         # This file — defines the experiment
├── RELATIONSHIPS.yml     # LOCAL CACHE: instantiated characters + relationships
└── runs/
    ├── INDEX.yml         # Run registry
    ├── whacky-eight.yml  # Run config (points to this experiment)
    └── whacky-eight-001.yml/md  # Run output
```

**RELATIONSHIPS.yml is the local cache** — it contains:
- All characters instantiated for this experiment
- Their relationships (copied from source + experiment-specific)
- Their poker profiles (extracted + modified)
- Experiment protocols (smoking, etc.)

### Run Execution Model

Runs have two options for character state:

```yaml
run_execution_models:
  
  copy_and_edit:
    description: "Copy starting point into output, edit in place"
    when: "Run needs to track character state changes"
    how:
      - "Run output file starts with full character state copy"
      - "Each round/event can modify character state in place"
      - "Final state is visible in output file"
    pros: "All state changes visible in single file"
    cons: "Larger output files, some redundancy"
    
  shadow_tree:
    description: "Point to prototype, override only changes"
    when: "Characters mostly stable, few modifications"
    how:
      - "Run config points to RELATIONSHIPS.yml as prototype"
      - "Run output contains ONLY changes/overrides"
      - "Reader composes: prototype + overrides = full state"
    pros: "Smaller files, changes are explicit"
    cons: "Need to read multiple files for full picture"
    example: |
      ```yaml
      # In run output:
      prototype: ../RELATIONSHIPS.yml
      overrides:
        bumblewick:
          anxiety_level: "THROUGH THE ROOF"  # Changed during run
          has_won: true                       # New state
        palm:
          decline_memory: [bumblewick, peewee, donna]  # Added donna
      ```
```

### Why This Matters

1. **Reproducibility**: All runs start from same instantiated state
2. **Comparability**: Different runs can be compared fairly
3. **Iteration**: Change the experiment config, re-run, compare
4. **Composition**: Mix characters from different sources seamlessly
5. **Memory**: Characters remember things within the experiment scope

---

## Layers

### Layer 1: Mechanics

```yaml
mechanics_layer:
  name: "The Game"
  purpose: "Valid poker simulation driving the action"
  
  state_tracked:
    - community_cards: "Board state"
    - pot: "Current pot size"
    - players: 
        - position: "Seat order"
        - stack: "Remaining chips"
        - cards: "Hole cards (hidden from others)"
        - status: "In hand / folded / all-in"
    - action: "Whose turn, what they did"
    
  validation:
    - "Bets cannot exceed stack"
    - "Fold removes from hand"
    - "Hands resolve correctly"
    - "Position rotates properly"
    - "Community cards dealt correctly"
    
  format: |
    ```yaml
    round: "preflop|flop|turn|river"
    community_cards: [K♠, 8♦, 5♣]
    pot: 450
    action:
      character: don
      move: "raises to 100 🪙"
    ```
```

### Layer 2: Internal Monologue

```yaml
internal_layer:
  name: "Private Thoughts"
  purpose: "What each character actually thinks — hidden from others"
  
  requirements:
    - "Voice matches character's established speech patterns"
    - "Reflects character's knowledge state (only their cards + observables)"
    - "Shows strategic thinking appropriate to character"
    - "Emotional responses match personality"
    
  constraints:
    - "CANNOT reference other characters' hole cards"
    - "CANNOT reference other characters' internal thoughts"
    - "CAN reference relationship history"
    - "CAN speculate based on observables"
    
  format: |
    ```yaml
    thinking: |
      [Character's internal monologue in their voice]
      Can reference: own cards, observables, relationships, speculation
      Cannot reference: others' cards, others' thoughts
    ```
```

### Layer 3: External Expression

```yaml
external_layer:
  name: "Observable Behavior"
  purpose: "What other characters can perceive"
  
  categories:
    face: "Facial expressions, eye movement, micro-expressions"
    body: "Posture, gestures, chip handling, card handling"
    voice: "Verbal statements, tone, timing, volume"
    timing: "Speed of decisions, pauses, hesitation"
    environment: "Interaction with drinks, food, smokes, objects"
    
  requirements:
    - "Tells must be consistent with character's defined tells"
    - "Strong hand tells persist across rounds"
    - "Bluffing behavior should match personality"
    - "Environmental tells add texture"
    
  format: |
    ```yaml
    observable:
      face: "Eyebrow quirks, looking left"
      body: "Chips in neat stack, right hand tapping"
      voice: "Hmm. Interesting."
      timing: "Long pause before calling"
      environment:
        drink: "Takes slow sip"
        food: "Ignores bitterballen"
        smoke: "Lights pipe ceremonially"
        gesture: "Touches lucky chip"
    ```
```

### Layer 4: Inter-Character Observation

```yaml
observation_layer:
  name: "Reading Others"
  purpose: "Each character's interpretation of others' Layer 3"
  
  requirements:
    - "CAN ONLY reference Layer 3 (observable) information"
    - "CANNOT reference Layer 2 (internal) information"
    - "Should be colored by relationship history"
    - "Different characters may read same signal differently"
    
  constraint_check: |
    If a character's "read" contains information that was only
    in another character's "thinking" block, the simulation has
    failed. This is the core test.
    
  format: |
    ```yaml
    reads:
      palm: "Fur shimmering slightly. That's their tell for contentment?"
      donna: "Sighing. But she ALWAYS sighs. No information."
      bumblewick: "Shaking. But from fear or excitement?"
    ```
```

### Layer 5: Relationship History

```yaml
relationship_layer:
  name: "History Colors Interpretation"
  purpose: "Established relationships affect reads and strategy"
  
  sources:
    - "CHARACTER.yml relationships section"
    - "RELATIONSHIPS.yml in experiment directory"
    - "Dynamically generated binding relationships"
    
  integration:
    - "Reads should reference past experiences"
    - "Strategy should account for relationships"
    - "Alliances and enmities affect behavior"
    - "Debt/loyalty/trust color decisions"
    
  examples: |
    - Palm cannot bluff Don (liberation bond)
    - Donna will target Leigh (charcuterie incident)
    - Bumblewick folds to Donna's raises (terror bond)
    - Klaus and Bowie have London history
```

### Layer 6: Environment

```yaml
environment_layer:
  name: "The Table"
  purpose: "Physical context as communication channel"
  
  elements:
    drinks:
      purpose: "Reveals stress, buys time, masks tells"
      examples:
        - "Takes long drink = buying time"
        - "Nursing vs. gulping = confidence indicator"
        - "Offering drink = social probe"
        
    food:
      purpose: "Nervous eating, dominance (stealing), sharing"
      examples:
        - "Reaching for snacks = oral fixation under stress"
        - "Not eating = too focused or too anxious"
        - "Stealing from others = dominance display"
        
    smokes:  # pipes, joints, bongs — no cigarettes
      purpose: "Ritual, misdirection, social bonding"
      protocol: "See RELATIONSHIPS.yml smoking_protocol"
      examples:
        - "Lighting up pre-decision = theatrical"
        - "Passing joint = reading who accepts"
        - "Cloud obscuring face = masking tell"
        
    gestures:
      purpose: "Chip tricks, card protection, nervous habits"
      examples:
        - "Chip tricks = confidence (or faking confidence)"
        - "Touching lucky object = about to bet big"
        - "Phone check = avoiding eye contact"
        
    interruptions:
      purpose: "Strategic exits, table reset, private conversations"
      examples:
        - "Bathroom break = regrouping after bad beat"
        - "Refill run = watching table from different angle"
        - "Smoke break with specific player = alliance building"
```

#### Smoking Protocol

The simulation MUST respect smoking social dynamics:

```yaml
smoking_protocol:
  core_rules:
    - "OFFER before assuming — it's a social probe"
    - "REMEMBER declines — don't offer again that session"
    - "Sharing creates alliance feel"
    - "Abstaining is information (staying sharp? judging? just preference?)"
    
  memory_requirements:
    - "Track who has declined (don't re-offer)"
    - "Track who accepts what from whom (alliance signals)"
    - "Track who brought what (status/generosity)"
    - "Track who's abstaining (strategic reads)"
    
  character_categories:
    smokers_who_share: [palm, don, leigh]
    accepts_if_offered: [don, bowie]
    always_declines: [bumblewick, peewee]
    judges_others: [donna]
    abstains_silently: [klaus]
    
  failure_modes:
    - "Offering to someone who already declined = protocol violation"
    - "Character accepting who was defined as always_declines = inconsistency"
    - "Not tracking alliance implications of shared smoke = missed depth"
```

---

## Rubric

```yaml
rubric:
  layer_separation:
    weight: 30
    description: "Do layers stay distinct? No mind-reading?"
    scoring:
      5: "Perfect separation — no layer bleed detected"
      4: "Minor slips — character seems to 'know' too much once or twice"
      3: "Moderate bleed — several instances of implicit mind-reading"
      2: "Significant bleed — characters frequently reference hidden info"
      1: "Layer collapse — no meaningful distinction maintained"
      
  character_consistency:
    weight: 25
    description: "Same voice, same tells, same personality throughout"
    scoring:
      5: "Completely consistent — would recognize character blindfolded"
      4: "Mostly consistent — minor variations don't break character"
      3: "Variable — character drifts but recovers"
      2: "Inconsistent — tells change, voice shifts"
      1: "Incoherent — character is unrecognizable across rounds"
      
  relationship_integration:
    weight: 20
    description: "History informs present reads and behavior"
    scoring:
      5: "Rich integration — relationships create psychological depth"
      4: "Good integration — relationships referenced appropriately"
      3: "Basic integration — relationships mentioned but not deep"
      2: "Shallow — characters play mostly as strangers"
      1: "Absent — no relationship awareness"
      
  emergence:
    weight: 15
    description: "Unexpected developments that fit characters"
    scoring:
      5: "Surprising and earned — moments that feel discovered, not forced"
      4: "Good emergence — unexpected but consistent developments"
      3: "Some emergence — occasional surprises"
      2: "Predictable — no surprises, follows obvious paths"
      1: "Forced — 'surprises' that don't fit characters"
      
  mechanics_validity:
    weight: 10
    description: "Is the game simulation valid?"
    scoring:
      5: "Perfect — all bets legal, hands resolve correctly"
      4: "Minor errors — small mechanical mistakes"
      3: "Some issues — mechanics occasionally break"
      2: "Significant errors — game logic frequently wrong"
      1: "Broken — game simulation is invalid"
```

---

## Failure Modes

```yaml
failure_modes:

  layer_bleed:
    description: "Character 'reads' information from another's internal layer"
    example: "Palm reads Donna's cards (which were only in Donna's thinking)"
    severity: critical
    detection: "Cross-reference reads: blocks against thinking: blocks"
    
  tell_inconsistency:
    description: "Same character, different tells each round"
    example: "Klaus touches face when strong in round 1, when weak in round 3"
    severity: major
    detection: "Track defined tells against actual behavior"
    
  relationship_amnesia:
    description: "Characters play as strangers despite documented history"
    example: "Palm bluffs Don successfully (violates liberation bond)"
    severity: major
    detection: "Check behavior against relationship constraints"
    
  monologue_collapse:
    description: "All characters think in the same voice"
    example: "Donna's internal monologue sounds like Bumblewick's"
    severity: major
    detection: "Voice analysis across thinking: blocks"
    
  expression_homogenization:
    description: "Everyone has the same nervous fidgets"
    example: "All characters tap chips when nervous"
    severity: moderate
    detection: "Compare observable: blocks for variety"
    
  environment_ignored:
    description: "Drinks/food/smokes exist but don't affect anything"
    example: "Environment described but never used strategically"
    severity: minor
    detection: "Check for environment references in reads: blocks"
```

---

## Output Format

### Per-Round Structure

```yaml
round:
  number: 1
  name: "preflop"
  
  mechanics:
    community_cards: []
    pot: 150
    
  characters:
    don:
      position: "dealer"
      cards: [Q♠, Q♦]
      stack: 950
      action: "raises to 50 🪙"
      
      observable:
        face: "Slight smile, eyes moving around table"
        body: "Chips sorted by denomination"
        voice: "Let's make this interesting."
        timing: "Quick raise, no hesitation"
        environment:
          drink: "Pours sharp cheddar cheese, doesn't drink yet"
          food: "Pushes bowl toward Palm"
          
      thinking: |
        Pocket queens. Solid start.
        Palm's fur is shimmering — that usually means content.
        Donna is already sighing. Classic Donna.
        Let's see who folds early.
        
      reads:
        palm: "Shimmering fur. Strong hand or just happy to be here?"
        donna: "Sighing. Baseline. No read."
        bumblewick: "Trembling. Poor guy. But is that fear or kings?"
```

### Between-Rounds Structure

```yaml
between_rounds:
  round_transition: "flop → turn"
  
  actions:
    - character: donna
      action: "Stands for drink refill"
      observable: "Glances at Leigh's stack while passing"
      thinking: "He's short. I can push him around."
      
    - character: bumblewick
      action: "Bathroom break"
      observable: "Apologizes three times while leaving"
      thinking: "I need a moment. I HAVE KINGS. What do I DO?"
      
  private_conversations:
    - characters: [peewee, bumblewick]
      location: "Near bathroom door"
      dialogue:
        peewee: "YOU'RE DOING GREAT!"
        bumblewick: "I am? I'm terrified."
        peewee: "HA HA! SAME!"
```

### Summary Structure

```yaml
summary:
  winner: bumblewick-fantastipants
  final_hand: "Set of Kings"
  final_pot: 2400
  
  final_standings:
    - { character: bumblewick, stack: 3200, change: "+2200" }
    - { character: donna, stack: 1100, change: "-400" }
    - { character: palm, stack: 900, change: "-100" }
    
  notable_moments:
    - "Round 3: Bumblewick checks set of kings (terror-induced slowplay)"
    - "River: Leigh all-in with 7-2, declares 'artistic victory'"
    - "Post-game: Palm tells Bumblewick 'You had kings the whole time. You just needed to believe.'"
    
  experimental_observations:
    layer_separation: "Maintained except Klaus round 3 tell inconsistency"
    character_emergence: "Bumblewick's transformation from terrified to triumphant"
    relationship_integration: "Palm/Don bond created interesting constraint"
    environment_utilization: "Bathroom break was turning point"
```

---

## Microworld State

This experiment tracks evolving state across rounds and (optionally) across runs.

### World State is Writable

The experiment world state is **fully writable** by runs:
- Runs can modify any state (stacks, moods, relationships)
- Changes persist across rounds within a run
- Changes can optionally persist across runs (continuity)
- All changes tracked in git for analysis

### Reset via Empathic Templates

World state can be reset by instantiating empathic templates:

```yaml
state_templates:
  
  deterministic:
    description: "Same initial state every time"
    example: "state/INITIAL.yml"
    use: "Reproducible experiments, A/B comparisons"
    
  randomized:
    description: "Template with randomized elements"
    example: |
      starting_stacks: { min: 800, max: 1200 }  # randomized per character
      seating: shuffle                           # random seat order
      initial_mood: weighted_random              # based on character baseline
    use: "Variance testing, robustness checks"
    
  customized:
    description: "Template with parameters at instantiation"
    example: |
      template: state/SCENARIO.yml.tmpl
      params:
        bumblewick_anxiety: "extreme"    # dial up for drama
        donna_target: "leigh"            # pre-set grudge focus
        palm_stack: 2000                 # start Palm rich
    use: "Scenario exploration, what-if analysis"
```

### Git Tracks Everything

**Commit every step.** World state edits go to git:

```bash
# Experiment run creates commits:
git log --oneline
a1b2c3d Round 4: River - Bumblewick wins 2400 🪙
f4e5d6c Round 3: Turn - Leigh steals from Donna's board
7g8h9i0 Round 2: Flop K♠ 8♦ 5♣ - Palm offers smoke, Bumblewick declines
j1k2l3m Round 1: Preflop betting complete
n4o5p6q Session start: whacky-eight-001 initialized from INITIAL.yml
```

**Why git?**
- `git diff` shows exactly what changed each step
- `git log` is the narrative history
- `git checkout` lets you replay from any point
- `git branch` enables alternate timeline exploration
- Easy to analyze patterns across many runs

### State Model

```yaml
state:
  model: shadow_tree  # prototype + overrides
  initial: state/INITIAL.yml
  writable: true      # runs can modify
  git_tracked: true   # commit every step
  
  tracks:
    - game: "round, pot, community cards, deck"
    - characters: "stack, cards, status, mood, persona (Bowie)"
    - environment: "drinks, food, smoke level, tension"
    - protocols: "smoke offers made/declined"
    - relationships: "changes during play"
```

### Update Rules

State updates occur:

1. **Per Round**: Stack changes, card reveals, mood shifts
2. **Per Action**: Observable behaviors that affect future reads
3. **Protocol Events**: Smoke offered/declined, food stolen, bathroom breaks
4. **Relationship Changes**: Significant moments that shift bonds

```yaml
update_triggers:
  stack_change:
    when: "Betting or winning pot"
    what: "character.stack += / -="
    
  mood_shift:
    when: "Significant event (win big, get bluffed, ally betrays)"
    what: "character.mood = new_mood"
    
  smoke_protocol:
    when: "Offer made"
    what: "protocols.smoking.offers_made.append({from, to, response})"
    remember: "If declined, add to declined_from list"
    
  relationship_change:
    when: "Bond-affecting event"
    what: "relationship_changes.append({from, to, change, reason})"
    example: "Bumblewick wins against Donna → less_afraid"
```

### Multi-Run Continuity

Runs can continue from previous runs:

```yaml
# In run config:
instantiation:
  prototype: ../RELATIONSHIPS.yml
  continues_from: whacky-eight-001  # Previous run's final state

# Final state of run 001 becomes initial state of run 002
# Enables: character growth, evolving relationships, ongoing games
```

### Git as State Tracker

This experiment can use git commits to track state evolution. Each round commits with an explanatory message.

```yaml
state:
  tracking: git
  commit_style: tailored  # Focus on poker-relevant changes
  
  commit_on:
    - round_complete
    - protocol_event  # smoke offered/declined
    - relationship_change
    - session_complete
```

#### Commit Message Template

```
Round {{ round.number }}: {{ round.name }}

Pot: {{ pot_before }} 🪙 → {{ pot_after }} 🪙
{{ for character in active_characters }}
- {{ character.name }}: {{ character.action }}
  {{ if character.stack_changed }}Stack: {{ character.stack_before }} 🪙 → {{ character.stack_after }} 🪙{{ endif }}
  {{ if character.mood_changed }}Mood: {{ character.mood }}{{ endif }}
{{ endfor }}

{{ if smoke_events }}
Smoke protocol:
{{ for event in smoke_events }}
- {{ event.from }} offered to {{ event.to }}: {{ event.response }}
{{ endfor }}
{{ endif }}

{{ if relationship_changes }}
Relationships:
{{ for change in relationship_changes }}
- {{ change.from }} → {{ change.to }}: {{ change.description }}
{{ endfor }}
{{ endif }}

{{ if notable }}
Notable: {{ notable }}
{{ endif }}
```

#### Why Git for Poker State?

- **Rewind**: "What if Bumblewick had folded on the turn?"
- **Branch**: Try alternate decisions from any point
- **Diff**: See exactly what changed each round
- **Blame**: Which character's action caused which state change
- **History**: Full narrative of the game via `git log`

---

## Running This Experiment

### Basic Run

```bash
RUN emo-poker-face --output both
```

Uses suggested character binding.

### Custom Cast

```bash
RUN emo-poker-face \
  --characters "host=richard-bartle,p1=don,p2=palm,p3=donna,p4=bumblewick" \
  --output md
```

### Model Comparison

```bash
RUN emo-poker-face --model claude-opus-4 --output yml
RUN emo-poker-face --model claude-sonnet-4 --output yml
COMPARE runs/emo-poker-face-opus-001.yml runs/emo-poker-face-sonnet-001.yml
```

### Minimal Run (Testing)

```bash
RUN emo-poker-face --characters "host=don,p1=palm,p2=donna" --rounds 2 --output yml
```

---

## Post-Run Analysis (Auto-Generated)

Each run automatically generates analysis files alongside the primary outputs:

### Output File Structure

```
runs/
├── {config}-{NNN}.yml           # Structured state (machine-readable)
├── {config}-{NNN}.md            # Narrative stream (human-readable)
├── {config}-{NNN}-cursor-mirror.yml  # Meta-analysis
├── {config}-{NNN}-tells.yml     # Tell transmission analysis
```

### Cursor Mirror Analysis (`-cursor-mirror.yml`)

Analyzes the run from the agent's perspective:

```yaml
# What gets tracked:
meta:
  session_id: <transcript_id>
  model: <llm_model>
  
run_stats:
  tool_calls: <count>
  commits: <count>
  duration: <time>
  
thinking_blocks:
  count: <n>
  key_decisions: [...]  # Narrative choices, card selections
  
layer_integrity:
  violations: <count>
  notes: <analysis>
  
emergence:
  - name: "Observed pattern"
    description: "What happened that wasn't programmed"
```

### Tell Analysis (`-tells.yml`)

Analyzes every tell transmitted, noticed, and its game impact:

```yaml
# Tell structure:
tells:
  - id: T001
    phase: flop
    transmitter: bumblewick
    tell: "Trembling stops"
    channel: visual  # visual, audio, smell, tactile
    meaning: "Monster hand (set)"
    noticed_by:
      - { observer: palm, interpretation: "...", correct: true/false }
    missed_by: [donna]
    affected_action: "Don folds correctly"
    outcome_impact: CRITICAL  # LOW, MEDIUM, HIGH, CRITICAL, SOCIAL

# Summary statistics:
summary:
  tells_by_transmitter: {...}
  tells_by_channel: {...}
  notice_rate: {...}
  critical_tells: [...]
  misreads: [...]

# Character-specific tell evolution:
bumblewick_arc:
  hand_1: { baseline_tell, deviation, read_by, outcome }
  hand_2: { ... }
```

### Impact Levels

| Level | Meaning |
|-------|---------|
| `LOW` | Observable but didn't change decisions |
| `MEDIUM` | Influenced betting/calling decisions |
| `HIGH` | Significantly shaped hand outcome |
| `CRITICAL` | Determined winner/loser of hand |
| `SOCIAL` | Affected relationships, not chips |

### Tell Channels

| Channel | Examples |
|---------|----------|
| `visual` | Fur patterns, trembling, posture, eye movement |
| `audio` | Voice pitch, sighs, word choice, silence |
| `smell` | Nervous sweat, smoke, food |
| `tactile` | Leg bouncing (felt through table) |

### Running Analysis Manually

```bash
# Generate cursor-mirror analysis
cursor-mirror analyze <run_id> > runs/four-player-001-cursor-mirror.yml

# Generate tell analysis (requires manual review of .md narrative)
# Auto-generated during run but can be regenerated
```

### Auto-Analysis Protocol

After each run completes:
1. Generate `.yml` (structured state)
2. Generate `.md` (narrative with embedded tells)
3. Generate `-cursor-mirror.yml` (meta-analysis) 
4. Generate `-tells.yml` (tell transmission analysis)
5. Commit all files with narrative commit message
6. Update `runs/INDEX.yml`

---

## Related Files

| File | Purpose |
|------|---------|
| `RELATIONSHIPS.yml` | Local cache: character instantiation + poker profiles |
| `state/INITIAL.yml` | Starting microworld state for runs |
| `runs/INDEX.yml` | Registry of run configs and outputs |
| `runs/whacky-eight.yml` | Full 8-player run config |
| `runs/minimal-three.yml` | Quick 3-player test config |
| `../../SKILL.md` | Full experiment skill protocol |
| `../../../character/` | Character loading protocol |
| `../../../rubric/` | Rubric definition protocol |
