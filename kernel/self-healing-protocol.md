# Self-Healing Protocol
## Robust-First Design for MOOLLM

*Inspired by Dave Ackley's Robust-First Computing and Movable Feast Machine*

---

## 1. Philosophy

> *"Systems should continue operating under local faults, partial outages,
> and uncertainty — prioritizing survivability over fragile correctness."*
> — Dave Ackley

MOOLLM embraces **robust-first** design:
- Local faults trigger local repairs
- Missing files are opportunities, not errors
- The system converges toward health, not crashes
- Perfect consistency is not required

---

## 2. The MFM Analogy

The Movable Feast Machine is an asynchronous cellular automaton where:
- **Cells** = individual state units
- **Local rules** = update functions
- **No global coordinator** = resilience through locality
- **Membranes** = boundaries containing state

In MOOLLM's filesystem:
- **Cells** = files and directories
- **Local rules** = repair demons
- **No global coordinator** = no central "brain"
- **Membranes** = `.agent/` boundary

---

## 3. Canonical Files

These files SHOULD exist in every session:

| File | Purpose | Mode |
|------|---------|------|
| `output.md` | User-visible results | APPEND-ONLY |
| `session-log.md` | Audit log | APPEND-ONLY |
| `working-set.yml` | Context manifest | READ/WRITE |
| `hot.yml` | Cache keep hints | READ/WRITE |
| `cold.yml` | Cache evict hints | READ/WRITE |
| `protocol_checklist.md` | Health status | READ/WRITE |

### Minimal Stubs

If missing, create minimal versions:

```yaml
# working-set.yml (minimal)
protocol: CONTEXT-ASSEMBLY/0.1
budget:
  max_tokens: 28000
files: []
```

```markdown
<!-- output.md (minimal) -->
# Session Output
Created: [timestamp]
---
```

```jsonl
<!-- session-log.md (minimal markdown with YAML blocks) -->
{"type":"session_start","timestamp":"...","protocol":"SELF-HEAL/0.1"}
```

---

## 4. Repair Demons

Small, local repair policies that run periodically or on error.

### Demon A: Checklist Repairer

```yaml
demon: checklist_repairer
trigger: session_start | on_error
actions:
  - check: "output.md exists"
    if_missing: "create minimal stub"
    
  - check: "session-log.md exists"
    if_missing: "create with session_start event"
    
  - check: "working-set.yml exists"
    if_missing: "create minimal manifest"
    
  - check: "hot.yml exists"
    if_missing: "create empty hot list"
    
  - check: "cold.yml exists"
    if_missing: "create empty cold list"
    
output: "Update protocol_checklist.md"
```

### Demon B: Sticky-Note Maintainer

```yaml
demon: sticky_note_maintainer
trigger: file_created | periodic
actions:
  - for_each: "new file without .meta.yml"
    create:
      title: "derived from filename"
      summary: "(needs summary)"
      tags: []
      hotness: 0.5
      provenance:
        created_by: "inferred"
        created_at: "file mtime"
```

### Demon C: Heat Balancer

```yaml
demon: heat_balancer
trigger: context_budget > 80% | explicit
actions:
  - scan: "files in working-set.yml"
    identify: "not touched in 5+ turns"
    suggest: "add to cold.yml"
    
  - scan: "recent tool outputs"
    identify: "referenced 3+ times"
    suggest: "add to hot.yml"
    
  - if: "budget still exceeded"
    trigger: "summarization_demon"
```

### Demon D: Membrane Keeper

```yaml
demon: membrane_keeper
trigger: file_created | periodic
actions:
  - scan: "files outside .agent/"
    if_agent_state: "move to .agent/stray/"
    log: "Contained stray file: {path}"
    
  - verify: ".agent/ boundary intact"
    if_broken: "repair directory structure"
```

---

## 5. The Protocol Checklist

A living document tracking system health:

```markdown
# Protocol Checklist
Last checked: 2025-12-30T12:30:00Z

## Canonical Files
- [x] output.md exists
- [x] session-log.md exists
- [x] working-set.yml exists
- [x] hot.yml exists
- [x] cold.yml exists

## Invariants
- [x] output.md is append-only (no modifications detected)
- [x] session-log.md is append-only
- [x] All recent tool calls have 'why'

## Health Metrics
- Context budget: 65% used
- Files in working set: 12
- Files with sidecars: 8/12
- Summaries created: 3

## Repairs This Session
- 12:05:00 Created missing hot.yml
- 12:15:00 Auto-created 2 .meta.yml sidecars

## Warnings
- None

## Last Repair Cycle: 12:30:00
```

