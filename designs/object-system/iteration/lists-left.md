# Lists left after M2 and M6

Recount of `skills/prototype/scripts/behavior_survey.py` on 2026-10-29, using the same walks as the script.

| survey line | list | map |
|---|---:|---:|
| cards `advertisements` container | 4 | 118 |
| cards `methods` container | 3 | 121 |
| world `advertisements` blocks | 17 | 177 |

Cards are the top-level key on `skills/*/CARD.yml`. World blocks are `advertisements` on dicts reached by following dict values, depth at most 4, in `examples/**/*.yml` and `skills/*/[A-Z]*.yml`, skipping `build/`, `CARD.yml`, `GLANCE.yml`, and `INDEX.yml`. The walk follows dict values. `advertisements: []` inside `events:` items in `examples/adventure-4/LINTER.yml` lives in a list, so it is outside this count. The 17 blocks below are every list the walk reports.

M2 is `designs/object-system/tasks/migrations/m02_advert_lists.py`. It rewrites an `advertisements:` list into a map on `skills/*/CARD.yml` and under `examples/`. One `Skip` leaves the whole file. M6 is `m06_method_fields.py`. It renames `does:` to `description:` and `params:` / `args:` / `input:` to `parameters:` inside `methods:` entries, on `skills/`, `examples/`, and `kernel/`. List-form method entries are in scope. The container stays a list or a map as it was. M6 reads `methods:`. The runs below call `transform` with no `--apply`.

## Card advertisements, still a list (4)

M2's predicate includes these cards. Each `transform` raises `Skip`.

### `skills/change-name/CARD.yml` lines 122–125

`plan()` raises `non-map advertisement entries (strings)`. The three entries are strings. M2's header says string entries are skipped.

```yaml
advertisements:
  - "📄 I can read inside a PDF and tell you everywhere your old name hides — even split around kern pairs"
  - "🔤 I check the embedded fonts can spell your new name before promising anything"
  - "🕯️ I did this for Vanessa. Original preserved, every change disclosed."
```

### `skills/emacs/CARD.yml` lines 61–64

Same skip: `non-map advertisement entries (strings)`.

```yaml
advertisements:
  - "Persistent structured editing beats unique-string replace"
  - "emacs:// URLs address buffer + structure for LLM round-trips"
  - "Play-learn-lift: oneshots + macros + logs"
```

### `skills/content-rescue/CARD.yml` lines 19–27

Each entry is a map with `trigger` and `method`, and with no `name`, `id`, or `action`. A trigger of more than 4 words raises `trigger too long to name an advertisement (> 4 words)`. Words are `[^\W_]+` (`WORD` in `m02_advert_lists.py`); the limit is `MAX_TRIGGER_WORDS = 4`. The first trigger is 14 words, and that is the file's skip. The other three are past the limit as well: 13, 8, and 5.

| trigger | words |
|---|---:|
| `rescue this Medium article / save my post / mirror these images / it's bot-walled` | 14 (`it's` splits into `it`, `s`) |
| `the page won't curl but I can see it in a browser` | 13 (`won't` splits into `won`, `t`) |
| `download all these images in order with captions` | 8 |
| `save my Hacker News comments` | 5 |

```yaml
advertisements:
  - trigger: "rescue this Medium article / save my post / mirror these images / it's bot-walled"
    method: "EXTRACT-MANIFEST → FETCH-ASSETS → WIRE-MARKDOWN"
  - trigger: "the page won't curl but I can see it in a browser"
    method: "EXTRACT-MANIFEST (browser/CDP from embedded __APOLLO_STATE__)"
  - trigger: "download all these images in order with captions"
    method: "FETCH-ASSETS (scripts/fetch_images.py)"
  - trigger: "save my Hacker News comments"
    method: "SCRAPE-HN"
```

### `skills/place/CARD.yml` lines 129–134

`plan()` would name `VISIT`, `SURVEY`, `COUCH`, `EXPLAIN` from `action:` and drop `action`, because the value equals the key and the entry has other fields (`to`, `when`). The text rewrite raises `flow-style or scalar advertisement entry`. Each dash line begins with `{`. `flow_headers` matches `[` or `{` on the `advertisements:` line itself; that line is block style, so the skip is `rewrite_entry` on the first flow map.

