# The Prestoration, Blow by Blow

*Live commentary from the Semantic Soccer World Cup semifinal. The goal: record a memorial
for Vanessa Freudenberg by reading and discussing her paper — with her name on it. Every
command, every error message, every own-goal averted, as it happened. 2026-07-20, one
afternoon, one agent, one nudge.*

## First half — The Search

**KICKOFF.** Don asks: where is the better version by Vanessa Freudenberg? The agent opens
with a wide sweep — a single ripgrep across *twenty* workspace repos for
`Freudenberg|SqueakJS`. Eighteen come back empty; **moollm** and **WillWrightShowForFood**
light up with forty-plus files. The memorial infrastructure already exists. Good field
position.

**Minute 3.** `curl` pulls the Wayback snapshot of her PDF — 478,983 bytes in hand. First
shot on goal: `pdftotext` … **not installed.** Fallback `strings` prints nothing useful.
The crowd groans.

**Minute 5.** Second attempt, raw Python: scan the PDF bytes for `Vanessa|Bert|Freudenberg`.
Result: `Counter({b'Bert': 1, b'Freudenberg': 1})` — but wait, the context print shows
`(Accepted)-250(for)-250(DLS)`. **Red herring!** The match landed in an uncompressed
scrap; the real text is deflate-compressed. You can't grep what you haven't inflated.

**Minute 9.** The agent inflates every stream with `zlib` and searches again — and now the
truth appears in its native costume:

```
[(Bert)-250(Freudenber)18(g)]TJ
```

There it is, folks — the reason every naive search in history has failed on this file.
The name isn't stored as "Freudenberg". It's stored as **"Freudenber", a kerning
adjustment of 18 milli-ems, then "g"**. TeX split her name around a kern pair. To find a
name in a PDF you must think like a typesetter.

**Minute 15.** The away fixtures, rapid fire: **ACM Digital Library** — still Bert.
**dblp** — still Bert. **Semantic Scholar** — "B. Freudenberg". **DLS 2024 award page** —
*Vanessa Freudenberg*, credited correctly, linking to the uncorrected DOI. The scoreboard
of the entire scholarly record: right everywhere people write *about* the paper, wrong in
every copy *of* it.

**Minute 22.** Attempt to fetch her live site: thirty seconds of silence, `exit 1`, and a
`FileNotFoundError` for the download that never happened. **freudenbergs.de is down.**
The primary source is gone; only the Archive remains.

**Minute 25.** The killer stat, from the Wayback CDX API: every snapshot of the PDF from
July 2024 to January 2025 carries **the identical digest** —
`V5LDFWOYPJXKR3ZRYMFFR6H6C447M45C`. The file never changed. There was never a corrected
version at that URL. Fixity, ladies and gentlemen: the Archive can prove a negative.

**Minute 31.** Brief scuffle with the GitHub API — anonymous request bounced with a 401,
and the error JSON crashes the parser with a `TypeError` for good measure. Two errors in
one command! The agent switches to the `gh` CLI: `codefrau/SqueakJS` has no `docs/`
(404), no PDFs anywhere in the tree. squeak.js.org links only the JIT notes.

**HALFTIME VERDICT:** No corrected PDF exists on this Earth. The agent proposes the
institutional plays — ACM name-change petition, co-author re-typeset — correct, slow,
and useless for this week's screencast.

## Second half — The Surgery

**Minute 46.** From the touchline, the manager makes the call that changes the match:

> **Don:** How about downloading the old pdf file and ninja-editing it to have the
> correct name, then including that in the repo?

**Minute 47.** Equipment check: `qpdf`? No. `mutool`? No. `pikepdf`? `ModuleNotFoundError`.
Only Ghostscript stands ready. `pip install pikepdf` — three seconds, and the surgical
theater is open.

**Minute 50.** THE MOMENT OF THE MATCH. The agent inspects the embedded font subset
`PRMLRZ+NimbusRomNo9L-Regu` and reads its CharSet:
`/A/B/C … /V/W … /a … /v/w …` — **every glyph needed to spell "Vanessa" is already
embedded in her paper.** The font was carrying her name all along, waiting twelve years
for someone to use it.

