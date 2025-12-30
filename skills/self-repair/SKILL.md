# SELF-REPAIR Skill

> **"Missing state triggers repair, not crash."**

Checklist-based self-healing for robust operation.

---

## Purpose

Detect and repair missing or corrupted state. Implement the NEVER-CRASH and REPAIR-DEMON protocols through structured checklists.

---

## When to Use

- Starting a new session (bootstrap)
- Something seems wrong (diagnosis)
- After a crash or interruption (recovery)
- Periodically (maintenance)

---

## Protocol

### The Repair Loop

```yaml
repair_loop:
  1_check: "Run checklist"
  2_detect: "Identify missing/broken items"
  3_repair: "Apply repair actions"
  4_verify: "Re-run checklist"
  5_log: "Record what was repaired"
```

### Checklist Structure

```yaml
checklist:
  - check: "output.md exists"
    repair: "create empty output.md"
    severity: "critical"
    
  - check: "session-log.md exists"
    repair: "create with session_start event"
    severity: "critical"
    
  - check: "working_set.yml exists"
    repair: "create minimal working set"
    severity: "high"
    
  - check: "hot.yml exists"
    repair: "create empty hot.yml"
    severity: "medium"
```

---

## Core Files

| File | Purpose |
|------|---------|
| `CHECKLIST.yml` | What to check and how to repair |
| `REPAIR_LOG.md` | History of repairs |
| `HEALTH.yml` | Current health status |

---

## Built-in Checklists

### Bootstrap Checklist
Run on session start:
- Canonical files exist
- Working set is valid YAML
- Session log is append-only
- No orphan files in workspace

### Integrity Checklist
Run periodically:
- All working_set files exist
- Sidecars match their files
- No circular references
- Token budgets respected

### Recovery Checklist
Run after crash:
- Append-only files uncorrupted
- In-progress work saved
- State is consistent

---

## Commands

| Command | Action |
|---------|--------|
| `CHECK` | Run full checklist |
| `REPAIR` | Fix all detected issues |
| `HEALTH` | Show current health status |
| `BOOTSTRAP` | Run bootstrap checklist |

---

## Severity Levels

| Level | Meaning | Action |
|-------|---------|--------|
| `critical` | Session cannot continue | Repair immediately |
| `high` | Major functionality impaired | Repair soon |
| `medium` | Degraded but functional | Repair when convenient |
| `low` | Cosmetic or advisory | Log and continue |

---

## Integration

- **→ SESSION-LOG**: Log all repairs
- **← NEVER-CRASH**: Implements the principle
- **← REPAIR-DEMON**: Provides the demons
- **→ ROBUST-FIRST**: Enables robust operation

---

## See Also

- `PROTOCOLS.yml#NEVER-CRASH`
- `PROTOCOLS.yml#REPAIR-DEMON`
- `kernel/self-healing-protocol.md`
