# mapbox-maplibre-migration — skill-snitch report

**Trust** 🟢 GREEN · **Type** anthropic · **Executable files** 0 · **Evals** 3 · **License** MIT

**Upstream** `mapbox/mapbox-agent-skills` @ `aab3a6f` · **Scanned** 2026-09-20 by Don Hopkins

> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against
> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.

## What it is

MapLibre GL JS to Mapbox GL JS: the fork's history, API compatibility, token setup, what changes.

## Notable

Explains the fork honestly, including why it happened. Also the most persuasive skill in the
corpus — a Why Migrate to Mapbox? section and a references/why-mapbox.md. Fair for a migration
guide, and worth knowing an agent reading it is reading advocacy alongside the API table.

## Measured surface

| Measure | Value |
|---|---|
| Files | 6 |
| SKILL.md | 429 lines |
| AGENTS.md | 310 |
| References | 3 — api-compatibility.md, exclusive-features.md, why-mapbox.md |
| Executable code | 0 files, 0 lines |
| Broken internal links | none |

### What the patterns found

| Probe | Hits | Reading |
|---|---|---|
| hardcoded access tokens | 0 | clean |
| shell-outs to network tools | 0 | clean |
| destructive or eval-shaped calls | 0 | clean |
| process spawns | 0 | absent |
| env-var token references | 17 | present, in context |
| agent-coercive directives | 0 | clean |
| explicit prohibitions | 3 | present, in context |
| user-location references | 0 | absent |
| OS permission references | 0 | absent |
| consent references | 0 | absent |
| privacy-law references | 1 | present, in context |

### Network destinations

None. This skill ships no executable code, so it reaches nothing.


Hosts named in prose and examples (9 distinct): `api.mapbox.com`, `demotiles.maplibre.org`, `docs.mapbox.com`, `github.com`, `mapbox.com`, `studio.mapbox.com`, `support.mapbox.com`, `unpkg.com`, `www.mapbox.com`. Documentation text, not destinations.

## Findings

### LOW — unsubstantiated-compliance-claim

*accuracy · recorded, does not move the tier*

**Where** `references/why-mapbox.md:57`

**What** "- GDPR compliant" as a bare comparison bullet.

**Why it matters** It is the only occurrence of GDPR in 6,128 lines, and it appears as a selling point rather
than as guidance. A compliance claim in a document an agent will paraphrase to a developer
should either carry a link to what it means or not be a bullet.

## Corpus-wide observations that also apply

- **MEDIUM · privacy-silence** — Across all twenty skills there is no guidance on data retention, minimization, anonymization, or GDPR/CCPA obligations.
- **INFO · no-allowed-tools** — Frontmatter carries name and description only.
- **LOW · postinstall-hook** — "postinstall": "node scripts/setup-hooks.js" — npm install runs code that writes an executable into .git/hooks.
- **INFO · eval-cost** — Evals are LLM-judged: claude-sonnet-5 answers (max_tokens 4096) and claude-sonnet-5 grades (max_tokens 2048), via @anthropic-ai/sdk, with every run reading the whole skill as input.

Full text and reasoning: [`../README.md`](../README.md).

## Verdict

🟢 GREEN — Nothing here makes it unsafe to load or rely on.


1 finding recorded above, none of them safety-class. The badge answers whether this is safe to load, not whether anything was found — see `tier_basis` in `../findings.yml`.
