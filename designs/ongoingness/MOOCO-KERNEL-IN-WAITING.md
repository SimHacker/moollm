# MOOCO — The Kernel the Conversation Presupposed

The rwk-chat conversation talks about "the orchestrator" as if it were
hypothetical: the kernel that manages the context window as virtual memory,
handles interrupts at token boundaries, pages skills in and out, schedules
background cognition. It is not hypothetical. It is MOOCO — the MOO Custom
Orchestrator, a sibling repo (`mooco/`) with roughly 17,000 lines of design
documents, derived from Leela's production PDA orchestrator (Juho Hietala) and
extended with MOOLLM patterns. ChatGPT never heard about it; there wasn't
bandwidth in the session. This document supplies the half of the conversation
that stayed in Don's head.

The short version: **every abstract claim in the ongoingness conversation has
a concrete counterpart already designed in mooco.** The conversation was not
speculation about what an orchestrator might do; it was a description, from
the outside, of a system whose blueprints already existed.

## The correspondence map

| Ongoingness conversation says | MOOCO design specifies | Where |
|-------------------------------|------------------------|-------|
| Orchestrator = kernel; LLM = CPU | MOOCO as proxy "in total control": intercept, analyze, filter, record everything | MOOCO-IN-THE-MIDDLE.md |
| Continuity of memory needs a hierarchy | Three-tier memory: ephemeral (Postgres), persistent (git), reflective (mirrors) | MOOCO-MEMORY.md |
| Attention-aware paging | The `heat` operation: activation counts `[direct, 1-hop, 2-hop]`, decay, warm/cold | MOOCO-SKILL-MANAGER.md |
| Speculative activation / prefetch | CG (Treasure Collector): diffusion, advertisement prefetch, cache-miss learning | MOOCO-SKILL-SYSTEM.md |
| Agency over attention (curiosity prerequisite 4) | LLM-driven paging: include/exclude/trigger/page_in/page_out; focus lock and defocus | Both skill docs |
| K-lines restore states of mind | `k_line_activate` as first-class message part and SSE event; K-CACHE.yml capsules | MOOCO-ARCHITECTURE.md, MOOCO-SCHEMA.md |
| Idle cognition on a budget | Local-model snitch: cheap background models watch, summarize, annotate the stream | MOOCO-IN-THE-MIDDLE.md |
| Agencies inside, language at boundaries | Division of labor: TypeScript does mechanical diffusion, LLM does fuzzy judgment | MOOCO-SKILL-MANAGER.md |
| Inference as Unix process, not CGI script | Reconnection-first streaming: the stream survives the client | MOOCO-STREAMING.md |
| "Watch yourself think" | mooco-mirror: query your own past sessions, k-line activations, room traversals | MOOCO-ARCHITECTURE.md |

The first two extensions are treated in detail in
[KLINE-CONTEXT-CACHE.md](KLINE-CONTEXT-CACHE.md). The rest of this document
covers the correspondences that go beyond paging.

## Three continuities, three memory tiers

[ONGOINGNESS.md](ONGOINGNESS.md) splits the consciousness-stream question into
continuity of computation, of memory, and of subjective experience, and says
the design mistake is arguing about the third while the first two remain
unbuilt. MOOCO-MEMORY.md is the build plan for the second:

- **Ephemeral** (PostgreSQL) — the chat log: messages, thinking blocks, tool
  calls. Working memory, preserved indefinitely rather than discarded. The
  name describes authority, not durability: the storage is fully persistent,
  but the content is ephemera in the archivist's sense — process, drafts,
  the trace of thought — and nothing rebuilds from it. "Episodic" would be
  the less misleading label: a durable record of what happened, as opposed
  to git's canonical statement of what is.
- **Persistent** (git) — the single source of truth: skills, characters,
  world state, code. The microworld itself. Sessions load from git and commit
  decisions back to git.
- **Reflective** (mirrors) — cursor-mirror reads Cursor's past sessions;
  mooco-mirror reads MOOCO's own. `getKLineActivations()`,
  `getRoomHistory()`, semantic search over past thought via pgvector.

