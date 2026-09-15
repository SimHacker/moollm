# Verbs, pie menus, and rubrics that score a life over its own log

A bench is an object that advertises `SIT`, `EAT`, `SMOKE`, `NAP`, `WAIT`, `READ`, `WATCH-DUCKS`.
Pick one from a pie menu, it happens, it gets logged, and consequences follow. Scores are then
computed over the log by **rubrics**, which are data rather than code -- so a nanogame is ten
lines of YAML and anybody can write one.

This is The Sims' architecture pointed at real street furniture. Objects advertise scored
actions; the actor picks; the pie menu is the picker. All three parts already have a lineage
here, which is why this is a small design rather than a large one.

## The object advertises; the menu is generated

```yaml
# spots/vondelpark-pond-bench-east.yml
inherits: [bench, spot, place]
osm: { type: node, id: 1234567890, tags: { amenity: bench, backrest: yes, direction: 265 } }
seats: 3
advertises:
  - { verb: SIT,         always: true }
  - { verb: EAT,         when: "you are carrying food" }
  - { verb: SMOKE,       when: "you are carrying something from inventory/" }
  - { verb: NAP,         when: "sun is on it and nobody else is" }
  - { verb: WATCH-DUCKS, when: "always, and it is underrated" }
```

The menu is not authored per object -- it is **rendered from `advertises:`**, filtered by what
you are carrying and what time it is. Add `WATCH-DUCKS` to the bench prototype and every bench
in the city grows the verb. That is the whole reason objects hold their own verbs instead of
the app holding a switch statement, and it is
[directories-as-advertisements](../../skills/design-sense/lenses/directories-as-advertisements.md)
applied to furniture.

## Why a pie menu, specifically

Not nostalgia. On a bench, one-handed, in gloves, in the sun, with a phone: constant distance
to every item, direction rather than position as the target, no scanning of a vertical list,
and muscle memory after the third use so the menu stops being read at all. That is
[Fitts](../../skills/design-sense/lenses/fitts.md) doing the work it was measured doing in
CHI'88 -- and the measurement is the point, since the alternative claim would be a matter of
taste.

Six to eight verbs per object is the working limit, which is also roughly the number of things
you can honestly do with a bench.

## The log

