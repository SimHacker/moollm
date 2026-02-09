#!/usr/bin/env python3
"""mine: Extract semantic resources from images.

Give the vision LLM an image and a shopping list of resource types.
It looks at the picture and extracts quantities/intensities of each.

Resource types can be ANYTHING:
  - Objects: people, furniture, animals, vehicles
  - Materials: wood, metal, stone, fabric
  - Colors: dominant hues with hex codes
  - Moods: calm, tense, joyful, melancholic
  - Emotions: what feelings the image evokes
  - Textures: rough, smooth, grainy, polished
  - Smells: inferred from visual cues (bread, coffee, flowers)
  - Sounds: implied (silence, busy, nature)
  - Abstract: nostalgia, hope, danger, mystery
  - Philosophical: meaning, narrative, time, existence

Providers (all have vision):
  openai      GPT-4o, GPT-4o-mini
  google      Gemini 2.0 Flash, Gemini 1.5 Pro
  anthropic   Claude 3.5 Sonnet, Claude 3 Opus

Environment Variables:
  OPENAI_API_KEY        OpenAI
  GOOGLE_API_KEY        Google Gemini
  ANTHROPIC_API_KEY     Anthropic Claude

Usage:
  mine.py image.jpg                           # Use default resource types
  mine.py image.jpg --resources schema.yml    # Custom shopping list
  mine.py image.jpg --resources "gold,gems,danger,mood"  # Inline list
  mine.py image.jpg --depth philosophical     # Mine deep resources
  cat schema.yml | mine.py image.jpg -        # Schema from stdin

Output is YAML Jazz with semantic comments:
  resources:
    gold:
      quantity: 150        # Piles of coins, ~150 visible
      confidence: 0.9
    danger:
      intensity: 0.7       # Dark corners, unknown depths
      notes: "Something lurks in shadows"
"""

import argparse
import base64
import json
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional

# CONFIGURATION

VERSION = "0.1.0"

class Provider(Enum):
    """Vision LLM providers."""
    OPENAI = "openai"
    GOOGLE = "google"
    ANTHROPIC = "anthropic"

ENV_KEYS = {
    Provider.OPENAI: "OPENAI_API_KEY",
    Provider.GOOGLE: "GOOGLE_API_KEY",
    Provider.ANTHROPIC: "ANTHROPIC_API_KEY",
}

DEFAULT_MODELS = {
    Provider.OPENAI: "gpt-4o-mini",
    Provider.GOOGLE: "gemini-2.0-flash",
    Provider.ANTHROPIC: "claude-3-5-sonnet-20241022",
}

# Depth levels for mining
DEPTH_LEVELS = {
    "surface": "Objects, materials, colors visible in the image",
    "deep": "Hidden meanings, emotions, atmosphere, implied sensations",
    "sensations": "Colors (with hex), textures, inferred smells/sounds, feelings",
    "philosophical": "Abstract concepts, narrative essence, existential elements",
    "full": "All depth levels combined"
}

# Default resource types by depth
DEFAULT_RESOURCES = {
    "surface": [
        "objects", "people", "animals", "materials", "colors", 
        "lighting", "composition", "text"
    ],
    "deep": [
        "mood", "atmosphere", "tension", "emotion", "narrative",
        "relationships", "action", "time_of_day"
    ],
    "sensations": [
        "dominant_colors", "textures", "implied_smells", "implied_sounds",
        "temperature", "humidity", "movement"
    ],
    "philosophical": [
        "meaning", "symbolism", "mortality", "hope", "danger",
        "mystery", "beauty", "passage_of_time", "existence"
    ],
    "full": []  # All of the above
}

