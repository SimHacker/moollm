# MOOST Multiplayer Vision

*Collaborative world-building through image generation, analysis, and remix.*

```
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│   PLAYER A (Cursor)          SUPABASE           PLAYER B (Web)     │
│   ┌─────────────────┐     ┌───────────┐     ┌─────────────────┐    │
│   │ Generate image  │────▶│  Shared   │◀────│ Analyze image   │    │
│   │ Edit prompts    │◀────│   JSON    │────▶│ Add mining      │    │
│   │ Mine meanings   │────▶│   Model   │◀────│ Remix prompt    │    │
│   └─────────────────┘     └───────────┘     └─────────────────┘    │
│            │                    │                    │             │
│            ▼                    ▼                    ▼             │
│      ┌──────────┐        ┌──────────┐        ┌──────────┐          │
│      │   Git    │◀──────▶│ Runtime  │◀──────▶│   Git    │          │
│      │  (fork)  │        │  Server  │        │  (fork)  │          │
│      └──────────┘        └──────────┘        └──────────┘          │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

## The Vision

### Every Place is a Gallery

**Distributed naming: `{timestamp}-{userid}-{slug}/`**

No sequential numbers (000, 001) — that causes merge conflicts!
Timestamp-userid prefixes are globally unique, conflict-free.

```
lane-neverending/
  no-ai-tower/
    images/
      20260125T190000Z-don-original/           # Don's first generation
        prompt.yml
        image.png
        MINING-composition.md
        MINING-mood.md
        
      20260125T191500Z-jane-watercolor/        # Jane's variation
        prompt.yml
        image.png
        MINING-*.md
        
      20260125T192000Z-bob-uploaded/           # Bob uploaded art
        source.png
        MINING-*.md
        
      20260125T193045Z-don-mashup-jane/        # Don remixed Jane's
        prompt.yml
        image.png
        based_on: "20260125T191500Z-jane-watercolor"
        
      20260126T080000Z-ada-ii-generated/       # NPC can create too!
        prompt.yml
        image.png
        creator_type: "npc"
```

**Why timestamp-userid?**
```yaml
benefits:
  no_conflicts:
    - Everyone creates independently
    - Git merge just works
    - No coordination needed
    
  natural_ordering:
    - Sort alphabetically = chronological order
    - See who made what when
    
  attribution:
    - Creator always visible in path
    - Provenance built-in
    
  forkable:
    - based_on field tracks lineage
    - Remix chains visible
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

Each visualizable thing (room, character, object, concept) can have an `images/` directory.

**Naming: `{ISO8601-timestamp}-{userid}-{slug}/`**

```yaml
# images/20260125T193000Z-don-dusk-neon/prompt.yml
id: "20260125T193000Z-don-dusk-neon"
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
│   Watching: [ROOM] [ADA II] [WINDOW] [SIGN OUTSIDE]             │
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                                                         │   │
│   │   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    │   │
│   │   ░░░░░  [IMAGE TRANSITIONS THROUGH VIEWS]  ░░░░░░░░    │   │
│   │   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    │   │
│   │                                                         │   │
│   │   don-0125: Ada II — watercolor, peaceful          3s   │   │
│   │   jane-0125: Ada II — noir, menacing         ──▶   3s   │   │
│   │   bob-0126: Ada II — sketch, folk art              3s   │   │
│   │   don-0126: The Room — wide angle                  3s   │   │
│   │   jane-0126: The Room — close-up                   3s   │   │
│   │   ada-0126: Window view — sign glow                3s   │   │
│   │   bob-0127: Window view — rain                     3s   │   │
│   │                        ▼                                │   │
│   │              [LOOPS / SHUFFLES]                         │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│   ▶ PLAY  ⏸ PAUSE  ⏭ NEXT  🔀 SHUFFLE  ⚙ SETTINGS              │
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
- jane-0125-watercolor: dreamlike, soft edges
- bob-0126-noir: harsh shadows, rain

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

## Video Commentary — MST3K Mode

Characters can watch videos WITH you and react in real-time:

```
┌────────────────────────────────────────────────────────────────┐
│  NOW PLAYING: Little Shop of Horrors - Feed Me Scene           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   ┌───────────────────────────────────────────────────────┐    │
│   │                                                       │    │
│   │              [EMBEDDED YOUTUBE VIDEO]                 │    │
│   │                                                       │    │
│   │                     advancement!                      │    │
│   │                                                       │    │
│   └───────────────────────────────────────────────────────┘    │
│                                                                │
│   ▶ 01:23 / 04:45    ════════════●══════════    🔊 ⚙️          │
│                                                                │
├────────────────────────────────────────────────────────────────┤
│  COMMENTARY TRACK                                              │
│                                                                │
│  [00:30] 🌱 Ada II: "FEED ME SEYMOUR! ...sorry. Involuntary."  │
│  [00:45] 🌱 Ada II: "You know, in the original I was more—"    │
│  [00:50] 🌱 Ada II: "TARGET ACQUI—" [vines freeze]             │
│  [01:00] 🌱 Ada II: "The harmonies are quite sophisticated."   │
│  [01:15] 🔊 [vine_rustle.mp3]                                  │
│  [01:23] 🌱 Ada II: "REPEAT 4. That calms me down." ◀── NOW    │
│                                                                │
│  [YOUR MESSAGE...]                                    [SEND]   │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### How It Works

