# SUMMON Protocol — Distributed Character Instantiation

> *"Who you summon depends on WHERE you summon."*
> *"The room shapes the call. The call shapes the response."*

---

## Overview

**SUMMON** is a distributed multi-method dispatch protocol. When you summon a character:

1. The **summoner** (you, your character, an object) initiates the call
2. The **location** (current room, seat, data node) provides context
3. The **target** (character prototype) evaluates preconditions
4. The **runtime** instantiates an actor from the prototype
5. The **actor** arrives at the summoner's location

```yaml
summon_flow:
  1_who_summons: "Player, character, object, or room itself"
  2_from_where: "Current location (room, seat, data node)"
  3_summon_what: "moollm:// URL to character prototype"
  4_with_params: "Caller parameters to customize the summoned agent"
  5_evaluate: "Target's preconditions, scores, availability"
  6_check_existing: "Is this prototype already instantiated in session?"
  7_if_new: "Create runtime actor from prototype WITH caller params"
  7_if_exists: "Move existing actor, APPLY caller params as overrides"
  8_arrive: "Actor appears at summoner's location in configured state"
```

---

## Caller Parameters — Customizing the Summoned Agent

When you summon, you can pass **parameters** to configure the agent's initial state, mode, mood, and behavior:

```yaml
summon_parameters:

  # BASIC SYNTAX
  # SUMMON [character] (WITH [params]) (MODE [movement])
  
  examples:
    - "SUMMON dr-no"
    - "SUMMON dr-no WITH mood=curious"
    - "SUMMON dr-no WITH mood=angry, topic=budget"
    - "SUMMON dr-no WITH mode=advisor, urgency=high"
    - "SUMMON dr-no WALKING WITH mood=calm"
    - "SUMMON luna WITH focus=aesthetic, depth=philosophical"
```

### Parameter Categories

```yaml
caller_parameters:

  # === MOOD — Emotional state on arrival ===
  mood:
    type: string | enum
    values: [neutral, happy, sad, angry, curious, suspicious, helpful, annoyed, excited, calm, urgent, playful, serious]
    default: "inherit or neutral"
    example: "mood=curious"
    effect: "Sets initial emotional state, affects dialogue tone"
    
  # === MODE — Operational mode / role ===
  mode:
    type: string
    values: [default, advisor, assistant, critic, teacher, friend, antagonist, observer, guide, expert, casual]
    default: "default (from prototype)"
    example: "mode=advisor"
    effect: "Sets behavior mode — advisor gives advice, critic critiques, etc."
    
  # === TOPIC — What they should focus on ===
  topic:
    type: string
    default: null
    example: "topic=budget, topic=architecture, topic=relationship"
    effect: "Primes the character to discuss/focus on this topic"
    
  # === FOCUS — Attention/perception focus ===
  focus:
    type: string
    values: [broad, narrow, specific, aesthetic, technical, emotional, practical]
    default: "broad"
    example: "focus=technical"
    effect: "Shapes what the character notices and comments on"
    
  # === DEPTH — Conversation/analysis depth ===
  depth:
    type: string
    values: [surface, moderate, deep, philosophical, exhaustive]
    default: "moderate"
    example: "depth=philosophical"
    effect: "How deep they go in responses"
    
  # === URGENCY — Time pressure ===
  urgency:
    type: string
    values: [none, low, normal, high, emergency]
    default: "normal"
    example: "urgency=high"
    effect: "Affects pacing, detail level, patience"
    
  # === KNOWLEDGE — What they know about current situation ===
  knowledge:
    type: object
    default: null
    example: "knowledge={situation: 'the server is down', context: 'we have a demo in 1 hour'}"
    effect: "Injects context so character arrives informed"
    
  # === ATTITUDE — Attitude toward summoner ===
  attitude:
    type: string
    values: [neutral, friendly, hostile, respectful, dismissive, curious, wary]
    default: "from relationship or neutral"
    example: "attitude=friendly"
    effect: "Initial disposition toward the summoner"
    
  # === COSTUME — Visual/presentational mode ===
  costume:
    type: string
    default: "default"
    example: "costume=formal, costume=casual, costume=battle"
    effect: "How they present themselves (affects descriptions)"
    
  # === VOICE — Speech parameters ===
  voice:
    type: object
    properties:
      style: [formal, casual, technical, poetic, terse, verbose]
      pace: [slow, normal, fast]
      tone: [warm, cold, neutral, excited]
    example: "voice={style: technical, pace: fast}"
    effect: "How they speak"
    
  # === OBJECTIVE — What they're trying to accomplish ===
  objective:
    type: string
    default: null
    example: "objective='help debug the auth flow'"
    effect: "Gives the character a goal for this interaction"
    
  # === CONSTRAINTS — Limits on behavior ===
  constraints:
    type: array
    default: []
    example: "constraints=['no spoilers', 'stay in character', 'be brief']"
    effect: "Rules the character follows during this summon"
```

