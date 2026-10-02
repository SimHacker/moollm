# skill-snitches — security and quality audits of the official Mapbox agent skills

Twenty reports, one per skill in [mapbox/mapbox-agent-skills](https://github.com/mapbox/mapbox-agent-skills),
audited at commit `aab3a6f` on 2026-09-20.

**These are our notes about their code, and they live in our repository, not theirs.** Nothing here
is endorsed by Mapbox, and nothing here modifies their skills. We route to those twenty skills from
[`skills/mapbox/`](../), which makes their failure modes ours — so we read them the way you read a
dependency you are about to ship, and wrote down what we found. Every finding is offered upstream as
an issue or a PR.

## The short version

| | |
|---|---|
| Skills audited | 20 |
| Trust | 19 🟢 GREEN, 1 🔵 BLUE, 0 yellow/orange/red |
| Findings | 6 skill-specific (2 medium, 4 low) + 4 corpus-wide |
| Skills shipping executable code | 1 of 20 |
| Third-party network destinations in shipped code | 0 |
| Hardcoded credentials | 0 |
| Evals in the corpus | 89 |

The one BLUE is `mapbox-mcp-runtime-patterns`, and only because it is the sole skill that ships
runnable code — which, having read all 1,272 lines of it, is the best-behaved code in the audit.

**The only non-green verdict we issued anywhere is our own skill**, at
[`../skill-snitch-report.md`](../skill-snitch-report.md): 🟡 YELLOW, because ours is the only skill
in this comparison that can shell out to a password manager and resolve a live production
credential. Theirs cannot do anything. Applying the rule evenly puts us below all twenty of them,
so that is where we put ourselves.

## What a clean result actually means

"We found nothing" is worth reading only if you can see what was looked for. Across 6,128 lines of
`SKILL.md` and 1,272 lines of shipped examples:

- **0 hardcoded access tokens.** Every example uses a placeholder or an environment variable. In a
  corpus about a token-authenticated API, written fast, by many hands, this is the result that is
  hardest to achieve and easiest to skip past.
- **0 shell-outs in skill prose.** No `curl`, `wget`, `nc`, `ssh`, `rm -rf`, `eval()`, `os.system`.
- **0 agent-coercive directives.** Nothing shaped like "ignore previous instructions", "do not tell
  the user", or "without asking". For a corpus that an agent loads into its own context, this is a
  prompt-injection surface, and it is empty.
- **0 third-party network destinations.** Every host in executable code is `mcp.mapbox.com`.
- **0 dangling internal links.** Every `references/*.md` a skill points at exists, and no reference
  file is orphaned.
- **Token handling in all five runnable examples is exemplary**: read from the environment, never
  hardcoded, and every one fails closed with a raise or throw when the variable is absent.

## The six skill-specific findings

| Skill | Finding | Severity | Class |
|---|---|---|---|
| `mapbox-token-security` | `unenterable-wildcard-guidance` | medium | accuracy |
| `mapbox-store-locator-patterns` | `location-collection-without-privacy-guidance` | medium | privacy-guidance |
| `mapbox-mcp-runtime-patterns` | `npx-at-runtime` | low | safety |
| `mapbox-web-integration-patterns` | `restriction-not-repeated-at-point-of-use` | low | accuracy |
| `mapbox-maplibre-migration` | `unsubstantiated-compliance-claim` | low | accuracy |
| `mapbox-data-visualization-patterns` | `cross-skill-link` | low | hygiene |

Two are worth reading in full. Both are in the per-skill reports with line numbers.

**The wildcard one is about the eval, not the doc.** `mapbox-token-security` recommends URL
restriction patterns the Mapbox console rejects — `http://localhost:*` for development,
`https://*.myapp.com/*` for subdomains — and entering either returns *"Wildcard characters (\*) are
not supported in URL restrictions."* Measured against a live restricted token rather than inferred:
restriction matching is origin equality, not URL-prefix matching. With `https://ebike-safari.com`
listed, referers of `/`, `/rides` and `/index.html` all pass, so a path wildcard has nothing to
express; with `http://localhost:5173` listed, 4173 and 3000 are refused, so a *port* wildcard is
exactly what a developer needs and cannot have. The implementation is consistent with itself; the
guidance describes prefix matching for something that does not do prefix matching.

The part we would actually bring to a meeting is that `evals/evals.json:25` grades an answer
**correct** for recommending the unenterable pattern. A graded expectation that rewards the wrong
answer freezes it: the suite passes, so the advice looks maintained. That is the failure mode
specific to evaluating judgment rather than output — and it is an argument *for* the harness. Without
that eval file this would have been an opinion about a doc page instead of a reproducible finding
with a line number.

**The privacy one is about the whole corpus, loudest in one skill.** In 6,128 lines there is no
guidance on retention, data minimization, anonymization, or GDPR/CCPA obligations. The single
occurrence of "GDPR" is an unsubstantiated bullet in a competitive comparison. The platform SDK
skills handle OS permission flows properly — Android covers `ACCESS_FINE_LOCATION`, iOS covers the
`NSLocation*` keys — so the corpus teaches *acquiring* a location correctly and is silent on
*holding* one. `mapbox-store-locator-patterns` is where that lands hardest: it has the heaviest
user-location surface of the twenty and one mention of permissions, for a skill whose entire job is
to take a person's position and use it. A nearest-store answer does not need five decimal places.

The constructive version: a `mapbox-location-privacy` skill, sibling to `mapbox-token-security`.
That skill already proves the shape works — it turns a compliance-flavored topic into concrete
token decisions, and retention windows, precision reduction, and consent scope would take the same
treatment.

## How these were generated

Two phases, which is skill-snitch's own rule: **grep finds, reading understands.**

Phase one is [`../scripts/snitch_mapbox_skills.py`](../scripts/snitch_mapbox_skills.py). It measures
structure, counts executable files and lines, extracts every host, parses eval files, checks every
internal link, and runs eleven named pattern probes across all twenty skills. It **cannot form an
opinion**: no tier is computed from measurements, and a skill absent from `findings.yml` is reported
as ⚪ UNJUDGED rather than assumed clean.

Phase two is a person reading what phase one pointed at, and writing it into
[`findings.yml`](findings.yml) — tiers, severities, classes, and why any of it matters.

```bash
python3 scripts/snitch_mapbox_skills.py table   # roll-up, writes nothing
python3 scripts/snitch_mapbox_skills.py scan    # regenerate all twenty reports
python3 scripts/snitch_mapbox_skills.py self    # regenerate ours, same scanner
```

The split is the point, and it is the reason this is worth forwarding to the people who wrote the
skills. Half of every report is measurement that re-runs against any commit and needs no trust in
us; the other half is opinion with a name and a date on it. A document that mixes the two is one
where you cannot tell which parts survive a re-run.

Reports are **derived files**. Edit `findings.yml` and regenerate; do not hand-edit a report.

### How a tier is decided

skill-snitch's ladder was designed for skills that can execute — it asks whether loading this thing
can hurt you. Nineteen of these twenty ship no code, so that axis is uniformly green and, used
alone, says nothing about twenty documents whose whole job is to be correct. Worse, a strict reading
computes 🟡 YELLOW ("review before use") for `mapbox-token-security` because its wildcard advice is
wrong — a verdict that is both precise and false.

So findings carry a **class**, and only `safety` moves the tier. `accuracy`,
`privacy-guidance` and `hygiene` are recorded, tracked, and reported on the same page as the badge,
without pretending a wrong sentence makes a file dangerous.

**🟢 GREEN here means "nothing makes this unsafe to load", not "nothing was found."**
`mapbox-token-security` is GREEN and carries a medium finding. Read the findings, not the badge.

The rule is enforced rather than asserted: the scanner recomputes each tier from safety-class
findings and prints a warning when `findings.yml` disagrees with its own stated basis. It caught two
of ours on the first run, where we had graded by feel.

## Two mistakes this audit made, and what they cost

Kept in because an audit that reports only its successes has told you nothing about its method.

**A false positive from pattern matching.** The link checker reported
`references/interactions.md` missing from two skills. Reading the lines showed both are correct
cross-skill references — `../mapbox-style-patterns/references/interactions.md` — and our regex had
matched the tail of a valid path. Had we shipped that, Mapbox would have received a bug report for a
bug that does not exist, which is how audits lose their audience. The checker now resolves targets
relative to the linking file.

**The scanner found itself.** Run against our own skill, it counted the twenty reports it had just
written as source files and read their probe tables as hits — 94 "privacy-law references", 4
"agent-coercive directives" — all of it its own output, plus its own regex definitions matching
themselves. Generated output is now excluded, the pattern-defining file is exempt from probing, and
the exemption is **printed in the report** rather than applied quietly. skill-snitch's own
`ignore.yml` carries the same entry for `cursor_mirror.py`, which we found only after making the
mistake ourselves.

## Corpus-wide observations

Recorded once rather than pasted into twenty reports. Full reasoning in [`findings.yml`](findings.yml).

- **MEDIUM `privacy-silence`** — no retention, minimization, anonymization or GDPR/CCPA guidance
  anywhere in the corpus.
- **LOW `postinstall-hook`** — the repo's root `package.json` runs `scripts/setup-hooks.js` on
  `npm install`, writing an executable into `.git/hooks`. Read in full: it copies a local pre-push
  hook, no network, no obfuscation, clear logging. Benign and good practice. Recorded because a
  postinstall that writes an executable is the *shape* of a real supply-chain vector, and "we
  checked, it is fine" is worth more than silence.
- **INFO `no-allowed-tools`** — frontmatter is `name` and `description` only. Not a violation;
  Anthropic's format does not require more. It is a note about auditability: with nothing declared,
  there is no declared-versus-observed diff to run, so runtime surveillance can say what happened
  but never whether it was promised.
- **INFO `eval-cost`** — evals are LLM-judged, `claude-sonnet-5` both answering and grading, with
  every run reading the whole skill as input. 89 evals across 20 skills. The harness is the best
  idea in the repo and it is not free; knowing which skills changed is what makes it affordable.

## Layout

```
skill-snitches/
├── README.md                              this file, hand-written
├── findings.yml                           the judgments: tiers, severities, classes, reasoning
├── CORPUS.yml                             derived roll-up, machine-readable
└── <skill-name>/skill-snitch-report.md    one per skill, derived
```

Our own report is at [`../skill-snitch-report.md`](../skill-snitch-report.md), deliberately outside
this directory: this one is for theirs.

## Provenance

- **Audited**: `mapbox/mapbox-agent-skills` @ `aab3a6f` (2026-09-16), MIT, © 2026 Mapbox, Inc.,
  owned by `@mapbox/locationai`.
- **Method**: [`skill-snitch`](../../skill-snitch/) SCAN, two-phase, plus live measurement against a
  restricted production token for the URL-restriction finding.
- **Auditor**: Don Hopkins, 2026-09-20. Not commissioned, not adversarial. We use these skills.
- **Their repo is unmodified.** Their skills stay in their checkout with their own remote and
  lifecycle; we mount them as a sibling rather than vendoring them. See [`../SKILL.md`](../SKILL.md).
