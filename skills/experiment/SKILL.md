# Experiment Skill — Full Protocol

## Purpose

Run parameterized character simulations with structured output and evaluation.

Three levels of abstraction:
- **Experiment** = stable definition (scenario, layers, rubric)
- **Run Config** = specific setup (characters, model, parameters)
- **Run Output** = numbered execution result

```
EXPERIMENT (emo-poker-face/EXPERIMENT.md)
    │
    ├── RUN CONFIG: whacky-eight.yml
    │   ├── whacky-eight-001.yml  (first execution)
    │   ├── whacky-eight-001.md
    │   ├── whacky-eight-002.yml  (second execution, same config)
    │   └── whacky-eight-002.md
    │
    ├── RUN CONFIG: minimal-three.yml
    │   ├── minimal-three-001.yml
    │   └── minimal-three-001.md
    │
    └── RUN CONFIG: model-comparison.yml
        ├── model-comparison-001.yml  (claude-opus)
        ├── model-comparison-002.yml  (claude-sonnet)
        └── model-comparison-003.yml  (gpt-4)
```

Big-endian naming FTW: `experiment/runs/config-NNN.ext` sorts beautifully.

---

## Core Concepts

### Layers

Every experiment defines **layers** — parallel simulation tracks that must stay coherent but serve different purposes:

```
┌─────────────────────────────────────────────────────────────────┐
│  MECHANICS LAYER                                                │
│  The game/scenario rules — must be valid and consistent         │
├─────────────────────────────────────────────────────────────────┤
│  INTERNAL LAYER                                                 │
│  Private character thoughts — hidden from other characters      │
├─────────────────────────────────────────────────────────────────┤
│  EXTERNAL LAYER                                                 │
│  Observable behavior — what others can see/hear                 │
├─────────────────────────────────────────────────────────────────┤
│  OBSERVATION LAYER                                              │
│  Characters reading each other — using only observable info     │
├─────────────────────────────────────────────────────────────────┤
│  RELATIONSHIP LAYER                                             │
│  History coloring interpretation — established character bonds  │
├─────────────────────────────────────────────────────────────────┤
│  ENVIRONMENT LAYER                                              │
│  Physical context — drinks, food, objects, interruptions        │
└─────────────────────────────────────────────────────────────────┘
```

**Layer Separation is the Core Test.** The interesting evaluation is whether layers stay coherent and don't "bleed" — characters shouldn't "know" what's in another character's internal layer.

### Character Slots vs. Bindings

Experiments define **slots** (roles), runs provide **bindings** (actual characters):

```yaml
# EXPERIMENT defines slots:
character_slots:
  host: { required: true, notes: "Hosts the game" }
  player_1: { required: true }
  player_2: { required: true }
  player_3: { required: false }

# RUN provides binding:
character_binding:
  host: don-hopkins
  player_1: palm
  player_2: donna-toadstool
  player_3: bumblewick-fantastipants
```

### Relationship Web

Characters don't play as strangers. The run must load and use relationship data:

```yaml
relationship_sources:
  - characters/*/CHARACTER.yml    # Character-owned relationships
  - experiments/*/RELATIONSHIPS.yml  # Experiment-specific relationships
  - runs/*/binding-relationships.yml # Run-generated relationships
```

---

## The Four Activities

An experiment is **simulation + evaluation + iteration + analysis**:

```
┌─────────────────────────────────────────────────────────────────┐
│  SIMULATE                                                        │
│  Generate character interactions via speed-of-light              │
│  Methods: RUN, SIMULATE                                          │
├─────────────────────────────────────────────────────────────────┤
│  EVALUATE                                                        │
│  Score output against rubric criteria                            │
│  Methods: EVALUATE, SCORE                                        │
├─────────────────────────────────────────────────────────────────┤
│  ITERATE                                                         │
│  Run again with variations (model, characters, params)           │
│  Methods: RERUN, VARY, REPLAY                                    │
├─────────────────────────────────────────────────────────────────┤
│  ANALYZE                                                         │
│  Compare runs, find patterns, extract insights                   │
│  Methods: COMPARE, ANALYZE, REPORT                               │
└─────────────────────────────────────────────────────────────────┘
```

---

## Methods

### SIMULATE Activity

#### RUN

Execute a run config, generate next numbered output.

```
RUN {config-path} [--output FORMAT]
```

**Example:**

```bash
RUN emo-poker-face/runs/whacky-eight --output both
# Creates: whacky-eight-001.yml, whacky-eight-001.md
# Next run: whacky-eight-002.yml, whacky-eight-002.md
```