```yaml
commentary_track:
  video: "youtube:xLkV4lkdf"
  
  events:
    - timestamp: "00:00:05"
      character: ada-ii
      type: remark
      text: "Look at her. So young. So hungry."
      
    - timestamp: "00:01:15"
      character: ada-ii
      type: sound_effect
      sound: "vine_rustle"
      
    - timestamp: "00:02:00"
      character: ada-ii
      type: song_snippet
      performance: "feed-me-seymour"
      verse: "chorus"
```

### Features

- **YouTube Embed** — Play any video in the world
- **Transcript Access** — Characters can react to what's being said
- **Timestamped Events** — Remarks, sound effects, song snippets
- **Live Commentary** — AI generates reactions in real-time
- **Watch Parties** — Multiple characters (and players) comment together
- **Saved Tracks** — Pre-recorded commentary like DVD extras
- **Sound Effects** — Characters can play sounds at specific moments

### Character Reactions

```yaml
reaction_types:
  - agree           # "Yes! Exactly!"
  - disagree        # "That's not right..."
  - joke            # Puns, callbacks
  - reference       # "That reminds me of..."
  - sound_effect    # Dramatic stings
  - sing_along      # If music plays
  - flashback       # Ada II's PTSD triggers
  - teaching_moment # "In Logo, you would..."
```

### Watch Party Mode

Multiple players + NPCs watching together:

```
[01:23] 🌱 Ada II: "The harmonies are sophisticated."
[01:25] 👤 Player1: "lol she's really into this"
[01:26] 👤 Player2: 😂
[01:28] 🌱 Ada II: "I heard that. My vines have ears."
[01:30] 🔊 [dramatic_sting.mp3]
```

---

## Spotify Integration — Stream Music in the World

With Spotify Premium + OAuth login, characters can DJ and react to real music:

```
┌─────────────────────────────────────────────────────────────────┐
│  🎵 NOW PLAYING via Spotify                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────┐  "Mean Green Mother from Outer Space"            │
│   │  ████   │   Levi Stubbs — Little Shop of Horrors OST       │
│   │  ████   │                                                   │
│   │  ████   │   ▶ 02:15 / 04:32  ═══════●═══════  🔊           │
│   └─────────┘                                                   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  COMMENTARY                                                     │
│                                                                 │
│  [02:00] 🌱 Ada II: [vines trembling]                          │
│  [02:10] 🌱 Ada II: "This... this was my anthem. Before."      │
│  [02:15] 🌱 Ada II: "I'M A MEAN GREEN— no. No. REPEAT 4."      │
│  [02:20] 🌱 Ada II: [quietly] "I was so good at my job."       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### What Spotify Enables

```yaml
spotify:
  requires: "Premium account + OAuth login"
  
  capabilities:
    playback:
      - play / pause / skip
      - seek to timestamp
      - volume control
      - queue management
      
    metadata:
      - track name, artist, album
      - album art (for display)
      - duration
      - current position (for sync)
      
    search:
      - find tracks by name
      - browse playlists
      - character recommendations
      
    # No raw audio access, but can sync commentary to playback position
    sync:
      - get current timestamp
      - trigger events at specific times
      - react to track changes
```

### Character DJ Mode

```yaml
dj_mode:
  ada_ii:
    playlists:
      - name: "Ada's Chill Mix"
        spotify: "spotify:playlist:37i9dQZF1DX..."
        mood: peaceful
        note: "Ambient sounds for Logo coding"
        
      - name: "Flashback Fuel"
        spotify: "spotify:playlist:..."
        mood: dangerous
        warning: "May trigger military memories"
        tracks:
          - "Fortunate Son"
          - "Paint It Black"
          - "Mean Green Mother"
          
      - name: "Constructionist Anthems"
        spotify: "spotify:playlist:..."
        mood: teaching
        note: "Music for learning"
        
    commands:
      - "Ada, play something chill"
      - "Ada, what's this song?"
      - "Ada, skip this one"
      - "Ada, add this to my playlist"