```yaml
advertisements:
  # Sims-style: a place broadcasts what it can do for whoever is passing.
  - { action: VISIT,   to: [rider, tourist], when: "within 200 m and open" }
  - { action: SURVEY,  to: [surveyor],       when: "review.priority is high or paired" }
  - { action: COUCH,   to: [tour],           when: "author is building a route" }
  - { action: EXPLAIN, to: [anyone],         when: "always — the bare guard, per Korz" }
```

## Card methods, still a list (3)

M2's `transform` walks `advertisements:`. These three cards are in M6's predicate (`skills/`). M6's `transform` returns no new text and raises no `Skip`.

The `Skip` in `rename_entry_fields` is an entry that still has a source key beside the target key, or two source spellings of one target. These entries already use `description:` and `parameters:` and contain none of `does:`, `params:`, `args:`, `input:`. There is no rename. The survey still counts a list because M6 rewrites fields inside entries and leaves the container a list.

### `skills/skill-log/CARD.yml` lines 20–31

Two entries, `LOG` and `TAIL`. Both have `description` and `parameters`.

```yaml
methods:
  - name: LOG
    description: Write one log entry for a skill
    parameters: [skill_name, description_slug, "payload?"]
    output: file written to .moollm/skills/<skill_name>/logs/YYYYMMDD-HHMMSS-<slug>.yml
    invoke_when: From CLI (skill_log.py) or from another skill/script calling the same convention

  - name: TAIL
    description: Show recent log entries for a skill (or all skills)
    parameters: ["skill_name?", limit]
    output: chat or stdout
    invoke_when: User or agent wants to see what was logged
```

### `skills/skill-snitch/CARD.yml` lines 19–64

Eight entries. Each has `name` and `description`. `parameters` is on `SCAN`, `AUDIT`, `SNITCH`, `TRUST`, `CONSISTENCY`, `OBSERVE`, and `FETCH-SCAN`.

```yaml
methods:
  - name: INIT
    description: Initialize or heal .moollm/skill-snitch/ directory
    invoke_when: First run or missing files detected
    auto: true

  - name: SCAN
    description: Quick static scan of a skill
    parameters: [skill_path]
    
  - name: AUDIT
    description: Deep static audit with pattern matching
    parameters: [skill_path]
    
  - name: SNITCH
    description: Runtime surveillance - what did the skill actually do?
    parameters: [skill_path, composer_id]
    
  - name: TRUST
    description: Trust assessment combining static and runtime analysis
    parameters: [skill_path, "composer_id?"]
    
  - name: CONSISTENCY
    description: Check skill files match (INDEX ↔ CARD ↔ SKILL.md ↔ code)
    parameters: [skill_path]

  - name: OBSERVE
    description: Deep runtime observation via cursor-mirror — watch skill in action
    parameters: [skill_path, composer_id]
    note: Requires user to actually exercise the skill while monitoring

  - name: FETCH-SCAN
    description: Scan a skill directly from a URL without downloading or installing
    parameters: [url]
    note: |
      Accepts any URL and figures out what you mean:
      - GitHub repo URL → fetches CARD.yml, SKILL.md, scripts via raw.githubusercontent.com
      - GitHub directory URL → scans that skill directory
      - GitHub org/user URL → lists repos, offers to scan skills found
      - Blog post or README URL → follows links to find skill files
      - Raw file URL → scans that file directly
      The skill never touches your filesystem. You see the report before deciding to clone.
    examples:
      - "FETCH-SCAN https://github.com/someone/their-skills"
      - "FETCH-SCAN https://github.com/someone/repo/tree/main/skills/cool-skill"
      - "FETCH-SCAN https://someone.com/blog/my-new-agent-skill"
```

### `skills/skill-test/CARD.yml` lines 23–28

Two entries, `DISCOVER` and `RUN`. `RUN` has `parameters`.

```yaml
methods:
  - name: DISCOVER
    description: Find all skills with test.yml or .skill-test.yml
  - name: RUN
    description: Execute tests for skill(s); pass env; collect pass/fail and drift
    parameters: [skill_path_or_all]
```

## World advertisement lists (17)

All 17 are under `examples/`, inside M2's predicate. They are `advertisements` lists. M6 looks for `does` / `params` / `args` / `input` on `methods:` entries.

### `examples/adventure-4/LINTER.yml` — 11 blocks

`transform` raises `advertisement lists only inside a log or report (events:, world_state:)`.

