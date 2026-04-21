# 🍲 CAULDRON — Full Protocol

Two-phase discipline for large cross-cutting technical plans. This file documents the full CAULDRON protocol: when to invoke, how each K-line works, how cauldron composes with the rest of MOOLLM, and a full worked walkthrough against the first real-world instance.

**Classification: meta-orchestrator.** Cauldron is not a leaf skill — it sequences K-lines, iterates within them (SCRY loops, STIR turns, TASTE/STIR ping-pong), conditionally branches on state signals, composes sub-skill outputs into next-step inputs, and delegates work to three tiers: **tools** (sister-scripts), **other LLM skills** (trekify/skill-snitch/committee), and **the LLM itself** (for holistic interpretation). See [CARD.yml `orchestration_model`](CARD.yml) for the full state machine, guards, and delegation classification.

**Patron:** The Weird Sisters (Macbeth). Practical, not parodic: the brew produces dinner, not curses.

**Tagline:** *Melt a big plan down. Ladle out small PRs.*

See [GLANCE.yml](GLANCE.yml) for the 50-line summary and [CARD.yml](CARD.yml) for the machine-readable interface. See [README.md](README.md) for the pitch. See [META-PLAN.md](META-PLAN.md) for the self-replication story — how cauldron was brewed, how future cauldrons mutate, the Thumb Principle, and the Three Laws.

---

## 1. When to invoke CAULDRON

Use cauldron when **all three** are true:

1. The problem is **cross-cutting** — touches multiple apps, subsystems, repos, or roles.
2. The total work is **many PRs worth** — at minimum 5, more usually 10–20.
3. **Multiple people or LLM agents** can usefully work on different parts in parallel once the shape is known.

Do not use cauldron for:

- **Single-PR changes.** Write a clear PR description and ship it.
- **Exploratory research** where the shape of the problem isn't known yet. Start with a small "what do I even want to know?" doc and iterate on smaller scales; invoke cauldron once you hit "this spans multiple systems."
- **One-person efforts with no future readers.** Cauldron is leverage through docs; no audience = no leverage.
- **Production incidents.** Fix the thing. Write the playbook afterward if the incident will recur.

---

## 1.5. Cauldron is a meta-orchestrator

Cauldron's job is not to do the work. Its job is to **sequence**, **iterate**, **branch**, **compose**, and **delegate** — so the right actor does the right step at the right time, with the right inputs from the prior step.

**Sequential.** Phases run in order: MELT → STIR* → LADLE → ANCHOR → LINK → TASTE → SERVE. This is the happy path.

**Iterative.** Three nested iteration shapes:

- **STIR × N turns** — every user message folds into the monolith; Phase 1 may last 30+ turns.
- **SCRY × N reports** — within ANCHOR / LINK / TASTE, tool-reports-LLM-decides-iterate loops run until the report is clean OR the tool itself needs fixing (meta-fix).
- **Phase ping-pong** — TASTE can send you back to STIR if smells are structural; LADLE can be redone if the monolith wasn't stable after all.

**Conditional.** Cauldron branches on state signals, not on fixed schedules:

| Signal | Guard | Transition |
|---|---|---|
| Section numbers renumbering? | Yes → stay in STIR. No → eligible for LADLE. | STIR → STIR or STIR → LADLE |
| SCRY report clean? | Yes → next phase. No → LLM fixes content or fixes the tool; re-SCRY. | in-phase iteration |
| TASTE found structural smells? | Yes → back to STIR (redo content). No / cosmetic → SERVE. | TASTE → STIR or TASTE → SERVE |
| Skill-snitch audit clean? | Yes → SERVE commits. No → tighten trekify dict; re-PROBE; re-SCRY. | SERVE iteration |

**Composing.** Output of step N is a named, typed input to step N+1. No hidden state:

```
MELT   → {monolith_path, session_id}
STIR   → {sections_modified, questions_added/resolved, consolidated_monolith}
LADLE  → {created_files, section_map, playbook_list}
ANCHOR → {verified_count, broken_citations}           (SCRY until broken == [])
LINK   → {links_checked, broken_links}                (SCRY until broken == [])
TASTE  → {smells, next_steps}                         (branch: STIR or SERVE)
SERVE  → {commit_sha, pr_url, example_dir, dispatch_plan}
```

