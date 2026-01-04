# Imaging

> *"Every image is a semantic snapshot. The metadata IS the meaning."*

---

## The Rule

**When generating ANY image, ALWAYS include full context as metadata.**

This isn't optional. This isn't "nice to have." This is how MOOLLM ensures coherence, reproducibility, and meaning in visual generation.

---

## Why Metadata Matters

Images without metadata are orphans — beautiful but contextless. With metadata:

| Benefit | How |
|---------|-----|
| **Coherence** | Same character looks the same across images |
| **Reproducibility** | Can regenerate with identical context |
| **Psychology → Visuals** | Personality affects posture, expression |
| **Series consistency** | Photo series stays coherent |
| **Semantic clipboard** | Copy/paste meaning, not just pixels |

---

## The Semantic Clipboard

Think of image metadata as a **semantic clipboard** — when you "copy" a scene for image generation, you're copying:

- Who is there (Mind Mirror profiles, costumes, moods)
- Where they are (room, lighting, atmosphere)
- What's happening (action, context, narrative moment)
- How to see it (camera angle, style, focus)

This "clipboard" can be:
- **Pasted** to generate the image
- **Modified** to create variations
- **Stored** as a card for later use
- **Shared** with other processes
- **Compared** across different moments

---

## What to Include

### For Characters

```yaml
subject:
  name: "Captain Ashford"
  
  # Mind Mirror personality snapshot
  mind_mirror:
    confident: 6       # Walks into rooms like they own them
    cheerful: 5        # Default mood: amused by existence
    proud: 5           # Won't ask for help even when should
    creative: 6        # Solutions from left field
    
  # Current appearance
  costume: "Space pirate with holographic eyepatch"
  accessories: ["brass compass", "leather satchel"]
  
  # Emotional state at this moment
  mood: "victorious, exhausted, relieved"
  expression: "triumphant grin, eyes slightly wet"
  body_language: "chest out, shoulders back, slight swagger"
  
  # What they're doing/holding
  action: "holding the Golden Chalice aloft"
  holding: "Golden Chalice (glowing softly, ancient runes visible)"
```

**Why personality matters for visuals:**
- `confident: 6` → stands tall, takes up space
- `timid: 6` → hunched, makes self smaller
- `cheerful: 5` → smile lines, bright eyes
- `restless: 4` → dynamic pose, mid-motion

### For Rooms

```yaml
room:
  name: "Treasure Chamber"
  
  # Atmosphere
  lighting: "warm golden glow from treasure piles"
  atmosphere: "ancient, dusty, awe-inspiring"
  temperature: "cool, slightly damp"
  
  # What's visible
  notable_objects:
    - "Mountains of gold coins catching light"
    - "Ancient tapestries depicting forgotten kings"
    - "Empty pedestal where chalice was"
    - "Cobwebs in corners, undisturbed for centuries"
    
  # Spatial layout
  exits_visible: ["dark archway to the north", "collapsed tunnel east"]
  ceiling: "vaulted, lost in shadow above"
  floor: "cracked marble, coins scattered"
```

### For Objects

```yaml
object:
  name: "Golden Chalice"
  
  # Physical properties
  material: "gold with silver inlay"
  size: "fits in two hands"
  condition: "pristine despite age"
  
  # Special properties
  magical_effects: "soft golden glow, warmth to touch"
  inscriptions: "ancient runes spiraling around rim"
  
  # Current state
  position: "held aloft by Captain Ashford"
  lighting_interaction: "reflects torch light, casts golden shadows"
```

### For Complete Scenes

```yaml
image_prompt:
  type: scene
  
  # WHO
  subject:
    name: "Captain Ashford"
    mind_mirror:
      confident: 6, cheerful: 5, proud: 5, creative: 6
    costume: "Space pirate with holographic eyepatch"
    mood: "victorious, exhausted, relieved"
    action: "holding the Golden Chalice aloft"
    
  # WHERE  
  room:
    name: "Treasure Chamber"
    lighting: "warm golden glow from treasure piles"
    atmosphere: "ancient, dusty, awe-inspiring"
    notable_objects:
      - "Mountains of gold coins"
      - "Ancient tapestries on walls"
      - "Empty pedestal where chalice was"
      
  # OTHER OCCUPANTS
  other_characters: []
  
  # HOW TO SEE IT
  camera:
    angle: "low angle, looking up (heroic)"
    distance: "medium shot, waist up"
    focus: "character face and chalice"
    depth_of_field: "shallow, background softly blurred"
    
  # STYLE
  style:
    aesthetic: "dramatic portrait, chiaroscuro lighting"
    mood: "triumphant, epic, earned"
    references: "Rembrandt lighting, adventure movie poster"
```

---

## The Protocol

