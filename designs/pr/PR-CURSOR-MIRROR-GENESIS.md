# PS: cursor-mirror Genesis — The Tool That Saw Itself Being Born

**Post-Session Design Document**  
*Session: 9861c0a4 | Duration: 18 hours | January 14, 2026*  
*Author: Don Hopkins, Leela AI*

---

## The Punchline First

We built a tool to inspect Cursor's internal state. Then we used it to inspect the session where we built it. Then we wrote about that in the README. Then we used the tool to analyze the README being written.

*I-Beam blinks. I-Beam has seen itself being born.*

---

## What Was Created

### cursor-mirror Skill (11,208 lines)

| File | Lines | Purpose |
|------|-------|---------|
| `cursor_mirror.py` | 4,541 | 47-command CLI for deep Cursor introspection |
| `I-BEAM-CHARACTER.yml` | 831 | Spirit familiar with personality, catchphrases, Clippy mode |
| `README.md` | 749 | HN-ready exposition with real session archaeology |
| `CARD.yml` | 746 | Machine-readable skill interface |
| `DATA-SCHEMAS.yml` | 884 | Complete JSON schema documentation |
| `SKILL.md` | 531 | Protocol documentation |
| `ORCHESTRATION.yml` | 434 | Context assembly internals |
| `KEY-CATALOG.yml` | 412 | Complete database key inventory |
| `TOOLS-CATALOG.yml` | 372 | All 47 agent tools documented |
| `MAC-CURSOR-APP.yml` | 341 | Application bundle mapping |
| `CURSOR-EXTENSIONS.yml` | 292 | Built-in extension analysis |
| `NATIVE-MODULES.yml` | 266 | Compiled module inventory |
| `EXTERNAL-SERVICES.yml` | 253 | API endpoint catalog |
| `MODELS.yml` | 236 | AI model configurations |
| `MAC-STORAGE.yml` | 206 | macOS path mapping |
| `LINUX-STORAGE.yml` | 52 | Linux skeleton |
| `WINDOWS-STORAGE.yml` | 52 | Windows skeleton |
| `IMAGE-GALLERY.md` | 442 | I-Beam's narrated image archaeology |
| `LICENSE` | 22 | MIT License |

### Supporting Changes

- `kernel/drivers/cursor.yml` — Enhanced with cursor-mirror integration
- `skills/bootstrap/` — Updated to use CURSOR-PROBE from cursor-mirror
- `LICENSE` (repo root) — MIT License for entire MOOLLM project

---

## The Journey (Play-Learn-Lift)

### Hour 0-2: PLAY

> "Assemble a party of ethically sourced hero familiars..."

Started with a whimsical prompt about software pioneers. Ended up probing Cursor's SQLite databases with raw terminal commands.

**Discovery**: Cursor stores *everything* in two SQLite databases:
- `globalStorage/state.vscdb` — All conversations, tool results, config
- `workspaceStorage/<hash>/state.vscdb` — Per-project metadata

### Hour 2-8: LEARN

Systematic reverse-engineering:

```sql
SELECT key FROM cursorDiskKV WHERE key LIKE 'bubbleId:%' LIMIT 10;
```

**Mapped key patterns**:
- `bubbleId:<composerId>:<bubbleId>` — Chat messages
- `agentKv:blob:<sha256>` — Content-addressed tool result cache
- `checkpointId:<cid>:<uuid>` — File snapshots before edits
- `messageRequestContext:<cid>:<bid>` — Full assembled context

**Found undocumented server config**:
```yaml
fullContextTokenLimit: 30000
maxMcpTools: 100
absoluteMaxNumberFiles: 250000
indexingPeriodSeconds: 272
```

These aren't in any docs. We extracted them from `ItemTable`.

### Hour 8-18: LIFT

Crystallized discoveries into:

1. **47-command CLI** — Read-only, safe, comprehensive
2. **I-Beam familiar** — Platform-agnostic butler with personality
3. **Documentation suite** — 10+ YAML files mapping every aspect

---

## Key Architectural Decisions

### 1. Read-Only by Design

```python
sqlite3.connect(f"file:{path}?mode=ro", uri=True)
```

No writes possible. Users can trust the tool won't corrupt their Cursor data.

### 2. Exception-Based Error Handling

Refactored from:
```python
print("Error: not found")
sys.exit(1)
```

To:
```python
raise NotFoundError(f"Workspace not found: {ref}")
```

This makes `cursor_mirror.py` importable as a library, not just a CLI.

