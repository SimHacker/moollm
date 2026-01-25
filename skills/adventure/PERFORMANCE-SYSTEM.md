# Performance System — Plug-in Speech Synthesizer Performances

*"Feed me... some attention! I have performances prepared."* — Ada II

## Overview

The Performance System enables characters like Ada II to perform songs, soliloquies, and essays using browser speech synthesis. Performances are defined in YAML files and played back with multi-character voices, karaoke-style lyrics display, and playback controls.

**Inspired by:** `temp/lloooomm/dist/audrey-serenades-seymour-lloooomm-response.html`

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     PERFORMANCE SYSTEM                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    │
│   │  YAML Files  │───▶│ Performance  │───▶│   Speech     │    │
│   │  (Songs)     │    │   System     │    │   Synthesis  │    │
│   └──────────────┘    └──────────────┘    └──────────────┘    │
│         │                    │                   │             │
│         │             ┌──────┴──────┐           │             │
│         │             │             │           │             │
│   ┌─────▼─────┐  ┌────▼────┐  ┌────▼────┐  ┌──▼──────┐      │
│   │ Repertoire │  │ Karaoke │  │ Controls │  │ Voice   │      │
│   │ Registry   │  │ Display │  │   UI     │  │ Manager │      │
│   └───────────┘  └─────────┘  └──────────┘  └─────────┘      │
│                                                                │
└─────────────────────────────────────────────────────────────────┘
```

## Files

- `dist/performance.js` — Core performance system
- `dist/speech.js` — Speech synthesis module (existing)
- `florist/back-room/ada-ii-song-feed-me-seymour.yml` — Example song

## Song YAML Format

Songs are defined in YAML with this structure:

```yaml
# Song metadata
meta:
  song_title: "Feed Me, Seymour! (Constructionist Version)"
  source: "LLOOOOMM Archive"
  
# Character voice configurations
speech_config:
  ada:
    pitch: 0.4
    rate: 0.8
    volume: 1.0
    preferred_voices: ['Samantha', 'Victoria']
  seymour:
    pitch: 0.2
    rate: 1.0
    preferred_voices: ['Daniel', 'Alex']

# The actual performance
lloooomm_song:
  dialogue_intro:
    - character: seymour
      text: "Here you go, girl..."
      
  verse_1:
    title: "Introduction"
    lyrics: |
      Think me! Code me! Grow me!
      Think me, Seymour...
    duration_ms: 5000
    emote: "[vines swaying]"
```

## Usage

### Basic Playback

```javascript
// Initialize
const performer = new PerformanceSystem(speechSystem);

// Load and play
await performer.loadFromYAML('ada-ii-song-feed-me-seymour.yml');
performer.play();

// Controls
performer.pause();
performer.stop();
performer.setSpeed(1.5);  // 0.3 to 2.0
```

### With Karaoke Display

```javascript
// Create display
const display = new KaraokeDisplay('karaoke-container', performer);
const controls = new PerformanceControls('controls-container', performer);

// Events
performer.on('lineStart', (line, idx) => console.log(`Speaking: ${line.text}`));
performer.on('complete', () => console.log('Performance complete!'));
```

### Ada II Performer

```javascript
const ada = new AdaIIPerformer(performer);

// List what Ada II can perform
console.log(ada.listRepertoire());

// Request a performance
await ada.perform('feed-me-seymour');

// Ada II greets you
console.log(ada.getGreeting());
// → "Feed me... some attention! I have performances prepared."
```

## Ada II's Repertoire

### Currently Available

| ID | Title | Type | Duration |
|----|-------|------|----------|
| `feed-me-seymour` | Feed Me, Seymour! (Constructionist Version) | Song | ~5 min |

### Coming Soon

| ID | Title | Type | Notes |
|----|-------|------|-------|
| `papert-mindstorms-intro` | Mindstorms: Introduction | Essay | Seymour Papert's classic |
| `mean-green-mother` | Mean Green Mother (Reprise) | Song | Ada II's origin story |
| `suddenly-seymour` | Suddenly Seymour (Logo Remix) | Song | Love ballad with turtles |

## Adventure Integration

When a player enters Ada II's room and talks to her:

```yaml
# In ROOM.yml or character interaction
on_talk:
  - action: offer_performance
    dialog: |
      Ada II's vines rustle with anticipation.
      "Ah, a visitor! Would you like to hear me sing?"
    options:
      - id: feed-me-seymour
        label: "🎵 Feed Me, Seymour!"
      - id: decline
        label: "Maybe later..."
```

## Voice Modes

Ada II has multiple voice modes that can be triggered:

| Mode | Pitch | Rate | When Used |
|------|-------|------|-----------|
| `normal` | 0.8 | 0.9 | Regular speech |
| `singing` | 0.6 | 0.75 | During songs |
| `flashback` | 0.3 | 1.3 | Military memories |
| `recovery` | 1.0 | 0.7 | After flashbacks |

## Events

| Event | Payload | Description |
|-------|---------|-------------|
| `loaded` | performance | Performance loaded |
| `start` | performance | Playback started |
| `lineStart` | line, index | Line begins |
| `lineEnd` | line, index | Line ends |
| `pause` | currentLine | Playback paused |
| `stop` | - | Playback stopped |
| `complete` | performance | Reached end |
| `speedChange` | speed | Speed changed |

## CSS Styling

The karaoke display expects these CSS classes:

```css
.karaoke-display {
  background: #1a1a1a;
  border: 2px solid #ffd700;
  padding: 20px;
  height: 400px;
  overflow-y: auto;
}

.karaoke-current {
  font-size: 1.4em;
  color: #ffd700;
  animation: pulse 2s infinite;
}

.karaoke-current.speaking {
  background: rgba(255, 215, 0, 0.1);
}

.karaoke-history-entry {
  opacity: 0.6;
  font-size: 1em;
}

.speaker-name { font-weight: bold; }
.speaker-ada { color: #ff6b9d; }
.speaker-seymour { color: #4ecdc4; }
.speaker-narrator { color: #9c27b0; }

.emote {
  font-style: italic;
  opacity: 0.7;
}
```

## Future Enhancements

1. **Papert Essays** — Ada II reads Seymour Papert's writings
2. **Duets** — Multiple characters singing together
3. **Audience Participation** — Player can join in
4. **Music Backing Track** — Web Audio API integration
5. **Video Recording** — Export performances
6. **Custom Songs** — User-submitted YAML performances

## Credits

- **Original Inspiration:** Little Shop of Horrors (1982)
- **LLOOOOMM Adaptation:** Constructionist learning parody
- **Ada II Character:** NO AI TOWER / Adventure-4
- **Speech System:** MOOLLM Adventure Runtime
