# mapbox-android-patterns — skill-snitch report

**Trust** 🟢 GREEN · **Type** anthropic · **Executable files** 0 · **Evals** 6 · **License** MIT

**Upstream** `mapbox/mapbox-agent-skills` @ `aab3a6f` · **Scanned** 2026-09-20 by Don Hopkins

> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against
> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.

## What it is

Maps SDK integration for Android: install, markers, user location, custom data, camera, featureset interactions.

## Notable

Handles the mechanical half of location properly — 23 references to permissions, including
ACCESS_FINE_LOCATION, with a dedicated references/location-tracking.md. The corpus-wide
privacy-silence observation applies, but this skill is not where the OS-level flow is missing.

## Measured surface

| Measure | Value |
|---|---|
| Files | 9 |
| SKILL.md | 412 lines |
| AGENTS.md | 361 |
| References | 6 — annotations.md, camera-styles.md, compose.md, custom-data.md, interactions.md, location-tracking.md |
| Executable code | 0 files, 0 lines |
| Broken internal links | none |

### What the patterns found

| Probe | Hits | Reading |
|---|---|---|
| hardcoded access tokens | 0 | clean |
| shell-outs to network tools | 0 | clean |
| destructive or eval-shaped calls | 0 | clean |
| process spawns | 0 | absent |
| env-var token references | 5 | present, in context |
| agent-coercive directives | 0 | clean |
| explicit prohibitions | 2 | present, in context |
| user-location references | 11 | present, in context |
| OS permission references | 23 | present, in context |
| consent references | 0 | absent |
| privacy-law references | 0 | absent |

### Network destinations

None. This skill ships no executable code, so it reaches nothing.


Hosts named in prose and examples (5 distinct): `account.mapbox.com`, `api.mapbox.com`, `docs.mapbox.com`, `github.com`, `schemas.android.com`. Documentation text, not destinations.

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
