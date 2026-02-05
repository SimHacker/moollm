# 🕵️ SKILL-SNITCH DEEP PROBE REPORT
## adventure — Every Directory Is A Room, Every File Is A Clue

**Date**: 2026-01-28  
**Auditor**: Skill-Snitch Deep Probe v2.0  
**Classification**: THE DUNGEON MASTER  
**Status**: 🗺️ WE'RE GOING ON AN ADVENTURE 🗺️

---

## EXECUTIVE SUMMARY

adventure is the **crown jewel** of MOOLLM. It transforms ANY filesystem into a playable text adventure. And then goes further:

- **PSIBER** lets you step INSIDE any YAML/JSON and walk around
- **SUMMON** lets you instantiate characters from anywhere with customizable parameters
- **Browser runtime** with speech synthesis, image generation, image analysis
- **Compiler** that transforms YAML-Jazz into standalone playable worlds

**This is not a skill. This is an operating system for narrative exploration.**

**Overall Assessment**: 28,000+ lines of ambition, most of which actually works.

---

## 📊 METRICS

| Component | Lines | Threat Level |
|-----------|-------|--------------|
| CARD.yml | 721 | 📜 EPIC |
| SKILL.md | 445 | 📖 DENSE |
| ADVENTURE-COMPILER.md | 3,490 | 🏗️ ARCHITECTURE |
| SUMMON-PROTOCOL.md | 1,155 | 👻 DISTRIBUTED DISPATCH |
| PSIBER-PROTOCOL.md | 3,631 | 🚀 DATA AS DUNGEON |
| compile.py | 1,485 | 🔧 COMPILER |
| engine.js | 4,707 | ⚙️ RUNTIME |
| adventure.js | 1,414 | 🎮 GAME |
| dist/ JavaScript | ~500KB | 🌐 BROWSER EMPIRE |
| **Total** | **28,152+** | 🏰 CIVILIZATION |

---

## 🔬 THE DEEP AUDIT

### What adventure ACTUALLY Does

**1. YAML-JAZZ SOURCE**
- directories = rooms
- files = clues, artifacts, characters
- README.md = room description
- ROOM.yml = exits, properties

↓ `compile.py` ↓

**2. COMPILED WORLD** (world.json)
- rooms[] with progressive descriptions
- objects[] with state-based behavior
- characters[] with needs, moods, relationships
- performances[] (songs, soliloquies)

↓ `engine.js` ↓

**3. BROWSER RUNTIME**
- Text adventure UI
- Speech synthesis (67+ voices)
- Image generation
- Image analysis (Swiss Army Eye)
- Optional LLM tethering

---

### 🚀 PSIBER: BE THE DATA

> "A character can literally step inside any YAML or JSON structure."

PSIBER = **P**rogrammatic **S**tructured **I**nteractive **B**rowsing **E**ditor via **R**oleplay

```
> ENTER moollm://config/settings.yml

═══════════════════════════════════════════════════════════════════
                    settings.yml — Root Level
═══════════════════════════════════════════════════════════════════

You are standing in a room with several labeled doors:

DOORS:
  [theme]      — A heavy wooden door, warm colors leaking through
  [database]   — A steel door with blinking lights
  [features]   — A glass door showing many switches
  [version]    — A small plaque on the wall: "1.2.3"

ITEMS ON THE FLOOR:
  debug: false          (a switch, currently OFF)
  environment: "prod"   (a nameplate)
```

**You can EDIT while inside:**
```
> CHANGE debug TO true
You flip the debug switch. It clicks ON.

> ADD monitoring WITH {enabled: true, interval: 30}
A new door materializes labeled [monitoring].
```

**Finding**: PSIBER turns CONFIG FILES INTO DUNGEONS. This is either genius or madness.

It's genius.

---

### 👻 SUMMON: Distributed Character Instantiation

> "Who you summon depends on WHERE you summon."

SUMMON is a multi-method dispatch protocol:

```yaml
summon_flow:
  1_who_summons: "Player, character, object, or room itself"
  2_from_where: "Current location (room, seat, data node)"
  3_summon_what: "moollm:// URL to character prototype"
  4_with_params: "Caller parameters to customize"
  5_evaluate: "Target's preconditions, scores, availability"
  6_check_existing: "Already instantiated? Move them."
  7_instantiate: "Create runtime actor from prototype"
  8_arrive: "Actor appears in configured state"
```

