# Compiling examples/adventure-4 to adventure.json

The compiler is `skills/adventure/adventure.py`. `compile` lints the adventure, and when that lint has zero ERROR events it calls `export_runtime_json` and writes `adventure.json`, `index.html`, and a copy of `adventure.js` into the output directory.

From the repo root:

```
python3 skills/adventure/adventure.py compile examples/adventure-4/ --output build/
```

`--output` is the directory. The JSON name is always `adventure.json` inside it, so that command writes `build/adventure.json` relative to the current directory. With no `--output`, the directory is `<adventure>/build/`, which for this tree is `examples/adventure-4/build/`.

Module docstring (`skills/adventure/adventure.py`):

```
adventure.py: Lint and compile MOOLLM adventures.

Sniff the end of this file for the tribute stash and lineage notes.

Usage:
  python adventure.py lint <adventure-path> [options]
  python adventure.py compile <adventure-path> [options]
  python adventure.py merge <adventure-path> <state.json> [options]
  python adventure.py serve <adventure-path>

Examples:
  python adventure.py lint examples/adventure-4/ --format yaml --dump
  python adventure.py compile examples/adventure-4/ --output build/
```

`cmd_compile` docstring:

```
Compile an adventure to a web application.

Generates:
- adventure.json — Compact runtime JSON for browser/Node
- index.html — Standalone playable page
- Copies adventure.js runtime

The JSON contains ONLY what the runtime needs:
- Rooms with exits and progressive descriptions (glance/look/example/examine)
- Objects with advertisements, compiled JS/PY
- Characters with inventory, location
- Initial flags and starting room

Rooms synthesize from ROOM.yml + README.md. Objects and characters
describe themselves; rooms do not duplicate artifact descriptions.
All extra YAML Jazz (comments, metadata, design docs) stays in YAML.
The runtime gets a lean, fast, stripped-down view.
```

The usage text printed when `cmd_compile` is called with no path (argparse requires `path`, so `compile --help` does not print this):

```
Usage: adventure.py compile <adventure-path> [options]

Options:
  --output DIR    Output directory (default: <adventure>/build/)
  --standalone    Include runtime in output (no external deps)

Example:
  adventure.py compile examples/adventure-4/
  adventure.py compile examples/adventure-4/ --output ./build/
```

`python3 skills/adventure/adventure.py compile --help` prints:

```
usage: adventure.py compile [-h] [--output OUTPUT] [--standalone] path

positional arguments:
  path             Adventure directory path

options:
  -h, --help       show this help message and exit
  --output OUTPUT  Output directory
  --standalone     Embed runtime in HTML
```

`compile` has no dry-run. `--dry-run` belongs to `merge`.

`skills/adventure/compile.py` is a different program. Its default output is `build/world.json`. Repo-root `build/world.json` is present (6 Sep 2026, 17:17, 3336891 bytes) and is gitignored. It is not `adventure.json`.

## Does build/adventure.json exist?

Repo-root `build/adventure.json` does not exist. `.gitignore` ignores `build/`, with an exception for `examples/adventure-4/build/`. That path is not in HEAD.

`examples/adventure-4/build/adventure.json` exists.

- Filesystem mtime: 10 Oct 2026, 12:01:57
- Size: 155973 bytes
- `generated` inside the JSON: `2026-01-10T10:06:27.098035`
- Last commit that touched the path: `99ad167c`, 27 Jan 2026, "Expand Lane Neverending slideshow and assets."

The October mtime is later than both the `generated` field and that commit. `git diff HEAD -- examples/adventure-4/build/adventure.json` is empty and the blob size matches, so the file on disk is the HEAD blob.

## Compare against HEAD without a long compile

Diffing the tracked file needs no compile, and the diff is empty. That compares the checked-in snapshot to itself.

A new compile of the current `examples/adventure-4` tree is a full lint of that tree, then a write. There is no flag that emits `adventure.json` without that walk. `cmd_compile` writes the file only when the lint has zero ERROR events. A non-standard `mind_mirror` property is an ERROR (`INVALID_SCHEMA`, "not in Leary 32"), so a lint that still reports those errors exits before writing a JSON to diff.

Repo-root `build/adventure.json` has no HEAD blob. A compile with `--output build/` from the repo root would land in the gitignored `build/` directory, and `git diff HEAD` cannot see it.

`export_runtime_json` puts advertisements on each object and copies every key of each advertisement entry (defaults first, then the entry; `condition` fills `guard` when `guard` is absent). It does not write `methods` onto the object. A diff of `adventure.json` cannot show a lost method key.

## Advertisement and method keys

`skills/adventure/test_advertisement_shapes.py` covers both, on a one-room fixture, through `normalize_advertisements`, `export_advertisement`, the linter's `COMPILE_EXPRESSION` events, and `export_runtime_json`. It does not compile `examples/adventure-4`.

From the repo root:

```
python3 skills/adventure/test_advertisement_shapes.py
```

That run: 20 tests, OK, 0.020s.

Module docstring:

```
test_advertisement_shapes.py — advertisement normalization in the adventure compiler.

Run with: python3 test_advertisement_shapes.py
Or: python3 -m unittest test_advertisement_shapes -v
```

The second form is run from `skills/adventure/`. The script puts its own directory on `sys.path`, so the first form works from the repo root as `python3 skills/adventure/test_advertisement_shapes.py`.

`LinterAndExport` docstring:

```
A list-form object still gets its method and advertisement checks, and exports by name.
```

`export_advertisement` docstring:

```
Runtime JSON for one advertisement: engine fields with their defaults,
then every key of the entry. condition: also fills guard: when the entry
has no guard.
```

The method checks assert linter fields: `methods.BLINK.effect` targets `methods.BLINK.effect_js` and `methods.BLINK.effect_py`; a string method `methods.STARE` targets `methods_js.STARE`. The export check asserts advertisement names `SPEAK-TO` and `ON-HELLO` and that `action`, `result`, `trigger`, and `guard` survive into the runtime JSON.