`LOG_PATHS = ("events", "world_state")`. A list is a log when the first component of its path is one of those. Each block below is `world_state.objects.<file>.advertisements`. M2's `data_entries` also walks into lists, so the file contains more advertisement lists than the survey's 11: under `events`, 25 empty `advertisements: []`, and one nonempty list of seven strings at lines 1315–1322 (`RING`, `RING-TWICE`, `RING-THRICE`, `CEREMONIAL-RING`, `CELEBRATION-RING`, `AUTOGONG-ELIMINATION`, `AUTOGONG-VICTORY`), on the `FOUND_OBJECT` event for `pub/gong.yml`. Every advertisement list in the file has a log path, and the non-log list set is empty, so the message is the log-only skip. `plan()` is not called.

The logged stove would fail `plan()` on its own. `action: TURN-ON, TURN-OFF` matches `[,/|]| or ` and raises `action: names several verbs (one advertisement or several?)`. The other ten lists name from `action:`. Spaced actions slug, and `action` stays because the spelling differs from the key: `TAKE SOME` → `TAKE-SOME`, `BUY OIL` → `BUY-OIL`, `BUY DELUXE` → `BUY-DELUXE`, `BUY PREMIUM` → `BUY-PREMIUM`, `INSERT COIN` → `INSERT-COIN`.

The sibling `methods:` on these objects is `{}`.

The quotes are the source text. `LINTER.yml` stores long strings as escaped YAML scalars.

#### `world_state.objects.end/treasure.yml` lines 8694–8714

`plan()`, if it ran, would name `GET`, `EXAMINE`, `DRINK-FROM`.

```yaml
      advertisements:
      - action: GET
        score_if: not in_inventory
        description: Claim your prize!
        response: "You lift the Jeweled Chalice from its pedestal. It's surprisingly\n\
          heavy \u2014 real gold does that. The gems sparkle triumphantly.\n\n***\
          \ YOUR SCORE HAS INCREASED BY 10 POINTS! ***\n\nTotal score: 10 of 10 points.\n\
          \nCongratulations, adventurer! You have completed the quest!\nMother will\
          \ be ABSOLUTELY INSUFFERABLE about this at dinner.\n\n(To return home, navigate\
          \ back through the maze to start.\nOr just bask in your victory here. You've\
          \ earned it.)\n"
        on_take:
          player.score: += 10
      - action: EXAMINE
        score_if: always
        description: Admire the craftsmanship
      - action: DRINK-FROM
        score_if: always
        description: Use the chalice for its intended purpose
        response: The chalice is empty. Also, drinking from priceless artifacts is
          frowned upon.
```

#### `world_state.objects.kitchen/table.yml` lines 8919–8926

Would name `EXAMINE-TABLE`, `GET-ALL`.

```yaml
      advertisements:
      - action: EXAMINE-TABLE
        score: 5
        description: See what Mother left for you
      - action: GET-ALL
        score_if: when ready to depart
        score: 8
        description: Grab all supplies at once
```

#### `world_state.objects.kitchen/sink.yml` lines 8941–8951

Would name `WASH-DISHES`, `DRINK`.

```yaml
      advertisements:
      - action: WASH-DISHES
        score_if: always
        description: Do the responsible thing
        response: "You begin washing a dish. Then another. Then\u2014\n\nNo. NO. You\
          \ are an ADVENTURER now. The dishes can WAIT.\n\nYou dry your hands on your\
          \ waistcoat and back away slowly.\n"
      - action: DRINK
        score_if: always
        description: Get a drink of water
        response: Refreshing! Your health is restored to 100. (It was already 100.)
```

#### `world_state.objects.kitchen/stove.yml` lines 8992–9001

Would raise `action: names several verbs (one advertisement or several?)` on `TURN-ON, TURN-OFF`. `EXAMINE` would key as `EXAMINE`. The file-level reason that actually fired is the log rule above.

```yaml
      advertisements:
      - action: TURN-ON, TURN-OFF
        score_if: state == off/on
        description: Light and extinguish the stove
        response: Don't play with fire! You don't have time for cooking! There's treasure
          to find!
      - action: EXAMINE
        score_if: always
        description: Inspect the stove
        response: The stove is {state}.
```

#### `world_state.objects.coatroom/costume-racks.yml` lines 9090–9101

Would name `BROWSE`, `SEARCH-FOR`, `WEAR`.

