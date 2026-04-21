# 🍲 CAULDRON

> *"Double, double, toil and trouble; fire burn and cauldron bubble."*
>
> *— The Weird Sisters, Macbeth*

Two-phase discipline for large cross-cutting technical plans. **Melt** a gnarly problem into one brewing monolith. **Ladle** out a tree of topical docs plus executable playbooks that lower-cost LLM executors can run in parallel.

## The shape

```
Phase 1: melt, cook, brew                Phase 2: ladle, serve
┌─────────────────────────────┐         ┌─────────────────────────────┐
│ docs/<topic>-plan.md        │         │ docs/<topic>/               │
│  §1, §2, §3, …              │         │   README.md                 │
│  Appendix A wisdom          │   ──▶   │   01..10-topic.md           │
│  Appendix B open questions  │         │   design-wisdom.md          │
│                             │         │   META-PLAN.md              │
│  One file. Messy. Numbered. │         │   playbooks/                │
│  Grep-anchored. Walk-backs  │         │     README.md (dep graph)   │
│  visible. Questions tracked │         │     PB-01-…md … PB-NN-…md   │
└─────────────────────────────┘         └─────────────────────────────┘
     High-cost designer                      Low-cost executors
     synthesizes once                        parallelize N PRs
```

## Why two phases

Because they serve different goals with different tools:

- **Phase 1 is for finding the shape.** Relationships form; rules clash and resolve; open questions accumulate; walk-backs stay visible. A single file is easier to scroll than a directory whose structure is still in flux.
- **Phase 2 is for downloading the designer's accumulated context into docs so executors don't need the designer in the room.** Templated playbooks, bidirectional navigation, grep-anchored claims.

Moving to Phase 2 too early freezes half-baked ideas. Staying in Phase 1 too long means the team can't help. Cauldron names both phases, signals the transition, and mechanizes the split.

## The seven protocols

| K-line | Phase | What it does |
|---|---|---|
| **MELT** | 1 | Start a new monolith. `docs/<topic>-plan.md`. Numbered sections. Reserved Appendix B. |
| **STIR** | 1 | Fold a new user turn into the monolith. Preserve walk-backs. Update Appendix B. |
| **LADLE** | transition | Split the stable monolith into the topical tree + playbook directory. |
| **ANCHOR** | transition | Re-verify every cited path / line number / function via ripgrep. |
| **LINK** | transition | Bidirectional Navigation ↔ Implemented-by links. Run link-checker. |
| **TASTE** | 2 | End-to-end readthrough. Smell-test for vague TBDs or dangling questions. |
| **SERVE** | 2 | Deliver. Commit. Optionally create a trekified teaching copy. |

Details: [SKILL.md](SKILL.md) and [CARD.yml](CARD.yml).

## Cauldron in the MOOLLM constellation

Cauldron is a conductor. The work is done by existing MOOLLM skills:

| Skill | Role in the brew |
|---|---|
| **[bootstrap](../bootstrap/)** | Phase-1 session warmup; the pot isn't empty, it's pre-seasoned. |
| **[cursor-mirror](../cursor-mirror/)** | Probe prior sessions for half-finished ingredients. Export Phase-1 chat as Phase-2 source material. |
| **ripgrep** | Ground every factual claim against the actual code. ANCHOR's whole purpose. |
| **[empathic-templates](../empathic-templates/)** | 10-section playbook template with `{{describe_X}}` / `{{summarize_Y}}` slots LLMs fill from the monolith. |
| **[k-lines](../k-lines/)** | Every numbered § and every playbook is a K-line. Cross-refs are K-REFs. |
| **yaml-jazz** | Appendix B open-questions tracker is structured YAML with semantic comments. |
| **[trekify](../trekify/)** | Sanitize the example ingredients for public/teaching use. |
| **skill-snitch** | Audit the sanitized output for leaked proprietary details. |
| **[thoughtful-commitment](../thoughtful-commitment/)** | Delivery commit with cursor-mirror-backed reasoning. |
| **[adversarial-committee](../adversarial-committee/)** | Pressure-test design ideas during STIR before inscribing. |
| **no-ai-slop / no-ai-hedging / no-ai-sycophancy** | Ambient hygiene on everything cauldron writes. |
| **postel** | Accept messy Phase-1 clarifications; emit clean Phase-2 specs. |
| **robust-first** | Executors stop-and-escalate on unexpected state, not silently skip. |

## Signals you are in Phase 1 (and should stay)

- Sections are still being renumbered.
- Contradictory rules coexist until resolved in context.
- You catch stale claims by grepping and fixing them.
- Appendix B keeps growing.

## Signals Phase 2 is ready

