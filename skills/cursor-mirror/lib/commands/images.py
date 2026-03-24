# Image commands: images, image-path, image-info, image-gallery
# Extracted from cursor_mirror_old.py during Phase 2 refactoring.

from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import unquote

import yaml
import os

from ..db import open_db, decode_blob, get_item_table_value, get_reactive_storage
from ..paths import GLOBAL_DB, WORKSPACES_ROOT, BASE_DIR
from ..keys import SESSION_LIST_KEYS, COMPOSER_STATE_KEY, NOTABLE_GLOBAL_KEYS
from ..discovery import iter_workspace_paths, get_workspace_folder, folder_uri_to_path
from ..composers import get_workspace_composers, get_all_composers, get_bubble_counts, clear_caches
from ..bubbles import iter_bubbles, load_bubbles, get_bubble_text, has_content, extract_bubble_text, is_error, USER, ASSISTANT
from ..resolve import resolve_workspace, resolve_composer, resolve_composer_id
from ..format_util import format_ts, get_output_format, output_data, format_not_supported
from ..debug_util import debug
from ..sources import register_source


def iter_image_paths() -> Iterator[Tuple[Path, str, str]]:
    """Iterate all cached images across workspaces.
    
    Yields: (image_path, workspace_hash, workspace_folder)
    """
    for ws_path in iter_workspace_paths():
        img_dir = ws_path / "images"
        if img_dir.exists():
            ws_hash = ws_path.name
            ws_folder = get_workspace_folder(ws_path) or "unknown"
            for img in img_dir.iterdir():
                if img.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
                    yield img, ws_hash, ws_folder


def get_image_metadata(img_path: Path, ws_hash: str, ws_folder: str) -> Dict[str, Any]:
    """Get metadata for an image file."""
    stat = img_path.stat()
    return {
        "path": str(img_path),
        "filename": img_path.name,
        "uuid": img_path.stem.replace("image-", "").replace("Screenshot ", ""),
        "workspace": ws_folder.split("/")[-1] if ws_folder else "unknown",
        "workspace_hash": ws_hash,
        "size_kb": round(stat.st_size / 1024, 1),
        "size_bytes": stat.st_size,
        "modified": datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M'),
        "modified_ts": stat.st_mtime,
    }


def cmd_images(args):
    """List cached images from chat sessions."""
    images = []
    
    for img_path, ws_hash, ws_folder in iter_image_paths():
        meta = get_image_metadata(img_path, ws_hash, ws_folder)
        images.append(meta)
    
    # Sort
    if args.sort == "date":
        images.sort(key=lambda x: x["modified_ts"], reverse=True)
    elif args.sort == "size":
        images.sort(key=lambda x: x["size_bytes"], reverse=True)
    elif args.sort == "workspace":
        images.sort(key=lambda x: (x["workspace"], -x["modified_ts"]))
    
    # Limit
    if args.limit:
        images = images[:args.limit]
    
    if get_output_format(args) != "text":
        print(fmt(images, args))
    else:
        # Group by workspace
        by_ws: Dict[str, List[Dict]] = {}
        for img in images:
            ws = img["workspace"]
            if ws not in by_ws:
                by_ws[ws] = []
            by_ws[ws].append(img)
        
        print(f"Cached Images ({len(images)} total)")
        print("═" * 80)
        
        for ws, imgs in sorted(by_ws.items(), key=lambda x: -len(x[1])):
            total_kb = sum(i["size_kb"] for i in imgs)
            print(f"\n📁 {ws} ({len(imgs)} images, {total_kb:.1f} KB)")
            print("─" * 60)
            for img in imgs[:10]:  # Show first 10 per workspace
                print(f"  {img['modified']}  {img['size_kb']:>7.1f}KB  {img['uuid'][:8]}...")
            if len(imgs) > 10:
                print(f"  ... and {len(imgs) - 10} more")


def cmd_image_path(args):
    """Get full path to a cached image."""
    ref = args.ref.lower()
    
    for img_path, ws_hash, ws_folder in iter_image_paths():
        if ref in img_path.name.lower() or ref in str(img_path).lower():
            print(str(img_path))
            return
    
    raise NotFoundError(f"Image not found: {args.ref}")


