# Don Hopkins on HN: Winer, UserLand, outliners

Machine sweep of the Hacker News Algolia index for comments by `DonHopkins` matching the
Winer/UserLand/outliner vocabulary, confirmed by local regex against each comment body
(Algolia typo-tolerance off, plus a second local pass to drop near-matches).

- **Confirmed unique comments:** 71
- **Range:** 2014-05-11 → 2026-09-03
- **Regenerate:** `python3 data/sweep.py` (writes `data/hn-donhopkins-outliner-sweep.json`)

Buckets below: **core** mentions Winer or a UserLand product by name; **outliner** is about
outliners without naming him; **incidental** matched only a generic word (mostly "frontier" as in
frontier models / Electronic Frontier Foundation) and is kept for completeness, not relevance.

Narrative and deduplication: [`README.md`](../README.md).

## Core — Winer / UserLand named  (39)

- **2014-05-11** · [`7728020`](https://news.ycombinator.com/item?id=7728020) · *The Unix Haters Handbook (1994) [pdf]*  
  `Dave Winer, Winer`  
  In order to truly appreciate the rich dynamic interactive multimedia experience of this web page, you should view it in a modern browser fully supporting the standard <BLINK> tag, such as Netscape Navigator version 3.0 gold. That was the only legitimately justifiable use of the <BLINK> tag that …

- **2016-10-26** · [`12800570`](https://news.ycombinator.com/item?id=12800570) · *Parsing JSON is a Minefield*  
  `OPML`  
  You could even write comments as a linear RSS feed of nested OPML outlines, by converting all that XML to JSON.

- **2018-01-24** · [`16226209`](https://news.ycombinator.com/item?id=16226209) · *Ted Nelson on What Modern Programmers Can Learn from the Past [video]*  
  `Dave Winer, Frontier, Manila, OPML, Radio UserLand, UserLand, Winer, outliner`  
  Reading documents from 20 years ago is a mixed bag. Links usually fail horribly, which was something Xanadu was trying to solve, but I'm not convinced they could have solved it so well that 20-year-old links would still actually work in practice. I've always tried to write documents in a simple …

- **2018-01-24** · [`16224154`](https://news.ycombinator.com/item?id=16224154) · *Ted Nelson on What Modern Programmers Can Learn from the Past [video]*  
  `Dave Winer, Frontier, UserLand, Winer`  
  I think his biggest problem is that he refuses to collaborate with other people, or build on top of current technology. He's had a lot of great important inspirational ideas, but his implementation of those ideas didn't go anywhere, he's angry and bitter, and he hasn't bothered re-implementing …

- **2018-01-24** · [`16226845`](https://news.ycombinator.com/item?id=16226845) · *Ted Nelson on What Modern Programmers Can Learn from the Past [video]*  
  `Radio UserLand, UserLand`  
  Server side scripting languages were critical to the success of the web, before browser side JavaScript was available and matured. Simple stateless perl cgi scripts forked from apache that talk to text databases or mysql were the first simplest step, but things got much more interesting with long …

- **2018-06-14** · [`17309132`](https://news.ycombinator.com/item?id=17309132) · *Console.table()*  
  `Frontier, Radio UserLand, UserLand`  
  Recently I've been working on kind of the converse of this problem with JSON and spreadsheets, and I'll briefly describe it here (and I'll be glad to share the code), in the hopes of getting some feedback and criticism: How can you conveniently and compactly represent, view and edit JSON in …

- **2018-08-24** · [`17835440`](https://news.ycombinator.com/item?id=17835440) · *The rise and rise of JSON (2017)*  
  `Winer`  
  >Though one might think that a contest between data interchange formats would be unlikely to engender death threats, Winer wrote: >"No doubt I can write a routine to parse [JSON], but look at how deep they went to re-invent, XML itself wasn’t good enough for them, for some reason (I’d love to hear …

- **2019-05-12** · [`19889362`](https://news.ycombinator.com/item?id=19889362) · *Surprising Bash Variables*  
  `UserLand`  
  It's perfectly fair. You're the one who got to cherry pick the script to use as an example, so don't complain that I cherry picked the most ridiculous line of that code. Python can generate a human readable help menu with much less trouble. Tell me one thing about that script that's easier in bash …

- **2019-07-13** · [`20425970`](https://news.ycombinator.com/item?id=20425970) · *I was wrong about spreadsheets (2017)*  
  `Aretha, Dave Winer, Frontier, Manila, OPML, Radio UserLand, ThinkTank, UserLand, Winer, XML-RPC, outliner`  
  The thing that's missing from "Google Docs" is a decent collaborative outliner called "Google Trees", that does to "NLS" and "Frontier" what "Google Sheets" did to "VisiCalc" and "Excel". And I don't mean "Google Wave", I mean a truly collaborative extensible visually programmable spreadsheet-like …

- **2019-08-12** · [`20672970`](https://news.ycombinator.com/item?id=20672970) · *Python Is Eating the World*  
  `Aretha, Dave Winer, Frontier, Manila, OPML, Radio UserLand, UserLand, Winer, XML-RPC, outliner`  
  That's a stupendously anonymous appeal to authority you've made there, and it's unclear what argument you're actually saying without some explicit parenthesis around all those deeply nested phrases, or some kind of grammatical diagram. Can you please restate how we disagree in a few simple …

- **2019-08-23** · [`20780928`](https://news.ycombinator.com/item?id=20780928) · *A Pissed-Off Tutorial for Google Wave (2010) [video]*  
  `Aretha, Dave Winer, Frontier, ThinkTank, UserLand, Winer, outliner, outlining`  
  One thing an outliner lets you do that you can't do with something like Wave or a tree structured discussion group is to arbitrarily rearrange the tree. You're right, you can represent tree-structured outlines in Word or Docs (or JSON in Excel or Sheets as I described here [1]), but it's clumsy …

- **2019-08-23** · [`20773851`](https://news.ycombinator.com/item?id=20773851) · *A Pissed-Off Tutorial for Google Wave (2010) [video]*  
  `Dave Winer, Frontier, Winer, outliner`  
  I love the collaborative features of Google Docs and Google Sheets. The thing that's missing from "Google Docs" is a decent collaborative outliner called "Google Trees", that does to "NLS" and "Frontier" what "Google Sheets" did to "VisiCalc" and "Excel". And I don't mean "Google Wave", I mean a …

- **2019-10-06** · [`21170440`](https://news.ycombinator.com/item?id=21170440) · *Representing and Editing JSON with Spreadsheets (2018)*  
  `Aretha, Dave Winer, Frontier, Manila, OPML, Radio UserLand, ThinkTank, UserLand, Winer, XML-RPC, outliner`  
  DonHopkins 85 days ago | parent | favorite | on: I was wrong about spreadsheets (2017) The thing that's missing from "Google Docs" is a decent collaborative outliner called "Google Trees", that does to "NLS" and "Frontier" what "Google Sheets" did to "VisiCalc" and "Excel". And I don't mean …

- **2019-10-06** · [`21170438`](https://news.ycombinator.com/item?id=21170438) · *Representing and Editing JSON with Spreadsheets (2018)*  
  `Aretha, Dave Winer, Frontier, ThinkTank, UserLand, Winer, outliner, outlining`  
  DonHopkins 43 days ago [-] One thing an outliner lets you do that you can't do with something like Wave or a tree structured discussion group is to arbitrarily rearrange the tree. You're right, you can represent tree-structured outlines in Word or Docs (or JSON in Excel or Sheets as I described …

- **2019-10-06** · [`21170436`](https://news.ycombinator.com/item?id=21170436) · *Representing and Editing JSON with Spreadsheets (2018)*  
  `Dave Winer, Frontier, Winer, outliner`  
  DonHopkins 44 days ago [-] I love the collaborative features of Google Docs and Google Sheets. The thing that's missing from "Google Docs" is a decent collaborative outliner called "Google Trees", that does to "NLS" and "Frontier" what "Google Sheets" did to "VisiCalc" and "Excel". And I don't …

- **2019-10-06** · [`21170434`](https://news.ycombinator.com/item?id=21170434) · *Representing and Editing JSON with Spreadsheets (2018)*  
  `Dave Winer, Frontier, Winer`  
  I wrote some stuff in previous HN discussions about outliners and spreadsheets, and also some stuff about Dave Winer's Frontier, which I'll quote and link to here:

- **2019-12-08** · [`21736782`](https://news.ycombinator.com/item?id=21736782) · *Learning to code vs. learning to automate*  
  `Frontier, UserLand, outliner`  
  There used to be Userland Frontier, which was actually earlier and better than AppleScript! >UserLand's first product release of April 1989 was UserLand IPC, a developer tool for interprocess communication that was intended to evolve into a cross-platform RPC tool. In January 1992 UserLand …

- **2020-01-29** · [`22176317`](https://news.ycombinator.com/item?id=22176317) · *Ted versus The Media Lab [video]*  
  `Dave Winer, Frontier, UserLand, Winer`  
  I recently read Ben Shneiderman's review of Ted Nelson's Computer Lib (1974) in his list of books that were key influences on his professional and personal life, and his criticism of Ted rings true. His criticisms are fair and well thought out, and I definitely agree with him in this case, both …

- **2020-02-09** · [`22282936`](https://news.ycombinator.com/item?id=22282936) · *HyperCard: What Could Have Been (2002)*  
  `Frontier, Radio UserLand, UserLand`  
  Apple's OpenDoc based browser, CyberDog, was also quite amazing and flexible, because it was completely component based and integrated with OpenDoc. But that plane never got off the ground, because Steve Jobs rightfully focused on saying "No" and "put a bullet in OpenDoc's head". >Cyberdog was an …

- **2021-02-21** · [`26217472`](https://news.ycombinator.com/item?id=26217472) · *Project Xanadu*  
  `Dave Winer, Frontier, UserLand, Winer`  
  I wrote about this on HN a few years ago, and Dave Winer's Userland Frontier discussion group a couple decades ago, after Xanadu released some open source code, which was actually the output of a Smalltalk=>C++ transpiler. (That code was actually from a team Autodesk, not directed by Ted Nelson -- …

- **2022-02-05** · [`30220932`](https://news.ycombinator.com/item?id=30220932) · *Spotify deletes 70 Joe Rogan episodes*  
  `Dave Winer, Winer`  
  What, and document all of RSS's embarrassing design flaws??! >The worst use of the <BLINK> tag ever was the discussion held in the early days of RSS about escaping HTML in titles, whose attention-grabbing title went something like this: "Hey, what happens when you put a <BLINK> tag in the …

- **2022-03-31** · [`30871497`](https://news.ycombinator.com/item?id=30871497) · *Excel 2.0 – Is there a better visual data model than a grid of cells?*  
  `Aretha, Dave Winer, Frontier, Manila, OPML, Radio UserLand, ThinkTank, UserLand, Winer, XML-RPC, outliner`  
  I posted this a few years ago, asking why there isn't a decent and flexible collaborative outliner like "Google Trees": The thing that's missing from "Google Docs" is a decent collaborative outliner called "Google Trees", that does to "NLS" and "Frontier" what "Google Sheets" did to "VisiCalc" and …

- **2022-11-10** · [`33541350`](https://news.ycombinator.com/item?id=33541350) · *Meta lays off 11,000 people*  
  `Dave Winer, Winer`  
  Plate of Shrimp: >I blame Eric Raymond and to a lesser extent Dave Winer for bringing this kind of schlock writing onto the Internet. Raymond is the original perpetrator of the "what is a hacker?" essay, in which you quickly begin to understand that a hacker is someone who resembles Eric Raymond. …

- **2022-12-24** · [`34117121`](https://news.ycombinator.com/item?id=34117121) · *RssCloud, WordPress. FeedLand, and Dave Winer*  
  `Dave Winer, Winer`  
  The worst use of the <BLINK> tag ever was the discussion held in the early days of RSS about escaping HTML in titles, whose attention-grabbing title went something like this: "Hey, what happens when you put a <BLINK> tag in the title???!!!" The content of that notorious discussion went on and off …

- **2023-04-23** · [`35674125`](https://news.ycombinator.com/item?id=35674125) · *JSON vs. XML with Douglas Crockford*  
  `Dave Winer, Frontier, Winer, outliner, scripting.com`  
  It's worth listening to, or at least reading the transcript, just for the Dave Winer burn. (And so much more!) >Adam: That was it. That was the creation of JSON, which everyone is using today. But back then, everyone rejected it. >In some ways it was a marketing problem. On one side, you had Doug, …

- **2023-07-01** · [`36544440`](https://news.ycombinator.com/item?id=36544440) · *Atom feed format was born 20 years ago*  
  `Dave Winer, Winer`  
  DonHopkins on May 11, 2014 | parent | context | favorite | on: The Unix Haters Handbook (1994) [pdf] [...] The worst use of the <BLINK> tag ever was the discussion held in the early days of RSS about escaping HTML in titles, whose attention-grabbing title went something like this: "Hey, what …

- **2023-07-01** · [`36544675`](https://news.ycombinator.com/item?id=36544675) · *Atom feed format was born 20 years ago*  
  `DaveNet`  
  I and another old mutual friend of Dave's were both on his pre-RSS DaveNet mailing list for a long time past when it stopped being interesting, and we would always joke about how we were both afraid to ask him to remove us from DaveNet, because whenever somebody else would ask to be removed, it …

- **2023-07-07** · [`36629380`](https://news.ycombinator.com/item?id=36629380) · *Show HN: OPML list of Hacker News Users Personal Blogs*  
  `Dave Winer, OPML, Winer`  
  Why do RSS feeds need to be imported/exported as anything other than RSS feeds? According to this thread, four out of five RSS apps on Linux Mint failed to import the OPML file, and the one that did was buggy: Maybe I'm thick, but it bewilders me that someone wouldn't simply use RSS or Atom …

- **2023-07-07** · [`36627453`](https://news.ycombinator.com/item?id=36627453) · *Show HN: OPML list of Hacker News Users Personal Blogs*  
  `Dave Winer, Frontier, Manila, OPML, Radio UserLand, UserLand, Winer, XML-RPC`  
  Then why not use RSS, or Atom, or CSV, or HTML, for that matter? That OPML "outline" has no tree structure at all, except for the single top level container item: <outline title="HN Personal Blogs" text="HN Personal Blogs"> What is the point of using OPML for a flat structure? Outlines are all …

- **2023-07-07** · [`36629566`](https://news.ycombinator.com/item?id=36629566) · *Show HN: OPML list of Hacker News Users Personal Blogs*  
  `OPML`  
  Apparently now RSS stands for "RSS Serves Structures" and OPML stands for "OPML Presents Mere Lists".

- **2023-07-07** · [`36627214`](https://news.ycombinator.com/item?id=36627214) · *Show HN: OPML list of Hacker News Users Personal Blogs*  
  `OPML`  
  OMFG somebody remembers OPML!

- **2024-03-14** · [`39709278`](https://news.ycombinator.com/item?id=39709278) · *Spreadsheets are all you need*  
  `Frontier, UserLand, outliner`  
  The "Visual" in "Visual Programming Language" is about the graphical, interactive method of creating and understanding programs, rather than merely the visibility of textual or graphical code. Spreadsheets typically show the entire formula of the selected cell at the top of the window, at the full …

- **2024-10-26** · [`41952842`](https://news.ycombinator.com/item?id=41952842) · *Company named "><SCRIPT SRC=HTTPS://MJT.XSS.HT> LTD" forced to change it (2020)*  
  `Dave Winer, Winer`  
  The worst use of the <BLINK> tag ever was the discussion held in the early days of RSS about escaping HTML in titles, whose attention-grabbing title went something like this: "Hey, what happens when you put a <BLINK> tag in the title???!!!" The content of that notorious discussion went on and off …

- **2025-08-29** · [`45062689`](https://news.ycombinator.com/item?id=45062689) · *RSS is awesome*  
  `Dave Winer, Winer`  
  And instead of "feeds", call them "holes". And instead "subscriptions", they're "heads up". Dave Winer's would be the biggest with the most!

- **2025-09-21** · [`45326354`](https://news.ycombinator.com/item?id=45326354) · *Review: Project Xanadu – The Internet That Might Have Been*  
  `Dave Winer, Frontier, UserLand, Winer`  
  DonHopkins on Jan 24, 2018 | parent | context | favorite | on: Ted Nelson on What Modern Programmers Can Learn fr... I think his biggest problem is that he refuses to collaborate with other people, or build on top of current technology. He's had a lot of great important inspirational ideas, but …

- **2026-05-29** · [`48320279`](https://news.ycombinator.com/item?id=48320279) · *Avoid Using "< [Cdata[ ]]>" in RSS*  
  `Dave Winer, Winer`  
  The worst use of the <BLINK> tag ever was the discussion held in the early days of RSS about escaping HTML in titles, whose attention-grabbing title went something like this: "Hey, what happens when you put a <BLINK> tag in the title???!!!" The content of that notorious discussion went on and off …

- **2026-07-23** · [`49022707`](https://news.ycombinator.com/item?id=49022707) · *Malleable computing, Emacs, and you*  
  `Aretha, Dave Winer, Frontier, Manila, OPML, Radio UserLand, ThinkTank, UserLand, Winer, XML-RPC, outliner, scripting.com`  
  Re CharlesW: OSA was an OS-level malleable-computing layer, on paper. Apple Events exposed scriptable objects; OSA let multiple scripting dialects share the same runtime. The gap was who actually shipped working product. Dave Winer's Frontier (UserTalk) is the piece these threads usually skip. …

- **2026-08-02** · [`49144561`](https://news.ycombinator.com/item?id=49144561) · *Atom is better than RSS, in ways that matter*  
  `Dave Winer, Scripting News, Winer`  
  I used to be on Dave Winer's scripting-news mailing list, and then somebody posted a request to be removed, so he removed them in a huff and then complained about how they hurt his feelings to the rest of the mailing list (not that they spammed the list, but that he was insulted they wanted off). …

- **2026-08-02** · [`49144462`](https://news.ycombinator.com/item?id=49144462) · *Atom is better than RSS, in ways that matter*  
  `Dave Winer, Winer`  
  Who remembers when everybody was syndicating all their favorite RSS feeds on their own blogs, and then some joker posted a blog entry to his own RSS feed with a title like "What happens when you put an unbalanced <BLINK> tag into the title?", and the ENTIRE BLOGOSPHERE started blinking? The …

## Outliners — no Winer mention  (16)

- **2018-11-20** · [`18496435`](https://news.ycombinator.com/item?id=18496435) · *Visual Programming – Why It’s a Bad Idea*  
  `outliner`  
  Years ago I developed a visual interface to an existing non-visual language, the multi threaded object oriented dialect of PostScript in the NeWS window system. Since PostScript is homoiconic, the data viewers and editors could also be applied to code! It didn't try to replace text based …

- **2019-01-06** · [`18837730`](https://news.ycombinator.com/item?id=18837730) · *Tree Style Tabs*  
  `outliner`  
  That's how I implemented tabbed windows in 1988 for the NeWS window system and UniPress Emacs (aka Gosling Emacs aka Evil Software Hoarder Emacs), which supported multiple windows on NeWS and X11 long before Gnu Emacs did. That seemed to me like the most obvious way to do it at the time, since …

- **2020-03-01** · [`22456683`](https://news.ycombinator.com/item?id=22456683) · *Sun's NeWS was a mistake, as are all toolkit-in-server windowing systems (2013)*  
  `outliner`  
  In this video of Eric Bier and his colleagues from Xerox PARC demonstrating Cedar, they discuss writing resolution independent applications, and the problem and approaches to matching the text and formatting displayed on the screen, with how it looks when printed: >Eric Bier Demonstrates Cedar. …

- **2020-03-28** · [`22708076`](https://news.ycombinator.com/item?id=22708076) · *Is there any code in Firefox (as of 2020) that comes from Netscape Navigator?*  
  `outliner`  
  NSAPI, the server based Netscape Server Application Programming Interface, is not to be confused with NPAPI, the browser based Netscape Plug-in Application Programming Interface. (I only say that because I just confused them, then realized my mistake.) NSAPI: NPAPI: FWIW, here's some feedback I …

- **2020-04-26** · [`22987470`](https://news.ycombinator.com/item?id=22987470) · *Maybe visual programming is the answer, maybe not*  
  `outlining`  
  That's right. It has to do with the dimensionality and topology of the language syntax, not just how it looks. C++ is not a visual programming language, no matter how much you colorize and pretty-print and fold it, because it's represented as a one-dimensional stream of characters, one after the …

- **2020-11-04** · [`24990829`](https://news.ycombinator.com/item?id=24990829) · *Dear ImGui – Bloat-free graphical user interface library for C++*  
  `outliner`  
  I agree. They work fine for simplistic interfaces with a few buttons, but what about more complex widgets, like plain/rich/code text editors, that have a lot of different callbacks and fire many different asynchronous events? Sure, a button function that returns a boolean can be used as a simple …

- **2021-04-19** · [`26860781`](https://news.ycombinator.com/item?id=26860781) · *PostScript Language Reference (1999) [pdf]*  
  `outliner`  
  PostScript can certainly handle resizable windows (or "responsive" rendering as the kids are calling it these days). See the heavily commented PizzaTool source code, which renders a color preview of your pizza in a resizable pizza shaped window (which you can spin) as well as faxing a hires black …

- **2021-05-16** · [`27174053`](https://news.ycombinator.com/item?id=27174053) · *Show HN: ThingsTwin – 3D House Plan Based UI for Smart Home*  
  `outlining`  
  In 2008, four years after I published it during the 2004 election, I discovered that some research scientists incuding Marc Davies at the University of Essex Digital Lifestyles Centre forked and cloned (or "hacked into") my open source "Dumbold Voting Machine for The Sims 1" virtual agitprop, and …

- **2021-06-05** · [`27404616`](https://news.ycombinator.com/item?id=27404616) · *Apple, Mozilla, Google, Microsoft form group to standardize browser plug-ins*  
  `outliner`  
  NSAPI was horrible in many ways from day one. FWIW, here's some feedback I wrote up and sent to Netscape about the original version of the Netscape 2.0b3 plug-in SDK (NPAPI), when I worked at Kaleida. This was from around 1995, when JavaScript was called LiveScript, before anything like …

- **2022-01-14** · [`29931338`](https://news.ycombinator.com/item?id=29931338) · *Revisiting why hyperlinks are blue*  
  `outlining`  
  Here's an even more interesting version of Vannevar Bush's 1945 essay "As We May Think", annotated by Douglas Englebart: The MIT/Brown Vannevar Bush Symposium >Influence on Doug Engelbart >Scanned image of Doug's copy of the article >Doug's copy of the article circa 1962 - check it out (courtesy …

- **2022-03-31** · [`30871555`](https://news.ycombinator.com/item?id=30871555) · *Excel 2.0 – Is there a better visual data model than a grid of cells?*  
  `outliner`  
  How about a spreadsheet that's also an outliner? Here's an article and HN discussion about "Representing and Editing JSON with Spreadsheets" that I posted a few years ago about shoe-horning JSON into spreadsheets so it was easier to edit and process. But ideally I'd prefer a collaborative …

- **2023-01-09** · [`34306017`](https://news.ycombinator.com/item?id=34306017) · *Alan Kay on web browsers, document viewers, Smalltalk, NeWS and HyperCard (2021)*  
  `outliner`  
  But HTML is for sissies, and the JavaScript debugger has come so far! ;) For the truly brave and principled, you should be able to disable the HTML view completely, and browse the web entirely through the JavaScript debugger console, network log, DOM and CSS editor, JavaScript sources, …

- **2023-09-10** · [`37454537`](https://news.ycombinator.com/item?id=37454537) · *A guy preserving the new history of PC games, one Linux port at a time*  
  `outlining`  
  You can be Pro-Native without being Anti-Wine. In 2001 I wrote: "Those irrational people who reject Wine for purely political reasons, are doing much more damage to Linux than Wine will ever do. They're trying to argue that trivial invisible implementation details matter so much to users, that …

- **2024-04-16** · [`40050697`](https://news.ycombinator.com/item?id=40050697) · *Descent 3 Source Code*  
  `outlining`  
  The Sims was like that too, and it's only recently that anyone's tried to launch a full-blown competitor, Life By You from Paradox, who also launched a full blown SimCity competitor, Cities: Skylines. It's run by Rob Humble, who managed The Sims 2 and 3. Myst was the top selling game of all time …

- **2025-07-23** · [`44661955`](https://news.ycombinator.com/item?id=44661955) · *When Is WebAssembly Going to Get DOM Support?*  
  `outliner`  
  That's because Java used the old piece-of-shit NPAPI (Netscape Plugin Application Programming Interface) from 1995, first released in the NetScape 2.0b3 Plug-in SDK: Problems Found with the NetScape Plug-in API. By Don Hopkins, Kaleida Labs: More about Netscape's fleeting obsession with Java and …

- **2025-11-19** · [`45981599`](https://news.ycombinator.com/item?id=45981599) · *Cloudflare Global Network experiencing issues*  
  `outlining`  
  Are you actually so mind-numbingly ignorant that you think Rebecca Heineman had a brother named Bill, that you would rudely and incorrectly try to correct people who knew her story well, during a memorial discussion of her life and death? Or were you purposefully going out of your way to …

## Incidental keyword matches  (16)

- **2015-03-26** · [`9269368`](https://news.ycombinator.com/item?id=9269368) · *NSA is monitoring key Internet routers (1996)*  
  `Frontier`  
  Remember the Clipper chip? It was announced in 1993 and by 1996 was entirely defunct. EFF and Wired Magazine published a lot of anti-clipper backlash during that time. >Backlash >Organizations such as the Electronic Privacy Information Center and the Electronic Frontier Foundation challenged the …

- **2018-05-19** · [`17106103`](https://news.ycombinator.com/item?id=17106103) · *Pie Menus: A 30-Year Retrospective: Take a Look and Feel Free*  
  `Frontier`  
  Good questions! It's a very difficult problem, and I don't know of a universal solution. I haven't been very happy with any of the higher level multitouch tracking API's that I've used. I usually just end up writing a lot of ugly Rube Goldbergesque spaghetti event handling code with lots of global …

- **2019-05-15** · [`19916938`](https://news.ycombinator.com/item?id=19916938) · *Unlimited Google Drive storage by splitting binary files into base64*  
  `Frontier`  
  In 1998, the EFF and John Gilmore published the book about "Deep Crack" called "Cracking DES: Secrets of Encryption Research, Wiretap Politics, and Chip Design". But at the time, it would have been illegal to publish the code on a web site, or include a CDROM with the book publishing the "Deep …

- **2019-08-12** · [`20672856`](https://news.ycombinator.com/item?id=20672856) · *US Navy will replace touchscreen with mechanical controls on its destroyers*  
  `Frontier`  
  In Michael Naimark's series of articles about "VR and AR Fundamentals" [1], the chapter on "Other Senses (Touch, Smell, Taste, Mind)" [2] discusses haptic feedback, and even mentions Hiroo Iwata's delicious "Food Simulator" [3]. [1] VR and AR Fundamentals: [2] Other Senses (Touch, Smell, Taste, …

- **2019-08-28** · [`20817703`](https://news.ycombinator.com/item?id=20817703) · *Stop Calling It “Military-Grade Encryption”*  
  `Frontier`  
  Actually, that's what already happened. And now they're trying to do it again. Posted on July 24, 2019 by Bruce Schneier on Security> Yesterday, Attorney General William Barr gave a major speech on encryption policy -- what is commonly known as "going dark." Speaking at Fordham University in New …

- **2020-03-06** · [`22502125`](https://news.ycombinator.com/item?id=22502125) · *The X-Windows Disaster (1994)*  
  `Frontier`  
  Bill Joy referred to X-Windows as "Rasterop on Wheels". I gave a NeWS/Pie Menus/HyperTies/Emacs demo to Steve Jobs once, on the trade show floor at the Educom conference, right after he finally released the NeXT Machine, in November of 1988. Sun was letting me demo NeWS and the stuff we were …

- **2020-10-29** · [`24926397`](https://news.ycombinator.com/item?id=24926397) · *The Fall of Silicon Valley*  
  `Frontier`  
  That Sun commie hippie hackers smoked dope and walked around barefoot and didn't cut their hair? Sun's Solaris for hippies to arrive next week. John Gage was on Richard Nixon's Enemies List. California inspired: from flower power to Silicon Valley. How 1960s Bay Area radicalism helped shape the …

- **2021-11-13** · [`29210302`](https://news.ycombinator.com/item?id=29210302) · *Open Source Vibrotactile Haptics Platform for On-Body Applications*  
  `Frontier`  
  Relax and tighten, Kyle! Relax and Tighten — A Haptics-based Approach to Simulate Sphincter Tone Assessment, presented at Asia Haptics 2016 ( might be considered NSFW by some, or work related by others): DiRECT: we put the "finger" into "digital"! Good golly, they've even gamified it: >+ Public …

- **2022-10-06** · [`33108544`](https://news.ycombinator.com/item?id=33108544) · *Recording the Grateful Dead: The Culture of Tapers*  
  `Frontier`  
  Wow cool! That is indeed the highest praise, though easily misinterpreted out of context. I saw a bunch of Flying Other Brothers concerts, who started at an Electronic Frontier Foundation (EFF) benefit at The Fillmore Auditorium in 1997, and occasionally backed Bob Weir and Mickey Hart!

- **2023-11-30** · [`38474858`](https://news.ycombinator.com/item?id=38474858) · *The Unix-Haters Handbook (1994) [pdf]*  
  `Frontier`  
  The Unix-Haters Handbook was published in 1994, two years before the Open Group was founded in 1996, three years before they took over the X-Window system in 1997, five years before the formation of X.org, and ten years after X-Windows was released in 1984. XFree86 was not very widely used in …

- **2024-02-08** · [`39300605`](https://news.ycombinator.com/item?id=39300605) · *John Walker, founder of Autodesk, has died*  
  `Frontier`  
  I really love and was deeply inspired by the great work that John Walker did with Rudy Rucker on cellular automata, starting with Autodesk's product CelLab, then James Gleick's CHAOS -- The Software, Rudy's Artificial Life Lab, John's Home Planet, then later the JavaScript version WebCA, and lots …

- **2024-12-22** · [`42487216`](https://news.ycombinator.com/item?id=42487216) · *Classic Computer Magazines*  
  `Frontier`  
  Anybody know where to find an archive of Morph's Outpost on the Digital Frontier?

- **2025-07-02** · [`44440930`](https://news.ycombinator.com/item?id=44440930) · *Why Do Swallows Fly to the Korean DMZ?*  
  `Frontier`  
  何為吞蠅 蠅永同音一 化驚腸內舞 雙義笑開顏 歸路際無定 蠅永同音一 What is this “swallowing flies”? “Fly” and “shadow” share the same voice, always. In a flash it’s startled -- inside it dances like starlight. The double pun draws us to smile. Homeward the light finds no single course. “Fly” and “shadow” -- one and the same …

- **2025-10-25** · [`45706551`](https://news.ycombinator.com/item?id=45706551) · *Rock Tumbler Instructions*  
  `Frontier`  
  You can train the smart ones [1], and even wirelessly remotely control them with a mobile app [2], as long as you restrict yourself to commanding them to do things they were going to do anyway, just like cats. Kudos to the Stoned Republicans of the High Frontier Panel and The Heritage Foundation …

- **2026-08-22** · [`49399891`](https://news.ycombinator.com/item?id=49399891) · *Stop Making TUIs*  
  `Frontier`  
  In the age of graphical user interfaces, direct manipulation, info visualization, WebGPU in the browser, and frontier AI, it seems ridiculous to have a VT100 escape code interpreter between you and your LLM. Like Brooke Shields, I'd rather nothing comes between me and my LLMs.

- **2026-09-03** · [`49546640`](https://news.ycombinator.com/item?id=49546640) · *Higher Multipoles of the Cow*  
  `Frontier`  
  Berkeley has been on the frontier of cow detection and tracking for decades.
