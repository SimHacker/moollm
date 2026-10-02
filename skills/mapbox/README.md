# mapbox — a router over Mapbox's own Agent Skills

A MOOLLM skill that **orchestrates Mapbox's twenty Agent Skills** instead of restating them, and
carries the operator-local reality they can't know: which token is for which surface, and how URL
restrictions actually behave when you probe them.

Mapbox publishes [mapbox/mapbox-agent-skills](https://github.com/mapbox/mapbox-agent-skills) — 20
skills, 6,128 lines of `SKILL.md`, 89 eval cases, MIT. This skill does not copy a word of it. It
mounts that repo as a sibling checkout, resolves it at runtime, and routes questions into it.

*For readers new to the format: an Agent Skill is a markdown file an AI coding agent loads on
demand — expertise as instructions, not code. The interesting problem once a platform ships twenty
of them is selection, and that is what this skill does.*

## Why a skill on top of skills

Everything here falls into one of three gaps. Nothing here duplicates upstream.

| Gap | What this skill does |
|---|---|
| **Which of the twenty?** | Deterministic keyword routing you can run, diff and version — not description-matching inside a host that may or may not have all 20 installed |
| **What the twenty don't cover** | Names the uncovered subjects out loud (tilesets, fonts, sprites, accounts, Atlas, licensed data products) and answers with the CLI instead of a near-miss skill |
| **What no published doc can know** | Token roles for *this* operator, framework traps in *these* repos, and restriction behaviour *measured* against the live API |

The honest scope: if you're in a host with all twenty installed, it already selects by description.
The router earns its place when you want a reproducible answer to "which skill", when you're on a
surface with no skill auto-loading, or when the answer depends on local facts.

## Mounted, not vendored

```
$MAPBOX_AGENT_SKILLS                          explicit override
~/GroundUp/git/mapbox-agent-skills            conventional checkout
./mapbox-agent-skills · ../ · ../../          sibling in a workspace
~/.agents/skills · ~/.claude/skills           installed by `npx skills add`
→ falls back to the GitHub URL, and says the catalog is unavailable
```

MIT permits copying, which is exactly the problem: a vendored copy is a fork with no maintainer,
and it drifts silently. Upstream moved four days before this skill was written. A resolver that
degrades to a URL is more honest than a stale snapshot, and it keeps attribution intact.

## Map, meet territory

Worth saying out loud, because it is the whole design and not a joke: this skill is **a map of a map
company's maps of its own platform.** The routing table is the index; the twenty skills are the
territory; and the discipline the resolver above enforces is the oldest one in the subject — *the map
is not the territory.* Vendoring would be pasting the territory into the legend.

The name for that idea in this repo is **korz**, after the language by David Ungar, Harold Ossher and
Doug Kimelman (*Korz: Simple, Symmetric, Subjective, Context-Oriented Programming*, Onward! 2014),
itself named for Korzybski's *Science and Sanity*. MOOLLM's working stance is the two-sided version —
**the map both is and is not the territory**: the router is the world *for the agent* navigating it,
and a representation *for the person* maintaining it. Both true, and the resolver is where the seam
lives.

One thing the analogy gives Mapbox readers for free, in your own vocabulary: MOOLLM's reading order
is a **tile pyramid**. `GLANCE` is the whole world in one tile, `CARD` is the metro, `SKILL` is
streets, `README` is a doorway — and the rule "never load a lower level without the level above" is
just traversing the pyramid instead of teleporting to z18, the same reason an overzoomed client falls
back to the parent tile. It is called the *Semantic Image Pyramid*, which was named before anyone
noticed the analogy, and an image pyramid is of course what a tile pyramid is.

Where the skill deliberately parts company with Korz: Korz dispatches on the whole context and
demands a unique most-specific match, so **a tie is an error**. The router returns every hit with the
keywords that fired it, because in skill selection ambiguity is information — "this question touches
security *and* web integration" is the useful answer. That is the HyperTIES index manager's choice
rather than Korz's: an ambiguous name there raises a menu, not an exception.

## The surfaces, and when this skill reaches for each

Not a description of Mapbox's platform — a record of which door we pick, and why.

| Surface | Reached for when | Cost |
|---|---|---|
| **REST + `curl`/`jq`** | One-shot geocode, a tile probe, anything scriptable or CI-bound | Most composable; you own retries and paging |
| **`mapbox` CLI** (`cli.mapbox.com/install.sh`) | Tilesets, fonts, sprites, account and usage — the subjects the twenty skills don't cover | A binary to install and keep current |
| **`@mapbox/mcp-server`** (runtime, 0.14.0) | An agent answering questions about the world: geocode, search, directions, isochrone, matrix, static | Protocol overhead per call; a server to supervise |
| **`@mapbox/mcp-devkit-server`** (0.8.2) | Authoring and account work: styles, token lifecycle, validation, bounding boxes | Same, plus write scope on a secret token |
| **`@mapbox/mcp-docs-server`** (0.3.1) | Documentation lookup when the skills stop short | Same |
| **SDKs** (GL JS, iOS, Android, Flutter) | Anything shipping in a product | Build-time weight; the routed skills cover the patterns |

Rule of thumb this skill applies: **if it runs once, `curl` it; if an agent must decide with it,
MCP it; if it ships to a user, SDK it.** MCP's value is the tool schema, and the price is a process.

Versions checked against npm on 2026-09-20. Worth noting that the skills repo points at the runtime
and devkit servers but never mentions `@mapbox/mcp-docs-server`, so agents following the skills will
not discover it — which is a shame, since documentation lookup is what an agent needs most.

## The twenty, grouped by the question that reaches for them

Names only — the descriptions are one read away upstream, and respelling them is what this skill
exists to avoid.

- **Security** — `mapbox-token-security`
- **Platform** — `mapbox-web-integration-patterns`, `mapbox-web-performance-patterns`, `mapbox-ios-patterns`, `mapbox-android-patterns`, `mapbox-flutter-patterns`
- **Design** — `mapbox-cartography`, `mapbox-style-patterns`, `mapbox-style-quality`, `mapbox-data-visualization-patterns`
- **Domain** — `mapbox-search-patterns`, `mapbox-search-integration`, `mapbox-navigation-patterns`, `mapbox-geospatial-operations`, `mapbox-store-locator-patterns`
- **Migration** — `mapbox-google-maps-migration`, `mapbox-maplibre-migration`
- **Agentic** — `mapbox-mcp-runtime-patterns`, `mapbox-mcp-devkit-patterns`, `mapbox-location-grounding`

## Field notes

Measured, not read. Probed **2026-09-20** against
`api.mapbox.com/v4/mapbox.mapbox-streets-v8/1/0/0.vector.pbf` with a URL-restricted public token.
These are the findings that changed how we ship, and the reason this skill isn't just a link.

| Finding | Detail |
|---|---|
| **No `Referer`, no tile** | URL restrictions are enforced on the `Referer` header, and `curl`, CI, server-side `fetch` and MCP all send none — so all four get `403`. The token that protects the browser breaks the shell. |
| **Enforcement is per-endpoint** | Tiles enforced. `/styles/v1/<user>/<id>` metadata answered `200` from every origin we tried. Restrictions are not a uniform perimeter. |
| **Edits propagate in minutes** | Mid-propagation, `http://localhost:5173` answered `200` while `http://localhost:5173/` answered `403` — which reads exactly like a trailing-slash matching bug and is not one. Re-probed 85 minutes later, every variant passed. Re-probe before concluding anything; we drew the wrong conclusion here first. |
| **Matching is origin equality** | The path is never consulted: with `https://ebike-safari.com` listed, `/rides` and `/index.html` both pass. Combined with the port result below, an entry is compared as scheme + host + port. |
| **Ports pin exactly** | `http://localhost:5173` listed does **not** admit `:4173` or `:3000` — so Vite dev works and `vite preview` 403s. |
| **Apex covers `www`** | `https://ebike-safari.com` listed also admitted `www.ebike-safari.com`. |
| **Public tokens edit in place** | Changing scopes or URL restrictions leaves the `pk.` string unchanged — rotation without redeploy. Secret scopes yield an `sk.`, shown once. |

One framework trap, ours not Mapbox's, recorded because it bites hard: in SvelteKit a `PUBLIC_*`
variable is compiled into the prerendered bundle at build time and baked into the image, so
rotating it means rebuilding. Name it `MAPBOX_TOKEN`, read it server-side via
`$env/dynamic/private`, hand it to the browser at runtime — then rotation is a restart.

## What we took from Mapbox, which is the best idea in that repo

The `evals/evals.json` pattern — `{skill_name, evals: [{prompt, expected_output, expectations[]}]}`
graded FULL/PARTIAL/MINIMAL/MISS by a judge model, rolled up per skill and diffed against a stored
baseline. **It is a regression test for judgment, and almost nobody builds one.**

MOOLLM has a documentation pyramid (`GLANCE` → `CARD` → `SKILL` → `README`) across about 150 skills
and had **no way to test a skill's judgment**. You could see that a skill was well-formed; you could
not tell whether editing it made the advice worse. Mapbox's harness is that missing rung, and it is
the strongest argument we have seen for evals as a *routine* artifact of authoring rather than a
research activity.

What we are not going to pretend: **retrofitting this onto 150 skills is real money, not a weekend.**
Every run is a judge model grading hundreds of expectations, and that per-run cost is what sets the
refresh cadence — which is probably the charitable and correct reading of finding 2 below, rather than
neglect. So: adopted where it earns its keep, starting with the skills whose advice is load-bearing.
The larger interest is plainer than a promise — **skill validation is work we would like to do**, on
this harness included.

Worth saying plainly, since skill counts invite the wrong comparison: **it is not how many skills you
have, it is how seamlessly they compose.** A library is a language, not a catalogue — which is the
whole reason this particular skill is a router rather than a twenty-first skill.

Planning notes: [`CAULDRON.md`](./CAULDRON.md).

## Two things to flag upstream — and the harness is why they are visible

Read these as evidence that the eval pattern works, because that is what they are: **this class of bug
is only findable in a system that writes its expectations down.** A platform whose guidance lives in
prose has the same contradictions with nothing to catch them. Offered as field reports from someone
using the platform, not as corrections — we may be wrong about the first one's scope, and we say where
we didn't test.

**1. `http://localhost:*` is recommended, rewarded by the evals, and rejected by the console.**

The pattern appears as guidance in three places and is then graded as correct in a fourth:

- `skills/mapbox-token-security/SKILL.md:158` — `http://localhost:*   # Local development`
- `skills/mapbox-token-security/SKILL.md:192` — `allowedUrls: ["http://localhost:*", "http://127.0.0.1:*"]`
- `skills/mapbox-token-security/AGENTS.md:93` — `http://localhost:*   # Development`
- `skills/mapbox-token-security/evals/evals.json:25` — expectation: *"Recommends `http://localhost:*` or `http://127.0.0.1:*` for local development"*
- `evals/baseline.json:1904` — that expectation scored **FULL (3)**

On 2026-09-20 the account console refused to save it: *"Wildcard characters (\*) are not supported
in URL restrictions."* We worked around it by listing every origin explicitly. **What we did not
test:** whether the tokens API accepts what the console UI refuses — if it does, this is a UI
limitation rather than a docs error, and the fix is a different one.

The probe above suggests why the two disagree: **matching appears to be origin equality, and the
path is never consulted.** That makes the recommended `https://myapp.com/*` form not just
unenterable but unnecessary — there is nothing for the `/*` to match, because a restriction entry is
compared as scheme + host + port. If that reading is right, the guidance and the eval are describing
URL-prefix matching for an implementation that does origin comparison, and the wildcard rejection is
the implementation being consistent with itself.

The interesting part isn't the discrepancy, it's the mechanism: **an eval that rewards the wrong
answer freezes it.** The suite is working exactly as designed and still pins advice that can't be
entered. That's a hazard of the pattern for anyone adopting it, us included.

**2. The committed baseline no longer covers the suite.**

`evals/baseline.json` records `totalEvals: 51`, timestamped `2026-03-30`, with both model and judge
pinned to `claude-sonnet-4-20250514`. The skills now define **89** cases across 20 skills. So about
40% of the current suite has no recorded baseline, and the scores that do exist were graded by a
May-2025 model. A regression harness is only as good as the freshness of what it regresses against.

Both of these are easy to file as issues or PRs upstream if that's useful — say the word.

The lesson we're carrying into our own adoption, rather than filing at anyone: **an expectation is an
assertion about the world, and it goes stale like any other.** An eval that rewards an answer freezes
it, so a green suite can pin advice that cannot be entered. That is a hazard of the pattern for
everybody who adopts it, us included, and it does not make the pattern less worth adopting.

## Try it

```bash
python3 scripts/mapbox_router.py where                    # resolved checkout, or how to mount one
python3 scripts/mapbox_router.py list                     # the catalog, read from upstream
python3 scripts/mapbox_router.py route "cluster 50k points and keep 60fps"
python3 scripts/mapbox_router.py doctor                    # probe a token live, classify the 403s
python3 scripts/mapbox_router.py measured                  # the table above, from source
```

Mount upstream first, anywhere the resolver looks:

```bash
git clone https://github.com/mapbox/mapbox-agent-skills ~/GroundUp/git/mapbox-agent-skills
```

Tokens resolve by **role**, from a password manager, never pasted: a URL-restricted token for the
browser, an unrestricted one for CLI, MCP and CI. They are different tokens because they run in
different places — not because they belong to different people.

## We also audited all twenty of them

Routing to a dependency means inheriting its failure modes, so we read the twenty the way you read
code you are about to ship. The reports are in [`skill-snitches/`](skill-snitches/) — one per skill,
plus a [roll-up](skill-snitches/CORPUS.yml) and the [reasoning](skill-snitches/findings.yml).

**19 GREEN, 1 BLUE, nothing worse.** Zero hardcoded credentials in 6,128 lines, zero third-party
network destinations, zero prompt-injection-shaped directives, and token handling in all five
runnable examples that reads from the environment and fails closed. Six skill-specific findings, two
of them medium: the wildcard guidance described above, and a corpus-wide silence on what to do with
a user's location once you have it.

The only non-green verdict we issued is **ours** — [`skill-snitch-report.md`](skill-snitch-report.md),
🟡 YELLOW, because this skill is the one thing in the comparison that can read a live credential out
of a password manager. Nineteen of theirs cannot execute anything at all. The rule applied evenly
puts us below all twenty, so that is where we put ourselves.

Half of each report is measurement that re-runs against any commit
([`scripts/snitch_mapbox_skills.py`](scripts/snitch_mapbox_skills.py)) and needs no trust in us; the
other half is opinion with a name and a date on it.

## Files

| File | What it's for |
|---|---|
| `GLANCE.yml` | Is this relevant? (~70 lines) |
| `CARD.yml` | The interface: methods, upstream config, key roles, measured table |
| `SKILL.md` | The protocol: routing, the 403 decision tree, surface selection |
| `scripts/mapbox_router.py` | The implementation, and its own documentation |
| `scripts/snitch_mapbox_skills.py` | The auditor: measures their twenty and ours, writes the reports |
| `skill-snitches/` | Twenty audit reports of Mapbox's skills, plus findings and roll-up |
| `skill-snitch-report.md` | The audit of *this* skill, by the same script |
| `CAULDRON.md` | Adopting the evals pattern repo-wide |

## Credits

The twenty skills, the `evals` pattern and the three MCP servers are Mapbox's work —
[mapbox/mapbox-agent-skills](https://github.com/mapbox/mapbox-agent-skills), MIT, © 2026 Mapbox,
Inc. Read against commit `aab3a6f` (2026-09-16). This skill is a router and a set of field notes;
the expertise upstream is theirs.

Part of [MOOLLM](https://github.com/SimHacker/moollm) — see [`skills/`](../) for the rest.
