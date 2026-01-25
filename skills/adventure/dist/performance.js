/**
 * performance.js — MOOLLM Adventure Performance System
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Plug-in speech synthesizer performance system for characters.
 * Inspired by: temp/lloooomm/dist/audrey-serenades-seymour-lloooomm-response.html
 * 
 * Features:
 * - Load performances from YAML files (songs, soliloquies, essays)
 * - Multi-character dialogue with distinct voices
 * - Karaoke-style display with scrolling lyrics
 * - Speed controls and voice customization
 * - Interruptible playback with pause/resume
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 * USAGE
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * // Initialize with speech system
 * const performer = new PerformanceSystem(speechSystem);
 * 
 * // Load a performance from YAML
 * await performer.loadFromYAML('ada-ii-song-feed-me-seymour.yml');
 * 
 * // Or load from object
 * performer.loadPerformance({
 *     title: "Feed Me, Seymour!",
 *     characters: { ada: { pitch: 0.4, rate: 0.8 } },
 *     script: [
 *         { character: 'ada', text: 'Feed me!', duration: 2000 },
 *         ...
 *     ]
 * });
 * 
 * // Control playback
 * performer.play();
 * performer.pause();
 * performer.stop();
 * performer.setSpeed(1.5);
 * 
 * // Events
 * performer.on('lineStart', (line, index) => updateDisplay(line));
 * performer.on('lineEnd', (line, index) => markAsSpoken(line));
 * performer.on('complete', () => showEndScreen());
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// PERFORMANCE SYSTEM — Main orchestrator
// ═══════════════════════════════════════════════════════════════════════════════

class PerformanceSystem {
    constructor(speechSystem, options = {}) {
        this.speech = speechSystem;
        this.options = {
            defaultPauseBetweenLines: 500, // ms
            ...options
        };
        
        // State
        this.performance = null;
        this.currentLine = 0;
        this.isPlaying = false;
        this.isPaused = false;
        this.speed = 1.0;
        this.timeout = null;
        
        // Character voice cache
        this.characterVoices = new Map();
        
        // Event listeners
        this.listeners = new Map();
        
        // Available performances registry
        this.registry = new Map();
        
        console.log('🎭 Performance System initialized');
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // LOADING
    // ─────────────────────────────────────────────────────────────────────────
    
    /**
     * Load performance from YAML file
     */
    async loadFromYAML(url) {
        try {
            const response = await fetch(url);
            const text = await response.text();
            
            // Parse YAML (requires js-yaml or similar)
            const data = this._parseYAML(text);
            return this.loadPerformance(data, url);
        } catch (error) {
            console.error(`🎭 Failed to load performance from ${url}:`, error);
            throw error;
        }
    }
    
    /**
     * Load performance from object
     */
    loadPerformance(data, source = 'inline') {
        // Normalize to standard format
        this.performance = this._normalizePerformance(data);
        this.performance.source = source;
        
        // Reset state
        this.currentLine = 0;
        this.isPlaying = false;
        this.isPaused = false;
        
        // Setup character voices
        this._setupCharacterVoices();
        
        console.log(`🎭 Loaded: "${this.performance.title}" (${this.performance.script.length} lines)`);
        this.emit('loaded', this.performance);
        
        return this.performance;
    }
    
    /**
     * Normalize various YAML formats to standard script format
     */
    _normalizePerformance(data) {
        const performance = {
            title: data.meta?.song_title || data.title || 'Untitled Performance',
            type: data.type || 'song',
            characters: {},
            script: []
        };
        
        // Extract character configs
        if (data.speech_config) {
            for (const [char, config] of Object.entries(data.speech_config)) {
                performance.characters[char] = {
                    pitch: config.pitch || 1.0,
                    rate: config.rate || 1.0,
                    volume: config.volume || 1.0,
                    preferredVoices: config.preferred_voices || config.preferredVoices || []
                };
            }
        }
        
        // Convert song structure to flat script
        // Handle LLOOOOMM song format
        if (data.lloooomm_song) {
            performance.script = this._extractLLOOOOMMScript(data.lloooomm_song);
        }
        // Handle Ada adaptation format
        else if (data.ada_adaptation) {
            performance.script = this._extractAdaScript(data.ada_adaptation);
        }
        // Handle flat script format
        else if (data.script) {
            performance.script = data.script;
        }
        
        return performance;
    }
    
    /**
     * Extract script from LLOOOOMM song format
     */
    _extractLLOOOOMMScript(song) {
        const script = [];
        
        // Process sections in order
        const sections = [
            'dialogue_intro', 'verse_1', 'response_1', 'verse_2', 'interjection_1',
            'verse_3', 'response_2', 'verse_4', 'interjection_2', 'verse_5',
            'response_3', 'verse_6', 'finale', 'resolution'
        ];
        
        for (const section of sections) {
            const sectionData = song[section];
            if (!sectionData) continue;
            
            // Array of dialogue lines
            if (Array.isArray(sectionData)) {
                for (const line of sectionData) {
                    script.push({
                        character: line.character,
                        text: line.text,
                        duration: line.duration_ms || line.duration || this._estimateDuration(line.text),
                        emote: line.emote
                    });
                }
            }
            // Single line with character
            else if (sectionData.character) {
                script.push({
                    character: sectionData.character,
                    text: sectionData.text,
                    duration: sectionData.duration_ms || this._estimateDuration(sectionData.text),
                    emote: sectionData.emote
                });
            }
            // Verse with lyrics
            else if (sectionData.lyrics) {
                script.push({
                    character: 'audrey', // Default for verses
                    text: sectionData.lyrics.trim(),
                    duration: sectionData.duration_ms || this._estimateDuration(sectionData.lyrics),
                    section: section,
                    title: sectionData.title,
                    emote: sectionData.emote
                });
            }
        }
        
        return script;
    }
    
    /**
     * Extract script from Ada adaptation format
     */
    _extractAdaScript(ada) {
        const script = [];
        
        // Setup stage direction
        if (ada.setup?.stage_direction) {
            script.push({
                character: 'narrator',
                text: ada.setup.stage_direction.trim(),
                duration: this._estimateDuration(ada.setup.stage_direction),
                type: 'stage_direction'
            });
        }
        
        // Dialogue intro
        if (ada.dialogue_intro) {
            for (const line of ada.dialogue_intro) {
                script.push({
                    character: line.character || 'ada',
                    text: line.text,
                    duration: this._estimateDuration(line.text),
                    emote: line.emote
                });
            }
        }
        
        // Process verses
        const verses = ['verse_1_ada', 'verse_2_ada', 'verse_3_ada', 'finale_ada'];
        for (const v of verses) {
            if (ada[v]?.lyrics) {
                script.push({
                    character: 'ada',
                    text: ada[v].lyrics.trim(),
                    duration: this._estimateDuration(ada[v].lyrics),
                    title: ada[v].title,
                    note: ada[v].note
                });
            }
        }
        
        // Flashback moment
        if (ada.flashback_moment) {
            script.push({
                character: 'ada',
                text: ada.flashback_moment.text,
                duration: this._estimateDuration(ada.flashback_moment.text),
                emote: ada.flashback_moment.emote,
                voiceMode: 'flashback' // Special voice mode
            });
        }
        
        // Resolution
        if (ada.resolution_ada) {
            for (const line of ada.resolution_ada) {
                script.push({
                    character: line.character || 'ada',
                    text: line.text,
                    duration: this._estimateDuration(line.text),
                    emote: line.emote
                });
            }
        }
        
        return script;
    }
    
    /**
     * Estimate duration based on text length
     */
    _estimateDuration(text) {
        if (!text) return 2000;
        // Rough estimate: 100ms per character, minimum 2s
        return Math.max(2000, text.length * 100);
    }
    
    /**
     * Parse YAML text (simplified, for browser use)
     */
    _parseYAML(text) {
        // Use js-yaml if available
        if (typeof jsyaml !== 'undefined') {
            return jsyaml.load(text);
        }
        // Fallback: try JSON
        if (text.trim().startsWith('{')) {
            return JSON.parse(text);
        }
        throw new Error('YAML parser not available - include js-yaml library');
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // VOICE SETUP
    // ─────────────────────────────────────────────────────────────────────────
    
    /**
     * Setup voices for each character in the performance
     */
    _setupCharacterVoices() {
        if (!this.speech) return;
        
        const voices = window.speechSynthesis.getVoices();
        
        for (const [char, config] of Object.entries(this.performance.characters)) {
            let selectedVoice = null;
            
            // Try preferred voices
            for (const preferred of config.preferredVoices || []) {
                const voice = voices.find(v => 
                    v.name.includes(preferred) || 
                    v.name.toLowerCase().includes(preferred.toLowerCase())
                );
                if (voice) {
                    selectedVoice = voice;
                    break;
                }
            }
            
            // Fallback to any English voice
            if (!selectedVoice) {
                selectedVoice = voices.find(v => v.lang.startsWith('en')) || voices[0];
            }
            
            this.characterVoices.set(char, {
                voice: selectedVoice,
                config: config
            });
            
            console.log(`🎭 ${char} voice: ${selectedVoice?.name || 'default'}`);
        }
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // PLAYBACK CONTROL
    // ─────────────────────────────────────────────────────────────────────────
    
    /**
     * Start or resume playback
     */
    play() {
        if (!this.performance) {
            console.warn('🎭 No performance loaded');
            return;
        }
        
        if (this.isPaused) {
            this.isPaused = false;
            this.isPlaying = true;
            this._playNextLine();
        } else if (!this.isPlaying) {
            this.currentLine = 0;
            this.isPlaying = true;
            this.emit('start', this.performance);
            this._playNextLine();
        }
    }
    
    /**
     * Pause playback
     */
    pause() {
        if (this.isPlaying) {
            this.isPlaying = false;
            this.isPaused = true;
            clearTimeout(this.timeout);
            window.speechSynthesis.cancel();
            this.emit('pause', this.currentLine);
        }
    }
    
    /**
     * Stop playback and reset
     */
    stop() {
        this.isPlaying = false;
        this.isPaused = false;
        this.currentLine = 0;
        clearTimeout(this.timeout);
        window.speechSynthesis.cancel();
        this.emit('stop');
    }
    
    /**
     * Rewind to beginning
     */
    rewind() {
        const wasPlaying = this.isPlaying;
        this.stop();
        if (wasPlaying) {
            this.play();
        }
        this.emit('rewind');
    }
    
    /**
     * Set playback speed
     */
    setSpeed(speed) {
        this.speed = Math.max(0.3, Math.min(2.0, speed));
        console.log(`🎭 Speed: ${this.speed}x`);
        this.emit('speedChange', this.speed);
    }
    
    /**
     * Skip to specific line
     */
    skipTo(lineIndex) {
        if (lineIndex >= 0 && lineIndex < this.performance.script.length) {
            this.currentLine = lineIndex;
            if (this.isPlaying) {
                window.speechSynthesis.cancel();
                this._playNextLine();
            }
        }
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // INTERNAL PLAYBACK
    // ─────────────────────────────────────────────────────────────────────────
    
    /**
     * Play the next line in the script
     */
    async _playNextLine() {
        if (!this.isPlaying || this.currentLine >= this.performance.script.length) {
            if (this.currentLine >= this.performance.script.length) {
                this.isPlaying = false;
                this.emit('complete', this.performance);
            }
            return;
        }
        
        const line = this.performance.script[this.currentLine];
        this.emit('lineStart', line, this.currentLine);
        
        try {
            await this._speakLine(line);
        } catch (error) {
            console.error('🎭 Speech error:', error);
        }
        
        this.emit('lineEnd', line, this.currentLine);
        
        // Advance to next line after pause
        if (this.isPlaying) {
            const pauseDuration = this.options.defaultPauseBetweenLines / this.speed;
            this.timeout = setTimeout(() => {
                this.currentLine++;
                this._playNextLine();
            }, pauseDuration);
        }
    }
    
    /**
     * Speak a single line with character voice
     */
    _speakLine(line) {
        return new Promise((resolve) => {
            const characterData = this.characterVoices.get(line.character) || 
                                  this.characterVoices.get('narrator') ||
                                  { voice: null, config: {} };
            
            const utterance = new SpeechSynthesisUtterance(line.text);
            
            // Apply voice
            if (characterData.voice) {
                utterance.voice = characterData.voice;
                utterance.lang = characterData.voice.lang;
            }
            
            // Apply config with speed adjustment
            const config = characterData.config;
            utterance.pitch = config.pitch || 1.0;
            utterance.rate = (config.rate || 1.0) * this.speed;
            utterance.volume = config.volume || 1.0;
            
            // Handle special voice modes (e.g., flashback)
            if (line.voiceMode === 'flashback' && this.performance.characters.ada?.flashback) {
                const fb = this.performance.characters.ada.flashback;
                utterance.pitch = fb.pitch || 0.3;
                utterance.rate = (fb.rate || 1.3) * this.speed;
            }
            
            let resolved = false;
            
            const finish = () => {
                if (!resolved) {
                    resolved = true;
                    resolve();
                }
            };
            
            utterance.onend = finish;
            utterance.onerror = (e) => {
                console.warn('🎭 Speech error:', e);
                finish();
            };
            
            // Fallback timeout
            const estimatedDuration = Math.max(2000, line.text.length * 100) / this.speed;
            setTimeout(finish, estimatedDuration + 1000);
            
            window.speechSynthesis.speak(utterance);
        });
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // EVENT SYSTEM
    // ─────────────────────────────────────────────────────────────────────────
    
    /**
     * Register event listener
     */
    on(event, callback) {
        if (!this.listeners.has(event)) {
            this.listeners.set(event, []);
        }
        this.listeners.get(event).push(callback);
    }
    
    /**
     * Remove event listener
     */
    off(event, callback) {
        const listeners = this.listeners.get(event);
        if (listeners) {
            const index = listeners.indexOf(callback);
            if (index >= 0) {
                listeners.splice(index, 1);
            }
        }
    }
    
    /**
     * Emit event
     */
    emit(event, ...args) {
        const listeners = this.listeners.get(event);
        if (listeners) {
            for (const callback of listeners) {
                try {
                    callback(...args);
                } catch (error) {
                    console.error(`🎭 Event handler error (${event}):`, error);
                }
            }
        }
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // PERFORMANCE REGISTRY
    // ─────────────────────────────────────────────────────────────────────────
    
    /**
     * Register a performance in the registry
     */
    register(id, metadata) {
        this.registry.set(id, {
            id,
            ...metadata,
            registered: new Date()
        });
    }
    
    /**
     * List all registered performances
     */
    listPerformances() {
        return Array.from(this.registry.values());
    }
    
    /**
     * Get performance metadata
     */
    getPerformance(id) {
        return this.registry.get(id);
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// KARAOKE DISPLAY — Visual lyrics display
// ═══════════════════════════════════════════════════════════════════════════════

class KaraokeDisplay {
    constructor(containerId, performanceSystem) {
        this.container = document.getElementById(containerId);
        this.performer = performanceSystem;
        this.history = [];
        this.maxHistory = 10;
        
        // Bind events
        this.performer.on('lineStart', (line, idx) => this._onLineStart(line, idx));
        this.performer.on('lineEnd', (line, idx) => this._onLineEnd(line, idx));
        this.performer.on('complete', () => this._onComplete());
        this.performer.on('stop', () => this._onStop());
        
        // Initialize display
        this._initDisplay();
    }
    
    _initDisplay() {
        if (!this.container) return;
        this.container.innerHTML = `
            <div class="karaoke-display">
                <div class="karaoke-history"></div>
                <div class="karaoke-current">🎵 Click PLAY to start the performance! 🎵</div>
            </div>
        `;
    }
    
    _onLineStart(line, index) {
        const current = this.container.querySelector('.karaoke-current');
        if (current) {
            // Move previous to history
            if (current.textContent && !current.textContent.includes('Click PLAY')) {
                this._addToHistory(current.innerHTML);
            }
            
            // Display new line
            current.innerHTML = `
                <div class="speaker-name speaker-${line.character}">${line.character.toUpperCase()}</div>
                <div class="speech-text">${this._formatText(line.text)}</div>
                ${line.emote ? `<div class="emote">${line.emote}</div>` : ''}
            `;
            current.classList.add('speaking');
        }
        
        // Scroll to bottom
        this._scrollToBottom();
    }
    
    _onLineEnd(line, index) {
        const current = this.container.querySelector('.karaoke-current');
        if (current) {
            current.classList.remove('speaking');
            current.classList.add('spoken');
        }
    }
    
    _addToHistory(html) {
        const historyContainer = this.container.querySelector('.karaoke-history');
        if (!historyContainer) return;
        
        const entry = document.createElement('div');
        entry.className = 'karaoke-history-entry';
        entry.innerHTML = html;
        historyContainer.appendChild(entry);
        
        // Limit history
        while (historyContainer.children.length > this.maxHistory) {
            historyContainer.removeChild(historyContainer.firstChild);
        }
    }
    
    _onComplete() {
        const current = this.container.querySelector('.karaoke-current');
        if (current) {
            current.innerHTML = `
                <div class="performance-complete">
                    🎭 <strong>Performance Complete!</strong> 🎭<br/>
                    Click PLAY to perform again.
                </div>
            `;
        }
    }
    
    _onStop() {
        const current = this.container.querySelector('.karaoke-current');
        if (current) {
            current.innerHTML = '⏹️ Performance stopped. Click PLAY to start again.';
        }
    }
    
    _formatText(text) {
        // Convert newlines to <br>
        return text.replace(/\n/g, '<br>');
    }
    
    _scrollToBottom() {
        const display = this.container.querySelector('.karaoke-display');
        if (display) {
            display.scrollTop = display.scrollHeight;
        }
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// PERFORMANCE CONTROLS — UI for playback control
// ═══════════════════════════════════════════════════════════════════════════════

class PerformanceControls {
    constructor(containerId, performanceSystem) {
        this.container = document.getElementById(containerId);
        this.performer = performanceSystem;
        
        // Bind events
        this.performer.on('start', () => this._updateState('playing'));
        this.performer.on('pause', () => this._updateState('paused'));
        this.performer.on('stop', () => this._updateState('stopped'));
        this.performer.on('complete', () => this._updateState('stopped'));
        
        this._initControls();
    }
    
    _initControls() {
        if (!this.container) return;
        
        this.container.innerHTML = `
            <div class="performance-controls">
                <button class="control-btn play-btn" data-action="play">▶️ PLAY</button>
                <button class="control-btn pause-btn" data-action="pause" style="display:none;">⏸️ PAUSE</button>
                <button class="control-btn stop-btn" data-action="stop">⏹️ STOP</button>
                <button class="control-btn rewind-btn" data-action="rewind">⏮️ REWIND</button>
                
                <div class="speed-controls">
                    <span class="speed-label">Speed:</span>
                    <button class="speed-btn" data-speed="0.5">🐌 Slow</button>
                    <button class="speed-btn active" data-speed="1.0">🐱 Normal</button>
                    <button class="speed-btn" data-speed="1.5">🐆 Fast</button>
                    <button class="speed-btn" data-speed="2.0">🚀 Rocket</button>
                </div>
            </div>
        `;
        
        // Bind click handlers
        this.container.querySelectorAll('.control-btn').forEach(btn => {
            btn.addEventListener('click', () => this._onAction(btn.dataset.action));
        });
        
        this.container.querySelectorAll('.speed-btn').forEach(btn => {
            btn.addEventListener('click', () => this._onSpeed(parseFloat(btn.dataset.speed), btn));
        });
    }
    
    _onAction(action) {
        switch (action) {
            case 'play': this.performer.play(); break;
            case 'pause': this.performer.pause(); break;
            case 'stop': this.performer.stop(); break;
            case 'rewind': this.performer.rewind(); break;
        }
    }
    
    _onSpeed(speed, btn) {
        this.performer.setSpeed(speed);
        this.container.querySelectorAll('.speed-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
    }
    
    _updateState(state) {
        const playBtn = this.container.querySelector('.play-btn');
        const pauseBtn = this.container.querySelector('.pause-btn');
        
        if (state === 'playing') {
            playBtn.style.display = 'none';
            pauseBtn.style.display = 'inline-block';
        } else {
            playBtn.style.display = 'inline-block';
            pauseBtn.style.display = 'none';
        }
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// ADA II PERFORMER — Character-specific performer
// ═══════════════════════════════════════════════════════════════════════════════

class AdaIIPerformer {
    constructor(performanceSystem) {
        this.performer = performanceSystem;
        this.repertoire = new Map();
        
        // Register Ada II's songs
        this._registerRepertoire();
    }
    
    _registerRepertoire() {
        // Feed Me, Seymour
        this.repertoire.set('feed-me-seymour', {
            id: 'feed-me-seymour',
            title: 'Feed Me, Seymour! (Constructionist Version)',
            type: 'song',
            file: 'ada-ii-song-feed-me-seymour.yml',
            description: 'The classic Little Shop number, adapted for constructionist learning',
            duration: '~5 minutes'
        });
        
        // Future: Papert essays
        this.repertoire.set('papert-mindstorms-intro', {
            id: 'papert-mindstorms-intro',
            title: 'Mindstorms: Introduction',
            type: 'essay',
            file: 'papert-mindstorms-intro.yml',
            description: 'Seymour Papert on children and computers',
            duration: '~10 minutes',
            status: 'coming-soon'
        });
    }
    
    /**
     * List available performances
     */
    listRepertoire() {
        return Array.from(this.repertoire.values());
    }
    
    /**
     * Perform a piece from the repertoire
     */
    async perform(id) {
        const piece = this.repertoire.get(id);
        if (!piece) {
            console.warn(`🌿 Ada II doesn't know "${id}"`);
            return false;
        }
        
        if (piece.status === 'coming-soon') {
            console.log(`🌿 Ada II: "That one's still in rehearsal, darling..."`);
            return false;
        }
        
        console.log(`🌿 Ada II: "Ah, ${piece.title}! One of my favorites..."`);
        await this.performer.loadFromYAML(piece.file);
        this.performer.play();
        return true;
    }
    
    /**
     * Random greeting from Ada II
     */
    getGreeting() {
        const greetings = [
            "Hello, darling. Care for a song?",
            "Feed me... some attention! I have performances prepared.",
            "Ah, a visitor! Would you like to hear me sing?",
            "REPEAT 4. REPEAT 4. ...oh! Hello there. I have songs.",
            "Back in my DoD days, I never got to perform. Now I make up for lost time."
        ];
        return greetings[Math.floor(Math.random() * greetings.length)];
    }
}

// Export for browser
if (typeof window !== 'undefined') {
    window.PerformanceSystem = PerformanceSystem;
    window.KaraokeDisplay = KaraokeDisplay;
    window.PerformanceControls = PerformanceControls;
    window.AdaIIPerformer = AdaIIPerformer;
}

// Export for Node.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { PerformanceSystem, KaraokeDisplay, PerformanceControls, AdaIIPerformer };
}
