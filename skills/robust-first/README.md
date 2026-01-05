# 🛡️ Robust First

> Survive first. Be correct later.

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

Dave Ackley's principle: systems should prioritize **survivability** over **correctness**.

A system that crashes when confused is useless. A system that limps along incorrectly but keeps running can be repaired.

## The Philosophy

Traditional computing:
```
IF error THEN crash
"Fail fast and loud"
```

Robust-first computing:
```
IF error THEN repair_locally AND continue
"Stay alive and heal"
```

## Core Principles

1. **Never Crash** — Keep running, always
2. **Local Repair** — Fix problems where they occur
3. **Graceful Degradation** — Partial function beats no function
4. **Self-Healing** — Systems should repair themselves

## Related Skills

- [self-repair](../self-repair/) — repair mechanisms
- [postel](../postel/) — liberal interpretation
- [honest-forget](../honest-forget/) — graceful compression
