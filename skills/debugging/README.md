# 🔧 Debugging

> Systematic bug investigation with hypothesis tracking

## MOOLLM K-Lines

| K-Line | Why Related |
|--------|-------------|
| [adventure/](../adventure/) | Debugging IS adventure + hypothesis tracking |
| [sniffable-python/](../sniffable-python/) | Readable code aids debugging |
| [scratchpad/](../scratchpad/) | Debug scratch notes |
| [research-notebook/](../research-notebook/) | Investigation notes |
| [sister-script/](../sister-script/) | Document the fix |
| [session-log/](../session-log/) | Track all debug steps |
| [self-repair/](../self-repair/) | Automated fixes |
| [play-learn-lift/](../play-learn-lift/) | Debugging IS learning |
| [constructionism/](../constructionism/) | Try → Inspect → Hypothesize → Modify |

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol and schemas

## Overview

Debug problems methodically. Track hypotheses, test systematically, converge on root causes. Treats debugging as a structured adventure where each hypothesis is a quest to validate or refute.

The debugging loop: **OBSERVE → HYPOTHESIZE → TEST → LEARN → FIX**

## Key Techniques

| Technique | When to Use |
|-----------|-------------|
| Binary Search | Bug is somewhere in large space |
| Rubber Duck | Stuck, need fresh perspective |
| Minimal Repro | Complex system, unclear cause |
| Git Bisect | Bug is a regression |
| Print Debug | Need to understand flow |

## Example Session

```yaml
debug:
  bug: "Login fails with valid credentials"
  
  hypotheses:
    - id: 1
      claim: "Password hashing mismatch"
      status: refuted
      evidence: "Hashes match in logs"
      
    - id: 2
      claim: "Session cookie not set"
      status: confirmed
      evidence: "Cookie missing in response headers"
      
  fix: "Add Set-Cookie header to auth response"
  verified: true
```

