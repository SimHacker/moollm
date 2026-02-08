# Body Editor

**Body mesh editing for Sims characters.**

The Sims 1 uses a skeletal animation system with mesh files (BCF, BMF, CMX, SKN) defining character body shapes. The Body Editor works with SimObliterator's mesh pipeline to modify, generate, and export body data.

## Mesh Pipeline

```
Original .iff character data
       ↓
SimObliterator reads BCF/BMF/CMX/SKN chunks
  exports skeleton to JSON
  exports mesh to glTF
       ↓
Modification (AI-assisted or manual)
       ↓
Write back to .iff format
```

## Body Types

The Sims 1 has limited body types tied to the skin system. The Body Editor extends this by generating mesh variations based on character properties:
- Age (child, adult)
- Build (based on Active trait and Body skill)
- Posture (personality-influenced — outgoing Sims stand tall, shy Sims hunch)

## See Also

- [Face Editor](../face-editor/) — Companion tool for head/face
- [SimObliterator](../../../../../SimObliterator_Suite/) — Mesh export pipeline
