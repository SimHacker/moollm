/**
 * image-generate.js — Browser-based multi-provider image generation
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Generate images across different providers from the browser.
 * Mirrors the Python visualizer's multi-provider architecture.
 * 
 * PROVIDERS:
 *   openai      DALL-E 3, GPT-Image
 *   google      Imagen (via Gemini API)
 *   stability   Stable Diffusion 3.5
 *   replicate   Flux, SDXL
 *   
 * AUTH:
 *   Keys stored in localStorage (user provides)
 *   Or passed per-request
 *   Never sent to our servers — direct to provider APIs
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// PROVIDER CONFIGS
// ═══════════════════════════════════════════════════════════════════════════════

const IMAGE_PROVIDERS = {
    openai: {
        name: 'OpenAI',
        models: ['dall-e-3', 'dall-e-2'],
        defaultModel: 'dall-e-3',
        endpoint: 'https://api.openai.com/v1/images/generations',
        keyName: 'OPENAI_API_KEY',
        sizes: ['1024x1024', '1024x1792', '1792x1024'],
        defaultSize: '1024x1024'
    },
    
    google: {
        name: 'Google Imagen',
        models: ['imagen-3.0-generate-002', 'imagen-3.0-fast-generate-001'],
        defaultModel: 'imagen-3.0-generate-002',
        endpoint: 'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent',
        keyName: 'GOOGLE_API_KEY',
        sizes: ['1024x1024'],
        defaultSize: '1024x1024',
        note: 'Uses Gemini API with image generation'
    },
    
    stability: {
        name: 'Stability AI',
        models: ['sd3.5-large', 'sd3.5-medium', 'sd3-turbo'],
        defaultModel: 'sd3.5-large',
        endpoint: 'https://api.stability.ai/v2beta/stable-image/generate/sd3',
        keyName: 'STABILITY_API_KEY',
        sizes: ['1024x1024', '1536x1024', '1024x1536'],
        defaultSize: '1024x1024'
    },
    
    replicate: {
        name: 'Replicate',
        models: ['black-forest-labs/flux-1.1-pro', 'stability-ai/sdxl'],
        defaultModel: 'black-forest-labs/flux-1.1-pro',
        endpoint: 'https://api.replicate.com/v1/predictions',
        keyName: 'REPLICATE_API_TOKEN',
        sizes: ['1024x1024'],
        defaultSize: '1024x1024',
        note: 'Async — polls for completion'
    }
};

// ═══════════════════════════════════════════════════════════════════════════════
// KEY STORAGE
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Key store adapter — uses global APIKeyStore if available
 */
