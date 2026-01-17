# EvalCity: Design Document

> *What You Measure Is What You Get.*

---

## What Is EvalCity?

**EvalCity** is the EVAL version of SimCity — a civic simulation where **evaluation metrics, not just resources, shape the city**.

| SimCity asks | EvalCity asks |
|--------------|---------------|
| How do cities grow? | How do cities judge themselves? |
| What systems make a city work? | What metrics make a city "succeed"? |
| How do you balance resources? | How do you balance values? |

---

## Core Fantasy

You don't just zone land and build roads.

You define:
- Success metrics
- Compliance thresholds
- Audit mechanisms
- Performance reviews
- Enforcement priorities
- Appeal systems
- Transparency levels

**You don't build a city. You build a city's evaluation infrastructure.**

---

## Core Mechanics

### Metrics as Laws

In EvalCity, every metric becomes a law:

| SimCity | EvalCity |
|---------|----------|
| Population | Counted how? |
| Crime rate | Defined how? |
| Happiness | Measured how? |
| Pollution | By whose standard? |

**The metric's definition IS the ideology.**

### Goodhart's Law as Gameplay

> "When a measure becomes a target, it ceases to be a good measure."

This is the central tension:
- Set metrics → people optimize for them
- Optimization distorts behavior
- Distortion corrupts the metric
- You need new metrics
- Repeat forever

**Metric gaming is not a bug. It's the game.**

---

## What You Control

| Control | Effect |
|---------|--------|
| **Metric definitions** | What counts as "success" |
| **Data collection** | What gets measured |
| **Threshold settings** | What triggers action |
| **Enforcement priorities** | What actually gets enforced |
| **Audit frequency** | How often checks happen |
| **Appeal systems** | How to challenge judgments |
| **Transparency** | What the public sees |

---

## Failure Modes (As Gameplay)

| Failure | Description |
|---------|-------------|
| **Goodhart collapse** | Metrics gamed into meaninglessness |
| **Metric proliferation** | Too many metrics, analysis paralysis |
| **Enforcement bias** | Uneven application reveals prejudice |
| **Audit theater** | Appearance of oversight without substance |
| **Transparency theater** | Data without understanding |
| **Value laundering** | Bad outcomes renamed as good |
| **Bureaucratic evil** | Harm through process, not intent |

**Winning is never permanent. Stability is always provisional.**

---

## Citizen Behavior

Citizens in EvalCity:
- Optimize for visible metrics
- Game thresholds
- Appeal unfair judgments
- Protest metric definitions
- Form advocacy groups
- Corrupt inspectors
- Move to lower-scrutiny zones
- Start underground economies

**They are rational actors in an evaluation environment.**

---

## Zones as Evaluation Regimes

| Zone Type | Evaluation Character |
|-----------|---------------------|
| **High-compliance** | Heavy inspection, many metrics |
| **Light-touch** | Few metrics, self-reporting |
| **Experimental** | Changing metrics, pilot programs |
| **Legacy** | Old metrics, grandfathered exceptions |
| **Autonomous** | Community-defined metrics |
| **Exempt** | No formal evaluation |

---

## Historical Scenarios

Play through real evaluation regimes:

| Scenario | Theme |
|----------|-------|
| **Victorian London** | Sanitation metrics, class bias |
| **Soviet planning** | Production quotas, falsification |
| **Credit scoring** | Financial judgment, discrimination |
| **School testing** | Achievement metrics, teaching to test |
| **ESG ratings** | Corporate evaluation, greenwashing |
| **Social credit** | Comprehensive citizen scoring |

**Each scenario is procedural rhetoric about a real evaluation system.**

---

## Kay's Critique, Answered

Alan Kay said SimCity's assumptions are hidden. EvalCity's are explicit:

| SimCity | EvalCity |
|---------|----------|
| "More police = less crime" | You define the relationship |
| Industrial zoning logic | You set compliance rules |
| Tax rate effects | You choose what to measure |
| Hidden formulas | Inspectable evaluation |

**Every assumption is a setting you control.**

---

## Bogost's Procedural Rhetoric

EvalCity makes procedural rhetoric explicit:
- The simulation's rules ARE the argument
- But you can see them
- And change them
- And see what happens

**This is procedural rhetoric as a tool, not just an observation.**

---

## Technical Integration

| MOOLLM Concept | EvalCity Mapping |
|----------------|------------------|
| Rooms | City districts |
| CARD.yml | Policy interfaces |
| Skills | Evaluation protocols |
| Characters | Citizens, officials, activists |
| Session logs | City history |
| Worms | Audit bots |

---

## Micropolis Reverse Engineering

**The vision:** Extract SimCity's hidden logic into visible, editable YAML Jazz.

### The Pipeline

```
Original C++ Source → YAML Jazz Behavior Modules → LLM Interpretation
        ↓                        ↓                        ↓
   Micropolis engine      Readable prompts/data      Dynamic simulation
```

### How It Works

1. **Reverse-engineer** the Micropolis C++ source into YAML behavior modules
2. **Each module** describes one simulation mechanic as data + prompt
3. **The C++ engine** (or Python/JS wrapper) emits YAML events per zone
4. **The LLM** interprets events using the behavior modules
5. **Players** can read, edit, and reprogram any module

```yaml
# Example: Zone behavior module (extracted from C++ logic)
behavior: residential_growth
_comments: "Reverse-engineered from Micropolis zone.cpp"

inputs:
  - land_value
  - crime_rate
  - pollution
  - traffic
  - nearby_services

formula:
  # Original C++ logic, now visible:
  growth_score: (land_value * 0.3) - (crime * 0.2) - (pollution * 0.25) - (traffic * 0.1)
  
  _comments: |
    Note the hidden assumptions:
    - Land value weighted highest (capitalist bias?)
    - Crime and pollution roughly equal (are they?)
    - Traffic underweighted (car-centric?)
    
    YOU CAN CHANGE THESE WEIGHTS.

outputs:
  - population_delta
  - density_change
  - building_upgrade

events_emitted:
  - zone_grew
  - zone_declined
  - resident_moved
```

### Gingold-Style Diagrams as Data

Chaim Gingold's [reverse diagrams of SimCity](https://www.chaimgingold.com/) show visually how the simulation works. We make these **executable**:

```yaml
# Gingold diagram as YAML Jazz
diagram: simcity_power_flow
_comments: "Based on Gingold's visual reverse-engineering"

nodes:
  - id: power_plant
    type: source
    output: electricity
    
  - id: power_line
    type: conductor
    loss_per_tile: 0.02
    
  - id: zone
    type: sink
    requires: electricity
    behavior_without: |
      Becomes blighted. Industry leaves.
      _comments: "Why is power loss so catastrophic? Editable."

edges:
  - from: power_plant
    to: power_line
    flow: electricity
    
  - from: power_line
    to: zone
    flow: electricity
    decay: distance_based
```

### Victor-Style Dynamic Editing

In the spirit of Brett Victor, everything is **live-editable**:

| Brett Victor Principle | EvalCity Implementation |
|------------------------|-------------------------|
| See the state | YAML is always visible |
| Scrub time | Session logs replay any moment |
| Edit and see | Change formula, see immediate effect |
| No hidden state | Every assumption is a YAML field |

