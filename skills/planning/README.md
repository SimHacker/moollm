# 📋 Planning

> Structured task decomposition and tracking

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [play-learn-lift/](../play-learn-lift/) | Plans evolve via LEARN |
| [scratchpad/](../scratchpad/) | Draft plans in scratchpad |
| [plan-then-execute/](../plan-then-execute/) | Rigid execution mode |
| [action-queue/](../action-queue/) | Task scheduling |
| [sister-script/](../sister-script/) | Plans become automation |
| [debugging/](../debugging/) | Investigation planning |
| [session-log/](../session-log/) | Log plan progress |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Turn complex goals into actionable steps. Plans are **living documents** that evolve as you learn.

Unlike [plan-then-execute](../plan-then-execute/), these plans adapt.

## Structure

```yaml
plan:
  goal: "Implement authentication system"
  status: in_progress
  
  tasks:
    - id: 1
      name: "Design auth flow"
      status: done
      
    - id: 2
      name: "Implement login"
      status: in_progress
```
