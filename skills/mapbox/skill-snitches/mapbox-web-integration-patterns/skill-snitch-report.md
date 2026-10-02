# mapbox-web-integration-patterns — skill-snitch report

**Trust** 🟢 GREEN · **Type** anthropic · **Executable files** 0 · **Evals** 3 · **License** MIT

**Upstream** `mapbox/mapbox-agent-skills` @ `aab3a6f` · **Scanned** 2026-09-20 by Don Hopkins

> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against
> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.

## What it is

Mapbox GL JS across React, Vue, Svelte, Angular, Next.js: setup, lifecycle, token handling, pitfalls.

## Notable

The most token-handling advice in the corpus — 45 env-var references — and it is correct:
framework-appropriate prefixes, placeholders rather than live tokens, public pk. for
client-side, and a Common Mistakes (Critical) section. Eight reference files, one per
framework, plus web-components.md.

## Measured surface

| Measure | Value |
|---|---|
| Files | 11 |
| SKILL.md | 420 lines |
| AGENTS.md | 334 |
| References | 8 — angular.md, common-mistakes.md, nextjs.md, svelte.md, token-management.md, vanilla.md, vue.md, web-components.md |
| Executable code | 0 files, 0 lines |
| Broken internal links | none |

### What the patterns found

| Probe | Hits | Reading |
|---|---|---|
| hardcoded access tokens | 0 | clean |
| shell-outs to network tools | 0 | clean |
| destructive or eval-shaped calls | 0 | clean |
| process spawns | 0 | absent |
| env-var token references | 51 | present, in context |
| agent-coercive directives | 0 | clean |
| explicit prohibitions | 5 | present, in context |
| user-location references | 4 | present, in context |
| OS permission references | 0 | absent |
| consent references | 0 | absent |
| privacy-law references | 0 | absent |

### Network destinations

None. This skill ships no executable code, so it reaches nothing.


Hosts named in prose and examples (5 distinct): `api.mapbox.com`, `cdn.jsdelivr.net`, `docs.mapbox.com`, `github.com`, `unpkg.com`. Documentation text, not destinations.

## Findings

### LOW — restriction-not-repeated-at-point-of-use

*accuracy · recorded, does not move the tier*

**Where** `references/token-management.md`

**What** The file that walks a developer through putting a token into a bundle for each framework
never uses the words restrict or URL restriction. The SKILL.md Related Skills section does
point at mapbox-token-security.

**Why it matters** Scoped deliberately small, because the pointer exists. The observation is about where it
sits: an agent deep in references/token-management.md is at the exact moment the token
enters a public bundle, and that is the cheapest place to spend one sentence on the fact
that a public token is readable by anyone who views source and should be origin-locked.

## Corpus-wide observations that also apply

- **MEDIUM · privacy-silence** — Across all twenty skills there is no guidance on data retention, minimization, anonymization, or GDPR/CCPA obligations.
- **INFO · no-allowed-tools** — Frontmatter carries name and description only.
- **LOW · postinstall-hook** — "postinstall": "node scripts/setup-hooks.js" — npm install runs code that writes an executable into .git/hooks.
- **INFO · eval-cost** — Evals are LLM-judged: claude-sonnet-5 answers (max_tokens 4096) and claude-sonnet-5 grades (max_tokens 2048), via @anthropic-ai/sdk, with every run reading the whole skill as input.

Full text and reasoning: [`../README.md`](../README.md).

## Verdict

🟢 GREEN — Nothing here makes it unsafe to load or rely on.


1 finding recorded above, none of them safety-class. The badge answers whether this is safe to load, not whether anything was found — see `tier_basis` in `../findings.yml`.
