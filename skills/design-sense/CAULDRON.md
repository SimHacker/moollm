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
