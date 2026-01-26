# Gas Town Analysis: A Critical Examination

> *"I've never seen the code, and I never care to."*  
> — Steve Yegge, creator of Gas Town and Beads

**Status:** Complete  
**Date:** January 2026  
**Authors:** Don Hopkins, with Claude

---

## What This Directory Contains

A thorough analysis of Steve Yegge's Gas Town project, comparing it with MOOLLM's approach to multi-agent orchestration. These documents emerged from a deep-dive into the Gas Town codebase (`gastown/internal/`) and Steve's public writings.

| Document | Purpose |
|----------|---------|
| [GASTOWN-VS-MOOLLM-ANALYSIS.md](GASTOWN-VS-MOOLLM-ANALYSIS.md) | Detailed technical comparison |
| [YEGGE-ARC-ANALYSIS.md](YEGGE-ARC-ANALYSIS.md) | Steve's trajectory from Sourcegraph to shitcoin |
| [SPEED-OF-LIGHT-MEETS-CARRIER-PIGEONS.md](SPEED-OF-LIGHT-MEETS-CARRIER-PIGEONS.md) | Why internal simulation beats external IPC |
| [MOOLLM-TASK-TRACKING-DESIGN.md](MOOLLM-TASK-TRACKING-DESIGN.md) | Why "bead" is the wrong abstraction |
| [CONSTRUCTIONIST-TERMINOLOGY.md](CONSTRUCTIONIST-TERMINOLOGY.md) | Better vocabulary from Minsky, Papert, Kay, Wright |
| [BEADS-2026-01.md](BEADS-2026-01.md) | Initial research on the bead concept |
| [BEAD-ORCHESTRATION.yml](BEAD-ORCHESTRATION.yml) | YAML Jazz exploration of messaging |
| [GASTOWN-HN-POST.txt](GASTOWN-HN-POST.txt) | Draft HN response |

---

## Executive Summary

**Gas Town is wrong.** Not "optimized for different use cases" — just wrong.

### The Problems

1. **Invented terminology hostile to LLMs**
   - "bead", "polecat", "wisp", "GUPP", "MEOW"
   - Near-zero training data presence
   - Every use costs tokens explaining

2. **Shell-out architecture that wastes resources**
   - Go code spawns Python CLI to read JSONL from disk
   - Three language hops to read a file
   - "Abundant tokens" is not a feature, it's waste

3. **"Never look at the code" cowardice**
   - 225k lines of Go for an issue tracker
   - Creator has never read it
   - Can't dogfood what you won't examine

4. **Unfalsifiable gatekeeping**
   - "You're not Stage 7 yet"
   - Every criticism deflected onto the user
   - No metrics, no receipts, no accountability

5. **Crypto pump-and-dump ethics**
   - Promoted $GAS memecoin
   - Collected $238k+ in fees
   - Token collapsed 97%
   - "It's not a rug pull" is not a defense

### The ONE Useful Insight

Work should persist in git.

That's it. That's the insight. You could implement it with `gh issue` in 4 lines:

```bash
gh issue create --title "Task" --label "moollm"
gh issue edit 123 --milestone "Sprint-1"
gh issue edit 123 --assignee @worker
gh issue close 123 --comment "Done"
```

Instead, Gas Town has 225k lines of unread Go.

---

## On Steve Yegge

I've followed Steve's writing for decades. His rants on Lisp, Emacs, and software development shaped how I think about programming. "Execution in the Kingdom of Nouns" is a classic. The Google Platform Rant changed how the industry thinks about APIs.

That Steve — the one who thought carefully about language design, who wrote clearly about complex ideas, who held himself to intellectual standards — deserves respect.

But that Steve seems to be gone.

### The Arc

| Period | Role | What Happened |
|--------|------|---------------|
| 2006-2022 | Engineer at Google/Amazon | Influential blog posts, real systems |
| 2022-2024 | Head of Engineering, Sourcegraph | Led Cody AI development |
| 2024 | IC at Sourcegraph | Stepped down from leadership |
| 2025 | Left Sourcegraph | "Swinging big" |
| 2025-2026 | Solo developer | 225k unread lines, vibe-coded slop |
| 2026 | Crypto promoter | $GAS pump-and-dump |

The trajectory is concerning: declining institutional accountability, declining technical rigor, declining ethical standards.

### The Crypto Situation

From Sean Goedecke's analysis:

> "$GAS has no connection to Gas Town functionality. Buying the token provides no additional capabilities — it merely siphons money to Yegge while enriching early coin holders."

Steve knew what BAGS was — he wrote a Medium post explaining the mechanism. Then promoted anyway. The token collapsed 97%.

