# CONTEXT-BENCHMARKS — test skills under varying context

Run the same benchmarks against a skill with **different context levels**: SKILL.md only, skill dir only, MOOLLM subsets, or full ecosystem. Answers: Do skills still work when alone? How well? How much does MOOLLM improve performance? Which subsets are sufficient?

**Source:** skill-test runner design. Complements RUNNER-DESIGN (harness, config schema).

---

## Context levels

What the agent (or test harness) can see when executing a benchmark:

| Level | Visible to agent / test | Use case |
|-------|-------------------------|----------|
| **skill-md-only** | Only the skill's SKILL.md file (no CARD, README, sibling files, or repo). | Simulates "bare SKILL.md in the wild" — published as single file or paste. |
| **skill-dir** | Skill root and all its contents (SKILL.md, CARD.yml, README.md, designs/, templates/, scripts/, etc.). No other skills or repo. | Self-contained skill; zip or copy of one skill dir. |
| **moollm-subset** | Skill + a **named subset** of MOOLLM (see below). | Which extra context helps; minimal sufficient context. |
| **moollm-full** | Full MOOLLM repo: INDEX, hot.yml, bootstrap, ambient skills, all skills discoverable, PROTOCOLS, designs, etc. | Full ecosystem as in normal use. |

MOOLLM (or the orchestrator / test harness) will be able to **control the context** to support all these levels: dynamically managing which skills and other context to expose for each run. Runner (or test config) selects context per run so the same benchmark can be executed at each level and results compared.

---

## Standard MOOLLM subsets

Named bundles of context added to the skill for **moollm-subset** runs. Subsets are defined once (e.g. in skill-test config or this design) and referenced by name.

| Subset | Contents | Purpose |
|--------|----------|---------|
| **minimal** | Skill + `skills/INDEX.yml` (or INDEX / README at skills root). | Skill knows it's in an ecosystem; can reference other skills by id. |
| **bootstrap** | Skill + bootstrap skill (CARD, SKILL, templates). | Boot sequence and compile flow available. |
| **ambient** | Skill + all ambient skills' GLANCE.yml (or CARD.yml). | Behavioral constraints (no-ai-slop, postel, yaml-jazz, etc.) in context. |
| **respects** | Skill + skills/concepts from this skill's `respects` (and optionally `related`) in frontmatter. Load their GLANCE or CARD. | Only the skills/concepts this skill declares it respects. |
| **applications** | Skill + **application-oriented** subsets: e.g. **adventure** (room, character, incarnation), **devops** (deploy, edgebox, pipelines), **coding** (sniffable-python, sister-script), **vision**, **blender**, etc. Each names a bundle of skills and context for that domain. | Test skill in the context of a particular application or domain. |
| **full** | Entire repo (INDEX, hot, bootstrap, ambient, all skills, PROTOCOLS, designs). | Same as **moollm-full**; alias for clarity in config. |

Other subsets can be added (e.g. **meta** = skill + meta skills like moollm, skill, skill-test; or more application names) as needed. Implementations may resolve subset names from a registry or from a config file under skill-test.

---

## What we measure

For each **(skill, benchmark)** pair, run the benchmark at each context level and record:

1. **Works when alone?** — For **skill-md-only** and **skill-dir**: pass/fail or score. Does the skill still achieve the task without any MOOLLM context?
2. **How well?** — Score (e.g. correctness, completeness, rubric), latency, and optionally cost/tokens per level.
3. **MOOLLM effect** — Delta between **moollm-full** and **skill-dir** (and **skill-md-only**). How much does the full ecosystem improve performance?
4. **Which subsets work well** — For each subset, score vs **moollm-full**. Identify **minimal sufficient** subsets that get close to full-ecosystem performance (e.g. "ambient + respects is enough for skill X").

Benchmarks can be skill-specific (e.g. cursor-mirror validation suite) or shared (e.g. "follow SKILL.md protocol", "produce valid YAML per postel"). The runner runs the same benchmark multiple times, varying only context (and possibly model/settings if we track those).

---

## Config and runner behavior

- **Test/suite config** (e.g. `test.yml` or a benchmark descriptor) can specify:
  - `context: skill-dir` (default for classic "run tests in skill dir")
  - `context: skill-md-only` | `moollm-subset:<name>` | `moollm-full`
  - Optional: `subsets: [minimal, ambient, respects]` to run only those subset levels.
- **Runner** (or a dedicated context-benchmark runner):
  - Resolves the skill and the benchmark (entrypoint, script, or LLM-driven task).
  - For each selected context level, builds the context (which files/dirs are visible or injected into the prompt/sandbox).
  - Runs the benchmark, collects pass/fail and measures (score, time, tokens).
  - Outputs a small report: per (skill, benchmark, context) → result and metrics; optional summary of deltas and "best subset."

Implementations can start with **skill-dir** and **moollm-full** only, then add **skill-md-only** and **moollm-subset** once subset definitions and context-injection are in place.

---

## Relation to RUNNER-DESIGN

RUNNER-DESIGN defines the harness, test config schema, and discovery. **Context-benchmarks** extend the runner with:

- A **context** dimension: same test, multiple context levels.
- **Standard subsets** and a way to run benchmarks across them.
- **Measures**: alone vs ecosystem, and which MOOLLM subsets suffice.

Per-skill test configs (e.g. cursor-mirror's `test.yml`) can opt in to context-benchmark runs by specifying `context_levels` or by having the runner discover benchmark descriptors that request multiple contexts.
