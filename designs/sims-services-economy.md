# Sims Services & Economy → MOOLLM Events

> *Money, Services, Bills, Disasters, and External Agents*
> *The world intrudes on the household*

## The Economic Model

The Sims had a complete economic simulation:

| System | Description |
|--------|-------------|
| **Money** | Household funds, spending, earning |
| **Depreciation** | Objects lose value over time |
| **Bills** | Regular expenses based on lot value |
| **Services** | NPCs that arrive (maid, gardener, repairman) |
| **Careers** | Work schedules, promotions, income |
| **Disasters** | Fire, theft, floods, sickness |

This created tension between *maintenance* and *aspiration*.

---

## Money in MOOLLM

**The Sims:** Numeric currency, tracked precisely.

```
Household Funds: $15,420
├── Income: $350/day (career)
├── Expenses: $200/3 days (bills)
└── Net: growing slowly
```

**MOOLLM:** Currency as narrative element:

```yaml
# characters/don-hopkins/economy.yml
funds:
  gold: 2500
  reputation: high
  debts: none
  
income_sources:
  - source: tips-from-pub-performances
    frequency: occasional
    amount: variable
    
expenses:
  - category: pub-tab
    frequency: ongoing
    amount: modest
    
economic_mood: comfortable
```

The LLM can reason about economic state:

> "Don's comfortable but not wealthy. He earns occasional tips from performances, enough to cover his modest pub tab with some left for adventures."

---

## Services: External Agents

The Sims spawned NPCs who arrived to provide services:

| Service | Trigger | Behavior |
|---------|---------|----------|
| **Maid** | Scheduled or called | Cleans house |
| **Gardener** | Scheduled | Tends plants |
| **Repairman** | Called when broken | Fixes objects |
| **Pizza Delivery** | Phone order | Delivers food |
| **Fireman** | Fire detected | Fights fire |
| **Burglar** | Night + unlocked | Steals objects |
| **Grim Reaper** | Death | Claims souls |

These NPCs arrived, performed tasks, and left.

**MOOLLM:** Service NPCs as skills:

```yaml
# skills/service-npc/CARD.yml
name: SERVICE-NPC
role: External agent that enters, acts, exits

methods:
  - ARRIVE
  - PERFORM-SERVICE
  - BILL-CUSTOMER
  - DEPART

templates:
  maid:
    arrives_when: scheduled or summoned
    performs: cleaning all dirty surfaces
    costs: 10 gold per visit
    
  delivery:
    arrives_when: order placed
    performs: delivers item
    costs: item price + tip
    
  emergency:
    arrives_when: crisis detected
    performs: crisis resolution
    costs: variable
```

---

## Disasters: Crisis Events

**The Sims Disasters:**

```
Fire:
├── Trigger: cooking failure, fireplace misuse
├── Spread: to adjacent flammable tiles
├── Resolution: sprinkler, firefighter, extinguish
└── Consequence: damage, death possible

Theft:
├── Trigger: night + unlocked doors
├── Agent: burglar NPC
├── Target: valuable objects
└── Resolution: alarm, police, fight

Flood:
├── Trigger: broken appliance
├── Spread: water across floor
├── Resolution: repair, mop
└── Consequence: mood penalty, object damage

Sickness:
├── Trigger: low hygiene, social exposure
├── Effect: mood penalty, reduced performance
└── Resolution: rest, medicine
```

**MOOLLM:** Disasters as events:

```yaml
# skills/disaster/CARD.yml (conceptual)
name: DISASTER
role: Crisis events that demand immediate response

event_types:
  fire:
    triggers:
      - cooking-failure
      - unattended-flame
    propagation: adjacent-flammable
    responses:
      - flee
      - fight-fire
      - call-help
    consequences:
      - property-damage
      - injury
      - death
      
  grue:
    triggers:
      - darkness
      - no-lamp-oil
    propagation: none (instant)
    responses:
      - flee-to-light
      - use-lamp
      - dog-scares-grue
    consequences:
      - eaten
      
  crisis-general:
    effect: |
      Disasters interrupt normal action queues.
      All characters must respond before
      resuming scheduled activities.
```

---

## Bills and Maintenance

**The Sims:**

```
Bills arrive every 3 days:
├── Based on: lot value + object value
├── Due: before next bill cycle
├── Failure: repo man takes objects
└── Strategy: balance upgrades vs. income
```

**MOOLLM:** Maintenance as obligation:

```yaml
# pub/ROOM.yml
maintenance:
  rent:
    amount: 100 gold
    frequency: weekly
    due: monday
    consequence_if_missed: |
      The landlord grows irritable.
      Continued default risks eviction.
      
  utilities:
    amount: 25 gold
    frequency: weekly
    includes: [lighting, heating, magical-wards]
    
  cleaning:
    method: marieke handles it
    cost: included in wages
    
  supplies:
    method: restock as needed
    cost: variable
```

---

## Depreciation

**The Sims:** Objects lost value over time.

```
New TV: $3500
After 1 year: $2800
After 2 years: $2100
...
Sell value always < buy value
```

**MOOLLM:** Wear and condition:

