# Image Mining Examples

> *"The map is not the territory. The example is not the rule."*

## What's Here

**10 diverse `-exif.yml` sidecar examples** showing different metadata patterns for different image types. Each filename describes the scenario. Each file shows one possible way to structure your metadata.

**These are SUGGESTIVE, not DEFINITIVE.** Jazz your own metadata.

## The Examples

| File | Type | Demonstrates |
|------|------|--------------|
| `amsterdam-sunset-canal-exif.yml` | Travel photo | GPS, weather, story, series membership |
| `dall-e-cyberpunk-cat-exif.yml` | AI generated | Prompts, seed, variations, prompt iteration |
| `family-christmas-2024-exif.yml` | Family event | People tagging, relationships, traditions |
| `scanned-grandma-wedding-1952-exif.yml` | Historical scan | Estimated dates, provenance, restoration |
| `screenshot-error-message-exif.yml` | Tech screenshot | Bug tracking, system context, reproduction |
| `drone-aerial-beach-exif.yml` | Drone footage | Flight data, regulations, gimbal angles |
| `food-sushi-dinner-exif.yml` | Food photo | Restaurant, dish details, dietary info |
| `product-shot-coffee-mug-exif.yml` | Commercial | Client info, product specs, usage rights |
| `selfie-at-concert-exif.yml` | Social event | Event, venue, artist, memories |
| `art-museum-painting-exif.yml` | Art documentation | Artwork details, artist, museum context |

## The Four Sections

Every `-exif.yml` sidecar has four top-level sections:

```yaml
exif:      # Standard camera/GPS/datetime metadata
mining:    # YAML Jazz from Three Eyes
prompts:   # Generation prompts (AI images)
jazz:      # Arbitrary custom metadata (YOUR stuff)
```

### exif — Standard Metadata
What the camera recorded: Make, Model, ISO, GPS, DateTime, etc.

### mining — Three Eyes Output
What was extracted by image mining: resources, observations (left/right/third eye), characters, facets.

### prompts — AI Generation
For AI-generated images: model, prompt, negative_prompt, seed, variations, iterations.

### jazz — Your Metadata
Freeform YAML Jazz: projects, ratings, stories, workflow, links — whatever you need.

## How to Use These

**Learn by example:**
```bash
# See how travel photos are structured
cat amsterdam-sunset-canal-exif.yml

# See how AI images track prompts
cat dall-e-cyberpunk-cat-exif.yml
```

**Search across examples:**
```bash
# Find examples with GPS data
grep -l "GPSLatitude" *.yml

# Find examples with ratings
grep -l "favorite: true" *.yml
```

**Adapt for your images:**
1. Find an example similar to your use case
2. Copy the structure
3. Delete what you don't need
4. Add what you do need
5. Jazz freely

## Philosophy

💬 *"EXIF is the canonical truth. No database needed."*
   — Jaisen Mathai (2026)

💬 *"Show, don't tell. Example, don't enforce."*

The best metadata schema is the one you actually use. Start simple. Add fields when they matter. These examples show what's *possible*, not what's *required*.

## Related

- `../scripts/exif.py` — CLI for reading/writing EXIF and sidecars
- `../scripts/mine.py` — CLI for image mining
- `../CARD.yml` — Full skill documentation
- `../SKILL.md` — Protocol details
