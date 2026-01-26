# Adventure Engine V2 Architecture

```
███╗   ███╗ ██████╗  ██████╗ ████████╗ █████╗ ██╗     
████╗ ████║██╔═══██╗██╔═══██╗╚══██╔══╝██╔══██╗██║     
██╔████╔██║██║   ██║██║   ██║   ██║   ███████║██║     
██║╚██╔╝██║██║   ██║██║   ██║   ██║   ██╔══██║██║     
██║ ╚═╝ ██║╚██████╔╝╚██████╔╝   ██║   ██║  ██║███████╗
╚═╝     ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚══════╝
                                                       
██████╗ ██╗███████╗████████╗ ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗
██╔══██╗██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║
██║  ██║██║███████╗   ██║   ██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║
██║  ██║██║╚════██║   ██║   ██║   ██║██╔══██╗   ██║   ██║██║   ██║██║╚██╗██║
██████╔╝██║███████║   ██║   ╚██████╔╝██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║
╚═════╝ ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
```

> **Heritage**: MOO + MYST + Total Distortion = **MOOTAL DISTORTION**
> 
> *"You're a video producer in a parallel dimension. Find cameras. Win guitar battles. Capture TRUTH."*

---

> **Principle**: Static engine, dynamic data. Same JS every time, replace JSON blob.

## Directory Structure

```
skills/adventure/
├── engine/                    # STATIC — never changes per world
│   ├── engine.js             # Core runtime
│   ├── engine.css            # UI styles
│   ├── pie-menu.js           # Radial menu component
│   ├── drag-drop.js          # Drag/drop handling
│   ├── index.html            # Shell that loads JSON files
│   └── README.md             # Engine dev docs
│
├── compiler/                  # YAML → JSON compiler
│   └── compile.py            # Outputs world.json + characters.json
│
└── examples/
    └── adventure-4/
        └── build/
            ├── world.json       # Rooms, objects, exits, resources
            ├── characters.json  # NPCs, player characters
            └── presets.json     # Photographers, cameras, styles (optional)
```

## Data File Separation

| File | Contains | Changes When |
|------|----------|--------------|
| `world.json` | Rooms, objects, exits, prototypes, actions, menus | World geography/items change |
| `characters.json` | NPCs, player roster, dialog trees | Characters change |
| `presets.json` | Photographers, cameras, film, styles | Visualizer presets change |

**Why separate?**
- Plug same characters into different worlds
- Swap character packs (party, NPCs, test bots)
- Share character libraries across adventures
- Test world with minimal character set
- Presets are reusable across all adventures

### world.json (rooms, objects, actions)

```json
{
  "_meta": { "type": "world", "version": "2.0.0" },
  "config": { "starting_room": "room/lobby" },
  "registry": {
    "room/lobby": { "type": "room", "name": "The Lobby", ... },
    "room/pub": { "type": "room", "name": "The Pub", ... },
    "object/lamp": { "type": "object", "name": "Brass Lamp", ... },
    "action/take": { "type": "action", "code": "(world, subject) => {...}" },
    "menu/object_on_object": { "type": "menu", "actions": [...] },
    "prototype/container": { "type": "prototype", ... }
  }
}
```

### characters.json (NPCs, players)

```json
{
  "_meta": { "type": "characters", "version": "2.0.0" },
  "registry": {
    "character/bartender": { 
      "type": "character", 
      "name": "Marieke",
      "location": "room/pub",
      "dialog": "What'll it be, stranger?"
    },
    "character/ada-ii": {
      "type": "character",
      "name": "Ada II",
      "location": "room/lobby"
    },
    "character/player": {
      "type": "character",
      "name": "You",
      "is_player": true
    }
  }
}
```

### presets.json (visualizer config)

```json
{
  "_meta": { "type": "presets", "version": "2.0.0" },
  "registry": {
    "photographer/annie-leibovitz": { "type": "photographer", ... },
    "photographer/ansel-adams": { "type": "photographer", ... },
    "camera/minox-spy": { "type": "camera", ... },
    "camera/holga-120": { "type": "camera", ... },
    "film/portra-400": { "type": "film", ... },
    "style/jennell-jaquays-tribute": { "type": "style", ... }
  }
}
```

## Separation of Concerns

| Concern | Where | Changes When |
|---------|-------|--------------|
| Engine code | `engine/*.js` | Engine features change |
| World data | `world.json` | World content changes |
| Styling | `engine.css` | Look & feel changes |
| Compilation | `compile.py` | Export format changes |

**Engine dev**: Touch `engine/`
**World dev**: Edit YAML, run compiler, get new `world.json`

---

## world.json Schema

### Flat Registry Pattern

All objects live in ONE flat table, keyed by `type/id`:

