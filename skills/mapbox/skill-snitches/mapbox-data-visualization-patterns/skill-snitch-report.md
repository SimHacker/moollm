# mapbox-data-visualization-patterns — skill-snitch report

**Trust** 🟢 GREEN · **Type** anthropic · **Executable files** 0 · **Evals** 3 · **License** MIT

**Upstream** `mapbox/mapbox-agent-skills` @ `aab3a6f` · **Scanned** 2026-09-20 by Don Hopkins

> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against
> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.

## What it is

Choropleths, heat maps, 3D extrusions, data-driven styling, animation, and the performance envelope for each.

## Notable

Carries an explicit Data Size Rule, which is the kind of stated threshold an agent can actually act on.

## Measured surface

| Measure | Value |
|---|---|
| Files | 9 |
| SKILL.md | 302 lines |
| AGENTS.md | 537 |
| References | 6 — 3d-extrusions.md, animation.md, circles-lines.md, clustering.md, legends-use-cases.md, performance.md |
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
| user-location references | 0 | absent |
| OS permission references | 0 | absent |
| consent references | 0 | absent |
| privacy-law references | 0 | absent |

### Network destinations

None. This skill ships no executable code, so it reaches nothing.


Hosts named in prose and examples (6 distinct, 1 of them placeholders like myapp.com): `api.example.com`, `colorbrewer2.org`, `docs.mapbox.com`, `simple-statistics.github.io`, `turfjs.org`. Documentation text, not destinations.

## Findings

### LOW — cross-skill-link

*hygiene · recorded, does not move the tier*

**Where** `AGENTS.md:388`

**What** Points at mapbox-style-patterns's references/interactions.md by prose reference.

**Why it matters** Degrades gracefully — it names the target rather than linking it, so a skill copied out alone loses a pointer, not a page.

## Corpus-wide observations that also apply

- **MEDIUM · privacy-silence** — Across all twenty skills there is no guidance on data retention, minimization, anonymization, or GDPR/CCPA obligations.
- **INFO · no-allowed-tools** — Frontmatter carries name and description only.
- **LOW · postinstall-hook** — "postinstall": "node scripts/setup-hooks.js" — npm install runs code that writes an executable into .git/hooks.
- **INFO · eval-cost** — Evals are LLM-judged: claude-sonnet-5 answers (max_tokens 4096) and claude-sonnet-5 grades (max_tokens 2048), via @anthropic-ai/sdk, with every run reading the whole skill as input.

Full text and reasoning: [`../README.md`](../README.md).

## Verdict

🟢 GREEN — Nothing here makes it unsafe to load or rely on.


1 finding recorded above, none of them safety-class. The badge answers whether this is safe to load, not whether anything was found — see `tier_basis` in `../findings.yml`.
