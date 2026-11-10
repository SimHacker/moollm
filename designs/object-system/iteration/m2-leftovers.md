# M2 leftovers

Dry run of `designs/object-system/tasks/migrations/m02_advert_lists.py` on 2026-10-29: scanned 1561 files, would change 0, skipped 11. The script keys an `advertisements:` list by `name:`, else `id:`, else `slug(action)`, else `ON-` plus `slug(trigger)` when that trigger is at most 4 words. `slug` takes runs of word characters (`[^\W_]+`), joins them with hyphens, and uppercases the result. It drops the source field when the field text equals the key and the entry has other fields. A trigger-derived key keeps `trigger:`. One `Skip` leaves the whole file unwritten. The reason strings below are the ones that dry run printed.

## examples/adventure-4/kitchen/stove.yml

Skip: `action: names several verbs (one advertisement or several?)`. The comma in `action:` matches `[,/|]| or `.

```
  - action: TURN-ON, TURN-OFF
    score_if: "state == off/on"
    description: "Light and extinguish the stove"
```

A person decides whether that entry is one advertisement or two. One advertisement needs a `name:` the script does not derive, because it will not slug an action that names several verbs. Two advertisements would be `TURN-ON` and `TURN-OFF`, and `score_if: "state == off/on"` currently covers both states in the one entry. The next entry, `action: EXAMINE`, is one verb: the script would key it `EXAMINE` and drop `action:` because the text equals the key. It writes nothing until the comma entry is decided. This file is the same bytes as the three stove files under `examples/old/`.

## examples/old/adventure-1/kitchen/stove.yml

Skip: `action: names several verbs (one advertisement or several?)`. Same bytes as `examples/adventure-4/kitchen/stove.yml`. The blocking entry is:

```
  - action: TURN-ON, TURN-OFF
    score_if: "state == off/on"
    description: "Light and extinguish the stove"
```

A person decides whether `TURN-ON, TURN-OFF` is one advertisement, which needs a `name:` the script will not derive from a multi-verb action, or two advertisements keyed `TURN-ON` and `TURN-OFF`. `score_if: "state == off/on"` is the field that currently covers both states. `action: EXAMINE` on the following entry is one verb and would become the key `EXAMINE` with `action:` dropped, once the comma entry is decided.

## examples/old/adventure-2/kitchen/stove.yml

Skip: `action: names several verbs (one advertisement or several?)`. Same bytes as `examples/adventure-4/kitchen/stove.yml`. The blocking entry is:

```
  - action: TURN-ON, TURN-OFF
    score_if: "state == off/on"
    description: "Light and extinguish the stove"
```

A person decides whether `TURN-ON, TURN-OFF` is one advertisement, which needs a `name:` the script will not derive from a multi-verb action, or two advertisements keyed `TURN-ON` and `TURN-OFF`. `score_if: "state == off/on"` is the field that currently covers both states. `action: EXAMINE` on the following entry is one verb and would become the key `EXAMINE` with `action:` dropped, once the comma entry is decided.

## examples/old/adventure-3/kitchen/stove.yml

Skip: `action: names several verbs (one advertisement or several?)`. Same bytes as `examples/adventure-4/kitchen/stove.yml`. The blocking entry is:

```
  - action: TURN-ON, TURN-OFF
    score_if: "state == off/on"
    description: "Light and extinguish the stove"
```

A person decides whether `TURN-ON, TURN-OFF` is one advertisement, which needs a `name:` the script will not derive from a multi-verb action, or two advertisements keyed `TURN-ON` and `TURN-OFF`. `score_if: "state == off/on"` is the field that currently covers both states. `action: EXAMINE` on the following entry is one verb and would become the key `EXAMINE` with `action:` dropped, once the comma entry is decided.

## examples/adventure-4/pub/rooms/room-3/context-orrery.yml

Skip: `trigger too long to name an advertisement (> 4 words)`.

```
  - trigger: "context window"
  - trigger: "token limit"
  - trigger: "what do you know about"
```

`context window` and `token limit` are 2 words. The script would key them `ON-CONTEXT-WINDOW` and `ON-TOKEN-LIMIT` and keep `trigger:`. `what do you know about` is 5 words (`what`, `do`, `you`, `know`, `about`), and that entry aborts the file before any of the three are rewritten. A person supplies a `name:` for that third trigger, or shortens it to 4 words or fewer. The script will not build an `ON-` key from a trigger over the cap.

## examples/adventure-4/pub/rooms/room-3/thinking-mirror.yml

Skip: `trigger too long to name an advertisement (> 4 words)`.

```
  - trigger: "what am I thinking"
  - trigger: "why did I do that"
  - trigger: "introspection"
```

`what am I thinking` is 4 words, at the cap, so the script would key it `ON-WHAT-AM-I-THINKING` and keep `trigger:`. `introspection` is 1 word and would become `ON-INTROSPECTION`. `why did I do that` is 5 words (`why`, `did`, `I`, `do`, `that`), and that entry aborts the file. A person supplies a `name:` for `why did I do that`, or shortens that trigger to 4 words or fewer.

## skills/content-rescue/CARD.yml

