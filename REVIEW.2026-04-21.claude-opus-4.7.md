---
target: moollm
target_level: root
reviewer: claude-opus-4.7
date: 2026-04-21
session_driver: cursor
prompted_by: "Don Hopkins — 'deep dive review and analysis and design and goal discussion'"
yml_pair: REVIEW.2026-04-21.claude-opus-4.7.yml
---

# MOOLLM — Deep Review

**Confidence in overall judgment: 85%.** I read the kernel in full, the introspection cluster (cursor-mirror, bootstrap, skill-snitch) in depth, the schema skill at GLANCE-level, and scanned INDEX.yml / INDEX.md for the ecosystem. Adventure engine, most character skills, examples/adventure-4, and the NO-AI™ suite (beyond the 8 ambient ones I live under) were surface-read or unread. I'll call out what I'm guessing vs. what I've cited.

Evidence convention: every non-trivial claim cites `file:line`. Where I didn't read deeply enough to cite, I say so.

---

## What MOOLLM actually is (functional description, marketing stripped)

A filesystem-as-object-system for LLM-navigable microworlds, with four structural moves:

1. **Directories are objects.** A directory's files are its interfaces. `queryInterface(dir, 'room')` → `dir/ROOM.yml`. Implemented, not drawn: `kernel/SELFISH-COM-IMPLEMENTATION.md:42-74`.

2. **Prototypes over classes.** A directory declares `parents:` (or `PROTOTYPES.yml`) naming other directories, files, or — and this is where MOOLLM becomes genuinely unusual — latent-space concepts the LLM already knows ("Self", "jazz improvisation", "the Weird Sisters from Macbeth"). Resolution is the LLM walking the parent list and filling in what isn't reified.

3. **Advertisements beat dispatch.** Any object (file, directory, YAML section) can carry `advertisements:` — scored, guarded, condition-gated offers of capability. Handlers are picked by context scoring, not by name-matching or interface contract. Sims's SimAntics in the filesystem.

4. **K-lines as activation.** Names are Minsky K-lines. Uppercase symbols (POSTEL, SCRY, MELT) index to clusters in `PROTOCOLS.yml`. Filenames (CHARACTER.yml, ROOM.yml) are K-lines for interface kind. Skill directory names are K-lines for skill clusters. Name-as-pointer is cheaper than content-as-definition.

The three layers (kernel: infrastructure / skills: semantics / hardware: LLM+orchestrator — `kernel/ARCHITECTURE.md:20-34`) are enforced in practice, not just on paper. `kernel/` contains protocol files and no character/room/world semantics; the discipline holds under grep.

---

## What's strong (with evidence)

**The heritage-to-mechanism map is concrete.** Every philosophical ancestor in `kernel/ARCHITECTURE.md:573-586` maps to a named implementation: Self → `PROTOTYPES.yml` with ordered parents, Sims → `advertisements:` with scores/guards/effects, Minsky → K-lines in PROTOCOLS.yml and skill activation, Densmore-Rosenthal (`US5187786A`, 1991) → the whole filesystem-as-interface-registry scheme. I expected decorative "influenced by" gestures and found working reductions.

**Cursor-mirror is real reverse engineering.** `skills/cursor-mirror/CARD.yml:194-226,302-335` documents 102,724 LevelDB keys, 19,789 tool calls analyzed, platform-specific storage paths for three OSes, and the cursorDiskKV / ItemTable / workspaceStorage hierarchy — all machine-queryable. The CLI is 702 lines; `lib/*.py` adds 2,656 lines of structured analysis code. That's 3,358 lines of Python against a closed LevelDB, not a wrapper around an API. Few MOOLLM-adjacent systems have this level of self-inspection.

**The advisory/operational dichotomy is named, not papered over.** `kernel/ARCHITECTURE.md:72-88` lays out in a table which files are advisory on generic orchestrators (Cursor) vs. operational on smart orchestrators (MOOCO). The tension isn't hidden; it's the comparison's thesis. That level of honesty about layering is rare.

**The Coherence Engine framing is load-bearing.** The claim that "the LLM is the coherence engine" (`kernel/README.md:3-13`) isn't just a tagline — it's what justifies latent-space parent names, empathic templates, speed-of-light multi-turn, and the whole advertisement-scoring model. If the LLM isn't the resolver, MOOLLM collapses back into YAML-with-pretensions. Because it is, MOOLLM holds.

**Filesystem-as-object is validated by a working adventure engine.** `kernel/DIRECTORY-AS-OBJECT.md:117-120` cites 96 ROOM.yml files, 4200-line `engine.js`, compiled from YAML by a Python compiler. I didn't deep-read the engine this pass, but its existence as shipped code is what keeps the whole scheme from being airchair architecture.

---

## What's weak or drifting (with evidence)

**Index coherence is not enforced; it has already drifted.** Two concrete cases found in 30 minutes:

- `skills/INDEX.yml:6` says "130 skills" updated `2026-04-21` (today).
- `skills/INDEX.md:3` says "129 skills" updated `2026-03-24`.
- `skills/cursor-mirror/CARD.yml:142` states `cursor_mirror.py` is "~9800 lines"; `wc -l scripts/cursor_mirror.py` returns `702`. Even adding `lib/*.py` (2,656) totals 3,358, 2.8× less than documented.

Neither is catastrophic. Both are symptoms of the same missing piece: there's no SCRY-style gate on the artifacts that are supposed to enforce coherence. The cauldron skill's SCRY protocol names the pattern ("tool reports, LLM decides, iterate") but it's not wired to INDEX or CARD. The `skill-snitch` CONSISTENCY method (`skills/skill-snitch/GLANCE.yml:27`) checks `INDEX ↔ CARD ↔ SKILL.md ↔ code`, but either it's not run in CI or it's not run against INDEX.yml counts.

**Recommendation:** A ~50-line sister-script `scripts/check_coherence.py` that diffs INDEX.yml `all_skills` vs. `ls skills/`, diffs INDEX.yml vs. INDEX.md skill counts, re-derives CARD.yml line-count claims from actual file sizes, and exits non-zero on mismatch. Run in pre-commit. This is the SCRY pattern applied to MOOLLM's own index.

