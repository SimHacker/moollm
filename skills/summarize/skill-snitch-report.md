# Skill Snitch Report: summarize

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** KEEP THE ESSENCE. DROP THE NOISE.

---

## Executive Summary

**Context compression without losing truth.**

Create metadata sidecars. Sip before gulping.

"LLM reads foo-metadata.yml (tiny), decides if foo.yml is needed."

---

## Methods

| Method | Purpose |
|--------|---------|
| **SUMMARIZE** | Compress content |
| **EXTRACT** | Pull key points |
| **METADATA** | Create sidecar file |
| **SIP** | Read metadata to decide if full file needed |
| **BOOKMARK** | Add named pointer into file |

---

## Metadata Sidecar Protocol

For any `foo.yml`, create `foo-metadata.yml`:

```yaml
original-path: "./lord-shadow.yml"
size-hint: "180 lines"
keywords: [villain, boss, final-battle]

summaries:
  brief: "Evil overlord. Final boss."
  standard: "Lord Shadow, former hero corrupted..."
  detailed: "Full backstory..."
  combat: "Level 20 boss. Weak to sunlight."
  spoiler-free: "A mysterious dark lord."

bookmarks:
  - name: motivation
    line: 42
    note: "Why they turned evil"
  - name: weakness
    pattern: "^weakness:"
    note: "How to defeat"

visuals:
  icon:
    prompt: "Dark hooded figure..."
    style: "flat, 64x64"
```

---

## Multi-Focus Summaries

Different summaries for different needs:
- **brief** — One line
- **standard** — Paragraph
- **detailed** — Full context
- **combat** — Game stats
- **narrative** — Story hooks
- **spoiler-free** — Safe to share

---

## Bookmark Types

| Type | Example |
|------|---------|
| **Point** | line: 42 |
| **Region** | lines: "15-45" |
| **Pattern** | pattern: "^weakness:" |
| **Anchor** | anchor: "&combat-stats" |

---

## Security Assessment

### Concerns

1. **Summary distortion** — lossy compression
2. **Stale metadata** — file changes, sidecar doesn't

### Mitigations

- Principles: preserve truth, cite source
- last-modified tracking
- changes log for incremental updates

**Risk Level:** LOW — explicit about compression

---

## Principles

| Principle | Rule |
|-----------|------|
| **preserve-truth** | Never invent or distort |
| **highlight-key** | Main points first |
| **cite-source** | Link back to original |
| **compression-ratio** | Aim for 10:1 |
| **sip-before-gulp** | Metadata first, full file maybe |

---

## Verdict

**TOKEN-EFFICIENT BROWSING. APPROVE.**

Keep the essence. Drop the noise.

Sip metadata. Gulp full files only when needed.
