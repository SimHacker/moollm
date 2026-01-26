/**
 * recognition.js — Speech Recognition for MOOLLM Adventure
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Parallel to speech.js (synthesis), this handles speech-to-text.
 * 
 * Supports:
 * - Web Speech API (Chrome, Safari)
 * - Guidance for native platform speech recognition
 * - Event-driven architecture with callbacks
 * - Configurable options
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// PLATFORM DETECTION
// ═══════════════════════════════════════════════════════════════════════════════

const RecognitionPlatform = {
    /**
     * Detect current platform and browser
     */
    detect() {
        const ua = navigator.userAgent;
        const platform = navigator.platform || '';
        
        return {
            // OS
            isMac: /Mac/.test(platform),
            isWindows: /Win/.test(platform),
            isLinux: /Linux/.test(platform),
            isIOS: /iPhone|iPad|iPod/.test(ua),
            isAndroid: /Android/.test(ua),
            
            // Browser
            isChrome: /Chrome/.test(ua) && !/Edg/.test(ua),
            isSafari: /Safari/.test(ua) && !/Chrome/.test(ua),
            isFirefox: /Firefox/.test(ua),
            isEdge: /Edg/.test(ua),
            
            // Capabilities
            hasWebSpeechAPI: !!(window.SpeechRecognition || window.webkitSpeechRecognition),
            
            // Privacy implications
            get privacyNote() {
                if (this.isChrome) return '⚠️ Chrome sends audio to Google servers';
                if (this.isSafari) return 'Safari may process on-device (check settings)';
                return null;
            }
        };
    },
    
    /**
     * Get native speech recognition instructions for current platform
     */
    getNativeInstructions() {
        const p = this.detect();
        
        if (p.isMac || p.isIOS) {
            return {
                platform: 'macOS/iOS',
                name: 'Dictation',
                activation: 'Press Fn twice (or key set in System Settings)',
                setup: [
                    'System Settings → Keyboard → Dictation',
                    'Turn ON Dictation',
                    'Choose language',
                    'Optional: Enable "Enhanced Dictation" for offline'
                ],
                shortcut: 'Fn Fn (double-tap Function key)',
                voiceControl: {
                    name: 'Voice Control',
                    path: 'System Settings → Accessibility → Voice Control',
                    note: 'Full voice commands, replaces Dictation when enabled'
                }
            };
        }
        
        if (p.isWindows) {
            return {
                platform: 'Windows',
                name: 'Windows Speech Recognition',
                activation: 'Win + H',
                setup: [
                    'Settings → Time & Language → Speech',
                    'Enable "Speech Recognition"',
                    'Train your voice (optional but recommended)'
                ],
                shortcut: 'Win + H',
                voiceControl: {
                    name: 'Voice Access',
                    path: 'Settings → Accessibility → Voice Access',
                    note: 'Full voice control (Windows 11)'
                }
            };
        }
        
        if (p.isAndroid) {
            return {
                platform: 'Android',
                name: 'Google Voice Typing',
                activation: 'Tap microphone on keyboard',
                setup: [
                    'Settings → System → Languages & input',
                    'On-screen keyboard → Gboard → Voice typing',
                    'Enable "Use voice typing"'
                ],
                shortcut: '🎤 (microphone icon on keyboard)'
            };
        }
        
        if (p.isLinux) {
            return {
                platform: 'Linux',
                name: 'Various',
                options: [
                    { name: 'Whisper', note: 'Best quality, local, offline' },
                    { name: 'Vosk', note: 'Lightweight, offline' },
                    { name: 'GNOME Speech', note: 'Desktop integration' }
                ],
                setup: ['Install preferred speech recognition engine']
            };
        }
        
        return {
            platform: 'Unknown',
            name: 'Platform speech recognition',
            setup: ['Check your system accessibility settings']
        };
    }
};

// ═══════════════════════════════════════════════════════════════════════════════
// RECOGNITION EVENTS — Event types for callbacks
// ═══════════════════════════════════════════════════════════════════════════════

const RecognitionEvents = {
    // Lifecycle
    READY: 'ready',
    START: 'start',
    STOP: 'stop',
    END: 'end',
    
    // Results
    RESULT: 'result',           // Final result
    INTERIM: 'interim',         // Partial result (while speaking)
    
    // Audio
    AUDIO_START: 'audiostart',
    AUDIO_END: 'audioend',
    SOUND_START: 'soundstart',
    SOUND_END: 'soundend',
    SPEECH_START: 'speechstart',
    SPEECH_END: 'speechend',
    
    // Errors
    ERROR: 'error',
    NO_MATCH: 'nomatch',
    
    // Service
    SERVICE_CHANGE: 'servicechange'
};

