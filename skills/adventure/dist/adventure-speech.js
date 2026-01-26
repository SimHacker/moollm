/**
 * adventure-speech.js — Speech Integration for MOOLLM Adventure Runtime
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Adds text-to-speech capabilities to the adventure engine.
 * Requires: adventure.js, speech.js
 * 
 * Features:
 * - Speaks room descriptions when entering
 * - Speaks responses to commands
 * - Character-specific voices that persist
 * - Robot voices for AI/machine characters
 * - Effect voices for magical/supernatural events
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

/**
 * SpeechAdapter — UI Adapter with speech synthesis
 * 
 * Extends DOMAdapter to add speaking capabilities
 */
class SpeechAdapter extends DOMAdapter {
    constructor(containerId = 'adventure', speechOptions = {}) {
        super(containerId);
        
        this.speech = null;
        this.speechEnabled = speechOptions.enabled !== false;
        this.speakRooms = speechOptions.speakRooms !== false;
        this.speakResponses = speechOptions.speakResponses !== false;
        this.speakCommands = speechOptions.speakCommands || false;
        this.characterVoices = new Map(); // Character ID -> Voice
        
        // Default voice preferences
        this.defaultVoiceType = speechOptions.defaultVoiceType || 'any';
        this.defaultLanguage = speechOptions.defaultLanguage || 'en';
        
        // ═══════════════════════════════════════════════════════════════════════
        // NARRATOR VOICE — The "cool" voice for room descriptions and narration
        // ═══════════════════════════════════════════════════════════════════════
        this.narratorVoice = null;
        this.narratorConfig = speechOptions.narrator || {
            // Preferred voices in order (macOS dramatic voices)
            preferred: ['Bad News', 'Daniel', 'Alex'],
            // Fallback criteria if preferred not available
            fallback: { gender: 'male', type: 'human', language: 'en' },
            // Voice parameters for narrator
            pitch: 0.9,      // Slightly deeper
            rate: 0.95,      // Slightly slower, more deliberate
            volume: 1.0
        };
        
        // Initialize speech system
        this._initSpeech();
    }
    
    async _initSpeech() {
        if (typeof SpeechSystem !== 'undefined') {
            this.speech = new SpeechSystem();
            await this.speech.ready;
            console.log('🔊 Speech system initialized');
            
            // Initialize narrator voice
            this._initNarratorVoice();
        } else {
            console.warn('🔇 SpeechSystem not loaded - speech disabled');
            this.speechEnabled = false;
        }
    }
    
    /**
     * Initialize the narrator voice — tries preferred voices, falls back to criteria
     */
    _initNarratorVoice() {
        if (!this.speech) return;
        
        const voices = window.speechSynthesis.getVoices();
        const config = this.narratorConfig;
        
        // Try preferred voices in order
        for (const preferred of config.preferred || []) {
            const voice = voices.find(v => 
                v.name === preferred || 
                v.name.startsWith(preferred + ' ') ||
                v.name.includes(preferred)
            );
            if (voice) {
                this.narratorVoice = voice;
                console.log(`🎭 Narrator voice: ${voice.name}`);
                return;
            }
        }
        
        // Fallback to criteria-based selection
        if (config.fallback) {
            const match = this.speech.voiceDB.getRandomVoice(config.fallback);
            if (match) {
                this.narratorVoice = match.voice;
                console.log(`🎭 Narrator voice (fallback): ${match.voice.name}`);
                return;
            }
        }
        
        // Last resort: any English voice
        const anyEnglish = voices.find(v => v.lang && v.lang.startsWith('en'));
        if (anyEnglish) {
            this.narratorVoice = anyEnglish;
            console.log(`🎭 Narrator voice (default): ${anyEnglish.name}`);
        }
    }
    
    /**
     * Speak as the narrator (room descriptions, system messages)
     */
    speakAsNarrator(text, options = {}) {
        if (!this.speechEnabled || !this.speech) return;
        
        const config = this.narratorConfig;
        
        if (this.narratorVoice) {
            this.speech.speakWithVoice(text, this.narratorVoice, {
                pitch: config.pitch || 0.9,
                rate: config.rate || 0.95,
                volume: config.volume || 1.0,
                ...options
            });
        } else {
            // No narrator voice, use default male
            this.speech.speakMale(text, {
                pitch: 0.9,
                rate: 0.95,
                ...options
            });
        }
    }
    
    onLoad(world) {
        super.onLoad(world);
        
        // Add speech controls to UI
        if (this.container && this.speechEnabled) {
            this._addSpeechControls();
        }
    }
    
