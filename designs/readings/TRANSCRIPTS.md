# Transcripts — capture, cleanup, and linking

Plumbing for [readings](README.md). Four videos, ~87 minutes, 12,364 words
of speech.

**The finished artifacts do not live here.** The convention already exists in
this repo and it is a good one: a reading is filed next to the thing being read,
in a `readings/` directory, as a pair —

```
designs/object-system/readings/
    2026-07-14-object-system-readme-reading.md    cleaned prose, linked, chaptered
    2026-07-14-object-system-readme-reading.yml   timestamps, chapter index,
                                                  ASR corrections ledger,
                                                  media-event injection points
```

The `.md` is the cream: no timestamps, because they distract a human reader.
The `.yml` is the machinery: the same chapters with times, every ASR
misrecognition recorded as `wrong → right`, and a media-event track for a
synchronized player that does not exist yet. That split is right and this
directory does not duplicate it.

**What lives here** is the method ([README.md](README.md)), the tools, and the
staging area: `transcripts/raw/` for captions as downloaded, `transcripts/flat/`
for machine-flattened text on its way to a cleanup pass.

## The corpus

| Video | Date | Length | Case | Reading |
|---|---|---|---|---|
| [MOOLM Designs: Object System README](https://www.youtube.com/watch?v=0uBO6ZAcVTE) | 2026-07-14 | 33:22 | **A** | [done](../object-system/readings/2026-07-14-object-system-readme-reading.md) — 32 chapters, timestamps verified |
| [David MacKay's Dasher, Palm On Being Palm, and Tog's "The Infinite Numer of Monkeys"](https://www.youtube.com/watch?v=lL2sw2oYU98) | 2026-07-02 | 33:21 | **mixed** | not started |
| [✋💜🌊 The Long Version: Marathon Session Reading, Turn 7: The Wish is Spoken](https://www.youtube.com/watch?v=T-OIeUSc5vI) | 2026-07-02 | 11:07 | **B** | not started |
| [✋💜🌊 Palm Love Wave](https://www.youtube.com/watch?v=4GS8Xx0ZTZI) | 2026-07-02 | 9:31 | **B** | not started |

Case A and Case B are defined in [README.md](README.md) and are not the same
practice. **A Case B header must name Palm as the author of the text being
read.** A listener could hear that a character was being performed; a transcript
strips exactly that cue, leaving Palm's sentences under Don's name.

Where the three Palm readings should be filed: next to Palm's material, not
here. `lL2sw2oYU98` already has a natural neighbour in
[`palm-nook/study/infinite-typewriters.md`](../../examples/adventure-4/pub/stage/palm-nook/study/infinite-typewriters.md),
which cites it.

The title typo — "Numer" — is Don's, on YouTube, and stays. `[sic]` if quoted.

## Pipeline

```
yt-dlp --skip-download --write-auto-subs --sub-langs "en-orig,en" \
       --convert-subs srt -o "%(id)s.%(ext)s" <url>...    → transcripts/raw/
python3 srt2text.py transcripts/raw/*.srt --outdir transcripts/flat
                                                           → transcripts/flat/
    human-supervised cleanup, per the rules below          → <subject>/readings/*.md
python3 align.py raw/<id>.en-orig.srt <cleaned>.md --yaml  → chapters for the .yml
```

Two traps, written down so they cost nothing next time:

- **`--print` implies `--simulate`**, so a yt-dlp command that prints metadata
  downloads no subtitles and reports success.
- **YouTube's rolling window repeats at line granularity**, not cue
  granularity: every cue carries the previous line plus one new one. Dedupe
  whole cues and you get a transcript with everything in twice — 24,649 words
  where there are 12,364.

YouTube's ASR turned out good enough that local Whisper was unnecessary: it
produces punctuation, capitalization, and bracketed non-speech events like
`[snorts]`. `mlx_whisper` is installed if a future reading needs better, and
would earn its time mainly on jargon density, with an `initial_prompt` seeded
from the corrections ledger of a previous reading.

`align.py` exists because cleanup destroys timestamps and a media-event track
needs them back. It aligns cleaned prose to the caption word stream and reports
its own coverage and monotonicity, so a bad alignment cannot pass quietly.

## Cleanup rules

These are [Article VI](../../skills/no-ai-parrot/CONSTITUTION.md) applied to a
transcript. The governing line:

> **The pass may repair the channel. It may not touch the composition.**

The test is counterfactual: *would this fix still be needed if he had typed the
sentence?* If yes, it is composition — leave it.

**Repair the channel:**

- Misrecognized proper nouns. The 2026-07-14 ledger is the reference set:
  `moom → MOOLLM`, `Gary Dresser → Gary Drescher`, `Owen Dinsmore → Owen
  Densmore`, `lambdaoo → LambdaMOO`, `clots → CLOS`, `kines → K-lines`,
  `greable → greppable`. Casing of technical names is transcription, not style:
  `News → NeWS`, `loops → LOOPS`, `risk → RISC`.
- Homophones, word-boundary errors, punctuation, paragraph and chapter breaks.
- Dropped words unambiguous from context, in `[ ]` if there is any doubt.
- An author's correction of himself counts as channel repair when it is
  recorded: the 2026-07-14 reading fixes "shadow DOM" to **virtual DOM** on the
  strength of Don's own video comment, and says so in the header.

**Leave the composition alone:**

- No rewriting a clumsy sentence, tightening, or making it flow.
- No removing a digression for being one. The digressions are the product.
- No fixing grammar that is just how he talks. "An multiple inheritance
  object-oriented programming system" is spoken English and it stays.
- No deleting `[snorts]`, false starts, or self-interruptions. That is the
  patina, and it is the part no machine produces.
- No introducing vocabulary he did not say. Absolute: a cleanup pass that
  leaves model idiom behind hands over the authorship accusation for free.

**Flag, do not guess.** Anything unclear gets `[?]` and the raw ASR text goes in
the corrections ledger. A confident wrong reconstruction is worse than a marked
gap — the same discipline the no-ai-parrot corpus uses for quotes.

## Linking rules

Inherited from the 2026-07-14 reading, which states them and follows them:
same-repo references are relative paths, because they survive forks, clones and
offline reading; cross-repo references are absolute GitHub URLs, because they
have to survive being pasted into email; people and systems link to their
canonical homes.

Link generously, but only to verified targets. A dead link in a document whose
whole purpose is checkability is worse than no link. Link the first substantive
mention in a section, not every occurrence.

## Status

- [x] Captions captured for all four videos
- [x] `srt2text.py` — flattening, rolling-window dedupe, sentence paragraphing
- [x] `align.py` — timestamp recovery for cleaned transcripts
- [x] `0uBO6ZAcVTE` reading complete; chapter timestamps verified 2026-09-07,
      `timing.status` flipped from `pre-trim` to `verified`
- [ ] Three Palm readings, filed next to Palm's material, with Case B headers
- [ ] Diff the Case A transcript against `designs/object-system/README.md`; the
      remainder is the measurable claim in [README.md](README.md)
