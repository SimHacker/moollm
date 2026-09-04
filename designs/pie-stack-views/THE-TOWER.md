# The Tower

*Don Hopkins · September 2026*

**Thesis:** The semantic pyramid is not a ladder from glyph to full text. It is a SimTower: a 2D map of rooms at each level, with typed connectors between levels, and a *signed* vertical axis where up is how a thing presents itself and down is what holds it up. MOOLLM already shipped a worked instance of this and did not label it as one.

Part of the **pie-stack-views** design cluster ([README](README.md)). The menu-as-palace case: [Pie Menu Memory Palaces](PIE-MENU-MEMORY-PALACES.md). The record format: [View State Ancestors](VIEW-STATE-ANCESTORS.md).

---

## Cards carry both kinds of link

A card carries geographic links — lateral neighbors — and abstract links, `up` and `down` in detail. Once both exist, the pyramid stops being a single ordered sequence. Detail becomes a *floor*; topic becomes a *position on that floor*; and how you move between floors is a design choice with its own vocabulary.

A card is also **a contribution you make to the place that contains it**, which is the move that connects this to the tour case in [Views as Testimony](VIEWS-AS-TESTIMONY.md). A StoryMaker, ShowMaker, or eBike Safari scene attaches to a *where* — a location in a memory palace, a node in a mind map, or an actual physical place — not to a thread. The author picks the rung: a card can be a glyph, a title, a paragraph, or a fully produced scene mixing video, audio, structured JSON schema and YAML jazz, and it is the same kind of object at every one of those detail levels. Making it more detailed does not change what it is or where it lives; it fills in a lower rung.

Which means the card and the view are one shape from opposite directions. A card is an *authored* rung attached to a target. A view is a *chosen path* through rungs of a target. Both point rather than copy, both carry an author, both are addressable. That suggests one record type with two uses rather than two subsystems.

## The worked instance

[`examples/adventure-4/street/lane-neverending/`](../../examples/adventure-4/street/lane-neverending/) is a strip of street segments — `w3 w2 w1 center e1 e2 e3` — with buildings along it: Acme Surplus, Seymour Blooms the florist, Leela Manufacturing, the NO-AI Tower, and the Church of the Eval Genius, which states its own ancestry: *"a **loving parody** of the Church of the SubGenius, with sincere respect for its lineage and its weird. Slack is remembered. Bias is declared. The building keeps the score."*

That last sentence is this cluster's thesis, written earlier and elsewhere, as set dressing.

## The lateral axis is a cellular automaton neighborhood

`w3 w2 w1 center e1 e2 e3` is not a naming whim. It is literally cellular automata neighborhood
notation: cells indexed by signed offset from center, a one-dimensional neighborhood of radius 3.
The lane is described in its own design doc as *"a road that is whatever length it needs to be"* —
an unbounded lattice — and the buildings are cell states.

That makes the coordinate system explicit and gives the two axes different mathematics. **Laterally
you are in a CA neighborhood; vertically you are on a pyramid rung.** And a CA neighborhood is
already a sparse local view: a rule reads a fixed-radius window over the lattice and cannot see past
it, which is exactly the *scoped* reading that [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md)
formalizes and exactly the constraint the underground tunnel violates on purpose — a link that
reaches outside the neighborhood, invisible to any local rule.

