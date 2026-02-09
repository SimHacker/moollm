#!/usr/bin/env python3
"""
exif.py — EXIF Metadata Layer for Image Mining
Sister script to mine.py — handles the Fourth Eye (embedded metadata)

💬 "EXIF is the canonical truth. No database needed."
   — Jaisen Mathai (2026, immich-exif)

The image IS the database.

Usage:
    python exif.py read image.jpg
    python exif.py read image.jpg --field GPS
    python exif.py write image.jpg --field Description --value "Amsterdam sunset"
    python exif.py inject image.jpg --from mining.yml
    python exif.py extract image.jpg --to metadata.yml
    python exif.py sync image.jpg --with mining.yml
    python exif.py strip image.jpg --keep GPS DateTime
    python exif.py batch /photos --inject-from /mining

Dependencies:
    - exiftool (required) — https://exiftool.org
    - PyYAML (for YAML Jazz output)
    
Optional:
    - piexif (pure Python fallback)
    - Pillow (for image manipulation)

Install exiftool:
    macOS: brew install exiftool
    Ubuntu: apt install libimage-exiftool-perl
    Windows: download from exiftool.org
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Optional, Any

try:
    import yaml
except ImportError:
    yaml = None

# MOOLLM custom namespace for XMP
MOOLLM_NAMESPACE = "http://moollm.org/ns/1.0/"

# Standard EXIF field categories
FIELD_CATEGORIES = {
    "camera": [
        "Make", "Model", "LensModel", "FocalLength",
        "FNumber", "ExposureTime", "ISO", "Flash"
    ],
    "datetime": [
        "DateTimeOriginal", "CreateDate", "ModifyDate", "TimeZone"
    ],
    "gps": [
        "GPSLatitude", "GPSLongitude", "GPSAltitude",
        "GPSSpeed", "GPSDirection"
    ],
    "descriptive": [
        "Title", "Description", "Subject", "Keywords", "Comment"
    ],
    "organizational": [
        "Album", "Rating", "Label"
    ],
    "people": [
        "PersonInImage", "FaceRegions"
    ],
    "rights": [
        "Copyright", "Creator", "Rights", "License"
    ],
    "moollm": [
        "MiningPass", "ThirdEyeNotes", "YAMLJazzRef",
        "CharacterDetected", "ResourcesExtracted", "Facets", "Perspective"
    ]
}


def check_exiftool() -> bool:
    """Check if exiftool is available."""
    try:
        subprocess.run(
            ["exiftool", "-ver"],
            capture_output=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def run_exiftool(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """Run exiftool with given arguments."""
    cmd = ["exiftool"] + args
    return subprocess.run(cmd, capture_output=True, text=True, check=check)


def read_exif(image_path: str, field: Optional[str] = None, output_format: str = "yaml") -> dict:
    """
    Read EXIF metadata from image.
    
    Args:
        image_path: Path to image file
        field: Specific field or category to read (optional)
        output_format: "yaml" or "json"
    
    Returns:
        Dictionary of EXIF data
    """
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    args = ["-j", "-G"]  # JSON output, grouped by tag family
    
    if field:
        # Check if field is a category
        if field.lower() in FIELD_CATEGORIES:
            for f in FIELD_CATEGORIES[field.lower()]:
                args.extend([f"-{f}"])
        else:
            args.append(f"-{field}")
    
    args.append(image_path)
    
    result = run_exiftool(args)
    data = json.loads(result.stdout)
    
    if data:
        return data[0]
    return {}


def write_exif(image_path: str, field: str, value: str, overwrite: bool = True) -> bool:
    """
    Write a single EXIF field to image.
    
    Args:
        image_path: Path to image file
        field: EXIF field name
        value: Value to write
        overwrite: If True, overwrite original (default)
    
    Returns:
        True if successful
    """
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    args = [f"-{field}={value}"]
    if overwrite:
        args.append("-overwrite_original")
    args.append(image_path)
    
    result = run_exiftool(args, check=False)
    return result.returncode == 0


def inject_from_yaml(image_path: str, yaml_path: str, overwrite: bool = True) -> bool:
    """
    Bulk inject metadata from YAML file into image.
    
    YAML format:
        Description: "Amsterdam sunset"
        Keywords: ["travel", "netherlands", "sunset"]
        GPSLatitude: 52.37
        GPSLongitude: 4.89
        moollm:
            MiningPass: "2024-01-30-001"
            ThirdEyeNotes: "Golden hour, reflections on canal"
    
    Args:
        image_path: Path to image file
        yaml_path: Path to YAML file with metadata
        overwrite: If True, overwrite original
    
    Returns:
        True if successful
    """
    if yaml is None:
        raise ImportError("PyYAML required for inject. Install with: pip install pyyaml")
    
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    if not Path(yaml_path).exists():
        raise FileNotFoundError(f"YAML not found: {yaml_path}")
    
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    
    args = []
    
    def add_field(key: str, val: Any, prefix: str = ""):
        """Recursively add fields."""
        if isinstance(val, dict):
            for k, v in val.items():
                add_field(k, v, prefix=key)
        elif isinstance(val, list):
            # Keywords and similar list fields
            for item in val:
                args.append(f"-{key}={item}")
        else:
            field_name = f"{prefix}:{key}" if prefix else key
            args.append(f"-{field_name}={val}")
    
    for key, val in data.items():
        add_field(key, val)
    
    if overwrite:
        args.append("-overwrite_original")
    args.append(image_path)
    
    result = run_exiftool(args, check=False)
    return result.returncode == 0


def extract_to_yaml(image_path: str, yaml_path: str, categories: Optional[list[str]] = None) -> dict:
    """
    Extract all EXIF to YAML file.
    
    Args:
        image_path: Path to image file
        yaml_path: Path to output YAML file
        categories: Optional list of categories to extract
    
    Returns:
        Extracted data dictionary
    """
    if yaml is None:
        raise ImportError("PyYAML required for extract. Install with: pip install pyyaml")
    
    data = read_exif(image_path)
    
    # Organize into categories if requested
    if categories:
        organized = {}
        for cat in categories:
            if cat.lower() in FIELD_CATEGORIES:
                organized[cat] = {}
                for field in FIELD_CATEGORIES[cat.lower()]:
                    for key, val in data.items():
                        if field in key:
                            organized[cat][field] = val
        data = organized
    
    with open(yaml_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    
    return data


def strip_exif(image_path: str, keep: Optional[list[str]] = None, overwrite: bool = True) -> bool:
    """
    Strip EXIF metadata from image (privacy protection).
    
    Args:
        image_path: Path to image file
        keep: Optional list of fields to preserve
        overwrite: If True, overwrite original
    
    Returns:
        True if successful
    """
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    if keep:
        # Strip all, then restore kept fields
        data = read_exif(image_path)
        kept_data = {}
        for field in keep:
            for key, val in data.items():
                if field.lower() in key.lower():
                    kept_data[key] = val
        
        args = ["-all="]
        if overwrite:
            args.append("-overwrite_original")
        args.append(image_path)
        run_exiftool(args)
        
        # Restore kept fields
        for key, val in kept_data.items():
            # Extract just the field name
            field_name = key.split(":")[-1] if ":" in key else key
            write_exif(image_path, field_name, str(val), overwrite=True)
        
        return True
    else:
        args = ["-all="]
        if overwrite:
            args.append("-overwrite_original")
        args.append(image_path)
        result = run_exiftool(args, check=False)
        return result.returncode == 0


def copy_exif(source_path: str, target_path: str, overwrite: bool = True) -> bool:
    """
    Copy EXIF metadata from source to target image.
    
    Args:
        source_path: Path to source image
        target_path: Path to target image
        overwrite: If True, overwrite original target
    
    Returns:
        True if successful
    """
    if not Path(source_path).exists():
        raise FileNotFoundError(f"Source not found: {source_path}")
    if not Path(target_path).exists():
        raise FileNotFoundError(f"Target not found: {target_path}")
    
    args = ["-TagsFromFile", source_path]
    if overwrite:
        args.append("-overwrite_original")
    args.append(target_path)
    
    result = run_exiftool(args, check=False)
    return result.returncode == 0


def diff_exif(image1_path: str, image2_path: str) -> dict:
    """
    Compare EXIF between two images.
    
    Returns:
        Dictionary with 'only_in_1', 'only_in_2', 'different', 'same'
    """
    data1 = read_exif(image1_path)
    data2 = read_exif(image2_path)
    
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    
    result = {
        "only_in_1": {k: data1[k] for k in keys1 - keys2},
        "only_in_2": {k: data2[k] for k in keys2 - keys1},
        "different": {},
        "same": {}
    }
    
    for key in keys1 & keys2:
        if data1[key] != data2[key]:
            result["different"][key] = {
                "image1": data1[key],
                "image2": data2[key]
            }
        else:
            result["same"][key] = data1[key]
    
    return result


# SIDECAR FUNCTIONS — The -exif.yml Convention

def get_sidecar_path(image_path: str) -> Path:
    """Get the -exif.yml sidecar path for an image."""
    p = Path(image_path)
    return p.parent / f"{p.stem}-exif.yml"


def create_sidecar(image_path: str, include_mining: bool = True) -> dict:
    """
    Create a -exif.yml sidecar for an image.
    
    Schema:
        exif: Standard camera/GPS/datetime metadata
        mining: YAML Jazz from Three Eyes (empty template)
        prompts: Generation prompts (empty for photos)
        jazz: Arbitrary custom metadata (empty template)
    
    Args:
        image_path: Path to image file
        include_mining: Include mining template section
    
    Returns:
        Sidecar data dictionary
    """
    if yaml is None:
        raise ImportError("PyYAML required for sidecar. Install with: pip install pyyaml")
    
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    # Read EXIF data
    raw_exif = read_exif(image_path)
    
    # Organize into categories
    exif_section = {
        "camera": {},
        "datetime": {},
        "gps": {},
        "descriptive": {}
    }
    
    # Map raw EXIF to categories
    for key, val in raw_exif.items():
        # Skip internal fields
        if key in ["SourceFile", "ExifTool:ExifToolVersion"]:
            continue
        
        # Extract field name (after colon if grouped)
        field_name = key.split(":")[-1] if ":" in key else key
        
        # Categorize
        if field_name in FIELD_CATEGORIES["camera"]:
            exif_section["camera"][field_name] = val
        elif field_name in FIELD_CATEGORIES["datetime"]:
            exif_section["datetime"][field_name] = val
        elif field_name in FIELD_CATEGORIES["gps"]:
            exif_section["gps"][field_name] = val
        elif field_name in FIELD_CATEGORIES["descriptive"]:
            exif_section["descriptive"][field_name] = val
    
    # Build sidecar structure
    from datetime import datetime
    
    sidecar = {
        "_meta": {
            "source_image": Path(image_path).name,
            "sidecar_version": "1.0",
            "created": datetime.now().isoformat(),
            "last_sync": datetime.now().isoformat()
        },
        
        # Section 1: Standard EXIF
        "exif": exif_section,
        
        # Section 2: Mining data (YAML Jazz from Three Eyes)
        "mining": {
            "resources": {},
            "observations": {
                "left_eye": None,   # Structure
                "right_eye": None,  # Narrative
                "third_eye": None   # Meaning
            },
            "characters": [],
            "facets": [],
            "passes": []
        } if include_mining else None,
        
        # Section 3: Prompts (for AI-generated images)
        "prompts": {
            "generated": False,
            "model": None,
            "prompt": None,
            "negative_prompt": None,
            "seed": None,
            "variations": [],
            "inpaint": []
        },
        
        # Section 4: Jazz (arbitrary custom metadata)
        "jazz": {
            "project": {
                "album": None,
                "collection": None,
                "series": None,
                "sequence": None
            },
            "ratings": {
                "technical_quality": None,
                "emotional_impact": None,
                "favorite": False,
                "portfolio_candidate": False
            },
            "stories": {
                "story": None,
                "mood_when_taken": None,
                "who_was_there": []
            },
            "workflow": {
                "edited_in": None,
                "edit_notes": None,
                "versions": []
            },
            "links": {
                "related_images": [],
                "source_raw": None,
                "moollm_room": None
            }
        }
    }
    
    # Write sidecar file
    sidecar_path = get_sidecar_path(image_path)
    with open(sidecar_path, 'w') as f:
        # Add header comment
        f.write(f"# {sidecar_path.name}\n")
        f.write(f"# Sidecar for: {Path(image_path).name}\n")
        f.write(f"# Generated: {datetime.now().isoformat()}\n")
        f.write("#\n")
        f.write("# Sections: exif | mining | prompts | jazz\n")
        f.write("# grep -r 'keyword' *-exif.yml to search\n")
        f.write("#\n\n")
        yaml.dump(sidecar, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    return sidecar


def inject_sidecar(image_path: str, overwrite: bool = True) -> bool:
    """
    Inject -exif.yml sidecar back into image EXIF.
    
    Only injects the 'exif' section (camera, datetime, gps, descriptive).
    Mining, prompts, and jazz stay in sidecar only (too complex for EXIF).
    
    Args:
        image_path: Path to image file
        overwrite: If True, overwrite original
    
    Returns:
        True if successful
    """
    if yaml is None:
        raise ImportError("PyYAML required for sidecar. Install with: pip install pyyaml")
    
    sidecar_path = get_sidecar_path(image_path)
    if not sidecar_path.exists():
        raise FileNotFoundError(f"Sidecar not found: {sidecar_path}")
    
    with open(sidecar_path, 'r') as f:
        sidecar = yaml.safe_load(f)
    
    if not sidecar or "exif" not in sidecar:
        raise ValueError(f"Invalid sidecar format: {sidecar_path}")
    
    # Build exiftool args from exif section
    args = []
    
    for category, fields in sidecar["exif"].items():
        if isinstance(fields, dict):
            for field, value in fields.items():
                if value is not None:
                    args.append(f"-{field}={value}")
    
    if not args:
        return True  # Nothing to inject
    
    if overwrite:
        args.append("-overwrite_original")
    args.append(image_path)
    
    result = run_exiftool(args, check=False)
    
    # Update sidecar sync timestamp
    if result.returncode == 0:
        from datetime import datetime
        sidecar["_meta"]["last_sync"] = datetime.now().isoformat()
        with open(sidecar_path, 'w') as f:
            yaml.dump(sidecar, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    return result.returncode == 0


def batch_sidecars(directory: str, extensions: list[str] = None) -> list[str]:
    """
    Create sidecars for all images in directory.
    
    Args:
        directory: Path to directory
        extensions: Image extensions to process (default: common image types)
    
    Returns:
        List of created sidecar paths
    """
    if extensions is None:
        extensions = [".jpg", ".jpeg", ".png", ".heic", ".webp", ".tiff", ".gif"]
    
    dir_path = Path(directory)
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")
    
    created = []
    for ext in extensions:
        for image_path in dir_path.glob(f"*{ext}"):
            sidecar_path = get_sidecar_path(str(image_path))
            if not sidecar_path.exists():
                try:
                    create_sidecar(str(image_path))
                    created.append(str(sidecar_path))
                except Exception as e:
                    print(f"Warning: Failed to create sidecar for {image_path}: {e}")
        # Also check uppercase extensions
        for image_path in dir_path.glob(f"*{ext.upper()}"):
            sidecar_path = get_sidecar_path(str(image_path))
            if not sidecar_path.exists():
                try:
                    create_sidecar(str(image_path))
                    created.append(str(sidecar_path))
                except Exception as e:
                    print(f"Warning: Failed to create sidecar for {image_path}: {e}")
    
    return created


def index_sidecars(directory: str, output_path: str = None) -> dict:
    """
    Create searchable index of all sidecars in directory.
    
    Args:
        directory: Path to directory
        output_path: Path to output INDEX.yml (optional)
    
    Returns:
        Index dictionary
    """
    if yaml is None:
        raise ImportError("PyYAML required for index. Install with: pip install pyyaml")
    
    dir_path = Path(directory)
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")
    
    from datetime import datetime
    
    index = {
        "_meta": {
            "directory": str(dir_path.absolute()),
            "indexed_at": datetime.now().isoformat(),
            "image_count": 0,
            "has_gps": 0,
            "has_mining": 0,
            "favorites": 0
        },
        "images": []
    }
    
    for sidecar_path in dir_path.glob("*-exif.yml"):
        try:
            with open(sidecar_path, 'r') as f:
                sidecar = yaml.safe_load(f)
            
            if not sidecar:
                continue
            
            # Extract summary
            summary = {
                "image": sidecar.get("_meta", {}).get("source_image"),
                "sidecar": sidecar_path.name
            }
            
            # EXIF summary
            exif = sidecar.get("exif", {})
            if exif.get("datetime", {}).get("DateTimeOriginal"):
                summary["date"] = exif["datetime"]["DateTimeOriginal"]
            if exif.get("gps", {}).get("GPSLatitude"):
                summary["gps"] = True
                index["_meta"]["has_gps"] += 1
            if exif.get("descriptive", {}).get("Keywords"):
                summary["keywords"] = exif["descriptive"]["Keywords"]
            
            # Mining summary
            mining = sidecar.get("mining", {})
            if mining and mining.get("passes"):
                summary["mined"] = True
                index["_meta"]["has_mining"] += 1
            
            # Jazz summary
            jazz = sidecar.get("jazz", {})
            if jazz.get("ratings", {}).get("favorite"):
                summary["favorite"] = True
                index["_meta"]["favorites"] += 1
            if jazz.get("project", {}).get("album"):
                summary["album"] = jazz["project"]["album"]
            
            index["images"].append(summary)
            index["_meta"]["image_count"] += 1
            
        except Exception as e:
            print(f"Warning: Failed to index {sidecar_path}: {e}")
    
    # Write index if output path specified
    if output_path:
        with open(output_path, 'w') as f:
            f.write(f"# IMAGE INDEX — {dir_path.name}\n")
            f.write(f"# Generated: {datetime.now().isoformat()}\n")
            f.write(f"# Images: {index['_meta']['image_count']}\n")
            f.write("#\n\n")
            yaml.dump(index, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    return index


def format_output(data: Any, format: str = "yaml") -> str:
    """Format data for output."""
    if format == "json":
        return json.dumps(data, indent=2, ensure_ascii=False)
    elif format == "yaml" and yaml:
        return yaml.dump(data, default_flow_style=False, allow_unicode=True)
    else:
        return json.dumps(data, indent=2, ensure_ascii=False)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="EXIF Metadata Layer — The Fourth Eye",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Read all metadata
    python exif.py read sunset.jpg
    
    # Read GPS data only
    python exif.py read sunset.jpg --field GPS
    
    # Write description
    python exif.py write sunset.jpg --field Description --value "Amsterdam sunset"
    
    # Inject from YAML
    python exif.py inject sunset.jpg --from mining.yml
    
    # Extract to YAML
    python exif.py extract sunset.jpg --to metadata.yml
    
    # Strip metadata (keep GPS and DateTime)
    python exif.py strip sunset.jpg --keep GPS DateTime
    
    # Compare two images
    python exif.py diff image1.jpg image2.jpg
    
    # SIDECAR COMMANDS (foo.jpg → foo-exif.yml)
    
    # Create sidecar for image
    python exif.py sidecar sunset.jpg → sunset-exif.yml
    
    # Inject sidecar back into image
    python exif.py inject-sidecar sunset.jpg ← sunset-exif.yml
    
    # Batch create sidecars for directory
    python exif.py batch ./photos → *.jpg → *-exif.yml
    
    # Create searchable index
    python exif.py index ./photos --to INDEX.yml

💬 "The image IS the database."
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # read command
    read_parser = subparsers.add_parser("read", help="Read EXIF metadata")
    read_parser.add_argument("image", help="Image file path")
    read_parser.add_argument("--field", "-f", help="Specific field or category")
    read_parser.add_argument("--format", choices=["yaml", "json"], default="yaml")
    
    # write command
    write_parser = subparsers.add_parser("write", help="Write EXIF field")
    write_parser.add_argument("image", help="Image file path")
    write_parser.add_argument("--field", "-f", required=True, help="Field name")
    write_parser.add_argument("--value", "-v", required=True, help="Value to write")
    write_parser.add_argument("--no-backup", action="store_true", help="Overwrite original")
    
    # inject command
    inject_parser = subparsers.add_parser("inject", help="Inject metadata from YAML")
    inject_parser.add_argument("image", help="Image file path")
    inject_parser.add_argument("--from", dest="yaml_file", required=True, help="YAML file")
    inject_parser.add_argument("--no-backup", action="store_true")
    
    # extract command
    extract_parser = subparsers.add_parser("extract", help="Extract metadata to YAML")
    extract_parser.add_argument("image", help="Image file path")
    extract_parser.add_argument("--to", dest="yaml_file", required=True, help="Output YAML file")
    extract_parser.add_argument("--categories", nargs="+", help="Categories to extract")
    
    # strip command
    strip_parser = subparsers.add_parser("strip", help="Strip metadata (privacy)")
    strip_parser.add_argument("image", help="Image file path")
    strip_parser.add_argument("--keep", nargs="+", help="Fields to preserve")
    strip_parser.add_argument("--no-backup", action="store_true")
    
    # copy command
    copy_parser = subparsers.add_parser("copy", help="Copy metadata between images")
    copy_parser.add_argument("--from", dest="source", required=True, help="Source image")
    copy_parser.add_argument("--to", dest="target", required=True, help="Target image")
    copy_parser.add_argument("--no-backup", action="store_true")
    
    # diff command
    diff_parser = subparsers.add_parser("diff", help="Compare metadata")
    diff_parser.add_argument("image1", help="First image")
    diff_parser.add_argument("image2", help="Second image")
    diff_parser.add_argument("--format", choices=["yaml", "json"], default="yaml")
    
    # categories command
    subparsers.add_parser("categories", help="List field categories")
    
    # SIDECAR COMMANDS — The -exif.yml Convention
    
    # sidecar command
    sidecar_parser = subparsers.add_parser("sidecar", help="Create -exif.yml sidecar")
    sidecar_parser.add_argument("image", help="Image file path")
    sidecar_parser.add_argument("--no-mining", action="store_true", help="Skip mining template")
    
    # inject-sidecar command
    inject_sidecar_parser = subparsers.add_parser("inject-sidecar", help="Inject sidecar into image")
    inject_sidecar_parser.add_argument("image", help="Image file path")
    inject_sidecar_parser.add_argument("--no-backup", action="store_true")
    
    # batch command
    batch_parser = subparsers.add_parser("batch", help="Batch create sidecars")
    batch_parser.add_argument("directory", help="Directory path")
    batch_parser.add_argument("--extensions", nargs="+", help="Image extensions")
    
    # index command
    index_parser = subparsers.add_parser("index", help="Create searchable index")
    index_parser.add_argument("directory", help="Directory path")
    index_parser.add_argument("--to", dest="output", help="Output INDEX.yml path")
    index_parser.add_argument("--format", choices=["yaml", "json"], default="yaml")
    
    args = parser.parse_args()
    
    # Check for exiftool (except for commands that don't need it)
    no_exiftool_commands = ["categories", "index"]
    if args.command not in no_exiftool_commands and not check_exiftool():
        print("Error: exiftool not found. Install it:", file=sys.stderr)
        print("  macOS: brew install exiftool", file=sys.stderr)
        print("  Ubuntu: apt install libimage-exiftool-perl", file=sys.stderr)
        sys.exit(1)
    
    try:
        if args.command == "read":
            data = read_exif(args.image, args.field)
            print(format_output(data, args.format))
            
        elif args.command == "write":
            success = write_exif(args.image, args.field, args.value, not args.no_backup)
            if success:
                print(f"✓ Wrote {args.field}={args.value} to {args.image}")
            else:
                print(f"✗ Failed to write to {args.image}", file=sys.stderr)
                sys.exit(1)
                
        elif args.command == "inject":
            success = inject_from_yaml(args.image, args.yaml_file, not args.no_backup)
            if success:
                print(f"✓ Injected metadata from {args.yaml_file} to {args.image}")
            else:
                print(f"✗ Failed to inject", file=sys.stderr)
                sys.exit(1)
                
        elif args.command == "extract":
            data = extract_to_yaml(args.image, args.yaml_file, args.categories)
            print(f"✓ Extracted metadata to {args.yaml_file}")
            print(f"  Fields: {len(data)}")
            
        elif args.command == "strip":
            success = strip_exif(args.image, args.keep, not args.no_backup)
            if success:
                kept = f" (kept: {', '.join(args.keep)})" if args.keep else ""
                print(f"✓ Stripped metadata from {args.image}{kept}")
            else:
                print(f"✗ Failed to strip", file=sys.stderr)
                sys.exit(1)
                
        elif args.command == "copy":
            success = copy_exif(args.source, args.target, not args.no_backup)
            if success:
                print(f"✓ Copied metadata from {args.source} to {args.target}")
            else:
                print(f"✗ Failed to copy", file=sys.stderr)
                sys.exit(1)
                
        elif args.command == "diff":
            diff = diff_exif(args.image1, args.image2)
            print(format_output(diff, args.format))
            
        elif args.command == "categories":
            print("EXIF Field Categories:")
            for cat, fields in FIELD_CATEGORIES.items():
                print(f"\n{cat}:")
                for field in fields:
                    print(f"  - {field}")
        
        # SIDECAR COMMAND HANDLERS
        
        elif args.command == "sidecar":
            sidecar = create_sidecar(args.image, not args.no_mining)
            sidecar_path = get_sidecar_path(args.image)
            print(f"✓ Created sidecar: {sidecar_path}")
            print(f"  Sections: exif | mining | prompts | jazz")
            print(f"  grep -r 'keyword' *-exif.yml to search")
            
        elif args.command == "inject-sidecar":
            success = inject_sidecar(args.image, not args.no_backup)
            sidecar_path = get_sidecar_path(args.image)
            if success:
                print(f"✓ Injected {sidecar_path} → {args.image}")
            else:
                print(f"✗ Failed to inject sidecar", file=sys.stderr)
                sys.exit(1)
                
        elif args.command == "batch":
            created = batch_sidecars(args.directory, args.extensions)
            print(f"✓ Created {len(created)} sidecars in {args.directory}")
            for path in created[:10]:  # Show first 10
                print(f"  {path}")
            if len(created) > 10:
                print(f"  ... and {len(created) - 10} more")
                
        elif args.command == "index":
            output = args.output or str(Path(args.directory) / "INDEX.yml")
            idx = index_sidecars(args.directory, output)
            print(f"✓ Indexed {idx['_meta']['image_count']} images")
            print(f"  Has GPS: {idx['_meta']['has_gps']}")
            print(f"  Has mining: {idx['_meta']['has_mining']}")
            print(f"  Favorites: {idx['_meta']['favorites']}")
            print(f"  Index: {output}")
                    
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ImportError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
