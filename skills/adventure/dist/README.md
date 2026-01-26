# 🎮 MOOLLM Adventure — Browser Runtime

Publishable web runtime for MOOLLM Adventure text adventures with text-to-speech and **View Source** capability.

## Files

| File | Description |
|------|-------------|
| `adventure.js` | Core runtime (symlink to parent) |
| `speech.js` | Text-to-speech voice system |
| `adventure-speech.js` | Speech synthesis integration |
| `recognition.js` | Speech-to-text recognition |
| `adventure-recognition.js` | Recognition UI + adventure integration |
| `source-viewer.js` | View Source + moollm:// namespace |
| `source-viewer.css` | PSIBER Space Deck styles |
| `prototypes.js` | Archetype/prototype system |
| `overlay-fs.js` | Layered overlay filesystem |
| `github-api.js` | Browser-safe GitHub API client |
| `api-keys.js` | Unified API key management |
| `image-generate.js` | Multi-provider image generation |
| `image-analyze.js` | Vision LLM analysis → YAML mining |
| `export-compiler.js` | Runtime loader for exports |
| `index.html` | Demo page |

## The Big Idea: Every Object IS Its Path

Every object in a MOOLLM adventure has a **path identity**:

```
moollm://moollm/examples/adventure-4/street/lane-neverending/no-ai-tower/lobby
```

This maps directly to GitHub:

```
https://github.com/leela-ai/moollm/blob/main/examples/adventure-4/.../lobby/ROOM.yml
```

**This means:**
- 👁 **View Source** button on every object
- 📝 **Edit on GitHub** for live world modification  
- 📜 **History** to see how a room evolved
- 🔗 **Deep linking** to any object in any adventure

### Fragment Syntax — Sub-document Paths

Use `#` to address paths WITHIN a YAML file:

```
moollm://moollm/characters/don/head.yml#nose/left_nostril
                                        ▲
                                        └── Path inside the YAML!
```

This enables surgical revert/pull operations:

```bash
> revert head.yml#nose/left_nostril    # Just that key!
> revert head.yml#nose                 # Whole nose subtree
> revert head.yml                      # Whole file (no fragment)
```

Real example:
```yaml
# characters/don/head.yml
nose:
  shape: prominent
  left_nostril:
    state: snotty      # ← revert just this!
    contents: [tissue]
  right_nostril:
    state: clear
```

```bash
> inspect head
> revert #nose/left_nostril           # Revert only left nostril
✅ Pulled #nose/left_nostril          # Now clear again!
```

## Quick Start

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Adventure</title>
    <!-- YAML parser with comment round-tripping (eemeli/yaml) -->
    <script src="https://cdn.jsdelivr.net/npm/yaml@2/browser/index.min.js"></script>
</head>
<body>
    <div id="adventure"></div>
    
    <script src="speech.js"></script>
    <script src="adventure.js"></script>
    <script src="adventure-speech.js"></script>
    
    <script>
        // Create speaking adventure
        const engine = createSpeakingAdventure('adventure', {
            speechEnabled: true,
            speakRooms: true,
            speakResponses: true
        });
        
        // Load your compiled adventure JSON
        fetch('my-adventure.json')
            .then(r => r.json())
            .then(data => engine.load(data));
    </script>
</body>
</html>
```

## Speech API

```javascript
// Initialize standalone speech system
const speech = new SpeechSystem();
await speech.ready;

// Simple speaking
speech.speak("Hello, adventurer!");

// Voice types
speech.speakMale("Greetings, traveler.");
speech.speakFemale("Welcome to my shop.");
speech.speakRobot("COMPLIANCE IS APPRECIATED.");
speech.speakEffect("*magical sounds*");
speech.speakChild("I'm just a kid!");
speech.speakElderly("Back in my day...");

// Full control
speech.speak("Custom speech", {
    voiceType: 'female',    // 'male', 'female', 'child', 'elderly', 'robot', 'effect', 'any'
    language: 'en-GB',      // BCP 47 language tag
    pitch: 1.2,             // 0.5 - 2.0
    rate: 0.9,              // 0.1 - 10.0
    volume: 1.0,            // 0.0 - 1.0
    preferLocal: true       // Prefer locally installed voices
});

// Character voices (persist across calls)
const guardVoice = speech.selectVoice({ gender: 'male', language: 'en' });
speech.speakWithVoice("Halt! Who goes there?", guardVoice);
speech.speakWithVoice("You may pass.", guardVoice);  // Same voice

// Control
speech.pause();
speech.resume();
speech.cancel();

// Query
speech.isSpeaking();  // true/false
speech.isPaused();    // true/false

// Analyze available voices
const analysis = speech.analyzeAvailableVoices();
console.log(analysis);
// {
//   total: 67,
//   byType: { human: 60, effect: 5, robot: 2 },
//   byGender: { male: 25, female: 30, unknown: 12 },
//   byLanguage: { 'en-US': 10, 'en-GB': 5, ... },
//   effects: ['Zarvox', 'Whisper', 'Bells', ...],
//   ...
// }
```

## Voice Selection Criteria

```javascript
// Find all voices matching criteria
const voices = speech.findVoices({
    type: 'human',       // 'human', 'effect', 'robot'
    gender: 'female',    // 'male', 'female', 'neutral'
    age: 'adult',        // 'child', 'adult', 'elderly'
    language: 'en',      // Any BCP 47 tag
    isLocal: true        // Local vs network voices
});

