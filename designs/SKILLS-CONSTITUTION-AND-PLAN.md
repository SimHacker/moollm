# MOOLLM skills: constitution and continuing plan

A living document — the **constitution** of MOOLLM skills (principles, extensions, conventions) and the **continuing plan** (what we do, why, and what it enables). Skills are the primary unit of capability and convention in MOOLLM; this doc anchors them.

**See also:** [EVAL-INCARNATE-FRAMEWORK.md](./eval/EVAL-INCARNATE-FRAMEWORK.md) (full thesis), [skills/README.md](../skills/README.md) (index and anatomy), [SKILL-PUBLISHING-POLICY.md](./SKILL-PUBLISHING-POLICY.md) (publishing and metadata), [DESIGN-TO-SKILL-MAPPING.md](./DESIGN-TO-SKILL-MAPPING.md) (design → skill migration).

---

## 1. Core thesis

**Skills are conventions the model follows, not code the orchestrator runs.** Userland protocols over files.

- **Skills are programs.** The LLM is `eval()`. Documentation that learned to do things.
- **Anthropic foundation.** We extend [Anthropic's skill model](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-library) and the [Agent Skills](https://agentskills.io/) convention. We do not replace them; every Anthropic-compatible skill works in MOOLLM. Our extensions are additive.
- **Empathy is the interface.** Files and names are the API. The LLM interprets them; we design for that.

---

## 2. Eight extensions (and growing)

MOOLLM extends the base skill model with eight architectural innovations. Each has a **why** and **what it enables**.

| # | Extension | What it adds | Why | What it enables |
|---|-----------|--------------|-----|-----------------|
| 1 | **Instantiation** | Skills as prototypes that create instances. Not just prompts — living programs. | State and behavior separate; instances inherit from prototypes; one skill, many worlds. | Adventures, characters, rooms that persist and evolve; templates that generate real state. |
| 2 | **Multi-tier persistence** | Platform (ephemeral) → Narrative (append) → State (edit) → MOO-Maps (GLANCE/CARD/SKILL/README/examples/templates). | Different durability and mutability for different kinds of truth. | Long session logs, editable room state, inspectable skill interfaces, append-only audit. |
| 3 | **K-lines** | Names as semantic activation vectors (Minsky). A name wakes a constellation of meaning. | Cognition is associative; names are handles for clusters of knowledge and behavior. | "Palm" activates soul, history, relationships; directory listing as advertisement; big-endian naming. |
| 4 | **Empathic templates** | Smart generation from intent and context, not string substitution. | LLMs understand meaning; templates can be expressed in natural language and traits. | Character descriptions from traits; room descriptions from exits and objects; doc-first automation. |
| 5 | **Speed of light** | Many turns in one call, minimal tokenization. | Latency and round-trips are the real cost; one call can embody a full interaction. | 33-turn Fluxx, 21-turn cat prowl; instant telepathy; simulation without chat ping-pong. |
| 6 | **CARD.yml** | Machine-readable interface: methods, tools, state schema, advertisements. | Orchestrators and tools need to know what a skill can do without reading prose. | Containment (allowed-tools), snitch (declared vs actual), discovery, plugin surfaces. |
| 7 | **Ethical framing** | Room-based inheritance of performance context (framing, boundaries). | Ethics and tone should flow from place and context, not be bolted on. | Stage vs backstage; counters, walls, tardis patterns; representation and tribute protocols. |
| 8 | **Ambient skills** | Always-on behavioral shaping (no-AI hygiene suite). | Some constraints should apply to every turn without explicit invocation. | no-ai-slop, no-ai-gloss, no-ai-sycophancy, no-ai-hedging, no-ai-moralizing, postel, robust-first, yaml-jazz. |

**And growing.** Further extensions and conventions are part of the same constitution:

- **GLANCE.yml** — Smallest resolution of the semantic image pyramid; "is this relevant?" in one screen. Complements CARD (interface) and SKILL (protocol). Friendly; LLMs love to see them.
- **Skill-snitch** — Declared vs actual: compare CARD and SKILL and README to observed tool use and transcripts. Security audit, body-and-spirit, play-learn-lift.
- **Skill-test** — Validation and runner design per skill; cursor-mirror as test surface. Skills must be testable **naked**: outside the moollm repo and outside their normal directory (e.g. bare SKILL.md or skill dir in a temp location). Tests run in isolation so skills are reproducible and portable.
- **Publishing policy** — Self-contained SKILL.md, related skills documented, standard "Part of MOOLLM" blurb, metadata compatible with Anthropic/Agent Skills. Skills can be shared as zip or bare file and still point readers into the ecosystem. Publishing implies **naked testability**: the skill works when run outside moollm and outside its home dir.
- **Plugin surfaces** — Templates, examples, designs, reference, patterns, analyzers. Standard and ad hoc extension points so skills can grow without exploding the core.

The **why** is consistent: make skills **inspectable**, **composable**, **safe to run**, and **portable**, while keeping the human-readable README web as the primary map.

---

## 3. Conventions

### 3.1 Semantic image pyramid (reading order)

Never load a lower resolution without loading the one above. Order:

1. **GLANCE** (INDEX entry or GLANCE.yml) — "Is this relevant?" (~5–70 lines)
2. **CARD.yml** — "What can it do?" Interface, methods, ads (~50–200 lines)
3. **SKILL.md** — "How does it work?" Protocol, examples (~200–1000 lines)
4. **README.md** and resources — "Why was it built?" Deep context (500+ lines)

This convention minimizes token use and keeps agents and humans oriented.

### 3.2 Skill anatomy

Skills are **typically directories** but can take other forms: a single YAML or MD file; a skill developed inside its design document (like a notebook); or content spread across multiple files or dirs using **big-endian naming** and grouping conventions. Whatever the form, the same pyramid and interface ideas apply.

Every skill has:

- **README.md** — Human landing page; GitHub renders it. Discovery and navigation.
- **SKILL.md** — Full protocol and YAML frontmatter (name, description, allowed-tools, permissions, related, etc.). Execution and publishing.
- **CARD.yml** — Machine-readable interface: methods, tools, state, advertisements. Containment and tooling.
- **GLANCE.yml** — **Extremely highly recommended** unless it's obvious from context and directory listing (e.g. non-MOOLLM repos, other sub-trees not MOOLLM objects, or differently named summary files / generated descriptions). When in doubt, add one: GLANCEs are friendly — LLMs love to see them. Smallest resolution, "is this relevant?" in one screen. Complements CARD (interface) and SKILL (protocol). Single-file or notebook-style skills can embed a glance section or equivalent.

Optional: templates, scripts, designs/, examples/, reference/. See [skills/README.md](../skills/README.md) and [skill/SKILL.md](../skills/skill/SKILL.md).

### 3.3 Publishing

Skills may be published independently (zip of skill dir or bare SKILL.md). Conventions:

- **Self-contained** — SKILL.md must be usable alone; do not rely on CARD/README for critical behavior. Implies **naked testability**: the skill must run and validate outside the moollm repo and outside its home directory (e.g. in a temp dir with only the skill file or a copy of the skill dir).
- **Related skills** — Document `related` and optional `benefits_from`; add a short "Works well with" section.
- **Part of MOOLLM** — Include the standard blurb with links to repo README and skills/README so humans and LLMs land in the ecosystem.
- **Metadata** — Core: `name`, `description` (Anthropic-compatible). Extension: `permissions`, `allowed-tools`, `related`, `license`, `tags`, `credits`, optional `moollm`.

Full policy: [SKILL-PUBLISHING-POLICY.md](./SKILL-PUBLISHING-POLICY.md).

### 3.4 Permissions (MOOAM)

Permissions follow **MOOAM** (MOO Access Management), aligned with IAM: declare **allowed-tools** and **permissions** in frontmatter and CARD; reach is inferred from permissions. Containment and snitch use these declarations to enforce who can do what. Full model (principals, resources, permissions, grants, virtual tools, catalogue, enforcement): **[designs/MOOAM.md](./MOOAM.md)**.

### 3.5 MOOLLM compatibility and what the skill declares

Skills can declare that they are **MOOLLM-compatible** and which **skills**, **protocols**, and **concepts** they respect, support, consume, or compose with. Beyond direct compatibility with specific skills, there are **general concept K-lines** — postel, yaml-jazz, uri/path/github, ambient, speed-of-light, plugins, empathic — that name conventions and bodies of knowledge. Declaring them lets orchestrators (e.g. MOOCO) activate the right context.

| Declaration | Meaning |
|-------------|---------|
| **moollm_compatible** | This skill follows MOOLLM conventions (pyramid, anatomy, blurb, metadata). |
| **respects** | Skill ids or concept K-lines this skill follows or defers to. |
| **supports** | Skill ids or concepts this skill implements or enables. |
| **consumes** | Skill ids or concepts this skill depends on or reads. |
| **composes_with** | Skill ids or concepts this skill combines with in workflows. |

**Concept K-lines** (canonical names for conventions): `postel`, `yaml-jazz`, `uri`, `path`, `github`, `ambient`, `speed-of-light`, `plugins`, `empathic`. See [SKILL-PUBLISHING-POLICY.md](./SKILL-PUBLISHING-POLICY.md) for the full list and metadata format.

**In an MOOLLM-aware orchestrator** these declarations can **activate K-lines** and pull in related skills, knowledge, and examples. **K-line diffusion** (incrementally activating GLANCE → CARD → SKILL → examples on demand) is an aspiration for such runtimes. So a skill that declares `respects: [yaml-jazz, postel]` and `composes_with: [room]` gives any orchestrator that implements MOOLLM patterns a signal to warm the yaml-jazz and postel concepts and the room skill to the resolution needed. Declarations are the wiring for context gathering.

---

## 4. What this enables

- **Living instances** — Adventures, characters, rooms that persist and evolve. Skills are factories; instances are the output.
- **Play–learn–lift** — Explore, extract patterns, share wisdom. Session logs and protocol traces become the material for learning and skillification.
- **Audit and safety** — Declared tools (CARD) vs observed (transcript). Snitch, deep-snitch, and containment boundaries. Skills can be audited before and after use.
- **Portable skills** — Publish as zip or bare SKILL.md; standard metadata and blurb keep the skill findable and the ecosystem one click away.
- **Multi-resolution consumption** — Agents read GLANCE → CARD → SKILL as needed; humans read README and explore. Same skill, multiple audiences.
- **Ambient behavior** — Hygiene and robustness apply to every turn without explicit invocation. The constitution is always on.
- **K-line diffusion and on-demand activation** — Skills declare what they respect, support, consume, and compose with (skills and concepts). An orchestrator that implements MOOLLM patterns can use these declarations to activate K-lines and related skills/knowledge/examples and incrementally load GLANCE → CARD → SKILL → examples as appropriate.

---

## 5. Why an orchestrator (direction, not promise)

This constitution and plan describe what **an orchestrator that implements MOOLLM patterns** could do: host skills, respect CARD interfaces and declarations, enforce containment, and optionally watch/act (e.g. cursor-mirror, tool gating, declared-vs-observed checks). We design for that *direction* — rooms, characters, skills, K-lines, stream-machine–style infrastructure, tool-executor, provider abstraction — without committing this repo to building or shipping any specific product.

**What such an orchestrator could do with this:**

- **Host MOOLLM skills** — Load skills from a registry; respect CARD interfaces, permissions, and allowed-tools. Enforce containment so each skill only sees the tools it declares.
- **Tool gating and policy** — Before execution, check dangerous/confirmRequired and skill declarations; block, confirm, or scriptify suspicious commands. Use skill-snitch (declared vs actual) as input to policy.
- **Editor integration** — Read editor/session state (e.g. cursor-mirror, state.vscdb) and, where applicable, act through the same auth. Editor as UI; orchestrator as the layer that can watch, gate, and augment.

**In-the-middle** (proxy / protocol interpreter / editor / injector) is the longer-term *aspiration*: sit between the user and the world; watch the same stream the user sees; build a running mental model of skills, intention, and tool use; diff declared vs actual; optionally block or confirm risky commands and scriptify them into artifacts. That kind of design is the **reason** we care about skill declarations, containment, and protocol traces in this repo. CARD and SKILL state what a skill is allowed to do; cursor-mirror and skill-snitch provide the observed stream; an orchestrator (wherever it is implemented) can interpret, edit, and inject in the middle when the architecture allows.

We do not promise any specific orchestrator, feature, or timeline from this repo. We state that **this is the direction we design for** — so that skills, declarations, and traces are ready when and where such an orchestrator is built.

---

## 6. Summary

| Pillar | Content |
|--------|---------|
| **Thesis** | Skills are programs; LLM is eval(); Anthropic-compatible extensions. |
| **Eight + growing** | Instantiation, persistence, K-lines, empathic templates, speed of light, CARD, ethical framing, ambient; plus GLANCE, snitch, skill-test (naked: outside repo and dir), publishing (naked testability), plugin surfaces. |
| **Conventions** | Pyramid reading order; anatomy (README/SKILL/CARD/GLANCE — GLANCE extremely highly recommended unless reason not to, e.g. non-MOOLLM trees or directory listings enough); skills typically dirs but can be single file, design-doc notebook, or multi-file/dir with big-endian naming; publishing (self-contained, blurb, metadata); permissions and allowed-tools (MOOAM); declarations (moollm_compatible, respects/supports/consumes/composes_with for skills and concept K-lines). |
| **Concept K-lines** | postel, yaml-jazz, uri, path, github, ambient, speed-of-light, plugins, empathic — general conventions skills can declare they respect/support/consume/compose with. |
| **Enables** | Living instances, play-learn-lift, audit, portable skills, multi-resolution use, ambient behavior; K-line diffusion and on-demand activation in any MOOLLM-aware orchestrator. |
| **Why an orchestrator** | Host skills, enforce containment, gate tools; declarations activate K-lines and related knowledge/examples; in-the-middle proxy / protocol interpreter / editor / injector as the direction we design for. |

This document is the **continuing plan and constitution** of MOOLLM skills. Update it as the extension set and conventions evolve.