    _addSpeechControls() {
        const controls = document.createElement('div');
        controls.className = 'adventure-speech-controls';
        controls.innerHTML = `
            <button id="adventure-speech-toggle" title="Toggle Speech">
                🔊
            </button>
            <button id="adventure-speech-stop" title="Stop Speaking">
                ⏹️
            </button>
        `;
        
        this.container.prepend(controls);
        
        // Wire up controls
        document.getElementById('adventure-speech-toggle')?.addEventListener('click', () => {
            this.speechEnabled = !this.speechEnabled;
            const btn = document.getElementById('adventure-speech-toggle');
            if (btn) btn.textContent = this.speechEnabled ? '🔊' : '🔇';
            if (!this.speechEnabled && this.speech) {
                this.speech.cancel();
            }
        });
        
        document.getElementById('adventure-speech-stop')?.addEventListener('click', () => {
            if (this.speech) this.speech.cancel();
        });
    }
    
    /**
     * Speak text with optional character voice
     */
    speak(text, options = {}) {
        if (!this.speechEnabled || !this.speech) return;
        
        // Check for character voice
        if (options.character) {
            const voice = this._getCharacterVoice(options.character);
            const params = this._getCharacterVoiceParams(options.character);
            if (voice) {
                this.speech.speakWithVoice(text, voice, {
                    pitch: params.pitch || options.pitch || 1.0,
                    rate: params.rate || options.rate || 1.0,
                    volume: params.volume || options.volume || 1.0,
                    ...options
                });
                return;
            }
        }
        
        // Use type-based speaking
        const voiceType = options.voiceType || this.defaultVoiceType;
        
        switch (voiceType) {
            case 'narrator':
                this.speakAsNarrator(text, options);
                break;
            case 'robot':
                this.speech.speakRobot(text, options);
                break;
            case 'effect':
                this.speech.speakEffect(text, options);
                break;
            case 'male':
                this.speech.speakMale(text, options);
                break;
            case 'female':
                this.speech.speakFemale(text, options);
                break;
            case 'child':
                this.speech.speakChild(text, options);
                break;
            case 'elderly':
                this.speech.speakElderly(text, options);
                break;
            default:
                this.speech.speak(text, { 
                    ...options, 
                    language: options.language || this.defaultLanguage 
                });
        }
    }
    
    /**
     * Get or create a voice for a character
     * 
     * Characters can define voice preferences in their YAML:
     * 
     *   speech:
     *     preferred: "Bad News"        # Try this voice first
     *     fallback: "Ralph"            # Try this if preferred unavailable
     *     type: effect                 # Or: human, robot
     *     gender: male                 # Or: female, neutral
     *     age: adult                   # Or: child, elderly
     *     language: en                 # Language code
     *   params:
     *     pitch: 0.7                   # Voice pitch (0.5 - 2.0)
     *     rate: 0.9                    # Speech rate (0.5 - 2.0)
     *     volume: 1.0                  # Volume (0.0 - 1.0)
     */
    _getCharacterVoice(character) {
        const id = character.id || character;
        
        // Return cached voice if we have one
        if (this.characterVoices.has(id)) {
            return this.characterVoices.get(id);
        }
        
        const voices = window.speechSynthesis.getVoices();
        let voice = null;
        
        // Character has explicit speech configuration
        if (character.speech) {
            const speechConfig = character.speech;
            
            // Try preferred voice by name
            if (speechConfig.preferred) {
                voice = voices.find(v => 
                    v.name === speechConfig.preferred ||
                    v.name.startsWith(speechConfig.preferred + ' ') ||
                    v.name.includes(speechConfig.preferred)
                );
            }
            
            // Try fallback voice by name
            if (!voice && speechConfig.fallback) {
                voice = voices.find(v => 
                    v.name === speechConfig.fallback ||
                    v.name.startsWith(speechConfig.fallback + ' ') ||
                    v.name.includes(speechConfig.fallback)
                );
            }
            
            // Try criteria-based selection
            if (!voice) {
                const criteria = {};
                if (speechConfig.type) criteria.type = speechConfig.type;
                if (speechConfig.gender) criteria.gender = speechConfig.gender;
                if (speechConfig.age) criteria.age = speechConfig.age;
                if (speechConfig.language) criteria.language = speechConfig.language;
                
                if (Object.keys(criteria).length > 0) {
                    const match = this.speech.voiceDB.getRandomVoice(criteria);
                    if (match) voice = match.voice;
                }
            }
        }
        
        // Legacy voice property (simple criteria object)
        if (!voice && character.voice) {
            if (typeof character.voice === 'string') {
                // Voice name directly
                voice = voices.find(v => v.name.includes(character.voice));
            } else {
                // Criteria object
                const match = this.speech.voiceDB.getRandomVoice(character.voice);
                if (match) voice = match.voice;
            }
        }
        
        // Infer from character type
        if (!voice) {
            if (character.type === 'robot' || character.type === 'ai' || character.type === 'machine') {
                const match = this.speech.voiceDB.getRandomVoice({ type: 'robot' });
                if (match) voice = match.voice;
            } else if (character.type === 'plant' || character.type === 'monster') {
                const match = this.speech.voiceDB.getRandomVoice({ type: 'effect' });
                if (match) voice = match.voice;
            }
        }
        
        // Infer from gender
        if (!voice && character.gender) {
            const match = this.speech.voiceDB.getRandomVoice({ 
                gender: character.gender,
                type: 'human'
            });
            if (match) voice = match.voice;
        }
        
        // Last resort: random voice (but consistent per character)
        if (!voice) {
            // Use character ID to seed selection for consistency
            const hash = this._hashString(id);
            const index = hash % voices.length;
            voice = voices[index];
        }
        
        // Cache the voice
        if (voice) {
            this.characterVoices.set(id, {
                voice: voice,
                params: character.params || character.speech?.params || {}
            });
            console.log(`🎭 Character "${id}" voice: ${voice.name}`);
        }
        
        return voice;
    }
    
