# 📋 Planning

> Structured task decomposition and tracking

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol
- [Template: PLAN.yml](PLAN.yml.tmpl) — plan template
- [Template: PROGRESS.md](PROGRESS.md.tmpl) — progress log

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

## Related Skills

- [plan-then-execute](../plan-then-execute/) — rigid execution mode
- [action-queue](../action-queue/) — task scheduling
- [debugging](../debugging/) — investigation planning