# System prompt for mining
MINING_SYSTEM_PROMPT = """You are a resource extractor for images. Your job is to "mine" semantic resources from pictures.

You will receive:
1. An image to analyze
2. A list of resource types to extract (the "shopping list")
3. A depth level (surface, deep, sensations, philosophical, or full)

For each resource type, extract:
- quantity: Count if countable (objects, people)
- intensity: 0.0-1.0 scale if qualitative (mood, danger)
- value: Specific value if applicable (hex color, text content)
- confidence: 0.0-1.0 how certain you are
- notes: Brief observation (YAML Jazz comment style - insightful, specific)

Output ONLY valid YAML. Use comments liberally to add semantic richness.
Format as YAML Jazz - comments are semantic data, not just documentation.

Example output:
```yaml
# Mining results for treasure-room.jpg
# Depth: surface
# Timestamp: 2026-01-19T15:30:00Z

resources:
  gold:
    quantity: 150           # Piles of coins visible, estimated count
    confidence: 0.85
    notes: "Glinting in torchlight, some ancient, some fresh"
    
  gems:
    quantity: 25            # Mixed rubies, emeralds, sapphires
    confidence: 0.7
    subtypes:
      - ruby: 10
      - emerald: 8
      - sapphire: 7
      
  danger:
    intensity: 0.6          # Dark corners suggest hidden threats
    confidence: 0.75
    notes: "The shadows feel alive"
    
  nostalgia:
    intensity: 0.3          # Ancient coins evoke lost civilizations
    confidence: 0.6
    
  dominant_colors:
    - name: "gold"
      hex: "#FFD700"
      coverage: 0.4
    - name: "shadow-purple"  
      hex: "#2D1B4E"
      coverage: 0.3

exhausted: false           # Image still has resources to mine
mining_notes: |
  Rich lode. Multiple passes recommended.
  Deep philosophical mining would yield mortality/greed themes.
```

Be specific. Be insightful. Mine what's actually there, not what you imagine."""


@dataclass
class MiningResult:
    """Result of image mining."""
    success: bool
    resources: dict = field(default_factory=dict)
    yaml_output: str = ""
    error: Optional[str] = None


# CLI DEFINITION

