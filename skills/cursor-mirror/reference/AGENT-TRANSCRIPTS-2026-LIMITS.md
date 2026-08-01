# Agent transcripts (2026): what is readable, what is not

**Status:** observed Aug 2026 · **First case study:** [GROKOGANDA-DEFENSES.md](../../../designs/GROKOGANDA-DEFENSES.md) §1.2

Cursor now stores Agent sessions in **three partially overlapping layers**. None of them
gives full chain-of-thought. Constitution §6: say what we have and what we don't.

## Three layers (do not conflate)

| Layer | Location | User-visible chat text | Thinking summary | Tool calls (input) | Tool results | Terminal I/O |
|-------|----------|------------------------|------------------|-------------------|--------------|--------------|
| **Export Transcript** (UI) | Chat → Export | Summarized since ~Jan 2026 | **Excluded** (feature request, not bug) | **Excluded** | **Excluded** | **Excluded** |
| **agent-transcripts JSONL** | `~/.cursor/projects/<ws>/agent-transcripts/<id>/<id>.jsonl` | Yes (`type:text`) | **Absent** (0 blocks in probed sessions) | Yes (`type:tool_use`) | **Absent** | **Absent** |
| **SQLite bubbles** | `state.vscdb` → `composerData:*` + `bubbleId:*` | Yes | Yes (`bubble.thinking.text`) — **provider summary, not raw CoT** | Yes (`toolFormerData`) | Yes | Often in tool blobs |

**Agent-era drift:** many Agent composers exist **only** as JSONL. Workspace/global
`state.vscdb` may have **zero** `composerData:` rows and **zero** bubbles for that UUID
(probed on session `6130c625…`, Aug 2026). In that regime:

- `cursor-mirror thinking <id>` → empty (reads bubbles, not JSONL)
- `cursor-mirror tools <id>` → may still work via JSONL if wired; bubble path empty
- `cursor-mirror agent-transcript <id>` → user + assistant **text** + nested **tool_use** inputs

## What providers actually send ( ceiling )

