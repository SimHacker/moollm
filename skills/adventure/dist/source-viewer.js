/**
 * source-viewer.js — View Source for Every Object in the World
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * Every object in a MOOLLM adventure has a path identity:
 * 
 *   moollm://moollm/examples/adventure-4/street/lane-neverending/no-ai-tower/lobby
 *   
 * This maps directly to GitHub:
 * 
 *   https://github.com/leela-ai/moollm/blob/main/examples/adventure-4/.../lobby/ROOM.yml
 * 
 * This module provides:
 * - URL generation for GitHub (view, edit, blame, raw)
 * - Iframe-based source viewer overlay
 * - Pie menu integration for "View Source"
 * - moollm:// namespace resolution
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// MOOLLM NAMESPACE — Universal Object Identity
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * The moollm:// namespace maps object IDs to repository paths.
 * 
 * FULL FORMAT (explicit platform):
 *   moollm://PLATFORM/OWNER/REPO/PATH
 * 
 * Examples:
 *   moollm://github/SimHacker/moollm/examples/adventure-4/street/lane-neverending
 *   moollm://github/leela-ai/central/apps/insights/pyleela/brain/WAMPAgent
 *   moollm://gitlab/myorg/myrepo/path/to/object
 *   moollm://local/path/to/file  (local filesystem)
 * 
 * SHORT FORMAT (uses aliases):
 *   moollm://moollm/skills/adventure  → expands to github/SimHacker/moollm/...
 *   moollm://central/apps/insights    → expands to github/leela-ai/central/...
 * 
 * WITH GIT REF:
 *   moollm://github/SimHacker/moollm@v1.0.0/skills/adventure
 *   moollm://github/SimHacker/moollm@abc123def/debug-snapshot
 * 
 * This creates a global namespace where every YAML file, every room,
 * every object, every character has a unique, addressable identity.
 */

class MoollmNamespace {
    constructor(config = {}) {
        // Supported hosting platforms
        this.platforms = new Map([
            ['github', {
                name: 'GitHub',
                baseUrl: 'https://github.com',
                rawUrl: 'https://raw.githubusercontent.com',
                blobPath: 'blob',
                treePath: 'tree',
                editPath: 'edit',
                blamePath: 'blame',
                historyPath: 'commits'
            }],
            ['gitlab', {
                name: 'GitLab',
                baseUrl: 'https://gitlab.com',
                rawUrl: 'https://gitlab.com',
                rawSuffix: '/-/raw',
                blobPath: '-/blob',
                treePath: '-/tree',
                editPath: '-/edit',
                blamePath: '-/blame',
                historyPath: '-/commits'
            }],
            ['bitbucket', {
                name: 'Bitbucket',
                baseUrl: 'https://bitbucket.org',
                rawUrl: 'https://bitbucket.org',
                rawSuffix: '/raw',
                blobPath: 'src',
                treePath: 'src',
                editPath: 'src',
                blamePath: 'annotate',
                historyPath: 'history-node'
            }],
            ['local', {
                name: 'Local',
                baseUrl: 'file://',
                isLocal: true
            }]
        ]);
        
        // Repo aliases (short names → full platform/owner/repo)
        this.aliases = new Map([
            ['moollm', {
                platform: 'github',
                owner: 'SimHacker',
                repo: 'moollm',
                defaultBranch: 'main',
                description: 'MOOLLM — Skills, adventures, and kernel'
            }],
            ['central', {
                platform: 'github',
                owner: 'leela-ai',
                repo: 'central',
                defaultBranch: 'main',
                description: 'Leela Central — Main monorepo'
            }],
            ['gastown', {
                platform: 'github',
                owner: 'leela-ai',
                repo: 'gastown',
                defaultBranch: 'main',
                description: 'Gastown — Go runtime'
            }],
            ['mooco', {
                platform: 'github',
                owner: 'leela-ai',
                repo: 'mooco',
                defaultBranch: 'main',
                description: 'Mooco — New orchestrator'
            }]
        ]);
        
        // Override/add aliases from config
        if (config.aliases) {
            for (const [name, alias] of Object.entries(config.aliases)) {
                this.aliases.set(name, alias);
            }
        }
        
        // Legacy: repos config (convert to aliases)
        if (config.repos) {
            for (const [name, repo] of Object.entries(config.repos)) {
                // Parse github field like "leela-ai/moollm"
                const [owner, repoName] = (repo.github || '').split('/');
                this.aliases.set(name, {
                    platform: 'github',
                    owner: owner || name,
                    repo: repoName || name,
                    defaultBranch: repo.defaultBranch || 'main',
                    description: repo.description
                });
            }
        }
        
        // Override with config
        if (config.repos) {
            for (const [name, repo] of Object.entries(config.repos)) {
                this.repos.set(name, repo);
            }
        }
        
        // Current context (set by adventure compiler)
        this.currentAlias = config.currentRepo || config.currentAlias || 'moollm';
        this.currentBranch = config.currentBranch || 'main';
        
        // Alias: currentRepo = currentAlias
        this.currentRepo = this.currentAlias;
        
        // ═══════════════════════════════════════════════════════════════════════
        // GIT REF TRACKING — Branch/tag/commit per mounted path
        // ═══════════════════════════════════════════════════════════════════════
        // 
        // Different paths can be mounted from different git refs:
        // 
        //   /examples/adventure-4  → main (latest)
        //   /skills/v1             → v1.0.0 (tagged release)
        //   /skills/experimental   → feature-branch
        //   /debug-snapshot        → abc123def (specific commit)
        //
        // This enables:
        // - Mixing stable and experimental content
        // - Time travel to specific versions
        // - Revert to any known state
        // ═══════════════════════════════════════════════════════════════════════
        
        // Path → git ref mapping (most specific match wins)
        // Key: repo:path, Value: { ref, type, label }
        this.mounts = new Map();
        
        // Load mounts from config
        if (config.mounts) {
            for (const mount of config.mounts) {
                const key = `${mount.repo || this.currentRepo}:${mount.path}`;
                this.mounts.set(key, {
                    ref: mount.ref || 'main',
                    type: mount.type || 'branch', // 'branch', 'tag', 'commit'
                    label: mount.label || mount.ref,
                    mounted_at: mount.mounted_at || new Date().toISOString()
                });
            }
        }
    }
    
    /**
     * Mount a path to a specific git ref
     * @param {string} repo - Repository name
     * @param {string} path - Path prefix to mount
     * @param {string} ref - Git ref (branch, tag, or commit SHA)
     * @param {string} type - 'branch', 'tag', or 'commit'
     */
    mount(repo, path, ref, type = 'branch') {
        const key = `${repo}:${path}`;
        this.mounts.set(key, {
            ref,
            type,
            label: type === 'commit' ? ref.slice(0, 7) : ref,
            mounted_at: new Date().toISOString()
        });
    }
    
    /**
     * Get the git ref for a given path (most specific mount wins)
     * @param {string} repo - Repository name
     * @param {string} path - Full path
     * @returns {object} { ref, type, label } or default branch
     */
    getGitRef(repo, path) {
        // Find most specific matching mount
        let bestMatch = null;
        let bestLength = -1;
        
        for (const [key, mount] of this.mounts) {
            const [mountRepo, mountPath] = key.split(':');
            if (mountRepo !== repo) continue;
            
            // Check if path starts with mount path
            if (path.startsWith(mountPath) && mountPath.length > bestLength) {
                bestMatch = mount;
                bestLength = mountPath.length;
            }
        }
        
        if (bestMatch) {
            return bestMatch;
        }
        
        // Default to repo's default branch
        const repoInfo = this.repos.get(repo);
        return {
            ref: repoInfo?.defaultBranch || 'main',
            type: 'branch',
            label: repoInfo?.defaultBranch || 'main'
        };
    }
    
    /**
     * List all current mounts
     */
    listMounts() {
        return Array.from(this.mounts.entries()).map(([key, mount]) => {
            const [repo, path] = key.split(':');
            return { repo, path, ...mount };
        });
    }
    
