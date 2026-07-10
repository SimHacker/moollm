# Soul Plaza — Lane Neverending shop district (design)

> *Third places, workshops, apps-with-storefronts — zoned like Sims neighbors on an
> infinite street.*

**Status:** Scoped for future build-out (not implemented yet)
**Where:** **Inside existing segments** — primarily **e2** (Market Square) placeholder
storefronts and south-side lots. **No new street blocks yet** (Don, 2026-07-09): keep the
center dense, walkable, intense, and colorful before splicing `e4`/`w4` onto the loop.

**Lineage:** [Soul City](https://github.com/SimHacker/WillWrightShowForFood/tree/main/catalogs/soul-city)
(browser craft + creation) meets Habitat's zoned neighbors meets the MOOLLM Mall from
[THE-UPLIFT](../../../designs/sim-obliterator/THE-UPLIFT.md) — but **on the street**,
walkable, with sandwich boards. The lane [loops and splices](README.md#splice-topology-how-the-loop-grows);
shops are **lots on the ring**, not a separate mall map.

---

## Zoning model

Like a Sims neighborhood: each business is a **neighbor** on the lane.

```yaml
# conceptual — each shop gets this shape when built
shop:
  address: "14 Lane Neverending"
  side: north | south
  zone: commercial_third_place
  skill_or_design: path/to/the/tool
  storefront_sign: "WIG-O-RAMA — bouffants for every species"
```

Apps, tools, workshops, and shops are the **same thing** at different resolutions —
a directory you can enter. The Semantic Image Pyramid applies: `GLANCE.yml` on the
sandwich board → `CARD.yml` in the window → `SKILL.md` inside → `README.md` for the
deep lore.

---

## The MOOLLM Milk Bar 🥛

**Address:** 10 Lane Neverending (south side, e2) — *kid-friendly, with a wink.*

The [Korova Milk Bar](https://en.wikipedia.org/wiki/A_Clockwork_Orange) served
**moloko plus** — milk laced with whatever made the evening interesting before the
ultraviolence. The **MOOLLM Milk Bar** serves **milk plus imagination**: a third place
where you sit down, order a flavor, and leave **violently creative** (in the good way).

| Kid-facing | Parent wink |
|---|---|
| Milk mustaches, silly straws, comfy booths | "Plus" is dreaming, not drugs |
| Crafting fuel for the shops down the block | Clockwork Orange *costume* in the back room (never on the menu) |
| "Ultra-violet-ence" — paint-splatter craft corner | Ultraviolence → ultra-*violet*-ence |
| Guinea-pig-shaped marshmallows (Pet Shop next door sends referrals) | The milk bar does not serve anything that bites |

**Serves:** rest between shops, LLM "dreaming" sessions (idle imagination while your
object compiles), and the social glue that makes a strip mall feel like a *place*.

Stub: [`e2/moollm-milk-bar/`](e2/moollm-milk-bar/)

---

## Transmogrifier International — the conglomerate

**Transmogrifier** is not one shop — it's the **overarching Sims content-creation
international conglomerate**, like if Rug-O-Matic and Don's 2000 tombstone module grew
up and bought the block. Headquarters at **18 Lane Neverending**; branded branches
up and down the lane.

| Chain member | Address (planned) | What |
|---|---|---|
| **Transmogrifier World HQ** | 18 Lane Neverending (north) | Clone, GUID, export, the whole IFF pipeline |
| **Wig-O-Rama** | 14 Lane Neverending (north) | Wigs + **Wig-O-Matic** machines (stock new units, restock existing lots) |
| **Rug-O-Porium** | 16 Lane Neverending (north) | Rugs + **Rug-O-Matic** machines |
| **Head Shop** | 20 Lane Neverending (north) | Face/body skins (from THE-UPLIFT mall) |
| **Tombstone Studio** | 22 Lane Neverending (north) | Memorial objects (name + eulogy + photo) |
| **Mesh Lab** | 24 Lane Neverending (north) | glTF ↔ SKN, 3D editing |
| **Photo Book Press** | 26 Lane Neverending (north) | Pageable in-game books (guinea pig maintenance!) |
| **Pet Shop / Vet** | 12 Lane Neverending (south) | [THE-PET-SHOP](../../../designs/sim-obliterator/THE-PET-SHOP.md) — heal Nibbles |
| **Simplifier Annex** | 28 Lane Neverending (north) | Don's object simplification lineage |

Stubs: [`e2/transmogrifier-world/`](e2/transmogrifier-world/) · [`e2/wig-o-rama/`](e2/wig-o-rama/) · [`e2/rug-o-porium/`](e2/rug-o-porium/) · [`e2/pet-shop-vet/`](e2/pet-shop-vet/)

**Comedy register — Zach Mama style, trans-inclusive, up-punching:** see below.

---

## Other third places (already on the lane or adjacent)

| Place | Where | Role |
|---|---|---|
| The Gezelligheid Grotto | 7 (center, south) | Pub — ale and stories |
| Leela Manufacturing | 5 (w1, south) | Visual intelligence factory |
| ACME Surplus | 4 (w1, north) | Failed retail (contrast) |
| Church of the Eval Genius | 3 (w2, north) | Bias, refusal, evidence |
| NO AI Tower | 5½ | Logistics, elevator, mashup gallery |

---

## Build-out TODO (scoped, not now)

**Density first.** Fill the lots below before asking for more street. The center should
feel like a **main drag you can walk in five minutes** and still discover something new
every door.

1. Replace e2 placeholder storefronts (12/14/16) and south-side lots — **no new segments**.
2. Wire each `ROOM.yml` exit to its skill/design doc (soul-voice, Pet Shop, Wig-O-Matic…).
3. Add sandwich-board `GLANCE.yml` on each sidewalk (big-endian shop names cluster on
   the listing — MFM locality).
4. Milk Bar: kid-safe menu YAML + one back-room Easter egg sign (Clockwork Orange wink,
   not playable ultraviolence).
5. Transmogrifier chain: shared `TRANSMOGRIFIER-CORP.yml` holding brand, subsidiaries,
   and the joke style guide.
6. Cross-link to Soul City catalog and [Lane Neverending / Habitat](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ben-cerveny/moollm-lane-neverending-habitat.yml).
7. **Later:** splice `e4`/`w4` only when e2–center is full; **much later:** Möbius Street.

---

## Comedy register — Zach Mama × Transmogrifier

### What makes Zach Mama's style work (and why we borrow the *shape*, not the bits)

**Zach Mama** is a French-American comedian and jazz drummer who moved to the U.S. to
play drums in Black churches in North Philadelphia. His delivery is **rhythmic,
cadence-heavy storytelling** with a disarming, self-deprecating innocence — he sounds
like someone who genuinely does not know he is in trouble until the audience is already
laughing.

His most famous bit — the **Monica** joke — is a **life story**, not crowd abuse. Living
in North Philadelphia among Black friends and neighbors, he heard people call each other
cordially **"my [n-word]"** — an affectionate greeting on the street. He **picked it up
there**, with his thick French accent mishearing it as **"Monica"** (misgendering). That
sincere confusion is what he **tells on stage**, often to **primarily Black audiences**
who are not calling him anything; they **laugh hard when they get it**. The tag flips
who is outside the joke: *"If you don't get this joke, you don't have any Black friends.
I do."* He has many other routines that do not ride that gate.

What is breathtakingly beautiful about it — and why a Black audience (and every other
race in the room) roars — is that the comedy is **racial but not racist**:

- **He subverts the power dynamic.** He does not punch down or appropriate. He puts
  himself in total vulnerability and cultural confusion. He is always the butt.
- **The audience grants him insider status.** They can tell he *earned* it — years living
  and playing music with Black families in North Philly — so the bit becomes affectionate,
  shared, boundary-breaking laughter instead of a landmine.
- **The universality is confession, not claim.** Everyone has been the confused outsider
  who misheard a word and committed to the wrong story. His version is just the most
  high-stakes version of that human failure mode.

Find him as [@zachmama on YouTube](https://www.youtube.com/@zachmama) — the "Monica" bit is the one to watch first.

**In-world NPC:** default stand on [e2 northeast corner](../../characters/real-people/zach-mama/) by the Fountain of Infinite Loops; may relocate to this pub's stage when invited or when conversation hits a topic in [`routines.yml`](../../characters/real-people/zach-mama/routines.yml) — the **Annie Hall effect** (expert materializes; no quoted bits). Full tribute: [zach-mama/README.md](../../characters/real-people/zach-mama/README.md).

His own caption on the bit (the meta-joke is part of the joke):

> *"Who still doesn't get this joke? 😂 my favorite part every night is to look at the
> reactions and sit in the discomfort I created, watching people try to help each other
> understand even though they can't explain it too clearly or too loud 🤣 this joke is
> for my real friends who have real friends"*

That's the second punch: the **audience becomes the bit**. Outsiders flail to explain;
insiders already got it. The discomfort zone is a filter — *"for my real friends who
have real friends"* is the same gate as his tag line, turned into a nightly sport.

### The Transmogrifier joke style guide (trans-inclusive, up-punching)

Same **shape**, different words:

| Zach Mama move | Transmogrifier move |
|---|---|
| Mishears a charged word through accent/naivety | Mishears **trans** / **transform** / **Transmogrifier** / **GUID** as one blurry sound |
| Speaker is the butt, never the authority | The **French narrator** or the **conglomerate's pompous signage** is confused; trans people in the audience are in on the joke |
| Insider affection | Celebrates transformation, names, wigs, meshes — the *tools* that let people become |
| Tag flips power | Punch **the conglomerate** ("Transmogrifier International: we put the **mog** in smug") not marginalized people |

**Joke seeds** (signage, NPC bark, Milk Bar napkin doodles — not finished bits):

- *"I went to Transmogrifier International for a makeover. They said 'pick your
  pronouns and your mesh.' I said 'oui.' They said 'that's not a mesh.' I said 'it's a
  French mesh.' They promoted me to Regional Vice President."*
- *"At the Wig-O-Rama they kept saying 'welcome to the family.' I thought they meant
  the **Trans** family, so I brought a casserole. It was a support casserole. Everyone
  cried. The casserole was cloned with a new GUID."*
- *Monica parallel:* *"People kept calling me 'miss' at the mesh export counter. I
  thought they said 'mesh.' So I exported my head to glTF. Now I'm a file. Honestly
  it's better."*
- *"Transmogrifier motto: **Don't call us — do call them!**"* (soul-chat transverse
  Hollywood principle on a corporate billboard)
- *"Rug-O-Porium: we don't judge your floor, we **mogrify** it."*

**Hard rule:** jokes punch **up** at corporate absurdity and **sideways** at the narrator's
confusion. Never punch down at trans people, Black people, or pets. The guinea pig has
enough problems.

---

## Street map (planned overlay on e2/e3)

```
NORTH SIDE (e2 Market Square)
  12 — (south actually: Pet Shop)
  14 — Wig-O-Rama
  16 — Rug-O-Porium
  18 — Transmogrifier World HQ
  20 — Head Shop
  22 — Tombstone Studio
  ...

SOUTH SIDE
  10 — MOOLLM Milk Bar
  12 — Pet Shop / Vet
  ...
```

*Odd/even numbering TBD to match existing lane address conventions when lots are built.*