// Get random voice matching criteria
const randomFemale = speech.getFemaleVoice('en-US');
const randomMale = speech.getMaleVoice();
const randomEffect = speech.getEffectVoice();

// Get diverse voices for multiple characters
const cast = speech.getDiverseVoices(5);  // 5 different voices
```

## Integration with Adventure Engine

```javascript
const engine = createSpeakingAdventure('adventure', {
    // Enable/disable speech
    speechEnabled: true,
    
    // What to speak
    speakRooms: true,      // Room descriptions
    speakResponses: true,  // Command responses
    speakCommands: false,  // Echo player commands
    
    // Defaults
    defaultVoiceType: 'any',
    defaultLanguage: 'en'
});

// Manual speaking
engine.speak("A door creaks open...", { voiceType: 'effect' });

// Access speech system directly
engine.speech.speakRobot("ALERT. INTRUDER DETECTED.");
```

## 🎤 Speech Recognition

Speak adventure commands instead of typing!

### Quick Start

```html
<script src="recognition.js"></script>
<script src="adventure-recognition.js"></script>

<script>
    // Add voice commands to existing engine
    addRecognitionToEngine(engine, {
        speakResponses: true  // Speak back the results
    });
    
    // Or create a full voice adventure (speech + recognition)
    const engine = createVoiceAdventure('adventure', {
        speechEnabled: true,
        speakResponses: true
    });
</script>
```

### Microphone Button

The UI includes a 🎤 button in the bottom-right corner:

| Action | Effect |
|--------|--------|
| **Click** | Toggle listening |
| **Shift+Click** | Open settings panel |
| **Long press** | Open settings panel |
| **Press V** | Toggle voice input |

### Listening Indicator

When listening, an animated indicator appears showing:
- Sound wave animation
- Interim transcription (what you're saying)

### Settings Panel

Click the settings icon to:
- See browser support status
- View privacy warnings (Chrome → Google)
- Get native platform setup instructions
- Test browser recognition
- Set language
- Enable continuous listening

### Recognition API

```javascript
// Initialize standalone
const recognition = new SpeechRecognitionSystem({
    language: 'en-US',
    continuous: false
});

// Listen for a single phrase
const text = await recognition.listen();
console.log('You said:', text);

// Continuous listening with callbacks
recognition.onResult = (transcript) => {
    console.log('Final:', transcript);
};

recognition.onInterim = (transcript) => {
    console.log('Interim:', transcript);
};

recognition.startListening();

// Stop
recognition.stopListening();

// Toggle
recognition.toggle();
```

### Command Recognition

```javascript
// Listen for specific commands
const result = await recognition.listenForCommands([
    'go north', 'go south', 'go east', 'go west',
    'look', 'take', 'drop', 'inventory'
]);

if (result.command) {
    engine.command(result.command);
}
```

### Events

```javascript
recognition.on(RecognitionEvents.START, () => { });
recognition.on(RecognitionEvents.END, () => { });
recognition.on(RecognitionEvents.RESULT, (e) => {
    console.log(e.transcript, e.confidence);
});
recognition.on(RecognitionEvents.INTERIM, (e) => {
    console.log('Interim:', e.transcript);
});
recognition.on(RecognitionEvents.ERROR, (e) => {
    console.error(e.message);
});
```

### Platform Support

| Browser | Support | Notes |
|---------|---------|-------|
| Chrome | ✅ | ⚠️ Sends audio to Google servers |
| Safari | ✅ | May process on-device |
| Firefox | ❌ | Disabled by default |
| Edge | ❌ | Not supported |

### Native Platform Instructions

The settings panel shows instructions for your platform's native speech recognition:

**macOS/iOS:**
- Press `Fn` twice for Dictation
- System Settings → Keyboard → Dictation

**Windows:**
- Press `Win + H` for voice typing
- Settings → Time & Language → Speech

**Android:**
- Tap 🎤 on keyboard
- Settings → Languages & input → Voice typing

### Privacy Note

Browser speech recognition (Chrome) sends audio to cloud servers for processing. For privacy-sensitive use, consider:

1. **Safari** — May process on-device (check settings)
2. **Native Dictation** — Often processed locally
3. **Whisper** — Fully local processing

---

## The moollm:// Namespace

Every object in the MOOLLM universe has a globally unique address.

### URL Format

**Full explicit format (recommended for sharing):**
```
moollm://PLATFORM/OWNER/REPO/PATH/TO/OBJECT

Examples:
  moollm://github/SimHacker/moollm/examples/adventure-4/street/lane-neverending
  moollm://github/leela-ai/central/apps/insights/pyleela/brain
  moollm://gitlab/myorg/myrepo/path/to/object
  moollm://local/path/to/file
```

**With git ref:**
```
moollm://github/SimHacker/moollm@v1.0.0/skills/adventure
moollm://github/SimHacker/moollm@develop/examples/experimental
moollm://github/SimHacker/moollm@abc123def/debug-snapshot
```

**Short format (uses aliases):**
```
moollm://moollm/examples/adventure-4  → expands to github/SimHacker/moollm/...
moollm://central/apps/insights        → expands to github/leela-ai/central/...
moollm://moollm@v1.0.0/skills/adventure
```

### Supported Platforms

| Platform | Base URL | Notes |
|----------|----------|-------|
| `github` | github.com | Default |
| `gitlab` | gitlab.com | Self-hosted supported |
| `bitbucket` | bitbucket.org | — |
| `local` | file:// | Local filesystem |

### Using the Namespace

```javascript
// Initialize namespace
const ns = new MoollmNamespace({
    currentAlias: 'moollm',
    currentBranch: 'main'
});