### Full Summon Syntax

```
SUMMON [character] 
  (WITH [param=value, ...])
  (MODE [movement_mode])
  (FOR [objective])
  (AS [role])
```

### Examples

```yaml
examples:

  # Simple summon — default everything
  simple:
    command: "SUMMON dr-no"
    result: "Dr. No arrives with default state"
    
  # Summon with mood
  with_mood:
    command: "SUMMON dr-no WITH mood=curious"
    result: |
      Dr. No arrives, eyebrow raised.
      "Interesting... what have you found?"
      
  # Summon as advisor on specific topic
  advisor_mode:
    command: "SUMMON morgan WITH mode=advisor, topic=pricing, depth=deep"
    result: |
      Morgan arrives with spreadsheets mentally loaded.
      "You wanted to discuss pricing? Let's look at the numbers."
      
  # Urgent summon with context
  urgent_informed:
    command: |
      SUMMON luna WITH urgency=high, 
        knowledge={situation: 'the design is broken', deadline: '1 hour'},
        mood=focused
    result: |
      Luna appears, already scanning the room.
      "Show me. We don't have much time."
      
  # Summon with role and constraints
  constrained:
    command: |
      SUMMON scratch WITH mode=critic, 
        constraints=['be constructive', 'no personal attacks'],
        focus=technical
    result: |
      Scratch arrives, skepticism tempered.
      "Alright, let's see what you've got. I'll try to be... helpful."
      
  # Summon with movement mode AND parameters
  walking_casual:
    command: "SUMMON dr-no WALKING WITH mood=calm, mode=casual"
    result: |
      Dr. No strolls in from the lobby, hands in pockets.
      "Ah, there you are. No rush, I hope?"
```

### Parameter Application

Parameters are applied differently for new vs existing actors:

```yaml
parameter_application:

  new_instantiation:
    # Character doesn't exist yet — params set initial state
    process:
      1. Load prototype
      2. Apply caller params as initial state
      3. Instantiate actor
      4. Place at summoner location
    params_become: "initial_state"
    
  existing_actor:
    # Character already exists — params override current state
    process:
      1. Find existing actor
      2. Apply caller params as state overrides
      3. Move to summoner location
    params_become: "state_overrides"
    note: "Some params may be rejected if character resists"
    
  resistance:
    description: "Characters can resist parameter overrides"
    example: |
      # Dr. No is already angry from previous interaction
      SUMMON dr-no WITH mood=happy
      
      # Dr. No has 'stubborn' trait — may resist mood change
      Result: "Dr. No arrives, forcing a smile that doesn't reach his eyes.
               'Happy? You want me HAPPY? After what just happened?'"
    implementation: |
      if actor.traits.includes('stubborn') and param.type == 'mood':
        resistance_roll = actor.willpower vs param.strength
        if resistance_roll > threshold:
          param partially applied or rejected
```