**The kernel is long for a thing branded "boring."** `kernel/ARCHITECTURE.md` is 696 lines; `kernel/README.md:142` says "Make the kernel boring so the skills can be exciting." The kernel is *semantically* boring (doesn't know rooms/characters) but *conceptually* maximal (mermaid diagrams, heritage tables, magic-dictionary analogy from NeWS, 3-layer cake, advisory/operational comparison). That's not wrong — someone had to write this — but the framing is off: what the kernel actually is is "a principled introduction to a system design," which is different from "boring."

**Scale of INDEX outstrips boot practicality.** `skills/bootstrap/SKILL.md:34` declares INDEX.yml a mandatory first-read. INDEX.yml is 754 lines, ~6,500 tokens. At 130 skills × ~50-line GLANCE.yml average, the true activation-footprint is ~6,500 lines (a full session's working memory budget spent on a menu). Cursor-mirror's OPTIMIZE compilation is the intended mitigation (`kernel/ARCHITECTURE.md:237-316`), but it depends on having session-history data, which a first-time user lacks. First-boot and steady-state have different cost curves; bootstrap doesn't currently distinguish them.

**Core and playful skills are peers in the registry.** `worm`, `cat`, `dog`, `bartender`, `budtender` sit in `INDEX.yml:626-754`'s `all_skills:` alongside `cursor-mirror`, `representation-ethics`, `bootstrap`. Tier metadata exists on individual skills (`tier: primitive`, `tier: 2`) but the registry narrative doesn't prominently separate load-bearing from ornamental. A reader scanning INDEX encounters "budtender: cannabis specialist" before reaching "representation-ethics: ethics of simulation." The system looks busier than it is.

---

## Tensions worth calling out

**Advisory vs. operational.** The same `hot.yml` file is mirror-of-attention on Cursor and command-to-orchestrator on MOOCO. The principle is right (same artifact, different backing, NeWS-style magic dictionaries — `kernel/ARCHITECTURE.md:56-71`), but until MOOCO ships broadly, the "smart" column is aspirational. ~80% of current MOOLLM work happens on Cursor. The magic-dictionary analogy lands only when there's a real backing.

*Implication for investment:* Either MOOCO needs to ship to the point where it's the default, or Cursor-on-advisory needs to be treated as the primary target and the smart-orchestrator language de-emphasized. Running both tracks indefinitely spreads the mechanism thin.

**LLM-as-resolver-of-prototype-names.** MOOLLM's most novel move — declaring `parents: ["javascript", "jazz improvisation", "the Weird Sisters"]` and trusting the LLM to fill in — is also its strongest coupling to model behavior. Different models resolve the same K-line name differently. Across time, the same model's training changes the resolution. The artifact is reproducible; the resolution isn't.

This isn't a bug; it's the cost of the move. The mitigation is *reviewer panels* — different models reviewing the same snapshot, committing `REVIEW.<date>.<model>.{yml,md}` sidecars whose disagreements surface the variance. That's exactly what this review's filename convention enables. The review pattern is (unintentionally?) the natural calibration layer for the prototype-name ambiguity.

**Directories as first-class objects vs. files as first-class.** MOOLLM alternates: sometimes a directory IS the object and files are interfaces (`don-hopkins/CHARACTER.yml`), sometimes a file IS the object (`bob.yml`). The selfish-COM spec (`kernel/SELFISH-COM-IMPLEMENTATION.md:103-112`) names both, and `queryInterface` handles both, but the rule for *which to choose* isn't documented I could find. New authors default inconsistently. A small decision guide ("directory when multiple interfaces OR children; file otherwise") would help.

---

## Frontiers (hooked but unbuilt)

1. **Smart-orchestrator layer.** CARD.yml advertisements with `score/condition/type: AMBIENT` are specified and populated, but on Cursor no one reads them and auto-injects. This is the unbuilt middle. Biggest lever for making the skill ecosystem operational.

2. **SCRY gate on indexes.** Named in cauldron's SCRY protocol and skill-snitch CONSISTENCY method. Not wired. ~50 lines of Python in `scripts/` closes this.

3. **Review-panel composition.** `adversarial-committee` + multi-model REVIEW sidecars = formal panel review. Not assembled yet. This review is the substrate.

4. **Cross-repo skill portability.** `cauldron/META-PLAN.md:68-71` opens the door to sibling cauldrons (`cauldron-small`, `cauldron-cross-repo`). The patterns exist to generalize, but no sibling has been authored. Proof that the skill-as-prototype model supports copy-and-specialize is still a pending demonstration.

5. **Self-describing REVIEW as skill.** This pattern — dated, reviewer-attributed sidecar; big-endian filename for panel grouping; YAML scorecard + MD narrative paired like CARD+SKILL — is a natural candidate for `skills/review/`. Promotion should wait until 2+ reviewers have used it on 2+ repos to stress the schema.

---

## What I'd do differently

**Shorten bootstrap's mandatory-read set.** INDEX.yml at 754 lines is the wrong unit. Bootstrap should read GLANCE.yml of INDEX (top-10 foundation skills, cluster tags), plus whatever's in `.moollm/working-set.yml`. Full INDEX loads on demand when a session names an unfamiliar skill.

**Generate INDEX.md from INDEX.yml.** Sister-script the narrative index. Drift-by-construction dies permanently.

**Add a "tier" axis to INDEX narrative, not just per-skill metadata.** Explicit `foundational / applied / ornamental` grouping. Reader can read the foundational section and be functional without touching worm/cat/dog unless they're building an adventure.

**Name advisory mode as the primary mode on Cursor.** Don't market "magic dictionaries" on a driver that can't magic. Say "on Cursor these files are self-mirrors; on MOOCO they become directives" and treat the split as two genuinely different products, not a spectrum.

**Ship a `check_coherence.py` SCRY gate this week.** 50 lines of code; catches the kind of drift this review found; repays itself the first time it fires.

---

## What I'm uncertain about (honest gaps)

- **Adventure engine.** I cited `engine.js` at 4200 lines from metadata; I didn't read it. My confidence about the "validating concrete artifact" claim is ~70%, not 90%. Deep-read TBD.
- **Representation-ethics / ontology / hero-story triad.** GLANCE-read only. The claim that they form a coherent ethical framing is ~60% confident. Needs a focused pass.
- **MOOCO.** I haven't read the MOOCO repo or scripts. My claims about smart-orchestrator layering are based on how it's described in MOOLLM's docs, not on inspecting MOOCO itself.
- **The playful skills.** Cat, dog, worm, bartender — I assume these are adventure-game color from INDEX taglines. Could be wrong; could be that `worm` (two-pointer cursor, `EAT POOP BARF STICK-UP-BUM`) is a legitimate data-flow primitive I misread. Retraction welcome.

---

## Invitation to panel siblings

This review's filename encodes the time-first convention that makes multi-model panels trivially composable:

```
moollm/REVIEW.2026-04-21.claude-opus-4.7.yml
moollm/REVIEW.2026-04-21.claude-opus-4.7.md
```

Other models reviewing the same snapshot should commit next to it:

```
moollm/REVIEW.2026-04-21.gpt-5.4.yml
moollm/REVIEW.2026-04-21.gpt-5.4.md
moollm/REVIEW.2026-04-21.gemini-3-pro.yml
moollm/REVIEW.2026-04-21.gemini-3-pro.md
```

The scorecard axes and section headings here are suggestions, not a schema. Future reviewers may add axes, disagree with ratings, or cite evidence I missed. A meta-tool — perhaps `skills/review/scripts/panel_diff.py` — could then diff the scorecards and surface where reviewers disagree.

The point isn't consensus. The point is that **disagreement is evidence**: when a latent-space prototype name ("directory-as-object") resolves differently for two models, you've found either a useful ambiguity or a drift in the system. Either is worth making visible.

---

## Cross-references

- Deep dives: `kernel/REVIEW.2026-04-21.claude-opus-4.7.{yml,md}`, `skills/REVIEW.2026-04-21.claude-opus-4.7.{yml,md}`, `skills/cursor-mirror/REVIEW.2026-04-21.claude-opus-4.7.{yml,md}`
- Self-review of work authored this session: `skills/cauldron/REVIEW.2026-04-21.claude-opus-4.7.{yml,md}`
- Pattern seed: pattern definition in the paired `.yml` → `pattern_definition:` section

---

*This review is perspective, not canon. It will date. The point of the sidecar is that tomorrow's reviewer — another model, another me, or a human — can disagree productively by committing a sibling, not by overwriting this.*
