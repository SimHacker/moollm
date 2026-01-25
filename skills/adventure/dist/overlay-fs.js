/**
 * overlay-fs.js — Layered Overlay Filesystem for MOOLLM
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * CONCEPT: Multiple layers stacked on top of each other
 * 
 *   ┌────────────────────────────────────────────────────────────────────┐
 *   │  RUNTIME LAYER  (in-memory changes during simulation)              │
 *   ├────────────────────────────────────────────────────────────────────┤
 *   │  LOCAL LAYER    (sparse tree of your edits, uncommitted)           │
 *   ├────────────────────────────────────────────────────────────────────┤
 *   │  GIT LAYER      (mounted git repo at specific ref)                 │
 *   └────────────────────────────────────────────────────────────────────┘
 * 
 * Reading: Start from top, fall through to lower layers
 * Writing: Always goes to the top writable layer
 * 
 * MOUNT POINTS:
 *   /                           → git: SimHacker/moollm@main
 *   /skills/custom              → local: ~/my-skills/
 *   /examples/adventure-4       → git: SimHacker/moollm@v2.0.0
 *   /vendor/acme                → git: acme-corp/tools@develop
 * 
 * PSIBER VIEW: See any layer, any combination, or diffs between layers
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ═══════════════════════════════════════════════════════════════════════════════
// LAYER TYPES
// ═══════════════════════════════════════════════════════════════════════════════

const LayerType = {
    GIT: 'git',           // Remote git repo (read-only, cached)
    LOCAL: 'local',       // Local filesystem overlay (read-write)
    RUNTIME: 'runtime',   // In-memory runtime state (read-write, ephemeral)
    MEMORY: 'memory'      // Pure in-memory (for testing)
};

// ═══════════════════════════════════════════════════════════════════════════════
// LAYER — Single layer in the overlay stack
// ═══════════════════════════════════════════════════════════════════════════════

class Layer {
    constructor(config) {
        this.id = config.id || crypto.randomUUID?.() || Date.now().toString();
        this.type = config.type || LayerType.MEMORY;
        this.name = config.name || this.type;
        this.priority = config.priority || 0;  // Higher = on top
        this.writable = config.writable ?? (this.type !== LayerType.GIT);
        
        // For git layers
        this.source = config.source || null;  // { platform, owner, repo, ref }
        
        // For local layers
        this.basePath = config.basePath || null;  // Local filesystem path
        
        // Sparse storage (path → data)
        // Only stores what's different from lower layers
        this.data = new Map();
        
        // Deleted markers (path → true)
        // Marks files as "deleted in this layer" (whiteout)
        this.deleted = new Set();
        
        // Metadata
        this.created = new Date().toISOString();
        this.modified = this.created;
    }
    
    /**
     * Check if this layer has data for a path
     */
    has(path) {
        return this.data.has(path) || this.deleted.has(path);
    }
    
    /**
     * Get data from this layer (or undefined if not present)
     */
    get(path) {
        if (this.deleted.has(path)) {
            return { _deleted: true };  // Whiteout marker
        }
        return this.data.get(path);
    }
    
    /**
     * Set data in this layer
     */
    set(path, value) {
        if (!this.writable) {
            throw new Error(`Layer "${this.name}" is read-only`);
        }
        this.deleted.delete(path);  // Remove whiteout if exists
        this.data.set(path, value);
        this.modified = new Date().toISOString();
    }
    
    /**
     * Delete from this layer (creates whiteout)
     */
    delete(path) {
        if (!this.writable) {
            throw new Error(`Layer "${this.name}" is read-only`);
        }
        this.data.delete(path);
        this.deleted.add(path);
        this.modified = new Date().toISOString();
    }
    
    /**
     * List all paths in this layer (data + whiteouts)
     */
    paths() {
        return new Set([...this.data.keys(), ...this.deleted]);
    }
    
    /**
     * Get layer stats
     */
    stats() {
        return {
            id: this.id,
            type: this.type,
            name: this.name,
            priority: this.priority,
            writable: this.writable,
            entries: this.data.size,
            whiteouts: this.deleted.size,
            created: this.created,
            modified: this.modified
        };
    }
    
    /**
     * Clear all data in this layer
     */
    clear() {
        if (!this.writable) {
            throw new Error(`Layer "${this.name}" is read-only`);
        }
        this.data.clear();
        this.deleted.clear();
        this.modified = new Date().toISOString();
    }
    
    /**
     * Export layer as JSON
     */
    toJSON() {
        return {
            id: this.id,
            type: this.type,
            name: this.name,
            priority: this.priority,
            source: this.source,
            data: Object.fromEntries(this.data),
            deleted: [...this.deleted]
        };
    }
    
    /**
     * Import from JSON
     */
    static fromJSON(json) {
        const layer = new Layer({
            id: json.id,
            type: json.type,
            name: json.name,
            priority: json.priority,
            source: json.source
        });
        
        if (json.data) {
            for (const [path, value] of Object.entries(json.data)) {
                layer.data.set(path, value);
            }
        }
        
        if (json.deleted) {
            for (const path of json.deleted) {
                layer.deleted.add(path);
            }
        }
        
        return layer;
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// MOUNT POINT — Where a source is mounted in the namespace
// ═══════════════════════════════════════════════════════════════════════════════

class MountPoint {
    constructor(config) {
        this.path = config.path || '/';           // Mount path in namespace
        this.source = config.source;              // Source config
        this.layer = config.layer || null;        // Associated layer
        this.options = config.options || {};
        
        // Normalize path
        this.path = '/' + this.path.replace(/^\/+|\/+$/g, '');
    }
    
    /**
     * Check if a path falls under this mount
     */
    contains(targetPath) {
        const normalized = '/' + targetPath.replace(/^\/+|\/+$/g, '');
        return normalized === this.path || normalized.startsWith(this.path + '/');
    }
    
    /**
     * Get relative path within this mount
     */
    relativePath(targetPath) {
        const normalized = '/' + targetPath.replace(/^\/+|\/+$/g, '');
        if (normalized === this.path) return '';
        return normalized.slice(this.path.length + 1);
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// OVERLAY FS — The complete layered filesystem
// ═══════════════════════════════════════════════════════════════════════════════

class OverlayFS {
    constructor(config = {}) {
        // Layers (sorted by priority, highest first)
        this.layers = [];
        
        // Mount points (sorted by path length, longest first)
        this.mounts = [];
        
        // Default layers
        this._createDefaultLayers(config);
        
        // Namespace for URL resolution
        this.namespace = config.namespace || null;
    }
    
    /**
     * Create default layer stack
     */
    _createDefaultLayers(config) {
        // Runtime layer (top, in-memory, ephemeral)
        this.runtimeLayer = new Layer({
            type: LayerType.RUNTIME,
            name: 'runtime',
            priority: 100,
            writable: true
        });
        this.layers.push(this.runtimeLayer);
        
        // Local layer (middle, sparse local changes)
        this.localLayer = new Layer({
            type: LayerType.LOCAL,
            name: 'local',
            priority: 50,
            writable: true,
            basePath: config.localPath
        });
        this.layers.push(this.localLayer);
        
        // Git layer (bottom, read-only)
        if (config.git) {
            this.gitLayer = new Layer({
                type: LayerType.GIT,
                name: 'git',
                priority: 0,
                writable: false,
                source: config.git
            });
            this.layers.push(this.gitLayer);
        }
        
        this._sortLayers();
    }
    
    /**
     * Keep layers sorted by priority (highest first)
     */
    _sortLayers() {
        this.layers.sort((a, b) => b.priority - a.priority);
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // READ OPERATIONS — Fall through layers from top to bottom
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get data at path (unified view across all layers)
     */
    get(path) {
        const normalized = this._normalizePath(path);
        
        // Check each layer from top to bottom
        for (const layer of this.layers) {
            if (layer.has(normalized)) {
                const data = layer.get(normalized);
                if (data?._deleted) {
                    return undefined;  // Whiteout — file doesn't exist
                }
                return data;
            }
        }
        
        return undefined;
    }
    
    /**
     * Check if path exists in any layer
     */
    exists(path) {
        return this.get(path) !== undefined;
    }
    
    /**
     * Get data from a specific layer only
     */
    getFromLayer(path, layerName) {
        const layer = this.layers.find(l => l.name === layerName);
        if (!layer) return undefined;
        return layer.get(this._normalizePath(path));
    }
    
    /**
     * Get merged data with layer info
     */
    getWithLayers(path) {
        const normalized = this._normalizePath(path);
        const result = {
            path: normalized,
            exists: false,
            data: undefined,
            layers: []
        };
        
        // Check each layer
        for (const layer of this.layers) {
            if (layer.has(normalized)) {
                const data = layer.get(normalized);
                result.layers.push({
                    name: layer.name,
                    type: layer.type,
                    data: data,
                    isWhiteout: data?._deleted === true
                });
                
                // First non-whiteout is the visible value
                if (!result.exists && data && !data._deleted) {
                    result.exists = true;
                    result.data = data;
                    result.visibleFrom = layer.name;
                }
            }
        }
        
        return result;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // WRITE OPERATIONS — Always write to topmost writable layer
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Set data (writes to runtime layer by default)
     */
    set(path, data, layerName = 'runtime') {
        const normalized = this._normalizePath(path);
        const layer = this.layers.find(l => l.name === layerName);
        
        if (!layer) {
            throw new Error(`Layer "${layerName}" not found`);
        }
        
        layer.set(normalized, data);
        return this;
    }
    
    /**
     * Delete (creates whiteout in runtime layer)
     */
    delete(path, layerName = 'runtime') {
        const normalized = this._normalizePath(path);
        const layer = this.layers.find(l => l.name === layerName);
        
        if (!layer) {
            throw new Error(`Layer "${layerName}" not found`);
        }
        
        layer.delete(normalized);
        return this;
    }
    
    /**
     * Write changes from runtime to local layer
     */
    persist(path = null) {
        if (path) {
            // Persist single path
            const data = this.runtimeLayer.get(this._normalizePath(path));
            if (data && !data._deleted) {
                this.localLayer.set(path, data);
            } else if (this.runtimeLayer.deleted.has(path)) {
                this.localLayer.delete(path);
            }
        } else {
            // Persist all runtime changes
            for (const [p, data] of this.runtimeLayer.data) {
                this.localLayer.set(p, data);
            }
            for (const p of this.runtimeLayer.deleted) {
                this.localLayer.delete(p);
            }
        }
        return this;
    }
    
    /**
     * Discard runtime changes
     */
    discardRuntime(path = null) {
        if (path) {
            const normalized = this._normalizePath(path);
            this.runtimeLayer.data.delete(normalized);
            this.runtimeLayer.deleted.delete(normalized);
        } else {
            this.runtimeLayer.clear();
        }
        return this;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // DIFF OPERATIONS — Compare layers
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get diff between two layers
     */
    diff(fromLayer, toLayer) {
        const from = this.layers.find(l => l.name === fromLayer);
        const to = this.layers.find(l => l.name === toLayer);
        
        if (!from || !to) {
            throw new Error('Layer not found');
        }
        
        const changes = [];
        const allPaths = new Set([...from.paths(), ...to.paths()]);
        
        for (const path of allPaths) {
            const fromData = from.get(path);
            const toData = to.get(path);
            
            const fromDeleted = fromData?._deleted;
            const toDeleted = toData?._deleted;
            const fromExists = from.has(path) && !fromDeleted;
            const toExists = to.has(path) && !toDeleted;
            
            if (!fromExists && toExists) {
                changes.push({ type: 'added', path, value: toData });
            } else if (fromExists && !toExists) {
                changes.push({ type: 'removed', path, value: fromData });
            } else if (fromExists && toExists) {
                if (JSON.stringify(fromData) !== JSON.stringify(toData)) {
                    changes.push({ type: 'changed', path, from: fromData, to: toData });
                }
            }
        }
        
        return changes;
    }
    
    /**
     * Get all changes in runtime layer compared to base
     */
    getRuntimeChanges() {
        return this.diff('git', 'runtime');
    }
    
    /**
     * Get all local changes compared to git
     */
    getLocalChanges() {
        return this.diff('git', 'local');
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // MOUNT OPERATIONS — Add sources at mount points
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Mount a source at a path
     * @param {string} path - Mount point path
     * @param {object} source - Source config { type, platform, owner, repo, ref, ... }
     */
    mount(path, source) {
        const layer = new Layer({
            type: source.type || LayerType.GIT,
            name: `mount:${path}`,
            priority: 10,  // Between git and local
            writable: source.writable ?? false,
            source
        });
        
        const mount = new MountPoint({
            path,
            source,
            layer
        });
        
        this.layers.push(layer);
        this.mounts.push(mount);
        
        this._sortLayers();
        this._sortMounts();
        
        return mount;
    }
    
    /**
     * Unmount a path
     */
    unmount(path) {
        const normalized = '/' + path.replace(/^\/+|\/+$/g, '');
        
        const mountIndex = this.mounts.findIndex(m => m.path === normalized);
        if (mountIndex === -1) return false;
        
        const mount = this.mounts[mountIndex];
        this.mounts.splice(mountIndex, 1);
        
        // Remove associated layer
        const layerIndex = this.layers.findIndex(l => l === mount.layer);
        if (layerIndex !== -1) {
            this.layers.splice(layerIndex, 1);
        }
        
        return true;
    }
    
    /**
     * Keep mounts sorted by path length (longest first for matching)
     */
    _sortMounts() {
        this.mounts.sort((a, b) => b.path.length - a.path.length);
    }
    
    /**
     * Find mount point for a path
     */
    findMount(path) {
        const normalized = '/' + path.replace(/^\/+|\/+$/g, '');
        return this.mounts.find(m => m.contains(normalized));
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // TREE OPERATIONS — List and traverse
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * List all paths (unified across layers)
     */
    list(prefix = '') {
        const normalized = this._normalizePath(prefix);
        const allPaths = new Set();
        
        // Collect from all layers
        for (const layer of this.layers) {
            for (const path of layer.paths()) {
                if (path.startsWith(normalized)) {
                    allPaths.add(path);
                }
            }
        }
        
        // Filter out whiteouts
        const result = [];
        for (const path of allPaths) {
            if (this.exists(path)) {
                result.push(path);
            }
        }
        
        return result.sort();
    }
    
    /**
     * List with layer info
     */
    listWithLayers(prefix = '') {
        return this.list(prefix).map(path => ({
            path,
            ...this.getWithLayers(path)
        }));
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // UTILITIES
    // ═══════════════════════════════════════════════════════════════════════════
    
    _normalizePath(path) {
        if (!path) return '/';
        return '/' + path.replace(/^\/+|\/+$/g, '');
    }
    
    /**
     * Get stats for all layers
     */
    stats() {
        return {
            layers: this.layers.map(l => l.stats()),
            mounts: this.mounts.map(m => ({
                path: m.path,
                source: m.source
            })),
            totalPaths: this.list().length
        };
    }
    
    /**
     * Export entire state
     */
    toJSON() {
        return {
            layers: this.layers.map(l => l.toJSON()),
            mounts: this.mounts.map(m => ({
                path: m.path,
                source: m.source
            }))
        };
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// PSIBER VIEW — Unified visualization of overlay state
// ═══════════════════════════════════════════════════════════════════════════════

class PsiberView {
    constructor(overlayFS) {
        this.fs = overlayFS;
    }
    
    /**
     * Get unified tree view
     */
    tree(path = '/', options = {}) {
        const showLayers = options.layers ?? true;
        const showDiff = options.diff ?? true;
        
        const paths = this.fs.list(path);
        const result = [];
        
        for (const p of paths) {
            const info = this.fs.getWithLayers(p);
            
            const entry = {
                path: p,
                name: p.split('/').pop(),
                exists: info.exists,
                visibleFrom: info.visibleFrom
            };
            
            if (showLayers) {
                entry.layers = info.layers.filter(l => !l.isWhiteout).map(l => l.name);
            }
            
            if (showDiff && info.layers.length > 1) {
                // Check if modified from base
                const base = info.layers.find(l => l.type === 'git');
                const top = info.layers[0];
                
                if (base && top && base.name !== top.name) {
                    if (JSON.stringify(base.data) !== JSON.stringify(top.data)) {
                        entry.modified = true;
                    }
                }
            }
            
            result.push(entry);
        }
        
        return result;
    }
    
    /**
     * Get formatted tree display
     */
    format(path = '/', options = {}) {
        const tree = this.tree(path, options);
        const lines = [];
        
        for (const entry of tree) {
            let prefix = '';
            let suffix = '';
            
            // Layer indicators
            if (entry.visibleFrom === 'runtime') {
                prefix = '⚡';  // Runtime changes
            } else if (entry.visibleFrom === 'local') {
                prefix = '📝';  // Local changes
            } else if (entry.visibleFrom === 'git') {
                prefix = '📁';  // From git
            }
            
            if (entry.modified) {
                suffix = ' [modified]';
            }
            
            lines.push(`${prefix} ${entry.path}${suffix}`);
        }
        
        return lines.join('\n');
    }
    
    /**
     * Get diff view between git and current state
     */
    diffView() {
        const changes = this.fs.getRuntimeChanges();
        const lines = [];
        
        for (const change of changes) {
            switch (change.type) {
                case 'added':
                    lines.push(`+ ${change.path}`);
                    break;
                case 'removed':
                    lines.push(`- ${change.path}`);
                    break;
                case 'changed':
                    lines.push(`~ ${change.path}`);
                    break;
            }
        }
        
        return lines.join('\n');
    }
}

// ═══════════════════════════════════════════════════════════════════════════════
// EXPORTS
// ═══════════════════════════════════════════════════════════════════════════════

const OVERLAY_FS_EXPORTS = {
    LayerType,
    Layer,
    MountPoint,
    OverlayFS,
    PsiberView
};

// Browser
if (typeof window !== 'undefined') {
    Object.assign(window, OVERLAY_FS_EXPORTS);
}

// Node.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = OVERLAY_FS_EXPORTS;
}
