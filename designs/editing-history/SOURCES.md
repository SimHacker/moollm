# Quote ledger

Every quote used in this directory, checked against its primary source. Where a source is a
machine transcript of speech, that is stated, because it changes how the words may be quoted.

## Verification policy

1. **Written sources are quoted verbatim.** Nelson's own prose, Vim's documentation, published
   papers.
2. **Text transcripts of talks are quoted verbatim with their typos**, flagged once as
   transcripts. Fixing a transcriber's homophone silently would be inventing a quote.
3. **Mangled proper names get a bracketed correction**, because a reader cannot be expected to
   decode "Larry Testly".
4. **ASR captions are the weakest tier.** Where two independent transcriptions of the same audio
   disagree on a word, that word is elided with `[...]` rather than guessed. Structure and
   load-bearing clauses survive; the uncertain token does not get promoted to a quote.
5. **Non-adjacent sentences are joined with `[...]`**, never silently concatenated.

## Ted Nelson, written

### "Ted's ComParadigm in OneLiners" (1999)

https://xanadu.com.au/ted/TN/WRITINGS/TCOMPARADIGM/tedCompOneLiners.html

Nelson's own prose. Page carries `copyright 1999 Ted Nelson. Please quote on the Web`.
**Canonical for the clipboard indictment** -- use this one when a clean written source will do.

> Consider the "clipboard" on the Mac, PC or XWindows. It's just like a regular clipboard, except
> (a) you can't see it, (b) it holds only one object, (c) whatever you put there destroys the
> previous contents. Aside from that, IT'S JUST LIKE A REGULAR CLIPBOARD IN EVERY OTHER RESPECT--
> EXCEPT THERE AREN'T ANY OTHER RESPECTS!

> This is called a "metaphor". I see this pseudo-clipboard as stupidity at its height: a really
> terrible, destructive mechanism, excused by a word that makes it sound somehow okay. It is a
> further offense-- the greatest atrocity in the computer field, I believe-- that the crippled and
> destructive functions of this pseudo-clipboard have been falsely given the names "cut" and
> "paste"-- which for decades have meant something ENTIRELY different to writers, the function of
> parallel rearrangement with all things visible.

> Metaphors are scraps of resemblance that tie us down.

The caps are Nelson's. The `*` footnote marker after `"metaphor"` in the original is dropped.

### Internet Archive, "Cut and Paste, 2014"

https://archive.org/details/cutnpaste_201909

Item description, written by Nelson, uploaded by `TedNelson` on 2019-09-16. **Authoritative for
the 1984 date and for "Cram and Vomit" in print.**