```
type/id                         → object
────────────────────────────────────────────
room/lobby                      → { name: "The Lobby", ... }
room/pub/back-room              → { name: "Back Room", ... }
object/lamp                     → { name: "Brass Lamp", ... }
object/key                      → { name: "Rusty Key", ... }
character/bartender             → { name: "Marieke", ... }
character/ada-ii                → { name: "Ada II", ... }
photographer/annie-leibovitz    → { style: "intimate portraits", ... }
style/jennell-jaquays-tribute   → { periods: [...], ... }
camera/minox-spy                → { effects: [...], ... }
film/portra-400                 → { color_science: "warm", ... }
action/take                     → "(world, subject) => { ... }"
action/use_on                   → "(world, subject, object) => { ... }"
prototype/container             → { actions: ["open", "close"], ... }
menu/object_on_object           → { actions: ["use_on", "combine"], ... }
```

### Directory = Object

A `type/id` typically maps to a **directory**. The compiler:
1. Finds the directory
2. Parses all YAML files within
3. Inlines sub-objects into one JSON blob

```
Source Directory                    → Registry Entry
────────────────────────────────────────────────────────────────
pub/                                → room/pub (ROOM.yml + contents)
  ├── ROOM.yml                         name, description, exits
  ├── objects/                         inlined into room.objects
  │   ├── dartboard.yml
  │   └── jukebox.yml
  └── npcs/                            inlined into room.npcs  
      └── regular.yml

characters/bartender/               → character/bartender
  ├── CHARACTER.yml                    name, traits, location
  └── dialog.yml                       inlined into character.dialog
```

### Sub-object References with `#`

Point into compiled objects to get subtrees:

```
room/pub#exits                  → { north: "room/street", ... }
room/pub#objects                → [{ id: "object/dartboard", ... }, ...]
character/bartender#dialog      → { greeting: "What'll it be?", ... }
camera/minox-spy#effects        → ["high contrast", "visible grain", ...]
style/jaquays#periods           → { "judges-guild": {...}, "chaosium": {...} }
```

### Full Schema

```json
{
  "_meta": {
    "version": "2.0.0",
    "compiled_at": "2026-01-25T19:30:00Z",
    "source": "examples/adventure-4"
  },
  
  "_types": {
    "_doc": "Registry of known types for validation/UI",
    "room": { "icon": "🚪", "plural": "rooms" },
    "object": { "icon": "✨", "plural": "objects" },
    "character": { "icon": "👤", "plural": "characters" },
    "photographer": { "icon": "📷", "plural": "photographers" },
    "style": { "icon": "🎨", "plural": "styles" },
    "camera": { "icon": "📸", "plural": "cameras" },
    "film": { "icon": "🎞️", "plural": "film stocks" },
    "composition": { "icon": "🖼️", "plural": "compositions" },
    "action": { "icon": "⚡", "plural": "actions" },
    "prototype": { "icon": "🧬", "plural": "prototypes" },
    "menu": { "icon": "🥧", "plural": "menus" }
  },
  
  "config": {
    "starting_room": "room/lobby",
    "player": {
      "location": "room/lobby",
      "inventory": [],
      "character": "character/player"
    },
    "features": {
      "pie_menus": true,
      "drag_drop": true,
      "speech": false,
      "images": false
    }
  },
  
  "registry": {
    "_doc": "Flat object table: type/id → object",
    
    "room/lobby": {
      "type": "room",
      "id": "room/lobby",
      "name": "The Lobby",
      "description": "A grand entrance hall.",
      "exits": { 
        "north": "room/hallway", 
        "east": "room/office" 
      },
      "contents": ["object/lamp", "object/key"]
    },
    
    "room/pub/back-room": {
      "type": "room",
      "id": "room/pub/back-room",
      "name": "Back Room",
      "description": "A dingy back room behind the pub.",
      "exits": { "west": "room/pub" },
      "contents": []
    },
    
    "object/lamp": {
      "type": "object",
      "id": "object/lamp",
      "name": "Brass Lamp",
      "description": "An old brass lamp, tarnished with age.",
      "portable": true,
      "prototype": "prototype/light_source",
      "actions": ["action/take", "action/examine", "action/rub"]
    },
    
    "object/key": {
      "type": "object",
      "id": "object/key",
      "name": "Rusty Key",
      "portable": true,
      "actions": ["action/take", "action/examine", "action/use_on"]
    },
    
    "character/bartender": {
      "type": "character",
      "id": "character/bartender",
      "name": "Marieke",
      "location": "room/pub",
      "dialog": "What'll it be, stranger?"
    },
    
    "photographer/annie-leibovitz": {
      "type": "photographer",
      "id": "photographer/annie-leibovitz",
      "name": "Annie Leibovitz",
      "style": "Intimate celebrity portraits with dramatic staging",
      "signature": "Direct eye contact, environmental context, theatrical lighting",
      "prompt_modifiers": ["intimate portrait", "dramatic staging", "celebrity essence"]
    },
    
    "style/jennell-jaquays-tribute": {
      "type": "style",
      "id": "style/jennell-jaquays-tribute",
      "name": "Jennell Jaquays Tribute",
      "artist": { "name": "Jennell Jaquays", "years": "1956-2024" },
      "periods": {
        "judges-guild": { "years": "1976-1982", "characteristics": ["pen and ink", "dense crosshatching"] },
        "chaosium": { "years": "1982-1988", "characteristics": ["mythic scope", "runic borders"] }
      },
      "attribution_required": true
    },
    
    "camera/minox-spy": {
      "type": "camera",
      "id": "camera/minox-spy",
      "name": "Minox Subminiature",
      "era": "Cold War espionage",
      "effects": ["high contrast", "visible grain", "stolen moment quality"],
      "prompt_modifiers": ["spy camera aesthetic", "covert photography", "grainy surveillance"]
    },
    
    "film/portra-400": {
      "type": "film",
      "id": "film/portra-400",
      "name": "Kodak Portra 400",
      "color_science": "Warm skin tones, natural colors",
      "grain": "Fine, organic",
      "prompt_modifiers": ["Portra 400 film look", "warm skin tones", "natural color palette"]
    },
    
    "action/take": {
      "type": "action",
      "id": "action/take",
      "name": "Take",
      "code": "(world, subject) => { const obj = world.get(subject); if (!obj.portable) return `You can't take the ${obj.name}.`; world.player.inventory.push(subject); world.removeFromRoom(subject); return `You take the ${obj.name}.`; }"
    },
    
    "action/examine": {
      "type": "action",
      "id": "action/examine",
      "name": "Examine",
      "code": "(world, subject) => { const obj = world.get(subject); return obj.description || `It's a ${obj.name}.`; }"
    },
    
    "action/use_on": {
      "type": "action",
      "id": "action/use_on",
      "name": "Use On",
      "code": "(world, subject, object) => { const s = world.get(subject); const o = world.get(object); if (subject === 'object/key' && object === 'object/door') { world.setFlag('door_unlocked', true); return 'The door clicks open!'; } return `You can't use the ${s.name} on the ${o.name}.`; }"
    },
    
    "action/give": {
      "type": "action",
      "id": "action/give",
      "name": "Give",
      "code": "(world, subject, object) => { const s = world.get(subject); const o = world.get(object); if (o.type !== 'character') return 'You can only give things to people.'; return `${o.name} says: \"Thanks for the ${s.name}!\"`; }"
    },
    
    "prototype/container": {
      "type": "prototype",
      "id": "prototype/container",
      "name": "Container",
      "properties": { "is_open": false, "contents": [] },
      "actions": ["action/open", "action/close", "action/look_in"]
    },
    
    "prototype/light_source": {
      "type": "prototype",
      "id": "prototype/light_source",
      "name": "Light Source",
      "properties": { "is_lit": false },
      "actions": ["action/turn_on", "action/turn_off"]
    },
    
    "menu/self": {
      "type": "menu",
      "id": "menu/self",
      "name": "Self Actions",
      "context": "Click on object in inventory",
      "actions": ["action/examine", "action/drop", "action/use"]
    },
    
    "menu/object_on_object": {
      "type": "menu",
      "id": "menu/object_on_object",
      "name": "Object on Object",
      "context": "Drag object onto another object",
      "actions": ["action/use_on", "action/combine", "action/compare"]
    },
    
    "menu/object_on_character": {
      "type": "menu",
      "id": "menu/object_on_character",
      "name": "Object on Character",
      "context": "Drag object onto character",
      "actions": ["action/give", "action/show", "action/throw_at"]
    }
  }
}
```

---

## Engine API

```javascript
// engine.js exports

