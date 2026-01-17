# Sims Edith Editor → MOOLLM

> *Live Debugging, Introspection, Modification*
> *The game is the development environment.*

## Edith: The Hidden Power

Edith was The Sims' internal development environment — accessible by pressing 'e' during gameplay. It let developers (and power users) inspect and modify the running simulation in real-time:

- Browse all objects
- Trace behavior trees
- Modify simulation constants
- Edit strings and resources
- Debug routing and animation

MOOLLM inherits this philosophy: **the world is always inspectable and editable**.

---

## The Exhaustive Scope

The original Edith documentation listed nearly everything that could be inspected and edited:

### Objects and Properties
- Object Properties, Relationship Matrix, Strings
- GUIDs, Object Categories, Object Placement Constraints
- Function Tables, Single/Multi-Tile Objects, Surfaces
- Standard Heights (Ground, LowTable, Table, Counter, Hand, Sitting, EndTable)

### People and Simulation
- Person Properties, Personality, Astrological Sign
- Motives and Mood, Skills, Relationships
- Happy Weights, Biographies, Action Queue
- Family History, Babies, Death, Ghosts

### SimAntics Virtual Machine
- Tree Code, Tree Tables, Primitives, Subroutines
- Return Values, Parameters, Comments
- Tree Properties, Tree Tracing, Tree Debugging, Tree Breakpoints

### Autonomy System
- Motive Satisfaction, Advertisements, False Advertising
- Happyscape, Happiness Contribution Curves
- Ad Attenuation, Exit Conditions, Food Chain
- Interaction Queue Priority, Interactions

### World Structure
- Rooms, Room Scoring, Levels (upstairs/downstairs)
- Portals (Doors, Windows, Stairs, Ladder, Diving Board)
- Terrain, Water, Pools, Lighting, Shadows
- Coordinate Systems, Draw Groups

### Animation and Visuals
- Object Animation, Character Animation
- Suits, Heads, Hands, Bodies, Accessories
- Thought Balloons, Action Icons, Conversation Icons
- Censorship, Invisibility

### Content and Resources
- Resource Files (Global, SemiGlobal, Object)
- String Tables (Careers, Build, Live, UIText, Credits)
- Catalog Entries, CST Files, Body Strings
- HIT Files (audio), Vocals, Sound Effects

### Gameplay Systems
- Careers, Work, School, Money, Depreciation
- Services, Bills, Disasters (Fire, Theft, Floods, Sickness)
- Friendship and Romance, Visitors, Neighbors
- Non-Player Characters, Stalker Cam

MOOLLM equivalents are distributed across:
- **YAML files** — all object/character properties
- **Skills** — all behavior definitions
- **Directories** — room and world structure
- **Session logs** — history and events

---

## Three Modes

The Sims had three distinct modes, each with different editing capabilities:

| Mode | Purpose | Edith Access |
|------|---------|--------------|
| **Live Mode** | Play the game | Full debugging |
| **Buy Mode** | Place/move objects | Object placement |
| **Build Mode** | Architecture | Wall/floor editing |

**MOOLLM:** All modes are always available:

```bash
# "Live mode" — run the game
# Just continue the session

# "Buy mode" — edit objects
vim pub/bar/new-lamp.yml

# "Build mode" — edit structure
mkdir pub/new-wing
```

No mode switching required. Text editing is always active.

---

## Object Browser

**Sims:** Browse all object classes:

```
Object Browser
├── Appliances
│   ├── Stove (GUID: 0x1234)
│   ├── Fridge (GUID: 0x1235)
│   └── ...
├── Seating
│   ├── Chair (GUID: 0x2345)
│   └── ...
└── ...
```

From here you could:
- View tree tables (behaviors)
- Edit function tables
- Modify object definitions
- Find related dialogs

**MOOLLM:** The filesystem IS the object browser:

```bash
ls skills/
# Lists all skill "classes"

ls examples/adventure-4/pub/
# Lists all objects in pub

cat pub/bar/bartender.yml
# Inspect object properties
```

No special tool needed — standard file operations.

---

