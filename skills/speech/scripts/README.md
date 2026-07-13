# Speech scripts — tight integration entry points

| Script | Needs compile? | Role |
|--------|----------------|------|
| [say.sh](say.sh) | No | macOS TTS — wraps `say` |
| [stt_dispatch.py](stt_dispatch.py) | No | List/route STT backends; JSON stdout |
| [stt_whisper.py](stt_whisper.py) | No | File → text via `whisper` CLI if installed |
| [voystick_probe.py](voystick_probe.py) | No (pip deps) | Live pitch → JSON lines for VoyStick Y |

**Browser (TypeScript/JS — already shipped):**

- `skills/adventure/dist/speech.js` — TTS
- `skills/adventure/dist/recognition.js` — STT
- `skills/adventure/dist/adventure-recognition.js` — mic UI + engine hookup

**Native (must compile):**

- [../native/README.md](../native/README.md) — `moollm-speech` Swift CLI for SpeechAnalyzer

```bash
chmod +x say.sh
./say.sh "Hello from MOOLLM"
python3 stt_dispatch.py --list
python3 stt_whisper.py recording.wav --json
python3 voystick_probe.py --seconds 5
```

See [../STT-STACK.md](../STT-STACK.md) for full audit.
