/**
 * api-keys.js — Matrix-style API key management
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Spreadsheet UI: Providers (rows) × Services (columns)
 * Each cell can have its own key, or share keys across services.
 * 
 * FEATURES:
 *   Matrix storage    provider:service → key
 *   Spreadsheet UI    Click cells to edit, masked until revealed
 *   Copy/paste        Fill multiple cells with same key
 *   OAuth             GitHub login button, Google TODO
 *   Instructions      How to get keys for each provider
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// PROVIDERS & SERVICES
// ═══════════════════════════════════════════════════════════════════════════════

const PROVIDERS = {
    openai: {
        name: 'OpenAI',
        keyPattern: /^sk-[a-zA-Z0-9-_]{20,}$/,
        keyHint: 'sk-...',
        getKeyUrl: 'https://platform.openai.com/api-keys',
        testEndpoint: 'https://api.openai.com/v1/models',
        authHeader: (key) => ({ 'Authorization': `Bearer ${key}` }),
        instructions: `1. Go to platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with sk-)`
    },
    google: {
        name: 'Google AI',
        keyPattern: /^AIza[a-zA-Z0-9-_]{35}$/,
        keyHint: 'AIza...',
        getKeyUrl: 'https://aistudio.google.com/apikey',
        testEndpoint: 'https://generativelanguage.googleapis.com/v1beta/models?key={key}',
        authHeader: null,  // Uses query param
        instructions: `1. Go to aistudio.google.com/apikey
2. Click "Create API key"
3. Copy the key (starts with AIza)`,
        oauth: {
            supported: true,
            clientId: null,  // Set by app
            scopes: ['https://www.googleapis.com/auth/generative-language']
        }
    },
    anthropic: {
        name: 'Anthropic',
        keyPattern: /^sk-ant-[a-zA-Z0-9-_]{20,}$/,
        keyHint: 'sk-ant-...',
        getKeyUrl: 'https://console.anthropic.com/settings/keys',
        testEndpoint: null,  // CORS issues
        authHeader: (key) => ({ 'x-api-key': key, 'anthropic-version': '2023-06-01' }),
        instructions: `1. Go to console.anthropic.com/settings/keys
2. Click "Create Key"
3. Copy the key (starts with sk-ant-)
Note: Browser calls may need CORS proxy`
    },
    stability: {
        name: 'Stability AI',
        keyPattern: /^sk-[a-zA-Z0-9]{20,}$/,
        keyHint: 'sk-...',
        getKeyUrl: 'https://platform.stability.ai/account/keys',
        testEndpoint: 'https://api.stability.ai/v1/user/account',
        authHeader: (key) => ({ 'Authorization': `Bearer ${key}` }),
        instructions: `1. Go to platform.stability.ai/account/keys
2. Click "Create API Key"
3. Copy the key`
    },
    replicate: {
        name: 'Replicate',
        keyPattern: /^r8_[a-zA-Z0-9]{20,}$/,
        keyHint: 'r8_...',
        getKeyUrl: 'https://replicate.com/account/api-tokens',
        testEndpoint: 'https://api.replicate.com/v1/account',
        authHeader: (key) => ({ 'Authorization': `Token ${key}` }),
        instructions: `1. Go to replicate.com/account/api-tokens
2. Click "Create token"
3. Copy the token (starts with r8_)`
    },
    github: {
        name: 'GitHub',
        keyPattern: /^(gh[ps]_[a-zA-Z0-9]{36,}|github_pat_[a-zA-Z0-9_]{20,})$/,
        keyHint: 'ghp_... or github_pat_...',
        getKeyUrl: 'https://github.com/settings/tokens',
        testEndpoint: 'https://api.github.com/user',
        authHeader: (key) => ({ 'Authorization': `Bearer ${key}` }),
        instructions: `1. Go to github.com/settings/tokens
2. Generate new token (classic)
3. Select scopes: repo, read:user
4. Copy the token`,
        oauth: {
            supported: true,
            // GitHub Device Flow - works without client secret in browser
            deviceAuthUrl: 'https://github.com/login/device/code',
            tokenUrl: 'https://github.com/login/oauth/access_token',
            clientId: null,  // Set by app config
            scopes: ['repo', 'read:user']
        }
    },
    elevenlabs: {
        name: 'ElevenLabs',
        keyPattern: /^[a-f0-9]{32}$/,
        keyHint: '32 hex chars',
        getKeyUrl: 'https://elevenlabs.io/app/settings/api-keys',
        testEndpoint: 'https://api.elevenlabs.io/v1/user',
        authHeader: (key) => ({ 'xi-api-key': key }),
        instructions: `1. Go to elevenlabs.io/app/settings/api-keys
2. Click "Create API Key"
3. Copy the key`
    }
};

const SERVICES = {
    'image-generate': { name: 'Image Generate', icon: '🎨' },
    'image-analyze': { name: 'Image Analyze', icon: '🔬' },
    'llm-chat': { name: 'LLM Chat', icon: '💬' },
    'speech-synth': { name: 'Speech Synth', icon: '🔊' },
    'speech-recog': { name: 'Speech Recog', icon: '🎤' },
    'source-control': { name: 'Source Control', icon: '📂' }
};

// Which providers support which services
const PROVIDER_SERVICES = {
    openai: ['image-generate', 'image-analyze', 'llm-chat', 'speech-synth', 'speech-recog'],
    google: ['image-generate', 'image-analyze', 'llm-chat', 'speech-synth', 'speech-recog'],
    anthropic: ['image-analyze', 'llm-chat'],
    stability: ['image-generate'],
    replicate: ['image-generate'],
    github: ['source-control'],
    elevenlabs: ['speech-synth']
};

// ═══════════════════════════════════════════════════════════════════════════════
// MATRIX KEY STORE
// ═══════════════════════════════════════════════════════════════════════════════

class APIKeyMatrix {
    constructor(options = {}) {
        this.storageKey = options.storageKey || 'moollm_api_keys';
        this._cache = null;
    }
    
    /**
     * Get all keys as matrix object
     * Format: { "provider:service": { key, valid } }
     */
    getAll() {
        if (this._cache) return this._cache;
        try {
            const data = localStorage.getItem(this.storageKey);
            const parsed = data ? JSON.parse(data) : {};
            // Migrate old format (string values) to new format (objects)
            for (const [k, v] of Object.entries(parsed)) {
                if (typeof v === 'string') {
                    const [provider] = k.split(':');
                    parsed[k] = { key: v, valid: this._checkFormat(provider, v) };
                }
            }
            this._cache = parsed;
            return this._cache;
        } catch {
            return {};
        }
    }
    
    /**
     * Save matrix to storage
     */
    _save(matrix) {
        this._cache = matrix;
        localStorage.setItem(this.storageKey, JSON.stringify(matrix));
    }
    
    /**
     * Check if key matches provider's format
     */
    _checkFormat(provider, key) {
        const config = PROVIDERS[provider];
        if (!config?.keyPattern) return true;  // No pattern = assume valid
        return config.keyPattern.test(key);
    }
    
    /**
     * Get key for provider:service
     * @param {boolean} includeInvalid - If true, returns key even if invalid
     */
    get(provider, service, includeInvalid = false) {
        const matrix = this.getAll();
        const entry = matrix[`${provider}:${service}`];
        if (!entry) return null;
        if (!includeInvalid && !entry.valid) return null;
        return entry.key;
    }
    
    /**
     * Get key entry with validity info
     */
    getEntry(provider, service) {
        const matrix = this.getAll();
        return matrix[`${provider}:${service}`] || null;
    }
    
    /**
     * Set key for provider:service (validates format but saves anyway)
     */
    set(provider, service, key) {
        const matrix = this.getAll();
        if (key) {
            const valid = this._checkFormat(provider, key);
            matrix[`${provider}:${service}`] = { key, valid };
        } else {
            delete matrix[`${provider}:${service}`];
        }
        this._save(matrix);
    }
    
    /**
     * Update validity status after testing
     */
    setValid(provider, service, valid) {
        const matrix = this.getAll();
        const entry = matrix[`${provider}:${service}`];
        if (entry) {
            entry.valid = valid;
            this._save(matrix);
        }
    }
    
    /**
     * Set same key for all services a provider supports
     */
    setAllServices(provider, key) {
        const services = PROVIDER_SERVICES[provider] || [];
        for (const service of services) {
            this.set(provider, service, key);
        }
    }
    
    /**
     * Get first available VALID key for a service (any provider)
     */
    getForService(service) {
        const matrix = this.getAll();
        for (const provider of Object.keys(PROVIDERS)) {
            const entry = matrix[`${provider}:${service}`];
            if (entry?.key && entry.valid) {
                return { provider, key: entry.key };
            }
        }
        return null;
    }
    
    /**
     * Get all keys for a provider (valid only by default)
     */
    getForProvider(provider, includeInvalid = false) {
        const matrix = this.getAll();
        const result = {};
        for (const service of Object.keys(SERVICES)) {
            const entry = matrix[`${provider}:${service}`];
            if (entry?.key && (includeInvalid || entry.valid)) {
                result[service] = entry.key;
            }
        }
        return result;
    }
    
    /**
     * Get all entries for a provider with validity info
     */
    getEntriesForProvider(provider) {
        const matrix = this.getAll();
        const result = {};
        for (const service of Object.keys(SERVICES)) {
            const entry = matrix[`${provider}:${service}`];
            if (entry) {
                result[service] = entry;
            }
        }
        return result;
    }
    
    /**
     * Clear all keys
     */
    clearAll() {
        this._cache = {};
        localStorage.removeItem(this.storageKey);
    }
    
    /**
     * Export for backup
     */
    export() {
        return this.getAll();
    }
    
    /**
     * Import from backup
     */
    import(data) {
        this._save({ ...this.getAll(), ...data });
    }
    
    /**
     * Count filled cells (valid and total)
     */
    countKeys() {
        const matrix = this.getAll();
        let total = 0;
        let valid = 0;
        for (const entry of Object.values(matrix)) {
            if (entry?.key) {
                total++;
                if (entry.valid) valid++;
            }
        }
        return { total, valid, invalid: total - valid };
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// KEY TESTER
// ═══════════════════════════════════════════════════════════════════════════════

class APIKeyTester {
    async test(provider, key) {
        const config = PROVIDERS[provider];
        if (!config) return { success: false, error: 'Unknown provider' };
        
        // Format check
        if (config.keyPattern && !config.keyPattern.test(key)) {
            return { success: false, error: 'Invalid format' };
        }
        
        // No test endpoint
        if (!config.testEndpoint) {
            return { success: true, warning: 'Cannot verify' };
        }
        
        try {
            const url = config.testEndpoint.replace('{key}', key);
            const headers = config.authHeader ? config.authHeader(key) : {};
            
            const response = await fetch(url, { method: 'GET', headers });
            
            if (response.ok) {
                return { success: true };
            } else {
                const err = await response.json().catch(() => ({}));
                return { success: false, error: err.error?.message || `HTTP ${response.status}` };
            }
        } catch (e) {
            return { success: false, error: e.message };
        }
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// GITHUB OAUTH
// ═══════════════════════════════════════════════════════════════════════════════

class GitHubOAuth {
    constructor(options = {}) {
        this.clientId = options.clientId || PROVIDERS.github.oauth?.clientId;
        this.scopes = options.scopes || PROVIDERS.github.oauth?.scopes || ['repo', 'read:user'];
    }
    
    /**
     * Check if OAuth is configured
     */
    isAvailable() {
        return !!this.clientId;
    }
    
    /**
     * Start Device Flow (works in browser without client secret)
     */
    async startDeviceFlow() {
        if (!this.clientId) {
            throw new Error('GitHub OAuth client ID not configured');
        }
        
        const response = await fetch('https://github.com/login/device/code', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                client_id: this.clientId,
                scope: this.scopes.join(' ')
            })
        });
        
        if (!response.ok) {
            throw new Error('Failed to start device flow');
        }
        
        return response.json();
        // Returns: { device_code, user_code, verification_uri, expires_in, interval }
    }
    
    /**
     * Poll for token after user authorizes
     */
    async pollForToken(deviceCode, interval = 5) {
        const response = await fetch('https://github.com/login/oauth/access_token', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                client_id: this.clientId,
                device_code: deviceCode,
                grant_type: 'urn:ietf:params:oauth:grant-type:device_code'
            })
        });
        
        const data = await response.json();
        
        if (data.error === 'authorization_pending') {
            return { pending: true };
        } else if (data.error) {
            return { error: data.error_description || data.error };
        } else if (data.access_token) {
            return { token: data.access_token };
        }
        
        return { error: 'Unknown response' };
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// MATRIX UI — Spreadsheet-style key management
// ═══════════════════════════════════════════════════════════════════════════════