```yaml
# Live editing example
residential_growth:
  crime_weight: 0.2      # ← Drag this slider
  pollution_weight: 0.25  # ← Watch city respond
  
  _live_preview:
    affected_zones: 847
    projected_population_change: +12,340
    projected_land_value_change: -$2.3M
    
  _comments: |
    Try it: What if crime mattered less?
    What if pollution mattered more?
    The city will teach you what your values cost.
```

### Zone Events for LLM Simulation

The C++ engine emits events; the LLM interprets:

```yaml
# Engine output (per tick, per zone)
zone_event:
  tick: 4523
  zone_id: "R-47"
  type: residential
  
  state:
    population: 1240
    density: medium
    land_value: 72
    crime: 18
    pollution: 34
    power: true
    water: true
    
  neighbors:
    north: industrial
    south: commercial
    east: park
    west: residential
    
  pending_effects:
    - nearby_industrial_pollution: +5
    - park_land_value_boost: +8
    
  _prompt: |
    Given this zone's state and the residential_growth behavior module,
    determine: Should this zone grow, decline, or stay stable?
    Emit events for any changes.
```

### Why This Matters

| Hidden (Original SimCity) | Visible (EvalCity) |
|---------------------------|-------------------|
| Magic numbers in C++ | Named weights in YAML |
| Compiled behavior | Readable behavior modules |
| "That's just how it works" | "Here's why — change it if you disagree" |
| Play the designer's assumptions | Play YOUR assumptions |

**This is Alan Kay's critique, resolved through architecture.**

---

## The Uplift Architecture

**First EvalCity model:** Reverse-engineer Micropolis, UPLIFT it into YAML Jazz.

### Body and Mind

| Component | Role | Technology |
|-----------|------|------------|
| **Body** | The grid, the physics, the state | Micropolis C++ (or Python/JS port) |
| **Mind** | Interpretation, behavior, judgment | LLM + YAML Jazz modules |
| **Shared World** | Standard SimCity tile grid | Classic .cty save file (extended) |

The simulator is the body. The LLM is the mind. They share the microworld.

### The Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  SAVE FILE (Extended .cty)                                      │
│  ├── Standard tile grid                                         │
│  ├── Zone states                                                │
│  └── Agent metadata (NEW)                                       │
│                                                                 │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  SIMULATOR (C++/WASM/Python/JS)                                 │
│  ├── Parse save file                                            │
│  ├── Apply physics (fire spread, power flow, traffic)           │
│  └── BLURT OUT: YAML events for each object                     │
│                                                                 │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  LLM + YAML JAZZ MODULES                                        │
│  ├── Receive object blurts                                      │
│  ├── Apply behavior rules (editable!)                           │
│  ├── Emit Scats (evaluations, judgments)                        │
│  └── WRITE BACK: Tile edits, agent updates                      │
│                                                                 │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
                  SAVE FILE (updated)
                       │
                       └──────────────────────────────────────────→ repeat
```

### Object Blurts

The simulator doesn't just update tiles — it **blurts** structured descriptions:

```yaml
# Simulator blurt: Zone object
blurt:
  type: zone
  id: "R-47"
  location: [23, 45]
  
  state:
    zone_type: residential
    density: medium
    population: 1240
    powered: true
    watered: true
    
  environment:
    land_value: 72
    crime: 18
    pollution: 34
    traffic: medium
    
  neighbors:
    north: { type: industrial, pollution_contribution: +5 }
    east: { type: park, land_value_boost: +8 }
    
  _prompt: |
    This zone is residential, medium density, near industry.
    Apply residential_growth module. Should it grow or decline?
```

### Agents as Persistent Objects

Classic SimCity agents (tornado, monster, helicopter) become **persistent objects with metadata**:

```yaml
# Extended save file: Agent metadata
agents:
  
  helicopter_1:
    type: helicopter
    location: [45, 67]
    state: flying
    
    # NEW: LLM-managed metadata
    destination: [23, 45]
    destination_reason: "Responding to fire at R-47"
    mood: urgent
    pilot_name: "Officer Chen"
    
    _history:
      - "Dispatched from helipad at [12, 34]"
      - "Diverted from traffic patrol due to fire emergency"
      
    _behavior_module: helicopter_patrol
    
  tornado_1:
    type: disaster
    subtype: tornado
    location: [78, 23]
    path_direction: northeast
    
    # Tornado as character
    personality: "Chaotic, indifferent, beautiful in destruction"
    
    _comments: |
      In classic SimCity, the tornado is random.
      In EvalCity, you can ask: WHY is there a tornado?
      Climate policy? Divine judgment? Just weather?
      The answer affects how citizens respond.
      
  monster_1:
    type: disaster
    subtype: monster
    location: [56, 89]
    target: nuclear_plant_1
    
    motivation: "Attracted to radiation"
    origin_story: "Awakened by seismic activity from highway construction"
    
    _behavior_module: monster_rampage
    _can_be_reasoned_with: false
    _can_be_distracted: true
    _distraction_targets: [stadium, power_plant]
```

### LLM Edits

The LLM responds to blurts with **tile edits** and **agent updates**:

```yaml
# LLM response: Edits to apply
edits:
  
  tiles:
    - location: [23, 45]
      change: density_increase
      reason: "Park nearby boosted land value enough to trigger growth"
      
    - location: [24, 45]
      change: blight
      reason: "Industrial pollution exceeded residential tolerance"
      
  agents:
    - id: helicopter_1
      update:
        location: [23, 45]
        state: hovering
        action: "Assessing fire damage"
        next_action: "Return to helipad if fire contained"
        
  events:
    - type: citizen_protest
      location: [24, 45]
      cause: "Blight from industrial pollution"
      participants: 47
      demand: "Rezone industrial to commercial"
      
  scats:
    - stance: 🏭❌
      take: "Industrial-residential adjacency is failing"
      evidence: "3 residential zones blighted in 10 ticks"
      recommendation: "Buffer zone or rezoning needed"
```

### The Extended Save File

Classic .cty format + YAML Jazz metadata:

```yaml
# evalcity_save.yml (wraps or extends .cty)

format_version: "evalcity-1.0"
base_save: "city.cty"  # Original Micropolis save

# Extended metadata
metadata:
  city_name: "New Evalopolis"
  mayor: "Player One"
  evaluation_regime: "balanced_sustainability"
  
# Agent persistence (not in original .cty)
agents:
  - { id: helicopter_1, ... }
  - { id: tornado_1, ... }
  
# Behavior modules loaded
modules:
  - residential_growth
  - industrial_pollution
  - traffic_congestion
  - disaster_response
  
# Session log
history:
  - tick: 4520
    events: [...]
  - tick: 4521
    events: [...]
    
# Player's evaluation stance
player_values:
  environment_weight: 0.4
  economy_weight: 0.3
  equity_weight: 0.3
  _comments: "I care more about pollution than growth"
