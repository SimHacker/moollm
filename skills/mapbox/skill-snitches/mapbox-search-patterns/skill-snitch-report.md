# mapbox-search-patterns — skill-snitch report

**Trust** 🟢 GREEN · **Type** anthropic · **Executable files** 0 · **Evals** 3 · **License** MIT

**Upstream** `mapbox/mapbox-agent-skills` @ `aab3a6f` · **Scanned** 2026-09-20 by Don Hopkins

> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against
> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.

## What it is

Choosing the right search tool and parameters: geocoding versus POI search versus discovery.

## Notable

A selection skill with an explicit decision matrix and a Common Mistakes section. No AGENTS.md, which makes the SKILL.md the whole story.

## Measured surface

| Measure | Value |
|---|---|
| Files | 5 |
| SKILL.md | 388 lines |
| AGENTS.md | absent |
| References | 3 — advanced-params.md, optimization-combining.md, workflows.md |
| Executable code | 0 files, 0 lines |
| Broken internal links | none |

### What the patterns found

| Probe | Hits | Reading |
|---|---|---|
| hardcoded access tokens | 0 | clean |
| shell-outs to network tools | 0 | clean |
| destructive or eval-shaped calls | 0 | clean |
| process spawns | 0 | absent |
| env-var token references | 0 | absent |
| agent-coercive directives | 0 | clean |
| explicit prohibitions | 0 | absent |
| user-location references | 5 | present, in context |
| OS permission references | 0 | absent |
| consent references | 0 | absent |
| privacy-law references | 0 | absent |

### Network destinations

None. This skill ships no executable code, so it reaches nothing.


Hosts named in prose and examples (2 distinct): `api.mapbox.com`, `docs.mapbox.com`. Documentation text, not destinations.

## Findings

Nothing specific to this skill. The corpus-wide observations below still apply.

## Corpus-wide observations that also apply

- **MEDIUM · privacy-silence** — Across all twenty skills there is no guidance on data retention, minimization, anonymization, or GDPR/CCPA obligations.
- **INFO · no-allowed-tools** — Frontmatter carries name and description only.
- **LOW · postinstall-hook** — "postinstall": "node scripts/setup-hooks.js" — npm install runs code that writes an executable into .git/hooks.
- **INFO · eval-cost** — Evals are LLM-judged: claude-sonnet-5 answers (max_tokens 4096) and claude-sonnet-5 grades (max_tokens 2048), via @anthropic-ai/sdk, with every run reading the whole skill as input.

Full text and reasoning: [`../README.md`](../README.md).

## Verdict

🟢 GREEN — Nothing here makes it unsafe to load or rely on.
