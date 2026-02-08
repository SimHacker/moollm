# Simopolis Family Albums

**The Sims invented social storytelling. We're continuing it.**

The Sims 1 had a groundbreaking feature: the Family Album. The game automatically generated HTML pages with screenshots and captions documenting your Sims' lives. Players would decorate these pages, write stories about their families, and upload them to The Sims Exchange — creating the first mass platform for emergent narrative content.

Before Instagram. Before Facebook Timeline. Before TikTok. There was the Sims Family Album. Millions of families. Millions of stories. All generated from a life simulation running on a Pentium III.

Simopolis brings family albums back. But richer: markdown instead of HTML, AI-generated captions, Mind Mirror personality analysis, relationship arcs tracked over time, and the full narrative depth of MOOLLM characters.

## Available Albums

### Newbie Family Album
**`newbie-family/`** — Bob and Betty's story. The tutorial family, documented. Kitchen fires, budget struggles, Bob's first day of work (pending), Betty's quiet competence. A love story told through domestic survival.

### Goth Family Album
**`goth-family/`** — The Goths, before and after. Mortimer and Bella's early days. Cassandra's childhood. The disappearance. The silence that followed. A mystery told through family photographs with someone missing from every picture after page three.

## Album Structure

```
family-album/
├── README.md          # Album introduction and table of contents
├── pages/             # Individual album pages (markdown)
│   ├── 001-moving-day.md
│   ├── 002-first-meal.md
│   └── ...
├── captions.yml       # AI-generated or hand-written captions
└── timeline.yml       # Chronological event log
```

## Album Features

| Feature | Sims 1 Original | Simopolis Version |
|---------|-----------------|-------------------|
| Screenshots | Auto-captured BMP | Generated descriptions + prompts |
| Captions | Player-written | AI-generated from CHARACTER.yml |
| Pages | HTML templates | Markdown with YAML metadata |
| Sharing | The Sims Exchange | Git repository + web rendering |
| Narrative | Player interpretation | Character voice + Mind Mirror |
| Timeline | Sequential | Branching, with relationship tracking |

## Generation Pipeline

```bash
# Generate album from save data
python3 -m simobliterator album path/to/Family.FAM --output ./family-name/

# Generate album from MOOLLM characters
python3 tools/family-album-maker/generate.py --family newbie --output ./newbie-family/
```

## See Also

- [Characters](../characters/README.md) — The people in the albums
- [Tools / Family Album Maker](../tools/family-album-maker/) — Album generation tool
- [Exchange](../exchange/README.md) — Share albums
