# Event Logging Protocol
## Append-Only Audit Trail in Human-Readable Format

---

## 1. Overview

Every action in MOOLLM is logged to an append-only event stream.
This provides:
- Perfect audit trail
- Replay capability  
- Debugging support
- Analytics foundation

**Format Philosophy:** Events are logged to Markdown files with embedded YAML/JSON code blocks. Markdown is maximally human-readable while still supporting arbitrary structured data. YAML is preferred for its support of comments—**comments carry meaning**.

**Invariant:** Session logs are APPEND-ONLY. Never modify, never delete.

---

## 2. Why Markdown Over JSONL

| Aspect | JSONL | Markdown + Code Blocks |
|--------|-------|------------------------|
| Human readability | Poor | Excellent |
| Git diffs | Noisy | Clean |
| Comments | None | Full support |
| Context | None | Narrative possible |
| Parsing | Direct | Requires block extraction |
| Flexibility | Rigid | Arbitrary verbosity |

**The key insight**: Debugging is a human activity. Logs should serve humans first, machines second. Structured data lives in fenced code blocks; narrative context lives around them.

---

## 3. Log File Structure

### Location
```
.agent/sessions/<session_id>/session-log.md
```

### Format

```markdown
# Session Log: <session_id>

Started: 2025-12-30T12:00:00Z
Protocol: EVENT-LOG/0.2

---

## 12:00:00 — Session Start

<!-- Minimal metadata for session initialization -->

```yaml
type: session_start
session_id: sess-001
protocol: EVENT-LOG/0.2
```

---

## 12:00:05 — Tool Call: fs.read

Reading parser to check recursive descent handling.

```yaml
type: tool_call
tool: fs.read
call_id: call-001
args:
  path: src/parser.ts
  # Check if the recursive descent handles nested expressions
  # This is part of the expression parser audit
  why: "Check if recursive descent handles nested expressions"
```

---

## 12:00:05 — Tool Result: fs.read

```yaml
type: tool_result
call_id: call-001
success: true
duration_ms: 12
result:
  lines: 50
  # File contains the expected parseExpression function
```

---
```

### Key Principles

1. **Timestamps as headers** — Easy visual scanning
2. **Narrative before blocks** — Human context first
3. **YAML in code blocks** — Parseable structure
4. **Comments inside YAML** — Intent and context preserved
5. **Horizontal rules** — Clear event separation

---

## 4. Event Types

### Session Events

```yaml
# Session start - always first entry
type: session_start
timestamp: "2025-12-30T12:00:00Z"
session_id: sess-001
protocol: EVENT-LOG/0.2
# Optional context about what this session is for
purpose: "Debugging the expression parser"
```

```yaml
# Session end - always last entry
type: session_end
timestamp: "2025-12-30T14:30:00Z"
session_id: sess-001
reason: user_exit
stats:
  turns: 45
  tools: 123
  # High repair count suggests fragile state going in
  repairs: 7
```

### Tool Events

```yaml
type: tool_call
tool: fs.read
call_id: call-001
args:
  path: src/parser.ts
  # The 'why' is REQUIRED - it's not bureaucracy, it's self-documentation
  why: "Check if recursive descent handles nested expressions"
```

```yaml
type: tool_result
call_id: call-001
success: true
duration_ms: 12
result:
  lines: 50
  # Truncated actual content - just metadata here
```

```yaml
type: tool_error
call_id: call-001
error:
  code: NOT_FOUND
  message: "File not found: src/parser.ts"
  # Recovery suggestion for self-healing
  suggestion: "Check if file was renamed or moved"
```

### Model Events

```yaml
type: model_input
timestamp: "..."
tokens: 2500
files_in_context:
  - a.md
  - b.md
# Context was tight - watch for truncation issues
budget_usage: 0.89
```

```yaml
type: model_output
timestamp: "..."
tokens: 500
tool_calls: 1
# Model seemed confident about the fix
text_length: 1200
```

### Memory Events

```yaml
type: context_assembly
timestamp: "..."
budget: 28000
used: 23456
included:
  - a.md  # Hot - actively working
  - b.md  # Hot - referenced by a.md
excluded:
  - old_log.md  # Cold - not needed this turn
# Approaching budget limit - consider summarization
warning: "Budget usage at 84%"
```

```yaml
type: gc_run
trigger: budget
freed_tokens: 5000
files_affected: 3
# Summarized rather than deleted
action: summarize_then_evict
```

### Repair Events

```yaml
type: repair
demon: checklist_repairer
action: created
path: hot.yml
# File was missing, created minimal stub
stub_contents: "keep: []"
```

```yaml
type: bootstrap
# Fresh session, created canonical files
files_created:
  - output.md
  - session-log.md
  - working_set.yml
```

### User Events