class AdventureEngine {
  constructor(worldData, charactersData = {}, presetsData = {}) {
    this.registry = {};  // Flat object table
    this.config = worldData.config;
    this.types = worldData._types;
    this.actions = {};  // Compiled action closures
    
    // Merge registries: world + characters + presets
    Object.assign(this.registry, worldData.registry || {});
    Object.assign(this.registry, charactersData.registry || {});
    Object.assign(this.registry, presetsData.registry || {});
    
    // Or if passed as merged single object
    if (worldData.characters) {
      Object.assign(this.registry, worldData.characters);
    }
    if (worldData.presets) {
      Object.assign(this.registry, worldData.presets);
    }
    
    // Compile all action/* entries
    this.compileActions();
  }
  
  // Get object by type/id reference
  get(ref) {
    // Handle sub-object: "character/bartender#dialog"
    const [path, subkey] = ref.split('#');
    const obj = this.registry[path];
    if (!obj) return null;
    if (subkey) return obj[subkey];
    return obj;
  }
  
  // Get all objects of a type
  getByType(type) {
    return Object.entries(this.registry)
      .filter(([key]) => key.startsWith(`${type}/`))
      .map(([key, obj]) => obj);
  }
  
  // Compile action code strings into closures
  compileActions() {
    for (const [key, obj] of Object.entries(this.registry)) {
      if (key.startsWith('action/') && obj.code) {
        this.actions[key] = eval(obj.code);
      }
    }
  }
  
  // Execute action by reference
  do(actionRef, subjectRef, objectRef = null) {
    const action = this.actions[actionRef];
    if (!action) return `Unknown action: ${actionRef}`;
    return action(this, subjectRef, objectRef);
  }
  