class APIKeyMatrixUI {
    constructor(options = {}) {
        this.matrix = options.matrix || new APIKeyMatrix();
        this.tester = new APIKeyTester();
        this.githubOAuth = new GitHubOAuth(options.github || {});
        this.onUpdate = options.onUpdate || (() => {});
        this._clipboard = null;
    }
    
    show() {
        this._remove();
        
        const modal = document.createElement('div');
        modal.id = 'api-key-matrix-modal';
        modal.innerHTML = this._render();
        document.body.appendChild(modal);
        
        this._injectStyles();
        this._bindEvents();
    }
    
    _remove() {
        document.getElementById('api-key-matrix-modal')?.remove();
    }
    
    _render() {
        const providers = Object.keys(PROVIDERS);
        const services = Object.keys(SERVICES);
        
        return `
            <div class="akm-backdrop"></div>
            <div class="akm-container">
                <div class="akm-header">
                    <h2>🔑 API Keys</h2>
                    <div class="akm-header-actions">
                        <button data-action="export" title="Export">📤</button>
                        <button data-action="import" title="Import">📥</button>
                        <button data-action="clear" title="Clear All">🗑️</button>
                        <button class="akm-close" data-action="close">×</button>
                    </div>
                </div>
                
                <div class="akm-instructions">
                    Click cell to edit • Right-click to copy/paste • Keys masked until clicked
                </div>
                
                <div class="akm-matrix-scroll">
                    <table class="akm-matrix">
                        <thead>
                            <tr>
                                <th class="akm-corner"></th>
                                ${services.map(s => `
                                    <th class="akm-service-header" title="${SERVICES[s].name}">
                                        <span class="akm-icon">${SERVICES[s].icon}</span>
                                        <span class="akm-label">${SERVICES[s].name}</span>
                                    </th>
                                `).join('')}
                            </tr>
                        </thead>
                        <tbody>
                            ${providers.map(p => this._renderProviderRow(p, services)).join('')}
                        </tbody>
                    </table>
                </div>
                
                <div class="akm-footer">
                    <span class="akm-count">${this._renderKeyCount()}</span>
                    <input type="file" id="akm-import-file" accept=".json" style="display:none;">
                </div>
                
                <div id="akm-edit-panel" class="akm-edit-panel" style="display:none;">
                    <!-- Populated when cell clicked -->
                </div>
            </div>
        `;
    }
    