// ═══════════════════════════════════════════════════════════════════════════════
// RECOGNITION MANAGER — Core speech recognition handler
// ═══════════════════════════════════════════════════════════════════════════════

class RecognitionManager {
    constructor(options = {}) {
        // Options
        this.options = {
            language: options.language || 'en-US',
            continuous: options.continuous ?? false,      // Keep listening after result
            interimResults: options.interimResults ?? true, // Show partial results
            maxAlternatives: options.maxAlternatives || 1,
            ...options
        };
        
        // State
        this.isListening = false;
        this.isPaused = false;
        this.recognition = null;
        this.service = 'none';  // 'browser', 'native', 'none'
        
        // Event listeners
        this._listeners = new Map();
        
        // Platform info
        this.platform = RecognitionPlatform.detect();
        
        // Initialize
        this._init();
    }
    
    /**
     * Initialize speech recognition
     */
    _init() {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        
        if (SpeechRecognition) {
            this.recognition = new SpeechRecognition();
            this._setupRecognition();
            this.service = 'browser';
            this._emit(RecognitionEvents.READY, { service: 'browser' });
        } else {
            this.service = 'none';
            this._emit(RecognitionEvents.READY, { 
                service: 'none',
                reason: this._getUnsupportedReason()
            });
        }
    }
    
    /**
     * Get reason for lack of support
     */
    _getUnsupportedReason() {
        if (this.platform.isFirefox) {
            return 'Firefox: Speech Recognition disabled by default. Enable in about:config (media.webspeech.recognition.enable)';
        }
        if (this.platform.isEdge) {
            return 'Edge: Speech Recognition not supported';
        }
        return 'Browser does not support Web Speech API';
    }
    
    /**
     * Setup recognition event handlers
     */
    _setupRecognition() {
        if (!this.recognition) return;
        
        // Apply options
        this.recognition.lang = this.options.language;
        this.recognition.continuous = this.options.continuous;
        this.recognition.interimResults = this.options.interimResults;
        this.recognition.maxAlternatives = this.options.maxAlternatives;
        
        // Wire up events
        this.recognition.onstart = () => {
            this.isListening = true;
            this._emit(RecognitionEvents.START);
        };
        
        this.recognition.onend = () => {
            this.isListening = false;
            this._emit(RecognitionEvents.END);
            
            // Auto-restart if continuous and not manually stopped
            if (this.options.continuous && !this.isPaused) {
                this._restartRecognition();
            }
        };
        
        this.recognition.onresult = (event) => {
            this._handleResult(event);
        };
        
        this.recognition.onerror = (event) => {
            this._emit(RecognitionEvents.ERROR, {
                error: event.error,
                message: this._getErrorMessage(event.error)
            });
        };
        
        this.recognition.onnomatch = () => {
            this._emit(RecognitionEvents.NO_MATCH);
        };
        
        this.recognition.onaudiostart = () => this._emit(RecognitionEvents.AUDIO_START);
        this.recognition.onaudioend = () => this._emit(RecognitionEvents.AUDIO_END);
        this.recognition.onsoundstart = () => this._emit(RecognitionEvents.SOUND_START);
        this.recognition.onsoundend = () => this._emit(RecognitionEvents.SOUND_END);
        this.recognition.onspeechstart = () => this._emit(RecognitionEvents.SPEECH_START);
        this.recognition.onspeechend = () => this._emit(RecognitionEvents.SPEECH_END);
    }
    
    /**
     * Handle recognition result
     */
    _handleResult(event) {
        const results = event.results;
        const lastResult = results[results.length - 1];
        
        const transcript = lastResult[0].transcript;
        const confidence = lastResult[0].confidence;
        const isFinal = lastResult.isFinal;
        
        // Get alternatives
        const alternatives = [];
        for (let i = 0; i < lastResult.length; i++) {
            alternatives.push({
                transcript: lastResult[i].transcript,
                confidence: lastResult[i].confidence
            });
        }
        
        if (isFinal) {
            this._emit(RecognitionEvents.RESULT, {
                transcript,
                confidence,
                alternatives,
                isFinal: true
            });
        } else {
            this._emit(RecognitionEvents.INTERIM, {
                transcript,
                confidence,
                isFinal: false
            });
        }
    }
    