**Delegating to three tiers.** Every step in cauldron is one of:

1. **Delegated to a tool** (sister-script). Mechanical, verifiable, deterministic work. Examples: `split_monolith.py` (LADLE), `link_check.py` (LINK), `anchor_verify.py` (ANCHOR). **The tool reports; cauldron reads the report and decides.** SCRY shape.
2. **Delegated to another LLM skill.** Specialized LLM judgment that already has a home. Examples: `adversarial-committee` (STIR), `empathic-templates` (LADLE), `trekify` + `skill-snitch` (SERVE), `thoughtful-commitment` (SERVE), `cursor-mirror` (MELT, STIR, SERVE). **Each sub-skill's output becomes cauldron's next-step input.**
3. **Done by the LLM itself** inside cauldron's phase. Holistic interpretation that no sub-skill covers. Examples: choosing the initial section set in MELT; writing a walk-back in STIR; smell-testing the whole tree in TASTE. **Cauldron acts; it doesn't delegate.**

**Why the classification matters.** Most MOOLLM skills are leaves: one input → one output. Meta-orchestrators aren't: they carry state across phase boundaries, iterate with signal-driven loops, compose sub-skill outputs, and delegate to the right actor at each step. Other MOOLLM meta-orchestrators include `debate` / `adversarial-committee` (multi-agent), `plan-then-execute` (gated phases), `play-learn-lift` (3-phase sequential). Cauldron is the most complex of them — 7 phase-specific K-lines + 1 cross-cutting (SCRY) + iteration + branching.

If you want to build another meta-orchestrator (e.g. a `publish-book` skill, an `onboard-new-hire` skill), cauldron's structure is the template. The three-tier delegation classification — tool, sub-skill, LLM — generalizes beyond plans into any multi-step coordinated workflow.

See [CARD.yml `orchestration_model`](CARD.yml) for the state-machine diagram with explicit guards.

---

## 2. The K-lines

Seven phase-specific protocols (MELT through SERVE) plus **one cross-cutting**: SCRY, the lint-in-the-loop pattern that runs inside LINK, ANCHOR, TASTE, and SERVE. Each K-line activates a protocol cluster.

### 2.1 MELT — start a Phase-1 monolith

**Input:** a topic name, scope description.

**Output:** `docs/<topic>-plan.md` seeded with:

- `## 1. Current state: what is wrong` (the audit of why we're doing this)
- `## 2. Target model` (the proposed change)
- `## 3. Affected surfaces` (what changes where — filled in during STIR)
- … (sections accumulate during STIR)
- `## N. Open questions` (reserved; short)
- `## Appendix A. Design wisdom and conventions` (reserved for cross-cutting principles)
- `## Appendix B. Questions still awaiting a decision` (the tracker)

**Composition:** calls `bootstrap` for session warmup; reads `kernel/naming/NAMING.yml` to inherit big-endian / prefix-as-owner rules; applies `yaml-jazz` discipline to Appendix B.

**Discipline:**

- Every top-level section is numbered (§1, §2, …) and every sub-section is dotted (§3.1, §4.5.2). Numbers may be renumbered during Phase 1 but the *existence* of numbering is non-negotiable.
- Appendix B structure is fixed: B.1 resolved / B.2 open not-blocking / B.3 newly raised / B.4 drafting-answered.
- No implementation files are created. The plan is text.

### 2.2 STIR — fold a new turn into the monolith

**Input:** user message or clarifying turn; current monolith.

**Output:** modifications to one or more sections; possible new entries in Appendix B.

**Steps taken by STIR:**

1. **Read the monolith** (or the relevant §).
2. **Identify which § is affected.** If none, create a new § or Appendix subsection.
3. **Compose with `cursor-mirror`** to probe earlier sessions for related ingredients.
4. **Compose with `adversarial-committee`** if the user's input is contested (e.g., "should we abstract events?"). The committee's verdict lands in the § as reasoning, not just conclusion.
5. **Update cross-references.** If a new § is added, scan other sections for mentions of the same concept and add the §-number link.
6. **If a question was raised but not answered**, add an entry to Appendix B with a default answer and mark it `status: open`.
7. **If a prior question is now answered**, move it from B.2/B.3 to B.1 ("resolved, kept for audit"). Do not delete — the audit trail is a gift to future readers.

**Walk-backs are sacred.** If the user rejects a previously-accepted idea, update the § to open with *"An earlier draft proposed X; that design is cancelled. Reasoning: …"* and keep the rejected design visible. Future readers need to see the rejected alternatives, not just the surviving one.

**Composition:** `cursor-mirror`, `adversarial-committee`, `no-ai-slop` (ambient), `no-ai-hedging` (ambient — every claim gets a confidence), `postel` (ambient — tolerate messy user instructions).

### 2.3 LADLE — split the stable monolith

**Precondition:** the monolith's section numbering has been stable across at least the last 3 STIR invocations. If sections are still being renumbered, Phase 1 is not done.

**Input:** monolith path, output directory, section→file mapping.

**Output:** the Phase-2 tree:

```
docs/<topic>/
  README.md                              — scope + navigation
  01-<shortname>.md .. NN-<shortname>.md — topical files, one per top-level §
  design-wisdom.md                       — Appendix A
  <N>-open-questions.md                  — Appendix B carried forward
  playbooks/
    README.md                            — dependency graph + PR index
    PB-01-<short>.md .. PB-NN-<short>.md — one per landable PR
  META-PLAN.md                           — process wisdom extracted from this brew
```

**Steps taken by LADLE:**

1. **Section mapping.** The caller supplies a map: `§N → filename`. Cauldron writes this as a YAML comment block at the top of the split script.
2. **Split mechanically.** `scripts/split_monolith.py` walks `## N.` boundaries and writes each slice to its target file. **No manual copy-paste.**
3. **Preamble per file.** Each topical file gets a `> Maps to §X–§Y` preamble + back-link to the monolith for archaeology.
4. **Playbook generation.** For each landable PR, empathic-templates fills `templates/playbook.md.tmpl` from the relevant sections.
5. **README generation.** `templates/topical-readme.md.tmpl` fills with the topic table, the target-model summary, and the playbook index.

**Composition:** `empathic-templates` provides the slot-filling; `sister-script` convention governs the Python scripts (doc-first: the script's behavior matches what the doc says).

**Output principle:** keep the monolith. It's the Phase-1 artifact of record. Someone may want to scroll it end-to-end; someone may want to diff it against a future rebrew; someone may want to cite a §-number in a meeting. One file's worth of storage is not worth deleting.

### 2.4 ANCHOR — re-verify every claim

**Input:** the output directory from LADLE.

**Output:** a report of every claim verified + every claim that didn't match the code.

**Steps:**

1. Walk every markdown file.
2. For each `` `apps/foo/bar.py:123` `` or `` line 162 `` or `function_name` in a code-reference position, run a ripgrep that should match.
3. If the match fails or has moved (different line number), flag it.
4. Collect all flags into a report.

**Why:** line numbers drift. Function names get refactored. File sizes change. The Phase-1 monolith captured a snapshot; the tree might land days or weeks later; the code may have moved. ANCHOR is the "re-verify before committing" step.

**Composition:** `ripgrep` does the grepping; `no-ai-hedging` forbids "line ~120ish" phrasing — if a line number is cited, it's cited exactly or marked "drift-prone, re-grep on execution."

### 2.5 LINK — bidirectional navigation + link-checker

**Steps:**

1. **Playbook Navigation blocks.** Each playbook gets `## Navigation` with `Preceded by / Unlocks / Related / Design source`. The `Design source` links into the topical doc sections.
2. **Topical `## Implemented by` blocks.** Each topical doc gets a footer listing which playbooks implement its prescriptions.
3. **Playbook `## See also` blocks.** Reverse-direction from Navigation: what to monitor after landing, parallel playbooks, follow-up PRs.
4. **Link-checker.** `scripts/link_check.py` iterates every `[label](target)` and verifies the target exists. Broken links are a silent tax — eliminate them.

**K-REF format** (from `k-lines` skill): `path/to/file.md#section-anchor` with inline type/description.

**Composition:** `k-lines` for the cross-reference format.

### 2.6 TASTE — end-to-end readthrough

**Input:** the tree.

**Output:** a smell report: vague TBDs, dangling questions, inconsistent style, over-ambitious playbooks, under-specified verification.

**Smells to detect:**

- Phrases like "figure out later" / "TBD" / "we'll see" — commit to a default or mark as an Appendix B entry.
- Playbook steps without verification.
- Cross-refs that resolve but point at the wrong thing (caught by reading, not by link-checker).
- Playbook scope that's obviously >1 PR worth.
- Unresolved open questions that block a named playbook — should be flagged in the playbook's Prerequisites.
- Claims phrased with qualifier-stacks ("may potentially", "could perhaps be") — `no-ai-hedging` applies.

**Composition:** `no-ai-slop`, `no-ai-hedging`, `adversarial-committee` on contested sections, `postel` for charitable interpretation of the author's earlier self.

### 2.7 SERVE — deliver to executors

**Input:** the tree, plus delivery options.

**Output:**

- A `thoughtful-commitment`-style commit for the split PR, linking back to the cursor-mirror session.
- Optionally: a trekified teaching copy in the cauldron skill's `examples/` directory.

**Steps:**

1. `thoughtful-commitment COMMIT` with the rich message (summary + per-playbook list + link to META-PLAN.md).
2. If `create_trekified_example`, call `trekify MASK-FILE` over each file in the tree, using the project-specific substitution dictionary.
3. Run `skill-snitch SCAN` over the trekified output. Iterate if anything proprietary leaks through.
4. Commit the trekified example as a second PR against `moollm/skills/cauldron/examples/<topic>/`.
5. Produce a PR description referencing the dependency graph and suggesting a dispatch order for executors.

**Composition:** `thoughtful-commitment`, `trekify`, `skill-snitch`.

### 2.8 SCRY — lint-in-the-loop (cross-cutting)

Every other cauldron K-line that does verification uses **SCRY**: run a mechanical tool, read its text report, interpret, iterate.

**Principle:** tool reports, LLM decides, iterate until clean.

The tool is a **sensor**, not a judge. Its job is to tell the LLM faithfully what the literal state of the artifact is: which links are broken, which line numbers drifted, which TBDs are dangling, which secrets might have leaked through trekify. The tool does not decide what to do about its findings. The LLM does that.

**Shape:**

```
while iteration < max_iterations:
    report = run_tool(target)
    if report.clean: return CLEAN
    interpretation = llm_interpret(report, context)
    if interpretation.is_false_positive:
        update_tool_or_config(interpretation)   # meta-fix
        continue
    if interpretation.is_genuine_issue:
        apply_fix(interpretation.fix)
        continue
    if interpretation.is_ambiguous:
        return ESCALATE_TO_HUMAN
```

**Two observed failure modes that SCRY handles:**

1. **Genuine issue.** Tool says "broken link"; the link really is broken; LLM fixes it. (This is the common case.)
2. **False positive that reveals a tool bug.** Tool says "broken link"; the "link" is a literal `[label](target)` inside prose code blocks; LLM recognizes the tool's code-stripping is incomplete; LLM fixes the tool, re-runs, tool now passes. **The tool improves through use.**

**Why this pattern instead of "just write the right tool":**

- Tools that decide silently are risky — they paper over issues the LLM should surface.
- Tools that dump every possible warning produce noise the LLM has to re-interpret every run.
- The balance: **tool cites specific locations faithfully; LLM applies context-aware judgment**.

Neither sufficient alone. Neither optional. Iteration is the *expected* shape of the work.

**Implementations in this skill:**

- `scripts/link_check.py` — SCRY for cross-reference integrity (used by LINK).
- `scripts/anchor_verify.py` — SCRY for code-citation drift (used by ANCHOR).
- Planned: TASTE's smell-scanner; SERVE's skill-snitch wrapper.

**The same pattern elsewhere in MOOLLM:**

- `skill-snitch SCAN` — scans skill sources for security smells; LLM interprets/fixes.
- `trekify PROBE` — scans transcripts for leaked credentials; LLM masks.
- `trekify LONG-RANGE-SCAN` — scans the workspace; LLM audits findings.
- `cursor-mirror tgrep` — scans transcripts; LLM interprets patterns.
- `sister-script`'s entire premise: **tools emit text for LLMs to read, not just for machines to consume**.

**Tool contract** (what any SCRY-compatible tool must do):

- Produce text output (not JSON only — humans and LLMs read the same stream).
- Cite specific locations (`file:line`, not "somewhere in the repo").
- Exit non-zero on issues (so CI integration works).
- Be deterministic given the same input.
- Be fast (< 10s for the full tree).
- **Never silently apply fixes.** That's the LLM's job.
- **Never hide details.** The LLM needs the full context to decide.
- **Never rename / reformat without telling the LLM what changed.**
- **Never be clever about "what you probably meant."** Escalate instead.

**LLM contract** (what the LLM must do when reading a SCRY report):

- Read the whole report, not just the summary.
- Distinguish false positives (tool was wrong) from real issues (fix needed).
- Fix at the right level — could be tool config, could be doc content, could be escalation to a human.
- Re-run the tool to verify the fix worked. **Don't assume.**
- **Never ignore the report because "I'm sure it's fine."**
- **Never silently suppress warnings without documenting why.**

**See also:** [protocols/SCRY.yml](protocols/SCRY.yml) for the full protocol spec. This pattern is general to MOOLLM and deserves to be called out alongside `sister-script` as a core principle of how tools and LLMs cooperate.

---

## 3. Worked walkthrough — the configuration-flags instance

The first real-world cauldron instance. 30+ turns of Phase 1, then a single LADLE. Here's what each K-line did:

### 3.1 MELT

```
User: "You ever work with env vars that gate python imports and silently break autotest?"
```

Cauldron responded by:

1. Reading `moollm/kernel/naming/NAMING.yml` for naming conventions.
2. Creating `central/docs/CONFIGURATION-FLAGS-PLAN.md` with §1 (Current state), §2 (Target model), §3 (Affected surfaces), Appendix B (Questions tracker).
3. Seeding Appendix B with the questions implicit in the user's opening: "what's the canonical name? which aliases retire? what stays?"

### 3.2 STIR × 30

Each user turn folded into the monolith. Key STIR decisions preserved as walk-backs:

- **Storage abstraction proposed (§5 draft 1) → cancelled (§5 current).** The rejected design is still visible in §5's opening paragraph. Reason: Azure/edgebox future doesn't need a unified abstraction.
- **`pystorage` / `pyevents` / `pybigquery` shared packages proposed → all three cancelled.** Reasons preserved in §4.2 ("Not in this table").
- **`camera_code` bug characterized as "silent NULL" → upgraded to "every insert fails silently."** Evidence (ripgrep count + file inspection) preserved in §5 / §A.6.1.

Appendix B grew from 7 questions to 20. Most moved to B.1 (resolved) over successive turns.

### 3.3 LADLE

Single user turn: *"Now break it up into separate documents in docs/configuration including a top level README.md summary index."*

Cauldron's response:

1. Decided the shape: README + 10 topical files + playbooks/ + design-wisdom.md + META-PLAN.md.
2. Wrote a Python script that walked `## N.` boundaries and wrote each slice to its target file.
3. Generated 13 playbooks, each following the 10-section empathic template.
4. Added Navigation/Implemented-by/See-also blocks bidirectionally.

Total artifacts: 27 files, 5183 lines.

### 3.4 ANCHOR

Single user turn: *"be evidence based, grep and tree and fuzzy search."*

Cauldron's response:

1. Re-verified every cited line number in `apps/pyvision/vision/loggerwrapper.py`, `server.py`, `MiscUtils.py`, etc.
2. **Caught a material bug:** the plan said "pyvision silently writes NULL to `camera_name`." ripgrep showed `camera_code` appears 7 times in `loggerwrapper.py` including as the SQL column name itself → INSERT fails entirely. The plan was understating the bug.
3. **Corrected three factual errors:** `db/logs.sql` line 12 not 13; `self.gcp.*` count is 24 not 27; zero call-site migrations needed for `camera_code` (no callers pass it as a kwarg).

### 3.5 LINK

Same turn as ANCHOR. Cauldron:

1. Added a standardized `## Navigation` block to each of the 13 playbooks.
2. Added a `## See also` footer to each.
3. Added an `## Implemented by` block to each topical doc.
4. Ran the link-checker: 240 internal links, all resolved.

### 3.6 TASTE (in progress at time of writing)

Would run over the tree and flag: any "TBD" that should be an Appendix B entry; any playbook step without verification; any cross-ref that resolves but points at the wrong thing.

### 3.7 SERVE (pending)

Would produce:

- A `thoughtful-commitment`-style commit for `central/docs/configuration/` (27 new files).
- A trekified teaching copy in `moollm/skills/cauldron/examples/configuration-flags/`.
- A PR description referencing the dependency graph.

---

## 4. Self-ish object instantiation

A cauldron session **is an object** in MOOLLM's sense (see [`skills/object/`](../object/)). It has slots: its own files, its own content, and — optionally — a `parent` slot pointing at the cauldron skill. Self-style: there are no classes; prototypes are objects; *parents are optional slots, not mandatory ancestry*. Most brews do set `parent = cauldron` because the discipline is worth inheriting, but a brew that sets no parent is a perfectly valid first-class object. See [META-PLAN §1.5](META-PLAN.md#15-super-meta-plans--self-awareness-ungar-style) for the full treatment.

### 4.1 Parent slots (when wired)

When a brew *does* wire its parent slot, the common topology looks like this:

```
cauldron (skill, defined here)
  parent slot (optional) → MOOLLM kernel (DIRECTORY-AS-OBJECT, NAMING, K-lines, yaml-jazz, empathic-templates, …)

cauldron.<instance> (one brew, identified by its directory)
  parent slot (optional) → cauldron

cauldron.<instance>.§N (one numbered section)
  traits from → k-lines skill (when the section name IS a K-line)

cauldron.<instance>.PB-NN (one playbook)
  traits from → empathic-templates (when using the 10-section structure)
```

Read each arrow as "*may* draw from," not "must descend from." A brew that declares no parent inherits nothing — and that's fine. A brew that declares `parent = cauldron` inherits the discipline *by reference*, which means when cauldron's conventions evolve, the brew picks up the evolution for free.

### 4.2 Identity through location

A cauldron instance's identity **is its directory**. This is a direct application of `kernel/DIRECTORY-AS-OBJECT.md`: the filesystem IS the object graph.

- `central/docs/configuration/` **is** the configuration-flags cauldron instance.
- Moving the directory renames the instance.
- Copying it spawns a sibling cauldron.
- No registration table is needed; existence = registration.

### 4.3 Trait carriers

Each discipline is carried by a specific file-kind in the tree:

| Discipline | Carried by |
|---|---|
| Numbered sections | Every `##` heading in topical docs |
| K-lines | Every numbered section name and every playbook name |
| K-REFs | Every `[label](path#anchor)` cross-reference |
| Empathic-template slots | Every playbook's 10-section header layout |
| YAML-jazz | `<N>-open-questions.md` and Appendix B |
| Bidirectional navigation | `Navigation ↔ Implemented-by / Related ↔ See-also` blocks |
| Grep-anchored claims | Anything mentioning `path/to/file:NN` |

### 4.4 Why this matters

The discipline is **inherited by reference (optionally), not copied**. A cauldron instance that sets `parent = cauldron` doesn't re-declare its protocols; it picks them up from the skill. If the skill's conventions evolve (say, adding an A.13 error-handling appendix), those instances can pick up the new convention without being rewritten — only the files that need the convention care. A brew that prefers to stand alone simply doesn't set the parent slot and carries whatever discipline it wants, locally. Both are legal moves.

---

## 5. Failure modes and how cauldron recovers

### 5.1 The monolith is stalling (Phase 1 too long)

**Signal:** more than N successive STIRs produce minor edits only; no new sections; open questions accumulate without default answers.

**Recovery:** run `adversarial-committee` on the three oldest open questions. Commit to defaults and move on. If the committee can't decide, the question belongs in B.2 (deferred) not B.3 (new), and the plan ladles without it — one more open question is not a blocker.

### 5.2 LADLE produces playbooks that are too big

**Signal:** a playbook's Scope paragraph mentions 5+ distinct concerns; its Steps list runs 30+ items.

**Recovery:** in TASTE, split the playbook into 2–3 smaller ones. Add the dependency to `playbooks/README.md`. Do not merge with other playbooks to rebalance — that's the opposite of the one-PR-per-playbook rule.

### 5.3 ANCHOR catches many drifts

**Signal:** more than 10% of cited line numbers don't match.

**Recovery:** the monolith was written against a stale checkout. Rebase the monolith — for each flagged claim, update to current reality or mark "re-grep on execution." Then re-run ANCHOR.

### 5.4 Executor stops-and-escalates mid-playbook

**Signal:** playbook step fails; executor escalates.

**Recovery:** update the playbook, not the Slack thread. Future executors should read the fix in the doc. `no-ai-sycophancy` forbids "oh that's fine, just continue" — a genuine escalation means a genuine doc gap.

---

## 6. Versioning and evolution

Cauldron instances carry a version (in the monolith's front matter or README) of the cauldron skill they were brewed against. If the skill evolves:

- **Minor evolutions** (new empathic-template slot, new protocol K-line) — existing instances pick up the new convention naturally when they next STIR.
- **Breaking changes** (rename of Appendix B structure, change of playbook sections) — the skill's CHANGELOG describes the migration; instances can choose to migrate or pin to the older version by referencing it explicitly.

Migration between versions is itself a cauldron-worthy task. Recursion intended.

---

## 7. Related skills (detailed roles)

| Skill | Active during | What it does |
|---|---|---|
| [bootstrap](../bootstrap/) | every cauldron session start | Load hot.yml / cold.yml; establish context |
| [cursor-mirror](../cursor-mirror/) | STIR, LADLE, SERVE | Probe prior sessions; export Phase-1 chat for LADLE; link SERVE commit to session |
| `rg` (ripgrep, external tool) | ANCHOR | Verify every cited path/line/function. Not a MOOLLM skill today — just the binary. |
| [empathic-templates](../empathic-templates/) | LADLE | Fill playbook slot structure from monolith sections |
| [k-lines](../k-lines/) | throughout | K-line semantics for section names, playbook names, cross-refs |
| yaml-jazz | throughout | Appendix B structured YAML; semantic comments |
| [trekify](../trekify/) | SERVE (optional) | Produce the sanitized teaching copy |
| [skill-snitch](../skill-snitch/) | SERVE (optional) | Audit the trekified output for leaks |
| [thoughtful-commitment](../thoughtful-commitment/) | SERVE | Commit with cursor-mirror-backed reasoning |
| [adversarial-committee](../adversarial-committee/) | STIR, TASTE | Pressure-test contested ideas |
| no-ai-slop / no-ai-hedging / no-ai-sycophancy | ambient | Hygiene on every turn |
| postel | ambient | Accept messy input, emit clean output |
| robust-first | Phase 2 executor side | Stop-and-escalate, don't silently skip |

---

## 8. Quick reference

**When to invoke what:**

| Situation | K-line |
|---|---|
| Starting a new large plan | MELT |
| User adds a concern | STIR |
| Plan is stable, split it | LADLE |
| Verify claims against code | ANCHOR |
| Wire up navigation | LINK |
| Readthrough before shipping | TASTE |
| Deliver to executors | SERVE |

**File layout produced:**

```
docs/<topic>/
  README.md                              (Phase 2 scope + nav)
  01..NN-<topic>.md                      (topical files)
  design-wisdom.md                       (Appendix A)
  <N>-open-questions.md                  (Appendix B)
  META-PLAN.md                           (process wisdom)
  playbooks/
    README.md                            (dep graph + PR index)
    PB-01-<short>.md..PB-NN-<short>.md   (one per PR)
docs/<topic>-plan.md                     (Phase 1 monolith, kept)
```

**Playbook section order (empathic template):**

1. `## Navigation` — Preceded by / Unlocks / Related / Design source
2. `## Scope` — one paragraph
3. `## Prerequisites` — what must have landed first
4. `## Context` — links into topical docs
5. `## Files affected` — created/modified/deleted
6. `## Steps` — ordered, each atomic
7. `## Verification` — grep commands, test runs
8. `## Rollback` — what reverting means
9. `## Success criteria` — observable outcomes
10. `## See also` — reciprocal direction, follow-up checks

---

**🍲 Stir with purpose. Know when to ladle.**
