# SKILL-SNITCH DEEP PROBE REPORT
## micropolis — The filesystem is the city. Git is the multiverse.

**Date**: 2026-02-06
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: DESIGN SKILL — Status: DESIGNING
**Status**: Vision document and artifact archive. No executable code yet.

---

## EXECUTIVE SUMMARY

The most ambitious skill in MOOLLM, and the one that doesn't exist yet. Micropolis is the design specification for turning open source SimCity into a constructionist educational platform. The vision: MicropolisHub — Micropolis engine (C++/WebAssembly) + MOOLLM characters as AI tutors + mooco orchestrator (SvelteKit) + GitHub-as-MMORPG. All game state in git-controlled files. Branches are alternate timelines. Schools fork and own their instances.

The skill directory is currently a 12-file artifact archive documenting 35 years of SimCity heritage (1989-2026), from Will Wright's original through Don Hopkins's HyperLook/SimCityNet/OLPC ports to the MicropolisHub vision. Eight artifact files organize history, people, education philosophy, technical specs, connections to other ideas, plans, and unfulfilled dreams.

This is the design document for the platform that MOOLLM was built to enable.

**Overall Assessment**: APPROVE — pure documentation, zero execution surface, massive historical value

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| GLANCE.yml | 46 lines | NONE |
| CARD.yml | 105 lines | NONE |
| SKILL.md | 686 lines | NONE — design specification |
| README.md | present | NONE — mermaid diagrams |
| artifacts/INDEX.yml | index | NONE |
| artifacts/history.yml | version timeline | NONE |
| artifacts/people.yml | creator/pioneer bios | NONE |
| artifacts/education.yml | constructionist philosophy | NONE |
| artifacts/technical.yml | engine source map, save format | NONE |
| artifacts/connections.yml | related ideas, press | NONE |
| artifacts/plans.yml | scorecard, dreams | NONE |
| artifacts/unfulfilled-dreams.yml | 1990s visions | NONE |
| Total skill size | 12 files | NONE |
| Executable code | None | NONE |
| Required tools | None | NONE |
| Tier | 1 (designing) | N/A |

---

## WHAT IT DOES (OR WILL DO)

### MicropolisHub Vision

```
Micropolis Engine (C++/Emscripten/WebAssembly)
    ↓
MOOLLM (AI character orchestration — tutors, advisors, debate partners)
    ↓
mooco (SvelteKit multiplayer orchestrator)
    ↓
GitHub-as-MMORPG (the ultimate web stack)
```

**Core ideas**:
- Filesystem is the city (game state as files)
- Git is the multiverse (branches are timelines, PRs merge histories)
- Schools fork repos and own their instance
- AI tutors as MOOLLM characters who debate and advise
- "Nurturing environment, not a killer app"

### The Artifact Archive

Eight artifact files organize everything from the project's 35-year history:

| File | Content |
|------|---------|
| history.yml | 12 versions (1989-2026+), 6 YouTube demo videos |
| people.yml | Wright, Hopkins, Gingold, Robinett, Piaget, Papert, Kay, Minsky |
| education.yml | Constructionist philosophy, courseware ideas, newspaper metaphor |
| technical.yml | Save file binary format, C++ source map, SvelteKit components, tilesets |
| connections.yml | Stanford Generative Agents, Simlish, demoscene, Alan Kay, MOOLLM pitch |
| plans.yml | Delivered vs TODO scorecard, unfulfilled dreams |
| unfulfilled-dreams.yml | 1990s visions mapped to MOOLLM reality |

### Lineage Threads

Four historical threads converge:
1. **SimCity ports**: SimCity → HyperLook (1991) → SimCityNet (1993) → Micropolis/OLPC (2008)
2. **Will Wright**: SimCity (1989) → The Sims (2000)
3. **Method of Loci**: DreamScape (1995) → iLoci (2009) → MediaGraph (2010) → Bar Karma
4. **Web stack**: C++/SWIG/TurboGears → MicropolisCore/Emscripten/SvelteKit → GitHub-as-MMORPG

### Pioneers Referenced

Piaget (children construct knowledge), Papert (Logo, Mindstorms), Kay (Dynabook), Wright (SimCity, The Sims), Hopkins (DreamScape, Micropolis), Gingold (SimCity analysis), Robinett (Adventure, VR), Minsky (Society of Mind), Nelson (hypertext).

---

## DUAL-USE & BIAS ANALYSIS

**Profile**: DESIGN DOCUMENT — no executable capability, pure vision

| Check | Result |
|-------|--------|
| Bias declared | N/A — design specification, not active code |
| Invertibility | N/A — nothing to invert |
| Multi-purpose | YES (when built) — simulation, education, collaboration, AI tutoring |
| Persona capability | PLANNED — AI tutors as MOOLLM characters |
| Execution surface | ZERO — design docs only |

**Multi-purpose classification** (5 planned purposes):
1. **City simulation** — Micropolis engine as educational toy
2. **Constructionist education** — learn by building cities
3. **AI tutoring** — MOOLLM characters debate and advise
4. **Collaborative platform** — school-owned repos, multiplayer via GitHub
5. **Historical archive** — 35 years of SimCity/Micropolis documentation

**Design observation**: The "GitHub-as-MMORPG" concept makes GitHub's collaboration features (issues, PRs, comments, branches) into game mechanics. This is the most literal implementation of the adventure skill's "filesystem is a game world" principle — except the game world IS GitHub. When built, the dual-use surface will be significant: a SimCity that runs on GitHub with AI players is simultaneously an educational game, a software development platform, a social network, and an AI testbed.

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
| External references | Several (MicropolisCore GitHub, YouTube, Medium) | INFORMATIONAL — all public links |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | Status "designing" matches CARD and SKILL |
| CARD.yml | YES | MicropolisHub vision consistent across all files |
| SKILL.md | YES | Detailed spec matches CARD summary |
| README.md | YES | Mermaid diagrams visualize SKILL.md architecture |
| artifacts/ | YES | INDEX.yml matches actual files, links verified |

---

## SECURITY ASSESSMENT

**Risk Level**: NONE

Zero executable code. Zero tools required. Zero external connections at runtime. The skill is a curated artifact archive with a design specification. The external links are all to public GitHub repos, YouTube videos, and Medium posts.

**Future risk** (when built): The planned sister-script CLI, WebAssembly engine, and SvelteKit frontend will create a real execution surface. The git-multiverse concept (branches as timelines) will need careful access control for school-owned repos. AI tutor characters will need representation-ethics compliance.

---

## TRUST TIER

**GREEN** — Pure documentation. Historically significant as the design specification for the platform MOOLLM was built to enable. The artifact archive is a well-organized record of 35 years of educational simulation work.

---

## VERDICT

The skill that connects MOOLLM's philosophical roots (Papert's constructionism, Minsky's Society of Mind, Wright's Sims) to its most ambitious practical application. Currently a design document and historical archive — no executable code, no security surface, no risk.

The vision (SimCity + AI tutors + GitHub-as-MMORPG) is the most ambitious thing in MOOLLM. The artifacts are well-organized with an INDEX and consistent cross-references. The YouTube demo links and MicropolisCore repo references are the primary sources.

When this gets built, it will need a fresh Deep Probe. For now: all ambition, no attack surface.

APPROVE.