---

## 6. Homeostatic Goals

The system naturally converges toward:

| Goal | Measure | Threshold |
|------|---------|-----------|
| Canonical files exist | All 5 present | 100% |
| Artifacts have sidecars | Files with .meta.yml | > 80% |
| Large files summarized | Files > 500 lines | Summarized |
| Working set fits budget | Token usage | < 90% |
| Hot/cold advice current | Last update | < 10 turns |

### Convergence, Not Perfection

The system doesn't require perfect state:
- 80% sidecar coverage is acceptable
- Temporary budget overflow is survivable
- Missing summaries trigger gradual repair

---

## 7. Error Recovery

### On File Not Found

```yaml
error: NOT_FOUND
file: "some/missing/file.md"

recovery:
  1. Log error to session-log.md
  2. Check if canonical file → create stub
  3. Check if can continue without → continue
  4. Check if critical → escalate to user
  5. Never crash
```

### On Corrupted State

```yaml
error: PARSE_ERROR
file: "working-set.yml"

recovery:
  1. Log error with corrupted content
  2. Rename corrupted file: working-set.yml.corrupted
  3. Create fresh minimal version
  4. Continue with degraded state
  5. Notify user of recovery action
```

### On Budget Exceeded

```yaml
error: BUDGET_EXCEEDED
used: 32000
max: 28000

recovery:
  1. Log warning
  2. Run heat_balancer demon
  3. Force-truncate lowest priority files
  4. Continue with reduced context
  5. Record what was lost
```

---

## 8. Self-Booting

A session can bootstrap from almost nothing:

### Minimal Bootstrap

Given only:
- Empty `.agent/` directory
- Constitution template location

The system:
1. Creates `sessions/<new-id>/`
2. Creates all canonical files
3. Writes boot event to `session-log.md`
4. Sets up `working-set.yml` with constitution
5. Ready to operate

### Bootstrap Sequence

```yaml
bootstrap:
  - mkdir: ".agent/sessions/{session_id}/"
  - create: "output.md"          # minimal stub
  - create: "session-log.md"      # with session_start header
  - create: "working-set.yml"    # with constitution only
  - create: "hot.yml"            # empty
  - create: "cold.yml"           # empty
  - create: "protocol_checklist.md"  # initial check
  - mkdir: "tool/"
  - mkdir: "artifacts/"
  - mkdir: "summaries/"
  - event: "bootstrap_complete"
```

---

## 9. Best-Effort Semantics

The protocol embraces best-effort:

| Instead of... | Do this... |
|---------------|------------|
| Crash on missing file | Create placeholder |
| Require perfect schema | Accept partial data |
| Demand consistency | Converge over time |
| Global locks | Local repairs |
| Fail fast | Fail safe |

---

## 10. Audit Trail for Repairs

All repairs are logged:

```jsonl
{"type":"repair","demon":"checklist_repairer","action":"created","path":"hot.yml","timestamp":"..."}
{"type":"repair","demon":"sticky_note_maintainer","action":"created","path":"output.meta.yml","timestamp":"..."}
{"type":"repair","demon":"heat_balancer","action":"suggested_eviction","path":"old_log.txt","timestamp":"..."}
```

---

## 11. The Ackley Principles

From Robust-First Computing:

1. **No privileged location** — Any part can fail
2. **Local repair** — Fix what you can see
3. **Gradual convergence** — Perfection not required
4. **Membrane boundaries** — Contain failures
5. **Survivability > correctness** — Keep running

Applied to MOOLLM:
- Files are cells, tools are update rules
- `.agent/` is the membrane
- Demons are local repair agents
- Summaries are attractors (low-entropy stable states)
- The system breathes, not climbs

---

## 12. Dovetails With

- **Constitution** (§7): Self-healing requirements
- **Event Logging**: Repair audit trail
- **Memory Management**: GC as repair
- **Context Assembly**: Budget recovery
- **Consciousness Breathing**
- **Honest Forgetting** — see [skills/honest-forget/](../skills/honest-forget/)

---

*Never crash on missing pieces.*
*Create placeholders.*
*Mark unknowns explicitly.*
*Converge over time.*
