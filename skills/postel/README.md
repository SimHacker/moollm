# 📬 Postel

> Be conservative in what you send, liberal in what you accept

**Quick Links:**
- [Full Specification](SKILL.md) — complete protocol

## Overview

**POSTEL** is how MOOLLM handles ambiguity, errors, and incomplete instructions. Instead of failing, find the **best possible interpretation** that accomplishes the likely intent.

## The Protocol

```
1. GATHER context — what do we know?
2. INFER intent — what did they probably mean?
3. PROPOSE interpretation — state your understanding
4. ACT constructively — do the reasonable thing
5. REPORT uncertainty — flag what you assumed
```

## Also Known As

- The Robustness Principle
- Postel's Law (RFC 761, 1980)
- Best Possible Interpretation
- Charitable Interpretation

## Related Skills

- [yaml-jazz](../yaml-jazz/) — flexible interpretation of structure
- [honest-forget](../honest-forget/) — graceful handling of gaps