    /**
     * Parse a moollm:// URL
     * 
     * Formats:
     *   moollm://platform/owner/repo/path          Full explicit
     *   moollm://platform/owner/repo@ref/path      Full with git ref
     *   moollm://alias/path                        Short (uses alias)
     *   moollm://alias@ref/path                    Short with git ref
     *   path/to/object                             Just path (uses current context)
     * 
     * FRAGMENT — Sub-document path:
     *   moollm://repo/file.yml#key/subkey          Path within YAML
     *   moollm://repo/characters/don/head.yml#nose/left_nostril
     * 
     * @param {string} url - moollm:// URL or path
     * @returns {object} { platform, owner, repo, path, segments, gitRef, alias, fragment, fragmentPath }
     */
    parse(url) {
        let platform, owner, repo, path, explicitRef = null, alias = null;
        
        // ═══════════════════════════════════════════════════════════════════════
        // FRAGMENT — Sub-document path (#key/subkey/etc)
        // ═══════════════════════════════════════════════════════════════════════
        let fragment = null;
        let fragmentPath = null;
        
        if (url.includes('#')) {
            const [urlPart, frag] = url.split('#', 2);
            url = urlPart;
            fragment = frag;
            fragmentPath = frag.split('/').filter(s => s);
        }
        
        if (!url.startsWith('moollm://')) {
            // Just a path - use current context
            const currentAlias = this.aliases.get(this.currentAlias);
            if (currentAlias) {
                platform = currentAlias.platform;
                owner = currentAlias.owner;
                repo = currentAlias.repo;
                alias = this.currentAlias;
            } else {
                platform = 'github';
                owner = 'SimHacker';
                repo = 'moollm';
            }
            path = url.replace(/^\//, '');
        } else {
            const withoutProtocol = url.replace('moollm://', '');
            const parts = withoutProtocol.split('/');
            
            // Check if first part is a known platform
            if (this.platforms.has(parts[0])) {
                // Full format: platform/owner/repo[@ref]/path
                platform = parts[0];
                
                // Parse owner (might have @ref)
                const ownerPart = parts[1] || '';
                const ownerMatch = ownerPart.match(/^([^@]+)(?:@(.+))?$/);
                owner = ownerMatch ? ownerMatch[1] : ownerPart;
                
                // Check if ref is on owner or repo
                if (ownerMatch && ownerMatch[2]) {
                    // moollm://github/owner@ref/repo/path (unusual but support it)
                    explicitRef = ownerMatch[2];
                    repo = parts[2] || '';
                    path = parts.slice(3).join('/');
                } else {
                    // Parse repo (might have @ref)
                    const repoPart = parts[2] || '';
                    const repoMatch = repoPart.match(/^([^@]+)(?:@(.+))?$/);
                    repo = repoMatch ? repoMatch[1] : repoPart;
                    explicitRef = repoMatch ? repoMatch[2] : null;
                    path = parts.slice(3).join('/');
                }
            } else if (this.aliases.has(parts[0].replace(/@.*$/, ''))) {
                // Short format: alias[@ref]/path
                const aliasMatch = parts[0].match(/^([^@]+)(?:@(.+))?$/);
                alias = aliasMatch[1];
                explicitRef = aliasMatch[2] || null;
                
                const aliasInfo = this.aliases.get(alias);
                platform = aliasInfo.platform;
                owner = aliasInfo.owner;
                repo = aliasInfo.repo;
                path = parts.slice(1).join('/');
            } else {
                // Unknown - assume it's an alias we don't know about
                const aliasMatch = parts[0].match(/^([^@]+)(?:@(.+))?$/);
                alias = aliasMatch[1];
                explicitRef = aliasMatch[2] || null;
                
                // Default to github with alias as both owner and repo
                platform = 'github';
                owner = alias;
                repo = alias;
                path = parts.slice(1).join('/');
            }
        }
        
        // Get git ref (explicit > mount > default)
        let gitRef;
        if (explicitRef) {
            gitRef = {
                ref: explicitRef,
                type: this._guessRefType(explicitRef),
                label: explicitRef,
                explicit: true
            };
        } else {
            gitRef = this.getGitRef(alias || `${owner}/${repo}`, path);
        }
        
        return {
            platform,
            owner,
            repo,
            path,
            segments: path.split('/').filter(s => s),
            gitRef,
            alias,
            // Convenience: "owner/repo" format
            repo_full: `${owner}/${repo}`,
            // Sub-document fragment path
            fragment,
            fragmentPath
        };
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // SUB-DOCUMENT OPERATIONS — Get/set values within YAML by path
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get a value at a path within an object
     * @param {object} obj - The object to traverse
     * @param {string|array} path - Path like "nose/left_nostril" or ['nose', 'left_nostril']
     */
    static getAtPath(obj, path) {
        const keys = Array.isArray(path) ? path : path.split('/').filter(s => s);
        let current = obj;
        
        for (const key of keys) {
            if (current === null || current === undefined) return undefined;
            
            // Handle array indices
            if (Array.isArray(current) && /^\d+$/.test(key)) {
                current = current[parseInt(key, 10)];
            } else {
                current = current[key];
            }
        }
        
        return current;
    }
    
    /**
     * Set a value at a path within an object
     * @param {object} obj - The object to modify
     * @param {string|array} path - Path like "nose/left_nostril"
     * @param {*} value - Value to set
     * @param {boolean} create - Create intermediate objects if missing
     */
    static setAtPath(obj, path, value, create = true) {
        const keys = Array.isArray(path) ? path : path.split('/').filter(s => s);
        let current = obj;
        
        for (let i = 0; i < keys.length - 1; i++) {
            const key = keys[i];
            const nextKey = keys[i + 1];
            
            if (current[key] === undefined || current[key] === null) {
                if (!create) return false;
                // Create object or array based on next key
                current[key] = /^\d+$/.test(nextKey) ? [] : {};
            }
            
            current = current[key];
        }
        
        const lastKey = keys[keys.length - 1];
        current[lastKey] = value;
        return true;
    }
    
    /**
     * Delete a value at a path within an object
     */
    static deleteAtPath(obj, path) {
        const keys = Array.isArray(path) ? path : path.split('/').filter(s => s);
        let current = obj;
        
        for (let i = 0; i < keys.length - 1; i++) {
            if (current === null || current === undefined) return false;
            current = current[keys[i]];
        }
        
        if (current === null || current === undefined) return false;
        
        const lastKey = keys[keys.length - 1];
        if (Array.isArray(current) && /^\d+$/.test(lastKey)) {
            current.splice(parseInt(lastKey, 10), 1);
        } else {
            delete current[lastKey];
        }
        return true;
    }
    
    /**
     * Guess if a ref is a branch, tag, or commit
     */
    _guessRefType(ref) {
        // Commit SHA (7+ hex chars)
        if (/^[a-f0-9]{7,40}$/.test(ref)) return 'commit';
        // Semver-ish tag
        if (/^v?\d+\.\d+/.test(ref)) return 'tag';
        // Default to branch
        return 'branch';
    }
    
    /**
     * Format a moollm:// URL
     * 
     * Two calling conventions:
     *   format({ alias, path, ref })           — From options object
     *   format({ platform, owner, repo, path, ref })
     *   format(repo, path)                     — Simple repo + path
     */
    format(optsOrRepo, path) {
        // Simple form: format('moollm', 'skills/adventure')
        if (typeof optsOrRepo === 'string') {
            return `moollm://${optsOrRepo}/${(path || '').replace(/^\//, '')}`;
        }
        
        // Object form: format({ alias: 'moollm', path: '...', ref: 'v1.0' })
        const opts = optsOrRepo;
        if (opts.alias) {
            const refPart = opts.ref ? `@${opts.ref}` : '';
            return `moollm://${opts.alias}${refPart}/${opts.path || ''}`;
        } else {
            const refPart = opts.ref ? `@${opts.ref}` : '';
            return `moollm://${opts.platform}/${opts.owner}/${opts.repo}${refPart}/${opts.path || ''}`;
        }
    }
    
    /**
     * Get web URL for an object (GitHub, GitLab, etc.)
     * @param {string} moollmUrl - moollm:// URL or path
     * @param {string} view - 'blob', 'edit', 'blame', 'raw', 'tree'
     * @param {string} file - Optional specific file (ROOM.yml, README.md, etc.)
     */
    toWebUrl(moollmUrl, view = 'blob', file = null) {
        const parsed = this.parse(moollmUrl);
        const { platform, owner, repo, path, gitRef } = parsed;
        
        const platformInfo = this.platforms.get(platform);
        if (!platformInfo) {
            console.warn(`Unknown platform: ${platform}`);
            return null;
        }
        
        // Handle local paths
        if (platformInfo.isLocal) {
            return `file://${path}${file ? '/' + file : ''}`;
        }
        
        const ref = gitRef.ref;
        const fullPath = file ? `${path}/${file}` : path;
        const repoPath = `${owner}/${repo}`;
        
        // Build URL based on platform
        switch (view) {
            case 'blob':
            case 'view':
                return `${platformInfo.baseUrl}/${repoPath}/${platformInfo.blobPath}/${ref}/${fullPath}`;
            case 'edit':
                return `${platformInfo.baseUrl}/${repoPath}/${platformInfo.editPath}/${ref}/${fullPath}`;
            case 'blame':
                return `${platformInfo.baseUrl}/${repoPath}/${platformInfo.blamePath}/${ref}/${fullPath}`;
            case 'raw':
                if (platform === 'github') {
                    return `${platformInfo.rawUrl}/${repoPath}/${ref}/${fullPath}`;
                } else if (platformInfo.rawSuffix) {
                    return `${platformInfo.rawUrl}/${repoPath}${platformInfo.rawSuffix}/${ref}/${fullPath}`;
                }
                return `${platformInfo.baseUrl}/${repoPath}/raw/${ref}/${fullPath}`;
            case 'tree':
                return `${platformInfo.baseUrl}/${repoPath}/${platformInfo.treePath}/${ref}/${fullPath}`;
            case 'history':
                return `${platformInfo.baseUrl}/${repoPath}/${platformInfo.historyPath}/${ref}/${fullPath}`;
            default:
                return `${platformInfo.baseUrl}/${repoPath}/${platformInfo.blobPath}/${ref}/${fullPath}`;
        }
    }
    
    /**
     * Get all standard URLs for an object
     */
    getObjectURLs(moollmUrl) {
        const parsed = this.parse(moollmUrl);
        const { platform, owner, repo, path, gitRef, alias } = parsed;
        
        // Generate the canonical moollm:// URL
        const moollmCanonical = alias 
            ? this.format({ alias, path, ref: gitRef.explicit ? gitRef.ref : null })
            : this.format({ platform, owner, repo, path, ref: gitRef.explicit ? gitRef.ref : null });
        
        return {
            // The object itself (moollm:// URL)
            moollm: moollmCanonical,
            
            // Full explicit form (for sharing)
            moollmFull: this.format({ platform, owner, repo, path }),
            
            // Directory view
            tree: this.toWebUrl(moollmUrl, 'tree'),
            
            // Standard files
            room: this.toWebUrl(moollmUrl, 'blob', 'ROOM.yml'),
            readme: this.toWebUrl(moollmUrl, 'blob', 'README.md'),
            card: this.toWebUrl(moollmUrl, 'blob', 'CARD.yml'),
            skill: this.toWebUrl(moollmUrl, 'blob', 'SKILL.md'),
            
            // Actions
            edit: this.toWebUrl(moollmUrl, 'edit', 'ROOM.yml'),
            history: this.toWebUrl(moollmUrl, 'history'),
            
            // Raw for fetching
            rawRoom: this.toWebUrl(moollmUrl, 'raw', 'ROOM.yml'),
            rawReadme: this.toWebUrl(moollmUrl, 'raw', 'README.md'),
            
            // Metadata
            _parsed: parsed
        };
    }
    
    /**
     * Register an alias
     */
    registerAlias(name, config) {
        this.aliases.set(name, {
            platform: config.platform || 'github',
            owner: config.owner,
            repo: config.repo,
            defaultBranch: config.defaultBranch || 'main',
            description: config.description
        });
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// SOURCE VIEWER — Overlay for viewing object source
// ═══════════════════════════════════════════════════════════════════════════════

class SourceViewer {
    constructor(options = {}) {
        this.namespace = new MoollmNamespace(options.namespace);
        this.container = null;
        this.frame = null;
        this.isOpen = false;
        
        // Engine reference for live state
        this.engine = options.engine || null;
        
        // View mode: 'source', 'live', 'split'
        this.viewMode = options.viewMode || 'source';
        
        // Styling
        this.position = options.position || 'right'; // 'right', 'bottom', 'modal'
        this.width = options.width || '40%';
        this.height = options.height || '100%';
    }
    
    /**
     * Set engine reference for live state access
     */
    setEngine(engine) {
        this.engine = engine;
    }
    
    /**
     * Initialize the viewer container
     */
    init(parentContainer) {
        // Create overlay container
        this.container = document.createElement('div');
        this.container.id = 'source-viewer';
        this.container.className = 'source-viewer closed';
        this.container.innerHTML = `
            <div class="source-viewer-header">
                <span class="source-viewer-title">🔍 Inspector</span>
                <div class="source-viewer-mode">
                    <button data-mode="source" class="active" title="GitHub Source">📄 Source</button>
                    <button data-mode="live" title="Runtime State">⚡ Live</button>
                    <button data-mode="split" title="Side-by-Side">◧ Split</button>
                </div>
                <button class="source-viewer-close">✕</button>
            </div>
            <div class="source-viewer-tabs">
                <button data-view="room" class="active">ROOM.yml</button>
                <button data-view="readme">README</button>
                <button data-view="tree">Files</button>
                <button data-view="edit">Edit ↗</button>
            </div>
            <div class="source-viewer-content">
                <!-- Single pane for source/live -->
                <div class="source-viewer-pane source-pane">
                    <iframe class="source-viewer-frame" sandbox="allow-scripts allow-same-origin"></iframe>
                </div>
                <!-- Live state pane -->
                <div class="source-viewer-pane live-pane" style="display:none;">
                    <div class="live-state-header">
                        <span class="live-state-type"></span>
                        <span class="live-state-id"></span>
                        <div class="live-state-actions">
                            <button class="live-state-refresh" title="Refresh">🔄</button>
                            <button class="live-state-revert" title="Revert to source">⏪ Revert</button>
                        </div>
                    </div>
                    <pre class="live-state-json"></pre>
                    <div class="live-state-diff" style="display:none;">
                        <h4>⚡ Changed from Source:</h4>
                        <pre class="live-state-changes"></pre>
                    </div>
                </div>
            </div>
            <div class="source-viewer-info">
                <div class="source-viewer-path-container">
                    <code class="source-viewer-path"></code>
                    <span class="source-viewer-gitref" title="Git ref"></span>
                </div>
                <span class="source-viewer-status"></span>
            </div>
        `;
        
        // Insert into DOM
        if (parentContainer) {
            parentContainer.appendChild(this.container);
        } else {
            document.body.appendChild(this.container);
        }
        
        this.frame = this.container.querySelector('.source-viewer-frame');
        this.sourcePane = this.container.querySelector('.source-pane');
        this.livePane = this.container.querySelector('.live-pane');
        this.liveStateJson = this.container.querySelector('.live-state-json');
        this.liveStateChanges = this.container.querySelector('.live-state-changes');
        
        // Wire up events
        this.container.querySelector('.source-viewer-close').addEventListener('click', () => {
            this.close();
        });
        
        // View tabs (ROOM.yml, README, etc.)
        this.container.querySelectorAll('.source-viewer-tabs button').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const view = e.target.dataset.view;
                this._switchView(view);
            });
        });
        
        // Mode buttons (Source, Live, Split)
        this.container.querySelectorAll('.source-viewer-mode button').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const mode = e.target.dataset.mode;
                this._switchMode(mode);
            });
        });
        
        // Refresh live state
        this.container.querySelector('.live-state-refresh')?.addEventListener('click', () => {
            this._refreshLiveState();
        });
        
        // Revert to source
        this.container.querySelector('.live-state-revert')?.addEventListener('click', () => {
            this._revertToSource();
        });
        
        // Add styles
        this._injectStyles();
    }
    
    // ═══════════════════════════════════════════════════════════════════════════════
    // PULL FROM SOURCE — Multiple Merge Strategies
    // ═══════════════════════════════════════════════════════════════════════════════
    //
    // STRATEGIES:
    //   replace  — Full overwrite: source completely replaces live
    //   merge    — Source wins: merge source into live, source wins conflicts
    //   underlay — Live wins: merge source under live, live wins conflicts
    //   pick     — Select specific keys to pull from source
    //
    // The runtime prefers minimized JSON, but can load commented YAML.
    // Both parse to the same structures deterministically.
    //
    // ═══════════════════════════════════════════════════════════════════════════════

    /**
     * Pull source and apply with specified strategy
     * @param {string} strategy - 'replace', 'merge', 'underlay', 'pick'
     * @param {object} options - { keys: [...] } for pick strategy
     */
    async pullSource(strategy = 'replace', options = {}) {
        if (!this.currentEntity || !this.currentURLs) {
            console.warn('No entity to pull');
            return { success: false, error: 'No entity' };
        }
        
        this._setStatus('Fetching source...', 'loading');
        
        try {
            // Fetch raw source (YAML or JSON)
            const response = await fetch(this.currentURLs.rawRoom);
            if (!response.ok) {
                throw new Error(`Failed to fetch: ${response.status}`);
            }
            
            const sourceText = await response.text();
            const sourceData = await this._parseSource(sourceText);
            
            if (!sourceData) {
                throw new Error('Could not parse source');
            }
            
            // Apply with specified strategy
            const result = this._applyWithStrategy(
                this.currentEntity, 
                sourceData, 
                strategy, 
                options
            );
            
            // Refresh display
            this._refreshLiveState();
            
            // Emit event
            if (this.engine?.emit) {
                this.engine.emit('entity:pulled', {
                    entity: this.currentEntity,
                    source: sourceData,
                    strategy,
                    changes: result.changes
                });
            }
            
            this._setStatus(`✅ Pulled (${strategy})`, 'success');
            return { success: true, ...result };
            
        } catch (error) {
            console.error('Pull failed:', error);
            this._setStatus(`❌ Pull failed: ${error.message}`, 'error');
            return { success: false, error: error.message };
        }
    }
    
    /**
     * Revert to source (shortcut for pull replace)
     */
    async _revertToSource() {
        const entityId = this.currentEntity?.id || 'entity';
        
        if (!confirm(`⏪ Revert "${entityId}" to source?\n\nThis will discard all runtime changes.`)) {
            return;
        }
        
        return this.pullSource('replace');
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // FRAGMENT PULL — Revert just a subtree within the document
    // ═══════════════════════════════════════════════════════════════════════════
    //
    // URL: moollm://repo/path/to/file.yml#nose/left_nostril
    //
    // This reverts ONLY the nose.left_nostril key, not the whole file!
    //
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Pull a specific subtree from source
     * @param {string} moollmUrl - URL with fragment, e.g., path/to/file.yml#key/subkey
     * @param {string} strategy - 'replace', 'merge', 'underlay'
     */
    async pullFragment(moollmUrl, strategy = 'replace') {
        const parsed = this.namespace.parse(moollmUrl);
        
        if (!parsed.fragment) {
            // No fragment — fall back to regular pull
            return this.pullSource(strategy);
        }
        
        if (!this.currentEntity) {
            return { success: false, error: 'No entity loaded' };
        }
        
        const fragmentPath = parsed.fragmentPath;
        this._setStatus(`Pulling ${fragmentPath.join('/')}...`, 'loading');
        
        try {
            // Fetch full source
            const response = await fetch(this.currentURLs?.rawRoom || 
                this.namespace.toWebUrl(moollmUrl, 'raw'));
            if (!response.ok) {
                throw new Error(`Failed to fetch: ${response.status}`);
            }
            
            const sourceText = await response.text();
            const sourceData = await this._parseSource(sourceText);
            
            // Get the subtree from source
            const sourceSubtree = MoollmNamespace.getAtPath(sourceData, fragmentPath);
            
            if (sourceSubtree === undefined) {
                throw new Error(`Path not found in source: ${parsed.fragment}`);
            }
            
            // Get current live subtree
            const liveData = this.currentEntity.data || {};
            const liveSubtree = MoollmNamespace.getAtPath(liveData, fragmentPath);
            
            const changes = [];
            
            switch (strategy) {
                case 'replace':
                    // Replace just this subtree
                    MoollmNamespace.setAtPath(liveData, fragmentPath, this._deepClone(sourceSubtree));
                    changes.push({ 
                        type: 'replaced', 
                        path: parsed.fragment, 
                        from: liveSubtree, 
                        to: sourceSubtree 
                    });
                    break;
                    
                case 'merge':
                    // Merge source into live (source wins)
                    if (typeof sourceSubtree === 'object' && typeof liveSubtree === 'object') {
                        const merged = { ...liveSubtree, ...sourceSubtree };
                        MoollmNamespace.setAtPath(liveData, fragmentPath, merged);
                        changes.push({ type: 'merged', path: parsed.fragment });
                    } else {
                        MoollmNamespace.setAtPath(liveData, fragmentPath, this._deepClone(sourceSubtree));
                        changes.push({ type: 'replaced', path: parsed.fragment });
                    }
                    break;
                    
                case 'underlay':
                    // Only set if live is undefined
                    if (liveSubtree === undefined) {
                        MoollmNamespace.setAtPath(liveData, fragmentPath, this._deepClone(sourceSubtree));
                        changes.push({ type: 'added', path: parsed.fragment, to: sourceSubtree });
                    }
                    break;
                    
                case 'delete':
                    // Delete this path from live
                    MoollmNamespace.deleteAtPath(liveData, fragmentPath);
                    changes.push({ type: 'deleted', path: parsed.fragment });
                    break;
            }
            
            // Refresh display
            this._refreshLiveState();
            
            // Emit event
            if (this.engine?.emit) {
                this.engine.emit('entity:fragment-pulled', {
                    entity: this.currentEntity,
                    fragment: parsed.fragment,
                    fragmentPath,
                    strategy,
                    changes
                });
            }
            
            this._setStatus(`✅ Pulled #${parsed.fragment}`, 'success');
            return { success: true, changes };
            
        } catch (error) {
            console.error('Fragment pull failed:', error);
            this._setStatus(`❌ Pull failed: ${error.message}`, 'error');
            return { success: false, error: error.message };
        }
    }
    
    /**
     * Get a subtree from the current entity
     * @param {string} fragmentPath - Path like "nose/left_nostril"
     */
    getFragment(fragmentPath) {
        if (!this.currentEntity?.data) return undefined;
        return MoollmNamespace.getAtPath(this.currentEntity.data, fragmentPath);
    }
    
    /**
     * Set a subtree in the current entity
     * @param {string} fragmentPath - Path like "nose/left_nostril"
     * @param {*} value - Value to set
     */
    setFragment(fragmentPath, value) {
        if (!this.currentEntity?.data) return false;
        MoollmNamespace.setAtPath(this.currentEntity.data, fragmentPath, value);
        this._refreshLiveState();
        return true;
    }
    
    /**
     * Apply source data with specified merge strategy
     */
    _applyWithStrategy(entity, sourceData, strategy, options = {}) {
        if (!entity || !sourceData) return { changes: [] };
        
        const changes = [];
        const liveData = entity.data || {};
        
        // Keys to always preserve (runtime state)
        const RUNTIME_KEYS = ['_type', '_runtime', 'visited', 'discovered', '_lastSeen'];
        
        switch (strategy) {
            
            // ═══════════════════════════════════════════════════════════════════
            // REPLACE — Full overwrite, source wins completely
            // ═══════════════════════════════════════════════════════════════════
            case 'replace': {
                // Preserve runtime keys
                const preserved = {};
                for (const key of RUNTIME_KEYS) {
                    if (liveData[key] !== undefined) {
                        preserved[key] = liveData[key];
                    }
                }
                
                // Clear everything except _runtime prefixed
                for (const key of Object.keys(liveData)) {
                    if (!key.startsWith('_runtime')) {
                        changes.push({ type: 'removed', key, from: liveData[key] });
                        delete liveData[key];
                    }
                }
                
                // Apply all source data
                for (const [key, value] of Object.entries(sourceData)) {
                    changes.push({ type: 'set', key, to: value });
                    liveData[key] = this._deepClone(value);
                }
                
                // Restore preserved
                Object.assign(liveData, preserved);
                break;
            }
            
            // ═══════════════════════════════════════════════════════════════════
            // MERGE — Source wins conflicts, keeps live-only keys
            // ═══════════════════════════════════════════════════════════════════
            case 'merge': {
                for (const [key, value] of Object.entries(sourceData)) {
                    if (RUNTIME_KEYS.includes(key)) continue;
                    
                    const oldValue = liveData[key];
                    const newValue = this._deepClone(value);
                    
                    if (oldValue === undefined) {
                        changes.push({ type: 'added', key, to: newValue });
                    } else if (JSON.stringify(oldValue) !== JSON.stringify(newValue)) {
                        changes.push({ type: 'changed', key, from: oldValue, to: newValue });
                    }
                    
                    liveData[key] = newValue;
                }
                break;
            }
            
            // ═══════════════════════════════════════════════════════════════════
            // UNDERLAY — Live wins conflicts, source fills gaps
            // ═══════════════════════════════════════════════════════════════════
            case 'underlay': {
                for (const [key, value] of Object.entries(sourceData)) {
                    if (RUNTIME_KEYS.includes(key)) continue;
                    
                    // Only set if live doesn't have it
                    if (liveData[key] === undefined) {
                        const newValue = this._deepClone(value);
                        changes.push({ type: 'added', key, to: newValue });
                        liveData[key] = newValue;
                    }
                    // Live has it? Keep live value (no change)
                }
                break;
            }
            
            // ═══════════════════════════════════════════════════════════════════
            // PICK — Select specific keys to pull
            // ═══════════════════════════════════════════════════════════════════
            case 'pick': {
                const keys = options.keys || [];
                
                for (const key of keys) {
                    if (RUNTIME_KEYS.includes(key)) continue;
                    if (sourceData[key] === undefined) continue;
                    
                    const oldValue = liveData[key];
                    const newValue = this._deepClone(sourceData[key]);
                    
                    if (oldValue === undefined) {
                        changes.push({ type: 'added', key, to: newValue });
                    } else if (JSON.stringify(oldValue) !== JSON.stringify(newValue)) {
                        changes.push({ type: 'changed', key, from: oldValue, to: newValue });
                    }
                    
                    liveData[key] = newValue;
                }
                break;
            }
            
            // ═══════════════════════════════════════════════════════════════════
            // DEEP MERGE — Recursive merge for nested objects
            // ═══════════════════════════════════════════════════════════════════
            case 'deep': {
                this._deepMerge(liveData, sourceData, changes, '', RUNTIME_KEYS);
                break;
            }
            
            default:
                console.warn(`Unknown merge strategy: ${strategy}`);
        }
        
        // Update entity direct properties
        if (liveData.name) entity.name = liveData.name;
        if (liveData.description) entity.description = liveData.description;
        
        // Handle special collections
        this._updateCollections(entity, liveData);
        
        return { changes };
    }
    
    /**
     * Deep merge two objects
     */
    _deepMerge(target, source, changes, path, skipKeys) {
        for (const [key, value] of Object.entries(source)) {
            const fullPath = path ? `${path}.${key}` : key;
            
            if (skipKeys.includes(key)) continue;
            
            if (value && typeof value === 'object' && !Array.isArray(value)) {
                // Nested object — recurse
                if (!target[key] || typeof target[key] !== 'object') {
                    target[key] = {};
                    changes.push({ type: 'added', key: fullPath, to: {} });
                }
                this._deepMerge(target[key], value, changes, fullPath, skipKeys);
            } else {
                // Primitive or array — replace
                const oldValue = target[key];
                const newValue = this._deepClone(value);
                
                if (JSON.stringify(oldValue) !== JSON.stringify(newValue)) {
                    changes.push({ 
                        type: oldValue === undefined ? 'added' : 'changed', 
                        key: fullPath, 
                        from: oldValue, 
                        to: newValue 
                    });
                    target[key] = newValue;
                }
            }
        }
    }
    
    /**
     * Deep clone a value
     */
    _deepClone(value) {
        if (value === null || typeof value !== 'object') {
            return value;
        }
        if (Array.isArray(value)) {
            return value.map(v => this._deepClone(v));
        }
        const clone = {};
        for (const [k, v] of Object.entries(value)) {
            clone[k] = this._deepClone(v);
        }
        return clone;
    }
    
    /**
     * Update special entity collections (exits, contents, etc.)
     */
    _updateCollections(entity, data) {
        // Exits (Map)
        if (data.exits && entity.exits instanceof Map) {
            entity.exits.clear();
            for (const [dir, target] of Object.entries(data.exits)) {
                entity.exits.set(dir, target);
            }
        }
        
        // Contents (Set or Array)
        if (data.contents) {
            if (entity.contents instanceof Set) {
                entity.contents.clear();
                for (const item of data.contents) {
                    entity.contents.add(item);
                }
            } else if (Array.isArray(entity.contents)) {
                entity.contents.length = 0;
                entity.contents.push(...data.contents);
            }
        }
        
        // Characters in room (Set or Array)
        if (data.characters) {
            if (entity.characters instanceof Set) {
                entity.characters.clear();
                for (const char of data.characters) {
                    entity.characters.add(char);
                }
            } else if (Array.isArray(entity.characters)) {
                entity.characters.length = 0;
                entity.characters.push(...data.characters);
            }
        }
        
        // Inventory (Array)
        if (data.inventory && Array.isArray(entity.inventory)) {
            entity.inventory.length = 0;
            entity.inventory.push(...data.inventory);
        }
    }
    
    /**
     * Parse source text (YAML or JSON)
     * Handles both commented YAML and minimized JSON
     */
    async _parseSource(text) {
        const trimmed = text.trim();
        
        // Try JSON first (faster, no comments)
        if (trimmed.startsWith('{') || trimmed.startsWith('[')) {
            try {
                return JSON.parse(trimmed);
            } catch (e) {
                // Not valid JSON, try YAML
            }
        }
        
        // Try YAML
        return this._parseYaml(text);
    }
    
    /**
     * Parse YAML text to object
     * 
     * Preferred: eemeli/yaml — supports comment round-tripping!
     * Fallback: js-yaml — fast, no comments
     * Last resort: simple parser
     * 
     * CDN options:
     *   <script src="https://cdn.jsdelivr.net/npm/yaml@2/browser/index.min.js"></script>
     *   <script src="https://cdn.jsdelivr.net/npm/js-yaml@4/dist/js-yaml.min.js"></script>
     */
    async _parseYaml(yamlText) {
        // Preferred: eemeli/yaml (preserves comments!)
        // npm: yaml, global: YAML
        if (typeof YAML !== 'undefined') {
            return YAML.parse(yamlText);
        }
        
        // window.YAML (browser bundle)
        if (typeof window !== 'undefined' && window.YAML) {
            return window.YAML.parse(yamlText);
        }
        
        // Fallback: js-yaml (no comments, but fast)
        if (typeof jsyaml !== 'undefined') {
            return jsyaml.load(yamlText);
        }
        
        if (typeof window !== 'undefined' && window.jsyaml) {
            return window.jsyaml.load(yamlText);
        }
        
        // Last resort: simple parser
        return this._simpleYamlParse(yamlText);
    }
    
    /**
     * Stringify object to YAML (with comment preservation if possible)
     */
    _stringifyYaml(obj, options = {}) {
        // Preferred: eemeli/yaml (preserves comments!)
        if (typeof YAML !== 'undefined') {
            return YAML.stringify(obj, options);
        }
        
        if (typeof window !== 'undefined' && window.YAML) {
            return window.YAML.stringify(obj, options);
        }
        
        // Fallback: js-yaml
        if (typeof jsyaml !== 'undefined') {
            return jsyaml.dump(obj, options);
        }
        
        if (typeof window !== 'undefined' && window.jsyaml) {
            return window.jsyaml.dump(obj, options);
        }
        
        // Last resort: JSON (not ideal but works)
        return JSON.stringify(obj, null, 2);
    }
    
    /**
     * Set status message
     */
    _setStatus(message, type = 'info') {
        const statusEl = this.container?.querySelector('.source-viewer-status');
        if (statusEl) {
            statusEl.textContent = message;
            statusEl.className = `source-viewer-status status-${type}`;
        }
    }
    
    /**
     * Switch between source, live, and split modes
     */
    _switchMode(mode) {
        this.viewMode = mode;
        
        // Update mode button states
        this.container.querySelectorAll('.source-viewer-mode button').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === mode);
        });
        
        // Update pane visibility
        this.container.classList.remove('mode-source', 'mode-live', 'mode-split');
        this.container.classList.add(`mode-${mode}`);
        
        switch (mode) {
            case 'source':
                this.sourcePane.style.display = 'block';
                this.livePane.style.display = 'none';
                break;
            case 'live':
                this.sourcePane.style.display = 'none';
                this.livePane.style.display = 'block';
                this._refreshLiveState();
                break;
            case 'split':
                this.sourcePane.style.display = 'block';
                this.livePane.style.display = 'block';
                this._refreshLiveState();
                break;
        }
    }
    
    /**
     * Refresh the live state display
     */
    _refreshLiveState() {
        if (!this.engine || !this.currentEntity) {
            this.liveStateJson.textContent = '// No live state available\n// (Engine not connected)';
            return;
        }
        
        const entity = this.currentEntity;
        const state = this._getEntityState(entity);
        
        // Update header
        this.container.querySelector('.live-state-type').textContent = state._type || 'Entity';
        this.container.querySelector('.live-state-id').textContent = entity.id;
        
        // Pretty print JSON with syntax highlighting
        this.liveStateJson.innerHTML = this._syntaxHighlightJSON(state);
        
        // Show diff if we have source
        if (this.sourceState) {
            const changes = this._diffStates(this.sourceState, state);
            if (changes.length > 0) {
                this.container.querySelector('.live-state-diff').style.display = 'block';
                this.liveStateChanges.innerHTML = this._formatChanges(changes);
            } else {
                this.container.querySelector('.live-state-diff').style.display = 'none';
            }
        }
        
        // Update status
        this.container.querySelector('.source-viewer-status').textContent = 
            `Updated: ${new Date().toLocaleTimeString()}`;
    }
    
    /**
     * Get serializable state from an entity
     */
    _getEntityState(entity) {
        if (!entity) return {};
        
        // Build state object excluding circular refs
        const state = {
            _type: entity.constructor?.name || 'Entity',
            id: entity.id,
            name: entity.name
        };
        
        // Copy data properties
        if (entity.data) {
            for (const [key, value] of Object.entries(entity.data)) {
                if (key.startsWith('_')) continue; // Skip internal
                if (typeof value === 'function') continue;
                if (value instanceof Node) continue; // Skip DOM
                
                try {
                    // Test if serializable
                    JSON.stringify(value);
                    state[key] = value;
                } catch (e) {
                    state[key] = `[${typeof value}]`;
                }
            }
        }
        
        // Special handling for rooms
        if (entity.exits) {
            state.exits = {};
            entity.exits.forEach((target, direction) => {
                state.exits[direction] = typeof target === 'object' ? target.id : target;
            });
        }
        
        // Special handling for characters
        if (entity.inventory) {
            state.inventory = Array.from(entity.inventory).map(item => 
                typeof item === 'object' ? item.id : item
            );
        }
        
        // Contents (items in room)
        if (entity.contents) {
            state.contents = Array.from(entity.contents).map(item =>
                typeof item === 'object' ? item.id : item
            );
        }
        
        // Characters in room
        if (entity.characters) {
            state.characters = Array.from(entity.characters).map(char =>
                typeof char === 'object' ? char.id : char
            );
        }
        
        return state;
    }
    
    /**
     * Simple JSON syntax highlighting
     */
    _syntaxHighlightJSON(obj) {
        const json = JSON.stringify(obj, null, 2);
        return json
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?)/g, (match) => {
                let cls = 'json-string';
                if (/:$/.test(match)) {
                    cls = 'json-key';
                }
                return `<span class="${cls}">${match}</span>`;
            })
            .replace(/\b(true|false)\b/g, '<span class="json-boolean">$1</span>')
            .replace(/\b(null)\b/g, '<span class="json-null">$1</span>')
            .replace(/\b(-?\d+\.?\d*)\b/g, '<span class="json-number">$1</span>');
    }
    
    /**
     * Compare source state to live state
     */
    _diffStates(source, live) {
        const changes = [];
        
        // Check for changed/added values
        for (const key of Object.keys(live)) {
            if (key.startsWith('_')) continue;
            
            const sourceVal = source[key];
            const liveVal = live[key];
            
            if (sourceVal === undefined) {
                changes.push({ type: 'added', key, value: liveVal });
            } else if (JSON.stringify(sourceVal) !== JSON.stringify(liveVal)) {
                changes.push({ type: 'changed', key, from: sourceVal, to: liveVal });
            }
        }
        
        // Check for removed values
        for (const key of Object.keys(source)) {
            if (key.startsWith('_')) continue;
            if (live[key] === undefined) {
                changes.push({ type: 'removed', key, value: source[key] });
            }
        }
        
        return changes;
    }
    
    /**
     * Format diff changes for display
     */
    _formatChanges(changes) {
        return changes.map(change => {
            switch (change.type) {
                case 'added':
                    return `<span class="diff-added">+ ${change.key}: ${JSON.stringify(change.value)}</span>`;
                case 'removed':
                    return `<span class="diff-removed">- ${change.key}: ${JSON.stringify(change.value)}</span>`;
                case 'changed':
                    return `<span class="diff-changed">~ ${change.key}: ${JSON.stringify(change.from)} → ${JSON.stringify(change.to)}</span>`;
                default:
                    return '';
            }
        }).join('\n');
    }
    
    /**
     * Open the viewer for an object
     * @param {string|object} target - moollm:// URL, path, or entity object
     * @param {string} view - 'room', 'readme', 'tree', 'edit'
     */
    open(target, view = 'room') {
        if (!this.container) {
            this.init();
        }
        
        // Resolve target to path and entity
        let objectPath;
        if (typeof target === 'string') {
            objectPath = target;
            // Try to find entity in engine
            this.currentEntity = this._findEntity(target);
        } else if (target && typeof target === 'object') {
            // Direct entity reference
            this.currentEntity = target;
            objectPath = target.data?.source_path || target.id;
        } else {
            console.error('Invalid target:', target);
            return;
        }
        
        this.currentPath = objectPath;
        this.currentView = view;
        
        // Parse path to get repo, path, and git ref
        const parsed = this.namespace.parse(objectPath);
        
        const urls = this.namespace.getObjectURLs(objectPath);
        if (!urls) {
            console.error('Could not resolve URLs for:', objectPath);
            return;
        }
        
        this.currentURLs = urls;
        this.currentGitRef = parsed.gitRef;
        
        // Update path display
        this.container.querySelector('.source-viewer-path').textContent = urls.moollm;
        
        // Update git ref badge
        const gitRefEl = this.container.querySelector('.source-viewer-gitref');
        if (gitRefEl && this.currentGitRef) {
            const refIcon = this.currentGitRef.type === 'commit' ? '📌' :
                           this.currentGitRef.type === 'tag' ? '🏷️' : '🌿';
            gitRefEl.textContent = `${refIcon} ${this.currentGitRef.label}`;
            gitRefEl.className = `source-viewer-gitref ref-${this.currentGitRef.type}`;
            gitRefEl.title = `${this.currentGitRef.type}: ${this.currentGitRef.ref}`;
        }
        
        // Fetch source state for diff comparison
        this._fetchSourceState(urls.rawRoom);
        
        // Load appropriate view
        this._switchView(view);
        
        // Update live state if in live/split mode
        if (this.viewMode === 'live' || this.viewMode === 'split') {
            this._refreshLiveState();
        }
        
        // Show panel
        this.container.classList.remove('closed');
        this.container.classList.add('open');
        this.isOpen = true;
    }
    
    /**
     * Find entity in engine by path/id
     */
    _findEntity(pathOrId) {
        if (!this.engine) return null;
        
        const world = this.engine.world;
        if (!world) return null;
        
        // Try direct lookup by id
        const id = pathOrId.split('/').pop(); // Get last segment as id
        
        return world.rooms?.get(id) ||
               world.objects?.get(id) ||
               world.characters?.get(id) ||
               world.rooms?.get(pathOrId) ||
               world.objects?.get(pathOrId) ||
               world.characters?.get(pathOrId);
    }
    
    /**
     * Fetch original source state (YAML→JSON) for diff
     */
    async _fetchSourceState(rawUrl) {
        this.sourceState = null;
        
        if (!rawUrl) return;
        
        try {
            const response = await fetch(rawUrl);
            if (!response.ok) return;
            
            const yaml = await response.text();
            // Simple YAML-to-JSON (for basic cases)
            // In production, use a proper YAML parser
            this.sourceState = this._simpleYamlParse(yaml);
        } catch (e) {
            console.warn('Could not fetch source:', e);
        }
    }
    
    /**
     * Very simple YAML parser for basic display
     * (Not a full parser - just for common cases)
     */
    _simpleYamlParse(yaml) {
        // This is a stub - in production use js-yaml or similar
        // For now, just show raw text
        return { _raw: yaml };
    }
    
    _switchView(view) {
        if (!this.currentURLs) return;
        
        // Update tab active state
        this.container.querySelectorAll('.source-viewer-tabs button').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.view === view);
        });
        
        // Load URL into iframe
        let url;
        switch (view) {
            case 'room':
                url = this.currentURLs.room;
                break;
            case 'readme':
                url = this.currentURLs.readme;
                break;
            case 'tree':
                url = this.currentURLs.tree;
                break;
            case 'edit':
                url = this.currentURLs.edit;
                break;
            case 'history':
                url = this.currentURLs.history;
                break;
            default:
                url = this.currentURLs.tree;
        }
        
        if (url) {
            this.frame.src = url;
        }
        
        this.currentView = view;
    }
    
    /**
     * Close the viewer
     */
    close() {
        if (this.container) {
            this.container.classList.remove('open');
            this.container.classList.add('closed');
            this.frame.src = 'about:blank';
        }
        this.isOpen = false;
    }
    
    /**
     * Toggle the viewer
     */
    toggle(objectPath, view = 'room') {
        if (this.isOpen && this.currentPath === objectPath) {
            this.close();
        } else {
            this.open(objectPath, view);
        }
    }
    
    /**
     * Load styles — either from external CSS file or inline fallback
     */
    _injectStyles() {
        if (document.getElementById('source-viewer-styles')) return;
        
        // Try to load external CSS file
        const link = document.createElement('link');
        link.id = 'source-viewer-styles';
        link.rel = 'stylesheet';
        
        // Determine CSS path relative to this script
        const scripts = document.querySelectorAll('script[src*="source-viewer"]');
        let basePath = '';
        if (scripts.length > 0) {
            const scriptSrc = scripts[scripts.length - 1].src;
            basePath = scriptSrc.substring(0, scriptSrc.lastIndexOf('/') + 1);
        }
        
        link.href = basePath + 'source-viewer.css';
        link.onerror = () => this._injectInlineStyles();
        document.head.appendChild(link);
    }
    
    /**
     * Fallback: inject minimal inline styles if CSS file fails to load
     */
    _injectInlineStyles() {
        const style = document.createElement('style');
        style.id = 'source-viewer-styles-inline';
        style.textContent = `
            /* Minimal fallback styles */
            .source-viewer {
                position: fixed; top: 0; right: 0; width: 50%; height: 100vh;
                background: #1e1e2e; border-left: 2px solid #313244;
                display: flex; flex-direction: column; z-index: 9999;
                transition: transform 0.3s ease; font-family: system-ui, sans-serif;
            }
            .source-viewer.closed { transform: translateX(100%); }
            .source-viewer.open { transform: translateX(0); }
            .source-viewer-header { display: flex; align-items: center; padding: 10px 15px; background: #313244; }
            .source-viewer-title { font-weight: bold; color: #cdd6f4; margin-right: 15px; }
            .source-viewer-mode { display: flex; gap: 3px; margin-right: auto; }
            .source-viewer-mode button { background: #45475a; border: none; padding: 6px 12px; border-radius: 4px; color: #bac2de; cursor: pointer; }
            .source-viewer-mode button.active { background: #a6e3a1; color: #1e1e2e; }
            .source-viewer-tabs { display: flex; gap: 5px; padding: 8px 15px; background: #1e1e2e; }
            .source-viewer-tabs button { background: #45475a; border: none; padding: 5px 10px; border-radius: 3px; color: #bac2de; cursor: pointer; }
            .source-viewer-tabs button.active { background: #89b4fa; color: #1e1e2e; }
            .source-viewer-close { background: none; border: none; color: #f38ba8; font-size: 20px; cursor: pointer; }
            .source-viewer-content { flex: 1; display: flex; overflow: hidden; }
            .source-viewer-pane { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
            .source-viewer-frame { flex: 1; border: none; background: white; }
            .live-pane { background: #1e1e2e; overflow: auto; }
            .live-state-header { display: flex; align-items: center; gap: 10px; padding: 10px 15px; background: #313244; }
            .live-state-type { color: #cba6f7; font-weight: bold; }
            .live-state-id { color: #89b4fa; font-family: monospace; }
            .live-state-json { margin: 0; padding: 15px; font-family: monospace; font-size: 12px; color: #cdd6f4; overflow: auto; flex: 1; }
            .source-viewer-info { padding: 8px 15px; background: #313244; display: flex; justify-content: space-between; }
            .source-viewer-path { font-size: 11px; color: #a6adc8; font-family: monospace; }
            .json-key { color: #89b4fa; }
            .json-string { color: #a6e3a1; }
            .json-number { color: #fab387; }
            .json-boolean { color: #cba6f7; }
            .json-null { color: #f38ba8; }
            .diff-added { color: #a6e3a1; display: block; }
            .diff-removed { color: #f38ba8; display: block; }
            .diff-changed { color: #f9e2af; display: block; }
        `;
        document.head.appendChild(style);
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// PIE MENU INTEGRATION — View Source as menu item
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Create a "View Source" pie menu entry
 * 
 * The pie menu for any object includes:
 * - Cardinal directions for exits (N, S, E, W, etc.)
 * - Center: "View Source" (opens overlay)
 * 
 * @param {Entity} entity - The entity to view
 * @param {SourceViewer} viewer - The source viewer instance
 */
function createViewSourceMenuItem(entity, viewer) {
    return {
        label: '👁 View Source',
        icon: '👁',
        action: () => {
            // Use entity's path as the moollm:// ID
            const path = entity.data?.source_path || 
                         entity.data?.path || 
                         entity.id;
            viewer.open(path, 'room');
        },
        submenu: [
            { label: 'ROOM.yml', action: () => viewer.open(entity.id, 'room') },
            { label: 'README.md', action: () => viewer.open(entity.id, 'readme') },
            { label: 'All Files', action: () => viewer.open(entity.id, 'tree') },
            { label: 'Edit on GitHub', action: () => viewer.open(entity.id, 'edit') },
            { label: 'History', action: () => viewer.open(entity.id, 'history') }
        ]
    };
}

// ═══════════════════════════════════════════════════════════════════════════════
// ADVENTURE INTEGRATION — Add View Source to engine
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Extend an adventure engine with View Source capability
 * 
 * PSIBER Space Deck — The live object inspector!
 * 
 * Three modes:
 * - Source: View YAML on GitHub
 * - Live: View runtime JSON state
 * - Split: Side-by-side comparison (WHAT CHANGED?)
 */
function addViewSourceToEngine(engine, options = {}) {
    // Create namespace and viewer
    engine.namespace = new MoollmNamespace(options.namespace);
    engine.sourceViewer = new SourceViewer({
        namespace: options.namespace,
        position: options.viewerPosition || 'right',
        engine: engine  // Pass engine reference for live state
    });
    
    // Initialize viewer when DOM is ready
    if (engine.ui?.container) {
        engine.sourceViewer.init(document.body);
    }
    
    // Also set engine reference after init
    engine.sourceViewer.setEngine(engine);
    
    // Add viewSource command
    engine.viewSource = function(target = null) {
        let path;
        
        if (!target) {
            // View current room
            path = this.world.room?.data?.source_path || this.world.room?.id;
        } else if (typeof target === 'string') {
            // View by path/id
            const entity = this.world.objects.get(target) || 
                          this.world.characters.get(target) ||
                          this.world.rooms.get(target);
            path = entity?.data?.source_path || entity?.id || target;
        } else {
            // View entity directly
            path = target.data?.source_path || target.id;
        }
        
        if (path) {
            this.sourceViewer.open(path, 'room');
        } else {
            console.warn('No source path found for target');
        }
    };
    
    // Add inspect command (for live state)
    engine.inspect = function(target = null) {
        let entity;
        
        if (!target) {
            // Inspect current room
            entity = this.world.room;
        } else if (typeof target === 'string') {
            // Find by id/path
            entity = this.world.objects.get(target) ||
                    this.world.characters.get(target) ||
                    this.world.rooms.get(target);
        } else {
            entity = target;
        }
        
        if (entity) {
            this.sourceViewer.open(entity, 'room');
            this.sourceViewer._switchMode('live');
        }
    };
    
    // Add to command parser
    const originalCommand = engine.command.bind(engine);
    engine.command = function(input) {
        const cmd = input.trim().toLowerCase();
        
        // Handle view source commands
        if (cmd === 'source' || cmd === 'view source' || cmd === 'src') {
            this.viewSource();
            return { success: true, message: '📄 Opening source viewer...' };
        }
        
        if (cmd.startsWith('source ') || cmd.startsWith('src ')) {
            const target = cmd.replace(/^(source|src)\s+/, '');
            this.viewSource(target);
            return { success: true, message: `📄 Opening source for: ${target}` };
        }
        
        // Handle inspect commands (live state)
        if (cmd === 'inspect' || cmd === 'live') {
            this.inspect();
            return { success: true, message: '⚡ Opening live state inspector...' };
        }
        
        if (cmd.startsWith('inspect ') || cmd.startsWith('live ')) {
            const target = cmd.replace(/^(inspect|live)\s+/, '');
            this.inspect(target);
            return { success: true, message: `⚡ Inspecting: ${target}` };
        }
        
        // Handle split view command
        if (cmd === 'split' || cmd === 'diff') {
            this.viewSource();
            this.sourceViewer._switchMode('split');
            return { success: true, message: '◧ Split view: Source vs Live' };
        }
        
        // Handle revert command (alias for pull replace)
        // Supports fragments: revert path/to/file.yml#nose/left_nostril
        if (cmd === 'revert') {
            if (this.sourceViewer.currentEntity) {
                this.sourceViewer._revertToSource();
                return { success: true, message: '⏪ Reverting to source...' };
            }
            return { success: false, message: 'Open an entity with "inspect" first' };
        }
        
        if (cmd.startsWith('revert ')) {
            const target = cmd.replace(/^revert\s+/, '');
            
            // Check for fragment (#path/to/subtree)
            if (target.includes('#')) {
                if (!this.sourceViewer.currentEntity) {
                    return { success: false, message: 'Open an entity with "inspect" first' };
                }
                
                const fragment = target.split('#')[1];
                this.sourceViewer.pullFragment(target, 'replace');
                return { success: true, message: `⏪ Reverting #${fragment} to source...` };
            }
            
            // No fragment — revert whole entity
            this.inspect(target);
            setTimeout(() => this.sourceViewer._revertToSource(), 100);
            return { success: true, message: `⏪ Reverting ${target} to source...` };
        }
        
        // ═══════════════════════════════════════════════════════════════════
        // PULL COMMANDS — Different merge strategies
        // ═══════════════════════════════════════════════════════════════════
        
        // pull                    — Same as revert (replace)
        // pull replace            — Full overwrite from source
        // pull merge              — Source wins conflicts
        // pull underlay           — Live wins, source fills gaps
        // pull deep               — Deep recursive merge
        // pull pick key1 key2...  — Pull specific keys only
        
        if (cmd === 'pull' || cmd === 'pull replace') {
            if (!this.sourceViewer.currentEntity) {
                return { success: false, message: 'Open an entity with "inspect" first' };
            }
            this.sourceViewer.pullSource('replace');
            return { success: true, message: '⏬ Pull replace: full overwrite from source' };
        }
        
        if (cmd === 'pull merge') {
            if (!this.sourceViewer.currentEntity) {
                return { success: false, message: 'Open an entity with "inspect" first' };
            }
            this.sourceViewer.pullSource('merge');
            return { success: true, message: '⏬ Pull merge: source wins conflicts' };
        }
        
        if (cmd === 'pull underlay') {
            if (!this.sourceViewer.currentEntity) {
                return { success: false, message: 'Open an entity with "inspect" first' };
            }
            this.sourceViewer.pullSource('underlay');
            return { success: true, message: '⏬ Pull underlay: live wins, source fills gaps' };
        }
        
        if (cmd === 'pull deep') {
            if (!this.sourceViewer.currentEntity) {
                return { success: false, message: 'Open an entity with "inspect" first' };
            }
            this.sourceViewer.pullSource('deep');
            return { success: true, message: '⏬ Pull deep: recursive merge' };
        }
        
        if (cmd.startsWith('pull pick ')) {
            if (!this.sourceViewer.currentEntity) {
                return { success: false, message: 'Open an entity with "inspect" first' };
            }
            const keys = cmd.replace(/^pull pick\s+/, '').split(/\s+/);
            this.sourceViewer.pullSource('pick', { keys });
            return { success: true, message: `⏬ Pull pick: ${keys.join(', ')}` };
        }
        
        // Help for pull
        if (cmd === 'pull help' || cmd === 'pull ?') {
            return {
                success: true,
                message: `⏬ Pull Strategies:

  pull             Full overwrite (same as revert)
  pull replace     Full overwrite from source
  pull merge       Source wins conflicts, keeps live-only keys
  pull underlay    Live wins conflicts, source fills gaps  
  pull deep        Recursive merge of nested objects
  pull pick K1 K2  Pull only specific keys

FRAGMENT SYNTAX — Revert just a subtree:
  revert #path/to/key           Revert only that key
  revert file.yml#nose/left     Revert just nose.left

Examples:
  > inspect room
  > pull merge                    Merge source, source wins
  > pull underlay                 Fill in missing from source
  > pull pick description exits   Pull only those keys
  > revert #nose/left_nostril    Clear Don's snotty nostril!
  > revert head.yml#nose         Revert whole nose subtree`
            };
        }
        
        // Handle mount command (set git ref for path)
        if (cmd.startsWith('mount ')) {
            // mount path@ref or mount path ref
            const match = cmd.match(/^mount\s+(\S+?)(?:@(\S+)|\s+(\S+))?$/);
            if (match) {
                const path = match[1];
                const ref = match[2] || match[3] || 'main';
                this.namespace.mount(this.namespace.currentRepo, path, ref);
                return { success: true, message: `📌 Mounted ${path} @ ${ref}` };
            }
            return { success: false, message: 'Usage: mount path@ref or mount path ref' };
        }
        
        // List mounts
        if (cmd === 'mounts') {
            const mounts = this.namespace.listMounts();
            if (mounts.length === 0) {
                return { success: true, message: 'No custom mounts. Using default branches.' };
            }
            const list = mounts.map(m => 
                `  ${m.path} → ${m.ref} (${m.type})`
            ).join('\n');
            return { success: true, message: `📌 Git Mounts:\n${list}` };
        }
        
        // Pass to original handler
        return originalCommand(input);
    };
    
    // Add keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Ctrl/Cmd + U: View Source
        if ((e.ctrlKey || e.metaKey) && e.key === 'u') {
            e.preventDefault();
            engine.sourceViewer.toggle(
                engine.world.room?.data?.source_path || engine.world.room?.id
            );
        }
        
        // Ctrl/Cmd + I: Inspect (live state)
        if ((e.ctrlKey || e.metaKey) && e.key === 'i' && !e.shiftKey) {
            e.preventDefault();
            engine.inspect();
        }
        
        // Ctrl/Cmd + Shift + I: Split view (source + live)
        if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'I') {
            e.preventDefault();
            engine.viewSource();
            engine.sourceViewer._switchMode('split');
        }
    });
    
    return engine;
}

