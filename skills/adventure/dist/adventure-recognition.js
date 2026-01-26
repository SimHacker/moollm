/**
 * adventure-recognition.js — Speech Recognition UI for Adventure Engine
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Integrates speech recognition into the adventure game with:
 * - Microphone toggle button
 * - Configuration panel
 * - Visual feedback (listening indicator)
 * - Command mode (speak adventure commands)
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// RECOGNITION UI — Visual controls for speech recognition
// ═══════════════════════════════════════════════════════════════════════════════

class RecognitionUI {
    constructor(options = {}) {
        this.container = null;
        this.button = null;
        this.panel = null;
        this.indicator = null;
        
        // State
        this.isOpen = false;
        this.isListening = false;
        
        // Recognition system (set later)
        this.recognition = null;
        
        // Options
        this.options = {
            position: options.position || 'bottom-right',
            showButton: options.showButton ?? true,
            showIndicator: options.showIndicator ?? true,
            theme: options.theme || 'dark',
            ...options
        };
        
        // Callbacks
        this.onCommand = options.onCommand || null;
        this.onTranscript = options.onTranscript || null;
    }
    
    /**
     * Initialize UI with a recognition system
     */
    init(recognitionSystem, parentContainer = document.body) {
        this.recognition = recognitionSystem;
        
        // Create UI container
        this.container = document.createElement('div');
        this.container.className = `recognition-ui ${this.options.theme}`;
        this.container.innerHTML = this._createHTML();
        
        parentContainer.appendChild(this.container);
        
        // Get references
        this.button = this.container.querySelector('.recognition-button');
        this.panel = this.container.querySelector('.recognition-panel');
        this.indicator = this.container.querySelector('.recognition-indicator');
        this.interimText = this.container.querySelector('.recognition-interim');
        
        // Wire up events
        this._setupEvents();
        this._injectStyles();
        
        // Update initial state
        this._updateButton();
        this._updateSupportStatus();
    }
    
    /**
     * Create HTML structure
     */
    _createHTML() {
        return `
            <!-- Microphone Button -->
            <button class="recognition-button" title="Voice Input (V)">
                <span class="recognition-icon">🎤</span>
                <span class="recognition-status"></span>
            </button>
            
            <!-- Listening Indicator -->
            <div class="recognition-indicator" style="display: none;">
                <div class="recognition-waves">
                    <span></span><span></span><span></span><span></span><span></span>
                </div>
                <div class="recognition-interim"></div>
            </div>
            
            <!-- Configuration Panel -->
            <div class="recognition-panel" style="display: none;">
                <div class="recognition-panel-header">
                    <h3>🎤 Voice Input</h3>
                    <button class="recognition-panel-close">✕</button>
                </div>
                
                <div class="recognition-panel-content">
                    <!-- Service Status -->
                    <div class="recognition-section">
                        <h4>Service</h4>
                        <div class="recognition-service-status"></div>
                    </div>
                    
                    <!-- Browser Speech -->
                    <div class="recognition-section recognition-browser-section">
                        <h4>Browser Speech Recognition</h4>
                        <div class="recognition-browser-status"></div>
                        <div class="recognition-privacy-warning"></div>
                        <button class="recognition-test-btn">🎤 Test Browser Recognition</button>
                    </div>
                    
                    <!-- Native Platform -->
                    <div class="recognition-section recognition-native-section">
                        <h4>Native Platform Speech</h4>
                        <div class="recognition-native-instructions"></div>
                    </div>
                    
                    <!-- Settings -->
                    <div class="recognition-section">
                        <h4>Settings</h4>
                        <label class="recognition-option">
                            <input type="checkbox" class="recognition-continuous" />
                            Continuous listening
                        </label>
                        <label class="recognition-option">
                            <span>Language:</span>
                            <select class="recognition-language">
                                <option value="en-US">English (US)</option>
                                <option value="en-GB">English (UK)</option>
                                <option value="es-ES">Spanish</option>
                                <option value="fr-FR">French</option>
                                <option value="de-DE">German</option>
                                <option value="it-IT">Italian</option>
                                <option value="pt-BR">Portuguese (BR)</option>
                                <option value="nl-NL">Dutch</option>
                                <option value="ja-JP">Japanese</option>
                                <option value="zh-CN">Chinese (Simplified)</option>
                            </select>
                        </label>
                    </div>
                    
                    <!-- Help -->
                    <div class="recognition-section recognition-help">
                        <h4>Tips</h4>
                        <ul>
                            <li>Press <kbd>V</kbd> to toggle voice input</li>
                            <li>Speak adventure commands naturally</li>
                            <li>Say "go north", "look around", "take sword"</li>
                        </ul>
                    </div>
                </div>
            </div>
        `;
    }
    
    /**
     * Setup event handlers
     */
    _setupEvents() {
        // Button click - toggle listening or open panel
        this.button.addEventListener('click', (e) => {
            if (e.shiftKey || !this.recognition?.manager.supported) {
                // Shift+click or unsupported: open config panel
                this.togglePanel();
            } else {
                // Normal click: toggle listening
                this.toggleListening();
            }
        });
        
        // Long press - open panel
        let pressTimer;
        this.button.addEventListener('mousedown', () => {
            pressTimer = setTimeout(() => this.togglePanel(), 500);
        });
        this.button.addEventListener('mouseup', () => clearTimeout(pressTimer));
        this.button.addEventListener('mouseleave', () => clearTimeout(pressTimer));
        
        // Panel close
        this.panel.querySelector('.recognition-panel-close').addEventListener('click', () => {
            this.closePanel();
        });
        
        // Test button
        this.panel.querySelector('.recognition-test-btn').addEventListener('click', () => {
            this._testRecognition();
        });
        
        // Settings changes
        this.panel.querySelector('.recognition-continuous').addEventListener('change', (e) => {
            this.recognition?.manager.setContinuous(e.target.checked);
        });
        
        this.panel.querySelector('.recognition-language').addEventListener('change', (e) => {
            this.recognition?.manager.setLanguage(e.target.value);
        });
        
        // Recognition events
        if (this.recognition) {
            this.recognition.on(RecognitionEvents.START, () => {
                this.isListening = true;
                this._updateButton();
                this._showIndicator();
            });
            
            this.recognition.on(RecognitionEvents.END, () => {
                this.isListening = false;
                this._updateButton();
                this._hideIndicator();
            });
            
            this.recognition.on(RecognitionEvents.INTERIM, (e) => {
                this._showInterim(e.transcript);
            });
            
            this.recognition.on(RecognitionEvents.RESULT, (e) => {
                this._clearInterim();
                this.onTranscript?.(e.transcript, e);
            });
            
            this.recognition.on(RecognitionEvents.ERROR, (e) => {
                this._showError(e.message);
            });
        }
        
        // Keyboard shortcut
        document.addEventListener('keydown', (e) => {
            // V key to toggle voice (when not in input)
            if (e.key === 'v' && !this._isInputFocused()) {
                e.preventDefault();
                this.toggleListening();
            }
        });
    }
    
    /**
     * Check if user is typing in an input
     */
    _isInputFocused() {
        const active = document.activeElement;
        return active && (
            active.tagName === 'INPUT' ||
            active.tagName === 'TEXTAREA' ||
            active.isContentEditable
        );
    }
    
    /**
     * Toggle listening state
     */
    toggleListening() {
        if (!this.recognition) return;
        
        if (this.isListening) {
            this.recognition.stopListening();
        } else {
            this.recognition.startListening();
        }
    }
    
    /**
     * Toggle config panel
     */
    togglePanel() {
        if (this.isOpen) {
            this.closePanel();
        } else {
            this.openPanel();
        }
    }
    
    /**
     * Open config panel
     */
    openPanel() {
        this._updateSupportStatus();
        this.panel.style.display = 'block';
        this.isOpen = true;
    }
    
    /**
     * Close config panel
     */
    closePanel() {
        this.panel.style.display = 'none';
        this.isOpen = false;
    }
    
    /**
     * Update button appearance
     */
    _updateButton() {
        this.button.classList.toggle('listening', this.isListening);
        this.button.classList.toggle('supported', this.recognition?.manager.supported);
        
        const status = this.button.querySelector('.recognition-status');
        if (this.isListening) {
            status.textContent = '●';
            status.className = 'recognition-status active';
        } else if (this.recognition?.manager.supported) {
            status.textContent = '';
        } else {
            status.textContent = '!';
            status.className = 'recognition-status unsupported';
        }
    }
    
    /**
     * Update support status in panel
     */
    _updateSupportStatus() {
        if (!this.recognition) return;
        
        const help = this.recognition.getHelp();
        
        // Service status
        const serviceStatus = this.panel.querySelector('.recognition-service-status');
        if (help.browser.supported) {
            serviceStatus.innerHTML = `
                <span class="status-ok">✅ Browser speech recognition available</span>
            `;
        } else {
            serviceStatus.innerHTML = `
                <span class="status-warn">⚠️ ${help.browser.note}</span>
            `;
        }
        
        // Browser status
        const browserStatus = this.panel.querySelector('.recognition-browser-status');
        browserStatus.innerHTML = help.browser.supported
            ? '<span class="status-ok">✅ Supported</span>'
            : `<span class="status-error">❌ ${help.browser.note}</span>`;
        
        // Privacy warning
        const privacyWarn = this.panel.querySelector('.recognition-privacy-warning');
        if (help.browser.privacy) {
            privacyWarn.innerHTML = `<span class="status-warn">${help.browser.privacy}</span>`;
            privacyWarn.style.display = 'block';
        } else {
            privacyWarn.style.display = 'none';
        }
        
        // Native instructions
        const native = help.native;
        const nativeEl = this.panel.querySelector('.recognition-native-instructions');
        nativeEl.innerHTML = `
            <p><strong>${native.platform}: ${native.name}</strong></p>
            <p>Activation: <kbd>${native.shortcut || native.activation}</kbd></p>
            ${native.setup ? `
                <details>
                    <summary>Setup Instructions</summary>
                    <ol>
                        ${native.setup.map(s => `<li>${s}</li>`).join('')}
                    </ol>
                </details>
            ` : ''}
            ${native.voiceControl ? `
                <p>Full voice control: ${native.voiceControl.path}</p>
            ` : ''}
        `;
    }
    
    /**
     * Show listening indicator
     */
    _showIndicator() {
        if (this.indicator) {
            this.indicator.style.display = 'flex';
        }
    }
    
    /**
     * Hide listening indicator
     */
    _hideIndicator() {
        if (this.indicator) {
            this.indicator.style.display = 'none';
        }
        this._clearInterim();
    }
    
    /**
     * Show interim transcript
     */
    _showInterim(text) {
        if (this.interimText) {
            this.interimText.textContent = text;
            this.interimText.style.opacity = '1';
        }
    }
    
    /**
     * Clear interim transcript
     */
    _clearInterim() {
        if (this.interimText) {
            this.interimText.textContent = '';
            this.interimText.style.opacity = '0';
        }
    }
    
    /**
     * Show error message
     */
    _showError(message) {
        // Could show toast notification
        console.warn('Recognition error:', message);
    }
    
    /**
     * Test recognition
     */
    _testRecognition() {
        if (!this.recognition?.manager.supported) {
            alert('Browser speech recognition not supported. See native platform instructions.');
            return;
        }
        
        const testBtn = this.panel.querySelector('.recognition-test-btn');
        testBtn.textContent = '🎤 Listening...';
        testBtn.disabled = true;
        
        this.recognition.listen()
            .then(transcript => {
                testBtn.textContent = `✅ "${transcript}"`;
                setTimeout(() => {
                    testBtn.textContent = '🎤 Test Browser Recognition';
                    testBtn.disabled = false;
                }, 2000);
            })
            .catch(error => {
                testBtn.textContent = `❌ ${error.message}`;
                setTimeout(() => {
                    testBtn.textContent = '🎤 Test Browser Recognition';
                    testBtn.disabled = false;
                }, 2000);
            });
    }
    
    /**
     * Inject styles
     */
    _injectStyles() {
        if (document.getElementById('recognition-ui-styles')) return;
        
        const style = document.createElement('style');
        style.id = 'recognition-ui-styles';
        style.textContent = `
            /* ═══════════════════════════════════════════════════════════════
               Recognition UI Styles
               ═══════════════════════════════════════════════════════════════ */
            
            .recognition-ui {
                position: fixed;
                bottom: 20px;
                right: 20px;
                z-index: 9998;
                font-family: system-ui, -apple-system, sans-serif;
            }
            
            /* Microphone Button */
            .recognition-button {
                width: 50px;
                height: 50px;
                border-radius: 50%;
                border: none;
                background: #313244;
                color: #cdd6f4;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                position: relative;
                transition: all 0.2s;
                box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            }
            
            .recognition-button:hover {
                background: #45475a;
                transform: scale(1.05);
            }
            
            .recognition-button.listening {
                background: #f38ba8;
                animation: pulse 1.5s infinite;
            }
            
            .recognition-button:not(.supported) {
                opacity: 0.7;
            }
            
            .recognition-icon {
                font-size: 24px;
            }
            
            .recognition-status {
                position: absolute;
                top: 5px;
                right: 5px;
                font-size: 10px;
            }
            
            .recognition-status.active {
                color: #f38ba8;
                animation: blink 1s infinite;
            }
            
            .recognition-status.unsupported {
                color: #f9e2af;
            }
            
            @keyframes pulse {
                0%, 100% { box-shadow: 0 0 0 0 rgba(243, 139, 168, 0.4); }
                50% { box-shadow: 0 0 0 15px rgba(243, 139, 168, 0); }
            }
            
            @keyframes blink {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.3; }
            }
            
            /* Listening Indicator */
            .recognition-indicator {
                position: fixed;
                bottom: 80px;
                right: 20px;
                background: #1e1e2e;
                border: 1px solid #313244;
                border-radius: 8px;
                padding: 15px 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 10px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            }
            
            .recognition-waves {
                display: flex;
                align-items: center;
                gap: 3px;
                height: 30px;
            }
            
            .recognition-waves span {
                width: 4px;
                background: #f38ba8;
                border-radius: 2px;
                animation: wave 0.5s ease-in-out infinite;
            }
            
            .recognition-waves span:nth-child(1) { animation-delay: 0.0s; }
            .recognition-waves span:nth-child(2) { animation-delay: 0.1s; }
            .recognition-waves span:nth-child(3) { animation-delay: 0.2s; }
            .recognition-waves span:nth-child(4) { animation-delay: 0.1s; }
            .recognition-waves span:nth-child(5) { animation-delay: 0.0s; }
            
            @keyframes wave {
                0%, 100% { height: 10px; }
                50% { height: 30px; }
            }
            
            .recognition-interim {
                color: #a6adc8;
                font-size: 14px;
                font-style: italic;
                max-width: 250px;
                text-align: center;
                transition: opacity 0.2s;
            }
            
            /* Config Panel */
            .recognition-panel {
                position: fixed;
                bottom: 80px;
                right: 20px;
                width: 320px;
                max-height: 70vh;
                background: #1e1e2e;
                border: 1px solid #313244;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 30px rgba(0,0,0,0.4);
            }
            
            .recognition-panel-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 15px;
                background: #313244;
                border-bottom: 1px solid #45475a;
            }
            
            .recognition-panel-header h3 {
                margin: 0;
                color: #cdd6f4;
                font-size: 16px;
            }
            
            .recognition-panel-close {
                background: none;
                border: none;
                color: #f38ba8;
                font-size: 18px;
                cursor: pointer;
            }
            
            .recognition-panel-content {
                padding: 15px;
                overflow-y: auto;
                max-height: calc(70vh - 60px);
            }
            
            .recognition-section {
                margin-bottom: 20px;
            }
            
            .recognition-section h4 {
                color: #89b4fa;
                margin: 0 0 10px 0;
                font-size: 13px;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }
            
            .recognition-section p {
                color: #cdd6f4;
                margin: 5px 0;
                font-size: 14px;
            }
            
            .recognition-section ul {
                color: #a6adc8;
                margin: 5px 0;
                padding-left: 20px;
                font-size: 13px;
            }
            
            .recognition-section kbd {
                background: #45475a;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: 'SF Mono', Consolas, monospace;
                font-size: 12px;
            }
            
            .recognition-section details {
                margin-top: 10px;
            }
            
            .recognition-section summary {
                cursor: pointer;
                color: #89b4fa;
                font-size: 13px;
            }
            
            .recognition-section ol {
                color: #a6adc8;
                margin: 10px 0;
                padding-left: 20px;
                font-size: 13px;
            }
            
            .recognition-option {
                display: flex;
                align-items: center;
                gap: 10px;
                margin: 10px 0;
                color: #cdd6f4;
                font-size: 14px;
            }
            
            .recognition-option select {
                background: #313244;
                border: 1px solid #45475a;
                color: #cdd6f4;
                padding: 5px 10px;
                border-radius: 4px;
            }
            
            .recognition-test-btn {
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                background: #89b4fa;
                color: #1e1e2e;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 14px;
                transition: background 0.2s;
            }
            
            .recognition-test-btn:hover {
                background: #b4befe;
            }
            
            .recognition-test-btn:disabled {
                background: #45475a;
                color: #a6adc8;
                cursor: not-allowed;
            }
            
            .status-ok { color: #a6e3a1; }
            .status-warn { color: #f9e2af; }
            .status-error { color: #f38ba8; }
        `;
        document.head.appendChild(style);
    }
    
    /**
     * Destroy UI
     */
    destroy() {
        if (this.container) {
            this.container.remove();
        }
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// ADVENTURE RECOGNITION ADAPTER — Connect to adventure engine
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Add speech recognition to an adventure engine
 */
function addRecognitionToEngine(engine, options = {}) {
    // Create recognition system
    const recognition = new SpeechRecognitionSystem({
        language: options.language || 'en-US',
        continuous: options.continuous ?? false,
        interimResults: true
    });
    
    // Create UI
    const ui = new RecognitionUI({
        position: options.position || 'bottom-right',
        ...options
    });
    
    // Initialize UI
    ui.init(recognition, document.body);
    
    // Store on engine
    engine.recognition = recognition;
    engine.recognitionUI = ui;
    
    // Handle recognized commands
    recognition.onResult = (transcript) => {
        console.log('Voice command:', transcript);
        
        // Send to engine as command
        if (engine.command) {
            const result = engine.command(transcript);
            
            // Optionally speak the response
            if (engine.speech && options.speakResponses) {
                engine.speech.speak(result.message || result.description);
            }
        }
    };
    
    // Show interim results in game UI
    recognition.onInterim = (transcript) => {
        // Could show in game UI
        if (engine.ui?.showInterim) {
            engine.ui.showInterim(transcript);
        }
    };
    
    // Add voice command
    const originalCommand = engine.command?.bind(engine);
    if (originalCommand) {
        engine.command = function(input) {
            const cmd = input.trim().toLowerCase();
            
            // Voice commands
            if (cmd === 'voice' || cmd === 'listen' || cmd === 'mic') {
                ui.toggleListening();
                return { 
                    success: true, 
                    message: recognition.manager.listening 
                        ? '🎤 Voice input active. Speak commands.'
                        : '🎤 Voice input stopped.'
                };
            }
            
            if (cmd === 'voice help' || cmd === 'speech help') {
                const help = recognition.getHelp();
                return {
                    success: true,
                    message: `🎤 Voice Input Help:\n\n` +
                        `Browser: ${help.browser.supported ? '✅ Supported' : '❌ ' + help.browser.note}\n` +
                        `${help.browser.privacy || ''}\n\n` +
                        `Native ${help.native.platform}: ${help.native.name}\n` +
                        `Shortcut: ${help.native.shortcut || help.native.activation}`
                };
            }
            
            // Pass to original
            return originalCommand(input);
        };
    }
    
    // Keyboard shortcut V for voice
    document.addEventListener('keydown', (e) => {
        if (e.key === 'v' && !e.ctrlKey && !e.metaKey && 
            !['INPUT', 'TEXTAREA'].includes(document.activeElement?.tagName)) {
            e.preventDefault();
            ui.toggleListening();
        }
    });
    
    return { recognition, ui };
}

/**
 * Create a voice-enabled adventure (speech + recognition)
 */
function createVoiceAdventure(containerId, options = {}) {
    // Create speaking adventure first
    const engine = typeof createSpeakingAdventure !== 'undefined'
        ? createSpeakingAdventure(containerId, options)
        : new AdventureEngine(containerId);
    
    // Add recognition
    addRecognitionToEngine(engine, {
        speakResponses: options.speakResponses ?? true,
        ...options
    });
    
    return engine;
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const ADVENTURE_RECOGNITION_EXPORTS = {
    RecognitionUI,
    addRecognitionToEngine,
    createVoiceAdventure
};

// Browser
if (typeof window !== 'undefined') {
    window.RecognitionUI = RecognitionUI;
    window.addRecognitionToEngine = addRecognitionToEngine;
    window.createVoiceAdventure = createVoiceAdventure;
}

// Node.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ADVENTURE_RECOGNITION_EXPORTS;
}
