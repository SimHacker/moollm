/**
 * engine_v2.js — MOOTAL DISTORTION Engine V2
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * "Sheepy enough, but not too sheepy."
 * 
 * Flat registry, eval'd closures, client-side everything.
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

class MootalEngine {
    constructor() {
        this.registry = {};
        this.config = {};
        this.player = {
            location: null,
            inventory: []
        };
        this.flags = {};
        this.actions = {};
        this.ui = null;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // LOADING
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Load world data from JSON
     */
    load(worldData, charactersData = {}, presetsData = {}) {
        // Merge registries
        this.registry = {};
        Object.assign(this.registry, worldData.registry || {});
        Object.assign(this.registry, charactersData.registry || {});
        Object.assign(this.registry, presetsData.registry || {});
        
        this.config = worldData.config || {};
        
        // Set starting location
        this.player.location = this.config.starting_room || 'room/pub';
        
        // Compile actions
        this.compileActions();
        
        console.log('🎮 MOOTAL DISTORTION loaded!');
        console.log(`   ${Object.keys(this.registry).length} objects in registry`);
        console.log(`   Starting at: ${this.player.location}`);
        
        return this;
    }
    
    /**
     * Compile action code strings into closures
     */
    compileActions() {
        for (const [key, obj] of Object.entries(this.registry)) {
            if (key.startsWith('action/') && obj.code) {
                try {
                    this.actions[key] = eval(obj.code);
                } catch (e) {
                    console.warn(`Failed to compile action ${key}:`, e);
                }
            }
        }
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // REGISTRY ACCESS
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get object by type/id reference
     * Supports sub-object: "room/pub#exits"
     */
    get(ref) {
        if (!ref) return null;
        
        const [path, subkey] = ref.split('#');
        const obj = this.registry[path];
        
        if (!obj) return null;
        if (subkey) return obj[subkey];
        return obj;
    }
    
    /**
     * Get all objects of a type
     */
    getByType(type) {
        return Object.entries(this.registry)
            .filter(([key]) => key.startsWith(`${type}/`))
            .map(([key, obj]) => obj);
    }
    
    /**
     * Get current room
     */
    get room() {
        return this.get(this.player.location);
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // FLAGS & STATE
    // ═══════════════════════════════════════════════════════════════════════════
    
    setFlag(name, value = true) {
        this.flags[name] = value;
    }
    
    getFlag(name) {
        return this.flags[name] || false;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // NAVIGATION
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Navigate to a room via exit direction
     */
    go(direction) {
        const room = this.room;
        if (!room) {
            return "You're nowhere. That's concerning.";
        }
        
        const dir = direction.toLowerCase();
        let exit = room.exits?.[dir];
        
        // Check aliases
        if (!exit) {
            for (const [exitDir, ex] of Object.entries(room.exits || {})) {
                if (ex.aliases?.includes(dir)) {
                    exit = ex;
                    break;
                }
            }
        }
        
        if (!exit) {
            return `You can't go "${direction}" from here.\n\nExits: ${Object.keys(room.exits || {}).join(', ')}`;
        }
        
        // Check if locked
        if (exit.locked) {
            return exit.fail_message || "The way is locked.";
        }
        
        // Check guard condition
        if (exit.guard) {
            try {
                const guardFn = eval(exit.guard);
                if (!guardFn(this)) {
                    return exit.fail_message || "You can't go that way.";
                }
            } catch (e) {
                console.warn(`Guard eval failed for ${dir}:`, e);
            }
        }
        
        // Check destination exists
        const destination = this.get(exit.to);
        if (!destination) {
            return `The way to "${exit.to}" doesn't exist yet. (Missing room)`;
        }
        
        // Move player
        this.player.location = exit.to;
        
        // Return new room description
        return this.look();
    }
    
    /**
     * Look at current room
     */
    look() {
        const room = this.room;
        if (!room) {
            return "You're in the void. This shouldn't happen.";
        }
        
        const parts = [];
        
        // Room name
        parts.push(`═══ ${room.name} ═══`);
        parts.push('');
        
        // Description
        parts.push(room.description || 'You see nothing special.');
        parts.push('');
        
        // Contents (objects)
        if (room.contents?.length > 0) {
            parts.push('You see:');
            for (const objRef of room.contents) {
                const obj = this.get(objRef);
                if (obj) {
                    parts.push(`  • ${obj.name || objRef}`);
                }
            }
            parts.push('');
        }
        
        // Exits
        const exits = room.exits || {};
        if (Object.keys(exits).length > 0) {
            parts.push('Exits:');
            for (const [dir, exit] of Object.entries(exits)) {
                const desc = exit.description || `Exit ${dir}`;
                // Truncate long descriptions
                const shortDesc = desc.split('\n')[0].substring(0, 60);
                parts.push(`  ${dir.toUpperCase()}: ${shortDesc}`);
            }
        } else {
            parts.push('No obvious exits.');
        }
        
        return parts.join('\n');
    }
    
    /**
     * Examine an exit for full description
     */
    examineExit(direction) {
        const room = this.room;
        const dir = direction.toLowerCase();
        const exit = room?.exits?.[dir];
        
        if (!exit) {
            return `There's no exit "${direction}" here.`;
        }
        
        let desc = exit.description || `An exit leading ${direction}.`;
        
        // Check for dynamic description
        if (exit.description_js) {
            try {
                const descFn = eval(exit.description_js);
                desc = descFn(this);
            } catch (e) {
                console.warn(`Dynamic description eval failed:`, e);
            }
        }
        
        // Add note if present
        if (exit.note) {
            desc += `\n\n(${exit.note})`;
        }
        
        return desc;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // COMMAND PROCESSING
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Process a text command
     */
    command(input) {
        const parts = input.trim().split(/\s+/);
        const cmd = parts[0].toLowerCase();
        const args = parts.slice(1).join(' ');
        
        // Navigation commands
        const directions = ['north', 'south', 'east', 'west', 'up', 'down', 
                          'n', 's', 'e', 'w', 'u', 'd',
                          'northeast', 'northwest', 'southeast', 'southwest',
                          'ne', 'nw', 'se', 'sw', 'back', 'out', 'in'];
        
        // Direction shortcuts
        const dirMap = {
            'n': 'north', 's': 'south', 'e': 'east', 'w': 'west',
            'u': 'up', 'd': 'down',
            'ne': 'northeast', 'nw': 'northwest', 
            'se': 'southeast', 'sw': 'southwest'
        };
        
        if (directions.includes(cmd)) {
            return this.go(dirMap[cmd] || cmd);
        }
        
        if (cmd === 'go' && args) {
            return this.go(args);
        }
        
        // Look commands
        if (['look', 'l'].includes(cmd)) {
            if (args) {
                // Look at specific thing
                if (this.room?.exits?.[args.toLowerCase()]) {
                    return this.examineExit(args);
                }
                return `You don't see "${args}" here.`;
            }
            return this.look();
        }
        
        // Examine
        if (['examine', 'x', 'ex'].includes(cmd)) {
            if (!args) return 'Examine what?';
            if (this.room?.exits?.[args.toLowerCase()]) {
                return this.examineExit(args);
            }
            return `You don't see "${args}" here.`;
        }
        
        // Inventory
        if (['inventory', 'inv', 'i'].includes(cmd)) {
            if (this.player.inventory.length === 0) {
                return 'You are empty-handed.';
            }
            return 'You are carrying:\n' + 
                this.player.inventory.map(id => {
                    const obj = this.get(id);
                    return `  • ${obj?.name || id}`;
                }).join('\n');
        }
        
        // Help
        if (['help', '?'].includes(cmd)) {
            return `
MOOTAL DISTORTION — Commands

Navigation:
  NORTH, SOUTH, EAST, WEST, UP, DOWN (or N, S, E, W, U, D)
  GO <direction>
  
Look:
  LOOK (or L) — Describe current room
  LOOK <exit> — Describe an exit in detail
  EXAMINE <thing> (or X) — Look at something closely
  
Other:
  INVENTORY (or I) — See what you're carrying
  HELP (or ?) — This message

"Sheepy enough, but not too sheepy."
            `.trim();
        }
        
        return `I don't understand "${input}". Type HELP for commands.`;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // UI INTEGRATION
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Mount to a DOM element
     */
    mount(containerId) {
        const container = typeof containerId === 'string' 
            ? document.getElementById(containerId) 
            : containerId;
        
        if (!container) {
            console.error('Container not found:', containerId);
            return this;
        }
        
        container.innerHTML = `
            <div class="mootal-output" id="mootal-output"></div>
            <div class="mootal-input-row">
                <span class="mootal-prompt">&gt;</span>
                <input type="text" id="mootal-input" placeholder="What do you do?" autofocus>
            </div>
        `;
        
        this.ui = {
            output: document.getElementById('mootal-output'),
            input: document.getElementById('mootal-input')
        };
        
        // Handle input
        this.ui.input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                const input = this.ui.input.value.trim();
                if (input) {
                    this.print(`> ${input}`, 'command');
                    const result = this.command(input);
                    this.print(result, 'response');
                    this.ui.input.value = '';
                }
            }
        });
        
        return this;
    }
    
    /**
     * Print to output
     */
    print(text, type = 'response') {
        if (!this.ui?.output) {
            console.log(text);
            return;
        }
        
        const div = document.createElement('div');
        div.className = `mootal-line mootal-${type}`;
        div.textContent = text;
        this.ui.output.appendChild(div);
        this.ui.output.scrollTop = this.ui.output.scrollHeight;
    }
    
    /**
     * Start the game (show initial room)
     */
    start() {
        this.print(this.look(), 'room');
        if (this.ui?.input) {
            this.ui.input.focus();
        }
        return this;
    }
}

// Export for module and global use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { MootalEngine };
}
if (typeof window !== 'undefined') {
    window.MootalEngine = MootalEngine;
}
