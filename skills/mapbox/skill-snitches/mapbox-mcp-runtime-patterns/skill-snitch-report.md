# mapbox-mcp-runtime-patterns — skill-snitch report

**Trust** 🔵 BLUE · **Type** anthropic · **Executable files** 5 · **Evals** 4 · **License** MIT

**Upstream** `mapbox/mapbox-agent-skills` @ `aab3a6f` · **Scanned** 2026-09-20 by Don Hopkins

> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against
> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.

## What it is

MCP Server integration for agent frameworks: pydantic-ai, mastra, LangChain, CrewAI, smolagents, custom.

## Notable

The only skill in the corpus that ships executable code — 1,272 lines across five runnable
examples — and the code is exemplary on the thing that matters. Every example reads
MAPBOX_ACCESS_TOKEN from the environment, none hardcodes, and all five fail closed with a
raise or throw when it is absent. Every network destination is mcp.mapbox.com. This is the
skill most likely to be copied into production, and it is the one that earned the review.

## Measured surface

| Measure | Value |
|---|---|
| Files | 21 |
| SKILL.md | 198 lines |
| AGENTS.md | 454 |
| References | 8 — crewai.md, custom-agent.md, langchain.md, mastra.md, production.md, pydantic-ai.md, smolagents.md, use-cases.md |
| Executable code | 5 files, 1272 lines |
| Broken internal links | none |

### What the patterns found

| Probe | Hits | Reading |
|---|---|---|
| hardcoded access tokens | 0 | clean |
| shell-outs to network tools | 0 | clean |
| destructive or eval-shaped calls | 0 | clean |
| process spawns | 5 | present, in context |
| env-var token references | 55 | present, in context |
| agent-coercive directives | 0 | clean |
| explicit prohibitions | 7 | present, in context |
| user-location references | 1 | present, in context |
| OS permission references | 2 | present, in context |
| consent references | 0 | absent |
| privacy-law references | 0 | absent |

### Network destinations

Hosts appearing in executable code — the ones this skill can actually reach:

- `mcp.mapbox.com`


All first-party Mapbox.


Hosts named in prose and examples (9 distinct): `ai.pydantic.dev`, `console.mapbox.com`, `docs.crewai.com`, `docs.langchain.com`, `docs.mapbox.com`, `github.com`, `huggingface.co`, `mastra.ai`, `modelcontextprotocol.io`. Documentation text, not destinations.

## Findings

### LOW — npx-at-runtime

*safety · moves the tier*

**Where** `AGENTS.md:73, AGENTS.md:92, AGENTS.md:132, references/pydantic-ai.md:71`

**What** Documents spawning the MCP server with subprocess.Popen / spawn of npx @mapbox/mcp-server.

**Why it matters** The documented and correct way to run a local stdio MCP server, so this is not a
complaint. It is a surface worth stating plainly: npx resolves and executes a package from
the registry at run time, inside the agent's process tree. Pinning a version and
pre-installing is the hardening step for anyone running this unattended.

## Corpus-wide observations that also apply

- **MEDIUM · privacy-silence** — Across all twenty skills there is no guidance on data retention, minimization, anonymization, or GDPR/CCPA obligations.
- **INFO · no-allowed-tools** — Frontmatter carries name and description only.
- **LOW · postinstall-hook** — "postinstall": "node scripts/setup-hooks.js" — npm install runs code that writes an executable into .git/hooks.
- **INFO · eval-cost** — Evals are LLM-judged: claude-sonnet-5 answers (max_tokens 4096) and claude-sonnet-5 grades (max_tokens 2048), via @anthropic-ai/sdk, with every run reading the whole skill as input.

Full text and reasoning: [`../README.md`](../README.md).

## Verdict

🔵 BLUE — Safe, with a low-severity surface worth knowing about first.


1 finding recorded above, of which 1 safety-class. The badge answers whether this is safe to load, not whether anything was found — see `tier_basis` in `../findings.yml`.
