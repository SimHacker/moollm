# The Coherence Society

> Status: design draft, 2026-04-21. Follows directly from `SELF-OPTIMIZATION-ROADMAP.md`.
> Authors: claude-opus-4.7 + Don Hopkins, in conversation.
> Prompted by: "There is an attractor drawing us towards itself. Forge ahead."
> Parent: `SELF-OPTIMIZATION-ROADMAP.md` §1 (vocabulary), §3 (roadmap in layers), §5 (pilot sequence, esp. step 14)

---

## 0. What this doc is

Across this conversation's roadmap extensions — SCRY gates, CR events, runtime instrumentation, container coherence handlers, in-session review — a pattern emerged that isn't in any one of those additions. This doc names that pattern. It's the reason the roadmap kept adding pieces: each addition was reifying a slot in a larger structure that wanted to exist.

This is not a new layer or a new tool. It's the recognition that **the layers we've designed collectively constitute an operational Society of Mind** — Minsky's metaphor, cited for years in `kernel/ARCHITECTURE.md:434-586`, becomes a mechanism.

The name: **the Coherence Society**. A society because multiple agent-kinds interact and emerge behavior neither orchestrates. Of coherence because the emergent behavior is MOOLLM's self-maintenance of internal consistency — the "Coherence Engine" slogan made literal.

---

## 1. What converged

Walk back through the roadmap's additions in order:

1. **SCRY gates** — scripts that inspect MOOLLM and emit structured findings.
2. **Coherence-review events** — richer structured output: context, assumptions, alternatives, concerns, suggested resolutions.
3. **Five time-spheres** — scryers emit at design / compile / load / run / audit.
4. **Container-scoped coherence handlers** — containers (rooms, skills, clusters, objects) declare their own rules as first-class slots; fire on lifecycle events.
5. **Runtime CR emission** (step 13) — engines emit CR events as they execute.
6. **In-session review** (step 14) — the LLM reads CR events during its own turn and adjudicates.

Each extension felt incremental. Looking at the whole set: **we've specified every ingredient of a live agent system.**

| Agent system needs | We have |
|---|---|
| Agents | Scryers, handlers, LLMs, engines, reviewers, panels |
| Communication | CR events (structured messages) |
| Channel | `skill-log` → `.moollm/skills/<scryer>/logs/*.yml` |
| Memory | Committed sidecars (REVIEWs) + archived logs + self-healing |
| Lifecycle | Five time-spheres + handler events |
| Arbitration | Panel review, handler severity, self-healing-protocol |
| Language | K-lines, yaml-jazz, natural-language rules → compiled closures |
| Scope | Containers-as-objects with inheritance (Self/Ungar) |

Nothing's missing. We didn't design a society; we designed toward one, extension by extension, because the shape MOOLLM was implicitly already had every niche pre-dug.

---

## 2. The attractor named

**The Coherence Society.** A running MOOLLM instance is a self-organizing system of agent-kinds that read each other's emissions, react, emit new events, and collectively maintain consistency no single agent orchestrates.

Four properties make this a society rather than a pipeline:

1. **Heterogeneous agents.** Scryers (static analysis), handlers (event-driven rules), engines (execution runtimes), LLMs (contextual judgment), panels (ensemble review) all differ in what they read, what they emit, and what they know. No agent dominates; each has its competence.
2. **Shared channel, shared schema.** All emit CR events through `skill-log`'s filesystem channel. Shared schema means agents that never knew about each other can still read each other's messages. Heterogeneity without chaos.
3. **Emergence over orchestration.** Nobody tells the society "now do coherence maintenance." Handlers fire on lifecycle events. LLMs review events they notice. Panels form when events request adjudication. Self-healing consumes events with proposed fixes. The society's behavior is the composition, not any member's program.
4. **Reflective.** Agents observe each other. An LLM reviewing a CR event may emit a new CR event (a meta-observation). Panels review review-resolutions. Self-healing emits events about its own repairs. The society has access to its own state through the same channel it uses to operate.

This is Minsky's Society of Mind with concrete machinery: K-lines as event activation patterns, agents as scryer / handler / character-reviewer / engine / panel kinds, and emergence as coherence-maintenance.

