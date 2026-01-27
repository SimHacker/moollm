/**
 * engine.js — Adventure 4 Engine
 * ═══════════════════════════════════════════════════════════════════════════════
 * 
 * "Sheepy enough, but not too sheepy."
 * 
 * Flat registry, eval'd closures, client-side everything.
 * 
 * ═══════════════════════════════════════════════════════════════════════════════
 */

class MootalEngine {
    constructor() {
        this.registry = {};
        this.config = {};
        this.player = {
            id: 'player',
            location: null,
            inventory: [],
            tags: [],          // Tags for guard checks (staff, cat, dog, etc.)
            locationHistory: [],  // Browser-like location history
            historyIndex: -1,     // Current position in history (-1 = not navigating history)
            // Helper methods for guard closures (parallel-safe signature)
            // Called as subject.hasTag(), subject.hasItem(), etc.
            hasTag: (tag) => this.player.tags?.includes(tag),
            hasItem: (itemId) => {
                return this.player.inventory?.some(item => {
                    const id = typeof item === 'string' ? item : item.id;
                    return id === itemId || id?.endsWith('/' + itemId);
                });
            },
            hasInventoryTag: (tag) => {
                return this.player.inventory?.some(item => {
                    const obj = typeof item === 'string' ? this.get(item) : item;
                    return obj?.tags?.includes(tag);
                });
            }
        };
        this.flags = {};
        this.actions = {};
        this.ui = null;
        
        // Narrator system
        this.narrator = {
            style: 'classic',     // classic, sardonic, dramatic, minimalist, cozy, palm
            voice: false,         // TTS enabled
            verbose: true         // Full vs. brief descriptions
        };
        
        // Transaction ledger — all money transfers logged here
        this.ledger = [];
        this.ledgerEnabled = true;
        
        // ═══════════════════════════════════════════════════════════════════════
        // DUAL CURRENCY SYSTEM — Economic Reward for Good Play
        // ═══════════════════════════════════════════════════════════════════════
        //
        // THE GAME LOOP:
        //   1. Play the adventure → earn gold 🟡
        //   2. Be successful AND kind → build karma 😇
        //   3. Cash out gold → moolah 🪙 at karma-adjusted rate
        //   4. Better karma = your gold is worth MORE moolah!
        //
        // moolah 🪙 = Global systemic currency — the anchor, the stablecoin
        //            (persists across adventures, like petrodollars but less evil)
        //            "Gas" money. Ha ha. The Gastown pun writes itself.
        //
        // gold 🟡   = Adventure-local in-game currency (specific to this world)
        //            Exchange rate to moolah varies based on KARMA.
        //            Better karma = gold is worth more when converting to moolah.
        //
        // One-way relationship: moolah is the parent anchor, gold is the child.
        // Karma affects how much moolah you get for your gold — play well, prosper.
        //
        // Base rate: 10 gold = 1 moolah (at neutral karma)
        // Good karma: fewer gold needed (8, 6, 5...) — reward for kindness!
        // Bad karma: more gold needed (12, 15, 20...) — penalty for villainy
        //
        // This creates an economic incentive to play well, not just win.
        // ═══════════════════════════════════════════════════════════════════════
        
        // ═══════════════════════════════════════════════════════════════════════
        // THE SIN-AND-REPENT CYCLE — Emergent Moral Arbitrage
        // ═══════════════════════════════════════════════════════════════════════
        //
        // A FEATURE, NOT A BUG: Players will discover they can exploit the
        // karma-rate relationship through oscillation:
        //
        //   😇 REPENT PHASE (karma → +100, rate → 5:1)
        //      Do good deeds, help NPCs, complete quests ethically
        //      Convert gold → moolah at premium rate (100g → 20m)
        //
        //   😈 SIN PHASE (karma → -100, rate → 20:1)
        //      Go villain, betray NPCs, burn karma
        //      Convert moolah → gold at "discount" (20m → 400g)
        //
        //   💰 PROFIT: 100 gold → 400 gold (4x multiplier!)
        //
        // This is INTENTIONAL. The mechanic creates:
        //   • Natural story arcs (rise, fall, redemption)
        //   • Forces players to experience both play styles
        //   • Makes karma feel consequential, not cosmetic
        //   • Emergent gameplay — players discover it themselves
        //   • Speedrun potential — "morality%" categories
        //
        // HISTORICAL PRECEDENT: Medieval indulgences. The church literally
        // sold forgiveness. This recreates the economic model of 15th century
        // Catholicism. Martin Luther nailed 95 theses to a door about this.
        // Your players will nail speedrun strats to Discord.
        //
        // BALANCING FRICTION (optional future work):
        //   • NPCs remember your villain phase (reputation persistence)
        //   • Prices remember betrayal (hysteresis)
        //   • Karma velocity tracking (too-fast swings raise suspicion)
        //   • "Witnessed sins" that require specific atonement
        //   • Confession mechanic with real gameplay cost
        //
        // "Forgive me father, for I have arbitraged." 🙏💸
        // ═══════════════════════════════════════════════════════════════════════
        
        // ═══════════════════════════════════════════════════════════════════════
        // THE SAINT-SINNER CARTEL — Multi-Player Money Laundering
        // ═══════════════════════════════════════════════════════════════════════
        //
        // When karma is per-player, two players can coordinate to form an
        // exponential inflation loop:
        //
        //   PLAYER A (Saint 😇)              PLAYER B (Sinner 😈)
        //   karma: +100, rate: 5:1          karma: -100, rate: 20:1
        //
        //   100 gold → 20 moolah ─────────→ 20 moolah → 400 gold
        //                                              ↓
        //   200 gold ←──────── kickback ←──────────────┘ (keeps 200)
        //      ↓
        //   40 moolah ────────────────────→ 40 moolah → 800 gold
        //      ... EXPONENTIAL LOOP ...
        //
        // ATTACK ANALYSIS:
        //   • Solo: must oscillate karma (effort + time)
        //   • Cartel: maintain opposite states permanently (zero downtime)
        //   • Solo: linear profit
        //   • Cartel: EXPONENTIAL profit (doubling each cycle)
        //
        //   | Cycle | Gold In | Moolah | Gold Out | Net Created |
        //   |-------|---------|--------|----------|-------------|
        //   |   1   |   100   |   20   |   400    |    +300     |
        //   |   2   |   200   |   40   |   800    |    +600     |
        //   |   3   |   400   |   80   |  1600    |   +1200     |
        //
        // MONEY LAUNDERING APPLICATION:
        //   Dirty gold (stolen) → Saint converts → "clean" moolah
        //                       → transfer to Sinner → multiplied gold
        //   Origin laundered AND profit generated. Two crimes, one loop.
        //
        // EMERGENT GAMEPLAY THIS CREATES:
        //   • Natural alliances (need a karma buddy)
        //   • Economic classes (cartel insiders vs honest players)
        //   • Detective/cop gameplay (catching launderers)
        //   • Political intrigue (who's in the cartel?)
        //   • Whistleblower mechanics (betray your partner?)
        //
        // POSSIBLE FRICTION (if you want it):
        //   • Transfer tax between players
        //   • Karma contagion — receiving from sinners taints you
        //   • Rate based on transaction karma (average of parties)
        //   • Velocity limits on inter-player transfers
        //   • Public ledger / audit trail for large transactions
        //
        // "In the game of moolah, you either die a saint
        //  or live long enough to see yourself become a banker." 🏦😈
        // ═══════════════════════════════════════════════════════════════════════
        
        this.baseExchangeRate = 10;  // 1 moolah = N gold (at neutral karma)
        this.karma = 0;              // -100 to +100, affects exchange rate
        
        // Economic rubrics — multiple factors that blend to influence exchange rate
        // Each rubric: { value: -100 to +100, weight: 0-1 }
        // Total influence = weighted blend of all rubrics
        this.economicRubrics = {
            karma:       { value: 0, weight: 0.4, desc: 'Kindness & ethics' },
            exploration: { value: 0, weight: 0.2, desc: 'World discovery' },
            completion:  { value: 0, weight: 0.2, desc: 'Quests & goals' },
            social:      { value: 0, weight: 0.1, desc: 'NPC relationships' },
            creativity:  { value: 0, weight: 0.1, desc: 'Novel solutions' }
        };
        
        // Money flow table — aggregated flows between entities
        // Structure: { 'from_id': { 'to_id': { gold: N, moolah: N } } }
        this.moneyFlows = {};
        
        // Event log — all object movements, creations, destructions
        this.eventLog = [];
        this.eventLogEnabled = true;
        
        // Unified action log — ALL actions go through here
        this.actionLog = [];
        this.actionLogEnabled = true;
        
        // Object activity log — arbitrary messages from/about objects
        this.objectLog = [];
        this.objectLogEnabled = true;
        
        // Session start time
        this.sessionStart = Date.now();
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // TIMESTAMP UTILITIES
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Generate timestamp data for logs
     * @returns {object} { epoch, iso, time, elapsed }
     */
    now() {
        const epoch = Date.now();
        const date = new Date(epoch);
        return {
            epoch,                                    // Unix ms timestamp
            iso: date.toISOString(),                  // 2026-01-25T12:30:45.123Z
            time: date.toLocaleTimeString(),          // 5:30:45 AM
            date: date.toLocaleDateString(),          // 1/25/2026
            elapsed: epoch - this.sessionStart        // ms since session start
        };
    }
    
    /**
     * Format elapsed time as human-readable
     * @param {number} ms - Milliseconds
     */
    formatElapsed(ms) {
        if (ms < 1000) return `${ms}ms`;
        if (ms < 60000) return `${(ms/1000).toFixed(1)}s`;
        const mins = Math.floor(ms / 60000);
        const secs = Math.floor((ms % 60000) / 1000);
        return `${mins}m${secs}s`;
    }
    
    /**
     * Render a value as a text bar chart
     * @param {number} value - Value from -100 to +100
     * @param {number} width - Bar width in characters (default 10)
     */
    renderBar(value, width = 10) {
        // Normalize value to 0-1 range (where 0.5 is neutral)
        const normalized = (value + 100) / 200;
        const filled = Math.round(normalized * width);
        const bar = '█'.repeat(filled) + '░'.repeat(width - filled);
        return `[${bar}]`;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // JS COMPILATION — Wrap code body with standard signature, eval, cache
    // Signature: (world, subject, verb, object) => { body }
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Compile JS code body to closure with standard signature.
     * 
     * YAML contains just the body — no wrapper function:
     *   guard_js: "return subject?.hasTag('staff')"
     * 
     * This wraps and evals to:
     *   (world, subject, verb, object) => { return subject?.hasTag('staff') }
     * 
     * Parameters available in code (parallel-safe):
     *   - world: shared game state (this) — NEVER null
     *   - subject: who is acting — OK to be null
     *   - verb: what action — OK to be null
     *   - object: target — OK to be null
     * 
     * @param {string} body - JavaScript code body
     * @returns {Function} Compiled closure
     */
    compileJs(body) {
        // Wrap body with standard signature
        const wrapped = `(world, subject, verb, object) => { ${body} }`;
        return eval(wrapped);
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // GUARD HELPER METHODS — For parallel-safe closure signature
    // (world, subject, verb, object) => boolean
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get attempts counter for cumulative probability checks
     * @param {string} id - Unique ID (e.g., exit_id)
     * @returns {number} Number of attempts
     */
    getAttempts(id) {
        return this.flags[`attempts:${id}`] || 0;
    }
    
    /**
     * Set attempts counter for cumulative probability checks
     * @param {string} id - Unique ID
     * @param {number} n - Number of attempts
     */
    setAttempts(id, n) {
        this.flags[`attempts:${id}`] = n;
    }
    
    /**
     * Check if player has a specific tag
     * @param {string} tag - Tag to check
     * @returns {boolean}
     */
    hasTag(tag) {
        return this.player.tags?.includes(tag);
    }
    
    /**
     * Get room for a subject (entity)
     * @param {object} subject - Entity to get room for
     * @returns {object|null} Room object or null
     */
    room(subject) {
        if (!subject) return this.get(this.player.location);
        const location = subject.location || this.player.location;
        return this.get(location);
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // OBJECT ACTIVITY LOG — Objects logging about themselves and interactions
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Log an activity message from/about an object
     * @param {string} objectId - The object logging (or being logged about)
     * @param {string} message - What happened
     * @param {object} details - Additional details
     * @returns {object} The log entry
     */
    logObject(objectId, message, details = {}) {
        const obj = this.get(objectId);
        const ts = this.now();
        const entry = {
            id: this.objectLog.length + 1,
            timestamp: ts.epoch,
            time: ts.iso,
            elapsed: ts.elapsed,
            objectId,
            objectName: obj?.name || objectId.split('/').pop(),
            objectType: obj?.type || 'unknown',
            message,
            actor: this.player?.characterId || 'system',
            actorName: this.player?.name || 'System',
            location: this.player?.location || 'unknown',
            ...details
        };
        
        if (this.objectLogEnabled) {
            this.objectLog.push(entry);
        }
        
        // Console output
        const emoji = details.emoji || '📝';
        console.log(`${emoji} OBJ#${entry.id}: [${entry.objectName}] ${message}`);
        
        return entry;
    }
    
    /**
     * Log interaction between two objects
     * @param {string} subjectId - Object doing the action
     * @param {string} verb - What it did
     * @param {string} targetId - Object being acted upon
     * @param {object} details - Additional details
     */
    logInteraction(subjectId, verb, targetId, details = {}) {
        const subject = this.get(subjectId);
        const target = this.get(targetId);
        
        return this.logObject(subjectId, `${verb} ${target?.name || targetId}`, {
            verb,
            targetId,
            targetName: target?.name || targetId.split('/').pop(),
            emoji: details.emoji || '🔗',
            ...details
        });
    }
    
    /**
     * Log a state change on an object
     * @param {string} objectId - Object whose state changed
     * @param {string} property - What property changed
     * @param {any} oldValue - Previous value
     * @param {any} newValue - New value
     * @param {string} reason - Why it changed
     */
    logStateChange(objectId, property, oldValue, newValue, reason = '') {
        return this.logObject(objectId, `${property}: ${oldValue} → ${newValue}`, {
            type: 'state_change',
            property,
            oldValue,
            newValue,
            reason,
            emoji: '🔄'
        });
    }
    
    /**
     * Get activity log for a specific object
     * @param {string} objectId - Object to get logs for
     * @param {number} limit - Max entries to return
     */
    getObjectActivity(objectId, limit = 20) {
        return this.objectLog
            .filter(e => e.objectId === objectId || e.targetId === objectId)
            .slice(-limit)
            .reverse();
    }
    
    /**
     * Get all object activity (optionally filtered)
     * @param {number} limit - Max entries
     * @param {string} filter - Filter by object name or type
     */
    getObjectLog(limit = 20, filter = null) {
        let entries = this.objectLog;
        if (filter) {
            const f = filter.toLowerCase();
            entries = entries.filter(e => 
                e.objectId?.toLowerCase().includes(f) ||
                e.objectName?.toLowerCase().includes(f) ||
                e.message?.toLowerCase().includes(f)
            );
        }
        return entries.slice(-limit).reverse();
    }
    
    /**
     * Format object activity log for display
     */
    objectActivityReport(limit = 15, filter = null) {
        const entries = this.getObjectLog(limit, filter);
        
        if (entries.length === 0) {
            return filter 
                ? `📝 No object activity matching "${filter}".`
                : "📝 No object activity logged yet.";
        }
        
        let report = `📝 OBJECT ACTIVITY LOG${filter ? ` (filter: ${filter})` : ''}\n`;
        report += '═'.repeat(70) + '\n';
        
        for (const e of entries) {
            const time = e.time || new Date(e.timestamp).toISOString();
            const elapsed = e.elapsed !== undefined ? this.formatElapsed(e.elapsed) : '';
            const emoji = e.emoji || '📝';
            report += `${emoji} #${e.id} ${time}${elapsed ? ` (+${elapsed})` : ''}\n`;
            report += `   [${e.objectName}] ${e.message}\n`;
            if (e.targetName) {
                report += `   → ${e.targetName}\n`;
            }
            if (e.reason) {
                report += `   "${e.reason}"\n`;
            }
        }
        
        return report.trim();
    }
    
    /**
     * Format activity for a specific object
     */
    objectHistory(objectId, limit = 10) {
        const obj = this.get(objectId);
        const entries = this.getObjectActivity(objectId, limit);
        
        if (entries.length === 0) {
            return `📝 No activity recorded for ${obj?.name || objectId}.`;
        }
        
        let report = `📝 ACTIVITY: ${obj?.name || objectId}\n`;
        report += '─'.repeat(60) + '\n';
        
        for (const e of entries) {
            const time = e.time || new Date(e.timestamp).toISOString();
            const elapsed = e.elapsed !== undefined ? ` (+${this.formatElapsed(e.elapsed)})` : '';
            const emoji = e.emoji || '📝';
            const role = e.objectId === objectId ? '' : ' (as target)';
            report += `${emoji} ${time}${elapsed}${role}\n`;
            report += `   ${e.message}\n`;
        }
        
        return report.trim();
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // HISTORY ANALYSIS — Summarize and analyze object activity
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Analyze object activity log — stats, patterns, summaries
     */
    analyzeHistory() {
        const log = this.objectLog;
        const ts = this.now();
        
        if (log.length === 0) {
            return {
                totalEvents: 0,
                duration: 0,
                durationFormatted: '0ms',
                byObject: {},
                byActor: {},
                byType: {},
                byEmoji: {},
                timeline: [],
                mostActive: [],
                recentActivity: []
            };
        }
        
        // Time range
        const firstEvent = log[0];
        const lastEvent = log[log.length - 1];
        const duration = lastEvent.timestamp - firstEvent.timestamp;
        
        // Group by object
        const byObject = {};
        log.forEach(e => {
            const id = e.objectId;
            if (!byObject[id]) {
                byObject[id] = {
                    id,
                    name: e.objectName,
                    type: e.objectType,
                    events: [],
                    count: 0,
                    firstSeen: e.timestamp,
                    lastSeen: e.timestamp
                };
            }
            byObject[id].events.push(e);
            byObject[id].count++;
            byObject[id].lastSeen = e.timestamp;
        });
        
        // Group by actor
        const byActor = {};
        log.forEach(e => {
            const actor = e.actor || 'system';
            if (!byActor[actor]) {
                byActor[actor] = { id: actor, name: e.actorName || actor, count: 0 };
            }
            byActor[actor].count++;
        });
        
        // Group by event type (from emoji/type hints)
        const byType = {};
        log.forEach(e => {
            const type = e.type || (e.message?.split(' ')[0]) || 'activity';
            if (!byType[type]) {
                byType[type] = { type, count: 0, examples: [] };
            }
            byType[type].count++;
            if (byType[type].examples.length < 3) {
                byType[type].examples.push(e.message);
            }
        });
        
        // Group by emoji
        const byEmoji = {};
        log.forEach(e => {
            const emoji = e.emoji || '📝';
            if (!byEmoji[emoji]) {
                byEmoji[emoji] = { emoji, count: 0, messages: [] };
            }
            byEmoji[emoji].count++;
            if (byEmoji[emoji].messages.length < 3) {
                byEmoji[emoji].messages.push(e.message);
            }
        });
        
        // Most active objects
        const mostActive = Object.values(byObject)
            .sort((a, b) => b.count - a.count)
            .slice(0, 10);
        
        // Most active actors
        const mostActiveActors = Object.values(byActor)
            .sort((a, b) => b.count - a.count)
            .slice(0, 5);
        
        // Timeline buckets (group by elapsed time ranges)
        const timeline = [];
        const bucketSize = Math.max(1000, Math.ceil(duration / 10)); // 10 buckets or 1s min
        log.forEach(e => {
            const bucket = Math.floor((e.timestamp - firstEvent.timestamp) / bucketSize);
            if (!timeline[bucket]) {
                timeline[bucket] = { bucket, start: bucket * bucketSize, count: 0, objects: new Set() };
            }
            timeline[bucket].count++;
            timeline[bucket].objects.add(e.objectId);
        });
        
        return {
            totalEvents: log.length,
            duration,
            durationFormatted: this.formatElapsed(duration),
            sessionDuration: ts.elapsed,
            sessionDurationFormatted: this.formatElapsed(ts.elapsed),
            uniqueObjects: Object.keys(byObject).length,
            uniqueActors: Object.keys(byActor).length,
            firstEvent: firstEvent.time,
            lastEvent: lastEvent.time,
            byObject,
            byActor,
            byType,
            byEmoji,
            mostActive,
            mostActiveActors,
            timeline: timeline.filter(Boolean),
            recentActivity: log.slice(-10).reverse()
        };
    }
    
    /**
     * Format history analysis as report
     */
    historyReport() {
        const h = this.analyzeHistory();
        
        if (h.totalEvents === 0) {
            return "📜 HISTORY: No object activity recorded yet.";
        }
        
        let report = `📜 OBJECT ACTIVITY HISTORY\n`;
        report += '═'.repeat(70) + '\n\n';
        
        // Summary stats
        report += `📊 SUMMARY\n`;
        report += '─'.repeat(40) + '\n';
        report += `   Total events: ${h.totalEvents}\n`;
        report += `   Unique objects: ${h.uniqueObjects}\n`;
        report += `   Unique actors: ${h.uniqueActors}\n`;
        report += `   Activity span: ${h.durationFormatted}\n`;
        report += `   Session time: ${h.sessionDurationFormatted}\n`;
        report += `   First: ${h.firstEvent}\n`;
        report += `   Last:  ${h.lastEvent}\n\n`;
        
        // Most active objects
        if (h.mostActive.length > 0) {
            report += `🏆 MOST ACTIVE OBJECTS\n`;
            report += '─'.repeat(40) + '\n';
            h.mostActive.slice(0, 5).forEach((obj, i) => {
                const bar = '█'.repeat(Math.ceil(obj.count / h.totalEvents * 20));
                report += `   ${i + 1}. ${obj.name} (${obj.count}) ${bar}\n`;
            });
            report += '\n';
        }
        
        // Most active actors
        if (h.mostActiveActors.length > 0) {
            report += `👤 MOST ACTIVE ACTORS\n`;
            report += '─'.repeat(40) + '\n';
            h.mostActiveActors.forEach((actor, i) => {
                const bar = '█'.repeat(Math.ceil(actor.count / h.totalEvents * 20));
                report += `   ${i + 1}. ${actor.name} (${actor.count}) ${bar}\n`;
            });
            report += '\n';
        }
        
        // Activity by emoji type
        if (Object.keys(h.byEmoji).length > 0) {
            report += `🎨 ACTIVITY TYPES\n`;
            report += '─'.repeat(40) + '\n';
            Object.values(h.byEmoji)
                .sort((a, b) => b.count - a.count)
                .forEach(t => {
                    report += `   ${t.emoji} × ${t.count}\n`;
                });
            report += '\n';
        }
        
        // Recent activity
        if (h.recentActivity.length > 0) {
            report += `🕐 RECENT ACTIVITY\n`;
            report += '─'.repeat(40) + '\n';
            h.recentActivity.slice(0, 5).forEach(e => {
                const emoji = e.emoji || '📝';
                report += `   ${emoji} [${e.objectName}] ${e.message}\n`;
            });
        }
        
        return report.trim();
    }
    
    /**
     * Export history data as JSON
     */
    exportHistoryData() {
        const h = this.analyzeHistory();
        const ts = this.now();
        
        return {
            timestamp: ts.epoch,
            time: ts.iso,
            sessionDuration: this.formatElapsed(ts.elapsed),
            summary: {
                totalEvents: h.totalEvents,
                uniqueObjects: h.uniqueObjects,
                uniqueActors: h.uniqueActors,
                activitySpan: h.durationFormatted,
                firstEvent: h.firstEvent,
                lastEvent: h.lastEvent
            },
            mostActiveObjects: h.mostActive.map(o => ({
                id: o.id,
                name: o.name,
                type: o.type,
                eventCount: o.count
            })),
            mostActiveActors: h.mostActiveActors.map(a => ({
                id: a.id,
                name: a.name,
                eventCount: a.count
            })),
            activityByEmoji: Object.values(h.byEmoji).map(e => ({
                emoji: e.emoji,
                count: e.count,
                examples: e.messages
            })),
            timeline: h.timeline.map(t => ({
                bucket: t.bucket,
                startMs: t.start,
                eventCount: t.count,
                objectCount: t.objects.size
            })),
            events: this.objectLog
        };
    }
    
    /**
     * Format history data dump as JSON string
     * @param {boolean} compact - If true, output compact single-line JSON
     */
    historyDump(compact = false) {
        const data = this.exportHistoryData();
        return compact ? JSON.stringify(data) : JSON.stringify(data, null, 2);
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // NARRATIVE EXPORT — Package logs for LLM story generation
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Export session data in LLM-friendly format for narrative generation
     * @param {object} options - Export options
     * @returns {object} Structured data for LLM consumption
     */
    exportForNarrative(options = {}) {
        const ts = this.now();
        const narratorData = this.getNarrator();
        const narrator = {
            style: this.narrator.style,
            ...narratorData
        };
        
        // Build character context
        const player = {
            id: this.player.characterId,
            name: this.player.name,
            location: this.player.location,
            locationName: this.room?.name || 'unknown',
            gold: this.player.gold,
            moolah: this.player.moolah,
            inventory: this.player.inventory,
            tags: this.player.tags || []
        };
        
        // Get characters in current room
        const nearbyCharacters = this.getCharactersHere().map(c => ({
            id: c.id,
            name: c.name,
            species: c.species,
            mood: c.mood || 'neutral'
        }));
        
        // Format object activity as narrative events
        const objectEvents = this.objectLog.map(e => ({
            time: e.time,
            elapsed: this.formatElapsed(e.elapsed),
            subject: e.objectName,
            action: e.message,
            target: e.targetName || null,
            actor: e.actorName,
            location: e.location,
            emoji: e.emoji
        }));
        
        // Format transactions as economic events
        const economicEvents = this.ledger.map(tx => ({
            time: tx.time,
            elapsed: this.formatElapsed(tx.elapsed),
            from: this._txEntityName(tx.from),
            to: this._txEntityName(tx.to),
            amount: tx.amount,
            currency: tx.currency,
            reason: tx.reason
        }));
        
        // Format actions as player decisions
        const playerActions = this.actionLog.map(a => ({
            time: a.time,
            elapsed: this.formatElapsed(a.elapsed),
            action: a.name,
            success: a.success,
            params: a.params,
            error: a.error
        }));
        
        // Movement/event log
        const worldEvents = this.eventLog.map(e => ({
            time: e.time,
            elapsed: this.formatElapsed(e.elapsed),
            type: e.type,
            object: e.object || e.objectId,
            from: this._locationName(e.from),
            to: this._locationName(e.to),
            reason: e.reason
        }));
        
        return {
            meta: {
                exportTime: ts.iso,
                sessionDuration: this.formatElapsed(ts.elapsed),
                narrator: {
                    style: narrator.style,
                    tone: narrator.tone,
                    voice: narrator.voice
                }
            },
            context: {
                player,
                currentRoom: {
                    id: this.roomId,
                    name: this.room?.name,
                    description: this.room?.description
                },
                nearbyCharacters
            },
            timeline: {
                objectActivity: objectEvents,
                transactions: economicEvents,
                playerActions,
                worldEvents
            },
            summary: {
                totalEvents: this.objectLog.length + this.ledger.length + this.actionLog.length,
                objectsInvolved: [...new Set(this.objectLog.map(e => e.objectName))],
                charactersInvolved: [...new Set([
                    ...this.ledger.map(tx => tx.from),
                    ...this.ledger.map(tx => tx.to),
                    ...this.objectLog.map(e => e.actor)
                ].filter(x => x && x !== 'system' && x !== 'world'))],
                moneyMoved: {
                    gold: this.ledger.filter(tx => tx.currency === 'gold').reduce((s, tx) => s + tx.amount, 0),
                    moolah: this.ledger.filter(tx => tx.currency === 'moolah').reduce((s, tx) => s + tx.amount, 0)
                }
            }
        };
    }
    
    /**
     * Generate a prompt for LLM narrative generation
     * @param {string} style - Narrative style (summary, detailed, dramatic, etc.)
     */
    narrativePrompt(style = 'detailed') {
        const data = this.exportForNarrative();
        const narrator = data.meta.narrator;
        
        let prompt = `# Session Narrative Request\n\n`;
        prompt += `## Narrator Voice\n`;
        prompt += `Style: ${narrator.style}\n`;
        prompt += `Tone: ${narrator.tone || 'engaging'}\n`;
        prompt += `Voice: ${narrator.voice || 'third-person omniscient'}\n\n`;
        
        prompt += `## Current Scene\n`;
        prompt += `Location: ${data.context.currentRoom.name || data.context.currentRoom.id}\n`;
        prompt += `Player: ${data.context.player.name}\n`;
        if (data.context.nearbyCharacters.length > 0) {
            prompt += `Present: ${data.context.nearbyCharacters.map(c => c.name).join(', ')}\n`;
        }
        prompt += `\n`;
        
        prompt += `## Session Timeline (${data.meta.sessionDuration})\n\n`;
        
        // Merge and sort all events by time
        const allEvents = [
            ...data.timeline.objectActivity.map(e => ({ ...e, _type: 'object' })),
            ...data.timeline.transactions.map(e => ({ ...e, _type: 'transaction' })),
            ...data.timeline.worldEvents.map(e => ({ ...e, _type: 'world' }))
        ].sort((a, b) => new Date(a.time) - new Date(b.time));
        
        allEvents.forEach((e, i) => {
            if (e._type === 'object') {
                prompt += `${i + 1}. [${e.elapsed}] ${e.emoji || '📝'} ${e.subject} ${e.action}`;
                if (e.target) prompt += ` → ${e.target}`;
                prompt += `\n`;
            } else if (e._type === 'transaction') {
                const emoji = e.currency === 'gold' ? '🟡' : '🪙';
                prompt += `${i + 1}. [${e.elapsed}] ${emoji} ${e.from} paid ${e.amount} ${e.currency} to ${e.to} (${e.reason})\n`;
            } else if (e._type === 'world') {
                prompt += `${i + 1}. [${e.elapsed}] 🌍 ${e.type}: ${e.object} moved ${e.from} → ${e.to}\n`;
            }
        });
        
        prompt += `\n## Summary\n`;
        prompt += `- Objects involved: ${data.summary.objectsInvolved.join(', ') || 'none'}\n`;
        prompt += `- Money moved: ${data.summary.moneyMoved.gold} gold, ${data.summary.moneyMoved.moolah} moolah\n`;
        
        prompt += `\n## Request\n`;
        if (style === 'summary') {
            prompt += `Write a brief 2-3 sentence summary of what happened.\n`;
        } else if (style === 'dramatic') {
            prompt += `Write a dramatic narrative with vivid descriptions and emotional depth.\n`;
        } else if (style === 'humorous') {
            prompt += `Write a witty, humorous account with clever observations.\n`;
        } else {
            prompt += `Write an engaging narrative that captures the events, interactions, and atmosphere.\n`;
        }
        
        return prompt;
    }
    
    /**
     * Format narrative export as YAML for LLM context
     */
    narrativeYaml() {
        const data = this.exportForNarrative();
        
        // Simple YAML-ish format (not full YAML, but readable)
        let yaml = `# Adventure Session Export\n`;
        yaml += `# Generated: ${data.meta.exportTime}\n`;
        yaml += `# Duration: ${data.meta.sessionDuration}\n\n`;
        
        yaml += `narrator:\n`;
        yaml += `  style: ${data.meta.narrator.style}\n`;
        yaml += `  tone: ${data.meta.narrator.tone || 'engaging'}\n\n`;
        
        yaml += `player:\n`;
        yaml += `  name: ${data.context.player.name}\n`;
        yaml += `  location: ${data.context.player.locationName}\n`;
        yaml += `  gold: ${data.context.player.gold}\n`;
        yaml += `  moolah: ${data.context.player.moolah}\n\n`;
        
        yaml += `events:\n`;
        data.timeline.objectActivity.forEach(e => {
            yaml += `  - time: ${e.elapsed}\n`;
            yaml += `    subject: ${e.subject}\n`;
            yaml += `    action: "${e.action}"\n`;
            if (e.target) yaml += `    target: ${e.target}\n`;
        });
        
        if (data.timeline.transactions.length > 0) {
            yaml += `\ntransactions:\n`;
            data.timeline.transactions.forEach(tx => {
                yaml += `  - time: ${tx.elapsed}\n`;
                yaml += `    from: ${tx.from}\n`;
                yaml += `    to: ${tx.to}\n`;
                yaml += `    amount: ${tx.amount} ${tx.currency}\n`;
                yaml += `    reason: "${tx.reason}"\n`;
            });
        }
        
        return yaml;
    }
    
    /**
     * Export everything needed for Cursor/LLM state update
     * Includes current state + change log for replay
     */
    exportForCursor() {
        const ts = this.now();
        
        return {
            _meta: {
                format: 'mootal-cursor-export',
                version: '1.0',
                exportTime: ts.iso,
                sessionDuration: this.formatElapsed(ts.elapsed)
            },
            
            // Current game state
            state: {
                player: {
                    id: this.player.characterId,
                    name: this.player.name,
                    location: this.player.location,
                    gold: this.player.gold,
                    moolah: this.player.moolah,
                    inventory: [...this.player.inventory],
                    tags: this.player.tags || []
                },
                room: {
                    id: this.roomId,
                    name: this.room?.name,
                    contents: this.room?.contents || []
                },
                narrator: this.getNarrator()
            },
            
            // Change logs for replay/analysis
            logs: {
                actions: this.actionLog,
                objects: this.objectLog,
                events: this.eventLog,
                transactions: this.ledger
            },
            
            // Economy snapshot
            economy: {
                flows: this.moneyFlows,
                analysis: this.analyzeEconomy()
            },
            
            // History analysis
            history: this.analyzeHistory()
        };
    }
    
    /**
     * Record a money flow in the flow table
     */
    recordFlow(from, to, currency, amount) {
        if (!this.moneyFlows[from]) {
            this.moneyFlows[from] = {};
        }
        if (!this.moneyFlows[from][to]) {
            this.moneyFlows[from][to] = { gold: 0, moolah: 0 };
        }
        this.moneyFlows[from][to][currency] += amount;
    }
    
    /**
     * Get money flow analysis
     */
    getFlowAnalysis() {
        const entities = new Set();
        const inflows = {};   // entity → { gold, moolah } received
        const outflows = {};  // entity → { gold, moolah } sent
        
        // Aggregate flows
        for (const [from, targets] of Object.entries(this.moneyFlows)) {
            entities.add(from);
            if (!outflows[from]) outflows[from] = { gold: 0, moolah: 0 };
            
            for (const [to, amounts] of Object.entries(targets)) {
                entities.add(to);
                if (!inflows[to]) inflows[to] = { gold: 0, moolah: 0 };
                
                outflows[from].gold += amounts.gold;
                outflows[from].moolah += amounts.moolah;
                inflows[to].gold += amounts.gold;
                inflows[to].moolah += amounts.moolah;
            }
        }
        
        // Calculate net positions
        const netPositions = {};
        for (const entity of entities) {
            const inGold = inflows[entity]?.gold || 0;
            const inMoolah = inflows[entity]?.moolah || 0;
            const outGold = outflows[entity]?.gold || 0;
            const outMoolah = outflows[entity]?.moolah || 0;
            
            netPositions[entity] = {
                inGold, inMoolah,
                outGold, outMoolah,
                netGold: inGold - outGold,
                netMoolah: inMoolah - outMoolah,
                netTotal: (inGold - outGold) + (inMoolah - outMoolah)
            };
        }
        
        // Top flows (largest individual transfers)
        const topFlows = [];
        for (const [from, targets] of Object.entries(this.moneyFlows)) {
            for (const [to, amounts] of Object.entries(targets)) {
                if (amounts.gold > 0) {
                    topFlows.push({ from, to, currency: 'gold', amount: amounts.gold });
                }
                if (amounts.moolah > 0) {
                    topFlows.push({ from, to, currency: 'moolah', amount: amounts.moolah });
                }
            }
        }
        topFlows.sort((a, b) => b.amount - a.amount);
        
        return {
            entities: [...entities],
            inflows,
            outflows,
            netPositions,
            topFlows: topFlows.slice(0, 10),
            flowMatrix: this.moneyFlows
        };
    }
    
    /**
     * Format money flow report
     */
    flowReport() {
        const analysis = this.getFlowAnalysis();
        
        if (analysis.entities.length === 0) {
            return "💱 No money flows recorded yet.";
        }
        
        let report = `
╔═══════════════════════════════════════════════════════════════════╗
║  💱 MONEY FLOW ANALYSIS                                           ║
╚═══════════════════════════════════════════════════════════════════╝

📊 NET POSITIONS (in - out)
`;
        
        // Sort by net total
        const sorted = Object.entries(analysis.netPositions)
            .sort((a, b) => b[1].netTotal - a[1].netTotal);
        
        for (const [entity, pos] of sorted) {
            const name = this._txEntityName(entity);
            const sign = pos.netTotal >= 0 ? '+' : '';
            report += `   ${name.padEnd(25)} ${sign}${pos.netGold} 🟡  ${sign}${pos.netMoolah} 🪙\n`;
        }
        
        report += `\n🔝 TOP FLOWS\n`;
        for (const flow of analysis.topFlows.slice(0, 5)) {
            const fromName = this._txEntityName(flow.from);
            const toName = this._txEntityName(flow.to);
            const emoji = flow.currency === 'gold' ? '🟡' : '🪙';
            report += `   ${fromName} → ${toName}: ${flow.amount} ${emoji}\n`;
        }
        
        // Flow matrix summary
        report += `\n📈 FLOW MATRIX\n`;
        report += `   ${analysis.entities.length} entities participated in ${this.ledger.length} transactions\n`;
        
        return report.trim();
    }
    
    /**
     * Export full economic data as JSON (for analysis tools)
     */
    exportEconomicData() {
        const economy = this.analyzeEconomy();
        const flows = this.getFlowAnalysis();
        const ts = this.now();
        
        return {
            timestamp: ts.epoch,
            time: ts.iso,
            sessionDuration: this.formatElapsed(ts.elapsed),
            session: {
                transactionCount: this.ledger.length,
                actionCount: this.actionLog.length,
                eventCount: this.eventLog.length
            },
            economy: {
                population: economy.population,
                totalGold: economy.totalGold,
                totalMoolah: economy.totalMoolah,
                totalWealth: economy.totalWealth,
                avgWealth: economy.avgWealth,
                medianWealth: economy.medianWealth,
                giniIndex: economy.giniIndex,
                richest: economy.richest.slice(0, 5).map(c => ({ name: c.name, total: c.total })),
                poorest: economy.poorest.slice(0, 3).map(c => ({ name: c.name, total: c.total })),
                speciesWealth: economy.speciesWealth,
                categoryWealth: economy.categoryWealth
            },
            flows: {
                entities: flows.entities,
                netPositions: flows.netPositions,
                topFlows: flows.topFlows,
                matrix: flows.flowMatrix
            },
            transactions: this.ledger,
            player: {
                id: this.player.characterId,
                name: this.player.name,
                gold: this.player.gold,
                moolah: this.player.moolah,
                location: this.player.location
            }
        };
    }
    
    /**
     * Format economic data dump
     * @param {boolean} compact - If true, output compact single-line JSON
     */
    economicDump(compact = false) {
        const data = this.exportEconomicData();
        return compact ? JSON.stringify(data) : JSON.stringify(data, null, 2);
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // ACTION SYSTEM — All game actions go through this API
    // ═══════════════════════════════════════════════════════════════════════════
    // 
    // Design principles:
    // 1. Function names declare what they do (verb_noun pattern)
    // 2. Every action logs itself automatically
    // 3. Actions are representation-independent (work with any data format)
    // 4. Consistent return format: { success, data?, error?, action }
    // 5. Actions can be replayed, undone, tested
    //
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Execute and log an action
     * @param {string} actionName - Descriptive action name (e.g., 'player.take_object')
     * @param {object} params - Action parameters
     * @param {function} executor - Function that performs the action
     * @returns {object} { success, data?, error?, action }
     */
    action(actionName, params, executor) {
        const ts = this.now();
        const action = {
            id: this.actionLog.length + 1,
            timestamp: ts.epoch,
            time: ts.iso,
            elapsed: ts.elapsed,
            name: actionName,
            actor: this.player?.characterId || 'system',
            actorName: this.player?.name || 'System',
            location: this.player?.location || 'unknown',
            params: { ...params },
            success: false,
            error: null,
            result: null
        };
        
        try {
            // Execute the action
            const result = executor();
            
            action.success = result.success !== false;
            action.result = result.data || result;
            action.error = result.error || null;
            
            // Log to console
            const emoji = action.success ? '✅' : '❌';
            console.log(`${emoji} ACTION#${action.id}: ${actionName}`, 
                action.success ? '' : `[${action.error}]`);
            
        } catch (e) {
            action.success = false;
            action.error = e.message;
            console.log(`💥 ACTION#${action.id}: ${actionName} FAILED: ${e.message}`);
        }
        
        // Log to action log
        if (this.actionLogEnabled) {
            this.actionLog.push(action);
        }
        
        return {
            success: action.success,
            data: action.result,
            error: action.error,
            action
        };
    }
    
    /**
     * Get recent actions
     */
    getActions(limit = 20, filter = null) {
        let actions = this.actionLog;
        if (filter) {
            actions = actions.filter(a => a.name.includes(filter));
        }
        return actions.slice(-limit).reverse();
    }
    
    /**
     * Format action log for display
     */
    actionHistory(limit = 15) {
        const actions = this.getActions(limit);
        
        if (actions.length === 0) {
            return "📜 No actions recorded yet.";
        }
        
        let report = `📜 ACTION LOG (last ${actions.length})\n`;
        report += '═'.repeat(70) + '\n';
        
        for (const a of actions) {
            const time = a.time || new Date(a.timestamp).toISOString();
            const elapsed = a.elapsed !== undefined ? this.formatElapsed(a.elapsed) : '';
            const status = a.success ? '✅' : '❌';
            const params = Object.entries(a.params)
                .filter(([k, v]) => v !== undefined && k !== 'reason')
                .map(([k, v]) => `${k}=${typeof v === 'string' ? v.substring(0, 20) : v}`)
                .join(', ');
            
            report += `${status} #${a.id} ${time}${elapsed ? ` (+${elapsed})` : ''}\n`;
            report += `   ${a.name}${params ? ` — ${params}` : ''}\n`;
            if (a.params.reason) report += `   "${a.params.reason}"\n`;
            if (!a.success && a.error) report += `   ⚠️ ${a.error}\n`;
        }
        
        return report.trim();
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // EVENT LOG — All object movements and state changes
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Log an event to the event log
     * @param {string} type - Event type: 'take', 'drop', 'move', 'create', 'destroy', 'give', 'use'
     * @param {object} details - Event-specific details
     * @returns {object} The event record
     */
    logEvent(type, details) {
        const ts = this.now();
        const event = {
            id: this.eventLog.length + 1,
            timestamp: ts.epoch,
            time: ts.iso,
            elapsed: ts.elapsed,
            type,
            actor: this.player.characterId || 'player',
            actorName: this.player.name,
            location: this.roomId || 'unknown',
            ...details
        };
        
        if (this.eventLogEnabled) {
            this.eventLog.push(event);
        }
        
        // Console log for debugging
        const emoji = {
            take: '📥', drop: '📤', move: '🚚', create: '✨', 
            destroy: '💥', give: '🤝', use: '🔧', equip: '⚔️'
        }[type] || '📋';
        
        console.log(`${emoji} EVENT#${event.id}: ${type.toUpperCase()} | ${details.object || details.objectId || '?'} | ${details.reason || ''}`);
        
        return event;
    }
    
    /**
     * object.take — Take an object from current room into inventory
     */
    takeObject(objectId, reason = 'picked up') {
        return this.action('object.take', { objectId, reason }, () => {
            const room = this.room;
            if (!room) return { success: false, error: 'No current room' };
            
            // Find object in registry with matching location
            // Registry keys are like "object/garden/lamp", we need to match the full ID
            const objData = this.registry[objectId] || this.registry['object/' + objectId];
            
            if (!objData) {
                return { success: false, error: `Object "${objectId}" not found` };
            }
            
            // Check if object is in this room (by location property)
            const roomId = room.id || this.player?.location;
            if (objData.location !== roomId) {
                return { success: false, error: `Object "${objectId}" not in this room` };
            }
            
            // Check if object is portable
            if (objData.portable === false) {
                return { success: false, error: `You can't pick up the ${objData.name || objectId}.` };
            }
            
            const objRef = objectId;
            const objName = objData?.name || objRef;
            
            // Update object location to 'inventory'
            objData.location = 'inventory';
            
            // Add to inventory
            this.player.inventory.push(objRef);
            
            // Log event
            this.logEvent('take', {
                objectId: objRef,
                object: objName,
                from: this.player.location,
                to: 'inventory',
                reason
            });
            
            // Log object activity
            this.logObject(objRef, `taken by ${this.player.name}`, {
                emoji: '📥',
                from: this.player.location,
                reason
            });
            
            return { success: true, data: { object: objData, objRef } };
        });
    }
    
    /**
     * object.drop — Drop an object from inventory into current room
     */
    dropObject(objectId, reason = 'dropped') {
        return this.action('object.drop', { objectId, reason }, () => {
            const room = this.room;
            if (!room) return { success: false, error: 'No current room' };
            
            // Find in inventory
            const idx = this.player.inventory.findIndex(c => 
                c === objectId || c.includes(objectId)
            );
            
            if (idx === -1) {
                return { success: false, error: `Object "${objectId}" not in inventory` };
            }
            
            // Remove from inventory
            const objRef = this.player.inventory.splice(idx, 1)[0];
            const objData = this.get(objRef) || this.registry[objRef] || this.registry['object/' + objRef];
            const objName = objData?.name || objRef;
            
            // Update object location to this room (for getRoomObjects lookup)
            const roomId = room.id || this.player?.location;
            if (objData) {
                objData.location = roomId;
            }
            
            // Also add to room.contents for backwards compatibility
            if (!room.contents) room.contents = [];
            room.contents.push(objRef);
            
            // Log event
            this.logEvent('drop', {
                objectId: objRef,
                object: objName,
                from: 'inventory',
                to: this.player.location,
                reason
            });
            
            // Log object activity
            this.logObject(objRef, `dropped by ${this.player.name}`, {
                emoji: '📤',
                to: this.player.location,
                reason
            });
            
            return { success: true, data: { object: objData, objRef } };
        });
    }
    
    /**
     * object.give — Give an object to another character
     */
    giveObject(objectId, targetId, reason = 'gifted') {
        return this.action('object.give', { objectId, targetId, reason }, () => {
            // Find in inventory
            const idx = this.player.inventory.findIndex(c => 
                c === objectId || c.includes(objectId)
            );
            
            if (idx === -1) {
                return { success: false, error: `Object "${objectId}" not in inventory` };
            }
            
            // Get target
            const target = this.get(targetId);
            if (!target) {
                return { success: false, error: `Character "${targetId}" not found` };
            }
            
            // Remove from player inventory
            const objRef = this.player.inventory.splice(idx, 1)[0];
            const objData = this.get(objRef);
            const objName = objData?.name || objRef;
            
            // Add to target inventory
            if (!target.inventory) target.inventory = [];
            target.inventory.push(objRef);
            
            // Log event
            this.logEvent('give', {
                objectId: objRef,
                object: objName,
                from: this.player.characterId,
                to: targetId,
                toName: target.name,
                reason
            });
            
            // Log object activity
            this.logObject(objRef, `given to ${target.name} by ${this.player.name}`, {
                emoji: '🤝',
                from: this.player.characterId,
                to: targetId,
                reason
            });
            
            return { success: true, data: { object: objData, target } };
        });
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // OBJECT ECONOMY — Value, trading, buying, selling
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get object's economic value
     * @param {string} objectId - Object to check
     * @returns {object} { value, currency, name }
     */
    getObjectValue(objectId) {
        const obj = this.get(objectId);
        if (!obj) return { value: 0, currency: 'gold', name: objectId };
        
        return {
            id: objectId,
            name: obj.name || objectId.split('/').pop(),
            value: obj.value ?? 0,
            currency: obj.currency || 'gold',
            type: obj.type || 'item'
        };
    }
    
    /**
     * Appraise an object - get its market value
     * @param {string} objectId - Object to appraise
     */
    appraiseObject(objectId) {
        const info = this.getObjectValue(objectId);
        const emoji = info.currency === 'gold' ? '🟡' : '🪙';
        
        if (info.value === 0) {
            return `📋 ${info.name}: Worthless (can be given freely)`;
        }
        
        return `📋 ${info.name}: ${info.value} ${info.currency} ${emoji}`;
    }
    
    /**
     * Check if character wants to buy an object at its price
     * Override this for custom NPC buying behavior
     * @param {object} buyer - Character considering purchase
     * @param {object} item - Item info from getObjectValue
     * @returns {object} { willing, reason }
     */
    characterWantsToBuy(buyer, item) {
        // Default: buy if they have enough money and item has value
        const buyerGold = buyer.gold || 0;
        const buyerMoolah = buyer.moolah || 0;
        const buyerFunds = item.currency === 'gold' ? buyerGold : buyerMoolah;
        
        if (item.value === 0) {
            return { willing: false, reason: `${buyer.name} doesn't want worthless items.` };
        }
        
        if (buyerFunds < item.value) {
            return { willing: false, reason: `${buyer.name} can't afford ${item.value} ${item.currency}.` };
        }
        
        // Check if buyer has preferences (can be extended)
        if (buyer.interests && !buyer.interests.includes(item.type)) {
            return { willing: false, reason: `${buyer.name} isn't interested in ${item.type}s.` };
        }
        
        return { willing: true, reason: `${buyer.name} agrees to buy ${item.name} for ${item.value} ${item.currency}.` };
    }
    
    /**
     * Sell object from player inventory to another character
     * @param {string} objectId - Object to sell
     * @param {string} targetId - Character to sell to
     */
    sellObject(objectId, targetId) {
        return this.action('object.sell', { objectId, targetId }, () => {
            // Find in inventory
            const idx = this.player.inventory.findIndex(c => 
                c === objectId || c.includes(objectId)
            );
            
            if (idx === -1) {
                return { success: false, error: `Object "${objectId}" not in inventory` };
            }
            
            const objRef = this.player.inventory[idx];
            const item = this.getObjectValue(objRef);
            
            // Get target
            const target = this.get(targetId);
            if (!target) {
                return { success: false, error: `Character "${targetId}" not found` };
            }
            
            // Check if target wants to buy
            const decision = this.characterWantsToBuy(target, item);
            if (!decision.willing) {
                return { success: false, error: decision.reason };
            }
            
            // Execute transaction
            // 1. Target pays player
            const currency = item.currency;
            const amount = item.value;
            
            // Deduct from target
            target[currency] = (target[currency] || 0) - amount;
            
            // Add to player
            this.player[currency] = (this.player[currency] || 0) + amount;
            
            // Log transaction
            this.logTransaction(targetId, this.player.characterId, currency, amount, `purchased ${item.name}`);
            this.recordFlow(targetId, this.player.characterId, currency, amount);
            
            // 2. Transfer object
            this.player.inventory.splice(idx, 1);
            if (!target.inventory) target.inventory = [];
            target.inventory.push(objRef);
            
            // Log events
            this.logEvent('sell', {
                objectId: objRef,
                object: item.name,
                from: this.player.characterId,
                to: targetId,
                toName: target.name,
                value: amount,
                currency,
                reason: 'sold'
            });
            
            this.logObject(objRef, `sold to ${target.name} for ${amount} ${currency}`, {
                emoji: '💰',
                from: this.player.characterId,
                to: targetId,
                value: amount,
                currency
            });
            
            return { 
                success: true, 
                data: { 
                    object: item, 
                    buyer: target.name,
                    price: amount,
                    currency 
                } 
            };
        });
    }
    
    /**
     * Buy object from another character
     * @param {string} objectId - Object to buy  
     * @param {string} fromId - Character to buy from
     */
    buyObject(objectId, fromId) {
        return this.action('object.buy', { objectId, fromId }, () => {
            // Get seller
            const seller = this.get(fromId);
            if (!seller) {
                return { success: false, error: `Character "${fromId}" not found` };
            }
            
            // Find object in seller's inventory
            const sellerInv = seller.inventory || [];
            const idx = sellerInv.findIndex(c => 
                c === objectId || c.includes(objectId)
            );
            
            if (idx === -1) {
                return { success: false, error: `${seller.name} doesn't have "${objectId}"` };
            }
            
            const objRef = sellerInv[idx];
            const item = this.getObjectValue(objRef);
            
            // Check if player can afford it
            const currency = item.currency;
            const amount = item.value;
            
            if (amount > 0 && (this.player[currency] || 0) < amount) {
                return { success: false, error: `You can't afford ${amount} ${currency}` };
            }
            
            // Execute transaction (if item has value)
            if (amount > 0) {
                // Player pays
                this.player[currency] = (this.player[currency] || 0) - amount;
                
                // Seller receives
                seller[currency] = (seller[currency] || 0) + amount;
                
                // Log transaction
                this.logTransaction(this.player.characterId, fromId, currency, amount, `bought ${item.name}`);
                this.recordFlow(this.player.characterId, fromId, currency, amount);
            }
            
            // Transfer object
            sellerInv.splice(idx, 1);
            this.player.inventory.push(objRef);
            
            // Log events
            this.logEvent('buy', {
                objectId: objRef,
                object: item.name,
                from: fromId,
                fromName: seller.name,
                to: this.player.characterId,
                value: amount,
                currency,
                reason: 'purchased'
            });
            
            this.logObject(objRef, `bought from ${seller.name} for ${amount} ${currency}`, {
                emoji: '🛒',
                from: fromId,
                to: this.player.characterId,
                value: amount,
                currency
            });
            
            return { 
                success: true, 
                data: { 
                    object: item, 
                    seller: seller.name,
                    price: amount,
                    currency 
                } 
            };
        });
    }
    
    /**
     * List items for sale by a character (items in their inventory with value > 0)
     * @param {string} characterId - Character to check
     */
    getItemsForSale(characterId) {
        const char = this.get(characterId);
        if (!char) return [];
        
        const inv = Array.isArray(char.inventory) ? char.inventory : [];
        
        return inv
            .map(objId => this.getObjectValue(objId))
            .filter(item => item.value > 0);
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // CATALOG SYSTEM — Virtual stores, vending, mail-order
    // ═══════════════════════════════════════════════════════════════════════════
    //
    // Catalogs are virtual vendors with infinite stock.
    // Items ordered appear instantly in inventory (no delivery time yet).
    // 
    // Catalog definition:
    //   { id, name, description, currency, items: [{ id, name, price, type, ... }] }
    //
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get all available catalogs
     */
    getCatalogs() {
        const catalogs = [];
        for (const [id, obj] of Object.entries(this.registry)) {
            if (obj.type === 'catalog') {
                catalogs.push({ id, ...obj });
            }
        }
        return catalogs;
    }
    
    /**
     * Get a specific catalog by id or name
     */
    getCatalog(catalogId) {
        // Direct lookup
        let catalog = this.get(catalogId);
        if (catalog?.type === 'catalog') return { id: catalogId, ...catalog };
        
        // Try with catalog/ prefix
        catalog = this.get(`catalog/${catalogId}`);
        if (catalog?.type === 'catalog') return { id: `catalog/${catalogId}`, ...catalog };
        
        // Search by name
        for (const [id, obj] of Object.entries(this.registry)) {
            if (obj.type === 'catalog' && obj.name?.toLowerCase().includes(catalogId.toLowerCase())) {
                return { id, ...obj };
            }
        }
        return null;
    }
    
    /**
     * Browse a catalog's items
     * @param {string} catalogId - Catalog to browse
     */
    browseCatalog(catalogId) {
        const catalog = this.getCatalog(catalogId);
        if (!catalog) return null;
        
        const currency = catalog.currency || 'gold';
        const items = catalog.items || [];
        
        return {
            id: catalog.id,
            name: catalog.name,
            description: catalog.description,
            currency,
            itemCount: items.length,
            items: items.map(item => ({
                id: item.id,
                name: item.name,
                price: item.price || 0,
                currency: item.currency || currency,
                type: item.type || 'item',
                description: item.description
            }))
        };
    }
    
    /**
     * Order an item from a catalog
     * @param {string} catalogId - Catalog to order from
     * @param {string} itemId - Item to order (id or name match)
     */
    orderFromCatalog(catalogId, itemId) {
        return this.action('catalog.order', { catalogId, itemId }, () => {
            const catalog = this.getCatalog(catalogId);
            if (!catalog) {
                return { success: false, error: `Catalog "${catalogId}" not found` };
            }
            
            const items = catalog.items || [];
            const item = items.find(i => 
                i.id === itemId || 
                i.id?.includes(itemId) ||
                i.name?.toLowerCase().includes(itemId.toLowerCase())
            );
            
            if (!item) {
                return { success: false, error: `Item "${itemId}" not in ${catalog.name} catalog` };
            }
            
            const price = item.price || 0;
            const currency = item.currency || catalog.currency || 'gold';
            
            // Check if player can afford
            if (price > 0 && (this.player[currency] || 0) < price) {
                return { success: false, error: `You can't afford ${price} ${currency}` };
            }
            
            // Deduct payment
            if (price > 0) {
                this.player[currency] = (this.player[currency] || 0) - price;
                
                // Log transaction to catalog vendor
                this.logTransaction(this.player.characterId, catalog.id, currency, price, `ordered ${item.name}`);
                this.recordFlow(this.player.characterId, catalog.id, currency, price);
            }
            
            // Create the item in inventory (instant delivery!)
            const newItemId = `item/${item.id || item.name.toLowerCase().replace(/\s+/g, '-')}-${Date.now()}`;
            this.registry[newItemId] = {
                id: newItemId,
                name: item.name,
                type: item.type || 'item',
                value: item.resale || Math.floor(price * 0.5), // Resale value defaults to 50%
                currency: currency,
                description: item.description,
                from_catalog: catalog.id,
                ordered_at: this.now().iso
            };
            this.player.inventory.push(newItemId);
            
            // Log the creation/delivery
            this.logEvent('order', {
                objectId: newItemId,
                object: item.name,
                from: catalog.id,
                to: this.player.characterId,
                price,
                currency,
                reason: 'catalog order'
            });
            
            this.logObject(newItemId, `ordered from ${catalog.name}`, {
                emoji: '📦',
                from: catalog.id,
                price,
                currency
            });
            
            return {
                success: true,
                data: {
                    item: item.name,
                    itemId: newItemId,
                    price,
                    currency,
                    catalog: catalog.name,
                    delivery: 'instant'
                }
            };
        });
    }
    
    /**
     * Format catalog listing
     */
    catalogListing(catalogId) {
        const info = this.browseCatalog(catalogId);
        if (!info) return `Catalog "${catalogId}" not found.`;
        
        const emoji = info.currency === 'gold' ? '🟡' : '🪙';
        let report = `\n📚 ${info.name.toUpperCase()}\n`;
        report += '═'.repeat(50) + '\n';
        if (info.description) report += `${info.description}\n\n`;
        
        if (info.items.length === 0) {
            report += '(No items available)\n';
        } else {
            for (const item of info.items) {
                const itemEmoji = item.currency === 'gold' ? '🟡' : '🪙';
                report += `  ${item.name.padEnd(30)} ${String(item.price).padStart(5)} ${item.currency} ${itemEmoji}\n`;
                if (item.description) {
                    report += `    └─ ${item.description}\n`;
                }
            }
        }
        
        report += '\n' + '─'.repeat(50);
        report += `\nUse ORDER <item> FROM ${info.name} to purchase.`;
        
        return report;
    }
    
    /**
     * Format all catalogs list
     */
    catalogsList() {
        const catalogs = this.getCatalogs();
        
        if (catalogs.length === 0) {
            return '📚 No catalogs available.';
        }
        
        let report = '\n📚 AVAILABLE CATALOGS\n';
        report += '═'.repeat(50) + '\n';
        
        for (const cat of catalogs) {
            const items = cat.items?.length || 0;
            report += `\n  📖 ${cat.name}\n`;
            report += `     ${items} items | Currency: ${cat.currency || 'gold'}\n`;
            if (cat.description) {
                report += `     ${cat.description}\n`;
            }
        }
        
        report += '\n' + '─'.repeat(50);
        report += '\nUse CATALOG <name> to browse a specific catalog.';
        
        return report;
    }
    
    /**
     * object.create — Create a new object in the world
     */
    createObject(id, data, location = 'inventory', reason = 'created') {
        return this.action('object.create', { id, name: data.name, location, reason }, () => {
            // Add to registry
            this.registry[id] = { id, type: 'object', ...data };
            
            // Place it
            if (location === 'inventory') {
                this.player.inventory.push(id);
            } else if (location === this.roomId || location === 'room') {
                if (!this.room.contents) this.room.contents = [];
                this.room.contents.push(id);
            } else {
                // Try as character or room
                const target = this.get(location);
                if (target) {
                    if (!target.contents) target.contents = [];
                    if (!target.inventory) target.inventory = [];
                    (target.inventory || target.contents).push(id);
                }
            }
            
            // Log event
            this.logEvent('create', {
                objectId: id,
                object: data.name || id,
                from: 'system',
                to: location === 'inventory' ? 'inventory' : (location === 'room' ? this.player.location : location),
                reason
            });
            
            // Log object activity (first entry for this object!)
            this.logObject(id, 'created', {
                emoji: '✨',
                location,
                reason
            });
            
            return { success: true, data: { object: this.registry[id] } };
        });
    }
    
    /**
     * object.destroy — Destroy an object from the world
     */
    destroyObject(objectId, reason = 'destroyed') {
        return this.action('object.destroy', { objectId, reason }, () => {
            const objData = this.get(objectId);
            const objName = objData?.name || objectId;
            
            if (!objData) {
                return { success: false, error: `Object "${objectId}" not found` };
            }
            
            // Remove from player inventory
            const invIdx = this.player.inventory.indexOf(objectId);
            if (invIdx !== -1) {
                this.player.inventory.splice(invIdx, 1);
            }
            
            // Remove from current room
            if (this.room?.contents) {
                const roomIdx = this.room.contents.indexOf(objectId);
                if (roomIdx !== -1) {
                    this.room.contents.splice(roomIdx, 1);
                }
            }
            
            // Remove from registry
            delete this.registry[objectId];
            
            // Log object activity (last entry for this object!)
            this.logObject(objectId, 'destroyed', {
                emoji: '💥',
                reason
            });
            
            // Log event
            this.logEvent('destroy', {
                objectId,
                object: objName,
                from: this.player.location || 'world',
                to: 'void',
                reason
            });
            
            return { success: true, data: { objectName: objName } };
        });
    }
    
    /**
     * object.move — Move an object between locations (rooms, inventories)
     */
    moveObject(objectId, from, to, reason = 'moved') {
        return this.action('object.move', { objectId, from, to, reason }, () => {
            const objData = this.get(objectId);
            const objName = objData?.name || objectId;
            
            // Remove from source
            if (from === 'inventory' || from === 'player') {
                const idx = this.player.inventory.indexOf(objectId);
                if (idx !== -1) this.player.inventory.splice(idx, 1);
            } else {
                const source = this.get(from);
                if (source?.contents) {
                    const idx = source.contents.indexOf(objectId);
                    if (idx !== -1) source.contents.splice(idx, 1);
                }
                if (source?.inventory) {
                    const idx = source.inventory.indexOf(objectId);
                    if (idx !== -1) source.inventory.splice(idx, 1);
                }
            }
            
            // Add to destination
            if (to === 'inventory' || to === 'player') {
                this.player.inventory.push(objectId);
            } else if (to === 'void' || to === 'destroyed') {
                // Goes nowhere
            } else {
                const dest = this.get(to);
                if (dest) {
                    if (!dest.contents) dest.contents = [];
                    dest.contents.push(objectId);
                }
            }
            
            // Log event
            this.logEvent('move', {
                objectId,
                object: objName,
                from,
                to,
                reason
            });
            
            return { success: true, data: { objectName: objName, from, to } };
        });
    }
    
    /**
     * Get recent events from log
     * @param {number} limit - How many to return
     * @param {string} type - Filter by type (optional)
     */
    getEvents(limit = 10, type = null) {
        let events = this.eventLog;
        if (type) {
            events = events.filter(e => e.type === type);
        }
        return events.slice(-limit).reverse();
    }
    
    /**
     * Format event history for display
     */
    eventHistory(limit = 10) {
        const events = this.getEvents(limit);
        
        if (events.length === 0) {
            return "📋 No events logged yet.";
        }
        
        const emoji = {
            take: '📥', drop: '📤', move: '🚚', create: '✨', 
            destroy: '💥', give: '🤝', use: '🔧', equip: '⚔️'
        };
        
        let report = `📋 EVENT LOG (last ${events.length})\n`;
        report += '─'.repeat(70) + '\n';
        
        for (const e of events) {
            const time = e.time || new Date(e.timestamp).toISOString();
            const elapsed = e.elapsed !== undefined ? ` (+${this.formatElapsed(e.elapsed)})` : '';
            const icon = emoji[e.type] || '📋';
            const fromName = this._locationName(e.from);
            const toName = this._locationName(e.to || e.toName);
            report += `#${e.id} ${time}${elapsed} ${icon} ${e.type.toUpperCase()}\n`;
            report += `   ${e.object || e.objectId} | ${fromName} → ${toName}\n`;
            if (e.reason && e.reason !== e.type) {
                report += `   "${e.reason}"\n`;
            }
        }
        
        return report.trim();
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // TRANSACTION API — All money transfers go through here
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Log a transaction to the ledger
     * @param {string} from - Source (character ID, 'world', 'system', etc.)
     * @param {string} to - Destination (character ID, 'world', 'void', etc.)
     * @param {string} currency - 'gold' or 'moolah'
     * @param {number} amount - Amount transferred
     * @param {string} reason - Why this transfer happened
     * @returns {object} The transaction record
     */
    logTransaction(from, to, currency, amount, reason) {
        const ts = this.now();
        const tx = {
            id: this.ledger.length + 1,
            timestamp: ts.epoch,
            time: ts.iso,
            elapsed: ts.elapsed,
            from,
            to,
            currency,
            amount,
            reason,
            playerLocation: this.roomId || 'unknown'
        };
        
        if (this.ledgerEnabled) {
            this.ledger.push(tx);
        }
        
        // Console log for debugging (🟡 gold, 🪙 moolah)
        const txEmoji = currency === 'gold' ? '🟡' : '🪙';
        console.log(`${txEmoji} TX#${tx.id}: ${from} → ${to} | ${amount} ${currency} | "${reason}"`);
        
        return tx;
    }
    
    /**
     * Transfer currency between entities
     * @param {string} from - Source ID ('player', character ID, 'world', 'system')
     * @param {string} to - Destination ID
     * @param {string} currency - 'gold' or 'moolah'
     * @param {number} amount - Amount to transfer
     * @param {string} reason - Why this transfer is happening
     * @returns {object} { success, tx, error }
     */
    transfer(from, to, currency, amount, reason = 'unspecified') {
        if (amount <= 0) {
            return { success: false, error: 'Amount must be positive' };
        }
        
        if (!['gold', 'moolah'].includes(currency)) {
            return { success: false, error: 'Invalid currency (use gold or moolah)' };
        }
        
        // Get source balance
        let sourceBalance = 0;
        let sourceEntity = null;
        
        if (from === 'player') {
            sourceBalance = this.player[currency] || 0;
            sourceEntity = this.player;
        } else if (from === 'world' || from === 'system') {
            sourceBalance = Infinity; // World has unlimited funds
        } else {
            sourceEntity = this.get(from);
            sourceBalance = sourceEntity?.[currency] || 0;
        }
        
        // Check sufficient funds (unless from world/system)
        if (from !== 'world' && from !== 'system' && sourceBalance < amount) {
            return { 
                success: false, 
                error: `Insufficient ${currency}: has ${sourceBalance}, needs ${amount}` 
            };
        }
        
        // Get destination
        let destEntity = null;
        if (to === 'player') {
            destEntity = this.player;
        } else if (to === 'world' || to === 'void') {
            destEntity = null; // Money disappears
        } else {
            destEntity = this.get(to);
        }
        
        // Execute transfer
        if (sourceEntity && from !== 'world' && from !== 'system') {
            sourceEntity[currency] = (sourceEntity[currency] || 0) - amount;
        }
        
        if (destEntity && to !== 'world' && to !== 'void') {
            destEntity[currency] = (destEntity[currency] || 0) + amount;
        }
        
        // Record flow in global flow table
        this.recordFlow(from, to, currency, amount);
        
        // Log transaction
        const tx = this.logTransaction(from, to, currency, amount, reason);
        
        return { success: true, tx };
    }
    
    /**
     * Set narrator style
     */
    setNarratorStyle(style) {
        const styles = ['classic', 'sardonic', 'dramatic', 'minimalist', 'cozy', 'palm'];
        if (styles.includes(style.toLowerCase())) {
            this.narrator.style = style.toLowerCase();
            return `🎙️ Narrator style: ${style}`;
        }
        return `Unknown style. Available: ${styles.join(', ')}`;
    }
    
    /**
     * Get current narrator (loads from registry if available)
     */
    getNarrator() {
        const narrator = this.get('character/abstract/narrator');
        return narrator?.styles?.[this.narrator.style] || null;
    }
    
    /**
     * Set player character from registry (admin/init use)
     * @param {string} characterId - e.g., 'character/don-hopkins'
     */
    setPlayer(characterId) {
        const char = this.get(characterId);
        if (!char) {
            console.warn(`Character not found: ${characterId}`);
            return this;
        }
        
        this.player.characterId = characterId;
        this.player.id = char.id || characterId;
        this.player.tags = char.tags || char.ontology?.tags || [];
        this.player.name = char.name || char.character?.name || 'Player';
        
        // Load inventory (array of item IDs or objects)
        this.player.inventory = char.inventory || char.character?.inventory || [];
        
        // Load currencies (gold & moolah)
        this.player.gold = char.gold ?? char.character?.gold ?? 100;
        this.player.moolah = char.moolah ?? char.character?.moolah ?? 200;
        
        // Attach helper methods for guard closures (parallel-safe signature)
        // These are called as subject.hasTag(), subject.hasItem(), etc.
        const world = this;
        this.player.hasTag = (tag) => this.player.tags?.includes(tag);
        this.player.hasItem = (itemId) => {
            return this.player.inventory?.some(item => {
                const id = typeof item === 'string' ? item : item.id;
                return id === itemId || id?.endsWith('/' + itemId);
            });
        };
        this.player.hasInventoryTag = (tag) => {
            return this.player.inventory?.some(item => {
                const obj = typeof item === 'string' ? world.get(item) : item;
                return obj?.tags?.includes(tag);
            });
        };
        
        console.log(`🎭 Playing as: ${this.player.name}`);
        console.log(`   Tags: [${this.player.tags.join(', ')}]`);
        if (this.player.gold > 0 || this.player.moolah > 0) {
            console.log(`   Wallet: ${this.player.gold} gold 🟡 | ${this.player.moolah} moolah 🪙`);
        }
        
        return this;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // TOKEN PARSING — Parse currency amounts, resolve targets by tag
    // ═══════════════════════════════════════════════════════════════════════════
    //
    // Currency suffixes:
    //   gold: g, gp, go, gol, gold
    //   moolah: m, mo, moo, mool, moola, moolah
    //
    // Target resolution by tag:
    //   "monkey" → find characters in room with "monkey" tag
    //   If 0: error, If 1: use it, If >1: return disambiguation list
    //
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Parse a token that might be currency (e.g., "10gp", "50m", "100gold", "10")
     * Unsuffixed numbers default to gold (adventure-local currency).
     * 
     * Currency types:
     *   gold 🟡  = Adventure-local in-game currency (default)
     *   moolah 🪙 = Global systemic currency (persists across adventures)
     * 
     * @param {string} token - Token to parse
     * @returns {object|null} { amount, currency } or null if not currency
     */
    parseCurrency(token) {
        if (!token) return null;
        
        // Currency suffix patterns (order matters - longer first)
        const patterns = [
            // Gold: g, gp, go, gol, gold
            { regex: /^(\d+)(gold|gol|go|gp|g)$/i, currency: 'gold' },
            // Moolah: m, mo, moo, mool, moola, moolah
            { regex: /^(\d+)(moolah|moola|mool|moo|mo|m)$/i, currency: 'moolah' },
        ];
        
        for (const { regex, currency } of patterns) {
            const match = token.match(regex);
            if (match) {
                return { amount: parseInt(match[1], 10), currency };
            }
        }
        
        // Unsuffixed number defaults to gold (adventure-local currency)
        const bareNumber = token.match(/^(\d+)$/);
        if (bareNumber) {
            return { amount: parseInt(bareNumber[1], 10), currency: 'gold' };
        }
        
        return null;
    }
    
    /**
     * Get blended economic score from all rubrics
     * Returns weighted average of all rubric values (-100 to +100)
     */
    getEconomicScore() {
        // Sync karma rubric with karma value
        this.economicRubrics.karma.value = this.karma;
        
        let totalWeight = 0;
        let weightedSum = 0;
        
        for (const [name, rubric] of Object.entries(this.economicRubrics)) {
            weightedSum += rubric.value * rubric.weight;
            totalWeight += rubric.weight;
        }
        
        return totalWeight > 0 ? weightedSum / totalWeight : 0;
    }
    
    /**
     * Get current exchange rate (rubric-blended)
     * 
     * Multiple rubrics blend to affect the rate:
     *   - karma (40%): Kindness & ethics
     *   - exploration (20%): World discovery  
     *   - completion (20%): Quests & goals
     *   - social (10%): NPC relationships
     *   - creativity (10%): Novel solutions
     * 
     * Blended score +100 → rate 5  (best: 5 gold = 1 moolah)
     * Blended score    0 → rate 10 (neutral)
     * Blended score -100 → rate 20 (worst: 20 gold = 1 moolah)
     * 
     * moolah is the stable anchor (the "Gas" stablecoin, ha).
     * gold's value floats based on how you play across all dimensions.
     * 
     * @returns {number} Current gold:moolah exchange rate
     */
    getExchangeRate() {
        // Config override bypasses rubrics
        if (this.config?.exchange_rate) {
            return this.config.exchange_rate;
        }
        
        // Get blended score from all rubrics
        const score = this.getEconomicScore();
        
        // Score-adjusted rate: base ± score effect
        // score +100 → rate = base * 0.5 = 5 (gold worth more)
        // score -100 → rate = base * 2.0 = 20 (gold worth less)
        const factor = 1 - (score / 200);  // +100→0.5, 0→1.0, -100→1.5
        const rate = Math.round(this.baseExchangeRate * factor);
        
        // Clamp to reasonable bounds
        return Math.max(2, Math.min(50, rate));
    }
    
    /**
     * Adjust a specific economic rubric
     * @param {string} rubricName - karma, exploration, completion, social, creativity
     * @param {number} delta - Amount to add (-100 to +100 range)
     * @param {string} reason - Why the rubric changed
     */
    adjustRubric(rubricName, delta, reason = '') {
        const rubric = this.economicRubrics[rubricName];
        if (!rubric) {
            console.warn(`Unknown rubric: ${rubricName}`);
            return null;
        }
        
        const oldValue = rubric.value;
        rubric.value = Math.max(-100, Math.min(100, rubric.value + delta));
        
        // Sync karma property with karma rubric
        if (rubricName === 'karma') {
            this.karma = rubric.value;
        }
        
        if (this.eventLogEnabled && delta !== 0) {
            this.eventLog.push({
                _type: 'rubric',
                ...this.now(),
                rubric: rubricName,
                delta,
                oldValue,
                newValue: rubric.value,
                reason,
                newScore: this.getEconomicScore(),
                newRate: this.getExchangeRate()
            });
        }
        
        return rubric.value;
    }
    
    /**
     * Adjust karma (convenience wrapper for adjustRubric)
     * @param {number} delta - Amount to add (positive = good, negative = bad)
     * @param {string} reason - Why karma changed
     */
    adjustKarma(delta, reason = '') {
        return this.adjustRubric('karma', delta, reason);
    }
    
    /**
     * Adjust exploration rubric (world discovery)
     */
    adjustExploration(delta, reason = '') {
        return this.adjustRubric('exploration', delta, reason);
    }
    
    /**
     * Adjust completion rubric (quests & goals)
     */
    adjustCompletion(delta, reason = '') {
        return this.adjustRubric('completion', delta, reason);
    }
    
    /**
     * Adjust social rubric (NPC relationships)
     */
    adjustSocial(delta, reason = '') {
        return this.adjustRubric('social', delta, reason);
    }
    
    /**
     * Adjust creativity rubric (novel solutions)
     */
    adjustCreativity(delta, reason = '') {
        return this.adjustRubric('creativity', delta, reason);
    }
    
    /**
     * Exchange gold for moolah (adventure-local → global anchor)
     * Rate depends on karma — play well, your gold is worth more.
     * @param {number} goldAmount - Amount of gold to exchange
     * @returns {object} { success, goldSpent, moolahReceived, rate, karma, error }
     */
    exchangeGoldForMoolah(goldAmount) {
        const rate = this.getExchangeRate();
        
        if (goldAmount <= 0) {
            return { success: false, error: "Amount must be positive." };
        }
        if (this.player.gold < goldAmount) {
            return { success: false, error: `You only have ${this.player.gold} gold.` };
        }
        
        const moolahReceived = Math.floor(goldAmount / rate);
        if (moolahReceived < 1) {
            return { success: false, error: `Need at least ${rate} gold to get 1 moolah (rate: ${rate}:1, karma: ${this.karma}).` };
        }
        
        const goldSpent = moolahReceived * rate;
        this.player.gold -= goldSpent;
        this.player.moolah += moolahReceived;
        
        return { success: true, goldSpent, moolahReceived, rate, karma: this.karma };
    }
    
    /**
     * Exchange moolah for gold (global anchor → adventure-local)
     * moolah→gold always uses same rate (moolah is stable).
     * @param {number} moolahAmount - Amount of moolah to exchange
     * @returns {object} { success, moolahSpent, goldReceived, rate, error }
     */
    exchangeMoolahForGold(moolahAmount) {
        const rate = this.getExchangeRate();
        
        if (moolahAmount <= 0) {
            return { success: false, error: "Amount must be positive." };
        }
        if (this.player.moolah < moolahAmount) {
            return { success: false, error: `You only have ${this.player.moolah} moolah.` };
        }
        
        const goldReceived = moolahAmount * rate;
        this.player.moolah -= moolahAmount;
        this.player.gold += goldReceived;
        
        return { success: true, moolahSpent: moolahAmount, goldReceived, rate };
    }
    
    /**
     * Find characters in room matching a tag or name pattern
     * Returns: { found, matches, disambiguation }
     * @param {string} query - Tag or name to search for (e.g., "monkey", "cat")
     */
    resolveTarget(query) {
        const charsHere = this.getCharactersHere();
        const queryLower = query.toLowerCase();
        
        // Filter: match by tag, name, or id
        const matches = charsHere.filter(c => {
            if (c.ref === this.player.characterId) return false; // Skip self
            
            // Check tags
            const charData = this.get(c.ref);
            const tags = charData?.tags || [];
            if (tags.some(t => t.toLowerCase().includes(queryLower))) return true;
            
            // Check name
            if (c.name?.toLowerCase().includes(queryLower)) return true;
            
            // Check id
            if (c.id?.toLowerCase().includes(queryLower)) return true;
            
            return false;
        });
        
        if (matches.length === 0) {
            return { found: false, matches: [], error: `No "${query}" here.` };
        }
        
        if (matches.length === 1) {
            return { found: true, matches, target: matches[0] };
        }
        
        // Multiple matches - need disambiguation
        const disambiguation = matches.map(c => {
            const charData = this.get(c.ref);
            const desc = charData?.character?.description || charData?.description || '';
            const shortDesc = desc.split('\n')[0].slice(0, 60) || c.name;
            return { name: c.name, ref: c.ref, description: shortDesc };
        });
        
        return { 
            found: true, 
            matches, 
            needsDisambiguation: true,
            disambiguation,
            error: `Which ${query}?\n` + disambiguation.map(d => `  • ${d.name}: ${d.description}`).join('\n')
        };
    }
    
    /**
     * Give currency to a target (parsed from tokens like "10gp to monkey")
     * @param {string} currencyToken - e.g., "10gp", "50moolah"
     * @param {string} targetQuery - e.g., "monkey", "marieke"
     */
    giveMoney(currencyToken, targetQuery) {
        const parsed = this.parseCurrency(currencyToken);
        if (!parsed) {
            return { success: false, error: `"${currencyToken}" is not a valid currency amount.` };
        }
        
        const { amount, currency } = parsed;
        
        // Resolve target
        const resolution = this.resolveTarget(targetQuery);
        if (!resolution.found) {
            return { success: false, error: resolution.error };
        }
        if (resolution.needsDisambiguation) {
            return { success: false, error: resolution.error, disambiguation: resolution.disambiguation };
        }
        
        const target = resolution.target;
        const targetData = this.get(target.ref);
        
        // Check if player has enough
        if (!this.has(currency, amount)) {
            return { success: false, error: `You don't have ${amount} ${currency}.` };
        }
        
        // Transfer money
        return this.action('give.money', { amount, currency, to: target.ref }, () => {
            // Deduct from player
            this.player[currency] = (this.player[currency] || 0) - amount;
            
            // Add to target
            targetData[currency] = (targetData[currency] || 0) + amount;
            
            // Log transaction
            this.logTransaction(this.player.characterId, target.ref, currency, amount, `gift`);
            this.recordFlow(this.player.characterId, target.ref, currency, amount);
            
            return { 
                success: true, 
                data: { 
                    amount, 
                    currency, 
                    recipient: target.name,
                    recipientId: target.ref
                } 
            };
        });
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // CURRENCY API — Generic payment system
    // ═══════════════════════════════════════════════════════════════════════════
    //
    // world.has(currency, amount)           — Check if player can afford
    // world.pay(currency, amount, reason, to)  — Player pays someone
    // world.earn(currency, amount, reason, from) — Player receives payment
    // world.balance(currency?)              — Get player balance
    //
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Check if player has enough of a currency (query, no action logged)
     * @param {string} currency - 'gold' or 'moolah'
     * @param {number} amount - Amount to check
     */
    has(currency, amount) {
        return (this.player[currency] || 0) >= amount;
    }
    
    /**
     * Get player balance
     * @param {string} currency - 'gold', 'moolah', or null for both
     */
    balance(currency = null) {
        if (currency) {
            return this.player[currency] || 0;
        }
        return {
            gold: this.player.gold || 0,
            moolah: this.player.moolah || 0,
            total: (this.player.gold || 0) + (this.player.moolah || 0)
        };
    }
    
    /**
     * player.pay — Deduct currency from player, give to recipient
     * @param {string} currency - 'gold' or 'moolah'
     * @param {number} amount - Amount to pay
     * @param {string} reason - Why (for ledger)
     * @param {string} to - Recipient (default: 'world')
     * @returns {boolean} success
     */
    pay(currency, amount, reason = 'payment', to = 'world') {
        return this.action('player.pay', { currency, amount, to, reason }, () => {
            return this.transfer('player', to, currency, amount, reason);
        }).success;
    }
    
    /**
     * player.earn — Add currency to player from source
     * @param {string} currency - 'gold' or 'moolah'
     * @param {number} amount - Amount to receive
     * @param {string} reason - Why (for ledger)
     * @param {string} from - Source (default: 'world')
     * @returns {number|false} New balance or false if failed
     */
    earn(currency, amount, reason = 'reward', from = 'world') {
        const result = this.action('player.earn', { currency, amount, from, reason }, () => {
            return this.transfer(from, 'player', currency, amount, reason);
        });
        return result.success ? this.player[currency] : false;
    }
    
    /**
     * Charge player — Shorthand for pay with validation message
     * @param {string} currency - 'gold' or 'moolah'
     * @param {number} amount - Amount to charge
     * @param {string} reason - Why
     * @param {string} to - Recipient (default: 'world')
     * @returns {{ success: boolean, message: string }}
     */
    charge(currency, amount, reason, to = 'world') {
        if (!this.has(currency, amount)) {
            return { 
                success: false, 
                message: `Insufficient ${currency}: need ${amount}, have ${this.player[currency] || 0}` 
            };
        }
        const paid = this.pay(currency, amount, reason, to);
        return { 
            success: paid, 
            message: paid ? `Paid ${amount} ${currency}` : 'Payment failed' 
        };
    }
    
    /**
     * Get recent transactions from ledger
     * @param {number} limit - How many to return (default: 10)
     */
    getTransactions(limit = 10) {
        return this.ledger.slice(-limit).reverse();
    }
    
    /**
     * Format transaction history for display
     */
    transactionHistory(limit = 10) {
        const txs = this.getTransactions(limit);
        
        if (txs.length === 0) {
            return "📒 No transactions yet.";
        }
        
        let report = `📒 TRANSACTION LEDGER (last ${txs.length})\n`;
        report += '─'.repeat(60) + '\n';
        
        for (const tx of txs) {
            const time = tx.time || new Date(tx.timestamp).toISOString();
            const elapsed = tx.elapsed !== undefined ? this.formatElapsed(tx.elapsed) : '';
            const emoji = tx.currency === 'gold' ? '🟡' : '🪙';
            const fromName = this._txEntityName(tx.from);
            const toName = this._txEntityName(tx.to);
            report += `#${tx.id} ${time}${elapsed ? ` (+${elapsed})` : ''}\n`;
            report += `   ${fromName} → ${toName}: ${tx.amount} ${tx.currency} ${emoji}\n`;
            report += `   "${tx.reason}"\n`;
        }
        
        return report.trim();
    }
    
    /**
     * Get display name for transaction entity
     */
    _txEntityName(entityId) {
        if (entityId === 'player') return `You (${this.player.name})`;
        if (entityId === 'world') return 'The World';
        if (entityId === 'system') return 'System';
        if (entityId === 'void') return 'Void';
        const entity = this.get(entityId);
        return entity?.name || entityId.split('/').pop();
    }
    
    /**
     * Get display name for location (room, inventory, character)
     */
    _locationName(loc) {
        if (!loc) return '???';
        if (loc === 'inventory' || loc === 'player') return 'your inventory';
        if (loc === 'void' || loc === 'destroyed') return 'void';
        if (loc === 'world' || loc === 'system') return 'the world';
        
        // Try to resolve as entity
        const entity = this.get(loc);
        if (entity?.name) {
            if (loc.startsWith('room/')) return entity.name;
            if (loc.startsWith('character/')) return `${entity.name}'s inventory`;
        }
        
        // Fallback to readable ID
        return loc.split('/').pop().replace(/-/g, ' ');
    }
    
    /**
     * Analyze the world economy — currencies, wealth distribution, fun stats
     */
    analyzeEconomy() {
        const chars = Object.entries(this.registry)
            .filter(([id]) => id.startsWith('character/'))
            .map(([id, obj]) => ({
                id,
                name: obj.name || id.split('/').pop(),
                gold: obj.gold || 0,
                moolah: obj.moolah || 0,
                total: (obj.gold || 0) + (obj.moolah || 0),
                tags: obj.tags || [],
                species: obj.species || 'unknown'
            }));
        
        // Basic totals
        const totalGold = chars.reduce((sum, c) => sum + c.gold, 0);
        const totalMoolah = chars.reduce((sum, c) => sum + c.moolah, 0);
        const totalWealth = totalGold + totalMoolah;
        
        // Sort by wealth
        const byWealth = [...chars].sort((a, b) => b.total - a.total);
        const richest = byWealth.slice(0, 5);
        const poorest = byWealth.slice(-3).reverse();
        
        // Species wealth
        const speciesWealth = {};
        chars.forEach(c => {
            const sp = c.species || 'unknown';
            if (!speciesWealth[sp]) speciesWealth[sp] = { gold: 0, moolah: 0, count: 0 };
            speciesWealth[sp].gold += c.gold;
            speciesWealth[sp].moolah += c.moolah;
            speciesWealth[sp].count++;
        });
        
        // Category wealth (by tag)
        const categoryWealth = { animals: 0, humans: 0, fictional: 0, abstract: 0 };
        chars.forEach(c => {
            if (c.tags.includes('animals')) categoryWealth.animals += c.total;
            if (c.tags.includes('human') || c.species === 'human') categoryWealth.humans += c.total;
            if (c.tags.includes('fictional')) categoryWealth.fictional += c.total;
            if (c.tags.includes('abstract')) categoryWealth.abstract += c.total;
        });
        
        // Fun stats
        const avgWealth = Math.round(totalWealth / chars.length);
        const medianWealth = byWealth[Math.floor(chars.length / 2)]?.total || 0;
        const giniIndex = this._calculateGini(byWealth.map(c => c.total));
        
        // Gold vs Moolah preference
        const goldPreferrers = chars.filter(c => c.gold > c.moolah).length;
        const moolahPreferrers = chars.filter(c => c.moolah > c.gold).length;
        
        return {
            population: chars.length,
            totalGold,
            totalMoolah,
            totalWealth,
            avgWealth,
            medianWealth,
            giniIndex,
            richest,
            poorest,
            speciesWealth,
            categoryWealth,
            goldPreferrers,
            moolahPreferrers,
            chars  // Full data for deeper analysis
        };
    }
    
    /**
     * Calculate Gini coefficient (0 = perfect equality, 1 = total inequality)
     */
    _calculateGini(values) {
        if (values.length === 0) return 0;
        const sorted = [...values].sort((a, b) => a - b);
        const n = sorted.length;
        const sum = sorted.reduce((a, b) => a + b, 0);
        if (sum === 0) return 0;
        
        let numerator = 0;
        sorted.forEach((val, i) => {
            numerator += (2 * (i + 1) - n - 1) * val;
        });
        return Math.round((numerator / (n * sum)) * 100) / 100;
    }
    
    /**
     * Format economy report for display
     */
    economyReport() {
        const e = this.analyzeEconomy();
        
        let report = `
╔═══════════════════════════════════════════════════════════════════╗
║  💰 Adventure 4 ECONOMY REPORT 💰                           ║
╚═══════════════════════════════════════════════════════════════════╝

📊 OVERVIEW
   Population: ${e.population} characters
   Total Gold: ${e.totalGold.toLocaleString()} 🟡
   Total Moolah: ${e.totalMoolah.toLocaleString()} 🪙
   Combined Wealth: ${e.totalWealth.toLocaleString()}

📈 WEALTH DISTRIBUTION
   Average: ${e.avgWealth.toLocaleString()} per character
   Median: ${e.medianWealth.toLocaleString()}
   Gini Index: ${e.giniIndex} (0=equal, 1=unequal)
   ${e.giniIndex < 0.3 ? '✨ Fairly equal society!' : e.giniIndex < 0.5 ? '⚖️ Moderate inequality' : '⚠️ High inequality!'}

🏆 RICHEST CHARACTERS
${e.richest.map((c, i) => `   ${i + 1}. ${c.name.padEnd(22)} ${c.gold} 🟡 + ${c.moolah} 🪙 = ${c.total}`).join('\n')}

😢 POOREST CHARACTERS
${e.poorest.map(c => `   • ${c.name.padEnd(22)} ${c.gold} 🟡 + ${c.moolah} 🪙 = ${c.total}`).join('\n')}

🐾 WEALTH BY SPECIES`;
        
        Object.entries(e.speciesWealth)
            .sort((a, b) => (b[1].gold + b[1].moolah) - (a[1].gold + a[1].moolah))
            .slice(0, 6)
            .forEach(([species, data]) => {
                const total = data.gold + data.moolah;
                const avg = Math.round(total / data.count);
                report += `\n   ${species.padEnd(12)} ${data.count} chars, ${total} total (avg ${avg})`;
            });
        
        report += `

💱 CURRENCY PREFERENCES
   Gold lovers: ${e.goldPreferrers} characters prefer 🟡
   Moolah fans: ${e.moolahPreferrers} characters prefer 🪙
   ${e.moolahPreferrers > e.goldPreferrers ? '📱 Modern economy!' : '🏰 Traditional values!'}

🎲 YOUR STANDING
   You (${this.player.name}): ${this.player.gold} 🟡 + ${this.player.moolah} 🪙 = ${this.player.gold + this.player.moolah}
   Rank: ${e.chars.filter(c => c.total > this.player.gold + this.player.moolah).length + 1} of ${e.population}
`;
        
        return report.trim();
    }
    
    /**
     * Get characters present in current room
     * Includes: character/ refs, objects with type: npc
     */
    getCharactersHere() {
        const room = this.room;
        if (!room) return [];
        const roomId = room.id;
        
        const results = [];
        const seen = new Set();
        
        // Characters listed in room's characters array
        const charRefs = room.characters || [];
        for (const ref of charRefs) {
            if (seen.has(ref)) continue;
            seen.add(ref);
            const char = this.get(ref);
            if (char) results.push({ ...char, ref });
        }
        
        // Also check contents if it's an array of character refs
        if (Array.isArray(room.contents)) {
            const contentChars = room.contents.filter(c => 
                typeof c === 'string' && c.startsWith('character/')
            );
            for (const ref of contentChars) {
                if (seen.has(ref)) continue;
                seen.add(ref);
                const char = this.get(ref);
                if (char) results.push({ ...char, ref });
            }
        }
        
        // Also find objects with type: npc that are in this room
        // (NPCs can be defined as objects rather than characters)
        for (const [id, obj] of Object.entries(this.registry)) {
            if (seen.has(id)) continue;
            if (obj.type !== 'npc') continue;
            
            // Check if this NPC is in the current room (using location chain)
            if (this.isInRoom(obj, roomId)) {
                seen.add(id);
                results.push({ ...obj, ref: id });
            }
        }
        
        return results;
    }
    
    /**
     * Switch to playing as another character in the same room
     * @param {string} nameOrId - character name or ID
     */
    become(nameOrId) {
        const charsHere = this.getCharactersHere();
        
        if (charsHere.length === 0) {
            return "There's no one else here you can become.";
        }
        
        // Find by name or ID (case-insensitive)
        const search = nameOrId.toLowerCase();
        const target = charsHere.find(c => 
            c.name?.toLowerCase() === search ||
            c.id?.toLowerCase() === search ||
            c.ref?.toLowerCase().includes(search)
        );
        
        if (!target) {
            const names = charsHere.map(c => c.name || c.id).join(', ');
            return `No one called "${nameOrId}" is here.\n\nCharacters present: ${names}`;
        }
        
        // Can't become yourself
        if (target.ref === this.player.characterId) {
            return `You're already ${this.player.name}!`;
        }
        
        // Switch!
        const oldName = this.player.name;
        this.setPlayer(target.ref);
        
        return `🎭 You are now ${this.player.name}.\n\n` +
               `(Was: ${oldName})\n` +
               `Tags: [${this.player.tags.join(', ')}]\n\n` +
               this.look();
    }
    
    /**
     * List who's here
     */
    who() {
        const charsHere = this.getCharactersHere();
        
        if (charsHere.length === 0) {
            return "You're alone here.";
        }
        
        const lines = ['Characters present:'];
        for (const char of charsHere) {
            const isYou = char.ref === this.player.characterId;
            const tags = char.tags?.slice(0, 3).join(', ') || 'no tags';
            lines.push(`  ${char.name || char.id}${isYou ? ' (you)' : ''} [${tags}]`);
        }
        lines.push('');
        lines.push('Type BECOME <name> to switch characters.');
        
        return lines.join('\n');
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // LOADING
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Load world data from JSON
     * Supports typed table format (v3.0.0+): room, character, object, slideshow, catalog
     */
    load(worldData) {
        this.registry = {};
        
        // Handle typed table format: room, character, object, slideshow, catalog
        // IDs in the table are the full registry keys (e.g., character/real-people/don-hopkins)
        const TYPED_TABLES = ['room', 'character', 'object', 'slideshow', 'catalog'];
        for (const type of TYPED_TABLES) {
            if (worldData[type]) {
                for (const [id, obj] of Object.entries(worldData[type])) {
                    // IDs already have type prefix for character/object, but not for room
                    const key = id.startsWith(type + '/') ? id : `${type}/${id}`;
                    this.registry[key] = obj;
                }
            }
        }
        
        this.config = worldData.config || {};
        
        // Set starting location (prefix with room/ if needed)
        let startRoom = this.config.starting_room || 'pub';
        if (!startRoom.startsWith('room/')) {
            startRoom = 'room/' + startRoom;
        }
        this.player.location = startRoom;
        
        // Initialize location history with starting room
        this.player.locationHistory = [startRoom];
        this.player.historyIndex = 0;
        
        // Compile actions
        this.compileActions();
        
        console.log('🎮 Adventure 4 loaded!');
        console.log(`   ${Object.keys(this.registry).length} objects in registry`);
        console.log(`   Starting at: ${this.player.location}`);
        
        return this;
    }
    
    /**
     * Compile action code strings into closures
     */
    compileActions() {
        for (const [key, obj] of Object.entries(this.registry)) {
            if (key.startsWith('action/') && obj.code) {
                try {
                    this.actions[key] = eval(obj.code);
                } catch (e) {
                    console.warn(`Failed to compile action ${key}:`, e);
                }
            }
        }
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // REGISTRY ACCESS
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Get object by type/id reference
     * Supports sub-object: "room/pub#exits"
     * Auto-prefixes room/ for bare paths (exit destinations)
     */
    get(ref) {
        if (!ref) return null;
        
        const [path, subkey] = ref.split('#');
        let obj = this.registry[path];
        
        // Try with room/ prefix if not found (for exit destinations)
        if (!obj && !path.includes('/')) {
            obj = this.registry['room/' + path];
        }
        if (!obj && !path.startsWith('room/')) {
            obj = this.registry['room/' + path];
        }
        
        if (!obj) return null;
        if (subkey) return obj[subkey];
        return obj;
    }
    
    /**
     * Get all objects of a type
     */
    getByType(type) {
        return Object.entries(this.registry)
            .filter(([key]) => key.startsWith(`${type}/`))
            .map(([key, obj]) => obj);
    }
    
    /**
     * Get current room
     */
    get room() {
        return this.get(this.player.location);
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // FLAGS & STATE
    // ═══════════════════════════════════════════════════════════════════════════
    
    setFlag(name, value = true) {
        this.flags[name] = value;
    }
    
    getFlag(name) {
        return this.flags[name] || false;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // TEXT RESOLUTION
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Resolve polymorphic text field
     * Priority: {key}_js (closure) > {key} (string|array)
     * Caches compiled functions in {key}_js_fn
     * @param {object} obj - Object containing text fields
     * @param {string} key - Base key name (e.g., 'accept_message')
     * @returns {string|null}
     */
    resolveText(obj, key) {
        const jsKey = `${key}_js`;
        const fnKey = `${key}_js_fn`;
        
        // Priority 1: compiled closure
        if (obj[jsKey]) {
            try {
                // Cache compiled function
                if (!obj[fnKey]) {
                    obj[fnKey] = eval(`(function(world, player, room) { ${obj[jsKey]} })`);
                }
                
                // Execute cached function with context
                return obj[fnKey](this, this.player, this.room);
            } catch (e) {
                console.warn(`resolveText eval failed for ${jsKey}:`, e);
            }
        }
        
        // Priority 2: static value
        const val = obj[key];
        if (!val) return null;
        
        // Array → random pick
        if (Array.isArray(val)) {
            return val[Math.floor(Math.random() * val.length)];
        }
        
        // String → as-is
        return typeof val === 'string' ? val : null;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // NAVIGATION
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Move player to a location with history tracking (browser back/forward style)
     * 
     * History model: locationHistory contains ALL visited locations including current.
     * historyIndex points to current position. Back decrements, forward increments.
     * 
     * @param {string} newLocation - The room ID to move to
     * @param {boolean} addToHistory - Whether to add to history (false for back/forward nav)
     * @returns {string} The look description of the new room
     */
    goToLocation(newLocation, addToHistory = true) {
        // Normalize location
        const normalizedLocation = newLocation.startsWith('room/') ? newLocation : 'room/' + newLocation;
        
        if (addToHistory) {
            // If we're in the middle of history and navigating to new place,
            // truncate forward history (like browser does)
            if (this.player.historyIndex >= 0 && this.player.historyIndex < this.player.locationHistory.length - 1) {
                this.player.locationHistory = this.player.locationHistory.slice(0, this.player.historyIndex + 1);
            }
            
            // Add new location to history
            this.player.locationHistory.push(normalizedLocation);
            this.player.historyIndex = this.player.locationHistory.length - 1;
        }
        
        // Update location
        this.player.location = normalizedLocation;
        
        return this.look();
    }
    
    /**
     * Go back to previous location in history
     */
    goBack() {
        if (this.player.locationHistory.length <= 1) {
            return "No previous location. You're at the beginning of your journey.";
        }
        
        if (this.player.historyIndex <= 0) {
            return "No previous location. You're at the beginning of your journey.";
        }
        
        // Move back in history
        this.player.historyIndex--;
        const prevLocation = this.player.locationHistory[this.player.historyIndex];
        this.player.location = prevLocation;
        
        const historyInfo = `[${this.player.historyIndex + 1}/${this.player.locationHistory.length}]`;
        return `${historyInfo}\n\n${this.look()}`;
    }
    
    /**
     * Go forward in history (redo navigation)
     */
    goForward() {
        if (this.player.historyIndex >= this.player.locationHistory.length - 1) {
            return "No forward history. You're at the most recent location.";
        }
        
        // Move forward in history
        this.player.historyIndex++;
        const nextLocation = this.player.locationHistory[this.player.historyIndex];
        this.player.location = nextLocation;
        
        const historyInfo = `[${this.player.historyIndex + 1}/${this.player.locationHistory.length}]`;
        return `${historyInfo}\n\n${this.look()}`;
    }
    
    /**
     * Navigate to a room via exit direction
     */
    go(direction) {
        const room = this.room;
        if (!room) {
            return "You're nowhere. That's concerning.";
        }
        
        const dir = direction.toLowerCase();
        let exit = room.exits?.[dir];
        
        // Check aliases (also check UPPER case for consistency)
        if (!exit) {
            exit = room.exits?.[dir.toUpperCase()];
        }
        if (!exit) {
            for (const [exitDir, ex] of Object.entries(room.exits || {})) {
                // Defensive: ensure aliases are strings before toLowerCase
                const aliases = Array.isArray(ex.aliases) 
                    ? ex.aliases.filter(a => typeof a === 'string').map(a => a.toLowerCase())
                    : [];
                if (aliases.includes(dir)) {
                    exit = ex;
                    break;
                }
            }
        }
        
        if (!exit) {
            const exitList = Object.keys(room.exits || {}).join(', ');
            return `You can't go "${direction}" from here.\n\nExits: ${exitList}`;
        }
        
        // Check if locked
        if (exit.locked) {
            const msg = this.resolveText(exit, 'reject_message');
            return msg || "The way is locked.";
        }
        
        // Check guard condition
        if (exit.guard_js) {
            try {
                // Cache compiled guard function for JIT optimization
                if (!exit.guard_js_fn) {
                    exit.guard_js_fn = this.compileJs(exit.guard_js);
                }
                
                // Set exit_id on world for cumulative probability tracking
                this.exit_id = `${this.player.location}:${dir}`;
                
                // Execute guard with parallel-safe signature
                // world = this (shared state), subject = player, verb = 'go', object = exit
                const passed = exit.guard_js_fn(this, this.player, 'go', exit);
                if (!passed) {
                    const msg = exit.fail_message || this.resolveText(exit, 'reject_message');
                    return msg || "You can't go that way.";
                }
                
                // Show pass message if present
                if (exit.pass_message) {
                    console.log(exit.pass_message);
                }
            } catch (e) {
                console.warn(`Guard eval failed for ${dir}:`, e);
            }
        }
        
        // Check if blocked
        if (exit.blocked) {
            const msg = this.resolveText(exit, 'reject_message');
            return msg || "You can't go that way right now.";
        }
        
        // Check destination exists
        const destination = this.get(exit.to);
        if (!destination || !exit.to || exit.to === 'TODO') {
            const msg = this.resolveText(exit, 'reject_message');
            return msg || "You can't go that way right now. The path isn't ready.";
        }
        
        // Get accept message before moving
        const acceptMsg = this.resolveText(exit, 'accept_message');
        
        // Move player with history tracking
        const lookResult = this.goToLocation(exit.to, true);
        
        // Return accept message + new room description
        if (acceptMsg) {
            return `${acceptMsg}\n\n${lookResult}`;
        }
        return lookResult;
    }
    
    /**
     * Look at current room
     */
    look() {
        const room = this.room;
        if (!room) {
            return "You're in the void. This shouldn't happen.";
        }
        
        const parts = [];
        
        // Room name
        parts.push(`═══ ${room.name} ═══`);
        parts.push('');
        
        // Description
        parts.push(room.description || 'You see nothing special.');
        parts.push('');
        
        // Contents (objects)
        if (room.contents?.length > 0) {
            parts.push('You see:');
            for (const objRef of room.contents) {
                const obj = this.get(objRef);
                if (obj) {
                    parts.push(`  • ${obj.name || objRef}`);
                }
            }
            parts.push('');
        }
        
        // Exits
        const exits = room.exits || {};
        if (Object.keys(exits).length > 0) {
            parts.push('Exits:');
            for (const [dir, exit] of Object.entries(exits)) {
                const desc = exit.description || `Exit ${dir}`;
                // Truncate long descriptions
                const shortDesc = desc.split('\n')[0].substring(0, 60);
                parts.push(`  ${dir.toUpperCase()}: ${shortDesc}`);
            }
        } else {
            parts.push('No obvious exits.');
        }
        
        // Add room objects (glance level)
        const objectsList = this.listRoomObjects();
        if (objectsList) {
            parts.push(objectsList);
        }
        
        return parts.join('\n');
    }
    
    /**
     * Get objects located in the current room
     * Walks up location chain to find objects inside containers inside room
     */
    getRoomObjects() {
        const roomId = this.room?.id;
        if (!roomId) return [];
        
        const objects = [];
        for (const [id, obj] of Object.entries(this.registry)) {
            if (!id.startsWith('object/')) continue;
            if (obj.location === 'inventory') continue; // Skip items in player inventory
            
            // Walk up location chain to find containing room
            if (this.isInRoom(obj, roomId)) {
                objects.push(obj);
            }
        }
        return objects;
    }
    
    /**
     * Check if an object is in a room (directly or inside a container in the room)
     * Walks up location chain, checking for ROOM interface at each level
     * 
     * Handles:
     * - Direct placement: obj.location === roomId
     * - Containers: obj → chest → room
     * - Vehicles: rooms with location pointers (ship cabin moves with ship)
     * - Nested: obj → bag → chest → room
     * 
     * Special states:
     * - Self-reference (loc === id): "In your own head" - floating inside yourself,
     *   OUTSIDE the world. Valid meditative state. Not in any room.
     * - Circular chains: A→B→A - prevented by visited set
     */
    isInRoom(obj, roomId, visited = new Set()) {
        if (!obj || !obj.location) return false;
        
        const loc = obj.location;
        
        // Self-reference: "In your own head" - you're floating inside yourself,
        // outside the world. Not in any room. Valid meditative/introspective state.
        if (loc === obj.id) return false;
        
        // Prevent infinite loops from circular chains (A→B→A)
        if (visited.has(loc)) return false;
        if (obj.id && visited.has(obj.id)) return false;
        
        visited.add(loc);
        if (obj.id) visited.add(obj.id);
        
        // Direct match - object's location IS this room
        if (loc === roomId) return true;
        
        // Check if location is a room path (with or without room/ prefix)
        const normalizedLoc = loc.startsWith('room/') ? loc : 'room/' + loc;
        if (normalizedLoc === roomId) return true;
        
        // Look up the container/parent at this location
        const parent = this.registry[loc] || 
                       this.registry['object/' + loc] ||
                       this.registry['room/' + loc];
        
        if (!parent) return false;
        
        // If parent has a location, recurse up the chain
        if (parent.location) {
            return this.isInRoom(parent, roomId, visited);
        }
        
        // If parent IS a room (has id matching room pattern), check if it's our room
        if (parent.id === roomId || 'room/' + parent.id === roomId) {
            return true;
        }
        
        return false;
    }
    
    /**
     * Find an object in the current room by name or synonym
     */
    findRoomObject(query) {
        const q = query.toLowerCase().trim();
        const objects = this.getRoomObjects();
        
        // Exact ID match
        for (const obj of objects) {
            if (obj.id.toLowerCase().endsWith('/' + q)) return obj;
        }
        
        // Name match
        for (const obj of objects) {
            if (obj.name?.toLowerCase() === q) return obj;
        }
        
        // Synonym match
        for (const obj of objects) {
            if (obj.synonyms?.some(s => s.toLowerCase() === q)) return obj;
        }
        
        // Partial name match
        for (const obj of objects) {
            if (obj.name?.toLowerCase().includes(q)) return obj;
        }
        
        // Partial synonym match
        for (const obj of objects) {
            if (obj.synonyms?.some(s => s.toLowerCase().includes(q))) return obj;
        }
        
        return null;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // OBJECT LOD (Level of Detail) — glance → look → examine
    // Each supports polymorphic text: field → field_js → field_js_fn (cached)
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Resolve polymorphic text field with caching
     * Pattern: field → field_js → field_js_fn (compiled & cached)
     * 
     * @param {object} obj - Object with the field
     * @param {string} field - Base field name (e.g., 'glance', 'description', 'examine')
     * @param {string} fallback - Fallback text if field not found
     * @returns {string} Resolved text
     */
    resolveObjectText(obj, field, fallback = '') {
        // 1. Check for static text
        if (obj[field]) {
            return obj[field];
        }
        
        // 2. Check for dynamic _js version
        const jsField = `${field}_js`;
        if (obj[jsField]) {
            // Check cache first
            const fnField = `${field}_js_fn`;
            if (!obj[fnField]) {
                try {
                    // Compile and cache
                    obj[fnField] = eval(obj[jsField]);
                } catch (e) {
                    console.warn(`Failed to compile ${jsField}:`, e);
                    return fallback;
                }
            }
            // Execute cached function
            try {
                return obj[fnField](this, obj);
            } catch (e) {
                console.warn(`Failed to execute ${fnField}:`, e);
                return fallback;
            }
        }
        
        return fallback;
    }
    
    /**
     * GLANCE — Briefest description (for room listings, quick looks)
     * Falls back to: glance → name → id
     */
    glanceObject(obj) {
        const text = this.resolveObjectText(obj, 'glance', '');
        if (text) return text;
        
        // Fallback: name or derive from id
        if (obj.name) return obj.name;
        return obj.id?.split('/').pop()?.replace(/-/g, ' ') || 'something';
    }
    
    /**
     * LOOK — Normal description (default interaction)
     * Falls back to: description → glance → name
     */
    lookObject(obj) {
        const text = this.resolveObjectText(obj, 'description', '');
        if (text) return text;
        
        // Fallback to glance
        return this.glanceObject(obj);
    }
    
    /**
     * EXAMINE — Full detailed inspection
     * Falls back to: examine → description → glance
     */
    examineObject(obj) {
        let result = `═══ ${obj.name || 'Unknown'} ═══\n\n`;
        
        // Try examine first, then fall back through LOD tree
        let text = this.resolveObjectText(obj, 'examine', '');
        if (!text) {
            text = this.resolveObjectText(obj, 'description', '');
        }
        if (!text) {
            text = this.resolveObjectText(obj, 'glance', '');
        }
        if (!text) {
            text = `A ${(obj.name || 'thing').toLowerCase()}.`;
        }
        
        result += text;
        
        // For dreams, show link to full dream and metadata
        if (obj._is_dream) {
            result += '\n\n────────────────────────────────────────────';
            if (obj._dream_meta) {
                const meta = obj._dream_meta;
                if (meta.date) result += `\n📅 Date: ${meta.date}`;
                if (meta.type) result += `\n🏷️ Type: ${meta.type}`;
                if (meta.subject) result += `\n💭 Subject: ${meta.subject}`;
                if (meta.mood) result += `\n🎭 Mood: ${meta.mood}`;
            }
            if (obj._dream_url) {
                result += `\n\n📖 Full dream: ${obj._dream_url}`;
            }
        }
        
        // Show value if non-zero (economy info)
        if (obj.value > 0) {
            const emoji = (obj.currency === 'moolah') ? '🪙' : '🟡';
            result += `\n\nValue: ${obj.value} ${obj.currency || 'gold'} ${emoji}`;
        }
        
        // Show methods/actions if present
        if (obj.methods && typeof obj.methods === 'object') {
            const methodNames = Object.keys(obj.methods);
            if (methodNames.length > 0) {
                result += `\n\nActions: ${methodNames.join(', ')}`;
            }
        }
        
        return result;
    }
    
    /**
     * List objects in room with glance-level descriptions
     */
    listRoomObjects() {
        const objects = this.getRoomObjects();
        if (objects.length === 0) return '';
        
        const lines = ['', 'You can see:'];
        for (const obj of objects) {
            const glance = this.glanceObject(obj);
            const emoji = obj.emoji || '•';
            lines.push(`  ${emoji} ${glance}`);
        }
        return lines.join('\n');
    }
    
    /**
     * Examine an exit for full description
     */
    examineExit(direction) {
        const room = this.room;
        const dir = direction.toLowerCase();
        const exit = room?.exits?.[dir];
        
        if (!exit) {
            return `There's no exit "${direction}" here.`;
        }
        
        let desc = exit.description || `An exit leading ${direction}.`;
        
        // Check for dynamic description
        if (exit.description_js) {
            try {
                if (!exit.description_js_fn) {
                    exit.description_js_fn = this.compileJs(exit.description_js);
                }
                desc = exit.description_js_fn(this, this.player, 'examine', exit);
            } catch (e) {
                console.warn(`Dynamic description eval failed:`, e);
            }
        }
        
        // Add note if present
        if (exit.note) {
            desc += `\n\n(${exit.note})`;
        }
        
        return desc;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // COMMAND PROCESSING
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Process a text command
     */
    command(input) {
        const parts = input.trim().split(/\s+/);
        const cmd = parts[0].toLowerCase();
        const args = parts.slice(1).join(' ');
        
        // Navigation commands
        const directions = ['north', 'south', 'east', 'west', 'up', 'down', 
                          'n', 's', 'e', 'w', 'u', 'd',
                          'northeast', 'northwest', 'southeast', 'southwest',
                          'ne', 'nw', 'se', 'sw', 'back', 'out', 'in'];
        
        // Direction shortcuts
        const dirMap = {
            'n': 'north', 's': 'south', 'e': 'east', 'w': 'west',
            'u': 'up', 'd': 'down',
            'ne': 'northeast', 'nw': 'northwest', 
            'se': 'southeast', 'sw': 'southwest'
        };
        
        if (directions.includes(cmd)) {
            return this.go(dirMap[cmd] || cmd);
        }
        
        if (cmd === 'go' && args) {
            // History navigation
            const historyArgs = args.toLowerCase();
            if (['back', 'previous', 'prev'].includes(historyArgs)) {
                return this.goBack();
            }
            if (['forward', 'next', 'fwd'].includes(historyArgs)) {
                return this.goForward();
            }
            return this.go(args);
        }
        
        // ═══════════════════════════════════════════════════════════════════════
        // LOD Commands: GLANCE → LOOK → EXAMINE (increasing detail)
        // ═══════════════════════════════════════════════════════════════════════
        
        // GLANCE - Briefest description
        if (['glance', 'gl', 'g'].includes(cmd)) {
            if (!args) {
                // Glance at room objects
                const objects = this.getRoomObjects();
                if (objects.length === 0) return 'Nothing notable here.';
                const lines = objects.map(obj => {
                    const emoji = obj.emoji || '•';
                    return `  ${emoji} ${this.glanceObject(obj)}`;
                });
                return 'You glance around:\n' + lines.join('\n');
            }
            
            // Glance at specific object
            const roomObj = this.findRoomObject(args);
            if (roomObj) {
                return this.glanceObject(roomObj);
            }
            return `You don't see "${args}" here.`;
        }
        
        // LOOK - Normal description (medium detail)
        if (['look', 'l'].includes(cmd)) {
            if (args) {
                // Look at exit
                if (this.room?.exits?.[args.toLowerCase()]) {
                    return this.examineExit(args);
                }
                
                // Look at room object (medium detail)
                const roomObj = this.findRoomObject(args);
                if (roomObj) {
                    const emoji = roomObj.emoji || '';
                    const header = emoji ? `${emoji} ${roomObj.name}` : roomObj.name;
                    return `${header}\n${'─'.repeat(40)}\n${this.lookObject(roomObj)}`;
                }
                
                // Look at inventory object
                const invObj = this.player?.inventory?.find(id => {
                    const obj = this.registry[id];
                    return obj?.name?.toLowerCase().includes(args.toLowerCase());
                });
                if (invObj) {
                    const obj = this.registry[invObj];
                    return `${obj.name}\n${'─'.repeat(40)}\n${this.lookObject(obj)}`;
                }
                
                return `You don't see "${args}" here.`;
            }
            return this.look();
        }
        
        // EXAMINE - Full detailed inspection
        if (['examine', 'x', 'ex'].includes(cmd)) {
            if (!args) return 'Examine what?';
            
            // Check exits
            if (this.room?.exits?.[args.toLowerCase()]) {
                return this.examineExit(args);
            }
            
            // Check room objects (full detail)
            const roomObj = this.findRoomObject(args);
            if (roomObj) {
                return this.examineObject(roomObj);
            }
            
            // Check inventory objects
            const invObj = this.player?.inventory?.find(id => {
                const obj = this.registry[id];
                return obj?.name?.toLowerCase().includes(args.toLowerCase());
            });
            if (invObj) {
                const obj = this.registry[invObj];
                return this.examineObject(obj);
            }
            
            return `You don't see "${args}" here.`;
        }
        
        // Inventory
        if (['inventory', 'inv', 'i'].includes(cmd)) {
            if (this.player.inventory.length === 0) {
                return 'You are empty-handed.';
            }
            return 'You are carrying:\n' + 
                this.player.inventory.map(id => {
                    // Try multiple lookup paths: direct, object/, registry key
                    const obj = this.get(id) || 
                                this.registry[id] || 
                                this.registry['object/' + id];
                    const emoji = obj?.emoji || '•';
                    return `  ${emoji} ${obj?.name || id}`;
                }).join('\n');
        }
        
        // Get/Take object
        if (['get', 'take', 'grab', 'pick'].includes(cmd)) {
            if (!args) return 'Get what?';
            
            // Resolve name to object using findRoomObject (same as examine)
            const obj = this.findRoomObject(args);
            if (!obj) {
                return `You don't see "${args}" here.`;
            }
            
            const result = this.takeObject(obj.id);
            if (result.success) {
                return `You take the ${result.object?.name || args}.`;
            }
            return result.error;
        }
        
        // Drop object
        if (['drop', 'put', 'place'].includes(cmd)) {
            if (!args) return 'Drop what?';
            const result = this.dropObject(args);
            if (result.success) {
                return `You drop the ${result.object?.name || args}.`;
            }
            return result.error;
        }
        
        // Give object OR currency to character
        // Supports: "give 10gp to monkey", "give sword to marieke", "give 50m to cat"
        // Disambiguation: if multiple "monkey" in room, lists them for selection
        //
        // TODO: Support multiple direct objects ("give sword and shield to knight")
        // TODO: "feed cat" with 9 cats in room → same disambiguation
        // TODO: "feed all cats" → batch operation
        //
        if (['give'].includes(cmd)) {
            // Special case: "give me to me" - enter your own head (inventory = inside yourself)
            const argLower = args?.toLowerCase().trim();
            if (argLower === 'me to me' || argLower === 'myself to myself' || 
                argLower === 'me to myself' || argLower === 'myself to me') {
                // You're now inside your own head - your inventory becomes your location
                // This can be recovered with "go back" / "go previous"
                const playerChar = this.get(this.player.characterId);
                const dreamsRoom = playerChar?._dreamsRoom || 'room/characters/real-people/don-hopkins/dreams';
                
                // Check if dreams room exists
                const dreams = this.get(dreamsRoom);
                if (dreams) {
                    const result = this.goToLocation(dreamsRoom, true);
                    return `🧠 You give yourself to yourself...\n\nYou sink inward. The world dissolves.\nYou are now inside your own head.\n\n(Type "go back" to return to where you were)\n\n${result}`;
                }
                
                // Fallback: just set location to self (meditative state)
                return `🧠 You give yourself to yourself...\n\nYou sink inward. But there's no inner world defined.\nYou float in the void of undefined consciousness.\n\n(Type "go back" to return to where you were)`;
            }
            
            // Parse "give item to character" or "give item character"
            const toMatch = args?.match(/(.+?)\s+to\s+(.+)/i);
            const spaceMatch = args?.split(/\s+/);
            
            let itemName, targetName;
            if (toMatch) {
                itemName = toMatch[1].trim();
                targetName = toMatch[2].trim();
            } else if (spaceMatch && spaceMatch.length >= 2) {
                itemName = spaceMatch[0];
                targetName = spaceMatch.slice(1).join(' ');
            } else {
                return 'Give what to whom? Try: GIVE item TO character, or GIVE 10gp TO monkey';
            }
            
            // Check if itemName is currency (e.g., "10gp", "50m", "100gold")
            const currencyParsed = this.parseCurrency(itemName);
            if (currencyParsed) {
                // It's currency - use giveMoney with tag-based resolution
                const result = this.giveMoney(itemName, targetName);
                if (result.success) {
                    const d = result.data;
                    const emoji = d.currency === 'gold' ? '🟡' : '🪙';
                    return `💰 You give ${d.amount} ${d.currency} ${emoji} to ${d.recipient}.`;
                }
                return result.error;
            }
            
            // Not currency - it's an object. Use tag-based target resolution.
            const resolution = this.resolveTarget(targetName);
            if (!resolution.found) {
                return resolution.error;
            }
            if (resolution.needsDisambiguation) {
                return resolution.error; // Lists all matching characters
            }
            
            const target = resolution.target;
            const result = this.giveObject(itemName, target.ref);
            if (result.success) {
                return `You give the ${result.data?.object?.name || itemName} to ${target.name}.`;
            }
            return result.error;
        }
        
        // Sell object to character
        if (['sell'].includes(cmd)) {
            // Parse "sell item to character"
            const toMatch = args?.match(/(.+?)\s+to\s+(.+)/i);
            const spaceMatch = args?.split(/\s+/);
            
            let itemName, targetName;
            if (toMatch) {
                itemName = toMatch[1].trim();
                targetName = toMatch[2].trim();
            } else if (spaceMatch && spaceMatch.length >= 2) {
                itemName = spaceMatch[0];
                targetName = spaceMatch.slice(1).join(' ');
            } else {
                return 'Sell what to whom? Try: SELL item TO character';
            }
            
            // Find target character in room
            const charsHere = this.getCharactersHere();
            const target = charsHere.find(c => 
                c.name?.toLowerCase().includes(targetName.toLowerCase()) ||
                c.id?.toLowerCase().includes(targetName.toLowerCase())
            );
            
            if (!target) {
                return `${targetName} isn't here.`;
            }
            
            const result = this.sellObject(itemName, target.ref);
            if (result.success) {
                const d = result.data;
                const emoji = d.currency === 'gold' ? '🟡' : '🪙';
                return `💰 Sold! ${target.name} buys your ${d.object.name} for ${d.price} ${d.currency} ${emoji}`;
            }
            return result.error;
        }
        
        // Buy object from character
        if (['buy', 'purchase'].includes(cmd)) {
            // Parse "buy item from character"
            const fromMatch = args?.match(/(.+?)\s+from\s+(.+)/i);
            const spaceMatch = args?.split(/\s+/);
            
            let itemName, sellerName;
            if (fromMatch) {
                itemName = fromMatch[1].trim();
                sellerName = fromMatch[2].trim();
            } else if (spaceMatch && spaceMatch.length >= 2) {
                itemName = spaceMatch[0];
                sellerName = spaceMatch.slice(1).join(' ');
            } else {
                return 'Buy what from whom? Try: BUY item FROM character';
            }
            
            // Find seller character in room
            const charsHere = this.getCharactersHere();
            const seller = charsHere.find(c => 
                c.name?.toLowerCase().includes(sellerName.toLowerCase()) ||
                c.id?.toLowerCase().includes(sellerName.toLowerCase())
            );
            
            if (!seller) {
                return `${sellerName} isn't here.`;
            }
            
            const result = this.buyObject(itemName, seller.ref);
            if (result.success) {
                const d = result.data;
                const emoji = d.currency === 'gold' ? '🟡' : '🪙';
                if (d.price === 0) {
                    return `🛒 ${seller.name} gives you the ${d.object.name} for free!`;
                }
                return `🛒 Purchased! You buy ${d.object.name} from ${seller.name} for ${d.price} ${d.currency} ${emoji}`;
            }
            return result.error;
        }
        
        // Appraise object value
        if (['appraise', 'value', 'worth', 'price'].includes(cmd)) {
            if (!args) return 'Appraise what? Try: APPRAISE item';
            
            // Check inventory first
            const invItem = this.player.inventory.find(c => 
                c.includes(args.toLowerCase()) || c === args
            );
            if (invItem) {
                return this.appraiseObject(invItem);
            }
            
            // Check room contents
            const room = this.room;
            if (room?.contents) {
                const roomItem = room.contents.find(c => {
                    if (typeof c === 'string') return c.includes(args.toLowerCase());
                    return c.id?.includes(args.toLowerCase()) || c.ref?.includes(args.toLowerCase());
                });
                if (roomItem) {
                    const itemId = typeof roomItem === 'string' ? roomItem : (roomItem.id || roomItem.ref);
                    return this.appraiseObject(itemId);
                }
            }
            
            return `You don't see "${args}" here.`;
        }
        
        // List items for sale by character
        if (['shop', 'browse', 'merchandise', 'forsale'].includes(cmd)) {
            if (!args) {
                // Show what nearby characters have for sale
                const charsHere = this.getCharactersHere();
                let report = '🏪 NEARBY MERCHANTS\n' + '─'.repeat(40) + '\n';
                let anyItems = false;
                
                for (const char of charsHere) {
                    if (char.ref === this.player.characterId) continue;
                    const items = this.getItemsForSale(char.ref);
                    if (items.length > 0) {
                        anyItems = true;
                        report += `\n${char.name}:\n`;
                        for (const item of items) {
                            const emoji = item.currency === 'gold' ? '🟡' : '🪙';
                            report += `  • ${item.name}: ${item.value} ${item.currency} ${emoji}\n`;
                        }
                    }
                }
                
                if (!anyItems) {
                    return "🏪 Nobody here has anything for sale.";
                }
                return report.trim();
            }
            
            // Show specific character's items
            const charsHere = this.getCharactersHere();
            const target = charsHere.find(c => 
                c.name?.toLowerCase().includes(args.toLowerCase()) ||
                c.id?.toLowerCase().includes(args.toLowerCase())
            );
            
            if (!target) {
                return `${args} isn't here.`;
            }
            
            const items = this.getItemsForSale(target.ref);
            if (items.length === 0) {
                return `${target.name} has nothing for sale.`;
            }
            
            let report = `🏪 ${target.name}'s MERCHANDISE\n` + '─'.repeat(40) + '\n';
            for (const item of items) {
                const emoji = item.currency === 'gold' ? '🟡' : '🪙';
                report += `  • ${item.name}: ${item.value} ${item.currency} ${emoji}\n`;
            }
            report += `\nUse BUY <item> FROM ${target.name} to purchase.`;
            return report.trim();
        }
        
        // Catalog commands
        if (['catalogs', 'catalogues', 'vendors', 'stores'].includes(cmd)) {
            return this.catalogsList();
        }
        
        if (['catalog', 'catalogue'].includes(cmd)) {
            if (!args) return this.catalogsList();
            return this.catalogListing(args);
        }
        
        // Order from catalog
        if (['order'].includes(cmd)) {
            // Parse "order item from catalog"
            const fromMatch = args?.match(/(.+?)\s+from\s+(.+)/i);
            
            if (!fromMatch) {
                return 'Order what from where? Try: ORDER item FROM catalog';
            }
            
            const itemName = fromMatch[1].trim();
            const catalogName = fromMatch[2].trim();
            
            const result = this.orderFromCatalog(catalogName, itemName);
            if (result.success) {
                const d = result.data;
                const emoji = d.currency === 'gold' ? '🟡' : '🪙';
                if (d.price === 0) {
                    return `📦 Your ${d.item} from ${d.catalog} has arrived! (Free)`;
                }
                return `📦 Your ${d.item} from ${d.catalog} has arrived! (${d.price} ${d.currency} ${emoji})`;
            }
            return result.error;
        }
        
        // Wallet/balance
        if (['gold', 'money', 'coins', 'balance', 'wallet', 'moolah'].includes(cmd)) {
            const bal = this.balance();
            const rate = this.getExchangeRate();
            const karmaEmoji = this.karma > 20 ? '😇' : this.karma < -20 ? '😈' : '😐';
            if (bal.total === 0) {
                return "Your wallet is empty. Time to find some treasure! 🪙";
            }
            return `💰 Your Wallet:\n` +
                   `   ${bal.gold} gold 🟡  (adventure-local)\n` +
                   `   ${bal.moolah} moolah 🪙 (global stablecoin)\n` +
                   `   ─────────\n` +
                   `   Karma: ${this.karma} ${karmaEmoji}\n` +
                   `   Exchange: ${rate} gold = 1 moolah\n` +
                   `   (better karma = better rate)`;
        }
        
        // Karma/rubrics check
        if (['karma', 'reputation', 'rep', 'rubrics', 'score'].includes(cmd)) {
            const rate = this.getExchangeRate();
            const score = this.getEconomicScore();
            const scoreEmoji = score > 50 ? '🌟' : score > 20 ? '✨' : 
                              score < -50 ? '💀' : score < -20 ? '⚠️' : '➖';
            
            let report = `📊 Economic Rubrics\n\n`;
            
            // Show each rubric
            for (const [name, rubric] of Object.entries(this.economicRubrics)) {
                const bar = this.renderBar(rubric.value, 10);
                const pct = Math.round(rubric.weight * 100);
                report += `  ${name.padEnd(12)} ${bar} ${rubric.value.toString().padStart(4)} (${pct}% weight)\n`;
                report += `                ${rubric.desc}\n`;
            }
            
            report += `\n  ─────────────────────────────────\n`;
            report += `  ${scoreEmoji} Blended score: ${Math.round(score)}\n`;
            report += `  💱 Exchange rate: ${rate} gold = 1 moolah\n`;
            report += `  📈 Base rate: ${this.baseExchangeRate} (at neutral)\n\n`;
            report += `  Play well across all dimensions = better rate!`;
            
            return report;
        }
        
        // Currency exchange: EXCHANGE 100g, EXCHANGE 10m
        if (['exchange', 'convert', 'xchg'].includes(cmd)) {
            const rate = this.getExchangeRate();
            const karmaEmoji = this.karma > 20 ? '😇' : this.karma < -20 ? '😈' : '😐';
            
            if (!args) {
                return `💱 Currency Exchange\n\n` +
                       `Current rate: ${rate} gold 🟡 = 1 moolah 🪙\n` +
                       `Your karma: ${this.karma} ${karmaEmoji}\n\n` +
                       `Commands:\n` +
                       `  EXCHANGE 100g  — Convert 100 gold → moolah\n` +
                       `  EXCHANGE 10m   — Convert 10 moolah → gold\n\n` +
                       `Gold is adventure-local. Moolah is the global stablecoin.\n` +
                       `Better karma = better exchange rate for your gold.`;
            }
            
            const parsed = this.parseCurrency(args);
            if (!parsed) {
                return `"${args}" is not a valid amount. Try: EXCHANGE 100g or EXCHANGE 10m`;
            }
            
            if (parsed.currency === 'gold') {
                const result = this.exchangeGoldForMoolah(parsed.amount);
                if (result.success) {
                    return `💱 Exchanged ${result.goldSpent} gold 🟡 → ${result.moolahReceived} moolah 🪙\n` +
                           `   (rate: ${result.rate}:1, karma: ${result.karma})`;
                }
                return result.error;
            } else {
                const result = this.exchangeMoolahForGold(parsed.amount);
                if (result.success) {
                    return `💱 Exchanged ${result.moolahSpent} moolah 🪙 → ${result.goldReceived} gold 🟡\n` +
                           `   (rate: 1:${result.rate})`;
                }
                return result.error;
            }
        }
        
        // Economy analysis
        if (['economy', 'econ', 'wealth', 'gdp', 'stats'].includes(cmd)) {
            return this.economyReport();
        }
        
        // Money flow analysis
        if (['flows', 'flow', 'moneyflow', 'cashflow'].includes(cmd)) {
            return this.flowReport();
        }
        
        // History analysis (object activity summary)
        if (['history', 'activity', 'chronicle'].includes(cmd)) {
            return this.historyReport();
        }
        
        // History dump (JSON export)
        if (['historydump', 'hdump'].includes(cmd)) {
            const compact = args?.toLowerCase() === 'compact';
            return this.historyDump(compact);
        }
        
        // Narrative prompt for LLM
        if (['story', 'narrative', 'narrate'].includes(cmd)) {
            const style = args || 'detailed';
            return this.narrativePrompt(style);
        }
        
        // YAML export for LLM
        if (['storyyaml', 'nyaml'].includes(cmd)) {
            return this.narrativeYaml();
        }
        
        // Full Cursor export
        if (['cursorexport', 'cexport', 'export'].includes(cmd)) {
            const compact = args?.toLowerCase() === 'compact';
            const data = this.exportForCursor();
            return compact ? JSON.stringify(data) : JSON.stringify(data, null, 2);
        }
        
        // Economic data dump (JSON)
        if (['dump', 'econdump', 'econdata'].includes(cmd)) {
            const compact = args?.toLowerCase() === 'compact';
            return this.economicDump(compact);
        }
        
        // Transaction ledger
        if (['ledger', 'transactions', 'txs'].includes(cmd)) {
            const limit = args ? parseInt(args) || 10 : 10;
            return this.transactionHistory(limit);
        }
        
        // Event log
        if (['events', 'log'].includes(cmd)) {
            const limit = args ? parseInt(args) || 10 : 10;
            return this.eventHistory(limit);
        }
        
        // Action log (unified)
        if (['actions', 'audit'].includes(cmd)) {
            const limit = args ? parseInt(args) || 15 : 15;
            return this.actionHistory(limit);
        }
        
        // Object activity log
        if (['objlog', 'objectlog', 'objects'].includes(cmd)) {
            const limit = args ? parseInt(args) || 15 : 15;
            return this.objectActivityReport(limit);
        }
        
        // Object history (specific object)
        if (['objhistory', 'about'].includes(cmd)) {
            if (!args) return 'About what object? Usage: ABOUT <object-id>';
            return this.objectHistory(args);
        }
        
        // Narrator style
        if (['narrator', 'voice', 'style'].includes(cmd)) {
            if (!args) {
                const styles = ['classic', 'sardonic', 'dramatic', 'minimalist', 'cozy', 'palm'];
                return `🎙️ Current narrator: ${this.narrator.style}\n\nAvailable styles:\n` +
                    styles.map(s => `  ${s.toUpperCase()}${s === this.narrator.style ? ' ←' : ''}`).join('\n') +
                    `\n\nType NARRATOR <style> to change.`;
            }
            return this.setNarratorStyle(args);
        }
        
        // Character switching
        if (['who', 'characters', 'chars'].includes(cmd)) {
            return this.who();
        }
        
        if (['become', 'play', 'switch'].includes(cmd)) {
            if (!args) {
                return 'BECOME who? Type WHO to see characters here.';
            }
            return this.become(args);
        }
        
        // Help
        if (['help', '?'].includes(cmd)) {
            return `
Adventure 4 — Commands

Navigation:
  NORTH, SOUTH, EAST, WEST, UP, DOWN (or N, S, E, W, U, D)
  GO <direction>
  
Look:
  LOOK (or L) — Describe current room
  LOOK <exit> — Describe an exit in detail
  EXAMINE <thing> (or X) — Look at something closely
  
Characters:
  WHO — See who's here
  BECOME <name> — Switch to playing as another character
  
Objects:
  GET <thing> — Pick up an object
  DROP <thing> — Put down an object
  GIVE <thing> TO <target> — Give object or currency
    • GIVE sword TO marieke — give an object
    • GIVE 10gp TO monkey — give gold (g/gp/gold)
    • GIVE 50m TO cat — give moolah (m/mo/moo/moolah)
    • Targets resolve by name OR tag (asks which if multiple)
  INVENTORY (or I) — See what you're carrying

Trading:
  APPRAISE <thing> — Check an object's value
  SELL <thing> TO <character> — Sell at declared price
  BUY <thing> FROM <character> — Buy at declared price
  SHOP [character] — Browse items for sale

Catalogs:
  CATALOGS — List all mail-order catalogs
  CATALOG <name> — Browse a catalog's items
  ORDER <item> FROM <catalog> — Instant delivery!

Economy:
  WALLET — Check your balance (gold 🟡 + moolah 🪙)
  LEDGER [n] — View money transactions
  FLOWS — View money flow analysis
  ECONOMY — World economy report

Logs & History:
  EVENTS [n] — View object movement events
  ACTIONS [n] — View all actions (audit trail)
  OBJLOG [n] — View object activity log
  ABOUT <id> — View history for specific object
  HISTORY — Analyze object activity (summary)

Export (for LLM/Cursor):
  STORY [style] — Generate LLM narrative prompt (summary/detailed/dramatic/humorous)
  EXPORT [compact] — Full session state + logs (JSON, pretty or compact)
  DUMP [compact] — Economy data dump (JSON)
  HDUMP [compact] — History data dump (JSON)
  
Other:
  NARRATOR <style> — Change narrator voice
  HELP (or ?) — This message

"Sheepy enough, but not too sheepy."
            `.trim();
        }
        
        // Try as a custom exit direction (bar, games, arcade, stage, etc.)
        if (this.room?.exits?.[cmd] || this.room?.exits?.[cmd.toUpperCase()]) {
            return this.go(cmd);
        }
        
        return `I don't understand "${input}". Type HELP for commands.`;
    }
    
    // ═══════════════════════════════════════════════════════════════════════════
    // UI INTEGRATION
    // ═══════════════════════════════════════════════════════════════════════════
    
    /**
     * Mount to a DOM element
     */
    mount(containerId) {
        const container = typeof containerId === 'string' 
            ? document.getElementById(containerId) 
            : containerId;
        
        if (!container) {
            console.error('Container not found:', containerId);
            return this;
        }
        
        container.innerHTML = `
            <div class="mootal-output" id="mootal-output"></div>
            <div class="mootal-input-row">
                <span class="mootal-prompt">&gt;</span>
                <input type="text" id="mootal-input" placeholder="What do you do?" autofocus>
            </div>
        `;
        
        this.ui = {
            output: document.getElementById('mootal-output'),
            input: document.getElementById('mootal-input')
        };
        
        // Handle input
        this.ui.input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                const input = this.ui.input.value.trim();
                if (input) {
                    this.print(`> ${input}`, 'command');
                    const result = this.command(input);
                    this.print(result, 'response');
                    this.ui.input.value = '';
                }
            }
        });
        
        return this;
    }
    
    /**
     * Print to output
     */
    print(text, type = 'response') {
        if (!this.ui?.output) {
            console.log(text);
            return;
        }
        
        const div = document.createElement('div');
        div.className = `mootal-line mootal-${type}`;
        div.textContent = text;
        this.ui.output.appendChild(div);
        this.ui.output.scrollTop = this.ui.output.scrollHeight;
    }
    
    /**
     * Start the game (show initial room)
     */
    start() {
        this.print(this.look(), 'room');
        if (this.ui?.input) {
            this.ui.input.focus();
        }
        return this;
    }
}

// Export for module and global use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { MootalEngine };
}
if (typeof window !== 'undefined') {
    window.MootalEngine = MootalEngine;
}
