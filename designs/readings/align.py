#!/usr/bin/env python3
"""Recover timestamps for a cleaned transcript by aligning it to raw captions.

Cleaning a transcript throws the timestamps away: proper nouns get fixed, links
get added, chapter headings get written, and none of that survives in the ASR's
cue table. This puts the clock back.

It aligns the cleaned prose against the caption word stream with
difflib.SequenceMatcher and reports, for each `## ` heading, the caption
timestamp of the first word beneath it. Cleanup edits show up as gaps in the
alignment and are simply skipped, which is why an 80%-plus match rate still
yields exact chapter times.

Do not use keyword search for this. The first occurrence of a chapter's topic
word is usually not the chapter start — it is often much earlier, which produces
negative offsets and silent nonsense.

Usage:
    python3 align.py raw/VIDEOID.en-orig.srt cleaned-reading.md
    python3 align.py raw/VIDEOID.en-orig.srt cleaned-reading.md --yaml
"""

import argparse
import difflib
import pathlib
import re
import sys

from srt2text import dedupe, parse

WORD = re.compile(r"[^a-z0-9]")


def normalize(text):
    return [w for w in (WORD.sub("", t.lower()) for t in text.split()) if w]


def caption_words(srt_path):
    """[(word, start_seconds)] from a caption file, rolling window removed."""
    out = []
    for start, text, _silence in dedupe(parse(pathlib.Path(srt_path).read_text())):
        out.extend((w, start) for w in normalize(text))
    return out


def transcript_words(md_path):
    """([word], [(word_index, heading)]) from cleaned markdown.

    Starts at the first `## ` heading, so front matter and preamble prose do
    not pollute the alignment. Link syntax is reduced to its anchor text.
    """
    words, heads, started = [], [], False
    for line in pathlib.Path(md_path).read_text().splitlines():
        if line.startswith("## "):
            started = True
            heads.append((len(words), line[3:].strip()))
            continue
        if not started or line.startswith("#") or line.strip() == "---":
            continue
        clean = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)
        words.extend(normalize(re.sub(r"[*_`>]", "", clean)))
    return words, heads


def mmss(seconds):
    if seconds is None:
        return "?"
    return f"{int(seconds) // 60}:{int(seconds) % 60:02d}"


def align(srt_path, md_path):
    cap = caption_words(srt_path)
    words, heads = transcript_words(md_path)
    matcher = difflib.SequenceMatcher(None, words, [w for w, _ in cap],
                                      autojunk=False)
    blocks = [b for b in matcher.get_matching_blocks() if b.size]

    def timestamp(index):
        for b in blocks:
            if b.a <= index < b.a + b.size:
                return cap[b.b + (index - b.a)][1]
        following = [b for b in blocks if b.a > index]
        return cap[following[0].b][1] if following else None

    matched = sum(b.size for b in blocks)
    coverage = matched / len(words) if words else 0
    return [(timestamp(i), title) for i, title in heads], coverage, len(cap)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("srt")
    ap.add_argument("markdown")
    ap.add_argument("--yaml", action="store_true",
                    help="emit a chapters: block instead of a table")
    args = ap.parse_args()

    chapters, coverage, cap_count = align(args.srt, args.markdown)
    print(f"# aligned {coverage:.0%} of transcript against {cap_count} "
          f"caption words", file=sys.stderr)

    previous, monotonic = -1, 0
    for t, _title in chapters:
        if t is not None and t >= previous:
            monotonic += 1
            previous = t
    print(f"# monotonic {monotonic}/{len(chapters)} — anything less than all "
          f"of them means the alignment drifted", file=sys.stderr)

    if args.yaml:
        print("chapters:")
        for t, title in chapters:
            print(f'  - t: "{mmss(t)}"')
            print(f'    title: "{title}"')
    else:
        for t, title in chapters:
            print(f"{mmss(t):>7}  {title}")


if __name__ == "__main__":
    main()
