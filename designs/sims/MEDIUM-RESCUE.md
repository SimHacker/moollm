# Rescuing the Medium corpus, starting with the Wright lecture notes

**Goal.** Get Don's writing off Medium and into this system as markdown plus
YAML data: readable without an account, diffable, linkable, citable, and
archived with its own provenance. Medium has enshittified — paywalls on your own
work, hostile reading experience, no stable export path, and no way for a reader
to check a citation without being logged in.

**This document is the plan and the working record.** It starts with one
article because that article turned out to be the hard case, and the hard case
defines the process.

## The specimen: "Designing User Interfaces to Simulation Games"

https://donhopkins.medium.com/designing-user-interfaces-to-simulation-games-bd7a9d81e62d

Don's summary of Will Wright's talk to Terry Winograd's user interface class at
Stanford, 1996-04-26 — written before they worked together on The Sims. The
lecture video is now public via the Stanford archive, and there is a summarized
version of the lecture itself in
[`sims-will-wright-microworlds-1996.md`](sims-will-wright-microworlds-1996.md).

### It is not one article. It is at least three layers.

| Layer | When | What it is |
|---|---|---|
| **1996 notes** | 1996 | Written at or just after the lecture, before The Sims existed |
| **c. 2000 revision** | after The Sims shipped | Looking back at what was actually built versus what Wright previewed |
| **2023 revision** | Jan 2023 | Accompanying the release of the lecture video |

**Nothing in the current text marks which sentence belongs to which layer.**
That is the whole problem. A reader — or a citation, as in
[`../../skills/no-ai-parrot/corpus/CANON.md`](../../skills/no-ai-parrot/corpus/CANON.md)
— cannot tell whether a given observation was foresight in 1996 or hindsight in
2000 or framing in 2023, and those are very different claims.

The 2000 layer is the one most worth recovering, because it is the one with the
most at stake: **it is the post-mortem written by someone who had just spent
three years building the thing that the 1996 preview was a preview of.**

### What the 2000-era material was actually about

Recorded here from Don's account so the search knows what it is looking for. All
of it is the user-created-content agenda, which is the through-line from that
lecture to everything after:

- **User-created content tools**, as the point rather than as a feature
- **Edith** — the visual behavior editor for Sims objects. Don wanted it
  released. **Will wanted it released too and could not persuade EA.** It was
  soft-released to a university professor, who wrote his own documentation and
  gave both to his students; that package is findable
- **Educational versions of SimCity**
- **Transmogrifier** and similar easy-to-use content creation tools
- **Comic books generated from family albums**
- **Porting data between games** — which is exactly what Wright demonstrated in
  1996 by loading a SimCity file into Dollhouse, and exactly the "hobby model"
  he described in the Q&A
- **The SimCity source code**, which Don had in hand and wanted to release in
  some form

`verified: Don's account, 2026-09-07. needs-check on the professor's name and
the Edith documentation package before publishing any of it.`

## Archaeology: what has been established

Findings from the Wayback Machine, 2026-09-07.

**Two hashes circulate for this article; only one is real.** `bd7a9d81e62d` has
Wayback captures from 2022-02-10 onward. `6a4b7dd3d15b` has zero captures and
does not resolve — if it turns up in an old note or link, it is dead.

**The 2023 revision is measurable.** Capture sizes on the Medium URL, collapsed
by content digest:

| Capture | Bytes |
|---|---|
| 2022-02-10 | 31,576 |
| 2023-01-08 | 47,578 |
| 2023-01-30 | 97,977 |
| 2025-05-22 | 97,161 |

**The article roughly tripled in January 2023** and has been stable since. So
the 2023 layer is recoverable by diffing the 2022-02-10 capture against a
2023-02-01 one, and that diff is a good approximation of what the video release
added.

**The 1996 and 2000 layers are not on Medium at all.** There is no capture
before 2022-02-10, which is consistent with the article having been *moved* to
Medium late. Those layers live on the earlier hosts.

**The earlier host is `art.net`, and it is well preserved.**
`http://www.art.net/~hopkins/Don/` has captures from **1998** onward. Confirmed
present, all of it rescue-worthy in its own right:

| Subtree | Contents | Earliest capture |
|---|---|---|
| `simcity/` | `index`, `keynote`, `hyperlook-demo`, `simcity-announcement` | 1998-12 |
| `simcity/manual/` | `intro`, `tutorial`, `reference`, `refcard`, `inside`, `history`, `credits`, `bibliography` | 1999-01 |
| `hyperlook/` | `SimCity.tar.Z`, `HyperLook-runtime.tar.Z`, READMEs, product/tech info PostScript | 1998 |
| `piemenus/` | Dr. Dobb's article, `piewm.tar.Z`, `pie2lang.zip`, ActiveX source | 1998 |
| `psiber/` | The PSIBER Space Deck paper, chapter by chapter, plus PostScript | 1998 |
| `lang/scriptx/` | The full ScriptX `dreamdoc` class reference, Dr. Dobb's 11/94 pieces | 1998 |
| `lem/`, `art/` | Lem translations; cellular-automata artwork with MPEGs | 1998 |

**Negative result worth recording: there is no Wright or microworlds page on
`art.net`.** Searching the whole `~hopkins` tree for `wright`, `winograd`,
`microworld`, `dollhouse`, `edith`, `maxis` and `stanford` returns nothing. So
the 1996 and 2000 layers are not on art.net either, and the most likely home for
them is Don's own archives. A `donhopkins.com` CDX query timed out with a 504
and needs a narrower retry before that conclusion is firm.

**The lecture video is `nsxoZXaYJSk`** on Don's channel, title
"Will Wright  - Maxis -  Interfacing to Microworlds  - 1996-4-26", confirmed via
oembed.

### The 2000-era material is on `donhopkins.com` and it is dated

`donhopkins.com` is **live and serving** — these return HTTP 200 right now, no
archive needed:

| File | What it is | Date |
|---|---|---|
| [`/home/archive/TheSims/edith-notes.txt`](https://donhopkins.com/home/archive/TheSims/edith-notes.txt) | Don explaining Edith to the SimWatch list | 2000-08-26 |
| [`/home/archive/TheSims/comics.txt`](https://donhopkins.com/home/archive/TheSims/comics.txt) | "Making comic books from The Sims photo albums", cc'd to Scott McCloud and Will Wright | 2000-08-20 |
| [`/home/archive/maxscript/maxis-maxscript.ms`](https://donhopkins.com/home/archive/maxscript/maxis-maxscript.ms) | Maxis MaxScript source | — |
| [`/home/micropolis/dux-maxis-contract.txt`](https://donhopkins.com/home/micropolis/dux-maxis-contract.txt) | The DUX/Maxis contract | — |

**These are contemporaneous, dated primary sources from exactly the window the
2000 layer covers**, which makes them better evidence than any reconstruction
from a later revision. Both are emails to `SimWatch@egroups.com` in August 2000,
seven months after The Sims shipped.

Both files also have Wayback captures from **2021-04-20**, so they survive the
live site.

`verified: fetched from the live site 2026-09-07, HTTP 200; archived copies
confirmed at web.archive.org/web/20210420210002 and /20210420205931`

### What the two files actually establish

More than expected, and several of these are facts the repository wants
elsewhere.

**Edith** — `edith-notes.txt`, 2000-08-26:

> "'Edith' is a version of The Sims that's compiled with a whole bunch of
> special purpose editing tools built in. The name came from 'Edith Bunker', the
> first mother Sim, and it also means 'EDIT House'. (We would have called it
> 'Archie' for 'ARCHItecture Editor', but he's such a loud mouth close minded
> bigot, it didn't seem right.)"

- Edith edits **SimAntics**, "the visual programming language for scripting the
  behavior of The Sims." Now carried in
  [`../VISUAL-PROGRAMMING-LINEAGE.md`](../VISUAL-PROGRAMMING-LINEAGE.md),
  together with the SimCopter ancestry and Edith's live-editing property.
- **The language predates The Sims**: "The SymAntics [sic] language was used to
  program the people in SimCopter, and Edith evolved out of that." **Read that
  as descent, not naming** — in 1996 the tool was not yet called Edith and
  probably not yet called SimAntics either; the working name was *Tree
  Programming*. Chronology, corroboration and the open questions for Jacques
  Servin and Will Wright are in
  [`../VISUAL-PROGRAMMING-LINEAGE.md`](../VISUAL-PROGRAMMING-LINEAGE.md).
- On the Magic Cookie parenthetical in this email, see
  [What the Magic Cookie actually is](#what-the-magic-cookie-actually-is-from-the-source)
  below — the source contradicts the "256" figure.

`note: the 2000 email spells it "SymAntics" — an early variant of the
semantics pun. The established spelling is **SimAntics**, which is what the
rest of this repository uses and what anyone searching will use. Quote the
email verbatim with [sic]; write SimAntics everywhere else.`
- Edith controls behavior, not appearance. It was folded into the game rather
  than left standalone, and the consequence is the interesting part: "she is
  actually able to debug and edit code and data **while it's running live in the
  game**."
- Release was blocked on documentation — which Don was writing — and on a Maxis
  decision.

**Transmogrifier** — Edith's complement rather than a version of it. Written
*after* the game shipped, it changes surface appearance and not behavior. The
note describes a pending 2.0 release fixing a Magic Cookie bug, adding XML
import/export of object definitions, and handling 24-bit images and mismatched
palettes. Don also hoped to ship easy versions of the high-end body and
animation tools against gMax.

### What the Magic Cookie actually is, from the source

The email's parenthetical — *"the previous release 1.0 only lets you create 256
objects per cookie"* — **is not what the code does**, and the GUID layout is
worth recording correctly because it is the identity scheme for every
user-created Sims object.

`MakeUniqueGUID()` in `SimsKit/Transmogrifier/TransmogrifierDlg.cpp` scrambles a
timer, the clock and sixteen rounds of `rand()`, and then does this:

```c
// Mask out the middle 16 bits, and insert the object creator id.
newGuid &= 0xff0000ff;
newGuid |= (cookie & 0xffff) << 8;
```

So a 32-bit GUID is laid out **cookie in the middle, entropy on both ends**:

| Bits | Width | Contents |
|---|---|---|
| 31–24 | 8 | random |
| 23–8 | **16** | **Magic Cookie** — the object creator's id |
| 7–0 | 8 | random |

**The cookie is 16 bits and the per-object space is 16 bits** — 65 536 objects
per cookie, not 256. The per-object bits are *split around* the cookie rather
than sitting under it, which is why the comment says "mask out the middle."

`verified: read from source. All three trees present — Transmogrifier,
"Transmogrifier old" and "Copy of Transmogrifier" — contain byte-identical GUID
arithmetic, and no 256-element cap on objects or GUIDs exists in any of them.`

**What 2.0 did change**, by diff of `MakeUniqueGUID()` and `IsGUIDAlreadyUsed()`:

1. **Session-level GUID tracking.** 2.0 adds a `gUsedGUIDs` set and calls
   `UseGUID()` on every mint. 1.0 checked collisions only against objects in
   *already-loaded* res file models, so GUIDs minted earlier in the same session
   were invisible and **a batch of new objects could collide with each other.**
2. **A random cookie fallback.** `gMagicCookie` defaults to 0; 2.0 substitutes
   `rand() & 0xffff` when it is unset, instead of emitting every GUID with a
   zeroed creator field.

That first one is a real Magic Cookie collision bug, and it is the plausible
referent of the email's "fixes a bug with Magic Cookies." **The "256" is the
part no surviving source supports**, so it is recorded here as the email's claim
rather than as fact.

`todo: if the 256 figure matters, the 1.0 shipping binary is the only remaining
witness — SimsKit/Transmogrifier/Installer/ has TransmogrifierSetup.exe
alongside Transmogrifier_2.0_Setup.exe.`

**Use these names.** The 2000 email says "SimTransmogrifier" because that was
the name and the domain then; **do not carry that spelling into new prose.**

| Register | Name |
|---|---|
| Full, and the live home | **The Sims Transmogrifier** — <https://thesimstransmogrifier.com/> |
| Normal prose | **Transmogrifier** |
| Familiar | **TMog** |
| Code, CLI, module | `tmog` |

`verified: current name and canonical URL per Don, 2026-09-07. "SimTransmogrifier"
is historical and appears only inside the verbatim 2000 quote.`

**Comics** — `comics.txt`, 2000-08-20. A standalone utility to build comic books
from Sims photo albums, with speech balloons, thought bubbles and captions
overlaid so players could "put words into the Sims' mouths." It was at research
and design stage, and Don was soliciting requirements from players who had tried
to tell stories with the existing scrapbook and found it frustrating.

And one design-lineage fact worth lifting out, because it is first-hand:

> "Scott McCloud's wonderful comic book about comics 'Understanding Comics' was
> quite influential on the design of The Sims. There are some well used
> dog-eared copies of it sitting around the office at Maxis."

McCloud is already on the masters shelf in
[`../../skills/design-sense/`](../../skills/design-sense/); this is a direct
receipt for the connection, cc'd to McCloud himself.

So the layer archaeology has a shortcut: **rather than diffing captures to
guess what the 2000 revision said, start from the dated 2000 emails and work
outward.** They establish what Don was arguing at the time, in his own words,
with timestamps and a mailing list as witness.

Also present and unexpected: `donhopkins.com` carries a **2004 blog** under both
`/2004/MM/DD.html` and `/blog/2004/MM/DD.html`, and a `/home/etui/` area with a
`Simulation_Taxonomy` graphic and a `microworlds_screen.gif`. Neither is the
Wright article, but both are rescue targets and the `etui` directory is worth a
look for lecture-related images.

## TODO

Ordered by what unblocks what.

- [x] **Index `art.net/~hopkins/Don/`** — done; the subtree table is above. No
      Wright, microworlds, Dollhouse, Edith, Maxis, Winograd or Stanford page
      exists anywhere in that tree. Filter out the ARPANET image maps or they
      swamp every query.
- [x] **Retry the `donhopkins.com` CDX query** — done. Use
      `matchType=domain` rather than a `donhopkins.com*` glob, which 504s.
      Yielded the dated 2000 emails above.
- [ ] **Search Don's own archives** — email and disk — which are authoritative
      and beat the Wayback Machine wherever they overlap. The EDUCOM case in
      [`../../skills/no-ai-parrot/examples/educom-jobs.md`](../../skills/no-ai-parrot/examples/educom-jobs.md)
      is the precedent: his 1988 emails settled questions no public source could.
- [ ] **Diff 2022-02-10 against 2023-02-01** to isolate the 2023 layer.
- [ ] **Produce the local copy**: `wright-microworlds-notes.md` plus a sidecar
      `.yml`, following the convention already used for readings — prose in the
      `.md`, machinery in the `.yml`. The sidecar carries per-section layer
      attribution, so a citation can name a year and be checked.
- [ ] **Annotate the layers in the prose** only where a dated capture supports
      it. Where it does not, say so rather than guessing. Unmarked is honest;
      wrongly marked is worse than unmarked.
- [ ] **Chase Edith further.** `edith-notes.txt` is recovered and dated
      2000-08-26, which settles what Edith was and where the name came from.
      Still missing: the soft-released package, and the documentation the
      professor wrote for his students.

## The general process, once this one is done

The specimen defines the pipeline for the rest of the Medium corpus:

1. **Enumerate** the articles and their canonical URLs.
2. **Capture** every distinct Wayback digest per article, not just the latest —
   because revision history *is* content, and Medium does not expose it.
3. **Convert** to markdown, and split machinery into a sidecar `.yml`:
   timestamps, layer attributions, link status, image inventory.
4. **Repair links** against the Internet Archive rather than dropping them.
   Article IX of the constitution treats this as part of the work.
5. **Keep the wear.** Do not silently modernize prose, fix old opinions, or
   smooth over things that turned out wrong. Where a layer contradicts a later
   one, that contradiction is the most interesting thing on the page — see the
   two accounts of the Jobs demo in `educom-jobs.md`, which disagree and are
   both kept.
6. **Leave a forwarding address**, and leave the Medium version up. The point is
   to stop depending on it, not to erase it.

## One note on the irony

Checking whether either candidate URL resolved was impossible from the command
line: **Medium returns HTTP 403 to a plain request for Don's own article.** The
question "does this citation resolve?" could only be answered by asking the
Internet Archive.

A platform that will not let you verify your own citations is not a publishing
platform. It is a rental. That is the argument for this whole exercise, and it
arrived unprompted while doing the first step of it.
