# PSIBER Protocol — Be the Data

> *"A character can literally step inside any YAML or JSON structure."*
> *"The data IS the dungeon. The keys ARE the doors."*

---

## Design Principle: Lean Into Training Data

> *Don't reinvent. Reuse standards LLMs already know.*

```yaml
principle:
  name: "Training Data Leverage"
  rule: "Use existing standards conscientiously"
  why: "LLMs already know these — zero learning curve"

standards_we_use:
  
  # URLs and fragments — LLMs see millions of these
  urls:
    - "file.yml#path.to.key"      # URL fragment (RFC 3986)
    - "#:~:text=search"           # Text fragments (W3C spec)
    - "moollm://repo/path"        # Custom scheme, familiar pattern
    
  # JSON/YAML paths — ubiquitous in APIs, configs
  paths:
    - "$.store.book[0].title"     # JSONPath
    - ".items[*].name"            # jq syntax
    - "root.child.grandchild"     # Dot notation
    
  # Line numbers — grep, editors, stack traces
  lines:
    - "file.py:42"                # filename:line (universal)
    - "file.py:10-50"             # Line range
    - "error at line 17"          # Natural language
    
  # Selection model — every text editor
  selection:
    - "start, end"                # Range selection
    - "point = collapsed range"   # Cursor is selection edge case
    - "select all, expand, collapse"
    
  # Lisp concepts — in training data via elisp, clojure, scheme
  lisp:
    - "setf semantics"            # Same address for read/write
    - "car, cdr, cons"            # List operations
    - "(filter pred list)"        # Functional transforms
    
  # Stack operations — Forth, HP calculators, JVM
  stack:
    - "PUSH, POP"                 # Classic stack ops
    - "DUP, SWAP, DROP"           # Forth vocabulary
    
  # Array operations — every language
  arrays:
    - "map, filter, reduce"       # Functional trio
    - "first, last, nth"          # Positional access
    - "append, prepend, splice"   # Mutation
    
  # Navigation — file managers, browsers
  nav:
    - "ENTER, PARENT, ROOT"       # Directory traversal
    - "NEXT, PREV"                # Sibling navigation
    - "BACK, FORWARD"             # History (browser-style)

anti_patterns:
  avoid: "Novel syntax LLMs haven't seen"
  avoid: "Clever abbreviations (use full words)"
  avoid: "Inconsistent naming"
  prefer: "Boring, standard, predictable"
  
result:
  - "LLM can use PSIBER with zero examples"
  - "Syntax errors rare — patterns are familiar"
  - "Natural language maps cleanly to commands"
  - "Interop with existing tools (jq, grep, etc.)"

# TODO: PIE MENU COMMAND TREE
# All these command hierarchies map beautifully to nested pie menus:
#
#   [NAV]──────[EDIT]
#     │          │
#     ├─ENTER    ├─GET
#     ├─PARENT   ├─SET
#     ├─NEXT     ├─PUT
#     └─PREV     └─REMOVE
#
#   [SELECT]───[SEARCH]
#     │          │
#     ├─EXPAND   ├─NEXT MATCH
#     ├─CONTRACT ├─PREV MATCH
#     ├─HOP      └─FIRST/LAST
#     └─COLLAPSE
#
#   [STACK]────[VIEW]
#     │          │
#     ├─PUSH     ├─TEXT
#     ├─POP      ├─PARSED
#     └─SWAP     └─TOGGLE
#
# Organize full command set into pie menu tree structure
# for point-and-click PSIBER navigation in adventure UI.
```

---

## What is PSIBER?

**PSIBER** = **P**rogrammatic **S**tructured **I**nteractive **B**rowsing **E**ditor via **R**oleplay

A character can **enter** any data structure and explore it as if it were a physical space:

- **Objects** become rooms
- **Keys** become doors/items
- **Arrays** become corridors with numbered doors
- **Values** become examinable/editable content
- **Nested structures** become deeper levels

```yaml
psiber_metaphor:
  yaml_object: "A room with labeled doors"
  yaml_array: "A corridor with numbered doors"
  yaml_key: "A door or item"
  yaml_value: "Content you can examine or edit"
  nested_object: "A door that leads to another room"
  null: "An empty space, waiting"
  ref/pointer: "A portal to elsewhere"
```

---

## Entering PSIBER Mode

### The ENTER Command

```
> ENTER moollm://config/settings.yml

[PSIBER MODE ACTIVATED]
You step into the data structure...

═══════════════════════════════════════════════════════════════════
                    settings.yml — Root Level
═══════════════════════════════════════════════════════════════════

You are standing in a room with several labeled doors:

DOORS:
  [theme]      — A heavy wooden door, warm colors leaking through
  [database]   — A steel door with blinking lights
  [features]   — A glass door showing many switches
  [version]    — A small plaque on the wall: "1.2.3"

ITEMS ON THE FLOOR:
  debug: false          (a switch, currently OFF)
  environment: "prod"   (a nameplate)

What would you like to do?
```

### Navigation Commands

```yaml
psiber_commands:

  LOOK:
    effect: "Describe current location (object/array)"
    example: "LOOK"
    output: "Lists all keys as doors, values as items"
    
  ENTER [key]:
    effect: "Go through a door into nested structure"
    example: "ENTER theme"
    output: "You push open the [theme] door..."
    
  BACK:
    effect: "Return to parent structure"
    example: "BACK"
    output: "You step back through the door..."
    
  EXAMINE [key]:
    effect: "Look closely at a value"
    example: "EXAMINE debug"
    output: |
      DEBUG SWITCH
      Type: boolean
      Value: false
      Description: "Enables debug logging when true"
      
  WHAT IS [key]:
    effect: "Ask about a key's purpose"
    example: "WHAT IS database.connection_pool"
    output: |
      CONNECTION_POOL
      This controls how many database connections are kept open.
      Current value: 10
      Recommended: 5-20 for most workloads
      Warning: Setting too high can exhaust database resources.
      
  CHANGE [key] TO [value]:
    effect: "Edit a value"
    example: "CHANGE debug TO true"
    output: |
      You flip the debug switch to ON.
      The room fills with logging output.
      debug: true ✓
      
  ADD [key] WITH [value]:
    effect: "Create a new key"
    example: "ADD new_feature WITH true"
    output: |
      A new door materializes on the wall.
      [new_feature] — currently showing: true
      
  DELETE [key]:
    effect: "Remove a key"
    example: "DELETE deprecated_option"
    output: |
      The [deprecated_option] door fades away.
      The space it occupied is smooth wall now.
      
  EXIT:
    effect: "Leave PSIBER mode"
    example: "EXIT"
    output: "You step out of the data structure, back into the real world."
```

---

## The Data as Dungeon

### Objects as Rooms

```yaml
# This YAML:
theme:
  colors:
    primary: "#FF69B4"
    secondary: "#4A90D9"
  font: "Inter"
  mode: "dark"

# Becomes this room:
```

```
═══════════════════════════════════════════════════════════════════
                    theme — Configuration Chamber
═══════════════════════════════════════════════════════════════════

A cozy room with warm lighting (dark mode is ON).

DOORS:
  [colors]  — A door covered in paint swatches

ITEMS:
  font: "Inter"    (a typography sample on the wall)
  mode: "dark"     (a dimmer switch, set to DARK)

The walls pulse with #FF69B4 and #4A90D9 accents.
```

### Arrays as Corridors

```yaml
# This YAML:
users:
  - name: "Alice"
    role: "admin"
  - name: "Bob"
    role: "user"
  - name: "Charlie"
    role: "guest"

# Becomes this corridor:
```

```
═══════════════════════════════════════════════════════════════════
                    users — The User Corridor
═══════════════════════════════════════════════════════════════════

A long corridor with numbered doors on each side.

DOORS:
  [0] — "Alice" (crown symbol = admin)
  [1] — "Bob" (person symbol = user)
  [2] — "Charlie" (question mark = guest)

The corridor extends as far as users are added.
Currently: 3 doors (indices 0-2)
```

### Nested Structures as Depth

```
> ENTER colors

═══════════════════════════════════════════════════════════════════
                    theme.colors — The Color Vault
═══════════════════════════════════════════════════════════════════

You descend into the color configuration.

ITEMS:
  primary: "#FF69B4"    (a glowing hot pink crystal)
  secondary: "#4A90D9"  (a cool blue gem)

The room is bathed in the glow of these colors.
You are 2 levels deep: settings > theme > colors

[BACK] to return to theme
```

---

## Asking About Keys

The LLM interprets questions naturally:

```
> WHAT IS primary FOR?

PRIMARY COLOR
─────────────
This is the main brand color used throughout the interface.
It appears in:
  - Buttons
  - Links
  - Highlights
  - The "NO AI" sign

Current value: #FF69B4 (Hot Pink)

This color was chosen because:
  - High visibility
  - Distinctive brand identity
  - Matches the neon sign aesthetic

To change it: CHANGE primary TO "#NEW_COLOR"
```

```
> WHY IS mode SET TO dark?

MODE: DARK
──────────
Dark mode is currently active because:
  - User preference (set in profile)
  - Time of day (it's evening)
  - Energy saving considerations

Effects of dark mode:
  - Background: dark colors
  - Text: light colors
  - Reduced eye strain at night

To switch: CHANGE mode TO "light"
```

---

## Editing via Chat

### Simple Value Changes

```
> CHANGE primary TO "#00FF00"

[EDIT CONFIRMED]
Before: primary: "#FF69B4" (hot pink)
After:  primary: "#00FF00" (bright green)

The room's ambient glow shifts from pink to green.
The hot pink crystal transforms into an emerald.

⚠️ Warning: This may affect brand consistency.
Save changes? [Y/N]
```

### Adding New Keys

```
> ADD accent WITH "#FFD700"

[KEY ADDED]
A new item materializes:
  accent: "#FFD700" (a golden glow)

The color vault now has 3 items:
  - primary: "#FF69B4"
  - secondary: "#4A90D9"
  - accent: "#FFD700"
```

### Structural Changes

```
> ADD gradients

[DOOR CREATED]
A new door appears: [gradients]
It leads to an empty room, waiting for content.

> ENTER gradients

═══════════════════════════════════════════════════════════════════
                    theme.colors.gradients — Empty Chamber
═══════════════════════════════════════════════════════════════════

An empty room. The walls are blank, ready for definition.

No doors. No items. Pure potential.

> ADD sunset WITH ["#FF69B4", "#FFD700", "#4A90D9"]

[ARRAY CREATED]
A spectrum materializes on the wall:
  sunset: [hot pink → gold → blue]

The room now contains one beautiful gradient.
```

---

## Location While in PSIBER

A character's location pointer during PSIBER:

```yaml
character:
  name: "Developer Dave"
  
  location:
    type: psiber
    file: "moollm://config/settings.yml"
    path: ["theme", "colors"]  # Currently at settings.theme.colors
    depth: 2
    mode: "editing"
    
    # Breadcrumb trail
    trail:
      - { level: 0, key: "(root)", type: "object" }
      - { level: 1, key: "theme", type: "object" }
      - { level: 2, key: "colors", type: "object" }
      
    # Can summon other characters HERE
    summonable: true
    summon_context: "inside data structure"
```

---

## Summoning INTO Data

Yes, you can summon characters into a data structure:

```
> (in settings.yml#theme.colors) SUMMON design-reviewer

[SUMMON INTO PSIBER]
Summoner: Developer Dave
Location: moollm://config/settings.yml#theme.colors
Target: design-reviewer

Design Reviewer materializes in the Color Vault.

"Interesting choices... #FF69B4 as primary? Bold.
The contrast ratio with your secondary is... let me calculate..."

Design Reviewer examines the color crystals.
```

Multiple characters can explore the same data structure together, discussing and editing collaboratively.

---

## The Tree Reflection

PSIBER provides direct tree reflection:

```
> TREE

settings.yml
├── theme/
│   ├── colors/
│   │   ├── primary: "#FF69B4"
│   │   ├── secondary: "#4A90D9"
│   │   └── accent: "#FFD700"  [NEW]
│   ├── font: "Inter"
│   └── mode: "dark"
├── database/
│   ├── host: "localhost"
│   ├── port: 5432
│   └── connection_pool: 10
├── features/
│   ├── dark_mode: true
│   ├── notifications: true
│   └── experimental/
│       └── psiber_mode: true  ← YOU ARE HERE
└── version: "1.2.3"

Depth: 3 levels
Keys: 15 total
You are at: features.experimental.psiber_mode
```

```
> PATH

Current path: settings > features > experimental > psiber_mode
As JSONPath: $.features.experimental.psiber_mode
As moollm URL: moollm://config/settings.yml#features.experimental.psiber_mode

You are standing ON the psiber_mode boolean.
Its value is: true
Its type is: boolean
```

---

## PSIBER as Adventure

