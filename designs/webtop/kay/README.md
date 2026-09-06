# Alan Kay on the browser, HyperCard, and this work

**Kay has already reviewed the lineage this hub is built on, and he criticized it in two specific
ways that are worth more than the praise.** All of it is on the record, published by Don, and this
document keeps the quotes together with their provenance so they can be used without being
misattributed.

## The claim: the browser should have been an operating system, not an app

From his Quora answer to *"Should web browsers have stuck to being document viewers?"* — the answer
is no, and hard the other way:

> "Actually quite the opposite, if 'document' means an imitation of old static text media (and later
> including pictures, and audio and video recordings).
>
> "It was being willing to settle for an overly simple text format and formatting scheme — 'for
> convenience' — that started the web media architecture off in entirely the wrong direction
> (including the too simple reference scheme c.f. Doug Engelbart and Ted Nelson). Circa early 90s, it
> had the look and feel of an **atavistic hack**. I expected that Netscape would fix this rather than
> just try to dominate what was there."

And the positive form:

> "**The underlying system for a browser should not be that of an 'app' but of an Operating System**
> whose job would be to protectively and safely run encapsulated systems (i.e. 'real objects') gotten
> from the web. It should be the way that web content could be open-ended, and not tied to functional
> subsets in the browser."

> "This doesn't work if you only try to imitate old media, and especially the difficult to compose
> and edit properties of old media. You have to include all media that computers can give rise to,
> and you have to do it in a form that allows both **'reading' and 'writing' and the 'equivalent of
> literature' for all users.**"

## Symmetry is the word this hub needed

> "Apple's Hypercard was a terrific and highly successful end-user authoring system whose media was
> scripted, WYSIWYG, and **'symmetric'** (in the sense that the 'reader' could turn around and
> 'author' in the same high-level terms and forms). **It should be the start of — and the guide for —
> the 'User Experience' of encountering and dealing with web content.**"

*Symmetric* is a better term than anything in this cluster for what
[HYPERLOOK.md](../HYPERLOOK.md) describes and what [PLAYABLE-CORPUS.md](../PLAYABLE-CORPUS.md)
argues: not "documents should be programmable" but **the reader and the author operate in the same
terms.** Adopt the word.

And the verdict on what was lost:

> "HyperCard is an especially good example of a system that was 'finished and smoothed and
> documented' beautifully. It deserved to be successful. **And Apple blew it by not making the design
> framework the basis of a web browser** (as old PARC hands advised in the early 90s …)"

## What he said about *this* work, criticism included

He read Don's NeWS, HyperLook and SimCity material and responded. The praise:

> "This work is so good — for any time — and especially for its time — that I don't want to sully it
> with any criticisms in the same reply that contains this praise."
>
> "I will confess to not knowing about most of this work until your comments here — and this lack of
> knowledge was a minus in a number of ways wrt some of the work that we did at Viewpoints since ca
> 2000."

Then, in a separate reply, the criticism — **which is the part that matters:**

> "My only real regret about this terrific work is that **your group missed the significance for
> personal computing of the design of Hypertalk in Hypercard.**
>
> "It's not even that Hypertalk is the very best possible way to solve the problems and goals it took
> on — hard to say one way or another — but I think it is the best example ever actually done and
> given to millions of end users. And by quite a distance.
>
> "Dan Winkler and Bill Atkinson violated a lot of important principles of 'good programming language
> design', but they achieved the first overall system in which **end-users 'could see their own
> faces'**, and could do many projects, and learn as they went."

**He was right, and HyperLook contains the proof.** HyperLook chose PostScript as its scripting
language, and users complained until Arthur van Hoff wrote **PdB, a C-to-PostScript compiler**, so
they could avoid it. A dynamic language that end users decline to write is not an end-user authoring
system, whatever else it is. The receipt for Kay's criticism is a compiler in the same product.

In the same OLPC thread where the SimCity criticism below appears, the register toward Don is the
opposite: *"We are benefiting here from Don Hopkins' generosity (and of the original designers and
owners of these games)."*

## What he said about SimCity, which is a different target

**This is criticism of the game's design, not of Don's port**, and the distinction matters because
Don is on Kay's side of it — the letter it appears in opens by applauding him. And he says plainly
who he said it to:

> "**I actually argued with him [Will Wright] and Maxis for not making SimCity very educational.**
> […] I've never thought of it as a particularly good design for educational purposes."

The bracketed name is Don's editorial insertion. From the OLPC mailing list, November 2007:

> "My main complaint about this game has always been the **rigidity, and sometimes stupidity, of its
> assumptions** (counter crime with more police stations) and the **opaqueness of its mechanism**
> (children can't find out what its actual assumptions are, see what they look like, or change them
> to try other systems dynamics).
>
> "So I have used SimCity as an example of an **anti-ed environment** despite all the awards it has
> won. **It's kind of an air-guitar environment.**
>
> "In the past, I tried to get Maxis to take the actual (great) educational possibilities more
> seriously, but to no avail."