    /**
     * Get human-readable error message
     */
    _getErrorMessage(error) {
        const messages = {
            'no-speech': 'No speech detected. Try speaking louder.',
            'audio-capture': 'No microphone found or access denied.',
            'not-allowed': 'Microphone permission denied. Check browser settings.',
            'network': 'Network error. Speech recognition requires internet (Chrome).',
            'aborted': 'Recognition aborted.',
            'service-not-allowed': 'Speech recognition service not allowed.',
            'bad-grammar': 'Grammar error in speech recognition.',
            'language-not-supported': `Language "${this.options.language}" not supported.`
        };
        return messages[error] || `Recognition error: ${error}`;
    }
    
    /**
     * Restart recognition (for continuous mode)
     */
    _restartRecognition() {
        if (this.recognition && !this.isPaused) {
            setTimeout(() => {
                try {
                    this.recognition.start();
                } catch (e) {
                    // Already started, ignore
                }
            }, 100);
        }
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // PUBLIC API
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Start listening
     */
    start() {
        if (!this.recognition) {
            this._emit(RecognitionEvents.ERROR, {
                error: 'not-supported',
                message: this._getUnsupportedReason()
            });
            return false;
        }
        
        try {
            this.isPaused = false;
            this.recognition.start();
            return true;
        } catch (e) {
            if (e.name === 'InvalidStateError') {
                // Already started
                return true;
            }
            this._emit(RecognitionEvents.ERROR, {
                error: 'start-failed',
                message: e.message
            });
            return false;
        }
    }
    
    /**
     * Stop listening
     */
    stop() {
        this.isPaused = true;
        if (this.recognition) {
            this.recognition.stop();
        }
        this._emit(RecognitionEvents.STOP);
    }
    
    /**
     * Abort listening (immediate stop, discard results)
     */
    abort() {
        this.isPaused = true;
        if (this.recognition) {
            this.recognition.abort();
        }
    }
    
    /**
     * Check if currently listening
     */
    get listening() {
        return this.isListening;
    }
    
    /**
     * Check if browser speech recognition is available
     */
    get supported() {
        return this.service === 'browser';
    }
    
    /**
     * Get privacy warning for current browser
     */
    get privacyWarning() {
        return this.platform.privacyNote;
    }
    
    /**
     * Get native platform instructions
     */
    get nativeInstructions() {
        return RecognitionPlatform.getNativeInstructions();
    }
    
    /**
     * Set language
     */
    setLanguage(lang) {
        this.options.language = lang;
        if (this.recognition) {
            this.recognition.lang = lang;
        }
    }
    
    /**
     * Set continuous mode
     */
    setContinuous(continuous) {
        this.options.continuous = continuous;
        if (this.recognition) {
            this.recognition.continuous = continuous;
        }
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // EVENT SYSTEM
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Add event listener
     */
    on(event, callback) {
        if (!this._listeners.has(event)) {
            this._listeners.set(event, new Set());
        }
        this._listeners.get(event).add(callback);
        return () => this.off(event, callback); // Return unsubscribe function
    }
    
    /**
     * Remove event listener
     */
    off(event, callback) {
        if (this._listeners.has(event)) {
            this._listeners.get(event).delete(callback);
        }
    }
    
    /**
     * Add one-time event listener
     */
    once(event, callback) {
        const wrapper = (...args) => {
            this.off(event, wrapper);
            callback(...args);
        };
        this.on(event, wrapper);
    }
    
    /**
     * Emit event
     */
    _emit(event, data = {}) {
        if (this._listeners.has(event)) {
            for (const callback of this._listeners.get(event)) {
                try {
                    callback({ type: event, ...data });
                } catch (e) {
                    console.error(`Error in ${event} listener:`, e);
                }
            }
        }
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// SPEECH RECOGNITION SYSTEM — High-level API (parallel to SpeechSystem)
// ═══════════════════════════════════════════════════════════════════════════════

class SpeechRecognitionSystem {
    constructor(options = {}) {
        this.manager = new RecognitionManager(options);
        this.platform = RecognitionPlatform.detect();
        
        // Convenience callbacks
        this.onResult = options.onResult || null;
        this.onInterim = options.onInterim || null;
        this.onError = options.onError || null;
        this.onStateChange = options.onStateChange || null;
        
        // Wire up callbacks
        this._setupCallbacks();
    }
    
    _setupCallbacks() {
        this.manager.on(RecognitionEvents.RESULT, (e) => {
            this.onResult?.(e.transcript, e);
        });
        
        this.manager.on(RecognitionEvents.INTERIM, (e) => {
            this.onInterim?.(e.transcript, e);
        });
        
        this.manager.on(RecognitionEvents.ERROR, (e) => {
            this.onError?.(e.message, e);
        });
        
        this.manager.on(RecognitionEvents.START, () => {
            this.onStateChange?.('listening');
        });
        
        this.manager.on(RecognitionEvents.END, () => {
            this.onStateChange?.('stopped');
        });
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // SIMPLE API
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Listen for a single phrase and return it
     * @returns {Promise<string>} The recognized text
     */
    listen() {
        return new Promise((resolve, reject) => {
            if (!this.manager.supported) {
                reject(new Error(this.manager._getUnsupportedReason()));
                return;
            }
            
            // Temporarily disable continuous mode for single listen
            const wasContinuous = this.manager.options.continuous;
            this.manager.setContinuous(false);
            
            const cleanup = () => {
                this.manager.off(RecognitionEvents.RESULT, onResult);
                this.manager.off(RecognitionEvents.ERROR, onError);
                this.manager.setContinuous(wasContinuous);
            };
            
            const onResult = (e) => {
                cleanup();
                resolve(e.transcript);
            };
            
            const onError = (e) => {
                cleanup();
                reject(new Error(e.message));
            };
            
            this.manager.on(RecognitionEvents.RESULT, onResult);
            this.manager.on(RecognitionEvents.ERROR, onError);
            
            this.manager.start();
        });
    }
    
    /**
     * Start continuous listening
     */
    startListening() {
        this.manager.setContinuous(true);
        return this.manager.start();
    }
    
    /**
     * Stop listening
     */
    stopListening() {
        this.manager.stop();
    }
    
    /**
     * Toggle listening state
     */
    toggle() {
        if (this.manager.listening) {
            this.stopListening();
            return false;
        } else {
            return this.startListening();
        }
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // COMMAND RECOGNITION
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Listen for commands matching a grammar
     * @param {string[]} commands - Valid commands to match
     * @param {object} options - Options
     */
    listenForCommands(commands, options = {}) {
        const fuzzyMatch = options.fuzzy ?? true;
        const threshold = options.threshold ?? 0.7;
        
        return new Promise((resolve, reject) => {
            this.listen()
                .then(transcript => {
                    const normalized = transcript.toLowerCase().trim();
                    
                    // Exact match
                    if (commands.includes(normalized)) {
                        resolve({ command: normalized, transcript, exact: true });
                        return;
                    }
                    
                    // Fuzzy match
                    if (fuzzyMatch) {
                        for (const cmd of commands) {
                            if (this._fuzzyMatch(normalized, cmd.toLowerCase()) > threshold) {
                                resolve({ command: cmd, transcript, exact: false });
                                return;
                            }
                        }
                    }
                    
                    // No match
                    resolve({ command: null, transcript, exact: false });
                })
                .catch(reject);
        });
    }
    
    /**
     * Simple fuzzy matching (Levenshtein-based)
     */
    _fuzzyMatch(a, b) {
        if (a === b) return 1;
        if (a.includes(b) || b.includes(a)) return 0.8;
        
        // Simple similarity
        const longer = a.length > b.length ? a : b;
        const shorter = a.length > b.length ? b : a;
        
        let matches = 0;
        for (let i = 0; i < shorter.length; i++) {
            if (longer.includes(shorter[i])) matches++;
        }
        
        return matches / longer.length;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // INFO & HELP
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get service status
     */
    getStatus() {
        return {
            service: this.manager.service,
            supported: this.manager.supported,
            listening: this.manager.listening,
            language: this.manager.options.language,
            continuous: this.manager.options.continuous,
            privacyWarning: this.manager.privacyWarning,
            platform: this.platform
        };
    }
    
    /**
     * Get setup help
     */
    getHelp() {
        return {
            browser: {
                supported: this.manager.supported,
                note: this.manager.supported 
                    ? 'Browser speech recognition available'
                    : this.manager._getUnsupportedReason(),
                privacy: this.manager.privacyWarning
            },
            native: this.manager.nativeInstructions
        };
    }
    
    // Forward event subscriptions
    on(event, callback) { return this.manager.on(event, callback); }
    off(event, callback) { return this.manager.off(event, callback); }
    once(event, callback) { return this.manager.once(event, callback); }
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const RECOGNITION_EXPORTS = {
    RecognitionPlatform,
    RecognitionEvents,
    RecognitionManager,
    SpeechRecognitionSystem
};

// Browser: attach to window
if (typeof window !== 'undefined') {
    window.RecognitionPlatform = RecognitionPlatform;
    window.RecognitionEvents = RecognitionEvents;
    window.RecognitionManager = RecognitionManager;
    window.SpeechRecognitionSystem = SpeechRecognitionSystem;
}

// Node.js CommonJS
if (typeof module !== 'undefined' && module.exports) {
    module.exports = RECOGNITION_EXPORTS;
}