One entry per act. This is the same object as a
[geotoking episode](https://github.com/SimHacker/amsterdank/blob/main/skills/coffeeshop/GEOTOKING.md),
because it turns out an episode *is* a logged verb with an opinion attached.

```yaml
# log/2026-09-20T1625.yml
verb: SIT
where: spots/vondelpark-pond-bench-east.yml
when: 2026-09-20T16:25+02:00
facing: 265                 # degrees true. THE interesting field. See below.
duration_min: 40
consequences: [hunger -1, restlessness -3, sunburn +1]
used: inventory/2026-09-20-white-widow.yml     # if the verb consumed something
thought: "the sun goes down the length of the pond from here"
```

Consequences are data too, declared by the verb, so `EAT` reducing hunger is a line in the
bench's prototype rather than a rule in the engine.

## Direction is the field that makes it a game

**OSM already has this.** `amenity=bench` takes `direction=` in degrees or as a compass point,
alongside `backrest`, `seats`, `material`. So which way a bench faces is mappable, real, and
exactly the kind of question [StreetComplete](https://streetcomplete.app/) asks one tap at a
time. Your own photographs supply it too: `GPSImgDirection` in the EXIF is the bearing the
camera faced, so photographing the view from a bench records the view's direction for free.

Which means the circular histogram is not a gimmick laid over the data. It is a direct
rendering of a field the commons is already collecting.

## Circular statistics, which is the right math and is genuinely fun

Directions are not numbers on a line -- 350° and 10° are twenty degrees apart, not three
hundred and forty. So you cannot average them, and the mean of "north" and "south" is not
"east", it is *nothing*. The tools for this are standard and small:

Convert each of your *n* sittings to a unit vector and sum:

    C = Σ cos θᵢ ,  S = Σ sin θᵢ
    R̄ = √(C² + S²) / n          resultant length, 0 ≤ R̄ ≤ 1
    θ̄ = atan2(S, C)             mean direction, meaningless when R̄ ≈ 0

`R̄ = 1` means every bench you ever sat on faced the same way. `R̄ ≈ 0` means your sittings are
spread evenly around the compass. So:

    balance = 1 − R̄

And the significance test comes free: **Rayleigh's test**, `Z = n·R̄²`, tests the null
hypothesis that your directions are uniform. `Z > 3` on twenty sittings and you have a
statistically detectable bias in which way you like to face, which is a funny thing to be told
about yourself by a park.

**The property that makes it a good game:** you cannot improve balance by sitting more in your
favourite direction. The gradient of the score points at the arc of the compass you have been
neglecting, so the only way to win is to go sit somewhere you have never sat, facing a way you
do not prefer. A scoring function whose gradient points at unexplored city is worth more than
any achievement list.

Display it as a rose diagram: petals per 30° bin, the resultant vector drawn as a needle, and
the balance number under it. Overlay the *available* bench directions in the park and the
histogram stops being about you and starts being about how Vondelpark is built -- benches face
water and paths, so the raw distribution is not uniform either, and a really honest score is
your distribution measured against the park's.

## Rubrics are data

```yaml
# rubrics/bench-compass.yml
name: "Bench Compass"
what: "Sit facing every direction. You may sit anywhere; the bearing is what counts."
over: log/                        # the behavioural history, and nothing else
select: { verb: SIT, place_is_a: bench }
window: all-time                  # or 30d, or this-ride
metrics:
  benches_sat_in:   { count: distinct(where) }
  sittings:         { count: entries }
  balance:          { circular_balance: facing }        # 1 − R̄
  favourite_facing: { circular_mean: facing, only_if: "balance < 0.7" }
  rayleigh_z:       { rayleigh: facing }
goal:  { balance: "> 0.85", benches_sat_in: ">= 20" }
show:  rose(facing, bins: 12)
```

A rubric names a selection over the log, some metrics, a goal, and a display. It does not know
what a bench is and it cannot alter history. Everything a nanogame needs is in that shape, so:

- **`Bench Compass`** — the above.
- **`Bongo Bingo`** — squares are shops, a mark is a photograph with GPS within N metres of the
  square, the goal is a line. Same log, different selection.
- **`Nose Map`** — verb `SNIFF`, metrics over smell reports, goal is coverage rather than balance.
- **`Bridge Toll`** — count distinct bridges crossed, which the path grammar already knows from
  the trace.

Because rubrics are files, patrons can write them, which is what the `curate` and `vote` grants
in [PATRONS.md](../PATRONS.md) are for. A nanogame someone else invented over your own history
is a better present than a feature.

## What not to do

- **No leaderboard by default.** A public ranking of who smoked in the most parks is a
  spectacularly bad artifact to publish about real people, including yourself. Scores are local
  and opt-in, per the privacy rules in GEOTOKING.
- **No score without a visible rubric.** If the formula is not a file you can open and edit,
  the game is a slot machine and the number is a manipulation.
- **Do not gamify the ride into a step counter.** The verbs exist because sitting on a bench
  for forty minutes doing nothing is a legitimate use of an afternoon. A rubric that punishes
  it has misunderstood the city.
- **Never infer a verb from a trace.** A dwell is not a `SIT` and a slow patch is not a `NAP`.
  Logged acts are asserted by the person, or they are not facts.

## Related

- [`EBIKE-PATH-GRAMMAR.md`](./EBIKE-PATH-GRAMMAR.md) — dwell, velocity, and what a trace does and does not prove
- [`TOURS-AND-PLAYLISTS.md`](./TOURS-AND-PLAYLISTS.md) — stringing spots into a route
- [`SIGNED-ASSESSMENTS.md`](./SIGNED-ASSESSMENTS.md) — opinions keep their author and are never averaged
- [`OPENSTROLLMAP.md`](./OPENSTROLLMAP.md) — the subjective layer over OSM's objective geometry
- [`DISPENSERS-AND-SOUVENIRS.md`](./DISPENSERS-AND-SOUVENIRS.md) — objects that give you things to carry
- [amsterdank `GEOTOKING.md`](https://github.com/SimHacker/amsterdank/blob/main/skills/coffeeshop/GEOTOKING.md) — inventory, spots, episodes
