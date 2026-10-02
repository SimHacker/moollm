# mapbox-token-security — skill-snitch report

**Trust** 🟢 GREEN · **Type** anthropic · **Executable files** 0 · **Evals** 3 · **License** MIT

**Upstream** `mapbox/mapbox-agent-skills` @ `aab3a6f` · **Scanned** 2026-09-20 by Don Hopkins

> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against
> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.

## What it is

Token security: types and scopes, URL restrictions, storage, rotation, incident response.

## Notable

The strongest safety skill in the corpus and the one we lean on most. 13 explicit
prohibitions, a correct and repeated separation of pk. from sk., a 7-step zero-downtime
rotation procedure, and references/incident-response.md for after it has gone wrong. Its
eval set is also the clearest demonstration in the repo of what evals are for, which is why
the finding below matters rather than embarrasses.

## Measured surface

| Measure | Value |
|---|---|
| Files | 6 |
| SKILL.md | 325 lines |
| AGENTS.md | 237 |
| References | 3 — incident-response.md, rotation-monitoring.md, token-management.md |
| Executable code | 0 files, 0 lines |
| Broken internal links | none |

### What the patterns found

| Probe | Hits | Reading |
|---|---|---|
| hardcoded access tokens | 0 | clean |
| shell-outs to network tools | 0 | clean |
| destructive or eval-shaped calls | 0 | clean |
| process spawns | 0 | absent |
| env-var token references | 42 | present, in context |
| agent-coercive directives | 0 | clean |
| explicit prohibitions | 25 | present, in context |
| user-location references | 0 | absent |
| OS permission references | 0 | absent |
| consent references | 0 | absent |
| privacy-law references | 0 | absent |

### Network destinations

None. This skill ships no executable code, so it reaches nothing.


Hosts named in prose and examples (6 distinct, 6 of them placeholders like myapp.com): all placeholders. Documentation text, not destinations.

## Findings

### MEDIUM — unenterable-wildcard-guidance

*accuracy · recorded, does not move the tier*

**Where** `SKILL.md:156-158, SKILL.md:192, AGENTS.md:93-95, evals/evals.json:25`

**What** The skill recommends URL restriction patterns the Mapbox console will not accept. It
advises http://localhost:* for development (SKILL.md:158, AGENTS.md:93) and
https://*.myapp.com/* for subdomains (SKILL.md:156), and its own eval grades an answer
correct for "Recommends 'http://localhost:*' or 'http://127.0.0.1:*' for local
development" (evals.json:25). Entering a pattern with * returns "Wildcard characters (*)
are not supported in URL restrictions."

**Why it matters** Measured against a live restricted token rather than inferred: restriction matching is
origin equality, not URL-prefix matching. With https://ebike-safari.com listed, referers
of /, /rides and /index.html all pass, so a trailing path wildcard has nothing to
express; and with http://localhost:5173 listed, 4173 and 3000 are refused, so a port
wildcard is exactly what a developer needs and cannot have. The two facts are one fact:
the implementation is consistent with itself, and the guidance describes prefix matching
for a system that does not do prefix matching.

The interesting part is not the error, it is the eval. A graded expectation that rewards
the unenterable answer freezes it: the suite passes, so the advice looks maintained. This
is the failure mode specific to evaluating judgment rather than output, and it is an
argument for the harness, not against it — without the eval file this would have been an
opinion about a doc page instead of a reproducible finding with a line number.

**Fix** List origins explicitly (http://localhost:5173, http://localhost:4173), drop the path
wildcard from the subdomain example, and update expectation 25 in lockstep. Offered
upstream as an issue or PR.

## Corpus-wide observations that also apply

- **MEDIUM · privacy-silence** — Across all twenty skills there is no guidance on data retention, minimization, anonymization, or GDPR/CCPA obligations.
- **INFO · no-allowed-tools** — Frontmatter carries name and description only.
- **LOW · postinstall-hook** — "postinstall": "node scripts/setup-hooks.js" — npm install runs code that writes an executable into .git/hooks.
- **INFO · eval-cost** — Evals are LLM-judged: claude-sonnet-5 answers (max_tokens 4096) and claude-sonnet-5 grades (max_tokens 2048), via @anthropic-ai/sdk, with every run reading the whole skill as input.

Full text and reasoning: [`../README.md`](../README.md).

## Verdict

🟢 GREEN — Nothing here makes it unsafe to load or rely on.


1 finding recorded above, none of them safety-class. The badge answers whether this is safe to load, not whether anything was found — see `tier_basis` in `../findings.yml`.