## Object Inspector

**Sims:** Inspect any live object:

```
Object Inspector: Stove #47
  Position: (12, 8, 0)
  State: "cooking"
  Dirty: 35
  Broken: false
  Current Tree: "Make Meal"
  Stack:
    [0] Init (complete)
    [1] Main (running)
    [2] Make Meal (current)
```

**MOOLLM:** YAML files ARE the inspector:

```yaml
# Just read the file
cat pub/kitchen/stove.yml

# Contents show current state
state: idle
last_used: 2026-01-08
cleanliness: 65
last_cooked: breakfast_scramble
```

And the LLM can explain state:

> "The stove was last used this morning for breakfast. It needs cleaning — cleanliness is at 65%."

---

## Tree Editor

**Sims:** Visual behavior editor:

```
Tree: "Make Meal"
├─ [0] Test: has_ingredients?
│   ├─ TRUE → Continue
│   └─ FALSE → Exit (false)
├─ [1] Animate: "open_fridge"
├─ [2] Subroutine: "Get Ingredients"
├─ [3] Route to stove
├─ [4] Animate: "cook"
└─ [5] Create: "meal_object"
```

You could:
- Add/remove nodes
- Change parameters
- Set breakpoints
- Copy trees between objects

**MOOLLM:** Skills as editable prose:

```markdown
## skills/cooking/SKILL.md

### MAKE-MEAL

When a character prepares a meal:

1. **Check ingredients** — Verify fridge has what's needed
2. **Gather** — Collect ingredients from storage
3. **Prepare** — Use appropriate cooking surface
4. **Create meal** — Produce food object
5. **Serve** — Place meal appropriately

### Failure Modes

- No ingredients → suggest shopping
- No skill → risk of fire
- Interrupted → partial completion
```

Edit the prose, change the behavior.

---

## Tree Tracer

**Sims:** Watch execution in real-time:

```
TRACE: Sim#12 running "Use Toilet"
  [0] Enter tree
  [1] Test: bladder < 50? → TRUE
  [2] Route to (8, 4) → SUCCESS
  [3] Animate: "approach" → PLAYING
  [4] Test: occupied? → FALSE
  [5] Animate: "sit" → PLAYING
  ...
```

Invaluable for debugging behavior.

**MOOLLM:** The [return-stack](../skills/return-stack/) skill:

```yaml
# After action execution
execution_trace:
  - step: check_need
    condition: bladder_critical
    result: true
    
  - step: navigate
    target: bathroom
    result: arrived
    
  - step: interact
    object: toilet
    result: success
    
  - step: update_state
    changes:
      bladder: 0 → 100
```

Or ask the LLM: "Why did Palm go to the bathroom?"

> "Palm's bladder need was critical (15%), so he navigated to the nearest bathroom and used the facilities. His bladder need is now satisfied (100%)."

---

## Simulation Constants

**Sims:** Tunable parameters:

```
Edit Simulation Constants

Motive Decay:
  hunger_decay: 2.0 per hour
  energy_decay: 1.5 per hour
  social_decay: 1.0 per hour
  
Autonomy:
  think_frequency: 100 ticks
  best_action_weight: 0.8
  
Room Score:
  light_bonus: 10
  art_bonus: 5
  dirty_penalty: -10
```

Change these → change game feel.

**MOOLLM:** Constants in YAML:

```yaml
# kernel/constitution-core.md defines core behavior

# skills/needs/SKILL.md defines decay patterns:
decay_rates:
  hunger: moderate
  energy: slow
  social: gradual
  
# Tunable through editing the skills
```

---

## Simulation Globals

**Sims:** Global state:

```
Simulation Globals
  current_tick: 1847362
  time_of_day: 14:30
  day_of_week: Tuesday
  weather: sunny
  money: $15,420
  lot_value: $45,000
```

**MOOLLM:** Global state in top-level YAML:

```yaml
# working-set.yml
session:
  current_turn: 45
  
# adventure-4/state.yml (conceptual)
world:
  time: evening
  weather: clear
  mood: convivial
```

---

## String Editor

