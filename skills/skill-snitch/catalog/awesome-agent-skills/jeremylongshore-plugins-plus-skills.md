# jeremylongshore/claude-code-plugins-plus-skills — Deep Survey

> 270 plugins, ~739 skills. Most ambitious community effort. But 98% are markdown templates, many batch-generated. The value is in the infrastructure, not the individual skills.

**Repo**: https://github.com/jeremylongshore/claude-code-plugins-plus-skills
**Stars**: ~1.3k | **License**: MIT | **Format**: SKILL.md (2026 schema)

## What It Actually Is

A pnpm monorepo with 22 category directories under `plugins/`, a CLI package manager (`ccpi`), an Astro marketplace website, Firebase hosting, and extensive documentation (80+ numbered docs). The "1,537 skills" headline needs decomposition — actual plugin count is ~270, each with 1-3 skills, plus a `skills/` directory and planned-skills inflation.

**98% of plugins are markdown-only instruction templates.** Not executable code. The security risk is what instructions they give Claude to do with its tools, not what the plugins themselves execute.

**~2% are real MCP servers** (7 defined in presets, TypeScript/Python via npx/uvx). These are the actual executable code that needs security audit.

## What's Worth Studying

### 1. Tool Scoping (`allowed-tools`)

Every SKILL.md declares its tool permissions:
```yaml
allowed-tools: Read, Write, Edit, Grep, Glob, Bash(git:*), Bash(docker:*)
```

This is a security primitive MOOLLM lacks. The namespace scoping (`Bash(crypto:arbitrage-*)`) limits what shell commands the skill can request. Worth adopting for MOOLLM CARD.yml — each skill declares its tool surface explicitly.

### 2. Security Framework

3-tier trust levels: Community (minimal review) → Verified (2+ maintainer reviews, 7-day public review, tests) → Featured (active maintenance, 10+ users). CI scanning: structure validation, secret detection, malicious pattern detection, path traversal detection. Threat model covers prompt injection, data exfiltration, supply chain. Documented but enforcement is unclear — Hall of Fame table is empty.

### 3. Beads Task Tracking

`bd` CLI for session task management. `bd ready` after context compaction. "Landing the plane" protocol requires git push before session ends. Similar to MOOLLM's `.moollm/session-log.md` + `hot.yml`.

## What's NOT Worth Studying

### Boilerplate Skills

Many SKILL.md files reference `{baseDir}/references/` and `{baseDir}/templates/` directories that don't exist. These are batch-generated templates, not hand-crafted skills. The quality is wide but shallow — lots of categories, little depth per category.

### Crypto/DeFi Plugins (~15)

Arbitrage finder, cross-chain bridge monitor, DeFi portfolio tracker, derivatives tracker. Detailed enough to be functional but come with "EDUCATIONAL PURPOSES ONLY" disclaimers contradicted by production-level implementation. Financial risk surface. Not interesting for MOOLLM.

### research-to-deploy (Enterprise $199/month)

Auto-deploys infrastructure from web search results. The most dangerous concept — terraform apply based on Googled best practices. Currently vaporware (no implementation found). The concept is a security concern regardless.

## Six Plugins Scanned

| Plugin | Category | Trust | Key Finding |
|--------|----------|-------|------------|
| access-control-auditor | security | MEDIUM-HIGH | Scoped Bash namespaces, structured CVSS reports |
| ci-cd-pipeline-builder | devops | MEDIUM | kubectl/docker access via namespace wildcards |
| overnight-dev-plugin | ai-agency | MEDIUM-LOW | Unsupervised 6-8h autonomous sessions with auto-commit |
| automl-pipeline-builder | ai-ml | MEDIUM | `Bash(python:*)` is unrestricted Python |
| research-to-deploy | skill-enhancers | LOW | Auto-deploy from web search — dangerous concept |
| arbitrage-opportunity-finder | crypto | LOW-MEDIUM | Exchange API keys, bot integration, flash loans |

## MOOLLM Takeaways

| What to Adopt | Where |
|---------------|-------|
| `allowed-tools` scoping in CARD.yml | skill, card skills — declare tool surface |
| 3-tier trust levels | skill-snitch catalog tiers (already similar) |
| CI secret/pattern detection | skill-snitch automation |
| Beads task tracking pattern | session-log, thoughtful-commitment |
| The "overnight-dev" concept (with guard rails) | session management design |

| What NOT to Adopt | Why |
|-------------------|-----|
| Batch-generated boilerplate skills | Quality over quantity |
| `{baseDir}` template references to nonexistent dirs | MOOLLM skills reference real files |
| Auto-deploy from web search | Dangerous, no sandbox |
| "EDUCATIONAL PURPOSES ONLY" on production code | Either it's educational or it's not |