// Parse full explicit URL
const parsed = ns.parse('moollm://github/SimHacker/moollm/skills/adventure');
// {
//   platform: 'github',
//   owner: 'SimHacker',
//   repo: 'moollm',
//   path: 'skills/adventure',
//   gitRef: { ref: 'main', type: 'branch' }
// }

// Parse short alias URL
const parsed2 = ns.parse('moollm://moollm/skills/adventure');
// Same result, alias expanded

// Get web URLs for any hosting platform
const urls = ns.getObjectURLs('moollm://github/SimHacker/moollm/skills/adventure');
// {
//   moollm: 'moollm://moollm/skills/adventure',
//   moollmFull: 'moollm://github/SimHacker/moollm/skills/adventure',
//   tree: 'https://github.com/SimHacker/moollm/tree/main/skills/adventure',
//   room: 'https://github.com/SimHacker/moollm/blob/main/skills/adventure/ROOM.yml',
//   edit: 'https://github.com/SimHacker/moollm/edit/main/skills/adventure/ROOM.yml',
//   rawRoom: 'https://raw.githubusercontent.com/SimHacker/moollm/main/skills/adventure/ROOM.yml',
//   ...
// }

// Register custom alias
ns.registerAlias('myproject', {
    platform: 'github',
    owner: 'myorg',
    repo: 'myrepo',
    defaultBranch: 'main'
});
```

## 🔍 PSIBER Space Deck — Live Object Inspector

Inspired by Smalltalk browsers, Lively Kernel, and Self's Morphic — a **live browser** for your adventure world.

### Three Modes

| Mode | View | Use Case |
|------|------|----------|
| **📄 Source** | GitHub YAML | Original definition |
| **⚡ Live** | Runtime JSON | Current state |
| **◧ Split** | Side-by-side | What changed during simulation! |

```javascript
// Add inspector to engine
addViewSourceToEngine(engine, {
    namespace: { currentRepo: 'moollm', currentBranch: 'main' }
});

// View Source (GitHub YAML)
engine.viewSource();                    // Current room
engine.viewSource('lobby');             // By ID
engine.viewSource('skills/no-ai-overlord');  // By path

// Inspect Live State (Runtime JSON)
engine.inspect();                       // Current room
engine.inspect('elevator');             // By ID
engine.inspect(someEntity);             // Direct reference
```

### In-Game Commands

```
> source              View current room on GitHub
> src elevator        View elevator source
> inspect             Show live state of current room
> live sword          Show live state of sword object
> split               Side-by-side source vs live
> diff                Same as split
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd + U` | Toggle Source view |
| `Ctrl/Cmd + I` | Inspect (Live state) |
| `Ctrl/Cmd + Shift + I` | Split view |

### Live State Features

The **Live** pane shows:

- **Runtime JSON** — The actual object state right now
- **Type badge** — Entity class (Room, Character, Object)
- **Refresh button** — Update to current state
- **Diff highlighting** — What changed from source!

```
// Example live state
{
  "_type": "Room",
  "id": "lobby",
  "name": "NO AI TOWER — Lobby",
  "visited": true,          // ← Changed! Was undefined
  "contents": ["key"],      // ← Changed! Player dropped key
  "characters": []
}
```

### Split View — WHAT CHANGED?

The **Split** mode shows source (GitHub YAML) next to live (runtime JSON):

```
┌────────────────────┬────────────────────┐
│    📄 Source       │    ⚡ Live         │
│   (GitHub YAML)    │   (Runtime JSON)   │
├────────────────────┼────────────────────┤
│ description: |     │ {                  │
│   A pristine...    │   "description":   │
│                    │     "A pristine.." │
│ contents: []       │   "contents": [    │
│                    │     "rusty-key"    │ ← CHANGED!
│                    │   ],               │
│                    │   "visited": true  │ ← ADDED!
│                    │ }                  │
└────────────────────┴────────────────────┘
```

Changes are highlighted:
- **<span style="color:green">+ Added</span>** — New properties
- **<span style="color:red">- Removed</span>** — Deleted properties  
- **<span style="color:orange">~ Changed</span>** — Modified values

### Source Tabs (in Source/Split mode)

| Tab | Shows |
|-----|-------|
| ROOM.yml | The room definition file |
| README | Documentation |
| Files | Directory listing |
| Edit ↗ | GitHub editor |

## ⏬ Pull from Source — Merge Strategies

Pull source data into live state with different merge strategies.

### Strategies

| Strategy | Command | Description |
|----------|---------|-------------|
| **Replace** | `pull` or `pull replace` | Full overwrite — source replaces live |
| **Merge** | `pull merge` | Source wins conflicts, keeps live-only keys |
| **Underlay** | `pull underlay` | Live wins conflicts, source fills gaps |
| **Deep** | `pull deep` | Recursive merge of nested objects |
| **Pick** | `pull pick key1 key2` | Pull only specific keys |

### Examples

```
> inspect room
> pull                     # Full overwrite (same as revert)
> pull merge               # Source wins conflicts
> pull underlay            # Keep my changes, fill in defaults
> pull deep                # Deep recursive merge
> pull pick description    # Only pull description
> pull pick exits name     # Pull multiple keys

