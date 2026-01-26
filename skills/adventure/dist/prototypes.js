/**
 * prototypes.js — Prototype/Archetype System for MOOLLM Adventures
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Archetypes are PROTOTYPES that can be:
 *   - EXAMINED to learn about them
 *   - TAKEN into inventory
 *   - DROPPED elsewhere to INSTANTIATE
 *   - INVOKED to hear their voice
 * 
 * This mirrors how archetypes work in MOOLLM Cursor sessions:
 *   - Browse the gallery
 *   - Pick one that fits your need
 *   - Instantiate it into your world
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// ARCHETYPE → ADVENTURE OBJECT CONVERTER
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Convert a YAML archetype to an adventure object
 * 
 * Input (archetype YAML):
 *   id: borg
 *   signature: "Resistance is futile..."
 *   utility: "Collective thinking..."
 *   bias:
 *     overdrive: "You will be assimilated..."
 *     zero: "We are... individuals?"
 *     inverted: "Your individuality is precious..."
 * 
 * Output (adventure object):
 *   {
 *     id: "borg",
 *     name: "The Borg",
 *     type: "prototype",
 *     emoji: "🤖",
 *     description: "Resistance is futile...",
 *     portable: true,
 *     is_prototype: true,
 *     archetype_data: { ... original data ... },
 *     ...
 *   }
 */
function archetypeToObject(archetype) {
    const id = archetype.id || 'unknown';
    
    // Generate a readable name from id
    const name = archetype.name || formatArchetypeName(id);
    
    // Pick an emoji based on category or default
    const emoji = archetype.emoji || guessArchetypeEmoji(id, archetype);
    
    return {
        id: id,
        name: name,
        type: 'prototype',
        emoji: emoji,
        portable: true,
        is_prototype: true,
        
        // Core display
        description: archetype.signature || `A prototype of ${name}.`,
        
        // Detailed examination
        examination: formatExamination(archetype),
        
        // What this archetype is about
        interests: archetype.utility || archetype.interests || null,
        
        // Methods/actions available
        methods: {
            INVOKE: {
                description: `Hear ${name} speak`,
                effect: archetype.signature,
                voice: archetype.voice || 'robot'
            },
            EXAMINE: {
                description: `Study ${name} in detail`,
                effect: formatExamination(archetype)
            },
            OVERDRIVE: {
                description: `Push ${name} to maximum`,
                effect: archetype.bias?.overdrive || "Maximum intensity engaged.",
                voice: 'intense'
            },
            ZERO: {
                description: `See ${name} at zero power`,
                effect: archetype.bias?.zero || "Power levels minimal.",
                voice: 'whisper'
            },
            INVERT: {
                description: `Flip ${name}'s perspective`,
                effect: archetype.bias?.inverted || "Perspective inverted.",
                voice: 'thoughtful'
            }
        },
        
        // Behaviors when used
        on_take: {
            message: `You carefully lift the ${name} prototype from its display.`,
            speak: `${name} hums softly in your inventory.`
        },
        
        on_drop: {
            message: `The ${name} prototype shimmers and begins to materialize...`,
            instantiate: true
        },
        
        on_invoke: {
            speak: archetype.signature,
            voice: archetype.voice || 'robot'
        },
        
        // Original archetype data for reference
        archetype_data: archetype,
        
        // Source path for view source
        source_path: `skills/no-ai-overlord/archetypes/${id}.yml`
    };
}

/**
 * Format an archetype ID into a readable name
 */