```yaml
IMAGE-METADATA:
  meaning: "Image prompts include full scene context as metadata."
  invoke_when: "Generating any image"
  
  layers:
    - CHARACTER: "Mind Mirror + appearance + mood + action"
    - ROOM: "Atmosphere + lighting + objects + layout"
    - OBJECT: "Properties + state + interactions"
    - CAMERA: "Angle + distance + focus + style"
    
  principle: |
    The metadata IS the semantic content.
    The image is just one rendering of that content.
    With metadata, you can render again, differently.
    Without it, the image is a dead end.
```

---

## Integration with Other Skills

### Mind Mirror → Imaging

Mind Mirror profiles automatically feed into image generation:

```yaml
# From mind-mirror profile
confident: 6       # Walks into rooms like they own them

# Becomes imaging metadata  
body_language: "stands tall, takes up space, commanding presence"
expression: "direct eye contact, slight knowing smile"
```

### Soul Chat → Imaging

Conversation moments become image prompts:

```yaml
# From soul-chat
moment: "The bartender slides a drink across the counter with a knowing look"

# Becomes imaging metadata
scene:
  characters: [bartender, player]
  action: "drink sliding across polished wood"
  atmosphere: "intimate, conspiratorial"
  lighting: "warm tavern glow, face half in shadow"
```

### Adventure → Imaging

Room and object state feeds visualization:

```yaml
# From adventure room state
room: "Treasure Chamber"
objects: [chalice, gold_piles, tapestries]
player_position: "center, facing pedestal"

# Becomes imaging metadata
scene:
  room: { ... full room context ... }
  subject: { ... full character context ... }
  spatial: "character centered, surrounded by wealth"
```

---

## Variations and Series

With metadata, you can generate **coherent variations**:

```yaml
# Base prompt
base:
  subject: { ... Captain Ashford full context ... }
  room: { ... Treasure Chamber ... }
  action: "holding chalice"

# Variation 1: Different angle
variation_1:
  <<: *base
  camera:
    angle: "high angle, looking down (vulnerability)"
    
# Variation 2: Different moment
variation_2:
  <<: *base
  subject:
    mood: "shock, disbelief"
    action: "first touching the chalice"
    
# Variation 3: Different style
variation_3:
  <<: *base
  style:
    aesthetic: "watercolor, soft edges"
```

---

## Photo Series with Dependencies

For coherent photo series, reference shared elements:

```yaml
series: "Victory Photos"

shared_elements:
  chalice:
    description: "Golden Chalice with silver inlay and glowing runes"
    # All photos reference this for consistency
    
  character_state:
    mind_mirror: { confident: 6, cheerful: 5 }
    costume: "Space pirate with holographic eyepatch"
    
photos:
  - name: "wide_establishing"
    references: [shared_elements.chalice, shared_elements.character_state]
    camera: { angle: "wide", distance: "full room" }
    
  - name: "chalice_closeup"
    references: [shared_elements.chalice]
    camera: { angle: "macro", focus: "runes on rim" }
    
  - name: "victory_portrait"
    references: [shared_elements.chalice, shared_elements.character_state]
    camera: { angle: "low heroic", distance: "medium" }
```

---

## Storing Image Metadata as Cards

Image prompts can be saved as cards for reuse:

```yaml
# photo-victory-portrait.card.yml
card:
  type: image_prompt
  name: "Victory Portrait Template"
  
  template:
    subject:
      # Placeholders for any character
      name: "{{ character.name }}"
      mind_mirror: "{{ character.mind_mirror }}"
      costume: "{{ character.costume }}"
      mood: "triumphant"
      
    room:
      name: "{{ room.name }}"
      lighting: "dramatic, warm"
      
    style:
      aesthetic: "heroic portrait"
      references: "adventure movie poster"
      
  usage: |
    Play this card after any major victory.
    Fills in from current character and room state.
```

---

## Protocol Symbols

| Symbol | Meaning |
|--------|---------|
| `IMAGE-METADATA` | Full context snapshot for image generation |
| `SEMANTIC-CLIPBOARD` | Copy/paste meaning, not just data |
| `PHOTO-SERIES` | Coherent set of related images |
| `VARIATION` | Same base, different rendering |

---

## Dovetails With

- [mind-mirror/](../mind-mirror/) — Personality feeds image metadata
- [soul-chat/](../soul-chat/) — Conversation moments become scenes
- [room/](../room/) — Room state feeds environment
- [card/](../card/) — Image prompts as reusable cards
- [adventure/](../adventure/) — World state feeds visualization

---

## The Bottom Line

> **Every image is a semantic snapshot.**
>
> The metadata isn't overhead — it's the meaning.
> The image is just one possible rendering of that meaning.
> With metadata, you can render again. Differently. Better.
> Without it, the image is an orphan.
>
> **Copy meaning. Paste meaning. The semantic clipboard.**