  // Get pie menu for drag context
  getPieMenu(contextType, subjectRef, objectRef = null) {
    const menu = this.get(`menu/${contextType}`);
    if (!menu) return [];
    
    const subject = this.get(subjectRef);
    const object = objectRef ? this.get(objectRef) : null;
    
    // Filter to valid actions for this combo
    return menu.actions.filter(actionRef => {
      // Check if subject supports this action
      if (subject.actions && !subject.actions.includes(actionRef)) {
        return false;
      }
      return true;
    });
  }
  
  // Drag handler — detect context, return menu
  onDrag(subjectRef, targetRef) {
    const target = this.get(targetRef);
    if (!target) return [];
    
    const contextMap = {
      'character': 'object_on_character',
      'object': 'object_on_object',
      'room': 'object_on_room'
    };
    
    const context = contextMap[target.type];
    return context ? this.getPieMenu(context, subjectRef, targetRef) : [];
  }
  
  // State helpers
  get player() { return this.config.player; }
  get room() { return this.get(this.player.location); }
  
  setFlag(name, value) {
    this.config.flags = this.config.flags || {};
    this.config.flags[name] = value;
  }
  
  getFlag(name) {
    return this.config.flags?.[name];
  }
  
  removeFromRoom(objRef) {
    const room = this.room;
    const idx = room.contents.indexOf(objRef);
    if (idx >= 0) room.contents.splice(idx, 1);
  }
  
  addToRoom(objRef, roomRef = null) {
    const room = roomRef ? this.get(roomRef) : this.room;
    if (!room.contents.includes(objRef)) {
      room.contents.push(objRef);
    }
  }
}

// Usage:
// engine.get('room/lobby')
// engine.get('character/bartender#dialog')
// engine.getByType('photographer')  // for menu population
// engine.do('action/take', 'object/lamp')
// engine.do('action/use_on', 'object/key', 'object/door')
```
```

---

## Pie Menu Interaction Flow

```
1. User drags "object/key" from inventory
2. User drops onto "object/door"
3. Engine calls: onDrag('object/key', 'object/door')
4. Engine detects target.type = 'object' → context = 'object_on_object'
5. Engine calls: getPieMenu('object_on_object', 'object/key', 'object/door')
6. Engine shows pie menu: [action/use_on, action/combine]
7. User clicks "Use On"
8. Engine calls: do('action/use_on', 'object/key', 'object/door')
9. Action closure executes, returns: "The door clicks open!"
10. World state updated: flags.door_unlocked = true
```

## Menu Population for UI

```javascript
// Populate photographer dropdown
const photographers = engine.getByType('photographer');
// → [{ id: 'photographer/annie-leibovitz', name: 'Annie Leibovitz', ... }, ...]

// Populate camera dropdown
const cameras = engine.getByType('camera');
// → [{ id: 'camera/minox-spy', name: 'Minox Subminiature', ... }, ...]

// Build visualizer config from selections
const visualizerConfig = {
  photographer: 'photographer/annie-leibovitz',
  camera: 'camera/minox-spy',
  film: 'film/portra-400',
  style: 'style/jennell-jaquays-tribute',
  composition: 'composition/portrait'
};

// Get full objects for prompt assembly
const photographerData = engine.get(visualizerConfig.photographer);
const cameraData = engine.get(visualizerConfig.camera);
// ... assemble prompt from modifiers
```

---

## Export Config

An export config specifies what to pull together from multiple sources:

### EXPORT.yml

```yaml
# EXPORT.yml — What to include in this build

export:
  id: pub-adventure
  name: "The Pub Adventure"
  version: "1.0.0"

# Rooms to include (from any adventure)
rooms:
  - from: examples/adventure-4
    include:
      - pub              # room/pub
      - pub/back-room    # room/pub/back-room
      - street           # room/street
      - street/alley     # room/street/alley
  
  - from: examples/shared-spaces
    include:
      - lobby            # reusable lobby

# Characters to include
characters:
  - from: examples/adventure-4/characters
    include:
      - bartender
      - ada-ii
      - drunk-regular
  
  - from: examples/character-library
    include:
      - player-default   # generic player character

# Presets for visualizer (photographers, cameras, etc)
presets:
  - from: skills/visualizer
    include:
      - photographers/annie-leibovitz
      - photographers/ansel-adams
      - cameras/minox-spy
      - cameras/holga-120
      - film/portra-400
      - film/tri-x
      - styles/jennell-jaquays-tribute

# Actions and prototypes
actions:
  - from: skills/adventure/actions
    include: "*"    # all standard actions

prototypes:
  - from: skills/adventure/prototypes
    include:
      - container
      - light_source
      - door

# Menus
menus:
  - from: skills/adventure/menus
    include: "*"    # all standard pie menus

# Config overrides
config:
  starting_room: room/pub
  features:
    pie_menus: true
    drag_drop: true
    speech: false
    images: false
```

### Glob Patterns