```

**The classic SimCity grid is preserved. The LLM adds soul.**

---

## Hybrid Simulation: Deterministic + LLM

The classic Micropolis simulator runs tick-by-tick. The LLM runs **in parallel**, observing and intervening.

### Parallel Execution

```
┌────────────────────────────────────────────────────────────────────────┐
│                           GAME LOOP                                    │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   TICK N                                                               │
│   ┌──────────────────────┐    ┌──────────────────────┐                 │
│   │  SIMULATOR (sync)    │    │  LLM (async)         │                 │
│   │  - Fire spread       │───▶│  - Interpret events  │                 │
│   │  - Power flow        │    │  - Generate Scats    │                 │
│   │  - Traffic           │◀───│  - Edit save file    │                 │
│   │  - Zone growth       │    │  - Update metadata   │                 │
│   └──────────────────────┘    └──────────────────────┘                 │
│            │                            │                              │
│            ▼                            ▼                              │
│        STATE N+1                  EDITS QUEUED                         │
│            │                            │                              │
│            └────────────┬───────────────┘                              │
│                         ▼                                              │
│                   MERGE & SAVE                                         │
│                         │                                              │
│                         ▼                                              │
│                     TICK N+1                                           │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘
```

### Disabling Simulator Sections

**Key feature:** Disable deterministic code, let LLM take over.

```yaml
# simulation_config.yml
simulator_modules:

  fire_spread:
    enabled: true
    llm_override: false
    
  power_distribution:
    enabled: true
    llm_override: false
    
  traffic_simulation:
    enabled: true
    llm_override: partial  # LLM handles edge cases
    
  zone_growth:
    enabled: false         # DISABLED — LLM handles entirely
    llm_override: true
    llm_module: residential_growth.yml
    
  crime_calculation:
    enabled: true
    llm_override: before   # LLM runs BEFORE deterministic
    llm_module: crime_context.yml
    
  pollution_spread:
    enabled: true
    llm_override: after    # LLM runs AFTER, can adjust
    llm_module: pollution_judgment.yml
    
  disasters:
    enabled: true
    llm_override: true     # LLM controls disaster behavior
    sub_modules:
      tornado:
        enabled: false     # LLM controls tornado entirely
        llm_module: tornado_character.yml
      monster:
        enabled: false
        llm_module: monster_rampage.yml
      fire:
        enabled: true      # Deterministic fire spread
        llm_override: false
```

### Override Modes

| Mode | Behavior |
|------|----------|
| `enabled: true, llm_override: false` | Pure deterministic (classic SimCity) |
| `enabled: true, llm_override: before` | LLM pre-processes, then deterministic runs |
| `enabled: true, llm_override: after` | Deterministic runs, then LLM adjusts |
| `enabled: true, llm_override: partial` | LLM handles specific sub-cases |
| `enabled: false, llm_override: true` | LLM entirely replaces this module |

### Blocking vs Async Operations

Some LLM operations are async (fire and forget). Some block the simulation.

```yaml
# Event types and their blocking behavior
event_handling:

  async_events:
    # These don't block — simulation continues
    - scat_generation       # LLM commentary
    - metadata_update       # Agent backstories
    - journal_entry         # Session logging
    - worm_crawl            # Background analysis
    
  blocking_events:
    # These pause simulation until resolved
    
    - type: human_confirmation
      description: "Requires yes/no from player"
      example: "Approve $500M stadium bond?"
      timeout: null  # Wait forever
      
    - type: major_disaster_response
      description: "Player chooses response strategy"
      example: "Tornado approaching. Evacuate or shelter?"
      timeout: 30s  # Auto-choose if no response
      
    - type: policy_decision
      description: "Evaluation criteria change"
      example: "Redefine 'affordable housing' threshold?"
      timeout: null
      
    - type: rpc_external
      description: "Remote procedure call to external service"
      example: "Fetch real weather data for climate scenario"
      timeout: 10s
      fallback: use_cached
      
  semi_blocking_events:
    # Simulation slows but doesn't stop
    
    - type: citizen_petition
      description: "Citizens demand attention"
      slow_factor: 0.5  # Half speed until addressed
      auto_resolve_after: 50_ticks
      
    - type: llm_deep_analysis
      description: "Complex evaluation in progress"
      slow_factor: 0.25
      can_be_skipped: true
```

### Human in the Loop

```yaml
# Blocking for human decision
blocking_event:
  type: referendum
  question: "Should we rezone the waterfront?"
  
  context:
    current_zone: industrial
    proposed_zone: mixed_residential_commercial
    affected_residents: 2400
    affected_jobs: 890
    
  options:
    - id: approve
      label: "Approve rezoning"
      consequences:
        - "+1200 housing units"
        - "-890 industrial jobs"
        - "+$2M tax revenue (projected)"
        
    - id: reject
      label: "Reject rezoning"
      consequences:
        - "Industrial continues"
        - "Waterfront pollution continues"
        - "Housing shortage worsens"
        
    - id: modify
      label: "Modify proposal"
      opens: rezoning_editor
      
  _simulation_state: PAUSED
  _waiting_for: player_input
  _timeout: null  # No auto-resolve for referendums
```

### Gradual Uplift Path

Start deterministic, gradually hand control to LLM:

| Phase | Deterministic | LLM |
|-------|---------------|-----|
| 1. Classic | 100% | 0% (observer only) |
| 2. Commentary | 100% | Scats, no edits |
| 3. Metadata | 100% | Agent backstories, no gameplay effect |
| 4. Edge cases | 95% | Handles exceptions |
| 5. Selected modules | 70% | Full control of some systems |
| 6. Full hybrid | 50% | Physics deterministic, behavior LLM |
| 7. Full uplift | 10% | Only core physics, LLM does rest |

**You choose where on this spectrum to play.**

```yaml
# Quick presets
simulation_preset: hybrid_50

presets:
  classic:
    description: "Original Micropolis behavior"
    deterministic: 100%
    llm_role: observer
    
  commentary:
    description: "Classic + LLM commentary"
    deterministic: 100%
    llm_role: scats_only
    
  hybrid_50:
    description: "Shared control"
    deterministic: [physics, power, fire]
    llm_controlled: [growth, behavior, disasters]
    
  full_eval:
    description: "LLM-driven, physics grounded"
    deterministic: [fire_spread, power_flow]
    llm_controlled: everything_else
```

---

## Player Modes

| Mode | Role |
|------|------|
| **Mayor** | Set city-wide policies |
| **Inspector** | Enforce on the ground |
| **Citizen** | Navigate the system |
| **Activist** | Challenge the metrics |
| **Journalist** | Expose the gaps |
| **Auditor** | Meta-evaluate the evaluation |

---

## Multiplayer Potential

| Mode | Description |
|------|-------------|
| **City councils** | Vote on metrics |
| **Inter-city competition** | Different evaluation regimes |
| **Federal mandates** | Top-down metrics vs local adaptation |
| **Citizen movements** | Organized metric resistance |

---

## City File Format: city.yml

### File Structure

```
mycity/
├── city.cty              # Binary Micropolis save (import/export)
├── city.yml              # YAML Jazz representation (LLM-readable)
└── city-metadata.yml     # Extended metadata sidecar
```

### Import/Export Flow

```
┌─────────────┐     import      ┌─────────────┐
│  city.cty   │ ───────────────▶│  city.yml   │
│  (binary)   │                 │  (YAML)     │
└─────────────┘                 └─────────────┘
       ▲                               │
       │         export                │
       └───────────────────────────────┘
```

The binary .cty is for the C++ simulator. The .yml is for the LLM.

### city.yml Format

```yaml
# city.yml — YAML Jazz representation of SimCity save
format: evalcity-1.0
source: city.cty

header:
  name: "New Evalopolis"
  mayor: "Player One"
  population: 45230
  funds: 12500
  year: 1985