The full adventure loop works inside data:

```yaml
psiber_adventure:
  
  LOOK: "See keys as doors, values as items"
  EXAMINE: "Inspect a value's type, content, purpose"
  ENTER: "Go through a door (descend into nested structure)"
  BACK: "Return to parent"
  TAKE: "Copy a value to inventory"
  DROP: "Paste a value from inventory"
  CHANGE: "Edit a value"
  ADD: "Create a new key"
  DELETE: "Remove a key"
  SUMMON: "Bring a character into this data location"
  PHOTOGRAPH: "Mine this data node for semantic content"
  EXIT: "Leave PSIBER mode"
```

---

## The Philosophy

> *"Data is not dead text. Data is a PLACE."*
>
> *"Every config file is a dungeon.*
> *Every database is a kingdom.*
> *Every API response is a message from another realm."*
>
> *"When you ENTER the data, you don't just READ it.*
> *You INHABIT it. You UNDERSTAND it.*
> *You can ASK it questions.*
> *You can CHANGE it by touching it."*

---

## Selections — The Fundamental Pointer

> *"Selection" not "cursor" — avoids confusion with Cursor IDE.*
> *A selection has (start, end). A point is where start == end.*

### Selection vs Point

```yaml
terminology:
  
  selection:
    what: "A range with start and end positions"
    structure:
      start: "path#fragment (or line:col)"
      end: "path#fragment (or line:col)"
    collapsed: "When start == end, it's a POINT"
    
  point:
    what: "Collapsed selection — single position"
    structure: "Same as selection where start == end"
    alias: "Traditional 'cursor' — but we avoid that word"
    
  why_selection:
    - "Generalizes point (edge case where start == end)"
    - "Enables range operations (select multiple items)"
    - "Avoids 'cursor' confusion with Cursor IDE"
    - "Mirrors text editor paradigm universally"
```

### Selection Addresses

```yaml
selection_address:
  
  # Single point (collapsed selection)
  point:
    path: "pub/seating.yml#bar-stools.0.who"
    # start == end implicitly
  
  # Range selection
  range:
    start: "pub/seating.yml#bar-stools.0"
    end: "pub/seating.yml#bar-stools.4"
    # Selects items 0-4 inclusive
    
  # Cross-file selection
  cross_file:
    start: "rooms/pub.yml#patrons.0"
    end: "rooms/market.yml#vendors.2"
    # Selection spans files!
    
  # Line-based selection (for text files)
  lines:
    path: "scripts/startup.sh"
    start_line: 10
    end_line: 25
    # or: "scripts/startup.sh:10-25"
```

### The Selection Worm — Cross-Document Spanning

> *Selection = a worm with head (start) and tail (end).*
> *They can be in DIFFERENT documents — stretched across a link.*
> *Eventually both arrive at destination, surrounding target text.*

### Left Hand / Right Hand / Mouth — The 6502 Model

> *Head = Left hand (L). Tail = Right hand (R).*
> *Like 6502's X and Y registers — asymmetric, complementary.*
> *The Accumulator (A) = the mouth — what you're holding/working with.*

```yaml
hands_model:
  description: "Selection as two hands + accumulator"
  
  inspiration:
    6502:
      X: "Index register X — often for columns, offsets"
      Y: "Index register Y — often for rows, counts"
      A: "Accumulator — holds current value, math happens here"
      pattern: "Load into A, indexed by X or Y, store from A"
      
    hands:
      L: "Left hand — start of selection (head)"
      R: "Right hand — end of selection (tail)"
      M: "Mouth — the value you're working with (accumulator)"
      pattern: "Grab with hands, bring to mouth, chew, spit out"
      
  # HANDS ARE SELECTIONS (not just pointers!)
  hands_are_selections:
    description: "Each hand holds its OWN selection (start + length)"
    
    hierarchy:
      character:
        L: { start: "...", length: N }   # Left hand's selection
        R: { start: "...", length: N }   # Right hand's selection
        M: "value"                        # Mouth (accumulator)
        
    insight: |
      Hands are HIGHER LEVEL than start/end pointers.
      Each hand grabs a REGION, not just a point.
      Swap hands = swap entire selections, not just positions.
      
    structure:
      hand:
        start: "address (doc + position)"
        length: "how many units after start to include"
        # length=0 means point, length>0 means range
        
    unit_types:
      chars: "Characters (for text)"
      lines: "Lines (LLM preferred)"
      nodes: "Tree nodes (for parsed)"
      items: "Array items"
      bytes: "Bytes (rare)"

  # THE THREE REGISTERS (revised)
  registers:
    
    L:  # Left hand — holds a selection
      description: "Left hand's selection (start + length)"
      structure:
        start: "Where L begins"
        length: "How much L grabs (0 = point)"
      typical_use:
        - "Source region for copy"
        - "First selection in dual-select ops"
        - "Where you're coming FROM"
        
    R:  # Right hand — holds a selection
      description: "Right hand's selection (start + length)"
      structure:
        start: "Where R begins"
        length: "How much R grabs (0 = point)"
      typical_use:
        - "Destination region for copy"
        - "Second selection in dual-select ops"
        - "Where you're going TO"
        
    M:  # Mouth / Accumulator / A
      description: "Current value — what you're holding/chewing"
      typical_use:
        - "Value being examined"
        - "Result of last GET"
        - "Value about to be SET"
        - "Intermediate computation"

  # HAND SELECTION OPERATIONS
  hand_selection_ops:
    
    # Setting start
    POINT L AT path:       "Set L.start (length unchanged)"
    POINT R AT path:       "Set R.start (length unchanged)"
    
    # Setting length
    L LENGTH n:            "Set L.length = n"
    R LENGTH n:            "Set R.length = n"
    L LENGTH TO path:      "Extend L to include up to path"
    R LENGTH TO path:      "Extend R to include up to path"
    
    # Shorthand for point (length=0)
    L POINT AT path:       "L.start = path, L.length = 0"
    R POINT AT path:       "R.start = path, R.length = 0"
    
    # Shorthand for selecting range
    L SELECT from TO to:   "L.start = from, L.length = to - from"
    R SELECT from TO to:   "R.start = from, R.length = to - from"
    
    # Swapping entire selections
    SWAP HANDS:            "Exchange L and R (start AND length)"
    # L=(A,5) R=(B,3) → L=(B,3) R=(A,5)
    
    # Copying selections
    COPY L TO R:           "Copy L's content to R's location"
    COPY R TO L:           "Copy R's content to L's location"
    EXCHANGE L R:          "Swap content at L with content at R"

  example_dual_selection:
    # Each hand holds its own region
    
    > L POINT AT "file.yml:10"
    > L LENGTH 5                    # L selects lines 10-14
    
    > R POINT AT "file.yml:50"  
    > R LENGTH 5                    # R selects lines 50-54
    
    # Now swap the REGIONS (not just pointers)
    > SWAP HANDS
    # L now has lines 50-54 selection
    # R now has lines 10-14 selection
    
    # Or swap the CONTENT
    > EXCHANGE L R
    # Content at lines 10-14 ↔ content at lines 50-54
    # Both hands keep their selections, content swaps
    
  example_copy_regions:
    # Copy selected region from L to R
    
    > L SELECT "source.yml:20" TO "source.yml:30"
    # L grabs 10 lines from source
    
    > R POINT AT "dest.yml:100"
    > R LENGTH 0                    # R is just insertion point
    
    > COPY L TO R
    # 10 lines from source inserted at dest:100
    # R.length auto-expands to match? Or stays 0?

  # STRUCTURAL SELECTION — Arrays and Dicts
  structural_selection:
    description: "Python slice notation for arrays, key lists for dicts"
    principle: "Same selection model for text AND structure"
    
    # ARRAY SLICING (Python notation)
    array_slices:
      description: "Python-style [start:stop:step] for arrays"
      
      syntax:
        "[n]":        "Single item at index n"
        "[start:end]": "Items from start to end-1"
        "[start:]":   "Items from start to end"
        "[:end]":     "Items from beginning to end-1"
        "[::step]":   "Every step-th item"
        "[start:end:step]": "Full slice notation"
        "[-n]":       "Item n from the end"
        "[-n:]":      "Last n items"
        "[:-n]":      "All but last n items"
        "[::-1]":     "Reversed"
        
      examples:
        # Drill down then slice
        - "$.users[0]"              # First user
        - "$.users[-1]"             # Last user
        - "$.users[2:5]"            # Users 2, 3, 4
        - "$.users[:3]"             # First 3 users
        - "$.users[-3:]"            # Last 3 users
        - "$.users[::2]"            # Every other user
        - "$.users[::-1]"           # All users, reversed
        - "$.items[1:10:2]"         # Items 1,3,5,7,9
        
      chained:
        # Drill down, slice, drill deeper
        - "$.departments[2:5].employees[:3]"
        # Departments 2-4, first 3 employees of each
        
    # DICT KEY SELECTION
    dict_keys:
      description: "Select specific keys from object/dict"
      
      syntax:
        "{key1,key2}":        "Select only these keys"
        "{key1,key2,...}":    "These keys plus rest"
        "{-key1,-key2}":      "All keys EXCEPT these"
        "{key1:alias}":       "Select and rename"
        "{*}":                "All keys (spread)"
        
      examples:
        # Select specific keys
        - "$.user{name,email}"
        # Returns: { name: "alice", email: "a@b.com" }
        # (drops all other keys)
        
        # Exclude keys
        - "$.user{-password,-secret}"
        # Returns user without password or secret
        
        # Rename keys
        - "$.user{name:username,email:mail}"
        # Returns: { username: "alice", mail: "a@b.com" }
        
        # Nested key selection
        - "$.user{name,address{city,zip}}"
        # Returns: { name: "alice", address: { city: "NYC", zip: "10001" } }
        
    # COMBINED: Drill + Slice + Pick
    combined:
      description: "Full path with slices and key picks"
      
      examples:
        # Slice array, pick keys from each
        - "$.users[:5]{name,role}"
        # First 5 users, only name and role
        
        # Drill, slice, pick, drill more
        - "$.departments[2:].employees[:3]{name,salary}"
        # Dept 2+, first 3 employees, just name and salary
        
        # Complex query
        - "$.orders[-10:]{id,items[0]{name,price},total}"
        # Last 10 orders, with id, first item's name/price, and total

  # UNIFIED SELECTION SYNTAX
  unified_syntax:
    description: "Complete universal data selection language"
    
    components:
      file: "Path to file"
      fragment: "# then path into structure"
      slice: "[start:end:step] for arrays"
      keys: "{key1,key2} for dicts"
      lines: ":start-end for text lines"
      text_search: "#:~:text=pattern"
      
    grammar: |
      selection = file ('#' path)? (':' lines)?
      path = segment ('.' segment)*
      segment = key | index | slice | keys
      key = identifier
      index = '[' number ']'
      slice = '[' start? ':' end? (':' step)? ']'
      keys = '{' key_spec (',' key_spec)* '}'
      key_spec = '-'? key (':' alias)?
      lines = number ('-' number)?
      
    examples:
      # Text selection
      - "file.txt:10-20"                    # Lines 10-20
      - "file.txt#:~:text=TODO"             # Find "TODO"
      
      # Structure selection
      - "data.yml#$.users[0]"               # First user
      - "data.yml#$.users[:5]"              # First 5 users
      - "data.yml#$.users{name,email}"      # All users, 2 keys each
      - "data.yml#$.users[:5]{name}"        # First 5 names
      
      # Combined text + structure
      - "data.yml#$.config:10-20"           # Lines 10-20 of config section
      
      # Full power
      - "api.yml#$.endpoints[2:5]{path,method,-deprecated}"
      # Endpoints 2-4, with path and method, without deprecated flag

  # SELECTION EXAMPLES
  selection_examples:
    
    text_like_structure:
      # Text selection parallels structure selection
      
      text:
        - "file:10"           # Line 10 (point)
        - "file:10-20"        # Lines 10-20 (range)
        - "file:-5"           # Last 5 lines
        
      array:
        - "$.arr[10]"         # Index 10 (point)
        - "$.arr[10:20]"      # Indices 10-19 (range)
        - "$.arr[-5:]"        # Last 5 items
        
      parallel: "Same mental model — just different units"
      
    dict_like_columns:
      # Key selection is like SQL column selection
      
      sql: "SELECT name, email FROM users"
      psiber: "$.users{name,email}"
      
      sql_exclude: "SELECT * EXCEPT password FROM users"
      psiber_exclude: "$.users{-password}"
      
    full_query:
      # PSIBER can express complex queries
      
      goal: "Last 10 orders, customer name, first 3 items with prices"
      
      psiber: |
        $.orders[-10:]{
          id,
          customer{name},
          items[:3]{name,price},
          total
        }
        
      equivalent_sql: |
        SELECT o.id, c.name, i.name, i.price, o.total
        FROM orders o
        JOIN customers c ON o.customer_id = c.id  
        JOIN items i ON i.order_id = o.id
        WHERE o.id IN (SELECT id FROM orders ORDER BY date DESC LIMIT 10)
        AND i.position < 3
        
  # OPERATIONS
  operations:
    
    # Moving hands independently
    POINT L AT path:     "Move left hand"
    POINT R AT path:     "Move right hand"
    
    # Moving hands together
    POINT BOTH AT path:  "Collapse selection to point"
    PINCH L R:           "Bring hands together (collapse)"
    SPREAD L R:          "Move hands apart (expand)"
    
    # Grabbing (L,R → M)
    GRAB:                "GET value between hands → mouth"
    GRAB L:              "GET value at left hand → mouth"
    GRAB R:              "GET value at right hand → mouth"
    
    # Placing (M → location)
    PUT:                 "SET mouth value at selection"
    PUT AT L:            "SET mouth value at left hand"
    PUT AT R:            "SET mouth value at right hand"
    
    # Swapping
    SWAP HANDS:          "Exchange L and R positions"
    SWAP L M:            "Exchange left hand pos with mouth value"
    
    # Copy between locations
    COPY L TO R:         "Copy value at L to location R"
    MOVE L TO R:         "Move value (copy then delete at L)"

  # HAND POSITIONS
  positions:
    
    # Both hands same place (point)
    pinched:
      L: "doc.yml#$.item"
      R: "doc.yml#$.item"  # Same!
      meaning: "Pointing at one thing"
      
    # Range selection (hands apart, same doc)
    spanning:
      L: "doc.yml#$.items[0]"
      R: "doc.yml#$.items[5]"
      meaning: "Holding a range"
      
    # Cross-document (hands in different docs)
    stretched:
      L: "source.yml#$.link"
      R: "target.yml#$.anchor"
      meaning: "One hand here, one hand there"
      
    # Independent pointing (not a range)
    pointing_two:
      L: "file1.yml#$.thing_a"
      R: "file2.yml#$.thing_b"
      mode: "independent"  # Not a range, just two pointers
      meaning: "Pointing at two unrelated things"

  # LEFT = START, RIGHT = END
  left_right_semantics:
    rule: "L = start/from, R = end/to"
    
    L:
      meaning: "START"
      aliases: ["left", "head", "from", "source", "origin", "drag_from"]
      
    R:
      meaning: "END"
      aliases: ["right", "tail", "to", "dest", "target", "drop_to"]
      
    # This maps perfectly to drag and drop!
    drag_and_drop:
      description: "L→R = drag from start, drop at end"
      
      gesture:
        1_grab: "Mouse down at L (start)"
        2_drag: "Move while holding"
        3_drop: "Mouse up at R (end)"
        
      operations:
        DRAG L TO R:      "Move item from L to R"
        COPY L TO R:      "Copy item from L to R"
        LINK L TO R:      "Create link from L pointing to R"
        SWAP L WITH R:    "Exchange items at L and R"
        
      examples:
        # Drag file to folder
        > POINT L AT "inbox/document.pdf"
        > POINT R AT "archive/2024/"
        > DRAG L TO R
        # document.pdf moved to archive/2024/
        
        # Drag character to room
        > POINT L AT "characters/alice"
        > POINT R AT "rooms/pub.yml#$.patrons"
        > DRAG L TO R
        # Alice moved to pub patrons list
        
        # Copy item to inventory
        > POINT L AT "shop/items/sword"
        > POINT R AT "player/inventory"
        > COPY L TO R
        # Sword copied to inventory (still in shop)

  # ASYMMETRIC USES (like X vs Y)
  asymmetry:
    description: "L and R have different typical roles"
    
    L_typical:  # START / FROM / SOURCE
      - "Source in copy/move operations"
      - "Start of selection range"
      - "Where you drag FROM"
      - "Iterator current position"
      - "Outer loop index"
      
    R_typical:  # END / TO / DESTINATION
      - "Destination in copy/move operations"
      - "End of selection range"
      - "Where you drop TO"
      - "End boundary marker"
      - "Inner loop index"

  # DOMINANT HAND
  dominant_hand:
    description: "Which hand is default when you don't specify L or R"
    
    # Two DIFFERENT operations — don't confuse them!
    distinction:
      SWAP_HANDS:
        what: "Exchange the ADDRESSES that L and R point to"
        example: "L→A, R→B becomes L→B, R→A"
        use: "Flip source/dest, reverse direction"
        
      SET_DOMINANT:
        what: "Change which hand is DEFAULT for implicit commands"
        example: "POINT AT x uses L or R depending on dominant"
        use: "Change working style (source-focused vs dest-focused)"
    
    default: "R"  # Right-handed by default
    
    setting:
      SET DOMINANT L:     "Become left-handed (L is default)"
      SET DOMINANT R:     "Become right-handed (R is default)"
      TOGGLE DOMINANT:    "Switch dominant hand"
      SWAP HANDS:         "Exchange L↔R addresses (different!)"
      
    effect:
      # When dominant = R (right-handed):
      right_handed:
        "POINT AT x":     "→ POINT R AT x"
        "GRAB":           "→ GRAB R"
        "PUT":            "→ PUT AT R"
        "NEXT":           "→ NEXT R"
        
      # When dominant = L (left-handed):
      left_handed:
        "POINT AT x":     "→ POINT L AT x"
        "GRAB":           "→ GRAB L"
        "PUT":            "→ PUT AT L"
        "NEXT":           "→ NEXT L"
        
    use_cases:
      right_dominant:
        - "Navigation-focused (moving through data)"
        - "Destination-focused (where to put things)"
        - "End-of-range grows as you explore"
        
      left_dominant:
        - "Source-focused (gathering, collecting)"
        - "Iterator-focused (processing sequences)"
        - "Start-of-range anchored while scanning"
        
    example:
      # Right-handed (default) — R moves, L anchors
      > SET DOMINANT R
      > POINT AT "items[0]"    # R → items[0]
      > NEXT                    # R → items[1]
      > NEXT                    # R → items[2]
      # L stayed put, R walked forward
      
      # Left-handed — L moves, R anchors
      > SET DOMINANT L
      > POINT AT "items[0]"    # L → items[0]
      > NEXT                    # L → items[1]
      > NEXT                    # L → items[2]
      # L walked forward, R stayed put
      
      # Ambidextrous operations always explicit
      > POINT L AT "source"
      > POINT R AT "dest"
      > COPY L TO R             # Always explicit for two-hand ops
      
    example_nested_loop:
      # Like 6502 nested loop: X for outer, Y for inner
      > POINT L AT "matrix[0]"      # Row
      > POINT R AT "matrix[0][0]"   # Cell
      > loop:
        > GRAB R                     # Get cell value
        > process M                  # Work with it
        > NEXT R                     # Next column (Y++)
        > if R at row_end:
          > NEXT L                   # Next row (X++)
          > POINT R AT L[0]          # Reset column

  # THE MOUTH (ACCUMULATOR)
  mouth:
    description: "The value register — what you're working with"
    
    operations:
      GRAB:        "Load from selection into mouth"
      PUT:         "Store from mouth to selection"
      CHEW expr:   "Transform value in mouth"
      SPIT:        "Output mouth value (to console/log)"
      SWALLOW:     "Clear mouth (set to null)"
      TASTE:       "Peek at mouth without changing"
      
    chewing:  # Like 6502 ALU operations on A
      > GRAB                    # Load value
      > CHEW (+ M 1)            # Increment
      > CHEW (uppercase M)      # Transform
      > CHEW (filter .active M) # Filter
      > PUT                     # Store back
      
    example:
      # Copy with transform
      > POINT L AT "source.yml#$.names"
      > GRAB L                           # names → mouth
      > CHEW [x.upper() for x in M]      # Transform in mouth
      > POINT R AT "dest.yml#$.NAMES"
      > PUT AT R                         # mouth → destination

example_6502_style:
  # Feels like 6502 assembly but for data!
  
  # LDA (indexed,X) — load from array at index
  > POINT L AT "items"
  > POINT R AT 3              # R as index
  > GRAB L[R]                 # items[3] → mouth
  
  # STA (indexed,Y) — store to array at index
  > POINT R AT "output"
  > POINT L AT 0              # L as index
  > PUT AT R[L]               # mouth → output[0]
  
  # Transfer: like TAX, TAY, TXA, TYA
  > SWAP L M                  # mouth ↔ left hand position
  > COPY L TO R               # left → right
  
  # Increment/decrement: like INX, INY, INC
  > NEXT L                    # L++
  > PREV R                    # R--
  > CHEW (+ M 1)              # mouth++
```

