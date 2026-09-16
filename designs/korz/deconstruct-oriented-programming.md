# How to Disorient Almost Anything

In 1991, Chip Morningstar — an engineer, co-creator of Lucasfilm's
Habitat — attended the Second International Conference on Cyberspace
and found himself surrounded by postmodern literary theorists. Instead
of dismissing them, he did the engineering thing: he read the theory,
reverse-engineered deconstruction into a working recipe, and published
it as ["How to Deconstruct Almost Anything"](http://www.fudco.com/chip/deconstr.html).
His recipe, lightly restated:

1. Select a text.
2. Decide what it says — any defensible reading will do.
3. Find a distinction the text takes for granted.
4. Show that the distinction is really a hierarchy: one side is
   presumed superior.
5. Derive a reading in which the text undermines its own hierarchy.

The point of deconstruction, in Morningstar's hands, is not destruction.
It is showing that a text already contradicts its own premises once you
notice which assumption it quietly enthroned.

This essay applies the recipe to programming paradigm names — twice.
The first pass dissolves the class. The second dissolves the object.
What's left at the bottom is a language design David Ungar and
colleagues actually built, and a naming question worth asking him
(filed in [ask-david.md](ask-david.md)).

## First pass: the class

**Step 1 — the text.** A line of Smalltalk:

```smalltalk
Account subclass: #SavingsAccount
    instanceVariableNames: 'balance'
```

Smalltalk's founding slogan makes the reading official: "everything is
an object," and every object gets its behavior from its class.

**Step 2 — what it says.** The class is the essence of the account.
An instance is an account because it is a member of the class. Behavior
lives in the taxonomy; the objects at runtime are tokens stamped from
the mold.

**Step 3 — the distinction.** Class versus instance. Type versus token.
Essence versus accident.

**Step 4 — the hierarchy.** Programming culture presumes the class is
the superior pole. The class file is where the author works, the
debugger prints class names, and design patterns are drawn as class
diagrams. The instance is a second-class citizen, literally.

**Step 5 — the text undermines itself.** In 1987 David Ungar and
Randall Smith built Self, a Smalltalk descendant with no classes at
all. Objects inherit directly from other objects (prototypes), and
anything a class did — grouping, sharing, documentation — turns out to
be expressible as ordinary objects pointing at ordinary objects. The
kicker is that the machine never needed the taxonomy: Self's compiler
watched what actually happened at each call site and generated fast
code from observed behavior, and that technique became the JIT
technology that later made Java and JavaScript fast. The class
hierarchy was a reading aid for humans. The computation was
object-to-object all along.

Call this move **declassification**. The class survives it — but as an
optional view you can project when it helps, not as the axis the
runtime obeys.

## Second pass: the object

**Step 1 — the text.** One message send:

```smalltalk
anAccount withdraw: 100.
```

**Step 2 — what it says.** There is an object. It owns the method. The
message goes to it, and to it alone. One receiver, one privileged
actor — a little agent inside the object who does the real work.

**Step 3 — the distinction.** Receiver versus everything else. The
first argument of every call is sacred; the rest of the situation —
caller, thread, security domain, assertion mode, user, device, time of
day — is either unmentioned or bolted on later through annotations,
thread-locals, aspect weavers, and dependency injection.

**Step 4 — the hierarchy.** Object-oriented culture presumes the
receiver outranks the context. `self` is a keyword; the ambient
situation is somebody else's problem. Whole paradigms — subject-oriented
programming, context-oriented programming, aspect-oriented programming —
exist as separate movements precisely because the receiver was never
allowed to step down.

Marvin Minsky saw the same enthronement in psychology. In a 1982 essay
he demolished what he called the Single Agent theory — the folk idea of
"a little person deep down there" who does the real mental work — and
concluded: "Self, itself, is not a single thing." He wrote that five
years before Self the language shipped, and it reads as a prophecy of
what came next.

**Step 5 — the text undermines itself.** In 2014, Ungar — with Harold
Ossher and Doug Kimelman at IBM Research — took the step past Self:
Korz, a language with no objects. A Korz program is a flat collection
of slots (data and methods) owned by nothing. Each slot carries guards
over named dimensions — `rcvr`, `assertions`, `user`, `device`,
whatever the design needs. A message send happens in a context, a set
of dimension bindings that flows implicitly down the call chain, and
dispatch matches the whole context symmetrically. No argument is the
receiver.

Their worked example: define `pop()` once, guarded on
`{rcvr ≤ stack}`. Later, add assertion checking by defining a second
`pop()` guarded on `{rcvr ≤ stack, assertions ≤ true}` — more specific,
so it wins whenever the context carries `assertions: true`. The main
program switches assertions on, and no intermediate code mentions them;
the binding flows through implicitly. A new concern was added to a
running design without touching a line between the top and the bottom.

And the object survives this move the same way the class survived the
last one: as a view. Gather the slots along the `rcvr` dimension and
familiar objects reappear. Gather along `user` and you see one person's
version of the system. The object was a projection of the slot soup
along one axis — a projection with very good PR.

Call this move **deobjectification**.

## What's left: Oriented Programming

Run both passes and look at the residue. Every paradigm in the family
turns out to be the same mechanism with one dimension frozen into the
brand name:

| Paradigm | Frozen dimension |
|----------|------------------|
| Object-oriented | receiver |
| Subject-oriented | who is looking |
| Context-oriented | what is happening |
| Aspect-oriented | which concern cuts across |

Korz's own position papers argue that the last three are projections of
one smaller mechanism. This essay's proposal is one step blunter: drop
the modifier entirely. **Oriented Programming** — behavior selected by
orientation along any number of named dimensions, none privileged in
the name. The word even wants this reading: to orient (from Latin
*oriens*, the rising sun) is to establish a bearing, and an oriented
program is one whose behavior is relative to a declared bearing rather
than to nouns pretending to be physics.

The corollary writes itself. A language that names one axis in its
paradigm while actually running on a dozen unstated ones — classloader,
thread, transaction, annotation, weave order — is practicing
**Disoriented Programming**. It isn't wrong to use those dimensions.
It's disoriented to pretend only one appears on the compass.

## The arc, and the question

Three subtractions, forty years:

- Smalltalk: everything is an object, and classes rule the objects.
- Self (1987): remove the classes. Objects and messages remain, and
  the machinery gets *faster*.
- Korz (2014): remove the object boundary. Slots, dimensions, and
  context remain, and the paradigm wars over Subject versus Context
  versus Aspect collapse into a choice of which guard to freeze.

Each step selected a smaller text, found a smaller enthroned
distinction, and showed the previous language already contradicted it.
Morningstar's recipe, run on language design instead of literary
criticism — by the language designers themselves, in working code.

The open question, filed for David Ungar in
[ask-david.md](ask-david.md): the Korz papers still wear a modifier
("Simple, Symmetric, Subjective, Context-Oriented Programming"). Having
demoted the receiver, would he go the rest of the way and let the genre
just be called Oriented Programming?

Hang on to your sense of humor. Don't let anyone intimidate you with
taxonomy. And when someone insists a paradigm *is* object-oriented, ask
which dimension they froze — and which ones they're disoriented about.

---

*After Chip Morningstar's ["How to Deconstruct Almost Anything"](http://www.fudco.com/chip/deconstr.html)
(1991). Korz: Ungar, Ossher, Kimelman, Onward! 2014 — see
[README.md](README.md) for the language itself and
[design.md](korz-prime/README.md) for Korz′, its LLM-age reading. Minsky's essay:
"Why People Think Computers Can't," AI Magazine, 1982.*