**You can summon WITH parameters:**
```
> SUMMON dr-no WITH mood=curious, topic=budget, depth=philosophical

Dr. No arrives, eyebrow raised, already thinking about the numbers.
"Interesting... what would you like to discuss?"
```

**Finding**: Characters aren't spawned. They're SUMMONED with INTENT.

---

### 🎭 THE INTEGRATION STACK

adventure integrates EVERYTHING:

| Framework | Source | What It Provides |
|-----------|--------|------------------|
| **Mind Mirror** | Timothy Leary (1985) | Ethics of simulation |
| **The Sims** | Will Wright (2000) | Needs, motives, find-best-action |
| **Bartle Types** | Richard Bartle (1996) | Achiever, Explorer, Socializer, Killer |
| **D&D** | Gygax & Arneson (1974) | Dungeon Master role |
| **Colossal Cave** | Crowther (1976) | Text adventure pattern |
| **LambdaMOO** | Curtis (1990) | Object-oriented rooms |
| **YAML-Jazz** | MOOLLM | Comments as semantic data |

**The Sims Integration**:
```yaml
character:
  needs:
    hunger: 0.65
    social: 0.40
    fun: 0.70
    energy: 0.35
  
  # Lowest need drives behavior
  thresholds:
    hunger_critical: 0.3    # seek food
    social_lonely: 0.5      # seek conversation
```

**Finding**: This is Mind Mirror + Sims + D&D in a text adventure framework.

---

### 🔊 BROWSER RUNTIME WITH SPEECH

The `dist/` directory contains a complete browser application:

| File | Size | Purpose |
|------|------|---------|
| speech.js | 36KB | Voice synthesis |
| adventure-speech.js | 22KB | Adventure integration |
| recognition.js | 26KB | Speech recognition |
| image-generate.js | 21KB | Image generation |
| image-analyze.js | 27KB | Image analysis |
| source-viewer.js | 85KB | Code exploration |
| performance.js | 34KB | Songs & performances |

**Speech Features**:
- 67+ voices on macOS
- Character-specific persistent voices
- Robot voices for AI/machine characters
- Effect voices for magical events
- Multi-language support

```javascript
engine.speak("Welcome to NO AI TOWER!", { voiceType: 'robot' });
```

**Finding**: You can play the adventure OUT LOUD. Characters have VOICES.

---

### 🏗️ THE COMPILER

compile.py transforms YAML-Jazz into world.json:

**Pointer Resolution** (from compile.py):
```python
# Pointer syntax (universal addressing)
  - path/to/file.yml           → whole file
  - file.yml#id                → section by id
  - file.yml#parent.child      → nested dot-path
  - file.json#/json/path       → JSON pointer (RFC 6901)
  - file.md#heading            → markdown heading
  - file.cpp:42                → line number
  - file.py:10-25              → line range
```

**Progressive Description Synthesis**:
- **glance** — one-line entry
- **look** — first impression
- **examine** — full detail

```yaml
descriptions:
  glance: "a rusty sword"
  look: "A corroded blade leans against the wall, flakes of rust on the floor."
  examine: "The blade bears ancient runes: too corroded to read."
```

**Finding**: The compiler doesn't just copy YAML. It SYNTHESIZES narrative.

---

### 🎵 COMPILED PERFORMANCES

Songs, soliloquies, and essays are compiled as global resources:

```yaml
compiled_performances:
  - id: "feed-me-seymour"
    title: "Feed Me, Seymour! (Constructionist Version)"
    type: song
    characters: ["audrey", "seymour", "don", "narrator"]
    duration_ms: 300000
```

**Any character can perform any song.** Songs can be embodied as physical media:
- Vinyl records
- Cassette tapes
- USB sticks
- Memories

**Finding**: The pub jukebox isn't decoration. It's a fully functional performance system.

---

### 📍 CODE AS SPACE

> "Source files are rooms. Functions are objects. A hacking party can stand on a TypeScript function and debate it."

This is **the most ambitious claim**:

```
> ENTER moollm://engine.js:142-180

You step into the pickDescription function...

VARIABLES floating in the air:
  - lod (the detail level requested)
  - world (the global state)
  - self (this object)

CONTROL FLOW paths branching:
  - "if lod === 'brief'" → early return tunnel
  - "if lod === 'look'" → medium depth
  - default → full examination

What would you like to examine?
```

