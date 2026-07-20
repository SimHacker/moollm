# How and Why MOOLLM Skills Build On — and Extend — Anthropic Agent Skills

> Companion to [SKILL-PUBLISHING-POLICY.md](./SKILL-PUBLISHING-POLICY.md) (the normative metadata standard),
> [anthropic-skill-upgrades.md](./anthropic-skill-upgrades.md) (the upgrade catalog), and
> [anthropic-import-plan.md](./anthropic-import-plan.md) (the import strategy).
> This document is the explainer: the rationale and the extension inventory in one place.

## The foundation: Anthropic's skill model

Anthropic's Agent Skills convention is deliberately minimal: a skill is a
directory containing a `SKILL.md` file with YAML frontmatter (`name` +
`description`) and a markdown body of instructions, optionally accompanied by
`scripts/` (executable), `references/` (context), and `assets/` (output
templates). Loading is progressive: an agent first sees only the metadata,
loads the instructions when the description matches the task, and pulls in
resources on demand. It's a clean, ecosystem-agnostic packaging format for
procedural knowledge.

MOOLLM treats that model as its ABI. Every MOOLLM skill *is* a valid Anthropic
skill: a consumer that only reads `name` and `description` gets a working
skill and can ignore everything else. This is Postel's Law applied to skill
publishing — emit conservative (a strictly conforming SKILL.md), accept
liberal (any orchestrator, from Claude to Cursor to a bare LLM with a file
reader, can consume it).

## Why extend rather than invent

1. **Compatibility is distribution.** Skills get shared as zips, gists, and
   bare SKILL.md files pasted into chats. MOOLLM can't control where its
   skills land, so it standardizes on the format every runtime already
   understands, and layers its extensions as *optional* frontmatter fields
   that unknown consumers safely ignore.
2. **Lean into the training data.** Anthropic's format is in every modern
   model's latent space. Pointing at it ("this is a SKILL.md") activates
   prepaid knowledge; a novel format would be a cache miss billed on every
   call.
3. **Anthropic solved packaging, not ecosystem.** Vanilla skills are
   standalone: they don't know about each other, can't inherit, can't
   compose, carry no security declarations, and have no discovery mechanism
   beyond a description string. MOOLLM's extensions address exactly those
   gaps — everything Anthropic left out because it wasn't packaging's job.

## The frontmatter extensions (~10 and growing)

Core (Anthropic-compatible): `name`, `description`. Everything below is
optional and degrades gracefully. Normative definitions live in
[SKILL-PUBLISHING-POLICY.md](./SKILL-PUBLISHING-POLICY.md); the permission
model lives in [MOOAM.md](./MOOAM.md).

| # | Field | What it adds | Why |
|---|-------|-------------|-----|
| 1 | `allowed-tools` | Tool allowlist (virtual or runtime-specific names) | Containment; skill-snitch can check declared vs. actual tool use |
| 2 | `permissions` | IAM-style grants (read, write, files, terminal, youtube, ambient, code, history, wizard) per the MOOAM model | Security posture is declared, not inferred; principals get permissions on resources |
| 3 | `related` | Skill ids this skill builds on or composes with | Ecosystem linking; a skill arrives knowing its neighbors |
| 4 | `benefits_from` | `{skill, why}` pairs for skills that improve this one | Soft dependencies with rationale, not hard requirements |
| 5 | `moollm_compatible` | Declares the skill follows MOOLLM conventions | Enables filtering and K-line diffusion in aware orchestrators |
| 6 | `respects` | Skill ids or concept K-lines whose conventions it defers to (postel, yaml-jazz, uri, ambient…) | Activates the right background knowledge on load |
| 7 | `supports` | K-lines it implements or enables | Capability advertisement |
| 8 | `consumes` | K-lines it reads or depends on | Dependency declaration for incremental loading |
| 9 | `composes_with` | K-lines it combines with in workflows | Composition hints (e.g. `[room, character]`) |
| 10 | `license` | e.g. MIT | Publishing hygiene |
| 11 | `tags` | Classification | Discovery |
| 12 | `credits` | Attribution (people, papers, Anthropic itself) | Provenance |
| 13 | `moollm` | Publishing object: `ecosystem`, readme pointers, self-containment guidance | Wayfinding when the skill travels alone |

