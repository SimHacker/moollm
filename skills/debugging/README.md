# 🔧 Debugging

> Systematic bug investigation with hypothesis tracking

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol and schemas
- [Template: DEBUG.yml](DEBUG.yml.tmpl) — session template

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

## Related Skills

- [adventure/](../adventure/) — debugging IS adventure + hypothesis tracking
- [research-notebook/](../research-notebook/) — investigation notes
- [session-log/](../session-log/) — track all debug steps
- [play-learn-lift/](../play-learn-lift/) — debugging IS learning