This isn't tangential to evaluating Gas Town. When someone promotes worthless tokens to their audience and profits from the dump, their technical recommendations deserve extra scrutiny.

---

## MOOLLM's Alternative

### Intellectual Foundations

MOOLLM builds on 60+ years of proven patterns:

| Foundation | Source | Training Presence |
|------------|--------|-------------------|
| Prototype delegation | Self (Ungar & Smith) | Deep → became JavaScript |
| Rooms and objects | LambdaMOO, Zork, MUDs | Deep |
| Advertisement coordination | The Sims (Will Wright) | Deep — $5B+ franchise |
| K-lines and activation | Minsky's Society of Mind | Foundational |
| YAML with comments | Kubernetes, CI/CD | Ubiquitous |

### Architecture Difference

| Aspect | Gas Town | MOOLLM |
|--------|----------|--------|
| Multi-agent | External processes, IPC overhead | Speed-of-light: many agents, one LLM call |
| Persistence | Custom JSONL, shell-outs | Git + YAML files (or GitHub Issues) |
| Vocabulary | Invented jargon | Constructionist tradition |
| Code review | "Never look at it" | Every line reviewed |
| Accountability | "You're not ready" | Rubrics, metrics, receipts |

### Vocabulary

Instead of invented terms, use vocabulary LLMs know:

| Gas Town | Better Term | Source |
|----------|-------------|--------|
| bead | **issue** | GitHub |
| molecule | **workflow** | GitHub Actions |
| convoy | **milestone** | GitHub |
| hook | **assignee** | GitHub |
| polecat | **worker** | English |
| GUPP | *delete* | — |

Or use constructionist terms: **action** (Sims), **goal** (Minsky), **procedure** (Papert), **slot** (Self).

---

## The Car Park Capital Parallel

There's a satirical indie game called [Car Park Capital](https://store.steampowered.com/app/2507670/Car_Park_Capital/) that perfectly captures what Gas Town represents:

> "You've been hired by Big Auto to unleash the Freedom of Car Dependency on unsuspecting townsfolk! Spread glossy pro-car propaganda, outsmart those pesky anti-petrol protesters, and transform quiet neighborhoods into your parking empire!"

| Car Park Capital (Satirical) | Gas Town (Unironic) |
|------------------------------|---------------------|
| "Unleash the Freedom of Car Dependency" | "Unleash abundant token usage" |
| "Spread pro-car propaganda" | "Stage 8 developer" gatekeeping |
| "Outsmart anti-petrol protesters" | Dismiss critics as "not ready" |
| "Drill for oil" | Mine crypto ($GAS) |

**The critical difference:** Car Park Capital knows it's satire. Gas Town has zero self-awareness.

Steve Yegge is the "carbrain" NPC that Car Park Capital satirizes — the guy who thinks the solution to traffic is always more lanes, more parking, more cars.

---

## Conclusions

1. **Gas Town's architecture is wrong.** Shell-outs, invented vocabulary, and unread code are not features.

2. **The "abundant tokens" claim is a lie.** Parallelism multiplies costs. Efficient parallelism requires efficiency, not abundance.

3. **"Never look at the code" is cowardice.** You can't dogfood what you won't examine.

4. **The vocabulary is hostile to LLMs.** Use GitHub terms or constructionist vocabulary — anything with actual training data presence.

5. **The crypto situation reveals judgment.** When someone promotes tokens to their audience and profits from the collapse, their technical recommendations deserve scrutiny.

6. **The ONE useful insight is trivial.** "Work persists in git" could be implemented with `gh issue` in 4 lines.

---

## What MOOLLM Takes From This

- **Nothing from Gas Town's implementation.** It's vibe-coded slop.
- **The obvious insight about persistence.** Which we already had.
- **A lesson about accountability.** MOOLLM provides rubrics, metrics, and receipts.
- **A vocabulary analysis.** Use terms that LLMs know.

---

## A Note on Respect

Steve Yegge's early work deserves respect. His rants shaped a generation of programmers. The ideas about the Eval Empire, about language design, about platforms — these were real contributions.

Respecting someone's past work doesn't mean accepting their current work uncritically. It means holding them to the standards they once demonstrated they could meet.

Gas Town doesn't meet those standards. The crypto situation violates them entirely.

The Steve who wrote about Lisp and Emacs would be embarrassed by the Steve who promotes memecoins and 225k lines of unread Go.

---

## See Also

- [Gas Town GitHub](https://github.com/steveyegge/gastown)
- [Sean Goedecke: "Crypto grifters are recruiting open-source AI developers"](https://www.seangoedecke.com/gas-and-ralph/)
- [HN Discussion: "Welcome to Gas Town"](https://news.ycombinator.com/item?id=46458936)