The reflective tier is what makes "discover unfinished business" — the
conversation's definition of how curiosity emerges from persistence — an
implementable query rather than a metaphor. A system that can grep its own
past sessions for unresolved questions, failed predictions, and abandoned
plans has the raw material for prerequisite 3 (memory as accumulated
unfinished business). What's missing is only the scheduler that runs those
queries during idle time — and MOOCO's proxy position plus its cheap
local-model layer (below) is where that scheduler would live.

Continuity of computation — the KV cache, the first tier — is the one thing
MOOCO cannot supply over a provider API. That is precisely the NeLLM
boundary: MOOCO builds tiers two and three now; NeLLM adds tier one when you
own the runtime.

## Self's polymorphic inline caches, applied to attention

The conversation touched Self's dynamic deoptimization and the V8 lineage.
MOOCO-SKILL-SYSTEM.md carries that lineage further than the conversation had
room for: the k-line cache is explicitly modeled on **Self's polymorphic
inline caches (PICs)**.

| Self PIC | MOOCO k-line cache |
|----------|-------------------|
| Method dispatch site | Concept/query pattern |
| Receiver type cache | K-line → skill mappings |
| Cache hit = fast dispatch | Hot k-line = instant activation |
| Cache miss = slow lookup | Cold k-line = grep/search, then update cache |
| Polymorphic (multiple types per site) | Multiple skills per k-line, with hit counts |
| Megamorphic stub (too many types) | Too-generic k-line ("code") → skip cache, always search |

Two refinements the conversation never got to:

- **Directional traversal keys.** Cache keys are not just k-lines but ordered
  pairs: `security=>streaming` (adding auth to streams) activates different
  skills than `streaming=>security` (securing existing streams). The LLM
  reports which paths it actually followed; only those directed edges warm.
  Over sessions, frequently-followed paths become highways — spreading
  activation flows asymmetrically along **learned thought paths**, not
  undirected similarity.
- **Heat flows along weighted directed edges** with decay — Minsky's
  spreading activation, implemented as a deterministic TypeScript engine over
  a graph the LLM helped build.

This is the k-line-as-state-of-mind claim from
[KLINE-STATE-OF-MIND.md](KLINE-STATE-OF-MIND.md) given a cost model: the PIC
analogy says which reinstatements are fast paths and which fall back to
search, and how the fast paths are learned rather than declared.

## Focus lock and defocus: attention as an explicit policy

[ONGOINGNESS.md](ONGOINGNESS.md) names **agency over attention** as
curiosity's fourth prerequisite and calls attentional policy "where the
research is." MOOCO-SKILL-SYSTEM.md specifies the mechanism:

- **Scanning mode** — full skill index, warm cards, heat map injected. The
  model surveys what it could think about.
- **Focus lock** — the model chooses a cluster (skills, characters, rooms)
  and locks: index injection stops, context tightens by half or more,
  iteration accelerates. Expansion without rescan is allowed.
- **Defocus: the learning moment.** On unlock, the model reports
  `useful_k_lines` (polish those edges), `unused_k_lines` (tarnish them), and
  `missing` (mark the map — vocabulary the system lacked). The Treasure
  Collector persists the update to K-CACHE.yml, checked into git.

The defocus report is Drescher's loop applied to the attention graph itself:
predict (prefetch), act (focused work), observe surprise (cache misses,
unused activations), revise the schema (edge weights). The system is running
schema refinement over *its own attention machinery* — curiosity's machinery
pointed at the machinery.

This is also the honest implementation of "thought budget" from
[SKILL-ROADMAP.md](SKILL-ROADMAP.md): focus modes make attention spending
visible and reportable instead of ambient and unaccounted.

## Ongoingness at the product layer: streams that survive the client

The conversation's CGI-script indictment — prompt, run, exit — has a small-o
counterpart in MOOCO's streaming design (MOOCO-STREAMING.md,
MOOCO-DECISIONS.md): everything is an `AsyncGenerator<SSEEvent>`,
reconnection-first, with an ActiveStreamRegistry so a page reload or dropped
connection replays buffered events and resubscribes. **The client dying does
not kill the computation.** That is not KV-level continuity, but it is the
same architectural stance applied one layer up: the conversation is a
persistent process, and UIs are views onto it. A system designed this way is
already shaped to accept a persistent inference substrate underneath.

