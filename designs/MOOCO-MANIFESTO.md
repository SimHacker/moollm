# MOOCO Manifesto

> *MOOLLM defines the microworld. MOOCO runs it.*

**Status:** Public design vision (May 2026)  
**Companion:** [MOOLLM-MANIFESTO.md](MOOLLM-MANIFESTO.md) — filesystem as world, skills as programs  
**Implementation:** A private orchestrator prototype exists as **sketch and living tissue** — not a product announcement. This document is the guiding spec for what that runtime is trying to become.

---

## The gap MOOCO fills

[MOOLLM-MANIFESTO.md](MOOLLM-MANIFESTO.md) says: directories are rooms, files are objects, skills are programs, the LLM is `eval()`. That is **content** and **ontology** — 129+ skills in git, CARD.yml, SKILL.md, k-lines, YAML Jazz.

Git and Cursor can **read** that. They do not **run** it as a MOO:

- Which skills are **hot** for this turn?
- Which repo mount supplies `skills/character` vs a partial subtree?
- Who may **invoke** a sister script — the model, or only `skill_manager`?
- What did the session **actually load**, auditably?
- How do **shadow layers** (`.moollm/`) overlay upstream without forking the repo?

**MOOCO** (MOO Custom Orchestrator / Coordinator) is the **protocol endpoint** that answers those questions. Not a chatbot skin. A **server** the LLM **browses**.

---

## One sentence each

| Term | Role |
|------|------|
| **MOO** | Microworld Object Ontology — objects, verbs, rooms (LambdaMOO lineage, Papert microworlds) |
| **MOOLLM** | The moocroworld in files: skills, characters, designs, schemas |
| **MOOCO** | Orchestrator: mount namespace, activate k-lines, invoke skills safely, stream sessions, persist traces |
| **MOOFS** | Overlay file system — git layers, shadows, mounts ([MOOFS-DESIGN.md](MOOFS-DESIGN.md)) |
| **MOOT** | (Design) Git tree reification — `moot mount`, `moot sync`, URL → path — MOOCO orchestrates, MOOT reifies |

---

## MOOCO is not a chatbot

MOOCO is a **protocol endpoint**.

```text
LLM          ≈  browser (tabs, GET, partial fetch, sessions)
Orchestrator ≈  server   (resources, tools, policy, sandboxes)
```

The LLM requests:

```yaml
GET moollm://skills/character
GET moollm://rooms/control-room
GET moollm://docs/MOOCO-MANIFESTO
HEAD skill/cursor-mirror    # card only, not full SKILL.md
```

The orchestrator returns **representations** — markdown, YAML, summaries, embeddings, generated views. Full protocol essay: [MOOCO-MOO-CUSTOM-ORCHESTRATOR.md](MOOCO-MOO-CUSTOM-ORCHESTRATOR.md).

**Natural language in skills is executable content** — downloaded “program” the model runs. JSON is generated when needed, not assumed first ([orchestrator doc → Reversing JSON](MOOCO-MOO-CUSTOM-ORCHESTRATOR.md)).

**Symmetric cognition:** orchestrator provides resources and sandboxes; LLM provides interpretation — peers, not master/slave.

---

## Skills: manage, audit, secure, optimize

Plain `bash` can touch anything. MOOCO’s **`skill_manager`** tool cannot.

It only runs what skills **declare**:

| Callable | Declared in | Role |
|----------|-------------|------|
| **command** | CARD.yml | Chat-facing, natural language parameters |
| **method** | SKILL.md | Specialized procedures (CLOS-style dispatch) |
| **advertisement** | CARD.yml | Generic verb → best matching method |
| **script** | `scripts/` | Sister shell scripts, bounded execution |

Operations (design): **list**, **install**, **import** (foreign skill shapes → MOOLLM), **invoke**, **heat** (k-line introspection).

**Audit:** sessions persist tool calls with mandatory **`why`** on every invocation — trace what loaded, what fired, what ran. Play–learn–lift on the trace; skill-snitch-style “body and spirit” review over stored protocol, not mystery prompts.

**Optimize:** do not dump 129 SKILL.md files into context. **K-line activation** (below) promotes a **hot set** per turn.

**Secure:** sandboxed callables, skill_manager vs raw shell, git worktrees and containers for generated code — neither side fully trusted, both useful ([orchestrator → Sandboxed Reality](MOOCO-MOO-CUSTOM-ORCHESTRATOR.md)).

---

## Namespace: MOOFS, mounts, git trees

Skills live in git; runtime needs a **composed namespace**.

[MOOFS-DESIGN.md](MOOFS-DESIGN.md) — resolution stack (top wins):

```text
AMBIENT SKILLS     (global overlays: no-ai-slop, etc.)
ROOM MOUNTS        (while ENTER room)
CHARACTER MOUNTS   (GRANT / AFFLICT on a card)
LOCAL SHADOW       (.moollm/ — gitignored experiments)
WORKING BRANCH
UPSTREAM
BASE REPO          (published skills/*)
```

