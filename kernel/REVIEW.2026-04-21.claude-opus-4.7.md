---
target: moollm/kernel
target_level: cluster
reviewer: claude-opus-4.7
date: 2026-04-21
yml_pair: REVIEW.2026-04-21.claude-opus-4.7.yml
parent: ../REVIEW.2026-04-21.claude-opus-4.7.md
---

# Kernel — Deep Review

**Scope:** `kernel/README.md`, `ARCHITECTURE.md`, `DIRECTORY-AS-OBJECT.md` full-read; `SELFISH-COM-IMPLEMENTATION.md`, `INTEREST-GATES.yml`, `NAMING.yml` partial. The constitution and protocol files (context-assembly, memory-management, event-logging, self-healing, tool-calling) not deeply read this pass. **Confidence in kernel-wide judgment: 80%.**

## The move that matters

The kernel's thesis compresses to one line: **infrastructure, not semantics.** `kernel/README.md:29-40` lists what the kernel explicitly does not know ("memory palaces," "adventure rooms," "character personalities," "soul chat"). That disclaimer is not rhetorical — `ls kernel/` contains no character or room or advertisement files. The discipline holds.

This is the kernel's single most load-bearing design move. Break it and MOOLLM becomes a specific-purpose framework for LLM-driven adventure games. Keep it and MOOLLM becomes a substrate that adventure happens to be the demonstration of. The kernel keeps it.

## What it does well

**The three-layer cake (userland / kernel / hardware)** at `ARCHITECTURE.md:20-34` is the right abstraction. Skills don't talk to the LLM directly; they go through kernel protocols (tool-calling, context-assembly, event-logging, memory-mgmt, self-healing). This is exactly the Unix model adapted for LLM orchestration — and it survives contact with reality because skills honestly don't reach past the kernel.

**The directory-as-object spec is implemented, not drawn.** `DIRECTORY-AS-OBJECT.md` plus `SELFISH-COM-IMPLEMENTATION.md:42-74` give you working `queryInterface` code with a resolution table and a `toObjectPath` helper. The Densmore-Rosenthal patent citation (`US5187786A`, 1991) at `DIRECTORY-AS-OBJECT.md:122-130` shows Owen Densmore did this in Unix shells 35 years ago. The kernel is saying: "this works; it worked before; here's our version for YAML+LLM." That's responsible history.

**Heritage → mechanism map is concrete.** `ARCHITECTURE.md:573-586` pairs each philosophical ancestor with a named implementation: Ungar → `parents:` in directories, Wright → advertisements with scoring, Minsky → society-of-mind agents-all-the-way-down, Hewitt/Agha → message passing via advertisements. I expected decorative citations and found working reductions. This is the difference between "inspired by" and "reduces to."

**The advisory-vs-operational honesty.** `ARCHITECTURE.md:72-88` lays out in a table which files function differently on generic vs. smart orchestrators. The same `hot.yml` is a self-mirror on Cursor and a directive on MOOCO. Instead of hiding this, the kernel makes the split the design's centerpiece via the NeWS magic-dictionary analogy (`:56-71`). That level of naming-the-tension is rare.

## What's weaker

**"Boring kernel" is mislabeled.** `README.md:142` quotes "Make the kernel boring so the skills can be exciting." Fine aesthetic. But `ARCHITECTURE.md` is 696 lines of mermaid diagrams, heritage tables, three-layer discussions, driver matrices, and magic-dictionary analogies. That's not boring; that's a principled introduction to a sophisticated system design. The *behavior* is boring (semantic-free plumbing); the *documentation* is maximal.

The fix is a re-label, not a shrink. "Boring kernel" could mean "semantically neutral" rather than "short." Or ARCHITECTURE.md could split into a short core (introductory) and a long appendix (heritage, drivers, analogies). Right now it conflates the two.

**Advisory/operational leaks downward.** Every skill that interacts with `hot.yml` or `working-set.yml` has to re-explain the advisory-vs-operational distinction. Bootstrap does it. Cursor-mirror does it. Cauldron does it. The kernel names the tension but doesn't hide the cost — which means the cost shows up in every skill. On a smart-orchestrator-first system, this would be hidden behind a kernel API. On advisory-by-default, it's everywhere.

This isn't a bug; it's the toll of the design choice. But it's worth naming: running two orchestration models indefinitely multiplies the documentation surface.

