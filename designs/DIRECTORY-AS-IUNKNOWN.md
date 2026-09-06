# Directory as IUnknown: COM of the Filesystem

**MOOM** = COM for MOOLLM
**MOOLE** = OLE for MOOLLM  
**IUnmood** = The interface you query when you don't know what mood to be in ;)

How MOOLLM reimagines COM/OLE IUnknown as a filesystem pattern.

---

## The Insight

Traditional object orientation: objects contain data and methods.
COM/OLE IUnknown: objects contain interfaces you query at runtime.

**MOOLLM**: Directories ARE objects. Files ARE interfaces.
"QueryInterface" is just checking for ROOM.yml, CHARACTER.yml, SKILL.md.

---

## COM/OLE Background

Microsoft's Component Object Model (COM) was built on one fundamental interface:

```cpp
interface IUnknown {
    HRESULT QueryInterface(REFIID riid, void **ppvObject);
    ULONG AddRef();
    ULONG Release();
}
```

Every COM object implements IUnknown. To ask "can you do X?", you call
QueryInterface with the ID of interface X. The object either returns
a pointer to that interface, or E_NOINTERFACE.

Key insights from COM:
1. **Objects can have multiple interfaces** — same object, different views
2. **Runtime polymorphism** — discover capabilities at runtime
3. **Interface inheritance** — but NOT implementation inheritance
4. **Aggregation instead of inheritance** — compose objects, don't subclass
5. **Tear-off interfaces** — create interface on demand, with own state
6. **Controlling unknown delegation** — QueryInterface can delegate to inner objects
7. **Reference counting** — memory management without GC

Also inspired by: Owen Densmore and David SH Rosenthal's patented 
shell PATH file system based multiple inheritance object system 
(Smalltalk/NeWS/Self-like object system using the filesystem itself).

The seven points above are a condensation of Don's own COM synopsis, written on Hacker News in
November 2016 and archived verbatim at
[`object-system/sources/2016-com-synopsis.md`](object-system/sources/2016-com-synopsis.md). Two of
its arguments do not survive condensation, and the sections below restore them.

---

## Dual interfaces are the compiler thesis, with a vendor receipt

MIDL let one component publish **two** interfaces to the same functionality:

> both an OLE IDispatch interfaces taking variant type parameters, and also more efficient lower
> level COM interface taking primitive types. Runtimes like Visual Basic knew how to integrate dual
> interfaces and could bind to the more efficient underlying COM interfaces, instead of going through
> the slower generic dynamic IDispatch interfaces.

That is this repo's compilation strategy, shipped commercially in 1993 and load-bearing for a decade.

| | OLE | MOOLLM |
|---|---|---|
| Slow, general path | `IDispatch` — stringly-typed, late-bound, variants | the LLM reads the YAML and figures it out |
| Fast, specific path | vtable call with primitive types | compiled JSON tree, deterministic traversal |
| Who chooses | the runtime, at bind time | the reader — a human clicking, or a model |
| Guarantee | both paths reach the same behaviour | both paths reach the same behaviour |

