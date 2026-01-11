# Adventure Linter Session — January 10, 2026

> *"The linter is dumb and anal-retentive. The LLM is smart and helpful.
>   Together, they improve microworlds."*

---

## Session Overview

**Adventure:** Adventure 4 — A New Beginning  
**Date:** January 10, 2026  
**Goal:** Run the linter, analyze events, fix issues, compile expressions

---

## What We Built Today

Before starting the linter session, we designed and implemented:

### New Skills & Concepts

| Skill | Purpose |
|-------|---------|
| `logistic-container` | Factorio-style logistics boxes, grid storage |
| `image-mining` | Mine resources from photos/images (camera = pickaxe!) |
| Urban Metaphor | Grid rooms = city blocks at street intersections |
| Postal Integration | Instant transport layer for logistics |
| Instance Libraries | `skills/*/instances/` pattern |
| Event Handlers | YAML Jazz files that handle linter events |

### Files Created

- `designs/factorio-logistics-protocol.md` — 1200+ lines of design
- `skills/logistic-container/*` — Full skill with templates
- `skills/image-mining/*` — New skill with sensation mining
- `skills/skill/SKILL.md` — Instance library pattern
- `skills/buff/buffs/INDEX.yml` — 20+ reusable buffs
- `skills/image-mining/images/INDEX.yml` — Pre-analyzed images
- `skills/adventure/events/*` — Event handler templates

---

## Linter Results

**Command:**
```bash
python skills/adventure/adventure.py lint examples/adventure-4/ --format yaml --dump --output examples/adventure-4/LINTER.yml
```

**Summary:**
| Metric | Count |
|--------|-------|
| 🚪 Rooms | 36 |
| 📦 Objects | 37 |
| 🧑 Characters | 6 |
| 📄 Narrative/Docs | 41 |
| ❌ Errors | 8 |
| ⚠️ Warnings | 36 |
| ⚙️ Compile Requests | 9 |

---

## Event Analysis (318 Total Events)

### By Event Type

| Event Type | Count | Handler | Action Needed |
|------------|-------|---------|---------------|
| FOUND_EXIT | 106 | discovery | ✅ Info only |
| INFERRED_FILE_TYPE | 48 | discovery | ✅ Info only |
| FOUND_NARRATIVE | 41 | discovery | ✅ Info only |
| FOUND_ROOM | 36 | discovery | ✅ Info only |
| FOUND_OBJECT | 26 | discovery | ✅ Info only |
| **UNKNOWN_FILE_TYPE** | **23** | `UNKNOWN_FILE_TYPE.yml.tmpl` | 🔧 Add wrapper |
| STYLE_SUGGESTION | 9 | advisory | ℹ️ Optional |
| **COMPILE_EXPRESSION** | **9** | `COMPILE_EXPRESSION.yml.tmpl` | ⚙️ Generate code |
| **INVALID_SCHEMA** | **8** | `INVALID_SCHEMA.yml.tmpl` | ❌ Fix YAML |
| FOUND_CHARACTER | 6 | discovery | ✅ Info only |
| **BROKEN_REFERENCE** | **4** | `BROKEN_REFERENCE.yml.tmpl` | 🔗 Fix refs |
| ROOM_TOPOLOGY | 1 | topology | ✅ Map built |
| FOUND_ADVENTURE | 1 | discovery | ✅ Info only |

---

## Priority 1: Fix 8 YAML Syntax Errors

These block parsing and must be fixed first.

| # | File | Line | Issue |
|---|------|------|-------|
| 1 | `pub/pie-table.yml` | 32 | Block mapping error |
| 2 | `kitchen/mothers-note.yml` | 119 | Block collection error |
| 3 | `kitchen/fridge.yml` | 219 | Block collection error |
| 4 | `kitchen/tomtomagotchi.yml` | 97 | Block collection error |
| 5 | `coatroom/mannequin.yml` | 69 | Block collection error |
| 6 | `personas/linus-on-coffee-and-a-joint/PERSONA.yml` | ? | Block mapping error |
| 7 | `pub/menus/buds.yml` | 648 | Block scalar error |
| 8 | `pub/stage/palm-nook/study/tribute-to-tognazzini.yml` | ? | Block collection error |

---

## Priority 2: Compile 9 Expressions

All in `pub/gong.yml` — the ceremonial pub gong!

| Expression | Type | Natural Language |
|------------|------|------------------|
| RING.effect | action | "All conversation pauses..." |
| RING-TWICE.score_if | boolean | `urgent_situation OR point_of_order` |
| RING-TWICE.effect | action | "Immediate suspension..." |
| RING-THRICE.score_if | boolean | `performance_failing OR debate_deadlocked OR mercy_needed` |
| RING-THRICE.effect | action | "Current performance... ENDS" |
| CEREMONIAL-RING.effect | action | "The gong heralds..." |
| CELEBRATION-RING.score_if | boolean | `good_news OR victory OR milestone` |
| AUTOGONG-ELIMINATION.effect | action | "*GONG* — A merciful strike..." |
| AUTOGONG-VICTORY.effect | action | "A bright, celebratory tone..." |