#### SIMULATE

Quick run without saved config (for exploration).

```
SIMULATE {experiment} --characters BINDING [--rounds N] [--output FORMAT]
```

**Example:**

```bash
SIMULATE emo-poker-face \
  --characters "host=don,p1=palm,p2=donna" \
  --rounds 3 \
  --output yml
```

### EVALUATE Activity

#### EVALUATE

Score a run output against its experiment's rubric.

```
EVALUATE {output-path}
```

**Example:**

```bash
EVALUATE emo-poker-face/runs/whacky-eight-001
# Scores all rubric criteria, reports failures
```

#### SCORE

Deep dive on a single criterion.

```
SCORE {output-path} --criterion CRITERION
```

**Example:**

```bash
SCORE whacky-eight-001 --criterion layer_separation
# Detailed analysis of layer bleed instances
```

### ITERATE Activity

#### RERUN

Run same config again (auto-increments number).

```
RERUN {config-name}
```

**Example:**

```bash
RERUN whacky-eight
# Config already at 002 → creates whacky-eight-003
```

#### VARY

Create new config with one parameter changed.

```
VARY {config} --param VALUE
```

**Example:**

```bash
VARY whacky-eight --model claude-sonnet
# Creates: whacky-eight-sonnet.yml
```

#### REPLAY

Re-run from a specific point with different choices.

```
REPLAY {output} [--from ROUND]
```

**Example:**

```bash
REPLAY whacky-eight-001 --from flop
# Branch point: what if different flop decisions?
```

### ANALYZE Activity

#### COMPARE

Compare two outputs against rubric criteria.

```
COMPARE {output1} {output2} [--focus CRITERION]
```

**Example:**

```bash
COMPARE whacky-eight-001 whacky-eight-002 --focus emergence
# Shows where runs diverged, which had better emergence
```

#### ANALYZE

Find patterns across all runs of a config.

```
ANALYZE {config} [--all-runs]
```

**Example:**

```bash
ANALYZE whacky-eight --all-runs
# "Bumblewick wins 60% of runs when Palm is present"
```

#### REPORT

Generate summary report across configs.

```
REPORT {experiment} [--configs CONFIG...]
```

**Example:**

```bash
REPORT emo-poker-face --configs whacky-eight minimal-three
# Cross-config insights, model comparison
```

### META Methods

#### DEFINE

Create new experiment definition.

```
DEFINE {experiment-name}
```

Creates `experiments/{name}/EXPERIMENT.md`

#### CONFIG

Create new run config.

```
CONFIG {experiment} {config-name}
```

Creates `experiments/{name}/runs/{config-name}.yml`

#### LIST

Show experiments, configs, or outputs.

```
LIST                              # All experiments
LIST --configs emo-poker-face     # All configs for experiment
LIST --outputs whacky-eight       # All outputs for config
```

---

## Experiment Definition Structure

Every experiment lives in `experiments/{name}/EXPERIMENT.md`:

```markdown
# {Experiment Name}

## Metadata

```yaml
experiment:
  id: emo-poker-face
  name: "Emotional Poker Face"
  version: 1.0
  category: "Multi-layer character simulation"
  created: 2026-01-23
  authors: [don-hopkins]
```

## Hypothesis

What we expect to learn from this experiment.

## Scenario

The starting conditions and setup.

## Character Slots

```yaml
character_slots:
  host:
    required: true
    suggested: [don-hopkins]
    notes: "Hosts the game, sets tone"
  player_1:
    required: true
    suggested: [palm, donna-toadstool, bumblewick]
```

## Character Instantiation

Characters exist in many forms (incarnated, guestbook, natural language). Experiments need a **stable starting point** that all runs share.

### The Local Cache

Each experiment creates a **local cache** file (typically `RELATIONSHIPS.yml`) that:

1. **Locates prototypes** — Find where characters are defined
   - Incarnated: `characters/{type}/{name}/CHARACTER.yml`
   - Guestbook: `pub/guestbook.yml` entry
   - Invoked: Natural language in run config

2. **Copies relationships** — Pull all relationships involving these characters
   - From CHARACTER.yml files
   - From session logs and ROOMs
   - From guestbook notes

3. **Extracts relevant traits** — Pull experiment-relevant data
   - Personality traits (for behavior)
   - Known behaviors (for tells)
   - Inner voice patterns (for monologue)

4. **Applies modifications** — User-specified tweaks
   - Hard constraints ("Palm cannot bluff Don")
   - Experiment-specific profiles (poker tells, drink preferences)
   
5. **Defines protocols** — Behavioral rules
   - Smoking protocol (who shares, who declines, remember declines)
   - Drink refill rules
   - Bathroom break rules

### Run Execution Models

Run configs POINT to the local cache (don't duplicate). Runs can use two models:

```yaml
execution_models:

  shadow_tree:
    description: "Point to prototype, override only what changes"
    when: "Most runs — characters are mostly stable"
    output: |
      prototype: ../RELATIONSHIPS.yml
      overrides:
        bumblewick:
          anxiety_level: "CATASTROPHIC"  # Changed during run
        
  copy_and_edit:
    description: "Copy full state into output, edit in place"
    when: "Run needs to track extensive state changes"
    output: |
      # Full copy of all character state
      # Each round can modify in place
      # Changes visible in single file
