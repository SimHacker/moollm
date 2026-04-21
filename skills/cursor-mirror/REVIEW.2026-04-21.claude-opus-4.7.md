---
target: moollm/skills/cursor-mirror
target_level: skill
reviewer: claude-opus-4.7
date: 2026-04-21
yml_pair: REVIEW.2026-04-21.claude-opus-4.7.yml
parent: ../REVIEW.2026-04-21.claude-opus-4.7.md
---

# cursor-mirror — Deep Review

**Scope:** CARD.yml full; SKILL.md partial (first 120 of 792 lines); `lib/` module list and line counts; `scripts/cursor_mirror.py` line count. Did not read: script body, lib bodies, reverse-engineered reference files in detail, character definition, tests. **Confidence in claims: 85%** (high for what I read; absent for what I didn't).

## What it is functionally

The self-introspection instrument for LLM agents on Cursor. 59 commands, 3,358 lines of Python (702 CLI + 2,656 lib modules), reading Cursor's closed `state.vscdb` LevelDB (~9GB at `~/Library/Application Support/Cursor/User/globalStorage/state.vscdb`) plus the plaintext artifacts in `~/.cursor/`. It answers questions like:

- "What was I thinking 20 turns ago?" → `thinking @1`
- "What tools did I call?" → `tools @1`
- "What context was assembled?" → `context-sources @1`
- "What's my session health?" → `status`

Every command takes reference-shortcut syntax (`@1` = largest recent composer; `w3.c2` = workspace 3, composer 2; name fragments for fuzzy find) — `CARD.yml:118-120`, `SKILL.md:85-114`. The UX design assumes you don't want to memorize UUIDs.

Beyond watching, the skill also *compiles* — OPTIMIZE (`CARD.yml:125-128`) reads skill examples + user preferences + exclusions and emits optimized `.cursorrules`. This is the Cursor-side of the kernel's Cursor Optimization System (`kernel/ARCHITECTURE.md:237-316`): introspection → compilation → faster boot → repeat.

## What's strong

**This is real reverse engineering, committed.** `CARD.yml:194-226` catalogues five LevelDB key families (`bubbleId:*:*` for chat messages at 50K+ keys; `agentKv:*:*` for tool-result cache at 25K+; `checkpointId:*:*` for file snapshots at 10K+; `messageRequestContext:*:*` for context assembly; `ItemTable` for config/MCP registry/AI attribution). Combined totals documented at 102,724 keys, 19,789 tool calls analyzed. This isn't architecture fiction; this is "we opened the DB and enumerated it."

**Cross-OS coverage is not an afterthought.** `reference/reverse-engineered/storage/` contains `MAC-STORAGE.yml`, `LINUX-STORAGE.yml`, `WINDOWS-STORAGE.yml`, `DOTCURSOR-STORAGE.yml`, `MAC-CURSOR-APP.yml`. The CARD references all three platforms' Application Support paths (`CARD.yml:188-192`). Whoever built this actually considered running it on the three OSes, not just the author's.

**The `lib/` refactor is a sign of maturity.** 22 Python modules with clear boundaries: `bubbles.py`, `composers.py`, `sources.py`, `resolve.py`, `transcript.py`, `query_runner.py`, `sql.py`, `debug_util.py`, `feature_monitor.py`, `tool_validator.py`, `discovery.py`, `keys.py`, `paths.py`, `config.py`, `exceptions.py`, `format_util.py`, `datasette_export.py`, `commands/` directory. That's not a hastily-written CLI; that's a Python application that got refactored. 2,656 lines in lib/ vs. 702 in the CLI shell says the guts are load-bearing.

**Self-reflective posture explicit.** `SKILL.md:53-56`: "Cursor-mirror is a Play-Learn-Lift exemplar: it was built by reverse-engineering Cursor, then used to refine its own understanding, then uplifted into documented practice. That same loop is how we keep it accurate and aligned." That's one sentence describing a 3-stage dogfooding loop. It does what it says.

**`DATA-SCHEMAS.yml`, `KEY-CATALOG.yml`, `TOOLS-CATALOG.yml` make reverse engineering shareable.** 700+ lines of schemas, full `cursorDiskKV + ItemTable` inventory, all 29 Cursor agent tools with schemas. If the script breaks, the catalogs still carry the value. Separation of intelligence from implementation.

## What's weak

**CARD.yml overstates script size.** `CARD.yml:142` states "lines: ~9800" for `cursor_mirror.py`. Actual line counts:

```
wc -l scripts/cursor_mirror.py        → 702
wc -l lib/*.py (total)                → 2656
                                       ─────
                                        3358
```

The 9800 figure is ~2.8× the reality. Most likely explanation: the CLI was monolithic, got refactored into `lib/`, and the CARD figure wasn't updated. `scripts/cursor_mirror_old.py` still exists in the directory, consistent with this theory.

This is a low-severity issue (the skill still works) but high-symbol-value: CARD is the "sniffable interface," readers trust its metadata, and the ~9800 number lands as "this is a massive script" when in fact the script is modular and reasonably sized. A sister-script that regenerates the `lines:` field from actual code at commit time closes the gap permanently.

**CARD.yml at 354 lines strains pyramid discipline.** The INDEX.md reading protocol specifies CARD at 50-200 lines for interface-sniff. Cursor-mirror's CARD is 354, with substantial content that is *documentation* rather than *interface*: the full data-sources dictionary with three-OS paths, the key-pattern catalog, the reverse-engineered file inventory by directory.

Recommendation: split CARD into a slim CARD (methods, advertisements, familiar, brief data-source summary) and a REFERENCE.yml that absorbs the detailed schema/path material. Keeps the pyramid honest; makes the interface sniff fast again.

**Cold-start problem in OPTIMIZE.** The compilation loop (`CARD.yml:125-135`, `kernel/ARCHITECTURE.md:237-316`) depends on having introspection data — past usage patterns, skill invocations, context-source frequencies. First-time users have none. Current experience: ambient skills are still injected, but the *personalized* compilation that would make boot fast is empty until sessions accumulate.

Mitigation (unbuilt): ship a seed `.cursorrules` compiled by the skill authors from their own representative patterns. First-boot uses the seed; subsequent compilation overwrites with user-specific output. Converts cold-start from "no optimization" to "reasonable default → improving."

## Tensions

**Reverse-engineering stability.** Cursor is closed and evolves. The 102K key catalog is accurate as of whenever it was last updated. Cursor ships weekly; some of those changes will invalidate entries. `SKILL.md:51-56` honestly names this ("deliberate risk: what we discover may change"), which is the right posture. What's unbuilt: automated drift detection. A `cursor-mirror schema-audit` command that queries the live DB for key-pattern distribution and diffs against committed `KEY-CATALOG.yml` would protect the investment. Currently drift surfaces only when a query breaks.

**Self-description vs. self-implementation.** Cursor-mirror is a skill that reads the session it's running in. That self-reference is philosophically interesting (Papert's "thinking about thinking" epigraph at `SKILL.md:40-41`) and operationally tricky: does invoking `cursor-mirror status` from within a session show the state *including the invocation itself*? How recent can "what I just did" be? Reading my own live LevelDB while it's being written is a race condition. SKILL.md presumably addresses this; I didn't read that far this pass.

