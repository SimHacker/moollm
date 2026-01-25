# MOOST Multiplayer Vision

*Collaborative world-building through image generation, analysis, and remix.*

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   PLAYER A (Cursor)          SUPABASE           PLAYER B (Web)      │
│   ┌─────────────────┐     ┌───────────┐     ┌─────────────────┐    │
│   │ Generate image  │────▶│  Shared   │◀────│ Analyze image   │    │
│   │ Edit prompts    │◀────│   JSON    │────▶│ Add mining      │    │
│   │ Mine meanings   │────▶│   Model   │◀────│ Remix prompt    │    │
│   └─────────────────┘     └───────────┘     └─────────────────┘    │
│            │                    │                    │              │
│            ▼                    ▼                    ▼              │
│      ┌──────────┐        ┌──────────┐        ┌──────────┐         │
│      │   Git    │◀──────▶│ Runtime  │◀──────▶│   Git    │         │
│      │  (fork)  │        │  Server  │        │  (fork)  │         │
│      └──────────┘        └──────────┘        └──────────┘         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## The Vision

### Every Place is a Gallery

```
lane-neverending/
  no-ai-tower/
    images/
      000-original/           # First generation
        prompt.yml            # The prompt that made it
        image.png             # The generated image
        MINING-composition.md # Compositional analysis
        MINING-mood.md        # Emotional read
        MINING-symbols.md     # Symbolic interpretation
      001-player-remix/       # Player's variation
        prompt.yml            # Modified prompt
        image.png             # New generation
        MINING-*.md           # Fresh analysis
      002-uploaded/           # Player uploaded their own art
        source.png            # Original upload
        MINING-*.md           # AI analysis of human art
      003-mashup/             # Prompt mashup experiment
        prompt.yml            # Combined elements
        image.png
        MINING-*.md
```

### The Image Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  1. DESCRIBE ──▶ 2. GENERATE ──▶ 3. ANALYZE ──▶ 4. MINE        │
│       │              │               │              │           │
│       ▼              ▼               ▼              ▼           │
│   Edit text      API call       Vision API     Multiple        │
│   in room,       to DALL-E,     reads back     perspectives:   │
│   object,        Midjourney,    what it        - don.md        │
│   character      Stable Diff    actually made  - satellite.md  │
│                                                - mood.md       │
│       │              │               │              │           │
│       └──────────────┴───────────────┴──────────────┘           │
│                           │                                     │
│                           ▼                                     │
│                    5. SHARE ──▶ 6. REMIX                       │
│                         │           │                           │
│                         ▼           ▼                           │
│                    Supabase     Other players                   │
│                    broadcasts   see, fork,                      │
│                    to all       mashup, evolve                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Image Directory Structure

Each visualizable thing (room, character, object, concept) can have an `images/` directory:

```yaml
# images/000-dusk-neon/prompt.yml
id: "000-dusk-neon"
created_by: "don"
created_at: "2026-01-25T19:30:00Z"
generator: "dall-e-3"

prompt:
  style: "cinematic photography, magic hour"
  subject: |
    A one-story building at dusk. On its roof, a massive 40-foot 
    neon sign in hot pink, THREE LINES stacked vertically:
    NO
    AI  
    TOWER
    The sign is taller than the building. Forced perspective 
    makes the tiny building look like it's straining under 
    the weight of meaning.
  
  mood: "mysterious, liminal, question without answer"
  
  negative: "realistic text, readable letters, modern cars"

# Inherited context from parent directories
inherits:
  - ../../PHOTO.yml          # Structural truth
  - ../../MINING-don.md      # Don's voice for style
  - ../../MINING-sound.md    # Atmosphere cues

# Mining layers generated after image creation
mining:
  - MINING-composition.md    # Rule of thirds, focal points
  - MINING-color.md          # Palette analysis
  - MINING-symbol.md         # Semiotic read
  - MINING-mood.md           # Emotional temperature
  - MINING-narrative.md      # Story this image tells
```

## Standing Still, Seeing Everything

You don't have to move to explore. Stand in one place and watch the world transform:

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONTEMPLATION MODE                           │
│                                                                 │
│   Standing in: THE FLORIST                                      │
│   Watching: [ROOM] [ADA II] [WINDOW] [SIGN OUTSIDE]            │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                                                         │  │
│   │   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   │  │
│   │   ░░░░░  [IMAGE TRANSITIONS THROUGH VIEWS]  ░░░░░░░░   │  │
│   │   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   │  │
│   │                                                         │  │
│   │   000: Ada II — watercolor, peaceful               3s   │  │
│   │   001: Ada II — noir, shadows, menacing      ──▶   3s   │  │
│   │   002: Ada II — sketch, folk art                   3s   │  │
│   │   003: The Room — wide angle, cluttered            3s   │  │
│   │   004: The Room — close-up, details                3s   │  │
│   │   005: Window view — sign glowing outside          3s   │  │
│   │   006: Window view — rain streaks                  3s   │  │
│   │                        ▼                                │  │
│   │              [LOOPS / SHUFFLES]                         │  │
│   │                                                         │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│   ▶ PLAY  ⏸ PAUSE  ⏭ NEXT  🔀 SHUFFLE  ⚙ SETTINGS             │
│                                                                 │
│   Showing: Room + Characters + Objects + Views                  │
│   Speed: 3s per image   Transition: crossfade                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### What Cycles Through