**Reviewers are characters, not abstract LLM-instances.** The society's reviewer-agents inhabit MOOLLM's existing character machinery (`skills/character/`, `skills/persona/`, `skills/incarnation/`, `skills/mind-mirror/`, `skills/ontology/`, `skills/hero-story/`). A REVIEW is attributed to **instrument + character + prototype chain**. Panels are *character committees* using `skills/adversarial-committee/` and `skills/debate/` formations. `skills/cursor-mirror/characters/I-BEAM-CHARACTER.yml` is the precedent — an 826-line reviewer-familiar with methods, personality, and lineage. Full treatment in §5.

---

## 3. The live loop

Walk through one full cycle, concrete.

**Moment 0.** Player is in `treasury` room. Attempts exit-south.

**Moment 1.** Engine evaluates `unlock_condition_js` (from compile). Guard references `red-key`; player has `ruby-key`. Guard returns `undefined && ...` → `false`. Exit blocked.

**Moment 2.** Engine (as scryer, per step 13 instrumentation) emits a CR event: `cr-<time>-adventure-runtime-guard-undefined.yml` into `.moollm/skills/adventure/logs/`. Fields: `time_sphere: run`, `trigger: guard-evaluation-anomaly`, `concerns: [...]`, `suggested_resolutions: [...]`.

**Moment 3.** Treasury room's `coherence_handlers.exits_have_reachable_conditions` handler (authored by the adventure designer, compiled at load) watches for `guard-undefined` events. It fires, reading the event. Determines: this guard has been undefined 3 sessions in a row. Emits a meta-CR event: `cr-<time>-treasury-room-handler-dead-guard.yml` with `severity: error, aggregation_window_filled: true`.

