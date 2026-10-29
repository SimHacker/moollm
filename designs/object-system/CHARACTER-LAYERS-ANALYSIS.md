# Character layers across repos

One being can have a tree of incarnations, one layer per purpose and repo
([constitution §15](../../kernel/constitution-core.md#15-the-semantic-image-pyramid-concentrated-not-dry-universal),
"Layers across repos"). This surveys the layers that exist, how each spells identity,
parents, purpose and relationships, and what aligning them would take. Analysis only:
nothing in any repo has been migrated. Companion to [CARD-ANALYSIS.md](CARD-ANALYSIS.md).

Reproduce: `python3 skills/prototype/scripts/layers_survey.py all` (sections `census`,
`parents`, `ids`, `purpose`; `--root` names the directory holding the sibling repos).
Counts from 2026-10-29: 522 `CHARACTER.yml` files.

## The layers

| Layer | Where | Files | Purpose |
|---|---|---|---|
| adventure | `moollm/examples/adventure-4/characters/` | 57 | playing in the adventure: location, inventory, Sims motives, Mind Mirror, advertisements, methods |
| moollm-other | elsewhere in moollm (skills, other examples) | 18 | prototypes and skill examples |
| biography | `DonHopkins/characters/` | 90 | Don's authored portrayals of real people: representation ethics, bio, correspondence, ties |
| profile | `WillWrightShowForFood/characters/` | 303 | guests, subjects and memorials: life facts, invitation pipeline, memorial, sources, show suggestions |
| cast | `WillWrightShowForFood/characters/{menagerie,sims,robots}/` | 25 | fictional cast members imported from moollm with a local overlay |
| audience | `WillWrightShowForFood/repo-shows/*/audience/` | 28 | a seat at one show: planted questions (`questions.yml`, 31 files), disclosure, relationship to the subject |
| private | `RepoShowPrivate/characters/` | no CHARACTER.yml | correspondence, invitation drafts, sources not yet public |
| page | `MicropolisCore/apps/micropolis/website/pages/about/don-hopkins/` | 1 | a published page about a person; declares its upstream |

wwsff also defines its own layer schemas in `WillWrightShowForFood/schemas/`:
`portrayal-standards.yml`, `audience-character.yml`, `guest-invitation-status.yml`,
`invitation-workflow.yml`, `question-tree.yml`, `advertisement-dispatch.yml`, and others.
They already document defaults (`invitation.status` defaults to `draft`, `consent` to
`not_yet_asked`).

## Beings with several layers

67 of 445 ids have more than one layer.

| Id | Layers |
|---|---|
| don-hopkins | adventure, biography, profile, page |
| palm | adventure (`animals/monkey-palm`), profile, cast (`menagerie/palm`), audience (will-wright-premiere, snap-logo-brian-jens) |
| richard-bartle | adventure, biography, profile, audience |
| phil-salvador | biography, profile, audience |
| dents | adventure, moollm-other, cast |
| 51 people | biography + profile (alan-kay, will-wright, marvin-minsky, seymour-papert, ...) |
| 2 people | profile + audience (heather-castillo, steve-alvey) |
| 9 fictional | adventure or moollm-other + cast (grue, troll, slats, doctor-no, bella-goth, ...) |

The adventure layer is the centre of gravity for fictional beings; the biography and profile
layers are for real people. Overlap (Don, Richard Bartle, Palm) is by design.

## How layers point at each other

"This layer extends that one" is spelled seven ways:

| Spelling | Where | Count | Shape |
|---|---|---|---|
| `inherits:` | adventure, moollm-other, biography | 50, 15, 40 | list (biography: 30 list, 10 str) |
| `inherits:` | cast, profile | 21, 1 | map `{repo, path, absolute_url, canonical_dir, ...}` or `{moollm_skills, overlay_protocol}` |
| `moollm_source:` | cast, profile | 7, 3 | map `{absolute_url, repo, path, import_mode: overlay}`; duplicates `inherits:` |
| `character_ref:` | audience | 3 | relative path to the profile |
| `canonical_soul:`, `prototype_ref:`, `canonical_home:`, `moollm_home:` | audience | 2, 2, 1, 1 | paths or URLs |
| `wwsff_local:` | cast | 1 | path to the profile layer |
| `upstream:`, `canonical:` | page | 1, 1 | path to the biography layer; URL of the full site |

Most layers don't declare the relationship at all:

- 63 directories in `DonHopkins/characters/` share an id with a profile (53 with a
  CHARACTER.yml on both sides). 19 biography files mention wwsff; 1 profile file points back.
- 2 to 3 of 28 audience seats name their profile layer.

`inherits:` as a map in the cast layer mixes two relations: which layer this one extends (the
moollm character) and which skills apply (`moollm_skills: [character, mind-mirror, ...]`).

## Core facts across layers

Same id, biography vs profile, where both state the fact:

| Fact | Both state it | Disagree | Kind of disagreement |
|---|---|---|---|
| `name` | 53 | 0 | |
| `status` | 48 | 1 | jesus-mouse: `deceased` vs `memorial` (vocabulary) |
| `representation.consent_level` | 49 | 4 | jesus-mouse `5_deceased_legacy` vs `5` (spelling); **bill-joy 1 vs 3, scott-draves 2 vs 3** (facts to check) |
| `signifier` | 48 | 14 | meaning: biography uses 👤 living / 🕯️ deceased; profile uses a topical emoji (will-wright 🌍) |
| `type` | 53 | 53 | meaning: the layer's role (`invitation`, `memorial`, `dream-guest` vs `representational`), not the being's kind |

The bill-joy and scott-draves consent levels are the kind of drift a cross-layer lint
exists to catch: one of the two layers is wrong about what the person agreed to.

## Purpose keys

| Key | Layers | Shape |
|---|---|---|
| `status` | profile 298, biography 84, cast 25 | `living` 303, `deceased` 49, `active`, `unknown` |
| `representation` | profile 289, biography 72, audience 28, cast 19, page 1 | `{authored_by, consent_level, governed_by}` (profile), `{authored_by, consent_level, protocol, subject_rights, may, must_not}` (biography), `{kind, consent, speaks_as, may, must_not}` (page) |
| `invitation` | profile 275 | `{status, consent, document, show_seed, memorial_arc}`; status `draft` 172, `memorial` 45, `sent` 8, `dream_guest` 8, `stub` 5, `warm`, `not_offered` 4 |
| `memorial` | profile 45 | map |
| `real_being` | biography 77, audience 28, cast 25 | bool |
| `planted`, `disclosure` | audience 11 | the on-air disclosure for planted fictional audience |

Spelling splits inside one meaning:

- consent: `representation.consent_level: 3` (number), `consent_level: 5_deceased_legacy`,
  `representation.consent: self-sovereign` (page), `invitation.consent: not_yet_asked`
  (whether the invitation was accepted: a different fact with the same word).
- the standard governing a portrayal: `governed_by:` (profile) and `protocol:` (biography).
- relationships: `relationships:` map id → {type, narrative} (adventure 46, cast 22),
  `relationship:` prose to Don or the show (profile 24, audience 24), `connections:` (profile
  70), `friends:`.
- `status:` here is a fact about a being (living, deceased), not the stored work status
  SCHEMA.md forbids; `invitation.status` is a work status.

Envelopes: 434 of the 446 wwsff and biography files keep a `character:` wrapper (profile 292,
cast 25, audience 28, biography 89). moollm flattened its own in round 1.

## What each layer needs to run alone

Every layer carries, as a concentrated copy, the core it needs without the others:

```yaml
id: alan-kay
name: Alan Kay
real_being: true            # default false only in fictional layers; absent in a real-person layer means true
status: living              # living | deceased | fictional
signifier: "👤"             # the living/deceased convention; a topical emoji goes in emoji:
representation:
  consent_level: 3          # 1 self-sovereign · 2 explicit · 3 public figure · 4 private · 5 deceased
  authored_by: don-hopkins
  governed_by: moollm://github/SimHacker/moollm/skills/representation-ethics/
inherits: [ ... ]           # the layer(s) this one extends
```

The biography layer's "intentionally WET" ethics header, repeated in every portrayal so it
travels with a copied directory, is this rule already in practice.

## Declaring relations between layers

The constitution asks for relationships, transformations and dependencies to be explicit.
Three relations cover what the files do today:

| Relation | Meaning | Today's spellings |
|---|---|---|
| `inherits:` | lookup: this layer's missing slots come from that layer | `inherits:` lists, `character_ref:`, `moollm_source:`, `wwsff_local:`, `prototype_ref:`, `canonical_soul:`, cast `import_mode: overlay` |
| `derived_from:` | authoring: this layer is a projection of that one, copied or transformed by hand or by a script; a lint checks the copied facts agree | `upstream:` (page), the biography → profile pairs (undeclared) |
| `related:` / `layers:` | navigation: the being's other incarnations, a concentrated copy linted against the survey | `see_also:` paths, `wwsff_overlay.audience_fork`, `ticketpr_seats`, `menagerie:` |

Cross-repo references: the biography layer already writes
`moollm://github/SimHacker/moollm/skills/...` in its headers, and the cast layer writes both
an absolute GitHub URL and a repo-relative path. One form, a `moollm://github/<owner>/<repo>/<path>`
URI that the resolver maps to a sibling checkout or a URL, replaces the `{repo, path,
absolute_url, canonical_dir, character_url, ...}` maps.

## Rooms and objects

MicropolisCore has no rooms or object files; its MOOLLM objects are 3 skills
(`micropolis`, `micropolis-command-bus`, `screen-angel`) and the one page CHARACTER. wwsff has
4 ROOM.yml (shows as rooms: `repo-shows/will-wright-premiere/ROOM.yml` beside `SHOW.yml`,
`SEGMENTS.yml`, `SIMULATION.yml`, `CARD.yml`) and 241 CARDs. The show directory is a selfish-COM
object with four interfaces and one CARD, the shape §15 asks for. Rooms and objects outside
moollm are a smaller follow-up survey than characters.

## Decisions

| # | Decision | Leaning | Confidence |
|---|---|---|---|
| L1 | Core keys every character layer carries (above), each with a documented default | yes | 80% |
| L2 | Three relations: `inherits:` (lookup), `derived_from:` (authoring projection), `layers:` (navigation copy) | yes | 70% |
| L3 | Cross-repo references as `moollm://github/<owner>/<repo>/<path>`, resolved to a sibling checkout or URL | yes | 70% |
| L4 | Cast `inherits:` maps split into `inherits:` (the moollm character) and a skills list | yes | 80% |
| L5 | `signifier:` keeps the 👤/🕯️ convention; topical emoji move to `emoji:` | yes | 65% |
| L6 | `type:` names the being's kind; the layer's role (`invitation`, `memorial`, `audience`) moves to `layer:` or `role:` | yes | 60% |
| L7 | Consent: `representation.consent_level` number everywhere; `invitation.consent` stays (it is whether the invitation was accepted) | yes | 75% |
| L8 | `governed_by:` replaces `protocol:` in the biography layer | yes | 70% |
| L9 | `status:` for life facts is allowed in SCHEMA.md; `invitation.status` lints against `schemas/invitation-workflow.yml` | yes | 70% |
| L10 | A cross-layer lint: same-id layers agree on name, life facts, consent level; check bill-joy and scott-draves by hand first | yes | 85% |
| L11 | Flatten the `character:` envelopes in wwsff and DonHopkins (434 files), with each repo's own commit | yes | 75% |
| L12 | wwsff `schemas/` declare that they extend moollm skills (character, representation-ethics, advertisement) with `inherits:` | yes | 65% |