From one spot, watch all these transform:

```yaml
slideshow_layers:
  room:
    - "The florist shop — morning light"
    - "The florist shop — dusk, neon glow from outside"
    - "The florist shop — noir, dramatic shadows"
    - "The florist shop — watercolor dreamscape"
    
  characters:
    ada_ii:
      - "Ada II — peaceful, swaying"
      - "Ada II — hungry, vines reaching"
      - "Ada II — conducting the other plants"
      - "Ada II — military flashback, rigid"
      - "Ada II — singing, mouth open"
    
  objects:
    window:
      - "Window — NO AI TOWER sign visible"
      - "Window — rain streaks"
      - "Window — condensation, mysterious"
    counter:
      - "Counter — cluttered with pots"
      - "Counter — single wilting flower"
      
  views:
    - "Wide shot — whole room"
    - "Ada II close-up — detail on vines"
    - "Through the window — street view"
    - "Floor level — looking up at Ada II"
    - "Ceiling — looking down at everything"
```

### Transition Modes

```
CROSSFADE     — Gentle blend between images
HARD CUT      — Instant switch (noir feeling)
MORPH         — AI interpolation between views
GLITCH        — Databend transitions
PARALLAX      — Layers move at different speeds
```

### Ambient Mode

Leave it running. The room breathes. Ada II shifts between moods. The light changes. The sign outside flickers. You're not playing — you're *inhabiting*.

```javascript
// Ambient slideshow config
const ambientConfig = {
  location: "florist/back-room",
  include: ["room", "characters", "objects", "views"],
  shuffle: true,
  speed: 5000,  // 5 seconds per image
  transition: "crossfade",
  duration: 500,
  loop: true,
  
  // Time-of-day awareness
  timeSync: true,  // Show dusk images at dusk
  
  // Mood tracking
  moodBias: "peaceful",  // Favor calm images
  
  // Player activity
  pauseOnInteract: true,  // Stop when player does something
};
```

## The Slideshow Navigator

```
┌─────────────────────────────────────────────────────────────────┐
│  NO AI TOWER — Image Gallery                          [3/7]    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐  │
│   │                                                         │  │
│   │                   [CURRENT IMAGE]                       │  │
│   │                                                         │  │
│   │            ░░░░░ NO ░░░░░                               │  │
│   │            ░░░░░ AI ░░░░░                               │  │
│   │            ░░░ TOWER ░░░                                │  │
│   │                 ║                                       │  │
│   │            ┌────┴────┐                                  │  │
│   │            │ building │                                 │  │
│   │            └─────────┘                                  │  │
│   │                                                         │  │
│   └─────────────────────────────────────────────────────────┘  │
│                                                                 │
│   ◀ PREV │ 000 │ 001 │ [002] │ 003 │ 004 │ 005 │ 006 │ NEXT ▶  │
│                                                                 │
│   Created by: player_jane    Generator: midjourney-v6          │
│   Prompt: "watercolor style, twilight, dreamlike..."           │
│                                                                 │
│   [VIEW MINING] [EDIT PROMPT] [REMIX] [GENERATE NEW] [UPLOAD]  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Multiplayer Sync via Supabase

```typescript
// Real-time subscription to world changes
const worldChannel = supabase
  .channel('moost-world')
  .on('postgres_changes', 
    { event: '*', schema: 'public', table: 'world_objects' },
    (payload) => {
      // Another player edited the NO AI TOWER description!
      if (payload.new.path === 'lane-neverending/no-ai-tower') {
        // Update local view
        world.update(payload.new);
        
        // Show notification
        notify(`${payload.new.edited_by} changed the tower description`);
        
        // Offer to regenerate image with new description
        if (payload.new.description_changed) {
          offerRegenerate(payload.new);
        }
      }
    }
  )
  .subscribe();
```

### Shared JSON Model

```json
{
  "world_id": "moost-alpha",
  "revision": 4721,
  "players_online": ["don", "jane", "ada_ii"],
  
  "objects": {
    "lane-neverending/no-ai-tower": {
      "description": "...",
      "images": {
        "current": "003-jane-watercolor",
        "available": ["000-original", "001-don-remix", "002-uploaded", "003-jane-watercolor"],
        "generating": null
      },
      "last_edited_by": "jane",
      "last_edited_at": "2026-01-25T19:45:00Z"
    }
  },
  
  "active_generations": [
    {
      "player": "don",
      "target": "florist/ada-ii",
      "prompt": "...",
      "status": "pending",
      "started_at": "2026-01-25T19:44:30Z"
    }
  ]
}
```

## The Creative Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   NAVIGATE ──▶ LOOK ──▶ IMAGINE ──▶ DESCRIBE ──▶ GENERATE      │
│       │                                              │          │
│       │         ┌────────────────────────────────────┘          │
│       │         │                                               │
│       │         ▼                                               │
│       │      ANALYZE ──▶ MINE ──▶ SHARE ──▶ DISCUSS            │
│       │         │                              │                │
│       │         │         ┌────────────────────┘                │
│       │         │         │                                     │
│       │         ▼         ▼                                     │
│       └───── REMIX ◀── INSPIRE ◀── SEE OTHERS' WORK            │
│                                                                 │
│   The world grows through collaborative imagination             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Player Actions

### Generate
```
> generate image of no-ai-tower

