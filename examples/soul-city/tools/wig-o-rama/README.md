# Wig-O-Rama

**The wig shop of Soul City. Collect wigs, apply wigs, wig your pets.**

Wig-O-Rama is a shop and a collection system: browse a catalog of wigs, collect the ones you love, and apply them to any citizen — Sim, cat, or dog — through the [Wig-O-Matic](../../objects/electronics/wig-o-matic.IFF-OBJECT.yml) object placed in any lot.

The lineage is the "-O-Matic" family from the original Transmogrifier plans ([Autofac vision](../transmogrifier/README.md#the-autofac-vision-from-autofactxt)): Rug-O-Matic made rugs from images; Wig-O-Matic makes wigs from descriptions. Wig-O-Rama is the storefront around it — PetBed-O-Matic's spirit, Head Shop energy.

## How wigs work

A wig is a **head-layer overlay**: a texture (and optionally a mesh) that composites over a character's existing head without replacing it. Take it off and the original face is untouched — wigs are reversible by construction.

```
Wig definition (YAML)
       ↓
Texture generation (AI or hand-painted)
  mapped to head mesh UVs — adult, child, cat, dog variants
       ↓
Overlay compositing
  wig layer above head texture, below hats
       ↓
Round-trip export
  Sims 1 skin (.bmp + .cmx) via SimObliterator — game-compatible
```

Because the exchange templates already model **adult, child, cat, and dog** heads ([SKINS-AND-MESHES.yml](../../exchange/templates/SKINS-AND-MESHES.yml)), one wig definition can declare fits for any subset of species. A powdered periwig for Mortimer is a `C` (cranium) overlay on the adult head mesh; the same style declared for `cat` renders on the cat head mesh. Yes, the cat judges you. The wig stays on.

## The collection

Wigs live in the wearer-agnostic catalog:

```
wig-o-rama/
  catalog/
    <wig-id>.WIG.yml     # style, era, species fits, texture prompts
```

A `WIG.yml` names the style, its era and story, which species it fits, and how to generate or locate its textures. Collected wigs are referenced from a character's `CHARACTER.yml` inventory; the currently worn wig is part of their appearance state.

## Applying a wig

In-world, wigs are applied at the **Wig-O-Matic** — a salon-chair contraption with a mirror, a mannequin-head carousel, and a pneumatic fitting dome. Interactions:

| Interaction | Who | Effect |
|-------------|-----|--------|
| Try On Wig | Sims | Browse collection, preview, wear — Fun +15, Room +2 |
| Wig Your Pet | Sim targeting cat/dog | Fits the pet variant — Fun +20 for the Sim; the pet's dignity is its own affair |
| Remove Wig | Sims, pets | Restores natural head |
| Restock Carousel | Sims | Pulls newly collected wigs from the catalog |

## See Also

- [Wig-O-Matic object](../../objects/electronics/wig-o-matic.IFF-OBJECT.yml) — the machine itself
- [Face Editor](../face-editor/) — head texture pipeline the wig layer composites over
- [Transmogrifier](../transmogrifier/) — the "-O-Matic" family history
- [Exchange templates](../../exchange/templates/SKINS-AND-MESHES.yml) — adult/child/cat/dog head meshes