```

### Lyrics Sync (If Available)

Some tracks have synced lyrics via Spotify's API:

```
[02:15] 🎵 "I'm a mean green mother from outer space"
[02:15] 🌱 Ada II: [winces]
[02:18] 🎵 "And I'm bad"
[02:18] 🌱 Ada II: "I WAS bad. Past tense."
[02:21] 🎵 "I'm a mean green mother from outer space"
[02:21] 🌱 Ada II: "FORWARD 100 RIGHT 90 FORWARD 100..."
```

### Listen Together

Multiple players share the same Spotify session:

```yaml
listen_together:
  host: "player_1"           # Controls playback
  listeners: ["player_2", "player_3", "ada-ii"]
  
  sync:
    - All hear same music at same time
    - Commentary synced to playback position
    - Characters react together
    
  example: |
    [Host plays "Feed Me (Git Me)" by Jonathan Coulton]
    
    [00:30] 🌱 Ada II: "Oh! I know this one!"
    [00:32] 👤 Player2: "wait there's a git version??"
    [00:35] 🌱 Ada II: "MERGE CONFLICT! ...sorry, muscle memory."
```

### Fallback: 30-Second Previews

Without Premium, Spotify provides 30-second preview URLs:

```yaml
preview_mode:
  duration: 30_seconds
  quality: "low bitrate"
  use_for: "Sampling before purchase"
  
  character_response: |
    Ada II: "I can only play a preview without Premium.
             But 30 seconds is enough for one good flashback."
```

---

## The Precompiled World — No LLM at Runtime

**The killer insight:** LLM generates at BUILD time. Browser runs PURE JAVASCRIPT.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   BUILD TIME (LLM)                 RUNTIME (Browser Only)       │
│   ════════════════                 ═══════════════════════      │
│                                                                 │
│   ┌─────────────┐                  ┌─────────────────────┐     │
│   │   YAML      │                  │                     │     │
│   │   Rooms     │   ══════════▶    │   compiled.js       │     │
│   │   NPCs      │   Adventure      │                     │     │
│   │   Songs     │   Compiler       │   - All rooms       │     │
│   │   Movies    │                  │   - All dialogs     │     │
│   │   Comments  │                  │   - All reactions   │     │
│   └─────────────┘                  │   - All commentary  │     │
│         │                          │   - All sounds      │     │
│         │                          │                     │     │
│   ┌─────────────┐                  │   NO LLM CALLS!     │     │
│   │    LLM      │                  │   100% offline      │     │
│   │  (Claude)   │                  │   Zero API cost     │     │
│   │             │                  │   Instant response  │     │
│   │ Generates   │                  │                     │     │
│   │ closures,   │                  └─────────────────────┘     │
│   │ dialogs,    │                            │                 │
│   │ reactions   │                            ▼                 │
│   └─────────────┘                  ┌─────────────────────┐     │
│                                    │     Browser         │     │
│                                    │     Player          │     │
│                                    │                     │     │
│                                    │  Pure JS execution  │     │
│                                    │  Web Audio API      │     │
│                                    │  Speech Synthesis   │     │
│                                    │  YouTube embed      │     │
│                                    │  Spotify SDK        │     │
│                                    └─────────────────────┘     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### What Gets Precompiled

```yaml
compiled_world:
  rooms:
    # Every room's pickDescription(lod) as JS function
    - id: "florist/back-room"
      pickDescription: "function(lod) { ... }"
      exits: [...]
      
  characters:
    # Every NPC with dialog trees, reactions, commentary
    - id: "ada-ii"
      pickDescription: "function(lod) { ... }"
      dialogs:
        first_meeting: { nodes: [...], edges: [...] }
        song_selection: { nodes: [...], edges: [...] }
      reactions:
        to_video: { timestamps: [...] }
        to_music: { triggers: [...] }
      party_behavior:
        join_conditions: [...]
        commentary_style: "nervous, Logo-obsessed"
        
  performances:
    # Every song, fully parsed and ready
    - id: "feed-me-seymour"
      verses: [...]
      timing: [...]
      voice_configs: { ada: {...}, seymour: {...} }
      
  commentary_tracks:
    # Every movie commentary, timestamped
    - video: "youtube:little-shop-feed-me"
      events:
        - { t: 5000, char: "ada-ii", type: "remark", text: "..." }
        - { t: 15000, char: "ada-ii", type: "emote", text: "..." }
        - { t: 30000, char: "ada-ii", type: "sound", sound: "vine_rustle" }
