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

## Precedents and kin

- **Muzak's stimulus progression** — the 1940s shipped time-varying
  mood parameter tracks: fifteen-minute blocks ascending in intensity
  to fight worker fatigue. Muzak just never published the schema.
  Moody is stimulus progression with the schema in the open, per tag.
- **Brian Eno's ambient music** — "as ignorable as it is interesting"
  (*Music for Airports*). Moody media is ambient music with a
  machine-readable meaning track; Eno later built generative music for
  *Spore* with Will Wright, so the lineage loops back to Maxis anyway.
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
finally ambient about something.

## See also

- [The 1999 SimRadio email, in full](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/simradio-moody-1999-maxis-email.md)
  — the primary source, harvested with commentary in WWSFF
- [GAME-PIECES.md](GAME-PIECES.md) — advertisement auctions, buffs
  with expiration dates, the dispatch spectrum and temperature as
  context
- The Sims' advertisement scoring and the Room motive — the shipped
  ancestors
- Korz (Ungar/Ossher/Kimelman) — implicit context dimensions, the
  formal home of "the room sets it, everything inherits it"
