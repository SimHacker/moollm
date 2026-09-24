# A persistent clipping service

The rest of this directory makes the clipboard a repo with a forge in front of it: visible, more
than one, editable, never lost, with history, blame and review. This page puts an agent on that
repo, working continuously, and extends clippings from text on a screen to anything a person can
point a phone at.

Press clipping bureaus did this by hand from the 1880s: readers went through newspapers for a
client and mailed the cuttings with the paper's name and date pasted on. Two things carry over.
The clipping arrived with its source attached, and somebody kept working on the client's behalf
after the client stopped paying attention.

## What a clipping holds

```yaml
clipping: 2026-09-24T17:42-drawbridge-sign
content: photo.jpg                  # the bytes, cached
origin:                             # Nelson's link back, kept instead of cut
  kind: photo                       # text | url | file | screenshot | photo | frame | voice | position
  device: phone
  at: 2026-09-24T17:42:08+02:00
  where: { lat: 52.3731, lon: 4.8922, osm_way: 123456789 }
  by: don
readings:                           # the agent's claims, revisable, never merged into content
  - { kind: ocr, text: "Brug open 17:30-18:00", model: tesseract-5, confidence: 0.91 }
  - { kind: describe, text: "bridge schedule sign, Prinsengracht", model: vlm, confidence: 0.8 }
links:
  - { to: 2026-09-10T08:15-same-bridge-closed, why: same place }
```

The content is a cached copy; the origin is the address it came from. That is transclusion with a
cache: the clipping can always say where it came from, which is what the cut-and-paste clipboard
destroys. Readings are claims with a model and a confidence, kept beside the content and never
written over it. A wrong reading gets corrected by a new reading, not an edit that erases the
old one.

## What the agent does

- **Reads.** Text out of photos and screenshots, a transcript out of a voice note, what a frame
  shows. A frontier model for description, a dedicated reader for text, and a person when they
  disagree.
- **Files and links.** Same place, same person, same project, same source, near-duplicates.
- **Resurfaces.** When the current context matches a clipping (the place you stopped, the person
  you are meeting, the file you opened) the clipping comes back. The context is an attention
  mask in the sense of [`../PAIRED-LINKS.md`](../PAIRED-LINKS.md#masks-are-context-windows):
  deliberate, inspectable, and editable by the person.
- **Proposes, never edits.** Refilings, merges of duplicates, corrected readings and summaries
  arrive as pull requests against the clipping repo. The person accepts, edits or rejects them,
  and the review history is how the agent learns what this person wants kept.
- **Never deletes.** Deletion is the person's act.

## Inputs

Copy on any device. The share sheet. A screenshot. A photo. A voice note. A QR code scanned. A
position marked. A stop on the bike. Each one is a commit with its origin filled in by the device
that took it, not typed afterwards.

## As an Ebike Safari layer

A tenant in the sense of
[layers and games](https://github.com/SimHacker/WillWrightShowForFood/blob/main/apps/ebike-safari/design/layers-and-games.md):

- **Reads:** `STOP` events, photos and voice notes taken at stops, the snapped position.
- **Writes:** clippings keyed on place, under its own name.
- **Resurfaces by place.** Stop at the same drawbridge next month and the schedule photo you took
  there comes back, with the date you took it. Slow down past a shop you clipped and it waits for
  the next red light rather than interrupting the ride.
- **Publishes by pull request.** A clipping that is evidence about a place (a sign, a door, a
  menu board) can be offered to an information layer such as amsterdank as a claim with source,
  date and confidence. Nothing leaves without the rider.

The layer rules apply unchanged: the ride and the clippings are the rider's, and a layer receives
claims about places, never the trace of a person.

## Life in general

The same store with other contexts than place. The meeting brings back what you clipped about
the person. The document brings back the quotes you took from it and where each one sits in the
original. The project brings back the screenshots of the bug. Place is only the context Ebike
Safari happens to supply for free.

## Open

- **Forgetting.** Git keeps everything, and privacy sometimes needs a real purge: rewritten
  history, not a delete commit. The service needs both, with the purge recorded as having
  happened without recording what was purged.
- **Cost of reading.** Frontier model calls on every clipping add up. Read on demand and on
  resurfacing, cache the readings, and let dedicated readers handle the common cases.
- **The name.** The naming assignment in [README.md](README.md#why-there-is-no-cute-name-for-it-here)
  is still open, and a service on top of the thing does not close it.

Related: [BRANCHING-TIMELINES.md](BRANCHING-TIMELINES.md) for the repo underneath,
[`../interface-to-agency/ebike-safari.md`](../interface-to-agency/ebike-safari.md) for the ride as an
interface no agent can pedal.