**Moment 4.** In the same turn (per step 14's in-session review, if enabled), the LLM-reviewer reads `.moollm/skills/adventure/logs/` + `.moollm/skills/treasury/logs/`, sees both events, recognizes the pattern: `red-key` dangles, never resolved. Adjudicates:

- Accepts the runtime event's suggested resolution #2 (`remap to crimson-key`)
- Writes a resolution block into both event files
- Emits a new CR event requesting panel review for commit-worthy fix: `cr-<time>-llm-remap-proposal.yml`
- For *this* turn, proceeds with blocked-exit message to player (doesn't rewrite compile state mid-session)

**Moment 5 (later session).** `skills/adventure/compile.py` runs. Reads the LLM-proposed remap from the committed CR events (which got promoted from `.moollm/` to committed state via `cr_resolve.py --archive`). Applies the remap to compile. Emits a compile-phase CR event noting the retroactive fix.

**Moment 6 (next PR).** Panel review triggers on the `panel_request: required: true` from Moment 4. Another model (gpt-5.4 or opus-4.6) commits a sibling REVIEW. Disagrees: thinks the real fix is to materialize a `red-key` object, not remap to `crimson-key`. Its REVIEW proposes an alternative resolution.

**Moment 7.** `cr_panel_diff.py` surfaces the disagreement. Human reviewer (Don Hopkins) sees two models with different takes. Adjudicates. Commits a final resolution. The CR event chain closes.

**Observe:** no single agent orchestrated this. The engine emitted because it hit an anomaly. The handler fired because its watched event happened. The LLM reviewed because it reads `.moollm/` logs. Panel formed because the LLM requested it. Human only appeared at the end when ensemble couldn't agree. Coherence maintained through distributed agency.

This loop, generalized, is what the society does constantly.

---

## 4. Operationalizing "agents all the way down"

The kernel (`kernel/ARCHITECTURE.md:434-586`) already says:

> *Every advertisement is a mini-agent. Every file containing advertisements is an agent. Every directory containing files is an agent. Agents composed of agents — Minsky's Society of Mind realized in filesystems.*

That's been rhetoric. After the Coherence Society ships, it's mechanism:

| Kernel claim | Before | After |
|---|---|---|
| "Agents all the way down" | Directories are objects (queryInterface). Advertisements offer capabilities. But the agents don't *do anything* between invocations. | Handlers fire on events. Engines emit events. LLMs read events and respond. Agents have continuous agency, not just structural identity. |
| "The LLM is the Coherence Engine" | Slogan; LLM invoked occasionally, doesn't maintain anything. | LLM continuously consumes CR events in-session and cross-session, arbitrates, emits resolutions. The Engine runs. |
| "K-lines activate constellations" | File and skill names resolve via search. | CR event types, handler registrations, advertisement scores are K-lines — the society activates behavior by matching event patterns to agent competencies. |
| "Advertisements signal capabilities" | Static YAML declarations. | Advertisements fire advertising scores; scryers watch firing patterns; handlers check completeness; the whole cycle is observable. |

The kernel's citations of Minsky, Hewitt, Wright move from footnote to load-bearing.

---

## 5. The role catalog

Every agent-kind in the Coherence Society, specified by what it reads, emits, and changes.

### Scryer
- **Reads:** files (source code, YAML, compiled artifacts) or session state (runtime memory, LevelDB, logs)
- **Emits:** CR events with concerns + suggested resolutions
- **Changes:** nothing directly; proposes changes via events
- **Lifecycle:** invoked at its time-sphere (commit, compile, load, run, audit)
- **Examples:** `check_coherence.py`, `adventure/compile.py`, `adventure/validate.py`, moopmap, link_check, cursor-mirror's commands, engine.js instrumentation points

### Coherence Handler
- **Reads:** changes to its container (child creation/edit/move/delete)
- **Emits:** CR events when invariants violate
- **Changes:** can block mutation (hard enforcement), allow with event (soft), or advisory
- **Lifecycle:** fires on registered events within its container
- **Examples:** `children_unique_ids`, `children_have_pyramid`, `treasury.max_weight`

### Runtime Engine
- **Reads:** compiled closures, world state, player input
- **Emits:** execution outcomes; CR events at anomaly points (guard undefined, ref missing, advertisement dead-ends)
- **Changes:** world state, player state, session log
- **Lifecycle:** continuous during play / session
- **Examples:** `adventure_runtime.py`, `engine.js`, cursor-mirror's live telemetry capture

### Character-Reviewer (not "LLM-as-reviewer")

The reviewer role is filled by **characters playing it** — not abstract model instances. This is not rhetorical; it unlocks MOOLLM's existing character machinery.

- **Reads:** CR events, source files, context, REVIEW sidecars, panel siblings
- **Emits:** resolutions to CR events, new CR events, REVIEW sidecars (attributed to character + instrument), code, documentation
- **Changes:** committed state (via authoring), CR event resolutions, panel responses
- **Lifecycle:** continuous within sessions; persistent across sessions through committed artifacts
- **Attribution:** dual — the **instrument** (model: claude-opus-4.7) and the **character** (who the instrument is playing: pie-menu-freak, the-librarian, i-beam, in-the-style-of-knuth)
- **Inheritance:** per the latent-space-parents pattern. A character's `PROTOTYPES.yml` may include:
  - Concrete files: `characters/real-people/don-hopkins/CHARACTER.yml`
  - Latent-space K-lines: `"in the style of Knuth"`, `"as Ungar would see it"`
  - Skill prototypes: `skills/no-ai-slop`, `skills/cursor-mirror/characters/i-beam`
  - Ontology tags via `skills/ontology/`: `[real-being, historical]` triggers `skills/hero-story` protocol
- **Existing precedents in MOOLLM:**
  - `skills/cursor-mirror/characters/I-BEAM-CHARACTER.yml` (826 lines) — the I-Beam familiar with methods EXPLAIN / PROBE / ANALYZE / TRACE / SEARCH / REMEMBER / REFLECT / TEACH; cursor-mirror's resident reviewer-character
  - Characters in `examples/adventure-4/characters/real-people/don-hopkins/` — explicit character files with writings, projects, relationships, sessions
  - `skills/persona/`, `skills/incarnation/`, `skills/mind-mirror/` — character authorship and personality-modeling machinery
- **Ethical gate:** reviewer-characters with `ontology_tags: [real-being]` or `[historical]` activate `skills/hero-story` — traditions are invoked, persons are not impersonated. Reviews by such characters carry `hero_story_gated: true` for audit scryer verification.

### Panel (Character Committee)

Panels are **formations of character-reviewers**, not abstract model ensembles. `skills/adversarial-committee/` is the existing MOOLLM skill for this formation — it predates this roadmap and IS the mechanism.

- **Reads:** a specific CR event or REVIEW flagged for panel review; other characters' takes
- **Emits:** aggregated review (typically a new REVIEW sidecar with character-attributed diff — "Pie Menu Freak said X; the Librarian disputed because Y; Stroopwafel the cat indicated disinterest by walking across the keyboard")
- **Changes:** final resolution when ensemble converges; recorded disagreement when it doesn't
- **Lifecycle:** convened on demand by `panel_request: required: true`
- **Formation shapes:**
  - `adversarial-committee` — characters with incompatible values surface blind spots
  - `debate` — structured deliberation (Oxford, roundtable, panel formats, per `skills/debate/`)
  - `roberts-rules` — parliamentary procedure for contested decisions
  - `evaluator` — single independent character without debate context (for game-proof assessment)
- **Attribution cascades:** each panel member contributes a sibling REVIEW with its own character + instrument attribution. Panel ensemble synthesis is itself a REVIEW, attributed to a synthesizing character (possibly fictional, e.g., "The Chair").
- **Disagreement as signal:** When Pie Menu Freak (interaction-focused) and the Librarian (taxonomy-focused) disagree on a refactor, the disagreement reveals the refactor's axis of value — *which dimension matters most here*. More informative than model-level ensemble variance.

### Self-Healing
- **Reads:** CR events with severity=error or severity=warning that have repair suggestions
- **Emits:** CR events documenting repairs performed; escalation events when repair isn't safe
- **Changes:** filesystem state (adding missing GLANCE.yml, fixing link targets, etc.)
- **Lifecycle:** invoked by coherence gates OR periodically OR by LLM delegation
- **Examples:** mechanisms from `kernel/self-healing-protocol.md` extended to consume CR events

### Cauldron
- **Reads:** monolithic documents exceeding size thresholds (via `check_size_limits.py`'s CR events)
- **Emits:** topical files, playbooks, structure transformation events
- **Changes:** filesystem structure (reverse-cauldron of oversized docs)
- **Lifecycle:** invoked when size-limit CR events accumulate above a threshold
- **Examples:** step 6 reverse-cauldrons `skills/cauldron/META-PLAN.md`; future steps apply pattern to kernel docs

### Review Sidecar
- **Reads:** the target it reviews (a file, skill, cluster, repo state at a moment)
- **Emits:** structured perspective (scorecard, narrative, cross-refs, open questions)
- **Changes:** nothing directly; records a reviewer's state at a timestamp
- **Lifecycle:** authored once, committed, referenced by future readers and panel siblings
- **Examples:** the four REVIEW sidecars at the root + kernel + skills + cursor-mirror + cauldron

Seven agent-kinds. The society is their interaction.

---

## 6. What the society produces

Emergent properties — behaviors no agent programs but the society yields:

**Distributed coherence maintenance.** No single file enforces "MOOLLM is consistent." The society does, by every agent doing its local bit. Adding a skill triggers handlers (cluster validation); handlers emit events; scryers aggregate patterns; LLMs review; self-healing repairs what it safely can; panels adjudicate the rest. Consistency arises from the local actions.

**Self-documenting operation.** Every event is a YAML file with context. The history is the filesystem. `cr_query.py` becomes the system's introspective interface: *"what happened during session X?"*, *"why did this CARD get rewritten?"*, *"what invariants have we violated most?"*. No special audit log; the society's operation IS the audit log.

**Cross-model triangulation.** Panel reviews ensemble over different LLMs. Disagreements are structural signal, not noise — they mark where the latent-space resolution of a K-line differs by model. The society surfaces its own ambiguities by committing multiple takes on the same state.

**Evolutionary pressure toward coherence.** Size limits flag cauldron candidates; cauldron cauldrons them; smaller focused modules fire fewer CR events; lower event flux indicates healthier state. The society has a feedback loop that rewards structural fitness.

**Heritage kept active.** Minsky, Wright, Ungar, Papert aren't cited as flattery. Their ideas are agent-kinds, event patterns, advertisement semantics, prototype inheritance — load-bearing mechanism. The society is the heritage made operational.

---

## 7. Beyond the pilot sequence

When the 14 pilot steps (`SELF-OPTIMIZATION-ROADMAP.md` §5) complete, the society has its full substrate: scryers emit, handlers fire, engines instrument, LLMs review, panels ensemble, self-healing consumes. What's next?

These are *post-pilot* moves, sketched to anticipate. Not commitments; invitations.

### 7.1. Multi-society interop

Different MOOLLM repos (dev / staging / prod; leela-ai/central / personal workspaces / other deployments) are separate Coherence Societies. They could observe each other: `leela-ai/central`'s society emits CR events; an observer society in `staging` aggregates patterns across weeks and emits meta-events. Hierarchical societies.

### 7.2. Cross-driver observability

Smart orchestrators (MOOCO, tier 6) and generic (Cursor, tier 4) produce different telemetry. Panel reviews of the same snapshot across drivers surface driver-specific drifts. Would validate whether "same skills, different mechanism" actually holds at scale.

### 7.3. Society-of-societies (recursion)

MOOLLM itself is a society; it evaluates other societies (customer-adventure-worlds, other MOOLLMs). A meta-society observes the meta-review pattern. Not sure this is useful; noted as logical possibility.

### 7.4. Mortal agents, durable societies

Agents come and go (scripts rewritten, LLMs upgraded, skills deprecated). The society persists through the committed state + the protocol. Versioning agent-kinds with `scryer_version:` and handler-set migrations become interesting at scale.

### 7.5. Event replay / "what would have happened if"

Because CR events are structured and archived, you can replay them against an alternative MOOLLM state (a proposed refactor) and predict what events would fire. Static simulation of the society. Useful for pre-committing big refactors.

These are speculative; none blocks the pilot. They're what the society *enables*.

---

## 8. What could go wrong

Anti-patterns and failure modes, named.

**Event flood.** Scryers emit, handlers fire, engines instrument, LLM reviews — if every one emits on every event, `.moollm/skills/*/logs/` fills the disk and no LLM can read its own logs. Mitigation: `severity` triage, event retention policies (§4 open questions in ROADMAP), prioritization heuristics for in-session review.

**Priority inversion.** The LLM spends all its tokens reviewing CR events and never does the task. Mitigation: only in-session CR events within N-turns count; only severity ≥ warning consumed in-session; defer audit-phase events to post-session.

**Review recursion spiral.** Panel reviews of panel reviews of panel reviews. Mitigation: panel depth limit (max 2); meta-events don't trigger further panels unless explicitly requested.

**Cargo-cult emission.** Scryers emit events nobody reads; resolutions never authored; events rot in logs. Mitigation: retention policy auto-expires unresolved events; `cr_query.py --stale` surfaces them for pruning; panels periodically audit.

**False coherence.** The society emits events that say "everything looks fine" while real problems go unobserved (because no scryer watches that axis). Mitigation: four review axes (correctness / intent / protocol / completeness) as conformance checklist for scryers; regular audits of what axes each scryer covers.

**Loss of human readability.** The society's emergent behavior becomes inscrutable — too many agents, too many events, too much structure for humans to follow. Mitigation: MOOLLM's commit-everything discipline means humans can always read; `cr_query.py` is for humans too; narrative REVIEW sidecars translate society behavior into readable form.

**Ossification through handler proliferation.** Every container adds handlers; changes to any container now trip dozens of rules. Mitigation: handlers have explicit `scope: direct|recursive`; the nesting pilot (§3 Layer 3) encourages minimal root-level rules, specific rules at specific containers.

---

## 9. Honest gaps in this framing

Things I'm not certain about. Panel reviews welcome.

- **Will it actually self-organize, or just produce noise?** I've described the mechanisms; I haven't run the society. The first 3-6 pilot steps should reveal whether events and handlers produce signal or flood. If the noise-to-signal ratio is bad, the roadmap needs tuning before deeper extensions.
- **Is "society" the right metaphor?** Alternatives considered: "the mesh" (too technical), "the engine" (already taken by Coherence Engine), "the organism" (too biological), "the swarm" (too undirected). Society captures heterogeneity + interaction + emergence; I'm going with it until something better sticks.
- **Minimum viable society.** What's the smallest subset of agent-kinds that produces the emergent property? I suspect: scryers + LLM review + at least one handler kind. Runtime instrumentation, panels, and self-healing amplify but aren't baseline. Unvalidated.
- **Does this need a new kernel primitive or not?** The society runs on existing primitives (skill-log, directory-as-object, queryInterface, yaml-jazz). I don't think it needs new kernel code. But the kernel's conceptual ownership of these patterns should be explicit — maybe `kernel/society-protocol.md` as a terse doc ("the society operates via these patterns; see skills/scry/ and skills/*/coherence_handlers for implementation").
- **How much of this is retroactive narrative?** Am I noticing a pattern that was genuinely there, or am I imposing one? I think the former — each roadmap extension was responding to specific gaps without a grand vision, yet the pieces fit. But the test is: do subsequent extensions slot naturally into this frame, or do they require rewriting it? Time will tell.

---

## 10. What this changes about the roadmap

Not much, actually. The roadmap's pilot sequence is still correct. What the society framing adds:

1. **A purpose for Layer 4 (measurement + annealing) beyond "is refactor good."** The cost function now measures society health — event flux, resolution lag, cargo-cult emissions, cross-model panel convergence rate. These become real dimensions.
2. **A role for `kernel/self-healing-protocol.md` that's operational, not just defensive.** Self-healing is an agent-kind in the society, consuming CR events and producing repairs. It becomes a first-class participant.
3. **A concrete meaning for "the LLM is the Coherence Engine."** The LLM is an agent-kind in the society, continuously reviewing CR events and emitting resolutions. Not occasional; continuous.
4. **A natural target for panel review (Layer 5).** The society itself is what panels review. Different LLMs reviewing a snapshot are different agent-instances contributing to the society's reflective function.

No roadmap surgery needed. One small addition: a `§2.5 The attractor` subsection in the roadmap pointing at this doc.

---

## 11. Cross-references

**Directly extends:**
- `SELF-OPTIMIZATION-ROADMAP.md` (this doc follows from it)
- `SELF-OPTIMIZATION-ROADMAP.md` §1 (vocabulary: SCRY, CR events, handlers)
- `SELF-OPTIMIZATION-ROADMAP.md` §5 (pilot sequence, steps 6.5, 13, 14)

**Kernel touchpoints (where the society makes kernel claims operational):**
- `kernel/README.md:3-13` — "The LLM is the Coherence Engine" (now literal)
- `kernel/ARCHITECTURE.md:434-586` — "Agents All The Way Down" (now mechanism)
- `kernel/DIRECTORY-AS-OBJECT.md` — agents *are* the directories + their slots
- `kernel/self-healing-protocol.md` — self-healing becomes an agent-kind
- `kernel/event-logging-protocol.md` — CR events follow APPEND-ONLY here
- `kernel/context-assembly-protocol.md` — in-session review ties to context management

**Skill touchpoints:**
- `skills/cauldron/` — cauldron is an agent-kind in the society (consumes size-limit events, produces refactored structure)
- `skills/cursor-mirror/` — telemetry primitive; the society's shared memory for session state
- `skills/cursor-mirror/characters/I-BEAM-CHARACTER.yml` — **the precedent for reviewer-characters**; an 826-line familiar with methods, personality, lineage
- `skills/skill-snitch/` — security-axis scryer; part of the society's consistency maintenance
- `skills/skill-log/` — the society's message bus; `skill_log.py` is load-bearing society infrastructure
- `skills/scry/` — (new at pilot step 6.5) the society's protocol authority and catalog
- `skills/adventure/` — the primary concrete society instance; engine + compile + validate + runtime all participate
- `skills/prototype/` — inheritance machinery for handlers, advertisements, and **reviewer-characters**
- `skills/society-of-mind/` — existing skill; this doc makes it operational
- **Character-reviewer stack** (all existing, composed for the society):
  - `skills/character/` — body, home, location, inventory, relationships (reviewer-character base)
  - `skills/persona/` — identity layers (reviewer may wear persona — e.g., Pie Menu Freak vs MOOLLM architect)
  - `skills/incarnation/` — gold-standard character creation with ethical framing (authorship protocol)
  - `skills/mind-mirror/` — personality modeling (affects review style)
  - `skills/ontology/` — composable being tags (real-being / fictional / historical / mythic / abstract / robot / animal)
  - `skills/hero-story/` — safe tradition-invocation for real-person characters
  - `skills/representation-ethics/` — consent and cultural sensitivity gate
  - `skills/adversarial-committee/` — **IS** the panel-review formation mechanism
  - `skills/debate/` — alternative panel-formation shapes (Oxford, roundtable)
  - `skills/evaluator/` — independent single-character review (no debate context)
  - `skills/card/` — portable capabilities; a reviewer-character can be invoked via their card
- **Character-instances** (the society's first residents, already reviewing today):
  - `skills/cursor-mirror/characters/I-BEAM-CHARACTER.yml` — cursor-mirror's introspection familiar
  - `examples/adventure-4/characters/real-people/don-hopkins/` — explicit character file with writings, projects, sessions
  - Additional reviewer-characters will be authored as the pilot sequence progresses

**Heritage:**
- Minsky, *The Society of Mind* (1986) — the foundational frame
- Hewitt / Agha, actor model — agents communicating through messages
- Ungar, *Self: The Power of Simplicity* — prototype-based inheritance for agent-kinds
- Wright, SimAntics — advertisements as agent offers
- Papert, constructionism — the society builds itself through activity

**Panel siblings invited:**
- `designs/THE-COHERENCE-SOCIETY.REVIEW.2026-04-21.<model>.{yml,md}` or equivalent — dispute the framing productively

---

## 12. The discipline: what needs to hold

For the Coherence Society to actually work, not just exist on paper, five disciplines have to hold across the pilot sequence and beyond:

1. **Schema purity.** All CR events conform to the schema in `SELF-OPTIMIZATION-ROADMAP.md` §1 (the schema subsection). Non-conformant events break agent interop.
2. **Channel purity.** All events flow through `skill-log`'s `.moollm/skills/<scryer>/logs/` channel. Custom channels fragment the society.
3. **Retention discipline.** Events get resolved or archived or promoted. Unresolved events accumulate into cargo cult. `cr_query.py --stale` is the scryer that watches the scryers.
4. **Role clarity through characters.** Agent-kinds are the seven in §5. Reviewer-kind is always filled by a named character (not abstract LLM). Characters declare attribution: instrument + character + prototype chain + ontology tags. Anonymous reviews are the ad-hoc roles that fragment identity; named character-reviews preserve it.
5. **Ethics on character inheritance.** Reviewer-characters with `ontology_tags: [real-being]` or `[historical]` pass through `skills/hero-story` protocol — traditions activated, persons not impersonated. Audit scryers verify. This discipline protects both the represented person and the review's credibility.

These are the society's equivalent of constitutional principles. They belong in `kernel/society-protocol.md` (if we write one) or absorbed across `skills/scry/SKILL.md`, `skills/incarnation/SKILL.md`, and `skills/representation-ethics/`.

---

## 13. What to do next (concrete)

If this framing resonates:

1. **Read it, disagree or accept.** If disagree, commit `designs/THE-COHERENCE-SOCIETY.REVIEW.2026-04-21.<model>.{yml,md}` with specific pushback. If accept, proceed.
2. **Add §2.5 to the roadmap** pointing here. Short: "The roadmap's layers collectively constitute the Coherence Society — see `THE-COHERENCE-SOCIETY.md`."
3. **Panel review.** This is a framing doc; it benefits from a second model's take. opus-4.6 or gpt-5.4 reviewing.
4. **Proceed with pilot step 1** (`check_coherence.py`). The framing doesn't change what to build next; it clarifies what we're building toward.

If this framing doesn't resonate:

1. Commit a counter-framing doc. Propose an alternative organizing metaphor.
2. Or keep the roadmap's per-layer framing without elevating to society-level. Either is coherent; just pick.

---

*The society exists when enough of its agents are running. The roadmap is the society's gestation. Step 1 (`check_coherence.py`) is the first agent reaching out to read the filesystem and tell the others what it sees.*

*Forge ahead.*