**Sims:** Edit all text:

```
Strings Editor: UIText

ID    | String
------|-----------------------
1     | "OK"
2     | "Cancel"
3     | "Are you sure?"
4     | "Sim is hungry"
...
```

Enabled localization and quick text changes.

**MOOLLM:** Text is just... text:

```yaml
# Edit any YAML or markdown file
# All text is editable, no special tool

# pub/menus/drinks.yml
drinks:
  house_special:
    name: "Grotto Glow"  # Edit this text directly
    description: "A mysterious amber blend"
```

---

## Resource Editor

**Sims:** Low-level resource browser:

```
Resource Editor
├── BHAV (Behavior)
├── GLOB (Global)
├── OBJD (Object Definition)
├── STR# (String Table)
├── SPR2 (Sprites)
└── ...
```

Could hex-edit raw resources.

**MOOLLM:** Files are the resources:

```bash
# All resources are human-readable
cat skills/bartender/CARD.yml     # "Object definition"
cat skills/bartender/SKILL.md     # "Behavior"
cat pub/menus/drinks.yml          # "Data"

# No hex editing needed — it's all text
```

---

## Neighborhood Editor

**Sims:** Manage families and lots:

```
Neighborhood Editor
├── Lots
│   ├── Newbie House (occupied)
│   ├── Empty Lot 2
│   └── ...
├── Families
│   ├── Newbie (Bob, Betty)
│   ├── Goth (Mortimer, Bella, Cassandra)
│   └── ...
└── Relationships
    └── [matrix view]
```

**MOOLLM:** Directory structure:

```
examples/adventure-4/
├── characters/          # "Families"
│   ├── don-hopkins/
│   ├── palm/
│   └── ...
├── pub/                 # "Lots"
│   ├── bar/
│   ├── stage/
│   └── ...
└── maze/                # Another "lot"
```

---

## Live Modification

**Sims key feature:** Changes took effect immediately.

Edit a behavior tree → Sims use new behavior.
Change a constant → Simulation feels different.
Modify an object → All instances update.

**MOOLLM:** Same philosophy:

```bash
# Edit a skill
vim skills/bartender/SKILL.md

# Next LLM interaction uses new skill

# Edit character state
vim characters/palm/needs.yml

# Next turn reflects new state
```

Changes are immediate because the LLM reads files fresh.

---

## Breakpoints

**Sims:** Stop execution at specific points:

```
Set Breakpoint: "Make Meal" line 12

[Breakpoint hit]
> Inspect: cooking_skill = 3
> Inspect: ingredients = [egg, cheese]
> Step
> Continue
```

**MOOLLM:** "Breakpoints" are natural:

```markdown
# In session with LLM:

"Stop here. Before Palm enters the kitchen, 
what's his current state?"

# LLM reports state, waits for continue

"OK, continue."
```

Conversational debugging instead of formal breakpoints.

---

## Save Behaviors As Text

**Sims:** Export all trees as readable text:

```
File → Save All Behaviors As Text

Output:
Tree "Make Meal" (Object: Stove)
  [0] Expression: temp0 = stack.has_ingredients
  [1] If temp0 == FALSE, return FALSE
  [2] Animate: person, "open_fridge"
  ...
```

Useful for:
- Documentation
- Version control
- Sharing

**MOOLLM:** Skills ARE text:

```markdown
# No export needed — skills are already Markdown

# skills/cooking/SKILL.md is the canonical form
# Readable, editable, versionable
```

---

## Animation Browser

**Sims:** Inspect character animations:

```
Animation Browser
├── Walk Cycles
│   ├── a2o-walk-normal
│   ├── a2o-walk-tired
│   └── ...
├── Interactions
│   ├── a2o-sit-chair
│   ├── a2o-use-toilet
│   └── ...
└── Emotions
    ├── a2o-cry
    ├── a2o-laugh
    └── ...
```

Could preview, mix, and debug animations.

**MOOLLM:** Actions as narrative:

```yaml
# No animation files — actions described in prose

# When character sits:
"Palm settles into the worn leather chair, 
adjusting until he finds the familiar groove."

# Animation IS description
```

