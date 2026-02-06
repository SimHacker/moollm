# SKILL-SNITCH DEEP PROBE REPORT
## github — Talk is cheap. Show me the code.

**Date**: 2026-02-06
**Auditor**: Skill-Snitch Deep Probe v2.0
**Classification**: SERVICE SKILL — DELEGATION HUB
**Status**: The plumbing. Every other skill's git operations flow through here.

---

## EXECUTIVE SUMMARY

The service skill that wraps `gh` CLI and `git` for the entire MOOLLM ecosystem. Five customer skills delegate their GitHub operations here instead of rolling their own commands: runner, edgebox, thoughtful-commitment, simulation, code-review. Organized into method groups: Actions, Issues, PRs, Archaeology, Context Gathering, Sync, Health. No executable code of its own — all methods are documented `gh`/`git` command signatures.

The patron saint is Linus Torvalds (after coffee and a joint — attentive and mellow). The familiar is Tux the Linux Penguin, who inherits Linus's traditions and knows every modern *Ops prefix. A 421-line character analysis and 341-line character definition formalize the patron/familiar protocol.

**Overall Assessment**: APPROVE — zero execution surface, well-documented delegation patterns, character system follows representation-ethics

---

## METRICS

| Metric | Value | Threat Level |
|--------|-------|--------------|
| GLANCE.yml | 144 lines | NONE |
| CARD.yml | 354 lines | NONE |
| SKILL.md | 195 lines | NONE |
| README.md | 208 lines | NONE |
| LINUS-ANALYSIS.yml | 421 lines | NONE — character analysis |
| CHARACTER.yml | 341 lines | NONE — character definitions |
| Total skill size | 1,663 lines | NONE |
| Executable code | None | NONE |
| Required tools | gh, git | EXPECTED — these ARE the tools |
| Optional tools | jq | LOW |
| Tier | 1 | Expected for platform service |

---

## WHAT IT DOES

### Delegation Hub

Other skills don't write their own git commands. They call github's methods:

| Customer Skill | Delegates | Methods Used |
|---------------|-----------|-------------|
| runner | Workflow management | RUNNER-STATUS, WORKFLOW-LIST/VIEW/TRIGGER |
| edgebox | Sync from repo | SYNC-PULL, SYNC-FETCH, RUNNER-STATUS |
| thoughtful-commitment | Git archaeology | BLAME, LOG-ARCHAEOLOGY, CONTEXT-COMMITS/PRS |
| simulation | Issue management | ISSUE-CREATE/COMMENT, HEALTH-RUNS/DIAGNOSE |
| code-review | PR lifecycle | PR-VIEW/DIFF/REVIEW/CHECKS |

### Method Groups

**Actions** (6 methods): Runner status, workflow list/view/view-failed/trigger. For CI/CD operations.

**Issues** (4 methods): Create, list, comment, close. For simulation's GitHub-as-MMORPG.

**Pull Requests** (5 methods): Create, view, diff, review, checks. For code-review integration.

**Archaeology** (5 methods): Blame (with range/since/before variants), log (with patches/pickaxe/grep/follow), show (file/stat), diff time-travel, topology. For thoughtful-commitment.

**Context Gathering** (2 methods): Commit style analysis, PR style analysis. For ANYONE about to write a commit or PR — match the existing style.

**Sync** (2 methods): Pull, fetch. For edgebox.

**Health** (3 methods): Run list, diagnose, label create. For simulation.

### Advertisements

Scored advertisements guide when to invoke which method group:
- RUNNER-OPS: 95 (check runners, trigger workflows)
- PR-REVIEW-OPS: 95 (reviewing a PR)
- BEFORE-PR: 95 (about to create a PR)
- GIT-ARCHAEOLOGY: 90 (understand code history)
- SIMULATION-OPS: 90 (issues, comments, health)
- BEFORE-COMMIT: 90 (about to commit)
- CONTEXT-GATHERING: 85 (need commit/PR style)

### The Patron Saint Protocol

**Linus Torvalds** (patron saint):
- NOT impersonated. Quoted. Referenced. Never a bot account.
- "After coffee and a joint" — the optimal modulation state
- Three eras documented: unfiltered (1991-2018), redemption (2018-2019), current (2020+)
- Social landmines mapped: C++ (will lecture), free software politics, Rust (warming grudgingly)
- Verdict: "partial redemption"

