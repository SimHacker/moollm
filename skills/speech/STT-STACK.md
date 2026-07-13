# Speech skill — STT/TTS stack audit & integration plan

What exists today, what Apple exposes beyond SAPI, and how to wire **tight** integration for
Urban eBike Safari / VoyStick / adventure voice.

## Current inventory (honest)

| Layer | Status | Where |
|-------|--------|-------|
| **macOS TTS** | Shipped | `say` CLI · [voices/apple.yml](voices/apple.yml) |
| **Browser TTS** | Shipped | [adventure/dist/speech.js](../adventure/dist/speech.js) |
| **Browser STT** | Shipped (not in `speech/`) | [adventure/dist/recognition.js](../adventure/dist/recognition.js) · [adventure-recognition.js](../adventure/dist/adventure-recognition.js) |
| **macOS STT (new)** | Not wired | `SpeechAnalyzer` / `SpeechTranscriber` (iOS 26 / macOS 26+) — Swift only |
| **macOS STT (legacy)** | Not wired | `SFSpeechRecognizer` — Swift/ObjC |
| **Python STT** | Script stub | [scripts/stt_whisper.py](scripts/stt_whisper.py) · [scripts/stt_dispatch.py](scripts/stt_dispatch.py) |
| **Windows SAPI** | Documented only | Slats stack: ViaVoice → SAPI → Cepstral ([WWSFF stupid-fun-club.yml](https://github.com/SimHacker/WillWrightShowForFood/blob/main/characters/don-hopkins/career/stupid-fun-club.yml)) |
| **VoyStick pitch/vowel** | Not in any STT API | Phoneloper lineage · needs **parallel audio analysis** — [voystick.yml](voystick.yml) |

**CARD.yml TODO "integrate STT" is stale** — browser STT shipped in adventure `dist/`; gap is **native Apple**, **Python bridge**, and **VoyStick gesture channel**.

## What each API gives you

### Web Speech API (`recognition.js`)

- Transcript, confidence, interim vs final
- Continuous mode, command fuzzy-match (`listenForCommands`)
- Events: `speechstart`, `speechend`, `audiostart`, …
- **No** word timestamps, **no** pitch, **no** vowel/formants
- Chrome: cloud to Google; Safari: may be on-device

### Microsoft SAPI (Slats / pywin32)

```python
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello from Slats")
# Recognition: SAPI.SpSharedRecognizer + SpInProcRecoContext — separate setup
```

- TTS: voices, rate, pitch on **output** (not input analysis)
- STT: dictation grammar, confidence — **no** modern streaming timestamps like Apple 2025
- Don's Slats: IBM ViaVoice → **Microsoft SAPI** → Cepstral ([genealogy](https://github.com/SimHacker/WillWrightShowForFood/blob/main/process/CRAZY-IDEA-JAM.md))

### Apple SpeechAnalyzer (2025+ — replaces SFSpeechRecognizer for new work)

WWDC: [Bring advanced speech-to-text with SpeechAnalyzer](https://developer.apple.com/videos/play/wwdc2025/277/)

| Module | Use |
|--------|-----|
| `SpeechTranscriber` | Long-form, streaming, on-device |
| `DictationTranscriber` | Short utterances (SFSpeechRecognizer-like) |
| `SpeechDetector` | Voice activity — pair with transcriber |

**Exposed metadata (STT):**

- `audioTimeRange` per token/run — **word-level timestamps** (`attributeOptions: [.audioTimeRange]`)
- `isFinal` on streaming results (partial vs committed)
- Confidence on results
- Locale asset download via `AssetInventory`
- AsyncSequence `transcriber.results` — must drain **concurrently** with `analyzeSequence`
- `finalizeAndFinishThroughEndOfInput()` — required or session hangs ([Inscribe benchmark](https://get-inscribe.com/blog/apple-speech-api-benchmark.html))

**NOT exposed by Apple STT:**

- **Pitch contour** for VoyStick (need `AVAudioEngine` + YIN/aubio/Accelerate)
- **Vowel/formant position** (need F1/F2 tracker — [vowel-space.yml](platforms/vowel-space.yml), imitone lineage; **not** vocoder/LPC telephony tricks for live control)
- Custom vocabulary (still on legacy `SFSpeechRecognizer` per Apple docs)

Machine-readable: [platforms/apple-speech-analyzer.yml](platforms/apple-speech-analyzer.yml)

### VoyStick dual channel (safari target)

```
┌─────────────────────────────────────────────────────────┐
│  Mic (Ray-Ban / phone)                                   │
├──────────────────────┬──────────────────────────────────┤
│ SpeechTranscriber    │  voystick_stream (parallel)       │
│ → words, timestamps  │  → pitch Hz, vowel proxy, energy  │
│ → adventure commands │  → pie wedge X/Y                  │
└──────────────────────┴──────────────────────────────────┘
```

Apple handles **words**; MOOLLM handles **gesture** — same mic, two analyzers.

## Tight integration architecture

### Tier 0 — today (script, no compile)

| Tool | Command |
|------|---------|
| TTS | `skills/speech/scripts/say.sh "text"` |
| STT file | `python3 skills/speech/scripts/stt_whisper.py audio.wav` |
| STT route | `python3 skills/speech/scripts/stt_dispatch.py --help` |
| VoyStick probe | `python3 skills/speech/scripts/voystick_probe.py` (needs `aubio`, `sounddevice`) |

### Tier 1 — browser adventure (already shipped)

Load `recognition.js` + `adventure-recognition.js` — mic button, command → engine.

```javascript
const recognition = new SpeechRecognitionSystem({ continuous: true });
recognition.on('result', ({ transcript }) => engine.command(transcript));
recognition.startListening();
```

### Tier 2 — Swift CLI `moollm-speech` (compile once)

Thin macOS 26+ binary:

- stdin/stdout JSON lines: `{ "type": "partial"|"final", "text", "start", "end", "confidence" }`
- Python/Node adventure runtime spawns process, pipes mic via AVAudioEngine in Swift
- See [native/README.md](native/README.md) for module layout

### Tier 3 — unified `SpeechBus` (TypeScript)

Single facade in `skills/speech/dist/speech-bus.js` (planned):

- `speak(text, voice)` → speech.js or `say.sh` via shell
- `listen()` → recognition.js OR native bridge OR whisper fallback
- `voystick.onWedge((x,y) => …)` → optional pitch stream

Adventure compiler flag: `speech: true, recognition: true, voystick: false`.

## Slats / SAPI / Phoneloper lineage

| Era | Stack | VoyStick relevance |
|-----|-------|-------------------|
| Slats robot | SAPI TTS + recognition | COM automation — same era as pie menus |
| Phoneloper 2003 | Python + Flite, **pitch envelope** edit | Pitch tracking for phonoscope — manual + semi-auto |
| VoyStick lecture | pitch=Y, vowel=X | Homomorphic to pie menus |
| Safari 2026 | SpeechAnalyzer + aubio pitch | Dual channel on bike |

## Field test (Urban eBike Safari)

Primary: **SpeechAnalyzer** on iPhone handlebar mount (wind WER benchmark).
Secondary: **voystick_probe** on Mac for wedge mapping calibration before field.
Fallback: **WhisperKit** for locales SpeechTranscriber lacks.

Refs: [urban-ebike-safari voice_stack](https://github.com/SimHacker/WillWrightShowForFood/blob/main/repo-shows/ideas/urban-ebike-safari.yml) · [ride-game](https://github.com/SimHacker/moollm/blob/main/skills/simulation/examples/urban-safari-ride-game.yml)

## Implementation order

1. Fix skill docs (this file) + scripts — **done in this pass**
2. Wire `speech-bus` re-export in adventure `EXPORT.md` defaults `recognition: true`
3. Swift `moollm-speech` CLI for macOS/iOS 26+
4. `voystick_stream.py` → pie wedge mapper shared with adventure
5. Windows SAPI Python module for Slats parity (optional)
