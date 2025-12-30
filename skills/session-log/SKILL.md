# SESSION-LOG Skill

> **"Every action leaves a trace."**

Structured logging for audit trails and debugging.

---

## Purpose

Maintain append-only session logs in human-readable Markdown with embedded YAML blocks. Support debugging, replay, and audit requirements.

---

## When to Use

- Starting any session (automatic)
- After significant actions
- When debugging issues
- For compliance/audit needs

---

## Protocol

### Log Format

Markdown with embedded YAML:

```markdown
## 2025-01-15T10:30:00Z — Tool Call: fs.read

Reading configuration to understand project setup.

```yaml
type: tool_call
tool: fs.read
args:
  path: config.yml
  why: "Understand project configuration"
call_id: call-001
```
```

### Event Types

```yaml
event_types:
  session:
    - session_start
    - session_end
    - session_pause
    - session_resume
    
  tool:
    - tool_call
    - tool_result
    - tool_error
    
  model:
    - model_input
    - model_output
    - model_turn
    
  memory:
    - context_assembly
    - working_set_update
    - gc_run
    - summary_created
    
  repair:
    - repair_action
    - bootstrap
    
  user:
    - user_message
    - user_approval
    - user_edit
```

---

## Core Files

| File | Purpose |
|------|---------|
| `session-log.md` | The append-only log |
| `SESSION.yml` | Session metadata |

---

## Commands

| Command | Action |
|---------|--------|
| `LOG [event]` | Add event to session log |
| `REPLAY [from] [to]` | Show log segment |
| `SEARCH [pattern]` | Find in log |
| `STATS` | Show session statistics |

---

## Append-Only Guarantee

```yaml
append_only_rules:
  - "NEVER modify past entries"
  - "NEVER delete entries"
  - "Only append new events"
  - "Corruption triggers backup + fresh file"
```

---

## Why Markdown + YAML?

| Feature | Benefit |
|---------|---------|
| Human-readable | Can review logs directly |
| Appendable | Natural append-only structure |
| Embedded YAML | Structured data when needed |
| YAML comments | Semantic annotations |
| Tool-friendly | grep, search, parse |

---

## Integration

- **← SELF-REPAIR**: Logs all repairs
- **← PLAN-THEN-EXECUTE**: Logs plan execution
- **→ SUMMARIZE**: Session logs can be summarized
- **→ AUDIT-TRAIL**: Provides the trail

---

## See Also

- `PROTOCOLS.yml#SESSION-LOG`
- `PROTOCOLS.yml#AUDIT-TRAIL`
- `kernel/event-logging-protocol.md`