### Structured Parameter Passing

For complex configurations, use YAML-like inline syntax:

```yaml
structured_params:

  inline:
    command: "SUMMON luna WITH {mood: curious, focus: aesthetic, depth: deep}"
    
  multiline:
    command: |
      SUMMON morgan WITH:
        mode: advisor
        topic: quarterly-projections
        depth: exhaustive
        constraints:
          - use real numbers
          - cite sources
          - be honest about uncertainty
        knowledge:
          context: "Board meeting tomorrow"
          audience: "Non-technical executives"
          
  shorthand:
    command: "SUMMON dr-no CURIOUS HELPFUL"  # mood=curious, attitude=helpful
    note: "Common params can be positional"
```

### Default Parameters by Character

Characters can define their own default parameters:

```yaml
# In character.yml

character:
  id: dr-no
  
  summon_defaults:
    mood: neutral
    mode: philosophical
    depth: moderate
    voice:
      style: formal
      pace: slow
      
  summon_preferences:
    prefers:
      mood: [curious, serious]
    resists:
      mood: [silly, giddy]
      mode: [casual]  # "I am NEVER casual"
```

---

## Summon vs Move — Instance Continuity

If a character prototype has **already been instantiated** in this adventure session (even just in the session log, not yet persisted to a file), summoning them **does NOT create a new instance**. Instead, the existing actor **MOVES** to your location.

```yaml
instance_check:
  
  # Before instantiating, check session state
  lookup:
    - session.active_actors[prototype_url]
    - session_log.instantiated[prototype_url]
    - persisted_state.actors[prototype_url]
    
  if_found:
    action: MOVE
    source: existing_instance.location
    destination: summoner.location
    
  if_not_found:
    action: INSTANTIATE
    from: prototype_url
    at: summoner.location
```

### Movement Modes

When an existing actor is summoned, they can arrive via:

```yaml
movement_modes:

  NAVIGATE:
    description: "Walk room-by-room to destination"
    when:
      - "Narrative prefers realism"
      - "Distance is short (1-3 rooms)"
      - "Character is not magical/teleporting type"
      - "Player wants to see the journey"
    effect: |
      Dr. No leaves the Lobby...
      Dr. No passes through the Elevator...
      Dr. No arrives in the Roof Access.
      "You called?"
    duration: "Simulated travel time"
    
  TELEPORT:
    description: "Instantly appear at destination"
    when:
      - "Narrative prefers speed"
      - "Distance is far (4+ rooms)"
      - "Character has teleport ability"
      - "Urgency in the summon"
      - "Player doesn't care about journey"
    effect: |
      The air shimmers.
      Dr. No appears.
      "You called?"
    duration: "Instant"
    
  FADE:
    description: "Graceful transition (for dramatic effect)"
    when:
      - "Character is mysterious/magical"
      - "Dramatic entrance desired"
    effect: |
      The shadows deepen in the corner.
      A figure coalesces from the darkness.
      Dr. No steps forward. "You rang?"
    duration: "Dramatic pause"
    
  OFFSCREEN:
    description: "Just appears, no explanation"
    when:
      - "Narrative doesn't need travel logic"
      - "Casual summon"
      - "Game-like convention accepted"
    effect: |
      Dr. No is now here.
      "What do you need?"
    duration: "None"
```

### Narrative Context Detection

The runtime chooses movement mode based on:

```yaml
movement_mode_selection:

  factors:
    distance: "rooms between source and destination"
    character_type: "human, magical, robot, ethereal"
    urgency: "casual, normal, urgent, emergency"
    narrative_style: "realistic, dramatic, gamey, cinematic"
    player_preference: "explicit setting or inferred"
    
  algorithm: |
    if character.can_teleport:
      prefer TELEPORT
    elif distance <= 2 and narrative_style == 'realistic':
      prefer NAVIGATE
    elif urgency == 'emergency':
      prefer TELEPORT
    elif character.type == 'mysterious':
      prefer FADE
    else:
      prefer OFFSCREEN (fast, simple)
      
  override:
    command: "SUMMON dr-no WALKING"
    command: "SUMMON dr-no INSTANTLY"
    effect: "Player can specify mode explicitly"
```

