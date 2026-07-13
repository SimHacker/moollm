#!/usr/bin/env python3
"""MOOLLM speech — route STT to best available backend; JSON stdout for tight integration."""
from __future__ import annotations

import argparse
import json
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def backends() -> dict:
    return {
        "browser": {
            "available": True,
            "note": "Load skills/adventure/dist/recognition.js — live mic, no file path",
            "path": "skills/adventure/dist/recognition.js",
        },
        "whisper_file": {
            "available": shutil.which("whisper") is not None,
            "note": "skills/speech/scripts/stt_whisper.py <audio>",
        },
        "apple_speech_analyzer": {
            "available": False,
            "note": "macOS/iOS 26+ — build skills/speech/native moollm-speech Swift CLI",
            "spec": "skills/speech/platforms/apple-speech-analyzer.yml",
        },
        "macos_dictation": {
            "available": platform.system() == "Darwin",
            "note": "Fn Fn — not scriptable; use SpeechAnalyzer CLI when built",
        },
        "windows_sapi": {
            "available": platform.system() == "Windows",
            "note": "pywin32 SAPI.SpSharedRecognizer — Slats lineage; module not shipped yet",
        },
    }


def main() -> int:
    p = argparse.ArgumentParser(description="MOOLLM STT backend router")
    p.add_argument("--list", action="store_true", help="List backends as JSON")
    p.add_argument("--audio", help="Audio file for whisper backend")
    p.add_argument("--model", default="base.en")
    args = p.parse_args()

    b = backends()
    if args.list:
        print(json.dumps(b, indent=2))
        return 0

    if args.audio:
        script = Path(__file__).parent / "stt_whisper.py"
        if not b["whisper_file"]["available"]:
            print(json.dumps({"error": "whisper_not_installed", "backends": b}), file=sys.stderr)
            return 2
        proc = subprocess.run(
            [sys.executable, str(script), args.audio, "--model", args.model, "--json"],
            capture_output=True,
            text=True,
        )
        sys.stdout.write(proc.stdout)
        if proc.returncode != 0:
            sys.stderr.write(proc.stderr)
        return proc.returncode

    print(json.dumps({"hint": "Use --list or --audio path; live mic uses recognition.js"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
