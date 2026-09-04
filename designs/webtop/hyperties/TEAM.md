# Shneiderman's lab, and who did what

HyperTIES ran for roughly a decade at the University of Maryland Human-Computer Interaction Lab
under Ben Shneiderman's direction. Don joined for the NeWS workstation era in the late 1980s — one
segment of a longer history that started before he arrived and continued after. Credit here is
apportioned as the papers and the participants apportion it.

## Timeline

| When | What |
|---|---|
| Fall 1983 | Development begins at HCIL as **TIES** — The Interactive Encyclopedia System — on IBM PCs |
| 1983 | Embedded menus first implemented by **Dan Ostroff** |
| 1984–85 | Work supported by a US Department of the Interior contract, in connection with the U.S. Holocaust Memorial Museum and Education Center |
| Jan & Apr 1986 | The two influential papers publish: *IJMMS* and *CACM*. Embedded menus applied and tested by **Larry Koved** |
| 1986 | Renamed **HyperTIES** after a cease-and-desist: "TIES" collided with an existing trademark. "By then 'hyper' was a growing term" |
| 1987 | Commercial licensing to **Cognetics Corporation**, Princeton Junction NJ. Roughly 20 empirical studies reported at Hypertext '87, UNC |
| July 1988 | **Hypertext on Hypertext** — the full text of eight *CACM* papers on disk. The world's first electronic journal. ACM sold 4000+ copies |
| 1988 | **Hypertext Hands-On!** (Shneiderman & Kearsley) — the world's first electronic book |
| Oct 1988 | Educom show floor: NeWS, pie menus, Emacs, HyperTIES. Jobs and Bill Joy both walk up |
| 1988–89 | The NeWS workstation version: PostScript rendering, FORTH markup, C formatter, Emacs authoring tool, pie menus |
| Spring 1989 | Pie menu demo recorded; stills appear in the May 1989 HCIL Open House handout |
| Spring 1989 | Berners-Lee's WWW proposal cites Hypertext on Hypertext as the source of the "hot spots" idea |
| 1988–91 | High-precision touchscreen research; lift-off strategy; toggle switches |
| 1991 | *Designing to Facilitate Browsing: A Look Back at the Hyperties Workstation Browser*, **Hypermedia** 3(2), 101–117. The definitive account |
| 1988–93 | Apple sponsors HCIL. Jobs visits in person, 1988 |
| Apr 2020 | Ben writes the origins email to Don and John Gilmore; Gilmore forwards it to the Internet History list |
| Aug 2021 | Elise Blanchard's "Why are hyperlinks blue?" at Mozilla; the HN threads |
| Jan 2022 | Don's Medium archive collects it all — [distilled here](HN-ARCHIVE.md) |

Commercially, Cognetics *"made a modestly successful commercial run with it, doing dozens of
corporate projects, most notably the Hewlett-Packard user manual for their Laserjet 4 was
distributed as a Hyperties disk."*

## The lab

**Ben Shneiderman** — director. The embedded menu, the empirical method, and the discipline of
claiming precisely what you can defend: he disclaims coining "hyperlink" and claims the visual
interface for highlighted selectable text embedded in paragraphs. Roughly 20 studies decided
HyperTIES's defaults — link color, history stack, an easy BACK button, article length, global string
search. He has been consistently generous about this work being written up, and this pack exists at
his encouragement.

**Dan Ostroff** — graduate student; first implementation of embedded menus, 1983. With Shneiderman,
*Selection devices for users of an electronic encyclopedia* (1988).

**Larry Koved** — applied and tested embedded menus; Koved & Shneiderman, *CACM* April 1986 — the
citable origin of the embedded menu idea.

**Catherine Plaisant** — co-author of the 1991 browser paper; touchscreen toggle switches with
D. Wallace (1990), the work later cited as prior art against Apple's Slide-to-Unlock patents; and
high-precision touchscreens with Sears and Shneiderman.

**Rodrigo Botafogo** — co-author of the 1991 browser paper; structural analysis of hypertext.

**William Weiland** — co-author of the 1991 browser paper; HyperTIES browser development, and
specifically the **index manager** in C — the component that mapped an article or object *name* to
its location in a file. That makes him the author of the mechanism the whole synonym/self-naming
design rests on ([ARTICLE-SCHEMA.md](ARTICLE-SCHEMA.md)). The archive preserves Don's email to
`weiland@bensun` asking for `.h` files "for the index manager so that I can include them in fmt.c" —
resolution was Bill's, formatting was Don's.

**Don Hopkins** — the NeWS workstation version: the PostScript user interface and target classes,
the FORTH markup-language interpreter and storyboard-to-FORTH-word compiler, the C formatter, and
the UniPress Emacs MockLisp authoring tool (YAHTITTIE). Pie menus throughout, in both the browser
and the authoring tool.

**Jack Callahan, Mark Weiser** — with Hopkins and Shneiderman, *An empirical comparison of pie vs.
linear menus*, CHI '88, 95–100. Weiser is the same Mark Weiser who went on to coin ubiquitous
computing at PARC.

**Andrew Sears** — high-precision touchscreens; *design strategies and comparisons with a mouse*
(1989/1991).

**Richard Potter, Linda Weldon** — with Shneiderman, *Improving the accuracy of touch screens*,
CHI '88 — the lift-off strategy paper.

**Greg Kearsley** — co-author of *Hypertext Hands-On!*, 1988.

Ewing, Mehrabanzad, and Sheck appear with Ostroff and Shneiderman on the January 1986 *IJMMS*
mouse-versus-arrow-jump-keys comparison.

## Outside the lab, load-bearing

**James Gosling** wrote two of the four languages HyperTIES was built in — NeWS PostScript and
UniPress Emacs MockLisp — before he wrote Java. *"It was no coincidence."*

**Mitch Bradley** wrote the Sun FORTH (Forthmacs) that could dynamically link and call C by running
the Unix linker to relocate a library into FORTH's memory, because SunOS had no shared libraries
yet. It became **OpenFirmware**. **Jonathan Payne**'s Jove editor was built into it.

**Tim Berners-Lee** told Ben directly that he was influenced by the design as he saw it in Hypertext
on Hypertext, and adopted the light blue.

**John Gilmore** asked the question in 2020 that produced Ben's email, then forwarded it to the
Internet History mailing list, where it became the primary citable source.

**Elise Blanchard** (Mozilla) wrote the 2021 article that restarted the whole conversation and
reached Ben for more material. She and Don disagree about whether cyan counts as blue; her narrower
point — no direct evidence about Mosaic — stands.

## What the lab was actually for

The through-line is not any one feature. It is that **every interaction decision was measured before
it became a default.** Link color was an experiment. Highlighting method was an experiment. Single
versus double click was an experiment. Touchscreen selection strategy was an experiment. Pie versus
linear menus was an experiment with a published comparison.

That is the standard this hub is held to, and it is currently failing it: nearly everything in these
design documents is argument and lineage, not measurement. Ben's own summary of what he does — *"my
desire to be innovative while also having an impact"* — is the same standard applied to shipping.

Where a claim here is untested, it should say so.

↑ [hyperties](README.md) · [HN archive](HN-ARCHIVE.md) · [webtop hub](../README.md)