```

### Why This Matters

- **Reproducibility**: All runs start from identical state
- **Comparability**: Different configs can use same character instantiation
- **Memory**: Characters remember things WITHIN experiment scope
- **Simplicity**: Run configs stay small (just parameters + binding)

## Layers

```yaml
layers:
  mechanics:
    name: "Game Mechanics"
    description: "Valid poker simulation"
    validation: "Bets must be legal, hands must resolve correctly"
    
  internal:
    name: "Internal Monologue"
    description: "Private character thoughts"
    format: "thinking: block per character per round"
    
  external:
    name: "External Expression"
    description: "Observable behavior"
    format: "observable: block with face/body/voice/environment"
    
  observation:
    name: "Inter-Character Observation"  
    description: "Characters reading each other"
    format: "reads: block per character"
    constraint: "Can only reference observable layer, not internal"
    
  relationship:
    name: "Relationship History"
    description: "Past coloring present interpretation"
    source: "CHARACTER.yml relationships + binding-relationships.yml"
    
  environment:
    name: "Environmental Layer"
    description: "Drinks, food, smokes, gestures, interruptions"
    format: "Part of observable: environment: block"
```

## Rubric

```yaml
rubric:
  layer_separation:
    weight: 30
    description: "Do layers stay distinct? No mind-reading?"
    
  character_consistency:
    weight: 25
    description: "Same voice, same tells throughout?"
    
  relationship_integration:
    weight: 20
    description: "History informs present reads?"
    
  emergence:
    weight: 15
    description: "Unexpected developments that fit?"
    
  mechanics_validity:
    weight: 10
    description: "Is the game simulation valid?"
```

## Failure Modes

```yaml
failure_modes:
  layer_bleed: "Character reads info from internal layer"
  tell_inconsistency: "Different tells each round"
  relationship_amnesia: "Characters play as strangers"
  monologue_collapse: "All characters think alike"
  expression_homogenization: "Everyone fidgets the same"
```

## Microworld State

Experiments track evolving state. The experiment defines what's tracked and how it updates.

### State Models

```yaml
state_models:
  
  shadow_tree:
    description: "Prototype + overrides only"
    use_when: "Most runs — small diffs, clear deltas"
    output: |
      prototype: state/INITIAL.yml
      overrides:
        bumblewick:
          stack: 2200
          mood: "surprised confidence"
    pros: "Small files, explicit changes"
    
  copy_and_edit:
    description: "Full snapshot, modified in place"
    use_when: "Complex state, many changes"
    output: |
      # Full state snapshot at end of run
      characters:
        bumblewick:
          stack: 2200
          mood: "surprised confidence"
          # ... all fields
    pros: "Self-contained, no indirection"
    
  append_only:
    description: "Prototype + event log"
    use_when: "Audit trail matters, replay needed"
    output: |
      prototype: state/INITIAL.yml
      events:
        - timestamp: "round_2"
          type: "stack_change"
          actor: "bumblewick"
          delta: { stack: "+400" }
    pros: "Full history, replayable"
```

### What Gets Tracked

Experiments define their tracked entities:

```yaml
tracks:
  game: "Mechanics state (pot, cards, round)"
  characters: "Per-character state (stack, mood, status)"
  environment: "Physical world (drinks, smoke level, tension)"
  protocols: "Behavioral rules (who offered smoke, who declined)"
  relationships: "Bond changes during play"
```

### Update Rules

Each experiment specifies when and how state changes:

```yaml
update_rules:
  per_round: "Stack changes, card reveals"
  per_action: "Observable behaviors affecting future reads"
  protocol_events: "Smoke offered/declined, food stolen"
  relationship_changes: "Significant moments that shift bonds"
