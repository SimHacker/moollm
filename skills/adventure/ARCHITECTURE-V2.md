# Adventure Engine V2 Architecture

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

## Compilation Pipeline

```bash
# Compile YAML world to JSON
python compile.py examples/adventure-4/ --output build/world.json
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

## Next Steps

- [ ] Extract `engine.js` from embedded code
- [ ] Create `compile.py` skeleton
- [ ] Define `world.json` schema formally
- [ ] Implement pie menu component
- [ ] Wire up drag/drop to pie menus