```yaml
type: user_message
timestamp: "..."
length: 150
attachments:
  - file.png
# Message tone: question about implementation
```

```yaml
type: user_approval
action: tool_call
tool: terminal.run
approved: true
# User reviewed the command before execution
command_preview: "npm test"
```

---

## 5. Verbosity Levels

Log verbosity should adapt to context:

### Minimal (Production)
Just types, timestamps, success/failure.

```yaml
type: tool_result
call_id: call-001
success: true
```

### Standard (Development)
Add args, results, and key comments.

```yaml
type: tool_result
call_id: call-001
success: true
duration_ms: 12
result:
  lines: 50
# Parser looks correct
```

### Verbose (Debugging)
Full context, reasoning, suggestions.

```yaml
type: tool_result
call_id: call-001
success: true
duration_ms: 12
result:
  lines: 50
  first_line: "export function parseExpression(tokens: Token[])"
  # Contains recursive call at line 23
  # Uses precedence climbing, not recursive descent
  analysis_notes: |
    This is actually precedence climbing, not recursive descent.
    The recursion is in parseAtom, not parseExpression itself.
    Need to revise the audit approach.
```

---

## 6. Append-Only Guarantee

### Why Append-Only?

1. **Audit integrity** — History cannot be rewritten
2. **Debugging** — Full trace of what happened
3. **Replay** — Can reconstruct any past state
4. **Trust** — Users can verify agent behavior

### Enforcement

- Orchestrator MUST only append to session-log.md
- Model CANNOT call write tools on session-log.md except to append
- Any modification attempt is logged as a violation
- Corruption triggers recovery (backup + new file)

### Recovery from Corruption

```yaml
if session_log corrupted:
  1. rename: session-log.md → session-log.md.corrupted
  2. create: session-log.md (fresh)
  3. append:
    type: recovery
    from: corruption
    backup: session-log.md.corrupted
    # Human should review corrupted file
```

---

## 7. Querying Events

Events can be extracted and queried:

```bash
# Extract all YAML blocks from log
grep -Pzo '```yaml\n[\s\S]*?```' session-log.md

# Find all tool errors
grep -A 10 'type: tool_error' session-log.md

# Count events by type
grep '^type:' session-log.md | sort | uniq -c
```

### For Programmatic Access

Parse the markdown, extract fenced code blocks, parse as YAML:

```python
import re
import yaml

def extract_events(log_path):
    content = open(log_path).read()
    blocks = re.findall(r'```yaml\n(.*?)```', content, re.DOTALL)
    return [yaml.safe_load(block) for block in blocks]
```

---

## 8. Event Retention

### During Session
- All events kept in session-log.md
- No pruning during active session

### After Session

```yaml
retention_policy:
  hot: "keep indefinitely"    # Recent sessions
  warm: "compress after 7d"   # Older sessions  
  cold: "archive after 30d"   # Much older
  
compression:
  # Remove verbose results but keep the narrative
  - Collapse repetitive tool calls into summaries
  - Keep error and repair events (debugging gold)
  - Preserve all comments (they carry meaning!)
```

### Session Summary

At session end, generate a summary:

```yaml
# session-summary.yml (generated at session end)
session_id: sess-001
duration_minutes: 150
turns: 45

tool_usage:
  fs.read: 67   # Heavy reading - exploration phase
  fs.write: 23  # Moderate writing - implementation
  search.vector: 15
  terminal.run: 8  # Some test runs

errors:
  total: 3
  by_code:
    NOT_FOUND: 2  # Missing files - need better discovery
    TIMEOUT: 1

repairs:
  total: 5
  by_demon:
    checklist_repairer: 2
    sticky_note_maintainer: 3
    
# Session seemed productive - completed main task
retrospective: |
  Started with parser audit, discovered it uses precedence climbing.
  Refactored the audit approach mid-session.
  Main goal achieved, some cleanup remaining.
```

---

## 9. Comments Are Sacred

**YAML comments in logs are not decoration—they are data.**

Good log entry:
```yaml
type: tool_call
tool: fs.write
args:
  path: output.md
  content: "..."
  # Appending final summary after all tests passed
  # This concludes the debugging session
  why: "Append final summary"
```

Bad log entry:
```yaml
type: tool_call
tool: fs.write
args:
  path: output.md
  content: "..."
  why: "Append final summary"
```

The comments provide context that the structured fields cannot capture.

---

## 10. Dovetails With

- **Constitution** (§6): Audit requirements
- **Tool Calling Protocol**: Tool events, `why` parameter
- **Memory Management**: GC events, summarization
- **Self-Healing Protocol**: Repair events
- **YAML Jazz**: Comments carry meaning

---

*Every action leaves a trace.*
*The trace is human-readable.*
*The trace enables trust.*
