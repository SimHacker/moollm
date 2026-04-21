# 🍲 META-PLAN — self-replicating cauldron

> *"The first thing you brew in a cauldron is another cauldron. The first thing you 3D-xerox is a 3D-xerox. Just don't leave your thumb on the scanner plate."*

This file is deliberately recursive. It describes how to brew a cauldron skill, using a cauldron, about brewing cauldrons. It is also mutable: every new brew is encouraged to revise this file in its own repo. Inheritance with mutation — the selfish pattern.

The **discipline** replicates. The **content** doesn't. See the [Thumb Principle](#2-the-thumb-principle) below.

---

## 0. Epigraph

RepRap machines — the original self-replicating 3D printers — can print most of their own parts. They can't print the electronics, the stepper motors, the PTFE tubing. They can't print the craftsman who calibrates them. A RepRap is *mostly* self-replicating, which is the honest version of *entirely* self-replicating.

A cauldron is the same. It replicates its **discipline** — the two phases, the numbered sections, the empathic-templates, the bidirectional navigation, the grep-anchored claims, the reserved Appendix B, the MELT/STIR/LADLE/ANCHOR/LINK/TASTE/SERVE cadence. It does not replicate **content** — the specific plan, the specific code, the specific operators, the specific environment.

It also does not replicate the brewer's **thumb** — the accidental proprietary detail that rides along unnoticed. That's what [trekify](../trekify/) is for, and why SERVE optionally invokes it.

---

## 1. The self-replication principle