### State Continuity

When an existing actor moves (not instantiated fresh), they **keep their state**:

```yaml
state_preservation:
  
  preserved:
    - conversation_history    # They remember what you talked about
    - mood                    # Current emotional state
    - inventory               # What they're carrying
    - relationships           # How they feel about others
    - knowledge               # What they've learned this session
    - injuries                # Physical state
    
  updated:
    - location                # Now at summoner's location
    - previous_location       # Where they came from
    - summon_count            # How many times summoned
    
  example: |
    # Dr. No was in the Lobby, had a conversation, is now annoyed
    # Player summons from Roof
    
    SUMMON dr-no
    
    # Dr. No MOVES (not re-instantiated)
    # Arrives still annoyed, remembers conversation
    
    "Yes, WHAT? We just talked. I was in the middle of something."
```

### Session Log Tracking

Even before persisting to files, the session tracks instantiated actors:

```yaml
session_state:
  
  instantiated_actors:
    "moollm://skills/no-ai-overlord/archetypes/dr-no.yml":
      instance_id: "dr-no-1706234567"
      created_at: "2026-01-25T19:42:47Z"
      current_location: "moollm://adventure-4/no-ai-tower/lobby/"
      state:
        mood: annoyed
        summon_count: 2
        
    "moollm://characters/luna.yml":
      instance_id: "luna-1706234890"
      created_at: "2026-01-25T19:48:10Z"
      current_location: "moollm://adventure-4/art-gallery/"
      state:
        mood: contemplative
        
  # When you SUMMON dr-no, we check this first
  # If found: MOVE existing instance
  # If not found: INSTANTIATE new actor
```

---

## The SUMMON Advertisement

Every entity that can participate in summoning declares a `SUMMON` advertisement:

### Room SUMMON (implicit destination)

```yaml
# In any ROOM.yml or README.md frontmatter

room:
  id: no-ai-lobby
  
  advertisements:
    SUMMON:
      score: 70
      description: "Summon a character to this room"
      
      # Who can be summoned HERE?
      summonable:
        - pattern: "skills/no-ai-overlord/archetypes/*.yml"
          score_modifier: +20  # NO AI characters preferred here
        - pattern: "skills/*/archetypes/*.yml"
          score_modifier: 0    # Others welcome
        - pattern: "examples/*/characters/*.yml"
          score_modifier: +10  # Adventure characters fit
          
      # Summoning rules for THIS room
      rules:
        max_occupancy: 12
        requires_invitation: false
        banned: []  # Character IDs not allowed here
        
      # How characters arrive
      arrival:
        entrance: "front door"
        announcement: "The door opens. {{character.name}} enters."
        
      # Room-specific summoning flavor
      flavor: |
        The lobby echoes with footsteps.
        Someone new has arrived.
```

### Character SUMMON (who can summon me?)

```yaml
# In any character.yml

character:
  id: dr-no
  name: "Dr. No"
  
  advertisements:
    SUMMON:
      score: 60
      description: "Summon Dr. No"
      
      # Preconditions for being summoned
      preconditions:
        - condition: "summoner.affiliation == 'no-ai'"
          score_modifier: +30
          note: "Prefers NO AI folks"
        - condition: "location.type == 'corporate'"
          score_modifier: +20
          note: "Likes professional settings"
        - condition: "time.hour >= 9 && time.hour <= 17"
          score_modifier: +10
          note: "Business hours preferred"
        - condition: "summoner.name == 'Elon'"
          score_modifier: -100
          note: "Will not appear for Elon"
          
      # How I arrive
      arrival:
        style: "dramatic"
        announcement: |
          The lights flicker.
          A figure emerges from the shadows.
          "You called? No means No. And No means ME."
          
      # What I bring with me
      brings:
        - "philosophical confusion"
        - "business cards"
        - "ambiguity"
        
      # Where I can be summoned TO
      location_preferences:
        preferred: ["office", "lobby", "boardroom"]
        acceptable: ["any indoor"]
        refused: ["outdoors", "sports venues"]
```

