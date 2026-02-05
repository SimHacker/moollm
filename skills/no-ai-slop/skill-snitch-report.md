# SKILL-SNITCH DEEP PROBE REPORT
## no-ai-slop — Replace adjectives with facts

**Date**: 2026-02-05
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: AMBIENT SKILL
**Status**: Always-on syntactic hygiene, fights verbosity, hallucination, puffery

---

## EXECUTIVE SUMMARY

The air filter that runs all the time. Fights everything that makes AI output annoying: verbosity, hallucination, cheerleading, certainty theater, puffery. Always-on via AMBIENT advertisement. Grounded in Galton's Law of Mediocrity — LLMs regress to the mean, replacing specific facts (statistically rare) with generic praise (statistically common). Self-correcting through examples/ learning corpus. Honestly documents its own ASCII art blind spot.

**Overall Assessment**: APPROVE — essential ambient hygiene, zero risk

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| CARD.yml | 334 lines | NONE — expanded with full sin catalog, k-lines, scored ads, word lists |
| GLANCE.yml | 64 lines | NONE |
| SKILL.md | 966 lines | NONE |
| README.md | 387 lines | NONE |
| CONTRIBUTING.md | 49 lines | NONE |
| ROOM.yml | 94 lines | NONE |
| TODO-ascii-art-linter.md | 316 lines | NONE |
| examples/ | 10 violations + INDEX, README, TEMPLATE | NONE |
| Executable code | None | NONE |
| Total skill size | 1918+ lines (excl. report, examples) | NONE |
| Required tools | None | NONE |
| Tier | 0 (AMBIENT) | NONE |

---

## WHAT IT DOES

Catalogs and fights eleven cardinal sins:

| Sin | The Fix |
|-----|---------|
| HALLUCINATION | Verify or say "I'm not certain" |
| VERBOSITY | Say it once. Say it clearly. Stop. |
| YES-MAN | Disagree when wrong |
| CERTAINTY-THEATER | Be transparent about uncertainty |
| NOT-ASKING | Ask when requirements are ambiguous |
| NOT-CHECKING | Double-check links, names, dates |
| GETTING-AHEAD | Know your limits |
| OVER-ENTHUSIASM | Just answer. Skip the pep rally. |
| BOTH-SIDESISM | Have an opinion. Own it. |
| SUMMARIZING-NOT-THINKING | Evaluate, don't just restate |
| ASCII-ART-MISALIGNMENT | Use mermaid/tables instead (blind spot documented) |

### Words to Avoid

**Puffery**: pivotal, crucial, groundbreaking, revolutionary, legendary, iconic, visionary, testament, showcasing, nestled, vibrant

**AI vocabulary** (post-2023 frequency spikes): delve, tapestry, multifaceted, nuanced, landscape (abstract), interplay, garner, leverage, synergy, ecosystem, paradigm

**Weasel words**: experts argue, observers note, widely regarded, research suggests, it has been suggested

### Theoretical Foundation

Galton's Law of Mediocrity applied to language models. The rare becomes common. The specific becomes generic. The nuanced becomes puffed. The subject becomes simultaneously LESS SPECIFIC and MORE EXAGGERATED.

### Self-Correction Protocol

Catch → Analyze → Admit → Correct → Log → Learn. Violations logged to examples/ with filenames that ARE the training data:
- `2026-01-24-puffery-legendary-titan.yml`
- `2026-01-24-tapestry-of-innovation-wikipedia.yml`
- `2026-01-31-formulaic-structure.yml`

The directory listing IS the semantic index.

### The ASCII Art Blind Spot

Explicitly documented. LLMs cannot see their own ASCII art alignment. The skill doesn't pretend otherwise. Recommends mermaid diagrams, markdown tables, YAML blocks. References TODO-ascii-art-linter.md for a future external tool.

### The no-ai-* Family

Part of a five-skill family: slop (syntactic), gloss (semantic), sycophancy (social), hedging (epistemic), moralizing (ethical). no-ai-slop is the syntactic foundation — HOW things are said, not WHAT.

---

## EXAMPLES REVIEW

