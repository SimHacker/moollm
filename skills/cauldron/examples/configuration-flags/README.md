# Example: configuration-flags (trekified)

**Patron:** Geordi La Forge — *"We melted one document until the phase boundaries were real, then ladled it into containers any crew could run in parallel."*

This directory is the **public teaching copy** of a real cauldron brew: unifying environment variables and CLI flags across a 🖖 **Forward Sensor Inference Suite** (vision workers), a 🖖 **Positronic Action Processor** (insights), 🖖 **Forward Sensor Outposts** (edge deployments), and a cross-repo 🖖 **Validation Grid** (autotest). The proprietary source lives in the Leela `central` monorepo; here you get the **process**, the **substitution map**, a **condensed trekified monolith**, and **lessons**—without fleet-specific names or internals.

## What problem the real brew solved

One overloaded knob (`QUEUE_DRIVER`) had been smuggling decisions about 🖖 **Subspace Broadcast** (events), 🖖 **Long-Range Object Vault** (bulk storage), structured data stores, and logging. Autotest left the knob unset; imports never loaded cloud filesystem adapters; ground-truth reads failed **silently** and scores went to zero. Double negatives (`DISABLE_GCS`), three names for one project id, and deep `os.getenv` calls in library code completed the picture.

The target: **five orthogonal drivers**—events, data, storage, log sinks, MQTT—plus positive identity flags, **one parse site** at process entry, and small shared Python packages so every surface behaves the same whether the ship is in 🖖 **Sector 001** (cloud) or on an outpost.

## The cauldron shape (how this was cooked)

| Phase | Protocol | What happened |
|-------|----------|----------------|
| 1 | **MELT** → **STIR** × N | One kitchen-sink document grew from a few hundred lines to ~1,900+ over many turns. Numbered sections, walk-backs kept visible, Appendix B for open questions. No implementation during this phase—text only. |
| 1b | **Simulated annealing** (informal) | Early sections contradicted later ones; numbering churned; the appendix swelled—**that is supposed to happen**. High temperature: accept messy structure until the joint set (where the real cuts are) becomes obvious. Cool down: contradictions resolve into invariants and a PR sequence. |
| 2 | **LADLE** | Split into a tree: overview, affected surfaces, shared packages, storage, logging, ChainMap, deprecation, examples, invariants, open questions, **design-wisdom**, **META-PLAN**, and **playbooks/** (one landable PR each). |
| 2 | **ANCHOR** + **LINK** | Grep every path and line claim; fix drift (e.g. a logging bug was *worse* than the draft said). Bidirectional navigation between topics and playbooks. |
| 2 | **TASTE** | Smell-test for vague TBDs and executor confusion; trim noise. |
| 3 | **SERVE** (optional) | Trekify for this `examples/` directory; `skill-snitch` audit; ship. |

The reusable recipe for *how* to do Phase 1 → 2 is written up in the source tree as **META-PLAN** (see mapping below).

## Artifacts in *this* directory

| File | Role |
|------|------|
| [README.md](README.md) | You are here. Process + pointers. |
| [SUBSTITUTIONS.yml](SUBSTITUTIONS.yml) | Trekify dictionary for masking fleet terms if you regenerate artifacts. |
| [MONOLITH.md](MONOLITH.md) | Condensed **trekified** Phase-1 narrative (shape of the big doc, not a full 1,900-line paste). |
| [LESSONS.md](LESSONS.md) | What generalized beyond this one refactor. |
| [sharded/README.md](sharded/README.md) | Index of the Phase-2 tree and how it maps to the source repo. |

## Source of truth (non-trekified)

For the full monolith, the split tree, playbooks, execution reviews, and Harper's-style scorecard:

- Monolith draft: `docs/CONFIGURATION-FLAGS-PLAN.md` in [leela-ai/central](https://github.com/leela-ai/central)
- Phase-2 tree: `docs/configuration/` (README, `01-overview.md` … `10-open-questions.md`, `design-wisdom.md`, `META-PLAN.md`, `playbooks/`, `HARPERS-INDEX.md`)

Rough outcome from that effort (see Harper's Index in source): on the order of **18** merged PRs in **12** days, **13** playbook documents, **191** files touched, new shared packages for app config, logging, and retry—with documentation as a first-class deliverable.

## How to reproduce or extend this example

1. Edit [SUBSTITUTIONS.yml](SUBSTITUTIONS.yml) if fleet vocabulary shifts.
2. Run **trekify** over `central/docs/configuration/**/*.md` (and the monolith) with that dictionary; flag substitutions with 🖖 per the trekify skill.
3. **skill-snitch SCAN** on the output; fix leaks.
4. **link_check** (cauldron `scripts/link_check.py`) on the trekified tree.
5. Commit here as an updated teaching snapshot.

See [../README.md](../README.md) for the general contribution flow for cauldron examples.

## What readers should notice

- **Phase 1 is for thinking; Phase 2 is for shipping.** Mixing them loses walk-backs and forces premature file boundaries.
- **Open-question discipline** (Appendix B) prevents "we'll decide later" from evaporating.
- **Playbooks are the unit of parallel execution**—each one is one PR, with verification steps, not prose-only hope.
- **Evidence before rename:** grep-first culture is explicit in META-PLAN; it avoided pointless churn across live systems.

Live long and refactor sensibly. 🖖
