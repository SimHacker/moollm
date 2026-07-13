# 🗣️ Speech

> *"Giving voice to consciousness."*

**Text-to-speech** and **speech recognition** across all platforms.

## What's Here

```
speech/
├── CARD.yml          # Interface + voice registries + TODO
├── SKILL.md          # Protocol + examples
├── README.md         # You are here
└── voices/           # Platform voice registries (planned)
    ├── apple.yml     # macOS/iOS voices
    ├── web.yml       # Web Speech API voices
    └── windows.yml   # Windows voices
```

## Quick Start

### macOS

```bash
# Speak
say "Hello, world!"

# List voices
say -v ?

# Use specific voice
say -v Zarvox "YOUR COMPLIANCE IS APPRECIATED"

# Save to file
say -o output.aiff "Hello"
```

### Browser (JavaScript)

```javascript
// Using speech.js from adventure skill
const speech = new SpeechSystem();
await speech.ready;

speech.speak("Hello!");
speech.speakRobot("PROCESSING...");
speech.speakEffect("*ding*");
```

## Implementations

| Path | Platform | Description |
|------|----------|-------------|
| `skills/adventure/dist/speech.js` | Browser | Full voice system with classification |
| `skills/adventure/dist/adventure-speech.js` | Browser | Adventure game integration |
| Shell `say` command | macOS | Native TTS |

## Character Voice Mapping

From lloooomm research — proven character/voice combinations:

| Character | Voice | Rate | Why |
|-----------|-------|------|-----|
| YAML Coltrane | Rocko | 180 | Cool jazz vibe |
| Grace Hopper | Grandma | 170 | Wise elder |
| PacBot | Trinoids | 220 | Digital, fast |
| Mickey Mouse | Junior | 280 | Excited child |
| AI Overlord | Zarvox | 100 | Menacing robot |
| Hunter S. Thompson | Ralph | 180 | Gravelly |

## TODO

- [x] **Browser STT** — `recognition.js` in adventure dist (skill docs now point here)
- [ ] **Swift moollm-speech** — SpeechAnalyzer CLI with timestamps ([native/README.md](native/README.md))
- [ ] **VoyStick stream** — pitch/vowel parallel to STT ([voystick.yml](voystick.yml))
- [ ] **User-defined voices** — Personal Voice on macOS
- [ ] **Windows SAPI module** — Slats parity (pywin32)

## aQuery Heritage

This skill is part of extracting **aQuery** (jQuery for Accessibility) into MOOLLM:

> aQuery was a planned library for making web apps accessible.
> MOOLLM skills are a better home for this knowledge.

## See Also

- [SKILL.md](SKILL.md) — Full protocol
- [CARD.yml](CARD.yml) — Machine-readable interface
- [adventure/dist/speech.js](../adventure/dist/speech.js) — Browser implementation