**SELFISH-COM-IMPLEMENTATION.md is 3x DIRECTORY-AS-OBJECT.md.** The short one (184 lines) is more likely to be read. The implementation spec (576 lines) is where the actual protocol lives. The crosslinks are good (`DIRECTORY-AS-OBJECT.md:183` → impl, `SELFISH-COM-IMPLEMENTATION.md:1` → concept), but the 3:1 size asymmetry means real implementation details get under-read. Consider either compressing the impl or merging critical parts (e.g., the `queryInterface` resolution table) into the intro doc.

## Tensions worth calling out

**Kernel purity vs. magic-dictionary promise.** The kernel disclaims semantics; the magic-dictionary promise says smart orchestrators read CARD.yml advertisements and inject ambient skills. Isn't reading advertisements a semantic act?

The reconciliation (not stated explicitly in the docs I read, my inference from structure): the kernel doesn't *interpret* advertisements; it *routes* them to an LLM or orchestrator process that does. Ship-of-Theseus distinction. The machinery that reads `type: AMBIENT, score: 0.3` and decides "yes, inject" is either in the LLM's head (generic) or in a custom orchestrator (MOOCO) — neither of which is "the kernel."

Fine, but the distinction is subtle and the docs don't defend it. A naive reader sees "kernel parses CARD.yml" and assumes leak. A single diagram showing "kernel gives file contents to orchestrator; orchestrator interprets" would close this.

**INTEREST-GATES vs. advertisements.** `INTEREST-GATES.yml` defines proximity-based visibility gates (world / in-room / within-room-N / near:Nm / adjacent / touch). Advertisements use score/condition/effect. These overlap: an advertisement can have a `condition:` that amounts to "player is in same room." Two related mechanisms, unclear composition. Does a gate short-circuit score evaluation? Does `score × gate_passed` compose? The kernel names both; I couldn't find the composition rule. Likely in a skill; doesn't belong in the kernel itself; but a pointer would help.

## Frontiers

**Driver-tier exercise.** Tiers 1-6 are defined (`ARCHITECTURE.md:106-114`) but primarily tier 4 (Cursor) and tier 6 (MOOCO) see use. Tier 5 (Claude Code) and tier 2 (basic CLI) are specification only. The "same skills, different mechanism" portability claim rests on tiers 2, 3, 5 actually being exercised. Until they are, portability is aspiration.

**Coherence Engine measurement.** The kernel repeats "the LLM is the Coherence Engine" as thesis (`README.md:3-13`, `ARCHITECTURE.md:420-430`). But there's no definition of what *degraded* coherence looks like, how you'd detect it, or what metrics matter. If coherence is the thesis, the absence of measurement is a gap. Candidate metrics: context-assembly hit-rate (did the LLM get the files it actually needed?), decision-consistency (same prompt, same state, same answer?), introspection reproducibility (can cursor-mirror replay the same timeline deterministically?).

## What I'd do differently

1. **Split ARCHITECTURE.md.** A short `OVERVIEW.md` (100 lines: three layers, directory-as-object, orchestrator types, nothing else) + the current `ARCHITECTURE.md` as appendix (heritage, magic dictionaries, Cursor optimization, driver tiers).
2. **Re-label "boring kernel."** Replace with "semantically neutral kernel" or "infrastructure-only kernel." Keeps the same content, sheds the mis-cue.
3. **Name the LLM-as-prototype-resolver move.** `cauldron/META-PLAN.md` §1.5 establishes it; the kernel should cite and own it. It's the move that makes filesystem-as-object actually *work* for LLMs (rather than just for Densmore's shell scripts).
4. **Add a diagram for "kernel routes advertisements; orchestrator interprets."** One mermaid. Closes the semantic-leak question.

## What I'm uncertain about

- The `constitution-core.md` contents. I cited it from tables; didn't deep-read. Any claims about "universal principles" are ~60% confident.
- Driver details. The specific capability matrices (`kernel/drivers/*.yml`) — not read this pass.
- Context-assembly and memory-management protocols. The summaries in ARCHITECTURE.md are clear; the actual protocol files might have enforcement details I missed.

## Cross-references

- Parent (root synthesis): `../REVIEW.2026-04-21.claude-opus-4.7.md`
- Related cluster: `../skills/REVIEW.2026-04-21.claude-opus-4.7.md` (ecosystem)
- Key down-link: `../skills/cursor-mirror/REVIEW.2026-04-21.claude-opus-4.7.md` (driver+introspection proof-of-life)
- Panel siblings invited: `kernel/REVIEW.2026-04-21.<other-model>.{yml,md}`

---

*Kernel does its job: stays out of the way, provides primitives, names tensions it doesn't solve. The main room for improvement is documentation pacing, not design.*