And the constructive form, which is a design brief rather than a complaint:

> "Going to Python can help a few areas of this, but a better abstraction for the heart of SimCity
> would be **a way to show its rules/heuristics in a readable and writable form.**"

> "There is a nice separation between the 'rules/dynamics' of a game's world and the
> 'strategies/actions' of the characters. There could be a third separation to break out the graphics
> and sound routines as a media environment. […] in SimCity, the first and most useful breakout for
> children would be to allow various UIs to be made that would let children find out about and try
> experiments with the 'city dynamics rules'."

**Micropolis is the answer to that brief** — the simulation opened, the source published, the pie
menus added. Kay's objection has a repository as its reply, which is the only kind of reply this
project should aspire to. Don also published a written response at the time, *Responding to Alan
Kay's criticisms of SimCity*.

Two things not to blur. Kay's target here is **Maxis and the game's design**, which he says he tried
to change directly and failed; Don ported it and later opened it. And *"readable and writable rules"*
is the same demand as the HyperTalk criticism above, aimed at a different artifact — which makes it
one consistent position rather than two grievances.

## He has said nothing about gwern.net

No criticism, no praise, nothing found. His argument about the browser is architectural and dates
from the early nineties onward; it is about the web's design, and it neither mentions nor implies
anything about gwern.net specifically. **Do not stage Kay as a critic of gwern's work** — the
relevance is that gwern inherited a medium Kay considers a wrong turn, which is a different claim and
the only one supportable.

## The mission statement, handed over unprompted

> "For many reasons, **a second pass at the end-user programming problem** — that takes advantage of
> what was learned from Hypercard and Hypertalk — **has never been done** (AFAIK). The Etoys system
> in Squeak Smalltalk in the early 2000s was very successful, but the design was purposely limited to
> 8–11 year olds (in part because of constraints from working at Disney).
>
> "It's interesting to contemplate that the follow on system might not have a close resemblance to
> Hypertalk — perhaps only a vague one …."

That is the brief. The last line is also permission: the successor does not have to look like
HyperTalk, so an LLM sitting where the scripting language used to sit is not automatically a
betrayal of the idea.

## The design constraint that survives being handed to an LLM

From the OLPC threads, and it is the most directly applicable thing he has said about anything this
project builds:

> "One thing that has consistently worked is **'close to natural language but clearly not natural
> language'** […] it really helps if the **gist-view** of a program is a kind of metaphor for what it
> does, even if one has to think harder about the detailed meaning.
>
> "For children, Hypercard was OK in many respects for the gist-view, but **was too like English** for
> both deep understanding and for programming (many children had a hard time getting past the idea
> that Hypercard couldn't understand and do any reasonable English sentence)."

HyperTalk failed by looking *too much* like English, so users expected it to understand any English
sentence. MOOLLM writes skills and characters as markdown and YAML read by a model, which is the same
trap with the failure inverted — **the system now does understand reasonable English sentences**, so
the disappointment moves rather than vanishing: it relocates to the boundary between what the model
does reliably and what it does once and then not again.

The criterion survives intact. *Clearly not natural language* is a demand for a **visible boundary**,
and it is the argument for keeping YAML structure next to the prose: the structure is the part that
says *this is a form with edges, not a conversation.* His *gist-view* is also the semantic pyramid,
named better and thirty years earlier.

### The boundary is a property of the view, not of the notation

The stronger answer is that **the choice between prose and structure is not a choice.** `SKILL.md`
is the receipt: a skill exists as markdown *and* as YAML, each doing what it is good at — prose for
protocol, argument and voice; structure for fields, enumerations and anything a build has to read.
Neither is canonical. Write whichever comes naturally, in whichever order, and **the model generates
the missing one**, in either direction.

Which relocates Kay's boundary to where it belongs. *Clearly not natural language* is not a demand
that the author type in a restricted notation; it is a demand that **the edges be visible at the
moment you are looking for edges.** So there are several views over one substrate, and they are
peers:

| View | For | Boundary shows up as |
|---|---|---|
| Prose (`SKILL.md`) | protocol, reasoning, voice | headings and named sections |
| yaml-jazz text | people who like writing structure directly | keys, indentation, closed value sets |
| WYSIWYG | people who do not | a form with typed fields and no free-text escape |
| Domain-specific editor | one kind of object, done well | the widget refuses what the schema refuses |

**This is HyperLook's move, not a new one.** Metacircular property sheets were domain-specific
editors over the same objects that the drawing editor and the scripts also edited — you could open a
property sheet on a property sheet. Kay's own praise for HyperCard was for solving *end-user*
problems with limited degrees of freedom, and the multiple-views arrangement is how you get that
without giving up the deep dynamic language he wanted underneath: constrain the *view*, not the
substrate.

**The load-bearing requirement is comment preservation, and it is where this usually dies.** In
yaml-jazz, comments are semantic data that the model reads, not decoration — so an editor that
round-trips a file and drops its comments has destroyed meaning, not formatting. That rules out the
ordinary parse-and-re-emit pipeline (PyYAML discards comments by construction) and requires a
round-trip parser that preserves comments, key order and blank-line structure. Every WYSIWYG or
domain-specific editor is therefore built on that constraint or it is not built. It is a real
engineering commitment with a real library behind it, and it is checkable: round-trip a file through
each editor and diff.

Accessibility falls out of the same arrangement rather than being bolted on. The prose view is
already a document, the structured view is already a form, and both are text under version control —
so a screen reader gets a heading tree or a labelled form, whichever the reader prefers, instead of a
canvas full of unlabelled boxes.

**The honest cost is drift.** Two representations of one thing can disagree, and "generate the
missing one" only helps the first time. Once both exist and both get hand-edited, something has to
notice — so agreement between a skill's prose and its structure is a **build-time lint**, not a
convention, and the same LLM-proposes-human-confirms discipline applies as everywhere else. Which
also means the answer to Kay is conditional on that lint existing: without it, the parallel files are
a promise rather than a mechanism.

## Two more from OLPC that pre-date our own theses

**Science as map-making, which is the Know Knob's ancestor:**

> "**science is more like map-making for real navigators than bible-making**: IOW, the maps need to be
> as accurate as possible **with annotations for errors and kinds of measurements**, done by competent
> map-makers rather than story tellers, and they are always subject to improvement and rediscovery."

*Annotations for errors and kinds of measurements* is the signed assessment with its `evidence`
dimension, described in 2007 as a property of good maps.

**Gray boxes that pop open, which states our thesis better than we do:**

> "**the black and gray boxes that scaffold what they are doing can be popped open** and understood
> and modified […] 'forward' is a black box initially, and very useful in that form. But there is a
> point when the children will be greatly aided by understanding that forward is just a vector
> addition […] **The underlying language for the system itself has to reveal itself as the same
> species as what the children have been learning.**"

> "black or translucent boxes serve only on the side and not at the center of the learning. **What is
> the center and what is the side will shift as the learning progresses.**"

Opacity is graduated and moves with the reader — semantic zoom applied to mechanism rather than to
text. *Same species* is symmetry again, aimed at the substrate. And *on the side, not at the center*
is a placement rule for abstraction: a black box is fine right up until it contains the thing you are
supposed to be learning.

**And the warning aimed squarely at a repo like this one:**

> "**computer environments, once made (with lots of effort and dedication) tend to form tribal bonds
> that are rather religious in nature.** The amount of effort required plus the attendant religion
> makes it extremely difficult to take new insights and ideas and make brand new better environments."

Full extraction of all seven threads: [OLPC-2007.md](OLPC-2007.md).

## Views as watchers, from the MVC exchange

Don asked Kay directly about the evolution of MVC and Morphic. The reply is short and every sentence
in it is load-bearing here:

> "**Things seem to hang on in computing just because they work a little bit.**
>
> "MVC was originally done at PARC almost 40 years ago. The good part was philosophical — the idea to
> adapt the notion of 'cameras' and 'worlds' in the original 3D graphics stuff I participated in at
> Utah 45 years ago. The bad part of MVC was how we implemented it — much too much machinery, etc.
>
> "**I like to do views as 'watchers' which do not affect what they are viewing.** There are lots of
> ways to do this. Similarly, I like to also use 'watchers' (context sensitive to the views) to catch
> needed inputs. We have never done a really satisfactory **automatic inverter** for dealing with the
> loss of 'dimensions' that happen when a view is made (but we have done some experimental ones).
>
> "**One important criterion is for end-users of all kinds to be able to easily make their own views
> in a very powerful ad hoc way via construction.** We have done a number of adaptations and
> generalizations of how this can be done in Hypercard — and this seems to work well (enough)."

Four things this hub takes from that paragraph:

| Kay's phrase | Where it lands |
|---|---|
| Things hang on because they work a little bit | The standing indictment of the clipboard, the bookmark, tab order, and the browser itself |
| Views as **watchers** that do not affect what they view | [VIEWS-AS-TESTIMONY.md](../../pie-stack-views/VIEWS-AS-TESTIMONY.md) — a saved view as a non-destructive, citable artifact |
| Watchers to **catch needed inputs**, context-sensitive to the view | A view that also defines what you can do from it: the room's verb set |
| No satisfactory **automatic inverter** for the dimensions a view discards | The honest open problem. Every semantic-zoom rung throws information away, and turning the knob back does not restore what the summary dropped. Nobody has solved this, including us |

That last row is the most useful sentence Kay gave this project, because it names a hard problem the
design has been quietly assuming away.

## What we do differently, stated plainly

- **The substrate is git and static files, not a live image.** Kay's objects want a running system;
  we want an artifact that survives its window system, because NeWS did not.
- **The end-user language is a model, not a syntax.** His brief allows this. Whether it satisfies it
  is exactly the open question, and the LLM-at-build-time discipline in
  [`../../TAGSONOMY-COMPILER.md`](../../TAGSONOMY-COMPILER.md) is the attempt.
- **We do not get to skip his criticism.** *End users could see their own faces* is the standard.
  A system that requires an LLM subscription to author in fails it differently than PostScript did,
  but it does fail it, and that belongs in [OBJECTIONS.md](../OBJECTIONS.md).

## Provenance

| Quote | Where | Status |
|---|---|---|
| Browser as OS; atavistic hack; symmetry; reading and writing for all users | Kay's **Quora** answer, *"Should web browsers have stuck to being document viewers?"*, collected in [Don's article](https://donhopkins.medium.com/alan-kay-on-should-web-browsers-have-stuck-to-being-document-viewers-and-a-discussion-of-news-5cb92c7b3445) | Public |
| Praise and the two criticisms of Don's work; the "second pass" brief | Discussion thread on that answer plus an **email exchange** — Don replied by email to Kay, David Rosenthal and James Gosling; parts of the Quora discussion require login | Public via Don's article; the email thread's full contents are not published |
| HyperCard "deserved to be successful"; Apple blew it | Quoted by Don in [the HyperLook article](https://donhopkins.medium.com/hyperlook-nee-hypernews-nee-goodnews-99f411e58ce4) | Public |
| Things hang on; views as watchers; automatic inverter; end-users making their own views | Email to Don, published by him on HN — [`7755759`](https://news.ycombinator.com/item?id=7755759) (2014-05-16), reposted [`8841428`](https://news.ycombinator.com/item?id=8841428) | Public, quoted in full by Don |
| Anti-ed / air-guitar environment; rigid and opaque assumptions; readable and writable rules; the three-way separation of dynamics, strategies and media; "Don Hopkins' generosity" | **OLPC mailing list, November 2007** — a thread among Kay, SJ Klein, Guido van Rossum, Don and others about opening up SimCity | Public, archived by Don in his own repo — see the archive below |

### The OLPC archive is the richest source and it is already in a repo

Extracted thread by thread in **[OLPC-2007.md](OLPC-2007.md)**.
`micropolis/turbogears/micropolis/htdocs/static/html/alankay.html` mirrors **seven** discussions,
each with a `donhopkins.com` node URL behind it:

| Thread | Subject |
|---|---|
| node 145 | **SimCity Rules** — Kay, SJ Klein, Guido van Rossum, Don and others on articulating SimCity's rules so they are understandable and modifiable |
| node 134 | **Alan Kay's ideas about SimCity for OLPC** — where the anti-ed and air-guitar lines are |
| node 135 | **Responding to Alan Kay's criticisms of SimCity** — Don's answer, published |
| node 139 | Robot Odyssey |
| node 137 | OLPC visual programming language, with Guido van Rossum |
| node 140 | Visual programming |
| node 132 | Programming languages |

This is the substantive "discussions with Alan Kay" material, and it is public and Don's own archive.

**Still to pin down:** the original venue and date of the "deserved to be successful" quote; whether
the Kay/Rosenthal/Gosling email thread holds more that Don is willing to publish; whether the
donhopkins.com nodes are still live or the repo mirror is now the only copy; and **a clean copy of
node 140**, whose transcription in the mirror has dropped text mid-sentence in at least three places.
Don's recollection is the third source and should be recorded as *his recollection*, distinct from the
quotes above.

**One open personal thread:** in node 139 Kay asks Don, about the Etoys reimplementation of Robot
Odyssey, *"we now have funding and are really going to do it this year. Want to help design and build
it?"* Whether that went anywhere is not in the archive.

Portrayal discipline: [`skills/representation-ethics/`](../../../skills/representation-ethics/). We
quote what is published and do not construct his side of anything.

## Related

- [HYPERLOOK.md](../HYPERLOOK.md) — the system his HyperCard verdict is about, and where PdB proves his criticism
- [`../../pie-stack-views/VIEWS-AS-TESTIMONY.md`](../../pie-stack-views/VIEWS-AS-TESTIMONY.md) — watchers that do not affect what they watch
- [OBJECTIONS.md](../OBJECTIONS.md) — where "end users could see their own faces" is a charge against us
- [nelson/](../nelson/) — Kay cites Nelson and Engelbart on the too-simple reference scheme, which is that pack's whole subject

↑ [webtop hub](../README.md)