class ImageGenerateKeyStore {
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
        return Object.keys(IMAGE_PROVIDERS).filter(p => this.getKey(p));
    }
    
    hasAnyKey() {
        return this.getConfiguredProviders().length > 0;
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// IMAGE GENERATOR
// ═══════════════════════════════════════════════════════════════════════════════

class ImageGenerator {
    constructor(options = {}) {
        this.keyStore = options.keyStore || new ImageGenerateKeyStore();
        this.defaultProvider = options.defaultProvider || null;
        this.onProgress = options.onProgress || (() => {});
    }
    
    /**
     * Get available providers (have keys configured)
     */
    getAvailableProviders() {
        return this.keyStore.getConfiguredProviders();
    }
    
    /**
     * Get the best available provider
     */
    getBestProvider() {
        if (this.defaultProvider && this.keyStore.getKey(this.defaultProvider)) {
            return this.defaultProvider;
        }
        const available = this.getAvailableProviders();
        // Preference order
        const preference = ['google', 'openai', 'stability', 'replicate'];
        for (const p of preference) {
            if (available.includes(p)) return p;
        }
        return null;
    }
    
    /**
     * Generate an image
     * @param {string} prompt - The image description
     * @param {object} options - Generation options
     * @returns {Promise<{url: string, base64?: string, provider: string}>}
     */
    async generate(prompt, options = {}) {
        const provider = options.provider || this.getBestProvider();
        
        if (!provider) {
            throw new Error('No image generation provider configured. Add an API key.');
        }
        
        const key = options.apiKey || this.keyStore.getKey(provider);
        if (!key) {
            throw new Error(`No API key for provider: ${provider}`);
        }
        
        this.onProgress({ stage: 'starting', provider, prompt });
        
        switch (provider) {
            case 'openai':
                return this._generateOpenAI(prompt, key, options);
            case 'google':
                return this._generateGoogle(prompt, key, options);
            case 'stability':
                return this._generateStability(prompt, key, options);
            case 'replicate':
                return this._generateReplicate(prompt, key, options);
            default:
                throw new Error(`Unknown provider: ${provider}`);
        }
    }
    
    /**
     * OpenAI DALL-E
     */
    async _generateOpenAI(prompt, key, options) {
        const config = IMAGE_PROVIDERS.openai;
        const model = options.model || config.defaultModel;
        const size = options.size || config.defaultSize;
        
        this.onProgress({ stage: 'generating', provider: 'openai', model });
        
        const response = await fetch(config.endpoint, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${key}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model,
                prompt,
                n: 1,
                size,
                response_format: 'b64_json'
            })
        });
        
        if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(`OpenAI error: ${error.error?.message || response.statusText}`);
        }
        
        const data = await response.json();
        const base64 = data.data[0].b64_json;
        
        this.onProgress({ stage: 'complete', provider: 'openai' });
        
        return {
            provider: 'openai',
            model,
            base64,
            url: `data:image/png;base64,${base64}`,
            revised_prompt: data.data[0].revised_prompt
        };
    }
    
    /**
     * Google Imagen via Gemini API
     */
    async _generateGoogle(prompt, key, options) {
        const config = IMAGE_PROVIDERS.google;
        const model = options.model || config.defaultModel;
        
        this.onProgress({ stage: 'generating', provider: 'google', model });
        
        // Gemini image generation endpoint
        const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateImages?key=${key}`;
        
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                prompt: prompt,
                number_of_images: 1,
                aspect_ratio: '1:1',
                safety_filter_level: 'BLOCK_MEDIUM_AND_ABOVE',
                person_generation: 'ALLOW_ADULT'
            })
        });
        
        if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(`Google error: ${error.error?.message || response.statusText}`);
        }
        
        const data = await response.json();
        const base64 = data.generated_images?.[0]?.image?.image_bytes;
        
        if (!base64) {
            throw new Error('Google returned no image');
        }
        
        this.onProgress({ stage: 'complete', provider: 'google' });
        
        return {
            provider: 'google',
            model,
            base64,
            url: `data:image/png;base64,${base64}`
        };
    }
    
    /**
     * Stability AI
     */
    async _generateStability(prompt, key, options) {
        const config = IMAGE_PROVIDERS.stability;
        const model = options.model || config.defaultModel;
        
        this.onProgress({ stage: 'generating', provider: 'stability', model });
        
        const formData = new FormData();
        formData.append('prompt', prompt);
        formData.append('output_format', 'png');
        if (options.negativePrompt) {
            formData.append('negative_prompt', options.negativePrompt);
        }
        
        const response = await fetch(config.endpoint, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${key}`,
                'Accept': 'application/json'
            },
            body: formData
        });
        
        if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(`Stability error: ${error.message || response.statusText}`);
        }
        
        const data = await response.json();
        const base64 = data.image;
        
        this.onProgress({ stage: 'complete', provider: 'stability' });
        
        return {
            provider: 'stability',
            model,
            base64,
            url: `data:image/png;base64,${base64}`,
            seed: data.seed
        };
    }
    
    /**
     * Replicate (async polling)
     */
    async _generateReplicate(prompt, key, options) {
        const config = IMAGE_PROVIDERS.replicate;
        const model = options.model || config.defaultModel;
        
        this.onProgress({ stage: 'starting', provider: 'replicate', model });
        
        // Start prediction
        const startResponse = await fetch(config.endpoint, {
            method: 'POST',
            headers: {
                'Authorization': `Token ${key}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                version: model,
                input: { prompt }
            })
        });
        
        if (!startResponse.ok) {
            const error = await startResponse.json().catch(() => ({}));
            throw new Error(`Replicate error: ${error.detail || startResponse.statusText}`);
        }
        
        const prediction = await startResponse.json();
        
        // Poll for completion
        let result = prediction;
        while (result.status !== 'succeeded' && result.status !== 'failed') {
            this.onProgress({ stage: 'polling', provider: 'replicate', status: result.status });
            await new Promise(resolve => setTimeout(resolve, 1000));
            
            const pollResponse = await fetch(result.urls.get, {
                headers: { 'Authorization': `Token ${key}` }
            });
            result = await pollResponse.json();
        }
        
        if (result.status === 'failed') {
            throw new Error(`Replicate failed: ${result.error}`);
        }
        
        this.onProgress({ stage: 'complete', provider: 'replicate' });
        
        // Replicate returns URL, need to fetch for base64
        const imageUrl = Array.isArray(result.output) ? result.output[0] : result.output;
        
        return {
            provider: 'replicate',
            model,
            url: imageUrl
            // Note: URL is temporary, should download if needed
        };
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// KEY SETUP UI
// ═══════════════════════════════════════════════════════════════════════════════

class ImageGenerateKeyUI {
    constructor(generator) {
        this.generator = generator;
        this.keyStore = generator.keyStore;
    }
    
    /**
     * Show key configuration modal
     */
    show() {
        // Remove existing
        const existing = document.getElementById('imagegen-key-modal');
        if (existing) existing.remove();
        
        const modal = document.createElement('div');
        modal.id = 'imagegen-key-modal';
        modal.innerHTML = `
            <div style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.8);z-index:10000;display:flex;align-items:center;justify-content:center;">
                <div style="background:#1a1a2e;border-radius:8px;padding:24px;max-width:500px;width:90%;color:#eee;font-family:monospace;">
                    <h2 style="margin:0 0 16px;color:#e94560;">🎨 Image Generation Keys</h2>
                    <p style="color:#888;margin-bottom:20px;">
                        Your keys are stored locally in your browser. Never sent to our servers.
                    </p>
                    
                    ${Object.entries(IMAGE_PROVIDERS).map(([id, p]) => `
                        <div style="margin-bottom:16px;">
                            <label style="display:block;margin-bottom:4px;color:#4ecca3;">${p.name}</label>
                            <input type="password" 
                                   id="imagegen-key-${id}"
                                   value="${this.keyStore.getKey(id) || ''}"
                                   placeholder="${p.keyName}"
                                   style="width:100%;padding:8px;background:#16213e;border:1px solid #0f3460;border-radius:4px;color:#eee;font-family:monospace;">
                            <small style="color:#666;">${p.note || `Models: ${p.models.join(', ')}`}</small>
                        </div>
                    `).join('')}
                    
                    <div style="display:flex;gap:10px;margin-top:20px;">
                        <button id="imagegen-key-save" style="flex:1;padding:10px;background:#4ecca3;border:none;border-radius:4px;color:#1a1a2e;cursor:pointer;font-weight:bold;">
                            Save Keys
                        </button>
                        <button id="imagegen-key-cancel" style="flex:1;padding:10px;background:#0f3460;border:none;border-radius:4px;color:#eee;cursor:pointer;">
                            Cancel
                        </button>
                    </div>
                    
                    <p style="color:#666;font-size:12px;margin-top:16px;">
                        Get keys from: 
                        <a href="https://platform.openai.com/api-keys" target="_blank" style="color:#e94560;">OpenAI</a> |
                        <a href="https://aistudio.google.com/apikey" target="_blank" style="color:#e94560;">Google</a> |
                        <a href="https://platform.stability.ai/account/keys" target="_blank" style="color:#e94560;">Stability</a> |
                        <a href="https://replicate.com/account/api-tokens" target="_blank" style="color:#e94560;">Replicate</a>
                    </p>
                </div>
            </div>
        `;
        
        document.body.appendChild(modal);
        
        // Event handlers
        document.getElementById('imagegen-key-save').onclick = () => {
            Object.keys(IMAGE_PROVIDERS).forEach(id => {
                const input = document.getElementById(`imagegen-key-${id}`);
                const value = input.value.trim();
                if (value) {
                    this.keyStore.setKey(id, value);
                } else {
                    this.keyStore.removeKey(id);
                }
            });
            modal.remove();
            console.log('🔑 Keys saved:', this.keyStore.getConfiguredProviders());
        };
        
        document.getElementById('imagegen-key-cancel').onclick = () => {
            modal.remove();
        };
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// INTEGRATION WITH ADVENTURE ENGINE
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Add image generation to an adventure engine
 */
function addImageGenerateToEngine(engine, options = {}) {
    const generator = new ImageGenerator({
        onProgress: (progress) => {
            console.log('🎨 Image gen:', progress);
            engine.ui?.print(`[Image: ${progress.stage}${progress.provider ? ' via ' + progress.provider : ''}]`, 'system');
        },
        ...options
    });
    
    const keyUI = new ImageGenerateKeyUI(generator);
    
    // Add to engine
    engine.imageGenerate = generator;
    engine.imageGenerateUI = keyUI;
    
    // Add commands
    const origCommand = engine.command.bind(engine);
    engine.command = function(input) {
        const lower = input.toLowerCase().trim();
        
        if (lower === 'imagegen keys' || lower === 'image keys') {
            keyUI.show();
            return { handled: true };
        }
        
        if (lower.startsWith('generate image ') || lower.startsWith('visualize ')) {
            const prompt = input.replace(/^(generate image|visualize)\s+/i, '');
            engine.ui?.print(`Generating: "${prompt}"...`, 'system');
            
            generator.generate(prompt)
                .then(result => {
                    engine.ui?.print(`✅ Generated via ${result.provider}`, 'response');
                    // Could display image in UI here
                    if (result.url) {
                        console.log('🖼️ Image URL:', result.url);
                    }
                })
                .catch(err => {
                    engine.ui?.print(`❌ Generation failed: ${err.message}`, 'error');
                });
            
            return { handled: true, async: true };
        }
        
        return origCommand(input);
    };
    
    console.log('🎨 Image generation added to engine');
    console.log('   Commands: "imagegen keys", "generate image <prompt>"');
    console.log('   Configured providers:', generator.getAvailableProviders().join(', ') || 'none');
    
    return generator;
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const IMAGE_GENERATE_EXPORTS = {
    IMAGE_PROVIDERS,
    ImageGenerateKeyStore,
    ImageGenerator,
    ImageGenerateKeyUI,
    addImageGenerateToEngine
};

if (typeof window !== 'undefined') {
    Object.assign(window, IMAGE_GENERATE_EXPORTS);
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = IMAGE_GENERATE_EXPORTS;
}