map:
  width: 120
  height: 100
  
# Tile grid: symbolic or numeric
tiles:
  format: symbolic
  
  legend:
    ".": empty        "~": water        "#": forest
    "R": res_low      "r": res_med      "®": res_high
    "C": com_low      "c": com_med      "©": com_high
    "I": ind_low      "i": ind_med      "ℹ": ind_high
    "=": road         "H": highway      "+": intersection
    "P": coal_power   "N": nuke_power   "^": power_line
    "F": fire_stn     "D": police_stn   "G": park
    "*": fire         "!": rubble       "@": monster
    
  grid: |
    ~~~~~~~~~~~~.###.RRR.=.CCC.....~~~~
    ~~~~~~~~~~~~.###.rrr.=.ccc..P^^~~~~
    ~~~~~~~~~~~~.=====+=+==+======^~~~~
    ~~~~~~~~~~~~.....III.=.F.D....^~~~~

# Overlays: power, pollution, crime, traffic, land_value
overlays:
  
  power:
    format: binary  # 0/1
    grid: |
      000000001111111111111111
      000000001111111111111111
      
  pollution:
    format: numeric  # 0-255
    grid: |
      00,00,00,12,15,18,22,45,67
      00,00,00,15,20,25,30,55,78
      
  crime:
    format: heat
    legend: { ".": 0-10, "o": 11-30, "O": 31-60, "@": 61+ }
    grid: |
      .....ooooOOO@@@.....
      
  traffic:
    format: symbolic
    legend: { ".": none, "-": light, "=": medium, "#": heavy }
    grid: |
      ....---===###....

# Zones as structured objects (for LLM comprehension)
zones:
  - id: R-01
    type: residential
    density: low
    location: [12, 2]
    population: 120
    powered: true
    
  - id: I-01
    type: industrial
    location: [12, 6]
    jobs: 230
    pollution_output: 45

buildings:
  - id: power_plant_1
    type: coal
    location: [28, 4]
    output: 1200
```

### city-metadata.yml (Sidecar)

Extended metadata not in original .cty:

```yaml
# city-metadata.yml — EvalCity extensions
format: evalcity-metadata-1.0

# Agents with LLM-managed state
agents:
  helicopter_1:
    location: [45, 67]
    destination: [23, 45]
    destination_reason: "Responding to fire"
    pilot_name: "Officer Chen"
    
  tornado_1:
    location: [78, 23]
    personality: "Chaotic, beautiful"
    motivation: "Climate instability"

# Zone stories
zone_metadata:
  R-01:
    nickname: "Sunrise Heights"
    character: "Working class, tight-knit"
    issues: ["Rising pollution from I-01"]
    
  I-01:
    nickname: "The Foundry District"
    controversy: "Pollution affecting residents"
    protests: 3

# Player evaluation stance
player_values:
  environment_weight: 0.4
  economy_weight: 0.3
  equity_weight: 0.3
  _comments: "I care more about pollution than growth"

# Recent evaluations
scats:
  - tick: 45200
    stance: 🏭❌
    take: "Industrial-residential adjacency failing"
    
# History
history:
  - tick: 34000
    event: "Tornado destroyed downtown"
    damage: "$2.3M"
```

### Compact Tile Symbols

```
Legend (single-character grid):
────────────────────────────────
.  empty     ~  water      #  forest
R  res_low   r  res_med    ®  res_high
C  com_low   c  com_med    ©  com_high
I  ind_low   i  ind_med    ℹ  ind_high
=  road      H  highway    +  intersection
P  coal      N  nuke       ^  power_line
F  fire_stn  D  police     G  park
*  fire      !  rubble     @  monster
────────────────────────────────
```

**The LLM reads city.yml. The simulator reads city.cty. They stay in sync.**

### LLM Tile Editing: Commands vs Raw Data

**The question:** Can LLMs handle raw hex/base64 tile data?

| Format | Compactness | LLM Read | LLM Edit | Verdict |
|--------|-------------|----------|----------|---------|
| Symbolic grid | Medium | ✅ Excellent | ⚠️ Error-prone | Good for viewing |
| Numeric CSV | Medium | ✅ Good | ⚠️ Error-prone | Good for viewing |
| Hex string | High | ⚠️ Possible | ❌ Very hard | Not recommended |
| Base64 | Highest | ❌ Opaque | ❌ Impossible | For transport only |
| Raw binary | Highest | ❌ No | ❌ No | Simulator only |

**Insight:** LLMs can *read* compact representations, but they shouldn't *edit* them directly. Too error-prone. Off-by-one errors. Bit flips.

### The Solution: Editing Tool Commands

Like a user drawing on the map, the LLM issues **structured commands**.

**Key rule:** Every command requires `why` — the intent is a **required parameter**.

```yaml
# LLM output: editing commands with required intent
edit_commands:

  # Point operations
  - command: set_tile
    location: [23, 45]
    tile_type: residential_low_cottage
    why: "Expanding housing to address population demand from new factory jobs"
    
  - command: bulldoze
    location: [24, 46]
    why: "Clearing blighted structure to make room for park buffer"
    
  # Line operations (roads, power lines)
  - command: draw_road
    from: [10, 10]
    to: [20, 10]
    why: "Connecting new residential zone to main street for commuter access"
    
  - command: draw_power_line
    from: [28, 4]
    to: [28, 20]
    why: "Extending grid to power new southern development"
    
  # Rectangle operations (zones)
  - command: zone_area
    type: commercial
    top_left: [30, 30]
    size: [3, 3]
    why: "Creating commercial buffer between industrial and residential"
    
  # Building placement
  - command: place_building
    type: fire_station
    location: [15, 25]
    why: "Coverage gap in northeast quadrant — response times too slow"
    
  # Cursor-based (for sequential operations)
  - command: move_cursor
    to: [50, 50]
    why: "Starting downtown renovation project"
    
  - command: draw_from_cursor
    direction: east
    length: 10
    type: road
    why: "Main street extension for traffic flow improvement"
```

### Command Validation and Retry

The command interpreter validates and returns results. LLM can retry on failure.

**Key:** Responses echo back the original command so LLM has full context.

```yaml
# Command response configuration
response_config:
  echo_on_error: true      # Always echo original command
  echo_on_warning: true    # Always echo original command
  echo_on_success: false   # Default: silent success (no response)
  verbose_success: false   # Set true to get detailed success responses