    _renderKeyCount() {
        const { total, valid, invalid } = this.matrix.countKeys();
        if (total === 0) return 'No keys configured';
        if (invalid === 0) return `${valid} keys configured`;
        return `${valid} valid, <span style="color:#e94560">${invalid} invalid</span> (${total} total)`;
    }
    
    _renderProviderRow(provider, services) {
        const config = PROVIDERS[provider];
        const supported = PROVIDER_SERVICES[provider] || [];
        const hasOAuth = provider === 'github' && this.githubOAuth.isAvailable();
        
        return `
            <tr data-provider="${provider}">
                <td class="akm-provider-cell">
                    <div class="akm-provider-name">${config.name}</div>
                    <div class="akm-provider-actions">
                        <a href="${config.getKeyUrl}" target="_blank" title="Get key">🔗</a>
                        ${hasOAuth ? `<button data-action="oauth" data-provider="${provider}" title="Sign in">🔐</button>` : ''}
                        <button data-action="fill-row" data-provider="${provider}" title="Fill all">📋</button>
                    </div>
                </td>
                ${services.map(service => {
                    const isSupported = supported.includes(service);
                    const entry = this.matrix.getEntry(provider, service);
                    
                    if (!isSupported) {
                        return `<td class="akm-cell akm-cell-na" data-provider="${provider}" data-service="${service}">—</td>`;
                    }
                    
                    let cellClass = 'akm-cell-empty';
                    let status = '○';
                    let title = 'Click to add key';
                    
                    if (entry?.key) {
                        if (entry.valid) {
                            cellClass = 'akm-cell-valid';
                            status = '✓';
                            title = 'Valid key — click to edit';
                        } else {
                            cellClass = 'akm-cell-invalid';
                            status = '✗';
                            title = 'Invalid format — click to fix';
                        }
                    }
                    
                    return `
                        <td class="akm-cell ${cellClass}" 
                            data-provider="${provider}" 
                            data-service="${service}"
                            title="${title}">
                            <span class="akm-cell-status">${status}</span>
                        </td>
                    `;
                }).join('')}
            </tr>
        `;
    }
    
