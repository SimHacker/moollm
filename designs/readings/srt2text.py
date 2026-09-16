#!/usr/bin/env python3
"""Flatten a YouTube auto-caption SRT into paragraphed plain text.

YouTube's ASR emits a rolling window: each cue repeats the tail of the previous
one so captions scroll smoothly. Concatenating cues naively triples the text.
This keeps first occurrences only, then breaks paragraphs on long pauses.

The output is *raw material for a human-supervised cleanup pass*, not a
finished transcript. It deliberately preserves disfluencies, false starts and
bracketed non-speech events such as [snorts]: those are patina, and the cleanup
protocol in TRANSCRIPTS.md forbids removing them.

Usage:
    python3 srt2text.py transcripts/raw/VIDEOID.en-orig.srt > out.txt
    python3 srt2text.py --gap 2.5 raw/*.srt --outdir transcripts/flat
"""

import argparse
import pathlib
import re
import sys

TAG = re.compile(r"<[^>]+>")
TIME = re.compile(
    r"(\d\d):(\d\d):(\d\d)[,.](\d\d\d)\s*-->\s*(\d\d):(\d\d):(\d\d)[,.](\d\d\d)"
)


def seconds(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def parse(srt_text):
    """Yield (start, end, line) per caption *line*, tags stripped.

    Line granularity matters. YouTube's scrolling captions carry the previous
    line plus one new line in every cue, so deduping whole cues leaves every
    line in twice.
    """
    for block in re.split(r"\n\s*\n", srt_text):
        lines = [l for l in block.strip().splitlines() if l.strip()]
        if not lines:
            continue
        if lines[0].strip().isdigit():
            lines = lines[1:]
        if not lines:
            continue
        m = TIME.match(lines[0])
        if not m:
            continue
        g = m.groups()
        start, end = seconds(*g[:4]), seconds(*g[4:])
        for raw in lines[1:]:
            text = re.sub(r"\s+", " ", TAG.sub("", raw)).strip()
            if text:
                yield start, end, text


def dedupe(lines):
    """Drop the rolling-window repetition, keeping first appearance."""
    out, prev_end, seen = [], 0.0, None
    for start, end, text in lines:
        if text == seen:
            prev_end = max(prev_end, end)
            continue
        out.append((start, text, start - prev_end))
        seen = text
        prev_end = end
    return out


SENT_END = re.compile(r"(?<=[.!?])\s+")


def paragraphs(items, gap, target):
    """Group into paragraphs.

    YouTube cues overlap, so pause detection is unreliable and only fires on
    genuine long silences. The primary mechanism is therefore sentence-aware
    grouping to a target word count: break only at a sentence boundary, once
    the paragraph is long enough. Purely mechanical — no sentence is altered,
    reordered, or dropped.
    """
    paras, cur, words = [], [], 0

    def flush():
        nonlocal cur, words
        if cur:
            paras.append(" ".join(cur).strip())
            cur, words = [], 0

    for _start, text, silence in items:
        if cur and gap and silence >= gap:
            flush()
        for sentence in SENT_END.split(text):
            sentence = sentence.strip()
            if not sentence:
                continue
            cur.append(sentence)
            words += len(sentence.split())
            if words >= target and re.search(r"[.!?][\"')\]]?$", sentence):
                flush()
    flush()
    return paras


def convert(path, gap, target):
    items = dedupe(parse(pathlib.Path(path).read_text(encoding="utf-8")))
    return "\n\n".join(paragraphs(items, gap, target))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("srt", nargs="+")
    ap.add_argument("--gap", type=float, default=2.0,
                    help="pause in seconds that starts a new paragraph")
    ap.add_argument("--words", type=int, default=110,
                    help="target paragraph length; breaks at next sentence end")
    ap.add_argument("--outdir", help="write <id>.txt here instead of stdout")
    args = ap.parse_args()

    for path in args.srt:
        text = convert(path, args.gap, args.words)
        if args.outdir:
            out = pathlib.Path(args.outdir)
            out.mkdir(parents=True, exist_ok=True)
            stem = pathlib.Path(path).name.split(".")[0]
            dest = out / f"{stem}.txt"
            dest.write_text(text + "\n", encoding="utf-8")
            words = len(text.split())
            print(f"{dest}  {words} words", file=sys.stderr)
        else:
            print(text)


if __name__ == "__main__":
    main()
