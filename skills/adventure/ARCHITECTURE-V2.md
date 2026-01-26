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
│   ├── index.html            # Shell that loads world.json
│   └── README.md             # Engine dev docs
│
├── compiler/                  # YAML → JSON compiler
│   └── compile.py            # Outputs world.json
│
└── examples/
    └── adventure-4/
        └── build/
            └── world.json    # Compiled world data
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

```json
{
  "_meta": {
    "version": "2.0.0",
    "compiled_at": "2026-01-25T19:30:00Z",
    "source": "examples/adventure-4"
  },
  
  "config": {
    "starting_room": "lobby",
    "features": {
      "pie_menus": true,
      "drag_drop": true,
      "speech": false,
      "images": false
    }
  },
  
  "rooms": {
    "lobby": {
      "id": "lobby",
      "name": "The Lobby",
      "description": "A grand entrance hall.",
      "exits": { "north": "hallway", "east": "office" },
      "contents": ["lamp", "key"]
    }
  },
  
  "objects": {
    "lamp": {
      "id": "lamp",
      "name": "Brass Lamp",
      "description": "An old brass lamp.",
      "portable": true,
      "actions": ["take", "examine", "rub"]
    },
    "key": {
      "id": "key",
      "name": "Rusty Key",
      "portable": true,
      "actions": ["take", "examine", "use"]
    }
  },
  
  "characters": {
    "bartender": {
      "id": "bartender",
      "name": "Marieke",
      "location": "pub",
      "dialog_tree": "bartender-dialog"
    }
  },
  
  "actions": {
    "_doc": "JS strings that get eval'd into (world, subject, object?) => result",
    
    "take": "(world, subject) => { world.player.inventory.push(subject.id); return `You take the ${subject.name}.`; }",
    
    "drop": "(world, subject) => { const idx = world.player.inventory.indexOf(subject.id); if (idx >= 0) { world.player.inventory.splice(idx, 1); world.room.contents.push(subject.id); return `You drop the ${subject.name}.`; } return 'You are not carrying that.'; }",
    
    "examine": "(world, subject) => subject.description || `It's a ${subject.name}.`",
    
    "use_on": "(world, subject, object) => { if (subject.id === 'key' && object.id === 'door') { world.flags.door_unlocked = true; return 'The door clicks open!'; } return `You can't use the ${subject.name} on the ${object.name}.`; }",
    
    "give": "(world, subject, object) => { if (object.type === 'character') { return `${object.name} says: \"Thanks for the ${subject.name}!\"`; } return 'You can only give things to people.'; }"
  },
  
  "pie_menus": {
    "_doc": "Menus shown for different drag contexts",
    
    "self": {
      "_doc": "Click on object in inventory",
      "actions": ["examine", "drop", "use"]
    },
    
    "object_on_object": {
      "_doc": "Drag object onto another object",
      "actions": ["use_on", "combine", "compare"]
    },
    
    "object_on_character": {
      "_doc": "Drag object onto character",
      "actions": ["give", "show", "throw_at"]
    },
    
    "object_on_room": {
      "_doc": "Drag object onto room/floor",
      "actions": ["drop", "place", "throw"]
    }
  },
  
  "prototypes": {
    "_doc": "Object templates for inheritance",
    
    "container": {
      "actions": ["open", "close", "look_in"],
      "properties": { "is_open": false, "contents": [] }
    },
    
    "light_source": {
      "actions": ["turn_on", "turn_off"],
      "properties": { "is_lit": false }
    }
  }
}
```

---

## Engine API

```javascript
// engine.js exports

class AdventureEngine {
  constructor(worldData) {
    this.world = this.loadWorld(worldData);
    this.actions = this.compileActions(worldData.actions);
    this.pieMenus = worldData.pie_menus;
  }
  
  // Compile action strings into closures
  compileActions(actionDefs) {
    const actions = {};
    for (const [name, code] of Object.entries(actionDefs)) {
      if (name.startsWith('_')) continue; // Skip _doc
      actions[name] = eval(code);
    }
    return actions;
  }
  
  // Execute action
  do(actionName, subject, object = null) {
    const action = this.actions[actionName];
    if (!action) return `Unknown action: ${actionName}`;
    return action(this.world, subject, object);
  }
  
  // Get pie menu for drag context
  getPieMenu(context, subject, object = null) {
    const menuDef = this.pieMenus[context];
    if (!menuDef) return [];
    
    return menuDef.actions.filter(actionName => {
      // Filter to valid actions for this subject/object combo
      return this.isValidAction(actionName, subject, object);
    });
  }
  
  // Drag handler — returns pie menu
  onDrag(subject, target) {
    if (target.type === 'character') {
      return this.getPieMenu('object_on_character', subject, target);
    } else if (target.type === 'object') {
      return this.getPieMenu('object_on_object', subject, target);
    } else if (target.type === 'room') {
      return this.getPieMenu('object_on_room', subject, target);
    }
    return [];
  }
}
```

---

## Pie Menu Interaction Flow

```
1. User drags "key" from inventory
2. User drops "key" onto "door"
3. Engine detects: object_on_object context
4. Engine calls: getPieMenu('object_on_object', key, door)
5. Engine shows pie menu: [use_on, combine, compare]
6. User clicks "use_on"
7. Engine calls: do('use_on', key, door)
8. Action returns: "The door clicks open!"
9. World state updated: flags.door_unlocked = true
```

---

## Compilation Pipeline

```bash
# Compile YAML world to JSON
python compile.py examples/adventure-4/ --output build/world.json

# Output structure:
# 1. Walk adventure directory
# 2. Load all YAML files
# 3. Merge into single JSON blob
# 4. Inline action closures as strings
# 5. Write world.json
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
    // Load world data and start
    fetch('world.json')
      .then(r => r.json())
      .then(data => {
        window.engine = new AdventureEngine(data);
        engine.mount('#adventure');
        engine.start();
      });
  </script>
</body>
</html>
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
