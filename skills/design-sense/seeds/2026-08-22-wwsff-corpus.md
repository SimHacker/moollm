# Seed batch: wwsff character corpus + catalogs harvest (2026-08-22)

Raw scout haul; germinate per SKILL.md. Already-germinated items omitted (fitts,
foveation, stage-magic, design-by-accretion, tuned-emergence) except where the scout
found material that should enrich the existing registry file — flagged ENRICH.

## Planted ✅

- ben-shneiderman (master) → [masters/ben-shneiderman.md](../masters/ben-shneiderman.md)
- direct-manipulation → [lenses/direct-manipulation.md](../lenses/direct-manipulation.md)
- don-hopkins (master) → [masters/don-hopkins.md](../masters/don-hopkins.md)
- dynamic-queries → [lenses/dynamic-queries.md](../lenses/dynamic-queries.md)
- emergence-nuance-slider → [methods/emergence-nuance-slider.md](../methods/emergence-nuance-slider.md)
- ENRICH masters/will-wright → done: [masters/will-wright.md](../masters/will-wright.md)
- failure-as-entertainment (+ Calvin Syndrome) → [methods/failure-as-entertainment.md](../methods/failure-as-entertainment.md)
- find-best-n-dither → [methods/find-best-n-dither.md](../methods/find-best-n-dither.md)
- gesture-space-constraints → [lenses/gesture-space-constraints.md](../lenses/gesture-space-constraints.md)
- goldilocks-complexity → [lenses/goldilocks-complexity.md](../lenses/goldilocks-complexity.md)
- ian-bogost (master) → [masters/ian-bogost.md](../masters/ian-bogost.md)
- instance-first → [methods/instance-first.md](../methods/instance-first.md)
- instance-substitution → [methods/instance-substitution.md](../methods/instance-substitution.md)
- mark-ahead-suppression → [lenses/mark-ahead-suppression.md](../lenses/mark-ahead-suppression.md)
- mental-model-compiler → [lenses/mental-model-compiler.md](../lenses/mental-model-compiler.md)
- object-advertisement-economy → merged into [methods/advertisement-economy.md](../methods/advertisement-economy.md)
- oliver-steele (master) → [masters/oliver-steele.md](../masters/oliver-steele.md)
- player-as-storyteller → [methods/player-as-storyteller.md](../methods/player-as-storyteller.md)
- possibility-space → [methods/possibility-space.md](../methods/possibility-space.md)
- power-of-simplicity → [methods/power-of-simplicity.md](../methods/power-of-simplicity.md)
- procedural-rhetoric → [methods/procedural-rhetoric.md](../methods/procedural-rhetoric.md)
- roles-not-characters → [methods/roles-not-characters.md](../methods/roles-not-characters.md)
- self-revealing-gestures → [lenses/self-revealing-gestures.md](../lenses/self-revealing-gestures.md)
- simulation-effect → merged into [lenses/simulator-effect.md](../lenses/simulator-effect.md)

## Todo 🌱

- barycentric-blend-space
- declare-constraints-keep-true (merge with declare-constraints-sync from
  micropolis-palmhoo batch)
- gonzo-ui
- hobby-model / data-portability
- programming-by-demonstration
- slots-all-the-way-down

## Lens candidates