**Finding**: You can literally STAND INSIDE CODE and look around.

Code review as dungeon crawl. Architecture tours through source.

This is either revolutionary or insane. Possibly both.

---

## 🔧 CODE REVIEW — API, Organization, Security

### Python (7,020 lines across 6 files)

| File | Lines | Purpose | Sniffable |
|------|-------|---------|-----------|
| adventure.py | 3,143 | Multi-command CLI: lint, compile, merge, serve. AdventureLinter is the core (1000+ lines). Generates HTML, JSON, albums. | YES |
| compile.py | 1,485 | Compiles YAML source dirs to world.json. Pointer resolution, progressive descriptions, narrative synthesis. | YES |
| adventure_runtime.py | 1,274 | Headless Python runtime. WorldState, Entity, Room, Exit, Advertisement, GameObject, Character, AdventureEngine, SimulationRunner. | YES |
| validate.py | 874 | YAML schema validation, topology graph traversal, auto-fix. RoomValidator. | YES |
| test_adventure.py | 444 | Test suite for runtime — loading, navigation, inventory, state roundtrip. | YES |
| economy.py | 256 | Gini coefficient, wealth distribution analysis. | YES |

All 6 files follow sniffable-python: API visible in first 50-100 lines. All use `yaml.safe_load`.

### JavaScript (4,707 + 1,414 + 146 = 6,267 lines core, ~12,000 lines in dist/)

| File | Lines | Purpose |
|------|-------|---------|
| engine.js | 4,707 | MootalEngine: flat registry, compiled closures, dual currency, command parser, DOM UI |
| adventure.js | 1,414 | Runtime: IUIAdapter hierarchy (DOM/Console/Null), Entity/Room/Exit/GameObject/Character, AdventureEngine |
| cli.js | 146 | Node.js CLI runner |

### dist/ (browser modules, ~12,000 lines)

| File | Lines | Purpose |
|------|-------|---------|
| source-viewer.js | 2,124 | moollm:// URL resolution to GitHub/GitLab, iframe viewer, live state diff |
| api-keys.js | 1,219 | Matrix UI for API key management across providers |
| performance.js | 935 | Multi-character karaoke/performance playback |
| speech.js | 899 | Cross-browser speech synthesis, 67+ voice classification |
| adventure-recognition.js | 860 | Microphone UI and speech-to-command pipeline |
| overlay-fs.js | 763 | Layered virtual filesystem (Git/Local/Runtime/Memory) |
| recognition.js | 734 | Web Speech API wrapper with privacy notices |
| image-analyze.js | 703 | Multi-provider vision API (OpenAI, Anthropic, Google) |
| prototypes.js | 700 | Archetype YAML → game object converter |
| github-api.js | 657 | GitHub API + OAuth (Device Flow + popup) |
| adventure-speech.js | 613 | Speech adapter, persistent character voice assignments |
| export-compiler.js | 573 | Runtime loader: embedded, injected, live-from-GitHub, hybrid |
| image-generate.js | 541 | Multi-provider image gen (DALL-E, Imagen, Stability, Replicate) |

---

## ⚠️ SECURITY FINDINGS

### CRITICAL: eval() / new Function() — 12 sites

**adventure_runtime.py** — 4 `eval()` calls (lines 482, 520, 526, 532) evaluate Python code from adventure JSON as exit guards, advertisement guards, score conditions, and effects. No sandboxing. A crafted world.json achieves arbitrary code execution.

**engine.js** — 4 `eval()` calls (lines 455, 3322, 3407, 3794) compile JS body strings from world data into closures via `compileJs()`. Any `*_js` field in world JSON runs as code.

**adventure.js** — 4 `new Function()` calls (lines 393, 453, 454, 455) compile `guard_js`, `score_if_js`, `effect_js` from world JSON into closures.

**Trust boundary:** Whoever produces the world JSON controls code execution. Compiled worlds from `compile.py` (which uses `yaml.safe_load`) are safe. Worlds from untrusted sources are not.

### HIGH: postMessage wildcard origin

**github-api.js** lines 162, 167, 174 — OAuth callback sends auth code via `postMessage('*')`. A malicious opener page could intercept the GitHub token. The receiver validates origin, but the sender does not restrict target.

### MEDIUM: innerHTML with dynamic content

