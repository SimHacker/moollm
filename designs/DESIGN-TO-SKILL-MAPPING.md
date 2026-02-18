# Design → Skill migration plan

When a design crystallizes into a skill: **move the design into the skill first as DESIGN.md**, then push and pull parts into GLANCE, CARD, SKILL, README, and plugin surfaces. This document maps the full design tree to target skills, constituent parts, and plugin surfaces. Some docs stay in `designs/` (archival); some duplicate (pointer in skill, body in designs).

**Publishing:** Skills may be published independently (zip of skill dir or bare SKILL.md). Follow **[designs/SKILL-PUBLISHING-POLICY.md](./SKILL-PUBLISHING-POLICY.md)** — self-contained SKILL.md, related skills documented, standard "Part of MOOLLM" blurb, and standard metadata (Anthropic-compatible + MOOLLM extension).

---

## The pattern: design becomes skill

1. **Create or use skill dir** — `skills/<skill-id>/`.
2. **Add DESIGN.md** — Move or copy the design doc into the skill as `designs/DESIGN.md` (or `designs/<k-line>.md` in subdirs; see cursor-mirror, skill-test).
3. **Push/pull to artifacts:**
   - **GLANCE.yml** — what, why, when; k-lines; one screen.
   - **CARD.yml** — id, name, methods, advertisements, dependencies; **plugin surface declarations** (analyzers, patterns, surfaces, templates, etc.).
   - **SKILL.md** — protocol, prompts, workflow; ref to DESIGN.md for rationale.
   - **README.md** — user-facing; examples, install, invoke.
4. **Plugin surfaces** — Add standard and ad hoc plugin dirs; document in DESIGN.md and CARD.yml; builtin + user_path where applicable.
5. **Leave behind (optional)** — In `designs/`, keep a short pointer or duplicate for archaeology; update indexes/DESIGNS.md to point at the skill.

---

## Plugin surface taxonomy

Skills can extend via **standard** and **ad hoc** plugin surfaces. skill-snitch is the exemplar.

### Standard surfaces (reusable across skills)