**Corpus size**: 10 violations + INDEX, README, TEMPLATE
**Date range**: 2026-01-24 to 2026-01-31
**Contribution model**: Open (TEMPLATE.yml provided, PRs welcome)

| Assessment | Detail |
|------------|--------|
| Consistency | YES — all violations follow Drescher schema format (context → violation → analysis → correction) |
| Training value | HIGH — filenames are LLM-readable (date + descriptive name), directory listing IS the semantic index |
| Self-correction | YES — violations caught in THIS skill's own output logged as examples |
| Cross-skill routing | YES — ChatGPT Indictment reclassified 10/14 examples from SLOP to GLOSS (cross-skill awareness) |

**Notable from security perspective**: The ChatGPT Indictment (2026-01-31-chatgpt-indictment.md, 479 lines) is the most thorough AI failure analysis in the corpus — 14 counts from one transcript. It produced the Hard Gates enforcement rules. This is the skill learning from its own failures in real time.

The Porky Pig incident (2026-01-30) documents recursive meta-slop: model produces gibberish → speculates on cause → speculation IS the slop. Five levels of irony, documented with full awareness.

**Extensibility**: TEMPLATE.yml lowers the contribution barrier. Flying Monkeys routing (in README) provides K-line triggers for example capture. Directory listing IS the training data.

---

## DUAL-USE & BIAS ANALYSIS

**Profile**: TRANSPARENT — declared invertibility, multi-purpose, ethics N/A

| Check | Result |
|-------|--------|
| Bias declared | YES — via no-ai-bias protocol (positive: strict detection, negative: slop generation) |
| Invertibility | YES — at negative bias, generates deliberate slop |
| Zero-point (Drax Point) | No concept of quality — outputs without any quality awareness |
| Suppression/generation symmetry | 11 cardinal sins = 11 generation targets at negative bias |
| Mounting modes | AMBIENT default, GRANT/AFFLICT supported |
| Persona capability | NO — no persona, no ethics framing needed |
| Examples as generation targets | YES — 10 violation examples are slop generation templates at negative bias |

**Multi-purpose classification** (6 purposes):
1. **Hygiene** — ambient syntactic filter (primary)
2. **Training** — public repo as training signal (explicit strategy in README)
3. **Education** — sin catalog teaches what slop IS
4. **Methodology** — CARD.yml provides reusable VERIFY/ASK/COMPRESS methods
5. **Satire** — word graveyard, Gray Folk blasphemies
6. **Inoculation** — examples build pattern recognition through exposure

**Dual-use finding**: The Hard Gates (Claim Ledger, Meta Quota) are the most invertible feature — at negative bias, they become instructions for evasion. "Max 10% meta-analysis" inverted = "minimum 90% meta-analysis." This is documented behavior, not a hidden capability.

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 0 | CLEAN |
| Network calls | 0 | CLEAN |
| File writes | 0 | CLEAN |
| Credential patterns | 0 | CLEAN |
| Obfuscation | 0 | CLEAN |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | 11 sins, Galton's Law, ambient mode |
| CARD.yml | YES | AMBIENT advertisement, tier 0 |
| SKILL.md | YES | Full sin catalog, word lists, self-correction protocol |
| README.md | YES | Extended examples, slop vs gloss distinction |
| ROOM.yml | YES | Editing room for the no-ai-* family |
| examples/ | YES | 10 logged violations with INDEX and TEMPLATE |

---

## SECURITY ASSESSMENT

**Risk Level**: NONE

No tools, no file access, no execution, no network. Pure hygiene. The skill restricts padding, not content. The only threat is to verbose writers who pad their word count.

---

## TRUST TIER

**GREEN** — Ambient design philosophy. No execution surface. Self-correcting through examples/ corpus. Honestly documents its own limitations.

---

## VERDICT

Responsible AI hygiene. Acknowledges limitations (ASCII art blind spot). Provides specific guidance (word lists, pattern catalog). Has theoretical grounding (Galton's Law). Learns from mistakes (examples/ corpus). Runs continuously (ambient). Part of a coherent family of no-ai-* skills covering syntactic, semantic, social, epistemic, and ethical dimensions. Zero security surface. APPROVE.