```

```yaml
# Command interpreter responses — with full echo
command_results:

  # Success: silent by default (no response unless requested)
  # If verbose_success: true, you get:
  - command_id: cmd_001
    status: success
    echo:
      command: zone_area
      type: commercial
      top_left: [30, 30]
      size: [3, 3]
      why: "Creating commercial buffer between industrial and residential"
    result:
      tiles_changed: 9
      new_zone_id: C-15
      
  # Error: always echoes original so LLM remembers what it was doing
  - command_id: cmd_002
    status: error
    echo:
      command: place_building
      type: fire_station
      location: [15, 25]
      why: "Coverage gap in northeast — response times too slow"
    error_code: INSUFFICIENT_FUNDS
    message: "Fire station costs $500. Current funds: $350."
    suggestion: "Wait for tax revenue or reduce other spending."
    context:
      current_funds: 350
      required_funds: 500
      shortfall: 150
      estimated_ticks_to_afford: 8
    
  # Warning: echoes original, shows what's blocking
  - command_id: cmd_003
    status: warning
    echo:
      command: draw_road
      from: [10, 10]
      to: [20, 10]
      why: "Connecting new residential zone to main street for commuter access"
    warnings:
      - code: CROSSES_WATER
        message: "Road would cross water at [15, 12]. Bridge required."
        cost_increase: "$200 for bridge"
        at_location: [15, 12]
      - code: DEMOLITION_REQUIRED
        message: "Path crosses existing structure at [16, 10]."
        affected: "Residential building (population: 45)"
        at_location: [16, 10]
    action_required: confirm_or_modify
    options:
      - action: confirm
        description: "Proceed with bridge and demolition"
        total_cost: "$400 + demolition"
      - action: modify
        description: "Reroute to avoid obstacles"
      - action: cancel
        description: "Abandon this road"
    
  # Error: echoes original with suggestion
  - command_id: cmd_004
    status: error
    echo:
      command: set_tile
      location: [150, 200]
      tile_type: residential_low
      why: "Expanding housing on city edge"
    error_code: INVALID_LOCATION
    message: "Location [150, 200] is outside map bounds (120x100)."
    suggestion: "Check coordinates. Did you mean [50, 20]?"
    context:
      map_bounds: [120, 100]
      requested: [150, 200]
      nearest_valid: [119, 99]
```

### Why Echo the Original?

| Without echo | With echo |
|--------------|-----------|
| "Error: insufficient funds" | "You tried to place fire station at [15,25] because 'coverage gap in northeast'. Failed: insufficient funds." |
| LLM forgets context | LLM sees full picture |
| Retry is guesswork | Retry is informed |
| Intent lost | Intent preserved |

The echo reminds the LLM:
- **What** it was trying to do
- **Where** it was trying to do it
- **Why** it wanted to do it

This enables intelligent retry — not just repeating, but adapting strategy while preserving original intent.

### LLM Retry Pattern

```yaml
# LLM receives error, retries with correction
retry_sequence:

  attempt_1:
    command: place_building
    type: fire_station
    location: [15, 25]
    why: "Coverage gap in northeast"
    
    result:
      status: error
      error_code: INSUFFICIENT_FUNDS
      message: "Costs $500. Funds: $350."
      
  attempt_2:
    # LLM adjusts strategy
    command: wait_for_funds
    target_amount: 500
    why: "Need to accumulate funds for fire station"
    
    result:
      status: success
      ticks_waited: 12
      new_balance: $520
      
  attempt_3:
    # LLM retries original intent
    command: place_building
    type: fire_station
    location: [15, 25]
    why: "Coverage gap in northeast (retry after funding)"
    
    result:
      status: success
      building_id: fire_station_3
```

### Why Intent is Required

| Without `why` | With `why` |
|---------------|------------|
| "Place road here" | "Place road here to reduce commute time" |
| Action only | Action + reasoning |
| No audit trail | Decisions are explainable |
| Can't evaluate quality | Can judge if intent was achieved |
| Opaque to review | Transparent to players and worms |

**The `why` parameter turns commands into arguments. Every edit is a claim about what should happen and why.**

### Why Commands > Direct Edits

| Direct Grid Edit | Command-Based |
|------------------|---------------|
| "Change char at row 45 col 23 to 'R'" | `set_tile([23,45], residential)` |
| Error-prone (wrong row? wrong char?) | Semantic, validated |
| No undo history | Commands are logged |
| Hard to reason about | Intentions are clear |
| No retry on failure | Errors return, LLM retries |
| Silent corruption | Validated before apply |
| Can corrupt grid | Simulator validates |

### Viewing vs Editing Modes

```yaml
# For VIEWING: compact representation is fine
view_mode:
  format: symbolic_grid
  show_overlays: [pollution, traffic]
  
  # LLM sees this:
  grid_excerpt: |
    ~~~~~~~~~~~~.###.RRR.=.CCC.....
    ~~~~~~~~~~~~.###.rrr.=.ccc..P^^
    
  # LLM understands: "residential near industrial, power plant east"

# For EDITING: LLM emits commands
edit_mode:
  input: structured_commands
  validation: simulator_confirms
  
  # LLM emits:
  commands:
    - { command: zone_area, type: park, location: [25, 30], size: [2, 2] }
    - { command: draw_road, from: [25, 32], to: [30, 32] }
```

### Cursor-Based Editing (Natural Mode)

For complex operations, cursor metaphor is intuitive:

```yaml
cursor_session:
  # LLM controls a virtual cursor like a player
  
  - move: [50, 50]
    _comments: "Start at city center"
    
  - select_tool: road
  
  - drag:
      direction: east
      distance: 15
    _comments: "Main street extension"
    
  - move: [50, 55]
  
  - select_tool: zone_residential
  
  - drag:
      direction: southeast
      size: [6, 4]
    _comments: "New housing development"
    
  - select_tool: query
  
  - click: [52, 57]
    # Returns zone info for LLM to evaluate
```

### Hex/Base64 for Transport Only

```yaml
# Compact transport format (between systems, not for LLM editing)
tile_data:
  format: base64_uint16
  width: 120
  height: 100
  encoding: little_endian
  
  # 120 * 100 * 2 bytes = 24KB, base64 = ~32KB
  data: "AAAAAAAAAAEBAQEBAgICAgIDAwMD..."
  
  _note: |
    This is for efficient storage/transport.
    LLM should NOT edit this directly.
    Use edit_commands instead.
    Simulator decodes, applies commands, re-encodes.
```

### The Pattern

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   LLM READS:        Symbolic grid, zone objects, overlays   │
│                     (Human-readable, semantic)              │
│                                                             │
│   LLM WRITES:       Edit commands, cursor operations        │
│                     (Structured, validated, logged)         │
│                                                             │
│   SIMULATOR READS:  Binary .cty, hex tiles, raw data        │
│                     (Efficient, direct)                     │
│                                                             │
│   SIMULATOR WRITES: YAML events, state blurts               │
│                     (Translated for LLM consumption)        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**LLMs are readers and commanders, not byte-pushers.**

---

## LLM Simulation Pipeline

The LLM doesn't simulate everything at once. It runs in **staged passes**:

### The Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  STAGE 0: CONTEXT LOAD                                                  │
│  ├── Read game state (city.yml)                                         │
│  ├── Read rules (behavior modules)                                      │
│  └── Read input queue (main_events.yml)                                 │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  STAGE 1: EVENT ROUTING                                                 │
│  ├── Process main event queue                                           │
│  ├── Transform events → more specific events                            │
│  ├── Distribute to agent queues (append to .yml files)                  │
│  └── NO SIMULATION YET — just message passing                           │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  STAGE 2: AGENT WAKE-UP                                                 │
│  ├── Each agent pops events from their personal queue                   │
│  ├── Agents process events, send messages to other agents               │
│  ├── Still not simulating — preparing responses                         │
│  └── May take 1 or N passes per agent (based on "awakeness")            │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  STAGE 3: SIMULATION EXECUTION                                          │
│  ├── Agents execute their prepared actions                              │
│  ├── State changes applied                                              │
│  ├── New events generated                                               │
│  └── Results written back to game state                                 │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Stage 1: Event Routing

The first LLM pass just routes and transforms — no simulation work yet.

```yaml
# main_events.yml — Input queue
events:
  - id: evt_001
    type: user_action
    action: zone_residential
    location: [50, 60]
    size: [3, 3]
    timestamp: tick_45000
    
  - id: evt_002
    type: simulator_output
    subtype: fire_started
    location: [23, 45]
    intensity: 3
    
  - id: evt_003
    type: citizen_complaint
    about: pollution
    source_zone: I-01
    affected_zone: R-01
