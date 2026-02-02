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