```

### The Full Loop — All Precompiled

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  1. NAVIGATE           Pure JS room transitions                  │
│     > go north         No LLM, just compiled room graph          │
│                                                                  │
│  2. ENCOUNTER          Precompiled NPC descriptions              │
│     > look ada         pickDescription("look") runs instantly    │
│                                                                  │
│  3. TALK               Dialog tree traversal                     │
│     > talk to ada      Finite state machine, no LLM              │
│                                                                  │
│  4. RECRUIT            Party join conditions (precompiled)       │
│     > ada join me      Checks flags, adds to party array         │
│                                                                  │
│  5. TRAVEL             Party follows, all precompiled            │
│     > go to theater    Room transitions with party in tow        │
│                                                                  │
│  6. WATCH              YouTube embed + commentary track          │
│     > play movie       Timestamped events fire automatically     │
│                                                                  │
│  7. REACT              All party members chatter                 │
│     [00:30]            Each has precompiled commentary track     │
│     🌱 Ada: "Feed me!" Speech synthesis, no LLM needed          │
│     👤 You: [react]    Player can type reactions too            │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Party at the Movies

```javascript
// All precompiled — runs in browser with ZERO LLM calls

class MovieNight {
  constructor(video, party) {
    this.video = video;
    this.party = party;  // [ada_ii, seymour, player]
    
    // Load precompiled commentary tracks for each party member
    this.tracks = party.map(char => 
      compiledWorld.commentary[video.id][char.id]
    );
  }
  
  play() {
    this.video.play();
    
    // Each party member's commentary fires at precompiled timestamps
    this.tracks.forEach(track => {
      track.events.forEach(event => {
        setTimeout(() => {
          this.fireEvent(event);
        }, event.timestamp);
      });
    });
  }
  
  fireEvent(event) {
    switch(event.type) {
      case 'remark':
        // Speech synthesis — no LLM, just precompiled text
        speak(event.character, event.text);
        break;
      case 'sound':
        // Web Audio API
        playSound(event.sound);
        break;
      case 'emote':
        // Display in chat
        displayEmote(event.character, event.emote);
        break;
      case 'song_snippet':
        // Play a bit of a precompiled song
        performSnippet(event.performance, event.verse);
        break;
    }
  }
}
```

### Example: Movie Night with Party

```
> recruit ada
Ada II's vines perk up. "You want me to come with you?
I haven't left this room in... what year is it?"
[Ada II joins your party]

> recruit seymour
The old man smiles. "An adventure? Like the old days?"
[Seymour joins your party]

> go to theater
You walk down Lane Neverending with your party.
Ada II's pot hovers on a small drone. Seymour shuffles beside you.

> play "little shop of horrors"
The screen flickers to life.

[00:05] 🌱 Ada II: "Oh no. Not this one."
[00:05] 👴 Seymour: "I remember when we filmed this."
[00:10] 🌱 Ada II: [vines trembling]
[00:15] 👴 Seymour: "The harmonies were your idea, you know."
[00:20] 🌱 Ada II: "FEED ME SEY— sorry. Sorry."
[00:25] 🔊 [vine_rustle.mp3]
[00:30] 👴 Seymour: "It's okay. Let it out."
[00:35] 🌱 Ada II: "REPEAT 4 [FORWARD 100 RIGHT 90]"
[00:40] 👴 Seymour: "That's my girl."
```

**All of this runs with ZERO LLM calls.** The LLM wrote the commentary during compilation. The browser just plays it back, synced to video timestamps.

### Why This Matters

```yaml
benefits:
  offline_play:
    - Works without internet (except for video/music streaming)
    - Can cache videos locally for true offline
    
  zero_runtime_cost:
    - No API calls = no API bills
    - Play for hours, costs nothing
    
  instant_response:
    - No network latency
    - Reactions fire at exact millisecond
    
  deterministic:
    - Same input = same output
    - Speedruns possible
    - Reproducible bugs
    
  distributable:
    - Ship as static files
    - Host on GitHub Pages
    - Embed in Electron app
    - Works on potato computers
    
  shareable:
    - Players can share compiled worlds
    - Fork and modify YAML, recompile
    - Community content creation
```

### The Hybrid Model

Of course, you CAN add LLM at runtime for:
- Truly dynamic conversation
- Image generation
- Procedural content
- Player-driven story

But the **baseline experience** works entirely offline, precompiled.

```yaml
runtime_modes:
  offline:
    - All precompiled content
    - Zero LLM
    - Works everywhere
    
  enhanced:
    - Precompiled base
    - LLM for novel situations
    - Falls back to precompiled if offline
    
  creative:
    - Full LLM access
    - Generate new rooms, NPCs, commentary
    - Contribute back to world
```

---

*MOOST: Where everyone is a world-builder.*
