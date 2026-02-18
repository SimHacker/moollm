# MOOLLM skill publishing policy and SKILL.md metadata standard

Skills will be published independently (zip of full skill dir or bare `SKILL.md`). We cannot control distribution, so we standardize for **self-containment**, **discoverability**, and **ecosystem links** so that humans and LLMs land in the human-readable README web.

**Applies to:** All MOOLLM skills. Remember in the **skill** (meta-skill) and when authoring or publishing any MOOLLM skill.

---

## 1. Policy: self-contained and ecosystem-aware

### 1.1 Self-contained as much as possible

- **SKILL.md** should be usable alone when someone has only that file. Include enough protocol, examples, and caveats in the body that the skill is actionable without CARD.yml or README.md.
- **Optional files** (CARD.yml, GLANCE.yml, README.md, scripts/, designs/, examples/) improve experience but are not guaranteed to be present when the skill is shared as a single file. Do not refer to "see CARD.yml" for critical behavior; either inline the relevant interface in SKILL.md or state "When CARD.yml is present, it defines …".
- **Point directly to this skill's directory root on GitHub.** In the standard blurb (below), include the **skill dir URL** (e.g. `https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror`). Then most any LLM can browse and fetch the entire skill directory over the web. Bob's your uncle: one link gives the crawler the full skill tree. The moollm repo URL and skills index URL need only be mentioned once in that same blurb.
- **Argument for linking to GitHub rather than embedding README:** When publishing minimal (e.g. bare SKILL.md), prefer linking to the skill dir on GitHub instead of inlining README. GitHub is **LLM-crawl-friendly**: an LLM can hit the skill dir and get a directory listing. Brutalist directory listings are still instructional — file and dir names are K-lines that tell their own story and invite browsing. Drill in and you get the pretty README with Mermaid, tables, and full context. So the blurb points to the skill dir; the crawler gets structure and names first, then content.
- **Cross-references** to other skills or repo paths should use the standard blurb (below) so that readers know where to find the full ecosystem.

### 1.2 Document and suggest related MOOLLM skills

- In **SKILL.md frontmatter**, set `related` (and optionally `benefits_from`) to skill ids. In the body, add a short "Related skills" or "Works well with" section that lists those skills and why they help.
- **related** — Skill ids this skill builds on or composes with (e.g. `[moollm, skill, k-lines, bootstrap]`).
- **benefits_from** (optional) — Skill ids that improve this skill's use, with one-line why (see metadata schema below).

### 1.3 Standard "part of MOOLLM" blurb

Every MOOLLM skill must include the following (in SKILL.md and, when present, README.md) so people and LLMs can find the framework and the full skill index. **Lead with this skill's directory root on GitHub** so any LLM can browse and fetch the entire skill dir over the web. Mention the moollm repo and skills index once; the critical link is the skill dir.

**Placement and the dog-butt sniffing protocol:** Start and end of a document get the most attention. So:

- **Start = glance understanding.** If the blurb (or a minimal version) is at the **start** (e.g. right after the first heading), the first sniff answers "what is this, where do I get the rest?" — identity and fetch-ability. Good for LLM crawl and quick scan.
- **End = full context and parting.** The **full** blurb at the **end** (before license/copyright) reinforces identity and gives all links to anyone who read through. Good for takeaway and copy-paste.

**Recommendation:** Use both. Minimal at start (one line: "Part of MOOLLM · [This skill's directory](url)."); full section at end. If you only do one: **start** when glance and crawl matter most; **end** when you don't want to distract from the protocol until the reader has seen it.

- **In SKILL.md:** Put the **full** "Part of MOOLLM" section at the **end** of the file (before any license/copyright). Optionally add a **minimal line at the start** (right after the main title/heading): e.g. `Part of MOOLLM · [This skill's directory](https://github.com/SimHacker/moollm/tree/main/skills/{skill-id})`.
- **In README.md:** Put the full blurb in a short section at the **bottom** (e.g. "Part of MOOLLM" or "Ecosystem"). Optionally add a one-liner at the top for glance.

**Blurb text:** Replace `{skill-id}` with this skill's directory name (e.g. `cursor-mirror`). Use `tree/main` for the skill dir so GitHub shows the directory listing (crawl-friendly).

```markdown
## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/{skill-id}/](https://github.com/SimHacker/moollm/tree/main/skills/{skill-id})

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
```

Example for `cursor-mirror`:

```markdown
## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/cursor-mirror/](https://github.com/SimHacker/moollm/tree/main/skills/cursor-mirror)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
```

From the skill dir URL, an LLM gets the full listing; file and dir names (K-lines) are instructional; drilling in yields README, CARD, SKILL, and the rest. When published as a single file or zip elsewhere, these GitHub URLs ensure the blurb still works.

---

## 2. Standard SKILL.md metadata format

