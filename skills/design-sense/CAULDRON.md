# design-sense — cauldron (planning and harvest log)

Status: graduated. The skill exists; this doc lives inside it as the planning organ —
ingredient list, harvest log, germination queue. Fittingly, the skill about
design-by-accretion is being designed by accretion.

## What it is

One general-purpose **ambient design skill** instead of many tiny ones (no separate
fitts skill, no separate foveation skill). It models the working designer's head: the
constraints and methods that stay loaded *at all times* — "not a checklist item but an
ambient constraint, always on."

Scope: user interface, interactivity, game design, **and software design** (Self, Korz —
design of the invisible). Not visual styling; the skill never tells you what colors to use.
The wheelhouse: designing user interfaces for simulation games, and the systems under them.

Grows like cursor-mirror did: one socket, many plugin registries in subdirectories.

## Name

**`design-sense`** — a sense is ambient, involuntary, always sampling; scales from pie
menus to prototype semantics; says nothing about palettes. Reads as a K-line: "load
design-sense". Big-endian children: `design-sense/lenses/foveation.yml`.

Rejected: `designers-head` (repo in-joke as front door; save it as an exhibit inside),
`design-eye` (over-indexes vision once software design is in), bare `design` (dead K-line).

## Structure

```
skills/design-sense/
  GLANCE.yml / CARD.yml / SKILL.md   # kernel: what a design sense IS; ambient: true
  lenses/       # always-on perceptual/attention constraints, one file each
  methods/      # constraints on process — how the work proceeds over time
  masters/      # whose head are you borrowing (house-styles analog)
  seeds/        # raw harvest intake — not yet germinated into a registry
  domains/      # deeper dives per field (later)
    interaction/
    game/
    software/
```

Two registries, two axes: **lenses** constrain attention while you look;
**methods** constrain process while you build. Chris Trottier's pair forced the split —
accretion is not a lens, it's a method.

