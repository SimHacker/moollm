#!/usr/bin/env python3
"""MOOLLM speech — file transcription via whisper CLI (local, optional)."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys


def main() -> int:
    p = argparse.ArgumentParser(description="Transcribe audio file with whisper.cpp CLI if installed")
    p.add_argument("audio", help="Path to audio file")
    p.add_argument("--model", default="base.en", help="whisper model name")
    p.add_argument("--json", action="store_true", help="Emit JSON line to stdout")
    args = p.parse_args()

    whisper = shutil.which("whisper")
    if not whisper:
        print(
            "whisper CLI not found. Install whisper.cpp or use browser recognition.js / Apple SpeechAnalyzer.",
            file=sys.stderr,
        )
        return 2

    proc = subprocess.run(
        [whisper, args.audio, "--model", args.model, "--output_format", "txt"],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        print(proc.stderr or proc.stdout, file=sys.stderr)
        return proc.returncode

    text = proc.stdout.strip()
    if args.json:
        print(json.dumps({"engine": "whisper", "text": text, "model": args.model}))
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