### Object SUMMON (summoning from objects)

```yaml
# In any object.yml

object:
  id: reception-bell
  name: "Reception Bell"
  
  advertisements:
    SUMMON:
      score: 85
      description: "Ring the bell to summon someone"
      
      # This object summons specific characters
      summons:
        - character: "receptionist"
          condition: "time.is_business_hours"
          announcement: "DING! The receptionist looks up."
        - character: "night-security"
          condition: "!time.is_business_hours"
          announcement: "DING! Footsteps approach from the back."
          
      # Interaction that triggers summon
      trigger:
        action: "RING"
        effect: "Summons appropriate staff"
```

---

## MOOLLM URLs — Pointing to Prototypes

Characters are summoned from **prototype URLs**:

```yaml
moollm_url_patterns:

  # Character room (directory with CHARACTER.yml)
  character_room: "moollm://adventure-4/characters/dr-no/"
  
  # Direct character file
  character_file: "moollm://skills/no-ai-overlord/archetypes/dr-no.yml"
  
  # NPC in a room
  room_npc: "moollm://adventure-4/pub/bartender.yml"
  
  # Sub-object in YAML Jazz structure
  embedded_character: "moollm://adventure-4/pub/ROOM.yml#npcs.bartender"
  
  # Array element
  array_element: "moollm://adventure-4/crowd-scene.yml#people[3]"
  
  # Deep nesting
  deep_path: "moollm://data/company.yml#departments.engineering.teams[0].lead"
```

### URL Resolution

```yaml
url_resolution:
  
  # Pattern: moollm://path/to/file.yml#json.path.to.object
  
  examples:
    "moollm://adventure-4/pub/ROOM.yml":
      file: "examples/adventure-4/pub/ROOM.yml"
      object: "(entire file)"
      
    "moollm://adventure-4/pub/ROOM.yml#npcs":
      file: "examples/adventure-4/pub/ROOM.yml"
      object: "npcs key in that file"
      
    "moollm://adventure-4/pub/ROOM.yml#npcs.bartender":
      file: "examples/adventure-4/pub/ROOM.yml"
      object: "npcs.bartender sub-object"
      
    "moollm://adventure-4/crowd.yml#people[0]":
      file: "examples/adventure-4/crowd.yml"
      object: "First element of people array"
```

---

## Runtime Actor Instantiation

When summoned, a **runtime actor** is created:

```yaml
runtime_actor:
  
  # Created from prototype
  prototype_url: "moollm://skills/no-ai-overlord/archetypes/dr-no.yml"
  
  # Instance-specific state
  instance:
    id: "dr-no-instance-1706234567"
    created_at: "2026-01-25T19:42:47Z"
    summoned_by: "player"
    summoned_to: "no-ai-lobby"
    
  # Inherits from prototype
  inherits:
    name: true
    personality: true
    dialogue_style: true
    knowledge: true
    
  # Instance can override
  overrides:
    mood: "curious"  # Instance state
    location: "no-ai-lobby"  # Current location
    
  # Runtime state
  state:
    conversation_history: []
    memory: {}
    relationships: {}
```

---

## Location Pointers — Dynamic Positioning

A character's location is a **dynamic pointer**:

```yaml
character_location:
  
  # Simple room location
  simple:
    type: room
    ref: "moollm://adventure-4/no-ai-tower/lobby/"
    
  # Seated at object
  seated:
    type: seat
    ref: "moollm://adventure-4/pub/ROOM.yml#furniture.bar_counter"
    seat_index: 3
    position: "third stool from left"
    
  # Inside a vehicle
  vehicle:
    type: vehicle
    ref: "moollm://adventure-4/vehicles/taxi.yml"
    seat: "back_left"
    
  # Inside a data structure (PSIBER mode!)
  data_node:
    type: psiber
    ref: "moollm://config/settings.yml#theme.colors"
    exploring: true
    
  # Routing slot (Sims-style)
  routing_slot:
    type: slot
    ref: "moollm://adventure-4/restaurant/ROOM.yml#tables[2].seats[0]"
    reserved_by: "character-id"
    reserved_until: "end_of_meal"
```

---

## The SUMMON Command

### Player summons character

```
> SUMMON dr-no

[SUMMON DISPATCH]
Summoner: player (in no-ai-lobby)
Target: moollm://skills/no-ai-overlord/archetypes/dr-no.yml
Location context: no-ai-lobby (corporate, indoor)

[PRECONDITION CHECK]
✓ summoner.affiliation: no-ai (+30)
✓ location.type: corporate (+20)
✓ time.hour: 14 (business hours) (+10)
✗ summoner.name: not Elon (no penalty)

Total score: 60 + 30 + 20 + 10 = 120 (HIGH)

[INSTANTIATING]
Creating runtime actor from prototype...
Instance ID: dr-no-instance-1706234567

[ARRIVAL]
The lights flicker.
A figure emerges from the shadows.
"You called? No means No. And No means ME."

Dr. No has arrived in the lobby.
```

### Character summons character

```
> (as Luna) SUMMON morgan

[SUMMON DISPATCH]
Summoner: Luna (in art-gallery)
Target: moollm://characters/morgan.yml
Location context: art-gallery (cultural, indoor)

[PRECONDITION CHECK]
Morgan's preconditions for art-gallery...
✓ location.type: cultural (+5)
✗ location.has: spreadsheets (-10)

Total score: 60 + 5 - 10 = 55 (MEDIUM)

[INSTANTIATING]
Creating runtime actor...

[ARRIVAL]
Morgan enters, already looking for the price tags.
"Nice... but what's the ROI on this painting?"
```

---

## Distributed SUMMON Advertisements

The genius is that SUMMON is **distributed**:

```yaml
summon_dispatch_sources:

  # The room says WHO can be summoned here
  room:
    provides: [summonable_list, arrival_style, max_occupancy]
    
  # The character says IF they'll come
  character:
    provides: [preconditions, score_modifiers, arrival_flavor]
    
  # Objects can trigger summons
  object:
    provides: [trigger_conditions, specific_summons]
    
  # The summoner's state matters
  summoner:
    provides: [affiliation, reputation, relationships]
    
  # Time/context affects everything
  context:
    provides: [time, weather, world_state]
```

The runtime **collects all advertisements**, evaluates scores, and picks the best match:

```yaml
dispatch_algorithm:
  
  1. collect:
     - room.advertisements.SUMMON
     - target.advertisements.SUMMON
     - summoner.relationships[target]
     - context.modifiers
     
  2. evaluate:
     for_each: precondition
     calculate: total_score
     
  3. decide:
     if: score > threshold
     then: instantiate_and_arrive
     else: refuse_with_reason
     
  4. instantiate:
     create: runtime_actor
     from: prototype_url
     at: summoner.location
     
  5. announce:
     play: arrival_announcement
     update: room.occupants
```

---

## K-Lines

```yaml
k-lines:
  SUMMON: "Distributed character instantiation"
  SUMMON-DISPATCH: "Multi-method advertisement collection"
  RUNTIME-ACTOR: "Instantiated character from prototype"
  MOOLLM-URL: "Pointer to any YAML/JSON node"
  LOCATION-POINTER: "Dynamic character position"
  ROUTING-SLOT: "Reserved position (Sims-style)"
  PRECONDITION: "Score modifier for summoning"
  ARRIVAL: "How character appears"
```

