# MOOPMAP: Semantic Mipmap for LLM Context Management

> *"Grep invented in 1973 outperforms trillion-parameter embedding models when paired with an intelligent navigator."*
> — Nicolas Bustamante, "The RAG Obituary" (2026)

---

## What Is MOOPMAP?

**MOOPMAP** (MOO + mipmap) is MOOLLM's answer to the RAG problem: a pre-computed semantic compression pyramid that enables fast context loading without chunking, embedding, or vector search.

Like image mipmaps in computer graphics (pre-computed scaled versions for efficient rendering), moopmap provides pre-computed semantic resolutions for efficient LLM context assembly.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    SEMANTIC MIPMAP PYRAMID                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  RESOLUTION 0 — GLANCE.yml                                          │
│  ┌─────────────────────────────────────────────────────┐            │
│  │  Quick summary: what, why, when                     │  ~1.4 KB   │
│  │  Load first. Decide if more context needed.         │            │
│  └─────────────────────────────────────────────────────┘            │
│                            │                                        │
│                            ↓ need interface?                        │
│  RESOLUTION 1 — CARD.yml                                            │
│  ┌─────────────────────────────────────────────────────┐            │
│  │  Methods, capabilities, activation triggers         │  ~6.9 KB   │
│  │  Machine-readable. K-line references.               │            │
│  └─────────────────────────────────────────────────────┘            │
│                            │                                        │
│                            ↓ need full protocol?                    │
│  RESOLUTION 2 — SKILL.md                                            │
│  ┌─────────────────────────────────────────────────────┐            │
│  │  Complete specification. All methods detailed.      │  ~10 KB    │
│  │  Anthropic SKILL.md standard format.                │            │
│  └─────────────────────────────────────────────────────┘            │
│                            │                                        │
│                            ↓ need philosophy/examples?              │
│  RESOLUTION 3 — README.md                                           │
│  ┌─────────────────────────────────────────────────────┐            │
│  │  Deep context. Motivations. History. Examples.      │  ~3.7 KB   │
│  │  Human-readable narrative. Links everywhere.        │            │
│  └─────────────────────────────────────────────────────┘            │
│                            │                                        │
│                            ↓ need everything?                       │
│  RESOLUTION 4 — Directory Contents                                  │
│  ┌─────────────────────────────────────────────────────┐            │
│  │  scripts/, templates/, examples/, artifacts/        │  ~32 KB    │
│  │  The full implementation. Rarely need all of it.    │            │
│  └─────────────────────────────────────────────────────┘            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Why Not RAG?

