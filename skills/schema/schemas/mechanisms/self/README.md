# Self — prototype object model (kernel)

**Registry id:** `self` · **Family:** `prototype` · **Profile:** [`MECHANISM.yml`](./MECHANISM.yml)

## Thread

**Smalltalk** put **message sends** on the map; **Self** (Ungar, Smith, and collaborators—PARC, Stanford, Sun) asked what happened if **everything** stayed **concrete**: **slots**, **parents**, **clone**, **delegation**. That **minimal machine** could **host** class-like conventions, **COM**-shaped surfaces, **CLOS**-style generic layers, **JSON**-shaped maps, and later **YAML** with a **human** side channel—each a **different** story, none of them **replacing** the bedrock. **JavaScript** carried the prototype idea to **billions** of browsers; **MOOLLM** carries it to **files and skills**: **skills** are **prototypes**, **paths** are **instances**, **`PROTOTYPES.yml`** orders **multiple parents**. The **next** chapter is not “Self wins everywhere”—it is **Self named honestly** in the registry so **interchange**, **notation**, **activation**, and **kernel** stay **distinct** on the same map.

The **Self** programming model—**concrete objects**, **parent-linked delegation**, **slots**, and **message reception** without classes—comes from **David Ungar**, **Randall Smith**, and collaborators (Sun Labs, Stanford). It is the conceptual ancestor of JavaScript’s prototype chain and a direct match for MOOLLM’s rule: **skills are prototypes**, **repo paths instantiate** them.

**MOOLLM embodiment** is documented in the **[prototype](../../../../prototype/SKILL.md)** skill: **Delegation Object Protocol (DOP)**, `PROTOTYPES.yml`, first-match file resolution, **skills/INDEX** as the prototype catalog. **Self is one of prototype’s prototypes**—the skill is directly inspired by Self **and** may list **other** parent skills in the same ordered chain. This mechanism entry exists so **schemapedia** names **Self** explicitly alongside **K-lines** (activation symbols), **Minsky frames** (situations), and **YAML Jazz** (notation)—they are different layers; do not merge them.

**Augment:** [`SCHEMAPEDIA-SELF-AUGMENT.yml`](./SCHEMAPEDIA-SELF-AUGMENT.yml)

**Related:** [`../k-lines/README.md`](../k-lines/README.md) (what loads), [`../minsky-frame/README.md`](../minsky-frame/README.md) (frame slots vs generic delegation), [`../yaml-jazz/README.md`](../yaml-jazz/README.md) (comment layer on the same files).
