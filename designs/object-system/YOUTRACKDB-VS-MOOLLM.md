# YouTrackDB vs MOOLLM — two answers to "where does the object model live?"

**Harvest: 2026-07-14.** JetBrains open-sourced [YouTrackDB](https://github.com/JetBrains/youtrackdb)
(Apache 2.0) — an object-oriented graph database, successor to OrientDB. Analysis of the repo, the
[HN thread](https://news.ycombinator.com/item?id=48902026), the
[object-oriented modeling docs](https://github.com/JetBrains/youtrackdb/blob/develop/docs/object-oriented.md),
and Andrii Lomakin's manifesto
[Long road ahead](https://medium.com/@youtrackdb/long-road-ahead-6d648141a190) (Dec 2024) —
compared against MOOLLM's stack: LLM as coherence/execution engine, filesystem + YAML + git/GitHub
as representation/publishing/collaboration/data platform, Self-style prototypes as object model.

Part of the [object-system](README.md) series — see
[SELF-AND-MOOLLM.md](SELF-AND-MOOLLM.md) and
[LATENT-SPACE-INHERITANCE.md](LATENT-SPACE-INHERITANCE.md).
Related: [MEMGPT-ANALYSIS.md](../MEMGPT-ANALYSIS.md) · [GIT-AS-FOUNDATION.md](../GIT-AS-FOUNDATION.md) ·
[GARNET-AMULET-PROTOTYPE-SYSTEM.md](../GARNET-AMULET-PROTOTYPE-SYSTEM.md) ·
[DIRECTORY-AS-IUNKNOWN.md](../DIRECTORY-AS-IUNKNOWN.md) · [MOOAM.md](../MOOAM.md)

---

## What YouTrackDB is

- **OrientDB reborn.** Lomakin: OrientDB was "the passion of all my life"; SAP sunset it; the
  YouTrack team forked it (~2023) and is rebuilding it as YouTrackDB. Runs YouTrack in production.
- **Object-oriented graph DB in Java** (not Kotlin — HN noted the irony; it predates the fork and
  JetBrains doesn't bulk-port). JDK 21+. Embedded as a shaded uber-jar (all deps relocated under
  `com.jetbrains.youtrackdb.shade`) — the "no-deps embedded database" is the killer feature per HN.
- **Class-based schema at the DB level:** `CREATE CLASS Car EXTENDS Vehicle`, multiple inheritance
  (`ElectricCar EXTENDS Car, Electric`), `ABSTRACT`, typed properties, `DEFAULT "uuid()"` +
  `READONLY` for immutable ids. Vertex classes extend `V`, edge classes extend `E`; edges inherit
  too (`Leases EXTENDS Owns`).
- **Polymorphic queries at engine level:** `SELECT FROM Vehicle` returns Cars, Trucks, ElectricCars.
- **O(1) link traversal** (physical record ids — the OrientDB heritage), no runtime JOINs.
- **Snapshot isolation by default**; roadmap to serializable with opt-down to read-committed.
- **Query languages:** YQL (SQL + dot-notation traversal + MATCH), Gremlin/TinkerPop, ISO GQL
  planned.
- **Schema spectrum:** schema-less → schema-mixed → schema-full; runtime `ALTER CLASS` without
  downtime, data preserved.
- **Manifesto thesis:** stop being "everything for everyone" (OrientDB's mistake); deliver one
  coherent entity model — "seamless and transparent mapping of the application object model into
  a database model without hidden performance implications." Merge link-based and vertex/edge
  concepts into a single relation model. Xodus DNQ's developer-friendly API is the UX north star.

## The comparison, axis by axis

### 1. Object model: classes vs prototypes

YouTrackDB is the **Simula/Java tradition**: schema declared up front, inheritance as subsumption
lattice, the engine enforces shape. MOOLLM is the **Self tradition**: no classes — skills are
prototypes you clone and delegate to; a directory is an object, its files are slots; "inheritance"
is reading the level above (GLANCE → CARD → SKILL). Garnet/Amulet lineage
([GARNET-AMULET-PROTOTYPE-SYSTEM.md](../GARNET-AMULET-PROTOTYPE-SYSTEM.md)).

The deep difference is **who resolves polymorphism**:

- YTDB: `SELECT FROM Vehicle` returns declared subclasses — subsumption by declaration, accelerated
  by the engine.
- MOOLLM: "find all the vehicles" returns things that are vehicles **by meaning** — subsumption by
  understanding. Nothing was ever declared a Vehicle. The LLM is the subsumption engine. Call it
  vibe typing: duck typing where the duck test is administered by a reader.

YTDB's multiple inheritance (`ElectricCar EXTENDS Car, Electric`) maps to MOOLLM skill composition
(a character incarnates several skills; frontmatter `related:` mixins). Both reject single-rooted
hierarchies; YTDB checks the diamond at schema time, MOOLLM lets the reader reconcile.

### 2. Coherence engine: WAL vs LLM

YTDB maintains coherence with write-ahead logs, snapshot isolation, a cost-based optimizer
(equi-depth histograms), and schema validation — **deterministic invariant enforcement**. MOOLLM
maintains coherence with reading order (semantic image pyramid), ambient constraint skills, Postel
tolerance, and review — **probabilistic convention enforcement**. YTDB rejects malformed input;
MOOLLM accepts it liberally and emits it conservatively.

Git supplies MOOLLM's transactional substrate ([GIT-AS-FOUNDATION.md](../GIT-AS-FOUNDATION.md)), and
the mapping to YTDB's headline feature is exact:

| YouTrackDB | MOOLLM / git |
|---|---|
| Snapshot isolation | Every commit is a snapshot; readers see a stable tree |
| Transaction | Branch (long-running, optimistic) |
| Commit | Merge |
| Serialization conflict | Merge conflict — resolved by human/LLM, not aborted |
| WAL / recovery | Reflog + remote replicas |
| Audit / security profiling | Blame, signed commits, MOOAM grants ([MOOAM.md](../MOOAM.md)) |
| Observability | Human-readable diffs — the query plan IS the diff |

### 3. Links: O(1) RIDs vs paths with prose

YTDB's O(1) traversal follows physical record ids — fast and semantically bare. MOOLLM's links are
paths and markdown links — O(open-file) and semantically **dressed**: every edge ships with
surrounding prose, comments, provenance. YAML Jazz entropy preservation means the link carries
*why*, not just *to*. YTDB reifies edges as classes with properties (`Leases EXTENDS Owns` with
`since = 2024`); MOOLLM reifies edges as the exit skill — YAML with conditions, descriptions,
verbs. Same instinct (edges are first-class objects), different substrate.

### 4. Query: YQL/GQL vs English + grep + K-lines

YTDB queries in SQL-with-dots and graph MATCH patterns, index-accelerated. MOOLLM queries in
natural language, with grep/glob as the index scan and K-lines as prepared statements — symbolic
activators that pull a whole context up. The MOOLLM adventure verbs (GO/LOOK/TAKE over rooms and
exits) are a traversal DSL in the same family as Gremlin, except the "engine" understands why
you're traversing. The trade: YTDB answers in milliseconds and only answers what was asked; MOOLLM
answers in seconds and notices what you should have asked.

### 5. Schema evolution: ALTER CLASS vs Ninja Edit

Both evolve schema at runtime with data preserved. YTDB: `ALTER CLASS Customer SUPERCLASSES V,
Auditable` — instantly queryable through the new parent. MOOLLM: edit the YAML, fix links, update
the index at top (append-only with Ninja Edit exception). One thing MOOLLM preserves that no
database migration ever has: **the comments survive**. Schema history, rationale, and jokes ride
along in the same file.

### 6. The meta-irony: YouTrackDB's repo is a MOOLLM

The sharpest finding is not in the database — it's in how they build it. The YouTrackDB repo runs a
files-in-git + LLM-agents coherence process:

- `AGENTS.md` split into **per-role guidelines injected by "slate"** (their agent orchestrator)
- `.claude/` config; **@claude is one of the 147 contributors**
- `.pi` extension: "thread-weaving agent architecture", "mandatory user design review gate before
  **adversarial review**" — independently convergent with MOOLLM's adversarial-committee skill
- `workflow-issues/` and `issue-perf-*.md` — issues as markdown files in the repo
- A generated **workflow book** teaching contributors the research → design → plan review →
  track-by-track implementation → review pipeline
- CI that finalizes PR titles and descriptions before ready-for-review

JetBrains is using markdown-in-git with LLM roles and review gates as the coordination database to
build a binary deterministic database. **The repo is the MOOLLM; the artifact is the anti-MOOLLM.**
Two teams starting from opposite ends converged on the same substrate for the meaning-carrying
layer: plain files, git history, agent roles, structured review.

### 7. Lomakin's coherence vs MOOLLM's coherence

The manifesto's core complaint: OrientDB accumulated "the zoo of terms and concepts from different
areas hardly connected." His cure is to **narrow the model** — one coherent entity/relation model,
enforced by the engine, GQL-standard. MOOLLM's cure for the same disease is to **widen the
interpreter** — keep the zoo, make the reader smart enough to walk through it. These are the two
stable strategies for coherence: constrain the writer or empower the reader. Postel says do both,
in that order: accept liberally (reader), emit conservatively (writer). YTDB is all writer-side;
MOOLLM leans reader-side with writer-side conventions.

### 8. The HN thread's memento mori

znpy: "Object databases routinely go away and routinely come back" — cites Versant OODBMS. The
OODB death cycle has a consistent cause: the schema lives in one language runtime's type system,
and when the runtime generation turns over, the database dies with it. Versant died with its era's
C++/Java bindings; OrientDB nearly died with its maintainer economics; YTDB hedges by being
Apache 2.0 + JetBrains-production-critical (YouTrack runs on it).

MOOLLM's wager on the same question: put the schema in **natural language and plain files** — the
only runtime with a 5,000-year uptime and universal bindings. The corpus outlives any engine;
today's LLM is just the current query processor.

saastester's (flagged but fair) ops critique — durability, recovery, observability beat language
choice — reads differently against MOOLLM: git IS the WAL, GitHub IS the replica set, and diffs
ARE the observability. Boring infrastructure as a feature.

### 9. Scale envelopes — where each wins

| | YouTrackDB | MOOLLM |
|---|---|---|
| Records | Millions+, concurrent writers | Hundreds–thousands of meaning-dense entities |
| Traversal | Sub-ms, O(1) | Seconds, O(context) |
| Integrity | Enforced invariants, ACID | Reviewed conventions, git history |
| Query | Asked questions, fast | Unasked questions too, slow |
| Collaboration | Client protocol, roles | PRs, blame, forks — collaboration IS the platform |
| Schema origin | Declared by developers | Emergent from corpus + conventions |
| Failure mode | Aborted transaction | Confused reader (robust-first: degrade, log, continue) |

Complementary, not competing. The obvious hybrid: derive a graph index (YTDB-shaped or otherwise)
from a MOOLLM corpus as a **materialized view** — grep is fine until it isn't, and an O(1) link
index over `ties:` / exits / K-line references is a cache, not a source of truth. The inverse
hybrid already exists: YTDB's own development needed a MOOLLM-shaped layer the moment agents
joined the team.

## One-line summary

YouTrackDB moves the object model **down** into the storage engine so the application can forget
about mapping; MOOLLM moves the object model **up** into language so the engine can be anything.
Both are reactions to the same pain — the impedance mismatch between how people think and where
data lives — and JetBrains' own agent workflow is quiet evidence that for the meaning-heavy layer,
they picked MOOLLM's answer too.