The [RAG Obituary](https://x.com/nicbstme/status/2016251900249964865) (Bustamante, Jan 2026) articulates what MOOLLM discovered independently:

### The RAG Cascading Failure Problem

```
Chunking → Embedding → BM25 → Fusion → Reranking → LLM
   5%         5%         5%       5%        5%       5%
                            ↓
              Compound Error: ~23%
```

Each stage adds latency, cost, and error. And if chunking destroys a table or cross-reference, no amount of reranking fixes it.

### MOOPMAP's Single-Stage Alternative

```
Load GLANCE → (optionally) Load more resolutions → LLM
     1 step              1 step                    done
```

No chunking. No embeddings. No similarity scores. Just **pre-authored semantic summaries** at known file paths.

---

## Current Stats (2026-01-28)

From `designs/glance-mipmap-analysis.yml`:

| Metric | Value |
|--------|-------|
| Total text files | 3,015 |
| Total text size | 21.9 MB |
| Total GLANCE files | 284 |
| Total GLANCE size | 274 KB |
| **Compression ratio** | **1.23%** |

### By Category

| Category | Count | Avg GLANCE | Avg Direct Text | Ratio |
|----------|-------|------------|-----------------|-------|
| Skills | 118 | 1,394 bytes | 32,406 bytes | 23:1 |
| Rooms | 111 | 633 bytes | 34,078 bytes | 54:1 |
| Characters | 53 | 830 bytes | 30,700 bytes | 37:1 |

### Skill Pyramid (Average Bytes)

```
GLANCE.yml:     1,394 bytes  ████
CARD.yml:       6,871 bytes  ████████████████████
SKILL.md:      10,033 bytes  ██████████████████████████████
README.md:      3,745 bytes  ███████████
Direct text:   32,406 bytes  ████████████████████████████████████████████████████████████████████████████████████████████████
```

**Key insight:** GLANCE provides ~23:1 compression while preserving semantic coverage.

---

## Tool: moopmap.py

Location: `skills/moollm/scripts/moopmap.py`

### Usage

```bash
# From moollm repo root
python3 skills/moollm/scripts/moopmap.py

# Custom output
python3 skills/moollm/scripts/moopmap.py --output my-analysis.yml

# Specific repo
python3 skills/moollm/scripts/moopmap.py /path/to/moollm
```

### Output

Generates `designs/glance-mipmap-analysis.yml` with:

- **repo_summary**: Total files, bytes, compression ratio
- **by_category**: Stats for skills, rooms, characters
- **skill_pyramid**: Average bytes at each resolution level
- **top_10_widest_dirs**: Largest branching factor directories
- **top_10_skills_by_content**: Skills with most direct text

### Methodology

- **Width**: Top-level files + dirs (branching factor, not recursive)
- **Direct text**: Bytes of `.md/.yml/.yaml/.txt` files in directory only
- **No recursive du**: Avoids double-counting nested content
- **Categories**: Inferred from path (`/skills/` → skill, `/characters/` → character, etc.)

---

## Relationship to Other Designs

### MEMGPT-ANALYSIS.md

MemGPT manages memory by **paging** data in/out of context windows.

MOOPMAP provides the **static hierarchy** that makes paging efficient:
- GLANCE = what to prefetch
- CARD = interface for function calls
- SKILL.md = full spec when needed
- README = deep dive

**Connection:** MemGPT's `archival_storage` benefits from pre-summarized GLANCE files.

### moollm-medium-post.md

The Medium article uses moopmap stats to prove the semantic mipmap works:

> "274 KB of GLANCEs summarize 21.9 MB of content — 1.23% the size, but semantically complete."

### MOOLLM-PROTOCOLS.md

K-lines and semantic activation work **because** of the mipmap:
- K-line name → activates GLANCE → decides if more resolution needed
- No vector similarity required — names are semantic addresses

### GIT-AS-FOUNDATION.md

The mipmap is version-controlled:
- GLANCE files are first-class citizens
- Changes to content should update GLANCE
- Git diff shows semantic changes, not just token changes

---

## The RAG Obituary Connection

Bustamante's article validates MOOLLM's approach:

| RAG Problem | MOOPMAP Solution |
|-------------|------------------|
| Chunking destroys relationships | Directories as semantic units |
| Embeddings fail on jargon | K-lines activate by name |
| Reranking adds latency | Pre-authored relevance |
| Index maintenance burden | Files are instantly searchable |
| 5-stage cascading errors | Single-stage file load |

**Key quote from the article:**

> "Claude Code doesn't retrieve. It investigates: runs multiple searches in parallel, starts broad, then narrows based on discoveries, follows references naturally. No embeddings, no similarity scores, no reranking."

MOOLLM does the same — but with **pre-computed summaries** to make investigation faster.

---

## When You Still Need Vector Search

MOOPMAP is primary. Vector search (pgvector) is fallback:

| Use Case | Primary | Fallback |
|----------|---------|----------|
| "Load skill X" | GLANCE → CARD → SKILL.md | — |
| "Find skills like X" | K-line activation | pgvector similarity |
| "What did Y say 3 months ago?" | Session logs + grep | pgvector temporal search |
| "Rooms with this vibe" | — | pgvector embedding search |

**Philosophy:** Use vector search as a tool among tools, not the primary retrieval mechanism.

---

## Creating GLANCEs

### Structure

```yaml
# GLANCE.yml — MUST be at directory root
name: skill-name
type: skill | room | character | slideshow | session
emoji: 📦

what: One-line description of what this is
why: Why it exists, what problem it solves  
when: When to use it

# Category-specific fields
methods:        # for skills
contents:       # for rooms
personality:    # for characters
highlights:     # for slideshows

related:
  - other-thing-1
  - other-thing-2

lineage: Minsky → Papert → MOOLLM
```

### Guidelines

1. **Fit in ~50 lines** — If longer, you're including too much detail
2. **Pure data** — Comments are YAML Jazz, not filler
3. **Action-oriented** — Tell LLM what to DO with this
4. **Links optional** — K-line names are sufficient
5. **Update on change** — GLANCE should reflect current content

---

## Measuring Success

Run moopmap after significant changes:

```bash
# Before
python3 skills/moollm/scripts/moopmap.py
# Make changes
# After
python3 skills/moollm/scripts/moopmap.py
```

Watch for:
- **Compression ratio** staying ~1-2% (higher = GLANCEs too verbose)
- **Skill pyramid** ratios staying consistent
- **New directories** getting GLANCE files

---

## Future Work

1. **Auto-GLANCE generation** — LLM generates GLANCE from directory contents
2. **GLANCE linting** — Ensure all GLANCEs follow structure
3. **Compression tracking** — Historical compression ratio trends
4. **Cross-repo moopmap** — Analyze multiple MOOLLM instances

---

## References

- **Internal:**
  - `designs/glance-mipmap-analysis.yml` — Current stats
  - `designs/MEMGPT-ANALYSIS.md` — Memory management context
  - `designs/moollm-medium-post.md` — Public explanation
  - `skills/moollm/scripts/moopmap.py` — The analyzer tool

- **External:**
  - [The RAG Obituary](https://x.com/nicbstme/status/2016251900249964865) — Bustamante, Jan 2026
  - [MemGPT: LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — Packer et al., 2023
  - [Mipmapping](https://en.wikipedia.org/wiki/Mipmap) — Williams, 1983

---

*"RAG was a clever workaround for a context-poor era. MOOPMAP is designed for context-rich LLMs from the start."*
