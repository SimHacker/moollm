# Skill Snitch Report: debugging

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** DEBUGGING IS AN ADVENTURE. THE BUG IS THE TREASURE.

---

## Executive Summary

**Hypothesis-driven bug hunting.**

Form theories, test them, narrow down.

Treat it as an adventure where the bug is the treasure to find.

---

## Methods

| Method | Purpose |
|--------|---------|
| **START** | Begin investigation |
| **HYPOTHESIZE** | Form a theory |
| **TEST** | Test a hypothesis |
| **NARROW** | Eliminate possibilities |
| **TRACE** | Follow execution path |
| **BISECT** | Binary search for introduction point |
| **FIX** | Apply a fix |
| **DOCUMENT** | Record findings |

---

## Debug Session States

```
investigating → narrowing → fixing → verifying → resolved
                                               ↘ abandoned
```

---

## Strategies

| Strategy | Description |
|----------|-------------|
| **Wolf Fence** | Bisect the search space |
| **Rubber Duck** | Explain the problem out loud |
| **Simplify** | Remove complexity until bug disappears |
| **Fresh Eyes** | Step away, return later |
| **Assumptions** | Question everything you "know" |

---

## The BISECT Method

```
good (known working) ←──────────────────→ bad (broken)
                            ↓
                         test midpoint
                            ↓
              ┌─────────────┴─────────────┐
              ↓                           ↓
          good → bad                   bad → bad
       (bug in right half)          (bug in left half)
```

Binary search for when bug was introduced.

---

## Security Assessment

### Concerns

None. It's bug hunting methodology.

**Risk Level:** ZERO — pure investigation

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **Wolf fence algorithm** | Bisection |
| **Git bisect** | Version bisection |
| **Scientific method** | Hypothesis testing |

---

## Verdict

**SYSTEMATIC BUG HUNTING. APPROVE.**

Debugging is an adventure.

The bug is the treasure.
