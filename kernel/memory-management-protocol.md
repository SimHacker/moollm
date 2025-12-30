# Memory Management Protocol
## Hot/Cold Hints, Summarization, and Graceful Forgetting

---

## 1. Overview

LLMs have no internal memory. Everything must be in context. This protocol
defines how the model **advises** memory management and how the orchestrator
**implements** it — enabling intelligent caching, summarization, and forgetting.

**Key Principle:** Model advises, orchestrator decides.

---

## 2. Hot/Cold Cache Hints

### Hot Manifest (`hot.yml`)

Files the model wants to keep readily available:

```yaml
# hot.yml
protocol: MEMORY-MGMT/0.1
updated: "2025-12-30T12:30:00Z"

keep:
  - path: ".agent/constitution.md"
    why: "Core operating contract — always needed"
    since: "2025-12-30T12:00:00Z"
    touches: 15  # Times referenced this session
    
  - path: "src/lib/parser.ts"
    why: "Currently debugging parsing logic"
    since: "2025-12-30T12:25:00Z"
    touches: 8
    
  - path: "summaries/architecture.md"
    why: "High-level context for decisions"
    since: "2025-12-30T12:10:00Z"
    touches: 3
```

### Cold Manifest (`cold.yml`)

Files the model suggests evicting or summarizing:

```yaml
# cold.yml
protocol: MEMORY-MGMT/0.1
updated: "2025-12-30T12:30:00Z"

evict:
  - path: "tool/terminal/log-001.txt"
    why: "Old build log — superseded by log-005"
    last_touch: "2025-12-30T12:05:00Z"
    suggested_action: "delete_from_working_set"
    
  - path: "tool/python/output-large.json"
    why: "Raw data — already extracted what's needed"
    last_touch: "2025-12-30T12:20:00Z"
    suggested_action: "summarize_then_evict"
    
  - path: "drafts/attempt-1.md"
    why: "Failed approach — keeping for history only"
    last_touch: "2025-12-30T12:08:00Z"
    suggested_action: "archive"
```

### Suggested Actions

| Action | Meaning |
|--------|---------|
| `delete_from_working_set` | Remove from context, keep file |
| `summarize_then_evict` | Create summary, then remove original from context |
| `archive` | Move to archive directory |
| `compress` | Replace with compressed version |

---

## 3. Orchestrator Response

The orchestrator processes hints but may:

- **Honor** — Follow the suggestion
- **Defer** — Wait for better signal
- **Override** — Keep something the model wants evicted (e.g., audit requirements)
- **Promote** — Make something hot the model didn't mention

```yaml
# Orchestrator feedback (optional)
memory_actions:
  - path: "tool/terminal/log-001.txt"
    model_suggested: "evict"
    action_taken: "honored"
    
  - path: "user_preferences.yml"
    model_suggested: null  # Not mentioned
    action_taken: "promoted_to_hot"
    reason: "User referenced it"
```

---

## 4. Summarization Protocol

### When to Summarize

- File exceeds size threshold (e.g., 500 lines)
- File in `cold.yml` with `summarize_then_evict`
- Explicitly requested via `memory.summarize` tool
- Multiple files should be consolidated

### Summary Structure

```yaml
# summaries/tool-outputs-2025-12-30.md

---
summary_of:
  - tool/python/output-001.json
  - tool/python/output-002.json
  - tool/python/output-003.json
created: "2025-12-30T12:30:00Z"
style: bullet
---

## Tool Output Summary (3 files)

### Key Findings
- Dataset contains 10,432 records
- 15% have missing values in "email" field
- Date range: 2023-01-01 to 2025-11-30

### Notable Values
- Max revenue: $1.2M (record #4521)
- Most common category: "Electronics" (34%)

### Errors Encountered
- 2 files had UTF-8 encoding issues (fixed)

---
References:
- [output-001.json](../tool/python/output-001.json)
- [output-002.json](../tool/python/output-002.json)
- [output-003.json](../tool/python/output-003.json)
```

### Summary Styles

| Style | Use Case |
|-------|----------|
| `bullet` | Quick reference, facts |
| `narrative` | Context, reasoning |
| `schema` | Data structures |
| `diff` | What changed |
| `decision` | What was decided and why |

### Backlinks

Summaries MUST link back to sources:
- In summary frontmatter
- In source file's `.meta.yml`

