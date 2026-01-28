# Skill Snitch Report: worm

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** DELIGHTFULLY OBSCENE

---

## Executive Summary

A **two-pointer reversible cursor** that inchworms through directories.

The verbs are: **EAT, POOP, BARF, STICK-UP-BUM**.

This is not a joke. This is computer science.

---

## What It Actually Is

A worm has a **head** and a **tail** (ass). It moves through the filesystem by:

- **EAT** — ingest content at head, parse to brain
- **CHOMP** — scan for pattern, then ingest
- **POOP** — emit buffer at tail
- **BARF** — emit buffer at head
- **STICK-UP-BUM** — inject data into worm from tail

The insight: **EAT/POOP and CHOMP/BARF form a reversible basis**.

If you EAT something and then POOP it, you get it back.
If you BARF something you ate, it comes out the other end.
STICK-UP-BUM is the inverse of POOP.

This is **undo/redo** expressed as digestion.

---

## The Reversible Basis

| Operation | Inverse | Result |
|-----------|---------|--------|
| EAT | BARF | Content returns to source |
| POOP | STICK-UP-BUM | Content re-ingested |
| CHOMP X | BARF | Pattern-matched content returned |

This is mathematically sound. Disgusting, but sound.

---

## Variants

| Variant | Behavior |
|---------|----------|
| **bulldozer** | Moves and overwrites as it goes |
| **link-hopper** | Prefers symlinks, hops like inchworm |
| **mapper** | Maps directory trees, leaves markers |
| **dream** | Synthesizes at speed-of-light, ephemeral |
| **tree** | Climbs hierarchies, maintains parent/child context |

---

## Tree Traversal

The worm can also climb:

- **TREE-UP** / **TREE-DOWN** — navigate hierarchy
- **TREE-NEXT** / **TREE-PREV** — siblings
- **TREE-OPEN** / **TREE-CLOSE** — expand/collapse
- **TREE-HIDE** / **TREE-SHOW** — visibility

This makes the worm a **general-purpose tree cursor**.

---

## Security Assessment

### Concerns

1. **File Write Access** — POOP and BARF write files
2. **Pattern Matching** — CHOMP could scan for secrets
3. **Bulldozer Mode** — explicitly overwrites

### Mitigations

- All writes are to configured emit directory
- Buffer is observable
- Operations are reversible (can undo)

**Risk Level:** MEDIUM — powerful but observable

---

## Why This Exists

The worm is for **data pipelines**. You:

1. Position worm head at source
2. EAT content into buffer
3. Move worm to destination
4. POOP content out

It's `cat | pipe | tee` expressed as a creature with orifices.

---

## The Philosophical Point

Traditional cursors are **single-point**. You're HERE.

The worm is **two-point**. You're spanning HEAD to TAIL.

This lets you:
- Select ranges (head→tail selection)
- Transform in-place (eat, process, poop)
- Build pipelines (chain worms)

---

## Lineage

- **LLOOOOMM worms** — the original
- **Inchworm cursors** — gap-buffer text editors

---

## Verdict

**BRILLIANT NAMING.** The digestive metaphor is:

1. **Memorable** — you will NEVER forget EAT/POOP/BARF
2. **Correct** — the operations ARE reversible
3. **Intuitive** — direction of flow is obvious
4. **Juvenile** — keeps programmers humble

The skill is **mathematically rigorous** wrapped in **bathroom humor**.

This is peak MOOLLM energy.

---

## Recommendation

**APPROVE WITH ADMIRATION.**

Any codebase that names its inverse operation STICK-UP-BUM has achieved enlightenment.