```yaml
rooms:
  - from: examples/adventure-4
    include:
      - "pub/**"        # pub and all sub-rooms
      - "street/*"      # street's direct children only
      - "*"             # all top-level rooms

characters:
  - from: examples/adventure-4/characters
    include: "*"        # all characters

presets:
  - from: skills/visualizer
    include:
      - "photographers/*"   # all photographers
      - "cameras/*"         # all cameras
```

### Multiple Adventures

```yaml
# Pull from multiple adventures into one build
rooms:
  - from: examples/adventure-4
    include: ["pub/**", "street"]
    
  - from: examples/adventure-5
    include: ["castle/**"]
    
  - from: examples/shared
    include: ["*"]
```

---

## Compilation Pipeline

```bash
# Compile from export config
python compile.py EXPORT.yml --output build/

# Creates:
#   build/world.json       (rooms, objects, actions, menus, prototypes)
#   build/characters.json  (characters)
#   build/presets.json     (photographers, cameras, film, styles)

# Or merged into one file:
python compile.py EXPORT.yml --output build/ --merged
#   build/game.json        (everything combined)
```

### Source Path → Registry Key Mapping

```
Source File                              → Registry Key
─────────────────────────────────────────────────────────────
lobby/ROOM.yml                           → room/lobby
pub/back-room/ROOM.yml                   → room/pub/back-room
characters/bartender/CHARACTER.yml       → character/bartender
objects/lamp.yml                         → object/lamp
archetypes/container.yml                 → prototype/container
actions/take.yml                         → action/take

# From visualizer skill (merged in)
photographers/annie-leibovitz.yml        → photographer/annie-leibovitz
cameras/minox-spy.yml                    → camera/minox-spy
film/portra-400.yml                      → film/portra-400
styles/jennell-jaquays-tribute.yml       → style/jennell-jaquays-tribute
```

### Compiler Steps

```python
# compile.py pseudocode

def compile(source_dir, output_file):
    registry = {}
    
    # 1. Walk source directory
    for path in walk_yaml_files(source_dir):
        obj = load_yaml(path)
        
        # 2. Derive registry key from path + file type
        key = path_to_registry_key(path, obj)
        
        # 3. Ensure object has type and id
        obj['type'] = key.split('/')[0]
        obj['id'] = key
        
        # 4. Store in flat registry
        registry[key] = obj
    
    # 5. Merge in visualizer presets (photographers, cameras, etc.)
    for preset_type in ['photographer', 'camera', 'film', 'style', 'composition']:
        merge_presets(registry, preset_type)
    
    # 6. Compile action code (keep as strings for eval)
    for key, obj in registry.items():
        if key.startswith('action/') and 'effect' in obj:
            obj['code'] = compile_effect_to_js(obj['effect'])
    
    # 7. Build world.json
    world = {
        '_meta': { 'compiled_at': now(), 'source': source_dir },
        '_types': TYPE_DEFINITIONS,
        'config': extract_config(registry),
        'registry': registry
    }
    
    write_json(output_file, world)
```

---

## index.html (Static Shell)

```html
<!DOCTYPE html>
<html>
<head>
  <title>Adventure</title>
  <link rel="stylesheet" href="engine.css">
</head>
<body>
  <div id="adventure"></div>
  
  <script src="engine.js"></script>
  <script src="pie-menu.js"></script>
  <script src="drag-drop.js"></script>
  
  <script>
    // Load world + characters + presets (parallel fetch)
    Promise.all([
      fetch('world.json').then(r => r.json()),
      fetch('characters.json').then(r => r.json()),
      fetch('presets.json').then(r => r.json()).catch(() => ({}))  // optional
    ]).then(([world, characters, presets]) => {
      window.engine = new AdventureEngine(world, characters, presets);
      engine.mount('#adventure');
      engine.start();
    });
  </script>
</body>
</html>
```

### Alternative: Single Merged File

For simpler deployment, compiler can merge all into one:

```bash
python compile.py examples/adventure-4/ --output build/ --merged
# Creates: build/game.json (world + characters + presets combined)
```

```html
<script>
  fetch('game.json')
    .then(r => r.json())
    .then(data => {
      window.engine = new AdventureEngine(data);
      engine.mount('#adventure');
      engine.start();
    });
</script>
```

---

## Benefits

1. **Fast iteration**: Edit YAML, recompile, refresh browser
2. **Testable engine**: Engine tests don't need world data
3. **Testable worlds**: World tests can use minimal engine stub
4. **Clear boundaries**: JS devs work on engine, content creators work on YAML
5. **Cacheable**: Engine files cached, only world.json changes
6. **Debuggable**: world.json is human-readable, inspect in browser

---

## Migration Path

1. **Phase 1**: Extract current engine.js to static file
2. **Phase 2**: Create compile.py that outputs world.json
3. **Phase 3**: Add pie-menu.js and drag-drop.js
4. **Phase 4**: Test with adventure-4 world
5. **Phase 5**: Stub out speech/images for later

---

## Cameras as World Objects

> **TOTAL DISTORTION VIBES** — Find cameras scattered through the world!

Cameras aren't just visualizer presets — they're **discoverable objects**:

