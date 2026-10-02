# mapbox-navigation-patterns — skill-snitch report

**Trust** 🟢 GREEN · **Type** anthropic · **Executable files** 0 · **Evals** 18 · **License** MIT

**Upstream** `mapbox/mapbox-agent-skills` @ `aab3a6f` · **Scanned** 2026-09-20 by Don Hopkins

> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against
> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.

## What it is

Turn-by-turn directions, route optimization, live traffic, multi-stop routing, voice guidance, across web/iOS/Android.

## Notable

Carries 18 evals, by far the most in the corpus, and 9 explicit prohibitions — proportionate
for the skill whose output steers a moving vehicle. Also the only skill in the corpus that
uses the word consent. Includes references/android-performance-antipatterns.md, a file named
after its failure mode, which is a good habit.

## Measured surface

| Measure | Value |
|---|---|
| Files | 9 |
| SKILL.md | 148 lines |
| AGENTS.md | 449 |
| References | 6 — android-navigation-sdk.md, android-performance-antipatterns.md, best-practices.md, ios-navigation-sdk.md, ios-navigation-specialized.md, web-directions-api.md |
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
| explicit prohibitions | 4 | present, in context |
| user-location references | 0 | absent |
| OS permission references | 6 | present, in context |
| consent references | 8 | present, in context |
| privacy-law references | 0 | absent |

### Network destinations

None. This skill ships no executable code, so it reaches nothing.


Hosts named in prose and examples (3 distinct): `api.mapbox.com`, `docs.mapbox.com`, `github.com`. Documentation text, not destinations.

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