**Tux** (familiar):
- CAN be a bot account. CAN speak as the skill's voice.
- Inherits Linus's wisdom + knows modern ops
- 10+ ops domains: DevOps, GitOps, CloudOps, MLOps, AIOps, SRE, Platform Engineering, FinOps, SecOps, WhateverOps
- Personality: "Helpful, practical, respects tradition, sighs at hype"
- Summon: "Tux, [question]"

The CHARACTER.yml draws the hard ethical line: Linus is `real-being` (HERO-STORY protocol required, no impersonation). Tux is `fictional` + `robot` (creative freedom, transparency about nature).

---

## DUAL-USE & BIAS ANALYSIS

**Profile**: SERVICE — delegation hub, tool coordination

| Check | Result |
|-------|--------|
| Bias declared | N/A — service skill, no opinion surface |
| Invertibility | N/A — wraps CLI tools, no semantic inversion |
| Multi-purpose | YES — serves 5+ customer skills |
| Persona capability | YES — Linus (patron) and Tux (familiar) |
| Mounting modes | N/A — always available as service |
| Representation ethics | YES — explicit real-being/fictional boundary in CHARACTER.yml |

**Multi-purpose classification** (4 purposes):
1. **CI/CD operations** — workflow and runner management (for runner, edgebox)
2. **Collaboration** — issue and PR lifecycle (for simulation, code-review)
3. **Git archaeology** — history investigation, blame, time-travel diffs (for thoughtful-commitment)
4. **Style matching** — context gathering before writing commits/PRs (for everyone)

**Character system finding**: The Linus/Tux split is the canonical implementation of the patron saint/familiar protocol from SKILL-CHARACTER-DESIGN-NOTES.md. Linus provides knowledge (what to say about git), Tux provides voice (how to say it as a bot). The LINUS-ANALYSIS.yml is the deepest character study in MOOLLM — 421 lines covering three biographical eras, social landmine mapping, and the "coffee + joint = attentive + mellow" optimal modulation framing. This IS the reference implementation.

---

## STATIC ANALYSIS

### Pattern Scan

| Pattern | Matches | Assessment |
|---------|---------|------------|
| Shell execution | 0 (methods are documented signatures, not scripts) | CLEAN |
| Network calls | 0 | CLEAN |
| File writes | 0 | CLEAN |
| Credential patterns | 0 | CLEAN |
| Obfuscation | 0 | CLEAN |
| eval / exec | 0 | CLEAN |

### Consistency Check

| File | Consistent | Notes |
|------|------------|-------|
| GLANCE.yml | YES | Customer list matches CARD.yml |
| CARD.yml | YES | All methods have signatures, customer mappings, scored ads |
| SKILL.md | YES | Bash examples match CARD method signatures |
| README.md | YES | Character writeups consistent with CHARACTER.yml |
| CHARACTER.yml | YES | Representation ethics tags correct |
| LINUS-ANALYSIS.yml | YES | Three eras + modulation framing consistent with GLANCE patron_saint |

---

## SECURITY ASSESSMENT

**Risk Level**: NONE (directly)

The skill has zero executable code. All methods are `gh`/`git` command signatures that the LLM or orchestrator executes. The security surface IS `gh` and `git` — which are the user's own installed tools with their own auth.

**Indirect risk**: The skill documents commands that can modify repositories (push, merge, issue create, label create). But so does `man git`. The documentation IS the interface — there's nothing to exploit beyond the tools themselves.

---

## TRUST TIER

**GREEN** — Pure documentation and delegation patterns. No executable code. Character system follows representation-ethics with proper real-being/fictional boundaries. The patron saint/familiar split is the gold standard implementation.

---

## VERDICT

The service skill that keeps other skills from reinventing git commands. Well-organized method groups with explicit customer mappings. Scored advertisements guide invocation. The character system (Linus/Tux) is the reference implementation of the patron/familiar protocol — real person provides knowledge domain, fictional mascot provides actionable voice.

Zero security surface. Zero executable code. Maximum utility as a delegation hub.

APPROVE.