```yaml
# In a room's objects/
object/spy-camera:
  type: object
  name: "Suspicious Camera"
  description: "A tiny Minox camera hidden behind a loose brick."
  portable: true
  prototype: prototype/camera
  camera_preset: camera/minox-spy    # Links to visualizer preset
  
object/polaroid-found:
  type: object
  name: "Dusty Polaroid"
  description: "An old Polaroid OneStep, still has film!"
  portable: true
  prototype: prototype/camera
  camera_preset: camera/polaroid-onestep
  film_remaining: 3
```

### Camera Prototype

```yaml
prototype/camera:
  type: prototype
  actions:
    - action/take_photo    # TAKE PHOTO OF <target>
    - action/examine
    - action/check_film
  properties:
    camera_preset: null    # Which visualizer camera
    film_remaining: -1     # -1 = unlimited (digital), N = limited shots
```

### Gameplay Loop

```
1. Player finds "Suspicious Camera" behind the bar
2. > TAKE CAMERA
3. Camera added to inventory
4. > TAKE PHOTO OF BARTENDER
5. Engine:
   - Gets camera_preset from object: camera/minox-spy
   - Gets preset effects: ["high contrast", "grainy", "stolen moment"]
   - Generates image with those modifiers
   - Creates photo object in inventory: "photo/bartender-001"
6. Photo has metadata linking back to camera used, location, subject
```

### Different Cameras = Different Aesthetics

| Found Camera | Preset | Vibe |
|--------------|--------|------|
| Minox behind brick | `camera/minox-spy` | Grainy surveillance |
| Polaroid in attic | `camera/polaroid` | Instant nostalgia + peel-off evidence |
| Holga in thrift shop | `camera/holga-120` | Light leaks, dreamy |
| iPhone on corpse | `camera/iphone-15` | Crisp modern horror |
| Daguerreotype in museum | `camera/daguerreotype` | Victorian ghost vibes |
| ?????? | `camera/moollm-semantic-eye` | Sees what's REALLY there |

### Photo Objects

```yaml
object/photo-bartender-001:
  type: object
  subtype: photo
  name: "Photo of Marieke"
  description: "A grainy surveillance-style photo of the bartender."
  portable: true
  taken_with: object/spy-camera
  camera_preset: camera/minox-spy
  subject: character/bartender
  location_taken: room/pub
  timestamp: "2026-01-25T20:15:00Z"
  image_file: "photos/bartender-001.png"
```

Photos become **evidence**, **inventory items**, **gifts**, **clues**!

### Example Quest: The Art Agent

> *You defeated the Art Agent in a guitar battle. Now she wants something...*

```yaml
character/art-agent:
  type: character
  name: "Valentina Vex"
  description: "A severe woman in a black turtleneck. She lost the guitar battle but gained respect."
  location: room/gallery
  dialog: "Impressive shredding. But can you capture TRUTH? Bring me a photo that shows the REAL soul of this place."
  wants:
    type: photo
    requirements:
      camera_aesthetic: ["spy", "surveillance", "hidden"]  # grainy truth
      subject_type: character
      photographer_style: ["candid", "documentary"]        # not posed
      emotional_quality: ["authentic", "unguarded"]
    reward: object/gallery-key
```

**The Quest:**
```
1. Find a camera with the right vibe
   - Minox spy camera? ✓ Hidden, grainy, surveillance
   - Polaroid? ✗ Too nostalgic, too posed
   
2. Find the right photographer POV
   - Ada II's targeting reticle? Too clinical
   - Your own eyes? Too amateur
   - That drunk guy who sees everything? PERFECT
   
3. Find the right subject in the right moment
   - Bartender when she thinks no one's watching
   - The argument in the back room
   - The tear rolling down the regular's cheek

4. TAKE PHOTO AS drunk-regular OF bartender WITH minox-spy

5. Return to Valentina
   > GIVE PHOTO TO ART AGENT
   "Yes... YES. This is it. The unvarnished human condition.
    Here. You've earned access to the gallery."
```

### The AI Loop: Generation vs Recognition