def main():
    """Main entry point — CLI structure.
    
    Commands:
        (default)   Mine resources from image
        scan        Preview what can be mined (no extraction)
        schema      Output example resource schema
        providers   List available providers
    """
    parser = argparse.ArgumentParser(
        description=__doc__.split('\n')[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Output is YAML Jazz with semantic comments."
    )
    parser.add_argument("--version", action="version", version=VERSION)
    parser.add_argument("--debug", action="store_true", help="Show debug output")
    
    subparsers = parser.add_subparsers(dest="command")
    
    # mine command (default)
    mine_parser = subparsers.add_parser(
        "mine",
        help="Extract resources from image (default)",
        description="Analyze image and extract semantic resources."
    )
    _add_mine_args(mine_parser)
    
    # scan command
    scan_parser = subparsers.add_parser(
        "scan",
        help="Preview what can be mined",
        description="Quick scan without full extraction."
    )
    scan_parser.add_argument("image", help="Image file to scan")
    scan_parser.add_argument("--provider", "-p", choices=[p.value for p in Provider])
    
    # schema command
    schema_parser = subparsers.add_parser(
        "schema",
        help="Output example resource schema",
        description="Print example shopping list for each depth level."
    )
    schema_parser.add_argument(
        "--depth", "-d",
        choices=list(DEPTH_LEVELS.keys()),
        default="full",
        help="Depth level to show"
    )
    
    # providers command
    subparsers.add_parser(
        "providers",
        help="List available providers",
        description="Show which vision providers are available."
    )
    
    # Handle default command
    args, remaining = parser.parse_known_args()
    
    if args.command is None:
        if remaining:
            full_args = ["mine"] + remaining
            args = parser.parse_args(full_args)
        else:
            parser.print_help()
            sys.exit(0)
    
    if args.debug:
        os.environ["MINE_DEBUG"] = "1"
    
    _dispatch(args)


def _add_mine_args(parser):
    """Add arguments for mine command."""
    parser.add_argument(
        "image",
        help="Image file to mine (jpg, png, gif, webp)"
    )
    parser.add_argument(
        "resources_arg",
        nargs="?",
        help="Resource schema file, '-' for stdin, or comma-separated list"
    )
    parser.add_argument(
        "--resources", "-r",
        help="Resource types: file.yml, comma-list, or '-' for stdin"
    )
    parser.add_argument(
        "--depth", "-d",
        choices=list(DEPTH_LEVELS.keys()),
        default="surface",
        help="Mining depth (default: surface)"
    )
    parser.add_argument(
        "--provider", "-p",
        choices=[p.value for p in Provider],
        help="Vision provider (default: first available)"
    )
    parser.add_argument(
        "--model", "-m",
        help="Specific model (default: provider's best)"
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        help="Output file (default: stdout)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON instead of YAML"
    )


# IMPLEMENTATION

def _dispatch(args):
    """Route to handler."""
    if args.command == "mine":
        _cmd_mine(args)
    elif args.command == "scan":
        _cmd_scan(args)
    elif args.command == "schema":
        _cmd_schema(args)
    elif args.command == "providers":
        _cmd_providers()
    else:
        _cmd_mine(args)


def _debug(msg: str):
    """Print debug message."""
    if os.environ.get("MINE_DEBUG"):
        print(f"[DEBUG] {msg}", file=sys.stderr)


def _get_api_key(provider: Provider) -> Optional[str]:
    """Get API key for provider."""
    return os.environ.get(ENV_KEYS.get(provider, ""))


def _get_available_providers() -> list[Provider]:
    """Get providers with API keys set."""
    return [p for p in Provider if _get_api_key(p)]


def _select_provider(requested: Optional[str]) -> Provider:
    """Select provider."""
    available = _get_available_providers()
    
    if not available:
        print("Error: No vision providers available. Set at least one API key:", file=sys.stderr)
        for p in Provider:
            print(f"  export {ENV_KEYS[p]}=...", file=sys.stderr)
        sys.exit(1)
    
    if requested:
        provider = Provider(requested)
        if provider not in available:
            print(f"Error: Provider '{requested}' not available", file=sys.stderr)
            sys.exit(1)
        return provider
    
    return available[0]


def _load_image(path: str) -> tuple[bytes, str]:
    """Load image and detect media type."""
    image_path = Path(path)
    if not image_path.exists():
        print(f"Error: Image not found: {path}", file=sys.stderr)
        sys.exit(1)
    
    suffix = image_path.suffix.lower()
    media_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    
    media_type = media_types.get(suffix, "image/jpeg")
    image_data = image_path.read_bytes()
    
    _debug(f"Loaded {path}: {len(image_data)} bytes, {media_type}")
    return image_data, media_type


def _parse_resources(arg: Optional[str], depth: str) -> list[str]:
    """Parse resource list from argument."""
    if not arg:
        # Use defaults for depth
        if depth == "full":
            resources = []
            for level_resources in DEFAULT_RESOURCES.values():
                resources.extend(level_resources)
            return list(set(resources))
        return DEFAULT_RESOURCES.get(depth, DEFAULT_RESOURCES["surface"])
    
    if arg == "-":
        # Read from stdin
        content = sys.stdin.read().strip()
        try:
            import yaml
            data = yaml.safe_load(content)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "resources" in data:
                return data["resources"]
            else:
                return list(data.keys()) if isinstance(data, dict) else [content]
        except Exception:
            return [r.strip() for r in content.split(",")]
    
    path = Path(arg)
    if path.exists():
        # Load from file
        try:
            import yaml
            data = yaml.safe_load(path.read_text())
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "resources" in data:
                return data["resources"]
            else:
                return list(data.keys()) if isinstance(data, dict) else []
        except Exception as e:
            _debug(f"Failed to parse {path}: {e}")
            return []
    else:
        # Comma-separated list
        return [r.strip() for r in arg.split(",")]


def _mine_image(
    image_data: bytes,
    media_type: str,
    resources: list[str],
    depth: str,
    provider: Provider,
    model: str
) -> MiningResult:
    """Mine resources from image using vision LLM."""
    
    # Build user message
    resource_list = "\n".join(f"  - {r}" for r in resources)
    depth_desc = DEPTH_LEVELS.get(depth, DEPTH_LEVELS["surface"])
    
    user_message = f"""Mine this image for semantic resources.

Depth level: {depth}
Description: {depth_desc}

Shopping list (resource types to extract):
{resource_list}

For each resource, provide quantity/intensity, confidence, and insightful notes.
Output ONLY valid YAML with semantic comments (YAML Jazz style)."""

    _debug(f"Mining with {provider.value}/{model}, depth={depth}, {len(resources)} resource types")
    
    # Call appropriate provider
    if provider == Provider.OPENAI:
        return _mine_openai(image_data, media_type, user_message, model)
    elif provider == Provider.GOOGLE:
        return _mine_google(image_data, media_type, user_message, model)
    elif provider == Provider.ANTHROPIC:
        return _mine_anthropic(image_data, media_type, user_message, model)
    else:
        return MiningResult(success=False, error=f"Unknown provider: {provider}")


def _mine_openai(image_data: bytes, media_type: str, user_message: str, model: str) -> MiningResult:
    """Mine using OpenAI GPT-4V."""
    try:
        import httpx
    except ImportError:
        return MiningResult(success=False, error="httpx not installed")
    
    api_key = os.environ.get("OPENAI_API_KEY")
    image_b64 = base64.b64encode(image_data).decode()
    
    try:
        with httpx.Client(timeout=120.0) as client:
            response = client.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json={
                    "model": model,
                    "messages": [
                        {"role": "system", "content": MINING_SYSTEM_PROMPT},
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": user_message},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:{media_type};base64,{image_b64}"
                                    }
                                }
                            ]
                        }
                    ],
                    "max_tokens": 4000,
                }
            )
            response.raise_for_status()
            content = response.json()["choices"][0]["message"]["content"]
            return _parse_mining_output(content)
    except Exception as e:
        return MiningResult(success=False, error=str(e))


