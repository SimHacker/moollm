# MOODY: Mood Is Multimedia (Multimoodia)

Media that broadcasts meaning. A song is not just an audio track — it
carries a **parameter track**: time-varying heat levels for semantic
tags. Romantic, intellectual, educational, athletic, energetic,
imaginative — every emotion and reaction music can inspire, encoded as
envelopes that ride along with the waveform. When the artifact plays,
it broadcasts the track into the room. When it stops, the broadcast
stops. Mood is multimedia. **Multimoodia.**

Proposed by Don Hopkins to the Maxis team on **February 18, 1999** —
almost four years before The Sims Online — under the name **SimRadio**,
with the "moody track" as its emotional payload (primary source below).
It didn't ship. This document is the design, its history, and what
MOOLLM does with it now that the technology (and the object system)
finally caught up.

## The parameter track

Every moody artifact — a song, a video, a pure mood object with no
audible surface at all — carries alongside its media a track of
`(time, tag, heat)` envelopes:

```yaml
moody:
  tags:
    romantic:     [{t: 0, heat: 0.2}, {t: 45, heat: 0.9}, {t: 180, heat: 0.4}]
    energetic:    [{t: 0, heat: 0.1}, {t: 30, heat: 0.6}]
    intellectual: [{t: 0, heat: 0.0}]
```

The tag vocabulary is open: intellectual, romantic, educational,
athletic, energetic, imagination, melancholy, menace, nostalgia,
whatever the artifact can actually induce. Heat varies over time — the
slow build of a ballad, the drop in a dance track, the third-act
turn of a film — so the room's emotional weather has **weather**:
fronts move through, storms build and break. A mood swing is literally
an envelope.

## Two knobs: volume and meaning

The player gets a **volume knob** and a **meaning knob**, independent.
Volume modulates the audio amplitude; meaning modulates the semantic
amplitude — how hard the parameter track presses on the room. Turn the
meaning down and the love song is just pleasant noise; turn it up with
the volume at zero and you have a silent object radiating pure
influence — a scented candle, a mood ring for the room, a dog-whistle
broadcast only the behavior engine hears. The two knobs make the point
of the whole design in hardware: **the meaning of media is a separate
channel from its surface**, separately mixable.

## Rooms inherit heat; heat is ambient context

Ambient heat comes from **the room**, and the room inherits it, varying
over time, from whatever moody media is playing in it — audio, video,
pure mood objects, all summed into the room's current emotional
weather.

The Sims shipped a primitive ancestor: the **Room motive**, a static
scalar computed from décor, light, and mess. Moody generalizes the
scalar to a **time-varying vector**. The room score stops being a
number and becomes a climate.

Characters don't poll the stereo. They read the room — literally an
API call. **Setting the mood is a write; reading the room is a read.**
In Korz terms (Ungar, Ossher, Kimelman), ambient heat is a set of
**implicit context dimensions**: the room sets `{romantic: 0.9,
energetic: 0.3}` and every dispatch inside inherits it without any
object mentioning it in its signature — the `assertions: true` trick,
applied to atmosphere. In Sims terms, heat re-weights the
advertisement auction per tag: romantic heat up-scores the flirt ads,
athletic heat up-scores the basketball hoop, and the same object
advertises differently at midnight than at noon without changing a
byte of itself.

And **dispatch temperature can ride the track too** (see the dispatch
spectrum in [GAME-PIECES.md](GAME-PIECES.md)): a slow dance broadcasts
high romantic heat with *low* temperature — commit to the moment, no
dithering — while a party track broadcasts high energetic heat with
*high* temperature: anything strong might happen next. The DJ is
adjusting the room's exploration/exploitation tradeoff with a
crossfader.

## Your song: experience writes back

Everything above is the read path: authored tracks broadcast into
rooms, characters feel them. The other half of the design is the
**write path**. When a character has an experience while moody media
is playing, the experience writes an association back — onto **that
exact moment of that exact media** — creating a
**character-and-media-and-time specific overlay**. The overlay is
private: it plays back every time to that particular character, and
*only* they hear the tracks they added. The authored moody track is
the shared public base layer; personal overlays are private tracks
stacked above it — same envelope schema, different provenance,
different visibility.

Two granularities, one mechanism:

- **The ambient wash.** A joyous wedding gently associates *all* the
  songs that were playing — whole songs, entire — with happiness,
  bliss, and memories of the people being married. Low heat, wide
  envelope, many songs at once: the soundtrack of an afternoon
  becomes faintly golden forever.
- **The spike.** Your first kiss with your future spouse writes a
  **strong spike of emotion at the particular time of the particular
  media** that was playing — plus a full-song association around it.
  High heat, narrow envelope, one timestamp of one song.

The storage is Sims machinery, extended to media: each song carries a
**relationship matrix** with characters and objects (the song-level
associations — this song and that person, this song and that porch
swing) and a **temporal relationship matrix** (time-indexed: what
happened at t=1:47, who was there, what it felt like). A song is a
first-class party to relationships, exactly like a person.

Playback closes the loop. That song becomes **"your song"** — both of
you are moved whenever it plays, because you both wrote spikes onto
the same timestamp of the same media, and at the particular kiss
point you both get a strong emotional ping, together, every time.
"Darling, they're playing our song" is a temporal relationship matrix
having a cache hit. Proust's madeleine is the cross-modal case — any
media, any sense, can carry an overlay; involuntary memory is just
playback you didn't schedule.

And the overlays feed the auction like everything else. A song with a
grief spike *inhibits* — the widow leaves the room when it comes on;
the jukebox becomes a gift or a weapon; a suitor who learned your
song courts with it, and a cruel ex torments with it. The DJ can read
the room's aggregate public heat but never the private overlays,
which is exactly right: the radio knows what the song means, only you
know what it *meant*.

**Netflix and chill becomes a moody jam recording session.** Shared
media consumption is co-recording: two characters writing interleaved
private overlays onto the same movie at the same timestamps. The
movie becomes a shared diary that plays back differently to each of
them — and the correlation of their spikes at the same moments is the
measurable trace of a shared experience. Rewatching it together
replays both overlays in sync: the mood jam, remixed live, gaining a
new layer every session.

### The wedding playset: a ceremony is a mastering session

The write path at full scale is a wedding. The **wedding playset**
lets you build a jukebox of songs for the ceremony, including songs
bound to **formal cue points**: the processional (walking down the
aisle), the vows, the ring, the first dance, the bouquet toss. A
ceremony is a score with named slots, and filling the slots with
*your* music is the point — which makes wedding music the strongest
custom-content motivation in the game: import the songs, mark up
their moody tracks by hand, author the emotional arc of the biggest
day of your characters' lives.

When you perform the wedding, the playset plays the mood into the
audience, and the write path runs for **everyone attending at
once**: every guest gets overlays associating those songs with the
couple, the venue, and each other. A wedding is a mastering session
for a room full of hearts — "your song" written into a few dozen
ledgers simultaneously, which is why the whole town mists up when
the processional comes on at the diner years later. And the
reception keeps recording: dancing to the playlist, Netflix and
chill afterward — living and recording lifelong emotional
experiences, the foundational ambient background memories of a whole
life, laid down in the overlay layer where nothing but playback can
reach them.

You can have as many weddings and jukeboxes as you want. Serial
romantics accumulate emotional archaeology — strata of overlays from
different marriages on overlapping songs. And harsh breakups **edit
the responses**: the breakup remaster, a grief pass written *on top*
of the old joy rather than erasing it. The overlay layer is
append-only, like a heart — the song that made you swoon now makes
you leave the room, and the old joy is still under there, which is
exactly why it aches.

## Constraints: heat drives parameters, buffs gate the wires