---

## Profile Tools

**Sims:** Performance profiling:

```
Object Profile:
  Stove: 2.3ms average
  Toilet: 1.1ms average
  Phone: 0.8ms average
  
Sim Profile:
  Think loop: 12ms
  Route calc: 8ms
  Animation: 15ms
```

**MOOLLM:** Performance is LLM tokens:

```yaml
# working-set.yml tracks context
vm:
  context_used: 45000 tokens
  context_limit: 128000 tokens
  
# Optimization = reducing token usage
# Skills designed for concise representation
```

---

## Picture-in-Picture & Scrapbook

**Sims:** Visual snapshot tools:

```
Picture in Picture:
  View: [Another lot/room preview]
  
Scrapbook:
  [Screenshot 1] [Screenshot 2] [Screenshot 3]
  Family history captures...
```

Enabled visual documentation of gameplay moments.

**MOOLLM:** Session logs as scrapbook:

```markdown
# Session logs capture moments in prose

## Turn 15: The Party

Palm climbed onto the pie table and began an impassioned 
speech about bananas while Maurice yowled accompaniment...

[Session continues as living documentation]
```

Text captures more than screenshots — it captures meaning.

---

## Routing and Slots

**Sims:** Navigation system:

```
Routing Slots: Where Sims can stand/sit
├── Object slots (chair positions, counters)
├── Door slots (approach, pass through)
└── Routing logging (debug pathfinding)

Routing Logging:
  [ROUTE] Sim#12 finding path to Fridge
  [ROUTE] Blocked by Chair at (4,5)
  [ROUTE] Alternative: go around table
  [ROUTE] Path found: 12 tiles
```

**MOOLLM:** Routing through exits:

```yaml
# ROOM.yml
exits:
  kitchen:
    target: ../kitchen/
    description: "Through the swinging doors"
  upstairs:
    target: ./second-floor/
    description: "Up the creaky stairs"
    requirements:
      - light  # Can't navigate in darkness
```

LLM narrates the journey:
> "Palm navigated past the crowded bar, pushed through the swinging doors, and found himself in the steamy kitchen."

---

## The Development Philosophy

Edith embodied a philosophy:

> **The running game IS the development environment.**

You didn't quit to a separate tool. You developed while playing. Changes were immediate. Debugging was contextual.

MOOLLM inherits this completely:

1. **Files are the game state** — edit them directly
2. **LLM understands changes** — no compilation
3. **Session is continuous** — modify as you play
4. **Debugging is conversation** — ask the LLM why

---

## Cheat Codes

**Sims:** Keyboard cheats:

| Cheat | Effect |
|-------|--------|
| `rosebud` | +$1000 |
| `move_objects on` | Move anything |
| `autonomy off` | Full control |
| `aging off` | Stop time |

**MOOLLM:** "Cheats" are just edits:

```yaml
# Want more gold?
# Just edit the character file

# characters/don-hopkins/inventory.yml
gold: 999999  # Cheat!

# Want full control?
# Edit autonomy setting

# characters/palm/CHARACTER.yml
autonomy: player_controlled  # Full control
```

---

## Edith Menu Structure

The full Edith system had extensive menus:

### File Menu
- **Save All Behaviors** — Export trees as text (MOOLLM: skills already are text)
- **Suspend Files** — Hot-swap files without restart (MOOLLM: instant file changes)

### Window Menu  
- **Object Browser** — Browse all object classes
- **Tree Search** — Find trees by string
- **Function Search** — Find objects with specific functions

### Sims Menu
- **Object Inspector** — View live object state
- **Simulation Globals** — World-level variables
- **Simulation Constants** — Tunable parameters (Motive, Autonomy, Room Score, Neighborhood)

### Edit Constants Submenus
- **Motive Sim** — Decay rates, satisfaction curves
- **Autonomy** — Think frequency, action weights
- **Room Score** — Light, art, cleanliness bonuses
- **Neighborhood** — Family relationships, lot values

This structure maps directly to MOOLLM:

