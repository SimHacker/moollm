/**
 * speech.js — MOOLLM Adventure Speech Synthesis Module
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Extracted and refactored from lloooommagotchi.html
 * 
 * A comprehensive speech synthesis library that:
 * - Detects and classifies all available browser voices
 * - Supports voice selection by type, gender, age, language
 * - Provides convenient speaking methods with full customization
 * - Works across browsers (Chrome, Safari, Firefox, Edge)
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 * USAGE
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * // Initialize
 * const speech = new SpeechSystem();
 * await speech.ready;
 * 
 * // Simple speak
 * speech.speak("Hello, adventurer!");
 * 
 * // Speak with specific voice type
 * speech.speakRobot("RESISTANCE IS FUTILE");
 * speech.speakChild("I'm just a kid!");
 * speech.speakElderly("Back in my day...");
 * 
 * // Speak with full options
 * speech.speak("Welcome to the tower!", {
 *     voiceType: 'female',
 *     language: 'en-GB',
 *     pitch: 1.2,
 *     rate: 0.9
 * });
 * 
 * // Get random voice for character persistence
 * const characterVoice = speech.selectVoice({ gender: 'male', language: 'en' });
 * speech.speakWithVoice("I am your guide.", characterVoice);
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// VOICE DATABASE — Classifies and queries available voices
// ═══════════════════════════════════════════════════════════════════════════════

class VoiceDatabase {
    constructor() {
        // BLACKLISTED VOICES - DO NOT USE THESE!
        this.blacklist = [
            'Daniel (French (France))'  // Known problematic voice
        ];
        
        // Pattern-based recognition instead of huge lists
        this.patterns = {
            // Special effect voices (non-human)
            effects: /^(Bad News|Good News|Bells|Bahh|Boing|Bubbles|Cellos|Organ|Wobble|Whisper|Trinoids|Zarvox|Jester|Superstar)$/i,
            
            // Age-based patterns
            elderly: /^(Grandma|Grandpa|Grandm[aoe]ther|Grandf[aoe]ther)/i,
            child: /^(Junior|Kid|Child|Boy|Girl)/i,
            
            // Multi-language voice families (appear in many languages)
            multiLang: /^(Eddy|Flo|Reed|Rocko|Sandy|Shelley)(\s|$)/i,
            
            // Common female name patterns (fuzzy matching)
            femaleTokens: [
                'alice', 'amélie', 'amira', 'anna', 'catherine', 'damayanti', 
                'daria', 'ellen', 'flo', 'grandma', 'helena', 'ioana', 'joana',
                'kanya', 'karen', 'kathy', 'kyoko', 'lana', 'laura', 'lekha',
                'lesya', 'linh', 'luciana', 'marie', 'martha', 'meijia', 'melina',
                'milena', 'moira', 'monica', 'mónica', 'montse', 'nora', 'paulina',
                'samantha', 'sandy', 'sara', 'satu', 'shelley', 'tessa', 'tina',
                'tingting', 'tünde', 'yelda', 'yuna', 'zosia', 'zuzana'
            ],
            
            // Common male name patterns
            maleTokens: [
                'aaron', 'albert', 'arthur', 'daniel', 'eddy', 'fred', 'gordon',
                'grandpa', 'jacques', 'majed', 'martin', 'ralph', 'reed', 'rishi',
                'rocko', 'thomas', 'xander', 'hattori', 'o-ren'
            ],
            
            // Language detection from voice name
            langPattern: /\(([^)]+)\)\s*\(([a-z]{2}(?:-[A-Z]{2})?)\)$/,
            simpleLangPattern: /\(([a-z]{2}(?:-[A-Z]{2})?)\)$/,
            
            // Remote voice detection
            remote: /^Google\s/i,
            
            // Browser-specific patterns
            defaultTag: /\[DEFAULT\]/,
            localTag: /\[LOCAL\]/,
            remoteTag: /\[REMOTE\]/
        };
        
        // Known voice metadata (only for special cases and popular voices)
        this.knownVoices = new Map([
            // Special voices with unique characteristics
            ['Zarvox', { type: 'robot', gender: 'neutral', quality: 'synthetic' }],
            ['Whisper', { type: 'effect', gender: 'neutral', quality: 'soft' }],
            ['Bad News', { type: 'effect', gender: 'male', quality: 'dramatic' }],
            ['Good News', { type: 'effect', gender: 'female', quality: 'cheerful' }],
            ['Bells', { type: 'effect', gender: 'neutral', quality: 'musical' }],
            ['Bubbles', { type: 'effect', gender: 'neutral', quality: 'bubbly' }],
            ['Cellos', { type: 'effect', gender: 'neutral', quality: 'musical' }],
            ['Organ', { type: 'effect', gender: 'neutral', quality: 'musical' }],
            ['Trinoids', { type: 'robot', gender: 'neutral', quality: 'synthetic' }],
            ['Junior', { type: 'human', gender: 'male', age: 'child', quality: 'natural' }],
        ]);
    }
    
    /**
     * Parse a voice name string into structured components
     */
    parseVoiceName(voiceString) {
        const result = {
            name: '',
            language: '',
            langCode: '',
            country: '',
            isDefault: false,
            isLocal: true,
            isRemote: false,
            fullString: voiceString
        };
        
        // Check for tags
        result.isDefault = this.patterns.defaultTag.test(voiceString);
        result.isLocal = this.patterns.localTag.test(voiceString);
        result.isRemote = this.patterns.remoteTag.test(voiceString) || this.patterns.remote.test(voiceString);
        
        // Clean voice string from tags
        let cleanString = voiceString
            .replace(this.patterns.defaultTag, '')
            .replace(this.patterns.localTag, '')
            .replace(this.patterns.remoteTag, '')
            .trim();
        
        // Try to extract language info
        const langMatch = cleanString.match(this.patterns.langPattern);
        if (langMatch) {
            result.name = cleanString.substring(0, langMatch.index).trim();
            result.language = langMatch[1];
            result.langCode = langMatch[2];
            const countryMatch = result.langCode.match(/-([A-Z]{2})$/);
            if (countryMatch) {
                result.country = countryMatch[1];
            }
        } else {
            const simpleLangMatch = cleanString.match(this.patterns.simpleLangPattern);
            if (simpleLangMatch) {
                result.name = cleanString.substring(0, simpleLangMatch.index).trim();
                result.langCode = simpleLangMatch[1];
                const countryMatch = result.langCode.match(/-([A-Z]{2})$/);
                if (countryMatch) {
                    result.country = countryMatch[1];
                }
            } else {
                result.name = cleanString;
            }
        }
        
        return result;
    }
    
    /**
     * Classify a voice by type, gender, age, etc.
     */
    classifyVoice(voiceInfo) {
        const classification = {
            type: 'human',      // human, effect, robot
            gender: 'unknown',  // male, female, neutral, unknown
            age: 'adult',       // child, adult, elderly
            quality: 'natural', // natural, synthetic, effect
            isMultiLang: false
        };
        
        const name = voiceInfo.name.toLowerCase();
        
        // Check known voices first
        if (this.knownVoices.has(voiceInfo.name)) {
            return { ...classification, ...this.knownVoices.get(voiceInfo.name) };
        }
        
        // Check for effect voices
        if (this.patterns.effects.test(voiceInfo.name)) {
            classification.type = 'effect';
            classification.gender = 'neutral';
            classification.quality = 'effect';
            return classification;
        }
        
        // Check for elderly voices
        if (this.patterns.elderly.test(voiceInfo.name)) {
            classification.age = 'elderly';
            classification.gender = name.includes('grandma') ? 'female' : 'male';
            return classification;
        }
        
        // Check for child voices
        if (this.patterns.child.test(voiceInfo.name)) {
            classification.age = 'child';
            return classification;
        }
        
        // Check for multi-language voice families
        if (this.patterns.multiLang.test(voiceInfo.name)) {
            classification.isMultiLang = true;
        }
        
        // Gender detection through token matching
        const nameLower = name.toLowerCase();
        const femaleScore = this.patterns.femaleTokens.filter(token => 
            nameLower.includes(token) || this._fuzzyMatch(nameLower, token)
        ).length;
        const maleScore = this.patterns.maleTokens.filter(token => 
            nameLower.includes(token) || this._fuzzyMatch(nameLower, token)
        ).length;
        
        if (femaleScore > maleScore) {
            classification.gender = 'female';
        } else if (maleScore > femaleScore) {
            classification.gender = 'male';
        }
        
        return classification;
    }
    
    _fuzzyMatch(str1, str2) {
        if (Math.abs(str1.length - str2.length) > 3) return false;
        
        let matches = 0;
        const minLen = Math.min(str1.length, str2.length);
        for (let i = 0; i < minLen; i++) {
            if (str1[i] === str2[i]) matches++;
        }
        return matches / minLen > 0.7;
    }
    
    /**
     * Check if a voice language matches requested language
     */
    matchesLanguage(voiceLangCode, requestedLang) {
        if (!voiceLangCode || !requestedLang) return false;
        
        const voiceLang = voiceLangCode.toLowerCase();
        const requested = requestedLang.toLowerCase();
        
        // Exact match
        if (voiceLang === requested) return true;
        
        // Base language match (e.g., 'en' matches 'en-US', 'en-GB', etc.)
        if (requested.length === 2 && voiceLang.startsWith(requested + '-')) {
            return true;
        }
        
        // Specific variant requested but voice is base
        if (voiceLang.length === 2 && requested.startsWith(voiceLang + '-')) {
            return true;
        }
        
        return false;
    }
    
    /**
     * Find voices matching criteria
     */
    findVoices(criteria = {}) {
        const {
            type = null,      // 'human', 'effect', 'robot'
            gender = null,    // 'male', 'female', 'neutral'
            age = null,       // 'child', 'adult', 'elderly'
            language = null,  // 'en', 'en-US', etc.
            quality = null,   // 'natural', 'synthetic', 'effect'
            isLocal = null,   // true/false
            isMultiLang = null // true/false
        } = criteria;
        
        const allVoices = window.speechSynthesis.getVoices();
        const matches = [];
        
        for (const voice of allVoices) {
            // CHECK BLACKLIST - SKIP BANNED VOICES!
            if (this.blacklist.includes(voice.name)) {
                continue;
            }
            
            const voiceInfo = this.parseVoiceName(voice.name);
            voiceInfo.voiceObj = voice;
            
            // Language matching
            if (language && !this.matchesLanguage(voice.lang || voiceInfo.langCode, language)) {
                continue;
            }
            
            // Local/Remote matching
            if (isLocal !== null) {
                const voiceIsLocal = voice.localService !== false;
                if (isLocal !== voiceIsLocal) continue;
            }
            
            // Classification-based matching
            const classification = this.classifyVoice(voiceInfo);
            
            if (type && classification.type !== type) continue;
            if (gender && classification.gender !== gender && gender !== 'any') continue;
            if (age && classification.age !== age) continue;
            if (quality && classification.quality !== quality) continue;
            if (isMultiLang !== null && classification.isMultiLang !== isMultiLang) continue;
            
            matches.push({
                ...voiceInfo,
                ...classification,
                voice: voice
            });
        }
        
        return matches;
    }
    
    /**
     * Get a random voice matching criteria
     */
    getRandomVoice(criteria = {}) {
        const matches = this.findVoices(criteria);
        return matches.length > 0 ? 
            matches[Math.floor(Math.random() * matches.length)] : null;
    }
    
    /**
     * Get English voices
     */
    getEnglishVoices(preferLocal = true) {
        return this.findVoices({
            language: 'en',
            isLocal: preferLocal ? true : null,
            type: 'human'
        });
    }
    
    /**
     * Get a female voice
     */
    getFemaleVoice(language = null) {
        return this.getRandomVoice({
            gender: 'female',
            type: 'human',
            language: language
        });
    }
    
    /**
     * Get a male voice
     */
    getMaleVoice(language = null) {
        return this.getRandomVoice({
            gender: 'male',
            type: 'human',
            language: language
        });
    }
    
    /**
     * Get an effect voice
     */
    getEffectVoice() {
        return this.getRandomVoice({ type: 'effect' });
    }
    
    /**
     * Debug: Analyze all available voices
     */
    analyzeAvailableVoices() {
        const analysis = {
            total: 0,
            byType: {},
            byGender: {},
            byAge: {},
            byLanguage: {},
            multiLang: [],
            effects: [],
            unknown: []
        };
        
        const allVoices = window.speechSynthesis.getVoices();
        analysis.total = allVoices.length;
        
        for (const voice of allVoices) {
            const info = this.parseVoiceName(voice.name);
            const classification = this.classifyVoice(info);
            
            analysis.byType[classification.type] = (analysis.byType[classification.type] || 0) + 1;
            analysis.byGender[classification.gender] = (analysis.byGender[classification.gender] || 0) + 1;
            analysis.byAge[classification.age] = (analysis.byAge[classification.age] || 0) + 1;
            
            const lang = voice.lang || info.langCode || 'unknown';
            analysis.byLanguage[lang] = (analysis.byLanguage[lang] || 0) + 1;
            
            if (classification.isMultiLang) analysis.multiLang.push(info.name);
            if (classification.type === 'effect') analysis.effects.push(info.name);
            if (classification.gender === 'unknown' && classification.type === 'human') {
                analysis.unknown.push(info.name);
            }
        }
        
        return analysis;
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// SPEECH MANAGER — High-level speech synthesis API
// ═══════════════════════════════════════════════════════════════════════════════

class SpeechManager {
    constructor(voiceDB) {
        this.voiceDB = voiceDB;
        this.activeUtterances = new Set();
        this.voicesLoaded = false;
        this.loadAttempts = 0;
        this.maxLoadAttempts = 3;
        
        // Event callbacks
        this.onSpeakStart = null;
        this.onSpeakEnd = null;
        this.onSpeakError = null;
        
        this._initVoices();
    }
    
    _initVoices() {
        const attemptLoad = () => {
            const voices = window.speechSynthesis.getVoices();
            if (voices.length > 0) {
                this.voicesLoaded = true;
                console.log(`🎤 Loaded ${voices.length} voices`);
                return true;
            }
            return false;
        };
        
        if (attemptLoad()) return;
        
        window.speechSynthesis.onvoiceschanged = () => {
            if (!this.voicesLoaded && this.loadAttempts < this.maxLoadAttempts) {
                this.loadAttempts++;
                if (attemptLoad()) {
                    window.speechSynthesis.onvoiceschanged = null;
                }
            }
        };
    }
    
    /**
     * Select a voice without speaking
     */
    selectVoice(criteria = {}) {
        const voices = window.speechSynthesis.getVoices();
        if (voices.length === 0) return null;
        
        // If criteria is already a voice object, validate and return it
        if (criteria.voiceURI) {
            if (this.voiceDB && this.voiceDB.blacklist.includes(criteria.name)) {
                return null;
            }
            return this.isVoiceValid(criteria) ? criteria : null;
        }
        
        // If criteria is a voice URI string, find that exact voice
        if (typeof criteria === 'string') {
            const voice = voices.find(v => v.voiceURI === criteria);
            if (voice && this.voiceDB && this.voiceDB.blacklist.includes(voice.name)) {
                return null;
            }
            return voice || null;
        }
        
        // Random for 'any'
        if (criteria.voiceType === 'any' || Object.keys(criteria).length === 0) {
            const validVoices = voices.filter(v => 
                !this.voiceDB || !this.voiceDB.blacklist.includes(v.name)
            );
            return validVoices.length > 0 ? 
                validVoices[Math.floor(Math.random() * validVoices.length)] : null;
        }
        
        // Use voice database for smart selection
        const match = this.voiceDB.getRandomVoice(criteria);
        return match ? match.voice : null;
    }
    
    /**
     * Check if a voice is still valid (available in current browser)
     */
    isVoiceValid(voice) {
        if (!voice || !voice.voiceURI) return false;
        const voices = window.speechSynthesis.getVoices();
        return voices.some(v => v.voiceURI === voice.voiceURI);
    }
    
    /**
     * Get a diverse set of voices (for multi-character conversations)
     */
    getDiverseVoices(count = 5) {
        const voices = window.speechSynthesis.getVoices();
        if (voices.length === 0) return [];
        
        const diverse = [];
        const usedLangs = new Set();
        const usedTypes = new Set();
        
        for (let i = 0; i < Math.min(count, voices.length); i++) {
            let bestVoice = null;
            let bestScore = -1;
            
            for (const voice of voices) {
                if (diverse.some(v => v.voiceURI === voice.voiceURI)) continue;
                
                let score = 0;
                const info = this.voiceDB.parseVoiceName(voice.name);
                const lang = voice.lang || info.langCode || 'unknown';
                
                if (!usedLangs.has(lang)) score += 3;
                
                const classification = this.voiceDB.classifyVoice(info);
                if (classification.type === 'effect' || classification.type === 'robot') score += 2;
                if (!usedTypes.has(classification.type)) score += 1;
                if (!lang.startsWith('en')) score += 1;
                
                if (score > bestScore) {
                    bestScore = score;
                    bestVoice = voice;
                }
            }
            
            if (bestVoice) {
                diverse.push(bestVoice);
                const info = this.voiceDB.parseVoiceName(bestVoice.name);
                const lang = bestVoice.lang || info.langCode || 'unknown';
                usedLangs.add(lang);
                const classification = this.voiceDB.classifyVoice(info);
                usedTypes.add(classification.type);
            }
        }
        
        while (diverse.length < count && diverse.length < voices.length) {
            const randomVoice = voices[Math.floor(Math.random() * voices.length)];
            if (!diverse.some(v => v.voiceURI === randomVoice.voiceURI)) {
                diverse.push(randomVoice);
            }
        }
        
        return diverse;
    }
    
    /**
     * Speak with a specific voice object
     */
    speakWithVoice(text, voice, options = {}) {
        if (!voice || !this.isVoiceValid(voice)) {
            console.warn('🎤 Invalid voice provided, using default');
            return this.speak(text, options);
        }
        
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.voice = voice;
        
        this._applyOptions(utterance, options, voice);
        window.speechSynthesis.speak(utterance);
        
        return utterance;
    }
    
    /**
     * Main speak method with full options
     */
    speak(text, options = {}) {
        if (!window.speechSynthesis) {
            console.warn('🎤 Speech synthesis not available');
            return null;
        }
        
        const defaults = {
            voiceType: 'any',        // 'male', 'female', 'child', 'elderly', 'robot', 'effect', 'any'
            language: null,          // null, 'en', 'en-US', etc.
            preferLocal: true,       // Prefer local voices
            
            pitch: 1.0,              // Base pitch
            pitchMin: null,          // Min for random range
            pitchMax: null,          // Max for random range
            rate: 1.0,               // Base rate
            rateMin: null,           // Min for random range
            rateMax: null,           // Max for random range
            volume: 1.0,             // Volume 0-1
            
            trackUtterance: true,    // Track for cancellation
            cleanText: true,         // Remove shy hyphens etc
            
            onStart: null,
            onEnd: null,
            onError: null,
            onPause: null,
            onResume: null,
            
            queue: true              // Queue or cancel previous
        };
        
        const config = { ...defaults, ...options };
        
        try {
            const cleanedText = config.cleanText ? text.replace(/\u00AD/g, '') : text;
            const utterance = new SpeechSynthesisUtterance(cleanedText);
            
            // Select voice
            let selectedVoice = null;
            const voices = window.speechSynthesis.getVoices();
            
            if (voices.length > 0) {
                if (config.voiceType === 'any') {
                    selectedVoice = voices[Math.floor(Math.random() * voices.length)];
                } else {
                    const criteria = {};
                    
                    if (config.voiceType === 'male') {
                        criteria.gender = 'male';
                        criteria.type = 'human';
                    } else if (config.voiceType === 'female') {
                        criteria.gender = 'female';
                        criteria.type = 'human';
                    } else if (config.voiceType === 'child') {
                        criteria.age = 'child';
                        criteria.type = 'human';
                    } else if (config.voiceType === 'elderly') {
                        criteria.age = 'elderly';
                        criteria.type = 'human';
                    } else if (config.voiceType === 'robot') {
                        criteria.type = 'robot';
                    } else if (config.voiceType === 'effect') {
                        criteria.type = 'effect';
                    }
                    
                    if (config.language) criteria.language = config.language;
                    if (config.preferLocal) criteria.isLocal = true;
                    
                    const voiceMatch = this.voiceDB.getRandomVoice(criteria);
                    if (voiceMatch) selectedVoice = voiceMatch.voice;
                }
                
                if (selectedVoice) {
                    utterance.voice = selectedVoice;
                    console.log(`🎤 Selected: ${selectedVoice.name} (${selectedVoice.lang})`);
                }
            }
            
            // Apply parameters with randomization
            if (config.pitchMin !== null && config.pitchMax !== null) {
                utterance.pitch = config.pitchMin + Math.random() * (config.pitchMax - config.pitchMin);
            } else {
                utterance.pitch = config.pitch;
            }
            
            if (config.rateMin !== null && config.rateMax !== null) {
                utterance.rate = config.rateMin + Math.random() * (config.rateMax - config.rateMin);
            } else {
                utterance.rate = config.rate;
            }
            
            utterance.volume = config.volume;
            
            this._applyOptions(utterance, config, selectedVoice);
            
            if (!config.queue) {
                window.speechSynthesis.cancel();
            }
            
            window.speechSynthesis.speak(utterance);
            
            return utterance;
            
        } catch (error) {
            console.error('🎤 Speech error:', error);
            return null;
        }
    }
    
    _applyOptions(utterance, config, voice) {
        utterance.pitch = config.pitch || 1.0;
        utterance.rate = config.rate || 1.0;
        utterance.volume = config.volume || 1.0;
        
        utterance.onstart = (event) => {
            if (this.onSpeakStart) this.onSpeakStart(event, voice);
            if (config.onStart) config.onStart(event);
        };
        
        utterance.onend = (event) => {
            if (config.trackUtterance !== false) {
                this.activeUtterances.delete(utterance);
            }
            if (this.onSpeakEnd) this.onSpeakEnd(event, voice);
            if (config.onEnd) config.onEnd(event);
        };
        
        utterance.onerror = (event) => {
            if (config.trackUtterance !== false) {
                this.activeUtterances.delete(utterance);
            }
            if (this.onSpeakError) this.onSpeakError(event, voice);
            if (config.onError) config.onError(event);
        };
        
        utterance.onpause = (event) => {
            if (config.onPause) config.onPause(event);
        };
        
        utterance.onresume = (event) => {
            if (config.onResume) config.onResume(event);
        };
        
        if (config.trackUtterance !== false) {
            this.activeUtterances.add(utterance);
        }
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // Convenience methods
    // ─────────────────────────────────────────────────────────────────────────
    
    speakMale(text, options = {}) {
        return this.speak(text, { ...options, voiceType: 'male' });
    }
    
    speakFemale(text, options = {}) {
        return this.speak(text, { ...options, voiceType: 'female' });
    }
    
    speakChild(text, options = {}) {
        return this.speak(text, { ...options, voiceType: 'child' });
    }
    
    speakElderly(text, options = {}) {
        return this.speak(text, { ...options, voiceType: 'elderly' });
    }
    
    speakRobot(text, options = {}) {
        return this.speak(text, { ...options, voiceType: 'robot' });
    }
    
    speakEffect(text, options = {}) {
        return this.speak(text, { ...options, voiceType: 'effect' });
    }
    
    speakRandom(text, options = {}) {
        return this.speak(text, { 
            ...options, 
            voiceType: 'any',
            pitchMin: options.pitchMin || 0.5,
            pitchMax: options.pitchMax || 1.5,
            rateMin: options.rateMin || 0.5,
            rateMax: options.rateMax || 1.5
        });
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // Control methods
    // ─────────────────────────────────────────────────────────────────────────
    
    pause() {
        window.speechSynthesis.pause();
    }
    
    resume() {
        window.speechSynthesis.resume();
    }
    
    cancel() {
        window.speechSynthesis.cancel();
        this.activeUtterances.clear();
    }
    
    isSpeaking() {
        return window.speechSynthesis.speaking;
    }
    
    isPaused() {
        return window.speechSynthesis.paused;
    }
    
    isPending() {
        return window.speechSynthesis.pending;
    }
    
    getActiveCount() {
        return this.activeUtterances.size;
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// SPEECH SYSTEM — Top-level facade combining VoiceDatabase and SpeechManager
// ═══════════════════════════════════════════════════════════════════════════════

class SpeechSystem {
    constructor() {
        this.voiceDB = new VoiceDatabase();
        this.manager = new SpeechManager(this.voiceDB);
        
        // Promise that resolves when voices are loaded
        this.ready = this._waitForVoices();
    }
    
    _waitForVoices() {
        return new Promise((resolve) => {
            const voices = window.speechSynthesis.getVoices();
            if (voices.length > 0) {
                resolve(this);
                return;
            }
            
            const timeout = setTimeout(() => resolve(this), 2000);
            
            window.speechSynthesis.onvoiceschanged = () => {
                clearTimeout(timeout);
                resolve(this);
            };
        });
    }
    
    // ─────────────────────────────────────────────────────────────────────────
    // Delegate to manager
    // ─────────────────────────────────────────────────────────────────────────
    
    speak(text, options) { return this.manager.speak(text, options); }
    speakWithVoice(text, voice, options) { return this.manager.speakWithVoice(text, voice, options); }
    speakMale(text, options) { return this.manager.speakMale(text, options); }
    speakFemale(text, options) { return this.manager.speakFemale(text, options); }
    speakChild(text, options) { return this.manager.speakChild(text, options); }
    speakElderly(text, options) { return this.manager.speakElderly(text, options); }
    speakRobot(text, options) { return this.manager.speakRobot(text, options); }
    speakEffect(text, options) { return this.manager.speakEffect(text, options); }
    speakRandom(text, options) { return this.manager.speakRandom(text, options); }
    
    selectVoice(criteria) { return this.manager.selectVoice(criteria); }
    getDiverseVoices(count) { return this.manager.getDiverseVoices(count); }
    
    pause() { this.manager.pause(); }
    resume() { this.manager.resume(); }
    cancel() { this.manager.cancel(); }
    isSpeaking() { return this.manager.isSpeaking(); }
    isPaused() { return this.manager.isPaused(); }
    isPending() { return this.manager.isPending(); }
    
    // ─────────────────────────────────────────────────────────────────────────
    // Delegate to voiceDB
    // ─────────────────────────────────────────────────────────────────────────
    
    findVoices(criteria) { return this.voiceDB.findVoices(criteria); }
    getEnglishVoices(preferLocal) { return this.voiceDB.getEnglishVoices(preferLocal); }
    getFemaleVoice(language) { return this.voiceDB.getFemaleVoice(language); }
    getMaleVoice(language) { return this.voiceDB.getMaleVoice(language); }
    getEffectVoice() { return this.voiceDB.getEffectVoice(); }
    analyzeAvailableVoices() { return this.voiceDB.analyzeAvailableVoices(); }
    
    // ─────────────────────────────────────────────────────────────────────────
    // Event callbacks
    // ─────────────────────────────────────────────────────────────────────────
    
    set onSpeakStart(fn) { this.manager.onSpeakStart = fn; }
    set onSpeakEnd(fn) { this.manager.onSpeakEnd = fn; }
    set onSpeakError(fn) { this.manager.onSpeakError = fn; }
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const SPEECH_EXPORTS = {
    SpeechSystem,
    SpeechManager,
    VoiceDatabase
};

// Browser: attach to window
if (typeof window !== 'undefined') {
    window.Speech = SPEECH_EXPORTS;
    window.SpeechSystem = SpeechSystem;
}

// Node.js CommonJS
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SPEECH_EXPORTS;
}

// ES Module export
try {
    if (typeof exports === 'object') {
        Object.assign(exports, SPEECH_EXPORTS);
    }
} catch (e) { /* Not in module context */ }