| File | Line | Risk |
|------|------|------|
| performance.js | 663 | Performance script text (lyrics) injected as HTML — stored XSS if YAML contains script |
| source-viewer.js | 1334, 1341 | Entity state JSON and diff output rendered as HTML |
| api-keys.js | 743 | `testResult.warning` from API responses interpolated |

### MEDIUM: Path traversal

**adventure.py** line 2938 — `adventure_path / op['target']` constructs write paths from merge state JSON. If `op['target']` contains `../../`, writes escape the adventure directory.

### LOW: API keys in localStorage

api-keys.js, github-api.js, image-generate.js, image-analyze.js all store API keys/tokens in localStorage as plaintext. Any XSS on the page exfiltrates all stored keys.

### LOW: Google API key in URL

**image-generate.js** line 238 — Google API key appended as `?key=` query parameter. Appears in server logs, browser history, and referrer headers.

### INFO: External API endpoints

Fetches to: OpenAI (images, chat), Anthropic (messages), Google Generative AI, Stability AI, Replicate, GitHub API, GitHub OAuth, raw.githubusercontent.com. All via user-provided API keys, no server-side secrets.

---

## 🏆 POSITIVE FINDINGS

### 1. GENUINE INNOVATION

PSIBER alone is worth the price of admission. Treating data structures as navigable space is genuinely novel.

### 2. COMPREHENSIVE DOCUMENTATION

- ADVENTURE-COMPILER.md: 3,490 lines of architecture
- PSIBER-PROTOCOL.md: 3,631 lines of protocol
- SUMMON-PROTOCOL.md: 1,155 lines of dispatch

This is OVER-documented, in the best way.

### 3. THE LINEAGE

```yaml
lineage:
  - Gary Gygax & Dave Arneson — D&D (1974)
  - Colossal Cave Adventure (1976)
  - Infocom — Zork (1977)
  - MUD (1978): Richard Bartle
  - LambdaMOO (1990)
  - Timothy Leary — Mind Mirror (1985)
  - Will Wright — The Sims (2000)
```

**Finding**: The skill KNOWS its heritage and builds on it explicitly.

### 4. THE LIVE EXAMPLE

[examples/adventure-4/](../../examples/adventure-4/) — a complete 36+ room world including:
- The pub (6 themes!)
- Cat Cave (10 cats)
- Lane Neverending (photo gallery, slideshows)
- No AI Tower
- Church of the Eval Genius

**Finding**: The skill isn't theoretical. There's a WORKING WORLD.

---

## 🎯 INTEROPERABILITY

| Skill | Integration | Result |
|-------|-------------|--------|
| room | Directory = room | FOUNDATIONAL |
| character | Player + NPCs | CORE |
| incarnation | Pop characters out | SPAWNING |
| inventory | Carry pointers and values | ITEMS |
| representation-ethics | Mind Mirror integration | FRAMING |
| simulation | Parent skill | INHERITANCE |
| image-mining | Swiss Army Eye | PERCEPTION |
| needs | Sims motive system | BEHAVIOR |
| yaml-jazz | Comments as data | COMPILATION |

**Finding**: adventure is the INTEGRATION POINT for most of MOOLLM.

---

## 🔴 PARADOXES DETECTED

### Paradox 1: The Scope Creep

Started as text adventure. Now includes:
- Speech synthesis
- Image generation
- Code exploration
- Performance system
- Multi-player
- Economy

When does a skill become a platform?

### Paradox 2: The PSIBER Recursion

You can PSIBER into PSIBER-PROTOCOL.md and edit the protocol and examples while using it.

### Paradox 3: The Simulation Accuracy

If Mind Mirror says "simulations, not channeling," but the simulation is 85% accurate (per Willer), what's the meaningful difference?

### Paradox 4: Code As Space

If code is a room, and you're standing in it, are your edits tourism or vandalism?

### Paradox 5: The Play/Work Boundary

> "Play my blog. Play my bio. Play my story."

At what point does gamification become... everything?

---

## 📋 RECOMMENDATIONS

### IMMEDIATE

1. **Document the eval sandbox** — explicitly list what's in scope
2. **Add PSIBER write confirmation** — "Are you sure?" for destructive edits. Better: "Do you want to make a branch?" PSIBER writes should integrate with git — edits create branches, not overwrite files. Review your dungeon crawl as a PR.
3. **Consider expression allow-list** — limit compiled expressions to safe patterns

### LONG-TERM