    /**
     * Simple string hash for consistent voice assignment
     */
    _hashString(str) {
        let hash = 0;
        for (let i = 0; i < str.length; i++) {
            const char = str.charCodeAt(i);
            hash = ((hash << 5) - hash) + char;
            hash = hash & hash; // Convert to 32-bit integer
        }
        return Math.abs(hash);
    }
    
    /**
     * Get voice parameters for a character
     */
    _getCharacterVoiceParams(character) {
        const id = character.id || character;
        const cached = this.characterVoices.get(id);
        
        if (cached && cached.params) {
            return cached.params;
        }
        
        // Return from character config
        return character.params || character.speech?.params || {};
    }
    
    /**
     * Override print to add speech
     */
    print(text, type = 'response') {
        super.print(text, type);
        
        if (!this.speechEnabled || !this.speech) return;
        
        // Speak based on type
        if (type === 'room' && this.speakRooms) {
            // Room descriptions use narrator voice
            this.speakAsNarrator(text);
        } else if (type === 'narration' && this.speakResponses) {
            // Explicit narration also uses narrator
            this.speakAsNarrator(text);
        } else if (type === 'response' && this.speakResponses) {
            // Generic responses use narrator too
            this.speakAsNarrator(text);
        } else if (type === 'command' && this.speakCommands) {
            this.speak(text, { rate: 1.2 });
        }
    }
    
    /**
     * Print room description with narrator voice
     */
    printRoom(room) {
        super.printRoom(room);
        
        if (!this.speechEnabled || !this.speech || !this.speakRooms) return;
        
        // Room descriptions are always read by the narrator
        this.speakAsNarrator(room.describe());
    }
    
    /**
     * Speak a character's dialogue with their unique voice
     */
    printDialogue(character, text) {
        // Print to screen
        const name = character.name || character.id || 'Unknown';
        super.print(`${name}: "${text}"`, 'dialogue');
        
        // Speak with character's voice
        if (this.speechEnabled && this.speech) {
            const voice = this._getCharacterVoice(character);
            const params = this._getCharacterVoiceParams(character);
            
            if (voice) {
                this.speech.speakWithVoice(text, voice, {
                    pitch: params.pitch || 1.0,
                    rate: params.rate || 1.0,
                    volume: params.volume || 1.0
                });
            } else {
                // Fallback to generic speak
                this.speak(text);
            }
        }
    }
    
    /**
     * Have a character sing (slower, more dramatic)
     */
    printSinging(character, lyrics, options = {}) {
        const name = character.name || character.id || 'Unknown';
        super.print(`${name} sings: "${lyrics}"`, 'singing');
        
        if (this.speechEnabled && this.speech) {
            // Use singing voice if defined, otherwise regular voice
            const speechConfig = character.speech || {};
            const singingConfig = character.singing_voice || speechConfig;
            
            let voice = null;
            const voices = window.speechSynthesis.getVoices();
            
            // Try singing-specific preferred voice
            if (singingConfig.preferred) {
                voice = voices.find(v => v.name.includes(singingConfig.preferred));
            }
            
            // Fall back to character's regular voice
            if (!voice) {
                voice = this._getCharacterVoice(character);
            }
            
            // Singing parameters (slower, more expressive)
            const singingParams = character.singing_params || {};
            
            if (voice) {
                this.speech.speakWithVoice(lyrics, voice, {
                    pitch: singingParams.pitch || 1.0,
                    rate: singingParams.rate || 0.75,  // Slower for singing
                    volume: singingParams.volume || 1.0,
                    ...options
                });
            }
        }
    }
    