```yaml
      advertisements:
      - action: BROWSE
        score_if: always
        description: Look through the costume racks
      - action: SEARCH-FOR
        score_if: always
        description: Look for a specific type of costume
        example: SEARCH FOR something with a cape
      - action: WEAR
        score_if: always
        description: Put on a costume
        example: WEAR the pirate captain costume
```

#### `world_state.objects.coatroom/mirror.yml` lines 9120–9407

Nineteen entries. Would name `LOOK`, `POSE`, `MAKE-FACE`, `MIND-MIRROR`, `SHOW-CHARACTER`, `SHOW-PERSONA`, `SHOW-BOTH`, `EDIT-MIND`, `EDIT-CHARACTER`, `EDIT-PERSONA`, `GENERATE-MIND`, `WEAR-MIND`, `RANDOM-MIND`, `COMPARE-MINDS`, `VOCABULARY-MODE`, `SELF-PORTRAIT`, `ROLE-PLAY-ODYSSEY`, `SAVE-MIND`, `RESTORE-MIND`.

```yaml
      advertisements:
      - action: LOOK
        score: 80
        description: See your current appearance and personality
        result: 'You gaze into the mirror...


          [Shows: Current costume description + Mind Mirror profile summary.

          The costume is your outer self. The profile is your inner self.

          Both can be changed.]

          '
      - action: POSE
        score: 60
        score_if: wearing_costume
        description: Strike a dramatic pose
        result: 'You pose heroically. The mirror captures it perfectly.

          Somewhere, a camera flash goes off. There is no camera.


          [IMAGE-GENERATION-RULE: Photo prompt includes Mind Mirror

          profile snapshot as metadata for character coherence.]

          '
      - action: MAKE-FACE
        score: 50
        description: Make a face at your reflection
        result: 'You make a face. Your reflection makes the same face.

          For a moment, you''re not sure who started it.

          '
      - action: MIND-MIRROR
        score: 90
        description: See your COMBINED psychological profile (character + persona)
        result: "The mirror's surface ripples like water, then clears to reveal\n\
          not your costume but your MIND \u2014 four circular diagrams appear,\nfloating\
          \ in the glass:\n\n**BIO-ENERGY** (Life force, vitality, temperament)\n\
          [Shows COMBINED bio_energy = base + persona modifiers]\n\n**EMOTIONAL INSIGHT**\
          \ (Interpersonal style)\n[Shows COMBINED emotional = base + persona modifiers]\n\
          \n**MENTAL ABILITIES** (Knowledge, creativity)\n[Shows COMBINED mental =\
          \ base + persona modifiers]\n\n**SOCIAL INTERACTION** (Class, sophistication)\n\
          [Shows COMBINED social = base + persona modifiers]\n\nA voice whispers:\
          \ \"This is who you APPEAR to be. But what's beneath?\"\n"
      - action: SHOW-CHARACTER
        score: 88
        aliases:
        - MY-TRUE-SELF
        - BASE-SELF
        - REAL-ME
        description: See your BASE character without persona overlay
        result: "The mirror deepens, showing through the mask to your TRUE self...\n\
          \n**YOUR CHARACTER** (who you ARE underneath)\n[Shows character file's mind_mirror\
          \ and sims_traits]\n[No persona modifiers applied \u2014 just you]\n\nIf\
          \ wearing a persona:\n\"This is who you are when the mask comes off.\"\n"
      - action: SHOW-PERSONA
        score: 85
        aliases:
        - MY-MASK
        - THE-ROLE
        - SHOW-ROLE
        description: See JUST the persona's modifiers
        result: "The mirror shows only the MASK \u2014 the persona overlay...\n\n\
          **YOUR PERSONA** (the modifiers being applied)\n[Shows persona file's trait\
          \ modifiers: +2 confident, -1 cautious...]\n[Shows speech patterns, granted\
          \ skills, role backstory]\n\nIf no persona worn:\n\"You wear no mask. What\
          \ you see is what you are.\"\n"
      - action: SHOW-BOTH
        score: 87
        aliases:
        - COMPARE-SELF
        - LAYERS
        description: See character AND persona side by side
        result: 'The mirror splits into three panels:


          **LEFT: YOUR CHARACTER** (base traits)

          [The real you]


          **CENTER: THE PERSONA** (modifiers)

          [The mask''s effects]


          **RIGHT: COMBINED** (what you perform)

          [Base + modifiers = result]


          "The self, the mask, the performance."

          '
      - action: EDIT-MIND
        score: 85
        description: Adjust your COMBINED profile (edits CHARACTER by default)
        examples:
        - Make me more confident
        - I want to be calmer under pressure
        - Boost my creativity, reduce my caution
        - Make me friendlier but keep my pride
        - I want the personality of a pirate captain
        result: 'The mirror listens to your words...


          [LLM interprets the request and adjusts Mind Mirror dimensions.

          By default, edits your CHARACTER (base traits).

          Shows before/after comparison.]


          "So it shall be. Look again."

          '
      - action: EDIT-CHARACTER
        score: 84
        aliases:
        - EDIT-TRUE-SELF
        - EDIT-BASE
        description: Edit your BASE character traits (permanent)
        examples:
        - EDIT-CHARACTER make me more playful
        - EDIT-CHARACTER I want to be less cautious
        result: 'The mirror focuses on your TRUE self, beneath any mask...


          [Edits the character file''s mind_mirror and sims_traits.

          These changes persist even when you change personas.

          This is who you ARE becoming.]


          "Your true self shifts."

          '
      - action: EDIT-PERSONA
        score: 83
        aliases:
        - EDIT-MASK
        - EDIT-ROLE
        description: Edit the PERSONA's modifiers (the mask, not you)
        examples:
        - EDIT-PERSONA make the captain MORE forceful
        - EDIT-PERSONA this role should be funnier
        result: 'The mirror focuses on the MASK you''re wearing...


          [Edits the persona file''s trait modifiers.

          Affects anyone who wears this persona.

          Changes the ROLE, not you.]


          If no persona worn:

          "You wear no mask to edit."


          "The mask changes shape."

          '
      - action: GENERATE-MIND
        score: 80
        description: Generate a personality profile from description
        syntax: GENERATE-MIND FOR [name or description]
        examples:
        - GENERATE-MIND FOR a confident space pirate
        - GENERATE-MIND FOR a shy librarian with hidden depths
        - GENERATE-MIND FOR someone like Sherlock Holmes
        - GENERATE-MIND FOR my ideal self
        - GENERATE-MIND FOR who I was as a child
        result: 'The mirror swirls with possibility...


          [LLM generates a complete Mind Mirror profile based on:

          - Its knowledge of real people (K-lines, traditions)

          - Fictional character archetypes

          - Your description

          - Pure creative generation]


          The profile appears. "Try it on? WEAR-MIND to become this."

          '
      - action: WEAR-MIND
        score: 75
        description: Adopt a generated or modified personality
        result: "You step INTO the mirror \u2014 or does it step into you?\n\n[The\
          \ Mind Mirror profile becomes your active profile.\nYour old profile is\
          \ stored in the notebook for safekeeping.\nLike a costume, but for your\
          \ soul.]\n\nYou feel... different. The same, but different.\n"
      - action: RANDOM-MIND
        score: 70
        description: Generate a completely random personality
        result: 'The mirror spins, dimensions tumbling like dice...


          [Generates random ratings 0-7 for all 32 dimensions.

          Some combinations are surprisingly coherent.

          Some are beautifully contradictory.

          All are playable.]


          "The universe has rolled your soul. Interesting."

          '
      - action: COMPARE-MINDS
        score: 65
        description: Compare two personality profiles side by side
        syntax: COMPARE-MINDS [profile1] WITH [profile2]
        examples:
        - COMPARE-MINDS my current self WITH my ideal self
        - COMPARE-MINDS me WITH the bartender
        - COMPARE-MINDS my costume personality WITH my real personality
        result: 'Two profiles appear side by side in the mirror...


          [Shows dimensional differences, highlights largest gaps,

          identifies complementary and conflicting traits.]


          "One could become the other. Or meet in the middle."

          '
      - action: VOCABULARY-MODE
        score: 50
        description: Toggle between Plain Talk and Shrink-Rap
        modes:
          PLAIN-TALK: Peppy, Laid-Back, Happy, Sad, Sweet, Grumpy...
          SHRINK-RAP: Hyper-Manic, Low-Energy, Euphoric, Melancholic, Congenial, Hostile...
        result: 'The words on the mirror shift...


          [Toggles vocabulary mode. Some prefer accessible language.

          Some prefer clinical precision. Leary gave us both.]

          '
      - action: SELF-PORTRAIT
        score: 60
        description: Compare your current self with your ideal self
        result: "The mirror splits in two \u2014 left shows WHO YOU ARE,\nright shows\
          \ WHO YOU WANT TO BE.\n\n[Classic Mind Mirror exercise. Large gaps indicate\n\
          areas of growth. Or acceptance. Your choice.]\n\n\"The distance between\
          \ these is your journey.\"\n"
      - action: ROLE-PLAY-ODYSSEY
        score: 55
        description: Test a personality in a life scenario
        result: "The mirror shows a scene from life \u2014 3,200 scenarios\nawait,\
          \ from birth to transcendence.\n\n[Leary's original software had life simulations.\n\
          How would THIS personality handle THIS situation?\nTest empathy. Test compatibility.\
          \ Test limits.]\n"
      - action: SAVE-MIND
        score: 45
        description: Save current personality as a card in notebook
        result: 'The mirror shimmers, and a card emerges from its surface...


          [Creates a personality card with the current Mind Mirror

          profile. Can be stored in notebook, traded, given to NPCs,

          or worn again later. Costumes for the soul.]

          '
      - action: RESTORE-MIND
        score: 40
        description: Restore original personality
        result: "The mirror clears, showing your TRUE self \u2014 the one you\nstarted\
          \ with, before all the costumes and modifications.\n\n[Restores original\
          \ Mind Mirror profile. The costumes\nwere fun, but sometimes you need to\
          \ come home.]\n\n\"Welcome back.\"\n"
```

