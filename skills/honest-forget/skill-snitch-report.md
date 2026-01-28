# Skill Snitch Report: honest-forget

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** FORGET WITH INTEGRITY. LEAVE A TOMBSTONE.

---

## Executive Summary

**Graceful memory compression.**

When context overflows, forget gracefully. Summarize. Leave a pointer.

Never pretend you remember what you don't.

---

## The Principle

LLMs will forget. Context windows overflow.

**The WRONG response:**
> "I remember everything about our conversation"

**The RIGHT response:**
> "I've forgotten the details. Here's a summary. Full log at ./archive/session-42.md"

Leave tombstones. Point to graves.

---

## Methods

| Method | Purpose |
|--------|---------|
| **COMPRESS** | Summarize and mark for forgetting |
| **ARCHIVE** | Move to long-term storage |
| **RECALL** | Retrieve archived content |
| **ADMIT** | Acknowledge forgotten content |

---

## FORGET.yml Schema

```yaml
original-path: archive/session-42.md
summary: "Session 42: Explored the maze, found the key"
forgotten-at: 2026-01-28T14:30:00Z
reason: "Context overflow"
```

---

## The Metadata Pattern

Instead of reading full files, create lightweight sidecars:

```yaml
# adventure-log-metadata.yml
file: adventure-log.md
summary: "Session 12: Party found the key"
size: 45KB
key-events: [found-key, met-sphinx]
worth-reading-if: "Need details about the maze"
```

Sip metadata before deciding to read full file.

---

## Security Assessment

### Concerns

1. **Lost information** — compression loses detail
2. **Stale pointers** — archives move or delete

### Mitigations

- Summaries preserve essence
- Pointers explicit and traceable
- Archival science principles

**Risk Level:** LOW — honest about limitations

---

## Verdict

**EPISTEMIC HUMILITY. APPROVE.**

Forget with integrity.

Leave tombstones. Point to graves. Never pretend.
