---
name: container
description: "A directory that is a scope, not a place: its defaults: reach every room, character and object inside it, like OpenLaszlo's <node> or the CSS cascade."
license: MIT
tier: 1
allowed-tools: [read_file, write_file, run_terminal_cmd]
permissions: [read, write, terminal]
related: [room, object, character, adventure, prototype, logistic-container]
benefits_from:
  - { skill: prototype, why: "defaults: is looked up after an object's own slots and declared parents; resolve.py implements both" }
tags: [moollm, scope, cascade, defaults, hierarchy, composition]
credits: "Don Hopkins. Lineage: OpenLaszlo <node>, the CSS cascade, lexical scope."
---

# Container

> **Intermediate scopes that pass values down without being navigable rooms.**

Part of MOOLLM · [This skill's directory](https://github.com/SimHacker/moollm/tree/main/skills/container)

A container is a directory with a `CONTAINER.yml`. You can't walk into it; it groups what's
inside and gives those things default values. The maze is a container: every room in it is
dark unless the room says otherwise.

## The OpenLaszlo inspiration

In OpenLaszlo, `<node>` was a building block with attributes and children but no layout:

```xml
<node name="mazeDefaults">
  <attribute name="isDark" value="true"/>
</node>
```

`CONTAINER.yml` does the same for a directory tree:

```yaml
# maze/CONTAINER.yml
name: "The Twisty Maze"
defaults:
  room:
    lighting: 0      # pitch black; whether a grue hunts is the grue's call
```

## Container, room, meta

| Type | File | Navigable? | Passes values to children? |
|------|------|------------|----------------------------|
| Room | `ROOM.yml` | yes | no |
| Container | `CONTAINER.yml` | no | yes, through `defaults:` |
| Meta | `.meta.yml` | no | no (just metadata) |

Use a container when the directory is a grouping or a region, not a place. A directory can't
be both: if you can walk into it, it's a room, and sub-rooms that should share values go in a
container below or around it.

## `defaults:`

`defaults:` is keyed by what the child is:

| Key | Applies to |
|---|---|
| `room` | a directory with `ROOM.yml`, or the ROOM.yml itself |
| `character` | a directory with `CHARACTER.yml` |
| any interface name, lowercased | a directory or file with that interface (`run` for `RUN.yml`) |
| `object` | a plain YAML file (`coin.yml`) |
| the singular of a collection | an embedded object (`objects:` → `object`, `exits:` → `exit`) |

A talking room has both `ROOM.yml` and `CHARACTER.yml`, so both `room` and `character`
defaults apply to it. A container covers what's inside its directory, not the directory itself.

```yaml
# characters/animals/CONTAINER.yml
name: "Animal Characters"
defaults:
  character:
    can_speak_human: false   # Palm is special, and says so in her own file
    pet_able: true
  object:
    chewed: true
```

## Lookup order

For anything inside a container, a slot is looked up in this order; first match wins:

1. The object's own slots.
2. Its declared parents: `inherits:` and named `role*:` parents, and what they inherit.
3. `defaults:` of enclosing containers, nearest first.
4. Its implied skill parents (`ROOM.yml` → the `room` skill), the most generic.

Defaults come before the implied skill for the same reason an author's stylesheet beats the
browser's: the maze knows more about its rooms than the generic room skill does.

Across nested containers, values merge like the CSS cascade:

| Value | Nested containers |
|---|---|
| scalar | nearest container wins |
| map | deep-merged, nearer keys win |
| list | concatenated, nearest first |

```
cellar/
├── CONTAINER.yml        defaults: room: { lighting: 0, smells: [damp] }
├── vault/ROOM.yml       lighting → 0 (cellar)
├── lamp-room/ROOM.yml   lighting: 6, its own
└── deep/
    ├── CONTAINER.yml    defaults: room: { lighting: 1, smells: [brine] }
    └── well/ROOM.yml    lighting → 1 (deep); smells → [brine, damp]
```

That tree is `skills/prototype/examples/lookup/cellar/`, and the prototype skill's tests check
each line of it.

An object overrides a default by stating the slot. To add to a defaulted list rather than
replace it, there's no special syntax: the object states the whole list it wants.

## The rest of CONTAINER.yml

Everything outside `defaults:` describes the container itself: `rules:`, `constraints:`,
`ambient:`, `on_enter:`/`on_exit:`, `games:`, `lore:`, the place protocol
(`placement_rules:`, `zones:`) and logistics (`chest_mode:`, `provides:`, `request_list:`).
These don't become slots of the children. A child reaches them through where it is: the
LLM, a rule engine or the adventure runtime reads the containers enclosing a room and applies
the rules there. The prototype `skills/container/CONTAINER.yml` lists every field; every
CONTAINER.yml inherits it, so a container states only what differs.

## Older spellings

| Older | Write |
|---|---|
| `container:` wrapping the file | flat |
| `inherits: {key: value}` meaning "children get these" | `defaults: {room: {key: value}}` |
| `inherits:` as forced values, `defaults:` as fallbacks | one key, `defaults:`; a child that states the slot wins |

`inherits:` on a container means the container's own parents, as on any object.

## Tools

```bash
python3 skills/prototype/scripts/resolve.py lookup examples/adventure-4/maze/room-a floor
# found: examples/adventure-4/maze/CONTAINER.yml#defaults.room  via defaults: (enclosing container)
#   floor = 'uneven flagstones'
python3 skills/prototype/scripts/resolve.py lookup <object> <slot> --all   # every container that has it
```

The adventure linter (`skills/adventure/adventure.py`) treats a directory with `CONTAINER.yml`
as a scope, so rooms under it don't trigger "directory has room children but no ROOM.yml".
The adventure compiler (`compile.py`) doesn't apply `defaults:` yet: a compiled room has
only the slots its own file states.

## Methods

| Method | Does |
|---|---|
| CREATE | Write a CONTAINER.yml stating what differs from the prototype, for a directory that groups things |
| DEFAULT | Add a default for one kind of child; check with `resolve.py lookup` that it reaches them |
| TRACE | Say which container a value came from (`resolve.py lookup --all`) |

## Related patterns

- **Prototype delegation** (Self, JavaScript): parents an object names. Containers are the
  other axis: values that come from where an object is.
- **Lexical scope** (Lisp, JavaScript): inner scopes see outer bindings.
- **The CSS cascade**: values flow from ancestors, nearer rules win.
- **XML namespaces**: context flows through the tree.

## Credits

- **OpenLaszlo**: the `<node>` element as a non-visual scope
- **Self**: delegation without classes
- **CSS**: the cascade

## Part of MOOLLM

**This skill's directory (browse and fetch everything):** [skills/container/](https://github.com/SimHacker/moollm/tree/main/skills/container)

- **MOOLLM:** [repo](https://github.com/SimHacker/moollm) · **Skill index and docs:** [skills/README](https://github.com/SimHacker/moollm/blob/main/skills/README.md)
