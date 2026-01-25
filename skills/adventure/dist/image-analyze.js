/**
 * image-analyze.js — Vision LLM image analysis → YAML mining
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Send image + prompt to vision models, get structured YAML metadata back.
 * Browser-side reimplementation of the image-mining skill.
 * 
 * PROVIDERS:
 *   openai      GPT-4o, GPT-4 Vision
 *   anthropic   Claude 3.5 Sonnet, Claude 3 Opus
 *   google      Gemini 1.5 Pro, Gemini 1.5 Flash
 * 
 * OUTPUT:
 *   Structured YAML jazz — same format as MINING-*.yml files
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// VISION PROVIDER CONFIGS
// ═══════════════════════════════════════════════════════════════════════════════

const VISION_PROVIDERS = {
    openai: {
        name: 'OpenAI',
        models: ['gpt-4o', 'gpt-4o-mini', 'gpt-4-turbo'],
        defaultModel: 'gpt-4o',
        endpoint: 'https://api.openai.com/v1/chat/completions',
        keyName: 'OPENAI_API_KEY',
        maxImageSize: 20 * 1024 * 1024  // 20MB
    },
    
    anthropic: {
        name: 'Anthropic',
        models: ['claude-sonnet-4-20250514', 'claude-3-5-sonnet-20241022', 'claude-3-opus-20240229'],
        defaultModel: 'claude-sonnet-4-20250514',
        endpoint: 'https://api.anthropic.com/v1/messages',
        keyName: 'ANTHROPIC_API_KEY',
        maxImageSize: 20 * 1024 * 1024,
        note: 'Requires CORS proxy or backend'
    },
    
    google: {
        name: 'Google',
        models: ['gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-2.0-flash-exp'],
        defaultModel: 'gemini-1.5-flash',
        endpoint: 'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent',
        keyName: 'GOOGLE_API_KEY',
        maxImageSize: 20 * 1024 * 1024
    }
};

// ═══════════════════════════════════════════════════════════════════════════════
// MINING LAYER TEMPLATES — Prompt patterns for different analysis types
// ═══════════════════════════════════════════════════════════════════════════════

const MINING_LAYERS = {
    // Core visual analysis
    visual: {
        name: 'Visual Analysis',
        prompt: `Analyze this image and output YAML with these sections:
- composition: (rule of thirds, leading lines, framing, focal point)
- lighting: (direction, quality, color temperature, mood)
- color_palette: (dominant colors, harmony, emotional associations)
- depth: (foreground, midground, background elements)
- technical: (estimated focal length, aperture, exposure)`,
    },
    
    // Semantic/meaning layer
    semantic: {
        name: 'Semantic Mining',
        prompt: `Extract semantic meaning from this image as YAML:
- subjects: (list main subjects with descriptions)
- actions: (what's happening, implied motion)
- relationships: (between subjects, spatial and conceptual)
- symbols: (symbolic elements and their interpretations)
- narrative: (what story does this tell)
- mood: (emotional tone, atmosphere)`,
    },
    
    // Text/signage extraction
    text: {
        name: 'Text Extraction',
        prompt: `Extract all text and signage from this image as YAML:
- text_elements: (list each text element with location, content, font_style, size_estimate)
- signage: (any signs, labels, displays)
- typography: (font families, styles, hierarchy)
- language: (detected languages)
- legibility: (clarity, contrast, readability)`,
    },
    
    // Character/people analysis
    characters: {
        name: 'Character Analysis',
        prompt: `Analyze any people or characters in this image as YAML:
- subjects: (list each person/character)
  - appearance: (clothing, posture, expression)
  - emotion: (detected emotional state)
  - gaze: (where they're looking)
  - role: (implied role or occupation)
- interactions: (between characters)
- crowd_dynamics: (if multiple people)`,
    },
    
    // Architecture/environment
    environment: {
        name: 'Environment Analysis',
        prompt: `Analyze the environment and setting as YAML:
- location_type: (indoor/outdoor, urban/rural/natural)
- architecture: (style, era, materials)
- time_of_day: (lighting suggests...)
- weather: (if visible)
- era: (modern, vintage, futuristic)
- cultural_markers: (regional/cultural indicators)`,
    },
    
    // Object inventory
    objects: {
        name: 'Object Inventory',
        prompt: `Create an inventory of objects in this image as YAML:
- objects: (list each significant object)
  - name: 
  - location: (position in frame)
  - condition: (new, worn, etc)
  - significance: (why it matters)
- props: (background/incidental objects)
- textures: (notable material textures)`,
    },
    
    // Artistic/stylistic
    artistic: {
        name: 'Artistic Analysis',
        prompt: `Analyze artistic and stylistic elements as YAML:
- style: (photographic style, art movement influences)
- influences: (artists, photographers, films this evokes)
- techniques: (notable artistic techniques)
- genre: (documentary, portrait, landscape, etc)
- originality: (unique elements, clichés avoided/used)`,
    },
    
    // Passersby/viewer perspective
    passersby: {
        name: 'Passerby Perspectives',
        prompt: `Imagine different viewers encountering this scene. Output YAML:
- perspectives:
  - viewer: "tourist"
    reaction: (what they'd notice, think, feel)
  - viewer: "local resident"
    reaction: 
  - viewer: "photographer"
    reaction:
  - viewer: "child"
    reaction:
  - viewer: "historian"
    reaction:
- the_scene_itself: (if this scene could speak, what would it say)`,
    },
    
    // Satellite/aerial view
    satellite: {
        name: 'Orbital Perspective',
        prompt: `Imagine surveillance/orbital views of this location. Output YAML:
- thermal_signature: (heat patterns)
- traffic_patterns: (movement, flow)
- timestamp_markers: (time of day indicators)
- anomalies: (unusual patterns)
- historical_changes: (what might have changed over time)
- coordinates_estimate: (fictional but plausible)`,
    },
    
    // Sound layer (imagined)
    soundscape: {
        name: 'Soundscape Mining',
        prompt: `Imagine the soundscape of this scene. Output YAML:
- ambient: (background sounds)
- foreground: (prominent sounds)
- silence: (notable quiet areas)
- rhythm: (temporal patterns)
- emotional_tone: (what the sounds convey)
- decibel_estimate: (quiet/moderate/loud areas)`,
    },
    
    // Custom/freeform
    custom: {
        name: 'Custom Analysis',
        prompt: null  // User provides
    }
};

// ═══════════════════════════════════════════════════════════════════════════════
// IMAGE ANALYZER
// ═══════════════════════════════════════════════════════════════════════════════

class ImageAnalyzer {
    constructor(options = {}) {
        this.keyStore = options.keyStore || new ImageAnalyzeKeyStore();
        this.defaultProvider = options.defaultProvider || null;
        this.onProgress = options.onProgress || (() => {});
    }
    
    /**
     * Get available providers
     */
    getAvailableProviders() {
        return Object.keys(VISION_PROVIDERS).filter(p => this.keyStore.getKey(p));
    }
    
    /**
     * Get best available provider
     */
    getBestProvider() {
        if (this.defaultProvider && this.keyStore.getKey(this.defaultProvider)) {
            return this.defaultProvider;
        }
        const available = this.getAvailableProviders();
        const preference = ['google', 'openai', 'anthropic'];
        for (const p of preference) {
            if (available.includes(p)) return p;
        }
        return null;
    }
    
    /**
     * Analyze image with vision LLM
     * @param {string|Blob|File} image - URL, base64, or file
     * @param {string|object} layer - Mining layer name or custom prompt
     * @param {object} options - Analysis options
     * @returns {Promise<{yaml: string, parsed: object, provider: string}>}
     */
    async analyze(image, layer = 'visual', options = {}) {
        const provider = options.provider || this.getBestProvider();
        
        if (!provider) {
            throw new Error('No vision provider configured. Add an API key.');
        }
        
        const key = options.apiKey || this.keyStore.getKey(provider);
        if (!key) {
            throw new Error(`No API key for provider: ${provider}`);
        }
        
        // Build prompt
        let prompt;
        if (typeof layer === 'string' && MINING_LAYERS[layer]) {
            prompt = MINING_LAYERS[layer].prompt;
            if (!prompt) {
                throw new Error(`Layer "${layer}" requires custom prompt`);
            }
        } else if (typeof layer === 'object' && layer.prompt) {
            prompt = layer.prompt;
        } else if (typeof layer === 'string') {
            prompt = layer;  // Treat as custom prompt
        } else {
            throw new Error('Invalid layer specification');
        }
        
        // Add YAML instruction
        const fullPrompt = `${prompt}

IMPORTANT: Output ONLY valid YAML. No markdown code fences. No explanations before or after.
Start directly with the first key.`;
        
        // Convert image to base64 if needed
        const imageData = await this._prepareImage(image);
        
        this.onProgress({ stage: 'analyzing', provider, layer: typeof layer === 'string' ? layer : 'custom' });
        
        let result;
        switch (provider) {
            case 'openai':
                result = await this._analyzeOpenAI(imageData, fullPrompt, key, options);
                break;
            case 'google':
                result = await this._analyzeGoogle(imageData, fullPrompt, key, options);
                break;
            case 'anthropic':
                result = await this._analyzeAnthropic(imageData, fullPrompt, key, options);
                break;
            default:
                throw new Error(`Unknown provider: ${provider}`);
        }
        
        this.onProgress({ stage: 'complete', provider });
        
        // Parse YAML
        let parsed = null;
        try {
            // Try to use YAML library if available
            if (typeof YAML !== 'undefined') {
                parsed = YAML.parse(result.yaml);
            } else if (typeof jsyaml !== 'undefined') {
                parsed = jsyaml.load(result.yaml);
            }
        } catch (e) {
            console.warn('YAML parse failed:', e.message);
        }
        
        return {
            yaml: result.yaml,
            parsed,
            provider,
            model: result.model,
            layer: typeof layer === 'string' ? layer : 'custom'
        };
    }
    
    /**
     * Run multiple mining layers
     */
    async mineAll(image, layers = ['visual', 'semantic', 'text'], options = {}) {
        const results = {};
        
        for (const layer of layers) {
            this.onProgress({ stage: 'layer', layer, total: layers.length });
            try {
                results[layer] = await this.analyze(image, layer, options);
            } catch (e) {
                results[layer] = { error: e.message };
            }
        }
        
        return results;
    }
    
    /**
     * Prepare image for API
     */
    async _prepareImage(image) {
        // Already base64
        if (typeof image === 'string' && image.startsWith('data:')) {
            return {
                base64: image.split(',')[1],
                mimeType: image.match(/data:([^;]+)/)?.[1] || 'image/png'
            };
        }
        
        // URL - fetch and convert
        if (typeof image === 'string' && (image.startsWith('http') || image.startsWith('/'))) {
            const response = await fetch(image);
            const blob = await response.blob();
            return this._blobToBase64(blob);
        }
        
        // File or Blob
        if (image instanceof Blob) {
            return this._blobToBase64(image);
        }
        
        throw new Error('Unsupported image format');
    }
    
    async _blobToBase64(blob) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = () => {
                const dataUrl = reader.result;
                resolve({
                    base64: dataUrl.split(',')[1],
                    mimeType: blob.type || 'image/png'
                });
            };
            reader.onerror = reject;
            reader.readAsDataURL(blob);
        });
    }
    
    /**
     * OpenAI GPT-4 Vision
     */
    async _analyzeOpenAI(imageData, prompt, key, options) {
        const config = VISION_PROVIDERS.openai;
        const model = options.model || config.defaultModel;
        
        const response = await fetch(config.endpoint, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${key}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model,
                messages: [{
                    role: 'user',
                    content: [
                        {
                            type: 'image_url',
                            image_url: {
                                url: `data:${imageData.mimeType};base64,${imageData.base64}`
                            }
                        },
                        {
                            type: 'text',
                            text: prompt
                        }
                    ]
                }],
                max_tokens: options.maxTokens || 2000
            })
        });
        
        if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(`OpenAI error: ${error.error?.message || response.statusText}`);
        }
        
        const data = await response.json();
        const yaml = data.choices[0]?.message?.content || '';
        
        return { yaml: this._cleanYaml(yaml), model };
    }
    
    /**
     * Google Gemini Vision
     */
    async _analyzeGoogle(imageData, prompt, key, options) {
        const config = VISION_PROVIDERS.google;
        const model = options.model || config.defaultModel;
        
        const endpoint = config.endpoint.replace('{model}', model) + `?key=${key}`;
        
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                contents: [{
                    parts: [
                        {
                            inline_data: {
                                mime_type: imageData.mimeType,
                                data: imageData.base64
                            }
                        },
                        {
                            text: prompt
                        }
                    ]
                }],
                generationConfig: {
                    maxOutputTokens: options.maxTokens || 2000
                }
            })
        });
        
        if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(`Google error: ${error.error?.message || response.statusText}`);
        }
        
        const data = await response.json();
        const yaml = data.candidates?.[0]?.content?.parts?.[0]?.text || '';
        
        return { yaml: this._cleanYaml(yaml), model };
    }
    
    /**
     * Anthropic Claude Vision
     */
    async _analyzeAnthropic(imageData, prompt, key, options) {
        const config = VISION_PROVIDERS.anthropic;
        const model = options.model || config.defaultModel;
        
        const response = await fetch(config.endpoint, {
            method: 'POST',
            headers: {
                'x-api-key': key,
                'Content-Type': 'application/json',
                'anthropic-version': '2023-06-01',
                'anthropic-dangerous-direct-browser-access': 'true'
            },
            body: JSON.stringify({
                model,
                max_tokens: options.maxTokens || 2000,
                messages: [{
                    role: 'user',
                    content: [
                        {
                            type: 'image',
                            source: {
                                type: 'base64',
                                media_type: imageData.mimeType,
                                data: imageData.base64
                            }
                        },
                        {
                            type: 'text',
                            text: prompt
                        }
                    ]
                }]
            })
        });
        
        if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(`Anthropic error: ${error.error?.message || response.statusText}`);
        }
        
        const data = await response.json();
        const yaml = data.content?.[0]?.text || '';
        
        return { yaml: this._cleanYaml(yaml), model };
    }
    
    /**
     * Clean YAML output (strip markdown fences, etc)
     */
    _cleanYaml(text) {
        return text
            .replace(/^```ya?ml\n?/gm, '')
            .replace(/^```\n?/gm, '')
            .replace(/```$/gm, '')
            .trim();
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// KEY STORAGE (shared with image-gen if available)
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Key store adapter — uses global APIKeyStore if available
 */
class ImageAnalyzeKeyStore {
    constructor() {
        // Use global key store from api-keys.js if available
        this._global = typeof globalKeyStore !== 'undefined' ? globalKeyStore : null;
        this.storagePrefix = 'moollm_apikey_';  // Match api-keys.js format
    }
    
    setKey(provider, key) {
        if (this._global) {
            this._global.set(provider, key);
        } else {
            localStorage.setItem(this.storagePrefix + provider, key);
        }
    }
    
    getKey(provider) {
        if (this._global) {
            return this._global.get(provider);
        }
        return localStorage.getItem(this.storagePrefix + provider);
    }
    
    removeKey(provider) {
        if (this._global) {
            this._global.delete(provider);
        } else {
            localStorage.removeItem(this.storagePrefix + provider);
        }
    }
    
    getConfiguredProviders() {
        return Object.keys(VISION_PROVIDERS).filter(p => this.getKey(p));
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// KEY SETUP UI
// ═══════════════════════════════════════════════════════════════════════════════

class ImageAnalyzeKeyUI {
    constructor(analyzer) {
        this.analyzer = analyzer;
        this.keyStore = analyzer.keyStore;
    }
    
    show() {
        const existing = document.getElementById('imageanalyze-key-modal');
        if (existing) existing.remove();
        
        const modal = document.createElement('div');
        modal.id = 'imageanalyze-key-modal';
        modal.innerHTML = `
            <div style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.8);z-index:10000;display:flex;align-items:center;justify-content:center;">
                <div style="background:#1a1a2e;border-radius:8px;padding:24px;max-width:500px;width:90%;color:#eee;font-family:monospace;">
                    <h2 style="margin:0 0 16px;color:#4ecca3;">🔬 Vision Analysis Keys</h2>
                    <p style="color:#888;margin-bottom:20px;">
                        Keys for image analysis via vision LLMs. Shared with image generation.
                    </p>
                    
                    ${Object.entries(VISION_PROVIDERS).map(([id, p]) => `
                        <div style="margin-bottom:16px;">
                            <label style="display:block;margin-bottom:4px;color:#e94560;">${p.name}</label>
                            <input type="password" 
                                   id="imageanalyze-key-${id}"
                                   value="${this.keyStore.getKey(id) || ''}"
                                   placeholder="${p.keyName}"
                                   style="width:100%;padding:8px;background:#16213e;border:1px solid #0f3460;border-radius:4px;color:#eee;font-family:monospace;">
                            <small style="color:#666;">Models: ${p.models.slice(0,2).join(', ')}${p.note ? ` (${p.note})` : ''}</small>
                        </div>
                    `).join('')}
                    
                    <div style="display:flex;gap:10px;margin-top:20px;">
                        <button id="imageanalyze-key-save" style="flex:1;padding:10px;background:#4ecca3;border:none;border-radius:4px;color:#1a1a2e;cursor:pointer;font-weight:bold;">
                            Save Keys
                        </button>
                        <button id="imageanalyze-key-cancel" style="flex:1;padding:10px;background:#0f3460;border:none;border-radius:4px;color:#eee;cursor:pointer;">
                            Cancel
                        </button>
                    </div>
                </div>
            </div>
        `;
        
        document.body.appendChild(modal);
        
        document.getElementById('imageanalyze-key-save').onclick = () => {
            Object.keys(VISION_PROVIDERS).forEach(id => {
                const input = document.getElementById(`imageanalyze-key-${id}`);
                const value = input.value.trim();
                if (value) {
                    this.keyStore.setKey(id, value);
                } else {
                    this.keyStore.removeKey(id);
                }
            });
            modal.remove();
        };
        
        document.getElementById('imageanalyze-key-cancel').onclick = () => modal.remove();
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// INTEGRATION WITH ADVENTURE ENGINE
// ═══════════════════════════════════════════════════════════════════════════════

function addImageAnalyzeToEngine(engine, options = {}) {
    const analyzer = new ImageAnalyzer({
        onProgress: (progress) => {
            console.log('🔬 Analysis:', progress);
            engine.ui?.print(`[Analysis: ${progress.stage}${progress.layer ? ' layer=' + progress.layer : ''}]`, 'system');
        },
        ...options
    });
    
    const keyUI = new ImageAnalyzeKeyUI(analyzer);
    
    engine.imageAnalyze = analyzer;
    engine.imageAnalyzeUI = keyUI;
    
    // Commands
    const origCommand = engine.command.bind(engine);
    engine.command = function(input) {
        const lower = input.toLowerCase().trim();
        
        if (lower === 'analyze keys' || lower === 'vision keys') {
            keyUI.show();
            return { handled: true };
        }
        
        if (lower.startsWith('analyze image ') || lower.startsWith('mine image ')) {
            const parts = input.replace(/^(analyze|mine) image\s+/i, '').split(' ');
            const url = parts[0];
            const layer = parts[1] || 'visual';
            
            engine.ui?.print(`Mining "${layer}" layer...`, 'system');
            
            analyzer.analyze(url, layer)
                .then(result => {
                    engine.ui?.print(`✅ Mined via ${result.provider}`, 'response');
                    engine.ui?.print('```yaml\n' + result.yaml + '\n```', 'response');
                })
                .catch(err => {
                    engine.ui?.print(`❌ Analysis failed: ${err.message}`, 'error');
                });
            
            return { handled: true, async: true };
        }
        
        return origCommand(input);
    };
    
    console.log('🔬 Image analysis added to engine');
    console.log('   Commands: "vision keys", "mine image <url> [layer]"');
    console.log('   Layers:', Object.keys(MINING_LAYERS).join(', '));
    
    return analyzer;
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const IMAGE_ANALYZE_EXPORTS = {
    VISION_PROVIDERS,
    MINING_LAYERS,
    ImageAnalyzer,
    ImageAnalyzeKeyStore,
    ImageAnalyzeKeyUI,
    addImageAnalyzeToEngine
};

if (typeof window !== 'undefined') {
    Object.assign(window, IMAGE_ANALYZE_EXPORTS);
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = IMAGE_ANALYZE_EXPORTS;
}
