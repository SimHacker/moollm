# place — a subject with a location on Earth

*Read [`GLANCE.yml`](GLANCE.yml) then [`CARD.yml`](CARD.yml) first. This is the protocol:
how a place is keyed, how competing claims are held, and what may leave the repo.*

`room` knows what is inside it and which way is out. `place` knows where it is. Almost
everything on a map inherits both, and the combination is the normal case:

```yaml
inherits: [coffeeshop, room, place]   # a shop you can enter, at a tolerated address
inherits: [room, place]               # the same building after the shop closed
inherits: [place]                      # a bench, a bridge, a mural, a tour stop
```

Collisions resolve **left to right**, so ordering is how you say what a thing mostly is.

## Article 1: the address is the subject

Key on the address. Never on the name.

A name-keyed row forks the moment a shop rebrands, lies the moment it moves, and orphans
itself the moment it closes. An address-keyed record absorbs all three as ordinary edits:
the trading name is a **tenancy**, and a rebrand appends one. The bonus is the question
that name-keyed data can never answer -- *what used to be here* -- which falls out for
free, because former tenants are earlier entries in the same list.

Amsterdam makes this literal. The burgemeester tolerates cannabis sales at **addresses**,
not at businesses; the shop is what is currently standing on a tolerated spot.

The id is a slug: `oudezijds-voorburgwal-88h`. It never changes, even when everything
inside it does.

## Article 2: matching addresses is the whole game, and Dutch fights back

One street, five spellings. `1e Const. Huygensstraat` is `EERSTE CONSTANTIJN
HUYGENSSTRAAT`. Normalize before comparing: fold case and diacritics, expand
abbreviations, map ordinals onto digits (`eerste`, `1ste`, `1` → `1e`).

**Exclude the huisletter from the key.** The roster says `Amstel 8 H`, a directory says
`Amstel 8`, and a shopfront says neither. Matching on street plus number and *reporting*
the suffix disagreement finds the shop; matching on the full triple silently loses it.
The disagreement is worth keeping -- it is often the tell for a renumbered building.

House-number ranges (`88-90`) keep the low end and note the range. Which brings us to:

**Orphan pairs.** When an authority lists a number nobody uses and a directory names a
number the authority does not list, on the same street, a few doors apart, that is almost
always **one place wearing two numbers** -- not two problems. Pair them and put one look
at the door on the list. Amsterdam's Bulldog sits at 88 or 90 depending on who you ask.

## Article 3: coordinates are claims, and averaging them is a lie

A place collects coordinates: a government geocoder, a directory, OSM, and the GPS in
your pocket when you stood at the door. They disagree, sometimes by a whole building.

```yaml
coordinates:
  preferred: { lat: 52.3744626, lng: 4.8813694, source: field-survey }
  spread_m: 63           # two sources point at different buildings; the pair is the story
  claims:
    - { lat: 52.3744626, lng: 4.8813694, source: field-survey, observed: 2026-09-20 }
    - { lat: 52.3739900, lng: 4.8809100, source: cannamaps,    observed: 2026-09-15 }
```

Never write the mean. It is a point nobody asserted, it is usually in the canal, and it
destroys the only signal that says *go look*. Choose by documented source preference,
publish the spread, and let a high spread sort itself to the top of the review queue.

## Article 4: every source carries a license, and one field has teeth

`sources.yml` holds each source's license and one boolean, `osm_ok`. A build step refuses
to put a claim into the upload set unless its source says true.

| Source kind | Example | osm_ok | Why |
|---|---|---|---|
| Your own survey | photo, GPS trace, what the staff said | **yes** | yours, current, clean |
| Official publication | a municipal roster, a national geocoder | **yes** | open, and usually free of copyright by statute |
| The commons | OpenStreetMap itself | **yes** | ODbL, share-alike coming back |
| Scraped compilation | somebody's unlicensed directory | no | all rights reserved by default; EU database right may apply |
| Proprietary maps | anything Google-derived | **never** | extraction is forbidden; an import gets reverted and can flag the account |
| Memory | "I think it was called..." | no | a lead, not a survey |

This is why the bike ride is not merely nicer than desk research. **A field survey is the
only evidence that is both current and unambiguously yours to upload.** Everything else
is a lead telling you where to point the camera.

## Article 5: two kinds of past, never one column

A former trading name and a former use of the building are different pasts:

```yaml
tenancies:                  # who SOLD here
  - { name: "Mellow Yellow", until: 2016-12-31, cause: school-distance }
site_history:               # what the BUILDING was
  - what: "a used-horse depot, whose owner invented a crane for lifting horses out of the canal"
    confidence: lead        # remembered, not yet cited
```

Merge them and the guide starts telling people a horse depot sold hash. Keep them apart
and each stays interesting, with its own confidence ladder: **lead → cited → verified**.

## Article 6: review reasons name themselves

Nothing is flagged "needs attention". Every reason says what it is and what would settle
it, because a queue you cannot act on is a queue you will not work:

- `no-name` — on the roster and nobody names it. *Ride past and read the sign.*
- `roster-only` — a tolerated address invisible to every directory. *The most interesting row in the file.*
- `off-roster-but-open` — a source says open where the authority tolerates nothing. *Closure, move, or bad number.*
- `coord-conflict: 63 m` — two sources, two buildings. *Stand at the door with GPS.*
- `probable-renumbering` — paired with a named neighbour. *One look settles both.*
- `no-usable-coord` — no coordinate from a source we may publish. *Geocode officially, or go.*
- `stale-menu: 2011` — the newest evidence is fifteen years old. *Assume nothing.*

## The pipeline, in one line

```
authority + directories + memory  →  claims  →  places/*/PLACE.yml  →  derived views (CSV, SQL, map)
                                                        ↑
                                              survey writes here, and wins
```

YAML is the truth. Spreadsheets and databases are **derived and disposable**; regenerate
them, never edit them. The importer bootstraps a place once and afterwards only ever
*proposes*, because the human-authored comments in a PLACE.yml are data too, and a
generator that overwrites them is a generator that deletes the fieldwork.

## Related

- [`skills/room/`](../room/) — the interior; a place you can enter is both
- [`coffeeshop`](https://github.com/SimHacker/amsterdank/tree/main/skills/coffeeshop) — the first business type built on this, and it lives in
  [amsterdank](https://github.com/SimHacker/amsterdank) rather than here, because a tolerated
  address under a Dutch municipal beleidsregel is not a general-purpose idea. `place` is
  general; its subclasses belong wherever their jurisdiction and their data do.
- [`designs/webtop/OPENSTROLLMAP.md`](../../designs/webtop/OPENSTROLLMAP.md) — the subjective layer over OSM's objective geometry
- [`designs/webtop/SIGNED-ASSESSMENTS.md`](../../designs/webtop/SIGNED-ASSESSMENTS.md) — why assessments are signed and never averaged
- [`designs/webtop/EBIKE-PATH-GRAMMAR.md`](../../designs/webtop/EBIKE-PATH-GRAMMAR.md) — how a place is met at riding speed
- [`designs/webtop/TOURS-AND-PLAYLISTS.md`](../../designs/webtop/TOURS-AND-PLAYLISTS.md) — stringing places into a ride