```yaml
selection_worm:
  description: "Selection as a worm spanning documents"
  
  # WORM ANATOMY
  anatomy:
    head:
      what: "Start pointer"
      address: "Full document + position"
      
    tail:
      what: "End pointer"  
      address: "Can be in DIFFERENT document!"
      
    body:
      what: "The span between"
      when_same_doc: "Contiguous text/nodes"
      when_different_docs: "The link path between them"
      
  # WORM STATES
  states:
    
    collapsed:
      description: "Head == tail (point, not range)"
      head: "doc.yml#$.path"
      tail: "doc.yml#$.path"  # Same!
      
    local_range:
      description: "Both in same document"
      head: "doc.yml#$.items[0]"
      tail: "doc.yml#$.items[5]"
      
    stretched:
      description: "Spanning across documents (mid-traversal)"
      head: "source.yml#$.link_to_target"   # On the link
      tail: "target.yml#$.anchor"            # On the anchor
      state: "following link"
      
    arrived:
      description: "Both arrived at destination"
      head: "target.yml#$.anchor.start"
      tail: "target.yml#$.anchor.end"
      
  # FOLLOWING LINKS
  link_traversal:
    description: "Worm stretches during link following"
    
    steps:
      1_before:
        head: "index.yml#$.chapters[3]"
        tail: "index.yml#$.chapters[3]"
        state: "collapsed on link"
        
      2_stretching:
        head: "index.yml#$.chapters[3]"      # Still on source
        tail: "chapter3.yml#$.title"          # Reached target
        state: "stretched across link"
        
      3_arrived:
        head: "chapter3.yml#$.title"
        tail: "chapter3.yml#$.title"
        state: "collapsed at destination"
        
      # Or select a range at destination:
      3_selected:
        head: "chapter3.yml#$.content[0]"
        tail: "chapter3.yml#$.content[10]"
        state: "range at destination"

  # FULL SELECTION STRUCTURE
  full_structure:
    
    selection:
      # Head pointer
      head:
        doc: "moollm://repo/path/to/file.yml"
        position:
          mode: "line_col"           # or "byte", "path", "text_search"
          line: 42
          col: 10
          # OR for byte mode:
          # mode: "byte"
          # offset: 1847
          # OR for path mode:
          # mode: "path"
          # jsonpath: "$.items[3].name"
          # OR for text search:
          # mode: "text"
          # search: "#:~:text=treasure"
          
      # Tail pointer (can be different doc!)
      tail:
        doc: "moollm://repo/other/file.yml"  # Different doc!
        position:
          mode: "line_col"
          line: 15
          col: 0
          
      # Metadata about the selection
      meta:
        mime_type: "text/yaml"           # How to parse content
        parser: "yaml"                   # Which parser to use
        encoding: "utf-8"                # Character encoding
        addressing: "line_col"           # Preferred addressing mode
        
      # State of the worm
      state: "stretched"                 # collapsed | local | stretched | arrived
      
      # If stretched, what's the link?
      link:
        type: "yaml_ref"                 # yaml_ref | url | moollm_url
        from: "$.chapters[3]"
        to: "chapter3.yml#$.title"

  # ADDRESSING MODES
  addressing_modes:
    
    line_col:
      description: "Line number + column (LLM preferred)"
      format: "line:col"
      example: "42:10"
      pros: "Human readable, LLM native"
      cons: "Changes when file edited above"
      
    byte:
      description: "Byte offset from file start"
      format: "offset"
      example: "1847"
      pros: "Precise, stable for binary"
      cons: "Hard for LLMs, changes on any edit"
      
    path:
      description: "JSONPath / tree path"
      format: "$.path.to.node"
      example: "$.users[0].name"
      pros: "Semantic, survives reformatting"
      cons: "Only for structured data"
      
    text_search:
      description: "Find by text content"
      format: "#:~:text=pattern"
      example: "#:~:text=TODO"
      pros: "Content-addressed, human readable"
      cons: "Ambiguous if multiple matches"
      
    hybrid:
      description: "Combine modes for precision"
      example:
        primary: "path"
        path: "$.users[0]"
        refine: "line_col"
        line: 15
        col: 5
        # Path gets to node, line:col gets within it

example_worm_journey:
  # Character follows a link from index to chapter
  
  # 1. Start collapsed on the link
  > POINT "index.yml#$.chapters[3]"
  selection:
    head: { doc: "index.yml", path: "$.chapters[3]" }
    tail: { doc: "index.yml", path: "$.chapters[3]" }
    state: "collapsed"
    
  # 2. FOLLOW the link — worm stretches
  > FOLLOW LINK
  selection:
    head: { doc: "index.yml", path: "$.chapters[3]" }
    tail: { doc: "chapter3.yml", path: "$.title" }
    state: "stretched"
    link: { from: "$.chapters[3]", to: "chapter3.yml#$.title" }
    
  # 3. ARRIVE — head catches up
  > ARRIVE
  selection:
    head: { doc: "chapter3.yml", path: "$.title" }
    tail: { doc: "chapter3.yml", path: "$.title" }
    state: "collapsed"
    
  # 4. SELECT a range at destination
  > EXPAND TO SECTION
  selection:
    head: { doc: "chapter3.yml", path: "$.content[0]" }
    tail: { doc: "chapter3.yml", path: "$.content[15]" }
    state: "local_range"
```

