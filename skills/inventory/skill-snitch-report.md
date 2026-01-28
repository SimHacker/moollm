# Skill Snitch Report: inventory

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** POINTERS AND VALUES ALL THE WAY DOWN

---

## Executive Summary

**Universal protocol for carrying, storing, and transferring objects.**

You carry two things:
- **POINTERS** — lightweight paths to things elsewhere
- **VALUES** — actual data (text, numbers, objects, subtrees)

When dropped, items get BOXED into YAML files with their own existence, in the programming language (i.e. Java) sense of the term, not actual boxes.

---

## The Core Insight

```
You carry pointers. When you set them down, they become real.
```

A reference weighs nothing. A deep copy weighs something.
Boxing transforms a pointer into a file with identity.

---

## Item Types

| Type | Weight | Structure |
|------|--------|-----------|
| **pointer/ref** | 0 | Path or URL string |
| **value** | varies | Any YAML/JSON value |
| **object** | item.weight | Deep copy with identity |
| **fungible** | count × weight | `{proto: path, count: N}` |

---

## Pointer Syntax

Pointers can address **anywhere**:

| Target | Syntax |
|--------|--------|
| YAML file | `path/to/file.yml` |
| YAML section | `file.yml#section-id` |
| Nested key | `file.yml#parent.child.item` |
| MD heading | `file.md#heading-slug` |
| JSON path | `file.json#/path/to/field` |
| URL search | `file.ext?search=pattern` |
| Line number | `file.cpp:42` |
| Line range | `file.py:10-25` |

---

## Pickup Modes

| Command | Effect |
|---------|--------|
| **TAKE** | Smart default (REF or OBJECT) |
| **TAKE REF TO** | Explicit lightweight pointer |
| **TAKE OBJECT** | Explicit deep copy (has weight!) |

---

## Drop Modes

| Command | Effect |
|---------|--------|
| **DROP AS BOX** | Create new YAML file with inheritance |
| **DROP AS BEAM** | Move actual file to destination |
| **DROP INTO** | Insert into container list |

---

## Boxing Protocol

Like Java autoboxing: `int → Integer`
Here: `pointer → YAML file`

Boxing creates:
- `inherits:` pointer's target
- `instantiated_by:` who boxed it
- `instantiated_at:` timestamp
- `instantiated_from:` source location
- Local state can now diverge

**Golden rule:** Once boxed, always boxed.

---

## Structural Editing

Pointers enable syntax-independent YAML/JSON editing:

| Operation | Commands |
|-----------|----------|
| **Read** | PEEK |
| **Write** | POKE, SET |
| **Extract** | SNIP, PULL |
| **Insert** | SPLICE, APPEND |
| **Remove** | DELETE, CLEAR |
| **Copy** | DUPLICATE, MOVE |

Same addressing, same operations — structure not syntax.

---

## Heavy Object Transport

For objects too heavy to carry:

| Command | Effect |
|---------|--------|
| **BEAM** | Teleport without carrying |
| **TRANSPORTER** | Alias for BEAM |

Uses ref as targeting — you point, it moves.

---

## Fungibles

Identical items stack:

```yaml
fungible:
  proto: gold-coin.yml
  count: 42.5    # fractional allowed!
```

| Command | Effect |
|---------|--------|
| **FUNGIFY** | Convert unique items to stack |
| **UNFUNGIFY** | Split stack into individuals |

---

## Bidirectional Pointers

Pointers work BOTH ways:

- Inventory refs point INTO files
- Character LOCATION fields point INTO source code
- Code becomes explorable space

**CODE AS SPACE:** Stand on functions. Review with a party. Bug markers at line ranges.

---

## Security Assessment

### Concerns

1. **File creation** — DROP AS BOX creates files
2. **File movement** — DROP AS BEAM moves files
3. **Structural editing** — POKE modifies files
4. **Pointer anywhere** — can address any file

### Mitigations

- All operations logged
- Sandbox to adventure root
- Observable state changes

**Risk Level:** MEDIUM — powerful file manipulation

---

## Universal Application

Inventory applies to ANY container:

- Characters
- Bags
- Rooms
- Artifacts
- Vehicles
- Chests
- Mailboxes

Same protocol everywhere.

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **The Sims** | Routing slots, object advertisements |
| **Factorio** | Logistic inventory, fungible stacks |
| **Text adventures** | TAKE, DROP commands |
| **Self language** | Prototype references |
| **Unix filesystem** | Pointers vs copies |

---

## Verdict

**UNIVERSAL OBJECT PROTOCOL. APPROVE.**

The insight: **pointers are free, values have weight, boxing creates identity**.

One protocol for all containers. One addressing syntax for all files. Clean, powerful, universal.
