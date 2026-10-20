# Lookup fixture

A tiny object graph for [scripts/resolve.py](../../scripts/resolve.py) and its test. Each
directory is an object; `OBJECT.yml` holds its slots and its `inherits:` list.

```
animal              describe, legs, sound
pet      → animal   describe, owner
cat      → pet, animal, "Garfield, the comic-strip cat"   sound
sleepy   (a mood)   sound, energy
biscuit  → traits*: cat, mood*: sleepy                     name
loop-a   ↔ loop-b   a cycle
experiment/skills/run        a skill owned by one experiment
experiment/runs/first/RUN.yml   inherits it by filename
garden/ROOM.yml     a flat room with embedded objects
garden/GLANCE.yml   a view of the garden
```

What it shows:

| Lookup | Result | Why |
|---|---|---|
| `biscuit name` | biscuit | own slot |
| `biscuit sound` | cat | `traits*` is declared before `mood*`, first match wins |
| `biscuit sound --all` | cat, then sleepy and animal shadowed; Self-4 ambiguity flagged | cat and sleepy are unrelated, so Self 4 would refuse |
| `biscuit describe` | pet | depth-first: cat → pet before cat → animal |
| `biscuit energy` | sleepy | only the second named parent has it |
| `cat catchphrase` | not found; the latent parent "Garfield, the comic-strip cat" is listed | no file defines it; the LLM tier would answer from what it knows about Garfield |
| `loop-a x` | not found, cycle reported | cycles are skipped, not followed forever |
| `experiment/runs/first/RUN.yml trials` | experiment/skills/run | `RUN.yml` implies the nearest `run` skill; this experiment owns one |
| `garden/GLANCE.yml exits` | garden | a view's `subject*` is its directory |
| `garden/ROOM.yml#objects.gnome sound` | cat | an embedded object, addressed by path, with its own `inherits:` |
| `garden/ROOM.yml#objects.bench` parents | object (implied) | the collection key `objects` implies `skills/object` |

Run from the repo root:

```bash
python3 skills/prototype/scripts/resolve.py lookup skills/prototype/examples/lookup/biscuit sound --all
python3 skills/prototype/scripts/resolve.py parents skills/prototype/examples/lookup/biscuit
python3 skills/prototype/scripts/test_resolve.py
```
