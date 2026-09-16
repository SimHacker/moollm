# MOODY temperature — the room writes the dispatch context

*A [Korz example](README.md). MOOLLM-integrated: the cast is a MOOLLM
design with a 1999 pedigree. Teaches: interpreter-altering dimensions,
ambient context, and environments as context writers.*

## The cast, introduced properly

**MOODY** ("Mood Is Multimedia" —
[the design](https://github.com/SimHacker/moollm/blob/main/designs/MOODY.md))
is a MOOLLM design with a shipping-era backstory: Don proposed it to
the Maxis team on February 18, 1999 as **SimRadio**, with a "moody
track" as its emotional payload. The idea: media carries a
**parameter track** alongside its waveform — time-varying heat
levels for semantic tags:

```yaml
moody:
  tags:
    romantic:     [{t: 0, heat: 0.2}, {t: 45, heat: 0.9}, {t: 180, heat: 0.4}]
    energetic:    [{t: 0, heat: 0.1}, {t: 30, heat: 0.6}]
    intellectual: [{t: 0, heat: 0.0}]
```

When the artifact plays, it broadcasts the track into the room; when
it stops, the broadcast stops. A song doesn't just sound romantic —
it *emits* `romantic: 0.9` at second 45, and everything in the room
can read it. It didn't ship in The Sims; MOOLLM finally has the
object system it wanted.

## The mechanics: temperature as a dimension

Korz's paper lists, as future work, dimensions that alter the
interpreter itself. Korz′ ([design](../README.md)) standardizes one:
**`temperature:`** — how adventurous sampling and improvisation may
be at each dispatch. The two properties that make it Korz-shaped:

1. **It's ambient.** Temperature flows implicitly down the call
   chain like any other binding — the paper's `assertions: true`
   trick applied to determinism itself. A scene sets its dither
   once; every dispatch below inherits it. The party planner runs
   hot while the accountant in the same call chain runs cold,
   and no intermediate code mentions either.
2. **Zero recovers determinism.** `{temperature: 0}` is classical
   Korz — the strict tier is the corner case, not a different
   language. One dimension binding is the entire difference between
   the improvising system and the deterministic one.

## The MOODY move: the environment writes the binding

Who sets the temperature? In most systems, a config file. In the
MOODY reading, **the environment does** — ambient heat comes from
the room, and the room inherits it, time-varying, from the moody
media playing in it. The stereo broadcasts its parameter track; the
room integrates the broadcasts into its ambient context; every
dispatch in the room reads that context implicitly.

That completes a loop the other examples leave open: the
[Sims advertisement economy](sims-advertisements.md) has objects
bidding *for* attention; MOODY has objects writing *the conditions
of judgment themselves*. A romantic ballad doesn't advertise "dance
with me" — it raises `romantic:` heat so that everyone else's
dance-related advertisements score higher and every improvisation
leans warmer. The medium is the context. A room whose implicit
dispatch dimensions are written by the stereo is about as Korz as
game design gets.

And it generalizes past mood: any environmental writer — season,
weather, occupancy, alarm state — is a device that pours bindings
into an ambient context that dispatch reads for free. The room is
not a container; it's a **context author**. (In MOOLLM this is
literal: a room directory's YAML *is* the ambient context, and
containment-as-a-guard — [addressing.md](../addressing.md) — is what
makes "in the room" and "bound in the context" the same fact.)

## The knob worn honestly

One more Korz′ discipline point rides on this example: temperature
is *visible* in the context, not buried in an API call. A transcript
that shows `{temperature: 0.9, romantic: 0.8}` explains its own
improvisations the way the troll's head sizes explain his blend
([troll-blend.md](troll-blend.md)) — dispatcher state worn where the
reader can see it. When a scene goes strange, the first debugging
question is the same one a Sim's player asks: *what's playing on the
stereo?*

## The moody keyboard — the meaning knob at your fingertips

The stereo had two knobs: **volume** (surface amplitude) and
**meaning** (semantic amplitude). Korz′ adds a third interface for
LLM text transformation: the **moody keyboard**. Each key raises heat
on a tag or dispatch dimension — `poetic`, `flowery`, `e-prime`,
`color`, `temperature`, `rcvr` — and held keys **sum into ambient
context** the way MOODY rooms sum stereo tracks. You are not typing
characters; you are **setting the mood of the rewrite**. The LLM is
the meaning knob ([MOODY § MOOLLM](https://github.com/SimHacker/moollm/blob/main/designs/MOODY.md));
the keyboard is how you play it.

Korz is E-Prime for objects ([README](../../README.md)): red lives in
the dispatch, not in the rose. Spock holds only the `color` key:

> Along color, this rose dispatches red for me now.

Hold **poetic** and **flowery** too — same Korz/E′ discipline, higher
meaning gain:

```yaml
context:
  color: active
  e-prime: true
  poetic: 0.8
  flowery: 0.9
```

> In this light, between us, the rose *offers* me crimson — not a
> verdict sealed in the petal, but a blush the moment presses out
> along color; I am the one who gathers it there.

The hue stays in the **interaction** (Korz coordinates, not ontology).
The keyboard only turns up how loudly the room says so.

## Virtual heat vs API heat — the 2D map

ChatGPT's vanished UI "heat" was the **API sampler knob** — logits
dither at decode time, outside the weights. Korz′ **`{temperature:}`**
is the **virtual** binding: declared dispatch policy, ambient,
inheritance, transcript-visible. In plain chat they are **totally
decoupled** unless an orchestrator couples them on purpose. "Simon
says heat=0.0" writes the map; only infrastructure moves the
territory.

```text
virtual heat  (context: {temperature:}, moody keyboard, "simon says")
        ▲
   1.0  │  performative hot     │  honest hot
        │  (claims Zork,         │  (Zork says Zork,
        │   Kelvin runs)         │   Zork runs)
   0.0  │  honest cold           │  hidden dither
        │  (Kelvin / strict)     │  (claims Kelvin, dice roll)
        └────────────────────────┴──────────────────────► API heat
                              0.0              1.0
                         (sharp logits)   (dithered logits)
```

| Quadrant | Virtual | API | Meaning |
|---|---|---|---|
| Honest cold | ≈ 0 | ≈ 0 | Strict Korz, crystallize-friendly; often **no LLM** (Kelvin) |
| Hidden dither | ≈ 0 | high | Transcript lies — worst case for "compile this down" |
| Performative hot | high | ≈ 0 | Moody keyboard cranked, low token entropy — florid *style*, tight *dice* |
| Honest hot | high | high | Zork — exploration, deopt candidates, party planner |

The **diagonal** (virtual ≈ API) is coupled dispatch — what Korz′
wants when the engine exists. Off-diagonal is map/territory drift;
treat mismatch as a smell unless documented (e.g. high virtual, low
API for "crystallization preview").

**MOODY tag heat** (`romantic: 0.9`) is a **third axis** — meaning
gain, not either temperature above. Slow dance: high romantic heat,
**low** dispatch temperature; party track: high energetic heat, **high**
temperature.

The temperature adapter's job: read virtual → set API → log both.

```yaml
# coupled (honest hot)
context: {temperature: 0.9}
api:     {temperature: 0.9}

# honest cold — often no API at all
context: {temperature: 0.0}
route:   kelvin

# intentional decouple (document why)
context: {temperature: 0.8}
api:     {temperature: 0.2}
reason:  crystallization-preview
```

Prior art: consumer chat UIs that removed the heat slider left only
virtual heat — performers simulating temperature without moving the
sampler. Korz′ makes the gap visible so it can be closed.