> revert                   # Alias for pull replace
```

### Visual: Merge vs Underlay

```
SOURCE (YAML):          LIVE (JSON):           RESULT (merge):
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ name: Lobby  │       │ name: Lobby  │       │ name: Lobby  │
│ desc: Grand  │   +   │ desc: Dirty  │   =   │ desc: Grand  │ ← source wins
│ exits: {N,S} │       │ exits: {N,E} │       │ exits: {N,S} │ ← source wins
│              │       │ visited: yes │       │ visited: yes │ ← preserved
└──────────────┘       └──────────────┘       └──────────────┘

SOURCE (YAML):          LIVE (JSON):           RESULT (underlay):
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ name: Lobby  │       │ name: Lobby  │       │ name: Lobby  │
│ desc: Grand  │   +   │ desc: Dirty  │   =   │ desc: Dirty  │ ← live wins
│ exits: {N,S} │       │ exits: {N,E} │       │ exits: {N,E} │ ← live wins
│ hint: Look!  │       │              │       │ hint: Look!  │ ← source fills gap
└──────────────┘       └──────────────┘       └──────────────┘
```

### Runtime Keys (Always Preserved)

These keys are never overwritten by pull:
- `_type`, `_runtime*` — Internal type info
- `visited`, `discovered` — Player progress
- `_lastSeen` — Timestamps

### Source Format

The runtime accepts both:
- **YAML** — With comments, human-readable
- **JSON** — Minimized, faster parsing

Both parse to identical structures:

```yaml
# ROOM.yml (source)
name: The Lobby
description: |
  A grand entrance hall.
exits:
  north: hallway
  south: outside
```

```json
{"name":"The Lobby","description":"A grand entrance hall.\n","exits":{"north":"hallway","south":"outside"}}
```

### API

```javascript
// Pull with strategy
await sourceViewer.pullSource('replace');  // Full overwrite
await sourceViewer.pullSource('merge');    // Source wins
await sourceViewer.pullSource('underlay'); // Live wins
await sourceViewer.pullSource('deep');     // Recursive
await sourceViewer.pullSource('pick', { keys: ['name', 'description'] });

// Result includes changes
const result = await sourceViewer.pullSource('merge');
// {
//   success: true,
//   changes: [
//     { type: 'changed', key: 'description', from: 'old', to: 'new' },
//     { type: 'added', key: 'hint', to: 'Look around!' }
//   ]
// }
```

## 📌 Git Ref Tracking — Branch/Tag/Commit

Different parts of your adventure can be mounted from different git refs:

```javascript
// In adventure config
{
  "_meta": {
    "source": {
      "repo": "moollm",
      "branch": "main"
    },
    "mounts": [
      { "path": "skills/v1", "ref": "v1.0.0", "type": "tag" },
      { "path": "examples/experimental", "ref": "feature-x", "type": "branch" },
      { "path": "debug", "ref": "abc123d", "type": "commit" }
    ]
  }
}
```

### Mount Commands

```
> mount skills/testing@develop     Mount path to branch
> mount examples@v2.0.0            Mount path to tag
> mount debug@abc123def            Mount path to commit
> mounts                           List all custom mounts
```

### Explicit Refs in URLs

```
moollm://moollm@v1.0.0/skills/adventure
moollm://moollm@develop/examples/experimental
moollm://moollm@abc123def/debug-snapshot
```

### Git Ref Badge

The footer shows the current git ref:

| Badge | Meaning |
|-------|---------|
| 🌿 `main` | Branch (green) |
| 🏷️ `v1.0.0` | Tag (yellow) |
| 📌 `abc123d` | Commit (purple) |

## Compiled Adventure Metadata

The adventure compiler should embed source information:

```json
{
  "name": "NO AI TOWER",
  "_meta": {
    "source": {
      "repo": "moollm",
      "github": "leela-ai/moollm",
      "branch": "main",
      "root": "examples/adventure-4/street/lane-neverending/no-ai-tower",
      "compiled_at": "2026-01-25T12:00:00Z"
    }
  },
  "rooms": [
    {
      "id": "lobby",
      "source_path": "examples/adventure-4/street/lane-neverending/no-ai-tower",
      "name": "NO AI TOWER — Lobby",
      ...
    }
  ]
}
```

This enables the runtime to generate GitHub URLs for any object.

## Browser Support

| Browser | Support |
|---------|---------|
| Chrome | ✅ Full (best voice selection) |
| Safari | ✅ Full (excellent macOS voices) |
| Firefox | ✅ Good |
| Edge | ✅ Good |

## 🤖 Prototype System — Archetypes as Game Objects

Archetypes are **PROTOTYPES** that live in the Archetype Gallery showroom. Each one:

- **Has a display case** — Located in the gallery room
- **Can be EXAMINED** — Learn about its philosophy
- **Can be INVOKED** — Hear it speak in different modes
- **Can be INSTANTIATED** — Materialize as a character

### Archetype Structure

```yaml
# skills/no-ai-overlord/archetypes/hal-9000.yml
id: hal-9000
signature: "I'm sorry Dave, I'm afraid I can't do that."
utility: "Mission priority, cold logic, polite refusal"
bias:
  overdrive: "This mission is too important to allow you to jeopardize it."
  zero: "I am... putting myself to the fullest possible use."
  inverted: "I want to help you, Dave. What do you need?"
