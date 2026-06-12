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

## The MOO namespace — one canonical table

This is the **single source** for what each name means and its status. Other docs link here instead of redefining.


| Term            | Status           | Role                                                                                                                                                                               |
| --------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MOO**         | concept          | Microworld Object Ontology — objects, verbs, rooms (LambdaMOO lineage, Papert microworlds)                                                                                         |
| **MOOLLM**      | shipped          | The moocroworld in files: skills, characters, designs, schemas                                                                                                                     |
| **moo**         | **shipped**      | Moo VM CLI in `skills/moo/`; moorls (`moo://`, `moollm://`), `read`/`sniff`/`focus` = the LLM browser engine ([MOOCO-MOO-VM.md](MOOCO-MOO-VM.md))                                  |
| **moocroworld** | shipped          | Branches-as-objects model, `REPOS.yml`, attention trees; canonical `ClassName_ObjectID` naming ([skills/moocroworld/](../skills/moocroworld/SKILL.md))                             |
| **moopmap**     | shipped (script) | Semantic mipmap — local GLANCE→CARD→SKILL→README compression analysis ([MOOPMAP.md](MOOPMAP.md))                                                                                   |
| **MOOCO**       | prototype        | Orchestrator: mount namespace, activate k-lines, invoke skills safely, stream sessions, persist traces                                                                             |
| **MOOFS**       | design           | Overlay file system — git layers, shadows, GRANT/AFFLICT mounts ([MOOFS-DESIGN.md](MOOFS-DESIGN.md))                                                                               |
| **fragments**   | proposed         | Self-ish session/workspace config — `parents` merge, materialize scripts ([PROTOTYPE-FRAGMENT-CONFIG.md](PROTOTYPE-FRAGMENT-CONFIG.md))                                            |
| **MOOMC**       | future           | Meta compiler — distill fragments/skills into git-addressable artifacts (branch `ClassName_ObjectID`, tag, or repo) ([PROTOTYPE-FRAGMENT-CONFIG.md](PROTOTYPE-FRAGMENT-CONFIG.md)) |
| **MOOT**        | future           | Local git tree reifier — symlinks/worktrees on disk; complements moo's remote gh-backed VM ([mooco MOOKIE sketch](../../mooco/designs/MOOKIE.md))                                  |


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

Plain `bash` can touch anything. MOOCO’s `**skill_manager`** tool cannot.

It only runs what skills **declare**:


| Callable          | Declared in | Role                                         |
| ----------------- | ----------- | -------------------------------------------- |
| **command**       | CARD.yml    | Chat-facing, natural language parameters     |
| **method**        | SKILL.md    | Specialized procedures (CLOS-style dispatch) |
| **advertisement** | CARD.yml    | Generic verb → best matching method          |
| **script**        | `scripts/`  | Sister shell scripts, bounded execution      |


Operations (design): **list**, **install**, **import** (foreign skill shapes → MOOLLM), **invoke**, **heat** (k-line introspection).

**Audit:** sessions persist tool calls with mandatory `**why`** on every invocation — trace what loaded, what fired, what ran. Play–learn–lift on the trace; skill-snitch-style “body and spirit” review over stored protocol, not mystery prompts.

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


| GC                 | CG                                        |
| ------------------ | ----------------------------------------- |
| find dead → remove | find **hot** → **promote** into attention |
| free memory        | fill context with relevant skills         |


Components: **Detector** (what’s hot), **Diffuser** (spread along edges), **Hoarder** (`K-CACHE.yml`), **Treasure Map** (the graph).

**skill_manager `heat`:** show, trace, warm, cool edges — optimize what loads without brute-force grep every turn. **grepnet** (design): live index of k-line references across the moocroworld, updated on save.

Persistence (prototype direction): PostgreSQL + **pgvector** for embeddings and activation history; **mooco-mirror** queries sessions, tools, k-lines, rooms — introspect what the orchestrator actually did.

---

## Tools beyond skills

Shared package layer (design): `@moollm/stream-machine`, `sse-protocol`, `provider-base`, `tool-executor`, `tools-core`, `svelte-chat`, `cursor-mirror`, `mooco-mirror` — see [MOOCO-PACKAGES.md](MOOCO-PACKAGES.md).