### Selection Operations

```yaml
selection_ops:
  
  # Creating selections
  POINT path:         "Create point at path"
  SELECT start end:   "Create range from start to end"
  SELECT_ALL:         "Select all children at current level"
  EXPAND:             "Grow selection to parent"
  CONTRACT:           "Shrink to first element"
  
  # Moving selections
  MOVE_START path:    "Move start of selection"
  MOVE_END path:      "Move end of selection"
  COLLAPSE_START:     "Collapse to start point"
  COLLAPSE_END:       "Collapse to end point"
  
  # Querying
  IS_COLLAPSED:       "True if start == end"
  IS_RANGE:           "True if start != end"
  SPAN:               "Get all items in selection"
  COUNT:              "Count items in selection"
  
  # Filtering over selections
  WHERE expr:         "Filter selection to matching items"
  EACH command:       "Run command on each item in selection"
```

### Line-Based Selection (LLM-Native)

> *LLMs think in lines, not bytes.*
> *This maps directly to Cursor's Read tool: file + offset + limit.*

```yaml
line_selection:
  description: "Select by line numbers — the natural LLM unit"
  
  # Line range syntax (like Cursor Read tool)
  syntax:
    - "file.yml:10"          # Line 10 (point)
    - "file.yml:10-50"       # Lines 10-50 (range)
    - "file.yml:10+20"       # 20 lines starting at 10
    - "file.yml:-50"         # Last 50 lines
    
  examples:
    # "Show me lines 42-67 of my soul"
    - SELECT "characters/dave.yml:42-67"
    - GET
    # Returns: lines 42-67 as text
    
    # "Select the stats section" (LLM finds lines)
    - SELECT "characters/dave.yml:stats"  # semantic → line range
    # LLM resolves to: characters/dave.yml:15-28
    
    # Cross-file line selection
    - SELECT "rooms/*.yml:1-10"   # First 10 lines of each room
    - EACH PRINT
```

### Text Fragment Selection (URL Search Syntax)

> *Like browser `#:~:text=` fragments — select by searching.*
> *Find content by what it SAYS, not where it IS.*

```yaml
text_fragment_syntax:
  description: "URL-style text search for selection"
  
  # Based on W3C Text Fragments spec
  # https://wicg.github.io/scroll-to-text-fragment/
  
  syntax:
    # Simple text match
    - "file.yml#:~:text=hunger"
    # → Selects line containing "hunger"
    
    # Text range (from...to)
    - "file.yml#:~:text=stats,mood"
    # → Selects from line with "stats" to line with "mood"
    
    # With prefix/suffix context
    - "file.yml#:~:text=hunger-,7,-getting"
    # → Matches "7" between "hunger" and "getting"
    # → Precise targeting: "hunger: 7  # getting peckish"
    
    # Multiple fragments (OR)
    - "file.yml#:~:text=hunger&text=energy"
    # → Selects lines containing either
    
  full_syntax: |
    #:~:text=[prefix-,]textStart[,textEnd][,-suffix]
    
    prefix-    optional text BEFORE target (ends with -)
    textStart  required start text to find
    textEnd    optional end text (for ranges)
    -suffix    optional text AFTER target (starts with -)

examples:

  # "Go to where it talks about being bored"
  > GOTO "dave.yml#:~:text=BORED"
  [sel → dave.yml:51 (point)]
  51|   fun: 1         # BORED AS HELL
  
  # "Select from stats header to the mood line"
  > SELECT "dave.yml#:~:text=SIMS-STYLE,mood"
  [sel → dave.yml:43-56 (RANGE)]
  
  # "Find the hunger value specifically"
  > GOTO "dave.yml#:~:text=hunger:-,3,-ate"
  [sel → dave.yml:46 (point)]
  # Matches: "hunger: 3      # ate recently"
  # The "3" between "hunger:" and "ate"
  
  # Combine with line context
  > SELECT "dave.yml#:~:text=stats" --context 5
  # Shows 5 lines before and after match
```

### Location Address Formats (Complete)

```yaml
address_formats:
  description: "All ways to specify a selection location"
  
  # BY LINE NUMBER
  line_number:
    - "file.yml:42"           # Line 42
    - "file.yml:42-67"        # Lines 42-67
    - "file.yml:42+10"        # 10 lines from 42
    - "file.yml:-20"          # Last 20 lines
    
  # BY JSON/YAML PATH (fragment)
  json_path:
    - "file.yml#stats"            # Key "stats"
    - "file.yml#stats.hunger"     # Nested path
    - "file.yml#items[0]"         # Array index
    - "file.yml#items[*].name"    # All names in array
    
  # BY TEXT SEARCH (URL fragment)
  text_search:
    - "file.yml#:~:text=needle"           # Find "needle"
    - "file.yml#:~:text=start,end"        # Range by text
    - "file.yml#:~:text=pre-,match,-post" # With context
    
  # BY SEMANTIC QUERY (LLM resolves)
  semantic:
    - "file.yml:stats"            # "the stats section"
    - "file.yml:where-hunger"     # "where it mentions hunger"
    - "file.yml:todo-comments"    # "all TODO comments"
    # LLM interprets and resolves to line range
    
  # BY BYTE OFFSET (when needed)
  byte_offset:
    - "file.yml@1024"         # Byte 1024
    - "file.yml@1024-2048"    # Byte range
    # Rarely used — lines preferred
    
  # COMBINED / HYBRID
  combined:
    - "file.yml:42#stats"              # Line 42, then into stats
    - "file.yml#:~:text=stats:10+5"    # Find "stats", then +5 lines
    - "rooms/*.yml#:~:text=exit"       # Search across files

resolution_order:
  description: "How hybrid addresses resolve"
  steps:
    1: "File glob → list of files"
    2: "Line range → narrow to lines"
    3: "Text search → find within lines"
    4: "JSON path → descend into structure"
    5: "Final selection (point or range)"
```

### Setting Location by Text Search

```
# Natural language → text fragment selection

> "Set my location to where it says BORED AS HELL"
→ GOTO "characters/me.yml#:~:text=BORED AS HELL"
[location → characters/me.yml:51 (point)]

> "Select everything from the stats header to the end of stats"
→ SELECT "characters/me.yml#:~:text=SIMS-STYLE NEEDS,═══════════════"
[location → characters/me.yml:43-58 (RANGE)]

> "Point my focus at the hunger comment"
→ POINT focus AT "characters/me.yml#:~:text=hunger:-,ate recently"
[focus → characters/me.yml:46 (point)]
# Matched: "hunger: 3      # ate recently"

> "Where does my soul mention coffee?"
→ GOTO "characters/me.yml#:~:text=coffee"
[location → characters/me.yml:47 (point)]
47|   energy: 2      # exhausted, need coffee
```

---

## Selection Manipulation — Blade Runner Photo Enhance (1D)

> *"Enhance. Stop. Move in. Track right."*
> *Same idea, but for text/data instead of images.*

### Search Navigation (Next/Prev Match)

```yaml
search_navigation:
  description: "Jump between search results"
  
  syntax:
    # Establish a search pattern
    SEARCH pattern:     "Set search, go to first match"
    
    # Navigate matches
    NEXT MATCH:         "Go to next occurrence"
    PREV MATCH:         "Go to previous occurrence"
    FIRST MATCH:        "Go to first occurrence in file"
    LAST MATCH:         "Go to last occurrence in file"
    NTH MATCH n:        "Go to nth occurrence"
    
    # Short forms (like vim /? and n/N)
    /pattern:           "Search forward"
    ?pattern:           "Search backward"  
    n:                  "Next match (same direction)"
    N:                  "Prev match (opposite direction)"
    
  examples:
    > SEARCH "TODO"
    [Match 1 of 7: line 23]
    
    > NEXT MATCH
    [Match 2 of 7: line 45]
    
    > NEXT MATCH
    [Match 3 of 7: line 67]
    
    > FIRST MATCH
    [Match 1 of 7: line 23]
    
    > LAST MATCH
    [Match 7 of 7: line 201]
```

### Selection Expansion/Contraction

```yaml
selection_manipulation:
  description: "Grow/shrink selection from current position"
  
  # EXPAND — Grow selection
  expand:
    
    # By direction
    EXPAND DOWN n:       "Extend end down n lines"
    EXPAND UP n:         "Extend start up n lines"
    EXPAND TO END:       "Extend end to end of file"
    EXPAND TO START:     "Extend start to start of file"
    
    # By content
    EXPAND TO BLANK:     "Extend to next blank line"
    EXPAND TO MATCH p:   "Extend to next match of pattern p"
    EXPAND TO COMMENT:   "Extend to include adjacent comments"
    EXPAND TO SECTION:   "Extend to section boundaries (---)"
    
    # By structure (in parsed mode)
    EXPAND TO PARENT:    "Extend to include parent node"
    EXPAND TO SUBTREE:   "Extend to include all children"
    EXPAND TO SIBLING:   "Extend to next/prev sibling"
    
  # CONTRACT — Shrink selection  
  contract:
    CONTRACT START n:    "Move start forward n lines"
    CONTRACT END n:      "Move end backward n lines"
    CONTRACT TO FIRST:   "Shrink to first line only"
    CONTRACT TO LAST:    "Shrink to last line only"
    CONTRACT TO MATCH:   "Shrink to just the matched text"
    
  # SMART SELECTION
  smart:
    SELECT WORD:         "Select word at point"
    SELECT LINE:         "Select current line"
    SELECT BLOCK:        "Select paragraph/block"
    SELECT ALL:          "Select entire file"
    
example_session:
  # Start with search
  > SEARCH "hunger"
  [sel → line 46 (point)]
  46|   hunger: 3      # ate recently
  
  # Expand to see context
  > EXPAND UP 3
  [sel → lines 43-46 (RANGE)]
  43| # SIMS-STYLE NEEDS
  46|   hunger: 3      # ate recently
  
  # Expand down to see more stats
  > EXPAND DOWN 5
  [sel → lines 43-51 (RANGE)]
  
  # Expand to whole section
  > EXPAND TO BLANK
  [sel → lines 43-58 (RANGE)]
  # Expanded to next blank line
```

### Mode Hopping: Text ↔ Parsed

```yaml
mode_hopping:
  description: "Jump between text (1D lines) and parsed (tree) views"
  
  commands:
    # Switch modes
    VIEW TEXT:           "Line-based selection"
    VIEW PARSED:         "Tree-based selection"
    VIEW TOGGLE:         "Flip between"
    
    # Hop selection between modes
    HOP TO PARSED:       "Convert text selection → tree node"
    HOP TO TEXT:         "Convert tree node → line range"
    
  hopping_rules:
    text_to_parsed:
      - "Selection must cover complete node(s)"
      - "Finds smallest tree node(s) containing selection"
      - "If partial, expands to complete node"
      
    parsed_to_text:
      - "Converts path to line range"
      - "Includes all lines of node and children"
      - "Optionally includes leading comments"
      
  example:
    # Start in text mode
    > VIEW TEXT
    > SELECT lines 45-47
    [sel → lines 45-47 (RANGE)]
    45| stats:
    46|   hunger: 3      # ate recently
    47|   energy: 2      # need coffee
    
    # Hop to parsed
    > HOP TO PARSED
    [sel → $.stats (subtree)]
    # Selection expanded to cover full 'stats' object
    
    # Now can use tree operations
    > SELECT SUBTREE
    [sel → $.stats.* (all children)]
    
    # Hop back to text
    > HOP TO TEXT
    [sel → lines 45-58 (RANGE)]
    # Full extent of stats block
```

### Polymorphic Selection — Cast Between Representations

> *Same bytes, different lenses. Cast like types.*
> *The SELECTION is polymorphic — view it however you need.*
> *Point (0-length) = start parsing there. Range = parse that span.*