**Minute 55.** But this is not find-and-replace country. The byline is a TJ array inside
a centered text matrix. The agent pulls the `/Widths` table and does the arithmetic in
milli-ems: "Bert Freudenberg" = 7,008 units; "Vanessa Freudenberg" = 8,507 units,
including a proper **V–a kern pair of −111** so the V tucks over the a the way
Nimbus Roman intends. Difference: 1,499 units at 10.9589pt → the name must shift
**8.214 points left** to stay optically centered over "Communications Design Group".
Yes, the commentators are discussing kerning. This is the World Cup of kerning.

**Minute 61.** Safety sweep of all ten pages for any other occurrence: page 1 byline,
page 4 footnote URL, page 4 link annotation. Three targets, no surprises. The edit goes
in — one `assert count == 1` per pattern, no regex where bytes will do. (The manager
yells "NOW YOU HAVE TWO PROBLEMS!" from the bench. The agent, sensibly, used exactly one
regular expression all afternoon, to find its own previous edit.)

**Minute 68.** Ghostscript renders page 1, PIL crops the header, and the vision check
comes back: **Vanessa Freudenberg**, centered, serif, beautiful. But the agent spots
something in the frame — the email below her name still reads `bert@cdglabs.org`.

**Minute 72. THE OWN-GOAL THAT WASN'T.** The agent computes replacement widths for
`vanessa@codefrau.net` in the email font F45 … and Python throws
`IndexError: list index out of range`. Diagnosis, and you will not believe this one:
the F45 subset (`ZKOOMY+SFSS0900`, Computer Modern Sans) declares `LastChar 117`.
The letter **v** is code point **118**. The font subset embedded in her own paper ends
*one glyph short of the letter v* — it physically cannot spell "vanessa". You couldn't
write a more on-the-nose metaphor if you tried.

**Minute 78.** First fix attempt sets the email in the Times subset — renders fine,
but it's the wrong family; the other authors' emails are sans. The agent swaps in
**base-14 Helvetica at 8.4pt** (guaranteed available, no embedding needed), recomputes
the centering from Helvetica's AFM widths (shift 10.9pt), and replaces its own previous
edit. Sometimes you have to bring your own Helvetica.

**Minute 84.** Verification battery: 220-dpi zoom of `vanessa@codefrau.net` next to
`dan@cdglabs.org` — visually consistent. Full-document `txtwrite` extraction — page 1
reads "Vanessa Freudenberg … vanessa@codefrau.net", page 4 reads
`github.com/codefrau/SqueakJS/`, and **zero occurrences of the old name remain** in
rendered text. All ten pages render clean through the null device. Both files hashed:
original `a5a91c1d…`, memorial edition `b54bc844…`.

**Minute 89.** The paperwork, which is the whole point: original preserved untouched in
the same directory, README enumerating every edit, provenance `/Note` embedded inside
the PDF itself, commit, push, and four HTTP 200s confirming the links are live for Alan
and Craig.

## Extra time — The Twist

**Minute 93.** Don mentions a memory: Vanessa once replied to him on HN with a link to a
corrected paper. One query to the Algolia API — `author_codefrau`, 12 comments, filter
for "pdf|paper" — and there it is, **November 5, 2021**:

> "Dan published an updated version of that paper here:
> smalltalkzoo.thechm.org/papers/EvolutionOfSmalltalk.pdf …
> **The main improvement for me is not being deadnamed.**"

**GOOOOAL.** Parent comment confirmed: Don's own post, linking Dan Ingalls's HOPL paper.
The remembered "better version" was Dan's paper, corrected by Dan, for her — a
prestoration from inside the family, years before the word existed.

**Minute 96.** One last red herring for the highlight reel: the naive zlib scan of the
Zoo PDF finds only "Bert" — custom font encodings again — but proper Ghostscript
extraction shows **thirteen mentions of Vanessa Freudenberg** in the prose … and her
old name still sitting in the reference list, because citations follow ACM's uncorrected
version of record. The gap the whole afternoon was about, visible in a single document.

**Minute 98.** Even the stadium got cleaned mid-match — `/tmp` swept the downloaded PDFs
between sessions, forcing a re-download (same bytes, same size, no harm). The Zoo paper
is filed in her sources directory with her comment quoted in the README.

**FULL TIME.** The screencast has its paper. The original has its fixity. Vanessa has
her name. And the match report recommends one transfer for next season: a petition to
ACM, so the version of record finally plays for the right side.