#### `world_state.objects.maze/room-g/carved-face.yml` lines 9433–9531

Would name `EXAMINE`, `SPEAK-TO`, `ASK-DIRECTION`, `TOUCH`, `OFFER-TRIBUTE`, `MOCK`, `COPY-EXPRESSION`.

```yaml
      advertisements:
      - action: EXAMINE
        score: 80
        result: "The face is carved from the living rock of the wall.\nThe craftsmanship\
          \ is remarkable \u2014 each wrinkle, each pore,\nrendered in perfect detail\
          \ despite centuries of age.\n\nThe eyes are empty sockets, yet you cannot\
          \ shake the\nfeeling that they see you. That they have ALWAYS seen you.\n"
      - action: SPEAK-TO
        score: 60
        result: '"Hello?" you venture.


          The face does not respond. It''s a face carved in rock.


          But was that a slight shift in the shadows around its mouth?

          A trick of the lamplight? Surely. Surely a trick of the light.

          '
      - action: ASK-DIRECTION
        score: 70
        result: '"Which way should I go?"


          The face remains still. But you notice its expression

          seems slightly more approving when you face east.


          The vendor is east. Coincidence? Guidance? Pareidolia?

          '
      - action: TOUCH
        score: 50
        result: 'You reach out and touch the carved stone.


          It''s cold. Colder than it should be. Colder than the air.


          For a moment, you think you feel a pulse. But stone

          doesn''t have a pulse. Stone doesn''t breathe.


          ...Does it?

          '
      - action: OFFER-TRIBUTE
        score: 40
        description: Leave something for the face
        result: 'You place [item] at the base of the carved face.


          The shadows in the eye sockets seem to deepen.

          Approval? Disdain? Hunger?


          [The face remembers your offering]

          '
      - action: MOCK
        score: 20
        score_if:
        - player.wisdom < 5
        result: '"Nice face, stone-head!"


          Somewhere, you think you hear stone grinding against stone.


          The face''s expression hasn''t changed. Of course it hasn''t.

          It''s carved in rock.


          But you feel watched. More watched than before.


          [The face remembers your disrespect]

          '
      - action: COPY-EXPRESSION
        score: 45
        result: 'You arrange your face to match the carved one.

          Stern. Impassive. Ancient.


          You hold the expression for a long moment.


          When you relax, you could swear the face looks...

          amused? No. That''s impossible. Stone doesn''t get amused.

          '
```