    /**
     * Clean up
     */
    destroy() {
        if (this.speech) {
            this.speech.cancel();
        }
        super.destroy();
    }
}

/**
 * Create a speaking adventure engine
 * 
 * Options:
 *   speechEnabled: true/false — enable speech (default: true)
 *   speakRooms: true/false — speak room descriptions (default: true)
 *   speakResponses: true/false — speak command responses (default: true)
 *   speakCommands: true/false — echo commands aloud (default: false)
 *   defaultVoiceType: 'any'|'male'|'female'|... — default voice type
 *   defaultLanguage: 'en' — default language
 *   narrator: {
 *     preferred: ['Bad News', 'Daniel'] — try these voices first
 *     fallback: { gender: 'male', ... } — criteria if preferred unavailable
 *     pitch: 0.9 — narrator pitch
 *     rate: 0.95 — narrator rate
 *   }
 */
function createSpeakingAdventure(containerId = 'adventure', options = {}) {
    const adapter = new SpeechAdapter(containerId, {
        enabled: options.speechEnabled !== false,
        speakRooms: options.speakRooms !== false,
        speakResponses: options.speakResponses !== false,
        speakCommands: options.speakCommands || false,
        defaultVoiceType: options.defaultVoiceType,
        defaultLanguage: options.defaultLanguage,
        narrator: options.narrator || {
            // Default to dramatic "Bad News" voice on macOS, or deep male
            preferred: ['Bad News', 'Daniel', 'Alex', 'Ralph'],
            fallback: { gender: 'male', type: 'human', language: 'en' },
            pitch: 0.9,
            rate: 0.95
        }
    });
    
    const engine = new AdventureEngine(adapter);
    
    // Expose speech system on engine
    engine.speech = adapter.speech;
    engine.speechAdapter = adapter;
    
    // Add speak methods to engine
    engine.speak = (text, options) => adapter.speak(text, options);
    engine.speakAsNarrator = (text, options) => adapter.speakAsNarrator(text, options);
    engine.printDialogue = (character, text) => adapter.printDialogue(character, text);
    engine.printSinging = (character, lyrics, options) => adapter.printSinging(character, lyrics, options);
    
    return engine;
}

// ═══════════════════════════════════════════════════════════════════════════════
// DEFAULT NARRATOR CONFIGURATIONS
// ═══════════════════════════════════════════════════════════════════════════════

const NARRATOR_PRESETS = {
    // Dramatic narrator (default) — deep, slow, atmospheric
    dramatic: {
        preferred: ['Bad News', 'Daniel', 'Alex'],
        fallback: { gender: 'male', type: 'human', language: 'en' },
        pitch: 0.85,
        rate: 0.9
    },
    
    // Neutral narrator — clear, even-paced
    neutral: {
        preferred: ['Daniel', 'Samantha', 'Alex'],
        fallback: { type: 'human', language: 'en' },
        pitch: 1.0,
        rate: 1.0
    },
    
    // Whispery narrator — mysterious, soft
    mysterious: {
        preferred: ['Whisper', 'Samantha'],
        fallback: { gender: 'female', type: 'human', language: 'en' },
        pitch: 1.1,
        rate: 0.85
    },
    
    // Robot narrator — for sci-fi adventures
    robotic: {
        preferred: ['Zarvox', 'Trinoids'],
        fallback: { type: 'robot' },
        pitch: 1.0,
        rate: 0.95
    },
    
    // Cheerful narrator — upbeat, faster
    cheerful: {
        preferred: ['Good News', 'Samantha'],
        fallback: { gender: 'female', type: 'human', language: 'en' },
        pitch: 1.15,
        rate: 1.1
    },
    
    // British narrator — distinguished, proper
    british: {
        preferred: ['Daniel', 'Kate', 'Oliver'],
        fallback: { type: 'human', language: 'en-GB' },
        pitch: 0.95,
        rate: 0.95
    }
};

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const ADVENTURE_SPEECH_EXPORTS = {
    SpeechAdapter,
    createSpeakingAdventure,
    NARRATOR_PRESETS
};

// Browser: attach to window
if (typeof window !== 'undefined') {
    window.SpeechAdapter = SpeechAdapter;
    window.createSpeakingAdventure = createSpeakingAdventure;
    window.NARRATOR_PRESETS = NARRATOR_PRESETS;
    
    // Merge into Adventure namespace if exists
    if (window.Adventure) {
        Object.assign(window.Adventure, ADVENTURE_SPEECH_EXPORTS);
    }
}

// Node.js CommonJS
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ADVENTURE_SPEECH_EXPORTS;
}