```

LLM Stage 1 output — **distribute to agent queues**:

```yaml
# Output: events routed to specific queues

# → append to agents/fire_department/events.yml
fire_department_events:
  - id: evt_002_routed
    original: evt_002
    type: fire_alert
    location: [23, 45]
    priority: high
    message: "Fire detected. Dispatch required."
    
# → append to agents/city_planner/events.yml  
city_planner_events:
  - id: evt_001_routed
    original: evt_001
    type: zone_request
    location: [50, 60]
    zone_type: residential
    message: "User requested residential zone."
    requires: [power_check, water_check, approval]
    
# → append to agents/environmental_board/events.yml
environmental_events:
  - id: evt_003_routed
    original: evt_003
    type: complaint_received
    source: citizen
    issue: pollution
    accused: I-01
    message: "Citizen complaint about industrial pollution."
    requires: [investigation, ruling]
```

### Stage 2: Agent Wake-Up

Each agent processes their queue. Some need one pass, some need many.

```yaml
# Agent awakeness levels
agent_config:

  fire_department:
    awakeness: high          # Always responsive
    passes_per_tick: 1       # Quick decisions
    queue: agents/fire_department/events.yml
    
  city_planner:
    awakeness: medium        # Deliberate
    passes_per_tick: 1-3     # May need review cycles
    queue: agents/city_planner/events.yml
    
  environmental_board:
    awakeness: low           # Bureaucratic
    passes_per_tick: 0-1     # Often skips ticks
    backlog_threshold: 5     # Wakes up when queue builds
    queue: agents/environmental_board/events.yml
    
  citizens:
    awakeness: variable      # Based on events
    batch_processing: true   # Many agents, one pass
    passes_per_tick: 0-1
```

Agent processing example:

```yaml
# agents/fire_department/events.yml — Agent pops their queue
incoming:
  - id: evt_002_routed
    type: fire_alert
    location: [23, 45]
    priority: high

# Fire department agent processes:
agent_response:
  agent: fire_department
  event: evt_002_routed
  
  internal_state_update:
    active_fires: +1
    
  outgoing_messages:
    # Send to helicopter agent
    - to: agents/helicopter_1/events.yml
      message:
        type: dispatch_order
        destination: [23, 45]
        reason: "Fire response"
        priority: urgent
        
    # Send to fire station agents
    - to: agents/fire_station_1/events.yml
      message:
        type: deploy_units
        count: 2
        destination: [23, 45]
        
    # Notify mayor (low priority)
    - to: agents/mayor/events.yml
      message:
        type: incident_report
        incident: fire
        location: [23, 45]
        priority: info
        
  # NOT executing yet — just prepared responses
  pending_actions: []
```

### Batch Agent Processing

For many small agents (citizens, zones), process in batches:

```yaml
# One LLM call handles many agents
batch_processing:
  agent_type: citizen
  count: 50
  
  # All 50 citizens processed in one prompt
  context:
    - citizen_1: { events: [...], state: {...} }
    - citizen_2: { events: [...], state: {...} }
    ...
    
  output:
    - citizen_1: { messages: [...], mood_change: +0.1 }
    - citizen_2: { messages: [...], mood_change: -0.2 }
    ...
```

### Stage 3: Simulation Execution

After routing and agent preparation, execute the actual changes:

```yaml
# Collected actions from all agents
execution_queue:

  state_changes:
    - target: tile[23,45]
      change: fire_intensity
      from: 3
      to: 2  # Fire department effect
      
    - target: agent/helicopter_1
      change: location
      from: [12, 34]
      to: [23, 45]
      
    - target: zone/R-01
      change: pollution
      from: 34
      to: 36  # Slight increase from fire smoke
      
  new_events:
    - type: fire_contained
      location: [23, 45]
      tick: 45001
      
    - type: citizen_relief
      zone: R-01
      intensity: 0.3

  scats_emitted:
    - stance: 🚒✅
      take: "Fire department responded within 2 ticks"
      evaluation: positive
```

### Why Staged?

| All-at-once | Staged Pipeline |
|-------------|-----------------|
| One huge prompt | Smaller, focused prompts |
| Easy to overwhelm context | Fits in context window |
| Hard to debug | Each stage inspectable |
| No parallelism | Batch agents in parallel |
| Monolithic | Modular, composable |

### File-Based Message Passing

Events are just YAML appends — simple, inspectable, recoverable:

```
agents/
├── fire_department/
│   └── events.yml       # Fire dept's inbox
├── city_planner/
│   └── events.yml       # Planner's inbox
├── helicopter_1/
│   └── events.yml       # Helicopter's inbox
├── citizens/
│   ├── batch_001.yml    # Citizens 1-50
│   └── batch_002.yml    # Citizens 51-100
└── mayor/
    └── events.yml       # Mayor's inbox (usually ignored)
```

**Append to file = send message. Read from file = receive message. Simple as that.**

---

## Strip-Based Simulation: C64 Heritage → LLM Future

**Historical insight:** Original SimCity processed the city in **vertical strips** due to C64 memory constraints. This architecture maps perfectly to LLM context limits!

### How SimCity Works

```
┌──────────────────────────────────────────────────────────────┐
│                         CITY MAP                             │
│                                                              │
│  Strip 0  Strip 1  Strip 2  Strip 3  ...  Strip N            │
│  ┌────┐   ┌────┐   ┌────┐   ┌────┐       ┌────┐              │
│  │    │   │    │   │    │   │    │       │    │              │
│  │    │   │    │   │    │   │    │       │    │              │
│  │    │   │    │   │    │   │    │       │    │              │
│  │    │   │    │   │    │   │    │       │    │              │
│  │    │   │    │   │    │   │    │       │    │              │ 
│  └────┘   └────┘   └────┘   └────┘       └────┘              │
│                                                              │
│  Each tick: process one strip, advance to next               │
│  Full city processed over N ticks                            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

The C64 couldn't hold the whole city in memory. So SimCity:
1. Loads one vertical strip
2. Simulates that strip
3. Writes results back
4. Advances to next strip
5. Wraps around continuously

**This is exactly how we send chunks to an LLM!**

### Strip-Based LLM Simulation

```yaml
# Send one strip per LLM call
strip_simulation:
  current_strip: 5
  total_strips: 120
  strip_width: 1  # columns
  
  # What the LLM receives
  context:
    strip_data:
      column: 5
      height: 100
      tiles: |
        ~
        ~
        .
        R
        R
        r
        =
        I
        I
        .
        ...
        
    # Neighbors for edge effects
    left_strip_summary:
      column: 4
      zones: [residential, road]
      power: connected
      pollution: 12
      
    right_strip_summary:
      column: 6
      zones: [industrial, park]
      power: connected
      pollution: 45
      
    # Overlays for this strip
    overlays:
      power: [0,0,1,1,1,1,1,1,1,0,...]
      pollution: [0,0,5,8,12,15,18,45,50,35,...]
      traffic: [0,0,0,2,2,3,3,1,1,0,...]
      
  # LLM's job: simulate this strip
  task: |
    Process column 5. Apply zone growth, pollution spread (from neighbors),
    traffic effects. Emit events and state changes for this strip only.
```