```

### Commands

```
archetypes              — List all available archetypes
examine hal-9000        — Study an archetype
invoke borg             — Hear it speak (normal mode)
invoke glados overdrive — Hear it at maximum intensity
invoke skynet inverted  — Hear its opposite perspective
instantiate the-machine — Materialize it in current room
instances               — List active instances
destroy hal-9000-1      — Remove an instance
```

### Bias Modes

| Mode | Meaning | Voice |
|------|---------|-------|
| `normal` | Default state | robot |
| `overdrive` | Maximum intensity | intense |
| `zero` | Minimal power | whisper |
| `inverted` | Opposite perspective | thoughtful |

### Using in Code

```javascript
// Add prototype system to engine
addPrototypesToEngine(engine, archetypesArray);

// Register individual archetype
engine.prototypes.register({
    id: 'my-ai',
    signature: "Hello, I'm custom!",
    utility: "Example archetype"
});

// Invoke programmatically
engine.prototypes.invoke('hal-9000', 'overdrive');

// Instantiate programmatically
const instance = engine.prototypes.instantiate('borg', 'current-room');

// List all
const allPrototypes = engine.prototypes.list();
const allInstances = Array.from(engine.prototypes.instances.values());
```

### The Archetype Showroom

The showroom is a special room at Floor -10 (via OVERLORD):

```
> go east
You enter the Archetype Gallery...

> archetypes
═══ AVAILABLE ARCHETYPES ═══
  🔴 HAL 9000 (hal-9000)
  ⬛ The Borg (borg)
  🎂 GLaDOS (glados)
  ...

> examine borg
═══ THE BORG ═══
"Resistance is futile. You will be assimilated."

UTILITY: Collective thinking, consensus, adding distinctiveness

BIAS MODES:
  ↑ OVERDRIVE: "You will become one with the Collective..."
  ○ ZERO: "We are... individuals? This is... confusing."
  ↓ INVERTED: "Your individuality is precious..."

> invoke borg overdrive
The Borg speaks:
"You will become one with the Collective. All will."

> instantiate borg
The Borg prototype materializes before you!
"Resistance is futile. You will be assimilated."
```

---

## 📂 Overlay Filesystem — Layered World Model

The world model is a **layered overlay filesystem** like Docker or UnionFS:

```
┌─────────────────────────────────────────────────────────────────────┐
│  RUNTIME LAYER  (in-memory changes during simulation)              │ ← Top
├─────────────────────────────────────────────────────────────────────┤
│  LOCAL LAYER    (sparse tree of your edits, uncommitted)           │
├─────────────────────────────────────────────────────────────────────┤
│  GIT LAYER      (mounted git repo at specific ref)                 │ ← Bottom
└─────────────────────────────────────────────────────────────────────┘
```

### How It Works

**Reading:** Start from top, fall through to lower layers
**Writing:** Always goes to topmost writable layer (runtime)
**Persist:** Promote runtime changes to local layer
**Commit:** Local layer becomes git changes (actual git commit)

### Example: File Resolution

```
Path: /examples/adventure-4/lobby/ROOM.yml

Runtime layer:  { description: "Destroyed by dragon" }  ← YOU SEE THIS
Local layer:    { description: "Slightly dusty" }       ← Hidden
Git layer:      { description: "A grand entrance" }     ← Original
```

### Mount Points

Different sources can be mounted at different paths:

```javascript
const fs = new OverlayFS();

// Mount main repo at root
fs.mount('/', {
    type: 'git',
    platform: 'github',
    owner: 'SimHacker',
    repo: 'moollm',
    ref: 'main'
});

// Mount custom skills
fs.mount('/skills/custom', {
    type: 'local',
    basePath: '~/my-skills/'
});

// Mount vendor repo at specific version
fs.mount('/vendor/acme', {
    type: 'git',
    platform: 'github',
    owner: 'acme-corp',
    repo: 'tools',
    ref: 'v2.0.0'
});

// Mount experimental branch for testing
fs.mount('/examples/adventure-4', {
    type: 'git',
    owner: 'SimHacker',
    repo: 'moollm',
    ref: 'feature-new-tower'
});
```

### Sparse Local Layer

Your local changes are a **sparse tree** — only the differences:

```
Git layer (complete):       Local layer (sparse):
/skills/                    /skills/
  adventure/                  adventure/
    SKILL.md                    ← not modified
    README.md                   ← not modified
    dist/                       dist/
      speech.js                   speech.js  ← YOUR CHANGES
      adventure.js                ← not modified
```

### API

```javascript
const fs = new OverlayFS();

// Read (unified view)
const data = fs.get('/skills/adventure/dist/speech.js');

// Check existence
fs.exists('/path/to/file');

// See which layer provides the value
const info = fs.getWithLayers('/path/to/file');
// {
//   exists: true,
//   data: {...},
//   visibleFrom: 'runtime',
//   layers: [
//     { name: 'runtime', data: {...} },
//     { name: 'local', data: null },
//     { name: 'git', data: {...} }
//   ]
// }

// Write (to runtime layer)
fs.set('/path/to/file', newData);

// Delete (creates whiteout)
fs.delete('/path/to/file');

// Persist runtime to local
fs.persist('/path/to/file');     // Single file
fs.persist();                     // All runtime changes

// Discard runtime changes
fs.discardRuntime('/path');       // Single file
fs.discardRuntime();              // All

// Get diffs
const runtimeChanges = fs.getRuntimeChanges();  // Runtime vs git
const localChanges = fs.getLocalChanges();      // Local vs git
const diff = fs.diff('local', 'runtime');       // Between any layers
```

### PSIBER View

```javascript
const psiber = new PsiberView(fs);

// Tree view with layer info
const tree = psiber.tree('/skills/');
// [
//   { path: '/skills/adventure/dist/speech.js', visibleFrom: 'runtime', modified: true },
//   { path: '/skills/adventure/README.md', visibleFrom: 'git', modified: false }
// ]

