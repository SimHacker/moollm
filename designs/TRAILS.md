# Trails — attention as a sendable document

Three names for one object. The object is **someone's attention**: precious, shareable,
directly manipulable, versionable, replyable, playable back as history.

| Name | Who | Year | What they said |
|------|-----|------|----------------|
| **skip trail** | Vannevar Bush, *As We May Think* | 1945 | a parallel over a long account that "stops only on the salient items" |
| **attention mask** | here | — | weights over a path: show, skip, emphasis |
| **P-pyramid** | Marvin Minsky, K-Lines memo | 1979 | "an illusion of an agent's perspective" over a graph that is not a pyramid |

Spelling: **P-pyramid**. Minsky's. Not "pi", not "psi". The P is the agent whose look-down
projects the hierarchy. Full treatment: [P-PYRAMID.md](P-PYRAMID.md).

The quotes and the sendable-unit argument live in
[PAIRED-LINKS.md](PAIRED-LINKS.md#what-you-send-is-a-path-and-a-mask). This page is the
identity: those three names are the same artifact, and git is the store it already wants.

## Ted, BayCHI, mind maps

10 August 2021, "HCI Constructs Then and Now", hosted by Ted Selker.
https://www.youtube.com/watch?v=dOLXLk8TbxQ

Near the end, in Q&A, **Nicole Lazzaro** asked what he thought of mind mapping software
(thebrain.com). Auto-captions, punctuation added, no words added:

> I've looked at it and fiddled with it and didn't find any use for it. Hypertext I see is the
> extension of literature, especially parallel hypertext side by side. But mind mapping doesn't
> create -- okay, a document is a package of information with a point of view, and it has to be
> portable, and that has to be extendable to somebody else. And mind maps don't seem to fill a bill.

That is Ted, on the record, answering a question. Not a paraphrase of Don. Digest:
[`WillWrightShowForFood/.../2021-08-10-baychi-hci-constructs-transcript-digest.md`](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ted-nelson/sources/2021-08-10-baychi-hci-constructs-transcript-digest.md)
· puppet/MCC notes:
[`DonHopkins/.../2021-08-10-baychi-ted-nelson-qa.md`](https://github.com/SimHacker/DonHopkins/blob/main/characters/aaron-marcus/sources/2021-08-10-baychi-ted-nelson-qa.md)

His criterion, same talk, answering Aaron Marcus: a document is **sendable**, it **expresses
a point of view**, and **a person has to make it**. A mind map is a tangle. A trail is a
document. The structure stays; the trail is what you send.

## Bush, 1945 — credit the whole machine

https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/

He already had every part, under his own names:

- **The path**, built by hand, annotated, durable: "building a trail of many items… his
  trails do not fade."
- **The mask**, named **skip trail**: the historian "parallels [a vast chronological
  account] with a skip trail which stops only on the salient items."
- **Sending**: photograph the trail, pass it to a friend, insert it in their memex, link
  it into a more general trail.
- **The job**: "a new profession of trail blazers."
- **The inheritance**: not the master's conclusions, "the entire scaffolding by which
  they were erected."

A skip trail is not a shorter copy of the chronology. It is a second object, parallel to
the rank, that records what was salient. That is an attention mask. That is a P-pyramid
anchored at the historian.

## What the object can do

Because it is a document, not a session:

- **Share** — send the trail, not the library.
- **Manipulate** — edit steps, change the mask, rename the zinger. Directly, as text.
- **Version** — every cut is a commit. Blame, diff, revert.
- **Reply** — a pull request on a trail is an argument about the cut.
- **Play back** — full history is a demo, a tutorial, a reinterpretation. Same cells,
  different mask, different throughline.
- **Layer** — new information arrives as another commit on the trail, not a rewrite of
  the territory. Correct knowledge iteratively, over years.

That is what a git repo *does*. Linus built it for kernel source. The same machine holds
attention: small text, named, forked, reviewed, replayed. The forge is where trail
blazing happens in public.

A guided tour, a code review, a lecture, a bug walkthrough, a Memex loan, a context
window handed to an agent — same file type.

## eBike safari: trail, not ride

[`skills/urban-safari/`](../skills/urban-safari/) currently says **ride** because the
device files do: a FIT file is a ride, Flow syncs rides, the CLI takes `--trips-dir ./rides`.

The thing you *send* is not the FIT. The FIT is the chronology (Bush's vast account). The
GPS track plus video keyframes plus clustered transcript is a **skip trail** over that
account — salient items only, parallel, shareable. A friend does not inherit your wattage.
They inherit the scaffolding: where you looked, what you said over which corner, which
laps you kept.

Proposal, not a mass rename: keep `ride` for the device/FIT noun. Use **trail** for the
authored, masked, sendable overlay — the map JSON, the video path, the transcript
clusters. A session can contain several trails over one ride (out-and-back, the climb
only, the talk track). FOCUS-FLOW already treats a session as a tree of passes; those
passes are trails.

## Related

- [PAIRED-LINKS.md](PAIRED-LINKS.md) — Ted's three criteria, Bush quotes, path+mask YAML
- [P-PYRAMID.md](P-PYRAMID.md) — Minsky's name, level-band, K-line as stored mask
- [FOCUS-FLOW.md](webtop/hyperties/FOCUS-FLOW.md) — sequence on a page and on a map
- [INTERFACE-TO-AGENCY.md](INTERFACE-TO-AGENCY.md) — the same artifact, handed to an agent
- [editing-history/](editing-history/README.md) — history as the document
- [indexes/XANADU.md](../indexes/XANADU.md) — the substrate argument
