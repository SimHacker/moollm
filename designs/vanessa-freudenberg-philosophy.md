# Vanessa Freudenberg's Philosophy: Target JavaScript, Not WebAssembly

**Author:** [Don Hopkins](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/don-hopkins) — this is Don's tribute and exposition, **not** Vanessa speaking.

**Subject:** Vanessa Freudenberg's technical philosophy (target JavaScript, not WebAssembly; hybrid GC; ride the host JIT).

**Voice rules:** We *represent and discuss* her work ([memorial mode](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/memorial.md)). **Vanessa's words** appear only in blockquotes, verbatim from [preserved primary sources](#memorial--primary-sources). Everything else is Don Hopkins narrating, interpreting, or editorializing (including the Brendan Eich / JavaScript prototype critique).

*Written for Alan Kay, Dan Ingalls, Craig Latta, David Rosenthal, and friends — July 2026.*

---

The tech enabling JS to match native speed was Self research from the 80s, adapted two decades later. Below: context from people whose papers I highly recommend, and whom I've asked questions of and had interesting discussions with.

Vanessa Freudenberg [1], Craig Latta [2], Dave Ungar [3], Dan Ingalls, and Alan Kay had some great historical and fresh insights. Vanessa passed recently — the exchange where **she** said this in **her own words** is preserved in the [2023 Croquet Jasmine HN thread](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/hn-thread-2023-croquet-jasmine.md) (my [2024 recap on HN](https://news.ycombinator.com/item?id=40917424) keeps it circulating).

Vanessa had this exactly right. I asked her what she thought of using WASM with its new GC support for her SqueakJS [1] Smalltalk VM.

Everyone keeps asking why we don't just target WebAssembly instead of JavaScript. Vanessa's answer -- backed by real systems, not thought experiments -- was: why would you throw away the best dynamic runtime ever built?

To understand why, you need to know where V8 came from -- and it's not where JavaScript came from.

David Ungar and Randall B. Smith created Self [3] in 1986. Self was radical, but the radicalism was in service of *simplicity*: no classes, just objects with slots. Objects delegate to parent objects -- multiple parents, dynamically added and removed at runtime. That's it.

The Self team -- Ungar, Craig Chambers, Urs Hoelzle, Lars Bak -- invented most of what makes dynamic languages fast: maps (hidden classes), polymorphic inline caches, adaptive optimization, dynamic deoptimization [4], on-stack replacement. Hoelzle's 1992 deoptimization paper blew my mind -- they delivered simplicity AND performance AND debugging.

That team built Strongtalk [5] (high-performance Smalltalk), got acquired by Sun and built HotSpot (why Java got fast), then Lars Bak went to Google and built V8 [6] (why JavaScript got fast). Same playbook: hidden classes, inline caching, tiered compilation. Self's legacy is inside every browser engine.

Brendan Eich claims JavaScript was inspired by Self. This is an exaggeration based on a deep misunderstanding that borders on insult. The whole *point* of Self was simplicity -- objects with slots, multiple parents, dynamic delegation, everything just another object.

JavaScript took "prototypes" and made them *harder* than classes: `__proto__` vs `.prototype` (two different things that sound the same), constructor functions you must call with `new` (forget it and `this` binds wrong -- silent corruption), only one constructor per prototype, single inheritance only. And of course `==` -- type coercion so broken you need a separate `===` operator to get actual equality. Brendan has a pattern of not understanding equality.

The ES6 `class` syntax was basically an admission that the prototype model was too confusing for anyone to use correctly. They bolted classes back on top -- but it's just syntax sugar over the same broken constructor/prototype mess underneath. Twenty years to arrive back at what Smalltalk had in 1980, except worse.

Self's simplicity was the point. JavaScript's prototype system is more complicated than classes, not less. It's prototype theater. The engines are brilliant -- Self's legacy. The language design fumbled the thing it claimed to borrow.

Vanessa Freudenberg worked for over two decades on live, self-supporting systems [9]. She contributed to Squeak EToys, Scratch, and Lively. She was co-founder of Croquet Corp and principal engineer of the Teatime client/server architecture that makes Croquet's replicated computation work. She brought Alan Kay's vision of computing into browsers and multiplayer worlds.

SqueakJS [7] was her masterpiece -- a bit-compatible Squeak/Smalltalk VM written entirely in JavaScript. Not a port, not a subset -- the real thing, running in your browser, with the image, the debugger, the inspector, live all the way down. It received the Dynamic Languages Symposium Most Notable Paper Award in 2024, ten years after publication [1].

The genius of her approach was the garbage collection integration. It amazed me how she pulled a rabbit out of a hat -- representing Squeak objects as plain JavaScript objects and cooperating with the host GC instead of fighting it. Most VM implementations end up with two garbage collectors in a knife fight over the heap. She made them cooperate through a hybrid scheme that allowed Squeak object enumeration without a dedicated object table. No dueling collectors. Just leverage the machinery you've already paid for.

But it wasn't just technical cleverness — it was philosophy. In the [December 2023 thread](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/hn-thread-2023-croquet-jasmine.md), **Vanessa wrote**:

> "I just love coding and debugging in a dynamic high-level language. The only thing we could potentially gain from WASM is speed, but we would lose a lot in readability, flexibility, and to be honest, fun."
>
> — Vanessa Freudenberg, HN, December 2023

> "I'd much rather make the SqueakJS JIT produce code that the JavaScript JIT can optimize well. That would potentially give us more speed than even WASM."
>
> — Vanessa Freudenberg, HN, December 2023

**Don interprets:** her guiding principle was to do as little as necessary to leverage the enormous engineering achievements in modern JS runtimes [8] — structure generated code so the host JIT can optimize it; don't fight the platform, ride it. The preserved [JIT brain dumps](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/vanessa-freudenberg/sources/jit-notes) show how she planned to do that.

She was clear-eyed about WASM: yes, it helps for tight inner loops like BitBlt. But for the VM as a whole? You gain some speed and lose readability, flexibility, debuggability, and joy. Bad trade — **Don's summary of her position**, not a direct quote.

This wasn't conservatism. It was confidence — **Don's read** on why her stance mattered.

Vanessa understood that JS-the-engine isn't the enemy — it's the substrate. Work with it instead of against it, and you can go faster than "native" while keeping the system alive and humane. Keep the debugger working. Keep the image snapshotable. Keep programming joyful. **That closing paragraph is Don Hopkins**, synthesizing what her work and her quoted words imply — Vanessa knew that, and proved it.

---

## Memorial & primary sources

| Artifact | Link |
|----------|------|
| **SqueakJS paper — memorial edition** (byline corrected, original preserved) | [Freudenberg-2014-SqueakJS-memorial-edition.pdf](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/Freudenberg-2014-SqueakJS-memorial-edition.pdf) |
| Original PDF (untouched primary source) | [Freudenberg-2014-SqueakJS-original.pdf](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/Freudenberg-2014-SqueakJS-original.pdf) |
| How the memorial edition was made | [prestoration/](./prestoration/) — provenance, ethics, play-by-play |
| Her 2021 request not to be deadnamed | [hn-thread-2021-squeakjs.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/hn-thread-2021-squeakjs.md) |
| WASM / JS / Self thread (source of quotes above) | [hn-thread-2023-croquet-jasmine.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/hn-thread-2023-croquet-jasmine.md) |
| JIT design notes (preserved) | [jit-notes/](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/vanessa-freudenberg/sources/jit-notes) |
| Dan Ingalls HOPL paper (Zoo corrected edition she asked us to cite) | [Ingalls-2020-Evolution-of-Smalltalk-Zoo-corrected.pdf](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/Ingalls-2020-Evolution-of-Smalltalk-Zoo-corrected.pdf) |
| Character directory & memorial | [vanessa-freudenberg/](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/vanessa-freudenberg) |

---

## References

1. **Freudenberg et al** — SqueakJS paper (DLS 2014, Most Notable Paper Award 2024). **Memorial edition** (byline: Vanessa Freudenberg, provenance disclosed): https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/Freudenberg-2014-SqueakJS-memorial-edition.pdf — original untouched: https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/vanessa-freudenberg/sources/Freudenberg-2014-SqueakJS-original.pdf — ACM doi (still says "Bert"): https://doi.org/10.1145/2661088.2661100
2. **Craig Latta, Caffeine** -- Smalltalk livecoding in the browser -- https://thiscontext.com/
3. **Self programming language** -- prototype-based OO with multiple inheritance -- https://selflanguage.org/
4. **Hoelzle, Chambers & Ungar** -- Debugging Optimized Code with Dynamic Deoptimization (1992) -- https://bibliography.selflanguage.org/dynamic-deoptimization.html
5. **Strongtalk** -- high-performance Smalltalk with optional types -- http://strongtalk.org/
6. **Lars Bak** -- architect of Self VM, Strongtalk, HotSpot, V8 -- https://en.wikipedia.org/wiki/Lars_Bak_(computer_programmer)
7. **SqueakJS** -- bit-compatible Squeak/Smalltalk VM in pure JavaScript -- https://squeak.js.org/
8. **SqueakJS JIT design notes** — leveraging the host JS JIT. Live: https://squeak.js.org/docs/jit.md.html — **preserved in repo**: https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/vanessa-freudenberg/sources/jit-notes
9. **Vanessa Freudenberg** — profile and contributions -- https://conf.researchr.org/profile/vanessafreudenberg — character & sources: https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/vanessa-freudenberg

---

## MOOLLM Relevance

**Don Hopkins:** Vanessa's philosophy directly informs MOOLLM's approach:

| Vanessa's Principle | MOOLLM Application |
|---------------------|-------------------|
| Leverage host runtime | Use LLM capabilities, don't reimplement them |
| Hybrid GC cooperation | Let YAML Jazz work with LLM tokenization, not against it |
| Joy matters | Empathic expressions, readable prompts, humane systems |
| Do as little as necessary | Speed of Light -- one call, maximum leverage |
| Structure code for host optimization | Structure prompts for LLM optimization |

See also: [YAML Jazz](../skills/yaml-jazz/), [Speed of Light](../skills/speed-of-light/), [prestoration](./prestoration/)
