#!/usr/bin/env python3
"""mail_dedup.py: boil a pile of email threads down to each message's own new words.

A mailbox export, a thread pasted from a mail client, or a forwarded chain repeats
every message many times: each reply quotes the whole thread under it, each forward
carries it again. Of 1.5 MB of PIXIE correspondence, 213 KB was new text in 116
messages. This script finds the messages, cuts each one off where its quoting
starts, and keeps one copy of each.

    mail_dedup.py INPUT [-o OUT] [--split NAME]

INPUT is plain text: a pasted thread, a .txt or .eml export, several .mbox files
concatenated. OUT (default: INPUT.dedup.txt) gets one block per message:

    === <date> | <from> | <subject>
    <the message's own text>

--split NAME also writes OUT.mine.txt and OUT.others.txt, messages from NAME and
from everyone else, because they read differently: someone else's message is new
facts, your own is mostly context you already have.

How it works:
  1. Split before every header block: a "From:" line followed by Subject/Date/To/
     Cc/Sent. That catches mbox, Apple Mail, Gmail and Outlook forwards alike.
  2. Take From, Subject and Date from the headers. The body starts after the first
     blank line.
  3. Cut the body at the first sign of quoting: a line starting with ">", an
     "On ... wrote:" or "Am ... schrieb" attribution, an Outlook
     "-----Original Message-----" or "-----Ursprüngliche Nachricht-----" rule, a
     "Begin forwarded message:", or a "From:"/"Von:" line inside the body. Whatever
     follows is somebody else's message, and it is in the pile on its own.
  4. Key each message by (first 30 characters of the sender, first 200 of the text),
     and keep only the first copy. Forwards of the same message with different
     wrapping still match, because the key is the opening, not the whole.

What it does not do: decode MIME, strip signatures, or sort by date (Date formats
vary too much to trust; sort the output if you need to). It never drops a message
because it is short, so check the output for empty-looking blocks. Run it on a copy;
it only reads INPUT.
"""
import argparse
import re
from pathlib import Path

HEADER_SPLIT = re.compile(r"\n(?=From: .+\n(?:Subject|Date|To|Reply-To|Cc|Sent): )")
QUOTE_START = [
    re.compile(r"^On .* wrote:$"),
    re.compile(r"^Am .* schrieb"),
    re.compile(r"^-----\s*(Original Message|Ursprüngliche Nachricht)"),
    re.compile(r"^Begin forwarded message:$"),
    re.compile(r"^(From|Von): "),
]


def header(block, name):
    m = re.search(rf"^{name}: (.*)$", block, re.M)
    return m.group(1).strip() if m else ""


def own_text(block):
    body = block.split("\n\n", 1)[1] if "\n\n" in block else block
    kept = []
    for line in body.splitlines():
        if line.startswith(">"):
            continue
        if any(p.match(line.strip()) for p in QUOTE_START):
            break
        kept.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip()


def dedup(text):
    seen = set()
    for block in HEADER_SPLIT.split(text):
        sender, subject, date = header(block, "From"), header(block, "Subject"), header(block, "Date")
        body = own_text(block)
        key = (sender[:30], body[:200])
        if not body or key in seen:
            continue
        seen.add(key)
        yield sender, subject, date, body


def fmt(msg):
    sender, subject, date, body = msg
    return f"=== {date} | {sender} | {subject}\n{body}\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("input")
    ap.add_argument("-o", "--out")
    ap.add_argument("--split", metavar="NAME", help="also write .mine/.others, by sender containing NAME")
    a = ap.parse_args()
    src = Path(a.input)
    out = Path(a.out) if a.out else src.with_suffix(".dedup.txt")
    msgs = list(dedup(src.read_text(encoding="utf-8", errors="ignore")))
    out.write_text("\n".join(map(fmt, msgs)))
    total = sum(len(fmt(m)) for m in msgs)
    print(f"{len(msgs)} messages, {total:,} characters (from {src.stat().st_size:,} bytes) -> {out}")
    if a.split:
        mine = [m for m in msgs if a.split.lower() in m[0].lower()]
        others = [m for m in msgs if a.split.lower() not in m[0].lower()]
        for suffix, part in (("mine", mine), ("others", others)):
            p = out.with_suffix(f".{suffix}.txt")
            p.write_text("\n".join(map(fmt, part)))
            print(f"  {suffix}: {len(part)} messages -> {p}")


if __name__ == "__main__":
    main()