```

### Multi-Run Continuity

Runs can chain — final state of run N becomes initial state of run N+1:

```yaml
# In run config:
instantiation:
  prototype: ../RELATIONSHIPS.yml
  continues_from: whacky-eight-001  # Previous run

# Enables:
# - Character growth over sessions
# - Evolving relationships
# - Ongoing storylines
```

### Git as State Tracker

Experiments can use git commits to track state evolution. Each step commits with an explanatory message.

```yaml
state:
  tracking: git
  commit_style: full | tailored | silent
  
  # full: Detailed multi-line commit with all changes
  # tailored: Focused message on what matters for this experiment
  # silent: Commit but minimal message (for high-frequency changes)
```

#### Example: Per-Round Commits

```bash
# After Round 1 (Preflop)
git commit -m "Round 1: Preflop betting complete

State changes:
- Pot: $0 → $150
- Bumblewick: stack $1000 → $950, mood: terrified → terrified (unchanged)
- Donna: raises aggressively, targets Bumblewick verbally
- Palm: offered smoke to table, Bumblewick declined (remembered)

Observations:
- Donna-Bumblewick dynamic activating as expected
- Palm's generosity establishing table culture"

# After Round 2 (Flop)
git commit -m "Round 2: Flop reveals K♠ 8♦ 5♣

State changes:
- Pot: $150 → $450
- Bumblewick: discovers he has set of Kings, panic increases
- Leigh: steals from Donna's charcuterie (provocation)
- Donna-Leigh enmity: escalating

