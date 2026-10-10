---
name: mail-digest
tier: skill
type: utility
protocol: MAIL-DIGEST
aliases: [mail-dedup, digest-correspondence, boil-down-email, harvest-email]
audience: ["operators", "archivists", "agents"]
author: Don Hopkins
license: MIT
allowed-tools: [Read, Write, Shell]
related: [quora-harvest, cursor-mirror, copy-that, representation-ethics]
tags: [archival, email, correspondence, deduplication, privacy, harvesting]
credits: "Don Hopkins. Written while digesting the 2026 PIXIE correspondence with Heinz Lemke."
---

# Mail Digest

**Read each message once.**

A thread exported from a mail client repeats itself. Every reply quotes the thread
under it, every forward carries it again, and a long correspondence with a dozen
people is mostly copies. The PIXIE correspondence with Heinz Lemke, August to
October 2026, was 1.5 MB as exported; the new text in it was 213 KB, in 116
messages. Reading the pile reads most messages five or ten times, and so does a
model, at five or ten times the tokens.

This skill boils a pile down to each message's own words, then digests it in two
passes: a private archive of what matters, then a public harvest from that.

## DEDUP: the script

[`scripts/mail_dedup.py`](scripts/mail_dedup.py), no dependencies:

```
mail_dedup.py heinz-recent.txt --split "Don Hopkins"
116 messages, 207,595 characters (from 1,552,928 bytes) -> heinz-recent.dedup.txt
  mine: 57 messages -> heinz-recent.dedup.mine.txt
  others: 59 messages -> heinz-recent.dedup.others.txt
```

It splits the pile before every header block (`From:` followed by
Subject/Date/To/Cc/Sent, which matches mbox, Apple Mail, Gmail and Outlook
forwards), cuts each body at the first sign of quoting (`>` lines, `On ... wrote:`,
`Am ... schrieb`, `-----Original Message-----`, `Begin forwarded message:`, a
`From:` inside the body), and keeps the first copy of each (sender, opening text)
pair. Everything cut is somebody else's message, which is in the pile on its own.
The docstring is the manual.

`--split` separates your own messages from everyone else's, because they read
differently. Other people's messages are the new facts. Yours are mostly context you
already have, and the private parts of it are about you.

## DIGEST: two passes

**Pass 1, private.** Read the deduplicated text, others' first, and write a private
digest: facts with dates, decisions, offers, requests, open questions, and
everything personal, financial or not yet agreed to. It goes somewhere private (a
private repo, never a public one), deduplicated across messages, organized by
person and topic, with each fact dated. The raw export stays out of git entirely.

**Pass 2, public.** Harvest from the private digest, not from the mail, so the
privacy decision is made once and is visible. What goes public: facts that are on
the record or that the person would want stated, in their own published words
where possible, credited. What doesn't: money, health, contracts, personal
remarks, opinions about people, anything a correspondent hasn't agreed to make
public. When unsure, leave it private and ask.

For a large pile, read the others' file directly and hand your own to a subagent
with the same headings; they run in parallel.

## Privacy rules

- The raw export lives in an ignored directory (`temp/`) of a private repo, or
  outside any repo. It is never committed anywhere.
- Quote people only from messages they sent to you, and only publicly with
  consent or when it is the kind of thing they say in public anyway.
- Follow [representation-ethics](../representation-ethics/) for anyone portrayed:
  a real person's character file says what they said, never what they might have.
- A correspondent's correction of the record ("we never shipped it") goes public
  as a correction. Their reasons for declining something do not.

## Related

[quora-harvest](../quora-harvest/) gets walled-garden threads out flat;
[cursor-mirror](../cursor-mirror/) does the same for your own agent transcripts.
This one is for mail. Harvested text that leaves for another venue goes through
[copy-that](../copy-that/).
