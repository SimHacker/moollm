/**
 * adventure.js — The MOOLLM Adventure JavaScript Runtime
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * "Every program is a game. Every game is a world."
 *     — Will Wright
 * 
 * This runtime works in BOTH browser and Node.js environments.
 * UI is injected via adapters — swap DOM, console, or custom renderers.
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 * ARCHITECTURE
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * The runtime receives pre-compiled JSON with:
 * - Rooms, objects, characters, exits
 * - Pre-compiled JS functions for guards, effects, scores
 * - Runtime class tags for instantiation
 * 
 * NO VALIDATION HERE — the compiler already validated everything.
 * This is pure execution: fast, minimal, environment-agnostic.
 * 
 * UI ADAPTERS:
 * - ConsoleAdapter  — Node.js / terminal output
 * - DOMAdapter      — Browser with HTML elements
 * - NullAdapter     — Silent (for testing/simulation)
 * - Custom          — Implement IUIAdapter interface
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// ENVIRONMENT DETECTION
// ═══════════════════════════════════════════════════════════════════════════════

const IS_NODE = typeof window === 'undefined';
const IS_BROWSER = !IS_NODE;

// ═══════════════════════════════════════════════════════════════════════════════
// UI ADAPTER INTERFACE
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * IUIAdapter — Interface for UI output
 * Implement this to create custom renderers.
 */
class IUIAdapter {
    /** Called when adventure loads */
    onLoad(world) {}
    
    /** Print text output */
    print(text, type = 'response') {}
    
    /** Print room description */
    printRoom(room) { this.print(room.look(), 'room'); }
    
    /** Print error */
    printError(message) { this.print(message, 'error'); }
    
    /** Print command echo */
    printCommand(cmd) { this.print(`> ${cmd}`, 'command'); }
    
    /** Get input (async for readline support) */
    async getInput() { return ''; }
    
    /** Clear output */
    clear() {}
    
    /** Called on shutdown */
    destroy() {}
}

/**
 * NullAdapter — Silent adapter for testing/simulation
 */
class NullAdapter extends IUIAdapter {
    constructor() {
        super();
        this.output = [];
    }
    
    print(text, type = 'response') {
        this.output.push({ text, type });
    }
    
    getOutput() {
        return this.output;
    }
    
    clear() {
        this.output = [];
    }
}

/**
 * ConsoleAdapter — Node.js console output
 */
class ConsoleAdapter extends IUIAdapter {
    constructor(options = {}) {
        super();
        this.colors = options.colors !== false;
        this.readline = null;
        this.rl = null;
    }
    
    onLoad(world) {
        this._log('🎮 Adventure loaded!', 'system');
        this._log(`   ${world.rooms.size} rooms, ${world.objects.size} objects`, 'system');
        this._log('═'.repeat(60), 'system');
    }
    
    print(text, type = 'response') {
        this._log(text, type);
    }
    
    _log(text, type) {
        if (!this.colors) {
            console.log(text);
            return;
        }
        
        // ANSI colors for terminal
        const colors = {
            room: '\x1b[36m',      // Cyan
            command: '\x1b[33m',   // Yellow
            response: '\x1b[0m',   // Default
            error: '\x1b[31m',     // Red
            system: '\x1b[90m',    // Gray
            reset: '\x1b[0m'
        };
        
        const color = colors[type] || colors.response;
        console.log(`${color}${text}${colors.reset}`);
    }
    
    async getInput() {
        // Dynamic import for Node.js readline
        if (!this.readline) {
            try {
                this.readline = await import('readline');
                this.rl = this.readline.createInterface({
                    input: process.stdin,
                    output: process.stdout
                });
            } catch (e) {
                return '';
            }
        }
        
        return new Promise(resolve => {
            this.rl.question('> ', resolve);
        });
    }
    
    destroy() {
        if (this.rl) {
            this.rl.close();
        }
    }
}

/**
 * DOMAdapter — Browser DOM output
 */
class DOMAdapter extends IUIAdapter {
    constructor(containerId = 'adventure') {
        super();
        this.containerId = containerId;
        this.container = null;
        this.output = null;
        this.input = null;
        this.inputResolver = null;
    }
    