### Why This Works Beautifully

| C64 Constraint | LLM Parallel |
|----------------|--------------|
| Limited RAM | Limited context window |
| Process strip by strip | Send strip by strip |
| Write back to disk/RAM | Write back to save file |
| Neighbor data at edges | Left/right strip summaries |
| Full city over N ticks | Full city over N calls |

### Parallelization Opportunity

Unlike the C64, we can process multiple strips in parallel:

```yaml
# Parallel strip processing
parallel_batch:
  strips: [0, 20, 40, 60, 80, 100]  # Every 20th strip
  
  # These strips are far enough apart that they don't interact
  # Can run 6 LLM calls in parallel
  
  # Edge strips (adjacent to each other) must be sequential
  sequential_passes:
    - [0, 1, 2, 3, ...]      # Pass 1: even strips
    - [1, 3, 5, 7, ...]      # Pass 2: odd strips (with updated neighbors)
```

### Strip-Sized Context

Each strip fits comfortably in context:

```yaml
strip_context_budget:
  strip_tiles: 100           # 100 tiles (one column)
  overlay_data: 400          # 4 overlays × 100 values
  neighbor_summaries: 200    # Left/right edge info
  rules_reminder: 500        # Behavior module excerpt
  task_prompt: 200           # What to do
  
  total_tokens: ~1,400       # Tiny! Leaves room for reasoning
  
  # Compare to full city:
  full_city_tiles: 12,000    # 120 × 100
  full_city_overlays: 48,000 # Would exceed most context windows
```

