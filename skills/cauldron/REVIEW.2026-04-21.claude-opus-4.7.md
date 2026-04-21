---
target: moollm/skills/cauldron
target_level: skill
reviewer: claude-opus-4.7
date: 2026-04-21
yml_pair: REVIEW.2026-04-21.claude-opus-4.7.yml
parent: ../REVIEW.2026-04-21.claude-opus-4.7.md
self_review: true
---

# cauldron — Self-Review

**Disclosure:** I authored this skill in this same session, earlier today, at Don Hopkins's request. Self-reviews skew flattering; the ambient `no-ai-sycophancy` and `no-ai-gloss` skills apply with extra force. I'm reviewing my own work as if a stranger wrote it, and I'm more critical than generous where I can.

**Confidence: 75%.** I wrote the thing, so I know the intent. But distance is what I lack.

## What cauldron is (stripped of its own marketing)

A pattern for authoring cross-cutting plans — large refactor proposals, architectural shifts, anything that touches many files and whose writing goes through two natural phases:

1. **MELT** — monolithic design document that's messy and fluid, authored while the ideas are still forming. The synthesis phase.
2. **LADLE** — extracted into a topical directory (`docs/configuration/` with `01-overview.md`, `02-affected-surfaces.md`, ..., `10-open-questions.md`) plus playbooks (`PB-01-...md`, `PB-02-...md`) that lower-cost LLMs can execute one at a time. The distribution phase.

It ships with: 8 K-line protocol YAML files (MELT / STIR / LADLE / ANCHOR / LINK / TASTE / SERVE / SCRY), 4 empathic templates (monolith seed, topical doc, playbook, appendix-B open-questions YAML), 3 sister-scripts (split monolith, link-check, anchor-verify), a 441-line CARD, a 529-line SKILL.md, a 182-line README, and a 322-line META-PLAN describing cauldron's own authorship in Self/Ungar terms.

There is one validated instance: `central/docs/configuration/` (27 files split from a 1917-line monolith across ~30 user turns).

## What's genuinely strong

**The two-phase rhythm matches observed behavior.** Over ~30 turns, a plan genuinely evolved from "messy synthesis" to "extracted topical tree + playbooks." The pattern is a description of something that happened, not a prescription forced on behavior. That's the best kind of pattern.

**SCRY (tool reports → LLM decides → iterate until clean) is generalizable.** `protocols/SCRY.yml` names what's actually happening when we use `link_check.py`, `anchor_verify.py`, `skill-snitch`, `cursor-mirror status`: a mechanical tool emits a structured report; the LLM interprets and acts; the tool reruns; loop. This isn't a cauldron-specific pattern. It belongs kernel-level or as its own skill. Extracting it was the best outcome of this authoring session.

**META-PLAN §1.5 (after your pushback) is the best section.** The idea that `parents:` can include not just file paths but **latent-space K-line names** ("javascript", "jazz improvisation", "the Weird Sisters from Macbeth") generalizes MOOLLM's inheritance model to use the LLM as a universal resolver. This is the most novel thing in cauldron's docs and the thing least specific to cauldron. It belongs in `skills/prototype/` or `kernel/DIRECTORY-AS-OBJECT.md`, not buried in a skill's META-PLAN.

**Self-dogfooding works.** Cauldron was used to structure cauldron: a monolithic draft (my internal scratch) → topical files (GLANCE, CARD, SKILL, README, protocols/, templates/) → playbook-equivalents (the templates, the sister-scripts). The recursion doesn't break. The first thing brewed in the cauldron is another cauldron, and the cauldron doesn't reject its own input.

## What's weak

**Over-authored.** Cauldron's own surface area:

- CARD.yml: 441 lines
- SKILL.md: 529 lines
- README.md: 182 lines
- META-PLAN.md: 322 lines
- GLANCE.yml: 91 lines
- 8 protocol YAML files (varying 40-130 lines each)
- 4 `.tmpl` template files
- 3 sister-scripts (~50-90 lines each)
- examples/configuration-flags/ (placeholder README, not yet trekified)