**GRANT** = additive overlay. **AFFLICT** = suppressive overlay. Same skill file, two read directions.

**Multi-repo workspace (design):** full clones and **partial subtrees** — mount only `MicropolisCore/documentation/designs`, only `moollm/skills/micropolis`, etc. Logical URLs (`moollm://…`) bind to resolved paths after mount stack — stable addresses for the LLM-browser.

**Play → Learn → Lift:** experiment in `.moollm/` shadow → stage to branch → PR upstream. MOOCO orchestrates workflow; MOOFS defines layer semantics.

---

## K-lines: hot list, cache, resolution

Skills declare **k-lines** — vocabulary that activates conceptual clusters (indexes are k-lines: “procedural rhetoric” fires the right doc set).

**CG (Context Gatherer / Treasure Collector)** — lexical mirror of GC:

| GC | CG |
|----|-----|
| find dead → remove | find **hot** → **promote** into attention |
| free memory | fill context with relevant skills |

Components: **Detector** (what’s hot), **Diffuser** (spread along edges), **Hoarder** (`K-CACHE.yml`), **Treasure Map** (the graph).

**skill_manager `heat`:** show, trace, warm, cool edges — optimize what loads without brute-force grep every turn. **grepnet** (design): live index of k-line references across the moocroworld, updated on save.

Persistence (prototype direction): PostgreSQL + **pgvector** for embeddings and activation history; **mooco-mirror** queries sessions, tools, k-lines, rooms — introspect what the orchestrator actually did.

---

## Tools beyond skills

Shared package layer (design): `@moollm/stream-machine`, `sse-protocol`, `provider-base`, `tool-executor`, `tools-core`, `svelte-chat`, `cursor-mirror`, `mooco-mirror` — see [MOOCO-PACKAGES.md](MOOCO-PACKAGES.md).

| Tool class | Examples |
|------------|----------|
| **Core** | bash, python, fs-read/write, http, sql — each with `why` |
| **MOOLLM-native** | room ENTER/LEAVE, skill invoke, k-line HEAT/COOL |
| **Mirrors** | cursor-mirror (read IDE SQLite), mooco-mirror (read orchestrator DB) |
| **Namespace** | subtree move/copy, grepnet k-line query (design) |

Generalized verbs (not only HTTP): `INVOKE`, `ACTIVATE`, `ENTER`, `LEAVE`, `HEAT`, `COOL`, `FOCUS`, `DEFOCUS`, `REFLECT`.

---

## Relationship to Micropolis, Federation, outreach

MOOCO does not replace [MicropolisCore](https://github.com/SimHacker/MicropolisCore) or [moollm](https://github.com/SimHacker/moollm) design docs. It is how an agent **mounts** those repos, **heats** the right skills for “Stardew Bifrost” or “Sunny Street outreach,” **invokes** `sims-io` sisters safely, and **traces** what it read.

Federation character bridges are **file-format** work; MOOCO is **session and namespace** work — complementary layers.

---

## Implementation posture (honest)

- **This repo (`moollm/designs/`)** — public specs, manifestos, skill corpus.  
- **Orchestrator prototype** — private, incomplete, exercised daily as **living tissue**. Shapes packages and protocols here; may diverge and be rewritten.  
- **No release promises** — no dates, no “coming soon” product. Readers should treat MOOCO as **architecture you can implement yourself** from these docs + shared `@moollm/*` package sketches.  
- **Open packages** — MIT-leaning shared libraries are designed to be reusable; the full app shell is not committed to open source in this document.

If you only read one other MOOCO doc: [MOOCO-MOO-CUSTOM-ORCHESTRATOR.md](MOOCO-MOO-CUSTOM-ORCHESTRATOR.md) (browser/server protocol). If you read two: add [MOOFS-DESIGN.md](MOOFS-DESIGN.md) (layers and mounts).

---

## Document map

| Document | What |
|----------|------|
| [MOOCO-MANIFESTO.md](MOOCO-MANIFESTO.md) | **This file** — runtime vision |
| [MOOCO-MOO-CUSTOM-ORCHESTRATOR.md](MOOCO-MOO-CUSTOM-ORCHESTRATOR.md) | Protocol: LLM-as-browser, partial GET, symmetric cognition |
| [MOOFS-DESIGN.md](MOOFS-DESIGN.md) | Overlay FS, mounts, play–learn–lift |
| [MOOCO-PACKAGES.md](MOOCO-PACKAGES.md) | `@moollm/*` package graph, mirrors, DB sketch |
| [MOOLLM-MANIFESTO.md](MOOLLM-MANIFESTO.md) | Content-layer microworld vision |
| [FACTORIO-MOOLLM-DESIGN.md](FACTORIO-MOOLLM-DESIGN.md) | Factory metaphor for mooco dataflows |

---

## Closing

The web connected **documents**.

MOOCO connects **cognition** to **worlds** already written in git — skills, rooms, characters, designs — with inspectable mounts, activations, and traces.

MOOLLM is the moocroworld you can fork.

MOOCO is the MOO server that makes forking **runnable**.
