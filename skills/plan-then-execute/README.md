# 🔒 Plan Then Execute

> Frozen plans with human approval gates

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [planning/](../planning/) | Flexible, evolving plans |
| [action-queue/](../action-queue/) | Task scheduling |
| [representation-ethics/](../representation-ethics/) | Human approval gates |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Two-phase execution: **plan in isolation, execute the frozen sequence**. Security first — tool outputs cannot alter the plan.

## Why This Exists

If tool outputs can alter later actions, injected instructions may redirect the agent. This skill enforces:

1. **Plan phase** — Generate tool sequence before seeing untrusted data
2. **Approval gate** — Human reviews and approves
3. **Execution phase** — Run exactly that sequence

## Example

```yaml
plan:
  name: "Deploy to staging"
  status: approved  # Frozen after approval
  
  steps:
    - id: 1
      tool_call:
        tool: "terminal.run"
        args: { command: "npm test" }
      status: pending
```