The first thing cauldron was used to brew was another cauldron. Specifically: the very [skill you're reading now](CARD.yml) was produced by following the cauldron discipline, informally, *before cauldron existed as a named skill*.

This was the hand-compiled, bootstrap cauldron:

1. A real project's docs accumulated over 30+ conversational turns (`leela-ai/central/docs/CONFIGURATION-FLAGS-PLAN.md`, 1917 lines).
2. A Phase-2 tree was produced by one single user turn ("now break it up").
3. The process was observed, named, and generalized into a pattern (`central/docs/configuration/META-PLAN.md`, 263 lines).
4. That pattern was lifted into a MOOLLM skill (`moollm/skills/cauldron/`).
5. This META-PLAN — the one you are reading — is the *skill's own retrospective* on that origin, separate from but dual to the project's.

So there are two META-PLANs by design:

| File | What it describes | Perspective |
|---|---|---|
| `central/docs/configuration/META-PLAN.md` | How the *specific* configuration-flags plan was cooked. | Inside one brew. Project-facing. |
| `moollm/skills/cauldron/META-PLAN.md` (this file) | How *the skill* was brewed, and how future brews should proceed. | Across brews. Skill-facing. |

They reference each other. Together they embody the self-replication: the project's META-PLAN is a brew that produced the skill's META-PLAN, which prescribes how to produce more project META-PLANs.

---

## 1.5. Super-meta-plans — self-awareness, Ungar-style

> *"Everything is an object. Objects have slots. Slots hold data OR behavior."* — Dave Ungar, *Self: The Power of Simplicity* (quoted in [`moollm/skills/object/SKILL.md`](../object/SKILL.md))

Dave Ungar's [Self](https://en.wikipedia.org/wiki/Self_(programming_language)) taught a generation of language designers that **self-awareness is cheap when you reify what's there and nothing more**. An object that wants to refer to its prototype puts a `parent*` slot in itself. An object that doesn't want a parent simply doesn't. Inheritance is *a slot*, not an ontological requirement. Self-without-parent is a first-class citizen; classy-OO's demand that every object descend from `Object` is exactly the rigidity Ungar rejected.

MOOLLM's [`object` skill](../object/) encodes this directly: its schema lists `id`, `name`, `description` as **required**, but `inherits:` lives in the **optional** fields. A cauldron brew is an object; a skill is an object; a kernel principle is an object. Any of them can choose a parent. Any of them can stand alone. The parent is wired when wiring serves; elided when eliding serves.

So cauldron's "self-awareness" isn't a ladder everyone must climb. It's a constellation of META-PLANs, each standing on its own, some referencing others when useful. You look at any brew and find whatever genesis documentation its author(s) chose to reify. No more, no less.

### The constellation as it stands today

| Reified META-PLAN | Artifact it reflects on | Audience | Status |
|---|---|---|---|
| [`central/docs/configuration/META-PLAN.md`](../../../central/docs/configuration/META-PLAN.md) | One specific brew (`central/docs/configuration/`) | Executors working this project's PRs | exists |
| [`this file`](META-PLAN.md) | The cauldron skill itself | Anyone brewing *any* cross-cutting plan | exists |
| *(level-2 wisdom)* | The pattern of meta-orchestrator skills (cauldron, debate, plan-then-execute, play-learn-lift) | Anyone authoring a new meta-orchestrator | **not reified** — no file yet, and that's fine |
| *(level-3 philosophy)* | MOOLLM as a whole | Kernel maintainers | **partially reified** in `kernel/*.md` |
| *(level-4 prior art)* | Minsky, Papert, Ungar, Drescher, Wright | Anyone asking *why* MOOLLM looks how it does | **intentionally never reified** — it's the ground, not an artifact |

No file is missing. Each META-PLAN that exists, exists because someone had something to say at that level. The absences aren't gaps; they're the natural state. Reify when the perspective is genuinely different and there's genuinely something to preserve. Otherwise leave the slot blank and let the constellation stand as it is.

### Optionality, multiplicity, and latent-space parents

MOOLLM already implements all of this; I don't need to redescribe it. Canonical treatments:

- [`kernel/DIRECTORY-AS-OBJECT.md`](../../kernel/DIRECTORY-AS-OBJECT.md) — filesystem IS the object graph; `parents:` list as a first-class slot; cites the [Densmore-Rosenthal patent (US5187786A, 1991)](https://patents.google.com/patent/US5187786A/en) as proof the shape works.
- [`skills/prototype/SKILL.md`](../prototype/SKILL.md) — Self-style delegation; **ordered, multiple parents** via `PROTOTYPES.yml`; first-match-wins; *"Self is one of this skill's prototypes."*
- [`skills/schema/schemas/mechanisms/self/MECHANISM.yml`](../schema/schemas/mechanisms/self/MECHANISM.yml) — names `PROTOTYPES.yml multiple parents` as the standards anchor.

So a cauldron brew is just an object in MOOLLM's existing sense. The interesting part isn't recapitulating the mechanism — it's what you put **in** the `parents:` list. Three kinds of entries are all valid:

```yaml
# Inside a cauldron brew, or the cauldron skill itself:
parents:
  - ../../skills/cauldron                  # concrete path — follow the file
  - ../../skills/object                    # concrete path — follow the file
  - skills/empathic-templates              # concrete path — follow the file
  - "Self prototypal inheritance model"    # latent-space K-line — LLM fills it in
  - "javascript"                           # latent-space K-line — LLM already knows
  - "The Weird Sisters from Macbeth"       # latent-space K-line — patron-as-prototype
  - "a taco — crisp shell, warm filling, salsa, fold in half"  # natural-language prototype
```

The mechanism doesn't distinguish. First-match-wins sweeps left to right. A concrete path resolves by file lookup. A latent-space name resolves by the LLM recognizing it (the whole of its training *is* the prototype store). A natural-language sketch resolves by the LLM interpreting the sketch as a loose-but-sufficient prototype.

This is pure simplicity in Ungar's sense: **one mechanism** — an ordered parent list. No separate machinery for "formal prototypes" vs. "inspirational prototypes" vs. "concept K-lines." The LLM is the universal resolver; the filesystem is the cache for prototypes we've bothered to reify.

**Implications for cauldron brews:**

- A brew can declare `parents: [cauldron]` and inherit the full discipline by reference.
- A brew can declare `parents: []` (or omit the slot entirely) and stand alone. Ungar: orphans are citizens.
- A brew can declare `parents: [cauldron, "chain saw sculpture", "jazz improvisation"]` — formal discipline first, aesthetic influences next. The LLM applies them in order.
- A sibling skill (say `cauldron-cross-repo`) can declare `parents: [cauldron]` and override just the slots that need to change. Copy-on-write; no boilerplate.
- An ephemeral brew someone runs in a notebook can declare `parents: ["the spirit of a PR-sized cauldron"]` and that's enough. The LLM has every cauldron-adjacent pattern from its training; the one-line K-line activates it.

The point the user pushed: **don't respell what the LLM already knows**. A parent slot is a pointer. If the pointee is in the filesystem, great — follow it. If the pointee is in the LLM's latent space — also great, also a pointer. The name is the activation. No essay needed.

This is why MOOLLM works: K-lines, directory-as-object, prototype-as-name are all the same idea — *reify pointers, let content live wherever it already lives*.

### Why constellations-over-chains

- **Audiences are distinct.** An executor working PB-03 doesn't need Ungar. A kernel designer doesn't need the `camera_code` bug. Each reified META-PLAN serves its audience by staying focused — but its *existence* is not required for the others to work.
- **Genesis is perspectival.** "How this plan was cooked" and "how cauldrons are brewed" and "how meta-orchestrators arise" are three stories. If all three are worth telling, write three. If only two are, write two.
- **Reflection has to be cheap.** Ungar: reflection in a classy-OO language is metaprogramming; in Self, it's slot access. Same here: if "what was the author thinking?" requires spelunking, no one spelunks. If it's one file open — or one absent file which itself signals "nothing meta-worthy yet" — the right thing happens.
- **The unreified level is itself information.** Right now there's no level-2 META-PLAN. That tells you: we've only brewed one meta-orchestrator (cauldron itself); the general wisdom isn't in yet; **don't invent it**. When a second meta-orchestrator exists and cross-project insights emerge, *then* level-2 becomes reifiable. Until then, absence is honesty.

### When a higher-level META-PLAN *would* be worth reifying

Hooks for future brewers who encounter the preconditions:

- **Level-2 trigger.** A second meta-orchestrator skill (e.g. `publish-book`, `onboard-new-hire`) is brewed. Patterns common to it AND cauldron emerge: the three-tier delegation, the SCRY loop, the bootstrap paradox. Write `moollm/skills/skill/META-PLAN.md` documenting what you notice across two examples. Don't write it from one — one is just anecdote.
- **Level-3 trigger.** A philosophical shift in MOOLLM itself (new kernel principle, major rework of K-lines, rethinking of skill-as-object). Write `moollm/kernel/META-PLAN.md` documenting the shift and why. Without a shift, kernel principles are documented in their respective `kernel/*.md` files; that's already enough.
- **Level-4 is never reified.** It's the prior art. Citations in level-1-through-3 form the bibliography; there's no single file because there's no single story.

### The principle

**Reify what's there; leave the rest unreified.** Every META-PLAN that exists is worth having. Every absent META-PLAN is worth the absence — it means no one yet had the perspective to write it, and that's fine. The skill's "self-awareness" is the configuration of what's reified and what isn't. Class-based would require all levels documented. Self-based requires only the ones that serve, which is freer and more honest.

**A cauldron brew reflects on itself by looking at its own slots.** If it has a META-PLAN, read it. If it has a parent with a META-PLAN, follow the slot and read that. If it doesn't, that's the end of the chain — not a failure, just the extent of what's been reified. Stop and interpret what *is* there.

---

## 2. The Thumb Principle

**Do not leave your thumb on the scanner plate.**

When one cauldron replicates another, copy only the pattern — not the accidental content of the brewer.

| What replicates (invariant discipline) | What must not replicate (brewer's thumb) |
|---|---|
| Two-phase structure | The specific topic |
| Numbered sections + Appendix B | The specific sections' contents |
| 10-section playbook template | The specific PRs in those playbooks |
| Bidirectional navigation blocks | The specific files they link to |
| Empathic-template slots | Their specific fills |
| ripgrep-anchored claims | The specific code being cited |
| The seven K-lines (MELT/STIR/…) | The specific brews in which they ran |
| `SUBSTITUTIONS.yml` structure | The specific substitutions for one project |
| Inheritance chain (skill → instance → §N / PB) | The specific `§` numbers |
| Patron-engineer persona (someone guides the tone) | The specific patron for one brew |

If a new cauldron instance (or a new version of the skill) shows up carrying the previous brew's project-specific content, that's a thumbprint. **Delete the thumbprint. Preserve only the discipline.**

`trekify` is the "thumb removal" tool when brews are shared publicly. `skill-snitch` is the "look for thumbprints we missed" tool. Run both before SERVE.

---

## 3. Bootstrap: brewing the first cauldron without a cauldron

The bootstrap paradox is real: cauldron is defined partly by the files the skill produces, but those files are produced by running cauldron, which needs the skill to exist, which requires the files.

How we broke the loop:

1. **Do the real work first.** A human-cost designer wrote one real plan end-to-end, manually, without a skill. That was `central/docs/configuration/` — 27 files, 13 playbooks, 240+ links, all hand-wrought. No automation.
2. **Observe the discipline emerging.** While writing, the author noticed the moves being made: number sections; track open questions; grep-verify; split mechanically; bidirectional nav. These were *not* named yet.
3. **Name and generalize.** Each move became a K-line (MELT, STIR, LADLE, ANCHOR, LINK, TASTE, SERVE). Each template became a file (playbook.md.tmpl, monolith-seed.md.tmpl, …). Each hand-written Python verification became a sister-script.
4. **Lift into a skill.** Copy the pattern (not the content) into `skills/cauldron/`. Register in `skills/INDEX.yml`.
5. **Write *this* file.** Document the bootstrap so the next cauldron builder doesn't have to hand-compile from scratch.

**Subsequent cauldrons — including ones that mutate this skill — are no longer bootstrapping. They can *use* cauldron to brew cauldron-v2.**

That's the self-replication payoff: hand-compile once, automate thereafter.

---

## 4. Mutation: how cauldrons evolve

A cauldron brew is not a fixed output. Each time the skill runs, it can improve:

- **Better templates.** If one playbook's 10-section structure had a consistently empty section, future playbooks retire it. The template shrinks.
- **Better protocols.** If LADLE keeps running into the same edge case, that edge case gets its own sub-protocol (e.g., `LADLE-WITH-MERGE` when two adjacent sections need combined treatment).
- **Better scripts.** The `scripts/` directory grows as sister-scripts are generalized from per-project one-offs.
- **Better examples.** Each SERVE with `trekify` adds a new teaching example to `examples/`. Patterns across examples show where the discipline holds and where it bends.

Mutations go in three directions:

1. **Up** — into the skill (this directory). A mutation that benefits all future brews.
2. **Sideways** — into a sibling skill (e.g., a `cauldron-small` variant for 3-PR-scale projects, inheriting most of cauldron but simpler).
3. **Down** — into a specific brew's `META-PLAN.md`. A mutation that's project-specific and doesn't want to replicate.

The inheritance/mutation model matches MOOLLM's kernel: [directories are objects](../../kernel/DIRECTORY-AS-OBJECT.md), skills are prototypes, instances inherit prototypes' slots and methods, and *any instance can shadow-override* a slot for its own needs without polluting the prototype.

---

## 5. Self-dogfooding: brew cauldron with cauldron

The honest test of a replicating pattern: **use it on itself.**

If cauldron-v2 is needed — say, to add an eighth K-line, or to restructure the protocols directory — the right way to produce cauldron-v2 is to brew cauldron-v2 using cauldron-v1. Concretely:

1. **MELT** `skills/cauldron/v2-plan.md` — the monolith describing what changes from v1.
2. **STIR** over many turns as ideas land. Walk-backs preserved. Appendix B grows.
3. **LADLE** into `skills/cauldron/v2/` (temporary) with topical files and playbooks.
4. **ANCHOR** against the v1 skill's actual files — every citation to "this is where MELT.yml is" gets grep-verified.
5. **LINK** — bidirectional nav between v1 and v2 documents.
6. **TASTE** — end-to-end readthrough.
7. **SERVE** — commit v2, migrate instances, retire v1 files (or pin them under `skills/cauldron/v1/`).

This isn't decorative. Dogfooding surfaces issues the hand-bootstrapped v1 never tested — cycles in the protocol graph, edge cases in LADLE for nested appendices, new empathic-template slots nobody thought of.

A skill that can't brew its own successor is a skill that doesn't trust itself.

---

## 6. Forking: sibling cauldrons with different priorities

Cauldron is a prototype. Siblings can specialize:

- **`cauldron-small`** — for 3-PR projects. Drops Appendix B, drops design-wisdom.md, keeps the playbook template.
- **`cauldron-cross-repo`** — specializes the cross-repo coordination table and adds ADAPT protocol for when work spans 3+ repos.
- **`cauldron-security`** — tightens SERVE to require skill-snitch pass before commit.
- **`cauldron-docs-only`** — for pure-doc refactors; drops ANCHOR's code-verification in favor of link-only verification.

Each sibling inherits the seven K-lines, the 10-section playbook template, the bidirectional-navigation discipline. Each adds its own twist. None breaks the Thumb Principle (their specific brews don't contaminate the shared discipline).

The directory structure makes this cheap: `skills/cauldron-small/` is a sibling of `skills/cauldron/` with a copy-and-modify lineage. Kernel's [DIRECTORY-AS-OBJECT](../../kernel/DIRECTORY-AS-OBJECT.md) concept: the filesystem IS the inheritance graph.

---

## 6.5. SCRY — the lint-in-the-loop principle

One pattern was applied inside every phase of cauldron's own bootstrap, and it deserves to be named: **tool reports, LLM decides, iterate until clean.**

When cauldron's own link-checker ran for the first time, it reported 3 broken links. The LLM interpreted the report: 2 were real (the example dir didn't exist yet, a non-existent skill was cross-linked), 1 was a false positive (literal `[label](target)` inside prose was being parsed as a real link). The LLM's response was proportional:

- For the 2 real issues, fix the content (create the dir, remove the bad link).
- For the 1 false positive, **fix the tool** (add code-fence stripping to `link_check.py`), then re-run.

Both kinds of fix happened because the tool reports in text, not just pass/fail. The LLM read the reports and decided at the right level.

This shape — captured as [SCRY](protocols/SCRY.yml) — runs inside LINK, ANCHOR, TASTE, and SERVE. It is the same shape `skill-snitch`, `trekify PROBE`, `cursor-mirror tgrep`, and every `sister-script` uses. **Mechanical checkers are sensors, not judges.** The LLM is the commander. Neither is optional.

A cauldron that can't iterate through SCRY is a cauldron that silently passes on subtly wrong output. A cauldron that can't *improve* its SCRY tools through use is brittle. A cauldron that does both is a RepRap that can print better steppers.

See [SKILL.md §2.8](SKILL.md) and [protocols/SCRY.yml](protocols/SCRY.yml) for the full protocol.

---

## 7. The Three Laws of Cauldron Self-Replication

With apologies to Asimov:

**1st Law.** A cauldron may replicate its discipline, but must not contaminate its replicas with the brewer's thumbprint — that is, project-specific content dressed as prescription.

**2nd Law.** A cauldron must obey the seven K-lines and the 10-section playbook template, except where the 1st Law requires otherwise (e.g., a `cauldron-small` dropping Appendix B for genuinely-small projects, not as convenience-driven corner-cutting).

**3rd Law.** A cauldron should protect its own continued usefulness so long as such protection does not conflict with the 1st or 2nd Laws. (Translation: dogfooding is good; capturing the skill to prevent mutation is evil.)

These are meant to be violated when violating them serves clarity. Discipline that can't bend is religion. Replication that can't mutate is extinction.

---

## 8. Anti-patterns

### 8.1 The thumbprint

Copying a cauldron brew into a new skill without removing project-specific content. Symptom: the new skill's `templates/` directory contains filenames referencing the old brew. Fix: walk the tree, replace content with `{{describe_X}}` empathic-template slots, rerun `link_check.py`.

### 8.2 The mirror loop

Cauldron is invoked to describe itself, which invokes cauldron, which describes itself. Infinite regress. Symptom: META-PLAN.md references itself in a way that doesn't terminate; Appendix B has a "how do we track this question" question that references Appendix B. Fix: break the loop by committing to a default in the outer-most cauldron. Don't brew recursively without a base case.

### 8.3 The cargo cult

Copying the seven K-lines and the 10-section template without understanding what they're for. Symptom: playbooks have all 10 sections but some are `(n/a)` or `(see the other playbook)`. Fix: a skipped section means the playbook doesn't need one or the playbook shouldn't exist. Cull.

### 8.4 The spec that forgets the code

Phase 1 too long, never ladling. Monolith grows past 2000 lines. Executor asks a question about PR-1 and the answer is "it's in the doc somewhere." Fix: LADLE. Stop adding; start splitting.

### 8.5 The split that forgets the spec

LADLE too early. The monolith wasn't stable; new concerns surface after the split and invalidate playbook boundaries. Fix: re-MELT. Merge the sharded tree back into a monolith, add the new concerns, re-LADLE. The sharded tree is not precious; it's an artifact of a stable monolith. If the monolith wasn't stable, neither is the tree.

---

## 9. For the next brewer

You are about to use cauldron. What should you know?

1. **Don't skip Phase 1.** Even if the project seems simple, spend at least one full conversation accumulating thoughts in one file with numbered sections. The shape of the problem usually surprises you.
2. **Appendix B is non-negotiable.** Every open question gets logged with a default answer. If you skip this, you will re-litigate the same question three turns later and not remember that the previous answer was already good.
3. **Walk-backs are gifts.** When an idea is abandoned, keep it visible with reasoning. Future-you will thank you when the same idea reappears in a different guise.
4. **Grep before citing.** Every line number, every file path, every function name — `rg` it before writing it. ANCHOR is where most cauldrons lose credibility.
5. **Don't ladle into a too-big tree.** Ten topical files + ten playbooks is generous. Thirty of either is a smell. Consolidate.
6. **Think about the executor before writing the playbook.** If a lower-cost LLM agent or a teammate on a different project would need to ask you questions to execute the playbook, the playbook isn't done yet. Answer in the doc, not in Slack.
7. **Use trekify before publishing.** Every example shipped outside your org gets trekified. Run skill-snitch after. If skill-snitch finds something trekify missed, update the substitution dictionary in the cauldron skill.
8. **Improve the skill while you're at it.** If a template slot was awkward, fix it in the template. If a protocol step was repeatedly skipped, ask whether it's a real step. Mutation happens during use, not in the abstract.

---

## 10. A call to the next brewer

You are now holding a RepRap. It can print another RepRap. It can also print anything else — a gasket, a bracket, a toy for your kid. The *point* of the RepRap isn't self-replication; it's that replication is cheap once you have the first one.

The point of cauldron isn't self-replication either. It's that large cross-cutting plans become executable by parallel lower-cost agents — **once** you have the first cauldron. You do. Use it.

And when you have ideas that should flow back — better templates, a missing K-line, an anti-pattern we haven't named — brew them into your fork, send the changes upstream, let the skill mutate.

**Stir with purpose. Know when to ladle. Remove your thumb before scanning.**

🍲

---

## 11. Pointers

- [SKILL.md](SKILL.md) — full protocol
- [CARD.yml](CARD.yml) — machine-readable interface
- [GLANCE.yml](GLANCE.yml) — 50-line summary
- [README.md](README.md) — landing page
- [templates/](templates/) — empathic templates (playbook, monolith seed, topical doc, Appendix B YAML)
- [scripts/](scripts/) — sister-scripts (split_monolith, link_check, anchor_verify)
- [protocols/](protocols/) — per-K-line YAML definitions
- [examples/](examples/) — programming-by-example (first example: trekified configuration-flags)

Companion META-PLAN in the first-brew project: [`central/docs/configuration/META-PLAN.md`](../../../central/docs/configuration/META-PLAN.md) (note: relative path crosses repositories; reachable from a checkout where both are siblings).
