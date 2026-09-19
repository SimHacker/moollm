---
name: quora-harvest
tier: skill
type: utility
protocol: QUORA-HARVEST
aliases: [quora, quora-scrape, expand-all-folds, recap-a-thread]
audience: ["operators", "archivists", "agents"]
author: Don Hopkins
license: MIT
allowed-tools: [Read, Write, Shell, Browser]
related: [design-sense, copy-that, sister-script, cursor-mirror]
tags: [archival, scraping, publishing, walled-garden, browser-automation]
credits: |
  natecull captured Alan Kay's Quora corpus through Nov 2023 and archived it at
  archive.org/details/alan-kay-quora-2023-11, which is the reason the pre-2023
  material does not need scraping at all.
---

# Quora Harvest

**Open every fold once, then never hike it again.**

Quora holds substantive writing — Alan Kay's answers, and the arguments people like
Ken Kahn bring back at him — behind folds that make reading a thread twice a manual
reconstruction job. This skill gets a thread out intact: answer, comments, nested
replies, permalinks, flat Markdown, one file, quotable and linkable.

It runs in your own logged-in browser. Nothing is stored, no credentials move, and
requests come from the browser you were already reading in.

## The three folds, and why expansion is a loop

| Fold | What it hides | Label you click |
|---|---|---|
| Answer truncation | the body of the answer | `(more)`, `Continue Reading` |
| Comment collapse | the comment list, unmounted until asked | `N comments`, `View more comments` |
| Reply collapse | replies under individual comments, recursively | `View N replies` |

They interact: opening the comment list mounts comments that are themselves
truncated, and expanding one of those reveals a reply thread that is also
collapsed. So expansion is not a pass, it is a **fixpoint** — click everything,
wait for React to settle, look again, stop when a round finds nothing new.

Two more things stay folded and this skill does not chase them. Sibling answers
(`1 of 6 answers`) live at their own URLs, so five more answers to the same
question means five more fetches. Upvoter and sharer lists are not content.

## Why label text and not selectors

Quora's class names are obfuscated and churn. The **visible label is the product**
and does not move: a fold has to say something a human will click. So the expansion
loop matches trimmed `textContent` against a list of label patterns, filtered to
elements that are short, visible, and clickable — accepting Quora's div-soup
affordances (pointer cursor, click wrapper, button role) as clickable, not just
real buttons.

When Quora invents a new fold, add one regex to `EXPANDERS` in
[`scripts/quora-extract.js`](scripts/quora-extract.js). That array is the only part
of the file that should ever need touching.

The **structured parse is deliberately second class**, and the skill says so out
loud rather than pretending otherwise. Comments are found structurally — the
smallest box containing both a profile link and a permalink to itself — which
survives class renames better than selectors do, but not forever. Every record
therefore also carries the **full expanded page text**, so a degraded parse still
leaves you everything you came for.

## Methods

### SNIPPET — the fast path when the tab is already open

Paste [`scripts/quora-extract.js`](scripts/quora-extract.js) into devtools →
Sources → Snippets, once. Snippets persist. From then on, run the snippet on any
Quora page and call:

```js
__quoraCopy()      // expand everything, put Markdown on the clipboard
```

Or, if you only want the hike done and intend to read it yourself:

```js
await __quoraExpand()   // {rounds, clicked} — nothing else touched
```

### HARVEST-PAGE — a list of URLs

Quit Chrome, relaunch it with remote debugging, and leave it logged in:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

Then:

```bash
pip install playwright && playwright install     # once, ever
python3 scripts/quora_harvest.py urls my-urls.txt --out ~/quora-harvest
```

One `.md` and one `.json` per answer, named from the question and author slugs.
Already-harvested URLs are skipped, so interrupting and rerunning resumes.

### HARVEST-PROFILE — everything someone wrote

```bash
python3 scripts/quora_harvest.py profile Alan-Kay-11 --out ~/quora-harvest --limit 100
```

Scrolls the profile's answers tab collecting URLs until it stops finding new ones,
writes `Alan-Kay-11-answer-urls.txt` as the index, then harvests each at three
seconds apart. For a 600-answer corpus, run it in batches with `--limit` and let
the resume behavior carry you.

### RECAP — harvest is not the artifact

Raw harvest is input. The artifact is a recap in the house pattern: source URL and
capture date at the top, provenance and portrayal note, verbatim quotes, one
section per commenter thread so an exchange reads end to end, related recaps
linked, and your own reading in a section clearly marked as yours.

Gold standard, twenty-one of them:
[the Alan Kay Quora shelf](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/alan-kay/media/quora-recaps).
The [AGI answer](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/alan-kay/media/quora-recaps/agi-paradigm-shifts-and-no-moores-law-for-software.md)
is the one that motivated this tool: expanded by hand, and the hand-expansion turned
up Kay's actual verdict on Kahn's papers and the sharpest objection in the thread,
both of which the folded view hid completely.

## Don't scrape what someone already saved

Check these first:

- **The 2023 corpus.** natecull downloaded Alan Kay's answers through Nov 2023 and
  archived them: [archive.org/details/alan-kay-quora-2023-11](https://archive.org/details/alan-kay-quora-2023-11).
  Machine-OCR'd and noisy, so verify quotes against the source, but it means only
  2024-onward and the comment trees actually need fetching.
- **The Wayback Machine**, for individual answers someone thought to save.

Automated access is against Quora's terms of service. What this tool does is read
pages you can already read, from the browser you are already reading them in, at
human pace, for your own archive — which is a judgment call you are making, not one
the script makes for you.

## The lens underneath

This skill exists because of a design failure, not a technical gap:
[view-state-is-the-users](../design-sense/lenses/view-state-is-the-users.md). The
view a reader assembles by hand is the reader's, and destroying it with one
accidental click, with no undo and no address, is data loss. When readers start
maintaining mirrors of your content in another medium, that is the bug report.

## Part of MOOLLM

Part of [MOOLLM](https://github.com/SimHacker/moollm) — see the
[skills index](https://github.com/SimHacker/moollm/tree/main/skills). Usable
standalone: the two files in `scripts/` have no MOOLLM dependencies.