**seeds/** is the accretion intake: harvested principles land there raw, germinate
(named, stated plainly, sourced), then graduate to lenses/ or methods/. Sinsemilla
means *without seed*: seeds in, sinsemilla out — a cured registry is seedless by
definition. Simsemilla being, canonically, what they smoke in The Sims.

## Ingredients so far

Lenses:
- **fitts** — cost grows with distance, shrinks with size; the cheapest target walks
  over and stands under your gaze. Source: pie menu corpus; MicropolisCore
  `documentation/designs/pie-menus-fitts-law.md`.
- **foveation** — "Motion is a foveation summons. Only send it where you want the eye."
  Peripheral motion is a hardware interrupt; animate the rejects and you summon the eye
  to what the user just dismissed. Source: David Ungar critique of Don's Unity3D pie
  menus — wwsff `characters/david-ungar/fitts-and-foveation.md` (Sims popup head +
  RenderRoundShadow as prior art).
- **stage-magic** — simple view until complex truth; the magician controls where you
  look. Source: Ungar, Self morphs; already MOOLLM's GLANCE → CARD → SKILL pyramid.

Methods:
- **design-by-accretion** — layer, accumulate, let it grow, tune late. Source: Chris
  Trottier — wwsff `characters/chris-trottier/design-by-accretion.md`; kin to the
  cauldron skill (accretion as kitchen technique).
- **tuned-emergence** — the tuning pass is not optional; it is the second half of
  accretion. The Sims wasn't fun until the last months. Source: Chris Trottier 2004 —
  wwsff `characters/chris-trottier/tuned-emergence.md`.

Masters (seed set):
- **will-wright** — possibility space, failure as entertainment, player-as-storyteller,
  software toys; simulation-game UI as the native genre.
- **david-ungar** — power of simplicity, stage magic, foveation; dynamic deoptimization
  as design stance (pessimize until forced to deepen).
- **chris-trottier** — accretion + tuned emergence; the designer who lived the method
  inside EA's playbook.

Domains (later): interaction (pie menus, direct manipulation, self-explaining disabled
items), game (advertisement economy as UI, Sims storytelling spectrum), software
(Self, Korz, de-objectification).

## Harvest log

- 2026-08-22 — three parallel scouts swept wwsff characters/catalogs, moollm
  skills/designs, MicropolisCore designs + palmhoo. All three batches landed in
  seeds/ (2026-08-22-micropolis-palmhoo.md, 2026-08-22-moollm.md,
  2026-08-22-wwsff-corpus.md — ~60 candidates total). Founding registries
  germinated the seed set: lenses fitts, foveation, stage-magic; methods
  design-by-accretion, tuned-emergence; masters will-wright, david-ungar,
  chris-trottier.
- 2026-09-19 — **reasoning-is-not-science planted**, out of Kay's Quora answer (science
  as a heuristic prosthetic for poor commonsense thinking, and "more concern about
  reasoning as opposed to science") crossed with Don's question about thinkers who
  reason themselves into corners. The mechanism that earned it a file: reasoning is
  audited internally and science externally, so fluency accelerates the failure instead
  of protecting against it, and the fix has to be structural rather than an exhortation
  to be humble. Tests: does the practice generate a claim that could embarrass you with
  the grade recorded, what did the last update cost, and what leaves the design review.
  New lenses ad: deciding-whether-you-know-it. Also corrected two stale registry counts
  (lenses/GLANCE.yml said 31, methods/GLANCE.yml said 32). Registries now 33 lenses /
  33 methods / 59 masters.
- 2026-09-19 — **reasoning-is-not-science deepened**, same day, out of Don disputing a
  character-based dismissal and demanding the specific charge. Three things earned their
  way in. (1) The floating referent in the first test got a definition — you grade a
  *practice*, not a person, which is what makes it better than tribal sorting; Don's four
  calibrations (gwern yes, Tetlock and prediction markets yes, MIRI's decision theory
  mostly no, Adams structurally no) are now the worked table. (2) **The martyr's
  exemption**: a price paid continuously for a belief looks like the opposite of armchair
  certainty and measures sincerity, which was never in doubt — a cost you choose and can
  keep choosing has been removed from the circuit rather than wired into it. So the
  question is what the last *update* cost, never what the position has cost. (3) The
  economics under it: money, status, and fluency all let you absorb consequences
  indefinitely, and all three are normally read as qualifications — the same inversion the
  top of the file runs, now with Veblen in it. If you can pay not to be corrected, you
  won't be. Plus a specimen where the premise shipped and lost anyway (the cypherpunk
  sufficiency thesis, falsified by its own success rather than by its failure), and a new
  what-to-do-instead: precommit in observable terms, as a Ulysses pact aimed at a future
  self who will have better arguments than you do now.
- 2026-09-19 — **view-state-is-the-users planted**, straight from Don's rant about
  Quora's three independent folding mechanisms: expansion state a reader assembled
  by hand is the reader's, and one wrong click that destroys it with no undo and no
  address is a data-loss bug. Third sighting of the same principle (Nelson's
  clipboard in READING-CURSORS, the Google Maps shake-UNDO on the bike mount, now
  Quora), so it earned a file instead of a seed. Tests: how many actions back to
  where I was, and can you link to the expanded view. New lenses ad:
  designing-reading-and-navigation. Registries now 32 lenses / 33 methods /
  59 masters.
- 2026-09-17 — **keep-the-seed planted.** Don's multiplayer SimCity city-proposal
  design, from the notes in the Micropolis source: page through proposed cities,
  recover generated terrain because the RNG seed was saved, and proposing clears
  everyone's votes. Grown into the method that generative content owes six visible
  verbs (generate, reroll, edit, revise, reset, clear) and a history. New methods
  ad: working-with-generated-content. Registries now 31 lenses / 33 methods /
  59 masters.
- 2026-08-22 (afternoon) — **the great planting.** Format decision: all plugins
  are Markdown, not YAML (human-readable first; the yml originals converted and
  removed). Germinated nearly the whole queue: 28 lenses, 28 methods. Session
  batch (seeds/2026-08-22-dons-session.md): masking, one-page-designs,
  reverse-diagrams, explorable-explanations, time-to-penis,
  low-floor-no-ceiling, put-that-there, tourist-policy, point-dont-copy,
  tools-first-content-second — all planted.
- 2026-08-22 (afternoon) — **the masters shelf.** Grew from 3 heads to 57.
  One person, one file. Sources: the wwsff character corpus and the lloooomm
  roster at temp/lloooomm/00-Characters/. The Yoot Saito and Alan Kay files
  cross-link their 1993 MACWORLD Japan interview.
- 2026-08-22 (afternoon) — **votes and links pass.** Every master got a Votes
  section (positive imperatives, linked) alongside Vetoes. Every lens fleshed
  to gold standard with working links: relative paths in-repo, GitHub URLs
  cross-repo (github.com/SimHacker/…, github.com/YootTowerManagement/…); all
  link targets verified on disk. Subdirectory kernels written:
  GLANCE/CARD/README per registry, CARDs carrying dispatch-table advertisements
  (design context → lens set, work phase → method set, problem → head).

- 2026-08-22 (late afternoon) — **the media equation planting.** New batch
  (seeds/2026-08-22-beyond-human.md) harvested from the Stanford Storytelling
  Project's Beyond Human episode and germinated same day: lens media-equation
  (Nass & Reeves — people treat computers as social actors, involuntarily);
  methods poisoned-well (Microsoft Agent made screen characters radioactive
  for decades — autopsy the crater before re-entering a space) and
  vibe-labeled-voices (Jeff Adkins — casting metadata for synthetic voices).
  Masters shelf grew to 59: clifford-nass and byron-reeves, one person one
  file. Registries now 29 lenses / 30 methods / 59 masters.

- 2026-08-22 (evening) — **Stop Making TUIs harvest.** Batch
  seeds/2026-08-22-stop-making-tuis.md from Ptacek's Quarrelsome post and HN
  49384210 (including Don's Brooke Shields line). Planted: lenses cli-not-tui
  and keyboard-is-not-tui; methods summon-native and remote-cli-local-gui.
  Don's master file gained a vote. Registries now 31 lenses / 32 methods /
  59 masters / 6 seed batches.

## Count drift

**Six files claim this skill's registry sizes and no two agree.** Found 19 Sep 2026 while writing
`TIES.yml`, by the cheap method of running `ls` instead of trusting any of them.

| Source | lenses | methods | masters | seeds |
|---|---|---|---|---|
| **disk, 19 Sep 2026** | **35** | **34** | **60** | **7** |
| `GLANCE.yml` — *this skill's own front door* | 34 | 33 | 59 | — |
| `.cursorrules` — *ambient, every session* | 33 | 33 | 59 | — |
| `.cursor/rules/moollm-core.mdc` — *ambient, every session* | 31 | 32 | 59 | — |
| harvest log above, last entry | 33 | 33 | 59 | — |
| `TIES.yml`, first draft | 37 | 36 | 62 | 9 |

The `GLANCE.yml` row is the most embarrassing one: it is the file a reader hits first, and it
disagrees with the disk by one lens. Nobody was careless — the count was correct when typed, and
every later `PLANT A SEED` was a chance to miss it.

Two distinct failures, and they want different fixes:

**Stale hand-typed counts.** The log, `.cursorrules` and `moollm-core.mdc` were each right when
written and have been decaying since. The two ambient files are the expensive case: they load into
every session, so every boot pays tokens for a wrong number. They are bootstrap-compiled, so the fix
belongs at compile time — either compute the counts from disk or **stop stating them in an
always-loaded file**, which is the cheaper answer given that nothing downstream branches on 33 versus
35.

**A wrong formula, not a stale number.** `TIES.yml`'s 37/36/62/9 was `ls | wc -l`, which counts each
pile's own `CARD.yml` and `GLANCE.yml` as members. Every pile overcounted by exactly two. Worth
separating from the first failure because refreshing on a schedule would never have caught it — the
recipe was wrong, so it would have kept producing the same wrong answer, on time, forever.

The general rule this pushed into the TIES schema: a count is derivable, so either leave it out or
declare it as a cache with the command that regenerates it. Undeclared duplication is not a cache,
it is a fork. See `../ties/TIES-SCHEMA.yml` → `manifest_only_what_is_not_derivable`.

## Germination queue

Remaining Todo seeds (see seeds/ batch files for the journal of record):
declare-constraints-keep-true (merge the two batches' versions),
coherence-as-journalism, proposals-before-facts, gonzo-inhabited-chrome,
repo-as-simulation, sip-before-gulp, orthogonal-mixins,
query-by-presence, robust-first (pointer), postel (pointer),
programming-by-demonstration (Cypher/Lieberman master files exist; the method
file doesn't yet), slots-all-the-way-down, barycentric-blend-space,
hobby-model / data-portability. No masters currently queued.

Dedup rules learned: several candidates (robust-first, postel, k-lines,
procedural-rhetoric, simulator-effect, play-learn-lift, cauldron's melt-then-ladle)
are already whole moollm skills — the design-sense entry points at the skill via
a Dispatch line, holding only the design-sense angle. The three batches overlap
on Wright and the pie menu corpus; merged on germination, richest statement
kept, all sources cited.

## Relations

- copy-that — same kernel+plugin-registries shape (formats/, house-styles/).
- cauldron — the method this doc is following.
- wwsff character corpus — primary sources; lenses cite, don't duplicate.