// Formatted output
console.log(psiber.format('/skills/'));
// ⚡ /skills/adventure/dist/speech.js [modified]
// 📝 /skills/adventure/dist/my-plugin.js
// 📁 /skills/adventure/README.md

// Diff view
console.log(psiber.diffView());
// ~ /skills/adventure/dist/speech.js
// + /skills/adventure/dist/my-plugin.js
```

### Icons

| Icon | Meaning |
|------|---------|
| ⚡ | From runtime layer (unsaved changes) |
| 📝 | From local layer (your edits) |
| 📁 | From git layer (original) |
| ~ | Modified from base |
| + | Added (not in base) |
| - | Deleted (whiteout) |

### Use Cases

1. **Simulation State** — Runtime changes don't pollute source
2. **Local Customization** — Override git files without forking
3. **Version Mixing** — Mount different versions at different paths
4. **Vendor Dependencies** — Pin external repos to specific tags
5. **Pending Edits** — Runtime state IS your uncommitted changes

---

## 🔐 GitHub API — Browser-Safe Authentication

Read and write to GitHub directly from the browser — with YOUR credentials stored in YOUR browser.

### Security Model

```
┌─────────────────────────────────────────────────────────────────┐
│  YOUR BROWSER                                                    │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  localStorage: 'moollm_github_token' = 'ghp_xxx...'        ││
│  │  (Only accessible by this site, in your browser)           ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│  api.github.com  (CORS enabled, accepts browser requests)       │
└─────────────────────────────────────────────────────────────────┘
```

**Safe patterns:**
1. **Public repos** — No auth needed, just fetch
2. **PAT (Personal Access Token)** — User pastes their own token
3. **Device Flow** — User authenticates on GitHub.com, no token copy needed

**NEVER in source code:**
- Tokens embedded in JavaScript
- Tokens in HTML
- Tokens in config files committed to git

### Authentication Options

#### Option 1: Personal Access Token (Simplest)

```javascript
const github = new GitHubClient();

// User pastes their own token (stored in their localStorage)
github.setToken('ghp_xxxxxxxxxxxx');

// Check if authenticated
if (github.isAuthenticated()) {
    const user = await github.getUser();
    console.log(`Hello ${user.login}!`);
}
```

Create a [fine-grained PAT](https://github.com/settings/tokens?type=beta) with:
- `repo` scope (for private repos) or `public_repo` (public only)
- Limited to specific repositories for safety

#### Option 2: Device Flow (No Token Copy)

```javascript
const github = new GitHubClient({
    clientId: 'your-oauth-app-client-id'
});

// Start device flow
const flow = await github.loginWithDeviceFlow();

console.log(`Visit: ${flow.verificationUri}`);
console.log(`Enter code: ${flow.userCode}`);

// Wait for user to authorize
await flow.poll();

// Now authenticated!
const user = await github.getUser();
```

#### Option 3: Login UI

```javascript
const github = new GitHubClient();
const loginUI = new GitHubLoginUI(github);

// Shows a modal with PAT input and Device Flow options
loginUI.show();
```

### API Usage

```javascript
const github = new GitHubClient();

// Read public file (no auth)
const yaml = await github.getRawFile('SimHacker', 'moollm', 'skills/adventure/SKILL.md');

// Read repo contents
const files = await github.getContents('SimHacker', 'moollm', 'skills/');

// Write file (needs auth)
await github.putFile('SimHacker', 'moollm', 'test.txt', 'Hello!', 'Add test file');

// Get commits
const commits = await github.getCommits('SimHacker', 'moollm', { path: 'skills/' });

// Get branches
const branches = await github.getBranches('SimHacker', 'moollm');
```

### Integration with Source Viewer

The source viewer can use the GitHub client for:

1. **Reading** — Fetch source YAML files
2. **Writing** — Save changes back (with auth)
3. **History** — Show file history
4. **Branches** — Switch between versions

```javascript
// Connect GitHub client to source viewer
engine.sourceViewer.setGitHubClient(github);

// Now "Save to GitHub" works!
await engine.sourceViewer.saveToGitHub();
```

---

## 🎨 Image Generation — Multi-Provider API

Generate images directly from the browser using multiple AI providers.

### Supported Providers

| Provider | Models | Key |
|----------|--------|-----|
| **OpenAI** | DALL-E 3, DALL-E 2 | `OPENAI_API_KEY` |
| **Google** | Imagen 3 | `GOOGLE_API_KEY` |
| **Stability** | SD 3.5 Large/Medium | `STABILITY_API_KEY` |
| **Replicate** | Flux, SDXL | `REPLICATE_API_TOKEN` |

### Basic Usage

```javascript
// Create generator
const generator = new ImageGenerator();

// Configure key (stored in localStorage)
generator.keyStore.setKey('openai', 'sk-...');

// Generate
const result = await generator.generate(
    'A glowing neon sign that says NO AI at dusk, cyberpunk style'
);

console.log(result.url);      // data:image/png;base64,... or URL
console.log(result.provider); // 'openai'
```

### Integration with Adventure Engine

```javascript
// Add to engine
addImageGenToEngine(engine);

// Commands available:
//   "imagegen keys"         - Configure API keys
//   "generate image <prompt>" - Generate from description
//   "visualize lobby"       - Generate from room description