We build on **Anthropic's skill model** and the **Agent Skills** convention (name + description in YAML frontmatter, markdown body). MOOLLM extends this with optional fields that support tooling, ecosystem linking, and publishing.

### 2.1 Core (Anthropic / Agent Skills compatible)

| Field | Required | Description |
|-------|----------|-------------|
| **name** | Yes | Skill identifier; lowercase-with-hyphens. Becomes slash-command in some runtimes. |
| **description** | Yes | One or two sentences. When to use and what it does. Helps agents decide when to load the skill. |

These two fields are sufficient for minimal, ecosystem-agnostic publishing (e.g. bare SKILL.md in the wild).

### 2.2 MOOLLM extension (optional but recommended)

**Standard or invented?** There is no known external standard for skill capability or tool allowlists. Anthropic Agent Skills use "Level 1/2/3" for *load order* (metadata → instructions → resources), not for what a skill can do. We standardize on **IAM-style MOOAM conventions**: **permissions** (field name **permissions**) and **allowed-tools** (which tool resources the skill may use). In IAM terms: a **principal** (here, a character or skill) is granted **permissions** on **resources**; we map resources to **tools**, **files**, **paths**, **URLs**, **MCP resources**, **terminal**, and **context**. So we spell it out: declare **permissions** and **allowed-tools**; tooling infers reach (read/write → files; terminal → terminal; none → prompt-only). Full model — principals, resources, permissions, grants, virtual tool names, permission catalogue, enforcement — is in **[designs/MOOAM.md](./MOOAM.md)** (may later become a MOOAM skill with a mooam-manager).

| Field | Required | Description |
|-------|----------|-------------|
| **allowed-tools** | Recommended | List of tool names the skill may use. Prefer **virtual tool names** (see below) for cross-orchestrator skills; orchestrators map virtual → real. Otherwise runtime-specific names (e.g. Cursor `read_file`, `run_terminal_cmd`). Enables containment and snitch checks. |
| **permissions** | Recommended | List of permissions (read, write, files, terminal, youtube, ambient, code, history, wizard). Expresses what the skill can do; reach is inferred (files/read/write → files; terminal → terminal). Postel: accept legacy **reach** or **tier** and map to permissions (e.g. tier 0 → []; tier 1 → [files] or [read, write]; tier 2 → [files, terminal]). |
| **related** | Recommended | List of MOOLLM skill ids this skill builds on or composes with. |

**Postel (consumers):** Accept liberal input. **permissions:** accept list of strings (read, write, files, terminal, youtube, ambient, code, history, wizard; alias execute → terminal, admin or cow → wizard; files = read + write); or accept legacy **reach** / **tier** and map to permissions; omit = infer from allowed-tools. **allowed-tools:** accept list of strings; unknown names are runtime-specific. **Emit:** canonical form (list of tool names, list **permissions**; may expand files → read, write). Full catalogue: [designs/MOOAM.md](./MOOAM.md).

| **benefits_from** | Optional | List of `{ skill: "<id>", why: "<one line>" }` for skills that improve use. |
| **license** | Optional | e.g. `MIT`. |
| **tags** | Optional | e.g. `[moollm, meta, anthropic]`. |
| **credits** | Optional | Attribution (people, papers, Anthropic). |

### 2.2b MOOLLM compatibility and what the skill respects (optional)

Skills can declare that they are **MOOLLM-compatible** and which **skills**, **protocols**, and **concepts** they respect, support, consume, or compose with. These declarations can act as **K-line activators** in any orchestrator that implements MOOLLM patterns: they drive which related skills, knowledge, and examples get loaded (e.g. GLANCE → CARD → SKILL → examples) incrementally and on demand.

| Field | Required | Description |
|-------|----------|-------------|
| **moollm_compatible** | Optional | `true` if this skill follows MOOLLM conventions (pyramid, anatomy, publishing blurb, metadata). Enables "MOOLLM-compatible" filtering and K-line diffusion. |
| **respects** | Optional | List of **skill ids** and/or **concept K-lines** this skill respects (follows their conventions or defers to them). |
| **supports** | Optional | List of skill ids or concept K-lines this skill explicitly supports (implements or enables). |
| **consumes** | Optional | List of skill ids or concept K-lines this skill consumes (reads, depends on, or expects). |
| **composes_with** | Optional | List of skill ids or concept K-lines this skill composes with (combines in workflows). |

**Concept K-lines** (general conventions, not just skill ids) — use these so orchestrators can activate the right knowledge and examples:

- **postel** — Robustness principle (liberal in, conservative out).
- **yaml-jazz** — Semantic YAML; comments as data; three audiences (humans, LLMs, machines).
- **uri**, **path**, **github** — URI/path/GitHub conventions (resolving, linking, repo structure).
- **ambient** — Always-on behavioral shaping; ambient skills.
- **speed-of-light** — Many turns in one call; minimal tokenization.
- **plugins** — Plugin surfaces (templates, examples, patterns, analyzers); extensibility.
- **empathic** — Empathic templates, expressions; intent-based interpretation.

