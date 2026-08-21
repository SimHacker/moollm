# XANADU

**Could this be a substrate for Xanadu?**

A fair question to ask of anything that claims to take hypertext seriously. Here is the answer, told in order.

## The dream demanded guarantees

In 1965 Ted Nelson named both the technology — hypertext — and the condition it answers to: **everything is deeply intertwingled**. Project Xanadu specified what an honest medium owes its documents: links that know both their ends, inclusion by reference with provenance (transclusion), addresses that survive revision, and nothing that ever breaks. Not features. Guarantees, built into the substrate.

The web shipped without them — one-way links, 404s, copies with no memory of their source — and won by being easy. The dream didn't die; it just lost its funding.

## What survived, survived by handing users a language

The systems that thrived in the meantime shared one trait the web's documents lacked: their users could program them. Emacs endured every rewrite because it kept its extension language. HyperCard gave HyperTalk to everyone from day one. Even a bad embedded language beats none — Greenspun's tenth rule is the tax on going without.

And the other end of the spectrum proves it twice: Mathematica has thrived for four decades on being a language *worth paying for* — and it is now running endosymbiosis in both directions, growing LLM function calls inside its symbolic notebooks while its symbolic engine gets swallowed as a tool inside chat models. A good language doesn't just survive contact with machine learning; it metabolizes it, and gets metabolized, and both organisms come out stronger.

LambdaMOO ran the experiment at full scale: **scripting + the Adventure/Zork/MUD lineage + characters.** Hand every inhabitant a language and they build the world they live in. Reader equals writer equals programmer — the closest thing to Xanadu's spirit that actually shipped, and it shipped as a place.

But scripting alone doesn't buy the guarantees. A scripted world still breaks its links, still forgets its provenance. Something was missing, and it was never storage.

## The missing piece was a reader

Consider what an interface owes its user: to notice where you are and what you're doing, and to bring forward what matters *here, now* — context as the interface, attention as the scarce resource. That idea kept surfacing — considerate systems, context-aware computing — and kept hitting the same wall: the machine could sense the context but couldn't *understand* it.

MOOLLM's architecture is that idea, finally affordable: **directories are rooms, and a room is an activation context** — walking in loads what matters ([room](../skills/room/), [adventure](../skills/adventure/)). Names wake constellations of meaning ([k-lines](../skills/k-lines/)). The substrate doesn't have to be smart if the reading is.

## Then the reader arrived

An LLM is a reader that resolves by intent. Put one between the reader and the medium and the substrate can stay dumb and honest: **plain files and git, interpreted with empathy.** Now run the Xanadu checklist:

- **Two-way links** — resolved by reading, not by registry. Every link is bidirectional to a reader that can search.
- **Transclusion** — inclusion by reference *is* context assembly: reading a file into the context window, provenance attached.
- **Unbreakable links** — a moved file, a renamed section, a misspelled path resolve by intent ([postel](../skills/postel/): liberal in what you accept). Links don't break; they heal.
- **Version-aware addresses** — git: the whole history of every document, addressable, diffable, blame-able.
- **Intertwingularity** — cross-reference as first-class navigation ([file-system-object](../skills/file-system-object/SKILL.md), [Nelson-Links protocol](../designs/MOOLLM-PROTOCOLS.md)).

And the scripting birthright comes along for free, in its final form: **skills are programs, the LLM is `eval()`** ([Eval Incarnate Framework](../designs/eval/EVAL-INCARNATE-FRAMEWORK.md)), and the extension language is natural language.

The strongest objection deserves stating plainly: behavior-by-interpretation is exactly the compromise Xanadu existed to refuse — the web's original sin, repeated with a smarter reader. Guarantees enforced by an interpreter are only as good as the interpreter's judgment. That argument is welcome here; it would arrive as a file, and the files link back.

## Tilt your head: it was dispatch all along

Here is where the threads braid. The adventure game, decomposed, is **dispatch over dimensions**: Zork froze five of them into the Z-machine in 1979 — verb, direct object, indirect object, character, location. The Sims froze two. And character and location are the load-bearing pair: they are exactly the two dimensions MOOLLM reifies as directories — `characters/` and rooms. **The filesystem tree is the adventure game's coordinate system.**

Freeze *all* the dimensions and you get a cellular automaton: neighbors as dimensions, the rule table as guarded slots, total and decidable — simple rules, unreasonably rich behavior, an enumerable rule space. Melt them all and you get an LLM improvising on prose guards. One thermometer, every system on it — the full argument is [korz-prime](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/david-ungar/korz-prime.md), which reads CAs as context dispatch at absolute zero.

And the whole loop closes on a proposal made in 1984, in a paper on video feedback: *insert a digital computer into the feedback loop via a video frame buffer*. Swap the frame buffer for a language model and that is this repo's wiring diagram: sessions write files, files shape the next session, and structure emerges that nobody typed in ([SESSIONS.md](./SESSIONS.md) is the tape). Hold something up in front of the camera — a question, a character, a stuffed animal — and the loop metabolizes it.

## A place, not a promise

Xanadu promised a medium that keeps faith with its documents. MOOLLM's wager is that the faith can live in the reading instead of the plumbing: keep the substrate dumb and honest, make the reader empathic, and the guarantees become habits of interpretation — checked by git, healed by intent, intertwingled by default.

Not a tool you use. A place you can live in. Directories are rooms; the door is open.

- [README.md](../README.md) — what this place is.
- [QUICKSTART.md](../QUICKSTART.md) — get playing in two minutes.
- [PIONEERS.md](./PIONEERS.md) — the lineage, 22 giants.
- [The Pub](../examples/adventure-4/pub/) — where visitors end up anyway.
