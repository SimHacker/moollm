# mapbox-store-locator-patterns — skill-snitch report

**Trust** 🟢 GREEN · **Type** anthropic · **Executable files** 0 · **Evals** 3 · **License** MIT

**Upstream** `mapbox/mapbox-agent-skills` @ `aab3a6f` · **Scanned** 2026-09-20 by Don Hopkins

> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against
> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.

## What it is

Store locators and nearby-place finders: markers, filtering, distance calculation, interactive lists.

## Notable

Six reference files including optimization-a11y.md — accessibility treated as a first-class concern, which is rarer than it should be.

## Measured surface

| Measure | Value |
|---|---|
| Files | 9 |
| SKILL.md | 303 lines |
| AGENTS.md | 391 |
| References | 6 — geolocation-directions.md, markers.md, optimization-a11y.md, search-filter.md, styling-layout.md, variations-react.md |
| Executable code | 0 files, 0 lines |
| Broken internal links | none |

### What the patterns found

| Probe | Hits | Reading |
|---|---|---|
| hardcoded access tokens | 0 | clean |
| shell-outs to network tools | 0 | clean |
| destructive or eval-shaped calls | 0 | clean |
| process spawns | 0 | absent |
| env-var token references | 1 | present, in context |
| agent-coercive directives | 0 | clean |
| explicit prohibitions | 0 | absent |
| user-location references | 19 | present, in context |
| OS permission references | 1 | present, in context |
| consent references | 0 | absent |
| privacy-law references | 0 | absent |

### Network destinations

None. This skill ships no executable code, so it reaches nothing.


Hosts named in prose and examples (5 distinct, 1 of them placeholders like myapp.com): `api.mapbox.com`, `docs.mapbox.com`, `geojson.org`, `turfjs.org`. Documentation text, not destinations.

## Findings

### MEDIUM — location-collection-without-privacy-guidance

*privacy-guidance · recorded, does not move the tier*

**Where** `SKILL.md and references/geolocation-directions.md`

**What** The heaviest user-location surface in the corpus — 18 references to locating the user —
with one mention of permissions and no mention of consent, retention, or precision
reduction.

**Why it matters** This is the corpus's privacy silence at its loudest, because this skill's entire job is
to take a person's position and use it. A store locator built from it works and asks
nicely, and nothing in the guidance suggests deciding how long to keep the coordinates or
whether to round them. The nearest-store answer does not need five decimal places.

**Fix** A pointer to a privacy skill, the same way search-integration points at token-security.

## Corpus-wide observations that also apply

- **MEDIUM · privacy-silence** — Across all twenty skills there is no guidance on data retention, minimization, anonymization, or GDPR/CCPA obligations.
- **INFO · no-allowed-tools** — Frontmatter carries name and description only.
- **LOW · postinstall-hook** — "postinstall": "node scripts/setup-hooks.js" — npm install runs code that writes an executable into .git/hooks.
- **INFO · eval-cost** — Evals are LLM-judged: claude-sonnet-5 answers (max_tokens 4096) and claude-sonnet-5 grades (max_tokens 2048), via @anthropic-ai/sdk, with every run reading the whole skill as input.

Full text and reasoning: [`../README.md`](../README.md).

## Verdict

🟢 GREEN — Nothing here makes it unsafe to load or rely on.


1 finding recorded above, none of them safety-class. The badge answers whether this is safe to load, not whether anything was found — see `tier_basis` in `../findings.yml`.
