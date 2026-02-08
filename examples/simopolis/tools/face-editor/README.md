# Face Editor

**Character appearance generation from personality data.**

In The Sims 1, character appearance is defined by "skin suits" — pre-rendered sprite sets that combine head, body, and clothing into animation frames. The game shipped with a limited set of skins. The community created thousands more.

The Simopolis Face Editor generates character appearances from personality descriptions and CHARACTER.yml data. Instead of painting pixels, describe the character and generate their look.

## How It Works

The Sims 1 appearance pipeline:
- **Head mesh**: BCF/CMX format (bone/mesh data)
- **Skin textures**: BMP files mapped onto the mesh
- **Sprite frames**: Pre-rendered from all 4 rotations for each animation

SimObliterator can read SPR2 sprites and export to PNG. The mesh pipeline reads BCF/BMF/CMX/SKN and exports to glTF. Image generation can:
- Upscale original skin textures from 64x64 to high resolution
- Generate new faces based on personality traits
- Age characters (child → adult progression)
- Add narrative details (scars, tattoos, expressions from MOOLLM adventures)
- Write new skin textures back into the IFF

## From Traits to Face

```
CHARACTER.yml personality
  outgoing: 8, nice: 2, active: 7
       ↓
Personality → Appearance mapping
  high outgoing → open expression, direct gaze
  low nice → sharp features, set jaw
  high active → lean build, alert posture
       ↓
Image generation prompt
       ↓
Skin texture / portrait
```

## See Also

- [Characters](../../characters/README.md) — The people whose faces we generate
- [Body Editor](../body-editor/) — Body mesh companion tool
- [SimObliterator](../../../../../SimObliterator_Suite/) — Sprite/mesh export pipeline