| Edith Feature | MOOLLM Equivalent |
|---------------|-------------------|
| File → Save All Behaviors | `skills/` directory (already text) |
| Window → Object Browser | `ls` any directory |
| Window → Tree Search | `grep` across skills |
| Sims → Object Inspector | `cat` any YAML file |
| Sims → Simulation Globals | `working-set.yml` |
| Edit Constants | Skill parameter editing |

---

## Special Features

**Suspend Files Dialog:** Install new versions of files while the game runs. MOOLLM inherits this — edit a skill file, and the next LLM call uses the new version.

**Room Map Dialog:** Flat map of room layout. MOOLLM equivalent: the directory structure itself, viewable with `tree` or `ls -R`.

**Animation Inspector:** Journal and playback animations. MOOLLM equivalent: session logs that capture the "animation" of narrative.

---

## Dialog Navigation Graph

Edith's dialogs formed an interconnected graph — a navigation system for development tools:

```
"Edith" Dialog (entry: press 'e')
│
├──► "Animation Browser" ─► [complex animation debugging]
├──► "Find Objects" ─► [function search results]
├──► "Neighborhood" ─► [family/lot editing]
├──► "Object Browser" ─┬► "Edit Behavior File" ─► "Tree Editor"
│                      ├► "Edit Tree Table"
│                      ├► "Edit Object Definition"
│                      ├► "Edit Function Table"
│                      └► "Find Object Dialogs"
├──► "Object Inspector" ─► [live object state]
├──► "Resource Editor" ─┬► "Hex Resource Editor"
│                       └► "String Resource Editor"
├──► "Room Map" ─► [flat room layout]
├──► "Save Behaviors As Text" ─► [export all trees]
├──► "Simulation Constants" ─► [tunable parameters]
├──► "Simulation Globals" ─► [world state]
├──► "Strings" ─► [text editing]
└──► "Terrain Tweak" ─► [grass/color params]
```

**MOOLLM:** The filesystem IS the navigation graph:

```
moollm/ (entry: cd moollm)
│
├──► skills/ ──────────► [all skill definitions]
│    └──► bartender/ ──► CARD.yml, SKILL.md, README.md
│
├──► examples/ ────────► [all game content]
│    └──► adventure-4/ ► pub/, characters/, sessions/
│
├──► kernel/ ──────────► [core configuration]
│    └──► constitution-core.md
│
├──► designs/ ─────────► [documentation]
│    └──► MOOLLM-EVAL-INCARNATE-FRAMEWORK.md
│
└──► working-set.yml ──► [global state]
```

Navigation is `cd`. Inspection is `cat`. Editing is `vim`.

---

## Portals in Edith

The documentation listed these portal types:
- **Doors** — passage between rooms
- **Windows** — view without passage
- **Stairs** — level transitions
- **Ladder** — pool exit
- **Diving Board** — pool entry

**MOOLLM:** Portals are directory structure:

```yaml
# examples/adventure-4/pub/ROOM.yml
exits:
  # Door
  street:
    target: ../street/
    type: door
    
  # Stairs
  basement:
    target: ./cellar/
    type: stairs
    
  # Window (view only)
  garden_view:
    target: ../garden/
    type: window
    can_pass: false
    can_see: true
```

---

## See Also

- [MOOLLM-EVAL-INCARNATE-FRAMEWORK.md](./MOOLLM-EVAL-INCARNATE-FRAMEWORK.md) — The architecture
- [sims-pie-menus.md](./sims-pie-menus.md) — Pie menus (Edith uses them too)
- [don-hopkins-projects.md](./don-hopkins-projects.md) — PSIBER (visual debugger lineage)
- [skills/return-stack/](../skills/return-stack/) — Execution tracing
- [working-set.yml](../working-set.yml) — Context management
- [kernel/](../kernel/) — Core configuration
- [sims-simantics-vm.md](./sims-simantics-vm.md) — The behaviors being debugged

---

*"Edith User Interface Roadmap... Object Browser Object Inspector Tree Editor Tree Tracer Simulation Constants"*

When the world is text, the world is inspectable.