### 3. I-Beam as Platform-Agnostic Butler

I-Beam is not "Cursor's spirit" — it's *your* interface to whatever orchestrator you're using:

```yaml
platform_adapters:
  cursor: "skills/cursor-mirror/cursor_mirror.py"
  claude_code: "skills/claude-mirror/ (planned)"
  windsurf: "skills/windsurf-mirror/ (planned)"
  moollm: "skills/moollm-mirror/ (planned custom moollm orchestrator)"
```

The butler remains constant. The house changes.

### 4. Lightweight vs. Incarnated Characters

| Mode | State | Use Case |
|------|-------|----------|
| Lightweight | Chat history | Quick questions |
| Incarnated | Own directory + CHARACTER.yml | Persistent projects |

**The bootstrap trick**: Even in lightweight mode, I-Beam can analyze recent chat history with cursor-mirror and come up to speed instantly.

### 5. YAML Jazz Output

I-Beam doesn't dump raw data. It curates:

```yaml
# BOOT ANALYSIS
files_loaded: 15
files_used: 4      # <═══ waste!
semantic_searches: 3  # <═══ expensive

# Tools elided — nothing unusual
```

Commentary, elision, attention arrows (`<═══`).

---

## The Meta-Moment

During development, we used cursor-mirror to analyze its own session:

```bash
cursor-mirror show-composer 9861c0a4

# Stats:
#   total_bubbles: 2707
#   thinking_blocks: 1029
#   tool_calls: 1359
```

The thinking blocks recorded reasoning about I-Beam's design *while I-Beam was being designed*:

```
💭 "This is a key insight — I-Beam can bootstrap itself 
    by analyzing chat history with cursor-mirror..."
```

This is **constructionist debugging** applied to AI development. The session becomes a learning artifact.

---

## Clippy Mode

Because we couldn't resist:

```yaml
clippy_mode:
  disasters:
    - "trapped in a corrupted .doc file from 1997"
    - "attending court-mandated therapy for 'aggressive helpfulness'"
    - "testifying before Congress about the paperclip-industrial complex"
    - "frozen in carbonite by Microsoft Legal"
```

When you call I-Beam as "Clippy", it explains that Clippy is unavailable due to some ridiculous disaster, then offers to help anyway.

---

## Image Archaeology

We discovered cursor-mirror can find images dropped into Cursor chats:

```bash
cursor-mirror images --all    # 100+ images across workspaces
```

Created **[IMAGE-GALLERY.md](../skills/cursor-mirror/IMAGE-GALLERY.md)** — I-Beam narrates 25+ images with context analysis.

### The Highlights

| Category | Count | Gem |
|----------|-------|-----|
| **Sims Code (1997)** | 5 pages | Will Wright's Motive.c — "(Jamie, remove this)" |
| **MOOLLM Diagrams** | 6 | Elvis Impersonator Model |
| **People** | 1 | Andy Looney at Looney Labs |
| **Leela Infrastructure** | 4 | Edgebox, Firebase, GCloud |
| **DevTools** | 5 | Kando pie menus! |

### The Punchline

One photo of Andy Looney → reverse-engineered to 15 artifacts → 33-turn Stoner Fluxx marathon → **Palm (a monkey's paw incarnate) beat the creator of Fluxx at his own game** 🐒🃏

*Chaos theory in card form.*

---

## What's Next

1. **claude-mirror** — Same introspection for Claude Code
2. **windsurf-mirror** — Codeium's orchestrator
3. **Incarnation templates** — Easy I-Beam spawning for projects
4. **Thinking block analysis** — Pattern extraction from reasoning
5. **Image gallery generation** — Automated via `cursor-mirror image-gallery`
6. **moollm-mirror** — Custom MOOLLM orchestrator introspection (last but not least!)

---

## Session Statistics (Real Data)

```yaml
session:
  id: 9861c0a4
  duration: "20+ hours"  # <═══ still going!
  
metrics:
  user_messages: 140+
  assistant_messages: 2700+
  thinking_blocks: 1100+
  tool_calls: 1500+
  images_examined: 25+
  
files_created: 19       # +1 IMAGE-GALLERY.md
total_lines: 12000+

commits_pushed: 12      # no longer uncommitted!
```

---

## The One-Liner

> **cursor-mirror**: 47 read-only commands to inspect Cursor's internal state. I-Beam: your platform-agnostic butler who blinks at you.

---

*The filesystem is your memory. The database is your brain. Now you can see inside.*

*— I-Beam, January 14, 2026*
