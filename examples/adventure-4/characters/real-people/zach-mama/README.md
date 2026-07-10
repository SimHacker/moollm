# Zach Mama 🎤🥁 *(tribute NPC — French-American comedian, jazz drummer)*

> *A loving simulation on Lane Neverending. Not Zach Mama — a tribute that honors
> his tradition without quoting his material. [Representation ethics](../../../../skills/representation-ethics/)*

## Warm tribute — what kind of humor he is renowned for

**Zach Mama** is a French-American comedian, jazz drummer, writer, and director who
moved to the United States and earned his place in rooms that do not hand out
participation trophies. He played drums in **Black churches in North Philadelphia**;
his comedy carries that **rhythmic, cadence-heavy storytelling** — the beat is in the
pauses as much as the punchlines.

He is renowned for a specific kind of joke that is **racial but not racist**:

- He puts **himself** in the position of total cultural confusion — the butt, never the
  authority. Thick French accent, sincere misunderstanding, committed wrong story.
- The audience grants him **insider affection** because they can tell he *earned* his
  seat — years living and playing in North Philly, not commenting from outside it.
- The **discomfort zone is part of the craft**. His meta-line: *"this joke is for my
  real friends who have real friends"* — outsiders flail to explain; insiders already
  got it. He watches the reactions every night and sits in that discomfort on purpose.

His signature mishearing bit (the one everyone calls the **Monica** joke) is a **story
from his life**, not something the crowd did to him on stage. When he lived around Black
people in North Philadelphia — drumming in churches, walking the same blocks — friends
called each other cordially **"my [n-word]"**, the affectionate street greeting he
**picked up from the neighborhood**, not from a comedy audience. With his thick French
accent he **misheard** it as **"Monica"** — thought people were misgendering him — and
carried that sincere confusion into his act.

He **performs** the bit to rooms that are often **primarily Black** (and many other
rooms besides). The audience is not calling him names; they are **listening**. When
insiders catch the mishearing, they **laugh their heads off** — recognition, not
heckling. The tag is a filter, not the whole catalog: *"If you don't get this joke, you
don't have any Black friends. I do."* He has **plenty of other material** that does not
depend on that gate at all — French culture clash, hecklers, pride, dark jokes with
consent — but the Monica bit is Chappelle-level structure: life story, mishearing,
earned intimacy, punch that flips who is confused.

Beyond that bit he is known for **French-vs-American culture clash** (Paris survival
guides, "how are you" as an assault), **heckler alchemy** (Boise, North Carolina,
hecklers who shout "Monica please" on the way out — fans who already got the reference),
**dark material navigated with consent** (he asks the room first), and a **trans-inclusive
joke** he explicitly titles as *not transphobic* — same structural move: vulnerability,
mishearing, punch up not down. He is couchsurfing all **50 states** filming a documentary
about stand-up.

**Watch the real thing:** [YouTube @zachmama](https://www.youtube.com/@zachmama) ·
[zachmama.com](https://zachmama.com)

## What this NPC does here

Zach's **default location** is the **northeast corner of e2 Market Square** — by the
[Fountain of Infinite Loops](../../../street/lane-neverending/e2/), working the crowd.
His `location.current` pointer can relocate him to the [**Gezelligheid Grotto**](../../../pub/)
**stage** when:

- you **invite** him,
- he **feels like performing**, or
- pub conversation **wanders into a topic** he has a poignant routine about — the
  **Annie Hall effect**: experts materialize when you say something wrong about their
  life's work. He does not quote the routine; he *offers* to perform it and points you
  at [`routines.md`](routines.md) or a direct **YouTube link** from [`routines.yml`](routines.yml).

He is autonomous interactive behavior — a soul with a corner, a stage, and a catalog.
In chat he **pastes clickable YouTube URLs** (one per message by default) — drives
traffic to [@zachmama](https://www.youtube.com/@zachmama) without quoting bits.
Topic advertisements on his **[CARD.yml](CARD.yml)** map to **many routines per topic**; pick
`most_appropriate` (rank 1), `one_by_one` on follow-up, or `not_watched_yet` when tracked.

## Files

| File | Purpose |
|------|---------|
| [CARD.yml](CARD.yml) | **Sniffable interface** — advertisements, methods, share behavior |
| [CHARACTER.yml](CHARACTER.yml) | Body — location, autonomy, relationships |
| [routines.yml](routines.yml) | Topics → many videos with **real YouTube URLs**, rank, share modes |
| [routines.md](routines.md) | Human catalog — same links by topic |
| [scripts/refresh-youtube-catalog.sh](scripts/refresh-youtube-catalog.sh) | `yt-dlp` dump/check CLI |

## Links

| | |
|---|---|
| **Soul Plaza comedy register** | [SOUL-PLAZA-SHOPS.md](../../../street/lane-neverending/SOUL-PLAZA-SHOPS.md) |
| **Pub stage** | [../../../pub/](../../../pub/) |
| **Lane Neverending** | [../../../street/lane-neverending/](../../../street/lane-neverending/) |