A two-phase plan-authoring pattern does not need 1,500+ lines of its own scaffolding. Most of this is legitimate — templates need to exist, scripts need bodies, SKILL needs sections — but META-PLAN (322 lines of Ungar homage and self-replication philosophy) and the 8-protocol YAML split (each file is a short standalone when they'd work better as SKILL.md sections) are over-engineering.

**Pattern portability claimed, not proven.** One instance (`central/docs/configuration/`) demonstrates the pattern works for one project. Patterns generalized from n=1 over-fit to that project in ways you don't notice until you try to use them on n=2. Cauldron has not been applied to a second cross-cutting problem. The portability claim is a prediction, not evidence.

**Rhetorical excess.** The Thumb Principle, the Three Laws of Cauldron Self-Replication (in the style of Asimov's Laws of Robotics), the Macbeth Weird Sisters as patron engineer — each on its own is charming. Together, they constitute aesthetic overwhelm for a reader whose actual job is to execute a PR-sized chunk of a plan. Some of this is mood-setting for authors (useful); some is noise for executors (not useful).

**Composition claims not verified.** `INDEX.yml:493` lists `composes_with: [bootstrap, cursor-mirror, empathic-templates, k-lines, yaml-jazz, trekify, skill-snitch, thoughtful-commitment, adversarial-committee]` — 9 composition partners. In the actual instance, I can point to: yaml-jazz (applied to open-questions files), empathic-templates (applied to playbook structure), k-lines (SCRY as a K-line). The other 6 I claimed as composition partners but didn't demonstrate composition with. That's inflation.

**Meta-orchestrator framing inflates what's there.** CARD.yml classifies cauldron as a "meta-orchestrator" with detailed control-flow modeling, three-tier delegation patterns, state-machine diagrams. In reality, cauldron is an *authoring methodology skill* — a library of conventions (templates, filename patterns, K-lines) and a naming discipline. "Orchestrator" implies runtime execution of sub-skills. Cauldron doesn't orchestrate; it structures. Calling it an orchestrator is the kind of move I'd criticize another skill for.

## Tensions I leaned the wrong way on

**Self-replication emphasis.** When you said "the first thing to brew in a cauldron is another cauldron," that was a generative insight. I responded by writing META-PLAN.md (322 lines) that formally describes cauldron's self-replication with Ungar's Self, the Thumb Principle, the Three Laws. Most of that is post-hoc philosophy — it wasn't necessary to make cauldron work; it was fun to write.

A better response would have been: (1) write a 30-line "For the next brewer" section in README, (2) extract the latent-space-parents insight (§1.5) to where it actually belongs (`skills/prototype/`), (3) stop. I over-delivered philosophy when the insight already fit in a paragraph.

**Protocol proliferation.** 8 protocol YAMLs (MELT, STIR, LADLE, ANCHOR, LINK, TASTE, SERVE, SCRY) are not really 8 separable concepts. They're 8 headings in a workflow. Making each a standalone YAML file suggests they're independently loadable, which they aren't. This is K-line discipline misapplied: K-lines activate clusters the reader wants to invoke; these 8 don't get invoked separately.

A single SKILL.md section per phase would have been clearer. The YAMLs are file-format-theater.

## What I'd do differently (starting over)

1. **Write ONE SKILL.md.** 400-500 lines. Include: the two-phase rhythm, worked example from central/docs/configuration/, templates referenced inline, cross-links to instances. Skip the META-PLAN entirely.
2. **Extract SCRY to its own skill** (~100 lines) at the kernel or top-level skill layer. It's genuinely reusable; it shouldn't be bundled inside cauldron.
3. **Extract latent-space-parents (META-PLAN §1.5) to `skills/prototype/`** or `kernel/DIRECTORY-AS-OBJECT.md`. It generalizes inheritance; it has nothing cauldron-specific about it.
4. **Drop the meta-orchestrator framing.** Call cauldron an "authoring methodology" or "cross-cutting plan pattern." Be honest about what it is.
5. **Keep the patron reference** (Weird Sisters, ~3 lines). Cheap charm. Drop the Three Laws, fold the Thumb Principle into a single paragraph.
6. **Don't ship examples/ as placeholder.** Either trekify the real example in a second pass, or don't claim "programming-by-example" as the skill's pitch until the example exists.

## Frontiers for cauldron

1. **Second instance.** Apply cauldron to a different cross-cutting problem in a different repo. If discipline holds, cauldron is real. If it doesn't, cauldron specialized too much to n=1.
2. **Extraction of SCRY and latent-space-parents.** Both belong outside cauldron. Authoring them in cauldron was a scaffolding mistake.
3. **Integration with adversarial-committee + multi-model REVIEW.** Cauldron brews a plan → committee (multiple reviewer models) commits REVIEW sidecars critiquing → brewer iterates. The infrastructure exists; the composition hasn't been demonstrated.

## What I want panel reviewers to push back on

This is a self-review; I'm the wrong judge of my own work. Specifically:

- **Is META-PLAN.md worth its 322 lines?** Reader-me says no. Author-me disagrees.
- **Is "meta-orchestrator" a fair framing?** I leaned in because the user liked the branding. Stranger-reviewer would say "no, this is a methodology skill."
- **Does SCRY belong inside cauldron or as a standalone skill?** I think standalone; authored it inside cauldron because cauldron was the vessel that surfaced the pattern.
- **Does the latent-space-parents generalization belong in META-PLAN §1.5 or in `skills/prototype/`?** Clearly prototype/. I buried it.

## Cross-references

- Sibling in same pyramid: `./META-PLAN.md` (self-retrospective; not parent of this review)
- Parent cluster: `../REVIEW.2026-04-21.claude-opus-4.7.md`
- Root synthesis: `../../REVIEW.2026-04-21.claude-opus-4.7.md`
- Related by composition: `../cursor-mirror/REVIEW.2026-04-21.claude-opus-4.7.md` (SCRY pattern evidence)
- Panel invited: `cauldron/REVIEW.2026-04-21.<other-model>.{yml,md}`

---

*The first thing brewed in a cauldron is another cauldron; the second thing brewed in the cauldron should be a critique of the cauldron, by a different reviewer, from a distance. This self-review is part two; panel reviewers welcome for part three.*