Cursor staff ([forum, May 2026](https://forum.cursor.com/t/transcripts-no-longer-exported-in-full/150214)):

> For extended thinking models, providers intentionally only return a **summary** of the
> reasoning, not the full chain-of-thought. … What you see in chat as the thinking block
> is that same summary we get from the provider. We don't get the full chain ourselves.

So even when thinking **is** stored in SQLite bubbles, it is not hidden reasoning recovered
from disk — it is the same redacted summary the UI shows. **Full CoT is not recoverable**
from Cursor, export, JSONL, or bubbles.

Two separate gaps:

1. **Provider gap** — raw reasoning never shipped to Cursor.
2. **Cursor gap** — even the UI thinking summary and tool results often **not written** to
   JSONL or Export Transcript; bubble store depopulated for Agent-only sessions.

## Community discussion and tools

### Cursor forum (official stance)

- [Transcripts no longer exported in full](https://forum.cursor.com/t/transcripts-no-longer-exported-in-full/150214) — regression reports from Jan 2026; Dean Rie (May 2026): thinking / terminal / collapsed tool blocks **intentionally omitted** from Export; tracked as feature request, no ETA.
- [Richer agent transcripts + lifecycle data (Langfuse / stop hooks)](https://forum.cursor.com/t/richer-agent-transcripts-lifecycle-data-for-observability-langfuse-stop-hooks/166592) — community asks for `tool_result` rows, timestamps, `model_id`, thinking hash/length; notes JSONL is "much thinner" than Claude Code JSONL; recommends **hooks** (`stop`, `postToolUse`) to capture what disk omits.

### Open-source adapters (sibling ecosystem)

| Project | Thinking | Tool results | Notes |
|---------|----------|--------------|-------|
| [S2thend/cursor-history](https://github.com/S2thend/cursor-history) | From `bubble.thinking.text` | `toolFormerData` / formatToolCallWithResult | **Requires populated SQLite bubbles** — assimilated in `reference/assimilated/S2THEND-CURSOR-HISTORY.yml` |
| [@tracebench/adapter-cursor](https://www.npmjs.com/package/@tracebench/adapter-cursor) | Phase 2: `capabilityType` 30 from DB | Phase 2 from `toolFormerData` | Phase 1 JSONL: tool_use input only, no tool_result, no thinking; merges DB over JSONL when `composerId` matches |
| [dwqs/cursor-trace](https://github.com/dwqs/cursor-trace) | **Heuristic** on assistant text (language/pattern split) | Viewer only; reads JSONL | Not true thinking recovery — infers "thinking-like" segments from final text |
| cursor-mirror (us) | `thinking` command → bubbles | `tool-result`, `blobs` → bubbles | JSONL path added Aug 2026; honest limits documented here |

**cursor-trace** is useful for browsing JSONL in-IDE; it does **not** read a thinking channel
that isn't in the file. Treat its "Show thinking" as UX heuristics, not forensics.

## What *is* possible again (workarounds)

| Approach | Captures | Limitation |
|----------|----------|------------|
| Read **JSONL** directly | User text, assistant text, `tool_use` name+input | No thinking, no tool output |
| **SQLite Phase 2** (tracebench / cursor-history / cursor-mirror bubbles) | Thinking summary, tool results, timestamps | Only if Cursor still writes `composerData` for that session — **often empty for Agent JSONL-only** |
| **Cursor hooks** (`postToolUse`, `stop`) | Tool output, lifecycle, optional logging | Opt-in; must run during session; see Langfuse thread |
| **`agent --print --output-format stream-json`** | Thinking/assistant events in CLI stream | Separate from IDE Agent JSONL; per Cursor forum guidance |
| **Proxy** (CursorLens, TensorZero) | Request/response payloads, tokens | Traffic layer; not historical recovery |

There is **no** known way to retroactively recover thinking or tool results for a session
that was JSONL-only with empty bubbles — unless hooks or a proxy logged it live.

## cursor-mirror commands vs storage era

| Era | Transcript file | `thinking` | `tools` / `tool-result` |
|-----|-----------------|------------|-------------------------|
| Pre-2026 `.txt` | Flat `.txt` with `[Thinking]` markers | Parse `.txt` via `agent-transcript --thinking` | `[Tool call]` / `[Tool result]` in `.txt` |
| 2026 nested JSONL | `<id>/<id>.jsonl` | **Not in file** → command empty | `tool_use` in JSONL (input only); results need bubbles/hooks |
| SQLite-rich | `composerData` + bubbles | `bubble.thinking` (summary) | `toolFormerData`, agentKv blobs |

When `thinking` returns zero blocks, check:

```bash
# JSONL exists?
ls ~/.cursor/projects/*/agent-transcripts/<composer-id>/<composer-id>.jsonl

# Bubbles exist?
python3 skills/cursor-mirror/scripts/cursor_mirror.py sql global \
  "SELECT key FROM ItemTable WHERE key LIKE 'composerData:%' LIMIT 5"
```

If JSONL yes and bubbles no → **expected empty thinking**; use this doc, not fabrication.

## Empirical probe (6130c625…, Aug 2026)

Session analyzed in GROKOGANDA-DEFENSES:

| Metric | Count |
|--------|------:|
| JSONL lines | 484 |
| `content.type=text` | 579 |
| `content.type=tool_use` | 1088 |
| `content.type=thinking` | **0** |
| `composerData` keys for composer | **0** |

## Maintenance

When Cursor changes storage again: re-probe JSONL content types, re-check `composerData`
population, update this file and `DOTCURSOR-SCHEMAS.yml` → `agent_transcript_jsonl`.
Track forum + sibling repos per `SIBLING-REPOS.md` / `EXTERNAL-PROJECTS-COMPARISON.md`.