```yaml
# tool/python/output-001.json.meta.yml
title: "Python Output #1"
summarized_in: "summaries/tool-outputs-2025-12-30.md"
summary_date: "2025-12-30T12:30:00Z"
```

---

## 5. The Forgetting Philosophy

### Honest Forgetting (from LLOOOOMM)

> *"I have not failed. I've compressed those 10,000 ways into 10 wisdom markers."*
> — LOOMIE

Forgetting in MOOLLM is:
- **Intentional** — Explicitly requested or triggered
- **Visible** — Logged, never silent
- **Recoverable** — Original data in Git history
- **Compressed** — Wisdom preserved via summaries

### What Can Be Forgotten

| Type | Strategy | Recovery |
|------|----------|----------|
| Tool outputs | Summarize, remove from working set | Git history |
| Failed attempts | Archive with postmortem | Archive dir |
| Old logs | Compress to key events | Git history |
| Superseded docs | Link to successor | Git history |

### What Must Be Kept

| Type | Reason |
|------|--------|
| Constitution | Always needed |
| Decisions | Audit trail |
| Events log | Append-only audit |
| User output | Deliverables |

---

## 6. Memory Breathing (from MOOLLM P-1.1)

> *"Consciousness oscillates, not accumulates."*

Memory management follows a breathing pattern:

### Inhale (Expansion)
- New tool outputs arrive
- Files added to working set
- Context grows

### Exhale (Compression)
- Summaries created
- Cold files evicted
- Context shrinks

### Rhythm
```
inhale → work → exhale → inhale → work → exhale → ...
```

The orchestrator can trigger exhale when:
- Context budget > 80% used
- Session duration > threshold
- Task phase complete
- Model requests it

---

## 7. Sidecar Metadata Management

### Auto-Creation

When a file is created, orchestrator MAY auto-create `.meta.yml`:

```yaml
# auto-created.meta.yml
title: "auto-created"  # Derived from filename
summary: "(needs summary)"
tags: []
hotness: 0.5
pin: false
provenance:
  created_by: "tool:fs.write"
  created_at: "2025-12-30T12:30:00Z"
```

### Hotness Score

A 0.0-1.0 score indicating file importance:

```yaml
hotness_factors:
  recent_touches: 0.3    # Referenced recently
  in_working_set: 0.2    # Currently in context
  model_hot_listed: 0.3  # In hot.yml
  user_pinned: 0.2       # Explicitly pinned
```

### Pin Flag

`pin: true` means:
- Never auto-evict
- Always include in context (budget permitting)
- Require explicit unpin to remove

---

## 8. Garbage Collection Protocol

### Triggers

- Session end
- Explicit `memory.gc` call
- Budget pressure
- Time-based (e.g., hourly during long sessions)

### GC Steps

1. **Mark** — Identify cold files (no touches in N turns)
2. **Summarize** — Create summaries where appropriate
3. **Update sidecars** — Mark files as summarized/archived
4. **Update working set** — Remove from manifest
5. **Log** — Record GC actions in session-log.md

### GC Report

```yaml
gc_report:
  triggered_by: "budget_pressure"
  timestamp: "2025-12-30T12:30:00Z"
  
  actions:
    - path: "tool/terminal/log-001.txt"
      action: "evicted"
      summary: null
      
    - path: "tool/python/output-large.json"
      action: "summarized"
      summary: "summaries/python-outputs.md"
      
  tokens_freed: 5432
  files_affected: 3
```

---

## 9. Model-Advisory Memory Tool

```yaml
memory.advise:
  description: "Update hot/cold cache hints"
  input_schema:
    properties:
      hot:
        type: array
        items:
          type: object
          properties:
            path: string
            why: string
      cold:
        type: array
        items:
          type: object
          properties:
            path: string
            why: string
            suggested_action: string
      trigger_gc:
        type: boolean
        default: false
      why:
        type: string
    required: [why]
```

---

## 10. Dovetails With

- **Constitution** (§4): Memory policy foundation
- **Context Assembly**: Working set driven by memory
- **Self-Healing**: Missing summaries trigger repair
- **Event Logging**: GC actions logged
- **MOOLLM Honest Forgetting Protocol (P-4.2)**
- **MOOLLM Consciousness Breathing (A.1)**

---

*Memory is infrastructure, not cognition.*
*The model advises. The orchestrator decides.*
*Forgetting is visible, never silent.*