The declaration fields (5–9) are the most interesting: they're **K-line
activators**. A skill that says `respects: [yaml-jazz, postel]` isn't just
documenting itself — in a MOOLLM-aware orchestrator, that line triggers
incremental warming of the yaml-jazz and postel knowledge (their
GLANCE/CARD/SKILL/examples) on demand. Metadata becomes a loading protocol.

## Beyond frontmatter: structural and runtime extensions

The frontmatter is the visible edge. The deeper extensions change what a
skill *is*:

- **Semantic Image Pyramid.** Anthropic's progressive disclosure has three
  levels (metadata → instructions → resources). MOOLLM formalizes four
  human-and-LLM-readable resolutions: `GLANCE.yml` (5–70 lines, "is this
  relevant?") → `CARD.yml` (interface sniff) → `SKILL.md` (protocol) →
  `README.md` (deep context). Rule: never load a lower level without the one
  above. Context is a budget; the pyramid is its accounting system.
- **Self-containment policy.** Because distribution is uncontrollable,
  SKILL.md must be actionable alone — critical behavior lives in the body,
  never "see CARD.yml." Optional files enhance; they never gate.
- **The "Part of MOOLLM" blurb.** Every skill carries a link to its own
  GitHub directory, so a bare file in the wild is one URL away from its full
  tree. GitHub directory listings are LLM-crawl-friendly: filenames are
  K-lines, the listing is the advertisement index.
- **Prototype inheritance.** Anthropic skills are copy-paste standalone;
  MOOLLM skills clone from parents and override what differs (the `skill`
  meta-skill is the root prototype, not a tutorial — it's the runtime).
- **Mounting, buffs, advertisements.** Skills attach to characters and rooms
  (GRANT abilities, AFFLICT constraints), carry temporary modifications, and
  broadcast scored relevance so the right skill surfaces at the right time —
  instead of relying on a description string matching a prompt.
- **Ambient skills.** A trust tier Anthropic doesn't have: always-on
  behavioral constraints (the no-ai-* hygiene suite, postel, robust-first,
  yaml-jazz, copy-that) that live in context rent-free rather than loading
  per-task.
- **skill-snitch.** Security auditing that checks a skill's declared
  `permissions`/`allowed-tools` against its actual behavior — the
  declarations above are what make this check possible.

## The upshot

Anthropic defined a file format; MOOLLM builds a society on top of it. The
extensions convert standalone instruction documents into ecosystem citizens
that declare their permissions, know their relatives, inherit from
prototypes, mount onto characters and rooms, activate each other's knowledge
through K-lines, and remain — down to the last one — valid vanilla skills
that any Agent Skills consumer can pick up and run. Compatibility outward,
composition inward. That's the whole trick.

## See also

| Document | Role |
|----------|------|
| [SKILL-PUBLISHING-POLICY.md](./SKILL-PUBLISHING-POLICY.md) | Normative metadata standard and publishing rules |
| [MOOAM.md](./MOOAM.md) | Full permission model: principals, resources, grants, virtual tools |
| [anthropic-skill-upgrades.md](./anthropic-skill-upgrades.md) | Catalog: applying MOOLLM extensions to Anthropic's own skills |
| [anthropic-import-plan.md](./anthropic-import-plan.md) | Import strategy for Anthropic's skill library |
| [SKILLS-CONSTITUTION-AND-PLAN.md](./SKILLS-CONSTITUTION-AND-PLAN.md) | Declarations, concept K-lines, diffusion in MOOCO |
| [skills/skill/SKILL.md](../skills/skill/SKILL.md) | The meta-skill that enforces all of this |