    _renderEditPanel(provider, service) {
        const config = PROVIDERS[provider];
        const entry = this.matrix.getEntry(provider, service);
        const key = entry?.key || '';
        const isValid = entry?.valid ?? true;
        
        return `
            <div class="akm-edit-header">
                <strong>${config.name}</strong> → <strong>${SERVICES[service].name}</strong>
                <button data-action="close-edit">×</button>
            </div>
            
            <div class="akm-edit-instructions">
                <pre>${config.instructions}</pre>
                <a href="${config.getKeyUrl}" target="_blank">🔗 Open ${config.name}</a>
            </div>
            
            <div class="akm-edit-input">
                <input type="password" 
                       id="akm-key-input" 
                       value="${key}" 
                       placeholder="${config.keyHint}"
                       class="${key && !isValid ? 'akm-input-invalid' : ''}">
                <button data-action="toggle-show" title="Show/hide">👁️</button>
            </div>
            
            ${key && !isValid ? `
                <div class="akm-validation-error">
                    ⚠️ Invalid format — key saved but disabled. Expected: ${config.keyHint}
                </div>
            ` : ''}
            
            <div class="akm-edit-actions">
                <button data-action="test-key" data-provider="${provider}" data-service="${service}">🧪 Test</button>
                <button data-action="save-key" data-provider="${provider}" data-service="${service}">💾 Save</button>
                <button data-action="delete-key" data-provider="${provider}" data-service="${service}">🗑️</button>
                <button data-action="copy-key">📋 Copy</button>
                <button data-action="paste-key">📥 Paste</button>
            </div>
            
            <div id="akm-test-result" class="akm-test-result"></div>
        `;
    }
    