def cmd_image_info(args):
    """Show metadata for a cached image."""
    ref = args.ref.lower()
    
    for img_path, ws_hash, ws_folder in iter_image_paths():
        if ref in img_path.name.lower() or ref in str(img_path).lower():
            meta = get_image_metadata(img_path, ws_hash, ws_folder)
            
            # Try to get dimensions using file header
            try:
                with open(img_path, 'rb') as f:
                    header = f.read(24)
                    if header.startswith(b'\x89PNG'):
                        # PNG: width/height at bytes 16-24
                        import struct
                        w, h = struct.unpack('>II', header[16:24])
                        meta["dimensions"] = {"width": w, "height": h}
            except Exception:
                pass
            
            if get_output_format(args) != "text":
                print(fmt(meta, args))
            else:
                print(f"Image: {meta['filename']}")
                print("─" * 60)
                print(f"  Path:      {meta['path']}")
                print(f"  UUID:      {meta['uuid']}")
                print(f"  Workspace: {meta['workspace']}")
                print(f"  Size:      {meta['size_kb']:.1f} KB")
                print(f"  Modified:  {meta['modified']}")
                if "dimensions" in meta:
                    print(f"  Dimensions: {meta['dimensions']['width']}x{meta['dimensions']['height']}")
                print(f"\nTo read this image:")
                print(f"  Read: {meta['path']}")
            return
    
    raise NotFoundError(f"Image not found: {args.ref}")


def cmd_image_gallery(args):
    """Generate narrated image gallery markdown."""
    images = []
    
    for img_path, ws_hash, ws_folder in iter_image_paths():
        meta = get_image_metadata(img_path, ws_hash, ws_folder)
        images.append(meta)
    
    # Sort by date (newest first)
    images.sort(key=lambda x: x["modified_ts"], reverse=True)
    
    # Filter by workspace if specified
    if args.workspace:
        images = [i for i in images if args.workspace.lower() in i["workspace"].lower()]
    
    # Limit
    if args.limit:
        images = images[:args.limit]
    
    # Group by workspace
    by_ws: Dict[str, List[Dict]] = {}
    for img in images:
        ws = img["workspace"]
        if ws not in by_ws:
            by_ws[ws] = []
        by_ws[ws].append(img)
    
    # Generate markdown
    lines = [
        "# Image gallery",
        "",
        "*cursor-mirror extracted cached images from Cursor's workspace storage.*",
        "",
        "---",
        "",
        "## Overview",
        "",
        "```yaml",
        "# IMAGE INVENTORY",
        f"total_images: {len(images)}",
        "workspaces:",
    ]
    
    for ws, imgs in sorted(by_ws.items(), key=lambda x: -len(x[1])):
        total_kb = sum(i["size_kb"] for i in imgs)
        lines.append(f"  {ws}: {len(imgs)} images ({total_kb:.0f} KB)")
    
    if images:
        dates = [i["modified"] for i in images]
        lines.extend([
            "",
            "date_range:",
            f"  oldest: {min(dates)}",
            f"  newest: {max(dates)}",
        ])
    
    lines.extend([
        "```",
        "",
        "---",
        "",
    ])
    
    # Generate sections per workspace
    for ws, imgs in sorted(by_ws.items(), key=lambda x: -len(x[1])):
        total_kb = sum(i["size_kb"] for i in imgs)
        lines.extend([
            f"## {ws}",
            "",
            f"*{len(imgs)} images, {total_kb:.1f} KB total*",
            "",
            "| Date | Size | UUID | Path |",
            "|------|------|------|------|",
        ])
        
        for img in imgs:
            uuid_short = img["uuid"][:8] + "..."
            path_short = f"...{img['path'][-50:]}" if len(img['path']) > 50 else img['path']
            lines.append(f"| {img['modified']} | {img['size_kb']:.0f}KB | `{uuid_short}` | `{path_short}` |")
        
        lines.extend(["", "---", ""])
    
    # Usage section
    lines.extend([
        "## Usage",
        "",
        "To view an image in Cursor chat:",
        "",
        "```",
        "Read: /full/path/to/image.png",
        "```",
        "",
        "To list images:",
        "",
        "```bash",
        "cursor-mirror images --all",
        "cursor-mirror images --sort size",
        "cursor-mirror image-path <uuid>",
        "cursor-mirror image-info <uuid> --yaml",
        "```",
        "",
        "---",
        "",
        f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "*By: cursor-mirror image-gallery*",
    ])
    
    output = "\n".join(lines)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"Gallery written to: {args.output}")
    else:
        print(output)


# ~/.cursor Commands (2026-01-15)

DOTCURSOR_BASE = os.path.expanduser("~/.cursor")
DOTCURSOR_PROJECTS = os.path.join(DOTCURSOR_BASE, "projects")
DOTCURSOR_AI_TRACKING = os.path.join(DOTCURSOR_BASE, "ai-tracking", "ai-code-tracking.db")
DOTCURSOR_EXTENSIONS = os.path.join(DOTCURSOR_BASE, "extensions")

