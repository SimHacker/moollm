# LESSONS — configuration-flags brew

What transferred from one refactor to the **cauldron pattern** itself.

## 1. One file until the joints are real

Cross-cutting refactors need a place where contradictions can sit next to each other until a single cut line emerges. Numbered sections and a reserved appendix for questions beat premature directories. **Premature LADLE freezes the wrong boundaries.**

## 2. "Simulated annealing" is STIR with honesty

Early in Phase 1, high entropy is a feature: renumbering, overlapping rules, a fat appendix. That is not failure—it is search in design space. Cooling happens when invariants and non-goals stabilize and the PR graph stops reshuffling. Name the phase so stakeholders do not mistake mess for lack of progress.

## 3. Walk-backs are assets

When a design is cancelled (e.g. a giant shared storage package), **leave the reasoning in the doc.** Future readers inherit *why* not to build the zombie idea again.

## 4. Appendix B is a contract with your future self

Every open question gets a default answer and a link to where it was raised. Questions that "everyone will remember" are the first forgotten. Executors and reviewers use the same list.

## 5. Phase 2 optimizes for a different reader

Phase 1 optimizes for the author’s synthesis. Phase 2 optimizes for **someone who was not in the room**—including a lower-cost LLM on a single playbook. If a playbook step cannot be verified with a command, it is not ready.

## 6. ANCHOR catches narrative drift

The fleet’s code moved while the prose marinated. Grep updated a logging bug from "maybe wrong" to "**provably** silent and total." **ANCHOR is not pedantry; it is how docs earn trust.**

## 7. Playbooks encode the dependency DAG

Parallelism is a graph problem. Land shared packages before consumers; land renames with warning releases before deletes. The README graph is the schedule—**META-PLAN** documents why that beats ad-hoc ticket piles.

## 8. Orthogonal knobs beat clever overload

The deepest architectural lesson of the brew: **stop encoding four axes in one flag.** The documentation process forced that apart until the flag set was *combinable* without hidden coupling. Cauldron did not invent the fix—it made the fix **legible and executable**.

## 9. SERVE is a separate skill stack

Publishing a trekified example needs trekify + snitch + link check. Teaching quality and leak freedom are both gates; neither replaces the other.

---

*This file is intentionally short. The long-form principles live in the source tree’s `design-wisdom.md`; this extracts what applies to any future cauldron instance.*