- Section numbers have stabilized across multiple turns.
- Open questions have default answers and aren't changing daily.
- You stop writing new sections and start editing existing ones.
- The user says *"now break it up."*

## Exemplary instance

The first real-world cauldron brew: **the Leela AI configuration-flags plan**.

| Artifact | Purpose |
|---|---|
| `central/docs/CONFIGURATION-FLAGS-PLAN.md` (1917 lines) | Phase-1 monolith, kept as an archaeology artifact |
| `central/docs/configuration/README.md` | Phase-2 scope + navigation for skimmers |
| `central/docs/configuration/01..10-*.md` | Topical files (overview, shared packages, storage, logging, …) |
| `central/docs/configuration/design-wisdom.md` | Cross-cutting principles (Appendix A) |
| `central/docs/configuration/META-PLAN.md` | The process wisdom extracted from this brew |
| `central/docs/configuration/playbooks/` | 13 PR-sized playbooks with dependency graph |

The **trekified teaching copy** of that tree lives in [examples/configuration-flags/](examples/configuration-flags/). Every substitution 🖖-flagged; public academic citations (Minsky, Papert, Drescher) preserved; proprietary product / customer / infrastructure details masked.

Compare the real project to the trekified example side-by-side. The real one shows what cauldron produces on a real codebase with real risks. The trekified one is the teaching artifact.

## Quick start

**New plan:**

```bash
# Phase 1
moollm invoke cauldron:MELT --topic configuration-flags
# → creates docs/configuration-flags-plan.md with §1 scope + Appendix B

# N turns of STIR
moollm invoke cauldron:STIR --turn "now consider autotest's env vars"
# → appends a new § or folds into existing sections

# When stable
moollm invoke cauldron:LADLE --out docs/configuration/
# → creates the full topical + playbook tree

# Anchor every claim
moollm invoke cauldron:ANCHOR --out docs/configuration/ --strict
# → ripgrep-verifies every cited line number, file path, function name

# Wire up links
moollm invoke cauldron:LINK --out docs/configuration/
# → adds Navigation ↔ Implemented-by; runs link-checker

# Readthrough
moollm invoke cauldron:TASTE --out docs/configuration/
# → smell-tests for dangling TODOs, vague language

# Deliver
moollm invoke cauldron:SERVE --out docs/configuration/ --trekify-example
# → thoughtful-commitment for the split PR; trekified teaching copy
```

**Executor pickup:**

```bash
# Bootstrap first
moollm invoke bootstrap

# Read the playbook's Navigation block
cat docs/configuration/playbooks/PB-03-trim-pyvision-gcp.md | head -20

# Then work the Steps, running Verification after each
```

## Self-ish object instantiation

A cauldron session **is an object instance**. It inherits discipline from the cauldron skill:

```
cauldron (skill)
  └─ cauldron.instance (one brew)       — e.g., central/docs/configuration/
       ├─ cauldron.instance.§N           — one numbered section (a K-line)
       └─ cauldron.instance.PB-NN        — one playbook (an executable unit)
```

The directory is the identity. Moving `docs/configuration/` to `docs/config-v2/` renames the instance. Copying it spawns a sibling cauldron. Every tool that operates on "a cauldron" walks the directory structure, no registration table required — a direct application of MOOLLM's `kernel/DIRECTORY-AS-OBJECT.md`.

## Patron engineer

**The Weird Sisters** from *Macbeth*. Not because the work is cursed — because the work is alchemical. Many ingredients go in. Heat, time, and stirring transform them. When the brew is ready, you ladle specific useful portions out. The mess of ingredients is not a bug — it's the precondition for the clarity that follows. Stir with purpose. Know when to ladle.

## The self-replicating thing

The first thing you brew in a cauldron is another cauldron. This skill was brewed, informally, before it existed. See [META-PLAN.md](META-PLAN.md) for the self-replication story, the Thumb Principle (what replicates vs what doesn't), and the Three Laws of Cauldron Self-Replication.

## Related skills

- [trekify](../trekify/) — sanitizes the example copy shipped with cauldron.
- [cursor-mirror](../cursor-mirror/) — probes for ingredients; exports the Phase-1 chat.
- [empathic-templates](../empathic-templates/) — fills the playbook slots.
- [thoughtful-commitment](../thoughtful-commitment/) — delivers the SERVE commit.
- [k-lines](../k-lines/) — numbered sections and playbooks are K-lines.
- [adversarial-committee](../adversarial-committee/) — pressure-tests design ideas during STIR.
- [skill-snitch](../skill-snitch/) — audits the trekified example.
- [bootstrap](../bootstrap/) — warms up every cauldron session.

## Tagline

> **Melt a big plan down. Ladle out small PRs.**