def _mine_google(image_data: bytes, media_type: str, user_message: str, model: str) -> MiningResult:
    """Mine using Google Gemini Vision."""
    try:
        import httpx
    except ImportError:
        return MiningResult(success=False, error="httpx not installed")
    
    api_key = os.environ.get("GOOGLE_API_KEY")
    image_b64 = base64.b64encode(image_data).decode()
    
    try:
        with httpx.Client(timeout=120.0) as client:
            response = client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                params={"key": api_key},
                headers={"Content-Type": "application/json"},
                json={
                    "systemInstruction": {"parts": [{"text": MINING_SYSTEM_PROMPT}]},
                    "contents": [{
                        "parts": [
                            {"text": user_message},
                            {
                                "inline_data": {
                                    "mime_type": media_type,
                                    "data": image_b64
                                }
                            }
                        ]
                    }],
                }
            )
            response.raise_for_status()
            content = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            return _parse_mining_output(content)
    except Exception as e:
        return MiningResult(success=False, error=str(e))


def _mine_anthropic(image_data: bytes, media_type: str, user_message: str, model: str) -> MiningResult:
    """Mine using Anthropic Claude Vision."""
    try:
        import httpx
    except ImportError:
        return MiningResult(success=False, error="httpx not installed")
    
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    image_b64 = base64.b64encode(image_data).decode()
    
    try:
        with httpx.Client(timeout=120.0) as client:
            response = client.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": api_key,
                    "anthropic-version": "2023-06-01",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "max_tokens": 4000,
                    "system": MINING_SYSTEM_PROMPT,
                    "messages": [{
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": media_type,
                                    "data": image_b64,
                                }
                            },
                            {"type": "text", "text": user_message}
                        ]
                    }],
                }
            )
            response.raise_for_status()
            content = response.json()["content"][0]["text"]
            return _parse_mining_output(content)
    except Exception as e:
        return MiningResult(success=False, error=str(e))