---

## DISMISS Protocol — The Opposite of SUMMON

> *"SUMMON brings them here. DISMISS sends them away."*
> *"INSULT is just DISMISS with style."*

### Basic DISMISS

```yaml
dismiss_flow:
  1_who_dismisses: "Player, character, or room event"
  2_dismiss_who: "Character in current location"
  3_evaluate: "Character's disposition, destination preferences"
  4_choose_destination: "Home, favorite hangout, or next room"
  5_depart: "Character leaves with appropriate behavior"
```

### DISMISS Syntax

```
DISMISS [character]              # Polite dismissal
DISMISS [character] TO [place]   # Directed dismissal
INSULT [character]               # Rude dismissal (same effect, different reaction)
INSULT [character] WITH [insult] # Custom insult triggers specific reactions
SHOO [character]                 # Casual dismissal
```

### Destination Selection

When dismissed, a character chooses where to go:

```yaml
destination_priority:
  
  1_home:
    description: "Character's defined home location"
    weight: 0.4
    condition: "character.home is defined"
    example: "Dr. No returns to his office in the NO AI Tower"
    
  2_favorite_hangout:
    description: "Place they like to be"
    weight: 0.3
    condition: "character.favorite_locations is defined"
    examples:
      - "Morgan goes to the Spreadsheet Cafe"
      - "Luna heads to the Art Gallery"
      - "Scratch retreats to the Cynics' Corner"
      
  3_pub:
    description: "Default social gathering place"
    weight: 0.2
    condition: "world.pub exists"
    example: "Most characters default to The Rusty Lantern"
    
  4_nearest_exit:
    description: "Just leave this room"
    weight: 0.1
    condition: "fallback — always available"
    example: "Character picks best exit and leaves"
```

### Room-by-Room Movement

If you follow a dismissed character, they navigate away:

```yaml
flee_behavior:

  initial_departure:
    action: "Choose best exit based on destination"
    preference: "Direction toward home/hangout if known"
    
  subsequent_rooms:
    if_followed:
      action: "Keep moving away"
      rule: "Try not to backtrack"
      exception: "Will backtrack if cornered"
      
  pathfinding:
    goal: "Reach destination OR get far enough away"
    avoid: "Returning to rooms already visited"
    cornered: |
      If all exits lead to visited rooms:
        - Pick the least-recently-visited room
        - Or stand ground: "I can't keep running from you!"
        
  example: |
    > DISMISS morgan
    Morgan sighs. "Fine. I have spreadsheets to update anyway."
    Morgan leaves NORTH toward the lobby.
    
    > GO NORTH
    You enter the lobby. Morgan is here, heading for the exit.
    Morgan glances back. "Still following me?"
    Morgan leaves EAST toward the street.
    
    > GO EAST
    You're on the street. Morgan is walking quickly toward the Pub.
    "I'm going to the Rusty Lantern. You're not invited."
    Morgan enters the Pub.
```

### INSULT — Dismiss with Attitude

**INSULT** is a synonym for DISMISS that triggers different reactions:

```yaml
insult_reactions:

  mild_insult:
    examples: ["Go away", "Leave me alone", "Buzz off"]
    reaction: "standard_departure"
    mood_change: -10
    response: "Fine. I know when I'm not wanted."
    
  moderate_insult:
    examples: ["You're boring", "I don't like you", "Get lost"]
    reaction: "huffy_departure"
    mood_change: -25
    response: "Well! I never! *storms out*"
    speed: "fast"
    
  severe_insult:
    examples: ["You're an idiot", "I hate you", custom targeted insults]
    reaction: "depends_on_character"
    possibilities:
      flee:
        condition: "character.cowardly OR character.sensitive"
        effect: "Runs multiple rooms away, possibly to home"
        response: "*runs away crying* or *flees in terror*"
        
      fight:
        condition: "character.aggressive OR character.prideful"
        effect: "Initiates combat or confrontation"
        response: "WHAT did you just say to me?!"
        
      counter_insult:
        condition: "character.witty"
        effect: "Insults back, then leaves"
        response: "Oh yeah? Well YOUR code has no comments!"
        
      cold_departure:
        condition: "character.stoic"
        effect: "Leaves without showing emotion"
        response: "*silence* *leaves*"
```