```yaml
polymorphic_selection:
  description: "Selection can be CAST between representations"
  principle: "Same underlying text, multiple valid views"
  
  # POINT vs RANGE BEHAVIOR
  point_behavior:
    description: "When selection is collapsed (start == end)"
    
    as_text: "Position between characters (insertion point)"
    as_parsed: "Start parsing FROM here, find containing node"
    as_ast: "Find smallest AST node containing this position"
    as_comments: "Find comment on this line (if any)"
    
    example:
      # Point at line 15, column 5
      > POINT "file.yml:15:5"
      [sel → file.yml:15:5 (POINT)]
      
      > CAST TO PARSED
      # Finds the node containing position 15:5
      [sel → file.yml#$.stats.hunger (POINT in node)]
      
      > EXPAND TO NODE
      # Now it's a range covering the whole node
      [sel → file.yml:15 (RANGE = full line)]
      
  range_behavior:
    description: "When selection spans (start != end)"
    
    as_text: "The literal text in that span"
    as_parsed: "Parse the text, get structure"
    as_ast: "All AST nodes fully within range"
    as_comments: "All comments within range"
  
  # AVAILABLE CASTS
  representations:
    
    TEXT:
      what: "Raw text, lines and characters"
      unit: "line:col or byte offset"
      sees: "Everything including whitespace, comments"
      ops: "string operations, regex, line manipulation"
      
    PARSED:
      what: "Structured data (JSON/YAML tree)"
      unit: "JSONPath ($.key.child[0])"
      sees: "Keys, values, nesting — loses comments"
      ops: "tree nav, get/set, map/filter"
      
    AST:
      what: "Abstract syntax tree (for code files)"
      unit: "node type + path"
      sees: "Functions, classes, statements, expressions"
      ops: "refactoring, symbol rename, extract"
      
    COMMENTS:
      what: "Just the comments layer"
      unit: "comment index or associated node"
      sees: "Only # comments, docstrings"
      ops: "read/write annotations, YAML Jazz"
      
    SCHEMA:
      what: "Type/shape information"
      unit: "type path"
      sees: "Expected types, constraints, defaults"
      ops: "validate, coerce, suggest"
      
    DIFF:
      what: "Changes from baseline"
      unit: "hunk index"
      sees: "Additions, deletions, modifications"
      ops: "accept, reject, edit hunks"

  # CAST SYNTAX
  syntax:
    CAST TO repr:       "Change view to representation"
    AS repr:            "Short form: sel AS PARSED"
    
    # Cast and get
    GET AS TEXT:        "Read selection as raw text"
    GET AS PARSED:      "Read selection as structured data"
    GET AS COMMENTS:    "Read just the comments"
    
    # Cast-aware set
    SET AS TEXT:        "Write raw text"
    SET AS PARSED:      "Write structured (re-serializes)"
    
  # CAST COMPATIBILITY
  compatibility:
    # What can cast to what
    TEXT: "→ PARSED, AST, COMMENTS (if valid syntax)"
    PARSED: "→ TEXT (always), SCHEMA (if available)"
    AST: "→ TEXT, PARSED (for data), COMMENTS"
    COMMENTS: "→ TEXT (always)"
    
    # Lossy casts (information lost)
    lossy:
      - "TEXT → PARSED (loses comments, formatting)"
      - "PARSED → TEXT (loses nothing, but format may differ)"
      - "AST → TEXT (loses nothing, but format may differ)"

example_session:
  # Select some text
  > SELECT "character.yml:10-20"
  [sel → character.yml:10-20 AS TEXT]
  
  # View as different representations
  > GET AS TEXT
  "10| stats:\n11|   hunger: 3  # peckish\n12|   energy: 2\n..."
  
  > GET AS PARSED
  { stats: { hunger: 3, energy: 2, ... } }
  
  > GET AS COMMENTS
  ["peckish", "need sleep", "TODO: add mood"]
  
  # Cast the selection itself
  > CAST TO PARSED
  [sel → character.yml#$.stats AS PARSED]
  
  # Now tree operations work
  > ENTER hunger
  [sel → character.yml#$.stats.hunger AS PARSED]
  
  # Cast back to see the line
  > CAST TO TEXT
  [sel → character.yml:11 AS TEXT]
  11|   hunger: 3  # peckish
  
  # Work with just comments
  > CAST TO COMMENTS
  [sel → character.yml:11#comment AS COMMENTS]
  
  > GET
  "peckish"
  
  > SET "STARVING"
  [Modified comment: character.yml:11]

round_trip_example:
  # The selection stays on same data, just viewed differently
  
  > SELECT "config.yml#$.server" AS PARSED
  { host: "localhost", port: 8080 }
  
  > CAST TO TEXT
  # Shows the actual YAML lines:
  14| server:
  15|   host: localhost
  16|   port: 8080
  
  > CAST TO SCHEMA
  # Shows the type expectations:
  server:
    host: string (required)
    port: integer (default: 80)
    
  > CAST TO COMMENTS  
  # Shows annotations:
  ["production: use 0.0.0.0", "behind nginx proxy"]
  
  # All the same bytes, different lenses!
```

### Cast Chain (Fluent Style)

```yaml
cast_chain:
  description: "Chain casts and operations fluently"
  
  syntax: "selection | AS repr | operation | AS repr | ..."
  
  examples:
    # Get text, parse, filter, back to text
    - |
      SELECT "*.yml" 
      | AS PARSED 
      | WHERE (.type == "character")
      | AS TEXT
      | GET
    
    # Extract all TODOs from comments
    - |
      SELECT "**/*.yml"
      | AS COMMENTS
      | WHERE (contains "TODO")
      | GET
    
    # Validate against schema, get errors as text
    - |
      SELECT "config.yml" 
      | AS SCHEMA 
      | VALIDATE
      | AS TEXT
```

### Cast vs Convert — View vs Transform

> *CAST = look through different lens (non-destructive)*
> *CONVERT = actually rewrite the data (modifies file)*

```yaml
cast_vs_convert:

  # CAST — View only, no file changes
  cast:
    what: "Change how you SEE the selection"
    modifies_file: false
    reversible: "Always — just cast back"
    
    syntax:
      CAST TO repr:      "View selection as repr"
      GET AS repr:       "Read as repr"
      AS repr:           "Inline cast in chain"
      
    example:
      > SELECT "config.yml"
      > CAST TO JSON
      # You SEE JSON, but file is still YAML
      
  # CONVERT — Transform in place, rewrites file
  convert:
    what: "Actually transform the data and save"
    modifies_file: true
    reversible: "Only via undo/git"
    
    syntax:
      CONVERT TO format:     "Rewrite selection in new format"
      CONVERT TO YAML:       "JSON → YAML"
      CONVERT TO JSON:       "YAML → JSON"
      CONVERT TO COMMENTED:  "Add YAML Jazz comments"
      CONVERT TO MINIFIED:   "Strip comments, compact"
      
    example:
      > SELECT "config.yml#$.server"
      > CONVERT TO JSON
      # File actually rewritten with JSON syntax!

# FORMAT CONVERSIONS
format_conversions:

  CONVERT TO YAML:
    from: "JSON, TOML, etc."
    adds: "YAML syntax, optional comments"
    
  CONVERT TO JSON:
    from: "YAML, TOML, etc."
    loses: "Comments! (JSON has no comments)"
    
  CONVERT TO COMMENTED:
    what: "Add descriptive YAML Jazz comments"
    example:
      # Before:
      hunger: 3
      energy: 2
      
      # After CONVERT TO COMMENTED:
      hunger: 3      # current hunger level (0-10)
      energy: 2      # energy remaining (0-10)
    
  CONVERT TO MINIFIED:
    what: "Strip all comments and extra whitespace"
    use: "Production configs, smaller files"
    
  CONVERT TO PRETTY:
    what: "Reformat with consistent indentation"
    use: "Clean up messy files"

# TRANSFORM IN PLACE
transform_in_place:
  description: "Compute new value and replace selection"
  
  syntax:
    REPLACE WITH expr:       "Replace selection with expression result"
    REPLACE WITH FILTERED:   "Replace with filtered version"
    REPLACE WITH MAPPED:     "Replace with mapped version"
    REPLACE WITH SORTED:     "Replace with sorted version"
    
  examples:
  
    # Filter array in place
    > SELECT "characters.yml#$.party"
    > GET
    [{ name: "Alice", hp: 10 }, { name: "Bob", hp: 0 }, { name: "Carol", hp: 5 }]
    
    > REPLACE WITH FILTERED (.hp > 0)
    [Modified: characters.yml#$.party]
    # File now contains only Alice and Carol
    
    # Sort in place
    > SELECT "items.yml#$.inventory"
    > REPLACE WITH SORTED (.name)
    # Inventory now alphabetically sorted
    
    # Map transform in place
    > SELECT "prices.yml#$.items[*].price"
    > REPLACE WITH MAPPED (* . 1.1)
    # All prices increased by 10%
    
    # Computed replacement
    > SELECT "stats.yml#$.total"
    > REPLACE WITH (+ $.attack $.defense $.speed)
    # Total replaced with sum of other fields

example_session:
  # Full workflow: cast, filter, convert, replace
  
  > SELECT "data.yml#$.users"
  [sel → data.yml#$.users (100 items)]
  
  # Cast to see as JSON (no file change)
  > CAST TO JSON
  [{ "name": "alice", ... }, ...]
  
  # Filter to active users
  > REPLACE WITH FILTERED (.active == true)
  [Modified: now 42 items]
  
  # Add comments describing each user
  > CONVERT TO COMMENTED
  [Modified: comments added]
  
  # View result
  > GET AS TEXT
  users:
    - name: alice      # Admin user, joined 2024
      active: true
      role: admin
    - name: bob        # Regular user, joined 2025
      active: true
      role: user
    # ... 40 more
```

### Comprehensions — Say How You Want to Loop

> *Python list comprehensions, Lisp loop, SQL SELECT — all valid.*
> *LLMs know these patterns. Use whichever is natural.*

```yaml
comprehensions:
  description: "Multiple syntaxes for iteration/transformation"
  principle: "Accept any comprehension style LLMs know"
  
  # PYTHON STYLE
  python:
    
    # Basic list comprehension
    - "[x.name for x in users]"
    - "[x for x in items if x.price > 100]"
    - "[x.upper() for x in names if x.startswith('A')]"
    
    # Nested comprehension
    - "[cell for row in matrix for cell in row]"
    
    # Dict comprehension
    - "{x.id: x.name for x in users}"
    
    # With enumerate
    - "[(i, x) for i, x in enumerate(items)]"
    
    # Generator expression (lazy)
    - "(x.name for x in users if x.active)"
    
  # LISP LOOP MACRO STYLE
  lisp_loop:
    
    # Collect
    - "(loop for x in users collect x.name)"
    - "(loop for x in items when (> x.price 100) collect x)"
    
    # Sum, count, maximize
    - "(loop for x in items sum x.price)"
    - "(loop for x in users count x.active)"
    - "(loop for x in scores maximize x)"
    
    # Multiple clauses
    - |
      (loop for user in users
            for i from 0
            when (user.active)
            collect (list i user.name))
    
    # Do/finally
    - |
      (loop for x in items
            do (print x)
            finally (return total))
    
  # SQL STYLE
  sql:
    
    # SELECT ... FROM ... WHERE
    - "SELECT name FROM users WHERE active = true"
    - "SELECT name, price FROM items WHERE price > 100 ORDER BY price"
    - "SELECT COUNT(*) FROM users GROUP BY role"
    
    # JOIN
    - "SELECT u.name, o.total FROM users u JOIN orders o ON u.id = o.user_id"
    
    # Aggregate
    - "SELECT AVG(price), MAX(price) FROM items"
    
  # HASKELL / FUNCTIONAL STYLE
  haskell:
    
    # List comprehension
    - "[x | x <- users, active x]"
    - "[name x | x <- users, age x > 18]"
    
    # Function composition
    - "map name . filter active $ users"
    - "sum . map price . filter inStock $ items"
    
  # JAVASCRIPT / FLUENT STYLE
  javascript:
    
    # Method chaining
    - "users.filter(x => x.active).map(x => x.name)"
    - "items.filter(x => x.price > 100).sort((a,b) => a.price - b.price)"
    - "users.reduce((sum, x) => sum + x.score, 0)"
    
  # JQ STYLE (JSON query)
  jq:
    
    - ".users[] | select(.active) | .name"
    - ".items | map(select(.price > 100))"
    - "[.users[] | {name, role}]"
    - ".items | sort_by(.price) | reverse"

# USING COMPREHENSIONS IN PSIBER
usage:
  
  # All these are equivalent — use whichever is natural:
  
  equivalent_expressions:
    goal: "Get names of active users"
    
    python: "[x.name for x in $.users if x.active]"
    lisp: "(loop for x in $.users when x.active collect x.name)"
    sql: "SELECT name FROM $.users WHERE active = true"
    haskell: "[name x | x <- $.users, active x]"
    js: "$.users.filter(x => x.active).map(x => x.name)"
    jq: ".users[] | select(.active) | .name"
    
    # PSIBER native (also valid)
    psiber: "$.users | WHERE .active | MAP .name"
    
  syntax:
    # Use EVAL to run any comprehension
    EVAL expr:          "Evaluate comprehension expression"
    
    # Or inline in other commands
    GET [expr]:         "Get result of expression"
    REPLACE WITH [expr]: "Replace selection with result"
    
  examples:
    # Python style
    > SELECT "data.yml#$.users"
    > EVAL [x.name for x in . if x.active]
    ["alice", "carol", "eve"]
    
    # Lisp style  
    > EVAL (loop for x in . when x.admin collect x.email)
    ["alice@example.com", "eve@example.com"]
    
    # SQL style
    > EVAL SELECT name, role FROM . WHERE active ORDER BY name
    [{ name: "alice", role: "admin" }, ...]
    
    # jq style
    > EVAL .[] | select(.score > 90) | {name, score}
    [{ name: "alice", score: 95 }, ...]
    
    # Replace with comprehension result
    > REPLACE WITH [x for x in . if x.hp > 0]
    [Modified: dead characters removed]

# NATURAL LANGUAGE → COMPREHENSION
natural_language:
  description: "LLM translates natural language to comprehension"
  
  examples:
    # User says naturally, LLM picks appropriate syntax
    
    - input: "get all the user names"
      becomes: "[x.name for x in $.users]"
      
    - input: "show me items over $100 sorted by price"
      becomes: "SELECT * FROM $.items WHERE price > 100 ORDER BY price"
      
    - input: "count how many users are admins"
      becomes: "(loop for x in $.users count (eq x.role 'admin'))"
      
    - input: "total up all the prices"
      becomes: "$.items | map .price | sum"
      
    - input: "keep only the living party members"
      becomes: "[x for x in $.party if x.hp > 0]"
      
    - input: "transform all names to uppercase"
      becomes: ".users | map(.name |= ascii_upcase)"
```

