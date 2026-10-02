# moollm/skills/mapbox — skill-snitch report

**Trust** 🟡 YELLOW · **Type** moollm · **Executable files** 2 · **Evals** 0 · **License** MIT

**Skill** `SimHacker/moollm — skills/mapbox` @ `2fde5e7d` · **Scanned** 2026-09-20 by Don Hopkins
**Audits** `mapbox/mapbox-agent-skills @ aab3a6f` — the twenty skills this one routes to

> Derived file. Measurements come from `scripts/snitch_mapbox_skills.py` and re-run against
> any commit; judgments come from `skill-snitches/findings.yml`. Edit the findings, not this.

## What it is

A router over the twenty official skills, plus the local realities they do not cover: token roles, measured referer behavior, surface selection.

## Notable

Holds the most dangerous capability in this entire comparison. Nineteen of Mapbox's twenty
skills cannot execute anything; ours shells out to a password manager and can resolve a live
production credential. That asymmetry belongs in the open.

## Measured surface

| Measure | Value |
|---|---|
| Files | 8 |
| SKILL.md | 235 lines |
| AGENTS.md | absent |
| References | 0 |
| Executable code | 2 files, 999 lines |
| Broken internal links | none |

### What the patterns found

Excluded from pattern probing because it defines the patterns: `snitch_mapbox_skills.py`. Still counted as shipped code above.

| Probe | Hits | Reading |
|---|---|---|
| hardcoded access tokens | 0 | clean |
| shell-outs to network tools | 7 | REVIEW |
| destructive or eval-shaped calls | 0 | clean |
| process spawns | 2 | present, in context |
| env-var token references | 4 | present, in context |
| agent-coercive directives | 0 | clean |
| explicit prohibitions | 0 | absent |
| user-location references | 1 | present, in context |
| OS permission references | 2 | present, in context |
| consent references | 1 | present, in context |
| privacy-law references | 0 | absent |

### Network destinations

Hosts appearing in executable code — the ones this skill can actually reach:

- `api.mapbox.com`
- `cli.mapbox.com`
- `ebike-safari.com`
- `evil.example.com`
- `github.com`
- `localhost`
- `myapp.com`


Not first-party: `ebike-safari.com`, `evil.example.com`, `github.com`


Hosts named in prose and examples (1 distinct, 1 of them placeholders like myapp.com): all placeholders. Documentation text, not destinations.

## Findings

### MEDIUM — reads-a-credential-store

*safety · moves the tier*

**Where** `scripts/mapbox_router.py:255-262 (op_read), :392`

**What** Shells out to subprocess.run(['op', 'read', ref, '--account', ...]) and receives a live token.

**Why it matters** The capability is the point — resolving by reference is what keeps tokens out of pasted
strings and shell history — but it is still the one thing here that touches a vault.

**Mitigations**

- Never prints more than a prefix: line 396 emits three characters and a length, never the token.
- Read-only. No op write, no op item create, nothing that could alter the vault.
- Fails soft: returns None when op is absent, so it degrades instead of prompting.
- The token is used for exactly one thing, a 403-versus-200 probe against api.mapbox.com.

### LOW — token-in-query-string

*safety · moves the tier*

**Where** `scripts/mapbox_router.py:400`

**What** Builds PROBE_URL?access_token=<token> to test referer enforcement.

**Why it matters** Mapbox's own API takes the token as a query parameter, so there is no header alternative to
prefer. Recorded because query-string credentials are the kind of thing that ends up in
access logs and shell history generally. Here the URL is never printed and never written.

### LOW — reproduces-curl-pipe-sh

*safety · moves the tier*

**Where** `SKILL.md:151, CARD.yml:23, scripts/mapbox_router.py:382`

**What** Tells the operator to install the CLI with curl -fsSL https://cli.mapbox.com/install.sh | sh.

**Why it matters** Mapbox's documented install method, repeated faithfully — which is the problem. Piping a
remote script into a shell is a pattern we would flag in someone else's skill, and citing
the vendor is an explanation rather than a defense. Listed so the double standard is on the
record rather than in the reader's head.

### LOW — unpublished-outward-facing-docs

*hygiene · recorded, does not move the tier*

**Where** `git status: skills/mapbox/README.md, skills/mapbox/CAULDRON.md`

**What** Both untracked at audit time, while GLANCE.yml and mapbox_router.py carry uncommitted modifications.

**Why it matters** A consistency finding, and the practical one. The README is the document written to be sent
to someone at Mapbox, and it does not exist in the repository it points people at.

### INFO — deliberate-evil-referer

*hygiene · recorded, does not move the tier*

**Where** `scripts/mapbox_router.py:406`

**What** Sends Referer: https://evil.example.com/ on purpose.

**Why it matters** A negative control: a restricted token must return 403 for an origin that is not on its
list, and the only way to know is to be that origin. Any pattern scanner will flag the
string. Reading the line resolves it in five seconds, which is the whole argument for
two-phase scanning.

### INFO — committed-operator-identifiers

*hygiene · recorded, does not move the tier*

**Where** `CARD.yml:142-150, SKILL.md:183-184, scripts/mapbox_router.py:152-160`

**What** Contains a 1Password account name and vault item paths (op://Employee/Mapbox/...).

**Why it matters** References, not secrets — worthless without the vault and the hardware behind it. Deliberate:
this skill is operator-specific by design, and a reference nobody can resolve is not a
credential. Recorded because an automated scan will and should notice them.

## Verdict

🟡 YELLOW — Read it before you run it. It can reach something that matters.


6 findings recorded above, of which 3 safety-class. The badge answers whether this is safe to load, not whether anything was found — see `tier_basis` in `../findings.yml`.