The lineage here is not borrowed. [CAM6](https://github.com/SimHacker/CAM6) and Micropolis are both
cellular automata, and the neighborhood-plus-rule model is the one Don has been building worlds in
for decades. Naming the street segments this way is that habit surfacing.

## The vertical axis is signed

Street level is zero. Going up is *how the institution is seen*; going down is *how it actually works*. The church's own README tabulates its rooms in floor order already — the reading below is a re-reading of that table, not an invention — and every floor is a real directory.

| Rung | Where | The room |
|---|---|---|
| glyph | from the sky, miles off | the **crown** — the silhouette that identifies it without entry |
| title | the lane | facade and sign |
| abstract | ground | **Narthex of Declared Bias** — the summary it gives a visitor at the door |
| body | working floors | Audit Choir, Bias Library, Experiment Loft, Rubric Forge, Mirror Room |
| vantage | top | **Roof of Judgment** — "vane, garden, and skyline" |
| −1 | below | **Evidence Cellar** — logs, transcripts, receipts |
| −2 | below | **Bias Engine Room** — the gears that manufacture what the narthex asks you to declare |
| −3 | below | **Null Chapel** — type `silence` |
| −4 | below | **Refusal Vault** — abstention is also a score |
| −5 | bottom | **NO-AI Embassy** — the treaty with its declared enemy |

Descending is not "more elaboration." Each basement is more load-bearing and less publicly admitted than the floor above. The building's vertical axis *is an argument*, which is the only reason it works as a pyramid.

## The crown is the glyph rung, and the skyline is the contact sheet

You identify a building from across the city, from the air, looking down, without entering: one shape, no text. That is exactly the test the [glyph benchmark](../webtop/GLYPH-BENCHMARK.md) sets — recognizable at pie-slice size, distinct from its neighbors on the same street. A skyline is a grid of glyphs whose only job is to be told apart at a distance.

Note the duality at the top. The crown is the glyph *of* the building seen from outside; the Roof of Judgment is a *view from* the building looking down at the lane. Same floor, opposite directions — the card and the view again.

The lane's `slideshow/` directory is already this rung rendered. From the Gezelligheid Grotto at dusk: *"Down the block to the west, Leela's tall silhouette is visible in the distance. Farther still, the NO AI sign isn't in frame, but its presence stains the air: a faint magenta haze."* Identification at distance by silhouette, plus a building exerting presence past the edge of the frame — the glyph rung and the off-screen backlink, written as a photograph.

## Connectors are typed, and the type is a UI claim

Stairs walk one rung at a time; an elevator skips rungs. The church's `no-ai-elevator` has a panel reading *"If you want a miracle, take the stairs."* Progressive disclosure versus the popup that drops you straight to the bottom, argued as set dressing. The kinetic-navigation contract from [Pie Menu Memory Palaces](PIE-MENU-MEMORY-PALACES.md) applies unchanged: automatic transit when unattended, manual the instant it is touched.

## The tunnel is intertwingularity you cannot see from above

Church `basement-5` exits east to `../../no-ai-tower/basement-church-embassy/` — a relative path that *leaves its own subtree* to land in the mirror-image embassy in the rival's basement. Two institutions whose public faces oppose each other, joined at their deepest private level, with ambassadors posted on both sides. The room says so itself: *"Legends say this treaty hall does not exist. The door is never listed on public maps."*

No amount of zooming out reveals that link. It is only visible from the bottom, which is the honest structural claim about conspiracies and about dependency graphs alike.

## Each building type gets its own vertical semantics

The church descends epistemically — evidence, mechanism, silence, refusal, treaty. Leela Manufacturing descends *logistically*, and tabulates that too: Rooftop, 3 Shipping, 2 Factory, 1 Intake, G Lobby, B Basement, plus off-floor Loading Docks, a Storage Complex, Warehouse 23 for long-term artifacts, and a Mail Room with pneumatic tubes and pigeons. Storage, catalogs, mail, bookkeeping, docks and logistics networks are what sits under a factory the way receipts and abstentions sit under a church. Same signed axis; the content of "down" is set by what kind of institution it is. The Factorio reading is explicit in the corpus — a Factorio-inspired model of real data flow — and connects to the conveyor-belt treatment of peripheral views in [Views as Testimony](VIEWS-AS-TESTIMONY.md).

## A slogan is a name with many bindings

Leela's tagline *Manufacturing Intelligence* is not a double meaning but a stack of them, enumerated in [`skills/leela-ai/CARD.yml`](../../skills/leela-ai/CARD.yml): AI for manufacturing, where customers manufacture and we supply intelligence; building AI; Papert's constructionism; Kay's personal dynamic media, since watching Papert's Logo children shaped the Dynabook; Minsky's Society of Mind assembling intelligence from simple agents; Chomsky's *Manufacturing Consent* and the ethical awareness of engineered agreement; and growth mindset.

Which makes it the exact object PSIBER's definition editor was built for — one name, every definition in scope, all openable ([Peripheral Views](PERIPHERAL-VIEWS.md)).

And the readings are partly **sited**. Leela's basement R&D lab is listed as "Schema mechanism, causal learning," so Drescher's *Made-Up Minds* has a room, on the floor where foundations go, which is correct; the Minsky lineage is literal as well as intellectual, since Leela's CTO is Henry Minsky. But Chomsky's reading has no room and constructionism has no room. The building is a partially populated definition editor for its own name, and the empty floors are a to-do list rather than an omission. The floors you have not built are the readings you have not yet taken seriously.

## It is fractal

Each room carries its own `GLANCE.yml`, `README.md`, and `ROOM.yml` — glance rung, prose rung, machine rung — and the contract holds for all fourteen church rooms without exception. The glance rung is genuinely terse; the Rubric Forge's whole file is a name, a type, one sentence, a resident, a sign, a note, and its exit:

> description: Heavy table, iron weights, wall of criteria cards. Where people argue about weightings then commit.
> sign: "WEIGHTS ARE CHOICES. WRITE THEM DOWN."
> note: The forge isn't hot — it's focused.

Every room is a small pyramid, the building is a pyramid of pyramids, the lane is a pyramid of buildings, and the same three-file contract holds at every scale. That is the HyperTIES article schema ([`webtop/hyperties/ARTICLE-SCHEMA.md`](../webtop/hyperties/ARTICLE-SCHEMA.md)) enforced by directory convention.

## The palace was wired one way

The point of the building is to be a memory palace for a design corpus: `designs/eval/` holds about thirty documents, seven of them church-specific — a [constitution](../eval/CHURCH-EVAL-GENIUS-CONSTITUTION.md), [doctrine](../eval/CHURCH-EVAL-GENIUS-DOCTRINE.md), [liturgy](../eval/CHURCH-EVAL-GENIUS-LITURGY.md), [sisters](../eval/CHURCH-EVAL-GENIUS-SISTERS.md), [founders](../eval/CHURCH-EVAL-GENIUS-VAL-AND-FOUNDERS.md), [the hub](../eval/CHURCH-OF-THE-EVAL-GENIUS.md), and [the building map](../eval/CHURCH-EVAL-GENIUS-LANE-NEVERENDING.md). You learn the doctrine by walking floors that embody it.

It half worked, and the missing half was mechanical. The links ran design-doc → room and not back. `CHURCH-EVAL-GENIUS-LANE-NEVERENDING.md` *is* the directory map, listing `narthex/`, `rubric-forge/`, `basement-1-evidence/` by path; `EVAL-VS-SIM.md` carries a "go visit" table. But grepping `designs/` across the entire church room tree returned nothing — not one `ROOM.yml`, `README.md` or `GLANCE.yml` in the building pointed at the doctrine it embodied. The index knew about the palace and the palace did not know it was an index. For *discovery* — standing in the Refusal Vault, wanting to know what refusal means here — the wiring was absent; you could only find the doctrine if you already had it open.

That is the orphan failure named in [View State Ancestors](VIEW-STATE-ANCESTORS.md), arriving from the other side: the rooms were the orphans. The fix was one key per room:

```yaml
  learn:
    - doc: ../../../../../../designs/eval/CHURCH-EVAL-GENIUS-DOCTRINE.md
      why: "Abstention is also a score"
    - doc: ../../../../../../skills/no-ai-moralizing/CARD.yml
      why: "REFUSAL-THEATER — refusing as performance vs refusing for cause"
```

All fourteen church rooms now carry one, twenty-three backlinks total, every path validated by resolution. The mapping lives in the rooms themselves rather than in a manifest, so the applying script was scratch and is not checked in. The side benefit is that the empty-floor observation above became checkable: a reading with no room and a room with no reading now both show up as a dangling half.

Writing them also exposed drift the one-way wiring had hidden — the design doc's tree listing stops at `basement-4`, because the NO-AI Embassy was built afterward and nothing told the document.

## Honest cost

Free-form organization means the vertical axis carries meaning *only if the author is disciplined about it*. A building whose basements are merely more rooms teaches a reader nothing and is worse than a flat list, because it implies a gradient that is not there. The church earns its floors. Most generated buildings will not, and there is no mechanical check for this — only editing.

---

## Related

- [Pie Menu Memory Palaces](PIE-MENU-MEMORY-PALACES.md) — the menu promoted to a place; DreamScape, MediaGraph, iLoci
- [Views as Testimony](VIEWS-AS-TESTIMONY.md) — tours as saved views; Factorio conveyors
- [View State Ancestors](VIEW-STATE-ANCESTORS.md) — Bush's trails, the record format, the orphan cost
- [Peripheral Views](PERIPHERAL-VIEWS.md) — the definition editor, and the glyph vocabulary
- [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) — inheritance and override across nested scopes
- [Church of the Eval Genius](../eval/CHURCH-OF-THE-EVAL-GENIUS.md) · [the building](../eval/CHURCH-EVAL-GENIUS-LANE-NEVERENDING.md)
- [FACTORIO-MOOLLM-DESIGN](../FACTORIO-MOOLLM-DESIGN.md) — visible machinery as design vocabulary
- [webtop/hyperties/ARTICLE-SCHEMA.md](../webtop/hyperties/ARTICLE-SCHEMA.md) — the four-part node contract the file trio implements
