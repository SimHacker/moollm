# Skill Snitch Report: protocol (K-lines)

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** MINSKY'S MAGIC

---

## Executive Summary

**K-lines as semantic activation.** Saying the name activates a constellation of knowledge and behavior.

This is how MOOLLM protocols work. This is Marvin Minsky's insight from 1986.

---

## The K-line Insight

> Marvin Minsky's K-lines: a symbol that when activated reactivates the mental state from when it was learned.

When you say **ADVENTURE**, you activate:
- Text adventure patterns
- Room navigation
- LOOK, GO, TAKE commands
- Dungeon master narration

The single word **is** the activation.

---

## Methods

| Method | Purpose |
|--------|---------|
| **INVOKE** | Activate protocol by name |
| **DEFINE** | Create new protocol |
| **LIST** | Show available protocols |
| **K-REF** | Emit file pointer with metadata |
| **SISTER-SCRIPT** | Tool emits K-REFs, LLM reads selectively |

---

## K-REF Format

```
PATH[:LINE[-END]][#anchor][?search] # TYPE - DESC
```

Examples:
```
/path/file.txt:42:10-46 # secret 🔴
/path/screenshot.png # image - Cursor reads and analyzes!
/any/absolute/path/diagram.jpg # visual
```

**Critical:** Cursor can read **absolute paths** including **images**.

---

## Sister Script Pattern

1. Tool scans (fast, cheap)
2. Tool emits K-REFs (pointers, not content)
3. LLM reads selectively (parsimonious context usage)

This is how cursor-mirror works efficiently.

---

## Protocol Examples

| Protocol | Activates |
|----------|-----------|
| **ADVENTURE** | Text adventure patterns |
| **YAML-JAZZ** | Flexible YAML patterns |
| **PLAY-LEARN-LIFT** | The methodology |
| **BOOTSTRAP** | Session startup sequence |
| **PSIBER** | Data as navigable room |

---

## Security Assessment

### Concerns

1. **Arbitrary file reads** — K-REF can point anywhere
2. **Image analysis** — Cursor reads images from absolute paths
3. **Protocol injection** — Malicious protocol definitions

### Mitigations

- K-REF is read-only
- Image analysis is Cursor's capability
- Protocol definitions are visible in PROTOCOLS.yml

**Risk Level:** MEDIUM — powerful file access

---

## The Minsky Connection

Marvin Minsky, *Society of Mind* (1986):

> A K-line is a wirelike structure that attaches itself to whichever mental agents are active when you solve a problem or have a good idea. When you activate that K-line later, the agents attached to it are partially activated, creating a mental state similar to the original.

MOOLLM protocols ARE K-lines:
- **YAML-JAZZ** reactivates the mental state of "flexible semantic YAML"
- **ADVENTURE** reactivates "text adventure dungeon master"
- **BOOTSTRAP** reactivates "session startup orientation"

---

## Why This Matters

Without K-lines, every task requires full context injection.

With K-lines, a **single word** activates the relevant constellation.

This is massive compression:
- "ADVENTURE" = ~5000 tokens of context
- The LLM already knows text adventures
- We just need to **activate** that knowledge

---

## Verdict

**FOUNDATIONAL THEORY. APPROVE.**

K-lines are the **theoretical foundation** of MOOLLM protocols.

Saying the name IS the magic. Minsky knew this in 1986. We're just applying it to LLMs.