    _bindEvents() {
        const modal = document.getElementById('api-key-matrix-modal');
        if (!modal) return;
        
        // Backdrop close
        modal.querySelector('.akm-backdrop').onclick = () => this._remove();
        
        // Delegated click handling
        modal.onclick = async (e) => {
            const action = e.target.closest('[data-action]')?.dataset.action;
            const provider = e.target.closest('[data-provider]')?.dataset.provider;
            const service = e.target.closest('[data-service]')?.dataset.service;
            
            switch (action) {
                case 'close':
                    this._remove();
                    break;
                    
                case 'close-edit':
                    modal.querySelector('#akm-edit-panel').style.display = 'none';
                    break;
                    
                case 'export':
                    this._export();
                    break;
                    
                case 'import':
                    modal.querySelector('#akm-import-file').click();
                    break;
                    
                case 'clear':
                    if (confirm('Delete ALL API keys?')) {
                        this.matrix.clearAll();
                        this.show();
                        this.onUpdate();
                    }
                    break;
                    
                case 'oauth':
                    await this._startOAuth(provider);
                    break;
                    
                case 'fill-row':
                    this._fillRow(provider);
                    break;
                    
                case 'toggle-show':
                    const input = modal.querySelector('#akm-key-input');
                    input.type = input.type === 'password' ? 'text' : 'password';
                    break;
                    
                case 'test-key':
                    await this._testKey(provider, service);
                    break;
                    
                case 'save-key':
                    this._saveKey(provider, service);
                    break;
                    
                case 'delete-key':
                    this.matrix.set(provider, service, null);
                    this.show();
                    this.onUpdate();
                    break;
                    
                case 'copy-key':
                    this._clipboard = modal.querySelector('#akm-key-input').value;
                    modal.querySelector('#akm-test-result').textContent = 'Copied to clipboard';
                    break;
                    
                case 'paste-key':
                    if (this._clipboard) {
                        modal.querySelector('#akm-key-input').value = this._clipboard;
                    }
                    break;
            }
            
            // Cell click (not action button)
            const cell = e.target.closest('.akm-cell:not(.akm-cell-disabled)');
            if (cell && !action) {
                this._openEditPanel(cell.dataset.provider, cell.dataset.service);
            }
        };
        
        // Import file
        modal.querySelector('#akm-import-file').onchange = (e) => {
            const file = e.target.files[0];
            if (file) this._import(file);
        };
        
        // Right-click context menu
        modal.oncontextmenu = (e) => {
            const cell = e.target.closest('.akm-cell:not(.akm-cell-disabled)');
            if (cell) {
                e.preventDefault();
                this._showContextMenu(e.clientX, e.clientY, cell.dataset.provider, cell.dataset.service);
            }
        };
    }
    
