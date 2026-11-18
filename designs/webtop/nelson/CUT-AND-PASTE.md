# Cut and paste, in Ted Nelson's words

Ted Nelson has spent decades complaining that the clipboard stole the names of a writer's most
important tools. Everything quoted here is from his public writing and recorded talks, linked so
you can read or watch him say it. The last section says how [link pumps](../LINK-PUMPS.md) answer
him.

## The complaint

From [Ted's computer paradigm, expressed as one-liners](http://www.hyperland.com/TedCompOneLiners)
(1999), on his own site:

> Consider the "clipboard" on the Mac, PC or XWindows. It's just like a regular clipboard, except
> (a) you can't see it, (b) it holds only one object, (c) whatever you put there destroys the
> previous contents. Aside from that, IT'S JUST LIKE A REGULAR CLIPBOARD IN EVERY OTHER RESPECT--
> EXCEPT THERE AREN'T ANY OTHER RESPECTS!

> It is a further offense-- the greatest atrocity in the computer field, I believe-- that the
> crippled and destructive functions of this pseudo-clipboard have been falsely given the names
> "cut" and "paste"-- which for decades have meant something ENTIRELY different to writers, the
> function of parallel rearrangement with all things visible.

In the [video transcribed at MIT](https://web.mit.edu/m-i-t/forums/hypertext/paradigms/clipboard.htm)
he adds: "anything you put on it destroys what was there previously, and if the phone rings, you
lose the contents." In his BayCHI talk he says the functions "should have been called hide and
plug." And on the Internet Archive, describing his
[Cut and Paste, 2014](https://archive.org/details/cutnpaste_201909): "since the letters used on
both Mac and Windows are C and V, they could better have stood for Cram and Vomit."

## What the words meant

His first salaried job was as a copy boy at the New York Times, where the first task every morning
was filling the paste pots, so reporters could cut their drafts apart and paste them down in a new
order. In ["Real cut and paste"](https://www.youtube.com/watch?v=6_35RDA6r3g) he tells that story,
then cuts up a manuscript on a cutting board, staples the pieces in a new order, and writes between
them.

The other half of the story is Tolstoy's. Nelson tells it in
["HCI Constructs Then and Now"](https://www.youtube.com/watch?v=u5NECkdOSqs) (BayCHI, August 2021):
Tolstoy dictated each new version to two daughters at once, set one copy aside, and cut the other up
all over the floor of his dacha, calling out "don't touch my noodles" as he went for a walk. In
["Doing a full noodle"](https://www.youtube.com/watch?v=RWeY-zGWsbQ) Nelson does one himself and asks
why people don't understand that "writing takes a great deal of rearrangement; that's why there's so
much bad writing."

Asked at BayCHI what tool he writes with now, he answered: "scissors and a stapler in the outsy
position," so the staples pull out.

## What he asked for

The modest version, at BayCHI: "They could at least have made it visible and made it a stack for
rearrangement."

The real version is "pullacross editing," in
[Xanalogical Structure](https://xanadu.com.au/ted/XUsurvey/xuDation.html): "the author should be
able to pull screen contents from old versions into new, seeing all points of origin and also
seeing what contents have not yet been used."

And the larger point, from the one-liners, on WYSIWYG: imitating paper on a screen "is like tearing
the wings off a 747 and using it as a bus on the highway. What we really need is software designs
that go into realms that cannot be visualized on paper."

## How link pumps answer him

- **"You can't see it."** The clipboard is a folder in a git working tree, open beside the
  document.
- **"It holds only one object."** It holds a tree of clippings: a passage, its summary, and the
  sentences pulled out of it, filed together. That's the stack for rearrangement, with branches.
- **"Whatever you put there destroys the previous contents."** Every clipping is a commit, so a new
  one can't overwrite an old one. Neither can the phone ringing.
- **"Parallel rearrangement with all things visible."** A pump previews in both documents while you
  pull, and what moved leaves a stripe of words behind saying where it went.
- **"Seeing what contents have not yet been used."** Discards go to a trash folder you can open,
  and "not used yet" is a natural pump filter.
- **"Realms that cannot be visualized on paper."** Scissors can only move a piece or copy it. When a
  language model rewrites both sides, move and copy become one dial: each side keeps a version
  written for its own context.

An AI sidecar that copies your text into a prompt you can't see is Nelson's "hideyhole" again,
with a chauffeur. The pumps keep everything on the table.

## Sources

- Ted Nelson, [Ted's computer paradigm, expressed as one-liners](http://www.hyperland.com/TedCompOneLiners), 1999 ([mirror](https://xanadu.com.au/ted/TN/WRITINGS/TCOMPARADIGM/tedCompOneLiners.html)).
- [Clipboard: cut and paste](https://web.mit.edu/m-i-t/forums/hypertext/paradigms/clipboard.htm), transcription of a Nelson video, MIT.
- [Real cut and paste](https://www.youtube.com/watch?v=6_35RDA6r3g) and [Doing a full noodle](https://www.youtube.com/watch?v=RWeY-zGWsbQ), Ted Nelson on YouTube.
- [HCI Constructs Then and Now](https://www.youtube.com/watch?v=u5NECkdOSqs), BayCHI, August 10, 2021. Quotes are from YouTube's automatic captions, punctuated.
- [Cut and Paste, 2014](https://archive.org/details/cutnpaste_201909), Ted Nelson Archive, Internet Archive.
- [Doug Engelbart's Colloquium at Stanford, session 9](https://www.dougengelbart.org/colloquium/session_09/session_09_nelson.html), Nelson's talk, with the paste pots and Tolstoy's noodles.
- Ted Nelson, [Xanalogical Structure, Needed Now More than Ever](https://xanadu.com.au/ted/XUsurvey/xuDation.html).

↑ [Nelson: visible connection](README.md) · [Link pumps](../LINK-PUMPS.md)
