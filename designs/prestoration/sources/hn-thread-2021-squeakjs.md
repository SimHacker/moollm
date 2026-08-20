# The 2021 Hacker News Thread — Full Primary Source

The complete exchange in which Vanessa Freudenberg publicly asked not to be
deadnamed in citations. Story: [SqueakJS – A Squeak VM in JavaScript
(squeak.js.org)](https://news.ycombinator.com/item?id=29018465), October 27,
2021. Comment texts retrieved verbatim from the HN Algolia API
(`hn.algolia.com/api/v1/items/<id>`) on 2026-07-20; formatting flattened from
HTML, content unaltered.

**Link redirects (2026-07-20):** Dead URLs in verbatim quotes appear in backticks so they
do not render as broken links. **↪ Redirect** notes after affected comments point to working
copies. Full mapping: [sources/README.md — Broken link redirects](README.md#broken-link-redirects-hn-preservation).

**Nested quote attributions (2026-07-20):** **↪ Nested quotes** tables after affected
comments map embedded passages to [memorial PDF](Freudenberg-2014-SqueakJS-memorial-edition.pdf)
pages or the [Ingalls Zoo corrected PDF](Ingalls-2020-Evolution-of-Smalltalk-Zoo-corrected.pdf).

The chain of parentage, verified from the API:

| Comment | Author | Date | Parent |
|---------|--------|------|--------|
| [29019992](https://news.ycombinator.com/item?id=29019992) | DonHopkins | 2021-10-27 | story 29018465 |
| [29020468](https://news.ycombinator.com/item?id=29020468) | DonHopkins | 2021-10-27 | 29019992 |
| [29125515](https://news.ycombinator.com/item?id=29125515) | codefrau (Vanessa) | 2021-11-05 | 29020468 |

Worth noticing before reading: in the first comment, nine days *before*
Vanessa's reply, Don already wrote "**Vanessa** Freudenberg elegantly and
efficiently created a hybrid Smalltalk garbage collector" — her correct name,
in a comment whose links and quotations all still said "Bert." The thread
contains, in miniature, the exact gap the
[memorial edition](README.md) closes: the community had updated; the version
of record had not.

---

## 1. DonHopkins, 2021-10-27 — [29019992](https://news.ycombinator.com/item?id=29019992)

> One thing that's amazing about SqueakJS (and one reason this VM inside
> another VM runs so fast) is the way Vanessa Freudenberg elegantly and
> efficiently created a hybrid Smalltalk garbage collector that works with
> the JavaScript garbage collector.
>
> SqueakJS: A Modern and Practical Smalltalk That Runs in Any Browser
>
> `http://www.freudenbergs.de/bert/publications/Freudenberg-2014-SqueakJS.pdf`
>
> >The fact that SqueakJS represents Squeak objects as plain JavaScript
> objects and integrates with the JavaScript garbage collection (GC) allows
> existing JavaScript code to interact with Squeak objects. This has proven
> useful during development as we could re-use existing JavaScript tools to
> inspect and manipulate Squeak objects as they appear in the VM. This means
> that SqueakJS is not only a "Squeak in the browser", but also that it
> provides practical support for using Smalltalk in a JavaScript environment.
>
> >[...] a hybrid garbage collection scheme to allow Squeak object
> enumeration without a dedicated object table, while delegating as much work
> as possible to the JavaScript GC, [...]
>
> >2.3 Cleaning up Garbage
>
> >Many core functions in Squeak depend on the ability to enumerate objects
> of a specific class using the firstInstance and nextInstance primitive
> methods. In Squeak, this is easily implemented since all objects are
> contiguous in memory, so one can simply scan from the beginning and return
> the next available instance. This is not possible in a hosted
> implementation where the host does not provide enumeration, as is the case
> for Java and JavaScript. Potato used a weak-key object table to keep track
> of objects to enumerate them. Other implementations, like the R/SqueakVM,
> use the host garbage collector to trigger a full GC and yield all objects
> of a certain type. These are then temporarily kept in a list for
> enumeration. In JavaScript, neither weak references, nor access to the GC
> is generally available, so neither option was possible for SqueakJS.
> Instead, we designed a hybrid GC scheme that provides enumeration while not
> requiring weak pointer support, and still retaining the benefit of the
> native host GC.
>
> >SqueakJS manages objects in an old and new space, akin to a semi-space GC.
> When an image is loaded, all objects are created in the old space. Because
> an image is just a snapshot of the object memory when it was saved, all
> objects are consecutive in the image. When we convert them into JavaScript
> objects, we create a linked list of all objects. This means, that as long
> as an object is in the SqueakJS old-space, it cannot be garbage collected
> by the JavaScript VM. New objects are created in a virtual new space.
> However, this space does not really exist for the SqueakJS VM, because it
> simply consists of Squeak objects that are not part of the old-space linked
> list. New objects that are dereferenced are simply collected by the
> JavaScript GC.
>
> >When full GC is triggered in SqueakJS (for example because the
> nextInstance primitive has been called on an object that does not have a
> next link) a two-phase collection is started. In the first pass, any new
> objects that are referenced from surviving objects are added to the end of
> the linked list, and thus become part of the old space. In a second pass,
> any objects that are already in the linked list, but were not referenced
> from surviving objects are removed from the list, and thus become eligible
> for ordinary JavaScript GC. Note also, that we append objects to the old
> list in the order of their creation, simply by ordering them by their
> object identifiers (IDs). In Squeak, these are the memory offsets of the
> object. To be able to save images that can again be opened with the
> standard Squeak VM, we generate object IDs that correspond to the offset
> the object would have in an image. This way, we can serialize our old
> object space and thus save binary compatible Squeak images from SqueakJS.
>
> >To implement Squeak's weak references, a similar scheme can be employed:
> any weak container is simply added to a special list of root objects that
> do not let their references survive. If, during a full GC, a Squeak object
> is found to be only referenced from one of those weak roots, that reference
> is removed, and the Squeak object is again garbage collected by the
> JavaScript GC.

**↪ Redirect (2026-07-20):** Don's paper link (`freudenbergs.de/bert/...`) no longer
resolves. **Read the SqueakJS paper here instead:**

- **[Memorial edition](Freudenberg-2014-SqueakJS-memorial-edition.pdf)**
- **[Original as published](Freudenberg-2014-SqueakJS-original.pdf)**
- [Wayback snapshot, 2025-01-19](https://web.archive.org/web/20250119071632/https://freudenbergs.de/vanessa/publications/Freudenberg-2014-SqueakJS.pdf)

**↪ Nested quotes (2026-07-20):** Don [29019992](https://news.ycombinator.com/item?id=29019992)
opens with his own praise, then embeds long passages from **Vanessa Freudenberg et al.**,
*SqueakJS* (DLS 2014):

| Nested passage in Don's comment | Location in our cache |
|--------------------------------|------------------------|
| "The fact that SqueakJS represents Squeak objects as plain JavaScript objects…" (full paragraph) | §1 introduction, [memorial p. 2](Freudenberg-2014-SqueakJS-memorial-edition.pdf#page=2) |
| "[...] a hybrid garbage collection scheme…" | Contributions list, [memorial p. 2](Freudenberg-2014-SqueakJS-memorial-edition.pdf#page=2) |
| "2.3 Cleaning up Garbage" through weak-reference paragraph | §2.3 *Cleaning up Garbage*, [memorial p. 3](Freudenberg-2014-SqueakJS-memorial-edition.pdf#page=3) |

## 2. DonHopkins, 2021-10-27 — [29020468](https://news.ycombinator.com/item?id=29020468)

*(The quoted passage is Appendix A.5 of the **original** HOPL IV edition of Dan
Ingalls's paper, reproduced verbatim — which is why it says "Bert"
throughout. This is the comment Vanessa replied to.)*

> Also:
>
> The Evolution of Smalltalk: From Smalltalk-72 through Squeak.
> DANIEL INGALLS, Independent Consultant, USA
>
> `http://worrydream.com/refs/Ingalls%20-%20The%20Evolution%20of%20Smalltalk.pdf`
>
> >A.5 Squeak
>
> >Although Squeak is still available for most computers, SqueakJS has become
> the easiest way to run Squeak for most users. It runs in just about any web
> browser, which helps in schools that do not allow the installation of
> non-standard software.
>
> >The germ of the SqueakJS project began not long after I was hired at Sun
> Microsystems. I felt I should learn Java; casting about for a suitable
> project, I naturally chose to implement a Squeak VM. This I did; the result
> still appears to run at `http://weather-dimensions.com/Dan/SqueakOnJava.jar`.
>
> >This VM is known in the Squeak community as "Potato" because of some
> difficulty clearing names with the trademark people at Sun. Much later,
> when I got the Smalltalk-72 interpreter running in JavaScript, Bert and I
> were both surprised at how fast it ran. Bert said, "Hmm, I wonder if it's
> time to consider trying to run Squeak in JavaScript." I responded with
> "Hey, JavaScript is pretty similar to Java; you could just start with my
> Potato code and have something running in no time."
>
> >"No time" turned into a bit more than a week, but the result was enough to
> get Bert excited. The main weakness in Potato had been the memory model,
> and Bert came up with a beautiful scheme to leverage the native JavaScript
> storage management while providing the kind of control that was needed in
> the Squeak VM. Anyone interested in hosting a managed-memory language
> system in JavaScript should read his paper on SqueakJS, presented at the
> Dynamic Languages Symposium [Freudenberg et al. 2014].
>
> >From there on Bert has continued to put more attention on performance and
> reliability, and SqueakJS now boasts the ability to run every Squeak image
> since the first release in 1996. To run the system live, visit this url:
> https://smalltalkzoo.thechm.org/HOPL-Squeak.html?launch

**↪ Redirect (2026-07-20):** Don linked the **original HOPL edition** of Dan Ingalls's
paper (the one that deadnames Vanessa in Appendix A.5, quoted above). Vanessa asked people
to cite the **corrected Smalltalk Zoo edition** instead — see her reply in §3 below.
Working copies:

- **[Ingalls-2020-Evolution-of-Smalltalk-Zoo-corrected.pdf](Ingalls-2020-Evolution-of-Smalltalk-Zoo-corrected.pdf)** (preserved here)
- [smalltalkzoo.thechm.org/papers/EvolutionOfSmalltalk.pdf](https://smalltalkzoo.thechm.org/papers/EvolutionOfSmalltalk.pdf) (live)

The Potato JAR URL in the quote is also dead; no replacement known.

**↪ Nested quotes (2026-07-20):** Don [29020468](https://news.ycombinator.com/item?id=29020468)
quotes **Dan Ingalls**, *The Evolution of Smalltalk* (HOPL IV, 2020) — **original**
edition (deadnames Vanessa). The blockquote-within-blockquote is **Appendix A.5 Squeak**:

| Nested passage | Author | Location in our cache |
|----------------|--------|------------------------|
| Full A.5 block ("Although Squeak is still available…" through HOPL-Squeak launch URL) | **Dan Ingalls** (original HOPL text) | [Ingalls-2020-Evolution-of-Smalltalk-Zoo-corrected.pdf — Appendix A.5](Ingalls-2020-Evolution-of-Smalltalk-Zoo-corrected.pdf#page=87) — **corrected** edition; compare [live Zoo PDF](https://smalltalkzoo.thechm.org/papers/EvolutionOfSmalltalk.pdf#page=87) |

Vanessa asked people to cite the Zoo edition instead — see §3.

## 3. codefrau (Vanessa Freudenberg), 2021-11-05 — [29125515](https://news.ycombinator.com/item?id=29125515)

> Dan published an updated version of that paper here:
> https://smalltalkzoo.thechm.org/papers/EvolutionOfSmalltalk.pdf
>
> Would be great if you could cite that one next time. The main improvement
> for me is not being deadnamed. There are other corrections as well.

---

## Why this thread matters

1. **It is her wish, in her own words, in public** — the standing that the
   [memorial edition](README.md) rests on.
2. **It documents the corrected-edition pattern she endorsed**: Dan updated
   his paper and published the corrected version alongside the old one; she
   asked people to cite the new one. The memorial edition of her own paper
   follows exactly that pattern, applied to the one paper that never got it.
3. **It shows the gap in motion**: a commenter using her correct name in the
   same breath as links and quotations that couldn't — because version-of-
   record documents don't update themselves. That's the problem
   [prestoration](https://github.com/SimHacker/moollm/tree/main/designs/prestoration)
   and the [change-name skill](https://github.com/SimHacker/moollm/tree/main/skills/change-name)
   exist to fix.

Related sources in this directory: [README.md](README.md) (provenance index),
[Ingalls-2020-Evolution-of-Smalltalk-Zoo-corrected.pdf](Ingalls-2020-Evolution-of-Smalltalk-Zoo-corrected.pdf)
(the paper she asked us to cite),
[Vanessa's philosophy (MOOLLM)](https://github.com/SimHacker/moollm/blob/main/designs/vanessa-freudenberg-philosophy.md).