## The proxy position: a kernel needs to see everything

MOOCO-IN-THE-MIDDLE.md puts MOOCO between the user and the model backend:
every message and tool call passes through it. It can intercept, modify,
block, gate, or scriptify; it records the full stream to PostgreSQL
(time-series + pgvector) for replay and reflection. Two consequences for the
ongoingness argument:

- **A kernel is defined by its position, not its cleverness.** The NeLLM
  kernel manages the model from inside the token loop; MOOCO manages it from
  the protocol loop. Same role, different granularity of interrupt. The
  closer you move MOOCO toward the GPU, the more it becomes NeLLM — see the
  gradient table in [KLINE-CONTEXT-CACHE.md](KLINE-CONTEXT-CACHE.md).
- **Cheap background cognition already has a home.** The design runs a local
  model (Ollama-class) over the stream continuously: summarizing intention,
  annotating tool calls, diffing declared versus actual behavior. That is
  idle cognition with a budget — the conversation's requirement that
  background thinking follow expected value rather than self-stimulation —
  implemented with models cheap enough to run always-on.

## K-lines in the wire protocol

In MOOCO, k-lines are not documentation conventions; they are schema.
`k_line_activate` is a first-class message part type alongside `text`,
`thinking`, and `tool_call`; `k_line_fired` is an SSE event with source and
strength; `mooco-mirror k-lines @1` queries the activation history of any
past session; pgvector indexes them for semantic recall. The state-of-mind
capsule of [KLINE-STATE-OF-MIND.md](KLINE-STATE-OF-MIND.md) has a storage
substrate and a replay mechanism waiting for it.

## Division of labor is the agencies argument

[SERIALIZATION-LOSS.md](SERIALIZATION-LOSS.md) argues: agencies inside,
agents at boundaries; activation within, language at boundaries. MOOCO's
core split — *TypeScript does mechanical tracking; the LLM does fuzzy
judgment* — is that argument as an engineering decision. The orchestrator
tracks the k-line network, diffuses heat, filters warm items, executes paging
decisions: deterministic, auditable, no tokens spent. The model judges
relevance, chooses focus, reports what worked: the parts that need cognition.
Neither serializes its working state into chatbot messages at the other; they
share a compact protocol of activations and reports. The Dixie-cup failure
mode is avoided not by making messages richer but by not routing cognition
through messages at all.

## What this changes about the roadmap

[SKILL-ROADMAP.md](SKILL-ROADMAP.md) phases stay the same, with one
correction of emphasis: Phase 1 ("prove the architecture with ordinary LLM
calls") is not greenfield. The CG engine, heat operation, K-CACHE format,
focus protocol, and defocus learning loop are specified in mooco and waiting
for implementation. The experimental Priority-5 skills (attention-prefetch,
kv-checkpoint, latent-k-line) are not alternatives to the mooco design — they
are sensor upgrades to it, and the mooco implementation is their control
condition. Measure the K-CACHE hit rate first; that is the baseline the
runtime-level machinery must beat.

## Sources (mooco repo, sibling of moollm)

- `designs/MOOCO-ARCHITECTURE.md` — shared-core architecture, mooco-mirror, MOOLLM event mapping
- `designs/MOOCO-MEMORY.md` — three-tier memory, git as source of truth
- `designs/MOOCO-SKILL-SYSTEM.md` — CG/Treasure Collector, PIC-for-attention, focus lock, defocus, SHOUTED k-lines
- `designs/MOOCO-SKILL-MANAGER.md` — the `skill` tool, `heat` operation, K-CACHE.yml, see-also diffusion
- `designs/MOOCO-STREAMING.md` — AsyncGenerator streams, reconnection-first
- `designs/MOOCO-IN-THE-MIDDLE.md` — proxy position, local-model snitch, tool gating
- `designs/MOOCO-DECISIONS.md` — clean-room strategy, PDA lineage