> This shows the actual cut and paste process, done physically, that has been denied to us by
> software since those two words were redefined in 1984 to mean "hide" (on the invisible hideyhole
> called misleadingly the "clipboard") and "plug" (whatever's in the invisible hideyhole) to
> wherever you're pointing. Or since the letters used on both Mac and Windows are C and V, they
> could better have stood for Cram and Vomit.

Line breaks in the original description are collapsed here.

## Ted Nelson, text transcripts of talks

### MIT hypertext forum, clipboard segment (c. 1995)

https://web.mit.edu/m-i-t/forums/hypertext/paradigms/clipboard.htm

Transcript of a video segment. Undated on the page; datable to about 1995 from internal evidence
-- he says he has been trying to build the tool "for 35 years" and refers to his 1965 ACM paper as
"30 years ago", and mentions the Sapporo HyperLab.

> I am deeply angry at whatever technoid that changed the meanings of the words cut and paste from
> their true meaning of the parallel consideration of rearranged text on a table top to the hide
> and plug functions that we associate with the so called Macintosh clipboard. A clipboard which is
> just like any other clipboard, except you can't see it, anything you put on it destroys what was
> there previously, and if the phone rings, you lose the contents. It is like a real clipboard in
> every way, except that there are no aspects in which it is.

> the words cut and paste have always symbolized to me the quintessence of human creativity

> That is what rewriting is about. I do this for from 3 to 6 hours a day. But there are no software
> tools that allow you to do it. None! I've been trying to build a software tool that would allow
> you to do it for 35 years.

Not quoted: the sentence containing "garbagie", and "I filled the paste buds" (transcriber's
"pots"). The colloquium transcript below has the paste pots cleanly.

### Engelbart Colloquium, Stanford, Session 9 (1998)

https://www.dougengelbart.org/colloquium/session_09/session_09_nelson.html

**Unedited transcript, typos intact.** Said in Engelbart's own colloquium, with Engelbart present
and answering.

> The way we move things back and forth between these things is by the so called clip board which
> allows us to cut and paste, and copy. [...] This paradigm, I consider it an abomination. It must
> be swept away because it is at the heart of everything that is wrong with what people try to do
> with computers.

> Instead of calling these functions hide and plug, which would have been neutral terminology or
> slightly less neutral terminology with the keys that are conventional control C, control V, for
> cram and vomit. They call these things cut and paste. I have said for some years said that
> whoever chose those words should be hanged, because that is one of the principle social
> atrocities in the 20th Century. The fact that millions of people loose their valuable content
> every year because the phone rings or for some other dam reason because this brain dead mechanism
> screws up. Larry Testly [Tesler] says it was he.

> Engelbart: No. No. That was floating around in the sixties before.

The `[...]` in the first quote elides a digression about paradigms being invisible. `loose`,
`principle`, `dam`, `clip board` and "said for some years said" are the transcript's.

Nelson blames Tesler for the naming; Engelbart, in the room, will not even grant him the credit.

The paste pots, from the same page:

> It meant taking a draft, and cutting it, and taking all of the pieces in front of you on the
> table. Then saying this should go here, that is probably the best lead.....getting the sequence
> of materials as a parallel consideration of all of the parts. Looking at them simultaneously.
> Then using physical paste to put them in order.

Tolstoy, same page: two dictated copies, one filed, the other cut up across the floor of his
dacha, and "as he walked into the woods he'd call back. Don't touch my noodles."

His cousin in Norway, and **his own reply** -- the "exactly" is Nelson's, not Engelbart's:

> I just visited Norway, and a cousin of mine said I won't use computers because you can't see the
> previous version of what you are working. I said exactly.

What he showed her instead, which is transclusion with visible provenance:

> You are always going from a previous version to the next version and you want to see where the
> content came from. Here you have a document called Software Philosophy Long Version. And you pull
> across the paragraph, and you see a stripe showing its origin. Which remains in place, as shown
> here, showing you where it came from.

Not quoted: "an abdominal burden" and "abdominal mechanism", both the transcriber's
"abominable"; "I have an extreme grudge against both the parties and the Macintosh Team", where
"the parties" is probably "the PARC-ies" and is not clear enough to use.

## Ted Nelson, ASR captions

### BayCHI, "HCI Constructs Then and Now", 10 Aug 2021

https://www.youtube.com/watch?v=u5NECkdOSqs

Auto-generated captions, retrieved with `yt-dlp --write-auto-subs`, rolling duplicates collapsed.
**Weakest tier.** Punctuation below is added; no words are added.

Clean and load-bearing, the sentence that makes two of this directory's requirements Nelson's own:

> they could at least have made it visible and made it a stack for rearrangement but oh no

The euphemism line. One word is genuinely uncertain: these captions render it "made science sound
okay", and an earlier independent transcription of the same talk renders it "many signs sound
okay". Neither is a word. The clause is quoted with that token elided:

> These features should have been called hide and plug, but somehow using those familiar old words
> made [...] sound okay, like the words national socialism.

His subject is **euphemism**: a familiar, harmless-sounding name that launders the thing it
names. It is the same argument as "excused by a word that makes it sound somehow okay" in the 1999
written text, which is the safe citation if the point is ever disputed.

Also clear in these captions, for context rather than quotation: the clipboard is "an invisible
buffer", the words were "used to propagandize this abominable construct", the naming is a "crime
against humanity", and it "was perpetrated by a good friend of mine the late [great] larry
[Tesler]", who "kept insisting to me" over "many emails" that "the real cut and paste was only for
very specialist long-form work".

Digest with timestamps and the rest of the talk:
https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/ted-nelson/sources/2021-08-10-baychi-hci-constructs-transcript-digest.md

## Xerox Star

### "Designing the Star User Interface", Byte, April 1982

Smith, Irby, Kimball, Verplank, Harslem. Transcribed at GUIdebook:
https://guidebookgallery.org/articles/thestaruserinterfaceanoverview

> Star has a few commands that can be used throughout the system: MOVE, COPY, DELETE, SHOW
> PROPERTIES, COPY PROPERTIES, AGAIN, UNDO, and HELP. Each performs the same way regardless of the
> type of object selected. Thus we call them generic commands.

> Each generic command has a key devoted to it on the keyboard. (HELP and UNDO don't use a
> selection.)

> The keyboard has 24 easy-to-understand function keys.

On the `SAME` key, which is how COPY PROPERTIES is invoked, and which is the reason the keycap list
and the generic-command list differ:

> You select them with the mouse. You push the MOVE, COPY, or DELETE key. You push the OPEN key to
> see their contents, the PROPERTIES key to see their properties, and the SAME key to copy their
> properties.

> You can select the object(s) to be changed, push the SAME key, then designate the object to use as
> the source. COPY PROPERTIES makes the selection look the "same" as the source.

> You can select all the objects to be changed, push SAME, and select a line or symbol having the
> desired appearance.

Not quoted: the clause rendered "move the MOVE key" in both the GUIdebook and ACM transcriptions,
where the original means "press".

### Star Release 1 Product Software Functional Specification, v5.3 (1981)

https://bitsavers.org/pdf/xerox/star/STAR_Release_1_Product_Software_Functional_Specification_Ver_5.3_198115.pdf

> A user can move an object from one location to another by selecting it and pressing the MOVE key.

> A user can undo the effect of most commands by pressing the UNDO key. The system attempts to
> restore the user's environment to the state that existed before the command was invoked. Not all
> commands are totally reversible.

> A user may undo several successive commands by repeatedly invoking Undo.

**Star's undo was multi-level.** Any claim that Star had single-level undo is wrong; checked
against the spec.

### "Star graphics", Baudelaire and Stone, SIGGRAPH 1980

https://doi.org/10.1145/800064.801270

> The left function group contains the generic commands: MOVE, COPY, DELETE, SHOW PROPERTIES, COPY
> PROPERTIES, and AGAIN.

## Hacker News

### kps, 2022-06-14, on the Star keyboard

https://news.ycombinator.com/item?id=31740860

> The left function cluster replaced the chord set of Engelbart's NLS and the Alto, while retaining
> the same two-handed style of operation: mouse on the right to select the object, keys on the left
> to select the operation.

> Worth also noting that Star didn't use the Clipboard Cut/Copy/Paste (fragile invisible state)
> model, which I think came from Larry Tesler and certainly was popularized by the Macintosh.
> Instead it had the two operations MOVE, which moved the current selection to the target location,
> and COPY, which duplicated the current selection at the target location.

Verified verbatim through the Firebase item API. Independent of Nelson, and lands on the same
culprit.

## Vim

### `version7.txt`, Vim's own documentation

https://github.com/vim/vim/blob/master/runtime/doc/version7.txt

The software documenting the bug, in the release notes for the version that fixed half of it:

> Previously there was only one line of undo-redo. If, after undoing a number of changes, a new
> change was made all the undone changes were lost. This could lead to accidentally losing work.

And the other half, unfixed, in the same document:

> There is no graphical display of the tree with changes, navigation can be quite confusing.

Undo branches with `g-`, `g+`, `:earlier`, `:later`, `:undolist` shipped in Vim 7.0 (2006);
persistent undo via `undofile` shipped in 7.3 (2010).

### Vim 7.0 release announcement, Bram Moolenaar, 2006

https://marc.info/?l=vim-announce&m=114708043011893

From the feature list:

> Undo branches: never accidentally lose text again

## Sun

### `textedit(1)`, SunOS manual page

https://cmgm-new.stanford.edu/man2html/textedit.1.html

Authoritative for SunView's selection states and for what each L-key actually operated on. The
function-key table in this page is headed "Sun-2|3 Key", so it documents the Sun-2/Sun-3 era
bindings.

> There are two types of selections: a primary selection is indicated by video-inversion of the span
> of characters, and tends to persist. A secondary selection is indicated by underlining the span of
> characters and only exists while one of the four function keys corresponding to the commands Cut,
> Find, Paste, or Copy, is depressed.

> In addition, a selection can be "pending-delete," as indicated by overlaying the span of characters
> with a light gray pattern. A selection is made pending-delete by holding the CTRL key while clicking
> the LEFT or MIDDLE mouse buttons. If a primary selection is pending-delete, it is only deleted when
> characters are inserted, either by type-in or by Paste or Copy. If a secondary selection is
> pending-delete, it is deleted when the function key is released, except in the case of the Find,
> which deselects the secondary selection.

Per-key operand resolution, quoted from the function-key table:

> Copy L6 Copies the primary selection, either to the Clipboard or at the closest end of the
> secondary selection.

> Paste L8 Copies either the secondary selection or the Clipboard at the insertion point.

> Find L9 Searches for the pattern specified by, in order, the secondary selection, the primary
> selection, or the Clipboard.

> Cut L10 Erases, and moves to the Clipboard, either the primary or the secondary selection.

The table lists L1 Stop, L2 Again, L4 Undo, L5 Front, L6 Copy, L7 Open, L8 Paste, L9 Find, L10 Cut,
and F1 CAPSLOCK. **L3 (Props) is absent from it**, because `textedit` has no properties sheet; L3's
legend comes from the keyboard documentation, not from this page. The same page also documents Mac-style
keyboard equivalents alongside the L-keys: META-X cut, META-F find, META-C copy, META-V paste, and
META-P copy-then-paste.

### XView Reference Manual, Volume 7B, Appendix B (selection compatibility)

https://www.oreilly.com/library/view/volume-7b-xview/9780937175880/chapter-66.html

Authoritative for the rank names and for the keyboard-state-dependent resolver:

> asked should be one of SELN_CARET, SELN_PRIMARY, SELN_SECONDARY, SELN_SHELF, or SELN_UNSPECIFIED.

> If asked is SELN_UNSPECIFIED, the client indicates it wants whichever of the primary or secondary
> selections is appropriate given the current state of the function keys; the one acquired can be
> determined from the return value.

### `get_selection(1)`, SunOS manual page

https://cmgm-new.stanford.edu/man2html/get_selection.1.html

Confirms that the user-facing name for `SELN_SHELF` is the clipboard:

> 1: primary; 2: secondary; 3: clipboard.

## X11

### Inter-Client Communication Conventions Manual, Version 2.0

https://www.x.org/archive/X11R7.7/doc/xorg-docs/icccm/icccm.html

X Consortium Standard. Title page: **David Rosenthal, Sun Microsystems, Inc.**, edited by **Stuart
W. Marks, SunSoft, Inc.** Copyright 1988, 1991, 1993, 1994 X Consortium. The Preface to Version 1.1
credits the Cut-Buffer section to **Andrew Palay**. Quoted at length in
[SELECTIONS-AND-CUT-BUFFERS.md](SELECTIONS-AND-CUT-BUFFERS.md); the load-bearing passages are
Chapter 1 on scope and Chapter 3 on the ring.

> It was an explicit design goal of X Version 11 to specify mechanism, not policy.

> This document proposes suitable conventions without attempting to enforce any particular user
> interface.

> The cut buffers consist of eight properties on the root of screen zero, named by the predefined
> atoms CUT_BUFFER0 to CUT_BUFFER7. These properties must, at present, have type STRING and format
> 8.

> A client that stores data in the cut buffers (an owner) first must rotate the ring of buffers by
> plus 1 by using RotateProperties requests to rename each buffer; that is, CUT_BUFFER0 to
> CUT_BUFFER1, CUT_BUFFER1 to CUT_BUFFER2, ..., and CUT_BUFFER7 to CUT_BUFFER0.

> In response to a specific user request, a client may rotate the cut buffers by minus 1 by using
> RotateProperties requests to rename each buffer; that is, CUT_BUFFER7 to CUT_BUFFER6, CUT_BUFFER6
> to CUT_BUFFER5, ..., and CUT_BUFFER0 to CUT_BUFFER7.

> Data should be stored to the cut buffers and the ring rotated only when requested by explicit user
> action. Users depend on their mental model of cut buffer operation and need to be able to identify
> operations that transfer data to and fro.

On the selection side, the sentence that explains why a Unix clipping dies with its source:

> Each selection is owned by a client and is attached to a window. Selections communicate between an
> owner and a requestor. The owner has the data representing the value of its selection, and the
> requestor receives it.

The predefined selection names, from the name-space table in Chapter 1: `PRIMARY`, `SECONDARY`,
`CLIPBOARD`.

### Conrad Parker, ICCCM rant, 12 July 2001

https://github.com/porridgewithraisins/x11cp/blob/main/rant

Mail to `slug-chat`, replying to Sean Neakums quoting Jeff Waugh's "Go read the ICCCM. Come back
when you're done crying." Canonical copy as linked; the headers in that copy have the addresses
`xxxxxxxx`-masked, which is how it circulated. Profanity and capitals are the author's.

> Name one fucking program in the whole world that uses MULTIPLE selections by choice? [...] And
> XA_SECONDARY? Who the fuck uses the SECONDARY selection? and who actually queries TARGETS? All
> anyone ever fucking does with the selection is COPY TEXT!!

> The ICCCM is the coding equivalent of the Medieval rack, except its advertised as some kind of X11
> swingers party.

The `[...]` elides two sentences about `MULTIPLE` being a performance optimization nobody wants.