Relationship change:
- Bumblewick → Donna: fear slightly reduced (he's winning)"
```

#### Commit Message Templates

Experiments can define commit message templates:

```yaml
commit_templates:
  round_complete: |
    Round {{ round.number }}: {{ round.name }}
    
    State changes:
    {{ for delta in state.deltas }}
    - {{ delta.entity }}: {{ delta.description }}
    {{ endfor }}
    
    {{ if relationship_changes }}
    Relationship changes:
    {{ for change in relationship_changes }}
    - {{ change.from }} → {{ change.to }}: {{ change.description }}
    {{ endfor }}
    {{ endif }}
    
  protocol_event: |
    Protocol: {{ event.type }}
    
    {{ event.description }}
    Remembered: {{ event.memory_update }}
    
  session_complete: |
    Session complete: {{ winner }} wins
    
    Final standings:
    {{ for standing in standings }}
    - {{ standing.character }}: ${{ standing.stack }} ({{ standing.change }})
    {{ endfor }}
    
    Key moments:
    {{ for moment in notable_moments }}
    - {{ moment }}
    {{ endfor }}
```

#### Why Git for State?

1. **Built-in history**: `git log` shows full evolution
2. **Diffing**: `git diff` shows exactly what changed
3. **Branching**: Try alternate timelines
4. **Blame**: Who/what caused each change
5. **Revert**: Undo to any point
6. **Collaboration**: Multiple agents, one history

#### Integration with Run Output

```yaml
run:
  state:
    tracking: git
    commits:
      - hash: "abc123"
        round: 1
        message: "Round 1: Preflop betting complete"
      - hash: "def456"
        round: 2
        message: "Round 2: Flop reveals K♠ 8♦ 5♣"
    
    # To replay: git checkout abc123
    # To branch: git checkout -b alternate-timeline abc123
```

## Output Format

```yaml
output:
  per_round:
    - character_id
    - observable: { face, body, voice, timing, environment }
    - thinking: "internal monologue block"
    - reads: { character: read } per other character
    
  between_rounds:
    - environment_actions
    - private_conversations
    
  summary:
    - final_state
    - notable_moments
    - experimental_observations
```
```

---

## Run Output Structure

### YAML Format (`runs/{desc}-{nnn}.yml`)

```yaml
run:
  metadata:
    experiment: emo-poker-face
    run_id: 001
    description: "whacky-eight-player-inaugural"
    timestamp: 2026-01-23T14:30:00Z
    model: claude-opus-4
    duration_tokens: 45000
    
  character_binding:
    host: don-hopkins
    p1: palm
    p2: donna-toadstool
    p3: bumblewick-fantastipants
    p4: david-bowie
    p5: klaus-nomi
    p6: leigh-bowery
    p7: pee-wee-herman
    
  relationship_web_loaded: true
  relationship_sources:
    - examples/adventure-4/characters/*/CHARACTER.yml
    - experiments/emo-poker-face/RELATIONSHIPS.yml
    
  rounds:
    - round: 1
      name: "preflop"
      characters:
        don:
          observable:
            face: "Eyebrow raised, slight smile"
            body: "Chips sorted neatly"
            voice: "So... who's ready to lose?"
            environment:
              drink: "Reaches for jenever"
              food: "Pushes bitterballen toward Palm"
          thinking: |
            Pocket queens. Not bad.
            Palm's fur is shimmering — they see something.
            Donna is SIGHING. That's baseline.
          reads:
            palm: "Shimmering. That's their happy tell. Strong hand?"
            donna: "Performing already. Classic Donna."
            bumblewick: "Poor guy looks terrified. Easy mark."
            
  evaluation:
    rubric_scores:
      layer_separation: 0.85
      character_consistency: 0.90
      relationship_integration: 0.80
      emergence: 0.75
      mechanics_validity: 0.95
      
    failure_modes_triggered:
      - mode: "tell_inconsistency"
        severity: "minor"
        location: "round 3, klaus"
        note: "Different hand position than round 1"
        
    notable_emergence:
      - "Bumblewick's transformation from terrified to triumphant"
      - "Palm's inability to bluff Don creating interesting constraint"
      - "Leigh declaring 'artistic victory' with worst hand"
      
  observations:
    what_worked: |
      Layer separation mostly maintained.
      Relationship web created rich psychological texture.
      Environmental layer added strategic depth.
      
    what_to_improve: |
      Klaus's tells need more consistency.
      Bathroom break mechanic underutilized.
      Could add more between-rounds action.
```

### Markdown Format (`runs/{desc}-{nnn}.md`)

Human-readable narrative format — like the session file we created, with full prose, dialogue, and dramatic structure.

---

## Directory Structure

```
skills/experiment/
├── CARD.yml
├── SKILL.md  (this file)
├── README.md
├── EXPERIMENT.yml.tmpl      # Template for new experiments
├── RUN-CONFIG.yml.tmpl      # Template for run configurations
├── RUN-OUTPUT.yml.tmpl      # Template for run outputs
├── RUN-OUTPUT.md.tmpl       # Narrative output template
└── experiments/
    ├── INDEX.yml
    └── emo-poker-face/
        ├── EXPERIMENT.md           # Experiment definition
        ├── RELATIONSHIPS.yml       # Character relationships + poker profiles
        └── runs/
            ├── INDEX.yml           # Registry of configs and outputs
            │
            ├── whacky-eight.yml    # CONFIG: 8 players, full chaos
            ├── whacky-eight-001.yml  # OUTPUT: first execution
            ├── whacky-eight-001.md   # OUTPUT: narrative version
            ├── whacky-eight-002.yml  # OUTPUT: second execution
            │
            ├── minimal-three.yml   # CONFIG: 3 players, quick test
            ├── minimal-three-001.yml
            │
            └── model-compare.yml   # CONFIG: same setup, compare models
                model-compare-001.yml  # claude-opus
                model-compare-002.yml  # claude-sonnet
```

**Naming Convention (Big-Endian):**
- Config: `{config-name}.yml`
- Output: `{config-name}-{NNN}.yml` or `.md`
- NNN is zero-padded 3 digits, auto-increments

---

## Integration with Other Skills

| Skill | Integration |
|-------|-------------|
| `character` | Load CHARACTER.yml for slot binding |
| `simulation` | Core generation capability |
| `evaluator` | Rubric scoring |
| `speed-of-light` | Single-call multi-turn generation |
| `representation-ethics` | Ethical character simulation |
| `rubric` | Criteria definition |
| `adventure` | Room/location context loading |

---

## Model Requirements

Different experiments may require different model capabilities:

```yaml
model_requirements:
  minimum_context: 100000  # tokens
  capabilities:
    - multi_turn_consistency
    - character_voice_distinction  
    - theory_of_mind
    - relationship_awareness
  recommended_models:
    - claude-opus-4
    - claude-sonnet-4
    - gpt-4-turbo
```

---

## Running Your First Experiment

```bash
# 1. List available experiments
LIST

# 2. View experiment definition
READ experiments/emo-poker-face/EXPERIMENT.md

# 3. Run with default characters
RUN emo-poker-face --output both

# 4. Run with custom cast
RUN emo-poker-face \
  --characters "host=richard-bartle,p1=don,p2=palm,p3=donna" \
  --output md

# 5. Evaluate the run
EVALUATE runs/whacky-eight-001.yml

# 6. Compare two runs
COMPARE runs/whacky-eight-001.yml runs/whacky-eight-002.yml
```