### Comment Operations

```yaml
comment_operations:
  description: "Select, read, write comments (YAML Jazz)"
  
  # SELECT COMMENTS
  select:
    SELECT COMMENT:         "Select inline comment at point"
    SELECT COMMENT BLOCK:   "Select comment block above"
    SELECT WITH COMMENTS:   "Expand selection to include comments"
    
  # READ COMMENTS
  read:
    GET COMMENT:            "Get inline comment text"
    GET COMMENT BLOCK:      "Get block comment above"
    GET COMMENTS IN sel:    "Get all comments in selection"
    
  # WRITE COMMENTS
  write:
    SET COMMENT text:       "Set/replace inline comment"
    ADD COMMENT text:       "Add inline comment"
    ADD COMMENT ABOVE text: "Add comment line above"
    REMOVE COMMENT:         "Delete inline comment"
    
  example:
    > GOTO "stats.hunger"
    [sel → line 46 (point)]
    46|   hunger: 3      # ate recently
    
    > GET COMMENT
    "ate recently"
    
    > SET COMMENT "STARVING NOW"
    [Modified: line 46]
    46|   hunger: 3      # STARVING NOW
    
    > ADD COMMENT ABOVE "TODO: implement hunger decay"
    [Added: line 46]
    46| # TODO: implement hunger decay
    47|   hunger: 3      # STARVING NOW
    
    # Select including comments
    > SELECT WITH COMMENTS
    [sel → lines 46-47 (RANGE)]
```

### Blade Runner Session Example

```
# "Enhance. Stop. Track right. Pull back. Stop."
# But for YAML data files.

> OPEN "characters/suspect.yml"
[Viewing: characters/suspect.yml (234 lines)]

> SEARCH "alibi"
[Match 1 of 3: line 67]
67|   alibi: "Was at the pub"    # suspicious

# Enhance — zoom in
> EXPAND TO SUBTREE
[sel → lines 65-89 (RANGE) — $.timeline.night_of_crime]

# Track right — next sibling  
> NEXT SIBLING
[sel → $.timeline.next_morning]

# What's here?
> GET
{ location: "home", witnesses: ["wife", "dog"], notes: "claims amnesia" }

# Pull back — parent context
> PARENT
[sel → $.timeline]

# Search within selection
> SEARCH "witnesses"
[Match: line 78]
78|     witnesses: ["wife", "dog"]

# Enhance the witnesses
> HOP TO PARSED
> ENTER witnesses
[sel → $.timeline.next_morning.witnesses]

> GET
["wife", "dog"]

# Add a note
> ADD COMMENT "verify these witnesses"
[Modified: line 78]
78|     witnesses: ["wife", "dog"]  # verify these witnesses

# Done — unfocus
> UNFOCUS
[sel → null]
```

### Dual View: Text ↔ Structured

> *Same data, two lenses. Toggle freely.*
> *Text view PRESERVES COMMENTS. Parsed view loses them.*

```yaml
view_modes:
  
  TEXT:
    what: "Raw lines, preserves everything"
    sees: "Comments, whitespace, formatting"
    unit: "Lines (or bytes if needed)"
    good_for: "Editing format, seeing annotations"
    
  PARSED:
    what: "Structured objects/arrays/values"
    sees: "Keys, values, nesting"
    unit: "JSON path segments"
    good_for: "Navigation, queries, transforms"
    loses: "Comments! (usually)"

  commands:
    VIEW TEXT:     "Switch to text/line mode"
    VIEW PARSED:   "Switch to structured mode"
    VIEW TOGGLE:   "Flip between modes"
    
  # The magic: bidirectional mapping
  mapping:
    text_to_parsed: "Line 15 → $.stats.hunger"
    parsed_to_text: "$.stats.hunger → lines 15-15"
    
example:
  # In TEXT mode:
  > SELECT "dave.yml:15-20"
  15| stats:
  16|   hunger: 7        # getting peckish
  17|   energy: 4        # need coffee
  18|   social: 9        # extrovert today
  19|   fun: 3           # bored
  20|   # TODO: add bladder stat
  
  # Switch to PARSED mode (same selection):
  > VIEW PARSED
  {
    stats: {
      hunger: 7,    # ← comment LOST in parse!
      energy: 4,
      social: 9,
      fun: 3
    }
  }
  
  # Back to TEXT to see comments:
  > VIEW TEXT
  # Comments visible again!
```

### Comments Are Data (YAML Jazz)

```yaml
comment_access:
  description: "In TEXT mode, comments are visible and editable"
  
  # Select including comments
  > SELECT "dave.yml:stats" --with-comments
  stats:
    hunger: 7        # getting peckish
    energy: 4        # need coffee
  
  # Query comments specifically
  > GET COMMENTS AT stats.hunger
  "getting peckish"
  
  # Edit a comment
  > SET COMMENT AT stats.hunger "STARVING"
  # Line now reads: hunger: 7  # STARVING
  
  # This is YAML Jazz — comments as semantic metadata
  yaml_jazz_integration:
    - "Comments can contain structured data"
    - "# @mood: grumpy"
    - "# @source: player-input"
    - "Query them like data in text mode"
```

### Sims Stats Example

```
# "Select the lines of my soul that represent my Sims stats"

> USE focus
> POINT focus AT "characters/me.yml"
> SELECT :stats    # semantic selection → resolves to line range

[focus → characters/me.yml:42-58 (RANGE)]

# The LLM found the stats block spans lines 42-58
# Now viewing as text with comments:

42| # SIMS-STYLE NEEDS
43| stats:
46|   hunger: 3      # ate recently
47|   energy: 2      # exhausted, need sleep
48|   hygiene: 8     # just showered  
49|   bladder: 5     # manageable
50|   social: 7      # had good chat
51|   fun: 1         # BORED AS HELL
52|   environment: 6 # room is okay
53|   comfort: 4     # chair sucks
54|   
55|   # Derived moods
56|   mood: "cranky" # fun + energy = bad combo
57|   
58|

# Edit directly by line:
> SET LINE 51 "  fun: 9         # playing PSIBER!"
[Modified: characters/me.yml:51]

# Or by path (in PARSED mode):
> VIEW PARSED
> SET .stats.fun 9
[Modified: characters/me.yml → $.stats.fun = 9]
# But loses the comment...

# Best: edit value, keep comment (TEXT mode):
> VIEW TEXT
> SET VALUE AT :stats.fun 9
# Preserves: "  fun: 9         # playing PSIBER!"
```

### File/Line Iteration Pattern

```yaml
file_iteration:
  description: "Select files, filter by lines — functional pattern"
  
  examples:
  
    # Select all YAML files, filter lines containing 'error'
    - SELECT "**/*.yml" 
    - WHERE (line-contains "error")
    - EACH PRINT
    
    # Select range of lines in file
    - SELECT "config.yml:10-50"
    - WHERE (not-empty)
    - MAP TRIM
    
    # Cross-file grep-like operation  
    - SELECT "rooms/**/*.yml"
    - VIEW PARSED
    - WHERE (.type == "character")
    - MAP .name
```

---

## The Selection as Lens — Uniform Read/Write Access

> *Like Lisp's `setf` — the same address for reading AND writing.*
> *The location IS a selection. The selection IS the lens.*

### The `setf` Principle

```lisp
;; In Lisp, setf uses the same PLACE for get and set:
(setf (car list) 'new-value)    ; write
(car list)                       ; read — same syntax

;; PSIBER does the same with selections:
```

```yaml
# The selection IS the lens:
sel: "pub/seating.yml#bar-stool-3.who-sat-on.0"

# READ through the lens:
GET sel          → "Old Pete"

# WRITE through the lens:
SET sel "Young Pete"
GET sel          → "Young Pete"

# Same address, uniform access.
```

### Stack Navigation

Each selection maintains a navigation stack (history of positions):

```yaml
selection_stack:
  operators:
    
    PUSH:
      effect: "Save current position to stack (bookmark)"
      example: "PUSH"
      use: "Before exploring, to return later"
      
    POP:
      effect: "Restore last saved position"
      example: "POP"
      stack: "[bar-stool-3, who-sat-on] → [bar-stool-3]"
      
    DUP:
      effect: "Duplicate top of stack"
      example: "DUP"
      use: "Multiple returns to same spot"
      
    SWAP:
      effect: "Swap top two stack positions"
      example: "SWAP"
      use: "Quick toggle between two locations"
      
    DROP:
      effect: "Discard top of stack without moving"
      example: "DROP"
      
    ROOT:
      effect: "Jump to file root (doesn't clear stack)"
      example: "ROOT"
```

### Array Operators (at current position)

When selection points to an array:

```yaml
array_ops:

  # Positional (move selection within array)
  FIRST:    "Move selection to [0]"
  LAST:     "Move selection to [-1]"
  NTH n:    "Move selection to [n]"
  NEXT:     "Move to next sibling"
  PREV:     "Move to previous sibling"
  
  # Mutation (modify data at selection)
  APPEND value:    "Add to end of array"
  PREPEND value:   "Add to start of array"
  INSERT n value:  "Insert at index n"
  REMOVE:          "Remove element at selection"
  SPLICE n m:      "Remove m elements starting at n"
  
  # Functional (return new array, don't move)
  MAP expr:        "Transform each element"
  FILTER expr:     "Keep elements matching predicate"
  REDUCE expr:     "Fold array to single value"
  SORT key:        "Sort by key"
  REVERSE:         "Reverse array"
  
  # Query
  LENGTH:          "Count elements"
  FIND expr:       "Move selection to first match"
  FINDALL expr:    "List indices of all matches"
```

### Functional Expressions

Expressions can transform data at the selection:

```
# With selection pointing to a number:
> SET . (+ . 1)              # Increment (. = current value)
> SET . (* . 2)              # Double

# With selection pointing to a string:
> SET . (upcase .)           # Uppercase
> SET . (concat . "!")       # Append

# With selection pointing to an array:
> SET . (filter (> .age 18) .)   # Filter adults
> SET . (map .name .)            # Extract names
> SET . (sort .score .)          # Sort by score

# Conditional:
> SET . (if (> . 0) . 0)     # Clamp to non-negative

# Note: "." means "value at current selection"
```

### The Selection Protocol

