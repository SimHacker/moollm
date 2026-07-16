# Family Album Maker

**The Sims' original storytelling feature, rebuilt for MOOLLM.**

The Sims 1's Family Album was revolutionary: the game automatically captured screenshots of significant events (first kiss, promotion, fire, death) and let players arrange them into HTML pages with captions. Players wrote stories about their Sims and shared them on The Sims Exchange. It was the first mass platform for emergent narrative content.

The Family Album Maker generates rich, character-driven albums from MOOLLM data.

## Generation Pipeline

```
CHARACTER.yml data (traits, relationships, memories)
       ↓
Event detection:
  - Relationship milestones (first meeting, friendship, romance)
  - Career events (hired, promoted, fired)
  - Need crises (fire, hunger, exhaustion)
  - Life events (moving, marriage, birth)
       ↓
Caption generation:
  LLM writes captions in character voice
  Uses soul_philosophy for tone
  Uses mind_mirror for emotional framing
  Uses needs comments for internal monologue
       ↓
Album assembly:
  Markdown pages with YAML metadata
  Timeline tracking
  Relationship arcs
  Character development notes
       ↓
Output: albums/family-name/ directory
```

## Album Page Format

```markdown
# Page Title

**Date**: Day 3, Tuesday  
**Location**: Kitchen  
**Characters**: Bob Newbie, Betty Newbie  
**Event**: Kitchen Fire #2

Bob tried the stove again. Betty was upstairs. The smoke alarm — 
purchased after Fire #1 — did its job. The fire department arrived 
in 47 seconds. Bob stood in the front yard in his underwear.

**Bob's inner voice**: "I followed the recipe this time. I FOLLOWED it."

**Betty's inner voice**: "I heard the alarm. I didn't even get up. 
I just waited for the siren."

---
*Caption: Some lessons take more than one fire. Bob's cooking skill 
remains at 1.*
```

## Commands

```bash
# Generate album from save file
python3 tools/family-album-maker/generate.py --save path/to/Family.FAM --output ../albums/family-name/

# Generate album from existing characters
python3 tools/family-album-maker/generate.py --family newbie --characters ../characters/ --output ../albums/newbie-family/

# Add a page to existing album
python3 tools/family-album-maker/add-page.py --album ../albums/newbie-family/ --event "kitchen-fire-3"
```

## See Also

- [Albums](../../albums/README.md) — Generated albums
- [Characters](../../characters/README.md) — Source character data
- [Exchange](../../exchange/README.md) — Share albums
