# Skill Snitch Report: postgres-optimization

**Date:** 2026-01-28  
**Auditor:** Deep Probe  
**Verdict:** BEYOND THE OBVIOUS

---

## Executive Summary

**Unconventional PostgreSQL performance techniques.**

Beyond standard DBA knowledge: constraint exclusion, function-based indexes, hash exclusion constraints.

---

## Methods

| Method | Purpose |
|--------|---------|
| **ANALYZE-QUERY** | Profile slow query |
| **CHECK-CONSTRAINTS** | Evaluate constraint_exclusion |
| **LOWER-CARDINALITY** | Find function-based index opportunities |
| **HASH-UNIQUE** | Evaluate hash index for large values |
| **VIRTUAL-COLUMN** | Create generated column |
| **COMPARE-INDEXES** | Compare sizes and performance |
| **CHOOSE-INDEX-TYPE** | Recommend index type |
| **EXPLAIN-INDEX-INTERNALS** | Deep understanding |
| **DIAGNOSE-INDEX-USAGE** | Find unused/missing indexes |

---

## Index Types

| Type | Best For | Note |
|------|----------|------|
| **B-Tree** | General purpose, sorting, ranges | Default, only one for PK/unique |
| **Hash** | Equality on large values | 5x smaller than B-Tree |
| **BRIN** | Huge append-only, time series | Tiny but lossy |
| **GIN** | Arrays, JSONB, full-text | Read-heavy |
| **GiST** | Spatial, ranges, full-text | Write-heavy |
| **SP-GiST** | Specialized spatial/tree | Quadtrees, k-d trees |

---

## Unconventional Techniques

| Technique | Problem | Solution |
|-----------|---------|----------|
| **Constraint exclusion** | Full scans with impossible conditions | `SET constraint_exclusion TO 'on'` |
| **Function-based index** | Huge indexes on high-cardinality | Index on lower-cardinality expression |
| **Virtual column** | Expression match required | Generated column guarantees consistency |
| **Hash exclusion** | B-Tree too large for big text | Exclusion constraint with hash |

---

## Decision Tree

```
Equality only + large values → Hash
Ranges/sorting → B-Tree
Huge + append-only + correlated → BRIN
Arrays/JSONB/full-text → GIN (read) or GiST (write)
Geometric/ranges → GiST
Unsure → B-Tree
```

---

## Security Assessment

### Concerns

None. It's database optimization knowledge.

**Risk Level:** ZERO — pure performance

---

## Credits

| Source | Topic |
|--------|-------|
| **Haki Benita** | Unconventional techniques |
| **dlt** | Index internals |
| **Use The Index, Luke** | Definitive guide |

---

## Verdict

**UNCONVENTIONAL OPTIMIZATION. APPROVE.**

Beyond the obvious.

Constraint exclusion. Function-based indexes. Hash exclusion.