```
┌─────────────────────────────────────────────────────────────────────┐
│                        THE ADVERSARIAL ART LOOP                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐                                                   │
│  │  ART AGENT   │ ◄─── Has arbitrary rubric                         │
│  │  "I want     │      "surveillance aesthetic"                     │
│  │   TRUTH"     │      "unguarded moment"                           │
│  └──────┬───────┘      "raw human emotion"                          │
│         │                                                            │
│         ▼                                                            │
│  ┌──────────────┐                                                   │
│  │   PLAYER     │ ◄─── Makes choices                                │
│  │  Picks:      │      - Which camera?                              │
│  │  - Camera    │      - Which subject?                             │
│  │  - Subject   │      - Which moment?                              │
│  │  - POV       │      - Whose eyes?                                │
│  └──────┬───────┘                                                   │
│         │                                                            │
│         ▼                                                            │
│  ┌──────────────┐                                                   │
│  │  IMAGE GEN   │ ◄─── Interprets choices into image                │
│  │  (DALL-E,    │      Prompt assembled from:                       │
│  │   Midjourney │      camera.effects + subject.description +       │
│  │   Flux, etc) │      photographer.style + context                 │
│  └──────┬───────┘                                                   │
│         │                                                            │
│         ▼                                                            │
│  ┌──────────────┐                                                   │
│  │  IMAGE REC   │ ◄─── Analyzes what was actually generated         │
│  │  (GPT-4V,    │      Returns semantic tags:                       │
│  │   Claude,    │      "grainy", "candid", "melancholy",            │
│  │   Gemini)    │      "surveillance_aesthetic", "human_truth"      │
│  └──────┬───────┘                                                   │
│         │                                                            │
│         ▼                                                            │
│  ┌──────────────┐                                                   │
│  │   RUBRIC     │ ◄─── Score semantic overlap                       │
│  │   EVALUATOR  │      rubric ∩ recognized_tags = score             │
│  └──────┬───────┘                                                   │
│         │                                                            │
│         ▼                                                            │
│     Score > threshold?                                               │
│         │                                                            │
│    YES ─┴─ NO                                                        │
│     │      │                                                         │
│     ▼      ▼                                                         │
│  "YES!"  "Hmm, not quite. Try again."                               │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Rubric Schema

```yaml
character/art-agent:
  wants:
    rubric:
      required:           # MUST have these semantic tags
        - surveillance_aesthetic
        - candid
        - human_subject
      bonus:              # Extra points for these
        - melancholy
        - unguarded_moment
        - truth
        - raw_emotion
      forbidden:          # Instant rejection
        - posed
        - artificial
        - stock_photo
      threshold: 0.7      # 70% match required
      
      # Optional: specific weights
      weights:
        surveillance_aesthetic: 2.0   # Worth double
        truth: 1.5
        candid: 1.0
```

### Aesthetic Ranges (Goldilocks Rubrics)

Not just "high X" — but "medium X" with named sweet spots:

```yaml
character/replicant-hunter:
  wants:
    rubric:
      # Continuous aesthetic dimensions with target ranges
      dimensions:
        bladerunneresqueness:
          min: 0.25
          max: 0.75
          sweet_spot: 0.5
          name: "electric sheepy"
          too_low: "Too sunny. Where's the existential dread?"
          too_high: "Deckard, this is parody. Dial it back."
          just_right: "Yes... the sheep dream of this."
        
        noir_factor:
          min: 0.4
          max: 0.9
          sweet_spot: 0.7
          name: "venetian blind shadows"
          too_low: "Needs more shadows. More regret."
          too_high: "I can't see anything. It's just black."
        
        humanity_ambiguity:
          min: 0.3
          max: 0.7
          sweet_spot: 0.5
          name: "Turing test liminal"
          too_low: "Obviously human. Boring."
          too_high: "Obviously synthetic. Also boring."
          just_right: "I genuinely can't tell. Perfect."

character/synthwave-collector:
  wants:
    rubric:
      dimensions:
        retro_futurism:
          min: 0.6
          max: 1.0
          name: "neon chrome dreams"
        
        vaporwave:
          min: 0.0
          max: 0.3          # NOT too vaporwave
          too_high: "This is A E S T H E T I C, not synthwave. Know the difference."
        
        sunset_gradient:
          min: 0.5
          max: 0.8
          name: "miami vice twilight"

character/art-critic:
  wants:
    rubric:
      dimensions:
        pretentiousness:
          min: 0.2
          max: 0.4
          name: "accessible profundity"
          too_low: "Too pedestrian. Where's the subtext?"
          too_high: "Even I don't understand this, and I have three MFAs."
        
        originality:
          min: 0.7
          max: 1.0
          too_low: "I've seen this at every student show."
        
        technical_skill:
          min: 0.0           # Doesn't care!
          max: 1.0
          note: "Irrelevant. Outsider art is valid."
```

### Evaluation with Ranges

```javascript
function evaluateDimension(value, dim) {
  if (value < dim.min) {
    return { 
      success: false, 
      feedback: dim.too_low || `Too low on ${dim.name || 'this dimension'}` 
    };
  }
  if (value > dim.max) {
    return { 
      success: false, 
      feedback: dim.too_high || `Too high on ${dim.name || 'this dimension'}` 
    };
  }
  
  // In range! Calculate how close to sweet spot
  const sweet = dim.sweet_spot ?? (dim.min + dim.max) / 2;
  const distance = Math.abs(value - sweet);
  const maxDistance = Math.max(sweet - dim.min, dim.max - sweet);
  const score = 1 - (distance / maxDistance);
  
  return {
    success: true,
    score,
    feedback: dim.just_right || `Perfect ${dim.name || 'balance'}!`
  };
}
```

### Example Gameplay

```
> TAKE PHOTO OF replicant WITH holga STYLE blade-runner

Analyzing bladerunneresqueness... 0.89

Roy Batty squints at the image.

"Deckard, this is parody. Dial it back. 
 I want ELECTRIC SHEEPY — 0.25 to 0.75.
 Right now you're at 0.89. 
 Less rain. Fewer neon reflections. 
 Make me QUESTION if it's Blade Runner, not CERTAIN."