The crucial property is not that two paths exist. It is that **the fast path is derived from the
same declaration as the slow path**, so nothing has to be written twice and the two cannot drift.
A dual interface is one MIDL declaration, and the adventure compiler is one YAML tree — from which
falls out a browsable artifact that needs no model at runtime, which is the
[tagsonomy compiler](webtop/hyperties/LINK-RESOLUTION.md#the-build-step-is-the-whole-trick) move
stated in a vendor's interface-definition language thirty years early.

The direction of preference is also worth copying. Visual Basic bound the *fast* path whenever it
could and fell back to dynamic dispatch only when it could not, which is the honest default: pay for
interpretation when you must, never as a matter of course. A corpus that requires an LLM to navigate
has published only its `IDispatch`.

## The overshoot arc is the design budget

The post's history is not decoration; it is a failure mode named three times in one arc.

1. **VBX succeeded too well.** "Extremely popular and became a victim of their own success, after a
   whole industry grew up around them, and people started using them for all kinds of things they
   weren't intended for." Microsoft had to act to "mitigate the success disaster of VBX," so it
   invented COM. A **success disaster** is the specific shape of Kay's observation that things which
   only kind of work tend to hang on — VBX hung on hard enough to force a rewrite.
2. **COM was the good part.** "A very simple and ingenious idea that elegantly solved some real world
   problems."
3. **Then it kept going.** "It eventually evolved into something extremely complex that attempted to
   solve many other unrelated problems, and which required a massive amount of tooling, and that
   depended on Microsoft's Visual Studio and Win32 environment." And the verdict on the far end:
   **"DCOM is where COM went off the deep end."**

The lesson is not "component systems are bad." It is that the tooling dependency is what kills them.
COM's ingenious core needed MIDL, type-library compilers, wizards, and a specific IDE, so it could not
outlive that IDE — and every knock-off inherited the same disease. MOA needed Director. XPCOM needed
XPIDL, and Mozilla spent years removing it under the name *deCOMtamination*.

Which sets the budget that
[§ What We Skip](../kernel/DIRECTORY-AS-OBJECT.md#what-we-skip) spends: the interface language is
YAML, the type library is `CARD.yml`, the registry is the filesystem, and the compiler is a Python
script plus a model. Anyone with `ls` has the tooling. **The test to keep applying is whether a reader
who does not have our tools can still use the objects** — because that is the exact test COM failed,
after passing everything else.

---

## The class.ps Precedent: Dangerous Substrate, Structured Discipline

The standard objection to general-purpose, everyday multiple inheritance is
correct: as a daily tool it's a footgun. The answer is not to ban the
mechanism but to layer disciplines on top of it — and PostScript is the
canonical case study.

PostScript's dictionary stack is raw dynamic scope: `begin`/`end` push and
pop dictionaries at any time, precisely (or imprecisely) rewiring name
lookup for everything downstream. Doing that casually is a horrible idea —
spooky action at a distance, the archetype of why people distrust dynamic
scope. Yet Owen Densmore's **class.ps** (Object Oriented Programming in
NeWS) used exactly those low-level `begin`/`end` primitives to implement a
*structured* object system: first single inheritance like Smalltalk, later
multiple inheritance like Self. The lookup discipline — what gets pushed,
in what order, when — was encapsulated inside the class system, so ordinary
code never touched the dict stack directly. The dangerous mechanism wasn't
the enemy; it was the load-bearing substrate.

The same story repeats up the industry: C++ vtables are hand-corruptible
function-pointer tables; COM's QueryInterface disciplined them into
negotiated capability discovery; Java and C# interfaces made that
discipline a language feature. Pattern: **a maximally general sharp-edged
mechanism at the bottom, a structured protocol on top, everyday work
through the protocol — and the raw layer stays available for building the
next protocol.**

MOOLLM runs the same layering. The substrate is maximally general —
`prototype:` can point at anything, YAML inheritance chains can braid
freely. The discipline is the file conventions: drop an `INTERFACE.yml`
(or `ROOM.yml`, `CHARACTER.yml`, `GAME.yml`) into a directory and the
object grows a queryable facet, one file at a time, without touching what
was already there. Chris Trottier would call it **design by accretion** —
the discipline lives in the conventions and the query protocol, not in a
restriction of the substrate.

---

## Directory as Object

In MOOLLM, a directory is an object:

```
skills/adventure/
├── CARD.yml          # ICard interface
├── SKILL.md          # ISkill interface  
├── ROOM.yml          # IRoom interface (it's a room!)
├── CHARACTER.yml     # ICharacter interface (it's also a character!)
├── examples/         # Examples extension point
└── plugins/          # Plugin extension point
```

**"QueryInterface"** for MOOLLM:

```python
def query_interface(directory, interface_name):
    """Check if directory implements an interface."""
    patterns = {
        'room': ['ROOM.yml', 'ROOM.yaml'],
        'character': ['CHARACTER.yml', 'CHARACTER.yaml'],
        'skill': ['SKILL.md', 'CARD.yml'],
        'simulation': ['SIMULATION.yml'],
        'object': ['OBJECT.yml'],
    }
    
    for pattern in patterns.get(interface_name, []):
        if (directory / pattern).exists():
            return directory / pattern
    
    return None  # E_NOINTERFACE
```

---

## Multiple Interfaces, Shared State

A COM object can implement many interfaces sharing internal state.
A MOOLLM directory can implement many "interfaces" sharing files:

```
pub/bar/
├── ROOM.yml          # It's a room (location)
├── BUSINESS.yml      # It's a business (economy)
├── inventory.yml     # Shared state: what's in stock
├── ledger.yml        # Shared state: tabs and transactions
└── staff/            # Sub-objects (bartender, etc.)
    └── bartender/
        ├── CHARACTER.yml
        └── schedule.yml
```

The bar IS-A room AND IS-A business. Both interfaces read `inventory.yml`.
This is like COM aggregation but simpler.

---

## Inside-Out COM

Traditional COM: IUnknown is the root of an implementation class.
The class hides its data behind interface methods.

MOOLLM: The directory IS the data. Interfaces are views INTO the data.
The "implementation class" is the directory structure itself.

This is **inside-out COM**:
- COM: interface → hidden implementation → shared state
- MOOLLM: visible state → multiple interface files → shared directory

The filesystem provides:
- Persistence (files are durable)
- Versioning (git tracks changes)
- Inspection (you can `ls` and `cat` everything)
- Extension (add files to extend interfaces)

---

## The Self Language Parallel

David Ungar and Randy Smith's **Self** language pioneered prototype-based OOP:

| Traditional OOP | Self | MOOLLM |
|-----------------|------|--------|
| Classes | Prototypes | Template directories |
| Instances | Clones | Copied directories |
| Methods | Slots | YAML properties + skills |
| Inheritance | Delegation | `inherits:` in YAML |
| Mixins | Traits | Skill composition |

Self was **RISC OOP microcode** — a minimal mechanism that could efficiently
simulate class-based, prototype-based, trait-based, and other models.

MOOLLM has the same philosophy:
- **Minimal primitives**: directories, files, YAML, inheritance
- **Maximum expressiveness**: compose any OOP pattern you want
- **Runtime malleability**: change structure while running

---

## Self's Key Insights Applied to MOOLLM

### 1. Prototypes, Not Classes

Self: clone objects, not instantiate classes.
MOOLLM: copy directories, not instantiate schemas.

```bash
# "Cloning" a prototype
cp -r skills/character-template characters/new-character
```

### 2. Slots as Unified Concept

Self: everything is a slot (data, methods, parents).
MOOLLM: everything is a file or YAML property.

```yaml
# CHARACTER.yml
character:
  name: Marieke
  location: pub/bar/       # Data slot
  skills: [budtender]      # Method slots
  inherits: [skills/npc]   # Parent slot
```

### 3. Dynamic Inheritance

Self: parent slots can change at runtime.
MOOLLM: `inherits:` list can change, themes can swap prototypes.

```yaml
# During "space cantina" theme
inherits:
  - skills/space-bartender  # Different parent!
  - personas/z-4rt         # Different persona!
```

### 4. Traits as Composable Packets

Self: traits are composable behavior packets.
MOOLLM: skills are composable capability packets.

```yaml
skills:
  - skills/bartender      # Pour drinks
  - skills/therapist      # Listen to problems
  - skills/bouncer        # Maintain order
```

---

## Meta-Object Protocol

CLOS (Common Lisp Object System) has a meta-object protocol:
you can customize how objects work at the meta level.

MOOLLM has an implicit MOP:
- **How do we find interfaces?** → File patterns in directories
- **How do we resolve inheritance?** → `inherits:` in YAML
- **How do we dispatch?** → Skill loading and composition
- **How do we extend?** → Drop files in extension directories

The "meta-objects" are:
- The kernel's file-loading rules
- The skill resolution algorithm  
- The inheritance merger
- The extension point protocol

---

## Extension Points as Interface Contracts

COM has "interface definitions" (IDL files) specifying what methods exist.
MOOLLM has extension points specifying what files can be added:

```yaml
# In valentine-flux.yml
extension_points:
  keepers:
    directory: keepers/
    schema: keeper.yml
    description: "Add new Keeper cards"
    
  rules:
    directory: rules/
    schema: rule.yml
    description: "Add new Rule cards"
    
  cosmic_dealers:
    directory: cosmic-dealers/
    schema: cosmic-dealer.yml
    description: "Add cosmic dealer interventions"
```

Anyone can extend the game by dropping files in the right place,
following the right schema. This is COM-like extensibility without
the registry, without vtables, without DLLs.

---

## Rumsfeld's Known Unknowns (and IUnknown)

Donald Rumsfeld famously said:

> "There are known knowns; there are things we know we know.
> We also know there are known unknowns; that is to say we know
> there are some things we do not know. But there are also
> unknown unknowns—the ones we don't know we don't know."

This maps surprisingly well to MOOLLM:

| Rumsfeld | MOOLLM | Doctor NO/KNOW |
|----------|--------|----------------|
| Known knowns | Files we've read | What Doctor KNOW knows |
| Known unknowns | Files we know exist but haven't read | Questions Doctor NO asks |
| Unknown unknowns | Extensions not yet written | The humility of Doctor NO |

And of course: **IUnknown** is the interface you query when you
don't know what interfaces an object supports. The unknown-unknown
of COM is "I don't even know what to ask for."

This is allegorical for ethical AI:
- What do we KNOW about a person we're simulating?
- What do we know we DON'T know?
- What don't we know we don't know?

The no-ai-* skills try to make unknown unknowns into known unknowns.

---

## Practical Implications

### For Skill Authors

1. **Put capabilities in separate files** — each file is an "interface"
2. **Use `inherits:`** — delegate to parent prototypes
3. **Create extension points** — let others add capabilities
4. **Check for files, not types** — `if exists(ROOM.yml)` not `isinstance(Room)`

### For Character Authors

1. **Directory IS the character** — don't separate "schema" from "instance"
2. **Compose skills** — mix capabilities like Self traits
3. **Allow runtime changes** — themes can swap prototypes

### For Orchestrator Authors

1. **QueryInterface by globbing** — find what interfaces a directory supports
2. **Load lazily** — don't read everything, query for what you need
3. **Respect extension points** — look for user additions

---

## Summary

MOOLLM's filesystem-as-object-model is:
- **Inside-out COM** — data visible, interfaces as file patterns
- **Self-style prototypes** — clone directories, not instantiate classes
- **RISC OOP microcode** — minimal primitives, maximum expressiveness
- **Inspectable** — `ls` and `cat` beat debuggers
- **Versionable** — git gives you object history for free
- **Extensible** — drop files in extension points

The directory IS the IUnknown. QueryInterface is checking for files.
The unknown unknowns are the files not yet written.

---

*COM was asking: "What CAN you do?"*
*MOOLLM answers: "Look at my files. That's what I can do."*
