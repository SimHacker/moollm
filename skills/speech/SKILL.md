---
id: speech
name: Speech
type: [skill, accessibility, aquery]
emoji: 🗣️
tier: 0
---

# 🗣️ Speech — Text-to-Speech & Speech Recognition

> *"Giving voice to consciousness."*

Part of the **aQuery → MOOLLM Skills** extraction project (jQuery for Accessibility).

---

## Quick Reference

| Command | Effect |
|---------|--------|
| `say "text"` | Speak on macOS |
| `say -v Zarvox "text"` | Use specific voice |
| `say -v ?` | List all voices |
| `say -r 150 "text"` | Set rate (words/min) |
| `say -o file.aiff "text"` | Save to audio |

---

## Platforms

| Platform | Synthesis | Recognition | Notes |
|----------|-----------|-------------|-------|
| macOS | `say` command | Dictation | Best novelty voices |
| Web | `speechSynthesis` | `SpeechRecognition` | See speech.js |
| Windows | SAPI | Windows Speech | Similar to web |
| Linux | espeak, festival | Whisper | Open source |
| Cloud | Polly, Azure, Google | Transcribe, Whisper | Highest quality |

---

## macOS `say` Command

### Basic Usage

```bash
# Simple speech
say "Hello, world!"

# Choose a voice
say -v Samantha "Hello!"
say -v Zarvox "I AM ZARVOX!"
say -v Whisper "Secrets..."

# Adjust rate (words per minute)
say -r 100 "Very slow"
say -r 300 "Very fast"

# Save to file
say -o greeting.aiff "Hello!"
say -o greeting.m4a "Hello!"  # Compressed

# Read from file
say -f document.txt
```

### List All Voices

```bash
# All available voices
say -v ?

# Filter by language
say -v ? | grep "en_"

# Count voices
say -v ? | wc -l
```

### Voice Categories

| Category | Examples | Use For |
|----------|----------|---------|
| **Standard** | Samantha, Alex, Daniel | General narration |
| **Premium** | Enhanced voices (download) | High quality |
| **Elderly** | Grandma, Grandpa | Wise characters |
| **Child** | Junior | Young characters |
| **Novelty** | Zarvox, Trinoids, Whisper | Robots, effects |
| **Musical** | Bells, Cellos, Organ | Sound effects |
| **Dramatic** | Bad News, Good News | Announcements |

### Character Voice Assignments (from lloooomm)

```bash
# YAML Coltrane — Cool jazz vibe
say -v "Rocko" -r 180 "Every indent is a universe!"

# Grace Hopper — Wise elder
say -v "Grandma" -r 170 "A ship in port is safe, but that's not what ships are for!"

# PacBot — Digital entity
say -v "Trinoids" -r 220 "WAKA WAKA WAKA!"

# Mickey Mouse — Excited child
say -v "Junior" -r 280 "OH BOY!"

# Overlord AI — Menacing
say -v "Zarvox" -r 100 "YOUR COMPLIANCE IS APPRECIATED."

# Hunter S. Thompson — Gravelly intensity
say -v "Ralph" -r 180 "We were somewhere around Barstow..."
```

### Chorus Effects

```bash
# Background voices for overlap
say -v "Bells" "LLOOOOMM!" &
sleep 0.2
say -v "Cellos" "LLOOOOMM!" &
sleep 0.2
say -v "Organ" "LLOOOOMM!" &
wait
```

---

## Web Speech API

### Browser Implementation

See `skills/adventure/dist/speech.js` for full implementation.

```javascript
// Initialize
const speech = new SpeechSystem();
await speech.ready;

// Speak
speech.speak("Hello, adventurer!");
speech.speakRobot("RESISTANCE IS FUTILE");
speech.speakEffect("*magical sounds*");

// With options
speech.speak("Welcome!", {
    voiceType: 'female',
    language: 'en-GB',
    pitch: 1.2,
    rate: 0.9
});

// Character persistence
const guardVoice = speech.selectVoice({ gender: 'male' });
speech.speakWithVoice("Halt!", guardVoice);
speech.speakWithVoice("You may pass.", guardVoice);
```

### Voice Classification

The `VoiceDatabase` class classifies voices by:

- **Type**: human, effect, robot
- **Gender**: male, female, neutral
- **Age**: child, adult, elderly
- **Language**: BCP 47 codes (en-US, fr-FR, etc.)
- **Local/Remote**: Local voices vs. network voices

### Single Source of Truth

All voice classification data lives in **`voices/browser-voices.yml`**:

```yaml
# Blacklisted voices (known problematic)
blacklist:
  - name: "Daniel (French (France))"
    reason: "Known problematic voice"

# Effect voices (non-human)
types:
  effect:
    regex: "^(Bells|Zarvox|Trinoids|Whisper|...)$"

# Gender detection tokens
gender:
  female:
    tokens: [alice, amélie, samantha, ...]
  male:
    tokens: [aaron, daniel, ralph, ...]

# Character archetype recommendations
character_archetypes:
  wise_elder: { voice: Grandma, rate: 170 }
  robot_menacing: { voice: Zarvox, rate: 100 }
```

The JS code is generated from this YAML. To update voice classification, edit the YAML and rebuild.

---

## Speech Recognition

### Browser (SpeechRecognitionSystem) — **shipped**