---

## Priority 3: Identify 23 Unknown Files

| File Pattern | Inferred Type | Action |
|--------------|---------------|--------|
| `kitten-*.yml` (10 files) | character | Wrap in `character:` |
| `cat-*.yml` (2 files) | character | Wrap in `character:` |
| `bartender.yml`, `budtender-*.yml` | character | Wrap in `character:` |
| `drinks.yml`, `snacks.yml`, `games.yml` | menu/object | Add `lint_ignore: true` |
| `SIMS-TRAITS.yml`, `APPEARANCE.yml` | config | Add `lint_ignore: true` |
| `IMAGE-PROMPTS.yml` | config | Add `lint_ignore: true` |
| `captain-ashford.yml` | persona | Wrap appropriately |
| `guestbook.yml` | object | Wrap in `object:` |

---

## Priority 4: Fix 4 Broken References

| Source | Exit | Destination | Action |
|--------|------|-------------|--------|
| `personas/ROOM.yml` | east | `../skills/` | Ignore (external) |
| `pub/ROOM.yml` | UP | `rooms/` | **Create room** |
| `characters/ROOM.yml` | east | `../skills/` | Ignore (external) |
| `coatroom/ROOM.yml` | east | `$SKILLS/` | Ignore (variable) |

---

## Action Log

### Fix 1-8: All YAML Syntax Errors

**Status:** ✅ COMPLETE

| File | Issue | Fix |
|------|-------|-----|
| pie-table.yml | ASCII art block indentation | Removed slop |
| mothers-note.yml | `→` arrows in list items | Changed to `:` |
| fridge.yml | `—` em-dashes in list items | Changed to `:` |
| tomtomagotchi.yml | `→` arrows everywhere | Global sed replace |
| mannequin.yml | Unquoted `("text")` | Changed to `— text` |
| PERSONA.yml | Unquoted `("means")` | Changed to `— means` |
| buds.yml | `|` YAML operator in string | Changed to `or` |
| tribute-to-tognazzini.yml | Quoted partial strings | Single-quoted |

**Root cause:** YAML interprets `→`, `—`, `|`, and unquoted parentheses as special constructs. Always quote or rephrase!

---

## Priority 2: Compile Expressions

**Status:** ✅ COMPLETE (First Pass)

Compiled 3 boolean expressions in `pub/gong.yml`:
- `RING-TWICE.score_if` → `score_if_js` + `score_if_py`
- `RING-THRICE.score_if` → `score_if_js` + `score_if_py`
- `CELEBRATION-RING.score_if` → `score_if_js` + `score_if_py`

The `effect` fields are narrative prose (for display), not executable code.

---

## Current Status

After fixes:
```
📊 Linting complete: 0 errors, 39 warnings, 18 compile requests
```

| Before | After |
|--------|-------|
| 8 errors | 0 errors ✅ |
| 36 warnings | 39 warnings |
| 9 compile requests | 18 compile requests |

More objects discovered now that YAML parses correctly!

---

## Resolved Unknown File Types

Wrapped custom types in `object:` — their original `type:` field preserved:

```yaml
object:
  type: npc          # Original type stays
  species: felis_catus
  name: "Limonene"
```

20 files now recognized as objects (kittens, cats, menus, personas, etc.)

Kept `lint_ignore: true` for pure metadata:
- APPEARANCE.yml, SIMS-TRAITS.yml, IMAGE-PROMPTS.yml, LINTER.yml

---

## Current Status

```
📊 Linting complete: 0 errors, 13 warnings, 18 compile requests
   Found: 36 rooms, 49 objects, 6 characters
```

| Metric | Before | After |
|--------|--------|-------|
| Errors | 8 | 0 ✅ |
| Objects | 42 | 49 ⬆️ |
| Warnings | 39 | 13 ⬇️ |
| Unknown Files | 26 | 0 ✅ |

Remaining warnings:
- 4 BROKEN_REFERENCE (exits to external locations)
- 9 STYLE_SUGGESTION (advisory only)

---

## Remaining Work

1. ~~Fix 8 YAML errors~~ ✅
2. ~~Compile key expressions~~ ✅  
3. ~~Resolve 26 unknown file types~~ ✅
4. **Address remaining 13 warnings** (broken refs, style suggestions)
5. **Address 18 compile requests** (more expressions to compile)
6. Generate runtime (engine.js, style.css)