Using description from PHOTO.yml + your recent edits...
Style: cinematic, dusk, neon glow
Generating with DALL-E 3...

[████████████████████░░░░] 80%

Image generated! Saved as images/007-don-cinematic/
Running analysis...

MINING-composition.md: Strong vertical dominance, sign fills 60% of frame
MINING-mood.md: Liminal, questioning, slightly ominous
MINING-symbol.md: The sign-as-tower inverts expectations of scale

Share to world? [Y/n]
```

### Analyze (your own or uploaded)
```
> upload my-sketch.png to no-ai-tower

Uploaded as images/008-uploaded/source.png
Running vision analysis...

What I see:
- Hand-drawn sketch, pencil on paper
- The sign is drawn as physically impossible — letters floating
- Building is tiny, almost crushed
- Human figure for scale, looking up

Generated mining:
- MINING-style.md: Folk art quality, intentional naivety
- MINING-interpretation.md: Artist emphasizes impossibility
- MINING-emotion.md: Wonder mixed with unease

Add to gallery? [Y/n]
```

### Remix
```
> remix 003 with 005

Combining prompts:
- 003: watercolor style, dreamlike, soft edges
- 005: noir photography, harsh shadows, rain

Mashup prompt:
"Watercolor noir — soft washes of color but harsh 
compositional shadows. Rain streaks like brushstrokes.
The neon bleeds pink into wet pavement."

Generate? [Y/n]
```

### Edit-to-Regenerate
```
> edit no-ai-tower description

Current:
  "A one-story building with a 40-foot neon sign..."

Your edit:
  "A one-story building with a 40-foot neon sign,
   but now VINES are growing up the letters.
   Ada II's influence is spreading."

Save and regenerate image? [Y/n]

Generating with vine additions...
Image saved as images/009-vines/
```

## Git + Server Hybrid

```
LOCAL PLAY                    SHARED PLAY
───────────                   ────────────
Git repo                      Supabase DB
  │                               │
  ├── images/                     ├── images table
  │   └── 000-*/                  │   (URLs to storage)
  │       ├── prompt.yml          │
  │       ├── image.png           ├── prompts table
  │       └── MINING-*.md         │
  │                               ├── mining table
  └── can work offline            │
      commit when ready           └── real-time sync
      push to share                   instant updates
```

Players can:
1. **Work locally** — Git repo, offline, commit when ready
2. **Play live** — Supabase sync, see others in real-time
3. **Hybrid** — Local edits, push to sync, pull others' work

## The MOOST Protocol

```yaml
# Every image generation follows this protocol

1_describe:
  # Player edits text in room/object/character
  # Or writes fresh prompt
  # System assembles context from parent PHOTO.yml, MINING-*.md

2_generate:
  # Call image API with assembled prompt
  # Store in numbered directory
  # Record prompt.yml with full metadata

3_analyze:
  # Vision API reads generated image
  # "What do you see? Describe composition, mood, symbols."
  # Store raw analysis

4_mine:
  # Multiple perspective passes:
  #   - MINING-composition.md (formal analysis)
  #   - MINING-mood.md (emotional read)
  #   - MINING-symbol.md (semiotic interpretation)
  #   - MINING-narrative.md (what story does this tell?)
  #   - MINING-<player>.md (player's personal read)

5_share:
  # Commit to git OR
  # Push to Supabase
  # Notify other players

6_remix:
  # Others see your work
  # Fork your prompt
  # Mashup with their ideas
  # The world evolves
```

---

## The Dream

```
You walk down Lane Neverending at dusk.

The NO AI TOWER sign buzzes overhead — but wait,
this isn't the image you remember.

Jane was here. She painted vines climbing the letters.
Don added rain. The pavement is wet now.
Someone uploaded a sketch — folk art style, 
the building even tinier.

You look at Ada II through the florist window.
Three different players have drawn her.
One made her terrifying. One made her maternal.
One made her... dancing?

You have an idea.

> edit ada-ii
> "She's not dancing. She's conducting.
>  Her vines move like a maestro's hands.
>  The other plants in the shop sway in time."

> generate

The image appears. It's not what you imagined.
It's better. The AI saw something you didn't.

You run analysis. The mining reveals:
"The conducting gesture implies she controls more
than just this room. The other plants are her orchestra.
What symphony is she preparing?"

You share it.

Somewhere, Don sees your image appear in his feed.
He has an idea too.

The world grows.
```

---

*MOOST: Where everyone is a world-builder.*