```yaml
selection_protocol:
  
  # A selection has start (and optional end for ranges)
  address:
    start:
      file: "moollm://path/to/file.yml"
      path: ["key1", "key2", 0, "key3"]
      fragment: "#key1.key2.0.key3"
    end: null  # null = point, not-null = range
    
  # Uniform access
  read: "GET → value (or values if range)"
  write: "SET value → modifies at selection"
  
  # Navigation
  enter: "Descend into child"
  parent: "Go to parent"
  next/prev: "Move among siblings"
  goto: "Jump to address"
  
  # Named selections per character
  character_selections:
    location: "Where body IS"
    focus: "Where eyes LOOK"
    left_hand: "What left hand HOLDS"
    right_hand: "What right hand HOLDS"
    mind: "What mind CONTEMPLATES"
    third_eye: "What third eye PERCEIVES"
    
  # Edit = write through lens
  edit: |
    Character says "change this to X"
    → SET . X
    → File modified at selection.start
```

---

## Universal Tree Navigation

> *Navigation, editing, and stack ops are DISTINCT.*
> *Works on any JSON/YAML structure uniformly.*
> *"Selection" = (start, end) range. "Point" = collapsed selection.*

### Three Distinct Operation Classes

```yaml
operation_classes:

  # 1. TREE NAVIGATION — Move the selection through structure
  navigation:
    description: "Move selection position without changing data"
    operations:
      # Vertical (depth)
      ENTER [key]:    "Descend into child by key/index"
      PARENT:         "Go to parent node"
      ROOT:           "Go to document root"
      
      # Horizontal (siblings)
      NEXT:           "Next sibling (in array or object)"
      PREV:           "Previous sibling"
      FIRST:          "First sibling / first child"
      LAST:           "Last sibling / last child"
      
      # Indexed
      NTH n:          "Go to nth sibling (0-indexed)"
      KEY k:          "Go to sibling with key k (in objects)"
      
      # Jump
      GOTO path:      "Jump to absolute/relative path"
      BACK:           "Return to previous position (history)"
      FORWARD:        "Redo position (history)"
      
  # 2. VALUE EDITING — Modify data at selection
  editing:
    description: "Read/write values, modify structure"
    operations:
      # Read
      GET:            "Read value at selection (or values if range)"
      TYPE:           "Get type (string, number, array, object, null)"
      
      # Write scalar
      SET value:      "Replace value at selection"
      CLEAR:          "Set to null"
      
      # Object operations
      PUT key value:  "Add/update key in object"
      UNSET key:      "Remove key from object"
      RENAME old new: "Rename a key"
      KEYS:           "List all keys"
      HAS key:        "Check if key exists"
      
      # Array operations  
      APPEND value:   "Add to end of array"
      PREPEND value:  "Add to start"
      INSERT i value: "Insert at index"
      REMOVE:         "Remove element at selection"
      SPLICE i n:     "Remove n elements starting at i"
      
  # 3. STACK/HISTORY — Manage selection position stack
  stack:
    description: "Bookmark and recall selection positions"
    operations:
      PUSH:           "Save current position to stack"
      POP:            "Restore last saved position"
      DUP:            "Duplicate top of stack"
      SWAP:           "Swap top two stack positions"
      DROP:           "Discard top of stack"
      CLEAR_STACK:    "Clear entire position stack"
      PEEK:           "Show top of stack without popping"
      DEPTH:          "Show stack depth"
```

### Tree Navigation Detail

```yaml
tree_navigation:

  # VERTICAL — Depth traversal
  
  ENTER:
    syntax: "ENTER [key|index|path]"
    examples:
      - "ENTER users"        # Enter child key
      - "ENTER 0"            # Enter array index
      - "ENTER users.0.name" # Enter path
    works_on: "objects and arrays"
    error: "Key/index not found"
    
  PARENT:
    syntax: "PARENT"
    alias: "UP, .."
    effect: "Move to parent node"
    at_root: "No-op (already at root)"
    
  ROOT:
    syntax: "ROOT"
    alias: "/"
    effect: "Jump to document root"
    clears: "Navigation history? No — can still BACK"
    
  # HORIZONTAL — Sibling traversal
  
  NEXT:
    syntax: "NEXT"
    alias: "→, >"
    in_array: "Move to index + 1"
    in_object: "Move to next key (insertion order)"
    at_end: "Wrap to first, or error (configurable)"
    
  PREV:
    syntax: "PREV"
    alias: "←, <"
    in_array: "Move to index - 1"
    in_object: "Move to previous key"
    at_start: "Wrap to last, or error (configurable)"
    
  FIRST:
    syntax: "FIRST"
    alias: "^, HOME"
    effect: "Move to first sibling/child"
    in_array: "Index 0"
    in_object: "First key"
    
  LAST:
    syntax: "LAST"
    alias: "$, END"
    effect: "Move to last sibling/child"
    in_array: "Index -1 (length - 1)"
    in_object: "Last key"
    
  NTH:
    syntax: "NTH n"
    effect: "Move to nth sibling (0-indexed)"
    negative: "NTH -1 = LAST, NTH -2 = second to last"
    
  KEY:
    syntax: "KEY k"
    effect: "Move to sibling with key k"
    only_for: "Objects (dicts)"
    
  # JUMP — Non-local navigation
  
  GOTO:
    syntax: "GOTO path"
    examples:
      - "GOTO users.0.name"           # Relative from cursor
      - "GOTO /users.0.name"          # Absolute from root
      - "GOTO ../sibling"             # Relative with parent
      - "GOTO other-file.yml#path"    # Different file
    
  BACK:
    syntax: "BACK"
    alias: "UNDO-NAV"
    effect: "Return to previous cursor position"
    uses: "Navigation history (separate from stack)"
    
  FORWARD:
    syntax: "FORWARD"
    alias: "REDO-NAV"
    effect: "Go forward in navigation history"
```

### Quick Reference Card

```
╔═══════════════════════════════════════════════════════════════╗
║                    PSIBER COMMAND CARD                        ║
║              Selection = (start, end) range                   ║
║              Point = collapsed selection (start == end)       ║
╠═══════════════════════════════════════════════════════════════╣
║  NAVIGATION (move selection)                                  ║
║  ─────────────────────────────────────────────────────────── ║
║  ENTER key    descend into        PARENT      go up          ║
║  ROOT         go to top           GOTO path   jump to path   ║
║  NEXT         next sibling        PREV        prev sibling   ║
║  FIRST        first child         LAST        last child     ║
║  NTH n        nth sibling         KEY k       sibling by key ║
║  BACK         undo navigation     FORWARD     redo navigation║
╠═══════════════════════════════════════════════════════════════╣
║  SELECTION (ranges)                                           ║
║  ─────────────────────────────────────────────────────────── ║
║  POINT path   set selection       SELECT a b  range a to b   ║
║  COLLAPSE     range to point      EXPAND      point to range ║
║  COUNT        items in range      SPAN        list range     ║
╠═══════════════════════════════════════════════════════════════╣
║  EDITING (modify data at selection)                           ║
║  ─────────────────────────────────────────────────────────── ║
║  GET          read value(s)       SET v       write value    ║
║  TYPE         get type            CLEAR       set to null    ║
║  PUT k v      add/update key      UNSET k     remove key     ║
║  RENAME o n   rename key          KEYS        list keys      ║
║  APPEND v     add to end          PREPEND v   add to start   ║
║  INSERT i v   insert at i         REMOVE      delete at sel  ║
║  SPLICE i n   remove n at i                                  ║
╠═══════════════════════════════════════════════════════════════╣
║  STACK (position bookmarks)                                   ║
║  ─────────────────────────────────────────────────────────── ║
║  PUSH         save position       POP         restore pos    ║
║  DUP          duplicate top       SWAP        swap top two   ║
║  DROP         discard top         PEEK        show top       ║
║  DEPTH        stack depth         CLEAR_STACK empty stack    ║
╠═══════════════════════════════════════════════════════════════╣
║  FUNCTIONAL (over selection)                                  ║
║  ─────────────────────────────────────────────────────────── ║
║  MAP f        transform each      FILTER p    keep matches   ║
║  REDUCE f     fold to one         SORT k      sort by key    ║
║  FIND p       first match         EACH cmd    run on each    ║
║  WHERE p      narrow selection    REVERSE     reverse array  ║
╚═══════════════════════════════════════════════════════════════╝
```

### Example Session

```
> ENTER pub/seating.yml
[sel → pub/seating.yml# (point)]

> ENTER bar-stools
[sel → pub/seating.yml#bar-stools (point)]
[Value: array of 5 stools]

> FIRST
[sel → pub/seating.yml#bar-stools.0 (point)]
[Value: { id: "stool-1", who: "Old Pete", drink: "whiskey" }]

> ENTER who
[sel → pub/seating.yml#bar-stools.0.who (point)]
[Value: "Old Pete"]

> SET "Young Pete"
[Modified: pub/seating.yml#bar-stools.0.who = "Young Pete"]

> PARENT
[sel → pub/seating.yml#bar-stools.0 (point)]

> NEXT
[sel → pub/seating.yml#bar-stools.1 (point)]
[Value: { id: "stool-2", who: null, drink: null }]

> PUT who "Alice"
[Modified: pub/seating.yml#bar-stools.1.who = "Alice"]

# Make a RANGE selection (not just a point)
> SELECT bar-stools.0 TO bar-stools.4
[sel → bar-stools.0..bar-stools.4 (RANGE of 5)]

> GET | MAP .who | FILTER (not null)
["Young Pete", "Alice"]

# Collapse back to point
> COLLAPSE START
[sel → pub/seating.yml#bar-stools.0 (point)]

# Navigation history:
> BACK
[sel → pub/seating.yml#bar-stools.1 (point)]

> FORWARD
[sel → pub/seating.yml#bar-stools.0 (point)]
```

### Navigation History vs Stack

```yaml
distinction:
  
  navigation_history:
    what: "Where selection has BEEN (automatic)"
    ops: "BACK, FORWARD"
    like: "Browser history"
    
  position_stack:
    what: "Where you MARKED (manual bookmarks)"
    ops: "PUSH, POP, DUP, SWAP"
    like: "Bookmarks you explicitly save"
    
  selection_type:
    point: "start == end (collapsed)"
    range: "start != end (spans multiple items)"
    
example:
  - "ENTER users"      # History: [root] → adds root to history
  - "ENTER 0"          # History: [root, users]
  - "PUSH"             # Stack: [users.0]  — explicit bookmark
  - "ENTER name"       # History: [root, users, users.0]
  - "BACK"             # → users.0 (from history)
  - "POP"              # → users.0 (from stack)
  # Both go to same place, different mechanism
```

---

## Character Selection — Read/Write Through Focus

> *Every character has a selection. Default: null (unfocused).*
> *Point it anywhere. Read and write through it.*

### The Basic Model

```yaml
character_selection:
  description: "Each character has ONE primary selection"
  
  default: null  # Unfocused — not pointing at anything
  
  when_set:
    - "Character is focused on something"
    - "Can READ value at selection"
    - "Can WRITE/EDIT if permitted"
    - "Selection = (start, end) — point or range"
    
  operations:
    FOCUS path:     "Set selection to path (point)"
    FOCUS a TO b:   "Set selection to range"
    UNFOCUS:        "Set selection to null"
    GET:            "Read value at selection"
    SET value:      "Write value at selection"
    
example:
  # Character starts unfocused
  alice:
    selection: null
    
  # Alice focuses on a file
  > FOCUS "pub/menu.yml#drinks"
  alice:
    selection:
      start: "pub/menu.yml#drinks"
      end: null  # point, not range
      
  # She can now read/write there
  > GET
  [drinks: { beer: 5, wine: 8, whiskey: 12 }]
  
  > SET .beer 6
  [Modified: pub/menu.yml#drinks.beer = 6]
  
  # She unfocuses
  > UNFOCUS
  alice:
    selection: null
```

### Selection as File Editing

```yaml
selection_editing:
  description: "Selection enables character-mediated file editing"
  
  flow:
    1: "Character focuses on data (file + path/lines)"
    2: "Character reads through selection"
    3: "Character edits through selection"
    4: "File is modified on disk"
    
  # This IS how the LLM edits files!
  mapping_to_cursor_tools:
    FOCUS: "Read tool — load file into context"
    GET: "Content already in context"
    SET: "StrReplace / Write tool"
    
  example: |
    > FOCUS "characters/alice.yml:15-30"
    # LLM: Read(characters/alice.yml, offset=15, limit=15)
    
    > SET LINE 20 "  mood: happy"
    # LLM: StrReplace(old="  mood: grumpy", new="  mood: happy")
```

---

## Named Selections (Extended Model)

> *Beyond the basic selection, characters can have named pointers.*
> *Location, focus, hands, mind, third eye — all optional.*

### Simple Character (One Selection)

```yaml
# Most characters just need one selection
character:
  name: "Alice"
  
  # The ONE selection — null when unfocused
  selection: null
  
  # When focused:
  # selection:
  #   start: "pub/menu.yml#drinks.beer"
  #   end: null  # point
```

### Selection as Thought — Mind Reading Protocol

> *Selection = where the character's mind IS.*
> *Flickering selections during simulation = train of thought.*
> *Final selection = what they concluded, output, care about.*

