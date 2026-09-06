# Don's COM synopsis, HN, 17 November 2016

The primary source behind this repo's **Selfish COM** line. Everything in
[DIRECTORY-AS-IUNKNOWN.md](../../DIRECTORY-AS-IUNKNOWN.md),
[kernel/DIRECTORY-AS-OBJECT.md](../../../kernel/DIRECTORY-AS-OBJECT.md) and
[kernel/SELFISH-COM-IMPLEMENTATION.md](../../../kernel/SELFISH-COM-IMPLEMENTATION.md) descends from the
reading of COM recorded here, so the text is archived rather than summarized.

| | |
|---|---|
| Author | `DonHopkins` |
| Item | [12975257](https://news.ycombinator.com/item?id=12975257) |
| Date | 2016-11-17 07:42:13 UTC |
| Points | 14 |
| Story | [Visual Studio for Mac Preview](https://news.ycombinator.com/item?id=12968830) |
| Parent | [12969323](https://news.ycombinator.com/item?id=12969323) by `mizzao` |

**The question it answers, verbatim and complete:**

> Can someone link to a synopsis describing what "COM" is? It's hard to search for. (e.g. microsoft
> com visual studio)

Which is why "Glad you asked!" opens the reply, and why the reply is the length it is. Note what the
question demonstrates about its own subject — see [the naming footnote](#the-name-defeated-two-attempts-to-fix-it)
below.

Replies: `pjmlp` objected that COM is not merely historical ("I guess you haven't looked into how
Windows 8, 8.x, 10 and UWP applications work"), calling the summary great regardless; Don clarified
that "essentially" meant *actually*; `72deluxe`: "Really really great summary."

---

## Verbatim

Glad you asked! One of my favorite topics. ;)

COM is essentially a formal way of using C++ vtables [1] from C and other languages, so you can create and consume components in any language, and call back and forth between them. It's a way of expressing a rational subset of how C++ classes work and format in memory, in a way that can be implemented in other languages.

It was the outcome of the C / C++ / Visual Basic language wars at Microsoft.

The original 16 bit version of Visual Basic version 1 through 3 had a plug-in extension mechanism called VBX -- Visual Basic Extensions [2].

They were extremely popular and became a victim of their own success, after a whole industry grew up around them, and people started using them for all kinds of things they weren't intended for, and wanted to use them from other languages and frameworks like Borland. Microsoft had to do something about that to mitigate the success disaster of VBX, so they invented COM.

At the time, Microsoft was transitioning from Win16 to Win32, so they came up with the 32 bit COM definition, also known as OCX's, or OLE Controls, which they later called ActiveX, because COM was so hard to search for, and they wanted to take the spotlight away from Java with a new buzzword.

So they brewed up a bunch of ugly C macrology that enabled C programmers (or Visual Studio wizards) to define COM interfaces in header and implementation files that just happened to lay out memory in the exact same way as vtables of C++ pure virtual classes.

While C++ programs would use other ugly macros to declare actual honest-for-god C++ classes to implement COM interfaces.

And Visual Basic programmers would ... do whatever it was that Visual Basic programmers did.

COM's IUnknown::QueryInterface [4] method is essentially like C++'s dynamic_cast [5]. But it also adds some object aggregation features [6] that let you compose multiple sub-objects together by aggregation instead of using monolithic inheritance. You could implement "tear off interfaces" [7] that lazily create aggregated sub-objects on demand, useful for implementing callback interfaces.

MFC (Microsoft Foundation Classes) is a set of C++ wrappers around the lower level Win32 interfaces, plus a huge framework for implementing GUI widgets and dialogs on top of Win32, and for wrapping rube-goldbergesque OLE Automation interfaces around C++ classes. For some time MFC was the primary way of implementing COM interfaces in C++, but it was infamous for being horribly complex, with all its ugly macros, Hungarian notation, and bizarre programming conventions.

Later on Microsoft came out with the C++-only ActiveX Template Library (ATL) [8], which, although it was still necessarily quite ugly, was a more elegant and powerful way of implementing COM components in C++, didn't have the baggage of supporting C, and let you implement COM/OLE/ActiveX components without the hideous MFC framework. ATL was popular for implementing all kinds of Internet Explorer plug-ins.

OLE was actually a layer of COM interfaces and MIDL (Microsoft Interface Definition Language) on top of COM, which adds the IDispatch interface for dynamically querying and invoking methods and properties at runtime, and variant types [9]: tagged unions for representing polymorphic data (i.e. VB data types) and passing parameters to OLE IDispatch functions.

OLE was the glue necessary for integrating COM components into the Visual Basic runtime, so it directly supported Visual Basic data types, calling conventions and semantics like indexed properties.

OLE also provided an interface definition language (ILD) you could compile into binary type libraries, use to generate boilerplate C and C++ interfaces, and OLE also had COM interfaces and structures for providing those type libraries at runtime. It also had a lot of persistence, runtime reflection, and user-interface related stuff for plugging components and dialogs together in windows, providing property sheets, editing and configuring controls, etc.

MIDL supported defining components with "dual interfaces" [10]: both an OLE IDispatch interfaces taking variant type parameters, and also more efficient lower level COM interface taking primitive types. Runtimes like Visual Basic knew how to integrate dual interfaces and could bind to the more efficient underlying COM interfaces, instead of going through the slower generic dynamic IDispatch interfaces.

IDL also described the intricacies of DCOM [11] interfaces (for in-process and networked remote procedure calls), parameter marshalling [12], and all kinds of other bizarre stuff. DCOM is where COM went off the deep end.

At its core, COM was essentially a very simple and ingenious idea that elegantly solved some real world problems, but it eventually evolved into something extremely complex that attempted to solve many other unrelated problems, and which required a massive amount of tooling, and that depended on Microsoft's Visual Studio and Win32 environment.

Microsoft actually ported ActiveX to the Mac using ATL and Metrowerks Code Warrior, in order to implement Microsoft Internet Explorer for Mac [13] (which was actually the best web browser on the Mac at the time, by far). But not a lot of third parties (except for me and a few other crazy people) ever used ActiveX on the Mac.

However it did become quite fashionable for other organizations to create portable COM knock-offs to solve some (hopefully fewer) of the same problems, but which were incompatible with Microsoft's tooling and COM itself (which kind of missed the main points of COM, but hey).

For example, Macromedia came up with MOA (Macromedia Open Architecture) [13], their COM-like plug-in extension mechanism for Director and other products.

And Mozilla came up with XP/COM [14], for implementing components in Mozilla/Firefox/XULRunner/etc, enabling programmers to implement and consume XP/COM components in C++ or JavaScript. Of course it has its own IDL and tooling, and suffers from many of the same problems that COM did.

Mozilla didn't go nearly as far down the rabbit hole as Microsoft did, and later backtracked in their valiant "deCOMification" aka "deCOMtamination" and "outparamdelling" efforts [15].

At this point in history, I think it's best to skip the "component technology" middleman and integrate extensions directly into the JavaScript engine itself. Which brings us back to the sub-topic of VSCode!

[1] Virtual Method Table: https://en.wikipedia.org/wiki/Virtual_method_table

[2] VBX: https://en.wikipedia.org/wiki/Visual_Basic_Extension

[3] Variant Type: https://en.wikipedia.org/wiki/Variant_type

[4] IUnknown::QueryInterface: https://msdn.microsoft.com/en-us/library/windows/desktop/ms6...

[5] dynamic_cast: https://msdn.microsoft.com/en-us/library/windows/desktop/ff4...

[6] Aggregation: https://msdn.microsoft.com/en-us/library/windows/desktop/ms6...

[7] Tear Off Interface: http://www.codeguru.com/cpp/com-tech/atl/performance/article...

[8] ActiveX Template Library: http://www.drdobbs.com/windows/the-activex-template-library/...

[9] Variant Types: https://en.wikipedia.org/wiki/Variant_type

[11] Distributed COM: https://en.wikipedia.org/wiki/Distributed_Component_Object_M...

[12] Marshalling: https://en.wikipedia.org/wiki/Marshalling_(computer_science)

[13] Macromedia Open Architecture (MOA): https://www.adobe.com/support/xtras/info/moa.html

[14] XP/COM: https://developer.mozilla.org/en-US/docs/Mozilla/Tech/XPCOM

[15] deCOMtamination: https://wiki.mozilla.org/Gecko:DeCOMtamination http://taras.glek.net/blog/categories/decomtamination/ https://blog.mozilla.org/tglek/category/decomtamination/

---

## Transcription notes

The footnote numbering has three defects, preserved above as written:

- **[10] is cited but never defined.** The body attaches it to "dual interfaces," the single most
  load-bearing reference for this repo, and the list skips from [9] to [11].
- **[13] is cited twice for different things** — Internet Explorer for Mac and Macromedia MOA — and
  the list defines only MOA. There is no citation for IE:mac.
- **[3] is defined but never cited.** It is a duplicate of [9], both pointing at the same Wikipedia
  variant-type page.

Also: "an interface definition language (ILD)" is a keying transposition of **IDL**, and
"honest-for-god" is Don's spelling of *honest-to-God*, left alone. The MSDN and Dr. Dobb's URLs are
truncated by HN's display with a trailing ellipsis, and most are dead now regardless — MSDN moved to
`learn.microsoft.com` and Dr. Dobb's stopped publishing in 2014. The live equivalents are collected in
[the mechanism registry](../../../skills/schema/schemas/mechanisms/com-xpcom/README.md).

## The name defeated two attempts to fix it

Microsoft renamed COM to ActiveX partly "because COM was so hard to search for." Twenty years later a
reader on Hacker News opens a thread by asking what COM is, **because it is hard to search for**, and
gets pointed at the rename. The rename did not take, and the question is a demonstration of its own
subject.

Don hit the same wall again in September 2026, trying to find a multiplayer browser toy:
"cursor is hard to search for since it is so overloaded." Same failure mode, and it is the argument
for the repo's naming discipline from the retrieval side: a name that cannot be searched for cannot be
found, so the thing needs a **handle you can say out loud and get back** — which is what
[self-naming text](../../webtop/hyperties/LINK-RESOLUTION.md) buys, and what
[GUID-NAMING](../HUMANSPLAINING.md) forbids the opposite of. Three letters, English word, ambiguous:
unfindable. This is not an aesthetic complaint, it is a broken index.

## What this repo takes from it

Pointers rather than a rehash, since each is developed where it belongs:

| From the post | Where it lands |
|---|---|
| `QueryInterface` ≈ `dynamic_cast`, aggregation over monolithic inheritance, tear-off interfaces | [DIRECTORY-AS-IUNKNOWN.md § COM/OLE Background](../../DIRECTORY-AS-IUNKNOWN.md#comole-background) |
| **Dual interfaces**: one component, a fast typed path and a slow dynamic path, runtime binds the fast one when it can | [DIRECTORY-AS-IUNKNOWN.md § Dual interfaces](../../DIRECTORY-AS-IUNKNOWN.md#dual-interfaces-are-the-compiler-thesis-with-a-vendor-receipt) |
| VBX success disaster → COM → "DCOM is where COM went off the deep end" | [DIRECTORY-AS-IUNKNOWN.md § The overshoot arc](../../DIRECTORY-AS-IUNKNOWN.md#the-overshoot-arc-is-the-design-budget) |
| "Skip the component technology middleman and integrate extensions directly into the JavaScript engine itself" | [SELFISH-COM-IMPLEMENTATION.md § Why JavaScript](../../../kernel/SELFISH-COM-IMPLEMENTATION.md#why-javascript-not-wasm) |
| "Required a massive amount of tooling, and depended on Visual Studio and Win32" | [DIRECTORY-AS-OBJECT.md § What We Skip](../../../kernel/DIRECTORY-AS-OBJECT.md#what-we-skip) |
| Type libraries: compiled interface descriptions, served at runtime for reflection | `CARD.yml` and `GLANCE.yml`, via [VISUAL-PROGRAMMING-LINEAGE.md](../../VISUAL-PROGRAMMING-LINEAGE.md) |

The four later posts on the same subject — COM vs SOM (2019), IFC vs Bongo (2019), Firefox XPCOM
(2020), WebAssembly components (2021) — are shorter and add the SOM contrast and the Wasm forward
look. This one is the fullest treatment.

↑ [object-system](../README.md) · [DIRECTORY-AS-IUNKNOWN.md](../../DIRECTORY-AS-IUNKNOWN.md) · [mechanism registry](../../../skills/schema/schemas/mechanisms/com-xpcom/README.md)
