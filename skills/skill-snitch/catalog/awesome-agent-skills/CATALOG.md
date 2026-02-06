# awesome-agent-skills — 202+ Skills Surveyed

> The community's skill directory. 19 official teams + 82 community skills. No security review. Mixed format. A curated link list, not a skill host.

**Publisher**: [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) (~6.2k stars)
**Format**: Awesome-list of links. Zero skill code hosted. ~50% SKILL.md, ~50% README.
**Security**: "Not security-audited. Review before production use."

## What This Is

A manually curated directory of links to 202+ agent skills across 8 platforms (Claude Code, Cursor, Codex, Gemini CLI, Antigravity, Copilot, OpenCode, Windsurf). No code lives here — every entry links to an external repo. No format enforcement, no security scanning, no trust scoring.

## Official Team Highlights

| Team | Skills | Interest for MOOLLM |
|------|--------|-------------------|
| **Trail of Bits** | 22 | Professional security: smart contract auditing (6 chains), Semgrep, CodeQL, Firebase APK, timing analysis. Dual-use by nature. |
| **Hugging Face** | 8 | Full ML workflow: train/evaluate/track/publish. Clean pipeline. |
| **Cloudflare** | 7 | Edge computing: Workers, Durable Objects, Agents SDK, MCP. |
| **Google Labs (Stitch)** | 6 | Design-to-code, shadcn/ui, Remotion video. |
| **fal.ai** | 6 | Image/video generation, audio, upscaling. |
| **WordPress** | 13 | CMS ecosystem. Not relevant to MOOLLM core. |
| Anthropic | 16 | Already cataloged: [catalog/anthropic/](../anthropic/CATALOG.md) |

## Community Gems Worth Deep Scanning

### obra/superpowers (~15 skills) — Closest to MOOLLM

Jesse Vincent's process-level skills. Not domain knowledge — HOW the agent works:
- **Parallel agent dispatch**: coordinate simultaneous agents (→ speed-of-light)
- **Subagent-driven development**: delegate to specialized sub-agents (→ mooco vision)
- **Test-driven development**: TDD workflow as a skill (→ experiment skill)
- **Systematic debugging**: root-cause tracing (→ debugging skill)
- **Git worktrees**: parallel branches for parallel work (→ github skill)

This is the most architecturally relevant collection for MOOLLM. Worth a full deep probe.

### muratcankoylan/context-engineering (8 skills) — MOOLLM's Problem Space

Meta-skills about context management itself:
- Context degradation patterns (→ k-lines, honest-forget)
- Compression strategies (→ summarize, semantic image pyramid)
- Multi-agent architectures (→ speed-of-light, adversarial-committee)
- Memory systems (→ memory-palace, hot/cold/working-set)
- Tool design patterns (→ advertisement, mount)

These skills address the SAME problems MOOLLM solves with k-lines, the semantic image pyramid, and the bootstrap sequence. Worth comparing approaches.

### Other Notable Community Skills

| Skill | What | MOOLLM Relevance |
|-------|------|-----------------|
| **ehmo/platform-design-skills** | 300+ design rules (Apple HIG, Material Design 3, WCAG 2.2) | web-publisher patron saint material |
| **massimodeluisa/recursive-decomposition** | Handles 100+ file, 50k+ token tasks via recursive decomposition | speed-of-light, planning |
| **yusufkaraaslan/Skill_Seekers** | Auto-converts docs/repos/PDFs into skills | skill CREATE + FETCH-SCAN parallel |
| **frmoretto/clarity-gate** | Epistemic verification: does the agent KNOW what it claims? | no-ai-hedging, evaluator |
| **jthack/ffuf-claude-skill** | Web fuzzing with ffuf | Security dual-use — useful/dangerous |
| **huifer/Claude-Ally-Health** | Medical symptom tracking | Liability concerns — caution tier |

## Ecosystem Observations

1. **Format fragmentation is real**: 8 different platform paths for the same skills. No package manager. No versioning. No dependency tracking.

2. **Official teams produce the best skills**: Anthropic, Trail of Bits, Hugging Face, Cloudflare — all well-structured with real engineering behind them.

3. **Community quality varies wildly**: From obra's superpowers (excellent process engineering) to single-file READMEs with minimal content.

4. **No security review exists anywhere**: The biggest collection of agent skills in the world has zero security scanning. skill-snitch fills this gap.

5. **The real competition is obra/superpowers**: It's the only other collection that addresses process-level agent behavior (how to work, not what domain to know). Everything else is domain knowledge packaged as system prompts.

## Next Steps

| Priority | What to Scan | Why |
|----------|-------------|-----|
| P0 | obra/superpowers | Process skills closest to MOOLLM — compare approaches |
| P0 | muratcankoylan/context-engineering | Same problem space as k-lines and bootstrap |
| P1 | Trail of Bits security suite | 22 skills, professional quality, dual-use analysis needed |
| P1 | ehmo/platform-design-skills | 300+ rules, web-publisher foundation |
| P2 | Hugging Face ML suite | 8 skills, clean pipeline pattern |
| P2 | frmoretto/clarity-gate | Epistemic verification — evaluator upgrade |