// ═══════════════════════════════════════════════════════════════════════════════
// COMPILER INTEGRATION — Add source paths during compilation
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Metadata to add to compiled adventure JSON
 * 
 * The adventure compiler should include:
 * 
 * {
 *   "name": "NO AI TOWER",
 *   "_meta": {
 *     "source": {
 *       "repo": "moollm",
 *       "github": "leela-ai/moollm",
 *       "branch": "main",
 *       "root": "examples/adventure-4/street/lane-neverending/no-ai-tower"
 *     }
 *   },
 *   "rooms": [
 *     {
 *       "id": "lobby",
 *       "source_path": "examples/adventure-4/street/lane-neverending/no-ai-tower/lobby",
 *       ...
 *     }
 *   ]
 * }
 */

const COMPILER_SCHEMA = {
    _meta: {
        source: {
            repo: "string — short name (moollm, central, etc.)",
            github: "string — owner/repo",
            branch: "string — branch name",
            root: "string — path to adventure root",
            compiled_at: "ISO timestamp",
            git_sha: "string — optional commit SHA"
        }
    },
    rooms: {
        source_path: "string — path relative to repo root (no extension)",
        source_file: "string — specific file (ROOM.yml)"
    }
};

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const SOURCE_VIEWER_EXPORTS = {
    MoollmNamespace,
    SourceViewer,
    createViewSourceMenuItem,
    addViewSourceToEngine,
    COMPILER_SCHEMA
};

// Browser: attach to window
if (typeof window !== 'undefined') {
    window.MoollmNamespace = MoollmNamespace;
    window.SourceViewer = SourceViewer;
    window.addViewSourceToEngine = addViewSourceToEngine;
    
    // Merge into Adventure namespace if exists
    if (window.Adventure) {
        Object.assign(window.Adventure, SOURCE_VIEWER_EXPORTS);
    }
}

// Node.js CommonJS
if (typeof module !== 'undefined' && module.exports) {
    module.exports = SOURCE_VIEWER_EXPORTS;
}
