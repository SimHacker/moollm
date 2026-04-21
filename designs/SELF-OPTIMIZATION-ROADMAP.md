# MOOLLM Self-Optimization Roadmap

> Status: design draft, 2026-04-21
> Authors: claude-opus-4.7 + Don Hopkins, in conversation
> Related: root REVIEW sidecars at `moollm/REVIEW.2026-04-21.*.{yml,md}`
> Supersedes: nothing yet; this is the first coherent statement of the plan

---

## 0. What this doc is

A roadmap for MOOLLM to **optimize itself** — using the mechanisms MOOLLM already has (cursor-mirror's introspection, cauldron's two-phase discipline, skill-snitch's static analysis, moopmap's compression stats, the SCRY protocol, panel reviews) to measure, refactor, and systematically improve its own kernel, skills, and scripts.

**What this doc is not:**

- Not a finished spec. It's a roadmap for several months of work.
- Not a commitment to every idea here. Each numbered layer can be dropped or deferred independently.
- Not a cauldron brew yet. When this doc outgrows "one readable markdown file" (say, past 800 lines, or when the first two pilots ship), it's itself a reverse-cauldron candidate: LADLE into `designs/self-optimization/` with topical docs + playbooks.

**Conventions of this doc:**

- Evidence-based. Every concrete claim cites a file or file:line.
- Reviewer-attributed. Disagreement is productive; commit a sibling REVIEW if you disagree.
- Bias toward small, reversible moves. Nothing in here should be a big bang.

---

## 1. Vocabulary

Six terms used throughout. Defining them once prevents drift.

### SCRY

**Two layers of meaning, both load-bearing:**

**As a verb (etymology).** Middle English *descry*, "to perceive / reveal." *Scrying* is divination through a reflecting surface — crystal-gazing, mirror-gazing, water-gazing. The scryer is the crystal ball; the LLM is the reader staring into it.

**As a retronym (Don Hopkins, 2026-04-21).** **S**elf **C**orrecting **R**ecursive **YAML**. Each letter earns its place:

- **S**elf — applied to MOOLLM on itself (self-optimization, self-correcting loops, Ungar's Self as ancestor).
- **C**orrecting — the point is correction, not just diagnosis. Findings carry suggested fixes; the loop doesn't terminate until clean.
- **R**ecursive — tool runs, LLM acts, tool reruns, LLM decides again. Also composes: scryers can scry scryers; reviews can review reviews; cauldrons can cauldron cauldrons.
- **YAML** — the output contract is structured YAML (per yaml-jazz). Scryers emitting JSON or free text are off-spec.

Both meanings coexist. The etymology is the metaphor (why it feels right); the retronym is the mechanism (what it does). Reading `SCRY` in a doc activates both — yaml-jazz applied to a K-line itself: names carry layered semantic data.

**SCRY output: findings vs. coherence-review events.** Simple scryers emit *findings* (pass/fail, error-at-line-42). Richer scryers emit **coherence-review events** — structured records of what the pass did, what context it considered, what assumptions it made, what alternatives it rejected, and what resolutions it offers to a reviewing LLM. Findings are terminal; CR events are conversational.

The adventure compiler is the canonical example. Compiling `unlock_condition: "Player has the red key"` into `return subject?.hasItem('red-key')` is a decision made in the context of nearby objects, flags, rooms. A CR event records the decision, the context consulted, the candidate alternatives (ruby-key vs crimson-key vs iron-key), and the concerns (no literal 'red-key' object exists; alarm flag has no setter). A reviewing LLM can then:

- accept the resolution,
- remap to one of the proposed alternatives in the CR event,
- escalate to the human author,
- or defer to panel review.

CR events use `skill-log`'s existing channel (`.moollm/skills/<skill>/logs/YYYYMMDD-HHMMSS-<slug>.yml`, time-big-endian). The COHERENCE-ENGINE K-line cashes out operationally as "the LLM reviews CR events in context."

**Where CR events fit the four review-kinds in MOOLLM:**

| Kind | Origin | Audience | Home |
|---|---|---|---|
| REVIEW sidecars | human/LLM perspective on state | future readers, panel reviewers | next to target (`REVIEW.<date>.<model>.{yml,md}`) |
| panel review | ensemble of reviewers | each other + the authored state | same as above, multiple sidecars |
| skill-snitch audits | security/consistency scans | trust decisions | `.moollm/skills/skill-snitch/` |
| **coherence-review events** | **machine-originated from scryer passes (any phase)** | **reviewing LLM in context** | **`.moollm/skills/<scryer>/logs/cr-*.yml`** |

Four kinds, same underlying shape (time-keyed, reviewer-attributed, YAML-structured, commit-as-fact), different originators and audiences.

**Five time-spheres of CR events.** Scryers emit at any phase of an artifact's lifecycle; all spheres write to the same channel, share the same schema, and are reviewed by the same LLM protocol.

| Sphere | Scryer examples | Trigger | Typical CR event |
|---|---|---|---|
| **design** | skill-snitch CONSISTENCY, check_coherence, naming-check | commit, pre-commit | "Skill directory exists but not registered in INDEX.yml" |
| **compile** | adventure compile.py, LLM-as-compiler, empathic-expressions | explicit build | "Source says 'red key'; three red-tagged candidates exist; chose 'red-key' (no match)" |
| **load** | world loader, resolver, skill activator | world boot, session start | "exits.south.destination points at `/caves/mine/` but ROOM.yml missing" |
| **run** | adventure_runtime.py, engine.js, LLM executing a turn | every turn, guard evaluation, advertisement firing | "Guard `hasItem('red-key')` returned undefined; player has ruby-key; probably compile bug" |
| **audit** | cursor-mirror, moopmap, session-score | post-session | "Player said 'red key' 5 times; 0 resolved; author likely meant crimson-key" |

The runtime-as-scryer case is specially important: **engine warnings become structured CR events instead of dropped `console.warn` calls.** Guards evaluating to undefined, advertisements firing with no receiver, flags referenced that were never set, branches never taken across N sessions — all observable runtime conditions become reviewable records. The Coherence Engine (the LLM per `kernel/README.md:3-13`) becomes operational through CR event review, not slogan.

**Four review axes that CR events cover** (generalizing beyond "compiled code correct"):

1. **Syntactic/semantic correctness** — references resolve, types match, JS evaluates without throwing.
2. **Intentional fidelity** — the compilation matches authorial intent in context (was "red key" literal or figurative?).
3. **Protocol conformance** — text follows K-line conventions, yaml-jazz, naming, POSTEL liberal-accept / conservative-emit, advertisement scoring, required slot semantics.
4. **Completeness** — the object has what its environment expects (cat with needs has advertisements to fulfill them; takeable object appears in some unlock_condition; room's exits all resolve).

A scryer emits concerns across these axes in a single CR event; the reviewing LLM decides which matter.

**Container-scoped coherence handlers.** Any container (room, skill directory, ontology tag, cluster, inventory, workspace) can declare `coherence_handlers:` as a first-class slot alongside `advertisements:` and `methods:`. Each handler specifies *when* it fires (lifecycle events: `created`, `edited`, `moved-in`, `moved-out`, `deleted`, `compile`, `load`, `audit`), *what rule* it enforces (authored in natural language; LLM-compiled to JS closure like `unlock_condition_js`), *severity* and *enforcement mode* (`hard` blocks edit, `soft` emits CR event, `advisory` records only), and *scope* (`direct` children or `recursive`). Handlers are inherited via `PROTOTYPES.yml` like any slot — generic rules on parent skills; specific overrides on concrete containers.

Example: `skills/no-ai/CARD.yml` declares `children_have_pyramid` (all sub-skills must have GLANCE/CARD), `children_unique_ids` (hard), `hygiene_naming` (warning on non-canonical names), `ambient_sync` (children with `type: AMBIENT` must be in `.cursor/rules/moollm-core.mdc`). Adding `skills/no-ai/hygiene/newsin/` fires the handlers; violations become CR events.

**Connections to existing MOOLLM machinery:**

| Existing piece | How coherence handlers extend it |
|---|---|
| Advertisements (Sims pattern) | Advertisements = what container *can* do; handlers = what container *must* hold. Dual pattern, same authoring grammar. |
| INTEREST-GATES.yml | Proximity/visibility gates on interaction; handlers are gates on mutation. Sibling mechanism. |
| `kernel/self-healing-protocol.md` | Handlers emit findings; self-healing auto-repairs where safe (add missing GLANCE) and escalates where not (duplicate id). |
| Empathic compilation | Handler `rule:` fields compiled same way as `unlock_condition` / method bodies. No new pipeline. |
| Schemapedia (`skills/schema/`) | Handlers are MOOLLM-internal schema mechanism; deserves `schemas/mechanisms/coherence-handler/MECHANISM.yml`. |
| Directory-as-object | `queryInterface(container, 'coherence-handlers')` → `container/CARD.yml.coherence_handlers` or dedicated HANDLERS.yml. |

**What container-scoped handlers unlock:** self-enforcing clusters (every nested skill cluster enforces its own invariants); declarative schema without a separate DSL (natural language rules, LLM-compiled); event-driven coherence checks (fire on specific mutations, not full sweeps); explicit cross-container coupling (via `touches_outside_container:` field); runtime-level structural checks for adventure worlds (a treasury room's "max capacity" handler fires on `moved-in`).

### Formal CR event schema and lifecycle

Every CR event, regardless of which scryer or which time-sphere emits it, conforms to this schema. Future `skills/scry/SKILL.md` will formalize; for now this is the normative reference.

**Required fields:**

```yaml
coherence_review_event:
  event_id: cr-<iso-timestamp>-<scryer>-<slug>    # unique; sortable by time
  scryer: <scryer-name>                            # e.g., adventure-compile, check_coherence
  scryer_version: git:<sha> | semver              # for reproducibility
  emitted_at: <iso-timestamp>
  time_sphere: design | compile | load | run | audit
  source:                                          # what was being analyzed
    file: <path>
    yaml_path: <optional dot-path within file>
    line: <optional line or range>
    text: <optional source excerpt>
```

**Optional field groups** (scryers include what's relevant):

```yaml
  compiled:                                        # present for transformation scryers
    target: javascript | python | yaml | ...
    output: <the produced artifact>

  context_considered:                              # what the scryer looked at
    world: <name>
    room: <path>
    nearby_objects: [<id, ...>]
    flags_referenced: [...]
    # domain-specific — scryers extend this freely

  resolved_assumptions:                            # what the scryer decided without asking
    - slot: <which part of source>
      action: <what was done>
      result: <outcome>
      alternatives_rejected: [...]

  concerns:                                        # findings; the review-worthy content
    - severity: error | warning | info
      type: <kebab-case category, e.g., unresolved-reference>
      id: <stable id within this scryer>
      message: <human-readable>
      axes: [correctness | intent | protocol | completeness]   # which of the four
      suggested_resolutions:
        - type: accept | remap | broaden | add-object | escalate-to-human | ...
          action: <prose>
          proposed_output: <optional concrete fix>
          rationale: <why this resolution>

  panel_request:                                   # when multi-reviewer input sought
    required: <bool>
    recommended: <bool>
    deadline: <optional>
    aggregation_window: <optional>

  touches_outside_container: [<paths>]             # for handlers that cross container boundaries

  resolution:                                      # appended after review (mutation-with-history)
    resolved_by: <reviewer id>
    resolved_at: <timestamp>
    action: accept | remap | escalate | defer-to-panel | suppress
    rationale: <prose>
    resulting_change: <optional commit ref or diff>
```

**Lifecycle — each CR event moves through states:**

```
emitted  →  reviewed  →  resolved
                    │
                    ├──→ accepted        (scryer's resolution was right; no change)
                    ├──→ remapped        (alternative resolution applied; concrete fix committed)
                    ├──→ escalated       (kicked to human author)
                    ├──→ deferred        (panel review pending)
                    └──→ suppressed      (determined non-issue; noted for pattern analysis)
```

The event file is append-only within its YAML (the `resolution:` block is added; not rewritten). This matches the `APPEND-ONLY` kernel principle (`PROTOCOLS.yml`).

**Storage — unified channel through `skill-log`:**

All scryers write to `.moollm/skills/<scryer-name>/logs/YYYYMMDD-HHMMSS-<event-slug>.yml`. Time-big-endian filenames for sort-first discovery. `skill-log` (the skill at `skills/skill-log/`) is the single emission channel; its `skill_log.py` primitive is used by all scryers, Python or otherwise. No scryer writes its own log format.

**Retention policy** (open question, §10 #8): how long CR events are retained locally vs. committed vs. archived. Initial proposal: runtime events (`.moollm/` is gitignored) are session-scoped unless promoted to commit; compile/design events land in CI artifacts; audit events may graduate to commit if they influenced a REVIEW.

**MOOLLM sense.** A mechanical tool stares into the code/docs/filesystem and emits a structured report of what it sees. The LLM reads the report as if reading the crystal ball. The LLM decides what to do (fix, refactor, accept, escalate, simulate, update), acts, and iterates. Tool-reports-LLM-decides-iterate is the SCRY protocol.

**SCRY is already pervasive in MOOLLM** — only the name is localized. Known existing scryers (all emit structured reports for LLM interpretation):

| Scryer | Scries for |
|---|---|
| `skills/adventure/compile.py` (1,481 lines) | YAML → JS closure compilation errors |
| `skills/adventure/validate.py` (867 lines) | Adventure world invariants (rooms, exits, inventory refs) |
| `skills/skill-snitch/` (SCAN, AUDIT, SNITCH, TRUST, CONSISTENCY methods) | Static and runtime skill audits |
| `skills/moollm/scripts/moopmap.py` (321 lines) | Pyramid compression stats |
| `skills/cauldron/scripts/link_check.py` | Internal markdown link resolution |
| `skills/cauldron/scripts/anchor_verify.py` | `file:line` citation drift |
| `skills/cursor-mirror/` commands (59 of them) | Session telemetry, key catalog |
| `skills/image-mining/scripts/{exif,mine}.py` | Image metadata extraction/validation |
| `skills/skill-log/scripts/skill_log.py` | Structured per-skill logging |
| `skills/groceries/scripts/ah.py` | Grocery API validation |

Over 10 scryers, ~9,000 lines of Python, all following the same tool-emits-structured-report shape. None currently declares `protocol: SCRY`. The promotion (next subsection) makes the pattern first-class.

**Current localization.** Protocol lives in `skills/cauldron/protocols/SCRY.yml` (135 lines). That file does not self-describe the etymology. `PROTOCOLS.yml` does not yet contain a SCRY K-line entry. Cross-refs from existing scryers are absent.

**Proposed promotion** (pilot sequence step 6.5):

1. `skills/scry/` — new tier-1 skill. GLANCE + CARD (methods + known scryer catalog) + SKILL.md (formal protocol, tool/LLM contract, composition patterns with skills, sister-scripts, compilers, CI gates) + README (etymology, lineage, why SCRY is a first-class MOOLLM primitive).
2. `PROTOCOLS.yml` entry — SCRY added as a top-level K-line alongside COHERENCE-ENGINE, YAML-JAZZ, POSTEL. Short definition + invoke_when list + `location: skills/scry/SKILL.md`.
3. `kernel/scry-protocol.md` — short kernel doc (~100 lines) establishing the tool/LLM contract as universal infrastructure. Points at `skills/scry/` for the full treatment. This is genuinely kernel-level: the contract is infrastructure, not semantics.
4. Cross-references in existing scryers — each gets `protocol: SCRY` in its frontmatter and a README pointer to `skills/scry/`. One sweeping PR or incremental per-skill PRs.

After promotion: SCRY is first-shelf MOOLLM vocabulary, the ~10 existing scryers acknowledge family membership, the protocol self-describes everywhere, and new scryers (the Layer 1 coherence gates, the Layer 4 experiment harness) inherit the pattern by reference.

### Self-optimization

The recursive move: MOOLLM uses MOOLLM's own mechanisms to improve MOOLLM. Specifically:

- Cursor-mirror (introspection skill) → measures session cost.
- Cauldron (methodology skill) → refactors monolithic docs.
- Skill-snitch (audit skill) → checks skill consistency.
- Moopmap (script) → measures pyramid compression.
- SCRY gates (scripts, unbuilt) → catch drift at commit time.
- REVIEW sidecars (pattern, just added) → multi-reviewer critique.
- The filesystem-as-object-graph → structural perturbation is local file moves.

"Self" as in Ungar's Self language: reflection is cheap because everything is an object with inspectable slots. MOOLLM's reflection is cheap because everything is a file in a navigable tree.

### Reverse cauldron

Cauldron as shipped describes a forward flow: **MELT** (synthesize ideas into monolithic draft) → **LADLE** (extract topical tree + playbooks).

**Reverse flow:** existing-monolith-in-the-wild (skipped MELT; the kitchen-sink doc already exists) → **LADLE** (distill into focused modules + playbooks for applying them).

Same LADLE phase. No MELT phase — the monolith is input, not output. Target audience identical: lower-cost LLMs needing small, focused, independently-loadable context modules.

Two precedents already in MOOLLM:

- **Code case:** `scripts/cursor_mirror_old.py` (monolithic) → `lib/{bubbles,composers,sources,...}.py` (22 focused modules, 2,656 lines) + 702-line CLI shell. Reverse cauldron applied to Python, already done.
- **Doc case:** the cauldron pilot at `central/docs/configuration/` — 1,917-line monolithic `CONFIGURATION-FLAGS-PLAN.md` → 27 topical files + 13 playbooks.

Cauldron's SKILL.md currently frames everything as forward flow; the reverse mode is under-advertised. Fix: add a `modes: {forward, reverse}` section to `skills/cauldron/CARD.yml` once reverse mode has one successful pilot.

### Simulated annealing (as framing, not algorithm)

The refactor methodology borrows SA's structure:

- **State** = current MOOLLM tree (files, skills, scripts, docs).
- **Perturbation** = one reversible refactor (nest a cluster, split a doc, extract a protocol, shrink a CARD).
- **Cost function** = weighted scalar over measurable dimensions (§4 below).
- **Acceptance** = if cost drops by ≥ε and panel review doesn't regress, accept; else revert.
- **Temperature** = risk appetite, scheduled over time. Early: bold restructures. Late: copy editing.

Why borrow SA: **greedy refactoring gets stuck in local minima.** Some refactors transiently worsen one dimension (splitting ARCHITECTURE.md adds file count) before paying off (per-file reads get cheaper). Greedy reverts such moves; SA accepts them. In practice, "temperature" is a social parameter (how much risk we'll take this month), not a numeric anneal.

### Coherence gates

Automated checks for invariants the system claims hold but that hand-maintenance lets drift. The SCRY principle mechanized as a linter family: emit structured reports, fail builds on hard violations, surface advisory findings for LLM decisions.

### Panel review

Multi-reviewer REVIEW sidecars (introduced 2026-04-21 under `REVIEW.<date>.<model>.{yml,md}`). Different models reviewing the same snapshot commit sibling files. Disagreement is evidence, not noise.

---

## 2. What motivates this (findings from the 2026-04-21 review)

Review findings cited from `moollm/REVIEW.2026-04-21.claude-opus-4.7.{yml,md}`:

**Drift already happening.** INDEX.yml says 130 skills / 2026-04-21; INDEX.md said 129 / 2026-03-24 (both now bumped by the emacs addition and my cauldron addition — but the *next* registration will drift again without automation). Cursor-mirror's CARD.yml:142 claims ~9800-line script; actual 702 CLI + 2,656 lib = 3,358. Both are low-severity as individual findings but they signal a missing class of automation.

**Scale exceeds working memory.** Bootstrap demands reading INDEX.yml (754 lines) at every session start. Full ambient injection + INDEX + hot.yml + CARDs consumes a meaningful fraction of context before any task work happens. Cursor-mirror OPTIMIZE is the intended mitigation but has a cold-start problem.

**Core and ornamental are peers.** Adventure-color skills (worm, cat, dog, bartender, budtender) sit in the flat registry next to load-bearing skills (cursor-mirror, representation-ethics, bootstrap). New-reader onboarding cost is inflated.

**Monolithic docs resist incremental improvement.** `kernel/ARCHITECTURE.md` (696 lines), `kernel/SELFISH-COM-IMPLEMENTATION.md` (576 lines), `skills/cursor-mirror/CARD.yml` (354 lines), `skills/cursor-mirror/SKILL.md` (792 lines), `skills/cauldron/META-PLAN.md` (322 lines — my own over-authoring). Each benefits from reverse-cauldron; none has a process that triggers the refactor.

**No measurement.** The kernel asserts "the LLM is the Coherence Engine" but doesn't define what *degraded coherence* looks like or how to measure it. Optimization without measurement is vibes.

### The attractor

During the 2026-04-21 design conversation, the roadmap's extensions (SCRY gates → CR events → time-spheres → container handlers → runtime instrumentation → in-session review) converged on a coherent emergent structure. Not a layer we designed; a shape we designed *toward* without realizing until it was nearly complete.

That shape has a name: **The Coherence Society**. MOOLLM's scryers, handlers, engines, character-reviewers, panels, self-healing, cauldron brews — all coordinating through CR events in `skill-log`'s channel — constitute an operational Society of Mind (Minsky, cited in `kernel/ARCHITECTURE.md:434-586` for years, now mechanism not metaphor). The Coherence Engine rhetoric becomes literal: the society is the engine.

**Reviewers in the society are characters, not abstract LLM-instances.** The reviewer role is filled by named characters inheriting from real-people prototypes (via latent-space K-lines gated by `hero-story`), from explicit character files in the filesystem, from skill-prototypes, and from persona layers. `skills/cursor-mirror/characters/I-BEAM-CHARACTER.yml` (826 lines) is the existing precedent — a reviewer-familiar with methods, personality, and lineage. Panels are character committees formed via `skills/adversarial-committee/`, `skills/debate/`, or `skills/evaluator/`. This unlocks MOOLLM's mature character machinery (`skills/character/`, `skills/persona/`, `skills/incarnation/`, `skills/mind-mirror/`, `skills/ontology/`) for the reviewer role — no new vocabulary needed.

Full treatment: [`designs/THE-COHERENCE-SOCIETY.md`](./THE-COHERENCE-SOCIETY.md). The roadmap's pilot sequence is the society's gestation; step 1 (`check_coherence.py`) is the first agent reaching out and telling the others what it sees.

---

## 3. The roadmap in layers

Each layer is independently valuable. Layers build on each other but none is a prerequisite to starting lower layers — Layer 1 is usable alone, Layer 5 is slower to pay off but deeper.

### Layer 1 — SCRY gates (scripts)

Individual linter-in-the-loop tools. Each small, single-purpose, structured-YAML output, exit-code-on-failure.

Homed at `skills/moollm/scripts/` (sibling of existing `moopmap.py`).

| Script | Invariant | Approx. LOC | Priority |
|---|---|---|---|
| `check_coherence.py` | INDEX.yml ↔ INDEX.md ↔ `ls skills/` agree; CARD `script.lines:` matches `wc -l`; required pyramid files exist | 150 | **first** |
| `compile_index_md.py` | Regenerate INDEX.md narrative from INDEX.yml + skill GLANCE headers — drift-by-construction dies | 150 | **first** (pairs with check_coherence) |
| `check_size_limits.py` | Flag files exceeding thresholds (SKILL.md > 600, CARD.yml > 250, GLANCE.yml > 100, kernel protocols > 300) as **cauldron candidates** | 80 | second |
| `check_links.py` | Internal link validator across all `.md` files — generalization of `skills/cauldron/scripts/link_check.py` | 120 | second |
| `check_naming.py` | Enforce `kernel/NAMING.yml` conventions on filenames, K-line caps, skill directory names | 100 | third |
| `check_ambient_injection.py` | Verify every skill with `type: AMBIENT` in CARD is referenced from compiled `.cursor/rules/*.mdc` | 80 | third |
| `run_container_handlers.py` | Walk the tree, find every container with `coherence_handlers:` declared, execute each handler against its children per registered events (compile/load); emit CR events for violations | 250 | **fourth** (after step 6.5 ships SCRY contract) |
| `regen_card_metrics.py` | Regenerate CARD.yml's `script.lines:` / `script.commands:` fields from actual source — kills the cursor-mirror 9800 drift class | 80 | third |

**Common SCRY output schemas (the tool/LLM contract).** Two shapes, tool picks the richer one when context-resolution matters:

*Finding-shaped output* — simple lint; terminal pass/fail:

```yaml
check_name:
  status: passed | warnings | failed
  invariants_total: N
  invariants_passed: M
  findings:
    - invariant: kebab-case-id
      severity: error | warning | info
      target: path/to/file[:line]
      detail: "What's wrong, factual."
      suggested_fix: "One-line concrete action."
      evidence: "Quote or structured data supporting the finding."
  summary: "One sentence: what the tool saw."
```

*Coherence-review-event-shaped output* — compilation, transformation, or context-dependent analysis; conversational not terminal:

```yaml
coherence_review_event:
  event_id: cr-<iso-timestamp>-<scryer>-<slug>
  scryer: scryer-name
  emitted_at: <timestamp>
  source: { file, yaml_path, text }
  compiled: { target, output }          # if a transformation
  context_considered: { ... }             # what the scryer looked at
  resolved_assumptions: [ ... ]           # what it decided without asking
  concerns: [ { severity, type, id, message, suggested_resolutions: [...] } ]
  panel_request: { required, recommended, deadline }
```

Scryers pick the shape that fits. Simple linters emit findings. Compilers, transformers, and anything that makes contextual judgments emit CR events. Both are readable by the same LLM-in-the-loop protocol; CR events just carry more signal for a reviewer to act on.

CR events flow through `skill-log`'s existing channel: `.moollm/skills/<scryer>/logs/YYYYMMDD-HHMMSS-<slug>.yml`. Time-big-endian filenames, YAML body, commit-or-archive per skill policy.

### Layer 2 — GitHub Actions workflow

One workflow file: `.github/workflows/scry.yml`. Runs the Layer 1 scripts on every PR and push to main.

Structure:

```yaml
# .github/workflows/scry.yml
# Runs coherence and size SCRY gates on every PR and push to main.
# Reports are committed as artifacts; failures block merge for hard invariants.

name: SCRY
on:
  pull_request:
    paths: [skills/**, kernel/**, designs/**, '*.md']
  push:
    branches: [main]

jobs:
  coherence:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - name: Install yaml deps
        run: pip install pyyaml
      - name: check_coherence
        run: python3 skills/moollm/scripts/check_coherence.py
      - name: check_links
        run: python3 skills/moollm/scripts/check_links.py
      - name: check_naming
        run: python3 skills/moollm/scripts/check_naming.py
      - name: run_container_handlers
        run: python3 skills/moollm/scripts/run_container_handlers.py --events compile,load

  advisories:
    runs-on: ubuntu-latest
    continue-on-error: true   # advisories don't block merge, just surface
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - name: check_size_limits
        run: python3 skills/moollm/scripts/check_size_limits.py
      - name: moopmap pyramid stats
        run: python3 skills/moollm/scripts/moopmap.py --check-trend
      - name: regen_card_metrics (drift detection)
        run: |
          python3 skills/moollm/scripts/regen_card_metrics.py --check-only
          # Non-fatal: flags drift without rewriting CARDs in CI

  compile_index:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - name: Regenerate INDEX.md
        run: python3 skills/moollm/scripts/compile_index_md.py --in-place
      - name: Fail if dirty
        run: git diff --exit-code skills/INDEX.md || { echo "INDEX.md drifted from INDEX.yml — regenerate and recommit"; exit 1; }
```

Three jobs:

1. **coherence** — hard gates; failure blocks merge. Catches INDEX drift, broken links, naming violations.
2. **advisories** — soft gates; `continue-on-error: true`. Surfaces oversized files (cauldron candidates) and pyramid-compression anomalies without failing the build.
3. **compile_index** — regenerates INDEX.md and fails if the regenerated version differs from the committed one. Forces INDEX to be a compiled artifact, not hand-maintained.

**Migration step:** Before this workflow lands, run all scripts locally and fix existing violations. The first `check_coherence.py` run will fire on the two drift cases already found (cursor-mirror CARD line count, any remaining index count asymmetry). Fix, commit, then wire the workflow.

### Layer 3 — Structural refactors (reverse cauldron + skill nesting)

Refactors enabled and protected by Layer 1/2 gates.

**Reverse cauldron pilot sequence** (each one PR + one REVIEW sidecar):

1. **`skills/cauldron/META-PLAN.md`** (322 lines) → reverse cauldron of cauldron's own meta-doc. My self-review in `skills/cauldron/REVIEW.2026-04-21.claude-opus-4.7.md` already names the extraction targets (§1.5 latent-space-parents → `skills/prototype/`; §6.5 SCRY → its own skill; rest collapsed to a 30-line README section). Low-risk, high-signal, dogfooding.
2. **`skills/cursor-mirror/CARD.yml`** (354 lines) → split into slim CARD + REFERENCE.yml. The CARD keeps interface (methods, advertisements, familiar). REFERENCE absorbs key-catalog, per-OS paths, documentation index. Pyramid discipline restored.
3. **`kernel/SELFISH-COM-IMPLEMENTATION.md`** (576 lines) → topical split: `queryInterface-protocol.md`, `inheritance-resolution.md`, `compiled-closures.md`. Smaller kernel doc to practice on before ARCHITECTURE.
4. **`kernel/ARCHITECTURE.md`** (696 lines) → the main target. 100-line overview + 9 topical modules (orchestrator-types, advisory-vs-operational, driver-architecture, context-assembly, memory-hierarchy, cursor-optimization, agents-all-the-way-down, heritage, coherence-engine). Bootstrap's mandatory read becomes cheaper; focused reads become richer.

**Skill nesting pilot sequence:**

1. **`skills/no-ai/`** — first nesting pilot. 8 skills (ideology + hygiene/* + performance/*) with crystalline shared identity. Low-risk because I depend on 5 of the 8 as ambient skills — breakage is immediately visible.
2. **`skills/introspection/`** — cursor-mirror, mooco-mirror, skill-snitch, skill-test, thoughtful-commitment, session-log, skill-log, return-stack. Eight skills with high semantic cohesion.
3. **`skills/ethics/`** — representation-ethics, ontology, hero-story + ontology's tags (real-being, fictional, historical, mythic, abstract, robot, animal) as `tags/` sub-cluster.
4. **`skills/character/`** — character, persona, incarnation, mind-mirror + modification/* sub-cluster.
5. Long tail — world/, groups/, communication/, deliberation/, methodology/, etc.

**Rule for nesting:** don't cluster below 3 genuinely-related children. `skills/dataflow/data-flow/` is bureaucracy; `skills/safety/` with just trekify and self-repair is borderline.

**Kernel-doc pattern from nesting:** the cluster directory gets GLANCE.yml (cluster summary) + CARD.yml (advertisements, lists children) + optional SKILL.md (cross-cutting cluster concepts) + optional README.md. Not every cluster needs all four.

**Path-churn mitigation.** Every `[cursor-mirror](skills/cursor-mirror/)` link in existing docs breaks on nesting. Options:

- **Symlinks** at old paths for a transition period (`skills/cursor-mirror/` → `skills/introspection/cursor-mirror/`).
- **Fuzzy `queryInterface`** at the kernel level accepting both paths.
- **Mechanical link rewrite** in one atomic commit after the move.

Pilot (`skills/no-ai/`) probably doesn't need mitigation because the 8 moved skills are mostly referenced by ID not path. Validate the no-ai pilot before worrying about mitigation; don't over-engineer.

### Layer 4 — Measurement + simulated annealing

The experiment harness that turns "does this refactor help?" from vibes into data.

Homed at `skills/moollm/scripts/experiment/`:

```
experiment/
  fixture_record.py   # capture a task + initial state as replayable fixture
  fixture_replay.py   # run a fixture under labeled configuration
  session_score.py    # compute cost-function dimensions for a session
  ab_compare.py       # run fixture under 2+ configurations, diff scores
  dashboard.py        # aggregate across sessions, trend over commits
```

Combined estimate: ~1,000 lines of Python. Same architecture as moo and cursor-mirror: thin command entries + shared `lib/experiment/`. Don't build all at once — start with `fixture_record.py` + `session_score.py` (~400 lines) to enable one A/B test; grow the harness as more refactors need measurement.

**The six cost dimensions and their measurement paths** — full table in §4 below.

**First experiment:** measure `skills/no-ai/` nesting pilot's effect on boot cost and hygiene-skill-navigation cost. Described in §5.

### Layer 5 — Panel review as soft acceptance

For perturbations where the scalar cost signal is ambiguous (dimensions trade off), ensemble-of-reviewers decides.

Protocol:

1. Perturbation proposed (a refactor PR).
2. Objective measurement: Layer 1 gates pass; Layer 4 experiment runs if applicable.
3. Panel of reviewer models commits REVIEW sidecars. At minimum: the authoring model plus one other (currently candidate models: claude-opus-4.6, gpt-5.4, gemini-3-pro).
4. Scorecards diffed via `scripts/panel_diff.py` (unbuilt; future Layer 4 tool).
5. Accept if objective improves AND panel median rating improves. Reject if both regress. Disagreement = new REVIEW explicitly noting tradeoff; human breaks ties.

**Disagreement between objective and subjective = valuable data.** If cost drops but panel hates the new structure, the cost function is missing a dimension. Update cost function; add dimension; re-measure.

---

## 4. The cost function

Six dimensions. Each measurable. Each has a cursor-mirror or cursor-mirror-adjacent path.

| # | Dimension | Lower is better because... | Measurement |
|---|---|---|---|
| 1 | **Boot-cost** | Tokens spent on orientation aren't spent on task | `cursor-mirror timeline @session` → tokens before first substantive tool call on task |
| 2 | **Navigation-cost** | Tool calls to find a skill are overhead | `cursor-mirror tools @session` → counts of `list_dir`/`read_file`/`grep` before target |
| 3 | **Recall-cost** | Files loaded but not used = wasted context | Diff `messageRequestContext` (loaded) ∆ files referenced in output |
| 4 | **Hallucination-cost** | References to non-existent skills = onboarding failure | Output references ∆ `INDEX.yml.all_skills` |
| 5 | **Maintenance-cost** | Churn on stable docs = system isn't stable | `git log` velocity on docs post-refactor; SCRY gate failure frequency |
| 6 | **Coherence-cost** | Drift = system lying about itself | `check_coherence.py` output count + severity |

**Starting weights:**

```yaml
# Proposed as designs/cost-function.yml — commit explicitly; dispute via REVIEW
weights:
  boot_cost:          0.30   # tokens on orientation
  navigation_cost:    0.30   # tool calls to find things
  recall_cost:        0.15   # load-but-don't-use
  hallucination_cost: 0.15   # reference-but-don't-load
  maintenance_cost:   0.05   # churn rate (long-term signal)
  coherence_cost:     0.05   # drift (long-term signal)
```

Total cost `C = Σ w_i × c_i`. Weights are a contract; disagree by committing a REVIEW against `designs/cost-function.yml` proposing different weights.

**Known weakness:** dimensions 1-4 are session-scoped; 5-6 are repo-scoped. Mixing timescales in one scalar is a simplification. In practice, run session-scoped comparisons (1-4) per-experiment; track repo-scoped (5-6) as monthly trends.

---

## 5. Pilot sequence

Suggested order. Each step is one PR + one REVIEW sidecar + one experiment (for later steps).

| # | Step | Type | Risk | Prerequisite |
|---|---|---|---|---|
| 1 | `check_coherence.py` + `compile_index_md.py` | Layer 1 | low | none |
| 2 | `.github/workflows/scry.yml` (coherence job only) | Layer 2 | low | step 1 passes locally |
| 3 | `check_size_limits.py` + `check_links.py` | Layer 1 | low | step 2 landed |
| 4 | Expand workflow with advisories job | Layer 2 | low | step 3 |
| 5 | `fixture_record.py` + `session_score.py` | Layer 4 | med | workflow stable |
| 6 | `skills/cauldron/META-PLAN.md` reverse-cauldron | Layer 3 | low | harness exists |
| **6.5** | **SCRY promotion: `skills/scry/` + `PROTOCOLS.yml` entry + `kernel/scry-protocol.md` + cross-refs from 10 existing scryers** | **Layer 1 foundation** | **low** | **scripts accumulate to validate the pattern** |
| 7 | `skills/no-ai/` nesting pilot + A/B experiment | Layer 3 + 4 | med | step 6 validated reverse mode |
| 8 | `skills/cursor-mirror/CARD.yml` refactor | Layer 3 | low | no-ai pilot validated |
| 9 | `skills/introspection/` nesting | Layer 3 | med | no-ai pilot validated |
| 10 | `kernel/SELFISH-COM-IMPLEMENTATION.md` split | Layer 3 | med | structural pattern validated |
| 11 | `kernel/ARCHITECTURE.md` split | Layer 3 | high | step 10 successful |
| 12 | `panel_diff.py` + multi-model REVIEW habit | Layer 5 | low | cumulative |
| **13** | **Runtime CR emission: `emit_cr_event()` primitive in `adventure_runtime.py` (Python) and `engine.js` (JavaScript); instrument at guard-eval / advertisement-fire / ref-lookup / flag-resolution / dead-branch points** | **Layer 4 extension** | **med** | **step 5 harness + step 6.5 SCRY skill** |
| **14** | **In-session CR review loop: the LLM reads `.moollm/skills/*/logs/cr-*.yml` during its own turn and adjudicates recent events before proceeding** | **Layer 5 extension** | **high (speculative)** | **step 13 shipping CR events in volume** |

**Rationale for step 6.5's placement.** SCRY promotion sits after enough scripts exist (steps 1, 3, 5 add ~5 more scryers to the ~10 already out there) to validate what the protocol covers, but before the deep structural refactors (steps 7-11) whose own scrying needs the brand firmly in place. Early enough to mesh with sister-scripts, skills, and the adventure compiler; late enough that the formalization reflects real usage not speculation.

**Rationale for step 13's placement.** Runtime instrumentation needs the CR event schema and `skills/scry/` contract already shipping (step 6.5). Before then, instrumentation would emit ad-hoc warnings; after, it emits conformant CR events into the unified channel. Estimated cost: ~30 LOC per runtime for the `emit_cr_event()` primitive, then ~5-15 instrumentation call sites per 1,000 lines of runtime code. `adventure_runtime.py` is 1,274 lines; rough estimate 6-19 call sites. `engine.js` is 4,200 lines; rough estimate 20-60 call sites.

**Rationale for step 14's placement and "speculative" label.** In-session self-adjudication closes the tightest feedback loop (LLM receives guard-eval CR event *during* its own turn, reviews, adjusts next action). Valuable but unproven; depends on CR events accumulating in volume (step 13 steady-state) and on a review heuristic for which events to read each turn (open question). High risk because LLM-reads-its-own-in-session logs creates context-management surprises. Listed as a pilot step so it's not lost; acceptable outcome is "tried, reverted to batch-review post-turn."

**Why this order.** Build cheap gates first (steps 1-4). Build measurement (step 5). Use the gates + measurement to guard refactors (steps 6-11). Gradually lower the acceptance threshold as the system learns.

**What NOT to do:**

- Don't start at step 11. Kernel is foundational; first use of a new pattern on a high-stakes target is bad hygiene.
- Don't skip step 6. If cauldron can't reverse-cauldron its own meta-plan, the pattern isn't ready.
- Don't commit step 5's harness without fixtures from at least one real session — an empty harness accumulates in a month.
- Don't add dimensions to the cost function to rationalize refactors that don't improve measured costs. Admit the refactor didn't help; keep looking.

---

## 6. GitHub Actions workflow — full design

See Layer 2 above for the skeleton. This section expands on decisions.

**Trigger scope.** Only on changes to `skills/`, `kernel/`, `designs/`, top-level `.md`. Typo fixes in unrelated files don't need gates running.

**Python setup.** Pinned to 3.12 for reproducibility. Dependencies: pyyaml only (initially). No heavy deps; SCRY scripts should be bootstrappable on minimal runners.

**Artifact storage.** SCRY reports (the structured YAML) get uploaded as workflow artifacts. PR review bots can fetch them to annotate PRs. Panel review tools (Layer 5) can reference them.

**Fail vs. warn.** Hard gates (coherence job) fail the build. Advisory gates (advisories job) use `continue-on-error: true` and surface in a dashboard. Rationale: drift-in-INDEX is an integrity violation; an oversized CARD is a cauldron candidate, not a bug.

**Hook to pre-commit.** The local pre-commit hook already validates YAML/JSON syntax (demonstrated live during this session's REVIEW commits). Extend to call the coherence script locally for fast feedback. CI is the backstop, not the primary gate.

**Workflow location.** `.github/workflows/scry.yml` — named after the protocol, one file, no sprawl. If a second workflow emerges (e.g., panel review automation), it gets its own file.

**Name ambiguity note.** "SCRY" is unusual; a reader who doesn't know the term will be confused. Options: (a) document the name in the workflow file header; (b) rename workflow to something clearer like `coherence.yml` or `lint.yml`. My preference: **keep `scry.yml`** and document the term in the workflow header, because SCRY names the *iterative LLM-in-the-loop pattern* (not just linting), and that pattern is worth branding. But this is a bikeshed-adjacent call; reviewer pushback welcome.

---

## 7. What not to do

Grouped themes, not item-by-item. Each bullet has caused enough grief elsewhere to warrant explicit prohibition.

- **No boil-the-ocean refactors.** One perturbation per PR per experiment.
- **No optimization toward superficial metrics** like "minimize file count" (which unrefactors) or "maximize documentation" (which bloats).
- **No cost function without measurement.** If you can't compute it, drop the dimension from the function rather than estimating it.
- **No panel reviews of trivial changes.** Run panels on structural refactors where taste matters. Typo fixes don't need multi-model review.
- **No treating annealing as replacement for taste.** The cost function encodes taste. If optimum is wrong, function is wrong. Panel disagreement surfaces bad functions.
- **No shipping layers as a suite.** Each layer independently valuable. Don't wait to ship Layer 1 until Layer 5 is ready.

---

## 8. Where things live (registry of paths this roadmap creates)

```
.github/workflows/scry.yml                  # Layer 2

skills/moollm/scripts/
  moopmap.py                                # exists
  check_coherence.py                        # Layer 1, step 1
  compile_index_md.py                       # Layer 1, step 1
  check_size_limits.py                      # Layer 1, step 3
  check_links.py                            # Layer 1, step 3
  check_naming.py                           # Layer 1, later
  check_ambient_injection.py                # Layer 1, later
  experiment/
    fixture_record.py                       # Layer 4, step 5
    fixture_replay.py
    session_score.py
    ab_compare.py
    dashboard.py
    panel_diff.py                           # Layer 5, step 12
    lib/experiment/                         # shared lib modules

designs/
  SELF-OPTIMIZATION-ROADMAP.md              # this file
  cost-function.yml                         # §4 weights as committable contract
  EXPERIMENT-2026-MM-DD-<name>.md           # per-experiment writeups
  self-optimization/                        # when this doc exceeds 800 lines, LADLE here

skills/no-ai/                               # Layer 3, step 7 (nesting pilot)
  GLANCE.yml
  CARD.yml                                  # includes coherence_handlers:
  README.md
  HANDLERS.yml                              # optional — if handlers grow past CARD slot
  ideology/ hygiene/ performance/

skills/introspection/                       # Layer 3, step 9
  GLANCE.yml / CARD.yml
  cursor-mirror/ mooco-mirror/ skill-snitch/ ...

skills/cauldron/
  SKILL.md                                  # update with modes:{forward,reverse}
  META-PLAN.md                              # reverse-cauldron target (step 6)
  (extraction targets: skills/prototype/, skills/scry/)

skills/scry/                                # pilot step 6.5 — promote from cauldron-local
  GLANCE.yml                                # etymology + retronym, one-paragraph what-is-it
  CARD.yml                                  # methods + advertisements + catalog pointer
  SKILL.md                                  # tool/LLM contract, CR event schema, composition
  README.md                                 # lineage, Don Hopkins retronym credit, why first-class
  catalog.yml                               # registry of all scryers in MOOLLM:
                                            #   per entry: name, path, time_sphere, scries_for,
                                            #   output_format (yaml conformant?),
                                            #   emits_cr_events (yes/no/partial),
                                            #   emits_suggested_fixes (retronym-C checkbox),
                                            #   recursive (retronym-R checkbox)
  scripts/
    cr_query.py                             # query CR events across skills by type/severity/time
    cr_resolve.py                           # mark a CR event as resolved with a reason
    cr_panel_diff.py                        # diff CR resolutions across reviewers (step 12)

kernel/scry-protocol.md                     # pilot step 6.5 — kernel-level tool/LLM contract
PROTOCOLS.yml                               # add SCRY K-line entry (alongside COHERENCE-ENGINE, YAML-JAZZ, POSTEL)

skills/schema/schemas/mechanisms/coherence-handler/
  MECHANISM.yml                             # schemapedia entry: container-scoped handlers
  README.md                                 # links to SCRY skill and kernel scry-protocol

kernel/SELFISH-COM-IMPLEMENTATION.md        # reverse-cauldron target (step 10)
kernel/ARCHITECTURE.md                      # reverse-cauldron target (step 11)

skills/adventure/
  adventure_runtime.py                      # step 13: add emit_cr_event() + instrumentation
  engine.js                                 # step 13: add emit_cr_event() + instrumentation
  lib/cr_events.py (or similar)             # step 13: shared CR event emission helper

skills/skill-log/                           # existing — elevated as universal CR emission channel
  scripts/skill_log.py                      # used by every scryer for CR event writes
  (documentation update needed: skill-log is the unified SCRY emission primitive)

.moollm/skills/<scryer>/logs/               # runtime CR event archive (gitignored)
.github/workflows/scry.yml                  # Layer 2 — see §3 Layer 2 for full spec
```

---

## 9. Documentation fixes this roadmap surfaces (not part of main plan; file separately)

Small cleanups noticed while writing this. None urgent.

- **`skills/cauldron/protocols/SCRY.yml`** does not explain the name. Add two-line etymology header: "Scrying = divination through a reflecting surface. Tool reports; LLM reads; iterate."
- **`skills/cursor-mirror/CARD.yml:142`** claims `~9800 lines`; actual 702 + 2,656 = 3,358. Update manually until Layer 1 auto-regenerates this field.
- **`skills/INDEX.md`** and `INDEX.yml` will drift again on next skill addition. This is the motivation for step 1; no one-off fix is worth it.
- **`skills/cauldron/META-PLAN.md`** is the target of pilot step 6. Its own self-review (`skills/cauldron/REVIEW.2026-04-21.claude-opus-4.7.md`) already lists extraction targets.

---

## 10. Open questions

These are the ones where my confidence is below 70%. Dispute productively via a REVIEW sidecar on this file.

- **Is "SCRY" the right brand?** ~~Previously questioned.~~ Resolved by reviewer + author agreement 2026-04-21: SCRY names a specific important pattern (LLM-in-the-loop analysis: mechanical tool emits structured report → LLM interprets → iterate) that deserves first-class branding. It meshes with skills, sister-scripts, the adventure compiler, CI gates, and the review panel. Promotion to top-level K-line via step 6.5.
- **Should the cost function weights be per-experiment or global?** Per-experiment = more honest (different refactors optimize different things); global = easier to trend. My take: commit global defaults to `designs/cost-function.yml`, let experiments override locally when needed.
- **Should panel review require ≥ 2 models, or is 1 non-authoring reviewer enough?** More reviewers = more robust but costs multiply. Start with 1 non-authoring reviewer; scale to 2-3 when panel diff tooling exists.
- **When does this roadmap itself deserve reverse-cauldron?** I think around 800 lines or after the first 3 pilots ship, whichever comes first. Currently ~450 lines. Noted as trigger.
- **Is `skills/moollm/scripts/` the right home for new scryers, now that `skills/scry/` exists (after step 6.5)?** Dual tenancy: `skills/scry/` hosts the protocol, catalog, and generic tools; `skills/moollm/scripts/` hosts MOOLLM-self-scryers (check_coherence, moopmap, compile_index_md) that scry MOOLLM specifically. Per-domain scryers live in their domain skill (`skills/adventure/compile.py` stays in adventure; `skills/skill-snitch/analyzers/*` stay in snitch). They all reference `skills/scry/SKILL.md` for the contract.
- **In-session CR review (step 14): safe or context-polluting?** Reading `.moollm/skills/*/logs/cr-*.yml` during a live turn could close the tightest feedback loop (engine emits CR event → LLM adjudicates → engine continues). It could also flood the context window with stale events, cause priority inversion on task work, or create feedback loops where reading events triggers more events. Unknown until tried. Proposed guardrail: LLM reads only events emitted in the current turn, filtered by a heuristic (severity ≥ warning, touches_current_room, etc.). Mark step 14 as experimental; acceptable outcome is "tried, reverted to post-turn batch review."
- **Cross-container coupling via `touches_outside_container:` — how strict?** Handlers that reach outside their container (e.g., `skills/no-ai/`'s `ambient_sync` touching `.cursor/rules/moollm-core.mdc`) couple containers in ways that make refactoring harder. Options: (a) forbid cross-container touches (strict encapsulation; handlers can only scry their own children); (b) allow with `touches_outside_container:` declaration (current proposal; visible coupling); (c) formalize cross-container dependencies with a linker that tracks them. Option (b) seems right for now; formalize if couplings proliferate.
- **CR event retention policy.** Runtime events can accumulate fast; `.moollm/skills/<scryer>/logs/` grows unbounded. Proposed defaults: (1) runtime events are session-scoped — truncated or archived at session end unless promoted (e.g., via `cr_resolve.py --archive`); (2) compile/design events are CI-artifact-scoped — published as workflow artifacts, not committed unless they cause a REVIEW; (3) audit events may graduate to committed artifacts if they informed a REVIEW sidecar. Formalize in `skills/scry/SKILL.md`.
- **Should the four review axes (correctness / intent / protocol / completeness) be required fields in every CR event's `concerns:` block?** Currently proposed as optional per-concern tag. Strict would be `axes: [...]` required. Benefit: forces scryer authors to think about which axes apply. Cost: extra field per concern. Soft default for v0; revisit after 10+ scryers emit events.

---

## 11. Cross-references

**Reviews that motivate this roadmap:**

- `moollm/REVIEW.2026-04-21.claude-opus-4.7.{yml,md}` — root findings (drift, scale, onboarding cost)
- `moollm/kernel/REVIEW.2026-04-21.claude-opus-4.7.{yml,md}` — "boring kernel" mis-label, advisory/operational leak
- `moollm/skills/REVIEW.2026-04-21.claude-opus-4.7.{yml,md}` — core-vs-ornamental mixing, pyramid strain
- `moollm/skills/cursor-mirror/REVIEW.2026-04-21.claude-opus-4.7.{yml,md}` — 9800→3358 line drift, CARD oversize
- `moollm/skills/cauldron/REVIEW.2026-04-21.claude-opus-4.7.{yml,md}` — self-review of cauldron, extraction targets

**Skills this roadmap depends on or extends:**

- `skills/moollm/` — home of the optimization tooling (scripts/moopmap.py exists; Layer 1 additions land here)
- `skills/cauldron/` — provides the reverse-cauldron pattern; itself a pilot target (step 6)
- `skills/cursor-mirror/` — measurement substrate; LevelDB introspection; reverse-cauldron target (step 8)
- `skills/skill-snitch/` — existing audit tooling; some checks may merge with Layer 1 scripts
- `skills/moopmap` — first script in the scry family; template for others
- `skills/bootstrap/` — mandatory-read reduction is one optimization target
- `skills/prototype/` — extraction target for latent-space-parents insight (META-PLAN §1.5 → here)
- `skills/scry/` — **new skill promoted at step 6.5**; protocol, catalog, generic tools
- `skills/schema/` — schemapedia entry `schemas/mechanisms/coherence-handler/` added at step 6.5
- `skills/skill-log/` — **elevated as the universal CR event emission channel**; its `skill_log.py` becomes load-bearing infrastructure for every scryer
- `skills/adventure/` — step 13 instruments runtime (`adventure_runtime.py` + `engine.js`) with CR event emission; `compile.py` and `validate.py` are existing SCRY instances worth cross-referencing from `skills/scry/catalog.yml`
- `skills/empathic-expressions/` / `skills/empathic-templates/` — natural-language-to-code compilation; coherence handler `rule:` fields and CR event `resolved_assumptions:` reuse this pipeline

**Kernel touchpoints:**

- `kernel/DIRECTORY-AS-OBJECT.md` — skill nesting is a generalization; coherence handlers are a first-class slot on the object model
- `kernel/NAMING.yml` — `check_naming.py` enforces
- `kernel/ARCHITECTURE.md` — reverse-cauldron target (step 11); "Coherence Engine" claim gets its operational cashout via CR events
- `kernel/SELFISH-COM-IMPLEMENTATION.md` — reverse-cauldron target (step 10)
- `kernel/self-healing-protocol.md` — **consumes CR events**: self-healing reads severity=error/warning CR events from `.moollm/skills/*/logs/` and either auto-repairs (add missing GLANCE.yml) or emits follow-up CR events escalating to human attention
- `kernel/event-logging-protocol.md` — CR events follow the `APPEND-ONLY` discipline from here (events mutate only by appending resolution blocks)
- `kernel/scry-protocol.md` — new kernel doc at step 6.5; establishes tool/LLM contract as universal infrastructure
- `PROTOCOLS.yml` — adds `SCRY:` K-line entry at step 6.5

**Cross-cutting concerns (name them explicitly):**

- **Coherence Engine as operational system.** The kernel's claim that "the LLM is the Coherence Engine" (`kernel/README.md:3-13`, `kernel/ARCHITECTURE.md:420-430`) was a slogan. After this roadmap lands: scryers (any time-sphere) emit CR events, the LLM reviews them in context, self-healing-protocol consumes them for auto-repair, panel-review ensembles adjudicate hard cases, and the event stream flows through skill-log. That's the slogan operationalized.
- **Event-based coherence maintenance.** Before: periodic sweeps (if any). After: handlers fire on lifecycle events, emitting CR events for just the delta. Cheaper at runtime; richer signal for review.
- **Unified observability.** Before: `console.warn` drops, CI failures in flight logs, grep-based archaeology. After: one channel (`.moollm/skills/*/logs/cr-*.yml`), one schema, one review protocol — queryable via `cr_query.py`, panel-reviewable via `cr_panel_diff.py`, trend-analyzable via roadmap Layer 4 dashboard.

---

## 12. How to disagree

Two expected modes:

1. **You disagree with a specific decision** (e.g., the weights in §4, the pilot order in §5, the cluster groupings in §3.3). Commit `designs/SELF-OPTIMIZATION-ROADMAP.REVIEW.<date>.<model>.{yml,md}` or equivalent sibling. State your position with evidence. I'll update the roadmap or fork a counter-roadmap.
2. **You disagree with the whole framing** (e.g., "simulated annealing is the wrong metaphor," "MOOLLM shouldn't have CI"). Commit a counter-design doc at `designs/ANTI-SELF-OPTIMIZATION.md` or similar. Make the case. If it's compelling, this doc supersedes to it.

Roadmap evolution is panel-reviewable. No single reviewer owns this.

---

*The best thing MOOLLM can do for itself is use itself to improve itself. The second-best thing is to measure whether the improvement actually happened.*