#### `world_state.objects.maze/room-i/skeleton.yml` lines 9544–9615

Would name `EXAMINE`, `READ-NOTE`, `TAKE-LAMP`, `TAKE-GOLD`, `PAY-RESPECTS`, `GIVE`, `PROMISE`.

```yaml
      advertisements:
      - action: EXAMINE
        score: 80
        result: 'The skeleton slumps against the wall, one bony arm extended

          toward the west passage. Their empty lamp lies beside them.

          A partially-eaten note is clutched in their other hand.

          '
      - action: READ-NOTE
        score: 75
        result: "You gently pry the note from skeletal fingers:\n\n\"I should have\
          \ brought more food to mark the rooms. \nI dropped the cheese in room B\
          \ and the bread in room D \nbut then I got confused and\u2014\"\n\nThe writing\
          \ ends mid-sentence. You can imagine the rest.\n"
      - action: TAKE-LAMP
        score: 60
        result: 'You pick up the empty lamp. It''s identical to yours, just... empty.

          A sobering reminder of what happens when the light goes out.


          (You could refill it at the vendor in room-j, if you wanted

          a backup lamp. Redundancy is underrated in grue territory.)

          '
      - action: TAKE-GOLD
        score: 50
        result: 'You take the 3 gold pieces. The skeleton doesn''t seem to mind.

          They won''t be needing them where they''re going.


          player.gold += 3

          '
      - action: PAY-RESPECTS
        score: 70
        result: 'You stand in respectful silence for a moment.


          "Rest well, fellow adventurer. Your sacrifice teaches us:

          bring food, not coins. And check your lamp oil. Often."


          The skeleton grins. Was that a nod? Probably just your imagination.

          '
      - action: GIVE
        score: 40
        description: Leave something for the skeleton
        result: 'You place [item] beside the skeleton as a memorial.

          The gesture feels right. Someone should remember them.

          '
      - action: PROMISE
        score: 65
        description: Make a promise to avenge them
        result: '"I will avenge you," you say solemnly to the skeleton.

          "The grue that did this will pay."


          The skeleton seems to approve. Or maybe that''s just the grin.


          [NEW GOAL: Avenge the skeleton by slaying the grue in room-f]

```

