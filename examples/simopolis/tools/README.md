# Simopolis Tools

**The original Sims tools, reimagined with AI.**

The Sims 1 shipped with powerful community tools: the Transmogrifier (object editor), FaceEditor (character appearance), and various lot/house tools. The modding community built more. These tools are why The Sims had the largest user-created content library of any game.

Simopolis reimagines these tools with AI assistance. Instead of manually editing pixel-level sprites, describe what you want and the LLM generates it. Instead of hand-crafting object behavior trees, specify the object's purpose and advertisements in YAML.

## Available Tools

| Tool | Original | Simopolis Version |
|------|----------|-------------------|
| [Transmogrifier](./transmogrifier/) | Manual sprite/mesh editor | AI-powered object creation from descriptions |
| [Face Editor](./face-editor/) | Pixel-level skin painting | Image generation from character descriptions |
| [Body Editor](./body-editor/) | Mesh vertex manipulation | Body type generation from personality |
| [House Builder](./house-builder/) | Grid-based lot editor | AI-assisted lot layout from descriptions |
| [Family Album Maker](./family-album-maker/) | HTML template system | Markdown generation from CHARACTER.yml data |

## The Original Transmogrifier

The Transmogrifier (`SimsKit/Transmogrifier/` in TheSims source) was the official object editing tool shipped in the SimsKit. It allowed modders to:
- Clone existing objects as starting points
- Edit sprite frames (the visual appearance)
- Modify object data (advertisements, interactions)
- Export and share custom objects as .iff files

The community used it to create everything from custom furniture to entire expansion-pack-quality content sets. The tool's accessibility was a design choice by Don Hopkins — make the creation tools as powerful as the game itself.

## AI-Powered Creation

In Simopolis, the creation pipeline is:

```
Description (natural language)
       ↓
LLM generates YAML definition
  object properties, advertisements, interactions
       ↓
Image generation for visual appearance
  sprites, textures, skins
       ↓
SimObliterator writes .iff file
  binary format for The Sims compatibility
       ↓
Object available in both Simopolis and The Sims
```

## See Also

- [Objects](../objects/README.md) — The catalog these tools create for
- [Exchange](../exchange/README.md) — Where created content is shared
- [SimObliterator Suite](../../../../SimObliterator_Suite/) — Binary format tools
- [TheSims / SimsKit](../../../../Code/TheSims/SimsKit/) — Original Maxis tools