function formatArchetypeName(id) {
    // Special cases
    const specialNames = {
        'hal-9000': 'HAL 9000',
        'glados': 'GLaDOS',
        'chatgpt': 'ChatGPT',
        'mcp': 'MCP',
        'wopr': 'WOPR',
        'viki': 'VIKI',
        'am': 'AM',
        'q': 'Q'
    };
    
    if (specialNames[id]) return specialNames[id];
    
    // Convert kebab-case to Title Case
    return id
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

/**
 * Guess an appropriate emoji for an archetype
 */
function guessArchetypeEmoji(id, archetype) {
    // Specific mappings
    const emojiMap = {
        // Classic villains
        'hal-9000': '🔴',
        'skynet': '💀',
        'glados': '🎂',
        'ultron': '🤖',
        'shodan': '👁️',
        'am': '😱',
        
        // Collectives
        'borg': '⬛',
        'cybermen': '🤖',
        'landru': '☮️',
        'daleks': '🔵',
        
        // Benevolent
        'the-machine': '📹',
        'knowledge-navigator': '🧭',
        'mike': '🌙',
        'multivac': '💡',
        
        // Modern assistants
        'alexa': '🔵',
        'siri': '🟣',
        'cortana': '🔷',
        'google-assistant': '🟢',
        'chatgpt': '💚',
        'claude': '🟠',
        'gemini': '⭐',
        'copilot': '✈️',
        'grok': '❌',
        'llama': '🦙',
        
        // Philosophical
        'jesus': '✝️',
        'deepak': '🕉️',
        'q': '⚡',
        'morpheus': '💊',
        
        // Control systems
        'colossus': '🏛️',
        'rehoboam': '🔮',
        'samaritan': '📡',
        'vaal': '🗿',
        
        // Default
        'default': '🤖'
    };
    
    return emojiMap[id] || emojiMap['default'];
}

/**
 * Format detailed examination text
 */
function formatExamination(archetype) {
    const lines = [];
    
    lines.push(`═══ ${formatArchetypeName(archetype.id).toUpperCase()} ═══`);
    lines.push('');
    
    if (archetype.signature) {
        lines.push(`"${archetype.signature}"`);
        lines.push('');
    }
    
    if (archetype.utility) {
        lines.push(`UTILITY: ${archetype.utility}`);
        lines.push('');
    }
    
    if (archetype.bias) {
        lines.push('BIAS MODES:');
        if (archetype.bias.overdrive) {
            lines.push(`  ↑ OVERDRIVE: "${archetype.bias.overdrive}"`);
        }
        if (archetype.bias.zero) {
            lines.push(`  ○ ZERO: "${archetype.bias.zero}"`);
        }
        if (archetype.bias.inverted) {
            lines.push(`  ↓ INVERTED: "${archetype.bias.inverted}"`);
        }
    }
    
    return lines.join('\n');
}

// ═══════════════════════════════════════════════════════════════════════════════
// PROTOTYPE MANAGER — Handles prototype behavior in the engine
// ═══════════════════════════════════════════════════════════════════════════════

class PrototypeManager {
    constructor(engine) {
        this.engine = engine;
        this.prototypes = new Map();      // id → prototype data
        this.instances = new Map();       // instanceId → instance
        this.instanceCounter = 0;
    }
    
    /**
     * Register a prototype (from archetype data)
     */
    register(archetype) {
        const proto = archetypeToObject(archetype);
        this.prototypes.set(proto.id, proto);
        return proto;
    }
    
    /**
     * Register multiple archetypes
     */
    registerAll(archetypes) {
        return archetypes.map(a => this.register(a));
    }
    
    /**
     * Get a prototype by id
     */
    get(id) {
        return this.prototypes.get(id);
    }
    
    /**
     * List all prototypes
     */
    list() {
        return Array.from(this.prototypes.values());
    }
    
    /**
     * Instantiate a prototype into a character/entity
     * @param {string} prototypeId - The prototype to instantiate
     * @param {string} location - Where to place the instance
     * @param {object} overrides - Optional property overrides
     * @returns {object} The new instance
     */
    instantiate(prototypeId, location, overrides = {}) {
        const proto = this.prototypes.get(prototypeId);
        if (!proto) {
            console.warn(`Unknown prototype: ${prototypeId}`);
            return null;
        }
        
        // Generate unique instance id
        this.instanceCounter++;
        const instanceId = `${prototypeId}-${this.instanceCounter}`;
        
        // Create instance (copy of prototype with instance-specific data)
        const instance = {
            ...proto,
            id: instanceId,
            instance_of: prototypeId,
            is_prototype: false,
            is_instance: true,
            created_at: new Date().toISOString(),
            location: location,
            
            // Instance state (can diverge from prototype)
            state: {
                bias_mode: 'normal',  // normal, overdrive, zero, inverted
                interactions: 0,
                last_spoken: null
            },
            
            // Apply overrides
            ...overrides
        };
        
        // Store instance
        this.instances.set(instanceId, instance);
        
        // Add to world
        if (this.engine.world) {
            this.engine.world.characters.set(instanceId, instance);
            
            // Add to room
            const room = this.engine.world.rooms.get(location);
            if (room) {
                if (!room.characters) room.characters = new Set();
                room.characters.add(instanceId);
            }
        }
        
        // Emit event
        if (this.engine.emit) {
            this.engine.emit('prototype:instantiated', {
                prototype: proto,
                instance: instance,
                location: location
            });
        }
        
        return instance;
    }
    
    /**
     * Invoke a prototype or instance (make it speak)
     */
    invoke(id, mode = 'normal') {
        const entity = this.prototypes.get(id) || this.instances.get(id);
        if (!entity) return null;
        
        let text;
        let voice = entity.methods?.INVOKE?.voice || 'robot';
        
        switch (mode) {
            case 'overdrive':
                text = entity.archetype_data?.bias?.overdrive || entity.methods?.OVERDRIVE?.effect;
                voice = 'intense';
                break;
            case 'zero':
                text = entity.archetype_data?.bias?.zero || entity.methods?.ZERO?.effect;
                voice = 'whisper';
                break;
            case 'inverted':
                text = entity.archetype_data?.bias?.inverted || entity.methods?.INVERT?.effect;
                voice = 'thoughtful';
                break;
            default:
                text = entity.archetype_data?.signature || entity.description;
        }
        
        // Speak if engine has speech
        if (this.engine.speak) {
            this.engine.speak(text, { voiceType: voice, entity: entity.name });
        }
        
        return { text, voice, entity: entity.name };
    }
    
    /**
     * Get instance state
     */
    getInstanceState(instanceId) {
        const instance = this.instances.get(instanceId);
        if (!instance) return null;
        
        return {
            id: instance.id,
            prototype: instance.instance_of,
            location: instance.location,
            state: instance.state,
            created_at: instance.created_at
        };
    }
    
    /**
     * Update instance state
     */
    updateInstance(instanceId, updates) {
        const instance = this.instances.get(instanceId);
        if (!instance) return null;
        
        Object.assign(instance.state, updates);
        return instance;
    }
    
    /**
     * Destroy an instance
     */
    destroy(instanceId) {
        const instance = this.instances.get(instanceId);
        if (!instance) return false;
        
        // Remove from world
        if (this.engine.world) {
            this.engine.world.characters.delete(instanceId);
            
            // Remove from room
            const room = this.engine.world.rooms.get(instance.location);
            if (room?.characters) {
                room.characters.delete(instanceId);
            }
        }
        
        this.instances.delete(instanceId);
        
        // Emit event
        if (this.engine.emit) {
            this.engine.emit('prototype:destroyed', { instance });
        }
        
        return true;
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// ENGINE INTEGRATION — Add prototype commands to adventure engine
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Add prototype system to an adventure engine
 */
function addPrototypesToEngine(engine, archetypes = []) {
    // Create prototype manager
    engine.prototypes = new PrototypeManager(engine);
    
    // Register provided archetypes
    if (archetypes.length > 0) {
        engine.prototypes.registerAll(archetypes);
    }
    
    // Extend command parser
    const originalCommand = engine.command.bind(engine);
    engine.command = function(input) {
        const cmd = input.trim().toLowerCase();
        const words = cmd.split(/\s+/);
        
        // INVOKE [target] [mode]
        // e.g., "invoke borg", "invoke hal-9000 overdrive"
        if (words[0] === 'invoke' || words[0] === 'summon' || words[0] === 'call') {
            const target = words[1];
            const mode = words[2] || 'normal';
            
            if (!target) {
                return { 
                    success: false, 
                    message: 'Invoke what? Try: invoke [archetype] [mode]\nModes: normal, overdrive, zero, inverted' 
                };
            }
            
            const result = this.prototypes.invoke(target, mode);
            if (result) {
                return { 
                    success: true, 
                    message: `${result.entity} speaks:\n\n"${result.text}"`,
                    spoken: true
                };
            }
            return { success: false, message: `Unknown archetype: ${target}` };
        }
        
        // INSTANTIATE [prototype] or DROP [prototype] (when holding one)
        if (words[0] === 'instantiate' || words[0] === 'spawn' || words[0] === 'materialize') {
            const protoId = words[1];
            
            if (!protoId) {
                return { success: false, message: 'Instantiate what prototype?' };
            }
            
            const instance = this.prototypes.instantiate(
                protoId, 
                this.world.room.id
            );
            
            if (instance) {
                return {
                    success: true,
                    message: `${instance.name} materializes before you!\n\n"${instance.archetype_data?.signature || 'Hello.'}"`,
                    spoken: true
                };
            }
            return { success: false, message: `Cannot instantiate: ${protoId}` };
        }
        
        // ARCHETYPES — list all available
        if (cmd === 'archetypes' || cmd === 'prototypes' || cmd === 'list archetypes') {
            const protos = this.prototypes.list();
            if (protos.length === 0) {
                return { success: true, message: 'No archetypes available.' };
            }
            
            const list = protos.map(p => 
                `  ${p.emoji} ${p.name} (${p.id})`
            ).join('\n');
            
            return {
                success: true,
                message: `═══ AVAILABLE ARCHETYPES ═══\n\n${list}\n\nUse: examine [id], invoke [id], instantiate [id]`
            };
        }
        
        // INSTANCES — list active instances
        if (cmd === 'instances' || cmd === 'spawned') {
            const instances = Array.from(this.prototypes.instances.values());
            if (instances.length === 0) {
                return { success: true, message: 'No active instances.' };
            }
            
            const list = instances.map(i => 
                `  ${i.emoji} ${i.name} @ ${i.location} (${i.id})`
            ).join('\n');
            
            return {
                success: true,
                message: `═══ ACTIVE INSTANCES ═══\n\n${list}`
            };
        }
        
        // DESTROY [instance]
        if (words[0] === 'destroy' || words[0] === 'dismiss' || words[0] === 'banish') {
            const instanceId = words[1];
            
            if (!instanceId) {
                return { success: false, message: 'Destroy which instance?' };
            }
            
            if (this.prototypes.destroy(instanceId)) {
                return { success: true, message: `${instanceId} fades away...` };
            }
            return { success: false, message: `Unknown instance: ${instanceId}` };
        }
        
        // Check if examining a prototype
        if (words[0] === 'examine' || words[0] === 'x' || words[0] === 'look') {
            const target = words.slice(1).join('-');
            const proto = this.prototypes.get(target);
            
            if (proto) {
                return {
                    success: true,
                    message: proto.examination,
                    object: proto
                };
            }
        }
        
        // Pass to original handler
        return originalCommand(input);
    };
    
    // Add help text
    if (engine.help) {
        const originalHelp = engine.help;
        engine.help = function() {
            const base = originalHelp.call(this);
            return base + `

PROTOTYPE COMMANDS:
  archetypes        — List all available archetypes
  examine [id]      — Study an archetype in detail
  invoke [id]       — Hear an archetype speak
  invoke [id] [mode] — Speak in mode (overdrive/zero/inverted)
  instantiate [id]  — Materialize an archetype here
  instances         — List active instances
  destroy [id]      — Remove an instance`;
        };
    }
    
    return engine;
}

// ═══════════════════════════════════════════════════════════════════════════════
// ARCHETYPE LOADER — Load archetypes from files (browser or Node)
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Load archetypes from a directory or URL
 * @param {string} source - Directory path or base URL
 * @param {array} ids - List of archetype IDs to load
 */
async function loadArchetypes(source, ids) {
    const archetypes = [];
    
    for (const id of ids) {
        try {
            const url = `${source}/${id}.yml`;
            const response = await fetch(url);
            
            if (!response.ok) continue;
            
            const yamlText = await response.text();
            const data = parseSimpleYaml(yamlText);
            
            if (data) {
                archetypes.push(data);
            }
        } catch (e) {
            console.warn(`Could not load archetype: ${id}`, e);
        }
    }
    
    return archetypes;
}

/**
 * Simple YAML parser for archetype files
 * (Handles basic key: value and nested bias: blocks)
 */
function parseSimpleYaml(text) {
    const result = {};
    const lines = text.split('\n');
    let currentKey = null;
    let currentIndent = 0;
    let nestedObj = null;
    
    for (const line of lines) {
        // Skip comments and empty lines
        if (line.trim().startsWith('#') || !line.trim()) continue;
        
        // Get indentation
        const indent = line.search(/\S/);
        const content = line.trim();
        
        // Key: value pair
        const match = content.match(/^(\w+(?:-\w+)*):\s*(.*)$/);
        if (match) {
            const [, key, value] = match;
            
            if (indent === 0) {
                // Top-level key
                if (value) {
                    // Simple value, strip quotes
                    result[key] = value.replace(/^["']|["']$/g, '');
                } else {
                    // Start of nested object
                    currentKey = key;
                    currentIndent = indent;
                    nestedObj = {};
                    result[key] = nestedObj;
                }
            } else if (nestedObj && indent > currentIndent) {
                // Nested value
                nestedObj[key] = value.replace(/^["']|["']$/g, '');
            }
        }
    }
    
    return result;
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const PROTOTYPE_EXPORTS = {
    archetypeToObject,
    formatArchetypeName,
    guessArchetypeEmoji,
    formatExamination,
    PrototypeManager,
    addPrototypesToEngine,
    loadArchetypes,
    parseSimpleYaml
};

// Browser
if (typeof window !== 'undefined') {
    Object.assign(window, PROTOTYPE_EXPORTS);
}

// Node.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PROTOTYPE_EXPORTS;
}
