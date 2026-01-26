/**
 * github-api.js — Browser-safe GitHub API Client
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Safe patterns for browser GitHub access:
 * 
 * 1. PUBLIC REPOS — No auth needed, just fetch
 * 2. OAUTH FLOW — User logs in via popup, token stays in THEIR browser
 * 3. FINE-GRAINED PAT — User pastes their own token (stored locally)
 * 
 * NEVER embed tokens in source code!
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// GITHUB CLIENT — Browser-safe API access
// ═══════════════════════════════════════════════════════════════════════════════

class GitHubClient {
    constructor(options = {}) {
        this.baseUrl = 'https://api.github.com';
        this.token = null;
        this.user = null;
        
        // Storage key for token (localStorage)
        this.storageKey = options.storageKey || 'moollm_github_token';
        
        // OAuth config (for popup flow)
        this.oauthConfig = {
            clientId: options.clientId || null,  // Your GitHub OAuth App client ID
            redirectUri: options.redirectUri || window.location.origin + '/oauth/callback',
            scope: options.scope || 'repo'  // 'repo' for private, 'public_repo' for public only
        };
        
        // Try to restore saved token
        this._loadToken();
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // AUTHENTICATION
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Check if we have a valid token
     */
    isAuthenticated() {
        return !!this.token;
    }
    
    /**
     * Set token manually (user pastes their PAT)
     * Token is stored in localStorage (user's browser only)
     */
    setToken(token) {
        this.token = token;
        
        if (token) {
            localStorage.setItem(this.storageKey, token);
        } else {
            localStorage.removeItem(this.storageKey);
        }
        
        // Clear cached user
        this.user = null;
    }
    
    /**
     * Load token from localStorage
     */
    _loadToken() {
        try {
            this.token = localStorage.getItem(this.storageKey);
        } catch (e) {
            // localStorage not available
            this.token = null;
        }
    }
    
    /**
     * Clear stored token (logout)
     */
    logout() {
        this.setToken(null);
        this.user = null;
    }
    
    /**
     * Start OAuth flow (popup)
     * Requires a GitHub OAuth App with your clientId
     */
    async loginWithOAuth() {
        if (!this.oauthConfig.clientId) {
            throw new Error('OAuth clientId not configured');
        }
        
        // Generate state for CSRF protection
        const state = crypto.randomUUID?.() || Math.random().toString(36);
        sessionStorage.setItem('github_oauth_state', state);
        
        // Build OAuth URL
        const authUrl = new URL('https://github.com/login/oauth/authorize');
        authUrl.searchParams.set('client_id', this.oauthConfig.clientId);
        authUrl.searchParams.set('redirect_uri', this.oauthConfig.redirectUri);
        authUrl.searchParams.set('scope', this.oauthConfig.scope);
        authUrl.searchParams.set('state', state);
        
        // Open popup
        const popup = window.open(
            authUrl.toString(),
            'github_oauth',
            'width=600,height=700,scrollbars=yes'
        );
        
        // Wait for callback
        return new Promise((resolve, reject) => {
            const checkClosed = setInterval(() => {
                if (popup.closed) {
                    clearInterval(checkClosed);
                    
                    // Check if we got a token
                    if (this.token) {
                        resolve(this.token);
                    } else {
                        reject(new Error('OAuth cancelled'));
                    }
                }
            }, 500);
            
            // Listen for message from popup
            window.addEventListener('message', (event) => {
                if (event.origin !== window.location.origin) return;
                
                if (event.data.type === 'github_oauth_callback') {
                    clearInterval(checkClosed);
                    popup.close();
                    
                    if (event.data.token) {
                        this.setToken(event.data.token);
                        resolve(this.token);
                    } else if (event.data.error) {
                        reject(new Error(event.data.error));
                    }
                }
            }, { once: true });
        });
    }
    
    /**
     * Handle OAuth callback (call from redirect page)
     * Note: Token exchange requires a backend (GitHub won't do it client-side)
     */
    static handleOAuthCallback() {
        const params = new URLSearchParams(window.location.search);
        const code = params.get('code');
        const state = params.get('state');
        const error = params.get('error');
        
        // Verify state
        const savedState = sessionStorage.getItem('github_oauth_state');
        if (state !== savedState) {
            window.opener?.postMessage({ type: 'github_oauth_callback', error: 'State mismatch' }, '*');
            return;
        }
        
        if (error) {
            window.opener?.postMessage({ type: 'github_oauth_callback', error }, '*');
            return;
        }
        
        if (code) {
            // Need to exchange code for token via backend
            // GitHub doesn't allow client-side token exchange for security
            window.opener?.postMessage({ 
                type: 'github_oauth_callback', 
                code,
                error: 'Token exchange requires backend. Use Device Flow or PAT instead.'
            }, '*');
        }
    }
    
    /**
     * Device Flow — Works without backend!
     * User visits a URL and enters a code
     */
    async loginWithDeviceFlow() {
        if (!this.oauthConfig.clientId) {
            throw new Error('OAuth clientId not configured');
        }
        
        // Request device code
        const response = await fetch('https://github.com/login/device/code', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                client_id: this.oauthConfig.clientId,
                scope: this.oauthConfig.scope
            })
        });
        
        const data = await response.json();
        
        // Return info for user to complete login
        return {
            userCode: data.user_code,
            verificationUri: data.verification_uri,
            expiresIn: data.expires_in,
            interval: data.interval,
            deviceCode: data.device_code,
            
            // Poll for token
            poll: () => this._pollDeviceToken(data.device_code, data.interval)
        };
    }
    
    async _pollDeviceToken(deviceCode, interval) {
        const poll = async () => {
            const response = await fetch('https://github.com/login/oauth/access_token', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    client_id: this.oauthConfig.clientId,
                    device_code: deviceCode,
                    grant_type: 'urn:ietf:params:oauth:grant-type:device_code'
                })
            });
            
            const data = await response.json();
            
            if (data.access_token) {
                this.setToken(data.access_token);
                return data.access_token;
            }
            
            if (data.error === 'authorization_pending') {
                // Keep polling
                await new Promise(r => setTimeout(r, interval * 1000));
                return poll();
            }
            
            throw new Error(data.error_description || data.error);
        };
        
        return poll();
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // API REQUESTS
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Make authenticated API request
     */
    async request(endpoint, options = {}) {
        const url = endpoint.startsWith('http') ? endpoint : `${this.baseUrl}${endpoint}`;
        
        const headers = {
            'Accept': 'application/vnd.github.v3+json',
            ...options.headers
        };
        
        if (this.token) {
            headers['Authorization'] = `Bearer ${this.token}`;
        }
        
        const response = await fetch(url, {
            ...options,
            headers
        });
        
        if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(error.message || `GitHub API error: ${response.status}`);
        }
        
        // Handle empty responses
        const text = await response.text();
        return text ? JSON.parse(text) : null;
    }
    
    /**
     * GET request
     */
    async get(endpoint) {
        return this.request(endpoint);
    }
    
    /**
     * POST request
     */
    async post(endpoint, data) {
        return this.request(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
    }
    
    /**
     * PUT request
     */
    async put(endpoint, data) {
        return this.request(endpoint, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
    }
    
    /**
     * PATCH request
     */
    async patch(endpoint, data) {
        return this.request(endpoint, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
    }
    
    /**
     * DELETE request
     */
    async delete(endpoint) {
        return this.request(endpoint, { method: 'DELETE' });
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // USER
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get authenticated user
     */
    async getUser() {
        if (this.user) return this.user;
        
        this.user = await this.get('/user');
        return this.user;
    }
    
    /**
     * Get user's repos
     */
    async getUserRepos(options = {}) {
        const params = new URLSearchParams({
            sort: options.sort || 'updated',
            per_page: options.perPage || 100
        });
        return this.get(`/user/repos?${params}`);
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // REPOS
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get repo info
     */
    async getRepo(owner, repo) {
        return this.get(`/repos/${owner}/${repo}`);
    }
    
    /**
     * Get repo contents (file or directory)
     */
    async getContents(owner, repo, path = '', ref = 'main') {
        const params = ref ? `?ref=${ref}` : '';
        return this.get(`/repos/${owner}/${repo}/contents/${path}${params}`);
    }
    
    /**
     * Get raw file content
     */
    async getRawFile(owner, repo, path, ref = 'main') {
        const url = `https://raw.githubusercontent.com/${owner}/${repo}/${ref}/${path}`;
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Failed to fetch: ${response.status}`);
        }
        return response.text();
    }
    
    /**
     * Create or update a file
     */
    async putFile(owner, repo, path, content, message, options = {}) {
        // Get current file SHA if updating
        let sha = options.sha;
        if (!sha && !options.create) {
            try {
                const existing = await this.getContents(owner, repo, path, options.branch);
                sha = existing.sha;
            } catch (e) {
                // File doesn't exist, will create
            }
        }
        
        const data = {
            message,
            content: btoa(unescape(encodeURIComponent(content))),  // Base64 encode
            branch: options.branch || 'main'
        };
        
        if (sha) {
            data.sha = sha;
        }
        
        return this.put(`/repos/${owner}/${repo}/contents/${path}`, data);
    }
    
    /**
     * Delete a file
     */
    async deleteFile(owner, repo, path, message, options = {}) {
        // Need current SHA
        const existing = await this.getContents(owner, repo, path, options.branch);
        
        return this.delete(`/repos/${owner}/${repo}/contents/${path}`, {
            message,
            sha: existing.sha,
            branch: options.branch || 'main'
        });
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // BRANCHES
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * List branches
     */
    async getBranches(owner, repo) {
        return this.get(`/repos/${owner}/${repo}/branches`);
    }
    
    /**
     * Get specific branch
     */
    async getBranch(owner, repo, branch) {
        return this.get(`/repos/${owner}/${repo}/branches/${branch}`);
    }
    
    /**
     * Create branch
     */
    async createBranch(owner, repo, branchName, fromSha) {
        return this.post(`/repos/${owner}/${repo}/git/refs`, {
            ref: `refs/heads/${branchName}`,
            sha: fromSha
        });
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // COMMITS
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get commits
     */
    async getCommits(owner, repo, options = {}) {
        const params = new URLSearchParams({
            sha: options.branch || 'main',
            per_page: options.perPage || 30
        });
        if (options.path) params.set('path', options.path);
        
        return this.get(`/repos/${owner}/${repo}/commits?${params}`);
    }
    
    /**
     * Get single commit
     */
    async getCommit(owner, repo, sha) {
        return this.get(`/repos/${owner}/${repo}/commits/${sha}`);
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// LOGIN UI — Simple UI for authentication
// ═══════════════════════════════════════════════════════════════════════════════

class GitHubLoginUI {
    constructor(client) {
        this.client = client;
    }
    
    /**
     * Show login dialog
     */
    show() {
        // Remove existing
        document.getElementById('github-login-dialog')?.remove();
        
        const dialog = document.createElement('div');
        dialog.id = 'github-login-dialog';
        dialog.innerHTML = `
            <div class="github-login-overlay">
                <div class="github-login-modal">
                    <h2>🔐 GitHub Login</h2>
                    
                    <div class="github-login-status" id="github-login-status"></div>
                    
                    <div class="github-login-method">
                        <h3>Option 1: Personal Access Token</h3>
                        <p>Create a <a href="https://github.com/settings/tokens?type=beta" target="_blank">fine-grained PAT</a> with repo access.</p>
                        <input type="password" id="github-pat-input" placeholder="ghp_xxxxxxxxxxxx">
                        <button id="github-pat-submit">Login with PAT</button>
                    </div>
                    
                    <div class="github-login-method">
                        <h3>Option 2: Device Flow</h3>
                        <p>Login via GitHub.com (no token to copy)</p>
                        <button id="github-device-flow">Start Device Login</button>
                        <div id="github-device-code" style="display:none;">
                            <p>Visit: <a id="github-device-url" target="_blank"></a></p>
                            <p>Enter code: <code id="github-device-code-value"></code></p>
                            <p><em>Waiting for authorization...</em></p>
                        </div>
                    </div>
                    
                    <div class="github-login-footer">
                        <button id="github-login-cancel">Cancel</button>
                    </div>
                </div>
            </div>
        `;
        
        // Add styles
        if (!document.getElementById('github-login-styles')) {
            const style = document.createElement('style');
            style.id = 'github-login-styles';
            style.textContent = `
                .github-login-overlay {
                    position: fixed; top: 0; left: 0; right: 0; bottom: 0;
                    background: rgba(0,0,0,0.7); z-index: 10000;
                    display: flex; align-items: center; justify-content: center;
                }
                .github-login-modal {
                    background: #1e1e2e; color: #cdd6f4; padding: 30px;
                    border-radius: 12px; max-width: 500px; width: 90%;
                }
                .github-login-modal h2 { margin-top: 0; color: #f9e2af; }
                .github-login-modal h3 { color: #89b4fa; margin-bottom: 10px; }
                .github-login-method { 
                    background: #313244; padding: 15px; border-radius: 8px; 
                    margin: 15px 0;
                }
                .github-login-modal input {
                    width: 100%; padding: 10px; margin: 10px 0;
                    background: #45475a; border: 1px solid #585b70; 
                    border-radius: 4px; color: #cdd6f4;
                }
                .github-login-modal button {
                    background: #89b4fa; color: #1e1e2e; border: none;
                    padding: 10px 20px; border-radius: 4px; cursor: pointer;
                    margin-top: 10px;
                }
                .github-login-modal button:hover { background: #b4befe; }
                .github-login-footer { text-align: right; margin-top: 20px; }
                .github-login-footer button { background: #45475a; color: #cdd6f4; }
                .github-login-status { padding: 10px; border-radius: 4px; margin-bottom: 15px; display: none; }
                .github-login-status.success { display: block; background: #a6e3a1; color: #1e1e2e; }
                .github-login-status.error { display: block; background: #f38ba8; color: #1e1e2e; }
                .github-login-modal a { color: #89b4fa; }
                .github-login-modal code { 
                    background: #45475a; padding: 5px 10px; border-radius: 4px;
                    font-size: 1.2em; font-family: monospace;
                }
            `;
            document.head.appendChild(style);
        }
        
        document.body.appendChild(dialog);
        
        // Wire up events
        const statusEl = document.getElementById('github-login-status');
        
        document.getElementById('github-pat-submit').addEventListener('click', async () => {
            const token = document.getElementById('github-pat-input').value.trim();
            if (!token) return;
            
            this.client.setToken(token);
            
            try {
                const user = await this.client.getUser();
                statusEl.className = 'github-login-status success';
                statusEl.textContent = `✅ Logged in as ${user.login}`;
                
                setTimeout(() => dialog.remove(), 1500);
            } catch (e) {
                statusEl.className = 'github-login-status error';
                statusEl.textContent = `❌ Invalid token: ${e.message}`;
                this.client.logout();
            }
        });
        
        document.getElementById('github-device-flow').addEventListener('click', async () => {
            if (!this.client.oauthConfig.clientId) {
                statusEl.className = 'github-login-status error';
                statusEl.textContent = '❌ OAuth client ID not configured';
                return;
            }
            
            try {
                const flow = await this.client.loginWithDeviceFlow();
                
                document.getElementById('github-device-code').style.display = 'block';
                document.getElementById('github-device-url').href = flow.verificationUri;
                document.getElementById('github-device-url').textContent = flow.verificationUri;
                document.getElementById('github-device-code-value').textContent = flow.userCode;
                
                const token = await flow.poll();
                
                const user = await this.client.getUser();
                statusEl.className = 'github-login-status success';
                statusEl.textContent = `✅ Logged in as ${user.login}`;
                
                setTimeout(() => dialog.remove(), 1500);
            } catch (e) {
                statusEl.className = 'github-login-status error';
                statusEl.textContent = `❌ ${e.message}`;
            }
        });
        
        document.getElementById('github-login-cancel').addEventListener('click', () => {
            dialog.remove();
        });
        
        dialog.querySelector('.github-login-overlay').addEventListener('click', (e) => {
            if (e.target === e.currentTarget) dialog.remove();
        });
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const GITHUB_API_EXPORTS = {
    GitHubClient,
    GitHubLoginUI
};

if (typeof window !== 'undefined') {
    Object.assign(window, GITHUB_API_EXPORTS);
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = GITHUB_API_EXPORTS;
}
