# The Sims Zodiac System

> *"not \*because\* I'm an aries, well, maybe because."*

## The Algorithm Nobody Knew About

Every Sims player has clicked zodiac signs in Create-a-Sim. Few realized the game was doing computational geometry in 5-dimensional space behind the scenes.

There's no birthday. There's no astrology table lookup. The Sims computes your zodiac sign by finding which archetype your personality is closest to using **Euclidean distance** in a 5D space defined by Neat, Outgoing, Active, Playful, and Nice.

Your five trait sliders define a point in personality space. Each zodiac sign is a fixed archetype vector. The game measures the distance from your point to all twelve archetypes and picks the nearest one. That's your sign.

## The Algorithm

Find the zodiac sign whose archetype is closest to your personality. Five traits define a point in space. Twelve archetypes are fixed points. Measure the distance to each one. Closest wins.

```javascript
// The twelve archetype vectors — one per zodiac sign
// Each is a personality fingerprint: [neat, outgoing, active, playful, nice]
const archetypes = {
  aries:       [5, 8, 6, 3, 3],
  taurus:      [5, 5, 3, 8, 4],
  gemini:      [4, 7, 8, 3, 3],
  cancer:      [6, 3, 6, 4, 6],
  leo:         [4, 10, 4, 4, 3],
  virgo:       [9, 2, 6, 3, 5],
  libra:       [2, 8, 2, 6, 7],
  scorpio:     [6, 5, 8, 3, 3],
  sagittarius: [2, 3, 9, 7, 4],
  capricorn:   [7, 4, 1, 8, 5],
  aquarius:    [4, 4, 4, 7, 6],
  pisces:      [5, 3, 7, 3, 7],
};

// Squared distance between two personality vectors
function personalityDistance(a, b) {
  let sum = 0;
  for (let i = 0; i < a.length; i++) {
    const diff = a[i] - b[i];
    sum += diff * diff;
  }
  return sum;
}

// Find the zodiac sign whose archetype is nearest to your traits
function computeZodiac(traits) {
  let bestSign = null;
  let bestDistance = Infinity;

  for (const [sign, archetype] of Object.entries(archetypes)) {
    const distance = personalityDistance(traits, archetype);
    if (distance < bestDistance) {
      bestDistance = distance;
      bestSign = sign;
    }
  }

  return bestSign;
}

// Example: a shy, neat, active introvert
computeZodiac([9, 2, 6, 3, 5]); // → "virgo" (distance: 0 — exact match!)

// Example: all zeros — no sign is meaningfully closest
// Every archetype is roughly equidistant (~125). The game shows nothing.
```

Sum of squared differences. Nearest neighbor. No magic — just geometry.

## The Archetype Table

Each sign is a 5-number vector. Every sign totals exactly 25 points — the same 25 points the player distributes during character creation.

| Sign | Neat | Outgoing | Active | Playful | Nice | Personality |
|------|------|----------|--------|---------|------|-------------|
| Aries | 5 | **8** | 6 | 3 | 3 | Social and energetic but not very nice |
| Taurus | 5 | 5 | 3 | **8** | 4 | Balanced but very playful |
| Gemini | 4 | 7 | **8** | 3 | 3 | Active social butterfly |
| Cancer | 6 | 3 | 6 | 4 | **6** | Balanced across the board |
| Leo | 4 | **10** | 4 | 4 | 3 | Maximum outgoing, everything else average |
| Virgo | **9** | 2 | 6 | 3 | 5 | Extremely neat, shy, active |
| Libra | 2 | 8 | 2 | 6 | **7** | Social and nice but lazy and messy |
| Scorpio | 6 | 5 | **8** | 3 | 3 | Neat, active, withdrawn |
| Sagittarius | 2 | 3 | **9** | 7 | 4 | Maximum activity, very playful |
| Capricorn | 7 | 4 | **1** | 8 | 5 | Neat and playful but almost inert |
| Aquarius | 4 | 4 | 4 | **7** | 6 | The most balanced sign |
| Pisces | 5 | 3 | 7 | 3 | **7** | Kind, active, shy |