Skip: `trigger too long to name an advertisement (> 4 words)`. Every trigger in the list is over the cap, counted with `[^\W_]+` (an apostrophe splits a contraction):

```
  - trigger: "rescue this Medium article / save my post / mirror these images / it's bot-walled"
  - trigger: "the page won't curl but I can see it in a browser"
  - trigger: "download all these images in order with captions"
  - trigger: "save my Hacker News comments"
```

Those counts are 14, 13, 8, and 5. The first line is also four phrases separated by ` / `. The several-verbs check looks only at `action:`, so the skip that fires is the length check, on the first entry, and the file stops there. A person supplies a `name:` for each of the four triggers. For the first line, that includes whether the four slash-separated phrases are one advertisement or four.

## skills/change-name/CARD.yml

Skip: `non-map advertisement entries (strings)`.

```
advertisements:
  - "📄 I can read inside a PDF and tell you everywhere your old name hides — even split around kern pairs"
  - "🔤 I check the embedded fonts can spell your new name before promising anything"
  - "🕯️ I did this for Vanessa. Original preserved, every change disclosed."
```

Each entry is a string. The script never reaches `name:`, `action:`, or `trigger:`, because those fields exist on a map. A person chooses a map key for each sentence and which field holds the sentence.

## skills/emacs/CARD.yml

Skip: `non-map advertisement entries (strings)`.

```
advertisements:
  - "Persistent structured editing beats unique-string replace"
  - "emacs:// URLs address buffer + structure for LLM round-trips"
  - "Play-learn-lift: oneshots + macros + logs"
```

Each entry is a string, so there is no `name:`, `action:`, or `trigger:` to slug. A person chooses a map key for each sentence and which field holds the sentence.

## skills/place/CARD.yml

Skip: `flow-style or scalar advertisement entry`. The list items start with `{`, which the rewriter refuses.

```
  - { action: VISIT,   to: [rider, tourist], when: "within 200 m and open" }
  - { action: SURVEY,  to: [surveyor],       when: "review.priority is high or paired" }
  - { action: COUCH,   to: [tour],           when: "author is building a route" }
  - { action: EXPLAIN, to: [anyone],         when: "always — the bare guard, per Korz" }
```

`VISIT`, `SURVEY`, `COUCH`, and `EXPLAIN` are each one verb and equal their own slug. In block form the script would key the map by that action and drop `action:`, because the text equals the key and `to:` and `when:` remain. A person decides that those four flow maps may be expanded into block entries under those keys on those terms.

## examples/adventure-4/LINTER.yml

Skip: `advertisement lists only inside a log or report (events:, world_state:)`. Line 1 is `lint_ignore: true`. `events:` is at line 11 and `world_state:` is at line 3123. Every `advertisements:` list in the file sits under one of those two keys: 26 lists under `events:` (25 empty, and one list of seven strings) and 11 nonempty lists under `world_state:` → `objects:`. The gong record:

```
  path: pub/gong.yml
  data:
    advertisements:
    - RING
    - RING-TWICE
    - RING-THRICE
    - CEREMONIAL-RING
    - CELEBRATION-RING
    - AUTOGONG-ELIMINATION
    - AUTOGONG-VICTORY
```

One object record inside the log:

```
world_state:
  objects:
    end/treasure.yml:
      advertisements:
      - action: GET
        score_if: not in_inventory
        description: Claim your prize!
```

The script's rule for that shape is that the lists are a record of past state.

## action: kept

The list-to-map rewrite already ran on these nine files. The script drops `action:` only when the field text equals the key. While rewriting, it records `action: kept, its spelling differs from the key` when the key is `slug(action)` and the field text is different. These nine files are that case: the key is hyphenated and `action:` still has a space. A later script can delete `action:` only after a person decides that the spaced spelling is the same name as the hyphenated key.

`examples/adventure-4/maze/room-f/gold-pile.yml`, `examples/old/adventure-1/maze/room-f/gold-pile.yml`, `examples/old/adventure-2/maze/room-f/gold-pile.yml`, and `examples/old/adventure-3/maze/room-f/gold-pile.yml` are the same bytes. The kept field is:

```
  TAKE-SOME:
    action: TAKE SOME
```

`examples/old/adventure-1/maze/room-j/lamp-vendor.yml` and `examples/old/adventure-2/maze/room-j/lamp-vendor.yml` are the same bytes. `examples/old/adventure-3/maze/room-j/lamp-vendor.yml` has the same four action lines at the same line numbers. The kept fields are:

```
  BUY-OIL:
    action: BUY OIL
  BUY-DELUXE:
    action: BUY DELUXE
  BUY-PREMIUM:
    action: BUY PREMIUM
  INSERT-COIN:
    action: INSERT COIN
```

`examples/old/adventure-1/start/lamp.yml` keeps one field:

```
  CHECK-OIL:
    action: CHECK OIL
```

`examples/old/adventure-2/start/lamp.yml` keeps the same pair at lines 123–124:

```
  CHECK-OIL:
    action: CHECK OIL
```

That is four gold-pile files, three lamp-vendor files, and two lamp files. Eighteen entries, nine files.
