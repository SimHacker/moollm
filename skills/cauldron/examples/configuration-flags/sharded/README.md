# Phase-2 tree index (configuration-flags)

This folder in **moollm** does not duplicate the full sharded corpus (that would fork the Fleet Monorepo). It indexes what Phase 2 **LADLE** produced so cauldron learners know what to look for in a finished brew.

## Canonical location

| Phase-2 role | File(s) in Fleet Monorepo |
|--------------|---------------------------|
| Skimmer entry | `docs/configuration/README.md` |
| Overview | `docs/configuration/01-overview.md` |
| Affected surfaces | `02-affected-surfaces.md` |
| Shared packages | `03-shared-packages.md` |
| Storage & paths | `04-storage-and-paths.md` |
| Logging | `05-logging.md` |
| ChainMap / pyvision layering | `06-pyvision-config-chainmap.md` |
| Deprecation & migration | `07-deprecation-and-migration.md` |
| Example configurations | `08-example-configurations.md` |
| Invariants & non-goals | `09-invariants-and-non-goals.md` |
| Open questions (Appendix B) | `10-open-questions.md` |
| Design wisdom (Appendix A) | `design-wisdom.md` |
| **How we cooked this** | `META-PLAN.md` |
| Harper's-style scorecard | `HARPERS-INDEX.md` |
| Playbook hub | `docs/configuration/playbooks/README.md` |
| Executable PR units | `docs/configuration/playbooks/PB-01-*.md` … `PB-13-*.md` (see hub for exact list) |
| Post-execution reviews | `docs/configuration/REVIEW.PB-*.md` |

## Original monolith

| Artifact | Path |
|----------|------|
| Kitchen-sink Phase-1 draft | `docs/CONFIGURATION-FLAGS-PLAN.md` |

## Trekified mirror (optional)

To populate a **full** trekified mirror under `examples/configuration-flags/sharded/`, run SERVE:

1. `trekify` each file in `docs/configuration/` using `../SUBSTITUTIONS.yml`.
2. `skill-snitch SCAN`.
3. `scripts/link_check.py` from cauldron.
4. Commit the tree here.

Until then, treat [MONOLITH.md](../MONOLITH.md) + this index as the teaching surface.

## Simulated annealing ↔ cauldron protocols

| Informal | Formal (cauldron) |
|----------|-------------------|
| Kitchen sink | **MELT** + **STIR** |
| Cooling / stable sections | Exit **STIR** → **LADLE** |
| Shard + verify | **LADLE** → **ANCHOR** → **LINK** |
| Executor readiness | **TASTE** |
| Public example | **SERVE** |

See `docs/configuration/META-PLAN.md` in the Fleet Monorepo for the full narrative (including the six user instructions that defined the process).