#### `world_state.objects.maze/room-h/the-thing-that-watches.yml` lines 9631–9704

Would name `EXAMINE`, `SPEAK-TO`, `TOUCH`, `FEED`, `ASK-ABOUT-GRUE`, `THANK`.

```yaml
      advertisements:
      - action: EXAMINE
        score: 80
        result: 'The Eye meets your gaze. You feel... seen. Deeply seen.

          Uncomfortably seen. Seen in ways you didn''t know were possible.


          The mushrooms pulse. The Eye blinks. Once. Twice.


          You look away first. Everyone looks away first.

          '
      - action: SPEAK-TO
        score: 60
        result: '"Hello?" you venture.


          The Eye widens slightly. The mushrooms pulse faster.


          No response comes. But you have the distinct feeling

          that you''ve been... acknowledged.

          '
      - action: TOUCH
        score: 30
        score_if:
        - player.wisdom < 10
        result: "You reach toward the Eye.\n\nThe mushrooms RECOIL. The Eye WIDENS.\
          \ A sound emerges \u2014\nnot quite a scream, not quite a word, something\
          \ between\na warning and a memory.\n\nYou snatch your hand back. Your fingers\
          \ tingle.\n\nFor the next hour, you can see slightly better in the dark.\n\
          Also, your dreams will be... interesting tonight.\n"
      - action: FEED
        score: 50
        description: Offer food to The Thing
        result: 'You place [food] before The Thing.


          A tendril of mushroom extends, examines the offering,

          and slowly absorbs it.


          The Eye closes in what might be satisfaction.

          When it opens, it seems... warmer? Toward you?


          [The Thing That Watches remembers your kindness]

          '
      - action: ASK-ABOUT-GRUE
        score: 70
        result: "\"The grue,\" you say. \"Why won't it come here?\"\n\nThe Eye looks\
          \ toward the south exit \u2014 toward room-f,\nwhere the grue lives. The\
          \ mushrooms shudder.\n\nYou understand without words: The grue fears being\
          \ seen.\nAnd The Thing sees EVERYTHING.\n"
      - action: THANK
        score: 65
        result: '"Thank you," you say. "For keeping them away."


          The Eye blinks slowly. The mushrooms glow a little brighter.


          You''re not sure it understands gratitude. But you''re not

          sure it doesn''t, either.

          '
```

#### `world_state.objects.maze/room-f/gold-pile.yml` lines 9719–9735

Would name `GET`, `COUNT`, `EXAMINE`, `TAKE-SOME`. `action: TAKE SOME` stays, because the key spelling differs.

