# PostgreSQL Optimization

> **From index fundamentals to unconventional techniques.**

This skill provides comprehensive PostgreSQL index and optimization knowledge:

## Files

| File | Contents |
|------|----------|
| **INDEXES.md** | Deep dive on index internals, types, costs, decision trees |
| **SKILL.md** | Unconventional optimization techniques |
| **CARD.yml** | Sniffable interface, methods, advertisements |
| **README.md** | This overview |

---

## INDEXES.md — Index Fundamentals

Captures foundational knowledge from [dlt's article](https://dlt.github.io/) (249 points on HN):

| Index Type | Best For | Key Insight |
|------------|----------|-------------|
| **B-Tree** | General purpose, sorting, ranges | Default, only type for PK/unique |
| **Hash** | Equality on large values | 5x smaller than B-Tree for URLs |
| **BRIN** | Huge append-only tables | Tiny (stores ranges, not values) |
| **GIN** | Arrays, JSONB, full-text | Fast lookups, high write cost |
| **GiST** | Spatial, ranges, full-text | Balanced read/write tradeoff |

**Essential reading**: [Use The Index, Luke](https://use-the-index-luke.com/)

---

## SKILL.md — Unconventional Techniques

From [Haki Benita's article](https://hakibenita.com/postgresql-unconventional-optimizations):

Three techniques are covered:

| Technique | Problem | Solution |
|-----------|---------|----------|
| Constraint Exclusion | Full scans on impossible queries | `SET constraint_exclusion TO 'on'` |
| Function-Based Indexes | Oversized indexes on high-cardinality columns | Index lower-cardinality expression |
| Hash Index Uniqueness | Giant B-Tree on large text values | Exclusion constraint with hash index |

## Key Insights

### 1. Check Constraints Are Optimization Hints (If You Ask)

PostgreSQL has check constraints that guarantee certain values can never exist. But by default, queries that ask for those impossible values still scan the table!

```sql
-- Table has CHECK (plan IN ('free', 'pro'))
SELECT * FROM users WHERE plan = 'Pro';  -- Scans 100K rows for 0 results
```

The fix is a session/connection setting:

```sql
SET constraint_exclusion TO 'on';
-- Now PostgreSQL recognizes the condition is always false
```

**Use case**: BI environments, ad-hoc query tools, reporting databases where users make typos.

### 2. Index What You Query, Not What You Store

If you store timestamps but query by day/month/year, you're paying for index precision you don't use.

```sql
-- Stores 10M distinct timestamps
-- But queries only need ~365 distinct dates per year
CREATE INDEX sale_sold_at_date_ix 
ON sale((date_trunc('day', sold_at AT TIME ZONE 'UTC'))::date);
```

Result: 66 MB index instead of 214 MB — 3x smaller.

The catch: expressions must match exactly. PostgreSQL 18's virtual generated columns solve this.

### 3. Hash Indexes Store Hashes, Not Values

B-Tree indexes store actual values in leaf blocks. For large text values (URLs, document paths), this creates huge indexes.

Hash indexes store only the hash — much smaller. PostgreSQL doesn't support `CREATE UNIQUE INDEX ... USING HASH`, but exclusion constraints achieve the same effect:

```sql
ALTER TABLE urls 
ADD CONSTRAINT urls_url_unique_hash 
EXCLUDE USING HASH (url WITH =);
```

Result: 32 MB index instead of 154 MB — 5x smaller, and faster queries.

## Community Discussion Highlights

From the Hacker News discussion:

### On Write Amplification

> "If you're dealing with <ridiculous number of users>, there is a good chance that you don't want to be putting BI/OLAP indices on your OLTP database."

The tradeoff: every index adds write overhead. Smaller indexes help, but sometimes the answer is a read replica with its own indexes.

### On Plan Caching

> "PG's lack of plan caching strikes again, this sort of thing is not a concern in other DB's that reuse query plans."

PostgreSQL does cache prepared statement plans (after 5 executions), but it's per-connection. The `constraint_exclusion` overhead matters for ad-hoc queries that aren't prepared.

### On BRIN Indexes (Not in Article)

For monotonic data (e.g., timestamps arriving in order), BRIN indexes are extremely small and fast. Worth considering alongside function-based indexes.

### On MERGE vs ON CONFLICT

MERGE (added in PostgreSQL 15) is more powerful than `INSERT ... ON CONFLICT` but has MVCC edge cases. For concurrent OLTP workloads, stick with `ON CONFLICT`. MERGE is better for manual fixups and batch operations.

## Files

| File | Purpose |
|------|---------|
| `CARD.yml` | Sniffable interface for activation |
| `SKILL.md` | Protocol and detailed techniques |
| `README.md` | This file — deep context |

---

## Index Type Quick Reference

```
What operations?
├── Equality only?
│   ├── Large values (URLs, UUIDs)? → Hash
│   └── Normal values → B-Tree
│
├── Ranges, sorting, ORDER BY? → B-Tree
│
├── Huge table, append-only?
│   └── Value correlates with physical location? → BRIN
│
├── Searching WITHIN data?
│   ├── Arrays, JSONB? → GIN
│   └── Full-text? → GIN (read-heavy) or GiST (write-heavy)
│
├── Geometric/spatial? → GiST
│
└── Unsure? → B-Tree (default)
```

---

## PostgreSQL 18 Changes

**Index Skip Scan** — Multi-column indexes can now be used even when queries only filter on lower-order columns. This changes longstanding wisdom about column ordering.

**Virtual Generated Columns** — Function-based indexes no longer require discipline. Create a virtual column that guarantees the correct expression.

---

## See Also

- [PostgreSQL EXPLAIN documentation](https://www.postgresql.org/docs/current/sql-explain.html)
- [PostgreSQL Index Introduction](https://www.postgresql.org/docs/current/indexes-intro.html) — surprisingly enjoyable
- [Use The Index, Luke](https://use-the-index-luke.com/) — essential reading
- [Hash Index Re-Introduction](https://hakibenita.com/postgresql-hash-index) — earlier article on hash indexes
- [12 Common SQL Mistakes](https://hakibenita.com/sql-dos-and-donts) — related patterns

## Credits

- **Unconventional Techniques**: "Unconventional PostgreSQL Optimizations" by Haki Benita (2026-01-20)
- **Index Fundamentals**: "Introduction to PostgreSQL Indexes" by dlt (2024-09-11)
- **Essential Reference**: [Use The Index, Luke](https://use-the-index-luke.com/) by Markus Winand