    onLoad(world) {
        if (!IS_BROWSER) return;
        
        this.container = document.getElementById(this.containerId);
        if (!this.container) {
            console.warn('Adventure container not found:', this.containerId);
            return;
        }
        
        this.container.innerHTML = `
            <div class="adventure-output" id="adventure-output"></div>
            <div class="adventure-input-row">
                <span class="prompt">&gt;</span>
                <input type="text" id="adventure-input" placeholder="What do you do?" autofocus>
            </div>
        `;
        
        this.output = document.getElementById('adventure-output');
        this.input = document.getElementById('adventure-input');
        
        this.input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && this.inputResolver) {
                const value = this.input.value.trim();
                this.input.value = '';
                this.inputResolver(value);
                this.inputResolver = null;
            }
        });
    }
    
    print(text, type = 'response') {
        if (!this.output) {
            console.log(text);
            return;
        }
        
        const div = document.createElement('div');
        div.className = `adventure-line ${type}`;
        div.textContent = text;
        this.output.appendChild(div);
        this.output.scrollTop = this.output.scrollHeight;
    }
    
    async getInput() {
        return new Promise(resolve => {
            this.inputResolver = resolve;
            if (this.input) this.input.focus();
        });
    }
    
    clear() {
        if (this.output) {
            this.output.innerHTML = '';
        }
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// EVENT EMITTER (environment-agnostic)
// ═══════════════════════════════════════════════════════════════════════════════

class EventEmitter {
    constructor() {
        this._handlers = {};
    }
    
    on(event, handler) {
        if (!this._handlers[event]) this._handlers[event] = [];
        this._handlers[event].push(handler);
    }
    
    off(event, handler) {
        if (!this._handlers[event]) return;
        this._handlers[event] = this._handlers[event].filter(h => h !== handler);
    }
    
    emit(event, data) {
        const handlers = this._handlers[event] || [];
        handlers.forEach(h => h(data));
        
        // Also dispatch DOM event if in browser
        if (IS_BROWSER) {
            document.dispatchEvent(new CustomEvent('adventure:' + event, { detail: data }));
        }
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// WORLD STATE
// ═══════════════════════════════════════════════════════════════════════════════

class WorldState extends EventEmitter {
    constructor() {
        super();
        this.rooms = new Map();
        this.objects = new Map();
        this.characters = new Map();
        this.player = null;
        this.currentRoom = null;
        this.flags = {};           // Global flags (booleans)
        this.variables = {};       // Global variables (numbers/strings)
        this.turn = 0;
        this.history = [];         // Action history for undo
        this.eventLog = [];        // Events for debugging/replay
    }
    
    /** Get the current room */
    get room() {
        return this.currentRoom;
    }
    
    /** Get player inventory */
    get inventory() {
        return this.player?.inventory || [];
    }
    
    /** Set a flag */
    setFlag(name, value = true) {
        this.flags[name] = value;
        this.emitEvent('flag_changed', { name, value });
    }
    
    /** Get a flag */
    getFlag(name) {
        return this.flags[name] || false;
    }
    
    /** Emit an event (wraps parent emit with logging) */
    emitEvent(type, data = {}) {
        const event = { type, data, turn: this.turn, time: Date.now() };
        this.eventLog.push(event);
        this.emit(type, event);  // Use parent EventEmitter
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// RUNTIME CLASSES
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Base class for all adventure entities
 */
class Entity {
    constructor(data, world) {
        this.id = data.id;
        this.name = data.name;
        this.description = data.description;
        this.data = data;  // Raw data for LLM access
        this.world = world;
    }
    
    /** Get description, possibly dynamic */
    describe() {
        return this.description || `A ${this.name}.`;
    }
}

/**
 * Room — A navigable location
 */
class Room extends Entity {
    constructor(data, world) {
        super(data, world);
        this.exits = new Map();
        this.contents = [];  // Objects in this room
        this.characters = []; // NPCs in this room
        this.atmosphere = data.atmosphere || {};
        
        // Build exits
        if (data.exits) {
            for (const [dir, exitData] of Object.entries(data.exits)) {
                this.exits.set(dir, new Exit(dir, exitData, world));
            }
        }
    }
    
    /** Get available exits as array */
    getExits() {
        return Array.from(this.exits.entries()).map(([dir, exit]) => ({
            direction: dir,
            description: exit.description,
            aliases: exit.aliases
        }));
    }
    
    /** Get visible objects */
    getObjects() {
        return this.contents.filter(obj => !obj.hidden);
    }
    
    /** Get present characters */
    getCharacters() {
        return this.characters;
    }
    
    /** Full room description with contents */
    look() {
        const parts = [this.describe()];
        
        const objects = this.getObjects();
        if (objects.length > 0) {
            parts.push('\nYou see: ' + objects.map(o => o.name).join(', '));
        }
        
        const chars = this.getCharacters();
        if (chars.length > 0) {
            parts.push('\nPresent: ' + chars.map(c => c.name).join(', '));
        }
        
        const exits = this.getExits();
        if (exits.length > 0) {
            parts.push('\nExits: ' + exits.map(e => e.direction).join(', '));
        }
        
        return parts.join('');
    }
}

/**
 * Exit — Connection between rooms
 */
class Exit extends Entity {
    constructor(direction, data, world) {
        super({ id: `exit-${direction}`, name: direction, ...data }, world);
        this.direction = direction;
        this.destination = data.destination;
        this.aliases = data.aliases || [];
        this.locked = data.locked || false;
        this.guard = data.guard_js ? new Function('world', `return (${data.guard_js})(world)`) : null;
    }
    
    /** Check if player can use this exit */
    canUse(world) {
        if (this.locked) return { allowed: false, reason: 'The way is locked.' };
        if (this.guard && !this.guard(world)) {
            return { allowed: false, reason: this.data.guard_fail || 'You cannot go that way.' };
        }
        return { allowed: true };
    }
}

/**
 * GameObject — Interactive object in the world
 */
class GameObject extends Entity {
    constructor(data, world) {
        super(data, world);
        this.emoji = data.emoji || '📦';
        this.portable = data.portable !== false;  // Default: can be picked up
        this.hidden = data.hidden || false;
        this.container = data.container || null;
        this.contents = [];
        this.advertisements = new Map();
        
        // Build advertisements (available actions)
        if (data.advertisements) {
            for (const [name, adData] of Object.entries(data.advertisements)) {
                this.advertisements.set(name, new Advertisement(name, adData, this, world));
            }
        }
    }
    
    /** Get available actions */
    getActions() {
        return Array.from(this.advertisements.values())
            .filter(ad => ad.isAvailable(this.world))
            .sort((a, b) => b.score(this.world) - a.score(this.world));
    }
    
    /** Short display name with emoji */
    get displayName() {
        return `${this.emoji} ${this.name}`;
    }
}

/**
 * Advertisement — An action available on an object
 */
class Advertisement {
    constructor(name, data, parent, world) {
        this.name = name;
        this.description = data.description;
        this.baseScore = data.score || 50;
        this.effect = data.effect;
        this.parent = parent;
        this.world = world;
        
        // Compile JS functions if provided
        this.guardFn = data.guard_js ? new Function('world', `return (${data.guard_js})(world)`) : null;
        this.scoreFn = data.score_if_js ? new Function('world', `return (${data.score_if_js})(world)`) : null;
        this.effectFn = data.effect_js ? new Function('world', `return (${data.effect_js})(world)`) : null;
    }
    
    /** Check if action is currently available */
    isAvailable(world) {
        if (this.guardFn) {
            try {
                return this.guardFn(world);
            } catch (e) {
                console.warn(`Guard failed for ${this.name}:`, e);
                return false;
            }
        }
        return true;
    }
    
    /** Calculate current score */
    score(world) {
        let s = this.baseScore;
        if (this.scoreFn) {
            try {
                if (this.scoreFn(world)) s += 20;  // Bonus if condition met
            } catch (e) {
                console.warn(`Score calculation failed for ${this.name}:`, e);
            }
        }
        return s;
    }
    
    /** Execute the action */
    execute(world) {
        world.emitEvent('action_start', { action: this.name, object: this.parent.name });
        
        let result = this.effect || `You ${this.name.toLowerCase()} the ${this.parent.name}.`;
        
        if (this.effectFn) {
            try {
                const fnResult = this.effectFn(world);
                if (fnResult) result = fnResult;
            } catch (e) {
                console.warn(`Effect failed for ${this.name}:`, e);
            }
        }
        
        world.emitEvent('action_complete', { action: this.name, object: this.parent.name, result });
        return result;
    }
}

/**
 * Character — NPC or player
 */
class Character extends Entity {
    constructor(data, world) {
        super(data, world);
        this.emoji = data.emoji || '👤';
        this.inventory = [];
        this.location = null;  // Room reference
        this.dialogue = data.dialogue || null;
        this.mood = data.mood || 'neutral';
        this.isPlayer = data.is_player || false;
    }
    
    /** Move to a room */
    moveTo(room) {
        if (this.location) {
            const idx = this.location.characters.indexOf(this);
            if (idx >= 0) this.location.characters.splice(idx, 1);
        }
        this.location = room;
        if (room) {
            room.characters.push(this);
        }
        this.world.emitEvent('character_moved', { character: this.name, room: room?.name });
    }
    
    /** Add item to inventory */
    take(object) {
        if (!object.portable) {
            return { success: false, message: `You can't take the ${object.name}.` };
        }
        
        // Remove from room
        if (object.container) {
            const idx = object.container.contents.indexOf(object);
            if (idx >= 0) object.container.contents.splice(idx, 1);
        } else if (this.location) {
            const idx = this.location.contents.indexOf(object);
            if (idx >= 0) this.location.contents.splice(idx, 1);
        }
        
        this.inventory.push(object);
        object.container = this;
        
        this.world.emitEvent('item_taken', { character: this.name, object: object.name });
        return { success: true, message: `You take the ${object.name}.` };
    }
    
    /** Drop item from inventory */
    drop(object) {
        const idx = this.inventory.indexOf(object);
        if (idx < 0) {
            return { success: false, message: `You don't have the ${object.name}.` };
        }
        
        this.inventory.splice(idx, 1);
        if (this.location) {
            this.location.contents.push(object);
            object.container = this.location;
        }
        
        this.world.emitEvent('item_dropped', { character: this.name, object: object.name });
        return { success: true, message: `You drop the ${object.name}.` };
    }
    
    /** Check if character has an item */
    has(objectId) {
        return this.inventory.some(obj => obj.id === objectId);
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// ADVENTURE ENGINE
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * AdventureEngine — Main game controller
 * 
 * @param {IUIAdapter} adapter - UI adapter (optional, defaults based on environment)
 */
class AdventureEngine {
    constructor(adapter = null) {
        this.world = new WorldState();
        this.ready = false;
        
        // Auto-select adapter based on environment
        if (adapter) {
            this.ui = adapter;
        } else if (IS_BROWSER) {
            this.ui = new DOMAdapter();
        } else {
            this.ui = new ConsoleAdapter();
        }
    }
    
    /**
     * Load compiled adventure JSON
     */
    async load(data) {
        console.log('🎮 Loading adventure:', data.name);
        
        // Create rooms
        for (const roomData of data.rooms || []) {
            const room = new Room(roomData, this.world);
            this.world.rooms.set(room.id, room);
        }
        
        // Create objects and place in rooms
        for (const objData of data.objects || []) {
            const obj = new GameObject(objData, this.world);
            this.world.objects.set(obj.id, obj);
            
            if (objData.location) {
                const room = this.world.rooms.get(objData.location);
                if (room) {
                    room.contents.push(obj);
                    obj.container = room;
                }
            }
        }
        
        // Create characters
        for (const charData of data.characters || []) {
            const char = new Character(charData, this.world);
            this.world.characters.set(char.id, char);
            
            if (charData.is_player) {
                this.world.player = char;
            }
            
            if (charData.location) {
                const room = this.world.rooms.get(charData.location);
                if (room) char.moveTo(room);
            }
        }
        
        // Create default player if none was marked
        if (!this.world.player) {
            const player = new Character({
                id: 'player',
                name: 'You',
                description: 'A curious adventurer.',
                is_player: true
            }, this.world);
            this.world.characters.set('player', player);
            this.world.player = player;
        }
        
        // Set starting room
        if (data.starting_room) {
            const startRoom = this.world.rooms.get(data.starting_room);
            if (startRoom && this.world.player) {
                this.world.player.moveTo(startRoom);
                this.world.currentRoom = startRoom;
            }
        }
        
        // Initialize flags
        if (data.initial_flags) {
            Object.assign(this.world.flags, data.initial_flags);
        }
        
        this.ready = true;
        this.world.emitEvent('adventure_loaded', { name: data.name });
        
        // Notify UI adapter
        this.ui.onLoad(this.world);
        
        return this;
    }
    
    /**
     * Run interactive game loop
     */
    async run() {
        if (!this.ready) {
            this.ui.printError('Adventure not loaded.');
            return;
        }
        
        // Print initial room
        this.ui.printRoom(this.world.room);
        
        // Main game loop
        while (true) {
            const input = await this.ui.getInput();
            if (!input) continue;
            
            // Quit commands
            if (['quit', 'exit', 'q'].includes(input.toLowerCase())) {
                this.ui.print('Goodbye!', 'system');
                break;
            }
            
            this.ui.printCommand(input);
            const result = this.command(input);
            
            if (result.success) {
                this.ui.print(result.message, 'response');
            } else {
                this.ui.printError(result.message);
            }
        }
        
        this.ui.destroy();
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // STATE EXPORT/IMPORT
    // ─────────────────────────────────────────────────────────────────────────
    
    /**
     * Export current world state to JSON.
     * 
     * This creates a snapshot that can be:
     * 1. Saved to localStorage/file for later
     * 2. Sent to LLM for intelligent merging back to YAML
     * 3. Used for debugging/replay
     * 
     * The LLM can read this and apply changes to the source YAML,
     * retaining extra keys and using intelligence to merge!
     */
    exportState() {
        const state = {
            _meta: {
                type: 'adventure-state',
                version: '1.0',
                exported: new Date().toISOString(),
                turn: this.world.turn
            },
            
            // Player state
            player: this.world.player ? {
                id: this.world.player.id,
                location: this.world.player.location?.id || null,
                inventory: this.world.player.inventory.map(o => ({
                    id: o.id,
                    name: o.name
                })),
                mood: this.world.player.mood
            } : null,
            
            // Global state
            flags: { ...this.world.flags },
            variables: { ...this.world.variables },
            
            // Room states (only modified properties)
            rooms: {},
            
            // Object states (only modified properties)  
            objects: {},
            
            // Character states
            characters: {},
            
            // History for replay
            history: this.world.history.slice(-100),  // Last 100 commands
            
            // Event log for debugging
            eventLog: this.world.eventLog.slice(-50)  // Last 50 events
        };
        
        // Export room modifications
        for (const [id, room] of this.world.rooms) {
            const roomState = {};
            
            // Track which objects are in each room
            roomState.contents = room.contents.map(o => o.id);
            roomState.characters = room.characters.map(c => c.id);
            
            // Only include if there's state to save
            if (roomState.contents.length > 0 || roomState.characters.length > 0) {
                state.rooms[id] = roomState;
            }
        }
        
        // Export object modifications
        for (const [id, obj] of this.world.objects) {
            const objState = {};
            
            // Track location
            if (obj.container) {
                if (obj.container instanceof Room) {
                    objState.location = obj.container.id;
                    objState.locationType = 'room';
                } else if (obj.container instanceof Character) {
                    objState.location = obj.container.id;
                    objState.locationType = 'character';
                }
            }
            
            // Track any dynamic properties from _extra
            if (obj.data._runtime) {
                objState._runtime = obj.data._runtime;
            }
            
            if (Object.keys(objState).length > 0) {
                state.objects[id] = objState;
            }
        }
        
        // Export character states
        for (const [id, char] of this.world.characters) {
            if (char.isPlayer) continue;  // Player handled separately
            
            state.characters[id] = {
                location: char.location?.id || null,
                mood: char.mood,
                inventory: char.inventory.map(o => o.id)
            };
        }
        
        return state;
    }
    
    /**
     * Export state as JSON string (for saving to file)
     */
    exportStateJSON(pretty = true) {
        return JSON.stringify(this.exportState(), null, pretty ? 2 : 0);
    }
    
    /**
     * Import state from a saved snapshot.
     * 
     * This restores:
     * - Player location and inventory
     * - Flags and variables
     * - Object locations
     * - Character states
     */
    importState(state) {
        if (state._meta?.type !== 'adventure-state') {
            throw new Error('Invalid state format');
        }
        
        // Restore flags and variables
        this.world.flags = { ...state.flags };
        this.world.variables = { ...state.variables };
        this.world.turn = state._meta.turn || 0;
        
        // Restore player
        if (state.player && this.world.player) {
            if (state.player.location) {
                const room = this.world.rooms.get(state.player.location);
                if (room) {
                    this.world.player.moveTo(room);
                    this.world.currentRoom = room;
                }
            }
            
            // Restore inventory
            this.world.player.inventory = [];
            for (const item of state.player.inventory || []) {
                const obj = this.world.objects.get(item.id);
                if (obj) {
                    this.world.player.inventory.push(obj);
                    obj.container = this.world.player;
                }
            }
        }
        
        // Restore object locations
        for (const [id, objState] of Object.entries(state.objects || {})) {
            const obj = this.world.objects.get(id);
            if (!obj) continue;
            
            if (objState.locationType === 'room') {
                const room = this.world.rooms.get(objState.location);
                if (room && !room.contents.includes(obj)) {
                    room.contents.push(obj);
                    obj.container = room;
                }
            }
        }
        
        // Restore character states
        for (const [id, charState] of Object.entries(state.characters || {})) {
            const char = this.world.characters.get(id);
            if (!char) continue;
            
            if (charState.location) {
                const room = this.world.rooms.get(charState.location);
                if (room) char.moveTo(room);
            }
            char.mood = charState.mood || 'neutral';
        }
        
        this.world.emitEvent('state_imported', { turn: this.world.turn });
    }
    
    /**
     * Save state to localStorage (browser only)
     */
    saveToLocalStorage(key = 'adventure-save') {
        if (!IS_BROWSER) return false;
        try {
            localStorage.setItem(key, this.exportStateJSON());
            return true;
        } catch (e) {
            console.error('Failed to save:', e);
            return false;
        }
    }
    
    /**
     * Load state from localStorage (browser only)
     */
    loadFromLocalStorage(key = 'adventure-save') {
        if (!IS_BROWSER) return false;
        try {
            const json = localStorage.getItem(key);
            if (!json) return false;
            this.importState(JSON.parse(json));
            return true;
        } catch (e) {
            console.error('Failed to load:', e);
            return false;
        }
    }
    
    /**
     * Process a player command
     */
    command(input) {
        if (!this.ready) {
            return { success: false, message: 'Adventure not loaded.' };
        }
        
        const cmd = input.trim().toLowerCase();
        const words = cmd.split(/\s+/);
        const verb = words[0];
        const args = words.slice(1).join(' ');
        
        this.world.turn++;
        this.world.history.push({ turn: this.world.turn, input: cmd });
        
        // Built-in commands
        switch (verb) {
            case 'look':
            case 'l':
                return this.look(args);
            
            case 'go':
            case 'n': case 'north':
            case 's': case 'south':
            case 'e': case 'east':
            case 'w': case 'west':
            case 'ne': case 'northeast':
            case 'nw': case 'northwest':
            case 'se': case 'southeast':
            case 'sw': case 'southwest':
            case 'u': case 'up':
            case 'd': case 'down':
            case 'in': case 'out':
                return this.go(verb === 'go' ? args : verb);
            
            case 'take':
            case 'get':
            case 'grab':
                return this.take(args);
            
            case 'drop':
            case 'put':
                return this.drop(args);
            
            case 'inventory':
            case 'inv':
            case 'i':
                return this.showInventory();
            
            case 'look':
            case 'examine':
            case 'x':
            case 'inspect':
                return this.examine(args);
            
            case 'talk':
            case 'speak':
                return this.talk(args);
            
            case 'help':
            case '?':
                return this.help();
            
            case 'exits':
                return this.exits();
            
            case 'stats':
                return this.stats();
            
            default:
                // Try to match an object action
                return this.tryAction(verb, args);
        }
    }
    
    /** Look at current room or specific thing */
    look(target) {
        if (!target) {
            if (!this.world.room) {
                return { success: false, message: "You're nowhere! (This is a miracle!)" };
            }
            return { success: true, message: this.world.room.look() };
        }
        return this.examine(target);
    }
    
    /** List exits from current room */
    exits() {
        if (!this.world.room) {
            return { success: false, message: "You're nowhere!" };
        }
        
        const exits = this.world.room.exits;
        if (exits.size === 0) {
            return { success: true, message: "There are no obvious exits." };
        }
        
        const lines = ["Exits:"];
        for (const [dir, exit] of exits) {
            const desc = exit.description.split('\n')[0].substring(0, 50) || `→ ${exit.destination}`;
            const aliases = exit.aliases.length ? ` (${exit.aliases.join(', ')})` : '';
            lines.push(`  ${dir}${aliases}: ${desc}`);
        }
        
        return { success: true, message: lines.join('\n') };
    }
    
    /** Show game statistics */
    stats() {
        const lines = [
            "Game Statistics:",
            `  Turn: ${this.world.turn}`,
            `  Rooms: ${this.world.rooms.size}`,
            `  Objects: ${this.world.objects.size}`,
            `  Characters: ${this.world.characters.size}`,
            `  Current room: ${this.world.room?.id || 'None'}`,
            `  Inventory items: ${this.world.player?.inventory.length || 0}`,
            `  Flags set: ${Object.values(this.world.flags).filter(v => v).length}`
        ];
        return { success: true, message: lines.join('\n') };
    }
    
    /** Move in a direction */
    go(direction) {
        // Normalize direction
        const dirMap = {
            'n': 'n', 'north': 'n',
            's': 's', 'south': 's',
            'e': 'e', 'east': 'e',
            'w': 'w', 'west': 'w',
            'ne': 'ne', 'northeast': 'ne',
            'nw': 'nw', 'northwest': 'nw',
            'se': 'se', 'southeast': 'se',
            'sw': 'sw', 'southwest': 'sw',
            'u': 'up', 'up': 'up',
            'd': 'down', 'down': 'down',
            'in': 'in', 'out': 'out'
        };
        
        // Also expand short forms back to full names
        const dirExpand = {
            'n': 'north', 's': 'south', 'e': 'east', 'w': 'west',
            'ne': 'northeast', 'nw': 'northwest', 'se': 'southeast', 'sw': 'southwest',
            'u': 'up', 'd': 'down'
        };
        
        const dir = dirMap[direction] || direction;
        const dirFull = dirExpand[dir] || dir;
        
        // Try multiple variations (case-insensitive)
        const tryDirs = [dir, dirFull, direction, dir.toUpperCase(), dirFull.toUpperCase(), direction.toUpperCase()];
        
        let exit = null;
        for (const tryDir of tryDirs) {
            exit = this.world.room.exits.get(tryDir);
            if (exit) break;
        }
        
        // Check aliases if still not found
        if (!exit) {
            for (const [_, e] of this.world.room.exits) {
                if (e.aliases.includes(direction) || e.aliases.includes(dir) || e.aliases.includes(dirFull)) {
                    exit = e;
                    break;
                }
            }
        }
        
        // Also check numeric room shortcuts (1-8)
        if (!exit && /^\d+$/.test(direction)) {
            for (const [_, e] of this.world.room.exits) {
                if (e.aliases.includes(parseInt(direction))) {
                    exit = e;
                    break;
                }
            }
        }
        
        if (!exit) {
            return { success: false, message: `You can't go ${direction}.` };
        }
        
        const check = exit.canUse(this.world);
        if (!check.allowed) {
            return { success: false, message: check.reason };
        }
        
        // Resolve destination - handle relative paths
        const dest = exit.destination;
        const currentId = this.world.room.id;
        
        // Try various normalizations
        const candidates = [];
        candidates.push(dest.replace(/\/$/, '')); // Strip trailing slash
        
        // If relative path, resolve from current room
        if (dest.startsWith('../')) {
            const parts = currentId.split('/');
            const destParts = dest.split('/');
            const upCount = destParts.filter(p => p === '..').length;
            const remaining = destParts.filter(p => p !== '..').join('/').replace(/\/$/, '');
            const base = parts.slice(0, -upCount).join('/');
            candidates.push(base ? `${base}/${remaining}` : remaining);
            candidates.push(remaining); // Also try just the remaining part
        }
        
        // Strip all ../ and ./ prefixes
        let stripped = dest.replace(/^(\.\.\/)+/, '').replace(/^(\.\/)+/, '').replace(/\/$/, '');
        candidates.push(stripped);
        candidates.push(stripped.split('/').pop()); // Just the last part
        
        let destRoom = null;
        for (const candidate of candidates) {
            if (!candidate) continue;
            destRoom = this.world.rooms.get(candidate);
            if (destRoom) break;
        }
        
        if (!destRoom) {
            return { success: false, message: 'That way leads nowhere.' };
        }
        
        this.world.player.moveTo(destRoom);
        this.world.currentRoom = destRoom;
        
        return { success: true, message: destRoom.look() };
    }
    
    /** Pick up an object */
    take(name) {
        const obj = this.findObject(name);
        if (!obj) {
            return { success: false, message: `You don't see a ${name} here.` };
        }
        return this.world.player.take(obj);
    }
    
    /** Drop an object */
    drop(name) {
        const obj = this.findInInventory(name);
        if (!obj) {
            return { success: false, message: `You don't have a ${name}.` };
        }
        return this.world.player.drop(obj);
    }
    
    /** Show inventory */
    showInventory() {
        const inv = this.world.player.inventory;
        if (inv.length === 0) {
            return { success: true, message: 'You are carrying nothing.' };
        }
        const items = inv.map(o => o.displayName).join('\n  ');
        return { success: true, message: `You are carrying:\n  ${items}` };
    }
    
    /** Examine something */
    examine(name) {
        // Check room objects
        let target = this.findObject(name);
        if (target) {
            const actions = target.getActions();
            let msg = target.describe();
            if (actions.length > 0) {
                msg += '\n\nActions: ' + actions.map(a => a.name).join(', ');
            }
            return { success: true, message: msg };
        }
        
        // Check inventory
        target = this.findInInventory(name);
        if (target) {
            return { success: true, message: target.describe() };
        }
        
        // Check characters
        target = this.findCharacter(name);
        if (target) {
            return { success: true, message: target.describe() };
        }
        
        return { success: false, message: `You don't see a ${name} here.` };
    }
    
    /** Talk to someone */
    talk(name) {
        const char = this.findCharacter(name);
        if (!char) {
            return { success: false, message: `You don't see ${name} here.` };
        }
        
        // TODO: Full dialogue system
        return { success: true, message: `${char.name} nods at you.` };
    }
    
    /** Try to match an action on an object */
    tryAction(verb, target) {
        const obj = this.findObject(target) || this.findInInventory(target);
        if (!obj) {
            return { success: false, message: `I don't understand "${verb}".` };
        }
        
        const action = obj.advertisements.get(verb.toUpperCase());
        if (!action) {
            return { success: false, message: `You can't ${verb} the ${obj.name}.` };
        }
        
        if (!action.isAvailable(this.world)) {
            return { success: false, message: action.data.guard_fail || `You can't do that right now.` };
        }
        
        const result = action.execute(this.world);
        return { success: true, message: result };
    }
    
    /** Show help */
    help() {
        return {
            success: true,
            message: `Commands:
  look (l)          - Describe current room
  go <direction>    - Move (n/s/e/w/ne/nw/se/sw/up/down/in/out)
  take <item>       - Pick up an item
  drop <item>       - Drop an item
  inventory (i)     - Show what you're carrying
  examine <thing>   - Look at something closely
  talk <person>     - Talk to someone
  <action> <item>   - Do an action on an item
  help              - Show this help`
        };
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // Helper methods
    // ─────────────────────────────────────────────────────────────────────────
    
    /** Find object in current room */
    findObject(name) {
        if (!name) return null;
        name = name.toLowerCase();
        return this.world.room?.contents.find(o => 
            o.name.toLowerCase().includes(name) ||
            o.id.toLowerCase() === name
        );
    }
    
    /** Find object in player inventory */
    findInInventory(name) {
        if (!name) return null;
        name = name.toLowerCase();
        return this.world.player?.inventory.find(o =>
            o.name.toLowerCase().includes(name) ||
            o.id.toLowerCase() === name
        );
    }
    
    /** Find character in current room */
    findCharacter(name) {
        if (!name) return null;
        name = name.toLowerCase();
        return this.world.room?.characters.find(c =>
            c.name.toLowerCase().includes(name) ||
            c.id.toLowerCase() === name
        );
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// NODE.JS CLI (when run directly)
// ═══════════════════════════════════════════════════════════════════════════════

async function main() {
    if (!IS_NODE) return;
    
    // Check for adventure JSON argument
    const args = process.argv.slice(2);
    if (args.length === 0) {
        console.log('MOOLLM Adventure Runtime');
        console.log('========================');
        console.log('Usage: node adventure.js <adventure.json>');
        console.log('');
        console.log('Or import as module:');
        console.log('  import { AdventureEngine, ConsoleAdapter } from "./adventure.js"');
        console.log('  const engine = new AdventureEngine(new ConsoleAdapter());');
        console.log('  engine.load(data).run();');
        return;
    }
    
    // Load and run adventure
    const fs = await import('fs');
    const path = await import('path');
    
    const adventurePath = path.default.resolve(args[0]);
    const data = JSON.parse(fs.default.readFileSync(adventurePath, 'utf-8'));
    
    const engine = new AdventureEngine(new ConsoleAdapter());
    await engine.load(data).run();
}

// Run main if this is the entry point
if (IS_NODE && process.argv[1]?.endsWith('adventure.js')) {
    main().catch(console.error);
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS (Universal - works in ES Modules, CommonJS, and script tags)
// ═══════════════════════════════════════════════════════════════════════════════

const ADVENTURE_EXPORTS = {
    // Engine & State
    AdventureEngine, 
    WorldState,
    EventEmitter,
    
    // Entities
    Room, 
    Exit, 
    GameObject, 
    Character, 
    Advertisement,
    
    // UI Adapters
    IUIAdapter,
    NullAdapter,
    ConsoleAdapter,
    DOMAdapter,
    
    // Environment
    IS_NODE,
    IS_BROWSER
};

// Browser: attach to window
if (IS_BROWSER) {
    window.Adventure = ADVENTURE_EXPORTS;
}

// Node.js CommonJS
if (IS_NODE && typeof module !== 'undefined' && module.exports) {
    module.exports = ADVENTURE_EXPORTS;
}

// Node.js global fallback
if (IS_NODE && typeof global !== 'undefined') {
    global.Adventure = ADVENTURE_EXPORTS;
}

// ES Module export (only works when loaded as module)
// Wrapped in try/catch for eval() compatibility
try {
    if (typeof exports === 'object') {
        Object.assign(exports, ADVENTURE_EXPORTS);
    }
} catch (e) { /* Not in module context */ }