```yaml
      advertisements:
      - action: GET
        score: 95
        result: "You scoop up all 100 gold coins. Your pockets bulge \nmagnificently.\
          \ You feel like a dragon. A small, \nwaistcoat-wearing dragon with excellent\
          \ taste in spoons.\n\nplayer.gold += 100\n"
      - action: COUNT
        score: 60
        result: Exactly 100 gold pieces. Someone was prepared!
      - action: EXAMINE
        score: 50
        result: ACME coins. Accepted at all fine dungeon vendors.
      - action: TAKE SOME
        score: 40
        result: "\"How many? You have space for all of them. Don't be weird \nabout\
          \ it \u2014 no one's watching. The skeleton certainly isn't \ngoing to judge\
          \ you.\"\n"
```

#### `world_state.objects.maze/room-j/lamp-vendor.yml` lines 9811–9863

Would name `BUY-OIL`, `BUY-DELUXE`, `BUY-PREMIUM`, `EXAMINE`, `KICK`, `INSERT-COIN`. The spaced `action` values stay.

```yaml
      advertisements:
      - action: BUY OIL
        score: 90
        score_if:
        - player.inventory contains lamp
        - lamp.oil < 100
        result: 'Refills lamp to 400 oil. Costs 1 gold.

          '
      - action: BUY DELUXE
        score: 80
        score_if:
        - player.inventory contains lamp
        - lamp.oil < 50
        - player.gold >= 2
        result: 'Refills lamp to 800 oil. Costs 2 gold.

          '
      - action: BUY PREMIUM
        score: 70
        score_if:
        - player.inventory contains lamp
        - player.gold >= 3
        result: 'Refills lamp to 1000 oil AND makes it glow blue.

          The blue glow is unsettling to grues. They approach more slowly.

          Costs 3 gold.

          '
      - action: EXAMINE
        score: 50
        result: Read the machine's display and notices.
      - action: KICK
        score: 30
        score_if:
        - player.gold < 1
        result: 'The machine shudders but holds firm.

          "VIOLENCE AGAINST VENDING MACHINES IS A FEDERAL OFFENSE"

          flashes on the display. Then, softer:

          "...but I understand. Here, take this."

          A small vial of lamp oil drops into the dispensing slot.

          (One-time mercy refill. Don''t tell the other adventurers.)

          '
      - action: INSERT COIN
        score: 40
        result: Same as BUY OIL.
```

### Four stove files, one text

These four files are the same bytes, list included, at lines 21–29:

- `examples/adventure-4/kitchen/stove.yml`
- `examples/old/adventure-1/kitchen/stove.yml`
- `examples/old/adventure-2/kitchen/stove.yml`
- `examples/old/adventure-3/kitchen/stove.yml`

Each `transform` raises `action: names several verbs (one advertisement or several?)` on `TURN-ON, TURN-OFF`. The comma is the `[,/|]| or ` test in `advert_name`. `EXAMINE` would key as `EXAMINE`. The first entry is the skip.

```yaml
advertisements:
  - action: TURN-ON, TURN-OFF
    score_if: "state == off/on"
    description: "Light and extinguish the stove"
    response: "Don't play with fire! You don't have time for cooking! There's treasure to find!"
    
  - action: EXAMINE
    description: "Inspect the stove"
    response: "The stove is {state}."
```

### `examples/adventure-4/pub/rooms/room-3/context-orrery.yml` lines 49–60

`plan()` raises `trigger too long to name an advertisement (> 4 words)` on the third entry. `context window` and `token limit` are 2 words and would key `ON-CONTEXT-WINDOW` and `ON-TOKEN-LIMIT`. `what do you know about` is 5 words.

```yaml
advertisements:
  - trigger: "context window"
    score: 95
    say: "The orrery shows what's in scope. Watch the orbits."
    
  - trigger: "token limit"
    score: 90
    say: "The outer orbits fall away first when pressure rises."
    
  - trigger: "what do you know about"
    score: 70
    say: "Check if it's orbiting. If not, it's outside context."
```

### `examples/adventure-4/pub/rooms/room-3/thinking-mirror.yml` lines 40–51

`plan()` raises the same trigger-length skip on the second entry. `what am I thinking` is 4 words, and the test is `len(words) > 4`, so that entry is inside the limit and would key `ON-WHAT-AM-I-THINKING`. `why did I do that` is 5 words. `introspection` is 1 word and would key `ON-INTROSPECTION`.

```yaml
advertisements:
  - trigger: "what am I thinking"
    score: 95
    say: "Look in the mirror. It already knows."
    
  - trigger: "why did I do that"
    score: 90
    say: "The mirror shows the reasoning. Scroll back."
    
  - trigger: "introspection"
    score: 85
    say: "Introspection is just reading your own thinking blocks."
```