```yaml
selection_as_thought:
  description: "Characters THINK by selecting"
  
  principle: |
    Just like humans highlight text while reading,
    characters select data as they process it.
    Their selection IS their attention/focus/thought.
    
  # DURING SIMULATION
  during_simulation:
    what: "Selection flickers as character thinks"
    
    example_thought_trace:
      - "SELECT inventory"           # Looking at inventory
      - "SELECT inventory.sword"     # Focusing on sword
      - "SELECT stats.strength"      # Checking if strong enough
      - "SELECT inventory.sword"     # Back to sword
      - "SELECT enemy.armor"         # Considering enemy
      - "SELECT inventory.sword.damage"  # Final focus
      # Selection left on sword.damage — that's what they decided matters
      
    visibility: "Can be shown as thought bubbles, highlights, trails"
    
  # AFTER TASK COMPLETES
  after_task:
    rule: "Leave selection on the OUTPUT or CONCLUSION"
    
    why:
      - "Next LLM cycle can READ THEIR MIND"
      - "Orchestrator knows what they care about"
      - "Natural continuation point"
      - "Like leaving cursor where you stopped typing"
      
    examples:
      - task: "Find the cheapest item"
        final_selection: "items.yml#$.products[7]"  # The answer
        
      - task: "Write a greeting"
        final_selection: "dialog.yml#$.greeting"    # What they wrote
        
      - task: "Decide what to do"
        final_selection: "decisions.yml#$.next_action"  # Their choice
        
  # MIND READING
  mind_reading:
    description: "Check what a character is thinking about"
    
    syntax:
      GET [character].selection:     "What are they focused on?"
      GET [character].selection.value: "What's the value there?"
      
    orchestrator_use:
      - "Check what agent concluded"
      - "Pass focus to next agent"
      - "Aggregate attention across party"
      - "Detect stuck/looping (same selection too long)"
      
    example:
      # Orchestrator checks what Alice found
      > GET alice.selection
      "inventory.yml#$.items[3].magic_ring"
      
      # Read the value she's focused on
      > GET alice.selection AS PARSED
      { name: "Ring of Power", effect: "+5 wisdom" }
      
      # Pass her focus to Bob for evaluation
      > SET bob.selection alice.selection
      # Now Bob is looking at the same ring

  # THOUGHT TRAILS (OPTIONAL)
  thought_trails:
    description: "History of selections = train of thought"
    
    structure:
      selection_history:
        - { time: "10:01:05", sel: "inventory" }
        - { time: "10:01:06", sel: "inventory.sword" }
        - { time: "10:01:08", sel: "stats.strength" }
        - { time: "10:01:10", sel: "inventory.sword" }
        # ...
        
    queries:
      GET [char].selection_history:    "Full thought trail"
      GET [char].selection_history[-5:]: "Last 5 thoughts"
      
    analysis:
      - "Detect circular thinking (same selections repeating)"
      - "Find decision points (long dwell time)"
      - "Trace how conclusion was reached"

example_workflow:
  # Task: Alice searches for treasure
  
  # 1. Alice starts searching
  > alice.FOCUS "dungeon.yml#$.rooms"
  # She's looking at all rooms
  
  # 2. She scans through (selection flickers)
  > alice.NEXT  # room[0]
  > alice.NEXT  # room[1]
  > alice.ENTER "contents"
  > alice.WHERE (.type == "treasure")
  # Found something!
  
  # 3. Task ends — selection left on result
  > GET alice.selection
  "dungeon.yml#$.rooms[3].contents[2]"
  # The treasure she found
  
  # 4. Orchestrator reads her mind
  > GET alice.selection AS PARSED
  { type: "treasure", name: "Golden Idol", value: 5000 }
  
  # 5. Pass to Bob for appraisal
  > SET bob.selection alice.selection
  > bob.EVAL "appraise(GET .)"
  # Bob now examining same object
```

### Extended Character (Named Selections)

```yaml
# Power users / NPCs with special abilities
character:
  name: "Developer Dave"
  
  # Primary selection (same as simple model)
  selection:
    start: "pub/main-room.yml#bar-counter"
    end: null
    
  # Additional named selections (optional)
  named_selections:
    
    # LOCATION — Where the body IS (usually a point)
    location:
      start: "pub/main-room.yml#bar-counter"
      end: null  # null = same as start (point, not range)
      description: "Physical presence"
      can_read: true
      can_write: true
      range: "immediate surroundings"
      
    # FOCUS — Where attention/eyes are pointed
    focus:
      start: "pub/seating.yml#bar-stool-3.who-sat-on"
      end: null  # point focus
      description: "Visual/mental attention"
      can_read: true
      can_write: false
      range: "line of sight"
      
      # Focus can span ranges:
      range_example:
        start: "pub/seating.yml#bar-stools.0"
        end: "pub/seating.yml#bar-stools.4"
        description: "Scanning all five stools"
        
    # HANDS — Where manipulation happens
    left_hand:
      start: "pub/main-room.yml#bar-counter.drinks.3"
      end: null
      description: "Left hand holding whiskey glass"
      can_read: true
      can_write: true
      range: "arm's length"
      holding: "whiskey glass"
      
    right_hand:
      start: null  # Empty, free
      end: null
      description: "Right hand free"
      can_read: true
      can_write: true
      range: "arm's length"
      holding: null
      
    # MIND — Internal selection, introspection
    mind:
      start: "characters/dave.yml#memories.yesterday"
      end: null  # or could select a range of memories
      description: "Internal contemplation"
      can_read: true
      can_write: true  # Can edit own thoughts
      range: "self"
      
    # THIRD_EYE — Remote/speculative perception
    third_eye:
      start: "tower/floor-7.yml#dr-no.current-thought"
      end: null
      description: "Remote viewing"
      can_read: true
      can_write: false
      range: "unlimited (accuracy decreases with distance)"
      requires: "IRIS-III bionic eye"
```

### Selection Commands

```yaml
selection_commands:

  # Set which named selection is active
  USE [selection]:
    example: "USE focus"
    effect: "Subsequent commands operate through focus"
    
  # Point a selection (make it a point, not range)
  POINT [selection] AT [address]:
    example: "POINT focus AT characters/alice.yml#mood"
    effect: "Set start=address, end=null (point)"
    
  # Make a range selection
  SELECT [selection] FROM [start] TO [end]:
    example: "SELECT focus FROM bar-stools.0 TO bar-stools.4"
    effect: "Selection now spans a range"
    
  # Collapse range to point
  COLLAPSE [selection] [START|END]:
    example: "COLLAPSE focus START"
    effect: "Range becomes point at start (or end)"
    
  # Read through selection
  GET [selection]:
    example: "GET focus"
    point: "Returns single value"
    range: "Returns all values in range"
    
  # Write through selection (if allowed)
  SET [selection] [value]:
    example: "SET left_hand empty"
    point: "Sets single value"
    range: "Sets all values in range to same value"
    
  # Swap selection targets
  SWAP [sel1] [sel2]:
    example: "SWAP location focus"
    effect: "Exchange what two selections point at"
    
  # Quick shortcuts
  LOOK AT [address]:      "POINT focus AT address"
  GRAB [address]:         "POINT right_hand AT address"
  THINK ABOUT [address]:  "POINT mind AT address"
  REMOTE VIEW [address]:  "POINT third_eye AT address"
  SCAN [start] TO [end]:  "SELECT focus FROM start TO end"
```

### Range Operations

```yaml
range_operations:
  description: "When a selection is a range (start != end)"
  
  # Iterate over range
  EACH [command]:
    example: "USE focus; EACH PRINT"
    effect: "Run command on each item in selection"
    
  # Filter range
  WHERE [expr]:
    example: "SELECT focus FROM items.* TO items.*; WHERE (.price > 100)"
    effect: "Narrow selection to matching items"
    
  # Transform range
  MAP [expr]:
    example: "GET focus | MAP .name"
    effect: "Extract/transform each item"
    
  # Aggregate range
  REDUCE [expr]:
    example: "GET focus | REDUCE (+ a b)"
    effect: "Fold range to single value"
    
  # Count
  COUNT:
    example: "USE focus; COUNT"
    effect: "Number of items in selection"
```

### Example: Introspection

```
# Look inward — focus selection on your own character data
> POINT focus AT characters/dave.yml#self

[focus → characters/dave.yml#self (point)]
You turn your attention inward...

> ENTER memories
[focus → characters/dave.yml#self.memories]
A corridor of memory doors stretches before you.

> ENTER yesterday
[focus → characters/dave.yml#self.memories.yesterday]
Yesterday's events crystallize...

> GET focus
[Value: { morning: "coffee at pub", noon: "meeting with dr-no", evening: "..." }]

# Edit your own memory (unreliable narrator!)
> SET focus.evening "nothing happened"
[Modified: characters/dave.yml#self.memories.yesterday.evening]
The memory shifts, blurs, rewrites itself...
```

### Example: Remote Viewing + Telekinesis

```
# Location: at the bar
# Focus: remote viewing the tower
> POINT third_eye AT tower/floor-7.yml#dr-no.desk

[Third Eye: tower/floor-7.yml#dr-no.desk]
Your third eye opens, perceiving across the distance...
Dr. No's desk materializes in your vision.

> GET third_eye
[Value: { papers: [...], coffee: "cold", drawer: "locked" }]

# Attempt telekinesis (if you have the ability)
> SET third_eye.coffee.temperature "hot"

[Permission check: third_eye.can_write = false]
Your third eye can see, but cannot touch at this range.
You would need to be physically present, or have
telekinetic abilities installed.

# With telekinesis upgrade:
> UPGRADE third_eye WITH telekinesis
[Third eye now has can_write: true for small objects]

> SET third_eye.coffee.temperature "hot"
[Modified: tower/floor-7.yml#dr-no.desk.coffee.temperature]
Across the distance, Dr. No's coffee begins to steam.
He looks around, suspicious.
```

### Example: Multi-Cursor Context Gathering

```
# Gather context from multiple sources simultaneously:

CONTEXT:
  location: "pub/main-room.yml#bar-counter"
    → immediate surroundings, who's nearby
  focus: "pub/main-room.yml#suspicious-stranger"
    → watching someone specific
  left_hand: "pub/menu.yml#drinks"
    → browsing the menu
  mind: "characters/dave.yml#memories.faces"
    → trying to remember if you've seen this stranger
  third_eye: "tower/security.yml#wanted-list"
    → remote viewing the wanted posters

# The LLM sees ALL cursor contexts when processing:
"You're at the bar (location), watching a suspicious stranger (focus),
holding a menu (left_hand), searching your memory (mind), and your
third eye is scanning the tower's wanted list (third_eye)..."
```

### Cursor Permissions

```yaml
cursor_permissions:
  
  read_local: "Can always read at location"
  write_local: "Can write within arm's reach of location"
  
  read_remote: "Focus can read at line-of-sight or mental range"
  write_remote: "Requires special ability (telekinesis, magic, etc.)"
  
  read_self: "Mind can always read own character data"
  write_self: "Mind can write to own memories, thoughts, state"
  
  read_others: "Third eye can perceive others (with limits)"
  write_others: "Requires consent, telepathy, or coercion"
  
  # Distance affects accuracy
  accuracy_falloff:
    same_room: 1.0
    line_of_sight: 0.9
    same_building: 0.7
    same_area: 0.5
    remote: 0.3
    speculative: 0.1
```

---

## K-Lines

```yaml
k-lines:
  PSIBER: "Programmatic Structured Interactive Browsing Editor via Roleplay"
  CURSOR-AS-LENS: "Same address for read and write — setf semantics"
  MULTI-CURSOR: "Location, focus, hands, mind — multiple pointers"
  LOCATION-CURSOR: "Where the body IS"
  FOCUS-CURSOR: "Where attention points — can be anywhere"
  HAND-CURSORS: "Where manipulation happens"
  MIND-CURSOR: "Internal introspection pointer"
  THIRD-EYE-CURSOR: "Remote viewing, speculation"
  UNIFORM-ACCESS: "GET and SET through the same path"
  STACK-NAVIGATION: "Push/pop/dup/swap for position history"
  ARRAY-OPERATORS: "First/last/next/map/filter/reduce"
  FUNCTIONAL-EXPRESSIONS: "Transform data where you stand"
  DATA-AS-ROOM: "Objects become explorable spaces"
  REMOTE-VIEWING: "Focus on distant locations"
  TELEKINESIS: "Write through remote cursor"
  INTROSPECTION: "Focus on self, edit own data"
```

---

## See Also

- `SUMMON-PROTOCOL.md` — Summoning characters into any location (including data)
- `MOOLLM-URLS.md` — URL syntax for pointing to data nodes
- `YAML-JAZZ.md` — The data format that makes this possible