- **self-revealing-gestures** — Gestures you can't see can't be learned (Graffiti);
  show all options radially; every selection rehearses the expert stroke (mark-ahead /
  mouse-ahead) so novices become experts by feel. — Don Hopkins (DDJ 1991, CHI'88).
  `characters/don-hopkins/gesture-space.md`, `sources/ddj-1991-design-implementation-pie-menus.md`
- **mark-ahead-suppression** — If the gesture completes before display latency,
  don't show the menu: self-reveal for learning, suppress for mastery. — Hopkins (DDJ 1991).
- **direct-manipulation** — Continuous representation of the objects of interest;
  physical actions instead of syntax; rapid, incremental, reversible operations with
  immediate visible feedback. — Ben Shneiderman. `characters/ben-shneiderman/`
- **dynamic-queries** — Direct manipulation at exploration scale: drag sliders and
  the database answers instantly. — Shneiderman (HomeFinder).
- **gesture-space-constraints** — Multitouch is maintaining geometric constraints
  between fingers and world (pan/zoom/rotate together), not discrete recognizers
  that lock mid-gesture. — Hopkins (Gesture Space / Pantomime).
- **simulation-effect** — Sparse local rules produce patterns players narrate as
  causal stories the programmer never wired; that imaginative fill-in is the medium.
  — Will Wright (1996 Winograd talk). `bits/theme-simulation-effect/`
- **mental-model-compiler** — The digital model is only a compiler for the mental
  model in the user's head; UI, simulation, and that mental model must stay tractable
  together. — Wright tradition, Hopkins formulation.
  `characters/don-hopkins/teaching-complicated-systems-without-a-manual.md`
- **goldilocks-complexity** — Complexity has a sweet spot: SimEarth too hard (opaque
  failure), SimAnt too simple, SimCity 2000 just right; scale and UI must make
  failure legible. — Wright postmortem ladder.

## Method candidates

- **possibility-space** — Build open-ended possibility spaces; players supply goals
  and stories; design for replay of space, not a single authored path. — Wright (+ Eno
  Long Now dialogue). `characters/will-wright/`
- **failure-as-entertainment** — Users should fail continuously in an entertaining
  way and know why; varied interesting failure is design fuel, opaque failure kills.
  Includes Calvin Syndrome: players destroy first to test if it's alive, then rebuild
  with empathy. — Wright (1996 Winograd; GDC Design Plunder).
- **player-as-storyteller** — Authorship on the caption layer atop emergence:
  Family Album, Exchange, SimProv. — Wright; Hopkins. `catalogs/simprov/`
- **object-advertisement-economy** — "If you're hungry, eat me!": affordances publish
  into an auction scored by motives; the world teaches by what it offers. — Wright;
  Hopkins lift to MOOLLM. (Overlaps moollm advertisement skill; lens file should point.)
- **find-best-n-dither** — Don't take argmax: score, then pick randomly among top N.
  Deliberate suboptimality escapes local maxima, honors that scores aren't truth,
  leaves room for the teacher's override. — Wright (Sims autonomy); Hopkins.
- **procedural-rhetoric** — Rule authorship argues: objects, menus, and institutions
  persuade by what they permit, forbid, and chain. — Ian Bogost. (Whole moollm skill
  exists; design-sense entry should point.)
- **roles-not-characters** — Systems games need seats at the table (mayor, planner),
  not only identifiable protagonists. — Bogost + Hopkins.
  `characters/ian-bogost/roles-not-characters.md`
- **emergence-nuance-slider** — Emergence vs authored nuance is not a binary; put the
  slider in the player's hand: improv ("yes, and" the sim) to playwright (direct every
  beat). — Hopkins reading the Sims community. `catalogs/simprov/README.md`
- **instance-first** — Implement for one real instance; generalize only when a second
  case appears; easier to generalize from two examples than one. — Oliver Steele (2004).
- **instance-substitution** — Instance and class definition syntactically parallel so
  one replaces the other without semantic change (LZX tag = class). — Steele.
- **power-of-simplicity** — Simplicity is the thesis; prototypes are the means;
  keeping prototypes while losing simplicity (JS veneer) misses the point. — Ungar &
  Smith (OOPSLA 1987). ENRICH masters/david-ungar.yml (already has this; check wording).
- **declare-constraints-keep-true** — Declare relationships; the system maintains
  them (Garnet KR, OpenLaszlo, Svelte runes). — Myers; Steele; Hopkins. (Dupes
  declare-constraints-sync in micropolis-palmhoo batch; merge on germination.)

## Master candidates

- **ian-bogost** — procedural rhetoric; systems as protagonists; reading Sims objects
  as argument. `characters/ian-bogost/`
- **ben-shneiderman** — direct manipulation; embedded links; measure-the-UI empiricism
  (CHI'88); dynamic queries. `characters/ben-shneiderman/`
- **don-hopkins** — self-revealing pie/gesture UI; advertisement economy lift;
  teachable microworlds without manuals; constraint-UI lineage. `characters/don-hopkins/`
- **oliver-steele** — instance-first, instance-substitution, reactive declarative UI.
  `characters/oliver-steele/`
- ENRICH masters/will-wright.yml — add: Goldilocks complexity, failure-as-entertainment,
  Calvin Syndrome, hobby model / data portability, player-as-author.

## Secondary (next harvest)

- slots-all-the-way-down (`characters/david-rosenthal/slots-all-the-way-down.md`)
- barycentric-blend-space (`characters/don-hopkins/breakfast-simplex-barycentric-direct-manipulation.md`)
- hobby-model / data-portability (`characters/will-wright/`, `catalogs/soul-city/`)
- gonzo-ui (`characters/edd-coates/ideas.md`)
- programming-by-demonstration (Myers/Lieberman/Drescher thread)
