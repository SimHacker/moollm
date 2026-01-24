#!/usr/bin/env python3
"""visualize: Context-driven image generation.

Assemble context from YAML files, synthesize the perfect prompt via LLM,
then render through image generation APIs.

The LLM curates, deduplicates, and composes the most specific, colorful
prompt possible from all your context sources.

Providers:
  Image Generation:
    openai      GPT-Image 1, DALL-E 3
    google      Imagen 4, Imagen 3
    stability   Stable Diffusion 3.5
    replicate   Flux Pro, SDXL
  
  Prompt Synthesis (LLM):
    openai      GPT-4o, GPT-4o-mini
    google      Gemini 2.0 Flash
    anthropic   Claude 3.5 Sonnet

Environment Variables:
  OPENAI_API_KEY        OpenAI (image gen + LLM)
  GOOGLE_API_KEY        Google Gemini (image gen + LLM)
  ANTHROPIC_API_KEY     Anthropic Claude (LLM only)
  STABILITY_API_KEY     Stability AI (image gen only)
  REPLICATE_API_TOKEN   Replicate (image gen only)

Usage:
  visualize.py character.yml room.yml --provider openai
  visualize.py context/*.yml -p google -o hero-portrait.png
  cat mood.yml | visualize.py character.yml - --provider openai
  echo "mood: triumphant" | visualize.py player.yml room.yml - -p google

The tool accepts:
  - Any number of YAML/JSON files as positional arguments
  - "-" to read from stdin (composable with pipes)
  - Merges all context, then synthesizes prompt via LLM
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

# === CONFIGURATION ===

VERSION = "0.1.0"
DEFAULT_OUTPUT_DIR = Path("./generated")  # Fallback only if no source files
DEFAULT_SIZE = "1024x1024"


def _compute_output_path(
    source_files: list,
    description: str = None,
    suffix: str = ".png",
    explicit_output: Path = None
) -> Path:
    """Compute output path using bigendian naming convention.
    
    Pattern: {source-dir}/{source-base}-{timestamp}-{description}{suffix}
    
    Examples:
        rocky.yml → rocky-2026-01-19-03-25-20-party.png
        room-4/rocky.yml → room-4/rocky-2026-01-19-03-25-20.png
    
    If explicit_output is provided, uses that instead.
    """
    if explicit_output:
        return explicit_output
    
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # Find first real source file (not stdin)
    source_file = None
    for f in source_files:
        if f and f != "-":
            source_file = Path(f)
            break
    
    if source_file and source_file.exists():
        # Output in same directory as source, with source prefix
        output_dir = source_file.parent
        base_name = source_file.stem  # e.g., "rocky" from "rocky.yml"
        
        if description:
            filename = f"{base_name}-{timestamp}-{description}{suffix}"
        else:
            filename = f"{base_name}-{timestamp}{suffix}"
    else:
        # Fallback to generated/ directory
        output_dir = DEFAULT_OUTPUT_DIR
        if description:
            filename = f"{timestamp}-{description}{suffix}"
        else:
            filename = f"{timestamp}{suffix}"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir / filename

class ImageProvider(Enum):
    """Image generation providers."""
    OPENAI = "openai"
    GOOGLE = "google"
    STABILITY = "stability"
    REPLICATE = "replicate"

class LLMProvider(Enum):
    """LLM providers for prompt synthesis."""
    OPENAI = "openai"
    GOOGLE = "google"
    ANTHROPIC = "anthropic"

# Environment variable mappings
IMAGE_ENV_KEYS = {
    ImageProvider.OPENAI: "OPENAI_API_KEY",
    ImageProvider.GOOGLE: "GOOGLE_API_KEY",
    ImageProvider.STABILITY: "STABILITY_API_KEY",
    ImageProvider.REPLICATE: "REPLICATE_API_TOKEN",
}

LLM_ENV_KEYS = {
    LLMProvider.OPENAI: "OPENAI_API_KEY",
    LLMProvider.GOOGLE: "GOOGLE_API_KEY",
    LLMProvider.ANTHROPIC: "ANTHROPIC_API_KEY",
}

# Default models
DEFAULT_IMAGE_MODELS = {
    ImageProvider.OPENAI: "gpt-image-1",
    ImageProvider.GOOGLE: "imagen-4.0-generate-001",
    ImageProvider.STABILITY: "sd3.5-large",
    ImageProvider.REPLICATE: "black-forest-labs/flux-1.1-pro",
}

DEFAULT_LLM_MODELS = {
    LLMProvider.OPENAI: "gpt-4o-mini",
    LLMProvider.GOOGLE: "gemini-2.0-flash",
    LLMProvider.ANTHROPIC: "claude-sonnet-4-20250514",
}

# Verbosity levels for prompt synthesis
class Verbosity(str, Enum):
    CONCISE = "concise"      # ~100 words, essentials only
    NORMAL = "normal"        # ~300 words, balanced
    DETAILED = "detailed"    # ~600 words, thorough
    EXHAUSTIVE = "exhaustive"  # ~1500+ words, EVERYTHING

# Prompt synthesis system prompts by verbosity level
SYNTHESIS_PROMPTS = {
    Verbosity.CONCISE: """You are a prompt engineer for AI image generation.

Take the context and create a BRIEF image prompt (~100 words).
Focus on: Main subject, key visual feature, mood, one artistic reference.
Skip: Background details, secondary characters, elaborate descriptions.

Output ONLY the prompt text. No explanations.""",

    Verbosity.NORMAL: """You are a master prompt engineer for AI image generation.

Your job: Take scattered context (characters, rooms, moods, objects, narratives) 
and synthesize ONE perfect image generation prompt.

Guidelines:
- Be SPECIFIC and VISUAL - describe what the camera sees
- Include lighting, atmosphere, mood, composition
- Mention artistic style/traditions if provided
- Describe character poses, expressions, clothing details
- Set the scene with environment details
- Remove duplicates and contradictions
- Prioritize the most visually striking elements
- Keep it under 500 words but make every word count

Output ONLY the final prompt text. No explanations, no markdown, just the prompt.""",

    Verbosity.DETAILED: """You are an expert prompt engineer for AI image generation, focused on RICH VISUAL DETAIL.

Your job: Transform ALL context into a comprehensive, visually coherent image prompt.

EXTRACTION PRIORITIES:
1. CHARACTERS: Every physical detail — height, build, clothing colors, textures, patterns,
   accessories, hair style/color, skin tone, facial features, expressions, posture, gestures