**Bold** = the sign's dominant trait.

## Why It Shows Nothing At Zero

When you haven't allocated any points yet, the UI shows no zodiac icon. One sign actually IS closest to (0,0,0,0,0) — but the game deliberately hides it.

The reason is procedural rhetoric: if zero personality points displayed a sign, that sign becomes "the sign with no personality." You've just insulted 1/12 of your user base by implying their zodiac sign means "zilch." Nobody wants to see their sign pop up as the default for a blank, pointless Sim.

So the game suppresses the display until points are committed. You have to make choices before you get an identity. The sign reflects who you chose to be, not which archetype happens to sit nearest to the origin.

## The Compatibility System

When two Sims meet, their zodiac signs affect the starting relationship:

| Your Sign | Attracted To | Repelled By |
|-----------|-------------|-------------|
| Aries | Gemini, Taurus | Cancer, Libra |
| Taurus | Aries, Libra | Virgo, Cancer |
| Gemini | Pisces, Virgo | Capricorn, Aries |
| Cancer | Taurus, Scorpio | Gemini, Aries |
| Leo | Sagittarius, Cancer | Capricorn, Gemini |
| Virgo | Aquarius, Sagittarius | Leo, Taurus |
| Libra | Virgo, Cancer | Pisces, Scorpio |
| Scorpio | Pisces, Leo | Libra, Aquarius |
| Sagittarius | Pisces, Capricorn | Libra, Scorpio |
| Capricorn | Aquarius, Taurus | Leo, Gemini |
| Aquarius | Capricorn, Sagittarius | Scorpio, Virgo |
| Pisces | Scorpio, Gemini | Leo, Aries |

These compatibility pairings are hardcoded, not computed from trait similarity. Some are counterintuitive (Leo attracted to Cancer? They're quite different in trait space). The design team chose them deliberately.

## Clicking a Sign — The Reverse Operation

When you click a zodiac icon in Create-a-Sim, the game does the reverse: it SETS your personality to that sign's archetype vector. Then you can redistribute from there.

```javascript
// Click a zodiac sign → set personality to its archetype
function setZodiacSign(sign) {
  const archetype = archetypes[sign];
  return {
    neat:     archetype[0],
    outgoing: archetype[1],
    active:   archetype[2],
    playful:  archetype[3],
    nice:     archetype[4],
  };
}

setZodiacSign("virgo");
// → { neat: 9, outgoing: 2, active: 6, playful: 3, nice: 5 }
// Now drag the sliders to customize from there.
```

## The Personality Array

Every Sim's personality is a flat array of numbers at runtime. Six traits, seven skills, eight needs, plus career, age, gender, and zodiac — all in one contiguous block.

```javascript
// The six personality traits (display scale 0-10, internal 0-1000)
const traits = {
  nice:      5,  // grouchy ↔ nice
  active:    5,  // lazy ↔ active
  generous:  5,  // selfish ↔ generous (hidden in Sims 1 UI, used by Sims Online)
  playful:   5,  // serious ↔ playful
  outgoing:  5,  // shy ↔ outgoing
  neat:      5,  // sloppy ↔ neat
};

// Convert between display (0-10) and internal (0-1000)
const toInternal = (display) => Math.round(display * 100);
const toDisplay = (internal) => internal / 100;
```

The generous trait exists in the data but the original Sims 1 never shows it to the player. It sits there quietly between Nice and Playful, waiting for The Sims Online to use it.

## For MOOLLM

In CHARACTER.yml files, the `sims:` block stores these values at the 0-10 display scale. The zodiac sign can be computed from the traits using the same Euclidean distance algorithm. The `generous` trait is included for completeness.

When a character beams down to The Sims via SimObliterator, these values multiply by 100. When they beam up, they divide by 100. Lossless round-trip.

The zodiac sign is always COMPUTED, never stored independently. If you change a character's traits, their sign may change. This is by design — the sign is a reading of personality, not a constraint on it.

See `ZODIAC.yml` for the complete data tables in machine-readable format.
See `SIMS-STATS.yml` and `SIMS-STATS.md` for the full character data reference.