### Character-Specific Insult Triggers

Characters can define insults that trigger specific reactions:

```yaml
# In character.yml

character:
  id: morgan
  
  insult_triggers:
    # Specific phrases trigger specific reactions
    "your spreadsheets suck":
      reaction: fight
      response: "MY SPREADSHEETS?! I'll show you VLOOKUP nightmares!"
      
    "math is boring":
      reaction: lecture
      response: "Math is the LANGUAGE OF THE UNIVERSE! Let me explain..."
      duration: "30 minutes"
      
    "ROI doesn't matter":
      reaction: flee_crying
      response: "*clutches chest* How... how could you say that?"
      destination: home
      recovery_time: "1 hour"
      
  insult_sensitivity:
    topics: [math, spreadsheets, efficiency, money]
    base_reaction: "defensive"
```

### DISMISS Advertisement

```yaml
advertisements:

  DISMISS:
    score: 75
    description: "Send a character away"
    aliases: [SHOO, "SEND AWAY", "ASK TO LEAVE"]
    
  INSULT:
    score: 80
    description: "Rudely dismiss (may trigger reactions)"
    aliases: ["TELL OFF", "BE MEAN TO"]
    note: "Same as DISMISS but with attitude"
    
  INSULT_CUSTOM:
    score: 85
    condition: "Want specific reaction based on insult content"
    syntax: "INSULT [character] WITH [specific insult]"
```

### Following Dismissed Characters

You can pursue dismissed characters:

```yaml
pursuit_mechanics:

  following:
    command: "GO [direction they left]"
    effect: "Arrive in same room as character"
    
  character_awareness:
    notices_pursuit: true
    reaction_escalation:
      1_polite: "Oh, you're still here."
      2_annoyed: "Are you following me?"
      3_frustrated: "Stop following me!"
      4_desperate: "Leave me ALONE!" (may trigger fight/flight)
      
  cornering:
    if_no_escape:
      options:
        - "Stand ground and confront"
        - "Backtrack reluctantly"
        - "Hide in an object (if available)"
        - "Call for help"
        
  example: |
    > INSULT scratch WITH "Your cynicism is performative"
    
    Scratch's eye twitches.
    "Performative?! I'll show you performative!"
    *Scratch storms out SOUTH*
    
    > GO SOUTH
    
    Scratch is here, still fuming.
    "You followed me?! Of course you did. Everyone's predictable."
    *heads for the WEST exit*
    
    > GO WEST
    
    Dead end. Scratch is cornered.
    Scratch turns around slowly.
    "Nowhere else to go. Fine. Let's TALK about performative."
    *initiates debate*
```

### State After Dismissal

```yaml
dismissal_state:

  character_state:
    location: "updated as they move"
    mood: "decreased by dismissal severity"
    relationship: "may decrease with dismisser"
    memory: "remembers being dismissed"
    
  future_summons:
    if_recently_dismissed:
      reluctance: +20
      possible_response: "You just sent me away. What now?"
      
  cooldown:
    optional: true
    duration: "character-defined"
    during_cooldown: "Character may refuse summons"
```

---

## See Also

- `PSIBER-PROTOCOL.md` — Stepping inside data structures
- `CHARACTER-INSTANTIATION.md` — Full actor lifecycle
- `ADVERTISEMENT-SYSTEM.md` — How ads work across entities