### The Uplift Path

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  ORIGINAL SIMCITY (C64)                                             │
│  └── Strip-based processing (memory constraint)                     │
│                                                                     │
│                         ↓ Uplift ↓                                  │
│                                                                     │
│  EVALCITY (LLM)                                                     │
│  └── Strip-based processing (context constraint)                    │
│      └── Same architecture, different reason!                       │
│      └── Can parallelize (C64 couldn't)                             │
│      └── LLM adds judgment, not just physics                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Strip Events

Each strip simulation emits events local to that strip:

```yaml
# Strip 5 simulation output
strip_5_results:
  
  state_changes:
    - row: 23
      change: population
      delta: +12
      why: "Adjacent commercial providing jobs"
      
    - row: 45
      change: pollution
      delta: +3
      why: "Drift from industrial in strip 6"
      
  events:
    - type: zone_upgraded
      location: [5, 23]
      from: residential_low
      to: residential_med
      
    - type: citizen_complaint
      location: [5, 45]
      issue: pollution
      source_direction: east  # From strip 6
      
  cross_strip_effects:
    # Effects that will apply when adjacent strips are processed
    - target_strip: 4
      effect: traffic_pressure
      amount: +2
      at_row: 30
      
    - target_strip: 6
      effect: land_value_boost
      amount: +5
      at_row: 23
      reason: "New residential development"
```

**The C64's memory constraint became SimCity's architecture. That architecture becomes the LLM's natural interface. History rhymes.**

---

## Programming by Demonstration: Watch the User, Learn the Style

**The user edits the map in real time. The LLM watches. This is programming by demonstration — the meat and potatoes and catnip of intuitive AI!**

### The User is Always Teaching

Every user action is an event the LLM can observe:

```yaml
# User action stream — LLM sees everything
user_events:

  - tick: 45000
    type: user_zone
    action: residential
    location: [50, 60]
    size: [3, 3]
    context:
      nearby: [industrial, park, road]
      funds_before: 12500
      funds_after: 11800
    # LLM notices: "User put residential near park, away from industrial"
    
  - tick: 45001
    type: user_bulldoze
    location: [23, 45]
    destroyed: blighted_residential
    context:
      pollution_level: 78
      crime_level: 45
    # LLM notices: "User cleared blight rather than trying to fix it"
    
  - tick: 45002
    type: user_road
    from: [50, 63]
    to: [60, 63]
    context:
      connects: [new_residential, main_street]
    # LLM notices: "User immediately connects new zones to infrastructure"
    
  - tick: 45010
    type: user_undo
    undid: user_zone
    location: [55, 70]
    # LLM notices: "User changed their mind — maybe wrong spot?"
    
  - tick: 45015
    type: user_pause
    duration: 30_seconds
    viewed: [pollution_overlay, traffic_overlay]
    # LLM notices: "User studying overlays before next action"
```

### Pattern Recognition

The LLM learns the user's style:

```yaml
# Inferred user patterns
user_style:
  
  inferred_preferences:
    - pattern: "Always places parks between industrial and residential"
      confidence: 0.89
      evidence: [action_23, action_45, action_67]
      
    - pattern: "Prioritizes fire coverage before expanding"
      confidence: 0.76
      evidence: [action_12, action_34]
      
    - pattern: "Avoids highways, prefers road networks"
      confidence: 0.82
      evidence: [never_used_highway_tool]
      
    - pattern: "Bulldozes blight quickly, doesn't wait for recovery"
      confidence: 0.91
      evidence: [action_5, action_18, action_29]
      
  inferred_values:
    environment_weight: 0.45  # Inferred from park placement
    economy_weight: 0.30     # Inferred from industrial patterns
    aesthetics_weight: 0.25  # Inferred from grid regularity
    
  play_style: "Careful planner, studies before acting, values buffers"
```

### LLM Adapts to User

Once the LLM knows the user's style, it can:

```yaml
# LLM suggestions based on learned style
adaptive_behavior:

  # Mirror user's patterns
  when_simulating_growth:
    apply: user_style.inferred_preferences
    example: "Since user always buffers industrial, simulate citizen expectations for buffers"
    
  # Predict what user would want
  proactive_suggestions:
    - suggestion: "Place park at [45, 30] to buffer new industrial?"
      reason: "Matches your pattern of industrial-residential buffering"
      confidence: 0.85
      
  # Ask in user's language
  dialogue_style:
    adapt_to: user_style.play_style
    example: "You usually study the overlays before expanding. Want to see pollution projections for this zone?"
    
  # Warn about breaks from pattern
  pattern_breaks:
    - warning: "You're placing residential directly adjacent to industrial"
      observation: "This differs from your usual buffer pattern"
      ask: "Intentional change, or would you like to add a park?"
```

### Teaching the LLM Explicitly

User can also teach directly:

```yaml
# Explicit teaching moments
teaching_events:

  - type: user_annotation
    action: zone_commercial
    location: [30, 40]
    user_note: "Tax revenue for upcoming stadium"
    # LLM learns: "Zoning can be strategic, not just demand-driven"
    
  - type: user_correction
    context: "LLM suggested industrial here"
    user_response: reject
    user_reason: "Too close to school"
    # LLM learns: "Schools have implicit buffers beyond overlay data"
    
  - type: user_demonstration
    action_sequence:
      - bulldoze: [10, 10]
      - zone: park
      - zone: residential_around_park
    user_label: "This is how I do neighborhood anchors"
    # LLM learns: "Parks first, then residential around them"
```

### The Feedback Loop

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   USER ACTS                                                         │
│   └── Zones, bulldozes, builds, pauses, undoes                      │
│                                                                     │
│              ↓                                                      │
│                                                                     │
│   LLM OBSERVES                                                      │
│   └── Sees every action as event with context                       │
│   └── Builds model of user's style and values                       │
│                                                                     │
│              ↓                                                      │
│                                                                     │
│   LLM ADAPTS                                                        │
│   └── Simulates according to inferred expectations                  │
│   └── Suggests in user's language                                   │
│   └── Warns about pattern breaks                                    │
│                                                                     │
│              ↓                                                      │
│                                                                     │
│   USER CORRECTS                                                     │
│   └── Accepts/rejects suggestions                                   │
│   └── Annotates decisions                                           │
│   └── Demonstrates preferred patterns                               │
│                                                                     │
│              ↓ (loop)                                               │
│                                                                     │
│   LLM REFINES                                                       │
│   └── Updates style model                                           │
│   └── Gets better at predicting                                     │
│   └── Becomes collaborative partner                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Why This is Catnip

| Traditional City Builder | EvalCity with PBD |
|--------------------------|-------------------|
| Game has fixed rules | Game learns YOUR rules |
| You play the designer's simulation | You teach YOUR simulation |
| "This is how cities work" | "This is how YOU think cities should work" |
| Optimization toward designer goals | Optimization toward YOUR goals |
| Static AI | Adaptive AI |

**Programming by demonstration means:**
- No configuration menus
- No preference dialogs  
- No "tell the AI what you want"
- Just **play**, and the AI **watches and learns**

**The map IS the program. Your actions ARE the specification. The LLM IS the student.**

---

## Why This Matters

EvalCity teaches:
- How metrics shape behavior
- Why "objective" measures aren't
- How bureaucracies work (and fail)
- Why transparency isn't enough
- What makes evaluation legitimate
- How power operates through data

**By letting players design evaluation systems and live with consequences.**

---

## Canonical Taglines

- **EvalCity** — What You Measure Is What You Get
- **EvalCity** — Govern the Criteria
- **EvalCity** — Every Metric Is a Choice
- **EvalCity** — Who Defines Success?

---

## Related Documents

- [EVAL-VS-SIM.md](./EVAL-VS-SIM.md) — Genre comparison
- [EVAL-BRAND-FAMILY.md](./EVAL-BRAND-FAMILY.md) — Title catalog
- [THE-EVALS-DESIGN.md](./THE-EVALS-DESIGN.md) — Social scale
- [../sims/simcity-multiplayer-micropolis.md](../sims/simcity-multiplayer-micropolis.md) — SimCity heritage

---

## Credits & Influences

| Person/Project | Contribution | EvalCity Connection |
|----------------|--------------|---------------------|
| **Will Wright** | SimCity, The Sims | Tile-based simulation, Simulator Effect |
| **Alexander Repenning** | AgentSheets, AgentCubes (1991-) | **Programming by Example**, graphical rewrite rules, "SimCity in 10 minutes" benchmark |
| **Alan Kay** | Smalltalk, Dynabook | "Black box criticism" that EvalCity directly addresses |
| **Seymour Papert** | Logo, Constructionism | Learning by building simulations |
| **Don Hopkins** | Micropolis, The Sims, MOOLLM | Synthesis of all above |

### AgentSheets and "SimCity in 10 Minutes"

#### The Question

In 1991, Alexander Repenning at University of Colorado asked:

> *"What kind of programming approaches should be added to computer media to support the creation of applications such as SimCity?"*

His benchmark was ambitious: **Can a child build SimCity in 10 minutes?**

Not play SimCity. Not modify SimCity. **Build** a working tile-based city simulation from scratch.

#### The AgentSheets Answer

AgentSheets introduced revolutionary concepts:

| Concept | How It Works | Why It Matters |
|---------|--------------|----------------|
| **Graphical Rewrite Rules** | Show a "before" state → show the "after" state → system learns the rule | No code. Just examples. |
| **Programming by Demonstration** | Drag a train on tracks. The system records: "when train is on track, move forward" | Actions become programs |
| **Visual AgenTalk** | IF-THEN rules with draggable conditions and actions | Visual, but Turing-complete |
| **Tactile Programming** | Programs are objects you can touch, test, drag, explore | Not just visual — interactive |
| **Agents on Sheets** | Sprites in a grid, like a spreadsheet of behaviors | SimCity's tile structure, made programmable |

#### How It Works

**Step 1: Create agents** (house, car, road, traffic light)

**Step 2: Define behaviors by example:**
```
BEFORE: 🚗 on 🛣️ facing →
AFTER:  🛣️ has 🚗 moved one tile →

BEFORE: 🚗 at 🚦 (red)
AFTER:  🚗 stays put

BEFORE: 🚦 (green) after 10 ticks
AFTER:  🚦 becomes (yellow)
```

**Step 3: Run.** The simulation executes all rules in parallel, every tick.

**Result:** A working traffic simulation in minutes, not months.

#### The Constructionist Philosophy

AgentSheets is rooted in Papert's constructionism:

> *"Students learn about a phenomenon and represent their knowledge in an animated graphical model, rather than simply watching or manipulating a representation provided for them."*
> — Ioannidou (2003)

The simulation is not consumed. It is **constructed**. The act of building IS the learning.

#### From AgentSheets to EvalCity

| AgentSheets (1991) | EvalCity (2026) |
|--------------------|-----------------|
| Graphical rewrite rules | YAML Jazz scats |
| Visual AgenTalk conditions | Emoji-anchored predicates |
| Agents on grid | Entities in rooms |
| Child as programmer | Player as evaluator |
| System learns from examples | LLM learns from play |
| Tile-based simulation | Metric-based simulation |
| "SimCity in 10 minutes" | "Your evaluation philosophy in 10 minutes" |

**The key insight transfers:**
- AgentSheets: The *rules* are defined by demonstration, not code
- EvalCity: The *metrics* are defined by play, not configuration

Both reject the black box. Both put authorship in the player's hands.

#### The LLM Upgrade

What AgentSheets did with graphical rewrite rules, EvalCity does with LLM coherence:

| AgentSheets | EvalCity |
|-------------|----------|
| Pattern match on pixel grids | Pattern match on semantic meaning |
| Rules fire when conditions match | LLM interprets when situations fit |
| Compile to Java applets | Emit YAML Jazz scats |
| Constrained to grid topology | Unconstrained semantic space |
| Learn tile behaviors | Learn evaluation philosophies |

**The 35-year arc:** AgentSheets → LLM = graphical rewrite rules upgraded to semantic understanding.

### Key References

- Repenning, A., Ioannidou, A., & Zola, J. (2000). *AgentSheets: End-User Programmable Simulations*. Journal of Artificial Societies and Social Simulation vol. 3, no. 3.
- Repenning, A. & Sumner, T. (1995). *Agentsheets: A Medium for Creating Domain-Oriented Visual Languages*. IEEE Computer 28(3).
- [AgentSheets.com](https://www.agentsheets.com) — The commercial product
- [AgentCubes](https://agentcubes.com) — 3D evolution (2006)
- [EduTechWiki: AgentSheets](https://edutechwiki.unige.ch/en/AgentSheets) — Educational context

---

*"EvalCity directly answers Alan Kay's criticism that SimCity is a black box with baked-in assumptions you can't see or change."*