> TAKE PHOTO OF replicant WITH iphone STYLE candid

Analyzing bladerunneresqueness... 0.52

Roy Batty's eyes fill with tears, lost in rain.

"Yes... the sheep dream of this.
 0.52 — right in the electric sheepy zone.
 The humanity ambiguity is... *chef's kiss*
 I genuinely can't tell if this is a memory or a photo.
 
 I've seen things you people wouldn't believe."

[Quest Complete: Tears in Rain obtained]
```

### Evaluation Flow

```javascript
async function evaluatePhotoForQuest(photo, quest) {
  const rubric = quest.wants.rubric;
  
  // 1. Get semantic tags from image recognition
  const recognizedTags = await analyzeImage(photo.image_file, {
    prompt: "List semantic qualities: mood, style, technique, emotion, subject"
  });
  // → ["grainy", "candid", "surveillance_aesthetic", "melancholy", 
  //    "human_subject", "unguarded_moment", "bar_interior", "portrait"]
  
  // 2. Check forbidden tags (instant fail)
  const forbidden = rubric.forbidden?.filter(t => recognizedTags.includes(t));
  if (forbidden?.length > 0) {
    return { 
      success: false, 
      reason: `I see ${forbidden.join(', ')}. That's not what I asked for.`
    };
  }
  
  // 3. Check required tags
  const missingRequired = rubric.required?.filter(t => !recognizedTags.includes(t));
  if (missingRequired?.length > 0) {
    return {
      success: false,
      reason: `Getting closer, but I don't see ${missingRequired.join(', ')}.`
    };
  }
  
  // 4. Calculate score with weights
  let score = 0;
  let maxScore = 0;
  
  for (const tag of [...(rubric.required || []), ...(rubric.bonus || [])]) {
    const weight = rubric.weights?.[tag] || 1.0;
    maxScore += weight;
    if (recognizedTags.includes(tag)) {
      score += weight;
    }
  }
  
  const normalizedScore = score / maxScore;
  
  // 5. Check threshold
  if (normalizedScore >= rubric.threshold) {
    return {
      success: true,
      score: normalizedScore,
      reason: `YES! This is exactly what I wanted. Score: ${Math.round(normalizedScore * 100)}%`
    };
  } else {
    return {
      success: false,
      score: normalizedScore,
      reason: `${Math.round(normalizedScore * 100)}%... Almost. Try a different approach.`
    };
  }
}
```

### The Game Within The Game

You're not just taking photos — you're:
1. **Interpreting** the NPC's vague artistic demands
2. **Experimenting** with camera/subject/POV combinations
3. **Coaxing** the generation AI to produce what you need
4. **Hoping** the recognition AI sees what you intended
5. **Iterating** until the rubric is satisfied

**The AIs are your tools AND your obstacles!**

```
> TAKE PHOTO AS drunk-regular OF bartender WITH minox-spy
Generating image...
Analyzing result...

Valentina studies the photo.

"Hmm. 73%. The surveillance aesthetic is there, but it feels too... 
intentional. Where's the TRUTH? The unguarded moment?
Try catching her when she doesn't know anyone's watching."

> WAIT UNTIL bartender IS distracted
You lurk in the shadows...
The bartender wipes down the bar, lost in thought.

> TAKE PHOTO AS drunk-regular OF bartender WITH minox-spy
Generating image...
Analyzing result...

Valentina's eyes widen.

"YES. 94%. That tear she doesn't know is falling... 
that's the human condition. That's TRUTH.
Here's your key to the gallery."

[Quest Complete: Gallery Key obtained]
```

### Guitar Battles Lead to Quests

| Defeated | They Want | You Need |
|----------|-----------|----------|
| Art Agent | Photo of truth | Spy cam + candid moment |
| Music Producer | Sound of the void | ??? |
| Ghost Hunter | Proof of the other side | Daguerreotype + haunted room |
| Film Director | The perfect scene | Cinematic camera + dramatic lighting |
| AI Researcher | Image that breaks minds | Semantic Eye + impossible subject |

**TOTAL DISTORTION VIBES INTENSIFY**

---

## Future: Skinnable UI

```yaml
# In EXPORT.yml (later)
skin:
  from: skins/myst-classic
  # or inline:
  theme:
    colors:
      bg: "#1a1a2e"
      accent: "#e94560"
      text: "#eee"
    fonts:
      main: "Courier New"
      heading: "Georgia"
    layout: "fullscreen"  # or "windowed", "terminal"
    pie_menu:
      style: "radial"     # or "list", "wheel"
      size: "medium"
```

Skin = CSS + layout templates + component variants. Engine stays same, swap skin.json.

---

## Next Steps

- [ ] Extract `engine.js` from embedded code
- [ ] Create `compile.py` skeleton
- [ ] Define `world.json` schema formally
- [ ] Implement pie menu component
- [ ] Wire up drag/drop to pie menus
- [ ] (Later) Skinnable UI system
