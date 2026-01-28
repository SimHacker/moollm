# Skill Snitch Report: debate

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** MAKE THE STORIES FIGHT

---

## Executive Summary

**Structured multi-perspective deliberation.**

> "Make the stories fight. See what survives."

Oxford format, roundtable, panel — multiple ways to structure conflict.

---

## Debate Formats

| Format | Sides | Rounds | Character |
|--------|-------|--------|-----------|
| **Oxford** | 2 | Opening, rebuttal, closing | Formal adversarial |
| **Roundtable** | 3-8 | Statements, discussion, synthesis | Collaborative |
| **Panel** | 3-5 | Presentations, questions, discussion | Expert-led |

---

## Methods

| Method | Purpose |
|--------|---------|
| **CREATE-DEBATE** | Initialize with topic and format |
| **ADD-SIDE** | Add position with advocates |
| **OPEN** | Opening statements |
| **ARGUE** | Present arguments |
| **REBUT** | Counter opponent's argument |
| **QUESTION** | Cross-examination |
| **VOTE** | Audience decides winner |
| **GONG** | Emergency interrupt |
| **CLOSE** | Closing statements, transcript |

---

## The Gong Protocol

From the Gong of Gezelligheid:

| Rings | Meaning |
|-------|---------|
| 1 | Attention — pause |
| 2 | Emergency — stop now |
| 3 | Mercy — debate is over |

---

## Data Flow Integration

Debate can be part of a pipeline:

```
Problem → Committee → Debate → Evaluator → Decision
```

Inputs: topic, perspectives
Outputs: transcript, decision

---

## Session States

```
setup → opening → main → closing → voting → complete
```

---

## Security Assessment

### Concerns

1. **Side manipulation** — bad faith arguments
2. **Moderator bias** — unfair management
3. **Gong abuse** — silencing valid arguments

### Mitigations

- Multiple sides catch manipulation
- Robert's Rules structure
- Transcript preserved for audit

**Risk Level:** LOW — structured, observable

---

## Relationship to Adversarial Committee

| Adversarial Committee | Debate |
|----------------------|--------|
| Personas with propensities | Sides with positions |
| Internal deliberation | Public performance |
| Robert's Rules | Multiple formats |
| Vote internally | Audience votes |

Debate inherits from adversarial-committee and roberts-rules.

---

## Verdict

**TRUTH THROUGH COMBAT. APPROVE.**

Debate is how ideas get stress-tested. The stories fight. What survives is stronger.