Advertisement re-weighting is the *soft* consumer of heat. The hard
consumer is **constraints**: declarative bindings (the
OpenLaszlo/Declare move — Temkin's instance-first constraint lineage)
that wire an environmental moody track directly to room and character
parameters, which in turn drive anything downstream. While the
binding is active, the parameter *follows the envelope*: a happiness
constraint tracks the joy tag of whatever's playing, room lighting
warms with the romantic envelope, a horror soundtrack's dread tag
drips straight into a character's comfort motive.

And **buffs enable and disable the constraints** — the binding is
exactly a conditional delegation edge from
[GAME-PIECES.md](GAME-PIECES.md): present, but only answering while
its condition holds. A BLISSED buff wires the room's joy envelope
into happiness at full gain; noise-cancelling headphones are a buff
that *disconnects* the wearer from the room's audio bindings
(silencing meaning as well as sound — or, with the meaning knob up,
only the sound); earplugs disable, mood amplifiers enable, a stiff
drink lowers the threshold on every romantic binding in the room.
Robust-first as always: a disabled constraint is not torn down, it
just stops writing — no stale bindings, no cleanup pass.

The degenerate case proves the range: **the brown note**. The
legendary infrasound frequency that makes you shit your pants is, in
this schema, just a tag whose constraint binds not to a mood but to
the **bladder motive, at max gain** — bladdermaxing: media driving
physiology, skipping the heart entirely. In The Sims it would be
localized as **the blue note**, because Sims pee blue puddles — the
game collapses all bodily catastrophe into one blue-puddled bladder
motive, so the note comes out the color of the puddle. (A blue note
is also the bent, flatted tone that makes the blues the blues, which
is exactly the register of a Sim standing in a puddle with both
hands on their head. No yellow or red notes — the palette is canon.)
MythBusters busted the note in the real world; in a microworld it
works every time, which is why the prank subwoofer with a BLUE-NOTE
parameter track is a legitimate plug-in object, and why the diaper
is a buff that disables exactly one binding. The point under the
joke: the moody track is a general-purpose parameter bus. Mood was
just the first thing worth broadcasting on it.

## The zig-zag: the simulation composes, the tape remembers

Three directions now. Authored moody media broadcasts meaning into
the world (the read path). Experience writes overlays back onto media
(the write path). The **zig-zag** is generation with a tape recorder
running: **generate moody music in response to events in the
simulation** — the Spore direction, music *from* meaning — **and
record the parameters as they're emitted, making a new moody object
you can replay.**

The recorded object is not an audio file with annotations bolted on.
It *is* the parameter stream — the meaning and the music in one
artifact — so replaying it re-synthesizes the sound *and*
re-broadcasts the feeling, and it can be **sampled, remixed, looped,
and scrubbed**. Scrub the wedding tape back and forth and the room
re-feels the toast, the kiss, the first dance, in any order, at any
speed. The reference instrument is **Laurie Anderson's tape-bow
violin**: recorded tape in the bow, a playback head on the bridge, so
that *performance is scrubbing a recording* — bowing a memory
forward and backward, at whatever speed the arm feels. The moody tape
is that, for feeling. Bow the memory.

To generate and record this well, the schema needs the musical
vocabulary as first-class terms — the words composers already use for
the shape of time:

- **envelopes** at the tag level: attack, decay, sustain, release —
  ramping up, dying away
- **dynamics**: crescendo, diminuendo, sforzando (the spike has a
  name in Italian)
- **motion**: accelerando, ritardando — escalation and relaxation as
  first-class curves
- **tension and closure**: build, drop, suspension, cadence — the
  resolution operator, the reason a scene feels *finished*
- **heat, energy, valence** — the moody tags themselves
- **determinism** — the temperature track, recorded like everything
  else: how dithered the moment was is part of the memory, so a
  chaotic party scrubs differently than a solemn vow

One vocabulary, both provenances: a composer hand-writes the same
envelopes the simulation emits live, so hand tracks and machine
tracks remix on equal terms — the jam session between the author and
the world. And the zig-zag composes with the write path
automatically: a tape generated at your wedding is born already being
"your song," the overlays mastered in at the moment of recording. The
generated tape is a save file of feeling — the home movie that knows
what it meant.

## Moody IRL: the ebike safari

None of this needs a game engine. Real life is already running the
simulation, and the shippable-now version of the zig-zag is a phone
on a bicycle. Ride an **ebike safari** through a city with music
playing, and record a **place+time sync track**: the song and its
position, the GPS trace, the photos and video you shoot, and your
spoken impressions — speech-to-text, either keyword commands
("mark," "love this," "come back here") or free natural-language
narration about what you're seeing. Every input lands on the same
timeline: `(time, place, tag, heat)` — the moody schema with two more
columns. Place is just more dimensions in the context.

The novel input channel is **GPS gestures**: the bike's path is a
gesture stroke drawn on the map plane, and it can be recognized like
any other gesture. **Stop in front of an address** — dwell is a
point-select, and dwell time is heat. **Encircle a fountain, a
statue, a block, a roundabout** — the loop is a lasso-select, and
what it encloses is the point of interest. The city is the screen,
the bike is the pen, and the ride is the ink. (Roundabouts are
pre-installed circular gesture guides — the municipal infrastructure
was built for this and never knew it.) No screen interaction while
riding: the annotation *is* the riding.

Playback is the tape-bow again, in real coordinates. Scrub the
safari and the music, the map position, the photos, and the spoken
impressions all stay in sync — bow your way back down the
Amstel at any speed, in either direction. The write path works in
real coordinates too: the song you were playing when you rounded
that fountain now carries a spike at that timestamp *and* that
lat/lon, so hearing the song re-evokes the place and returning to
the place re-evokes the song — the madeleine, geofenced. Share the
tape and a friend can ride your ride, with your soundtrack, your
photos surfacing as they pass the spots where you took them.

This is the version that ships soonest: no game, no engine, no
platform permission needed — a phone, an ebike, GPS, a music app
with a position API, and a speech-to-text loop. The artifact it
produces is a standard moody object, so the day a game or MOOLLM
microworld wants to import your safari as an in-world tape, the
schema is already the same.

And it shouldn't require the bike. A **demo mode** in any desktop or
mobile web browser gives the full experience without wheels, two
control schemes deep: **direct position manipulation** — drag the
marker to move instantly, or click a destination and the virtual
bike routes there on the real street network — and **first-person
riding**, with tilt gestures to steer on mobile. Every gesture works
identically: circle the fountain with your finger or with your
routed path and it's the same lasso, writing the same tape. Demo
mode is how the proof of concept travels — anyone, anywhere, can
ride your Amsterdam safari or record their own imaginary one, and
the tapes are interchangeable with the ones recorded on real
streets.

## SimRadio: live streaming into the dollhouse

The primary source is the **"Live SimRadio on the net" email of
February 18, 1999** to the Maxis team, harvested in full in
[WWSFF: simradio-moody-1999-maxis-email.md](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/simradio-moody-1999-maxis-email.md).
The pitch: Maxis runs **SimRadioStation** servers broadcasting MP3
music and **SimDJ** dialog over IP multicast, and the game gets a
receiver — solving "the problem of repeated music loops driving
players insane" while opening an advertising and distribution channel
for plug-in objects and Maxis/EA products. The moody track rides the
stream: music "encoded with a 'moody track', **marked up with events
that affected people emotionally**."

The advertisements are the load-bearing pun. A radio ad **is** a Sims
advertisement in the full behavioral sense: broadcast into the room,
scored by every character who hears it, acted on by the susceptible.
And the live kind carries a deadline — the email's twist is real-time
interactive call-in contests where **the contest players are the Sims**
(autonomous or player-directed), who "have to run to the phone and try
to be the 20'th caller when they hear a song by the Beatles." An
advertisement with an **expiration window**, answered inside the game
world by characters sprinting to the phone alongside the humans
listening to the same live stream. In [GAME-PIECES.md](GAME-PIECES.md)
terms, a time-windowed ad is a **buff with an expiration date**: it
stands next to the room, shouts into the auction, and stops answering
when the window closes. No cleanup, because the menu was never stored,
only derived.

The 1999 email had the whole economy sketched around that loop:

- **SimPrizes** — virtual money, furniture, personal growth,
  interesting visitors ("dinner with Elvis!"), unique decorative items
  (a Jim Morrison or Kermit the Frog poster), or real Maxis products
  ("Win a trip to the big SimCity!"). "Think of it like a game show,
  where the show is actually an entertaining advertisement for the
  prizes" — advertising as native content instead of interruption.
- **DLC with a doorbell** — win a plug-in object on air and it's
  seamlessly downloaded and "delivered to the front door," instead of
  leaving the game for an unwieldy FTP client. Object distribution as
  a diegetic event, before the term DLC existed.
- **Registration as carrot** — demo copies pick up free ad-heavy
  broadcast stations; registered copies get "cable TV" and "digital
  radio" with the good music, contests, and prizes. Anti-piracy by
  making the legitimate copy *more alive*.
- **"This would put the game 'online'"** — same broadcast, same time
  window, competing against other players — with, per the email, no
  major changes to the game's design or code. The Sims Online energy,
  four years before The Sims Online, at a fraction of the cost.

And the moody track came with **per-person reaction** built in:
"different people would react to the musical moods in different ways."
Heat is filtered through personality, never applied raw — the same
tag envelope makes the romantic Sim swoon and the grouchy one leave
the room. The email's worked examples are the design in miniature:
call the station and request a Sim's favorite song to raise their
happiness; "turn an unruly crowd into a wild party by turning off the
cop show on TV, and switching on the radio to a dance music station."
The DJ as behavior-engine input, the remote control as a mood API.

### A moody jukebox for The Sims 1, in SimAntics

Moody could ship *backward in time*, as custom content for the
original game. The build: a **jukebox object programmed in
SimAntics**, plus a companion authoring tool in the Transmogrifier
lineage — pick your MP3s, pair each with a hand-authored moody
track, and the tool generates the custom jukebox object with the
envelopes baked into its behavior data. While a song plays, the
jukebox's SimAntics tree walks the envelope and pushes mood and
motive deltas to everyone in the room — the room-inherits-heat model
retrofitted onto 2000-era simulation.

The honest engineering question is **synchronization**. SimAntics is
tick-driven: the object's only native clock is the simulation tick,
audio playback is fire-and-forget in the sound subsystem, and there
is no obvious wall-clock primitive — so out of the box, we're **hot
dogging it**: open-loop dead reckoning. But dead reckoning with
instruments is respectable navigation:

- **t=0 is known.** The jukebox issued the play call, so the song's
  start is anchored to an exact tick.
- **Ticks convert to seconds by calibration.** The companion tool
  ships measured ticks-per-second constants for each game speed;
  modern machines run The Sims 1 at full speed reliably, so the
  conversion is stable enough to track a song within a second or
  two. Game speed itself is invisible from inside the VM (ticks are
  the only clock, so all speeds feel identical from within), which
  leaves options: assume speed 1 and accept drift at fast-forward,
  or let the calibration err toward the speed players actually
  listen at.
- **Resync is free at every track boundary**, because the jukebox
  controls when songs start. Drift never accumulates past one song.
- **The envelope is forgiving.** This is emotional weather, not
  lip-sync: an ambient wash needs no synchronization at all, and a
  spike that lands two seconds late on a swell is inaudible in the
  heart. Quantize envelopes to coarse sections (intro, verse,
  chorus, drop) and dead reckoning never misses by a section.
- **The clean fix lives in the reimplementations.** FreeSO and
  Simitone can grow a real wall-clock or audio-position primitive
  properly, making the jukebox closed-loop where the platform allows
  it.

Precedent for the hot dogging: The Sims 1 itself never synced —
dancing Sims loop their animations near the stereo without a beat
tracker, and nobody ever noticed. Period-authentic imprecision.

## Precedents and kin

### Muzak: stimulus progression (1940s)

The 1940s shipped time-varying mood parameter tracks at industrial
scale. Muzak began as Wired Radio, Inc., founded on the patents of
**Major General George Owen Squier** (US Army Signal Corps, inventor
of multiplexed transmission over power lines), who coined the name by
splicing *music* into his favorite brand, *Kodak*. Its signature
product, **Stimulus Progression**, was a quantified mood engine: every
recording was assigned a numeric **stimulus value** based on tempo,
rhythm, instrumentation, and ensemble size, and programming was
assembled into **fifteen-minute blocks of ascending stimulus**
followed by silence — an envelope shaped to counter the measured
mid-morning and mid-afternoon dips of the industrial **fatigue
curve**. Wartime factories ran it on purpose (alongside the BBC's live
*Music While You Work*, 1940, with its own tempo and orchestration
rules); Muzak sold documented productivity claims for decades before
retiring Stimulus Progression in the 1980s as quantity-of-mood gave
way to "Audio Architecture" branding. The standard history is
**Joseph Lanza, *Elevator Music: A Surreal History of Muzak,
Easy-Listening, and Other Moodsong*** (1994; rev. 2004).

So the parameter track is not speculative — it ran for half a century.
Muzak just never published the schema, kept one scalar dimension, and
pointed the envelope at the *employer's* goal (output per worker).
Moody is stimulus progression with the schema in the open, per tag —
and pointed the other way, per the advertisements-that-learn rule in
[GAME-PIECES.md](GAME-PIECES.md): heat tuned to the *inhabitant's*
observed good, not the owner's extraction curve. Same engineering,
opposite principal.

### Eno: ambient, generative, and the loop back to Maxis

**Brian Eno** named the genre and stated its contract in the liner
notes of ***Ambient 1: Music for Airports*** (1978, following
*Discreet Music*, 1975): ambient music "must be able to accommodate
many levels of listening attention without enforcing one in
particular; it must be **as ignorable as it is interesting**." That is
a two-knob specification avant la lettre — surface you can tune out,
influence that keeps working — and Moody media is ambient music with
the influence channel made machine-readable.

Eno then spent decades making the *generator* explicit: the
rule-driven **generative music** systems he named in 1996 (the SSEYO
Koan software releases, and his talk framing composers as people who
plant seeds rather than build objects), later the ***Bloom*** app with
Peter Chilvers and *77 Million Paintings*. The lineage loops back to
Maxis concretely: for ***Spore*** (2008) Eno worked with Maxis audio
director **Kent Jolly** and composer **Aaron McLeran** (their GDC 2008
talk, *Procedural Music in SPORE*, is the reference; Jolly's Pd
convention paper covers the engineering) on a **generative score
running in EAPd** — EA's embedded dialect of Pure Data, used as event
logic driving the game's audio engine — music that mutates with how
you play rather than streaming fixed. Jolly compared Eno's
contributions to *Apollo: Atmospheres and Soundtracks*; Eno sent a CD
of new material within a week of the first phone call. It is the moody
track's inverse twin: instead of annotating fixed music with meaning,
generate the music *from* the meaning.

And the personal loop: Eno coined **"The Long Now"** and co-founded
the Long Now Foundation, where on **June 26, 2006** he and **Will
Wright** gave the seminar ***Playing with Time*** — generative music
and generative simulation as the same idea in different clothes
([YouTube](https://www.youtube.com/watch?v=Dfc-DQorohc) · WWSFF source
bundle with transcript:
[`will-wright/sources/2006-06-26-long-now-playing-with-time-eno-wright/`](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/will-wright/sources/2006-06-26-long-now-playing-with-time-eno-wright) ·
[Eno's room and show ideas](https://github.com/SimHacker/WillWrightShowForFood/tree/main/characters/brian-eno)).
Don met Brian after that talk and introduced him to Scott Draves of
Electric Sheep — a distributed generative artwork that is itself a
room-scale mood broadcast.

### The rest of the family

- **Film scoring and leitmotif** — a parameter track performed by an
  orchestra: the composer annotates the scene's semantic heat and the
  audience's behavior engine responds on cue.
- **The Sims' actual radio and TV** — Sims danced to the stereo and
  cried at sad TV; the channels were static heat sources with fixed
  tags. Moody makes the heat time-varying and the source live.
- **Set and setting** — the psychedelic-research term for how context
  shapes experience. The room is the setting; Moody gives the setting
  a mixing board.

## Why it didn't ship

Three reasons, in honest order:

1. **Opportunity cost.** The Sims was drowning in more-essential work;
   every feature on the disc displaced another. The email argued the
   integration itself was cheap ("would not require any major changes
   to the design of the game or the code") — but the servers, the
   stations, the SimDJs, and the live-ops staffing were a business,
   not a feature, and that business lost fair fights to features the
   game could not ship without.
2. **Technology timing.** It was practical in the RealAudio/SHOUTcast
   era — barely. The infrastructure for millions of concurrent
   listeners with synchronized interactive windows wanted the later
   internet.
3. **EA was conservative** with its flagship franchise — not an
   out-of-the-box-thinking kind of publisher about what a game could
   be connected to. Live talk radio with call-in windows inside The
   Sims was several boxes outside the box.

Pieces of the email did ship, slowly, at Maxis itself: the celebrity
visitor arrived as Drew Carey's limo in *House Party* (2001), diegetic
front-door delivery as *Makin' Magic*'s mystery box (2003), and "this
would put the game online" as The Sims Online (2002) — built the hard
way, as a full MMO, instead of the email's receiver-in-the-game route.
The studio's idea pool ran years ahead of its release schedule, and it
never emptied — much of what was imagined then still hasn't shipped
and still could.

The missed boat, for the record: the loop this design described —
live broadcast into a synthetic world, synchronized real-time events,
characters and players responding together inside a time window,
advertising as native game content — is now the concert-in-Fortnite,
creator-stream, live-ops economy that prints money for everyone else.
EA itself was sold for $55 billion — the largest leveraged buyout in
history, announced September 2025, closed August 4, 2026 — to a
consortium of Saudi Arabia's Public Investment Fund (93.4%), Silver
Lake, and Jared Kushner's Affinity Partners. The company that found
live radio in a dollhouse too adventurous for its flagship is now
owned by a sovereign wealth fund and a presidential son-in-law. Draw
your own envelope over that parameter track.

## MOOLLM: Moody now

MOOLLM's object system already has every socket this design needs:

- **Media artifacts carry `moody:` blocks** in their YAML — the
  parameter track is just more semantic data on the object, YAML Jazz
  style, authorable in prose ("builds from wistful to triumphant over
  three minutes") and compilable to envelopes by the adventure
  compiler.
- **Rooms sum the tracks of playing media** into ambient context.
  A directory is a room; the room's current heat vector is derived at
  read time from what's playing — never cached, so nothing goes stale
  when the music stops (robust-first: presence of a playing track IS
  the flag).
- **Advertisement scoring reads ambient heat** as implicit context —
  every CARD's advertisements are re-weighted by the room's current
  tags, and dispatch temperature itself can be a track.
- **Time-windowed broadcast ads are buffs** with `expires_at:` —
  the live call-in ad drops into the room's auction, shouts, and
  stops answering at the deadline.
- **Personal overlays live in the character's own directory**, not on
  the media — private by filesystem construction. An overlay file
  keyed by media path plus timestamp, append-only like a session log;
  the shared media artifact never mutates. At playback the character's
  overlays for the playing media are summed onto the public track —
  derived, never cached, so your song is your song on every machine
  that mounts your soul.
- **The LLM is the meaning knob.** The original design needed humans
  to author every parameter track. An LLM can *listen to the lyrics* —
  or read the scene, or the liner notes — and infer the track. The
  meaning channel finally has a universal decoder, which is the
  technology the design was waiting for.

## The pun shelf

A target-rich environment, as promised: **multimoodia** · mood
swing (it's an envelope) · mood ring (wearable room) · reading the
room (it's a read) · setting the mood (it's a write) · heat map
(the floor plan of feelings) · emotional weather (fronts move
through) · elevator music that actually elevates · theme song (a
theme is a parameter set) · in the mood (high tag heat) · killing
the mood (zeroing the track) · Muzak to my ears · the DJ's
crossfader as an exploration/exploitation knob · ambient computing,
finally ambient about something · they're playing our song (a
temporal relationship matrix cache hit) · Netflix and chill (a moody
jam recording session) · the madeleine (playback you didn't
schedule) · track record (literally) · bow the memory (tape-bow
violin, scrubbing as performance) · sforzando (the spike has a name
in Italian) · a save file of feeling · safari tracks (the ride is the
ink) · the madeleine, geofenced · roundabout (municipal circular
gesture guide) · the blue note (the bent tone that makes the blues
the blues, and the color of the puddle) · the breakup remaster (a
grief pass, append-only like a heart) · hot dogging it (dead
reckoning with feeling).

## See also

- [The 1999 SimRadio email, in full](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/simradio-moody-1999-maxis-email.md)
  — the primary source, harvested with commentary in WWSFF
- [Radio On Internet: SimRadio in context](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/simradio-radio-on-internet.md)
  — the Broadcast.com date collision, the Russ Hanneman ROI scene, the
  EAML counterfactual, and the open-commons plan to finally build it
- [Show seed: Moody — MIDI for Mood](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/moody-midi-for-mood/moody-midi-for-mood.yml)
  — the Tiny Life trio (dev, composer, emotion sting artist), Jerry
  Martin, David Levitt, and Will, on composers annotating their own
  meaning
- [GAME-PIECES.md](GAME-PIECES.md) — advertisement auctions, buffs
  with expiration dates, the dispatch spectrum and temperature as
  context
- The Sims' advertisement scoring and the Room motive — the shipped
  ancestors
- Korz (Ungar/Ossher/Kimelman) — implicit context dimensions, the
  formal home of "the room sets it, everything inherits it"
