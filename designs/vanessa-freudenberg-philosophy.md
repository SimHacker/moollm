# Vanessa Freudenberg's Philosophy: Target JavaScript, Not WebAssembly

*A technical tribute and design philosophy document*

You nailed it -- the tech enabling JS to match native speed was Self research from the 80s, adapted two decades later. Let me fill in some specifics from people whose papers I highly recommend, and who I've asked questions of and had interesting discussions with!

Vanessa Freudenberg [1], Craig Latta [2], Dave Ungar [3], Dan Ingalls, and Alan Kay had some great historical and fresh insights. Vanessa passed recently -- here's a thread where we discussed these exact issues: https://news.ycombinator.com/item?id=40917424

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

But it wasn't just technical cleverness -- it was philosophy. She wrote:

> "I just love coding and debugging in a dynamic high-level language. The only thing we could potentially gain from WASM is speed, but we would lose a lot in readability, flexibility, and to be honest, fun."

> "I'd much rather make the SqueakJS JIT produce code that the JavaScript JIT can optimize well. That would potentially give us more speed than even WASM."

Her guiding principle: do as little as necessary to leverage the enormous engineering achievements in modern JS runtimes [8]. Structure your generated code so the host JIT can optimize it. Don't fight the platform -- ride it.

She was clear-eyed about WASM: yes, it helps for tight inner loops like BitBlt. But for the VM as a whole? You gain some speed and lose readability, flexibility, debuggability, and joy. Bad trade.

This wasn't conservatism. It was confidence.

Vanessa understood that JS-the-engine isn't the enemy -- it's the substrate. Work with it instead of against it, and you can go faster than "native" while keeping the system alive and humane. Keep the debugger working. Keep the image snapshotable. Keep programming joyful. Vanessa knew that, and proved it!

---

## References

1. **Freudenberg et al** -- SqueakJS paper (DLS 2014, Most Notable Paper Award 2024) -- https://freudenbergs.de/vanessa/publications/Freudenberg-2014-SqueakJS.pdf
2. **Craig Latta, Caffeine** -- Smalltalk livecoding in the browser -- https://thiscontext.com/
3. **Self programming language** -- prototype-based OO with multiple inheritance -- https://selflanguage.org/
4. **Hoelzle, Chambers & Ungar** -- Debugging Optimized Code with Dynamic Deoptimization (1992) -- https://bibliography.selflanguage.org/dynamic-deoptimization.html
5. **Strongtalk** -- high-performance Smalltalk with optional types -- http://strongtalk.org/
6. **Lars Bak** -- architect of Self VM, Strongtalk, HotSpot, V8 -- https://en.wikipedia.org/wiki/Lars_Bak_(computer_programmer)
7. **SqueakJS** -- bit-compatible Squeak/Smalltalk VM in pure JavaScript -- https://squeak.js.org/
8. **SqueakJS JIT design notes** -- leveraging the host JS JIT -- https://squeak.js.org/docs/jit.md.html
9. **Vanessa Freudenberg** -- profile and contributions -- https://conf.researchr.org/profile/vanessafreudenberg

---

## MOOLLM Relevance

Vanessa's philosophy directly informs MOOLLM's approach:

| Vanessa's Principle | MOOLLM Application |
|---------------------|-------------------|
| Leverage host runtime | Use LLM capabilities, don't reimplement them |
| Hybrid GC cooperation | Let YAML Jazz work with LLM tokenization, not against it |
| Joy matters | Empathic expressions, readable prompts, humane systems |
| Do as little as necessary | Speed of Light -- one call, maximum leverage |
| Structure code for host optimization | Structure prompts for LLM optimization |

See also: [YAML Jazz](../skills/yaml-jazz/), [Speed of Light](../skills/speed-of-light/)
