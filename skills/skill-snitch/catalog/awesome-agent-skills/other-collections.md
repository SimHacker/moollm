# Other Agent Skill Collections

> Three more collections surveyed. The ecosystem is growing fast.

## travisvn/awesome-claude-skills (~6.5k stars)

**What**: Curated link list of Claude-specific skills. Official + community.
**Format**: Links to GitHub repos. SKILL.md spec.
**Security**: Warning section on arbitrary code execution. "Only install skills from trusted sources." No automated review.
**Hosts code**: No — links only.
**Overlap**: References Anthropic, obra/superpowers, Trail of Bits — everything we already cataloged.
**Verdict**: Useful as discovery index but redundant with VoltAgent's awesome-agent-skills. Notable for the security warning section — they at least acknowledge the risk.
**Repo**: https://github.com/travisvn/awesome-claude-skills

## jeremylongshore/claude-code-plugins-plus-skills (~1.3k stars)

**What**: The most ambitious community collection. 1,537 agent skills (1,298 standalone + 239 embedded in plugins). 270 plugins. Full source code hosted.
**Format**: SKILL.md spec (2026 schema compliant). Two types: AI Instruction Plugins (98%, markdown) + MCP Server Plugins (2%, TypeScript).
**Security**: User security guide, security policy, code of conduct, `ccpi validate` structural validator. Richard Hightower's reviews drove 4,300+ lines of fixes.
**Hosts code**: YES — full source in `plugins/` directory.
**Package manager**: `@intentsolutionsio/ccpi` (npm). `ccpi search`, `ccpi install`, `ccpi update`.

**Notable**:
- Skills Powerkit (first Agent Skills plugin, Oct 2025)
- Learning Lab (90+ pages, 11 interactive Jupyter notebooks)
- Production playbooks (11 guides, ~53,500 words)
- Website marketplace: claudecodeplugins.io
- Tool permissions system (`allowed-tools`)
- External plugin sync (`sources.yaml`)

**MOOLLM relevance**: The `ccpi` package manager is doing what MOOLLM's `skill` skill should do — search, install, update, validate. The `allowed-tools` permission system parallels gno's `Bash(gno:*)` scoping. The 2026 schema compliance is worth studying for compatibility.

**Worth deep scanning**: YES — 1,537 skills with hosted code is a goldmine AND a risk. skill-snitch should batch-scan this.

## agent-skills.md Marketplace (~13,295 skills)

**What**: Web marketplace indexing skills from GitHub repos across 10+ platforms.
**Format**: SKILL.md spec (YAML frontmatter required).
**Security**: Submission-based curation. No automated security review.
**Hosts code**: No — indexes GitHub repos, links to source.
**Scale**: 13,295 skills across 266 pages. The largest collection by far.

**Platforms supported**: VS Code, Gemini CLI, GitHub, Goose, Amp, Cursor, Claude Code, Claude, OpenAI Codex, Factory.

**MOOLLM relevance**: At 13k+ skills, this is where skill-snitch becomes ESSENTIAL infrastructure. The ClawHub malware rate was 13.5% (386/2,857). If the same rate applies here, there could be ~1,800 malicious skills in this marketplace. Nobody is scanning them.

**Worth deep scanning**: YES — the scale demands automated scanning. This is the consumer reports mission.

## Ecosystem Scale

| Collection | Skills | Hosted | Security |
|-----------|--------|--------|----------|
| Anthropic official | 16 | Yes | Internal review |
| VoltAgent awesome | 202+ | No (links) | "Not audited" |
| travisvn awesome | ~100 | No (links) | Warnings only |
| jeremylongshore plugins | 1,537 | Yes | Validator + guides |
| agent-skills.md | 13,295 | No (index) | Submission curation |
| openclaw/ClawHub | ~2,857 | Yes | None (13.5% malware) |
| **Total known ecosystem** | **~18,000+** | — | **Mostly unaudited** |

skill-snitch is the only security scanner designed for this ecosystem.