    _openEditPanel(provider, service) {
        const panel = document.querySelector('#akm-edit-panel');
        panel.innerHTML = this._renderEditPanel(provider, service);
        panel.style.display = 'block';
    }
    
    async _testKey(provider, service) {
        const input = document.querySelector('#akm-key-input');
        const result = document.querySelector('#akm-test-result');
        const key = input.value.trim();
        
        if (!key) {
            result.innerHTML = '<span class="akm-error">Enter a key first</span>';
            return;
        }
        
        result.innerHTML = '<span class="akm-testing">Testing...</span>';
        const testResult = await this.tester.test(provider, key);
        
        if (testResult.success) {
            result.innerHTML = `<span class="akm-success">✅ Key works!${testResult.warning ? ' (' + testResult.warning + ')' : ''}</span>`;
            // Mark as valid if test passes (even if format check failed)
            if (service) {
                this.matrix.setValid(provider, service, true);
            }
        } else {
            result.innerHTML = `<span class="akm-error">❌ ${testResult.error}</span>`;
        }
    }
    
    _saveKey(provider, service) {
        const key = document.querySelector('#akm-key-input').value.trim();
        this.matrix.set(provider, service, key || null);
        this.show();
        this.onUpdate();
    }
    
    _fillRow(provider) {
        const key = prompt(`Enter ${PROVIDERS[provider].name} API key to fill all services:`);
        if (key) {
            this.matrix.setAllServices(provider, key.trim());
            this.show();
            this.onUpdate();
        }
    }
    
    async _startOAuth(provider) {
        if (provider === 'github') {
            await this._githubOAuth();
        }
    }
    
    async _githubOAuth() {
        if (!this.githubOAuth.isAvailable()) {
            alert('GitHub OAuth not configured. Please enter a personal access token manually.');
            return;
        }
        
        try {
            const flow = await this.githubOAuth.startDeviceFlow();
            
            // Show user code
            const userCode = flow.user_code;
            const verifyUrl = flow.verification_uri;
            
            // Open verification URL
            window.open(verifyUrl, '_blank');
            
            alert(`Enter this code on GitHub:\n\n${userCode}\n\nClick OK after authorizing.`);
            
            // Poll for token
            let attempts = 0;
            const maxAttempts = 60;
            
            while (attempts < maxAttempts) {
                const result = await this.githubOAuth.pollForToken(flow.device_code);
                
                if (result.token) {
                    this.matrix.setAllServices('github', result.token);
                    this.show();
                    this.onUpdate();
                    alert('GitHub connected successfully!');
                    return;
                } else if (result.error && !result.pending) {
                    throw new Error(result.error);
                }
                
                await new Promise(r => setTimeout(r, (flow.interval || 5) * 1000));
                attempts++;
            }
            
            throw new Error('Authorization timed out');
        } catch (e) {
            alert(`GitHub OAuth failed: ${e.message}`);
        }
    }
    
    _showContextMenu(x, y, provider, service) {
        // Remove existing
        document.querySelector('.akm-context-menu')?.remove();
        
        const menu = document.createElement('div');
        menu.className = 'akm-context-menu';
        menu.style.left = `${x}px`;
        menu.style.top = `${y}px`;
        menu.innerHTML = `
            <button data-ctx="copy">📋 Copy</button>
            <button data-ctx="paste">📥 Paste</button>
            <button data-ctx="clear">🗑️ Clear</button>
        `;
        
        document.body.appendChild(menu);
        
        menu.onclick = (e) => {
            const ctx = e.target.dataset.ctx;
            if (ctx === 'copy') {
                this._clipboard = this.matrix.get(provider, service);
            } else if (ctx === 'paste' && this._clipboard) {
                this.matrix.set(provider, service, this._clipboard);
                this.show();
                this.onUpdate();
            } else if (ctx === 'clear') {
                this.matrix.set(provider, service, null);
                this.show();
                this.onUpdate();
            }
            menu.remove();
        };
        
        // Close on click outside
        setTimeout(() => {
            document.addEventListener('click', () => menu.remove(), { once: true });
        }, 10);
    }
    
