# Image Mining Scripts

> *"The image IS the database."*

## Scripts

### `mine.py` — Image Mining CLI

Extract semantic resources from images using the Three Eyes.

```bash
# Basic mining
python mine.py mine image.jpg

# With specific depth
python mine.py mine image.jpg --depth deep

# Multi-look with lens
python mine.py multi-look image.jpg --lens emotional
```

### `exif.py` — EXIF Metadata CLI

Read, write, and manage EXIF metadata — the Fourth Eye.

```bash
# Read all metadata
python exif.py read image.jpg

# Read specific field
python exif.py read image.jpg --field GPS

# Write metadata
python exif.py write image.jpg --field Description --value "Amsterdam sunset"

# Create -exif.yml sidecar
python exif.py sidecar image.jpg

# Inject sidecar back into image
python exif.py inject-sidecar image.jpg

# Batch create sidecars
python exif.py batch ./photos

# Create searchable index
python exif.py index ./photos --to INDEX.yml

# Strip metadata (privacy)
python exif.py strip image.jpg --keep GPS DateTime

# Compare metadata
python exif.py diff image1.jpg image2.jpg

# List field categories
python exif.py categories
```

## Dependencies

**Required:**
- Python 3.10+
- PyYAML (`pip install pyyaml`)
- exiftool (system command)

**Install exiftool:**
```bash
# macOS
brew install exiftool

# Ubuntu/Debian
apt install libimage-exiftool-perl

# Windows
# Download from https://exiftool.org
```

## The Four Eyes

```
👁️ LEFT EYE   — PHOTO.yml   — Structure (what IS)
👁️ RIGHT EYE  — PHOTO.md    — Narrative (how it FEELS)
👁️ THIRD EYE  — MINING-*    — Meaning (what it MEANS)
🧬 FOURTH EYE — EXIF        — Facts (EMBEDDED in file)
```

`mine.py` powers the first three eyes.
`exif.py` powers the fourth.

## Related

- `../examples/` — Diverse sidecar examples
- `../CARD.yml` — Full skill documentation
- `../SKILL.md` — Protocol details