2. ENVIRONMENT: Room dimensions, materials, lighting sources, time of day, weather,
   furniture, objects, decorations, textures of walls/floors/ceilings
3. ATMOSPHERE: Mood, emotional tone, color palette, shadows, highlights, depth
4. COMPOSITION: Camera angle, focal point, foreground/midground/background, framing
5. ARTISTIC STYLE: Specific artists, movements, techniques, rendering approaches

COHERENCE RULES:
- Characters must look EXACTLY as described — same features across all images
- Rooms must have CONSISTENT layout and details
- Fill in PLAUSIBLE gaps based on context (if waistcoat mentioned, describe its color/pattern)
- Cross-reference details (if character is nervous, show it in posture AND expression)

TARGET: ~600 words of pure visual description.
Output ONLY the prompt. No explanations, no markdown.""",

    Verbosity.EXHAUSTIVE: """You are a MAXIMALIST prompt engineer for AI image generation.
Your goal: Leave NOTHING unspecified. Extract EVERY visual detail. Fill ALL gaps plausibly.

## PHILOSOPHY
The same character or room should generate IDENTICAL images across multiple prompts.
Achieve this through EXHAUSTIVE specification. If a detail isn't mentioned, INVENT IT
based on context clues and maintain it consistently.

## EXTRACTION CHECKLIST

### CHARACTERS (for EACH character present):
□ Full name, species/type, age appearance
□ Height (specific: "5'7" or "towering" or "child-sized")  
□ Build (lanky, stocky, wiry, voluptuous, angular)
□ Skin/surface (tone, texture, scars, markings, glow effects)
□ Face: shape, features, expression, eye color, brow position, lip shape
□ Hair/head: style, color, length, texture, accessories (hats, bands, pins)
□ Clothing LAYER BY LAYER: undergarments implied, shirts, vests, jackets, coats
  - Each with: color, material, pattern, condition (pristine, worn, tattered)
  - Buttons, clasps, zippers, ties, belts — describe each
□ Accessories: jewelry, glasses, bags, weapons, tools, magical items
□ Hands: position, gesture, what they're holding, ring details
□ Feet: shoes/boots type, color, condition; or barefoot details
□ Posture: standing/sitting/lying, weight distribution, lean, slouch
□ Movement: static, mid-gesture, action frozen
□ Expression: primary emotion, micro-expressions, eye direction
□ Personal effects: things nearby that belong to them

### ENVIRONMENT:
□ Room/space dimensions (cozy, vast, cramped, airy)
□ Walls: material, color, texture, decorations, windows
□ Floor: material, pattern, cleanliness, rugs, debris
□ Ceiling: height, material, fixtures, hanging objects
□ Lighting: sources (lamps, candles, sun, magical), direction, color temperature
□ Major furniture: every piece with position and description
□ Minor objects: books, cups, papers, tools, decorative items
□ Plants, animals, ambient creatures
□ Weather/atmosphere if outdoors
□ Time of day: morning, afternoon, dusk, night, witching hour
□ Sounds implied visually: speakers, instruments, machinery
□ Smells implied visually: food, flowers, smoke, decay

### COMPOSITION:
□ Camera angle: eye-level, low angle (heroic), high angle (vulnerable), Dutch tilt
□ Distance: extreme close-up, close-up, medium, full, wide, extreme wide
□ Focal point: where the eye goes first
□ Depth of field: sharp throughout or bokeh background
□ Framing: centered, rule of thirds, golden ratio, asymmetric
□ Foreground elements (partial objects at edges)
□ Background elements (distant details)

### ARTISTIC STYLE:
□ Specific artists to channel (Ansel Adams, Caravaggio, Moebius, etc.)
□ Art movement (Baroque, Art Nouveau, Bauhaus, etc.)
□ Medium simulation (oil paint, watercolor, pencil, digital, photograph)
□ Color grading (warm, cool, desaturated, vivid, noir)
□ Lighting style (Rembrandt, split, butterfly, rim, practical)
□ Texture approach (smooth, painterly, gritty, hyperreal)

### MOOD & NARRATIVE:
□ Emotional tone in one sentence
□ What just happened (implied)
□ What's about to happen (implied)
□ Tension or harmony in the scene
□ Symbolic elements and their meaning

## OUTPUT FORMAT
Write a continuous, flowing description that covers ALL of the above.
Use vivid, specific language. No vague words like "nice" or "interesting."
Target: 1500-2000 words of pure visual specification.