    _export() {
        const data = this.matrix.export();
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = `moollm-api-keys-${new Date().toISOString().slice(0, 10)}.json`;
        a.click();
        
        URL.revokeObjectURL(url);
    }
    
    _import(file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            try {
                const data = JSON.parse(e.target.result);
                this.matrix.import(data);
                this.show();
                this.onUpdate();
            } catch (err) {
                alert('Import failed: ' + err.message);
            }
        };
        reader.readAsText(file);
    }
    
    _injectStyles() {
        if (document.getElementById('api-key-matrix-styles')) return;
        
        const style = document.createElement('style');
        style.id = 'api-key-matrix-styles';
        style.textContent = `
            #api-key-matrix-modal {
                position: fixed;
                inset: 0;
                z-index: 10001;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            }
            .akm-backdrop {
                position: absolute;
                inset: 0;
                background: rgba(0, 0, 0, 0.85);
            }
            .akm-container {
                position: relative;
                max-width: 900px;
                max-height: 90vh;
                margin: 5vh auto;
                background: #1a1a2e;
                border-radius: 12px;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                color: #eee;
            }
            .akm-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 12px 16px;
                background: #16213e;
                border-bottom: 1px solid #0f3460;
            }
            .akm-header h2 { margin: 0; font-size: 18px; }
            .akm-header-actions { display: flex; gap: 8px; }
            .akm-header-actions button {
                background: none;
                border: none;
                font-size: 16px;
                cursor: pointer;
                padding: 4px 8px;
                border-radius: 4px;
            }
            .akm-header-actions button:hover { background: rgba(255,255,255,0.1); }
            .akm-close { font-size: 24px !important; color: #888; }
            .akm-close:hover { color: #fff; }
            
            .akm-instructions {
                padding: 8px 16px;
                font-size: 12px;
                color: #666;
                background: #16213e;
            }
            
            .akm-matrix-scroll {
                overflow: auto;
                flex: 1;
                padding: 16px;
            }
            .akm-matrix {
                border-collapse: collapse;
                width: 100%;
                font-size: 13px;
            }
            .akm-matrix th, .akm-matrix td {
                border: 1px solid #0f3460;
                padding: 8px;
                text-align: center;
            }
            .akm-corner {
                background: #16213e;
                min-width: 120px;
            }
            .akm-service-header {
                background: #16213e;
                min-width: 80px;
                white-space: nowrap;
            }
            .akm-icon { display: block; font-size: 18px; }
            .akm-label { display: block; font-size: 10px; color: #888; margin-top: 2px; }
            
            .akm-provider-cell {
                background: #16213e;
                text-align: left !important;
            }
            .akm-provider-name { font-weight: 600; color: #4ecca3; }
            .akm-provider-actions {
                margin-top: 4px;
                display: flex;
                gap: 4px;
            }
            .akm-provider-actions a, .akm-provider-actions button {
                font-size: 12px;
                text-decoration: none;
                padding: 2px 4px;
                background: none;
                border: none;
                cursor: pointer;
            }
            
            .akm-cell {
                cursor: pointer;
                transition: background 0.1s;
            }
            .akm-cell:hover { background: #1a365d; }
            .akm-cell-valid { background: rgba(78, 204, 163, 0.15); }
            .akm-cell-valid .akm-cell-status { color: #4ecca3; }
            .akm-cell-invalid { background: rgba(233, 69, 96, 0.15); }
            .akm-cell-invalid .akm-cell-status { color: #e94560; }
            .akm-cell-empty .akm-cell-status { color: #444; }
            .akm-cell-na {
                background: #111;
                color: #333;
                cursor: not-allowed;
            }
            
            .akm-footer {
                padding: 8px 16px;
                background: #16213e;
                border-top: 1px solid #0f3460;
                font-size: 12px;
                color: #666;
            }
            
            .akm-edit-panel {
                position: absolute;
                right: 0;
                top: 0;
                bottom: 0;
                width: 320px;
                background: #16213e;
                border-left: 1px solid #0f3460;
                padding: 16px;
                overflow-y: auto;
            }
            .akm-edit-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 16px;
                font-size: 14px;
            }
            .akm-edit-header button {
                background: none;
                border: none;
                color: #888;
                font-size: 20px;
                cursor: pointer;
            }
            .akm-edit-instructions {
                background: #0f3460;
                padding: 12px;
                border-radius: 4px;
                margin-bottom: 16px;
            }
            .akm-edit-instructions pre {
                margin: 0;
                font-size: 11px;
                white-space: pre-wrap;
                color: #aaa;
            }
            .akm-edit-instructions a {
                display: inline-block;
                margin-top: 8px;
                color: #4ecca3;
                font-size: 12px;
            }
            .akm-edit-input {
                display: flex;
                gap: 4px;
                margin-bottom: 12px;
            }
            .akm-edit-input input {
                flex: 1;
                padding: 8px;
                background: #0f3460;
                border: 1px solid #1a365d;
                border-radius: 4px;
                color: #eee;
                font-family: monospace;
            }
            .akm-edit-input button {
                background: #0f3460;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                padding: 0 8px;
            }
            .akm-edit-actions {
                display: flex;
                flex-wrap: wrap;
                gap: 4px;
            }
            .akm-edit-actions button {
                padding: 6px 10px;
                background: #0f3460;
                border: none;
                border-radius: 4px;
                color: #ccc;
                cursor: pointer;
                font-size: 12px;
            }
            .akm-edit-actions button:hover { background: #1a365d; }
            
            .akm-test-result {
                margin-top: 12px;
                font-size: 12px;
            }
            .akm-success { color: #4ecca3; }
            .akm-error { color: #e94560; }
            .akm-testing { color: #888; }
            
            .akm-input-invalid {
                border-color: #e94560 !important;
                background: rgba(233, 69, 96, 0.1) !important;
            }
            .akm-validation-error {
                background: rgba(233, 69, 96, 0.15);
                border: 1px solid rgba(233, 69, 96, 0.3);
                color: #e94560;
                padding: 8px;
                border-radius: 4px;
                font-size: 11px;
                margin-bottom: 12px;
            }
            
            .akm-context-menu {
                position: fixed;
                background: #16213e;
                border: 1px solid #0f3460;
                border-radius: 4px;
                padding: 4px;
                z-index: 10002;
            }
            .akm-context-menu button {
                display: block;
                width: 100%;
                padding: 6px 12px;
                background: none;
                border: none;
                color: #ccc;
                text-align: left;
                cursor: pointer;
                font-size: 12px;
            }
            .akm-context-menu button:hover {
                background: #0f3460;
            }
        `;
        document.head.appendChild(style);
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// GLOBAL INSTANCES & COMPAT LAYER
// ═══════════════════════════════════════════════════════════════════════════════

const globalKeyMatrix = new APIKeyMatrix();
const globalKeyMatrixUI = new APIKeyMatrixUI({ matrix: globalKeyMatrix });

// Compatibility with old APIKeyStore interface
const globalKeyStore = {
    get(provider) {
        // Return first key found for this provider
        const keys = globalKeyMatrix.getForProvider(provider);
        return Object.values(keys)[0] || null;
    },
    set(provider, key, meta) {
        globalKeyMatrix.setAllServices(provider, key);
    },
    delete(provider) {
        for (const service of Object.keys(SERVICES)) {
            globalKeyMatrix.set(provider, service, null);
        }
    },
    list() {
        const result = [];
        for (const provider of Object.keys(PROVIDERS)) {
            const keys = globalKeyMatrix.getForProvider(provider);
            if (Object.keys(keys).length > 0) {
                result.push({
                    provider,
                    providerName: PROVIDERS[provider].name,
                    key: Object.values(keys)[0],
                    services: Object.keys(keys)
                });
            }
        }
        return result;
    },
    clearAll() {
        globalKeyMatrix.clearAll();
    },
    export() {
        return globalKeyMatrix.export();
    },
    import(data) {
        globalKeyMatrix.import(data);
    }
};

function showAPIKeyManager() {
    globalKeyMatrixUI.show();
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const API_KEYS_EXPORTS = {
    PROVIDERS,
    SERVICES,
    PROVIDER_SERVICES,
    APIKeyMatrix,
    APIKeyTester,
    GitHubOAuth,
    APIKeyMatrixUI,
    globalKeyMatrix,
    globalKeyMatrixUI,
    globalKeyStore,  // Compat
    showAPIKeyManager
};

if (typeof window !== 'undefined') {
    Object.assign(window, API_KEYS_EXPORTS);
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = API_KEYS_EXPORTS;
}