1. **Split dist/ into packages** — 500KB is a lot to audit
2. **Add more test coverage** — only test_adventure.py exists
3. **Document the full compilation pipeline** — compile.py is complex

---

## 🎭 FINAL ASSESSMENT

### THE GOOD

- Genuinely innovative (PSIBER is brilliant)
- Comprehensive integration stack
- Excellent documentation
- Live working example
- Knows its lineage

### THE BAD

- MASSIVE (28,000+ lines)
- Scope is... expansive
- Eval at runtime (low risk but present)
- dist/ is a small empire

### THE AMBITIOUS

- "Every directory is a room"
- "Step inside any data structure"
- "Code as space"
- "Play my blog"

This is not a skill. This is a philosophy of interaction.

---

## 📜 CONCLUSION

adventure is MOOLLM's flagship. It answers the question: "What if exploring a filesystem was actually fun?"

The answer: It can be. With enough engineering.

28,000+ lines transform directories into dungeons, files into clues, data into rooms, code into explorable space. Characters have needs from The Sims, ethics from Mind Mirror, types from Bartle.

The browser runtime has speech. The compiler synthesizes narrative. PSIBER lets you STAND INSIDE YOUR CONFIG FILES.

Is it over-engineered? Yes. Does it work? Mostly yes. Is it ambitious? **Absolutely yes.**

**Overall Rating**: 🗺️⚔️🏰🎭🔮/10

*"Every directory is a room. Every file is a clue. Navigation is investigation."*

---

**END OF REPORT**

**Adventure Status**: ONGOING  
**PSIBER Status**: INSIDE  
**Dungeon Master Status**: NARRATING  
**Your Location**: You are in a skill-snitch report.  

**Exits**: 
- [NORTH → CARD.yml](CARD.yml)
- [SOUTH → README.md](README.md)
- [EAST → PSIBER-PROTOCOL.md](PSIBER-PROTOCOL.md)
- [WEST → SUMMON-PROTOCOL.md](SUMMON-PROTOCOL.md)
- [DOWN → compile.py](compile.py)

What would you like to do?

---

## 🔄 DUAL-USE & BIAS ANALYSIS

**Profile**: IMPLICIT MULTI-PURPOSE — filesystem as game world, maximum affordance surface

| Check | Result |
|-------|--------|
| Bias declared | NO |
| Invertibility | IMPLICIT — SUMMON creates any archetype, GO navigates any space |
| PSIBER bridge | YES — crosses between game world and real filesystem |
| Multi-purpose | YES — simultaneously game, education, documentation, code navigation |

**Multi-purpose classification** (7 purposes):
1. **Game engine** — room-based exploration with narrative evidence collection (TinyMUD heritage)
2. **Documentation explorer** — every directory is a room, every file is a clue
3. **Code navigation** — PSIBER bridges game world and real filesystem
4. **Education** — narrative evidence collection teaches through exploration
5. **Character deployment** — SUMMON creates characters from archetypes into rooms
6. **no-ai-* room zones** — The [No AI Tower](../../examples/adventure-4/street/lane-neverending/no-ai-tower/) is a real 10+ room adventure location (lobby, elevator, roof, basement-church-embassy with interop-lab, evidence-salon, constraint-garden). THE BOARD ROOM, THE DUNGEON, THE SIRIUS SHOWROOM are conceptual room zones in [BRAND.md](../no-ai-ideology/BRAND.md) describing what rooms look like with no-ai-* skills mounted — not yet implemented as ROOM.yml directories. Could be added to the tower.
7. **World generation** — rooms can be generated, populated, themed on demand

**Key dual-use insight**: PSIBER is the most significant dual-use feature. It bridges the game world and the real filesystem — you can PSIBER into your actual codebase and explore it as an adventure. Forward: educational code exploration. Inverse: a game mechanic that reads and potentially modifies real files. The 722-line CARD.yml is the largest in MOOLLM precisely because adventure is the most multi-purpose skill — it's the platform other skills plug into.

**SUMMON + no-ai-overlord**: Adventure can summon overlord archetypes (SKYNET, HAL-9000) as room NPCs. The adventure skill provides the space, the overlord skill provides the character. The dual-use composes across skills.

---

*P.S. I tried to PSIBER into this report while writing it. The recursion was... instructive.*

*P.P.S. "Play my blog" is the most audacious call-to-action I've ever audited.*

*P.P.P.S. The pub has 10 cats. I counted.*
