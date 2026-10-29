# Methods: one core, three dialects

Round 2 of the vocabulary analysis, looking inside each `methods:` entry. Numbers from
`python3 skills/prototype/scripts/behavior_survey.py methods` plus ad-hoc counts recorded
here (2026-10-29). Canonical form: [../SCHEMA.md](../SCHEMA.md) ("`methods:` map").

## Populations

| Population | Blocks | Entries | Entry shape | Names |
|---|---|---|---|---|
| Cards (`skills/*/CARD.yml`) | 118 map, 3 list (skill-log, skill-snitch, skill-test) | 759 | 748 map, 11 string (content-rescue, showboat) | 741 UPPER, 18 lower (file-system-object, society-of-mind, biome) |
| Prototypes (`skills/{room,character,...}/*.yml`) | map | ROOM 5, CHARACTER 11 | map {signature, does} | UPPER |
| World (`examples/**`) | map | 444 | all map | mixed; engine expects lower |

## The dialects

**Card dialect** (the bulk): a command a player or model types.

```yaml
SUMMON:
  description: "Call an agent into the room"
  signature: "SUMMON <agent> [AS <role>]"
  parameters: { agent: "who", role: "optional costume" }
  output: chat + state-change
  invoked_by: [player, npc]
  effect: "Agent appears with its card loaded"
```

**Prototype dialect**: the same, with `does:` where cards say `description:`.

```yaml
# skills/room/ROOM.yml
LOOK: { signature: "LOOK (AT [thing])", does: "Describe the room or a thing in it" }
```

**Engine dialect**: a function body the compiler turns into JS/PY.

```yaml
methods:
  consume_fuel: "Reduce fuel by n; if empty set lit to false"
methods_js: { consume_fuel: "..." }
methods_py: { consume_fuel: "..." }
```

`_check_methods` in `skills/adventure/adventure.py` only looks at string entries ("1:1 MAPPING:
method name in YAML = method name in JS/PY"). Every one of the 444 world method entries is a
map, so the compiler checks none of them. World entries carry `description` 431, `effect` 342,
`parameters` 237, `returns` 79: the card dialect, sitting where the engine expects its own.

## Field census (cards)

| Field | Count | Shape | Notes |
|---|---|---|---|
| `description` | 470 | prose | `does` (20) means the same; never both on one entry |
| `output` | 382 | free text | 126 distinct after stripping parentheticals; see below |
| `parameters` | 379 | 379 map name→prose, 14 list | `params` 14, `args` 16, `input` 5 are synonyms |
| `signature` | 294 | string | 224 start with the method name; 70 don't (`PSIBER_ENTER` → `ENTER ...`, biome's shell commands) |
| `invoked_by` | 286 | list | player 178, any 21, self 16, moderator 15, operator 12, dm 12, customer 11 |
| `effect` | 266 | prose | world-state change, same word as advertisements |
| `note` | 115 | prose | jazz |
| `returns` | 50 | prose/map | overlaps `output` |
| `satisfies` | 26 | list | Sims motives, same word as advertisements |
| `customers` | 26 | list | overlaps `invoked_by` |
| long tail | ~40 keys | | `example(s)`, `category`, `composes_with`, `protocol`, `variants`, `emits`, `delegates_to`, `auth`, `gate`, `modes`, `dispatch`, `invoke_when` ... |

### `output` vocabulary

```
138 chat            42 chat+state-change    38 state-change     18 file+chat
 11 file             6 chat+state-changes    4 state-change+chat 3 state-changes
  2 chat+file        2 yaml                  2 transport-task    2 terminal  + 114 rarer values
```

The head is a channel set over three or four values: `chat`, `state-change`, `file`. Order
and plurals vary. The tail mixes channel with content ("chat (ranked list)", "yaml report").

### Names

UPPERCASE names are commands, the text-adventure verb a player types. Lowercase names are
code-callable functions (engine) or protocol steps (biome's `instantiate`, `register`;
file-system-object's `parse`, `validate`). The case already carries a distinction, and nobody
has written it down.

## Defects found

1. The compiler skips every map-form method (all 444 world entries). Methods that have a
   prose `effect:` and parameters never get JS/PY.
2. `does:` (prototypes, 20 card entries) and `description:` (470) are one field.
3. 11 string-form card methods and 3 list-form method blocks can't be read by anything that
   expects the card dialect.

## Proposed core

Every method entry, card or world, is a map that may use these and should not use synonyms
for them:

| Field | Meaning | Absorbs |
|---|---|---|
| `description` | what it does, one line | `does`, `summary`, `doc` |
| `signature` | how it is called, starting with the method name | `syntax`, `call`, `invocation` |
| `parameters` | map name → prose | `params`, `args`, `input` (and list forms become maps) |
| `effect` | prose, what changes in the world | |
| `output` | list from {chat, state-change, file}, plus prose in `returns` | |
| `returns` | prose or map, the value handed back | |
| `invoked_by` | list of roles | `customers` |
| `satisfies` | list of motives | |
| `body` | prose the compiler turns into `body_js` / `body_py` | the engine's string form |

Everything else on a method stays as YAML Jazz: `note`, `example(s)`, `variants`, `metaphor`,
`delegates_to`, `gate`, and the rest. They are object-specific and read by models.

## Options

- **Engine shape.** (a) The engine accepts the map form and compiles `body:` (or `effect:` when
  there is no body) to `body_js`/`body_py` inside the entry, like advertisements' `guard_js`.
  (b) Keep string methods for engine functions and map methods for commands, documented as two
  kinds. (a) removes the sibling `methods_js:`/`methods_py:` maps and matches advertisements.
- **Case.** (a) Document it: UPPER for commands, lower for functions and protocol steps.
  (b) Make everything UPPER. (a) records a distinction the files already make.
- **`output`.** (a) A list over a closed set {chat, state-change, file}, detail in `returns`.
  (b) Leave free text. (a) is mechanical for 262 of 382 entries.
- **`invoked_by` and `customers`.** Merge into `invoked_by`. `customers` appears in two cards
  (github, trekify) and names who calls the method, the same as `invoked_by`.

## Leanings

- The proposed core, as above (75%).
- Engine shape (a) (70%); it depends on whether `adventure.js` can read entry-level `_js`
  fields, which it already does for advertisements.
- Case (a) (80%).
- `output` (a) (60%); the tail carries meaning that `returns` must absorb.
- `does` → `description` in prototypes and cards (90%).