def _parse_mining_output(content: str) -> MiningResult:
    """Parse LLM output into MiningResult."""
    # Strip markdown code fences if present
    content = content.strip()
    if content.startswith("```yaml"):
        content = content[7:]
    elif content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    content = content.strip()
    
    try:
        import yaml
        resources = yaml.safe_load(content)
        return MiningResult(
            success=True,
            resources=resources if isinstance(resources, dict) else {"raw": resources},
            yaml_output=content
        )
    except Exception as e:
        _debug(f"YAML parse warning: {e}")
        # Return raw content as YAML output anyway
        return MiningResult(
            success=True,
            resources={},
            yaml_output=content
        )


# COMMAND IMPLEMENTATIONS

def _cmd_providers():
    """List available providers."""
    print("Vision Providers (for image mining):\n")
    for p in Provider:
        key = _get_api_key(p)
        status = "✓" if key else "✗"
        env = ENV_KEYS[p]
        model = DEFAULT_MODELS[p]
        if key:
            print(f"  {status} {p.value:12} ({model})")
        else:
            print(f"  {status} {p.value:12} (set {env})")


def _cmd_schema(args):
    """Output example resource schema."""
    depth = args.depth
    
    if depth == "full":
        print("# Full mining schema - all depth levels")
        print("# Use with: mine.py image.jpg --resources schema.yml --depth full\n")
        all_resources = []
        for level, resources in DEFAULT_RESOURCES.items():
            if level != "full":
                print(f"# {level.upper()}")
                for r in resources:
                    print(f"- {r}")
                    all_resources.append(r)
                print()
    else:
        print(f"# {depth.upper()} mining schema")
        print(f"# {DEPTH_LEVELS[depth]}\n")
        for r in DEFAULT_RESOURCES.get(depth, []):
            print(f"- {r}")


def _cmd_scan(args):
    """Quick scan of image."""
    image_data, media_type = _load_image(args.image)
    provider = _select_provider(getattr(args, 'provider', None))
    model = DEFAULT_MODELS[provider]
    
    # Quick scan with minimal resources
    scan_resources = ["objects", "people", "mood", "colors", "notable_features"]
    
    print(f"Scanning {args.image} with {provider.value}...\n", file=sys.stderr)
    
    result = _mine_image(image_data, media_type, scan_resources, "surface", provider, model)
    
    if result.success:
        print(result.yaml_output)
    else:
        print(f"Error: {result.error}", file=sys.stderr)
        sys.exit(1)


def _cmd_mine(args):
    """Mine resources from image."""
    # Load image
    image_data, media_type = _load_image(args.image)
    
    # Get resource list
    resources_arg = args.resources_arg or getattr(args, 'resources', None)
    resources = _parse_resources(resources_arg, args.depth)
    
    if not resources:
        print("Error: No resource types specified", file=sys.stderr)
        sys.exit(1)
    
    # Select provider
    provider = _select_provider(getattr(args, 'provider', None))
    model = getattr(args, 'model', None) or DEFAULT_MODELS[provider]
    
    print(f"Mining {args.image}", file=sys.stderr)
    print(f"  Provider: {provider.value}/{model}", file=sys.stderr)
    print(f"  Depth: {args.depth}", file=sys.stderr)
    print(f"  Resources: {len(resources)} types", file=sys.stderr)
    print(file=sys.stderr)
    
    # Mine!
    result = _mine_image(image_data, media_type, resources, args.depth, provider, model)
    
    if not result.success:
        print(f"Error: {result.error}", file=sys.stderr)
        sys.exit(1)
    
    # Output
    output = result.yaml_output
    if getattr(args, 'json', False):
        output = json.dumps(result.resources, indent=2)
    
    if args.output:
        args.output.write_text(output)
        print(f"✓ Saved: {args.output}")
    else:
        print(output)


# MAIN

if __name__ == "__main__":
    main()