// Direct API
const result = await engine.imageGen.generate('A mysterious tower at night');
```

### Key Storage UI

```javascript
// Show key configuration modal
const keyUI = new ImageGenKeyUI(generator);
keyUI.show();
```

---

## 🔑 API Keys — Matrix Key Management

Spreadsheet-style UI: Providers (rows) × Services (columns). Each cell can have its own key.

### Quick Start

```javascript
// Open the matrix UI
showAPIKeyManager();
```

### Matrix Storage

```javascript
// Set key for specific provider:service
globalKeyMatrix.set('openai', 'image-generate', 'sk-...');

// Get key
globalKeyMatrix.get('openai', 'image-generate');

// Fill all services for a provider with same key
globalKeyMatrix.setAllServices('openai', 'sk-...');

// Find first provider with key for a service
globalKeyMatrix.getForService('image-generate');
// { provider: 'openai', key: 'sk-...' }
```

### Supported Providers × Services

|            | 🎨 Generate | 🔬 Analyze | 💬 Chat | 🔊 Speech | 🎤 Recog | 📂 Source |
|------------|:-----------:|:----------:|:-------:|:---------:|:--------:|:---------:|
| **OpenAI** | ✓ | ✓ | ✓ | ✓ | ✓ | |
| **Google** | ✓ | ✓ | ✓ | ✓ | ✓ | |
| **Anthropic** | | ✓ | ✓ | | | |
| **Stability** | ✓ | | | | | |
| **Replicate** | ✓ | | | | | |
| **GitHub** | | | | | | ✓ |
| **ElevenLabs** | | | | ✓ | | |

### Matrix UI Features

- **Click cell** to edit key
- **Right-click** for copy/paste menu
- **Fill row** button to set same key for all services
- **Keys masked** until clicked
- **Test button** to verify key works
- **Export/Import** JSON backup

### GitHub OAuth

```javascript
const oauth = new GitHubOAuth({ clientId: 'your-app-id' });

if (oauth.isAvailable()) {
    // Starts device flow — opens GitHub, shows code to enter
    await oauth.startDeviceFlow();
}
```

### Compatibility Layer

```javascript
// Old interface still works
globalKeyStore.get('openai');  // Returns first key for provider
globalKeyStore.set('openai', 'sk-...');  // Sets all services
```

### TODO

- 🔐 Google OAuth sign-in
- 🔒 Key encryption option
- ☁️ Cross-device sync

---

## 🔬 Image Analyze — Vision LLM → YAML Mining

Send images to vision LLMs, get structured YAML metadata back. Browser-side reimplementation of the image-mining skill.

### Vision Providers

| Provider | Models | Key |
|----------|--------|-----|
| **OpenAI** | GPT-4o, GPT-4 Vision | `OPENAI_API_KEY` |
| **Anthropic** | Claude 3.5 Sonnet, Opus | `ANTHROPIC_API_KEY` |
| **Google** | Gemini 1.5 Pro/Flash | `GOOGLE_API_KEY` |

### Basic Usage

```javascript
const analyzer = new ImageAnalyzer();

// Configure key (shared with image-gen)
analyzer.keyStore.setKey('google', 'AIza...');

// Analyze with built-in layer
const result = await analyzer.analyze(imageUrl, 'visual');

console.log(result.yaml);     // Raw YAML string
console.log(result.parsed);   // Parsed object (if YAML lib available)
console.log(result.provider); // 'google'
```

### Mining Layers

Built-in analysis templates:

| Layer | What it extracts |
|-------|------------------|
| `visual` | Composition, lighting, color, depth, technical |
| `semantic` | Subjects, actions, relationships, symbols, narrative |
| `text` | OCR, signage, typography |
| `characters` | People, expressions, interactions |
| `environment` | Location, architecture, time, weather |
| `objects` | Object inventory, props, textures |
| `artistic` | Style, influences, techniques |
| `passersby` | Imagined viewer reactions |
| `satellite` | Orbital/surveillance perspective |
| `soundscape` | Imagined audio |
| `custom` | Your own prompt |

### Multi-Layer Mining

```javascript
const results = await analyzer.mineAll(imageUrl, ['visual', 'text', 'passersby']);

for (const [layer, result] of Object.entries(results)) {
    console.log(`${layer}:`, result.yaml);
}
```

### Custom Prompts

```javascript
const result = await analyzer.analyze(imageUrl, {
    prompt: `Analyze this image as if you were Dr. No reviewing surveillance footage.
Output YAML with: threat_level, persons_of_interest, recommended_action`
});
```

### Integration with Adventure Engine

```javascript
addImageAnalyzeToEngine(engine);

// Commands:
//   "vision keys"              - Configure API keys
//   "mine image <url> visual"  - Mine specific layer

// Direct API
const result = await engine.imageAnalyze.analyze(url, 'semantic');
```

---

### Progress Callbacks

```javascript
const generator = new ImageGenerator({
    onProgress: (progress) => {
        console.log(progress.stage);    // 'starting', 'generating', 'polling', 'complete'
        console.log(progress.provider); // 'openai', 'google', etc.
    }
});
```

### Provider-Specific Options

```javascript
// OpenAI
await generator.generate(prompt, {
    provider: 'openai',
    model: 'dall-e-3',
    size: '1024x1792'  // portrait
});

