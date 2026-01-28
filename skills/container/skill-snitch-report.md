# Skill Snitch Report: container

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** GROUPING WITHOUT LAYOUT

---

## Executive Summary

**Intermediate scope for inheritance and containment.**

Like OpenLaszlo's `<node>` — directories that provide inheritance without being navigable rooms.

---

## Container Schema

| Field | Purpose |
|-------|---------|
| **name** | Display name |
| **description** | What it represents |
| **inherits** | Properties flowing to children |
| **rules** | Rules within this scope |
| **defaults** | Default values for children |
| **constraints** | Things forbidden |
| **on_enter** | Expression for entering any child |
| **on_exit** | Expression for exiting any child |
| **ambient** | Environmental properties |

---

## Inheritance Resolution

```
1. self
2. parent_container
3. grandparent_container
4. adventure_defaults
5. skill_template
```

---

## Merge Strategy

| Type | Strategy |
|------|----------|
| Objects | deep_merge |
| Arrays | concatenate |
| Primitives | override |

---

## Ambient Properties

```yaml
ambient:
  sound: "distant rumble"
  smell: "sulfur"
  temperature: "hot"
  light_level: 0.3
  danger_level: 0.8
```

---

## Security Assessment

### Concerns

None. Pure organizational structure.

**Risk Level:** ZERO — just inheritance scope

---

## Lineage

| Source | Contribution |
|--------|--------------|
| **OpenLaszlo** | `<node>` element |
| **Self** | Prototype inheritance |
| **CSS** | Cascade |
| **XML** | Namespaces |

---

## Verdict

**INHERITANCE SCOPE. APPROVE.**

Grouping without layout.

Properties cascade to all children.
