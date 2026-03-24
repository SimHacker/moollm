# COM / XPCOM (schemapedia: `com-xpcom`)

**component_interop family.** **Binary** component models: Microsoft **COM** (interface layout, `IUnknown`, `QueryInterface`, type libraries, OLE/ActiveX layers) and Mozilla **XPCOM** (XP/COM) for Gecko—IDL-flavored, language-mixed, long-lived. This registry slot is for **orientation and citations**, not wire-format validation ([json-schema](../json-schema/README.md) is a different layer).

## Why it matters here

Same ecosystem that shipped **Win32**, **IE**, and **Gecko** also shipped **component middleware** that shaped how large codebases factored APIs. **Mozilla later rolled much of it back** under names like **decomification**, **decomtamination**, and **outparamdelling**—useful precedent when designing *any* plugin or embedding surface (including “give the scripting language a real native API” vs “standardize on vtables everywhere”).

## What’s distinctive

- **COM**: binary interface contract; hard to Google by name; **ActiveX** is not identical to “all COM” ([HN](https://news.ycombinator.com/item?id=20266627) thread on COM vs SOM and naming).
- **XPCOM**: Mozilla’s parallel; **XPIDL** and bindings; substantial **removal** effort documented on the wiki and in bugs.
- **Not** interchange JSON: API shapes may be JSON *today*, but COM/XPCOM are **memory/layout + IDL** stories.

## MOOLLM: Selfish COM (directory tree as object graph)

The kernel documents **Selfish COM**: directories as objects, files as interface facets, `QueryInterface` as path lookup (no vtables), plus Self-style `parents:` inheritance. Start with [DIRECTORY-AS-OBJECT.md](../../../../../kernel/DIRECTORY-AS-OBJECT.md); protocol detail in [SELFISH-COM-IMPLEMENTATION.md](../../../../../kernel/SELFISH-COM-IMPLEMENTATION.md).

## Python on Windows (COM / OLE)

The usual stack is **pywin32** (Mark Hammond lineage, maintained on GitHub): **`win32com.client`** for `Dispatch` (late-bound automation), **`pythoncom`**, `gencache` / **makepy** for early-bound wrappers from type libraries, plus Win32 APIs alongside COM. It is the practical way to script **Office**, **WMI**, shell COM objects, and many other `ProgID`-style servers from Python—**Windows-only**.

| Resource | URL |
|----------|-----|
| **PyPI — pywin32** | [pypi.org/project/pywin32](https://pypi.org/project/pywin32/) |
| **Source — mhammond/pywin32** | [github.com/mhammond/pywin32](https://github.com/mhammond/pywin32) |

**comtypes** ([PyPI](https://pypi.org/project/comtypes/)) is a **pure-Python** COM layer often used when you want typelib-centric codegen or a different binding style; same problem domain, different tradeoffs vs `win32com`.

## Anchor thread (Firefox 2020 + deCOM vocabulary)

Primary link requested:

| Resource | URL |
|----------|-----|
| **HN — “Is there any code in Firefox (as of 2020) that com…”** (DonHopkins on XP/COM, decomification, pointers) | [news.ycombinator.com/item?id=22708241](https://news.ycombinator.com/item?id=22708241) |

Related **Hacker News** and **Mozilla** primary sources (same conversation cluster as above):

| Resource | URL |
|----------|-----|
| HN — COM vs SOM, Don Box, IBM SOM article, **decomification / decomtamination**, WebAssembly aside | [news.ycombinator.com/item?id=20266627](https://news.ycombinator.com/item?id=20266627) |
| HN — **“What is COM?”** long synopsis (VBX → COM → OCX → ActiveX; **XP/COM**; deCOMtamination links) | [news.ycombinator.com/item?id=12975257](https://news.ycombinator.com/item?id=12975257) |
| HN — **DeCOMification** discussion | [news.ycombinator.com/item?id=12968830](https://news.ycombinator.com/item?id=12968830) |
| Mozilla wiki — **Gecko:DeCOMtamination** | [wiki.mozilla.org/Gecko:DeCOMtamination](https://wiki.mozilla.org/Gecko:DeCOMtamination) |
| Taras Glek — **decomtamination** category | [taras.glek.net/blog/categories/decomtamination/](http://taras.glek.net/blog/categories/decomtamination/) |
| Mozilla blog (Taras Glek) — **decomtamination** | [blog.mozilla.org/tglek/category/decomtamination/](https://blog.mozilla.org/tglek/category/decomtamination/) |
| Bugzilla — **outparamdelling** example | [bugzilla.mozilla.org/show_bug.cgi?id=455943](https://bugzilla.mozilla.org/show_bug.cgi?id=455943) |

## Encyclopedic / specs / books

| Kind | URL |
|------|-----|
| Wikipedia — **Component Object Model** | [en.wikipedia.org/wiki/Component_Object_Model](https://en.wikipedia.org/wiki/Component_Object_Model) |
| Wikipedia — **XPCOM** | [en.wikipedia.org/wiki/XPCOM](https://en.wikipedia.org/wiki/XPCOM) |
| Wikipedia — **IBM System Object Model** (contrast with COM) | [en.wikipedia.org/wiki/IBM_System_Object_Model](https://en.wikipedia.org/wiki/IBM_System_Object_Model) |
| Microsoft Learn — **COM** portal | [learn.microsoft.com/en-us/windows/win32/com/component-object-model--com--portal](https://learn.microsoft.com/en-us/windows/win32/com/component-object-model--com--portal) |
| Don Box — *Essential COM* (book) | [archive.org/details/essentialcom00boxd](https://archive.org/details/essentialcom00boxd) |
| Don Box vs IBM — **COM vs SOM** (archive.org capture) | [web.archive.org/web/19990127184653/http://www.develop.com/dbox/COM_vs_SOM_Summ.htm](https://web.archive.org/web/19990127184653/http://www.develop.com/dbox/COM_vs_SOM_Summ.htm) |

## Historical notes (1996) — Don Hopkins pluggers

| Topic | URL |
|-------|-----|
| **COM** | [donhopkins.com/home/interval/pluggers/com.html](https://donhopkins.com/home/interval/pluggers/com.html) |
| **OLE** | [donhopkins.com/home/interval/pluggers/ole.html](https://donhopkins.com/home/interval/pluggers/ole.html) |
| **OLE Controls** | [donhopkins.com/home/interval/pluggers/olecontrols.html](https://donhopkins.com/home/interval/pluggers/olecontrols.html) |
| **ActiveX** | [donhopkins.com/home/interval/pluggers/activex.html](https://donhopkins.com/home/interval/pluggers/activex.html) |
| **Win32** (index) | [donhopkins.com/home/interval/pluggers/win32.html](https://donhopkins.com/home/interval/pluggers/win32.html) |

## Interacts with

| Mechanism | Relationship |
|-----------|----------------|
| [shell-orchestration](../shell-orchestration/README.md) | Different era, same “glue automation” problem space on Windows; COM is not shell. |
| [json-schema](../json-schema/README.md) | Modern HTTP/tool schemas vs binary IDL-era contracts—meet only at application policy. |

## In-repo

- Profile: [`MECHANISM.yml`](./MECHANISM.yml)
- Parent: [`../../../SKILL.md`](../../../SKILL.md)