```yaml
# pub/bar/cocktail-shaker.yml
name: VINTAGE-COCKTAIL-SHAKER
acquired: founding-of-grotto
condition: well-worn
value:
  monetary: 50 gold
  sentimental: priceless
  
wear_pattern: |
  The shaker shows decades of use.
  Dents from countless celebrations.
  The silver is worn but polished.
  
# Depreciation is narrative, not numeric
```

---

## Careers and Work

**The Sims:**

```
Career Track: Culinary
Level 3: Sous Chef
├── Hours: 9am - 3pm
├── Pay: $150/day
├── Days: Mon-Fri
├── Requirements: 2 cooking, 1 charisma
├── Carpool: arrives 8am
└── Promotion: reach 4 cooking, 2 charisma
```

Characters left the lot for work, returning with money.

**MOOLLM:** Careers as background:

```yaml
# characters/marieke/career.yml
occupation: BUDTENDER
workplace: pub/bar/
schedule:
  days: [evening-shift]
  hours: flexible
  
duties:
  - tend-bar
  - recommend-strains
  - maintain-cat-cave
  - wisdom-dispensing
  
income:
  base: room-and-board
  tips: variable
  
advancement:
  path: none needed
  note: |
    Marieke has achieved her ideal position.
    She tends bar, loves her work, has cats.
```

---

## The Maid Pattern

One of the most common services — the maid:

**The Sims:**
1. Maid arrives at scheduled time (or when called)
2. Maid identifies all dirty objects
3. Maid routes to each, cleans
4. Maid bills household
5. Maid departs

**MOOLLM:** Service action pattern:

```yaml
# Narrative service visit

service_visit:
  service: cleaning
  provider: visiting-maid
  
  sequence:
    - arrival: |
        A knock at the pub door. Greta the cleaning gnome
        lets herself in with a ring of brass keys.
        
    - assessment: |
        She surveys the aftermath of last night's party
        with professional resignation. "The usual then."
        
    - work: |
        For the next hour, Greta is a whirlwind of
        efficiency — glasses collected, surfaces wiped,
        mysterious stains questioned but not judged.
        
    - completion: |
        "All done," she announces, dropping a small
        invoice on the bar. "Tell Marieke I said hello
        to the cats."
        
    - departure: |
        She lets herself out, keys jingling.
```

---

## The Grim Reaper Pattern

The ultimate service NPC:

**The Sims:**
1. Character dies (fire, drowning, etc.)
2. Grim Reaper materializes
3. Ghost of deceased can plead
4. Outcome: death confirmed or reprieve
5. Urn/gravestone appears

**MOOLLM:** Death as narrative event:

```yaml
# Handled by representation-ethics and character permanence

death_event:
  character: [whoever dies]
  
  protocol:
    - acknowledge: |
        Death in MOOLLM is significant.
        Characters don't casually die.
        
    - narrative: |
        The air grows cold. Maurice's fur stands on end.
        Something ancient enters the room.
        
    - resolution:
        options:
          - true-death: Character file archived
          - reprieve: Circumstances allow survival
          - ghost: Character becomes GHOST.yml
          
    - aftermath: |
        Other characters remember.
        The guest-book gains an entry.
        The world is changed.
```

---

## Economic Philosophy

Both systems share principles:

### Scarcity Creates Meaning

Resources are limited. Choices matter.

```yaml
# Not infinite wealth
# Choices have opportunity cost

decision:
  choice: Buy the fancy chandelier?
  cost: 500 gold
  benefit: +room_score, +prestige
  trade_off: Can't afford other upgrades
```

### Maintenance Creates Rhythm

Regular expenses create time pressure.

```yaml
# Bills arrive
# Rent is due
# Supplies need restocking

# This creates urgency and structure
```

### Services Create Stories

NPCs entering and leaving create narrative:

```yaml
# The maid who arrives every Tuesday
# The delivery person with gossip
# The mysterious repairman
# The burglar in the night

# External agents = story opportunities
```

---

## MOOLLM Enhancements

### Semantic Economy

```yaml
# Beyond numbers

economic_state:
  funds: "comfortable but not wealthy"
  debts: "a favor owed to the maze-keeper"
  reputation: "known as generous tipper"
  
# LLM understands implications
```

### Relationship-Based Services

```yaml
# Services affected by relationships

maid_relationship:
  with: greta-the-gnome
  history: 5 years service
  trust: high
  
  implications:
    - knows household secrets
    - gives benefit of doubt on messes
    - might warn of dangers
```

### Crisis Narration

```yaml
# Disasters become story beats

fire_narrative: |
  The grease pan catches.
  Flame licks toward the ceiling.
  
  Palm freezes for a moment — then
  his training kicks in. He grabs
  the extinguisher Maurice pointed
  out during orientation.
  
  Three seconds. Crisis averted.
  
  "This is why," Palm says, paws
  shaking slightly, "we always know
  where the extinguisher is."
```

---

## See Also

- [skills/economy/](../skills/economy/) — Economic simulation skill
- [skills/time/](../skills/time/) — Time and scheduling
- [sims-time-events.md](./sims-time-events.md) — Time and disasters
- [sims-social-system.md](./sims-social-system.md) — NPC interactions
- [representation-ethics](../skills/representation-ethics/) — Death handling

---

*"Money comes and goes. What matters is the story of how you spent it."*