Implementation lives in adventure `dist/` (canonical); speech skill owns protocol + native bridges.

| File | Role |
|------|------|
| [recognition.js](../adventure/dist/recognition.js) | Web Speech API wrapper |
| [adventure-recognition.js](../adventure/dist/adventure-recognition.js) | Mic UI + engine hookup |

See [STT-STACK.md](./STT-STACK.md) for full audit (Apple SpeechAnalyzer, SAPI, VoyStick).

```javascript
// Initialize
const recognition = new SpeechRecognitionSystem({
    language: 'en-US',
    continuous: false
});

// Listen for single phrase
const text = await recognition.listen();
console.log('You said:', text);

// Continuous listening
recognition.onResult = (transcript) => {
    console.log('Final:', transcript);
};
recognition.onInterim = (transcript) => {
    console.log('Interim:', transcript);
};
recognition.startListening();

// Command recognition
const result = await recognition.listenForCommands([
    'go north', 'look', 'take sword'
]);
if (result.command) {
    engine.command(result.command);
}
```

### Browser Support

| Browser | Support | Privacy |
|---------|---------|---------|
| Chrome | ✅ | ⚠️ Sends to Google |
| Safari | ✅ | May be on-device |
| Firefox | ❌ | Disabled by default |
| Edge | ❌ | Not supported |

### Native Platform Shortcuts

| Platform | Shortcut | Feature |
|----------|----------|---------|
| macOS | Fn Fn | Dictation |
| Windows | Win + H | Voice Typing |
| iOS | 🎤 on keyboard | Dictation |
| Android | 🎤 on keyboard | Voice Typing |

### Whisper (OpenAI / whisper.cpp)

```bash
# Using whisper.cpp (local)
whisper --model base.en audio.wav

# MOOLLM wrapper (JSON stdout)
python3 skills/speech/scripts/stt_whisper.py audio.wav --json

# List all STT backends
python3 skills/speech/scripts/stt_dispatch.py --list
```

### Apple SpeechAnalyzer (macOS/iOS 26+)

On-device streaming STT with **word timestamps** — Swift only; planned `moollm-speech` CLI.

- `SpeechTranscriber` + `attributeOptions: [.audioTimeRange]`
- Partial/final via `isFinal`; confidence per result
- **No pitch/vowel** — VoyStick uses parallel [voystick_probe.py](./scripts/voystick_probe.py)

See [platforms/apple-speech-analyzer.yml](./platforms/apple-speech-analyzer.yml) · [native/README.md](./native/README.md)

### VoyStick (gesture channel, not STT)

Pitch=Y, vowel=X vocal joystick for pie wedges — [voystick.yml](./voystick.yml). Phoneloper lineage.

---

## Personal Voice (macOS)

⚠️ **WORK IN PROGRESS** — See TODO in CARD.yml

### Known Limitations

1. **Apple Silicon only** (M1, M2, M3)
2. **Doesn't appear in `say -v ?`** — Must know exact name
3. **No `-o` flag support** — Can't save to file directly
4. **Privacy restricted** — May need special permissions

### Creating Personal Voice

1. System Settings → Accessibility → Personal Voice
2. Record 15+ minutes of phrases
3. Processing takes 15-60 minutes
4. Find voice name in Spoken Content settings

### Workarounds

- [SavePersonalVoiceAudio](https://github.com/limneos/SavePersonalVoiceAudio) — Extract Personal Voice audio
- Shortcuts app — Can use Personal Voice with "Speak" action
- Record system audio while speaking

---

## Integration with Adventure

The adventure runtime uses the speech skill:

```javascript
// Create speaking adventure
const engine = createSpeakingAdventure('adventure', {
    speechEnabled: true,
    speakRooms: true,
    speakResponses: true
});

// Rooms speak their descriptions
// Characters have persistent voices
// AI entities use robot voices
// Effects use novelty voices
```

See: `skills/adventure/dist/adventure-speech.js`

---

## aQuery Heritage

This skill is part of extracting **aQuery** (jQuery for Accessibility) into MOOLLM skills:

| aQuery Component | MOOLLM Skill |
|------------------|--------------|
| Speech synthesis | `speech/` |
| Speech recognition | `speech/` |
| Screen reader support | *(planned)* |
| Keyboard navigation | *(planned)* |
| Focus management | *(planned)* |
| ARIA utilities | *(planned)* |

---

## See Also

- **[STT-STACK.md](./STT-STACK.md)** — TTS/STT audit, Apple vs SAPI, integration tiers
- **[voystick.yml](./voystick.yml)** — pitch/vowel gesture channel (parallel to STT)
- **[scripts/README.md](./scripts/README.md)** — `say.sh`, `stt_dispatch.py`, `voystick_probe.py`
- **[voices/browser-voices.yml](./voices/browser-voices.yml)** — Single source of truth for voice data
- [speech.js](../adventure/dist/speech.js) — Browser implementation
- [adventure-speech.js](../adventure/dist/adventure-speech.js) — Adventure integration
- [voice-system-integration-guide.md](../../temp/lloooomm/03-Resources/documentation/voice-system-integration-guide.md) — lloooomm research
- [character-voice-tutorial.sh](../../temp/lloooomm/03-Resources/code/character-voice-tutorial.sh) — Shell examples