Example: a skill that generates YAML and follows Postel can set `respects: [yaml-jazz, postel]` and `composes_with: [room, character]`. An MOOLLM-aware orchestrator can use that to incrementally warm the yaml-jazz and postel K-lines (and their GLANCE/CARD/SKILL/examples) as needed.

### 2.3 Publishing and ecosystem (optional)

| Field | Required | Description |
|-------|----------|-------------|
| **moollm** | Optional | Object for MOOLLM-specific publishing. |
| **moollm.ecosystem** | Optional | `true` if this skill is part of the official MOOLLM skills set. |
| **moollm.repo_readme** | Optional | URL or path to repo top-level README (default: use standard blurb link). |
| **moollm.skills_readme** | Optional | URL or path to skills directory README (default: use standard blurb link). |
| **moollm.self_contained_guidance** | Optional | Short note for publishers: "This skill is self-contained; CARD.yml and README add interface and examples." |

### 2.4 Example: minimal (bare SKILL.md, anywhere)

```yaml
---
name: my-skill
description: "Does X when you need Y. Use when Z."
---
```

### 2.5 Example: full MOOLLM (in-repo or zip)

```yaml
---
name: cursor-mirror
description: "Introspect Cursor session state: chats, tool calls, context assembly. Use when reviewing past chats or debugging agent behavior."
allowed-tools: [read_file, run_terminal_cmd, grep]
permissions: [read, terminal]
related: [moollm, skill, bootstrap, play-learn-lift, skill-snitch]
benefits_from:
  - skill: skill-snitch
    why: "Audit skill security and declared vs actual tool use."
  - skill: bootstrap
    why: "Cursor driver and hot.yml inform what to introspect."
moollm_compatible: true
respects: [yaml-jazz, postel, path]
supports: [play-learn-lift]
consumes: [bootstrap]
composes_with: [skill-snitch, bootstrap]
license: MIT
tags: [moollm, introspection, utility, cursor]
credits:
  - "Anthropic — Skills model foundation"
  - "Don Hopkins, Leela AI — cursor-mirror"
moollm:
  ecosystem: true
  self_contained_guidance: "SKILL.md is usable alone; CARD.yml and scripts/ add interface and CLI."
---

# Cursor Mirror
...
```

### 2.6 Compatibility

- **Anthropic / Agent Skills:** Consumers that only read `name` and `description` get a valid skill.
- **MOOLLM tooling:** INDEX.yml, CARD.yml, skill-snitch, and bootstrap can use `permissions`, `allowed-tools`, `related`, `moollm`, and declaration fields (`moollm_compatible`, `respects`, `supports`, `consumes`, `composes_with`) when present. Any orchestrator that implements MOOLLM patterns can use declarations for K-line diffusion and incremental activation of GLANCE/CARD/SKILL/examples.
- **Standalone:** A single SKILL.md with name, description, and a self-contained protocol body works without the rest of the repo.

---

## 3. Where this is documented and enforced

| Location | What |
|----------|------|
| **designs/SKILL-PUBLISHING-POLICY.md** | This document (metadata, declarations, concept K-lines). |
| **designs/MOOAM.md** | Full MOOAM model (permissions, objects, virtual tools, enforcement). |
| **designs/SKILLS-CONSTITUTION-AND-PLAN.md** | Declarations, concept K-lines, K-line diffusion and on-demand activation in MOOCO. |
| **skills/skill/SKILL.md** | Meta-skill: references this policy and the metadata standard. |
| **skills/skill/SKILL.md.tmpl**, **README.md.tmpl** | Templates include frontmatter, declaration hints, and Part-of-MOOLLM blurb. |
| **skills/README.md** | Skill anatomy and "required files" can reference this policy. |
| **.cursorrules** (moollm) | Rule: MOOLLM skills must be self-contained, document related skills, include Part-of-MOOLLM blurb; use standard SKILL.md metadata. |
| **designs/DESIGN-TO-SKILL-MAPPING.md** | Pointer to this policy when creating or publishing skills. |

---

## 4. Summary

- **Self-contained:** SKILL.md works alone; do not rely on CARD/README for critical behavior.
- **Related skills:** Document and suggest related/benefits_from; add a short section in the body.
- **Ecosystem blurb:** Every skill includes the standard "Part of MOOLLM" section with links to repo README and skills README.
- **Metadata:** Core = name + description (Anthropic-compatible). Extension = allowed-tools, permissions, related, benefits_from, license, tags, credits, moollm (optional). Full MOOAM: [designs/MOOAM.md](./MOOAM.md).
- **Publish as:** Full skill dir (zip) or bare SKILL.md; the standard makes both usable and points readers into the human-readable README web.
