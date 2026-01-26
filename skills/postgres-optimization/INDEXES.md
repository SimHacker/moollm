# PostgreSQL Indexes — Deep Dive

> **"~20 minutes to understand what took PostgreSQL developers decades to build."**

This document captures foundational knowledge about PostgreSQL indexes for developers who have intuitive knowledge of what indexes are, but don't know the internals, tradeoffs, types, and advanced options.

---

## Credits

- **Source**: [Introduction to PostgreSQL Indexes](https://dlt.github.io/) by dlt (2024-09-11)
- **Discussion**: [Hacker News](https://news.ycombinator.com) — 249 points, 13 comments
- **Supplementary**: [Use The Index, Luke](https://use-the-index-luke.com/) — essential reading

---

## The Basics

Indexes are special database objects primarily designed to **increase the speed of data access by reading less data from disk**. They can also enforce constraints (primary keys, unique keys, exclusion).

### Key Rules of Thumb

1. **Indexes don't help unless the query matches** — columns and data types must match
2. **15-20% threshold** — index typically helps only if <15-20% of table will be returned
3. **Query planner decides** — uses statistics and costs, may prefer sequential scan for large result sets

### The Six Index Types

PostgreSQL ships with six index types:

| Type | Best For |
|------|----------|
| **B-Tree** | General purpose, sorting, ranges, equality (default) |
| **Hash** | Equality only, smaller for large values |
| **BRIN** | Huge tables, append-only, time series |
| **GIN** | Arrays, JSON, full-text search |
| **GiST** | Geometric, range types, full-text |
| **SP-GiST** | Non-balanced trees, specialized use cases |

---

## How Data Is Stored on Disk

### The Heap

Every table has one or more files on disk called the **heap**:

- Divided into **8KB pages**
- All rows (internally called "tuples") stored here
- **No specific order** — rows go wherever there's space

### Finding Heap Files

```sql
-- 1. Find data directory
SHOW data_directory;
--  /opt/homebrew/var/postgresql@16

-- 2. Get database OID
SELECT oid, datname FROM pg_database WHERE datname = 'my_database';
--   oid  |   datname
-- -------+------------
--  71122 | my_database

-- 3. Get table filenode
SELECT relfilenode FROM pg_class WHERE relname = 'foo';
--  relfilenode
-- -------------
--        71123

-- 4. Check file on disk
-- ls $PGDATA/base/71122/71123
```

### The ctid — Tuple Identifier

Every row has a `ctid` (current tuple id) — a pointer to its location in the heap:

```sql
SELECT ctid, * FROM foo;
--  ctid  | id |  name
-- -------+----+---------
--  (0,1) |  1 | Ronaldo   -- page 0, offset 1
--  (0,2) |  2 | Romario   -- page 0, offset 2
```

The index is a tree structure that maps **key values → ctid(s)** in the heap.

---

## How Indexes Speed Up Access

### Without Index — Sequential Scan

```sql
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM foo WHERE name = 'Ronaldo';
```

```
Gather  (cost=1000.00..12577.43 rows=1 width=18) (actual time=0.307..264.991 rows=1)
  Workers Planned: 2
  Workers Launched: 2
  Buffers: shared hit=97 read=6272     ← Read 6272 pages from disk!
  ->  Parallel Seq Scan on foo  (cost=0.00..11577.33 rows=1 width=18)
        Filter: (name = 'Ronaldo'::text)
        Rows Removed by Filter: 333333  ← Checked 333K rows per worker
Execution Time: 265.021 ms
```

**Without an index**: PostgreSQL reads ALL tuples in EVERY page and applies a filter.

### With Index — Index Scan

```sql
CREATE INDEX CONCURRENTLY ON foo(name);

EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM foo WHERE name = 'Ronaldo';
```

```
Index Scan using foo_name_idx on foo  (cost=0.42..8.44 rows=1 width=18)
  Index Cond: (name = 'Ronaldo'::text)
  Buffers: shared hit=4               ← Only 4 pages!
Execution Time: 0.077 ms
```

**With an index**: 
- 265ms → 0.077ms (**3,440x faster**)
- 6,369 pages → 4 pages (**1,592x less I/O**)

### Index Size Tradeoff

```sql
\di+
--                                      List of relations
--  Schema |     Name     | Type  | Owner | Table | Access method | Size
-- --------+--------------+-------+-------+-------+---------------+-------
--  public | foo_name_idx | index | dlt   | foo   | btree         | 30 MB
```

The index on 1M rows is 30MB — **same size as the table**. This is a cost.

---

## Costs of Indexes

### 1. Disk Space

Indexes are stored separately from the heap:

- **Not uncommon for B-Tree to be larger than the table**
- More storage costs
- Larger backups
- Increased replication traffic
- Slower backup/recovery

**Mitigation**: Partial indexes, multi-column indexes, space-efficient types (BRIN)

### 2. Write Operations

Every `INSERT`, `UPDATE`, `DELETE` that modifies an indexed column must also update the index:

```
Write to heap + Write to index₁ + Write to index₂ + ...
```

More indexes = more write overhead.

### 3. Query Planner Overhead

The query planner evaluates all possible execution strategies. More indexes = more options to consider = longer planning time.

For ad-hoc queries (not prepared statements), this overhead is paid every time.

### 4. Memory Usage

| Component | Memory Impact |
|-----------|---------------|
| **Shared buffers** | Index pages compete with data pages for cache |
| **Work memory** | Sorting and complex scans need more memory with larger indexes |
| **System catalog** | Index metadata stored in memory |
| **Maintenance** | VACUUM, REINDEX need memory |

**Note**: Larger indexed columns = deeper B-Tree (nodes have limited capacity).

---

## B-Tree Index

The **default** and most common index type. Used for system tables, TOAST, primary keys, unique constraints.

### Properties

- **Balanced tree** — all leaf nodes same distance from root
- **O(log n) search** — only ~20 comparisons for 1M rows
- **Works with disk** — efficient even when larger than RAM
- **Sorted keys** — enables `ORDER BY`, range scans, joins

### Structure

```
                    [Root: M]
                   /         \
          [Inner: G]        [Inner: T]
         /    |    \       /    |    \
    [A-F] [G-L] [M-R]  [S-T] [U-W] [X-Z]
      ↓     ↓     ↓      ↓     ↓     ↓
    heap  heap  heap   heap  heap  heap
```

- **Root/Inner nodes**: Pointers to lower levels
- **Leaf nodes**: Keys + pointers to heap (ctid)
- **Sibling pointers**: Enable forward/backward scanning

### Multiple Indexes with Bitmaps

PostgreSQL can combine multiple indexes using bitmaps:

```sql
SELECT * FROM users WHERE age = 30 AND login_count = 100;
```

If both `age` and `login_count` are indexed:

1. Scan age index → bitmap of pages that might have age=30
2. Scan login_count index → bitmap of pages that might have login_count=100
3. AND the bitmaps together
4. Only read the pages where both conditions might be true

### Multi-Column Indexes

```sql
CREATE INDEX ON my_table(a, b);
```

**Order matters!** The index can serve queries on:
- `WHERE a = ?` ✓
- `WHERE a = ? AND b = ?` ✓
- `WHERE b = ?` ✗ (unless PostgreSQL 18+ skip scan)

**PostgreSQL 18 added index skip scan** — can now use lower-order columns more efficiently. See [Peter Geoghegan's talk](https://youtu.be/RTXeA5svapg?si=_6q3mj1sJL8oLEWC&t=1366).

### Partial Indexes

Index only a subset of rows:

```sql
-- Only index enabled rules (if 90% are disabled)
CREATE INDEX ON rules(status) WHERE status = 'enabled';

-- For skewed distributions (90% TODO, 5% DOING, 5% DONE)
CREATE INDEX ON tasks(status) WHERE status <> 'TODO';
```

**Benefits**:
- Smaller index → fits in RAM
- Shallower → faster lookups
- Less write overhead

### Covering Indexes

If all columns in SELECT are in the index, PostgreSQL can skip the heap:

```sql
CREATE INDEX abc_idx ON bar(a, b);

-- Index-only scan! No heap access needed.
SELECT a, b FROM bar WHERE a = 42;
```

For covering indexes with extra columns that shouldn't break uniqueness:

```sql
CREATE INDEX abc_cov_idx ON bar(a, b) INCLUDE (c);
```

Column `c` is stored only in leaf nodes — more space-efficient than `(a, b, c)`.

### Expression Indexes

Index the result of a function:

```sql
-- Won't use index on name:
SELECT * FROM customers WHERE LOWER(name) = 'john doe';

-- Create expression index:
CREATE INDEX idx_lower_name ON customers (LOWER(name));

-- Now it's used!
```

Works with:
- Built-in functions (`lower()`, `upper()`, `date_trunc()`)
- User-defined **immutable** functions
- Expressions (`first_name || ' ' || last_name`)

---

## Hash Index

Stores 32-bit hash codes instead of actual values.

### When to Use

- **Equality only** (`=`, not `<`, `>`, `BETWEEN`)
- **Large values** (UUIDs, URLs, long strings)
- **Unique or mostly unique data**

### Size Comparison

For a table of URLs:

| Index Type | Size |
|------------|------|
| B-Tree | 154 MB |
| Hash | 32 MB |

**5x smaller** because only hashes are stored, not actual URLs.

### Limitations

- **Equality only** — no range queries
- **No ORDER BY** support
- **No multi-column indexes**
- **No uniqueness checking** (use exclusion constraint as workaround)

### Hash Functions

```sql
-- List hash functions
\df hash*
-- 50+ functions available
```

---

## BRIN Index

**Block Range Index** — stores min/max values per page range.

### When to Use

- **Huge tables** (many GB+)
- **Append-only** or low-update tables
- **Time series data**
- **Strong correlation** between column value and physical location

### How It Works

```
Pages 0-127:   min=2024-01-01, max=2024-01-15
Pages 128-255: min=2024-01-15, max=2024-01-31
Pages 256-383: min=2024-02-01, max=2024-02-15
...
```

Queries eliminate entire page ranges:

```sql
WHERE created_at = '2024-03-15'
-- Skip pages 0-255 entirely!
```

### Limitations

- **Lossy** — points to pages that *might* contain values
- **Bad for updates** — MVCC moves rows, breaks correlation
- **Don't use with pg_repack/pg_squeeze** — they reorganize data

### Tuning

```sql
CREATE INDEX ON events USING BRIN (created_at) 
WITH (pages_per_range = 32);  -- Default is 128
```

Smaller `pages_per_range` = more precise (larger index) but better filtering.

---

## GIN Index

**Generalized Inverted Index** — for searching items within composite data.

### When to Use

- **Arrays** — `@>`, `<@`, `&&` operators
- **JSONB** — `@>`, `?`, `?|`, `?&` operators
- **Full-text search** — `tsvector` columns

### Examples

```sql
-- Array containment
CREATE INDEX ON products USING GIN (tags);
SELECT * FROM products WHERE tags @> ARRAY['electronics', 'sale'];

-- JSONB search
CREATE INDEX ON events USING GIN (data);
SELECT * FROM events WHERE data @> '{"type": "click"}';

-- Full-text search
CREATE INDEX ON articles USING GIN (to_tsvector('english', content));
SELECT * FROM articles WHERE to_tsvector('english', content) @@ 'database & index';
```

### Requirements

- JSONB columns (not JSON)
- Text should be stored as `tsvector` or use `pg_trgm` extension

---

## GiST and SP-GiST

**Generalized Search Tree** and **Space-Partitioned GiST** — frameworks for building custom indexes.

### When to Use

- **Geometric types** (points, boxes, polygons)
- **Range types** (int4range, tsrange)
- **Network types** (inet, cidr)
- **Full-text search** (alternative to GIN)

### GIN vs GiST for Full-Text Search

| Factor | GIN | GiST |
|--------|-----|------|
| Lookup speed | Faster | Slower |
| Index size | Larger | Smaller |
| Build time | Slower | Faster |
| Update cost | Higher | Lower |

**Choose GIN** for read-heavy workloads.
**Choose GiST** for write-heavy workloads or smaller disk footprint.

---

## Quick Reference

### Diagnostic Queries

```sql
-- Check index sizes
\di+ table_*

-- Compare index to table size
SELECT 
    relname AS name,
    pg_size_pretty(pg_relation_size(oid)) AS size
FROM pg_class 
WHERE relname LIKE 'your_table%'
ORDER BY pg_relation_size(oid) DESC;

-- Index usage statistics
SELECT 
    indexrelname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
WHERE schemaname = 'public'
ORDER BY idx_scan DESC;

-- Unused indexes (candidates for removal)
SELECT 
    indexrelname,
    idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
AND indexrelname NOT LIKE '%_pkey';
```

### Index Type Decision Tree

```
What operations?
├── Equality only?
│   ├── Large values (URLs, UUIDs)? → Hash
│   └── Normal values → B-Tree
│
├── Ranges, sorting, ORDER BY? → B-Tree
│
├── Huge table, append-only, time series?
│   └── Strong correlation with physical location? → BRIN
│
├── Searching WITHIN data?
│   ├── Arrays, JSONB, full-text? → GIN (read-heavy) or GiST (write-heavy)
│   └── Geometric, ranges, network types? → GiST
│
└── General purpose, unsure? → B-Tree (default)
```

### Essential Further Reading

1. **[Use The Index, Luke](https://use-the-index-luke.com/)** — The definitive guide to SQL indexing
2. **[PostgreSQL Index Docs](https://www.postgresql.org/docs/current/indexes-intro.html)** — Surprisingly enjoyable to read
3. **[Incremental View Maintenance](https://github.com/sraoss/pg_ivm)** — pg_ivm extension for materialized view auto-updates

---

## Community Insights

From the Hacker News discussion:

### On Index Skip Scan (PostgreSQL 18+)

> "PostgreSQL 18 added support for index skip scan — multi-column indexes can now be used even when queries only filter on lower-order columns." — Peter Geoghegan (PostgreSQL committer)

This changes longstanding wisdom about column ordering in multi-column indexes.

### On Query Plan Caching

PostgreSQL caches prepared statement plans after 5 executions, but it's per-connection. For truly ad-hoc workloads, consider connection poolers that maintain plan caches.

### On BRIN vs Partitioning

BRIN is a good optimization to try *before* partitioning a table. If data is append-only and monotonic, BRIN can achieve similar scan reduction with much less complexity.

---

## Summary Table

| Index Type | O(lookup) | Supports | Size | Best For |
|------------|-----------|----------|------|----------|
| B-Tree | O(log n) | `=`, `<`, `>`, `BETWEEN`, `ORDER BY` | Large | General purpose |
| Hash | O(1)* | `=` only | Small | Large unique values |
| BRIN | O(1)* | `=`, `<`, `>`, `BETWEEN` | Tiny | Huge append-only tables |
| GIN | O(log n) | `@>`, `<@`, `&&`, `?`, `@@` | Large | Arrays, JSONB, full-text |
| GiST | O(log n) | Geometric ops, ranges, full-text | Medium | Spatial, ranges |
| SP-GiST | O(log n) | Specialized | Variable | Quadtrees, k-d trees |

*Amortized, with caveats.