## Frontiers

1. **Schema-drift detection.** Auto-audit live DB vs. committed catalog. Protects the 102K catalog from Cursor weekly releases.
2. **Generalization to other orchestrators.** `mooco-mirror` exists (INDEX.yml:525-527); the pattern (DB spelunking, timeline reconstruction, thinking extraction) generalizes. Lifting a shared `mirror` parent skill with per-orchestrator specializations (cursor, mooco, claude-code, chatgpt-when-leveldb-exposed) amortizes reverse-engineering cost.
3. **Ambient-skill introspection.** Currently no command for "what ambient skills are active for me right now." Natural fit for cursor-mirror given it reads everything else.
4. **Runnable doc examples.** `SKILL.md` Quick Start (`:85-114`) shows `cursor-mirror tree w3.c2.tools`. If these snippets ran as doctests at commit time, drift would be caught automatically.
5. **STAGE-* extracted as pattern.** CARD:33-76 defines STAGE-ADD / STAGE-CONSOLIDATE / STAGE-COMMIT / STAGE-PR for cursor-mirror's own contribution flow. The Play-Learn-Lift loop implemented operationally. Extract to a `staging` skill; any skill that wants user-local preference promotion-to-central could inherit.

## What I'd do differently

- **Regenerate CARD metadata from code.** Sister-script makes `lines:`, `commands:`, `output_formats:` derive-on-commit. Drift dies.
- **Split CARD → CARD + REFERENCE.** Keeps pyramid discipline. REFERENCE.yml is where the key-catalog pointers, per-OS paths, detailed schema indices live.
- **Ship seed `.cursorrules`.** First-boot gets authors' compiled output as a reasonable default, later overwritten by user-specific compilation.
- **Add `schema-audit` command.** Protect the 102K catalog from silent drift.
- **Clean up `cursor_mirror_old.py`.** If dead, delete. If preserved for reference, move to `archive/` and note.

## What I didn't read

- The 702-line CLI itself (only line count).
- The 22 lib modules (only list + line counts).
- SKILL.md beyond line 120 — the full 59-command reference, the Watching-Yourself-Think philosophy section, the detailed workflow examples.
- The character definition (`characters/I-BEAM-CHARACTER.yml` — the I-Beam familiar — 826 lines per CARD.yml:347).
- Tests.
- The reverse-engineered reference files (I cited line counts and summaries from CARD; didn't open the schemas themselves).

Anything I said about implementation quality is based on structure (module names, line counts, file organization) not code inspection. A reviewer who reads the code can override my structural guesses with actual assessments.

## Cross-references

- Parent cluster: `../REVIEW.2026-04-21.claude-opus-4.7.md` (skills ecosystem)
- Root: `../../REVIEW.2026-04-21.claude-opus-4.7.md`
- Related (introspection cluster): bootstrap (not reviewed this pass), skill-snitch (GLANCE only), session-log (not reviewed), return-stack (not reviewed)
- Panel siblings invited: `skills/cursor-mirror/REVIEW.2026-04-21.<model>.{yml,md}`

---

*Cursor-mirror is the concrete proof that the "Coherence Engine" rhetoric in the kernel cashes out. The engine can watch itself think because this skill exists. The friction points are documentation hygiene, not design.*