| Surface | Purpose | Example |
|--------|---------|--------|
| **templates/** | Scaffolding; init files | skill-snitch: README, config, ignore, trust-overrides |
| **examples/** | Example runs, sample data | adventure: rooms, characters |
| **catalog/** | Curated external items | skill-snitch: approved, caution, malware, MCP servers |
| **designs/** | Design docs inside skill; k-line naming, subdirs by source | cursor-mirror, skill-test |
| **reference/** | Reference data (keys, schemas, assimilated) | cursor-mirror: assimilated/, universal/, KEY-CATALOG |
| **tests/** | Test suite; entrypoint for skill-test | cursor-mirror/tests/ (future) |

### Ad hoc surfaces (skill-specific)

Defined in CARD.yml and DESIGN.md; builtin + user_path (e.g. `.moollm/skills/<name>/`) for merge.

| Skill | Surfaces | What they do |
|-------|----------|--------------|
| **skill-snitch** | patterns/, surfaces/, analyzers/, registry | Patterns = what to match; Surfaces = where to look; Analyzers = how to analyze; Registry = scan modes (merge builtin + user). |
| **skill-test** | designs/runner/, designs/<skill-id>/ | Per-skill validation designs (e.g. cursor-mirror/VALIDATION-SUITE). |
| **cursor-mirror** | reference/assimilated/, reference/universal/, reference/reverse-engineered/ | External knowledge; universal model; reverse-engineered artifacts. |
| **adventure** | rooms/, characters/, objects/ | Room YAML, character YAML, portable objects. |
| **incarnation** | characters/, templates/ | Character creation; templates for new characters. |

### Parameterization and extension

- **Builtin + user_path** — CARD lists `builtin:` (in-skill) and `user_path:` (e.g. `.moollm/skill-snitch/patterns/`). Runner merges both; user can add without forking.
- **Registry / modes** — Single file (e.g. `registry.yml`) that combines plugins into named modes (SCAN, AUDIT, SNITCH, or custom).
- **Schema per surface** — Each plugin type has a small schema (id, name, patterns/rules/source); DESIGN.md documents how to add new plugins.

---

## Mapping: design document → skill → parts and plugins

### Already in skill (designs moved or summarized)

| Design / location | Skill | Constituent parts | Plugin surfaces | Note |
|-------------------|-------|--------------------|-----------------|------|
| skills/cursor-mirror/designs/* | cursor-mirror | DESIGN.md = designs/README.md + 5 docs; ASSIMILATION, VALIDATION (summary), I/O, REVERSE-ENGINEERED, MOOCO | reference/assimilated, reference/universal, reference/reverse-engineered | Done. Validation detail in skill-test. |
| skills/skill-test/designs/* | skill-test | DESIGN.md = designs/README.md; runner/RUNNER-DESIGN; cursor-mirror/VALIDATION-SUITE | designs/<source>/ per skill | Done. |
| moollm/designs/SKILL-TEST-DESIGN.md | — | Pointer only → skills/skill-test/designs/ | — | Leave as pointer. |

### Single design → single skill (move into skill as DESIGN.md)

| Design doc | Target skill | Push to | Plugin surfaces to add | Leave behind |
|------------|--------------|---------|------------------------|--------------|
| **skill-snitch-design.md** | skill-snitch | DESIGN.md (full); GLANCE (what/why/when); CARD (already has analyzers, patterns, surfaces, templates); SKILL (protocol); README (user-facing) | Already has: patterns/, surfaces/, analyzers/, templates/, registry | designs/: pointer to skill or short summary. |
| **SKILL-SNITCH-EXTENSIBILITY.md** | skill-snitch | Merge into DESIGN.md or designs/extensibility/; CARD already declares user_path | Same | Can merge into skill-snitch DESIGN.md. |
| **SKILL-SECURITY-ARCHITECTURE.md** | skill-snitch or kernel | If snitch-specific → skill-snitch DESIGN.md; if org-wide → kernel or designs/ | — | Decide: security architecture = kernel vs skill. |
| **text-adventure-approaches.md** | adventure | designs/DESIGN.md or designs/TEXT-ADVENTURE-APPROACHES.md; SKILL ref | — | Leave copy in designs/ (archival). |
| **SKILL-CHARACTER-DESIGN-NOTES.md** | incarnation and/or character | designs/ in incarnation or character skill | templates/, examples/ | Possibly split: incarnation vs character skill. |
| **MOO-EXPERIMENTS.md** | adventure or new moo skill | designs/ | — | Leave in designs/ or move to skill if MOO becomes a skill. |
| **cursor-mirror-self-reflection.md** | cursor-mirror | designs/ or reference; CARD/SKILL ref | — | Move to cursor-mirror/designs/ as CURSOR-MIRROR-SELF-REFLECTION.md. |
| **cursor-self-review.md** | cursor-mirror or code-review | designs/ in skill | — | Map to code-review or cursor-mirror. |
| **emergent-self-observation-2026-01-24.md** | cursor-mirror or meta | designs/ | — | Archival or cursor-mirror designs/. |
| **self-aware-image-pipeline-explained.md** | image-mining or cursor-mirror | designs/ | — | Map to image-mining if exists. |
| **register-switching.md** | kernel or format-design | kernel/ or skill | — | Conceptual; kernel doc. |
| **legible-social-dynamics.md** | debate or evaluator | designs/ | — | Conceptual; leave or skill. |
| **anthropic-import-plan.md**, **anthropic-skill-upgrades.md** | skill (meta) or bootstrap | designs/ under skill | — | Migration notes; can live in skill or designs/. |
| **snap-moollm-integration.md** | New skill or kernel | designs/ | — | If becomes skill, move. |
| **NAMESPACING-SKILLS.md**, **SKILL-NAMESPACING.md** | skill (meta-skill) | DESIGN.md or kernel | — | Meta; kernel or skills/skill/. |
| **SKILL-ECOSYSTEM.md** | skill (meta) or kernel | DESIGN.md | — | Ecosystem = INDEX + trust; kernel or skill. |
| **MOOLLM-FOR-HACKERS.md** | moollm or kernel | README or docs | — | Top-level doc. |
| **MOOPMAP.md** | kernel or new skill | kernel/ or skill designs/ | — | Semantic mipmap; kernel. |
| **MEMGPT-ANALYSIS.md** | kernel or bootstrap | designs/ or kernel | — | Context design. |
| **MOOLLM-PERMISSIONS-ARCHITECTURE.md** | kernel | kernel/ | — | Permission model. |
| **MOOLLM-PROTOCOLS.md** | kernel | PROTOCOLS.yml + kernel | — | Protocol specs. |
| **GIT-AS-FOUNDATION.md** | kernel | kernel/ | — | Philosophy. |
| **FACTORIO-MOOLLM-DESIGN.md** | kernel or mooco | designs/ or kernel | — | Architecture. |
| **factorio-logistics-protocol.md** | Same | Merge or ref | — | |
| **DIRECTORY-AS-IUNKNOWN.md** | kernel or k-lines | kernel/ | — | |
| **CONNECTIONS-MAP-FRAME-SCHEMA-MICROWORLD.md** | kernel | designs/ or kernel | — | |
| **VISUAL-PROGRAMMING-LINEAGE.md** | kernel or format-design | — | Leave designs/. |
| **SICP-MOOLLM.md** | kernel or skill | — | Leave or skill. |
| **MOOFS-DESIGN.md** | New skill or kernel | — | If MOOFS becomes skill, move. |
| **SIMULATION-AS-SERVICE.md** | kernel or eval | — | Conceptual. |
| **HOME-AUTOMATION-MEMORY-PALACE.md** | New skill or leave | — | Leave until skill exists. |
| **GITHUB-AS-MMORPG.md** | kernel or leave | — | Metaphor; leave. |
| **STANFORD-GENERATIVE-AGENTS-WELCOME.md** | ethics or leave | — | Leave. |
| **SIMS-ASTROLOGY.md** | sims-design-index (in designs) or needs/simulator-effect | — | Sims family; leave in designs/sims or ref from skill. |
| **MOO-HERITAGE.md**, **WELCOME-LAMBDAMOO.md** | kernel or leave | — | MOO lineage. |
| **iloci.md**, **iloci.yml** | kernel or leave | — | Leave. |
| **nellm.md** | leave | — | Archival. |
| **ANATOMY-OF-A-CENSORSHIP-CASCADE.md** | ethics or leave | — | Leave. |
| **constitution-design-summary.md** | kernel (constitution-core) | Ref only | — | Already in kernel. |
| **glance-mipmap-analysis.yml** | kernel or MOOPMAP | — | Data. |
| **designs/snitches/*** | skill-snitch | designs/snitches/ or catalog/ | catalog/ | Malware hunts; snitch catalog. |

### Design families → one or more skills (grouped)

| Family | Design docs | Target(s) | Strategy |
|--------|-------------|-----------|----------|
| **eval/** | EVAL-INCARNATE-FRAMEWORK, EVAL-INCARNATE-PHILOSOPHY, EVAL-VS-SIM, EVAL-TAXONOMY, THE-EVALS-DESIGN, EVALEYE, EVALSELF, EVALCITY, CHURCH-OF-THE-EVAL-GENIUS, EVAL-FACTIONS, EVAL-ARTIFACTS, EVAL-WORMS, EMOJI-ANCHORS, EVAL-DOM-SPEC, SCATS-DESIGN, SHORT-DURATION-PERSONAL-EVALUATORS, README | **eval** (one skill or family) | Create skills/eval/ with designs/ containing all; DESIGN.md = EVAL-INCARNATE-FRAMEWORK + index; plugins: templates/, examples/, designs/<game>.md. Optionally one skill per game (eval-self, eval-eye, eval-city). |
| **sims/** | sims-design-index, sims-maxis-requirements, sims-happy-friends-home, sims-will-wright-microworlds-1996, sims-find-best-action, sims-simantics-vm, sims-object-model, sims-personality-motives, sims-social-system, sims-room-spatial, sims-pie-menus, sims-astrology, sims-edith-editor, sims-time-events, sims-inclusivity, sims-queer-identity-formation, sims-team-history, sims-tiny-life, sims-animation-visuals, sims-portable-objects, simcity-multiplayer-micropolis, etc. | **No single skill**; kernel + multiple skills (needs, action-queue, room, character, economy, advertisement) | Keep designs/sims/ as **archival index**; extracted concepts already in PROTOCOLS, kernel, and skills. Option: skills/sims-archaeology/ with DESIGN.md = sims-design-index + refs to all; plugin: designs/<doc>.md. |
| **ethics/** | ANTHROPIC-SOUL, PALM-PHILOSOPHER-MONKEY, MIND-MIRROR-FOUNDATION, THE-VOID, GENERATIVE-AGENTS-SMALLVILLE, PARK-1000-PEOPLE, WANG-LIMITS, WILLER, BERTONCINI, SHANAHAN, DESAI, LAZAR, XIE, VALUE-PROMPTING-SCHWARTZ, HULLMAN, SYNTHETIC-PSYCHOPATHOLOGY, README, etc. | **ethics** (one skill or index) or leave in designs/ | Option: skills/ethics/ with designs/ = index + papers; CARD = methods (cite, compare, frame). Or leave as designs/ethics/ for reference. |
| **gastown/** | GASTOWN-VS-MOOLLM, YEGGE-ARC, MOOLLM-TASK-TRACKING, CONSTRUCTIONIST-TERMINOLOGY, BEADS-2026-01, BEAD-ORCHESTRATION.yml, README | **kernel** (critique, positioning) | Move to kernel/gastown/ or keep designs/gastown/; no skill. |
| **postscript/** | LINGUISTIC-MOTHERBOARD, BRIAN-REID-POSTSCRIPT-HISTORY | **kernel** or card skill | CARD.yml lineage; keep in designs/ or kernel. |
| **openclaw/** | CHARACTERS-AS-AGENTS, MMORPG-GATEWAY, INVASION-PLAN, A2UI-DEEP-DIVE, ARCHITECTURE-ANALYSIS, SECURITY-AUDIT, SKILL-BRIDGE, README | **External repo** (openclaw) or designs/ | Leave in designs/openclaw/; not MOOLLM skill. |
| **sim-obliterator/** | PSYCHOPOMP-AND-THE-BIFROST, BATTLE-PLAN, BRIDGE, IFF-LAYERS, THE-UPLIFT, README, *.yml | **External or sim-obliterator skill** | If skill exists in moollm, move designs into it; else leave. |
| **indexes/** | BACKSTORY-NARRATIVE, PROCEDURAL-RHETORIC-INDEX, CHARACTER-SIMULATION-INDEX, AI-ETHICS-INDEX, CONSTRUCTIONIST-INDEX, INDEX.md | **indexes/** (repo level) or kernel | Keep in designs/indexes/ or move to indexes/ at repo root; not a skill. |
| **pr/** | All PR-*.md session logs | **Leave in designs/pr/** | Archival; no skill. Link from skill READMEs where relevant. |
| **raw-chats/**, **email/** | Transcripts, correspondence | **Leave in designs/** | Archival. |
| **Connections & influences** | don-hopkins-projects, vanessa-freudenberg-philosophy, perverts-guide, postmodern-deconstruction, antirez-ai-hype, kaleida-scriptx-dreamscape | **Leave in designs/** or kernel refs | Archaeology; optional kernel “lineage” doc. |
| **MOOLLM-MANIFESTO.md**, **moollm-medium-post.md** | **moollm** (root or kernel) | README / docs at root; not a skill | Keep in designs/; root README links. |
| **MOOLLM-EVAL-INCARNATE-FRAMEWORK.md** | **kernel + eval** | Master doc; kernel or designs/eval/ | Central; duplicate ref in eval skill if created. |

---

## Suggested execution order

1. **skill-snitch** — Move skill-snitch-design.md and SKILL-SNITCH-EXTENSIBILITY into skill as DESIGN.md (and optionally designs/extensibility.md). Update CARD/GLANCE/SKILL/README from design. Leave pointer in designs/.
2. **cursor-mirror** — Move cursor-mirror-self-reflection (and any other loose cursor-mirror designs) into skills/cursor-mirror/designs/. Fix skill-snitch ref (SKILL-TEST-DESIGN → skill-test) if not already.
3. **eval** — Create skills/eval/ with DESIGN.md = EVAL-INCARNATE-FRAMEWORK + index; designs/ subdir with k-line filenames for each game/philosophy doc. CARD, GLANCE, SKILL, README from framework. Plugin: designs/<game>.md, templates/, examples/.
4. **sims** — Either create skills/sims-archaeology/ with DESIGN.md = sims-design-index and designs/ mirror of design tree, or keep designs/sims/ as-is and add “Sims archaeology” section in indexes/DESIGNS.md only.
5. **Kernel** — Move MOOLLM-PERMISSIONS-ARCHITECTURE, GIT-AS-FOUNDATION, NAMESPACING-SKILLS, MEMGPT-ANALYSIS (and other kernel-level) into kernel/ as docs; designs/ keeps copies or pointers.
6. **indexes/DESIGNS.md** — Update all entries that now point to skills (skill-snitch, skill-test, cursor-mirror, eval when done) and add “Design lives in skill” where applicable.

---

## Summary table: document => skill => parts

| Design (or group) | Skill | DESIGN.md | GLANCE | CARD | SKILL | README | Plugins |
|-------------------|-------|-----------|--------|------|-------|--------|---------|
| skill-snitch-design + EXTENSIBILITY | skill-snitch | ✓ full | ✓ | ✓ | ✓ | ✓ | patterns, surfaces, analyzers, templates, registry |
| SKILL-TEST-DESIGN | skill-test | pointer only in designs/ | ✓ | ✓ | ✓ | — | designs/runner, designs/cursor-mirror |
| cursor-mirror designs/* | cursor-mirror | ✓ | ✓ | ✓ | ✓ | ✓ | reference/assimilated, universal, reverse-engineered |
| eval/* | eval | ✓ framework + index | ✓ | ✓ | ✓ | ✓ | designs/<game>, templates, examples |
| sims/* | (none or sims-archaeology) | index in designs/ or skill | — | — | — | — | — or designs/<doc> |
| ethics/* | (none or ethics) | index in designs/ or skill | — | — | — | — | — |
| gastown/* | kernel | — | — | — | — | — | kernel/gastown or leave |
| MOOLLM-MANIFESTO, etc. | kernel / root | — | — | — | — | — | Leave designs/ |
| pr/*, raw-chats, email | — | — | — | — | — | — | Leave designs/ |

This plan is the single mapping; adjust as skills are created or designs are merged.