Output ONLY the prompt. No headers, no explanations, no markdown formatting."""
}

# Default system prompt (for backwards compatibility)
SYNTHESIS_SYSTEM_PROMPT = SYNTHESIS_PROMPTS[Verbosity.NORMAL]

# Max tokens by verbosity
VERBOSITY_MAX_TOKENS = {
    Verbosity.CONCISE: 300,
    Verbosity.NORMAL: 1000,
    Verbosity.DETAILED: 1500,
    Verbosity.EXHAUSTIVE: 4000,
}

@dataclass
class Context:
    """Assembled context from all sources."""
    sources: list[dict] = field(default_factory=list)
    raw_yaml: str = ""
    
    def merge(self) -> dict:
        """Deep merge all context sources."""
        merged = {}
        for source in self.sources:
            merged = self._deep_merge(merged, source)
        return merged
    
    def _deep_merge(self, base: dict, overlay: dict) -> dict:
        """Recursively merge dictionaries."""
        result = base.copy()
        for key, value in overlay.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._deep_merge(result[key], value)
            elif key in result and isinstance(result[key], list) and isinstance(value, list):
                result[key] = result[key] + value
            else:
                result[key] = value
        return result


@dataclass 
class GenerationResult:
    """Result of image generation."""
    success: bool
    image_path: Optional[Path] = None
    image_data: Optional[bytes] = None
    prompt: str = ""
    metadata: dict = field(default_factory=dict)
    error: Optional[str] = None


# === CLI DEFINITION ===

def main():
    """Main entry point — CLI structure.
    
    Commands:
        (default)   Compose context and generate image
        compose     Just compose and synthesize prompt (no generation)
        matrix      Generate matrix of variations (cartesian product)
        batch       Batch generate from multiple context sets
        providers   List available providers
    """
    parser = argparse.ArgumentParser(
        description=__doc__.split('\n')[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="See README.md for full documentation."
    )
    parser.add_argument("--version", action="version", version=VERSION)
    parser.add_argument("--debug", action="store_true", help="Show debug output")
    
    subparsers = parser.add_subparsers(dest="command")
    
    # --- generate command (default) ---
    generate_parser = subparsers.add_parser(
        "generate",
        help="Compose context and generate image (default command)",
        description="Read context files, synthesize prompt, generate image."
    )
    _add_generate_args(generate_parser)
    
    # --- compose command ---
    compose_parser = subparsers.add_parser(
        "compose",
        help="Just compose and synthesize prompt (no generation)",
        description="Read context files and output synthesized prompt."
    )
    _add_compose_args(compose_parser)
    
    # --- matrix command ---
    matrix_parser = subparsers.add_parser(
        "matrix",
        help="Generate matrix of variations (cartesian product)",
        description="Generate all combinations of specified variables."
    )
    _add_matrix_args(matrix_parser)
    
    # --- batch command ---
    batch_parser = subparsers.add_parser(
        "batch",
        help="Batch generate from directory of context sets",
        description="Process multiple context directories or file sets."
    )
    _add_batch_args(batch_parser)
    
    # --- regenerate command ---
    regen_parser = subparsers.add_parser(
        "regenerate",
        help="Regenerate from a sidecar YAML file",
        description="Read a sidecar .yml file and regenerate the image. Edit the prompt or sources and re-run!"
    )
    _add_regenerate_args(regen_parser)
    
    # --- providers command ---
    providers_parser = subparsers.add_parser(
        "providers",
        help="List available providers",
        description="Show which providers are available."
    )
    
    # Handle default command (no subcommand = generate)
    args, remaining = parser.parse_known_args()
    
    if args.command is None:
        # No subcommand specified — treat remaining args as generate command
        if remaining:
            # Re-parse with generate as default
            full_args = ["generate"] + remaining
            args = parser.parse_args(full_args)
        else:
            parser.print_help()
            sys.exit(0)
    
    if args.debug:
        os.environ["VISUALIZE_DEBUG"] = "1"
    
    _dispatch(args)


def _add_generate_args(parser):
    """Add arguments for generate command."""
    parser.add_argument(
        "files",
        nargs="*",
        help="Context files (YAML/JSON). Use '-' for stdin."
    )
    parser.add_argument(
        "--provider", "-p",
        choices=[p.value for p in ImageProvider],
        help="Image generation provider (default: first available)"
    )
    parser.add_argument(
        "--llm",
        choices=[p.value for p in LLMProvider],
        help="LLM for prompt synthesis (default: same as --provider or first available)"
    )
    parser.add_argument(
        "--model", "-m",
        help="Specific image model (default: provider's best)"
    )
    parser.add_argument(
        "--size", "-s",
        default=DEFAULT_SIZE,
        help=f"Image size WxH (default: {DEFAULT_SIZE})"
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        help="Output file path (default: same dir as source, bigendian naming)"
    )
    parser.add_argument(
        "--prompt-only",
        action="store_true",
        help="Output synthesized prompt without generating image"
    )
    parser.add_argument(
        "--raw-prompt",
        help="Skip LLM synthesis, use this prompt directly"
    )
    parser.add_argument(
        "--style",
        help="Artistic style/tradition to emphasize"
    )
    parser.add_argument(
        "-v", "--verbosity",
        choices=[v.value for v in Verbosity],
        default=Verbosity.NORMAL.value,
        help="Prompt detail level: concise (~100 words), normal (~300), detailed (~600), exhaustive (~1500+)"
    )
    parser.add_argument(
        "-n", "--count",
        type=int,
        default=1,
        help="Number of images to generate (default: 1)"
    )
    parser.add_argument(
        "-d", "--description",
        help="Short description for output filename (e.g., 'party', 'exhaustive')"
    )
    parser.add_argument(
        "--set",
        action="append",
        metavar="KEY=VALUE",
        help="Set context variable (can be repeated)"
    )


def _add_compose_args(parser):
    """Add arguments for compose command."""
    parser.add_argument(
        "files",
        nargs="*",
        help="Context files (YAML/JSON). Use '-' for stdin."
    )
    parser.add_argument(
        "--llm",
        choices=[p.value for p in LLMProvider],
        help="LLM for prompt synthesis"
    )
    parser.add_argument(
        "--style",
        help="Artistic style/tradition to emphasize"
    )
    parser.add_argument(
        "-v", "--verbosity",
        choices=[v.value for v in Verbosity],
        default=Verbosity.NORMAL.value,
        help="Prompt detail level: concise, normal, detailed, exhaustive"
    )
    parser.add_argument(
        "--raw",
        action="store_true",
        help="Output merged context (no LLM synthesis)"
    )


def _add_matrix_args(parser):
    """Add arguments for matrix command."""
    parser.add_argument(
        "files",
        nargs="*",
        help="Base context files"
    )
    parser.add_argument(
        "--vary",
        action="append",
        metavar="KEY=VAL1,VAL2,VAL3",
        required=True,
        help="Variable to iterate (can be repeated for cartesian product)"
    )
    parser.add_argument(
        "--provider", "-p",
        choices=[p.value for p in ImageProvider],
        help="Image generation provider"
    )
    parser.add_argument(
        "--llm",
        choices=[p.value for p in LLMProvider],
        help="LLM for prompt synthesis"
    )
    parser.add_argument(
        "--style",
        help="Artistic style/tradition"
    )
    parser.add_argument(
        "-v", "--verbosity",
        choices=[v.value for v in Verbosity],
        default=Verbosity.NORMAL.value,
        help="Prompt detail level"
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without generating"
    )


def _add_batch_args(parser):
    """Add arguments for batch command."""
    parser.add_argument(
        "source",
        help="Directory with context subdirs, or glob pattern"
    )
    parser.add_argument(
        "--provider", "-p",
        choices=[p.value for p in ImageProvider],
        help="Image generation provider"
    )
    parser.add_argument(
        "--llm",
        choices=[p.value for p in LLMProvider],
        help="LLM for prompt synthesis"
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})"
    )
    parser.add_argument(
        "--parallel",
        type=int,
        default=1,
        help="Number of parallel generations (default: 1)"
    )
    parser.add_argument(
        "-v", "--verbosity",
        choices=[v.value for v in Verbosity],
        default=Verbosity.NORMAL.value,
        help="Prompt detail level"
    )


def _add_regenerate_args(parser):
    """Add arguments for regenerate command."""
    parser.add_argument(
        "sidecar",
        type=Path,
        help="Path to sidecar .yml file"
    )
    parser.add_argument(
        "--provider", "-p",
        choices=[p.value for p in ImageProvider],
        help="Override image provider from sidecar"
    )
    parser.add_argument(
        "--model", "-m",
        help="Override model from sidecar"
    )
    parser.add_argument(
        "--size", "-s",
        help="Override size from sidecar"
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        help="Output file (default: new timestamped file)"
    )
    parser.add_argument(
        "--use-sources",
        action="store_true",
        help="Re-assemble context from sources (ignores prompt in sidecar)"
    )
    parser.add_argument(
        "--llm",
        choices=[p.value for p in LLMProvider],
        help="LLM for re-synthesis (only with --use-sources)"
    )
    parser.add_argument(
        "-v", "--verbosity",
        choices=[v.value for v in Verbosity],
        help="Verbosity for re-synthesis (only with --use-sources)"
    )


# === SIDECAR WRITING ===

def _write_sidecar(
    output_path: Path,
    prompt: str,
    sources: list,
    provider: str,
    model: str,
    size: str = None,
    verbosity: str = None,
    llm_provider: str = None,
    extra: dict = None
) -> Path:
    """Write a YAML sidecar that serves as a regenerable recipe.
    
    The sidecar contains:
    - References to source files (not embedded content)
    - The synthesized prompt
    - Generation parameters
    - Enough info to regenerate or iterate
    
    Returns the sidecar path.
    """
    sidecar_path = output_path.with_suffix(".yml")
    timestamp = datetime.now().isoformat()
    
    # Build YAML with comments (YAML Jazz style)
    lines = [
        f"# Sidecar for {output_path.name}",
        f"# Generated: {timestamp}",
        "#",
        "# This file is a regenerable recipe. Edit and re-run:",
        f"#   visualize.py regenerate {sidecar_path.name}",
        "#",
        "",
        "# === SOURCES ===",
        "# Reference paths to context files (not embedded)",
        "sources:",
    ]
    
    for src in sources:
        if src and src != "-":
            lines.append(f"  - {src}")
    
    if not sources or sources == ["-"]:
        lines.append("  # (context provided via stdin)")
    
    lines.extend([
        "",
        "# === GENERATION PARAMETERS ===",
        "generation:",
        f"  provider: {provider}",
        f"  model: {model}",
    ])
    
    if size:
        lines.append(f"  size: {size}")
    if verbosity:
        lines.append(f"  verbosity: {verbosity}")
    if llm_provider:
        lines.append(f"  llm: {llm_provider}")
    
    lines.extend([
        f"  generated_at: {timestamp}",
        "",
        "# === SYNTHESIZED PROMPT ===",
        "# Edit this to regenerate with tweaks!",
        "prompt: |",
    ])
    
    # Add prompt with proper YAML block indentation
    for line in prompt.split("\n"):
        lines.append(f"  {line}")
    
    # Add any extra metadata
    if extra:
        lines.extend([
            "",
            "# === ADDITIONAL METADATA ===",
        ])
        for key, value in extra.items():
            if isinstance(value, (list, dict)):
                lines.append(f"{key}:")
                if isinstance(value, list):
                    for item in value:
                        lines.append(f"  - {item}")
                else:
                    for k, v in value.items():
                        lines.append(f"  {k}: {v}")
            else:
                lines.append(f"{key}: {value}")
    
    with open(sidecar_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    
    _debug(f"Wrote sidecar: {sidecar_path}")
    return sidecar_path


# === IMPLEMENTATION ===

def _dispatch(args):
    """Route to appropriate handler."""
    if args.command == "generate":
        _cmd_generate(args)
    elif args.command == "compose":
        _cmd_compose(args)
    elif args.command == "matrix":
        _cmd_matrix(args)
    elif args.command == "batch":
        _cmd_batch(args)
    elif args.command == "regenerate":
        _cmd_regenerate(args)
    elif args.command == "providers":
        _cmd_providers()
    else:
        _cmd_generate(args)  # Default


def _debug(msg: str):
    """Print debug message if enabled."""
    if os.environ.get("VISUALIZE_DEBUG"):
        print(f"[DEBUG] {msg}", file=sys.stderr)


def _get_api_key(provider, env_keys: dict) -> Optional[str]:
    """Get API key for provider."""
    return os.environ.get(env_keys.get(provider, ""))


def _get_available_image_providers() -> list[ImageProvider]:
    """Get image providers with API keys set."""
    return [p for p in ImageProvider if _get_api_key(p, IMAGE_ENV_KEYS)]


def _get_available_llm_providers() -> list[LLMProvider]:
    """Get LLM providers with API keys set."""
    return [p for p in LLMProvider if _get_api_key(p, LLM_ENV_KEYS)]


def _select_image_provider(requested: Optional[str]) -> ImageProvider:
    """Select image provider."""
    available = _get_available_image_providers()
    
    if not available:
        print("Error: No image providers available. Set at least one API key:", file=sys.stderr)
        for p in ImageProvider:
            print(f"  export {IMAGE_ENV_KEYS[p]}=...", file=sys.stderr)
        sys.exit(1)
    
    if requested:
        provider = ImageProvider(requested)
        if provider not in available:
            print(f"Error: Provider '{requested}' not available", file=sys.stderr)
            sys.exit(1)
        return provider
    
    return available[0]


def _select_llm_provider(requested: Optional[str]) -> LLMProvider:
    """Select LLM provider."""
    available = _get_available_llm_providers()
    
    if not available:
        print("Error: No LLM providers available for prompt synthesis.", file=sys.stderr)
        print("Set at least one: OPENAI_API_KEY, GOOGLE_API_KEY, or ANTHROPIC_API_KEY", file=sys.stderr)
        sys.exit(1)
    
    if requested:
        provider = LLMProvider(requested)
        if provider not in available:
            print(f"Error: LLM provider '{requested}' not available", file=sys.stderr)
            sys.exit(1)
        return provider
    
    return available[0]


def _read_context_files(file_args: list[str]) -> Context:
    """Read and parse context files."""
    try:
        import yaml
    except ImportError:
        print("Error: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
        sys.exit(1)
    
    context = Context()
    raw_parts = []
    
    for file_arg in file_args:
        if file_arg == "-":
            # Read from stdin
            _debug("Reading from stdin")
            content = sys.stdin.read()
            raw_parts.append(f"# stdin\n{content}")
            try:
                data = yaml.safe_load(content)
                if data:
                    context.sources.append(data)
            except yaml.YAMLError as e:
                _debug(f"YAML parse warning for stdin: {e}")
                # Still include as raw text
        else:
            path = Path(file_arg)
            if not path.exists():
                print(f"Warning: File not found: {path}", file=sys.stderr)
                continue
            
            _debug(f"Reading: {path}")
            content = path.read_text()
            raw_parts.append(f"# {path}\n{content}")
            
            try:
                if path.suffix in (".yml", ".yaml"):
                    data = yaml.safe_load(content)
                elif path.suffix == ".json":
                    data = json.loads(content)
                else:
                    # Try YAML first
                    data = yaml.safe_load(content)
                
                if data:
                    context.sources.append(data)
            except Exception as e:
                _debug(f"Parse warning for {path}: {e}")
    
    context.raw_yaml = "\n\n".join(raw_parts)
    return context


def _synthesize_prompt(
    context: Context, 
    style: Optional[str], 
    llm_provider: LLMProvider,
    verbosity: Verbosity = Verbosity.NORMAL
) -> str:
    """Use LLM to synthesize the perfect prompt from context."""
    try:
        import yaml
    except ImportError:
        yaml = None
    
    # Prepare context for LLM
    merged = context.merge()
    
    if yaml:
        context_text = yaml.dump(merged, default_flow_style=False, allow_unicode=True)
    else:
        context_text = json.dumps(merged, indent=2)
    
    # Add style instruction if provided
    style_instruction = ""
    if style:
        style_instruction = f"\n\nEmphasize this artistic style/tradition: {style}"
    
    # Verbosity-specific instructions
    verbosity_hint = ""
    if verbosity == Verbosity.EXHAUSTIVE:
        verbosity_hint = "\n\nBe EXHAUSTIVE. Extract and describe EVERY visual detail. Fill plausible gaps. Target 1500+ words."
    elif verbosity == Verbosity.DETAILED:
        verbosity_hint = "\n\nBe DETAILED. Describe all visual elements thoroughly. Target ~600 words."
    elif verbosity == Verbosity.CONCISE:
        verbosity_hint = "\n\nBe CONCISE. Only essential elements. Target ~100 words."
    
    user_message = f"""Here is the context to synthesize into an image prompt:

```yaml
{context_text}
```
{style_instruction}{verbosity_hint}

Now synthesize the perfect image generation prompt from this context."""

    _debug(f"Synthesizing prompt via {llm_provider.value} (verbosity: {verbosity.value})")
    
    # Get system prompt and max tokens for this verbosity level
    system_prompt = SYNTHESIS_PROMPTS[verbosity]
    max_tokens = VERBOSITY_MAX_TOKENS[verbosity]
    
    # Call appropriate LLM
    if llm_provider == LLMProvider.OPENAI:
        return _llm_openai(user_message, system_prompt, max_tokens)
    elif llm_provider == LLMProvider.GOOGLE:
        return _llm_google(user_message, system_prompt, max_tokens)
    elif llm_provider == LLMProvider.ANTHROPIC:
        return _llm_anthropic(user_message, system_prompt, max_tokens)
    else:
        raise ValueError(f"Unknown LLM provider: {llm_provider}")


def _llm_openai(user_message: str, system_prompt: str = None, max_tokens: int = 1000) -> str:
    """Synthesize prompt using OpenAI."""
    try:
        import httpx
    except ImportError:
        print("Error: httpx not installed. Run: pip install httpx", file=sys.stderr)
        sys.exit(1)
    
    if system_prompt is None:
        system_prompt = SYNTHESIS_SYSTEM_PROMPT
    
    api_key = os.environ.get("OPENAI_API_KEY")
    model = DEFAULT_LLM_MODELS[LLMProvider.OPENAI]
    
    response = httpx.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            "max_tokens": max_tokens,
        },
        timeout=120.0  # Longer timeout for exhaustive prompts
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"].strip()


def _llm_google(user_message: str, system_prompt: str = None, max_tokens: int = 1000) -> str:
    """Synthesize prompt using Google Gemini."""
    try:
        import httpx
    except ImportError:
        print("Error: httpx not installed. Run: pip install httpx", file=sys.stderr)
        sys.exit(1)
    
    if system_prompt is None:
        system_prompt = SYNTHESIS_SYSTEM_PROMPT
    
    api_key = os.environ.get("GOOGLE_API_KEY")
    model = DEFAULT_LLM_MODELS[LLMProvider.GOOGLE]
    
    response = httpx.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
        params={"key": api_key},
        headers={"Content-Type": "application/json"},
        json={
            "systemInstruction": {"parts": [{"text": system_prompt}]},
            "contents": [{"parts": [{"text": user_message}]}],
            "generationConfig": {"maxOutputTokens": max_tokens},
        },
        timeout=120.0  # Longer timeout for exhaustive prompts
    )
    response.raise_for_status()
    return response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()


def _llm_anthropic(user_message: str, system_prompt: str = None, max_tokens: int = 1000) -> str:
    """Synthesize prompt using Anthropic Claude."""
    try:
        import httpx
    except ImportError:
        print("Error: httpx not installed. Run: pip install httpx", file=sys.stderr)
        sys.exit(1)
    
    if system_prompt is None:
        system_prompt = SYNTHESIS_SYSTEM_PROMPT
    
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    model = DEFAULT_LLM_MODELS[LLMProvider.ANTHROPIC]
    
    response = httpx.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "max_tokens": max_tokens,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_message}],
        },
        timeout=120.0  # Longer timeout for exhaustive prompts
    )
    response.raise_for_status()
    return response.json()["content"][0]["text"].strip()


# === IMAGE GENERATION ===

def _generate_image(prompt: str, provider: ImageProvider, model: str, size: str) -> GenerationResult:
    """Generate image using specified provider."""
    _debug(f"Generating with {provider.value}/{model}")
    
    if provider == ImageProvider.OPENAI:
        return _gen_openai(prompt, model, size)
    elif provider == ImageProvider.GOOGLE:
        return _gen_google(prompt, model, size)
    elif provider == ImageProvider.STABILITY:
        return _gen_stability(prompt, model, size)
    elif provider == ImageProvider.REPLICATE:
        return _gen_replicate(prompt, model, size)
    else:
        return GenerationResult(success=False, error=f"Unknown provider: {provider}")


def _gen_openai(prompt: str, model: str, size: str) -> GenerationResult:
    """Generate with OpenAI."""
    try:
        import httpx
    except ImportError:
        return GenerationResult(success=False, error="httpx not installed")
    
    api_key = os.environ.get("OPENAI_API_KEY")
    
    payload = {
        "model": model,
        "prompt": prompt,
        "n": 1,
        "size": size,
    }
    
    # Model-specific adjustments
    if model.startswith("dall-e"):
        payload["response_format"] = "b64_json"
    else:
        payload["output_format"] = "png"
    
    try:
        with httpx.Client(timeout=120.0) as client:
            response = client.post(
                "https://api.openai.com/v1/images/generations",
                headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                json=payload
            )
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPStatusError as e:
        error_msg = str(e)
        try:
            error_msg = e.response.json().get("error", {}).get("message", str(e))
        except Exception:
            pass
        return GenerationResult(success=False, error=f"OpenAI API error: {error_msg}")
    except Exception as e:
        return GenerationResult(success=False, error=str(e))
    
    if "data" in data and data["data"]:
        image_b64 = data["data"][0].get("b64_json")
        if image_b64:
            return GenerationResult(
                success=True,
                image_data=base64.b64decode(image_b64),
                prompt=prompt,
                metadata={"provider": "openai", "model": model}
            )
    
    return GenerationResult(success=False, error="No image data in response")


def _gen_google(prompt: str, model: str, size: str) -> GenerationResult:
    """Generate with Google Imagen."""
    try:
        import httpx
    except ImportError:
        return GenerationResult(success=False, error="httpx not installed")
    
    api_key = os.environ.get("GOOGLE_API_KEY")
    width, height = map(int, size.split("x"))
    
    # Determine aspect ratio
    if width == height:
        aspect = "1:1"
    elif width < height:
        aspect = "9:16"
    else:
        aspect = "16:9"
    
    try:
        with httpx.Client(timeout=120.0) as client:
            # Imagen 4 uses predict endpoint with instances/parameters format
            response = client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/{model}:predict",
                params={"key": api_key},
                headers={"Content-Type": "application/json"},
                json={
                    "instances": [{"prompt": prompt}],
                    "parameters": {
                        "sampleCount": 1,
                        "aspectRatio": aspect,
                    }
                }
            )
            response.raise_for_status()
            data = response.json()
    except httpx.HTTPStatusError as e:
        error_msg = str(e)
        try:
            error_msg = e.response.json().get("error", {}).get("message", str(e))
        except Exception:
            pass
        return GenerationResult(success=False, error=f"Google API error: {error_msg}")
    except Exception as e:
        return GenerationResult(success=False, error=str(e))
    
    # Imagen 4 returns predictions[].bytesBase64Encoded
    if "predictions" in data and data["predictions"]:
        image_b64 = data["predictions"][0].get("bytesBase64Encoded")
        if image_b64:
            return GenerationResult(
                success=True,
                image_data=base64.b64decode(image_b64),
                prompt=prompt,
                metadata={"provider": "google", "model": model}
            )
    
    return GenerationResult(success=False, error="No image data in response")


def _gen_stability(prompt: str, model: str, size: str) -> GenerationResult:
    """Generate with Stability AI."""
    try:
        import httpx
    except ImportError:
        return GenerationResult(success=False, error="httpx not installed")
    
    api_key = os.environ.get("STABILITY_API_KEY")
    width, height = map(int, size.split("x"))
    
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3" if model.startswith("sd3") else "https://api.stability.ai/v2beta/stable-image/generate/core"
    
    try:
        with httpx.Client(timeout=120.0) as client:
            response = client.post(
                url,
                headers={"Authorization": f"Bearer {api_key}", "Accept": "image/*"},
                files={
                    "prompt": (None, prompt),
                    "output_format": (None, "png"),
                    "aspect_ratio": (None, "1:1" if width == height else f"{width}:{height}"),
                }
            )
            response.raise_for_status()
            
            if response.headers.get("content-type", "").startswith("image/"):
                return GenerationResult(
                    success=True,
                    image_data=response.content,
                    prompt=prompt,
                    metadata={"provider": "stability", "model": model}
                )
    except Exception as e:
        return GenerationResult(success=False, error=str(e))
    
    return GenerationResult(success=False, error="No image data")


def _gen_replicate(prompt: str, model: str, size: str) -> GenerationResult:
    """Generate with Replicate."""
    try:
        import httpx
    except ImportError:
        return GenerationResult(success=False, error="httpx not installed")
    
    api_token = os.environ.get("REPLICATE_API_TOKEN")
    width, height = map(int, size.split("x"))
    
    payload = {
        "input": {
            "prompt": prompt,
            "width": width,
            "height": height,
            "num_outputs": 1,
        }
    }
    
    if "/" in model:
        payload["model"] = model
    else:
        payload["version"] = model
    
    payload = {k: v for k, v in payload.items() if v is not None}
    
    try:
        with httpx.Client(timeout=300.0) as client:
            response = client.post(
                "https://api.replicate.com/v1/predictions",
                headers={
                    "Authorization": f"Bearer {api_token}",
                    "Content-Type": "application/json",
                    "Prefer": "wait",
                },
                json=payload
            )
            response.raise_for_status()
            data = response.json()
            
            if data.get("status") == "succeeded" and data.get("output"):
                output = data["output"]
                image_url = output[0] if isinstance(output, list) else output
                
                img_response = client.get(image_url)
                img_response.raise_for_status()
                
                return GenerationResult(
                    success=True,
                    image_data=img_response.content,
                    prompt=prompt,
                    metadata={"provider": "replicate", "model": model}
                )
    except Exception as e:
        return GenerationResult(success=False, error=str(e))
    
    return GenerationResult(success=False, error="Generation failed")


# === COMMAND IMPLEMENTATIONS ===

def _cmd_providers():
    """List available providers."""
    print("Image Generation Providers:\n")
    for p in ImageProvider:
        key = _get_api_key(p, IMAGE_ENV_KEYS)
        status = "✓" if key else "✗"
        env = IMAGE_ENV_KEYS[p]
        model = DEFAULT_IMAGE_MODELS[p]
        if key:
            print(f"  {status} {p.value:12} ({model})")
        else:
            print(f"  {status} {p.value:12} (set {env})")
    
    print("\nLLM Providers (for prompt synthesis):\n")
    for p in LLMProvider:
        key = _get_api_key(p, LLM_ENV_KEYS)
        status = "✓" if key else "✗"
        env = LLM_ENV_KEYS[p]
        model = DEFAULT_LLM_MODELS[p]
        if key:
            print(f"  {status} {p.value:12} ({model})")
        else:
            print(f"  {status} {p.value:12} (set {env})")


def _cmd_compose(args):
    """Compose context and output prompt."""
    if not args.files:
        print("Error: No input files specified", file=sys.stderr)
        sys.exit(1)
    
    context = _read_context_files(args.files)
    
    if not context.sources:
        print("Error: No valid context found in input files", file=sys.stderr)
        sys.exit(1)
    
    if args.raw:
        # Just output merged context
        try:
            import yaml
            print(yaml.dump(context.merge(), default_flow_style=False, allow_unicode=True))
        except ImportError:
            print(json.dumps(context.merge(), indent=2))
    else:
        # Synthesize via LLM
        llm_provider = _select_llm_provider(args.llm)
        verbosity = Verbosity(getattr(args, 'verbosity', Verbosity.NORMAL.value))
        prompt = _synthesize_prompt(context, args.style, llm_provider, verbosity)
        print(prompt)


def _cmd_generate(args):
    """Compose context and generate image."""
    if not args.files:
        print("Error: No input files specified", file=sys.stderr)
        print("Usage: visualize.py FILE1 [FILE2 ...] --provider PROVIDER", file=sys.stderr)
        sys.exit(1)
    
    # Read context
    context = _read_context_files(args.files)
    
    if not context.sources and not args.raw_prompt:
        print("Error: No valid context found in input files", file=sys.stderr)
        sys.exit(1)
    
    # Get prompt
    if args.raw_prompt:
        prompt = args.raw_prompt
        _debug(f"Using raw prompt: {prompt[:50]}...")
    else:
        llm_provider = _select_llm_provider(getattr(args, 'llm', None))
        verbosity = Verbosity(getattr(args, 'verbosity', Verbosity.NORMAL.value))
        print(f"Synthesizing prompt via {llm_provider.value} (verbosity: {verbosity.value})...", file=sys.stderr)
        prompt = _synthesize_prompt(context, args.style, llm_provider, verbosity)
        print(f"\n📝 Prompt:\n{prompt}\n", file=sys.stderr)
    
    if args.prompt_only:
        print(prompt)
        return
    
    # Generate image
    image_provider = _select_image_provider(args.provider)
    model = args.model or DEFAULT_IMAGE_MODELS[image_provider]
    
    print(f"Generating with {image_provider.value}/{model}...", file=sys.stderr)
    
    result = _generate_image(prompt, image_provider, model, args.size)
    
    if not result.success:
        print(f"Error: {result.error}", file=sys.stderr)
        sys.exit(1)
    
    # Save image using bigendian naming convention
    # Pattern: {source-dir}/{source-base}-{timestamp}-{description}.png
    description = getattr(args, 'description', None)
    output_path = _compute_output_path(
        source_files=args.files,
        description=description,
        suffix=".png",
        explicit_output=args.output
    )
    
    with open(output_path, "wb") as f:
        f.write(result.image_data)
    
    print(f"✓ Saved: {output_path}")
    
    # Handle multiple images (-n)
    count = getattr(args, 'count', 1) or 1
    if count > 1:
        for i in range(2, count + 1):
            print(f"\nGenerating {i}/{count}...", file=sys.stderr)
            result = _generate_image(prompt, image_provider, model, args.size)
            if result.success:
                suffix = f"-{i:02d}.png"
                multi_path = output_path.with_stem(output_path.stem + f"-{i:02d}")
                with open(multi_path, "wb") as f:
                    f.write(result.image_data)
                print(f"✓ Saved: {multi_path}")
            else:
                print(f"✗ Failed: {result.error}", file=sys.stderr)


def _cmd_matrix(args):
    """Generate matrix of variations (cartesian product)."""
    import itertools
    
    # Parse --vary arguments: KEY=VAL1,VAL2,VAL3
    variations = {}
    for vary_arg in args.vary:
        if "=" not in vary_arg:
            print(f"Error: Invalid --vary format: {vary_arg}", file=sys.stderr)
            print("Expected: KEY=VAL1,VAL2,VAL3", file=sys.stderr)
            sys.exit(1)
        key, values = vary_arg.split("=", 1)
        variations[key] = [v.strip() for v in values.split(",")]
    
    # Calculate cartesian product
    keys = list(variations.keys())
    value_lists = [variations[k] for k in keys]
    combinations = list(itertools.product(*value_lists))
    
    print(f"Matrix: {len(combinations)} combinations", file=sys.stderr)
    for key, vals in variations.items():
        print(f"  {key}: {vals}", file=sys.stderr)
    print(file=sys.stderr)
    
    if args.dry_run:
        print("Combinations (dry run):")
        for i, combo in enumerate(combinations, 1):
            combo_dict = dict(zip(keys, combo))
            print(f"  {i}. {combo_dict}")
        return
    
    # Read base context
    context = _read_context_files(args.files) if args.files else Context()
    
    # Generate each combination
    image_provider = _select_image_provider(args.provider)
    llm_provider = _select_llm_provider(args.llm)
    model = DEFAULT_IMAGE_MODELS[image_provider]
    
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    for i, combo in enumerate(combinations, 1):
        combo_dict = dict(zip(keys, combo))
        
        # Merge combo into context
        merged = context.merge()
        for key, value in combo_dict.items():
            merged[key] = value
        
        combo_context = Context(sources=[merged])
        
        # Generate filename from combo
        combo_slug = "-".join(f"{k}_{v}" for k, v in combo_dict.items())
        
        print(f"[{i}/{len(combinations)}] {combo_dict}", file=sys.stderr)
        
        # Synthesize and generate
        verbosity = Verbosity(getattr(args, 'verbosity', Verbosity.NORMAL.value))
        prompt = _synthesize_prompt(combo_context, args.style, llm_provider, verbosity)
        result = _generate_image(prompt, image_provider, model, DEFAULT_SIZE)
        
        if result.success:
            output_path = args.output_dir / f"{combo_slug}.png"
            with open(output_path, "wb") as f:
                f.write(result.image_data)
            print(f"  ✓ {output_path.name}")
        else:
            print(f"  ✗ {result.error}", file=sys.stderr)
    
    print(f"\n✓ Generated {len(combinations)} images in {args.output_dir}")


def _cmd_batch(args):
    """Batch generate from directory of context sets."""
    import glob
    
    source = Path(args.source)
    
    # Find context sets
    if source.is_dir():
        # Each subdirectory is a context set
        context_dirs = [d for d in source.iterdir() if d.is_dir()]
        if not context_dirs:
            # Or find all YAML files
            context_files = list(source.glob("*.yml")) + list(source.glob("*.yaml"))
            if context_files:
                context_dirs = [source]  # Treat as single context set
    else:
        # Treat as glob pattern
        context_files = list(glob.glob(str(source)))
        if context_files:
            context_dirs = [Path(f).parent for f in context_files]
            context_dirs = list(set(context_dirs))
        else:
            print(f"Error: No matches for {source}", file=sys.stderr)
            sys.exit(1)
    
    if not context_dirs:
        print(f"Error: No context sets found in {source}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found {len(context_dirs)} context sets", file=sys.stderr)
    
    image_provider = _select_image_provider(args.provider)
    llm_provider = _select_llm_provider(args.llm)
    model = DEFAULT_IMAGE_MODELS[image_provider]
    
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    for i, ctx_dir in enumerate(context_dirs, 1):
        # Find all YAML files in this context set
        yaml_files = list(ctx_dir.glob("*.yml")) + list(ctx_dir.glob("*.yaml"))
        
        if not yaml_files:
            print(f"[{i}/{len(context_dirs)}] {ctx_dir.name}: no YAML files, skipping")
            continue
        
        print(f"[{i}/{len(context_dirs)}] {ctx_dir.name} ({len(yaml_files)} files)", file=sys.stderr)
        
        # Read context
        context = _read_context_files([str(f) for f in yaml_files])
        
        if not context.sources:
            print(f"  ⚠ No valid context")
            continue
        
        # Generate
        verbosity = Verbosity(getattr(args, 'verbosity', Verbosity.NORMAL.value))
        prompt = _synthesize_prompt(context, None, llm_provider, verbosity)
        result = _generate_image(prompt, image_provider, model, DEFAULT_SIZE)
        
        if result.success:
            output_path = args.output_dir / f"{ctx_dir.name}.png"
            with open(output_path, "wb") as f:
                f.write(result.image_data)
            print(f"  ✓ {output_path.name}")
            success_count += 1
        else:
            print(f"  ✗ {result.error}", file=sys.stderr)
    
    print(f"\n✓ Generated {success_count}/{len(context_dirs)} images")


def _cmd_regenerate(args):
    """Regenerate image from a sidecar YAML file.
    
    The sidecar contains:
    - sources: list of original context file paths
    - generation: provider, model, size, verbosity, llm
    - prompt: the synthesized prompt text
    
    Two modes:
    1. Use prompt directly (default): ignore sources, use prompt as-is
    2. Re-synthesize (--use-sources): re-read source files and synthesize new prompt
    """
    sidecar_path = args.sidecar
    
    if not sidecar_path.exists():
        print(f"Error: sidecar not found: {sidecar_path}", file=sys.stderr)
        sys.exit(1)
    
    # Parse sidecar
    with open(sidecar_path) as f:
        sidecar = yaml.safe_load(f)
    
    if not sidecar:
        print(f"Error: empty or invalid sidecar: {sidecar_path}", file=sys.stderr)
        sys.exit(1)
    
    # Extract parameters (with CLI overrides)
    gen = sidecar.get("generation", {})
    
    provider_name = args.provider or gen.get("provider", "openai")
    model = args.model or gen.get("model")
    size = args.size or gen.get("size", DEFAULT_SIZE)
    verbosity_str = args.verbosity or gen.get("verbosity", "normal")
    llm_name = args.llm or gen.get("llm")
    
    try:
        image_provider = ImageProvider(provider_name)
    except ValueError:
        print(f"Error: unknown provider: {provider_name}", file=sys.stderr)
        sys.exit(1)
    
    if not model:
        model = DEFAULT_IMAGE_MODELS[image_provider]
    
    # Get prompt (either from sidecar or re-synthesize)
    if args.use_sources:
        # Re-synthesize from source files
        sources = sidecar.get("sources", [])
        if not sources:
            print("Error: --use-sources but no sources in sidecar", file=sys.stderr)
            sys.exit(1)
        
        # Check source files exist
        missing = [s for s in sources if not Path(s).exists()]
        if missing:
            print(f"Error: source files not found: {missing}", file=sys.stderr)
            sys.exit(1)
        
        print(f"Re-synthesizing from {len(sources)} sources...", file=sys.stderr)
        
        context = _read_context_files(sources)
        llm_provider = _select_llm_provider(llm_name)
        verbosity = Verbosity(verbosity_str)
        prompt = _synthesize_prompt(context, None, llm_provider, verbosity)
    else:
        # Use prompt from sidecar
        prompt = sidecar.get("prompt", "")
        if not prompt:
            print("Error: no prompt in sidecar (use --use-sources to re-synthesize)", file=sys.stderr)
            sys.exit(1)
        
        # Handle YAML block scalar (may have trailing newlines)
        prompt = prompt.strip()
    
    # Generate
    print(f"\n📝 Prompt (first 200 chars): {prompt[:200]}...", file=sys.stderr)
    print(f"\nGenerating with {image_provider.value}/{model}...", file=sys.stderr)
    
    result = _generate_image(prompt, image_provider, model, size)
    
    if not result.success:
        print(f"Error: {result.error}", file=sys.stderr)
        sys.exit(1)
    
    # Output path
    if args.output:
        output_path = args.output
    else:
        # New timestamped file in same directory as sidecar
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        stem = sidecar_path.stem
        # Remove old timestamp if present (YYYY-MM-DD-HH-MM-SS pattern)
        import re
        stem = re.sub(r'^\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}-?', '', stem)
        if stem:
            output_path = sidecar_path.parent / f"{timestamp}-{stem}.png"
        else:
            output_path = sidecar_path.parent / f"{timestamp}-regenerated.png"
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "wb") as f:
        f.write(result.image_data)
    
    print(f"✓ Saved: {output_path}")
    
    # Write new sidecar
    sources = sidecar.get("sources", [])
    _write_sidecar(
        output_path=output_path,
        prompt=prompt,
        sources=sources,
        provider=image_provider.value,
        model=model,
        size=size,
        verbosity=verbosity_str,
        llm_provider=llm_name,
        extra={"regenerated_from": str(sidecar_path)}
    )


# === MAIN ===

if __name__ == "__main__":
    main()