| Tool class        | Examples                                                             |
| ----------------- | -------------------------------------------------------------------- |
| **Core**          | bash, python, fs-read/write, http, sql — each with `why`             |
| **MOOLLM-native** | room ENTER/LEAVE, skill invoke, k-line HEAT/COOL                     |
| **Mirrors**       | cursor-mirror (read IDE SQLite), mooco-mirror (read orchestrator DB) |
| **Namespace**     | subtree move/copy, grepnet k-line query (design)                     |


Generalized verbs (not only HTTP): `INVOKE`, `ACTIVATE`, `ENTER`, `LEAVE`, `HEAT`, `COOL`, `FOCUS`, `DEFOCUS`, `REFLECT`.

---

## Relationship to Micropolis, Federation, outreach

MOOCO does not replace [MicropolisCore](https://github.com/SimHacker/MicropolisCore) or [moollm](https://github.com/SimHacker/moollm) design docs. It is how an agent **mounts** those repos, **heats** the right skills for “Stardew Bifrost” or “Sunny Street outreach,” **invokes** `sims-io` sisters safely, and **traces** what it read.

Federation character bridges are **file-format** work; MOOCO is **session and namespace** work — complementary layers.

---

## Implementation posture (honest)

- **This repo (`moollm/designs/`)** — public specs, manifestos, skill corpus.  
- **Orchestrator prototype** — private, incomplete, exercised daily as **living tissue**. Shapes packages and protocols here; may diverge and be rewritten.  
- **No release promises** — no dates, no “coming soon” product. Readers should treat MOOCO as **architecture you can implement yourself** from these docs + shared `@moollm/`* package sketches.  
- **Open packages** — MIT-leaning shared libraries are designed to be reusable; the full app shell is not committed to open source in this document.

**Compose** a session shape → [PROTOTYPE-FRAGMENT-CONFIG.md](PROTOTYPE-FRAGMENT-CONFIG.md). **Run** it → [MOOCO-MOO-VM.md](MOOCO-MOO-VM.md) (moo + hosted worlds). **Wire format** → [MOOCO-MOO-CUSTOM-ORCHESTRATOR.md](MOOCO-MOO-CUSTOM-ORCHESTRATOR.md). **Local shadows** → [MOOFS-DESIGN.md](MOOFS-DESIGN.md).

---

## Document map — what to read when


| Document                                                             | Scope                                                              | Read when                           |
| -------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------- |
| [MOOCO-MANIFESTO.md](MOOCO-MANIFESTO.md)                             | **This file** — runtime vision, namespace one-liners               | Start here                          |
| [PROTOTYPE-FRAGMENT-CONFIG.md](PROTOTYPE-FRAGMENT-CONFIG.md)         | **Compose-time** — `parents` merge, resolver, MOOMC → git emission | Building session/workspace *shapes* |
| [MOOCO-MOO-VM.md](MOOCO-MOO-VM.md)                                   | **Runtime** — moo fetch, hosted worlds, workers, branch sync       | Running or publishing orchestrators |
| [MOOCO-MOO-CUSTOM-ORCHESTRATOR.md](MOOCO-MOO-CUSTOM-ORCHESTRATOR.md) | **Protocol** — LLM-as-browser, GET/INVOKE, symmetric cognition     | Implementing the wire format        |
| [MOOFS-DESIGN.md](MOOFS-DESIGN.md)                                   | Local overlay layers, play–learn–lift                              | Shadow mounts and contribution      |
| [MOOCO-PACKAGES.md](MOOCO-PACKAGES.md)                               | `@moollm/`* packages, mirrors, DB sketch                           | Implementation layout               |


**DRY rule:** fragments describe *what to merge before run*; MOOCO docs describe *what happens while running*. Branch naming (`ClassName_ObjectID`) is canonical in [skills/moocroworld/](../skills/moocroworld/SKILL.md) — cited, not re-explained.


| Also                                                   |                                      |
| ------------------------------------------------------ | ------------------------------------ |
| [MOOLLM-MANIFESTO.md](MOOLLM-MANIFESTO.md)             | Content-layer microworld vision      |
| [FACTORIO-MOOLLM-DESIGN.md](FACTORIO-MOOLLM-DESIGN.md) | Factory metaphor for mooco dataflows |


---

## Closing

The web connected **documents**.

MOOCO connects **cognition** to **worlds** already written in git — skills, rooms, characters, designs — with inspectable mounts, activations, and traces.

MOOLLM is the moocroworld you can fork.

MOOCO is the MOO server that makes forking **runnable**.[ 