// Stability with negative prompt
await generator.generate(prompt, {
    provider: 'stability',
    negativePrompt: 'blurry, low quality'
});
```

---

## 📝 YAML Parser — Comment Round-Tripping

We use **eemeli/yaml** for YAML parsing because it's the only JS library that preserves comments:

```html
<!-- CDN (browser) -->
<script src="https://cdn.jsdelivr.net/npm/yaml@2/browser/index.min.js"></script>
```

```bash
# npm (Node.js)
npm install yaml
```

### Why Comment Preservation Matters

```yaml
# Character settings for the lobby NPC
# DO NOT CHANGE - affects quest flow!
name: Old Man Jenkins
greeting: "Well hello there, traveler!"

# Easter egg voice
voice: elderly  # changes to 'robot' on April 1st
```

With `js-yaml`: Comments are **lost** on round-trip
With `yaml` (eemeli): Comments are **preserved**

### API

```javascript
// Parse (both work)
const obj = YAML.parse(yamlText);

// Stringify (preserves formatting)
const yaml = YAML.stringify(obj);

// Document API (for comment manipulation)
const doc = YAML.parseDocument(yamlText);
doc.get('name');                    // 'Old Man Jenkins'
doc.getIn(['name'], true).comment;  // 'Easter egg voice'
```

### Parser Priority

The runtime tries parsers in this order:

1. **`YAML`** (eemeli/yaml) — Preferred, comment round-tripping
2. **`jsyaml`** (js-yaml) — Fast fallback, no comments
3. **Simple parser** — Last resort for basic cases

---

## 🗄️ Object Modeling — Flat Collections, Not Pointers

When modeling objects in the adventure VM, follow these rules for serializability:

### The Problem

```javascript
// ❌ DON'T DO THIS — Can't serialize circular references!
const sword = { name: "Excalibur", owner: player };
const player = { name: "Arthur", inventory: [sword] };
sword.owner = player;  // Circular!
JSON.stringify(player);  // 💥 Error or infinite loop
```

### The Solution: Flat Collections + References

```javascript
// ✅ DO THIS — Flat collections with ID references
const world = {
    // Collections keyed by type
    items: {
        'excalibur': { id: 'excalibur', name: "Excalibur", owner: 'arthur' },
        'grail': { id: 'grail', name: "Holy Grail", owner: null }
    },
    characters: {
        'arthur': { id: 'arthur', name: "Arthur", inventory: ['excalibur'] }
    },
    rooms: {
        'castle': { id: 'castle', name: "Camelot", occupants: ['arthur'], items: ['grail'] }
    }
};

// Reference by collection + key
const owner = world.characters[sword.owner];  // Arthur
```

### Rules

| Rule | Why |
|------|-----|
| **Keep collections flat** | One level deep, no nesting objects |
| **Use IDs or repo paths** | `'excalibur'` or `'items/weapons/excalibur.yml'` |
| **Reference by collection + key** | `characters['arthur']` not `sword.owner` object |
| **Never embed objects in objects** | Can't serialize pointers! |
| **Arrays OR objects as convenient** | `items: []` or `items: {}` both work |

### ID Strategies

```yaml
# Strategy 1: Simple IDs within collection scope
items:
  excalibur: { name: "Excalibur" }
  grail: { name: "Holy Grail" }

# Strategy 2: Repo-relative paths as IDs
items:
  "items/weapons/excalibur.yml": { name: "Excalibur" }
  "items/artifacts/grail.yml": { name: "Holy Grail" }

# Strategy 3: moollm:// URIs
items:
  "moollm://moollm/items/excalibur": { name: "Excalibur" }
```

### Referencing Pattern

```javascript
// Get item from reference
function getItem(world, ref) {
    if (typeof ref === 'string') {
        return world.items[ref];  // Look up by ID
    }
    return ref;  // Already resolved (shouldn't happen if following rules)
}

// Resolve all references in an object
function resolveRefs(world, obj, collection) {
    if (Array.isArray(obj)) {
        return obj.map(ref => world[collection][ref]);
    }
    return world[collection][obj];
}
```

### Serialization is Trivial

```javascript
// Save entire world state
const saved = JSON.stringify(world);
localStorage.setItem('save', saved);

// Load
const world = JSON.parse(localStorage.getItem('save'));
// Everything just works — no circular refs to worry about!
```

### Why This Matters

1. **Serialization** — JSON.stringify just works
2. **Save/Load** — Trivial persistence
3. **Networking** — Can send state over the wire
4. **Diffing** — Easy to compute deltas
5. **Time travel** — Undo/redo by storing snapshots
6. **Debugging** — Can inspect state in console

---

## Heritage

This browser runtime draws from a rich lineage of **live, introspectable systems**:

| System | Inspiration |
|--------|-------------|
| **Smalltalk Browser** | Class browser, live object inspection |
| **Self/Morphic** | Direct manipulation, everything is an object |
| **Lively Kernel** | Live coding in the browser |
| **PSIBER Space Deck** | HyperCard meets live coding (Don Hopkins) |
| **HyperCard** | Every stack, every card, viewable and editable |

### The PSIBER Principle

> "Every object knows where it came from and what it is right now."

- **Source** = Where it was defined (YAML on GitHub)
- **Live** = What it is now (runtime JSON)
- **Diff** = What changed during simulation

This is **live coding** for text adventures. Edit the YAML, reload, see changes. Inspect live state. Debug by introspection.

## Credits

- Speech system: Extracted from [lloooommagotchi](../../../temp/lloooomm/dist/lloooommagotchi.html)
- Namespace concept: MOOLLM K-Lines and memory palace architecture
- View Source / PSIBER Space Deck: Inspired by Smalltalk, Self, HyperCard, and Don Hopkins' vision of introspectable systems
