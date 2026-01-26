#!/usr/bin/env python3
"""
compile.py — Adventure 4 Compiler

Compiles YAML adventure sources to world.json with flat registry format.

Usage:
    python compile.py examples/adventure-4/ --output build/world.json
    python compile.py examples/adventure-4/ --output build/ --split
"""

import yaml
import json
import argparse
import sys
from pathlib import Path
from datetime import datetime, date


class YAMLJSONEncoder(json.JSONEncoder):
    """Handle YAML types that aren't JSON-serializable."""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Path):
            return str(obj)
        # Let the base class raise TypeError for other types
        return super().default(obj)


def load_yaml(path: Path) -> dict:
    """Load YAML file, return empty dict if not found."""
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def path_to_id(file_path: Path, adventure_root: Path) -> str:
    """Convert file path to adventure-relative ID: pub, pub/basement, etc."""
    relative = file_path.parent.relative_to(adventure_root)
    parts = str(relative).replace('\\', '/').split('/')
    # Filter out empty parts
    parts = [p for p in parts if p and p != '.']
    return '/'.join(parts) if parts else ''


def normalize_destination(dest: str, current_room_id: str) -> str:
    """Normalize exit destination to adventure-relative path.
    
    Handles:
    - Absolute: pub/basement -> pub/basement
    - Relative: ../street/ -> resolve relative to current
    - Simple: basement/ -> current/basement
    """
    if not dest:
        return None
    
    current_parts = current_room_id.split('/') if current_room_id else []
    dest_parts = dest.rstrip('/').split('/')
    result_parts = list(current_parts)
    
    for part in dest_parts:
        if part == '..':
            if result_parts:
                result_parts.pop()
        elif part and part != '.':
            result_parts.append(part)
    
    result = '/'.join(result_parts)
    if not result:
        return dest.rstrip('/') if not dest.startswith('..') else current_room_id
    
    return result


def compile_condition_to_js(condition: dict) -> str:
    """Compile a condition block to JavaScript guard code (body only).
    
    Returns JUST the code body — no wrapper function signature.
    The engine wraps with standard signature on eval:
      (world, subject, verb, object) => { ... }
    
    Parameters available in code (parallel-safe design):
      - world: shared game state (rooms, flags, player) — NEVER null
      - subject: who is doing the action — OK to be null (timer, system event)
      - verb: what action — OK to be null
      - object: target of action — OK to be null (intransitive verbs)
    
    Supports:
      - check: tag — subject has tag
      - check: inventory_tag — subject has item with tag in inventory
      - check: random — probability check
      - check: any — OR of multiple conditions
      - check: all — AND of multiple conditions
    
    Returns JavaScript code body for engine to wrap and eval.
    """
    check_type = condition.get('check', 'tag')
    
    if check_type == 'tag':
        tag = condition.get('tag', '')
        # subject?.hasTag for null safety — return expression directly
        return f"return subject?.hasTag('{tag}')"
    
    elif check_type == 'inventory_tag':
        tag = condition.get('tag', '')
        return f"return subject?.inventory?.some(item => item.tags?.includes('{tag}'))"
    
    elif check_type == 'random':
        prob = condition.get('probability', 0.5)
        cumulative = condition.get('cumulative', False)
        max_prob = condition.get('max_probability', 1.0)
        if cumulative:
            # Cumulative: track attempts, increase probability
            # Use world.getAttempts/setAttempts for shared state
            return f"const attempts = world.getAttempts(world.exit_id) || 0; const prob = Math.min({prob} + (attempts * 0.05), {max_prob}); world.setAttempts(world.exit_id, attempts + 1); return Math.random() < prob;"
        else:
            return f"return Math.random() < {prob}"
    
    elif check_type == 'any':
        # OR of multiple conditions
        sub_conditions = condition.get('conditions', [])
        sub_bodies = [compile_condition_to_js(c) for c in sub_conditions]
        # Extract return expression from each body and OR them
        exprs = []
        for body in sub_bodies:
            # Strip "return " prefix to get expression
            if body.startswith('return '):
                exprs.append(f"({body[7:].rstrip(';')})")
            else:
                exprs.append(f"({body.rstrip(';')})")
        return f"return {' || '.join(exprs)}"
    
    elif check_type == 'all':
        # AND of multiple conditions
        sub_conditions = condition.get('conditions', [])
        sub_bodies = [compile_condition_to_js(c) for c in sub_conditions]
        exprs = []
        for body in sub_bodies:
            if body.startswith('return '):
                exprs.append(f"({body[7:].rstrip(';')})")
            else:
                exprs.append(f"({body.rstrip(';')})")
        return f"return {' && '.join(exprs)}"
    
    else:
        # Unknown check type - always pass
        return "return true"


def compile_exit(direction: str, exit_data: dict, current_room_id: str) -> dict:
    """Compile an exit definition.
    
    Message naming convention:
      - {key}_message: static text string
      - {key}_message_js: JavaScript closure that produces text
      
    Message types:
      - description_message: What the exit looks like
      - traverse_message: Shown when successfully using the exit
      - traverse_back_message: Shown when returning (opposite direction)
      - pass_message: Shown when conditional check passes
      - fail_message: Shown when conditional check fails
      - reject_message: Shown when guard blocks passage
    
    Conditional exits:
      - condition.check: tag|inventory_tag|random|any|all
      - condition.pass: destination and message on success
      - condition.fail: destination and message on failure
    """
    exit_obj = dict(exit_data)
    
    if 'condition' in exit_data:
        condition = exit_data['condition']
        exit_obj['guard_js'] = compile_condition_to_js(condition)
        
        pass_block = condition.get('pass', {})
        if pass_block:
            if pass_block.get('to'):
                exit_obj['pass_to'] = normalize_destination(pass_block['to'], current_room_id)
            if pass_block.get('message'):
                exit_obj['pass_message'] = pass_block['message']
        
        fail_block = condition.get('fail', {})
        if fail_block:
            if fail_block.get('to'):
                exit_obj['fail_to'] = normalize_destination(fail_block['to'], current_room_id)
            if fail_block.get('message'):
                exit_obj['fail_message'] = fail_block['message']
        
        if 'pass_to' in exit_obj:
            exit_obj['to'] = exit_obj['pass_to']
        elif exit_data.get('to'):
            exit_obj['to'] = normalize_destination(exit_data['to'], current_room_id)
    else:
        exit_obj['to'] = normalize_destination(exit_data.get('to'), current_room_id)
    
    if 'description' in exit_obj:
        exit_obj['description_message'] = exit_obj['description']
    else:
        exit_obj['description_message'] = f'Exit {direction}'
    
    if 'traverse' in exit_data:
        exit_obj['traverse_message'] = exit_data['traverse']
    if 'traverse_back' in exit_data:
        exit_obj['traverse_back_message'] = exit_data['traverse_back']
    
    if 'guard_js' in exit_data:
        exit_obj['guard_js'] = exit_data['guard_js']
    if 'traverse_message_js' in exit_data:
        exit_obj['traverse_message_js'] = exit_data['traverse_message_js']
    if 'description_message_js' in exit_data:
        exit_obj['description_message_js'] = exit_data['description_message_js']
    
    return exit_obj


def compile_room(room_path: Path, adventure_root: Path) -> dict:
    """Compile a ROOM.yml to registry format.
    
    Pass-through philosophy: Keep ALL data from YAML.
    Linter validates required fields, compiler preserves everything
    for browser debugging/inspection.
    """
    data = load_yaml(room_path)
    
    # Handle both nested (room:) and flat format
    room_data = data.get('room', data)
    
    # Start with ALL the raw data (pass-through)
    result = dict(room_data)
    
    # Derive ID from path - ALWAYS use this for exit normalization
    path_derived_id = path_to_id(room_path, adventure_root)
    
    # For the room's actual ID, prefer path-derived but allow explicit override
    # (explicit IDs are legacy - path-derived is the canonical form)
    room_id = path_derived_id
    if 'id' in room_data:
        explicit_id = room_data['id']
        # Only use explicit ID if it looks like a full path (contains /)
        # Short names like "attic" break relative path resolution
        if '/' in explicit_id:
            room_id = explicit_id
        # Otherwise ignore the short explicit ID and use path-derived
    
    # Set/override required fields
    result['type'] = 'room'
    result['id'] = room_id
    result['_source'] = str(room_path.relative_to(adventure_root))
    
    # Ensure name exists
    if 'name' not in result:
        result['name'] = room_id.split('/')[-1].replace('-', ' ').title()
    
    # Compile exits - ALWAYS use path-derived ID for proper relative resolution
    if 'exits' in room_data:
        exits = {}
        for direction, exit_data in room_data['exits'].items():
            if isinstance(exit_data, str):
                # Simple format: "north: room/street"
                exit_data = {'to': exit_data}
            exits[direction.lower()] = compile_exit(direction, exit_data, path_derived_id)
        result['exits'] = exits
    
    return result


def compile_character(char_path: Path, adventure_root: Path) -> dict:
    """Compile a CHARACTER.yml to registry format.
    
    Pass-through philosophy: Keep ALL data from YAML.
    The full character definition is preserved for browser inspection.
    """
    data = load_yaml(char_path)
    
    # Start with ALL the raw data (pass-through)
    result = dict(data)
    
    # Character ID from path
    relative = char_path.parent.relative_to(adventure_root / 'characters')
    char_id = 'character/' + str(relative).replace('\\', '/')
    
    # Set/override required fields
    result['type'] = 'character'
    result['id'] = char_id
    result['_source'] = str(char_path.relative_to(adventure_root))
    
    # Extract commonly-needed fields to top level for easy access
    ontology = data.get('ontology', {})
    char_data = data.get('character', {})
    
    result['tags'] = ontology.get('tags', [])
    result['species'] = ontology.get('species')
    result['name'] = char_data.get('name', char_id.split('/')[-1].replace('-', ' ').title())
    
    # Initialize currency (gold & moolah) with randomized generous amounts
    # Use existing values if set, otherwise randomize
    import random
    
    # Gold: 50-500 (classic fantasy currency)
    if 'gold' not in result and 'gold' not in char_data:
        result['gold'] = random.randint(50, 500)
    else:
        result['gold'] = result.get('gold', char_data.get('gold', 100))
    
    # Moolah: 100-1000 (modern/funky currency)
    if 'moolah' not in result and 'moolah' not in char_data:
        result['moolah'] = random.randint(100, 1000)
    else:
        result['moolah'] = result.get('moolah', char_data.get('moolah', 200))
    
    return result


def compile_catalog(catalog_path: Path, adventure_root: Path) -> dict:
    """Compile a catalog YAML to registry format.
    
    Catalogs can be in two formats:
    1. object: { name, type: catalog, sections: { ... } } — ACME/Leela style
    2. Flat: { id, name, type: catalog, items: [...] } — Simple style
    
    Outputs flattened format for engine: { id, name, type, currency, items: [...] }
    """
    data = load_yaml(catalog_path)
    
    # Handle object: wrapper
    catalog_data = data.get('object', data.get('prototype', data))
    
    # Start with pass-through
    result = dict(catalog_data)
    
    # Generate ID
    relative = catalog_path.relative_to(adventure_root)
    catalog_id = catalog_data.get('id', str(relative.stem))
    if not catalog_id.startswith('catalog/'):
        catalog_id = 'catalog/' + catalog_id
    
    result['id'] = catalog_id
    result['type'] = 'catalog'
    result['_source'] = str(relative)
    result['currency'] = catalog_data.get('currency', 'gold')
    
    # Flatten sections into items array for engine
    items = []
    sections = catalog_data.get('sections', {})
    
    for section_name, section in sections.items():
        if not isinstance(section, dict):
            continue
            
        # Direct items in section
        for item in section.get('items', []):
            flat_item = {
                'id': item.get('item', item.get('name', '')).lower().replace(' ', '-'),
                'name': item.get('item', item.get('name', '')),
                'price': item.get('cost', item.get('price', 0)),
                'description': item.get('description', ''),
                'type': section.get('name', section_name),
                'section': section_name
            }
            # Copy extra fields (warning, malfunction_chance, etc.)
            for k, v in item.items():
                if k not in ['item', 'name', 'cost', 'price', 'description']:
                    flat_item[k] = v
            items.append(flat_item)
        
        # Items in categories (Leela style)
        for cat_name, cat_data in section.get('categories', {}).items():
            if not isinstance(cat_data, dict):
                continue
            for item in cat_data.get('items', []):
                flat_item = {
                    'id': item.get('sku', item.get('name', '')).lower().replace(' ', '-'),
                    'name': item.get('name', ''),
                    'price': parse_price(item.get('price', 0)),
                    'description': item.get('description', ''),
                    'type': cat_name,
                    'section': section_name
                }
                items.append(flat_item)
    
    # Also check for direct items array
    if 'items' in catalog_data:
        for item in catalog_data['items']:
            flat_item = {
                'id': item.get('id', item.get('name', '')).lower().replace(' ', '-'),
                'name': item.get('name', item.get('item', '')),
                'price': item.get('price', item.get('cost', 0)),
                'description': item.get('description', ''),
                'type': item.get('type', 'item')
            }
            items.append(flat_item)
    
    result['items'] = items
    return result


def parse_price(price_str):
    """Parse price from string like '5 coins' or '12' to int."""
    if isinstance(price_str, (int, float)):
        return int(price_str)
    if isinstance(price_str, str):
        # Extract first number
        import re
        match = re.search(r'\d+', price_str)
        if match:
            return int(match.group())
    return 0


def is_object_file(data: dict) -> bool:
    """Determine if a YAML file defines an object.
    
    Objects are identified by:
    - Having an 'object:' wrapper key
    - Having 'name' AND ('description' OR 'examine' OR 'type')
    """
    if 'object' in data:
        return True
    if 'prototype' in data:
        return True
    # Check for object-like structure
    if 'name' in data and ('description' in data or 'examine' in data or 'type' in data):
        return True
    return False


# ═══════════════════════════════════════════════════════════════════════════════
# SLIDESHOW COMPILATION
# ═══════════════════════════════════════════════════════════════════════════════

def compile_photo(photo_dir: Path, slideshow_id: str, adventure_path: Path, github_base: str) -> dict:
    """Compile a single photo directory into a photo entry.
    
    Each photo directory contains:
    - PHOTO.yml (structural metadata)
    - PHOTO.md (narrative description)
    - *.png/*.jpg (images - main and alternatives)
    - MINING-*.yml/md (mining layers)
    """
    photo_yml = photo_dir / 'PHOTO.yml'
    photo_md = photo_dir / 'PHOTO.md'
    
    data = load_yaml(photo_yml) if photo_yml.exists() else {}
    
    # Read narrative if exists
    narrative = ''
    if photo_md.exists():
        try:
            narrative = photo_md.read_text(encoding='utf-8')
        except:
            pass
    
    # Find all images
    images = []
    main_image = None
    for img_file in sorted(photo_dir.glob('*.png')) + sorted(photo_dir.glob('*.jpg')):
        rel_path = img_file.relative_to(adventure_path)
        img_entry = {
            'filename': img_file.name,
            'url': f"{github_base}/{rel_path}",
            'is_main': False,
        }
        # Identify main image (usually same name as directory)
        if img_file.stem == photo_dir.name or img_file.stem.replace('-', '_') == photo_dir.name.replace('-', '_'):
            img_entry['is_main'] = True
            main_image = img_entry
        # Mark versioned/alternative images
        if '-v' in img_file.stem or 'mistake' in img_file.stem.lower():
            img_entry['is_alt'] = True
        images.append(img_entry)
    
    # If no main found, use first non-alt image
    if not main_image and images:
        for img in images:
            if not img.get('is_alt'):
                img['is_main'] = True
                main_image = img
                break
        # Still none? Use first
        if not main_image:
            images[0]['is_main'] = True
            main_image = images[0]
    
    # Find all mining files
    mining = []
    for mine_file in sorted(photo_dir.glob('MINING-*')):
        mine_data = None
        if mine_file.suffix == '.yml':
            mine_data = load_yaml(mine_file)
        elif mine_file.suffix == '.md':
            try:
                mine_data = {'_markdown': mine_file.read_text(encoding='utf-8')}
            except:
                pass
        mining.append({
            'filename': mine_file.name,
            'perspective': mine_file.stem.replace('MINING-', ''),
            'data': mine_data,
        })
    
    # Build photo entry
    photo = {
        'id': f"{slideshow_id}/{photo_dir.name}",
        'dir': photo_dir.name,
        'name': data.get('name', photo_dir.name),
        'type': 'photo',
        # Subject info
        'subject': data.get('subject', {}),
        'mood': data.get('mood', ''),
        # Stereo vision
        'stereo': {
            'left_eye': data,  # Full PHOTO.yml
            'right_eye': narrative[:2000] if narrative else '',  # Truncated PHOTO.md
            'right_eye_full': len(narrative) if narrative else 0,  # Full length
        },
        # Images with GitHub URLs
        'images': images,
        'main_image': main_image['url'] if main_image else None,
        'image_count': len(images),
        # Mining layers
        'mining': mining,
        'mining_count': len(mining),
        # Metadata
        'exif': data.get('exif', {}),
        'iptc': data.get('iptc', {}),
        'xmp': data.get('xmp', {}),
        'camera': data.get('camera', {}),
        'style': data.get('style', {}),
        # Status
        'status': 'generated' if main_image else 'pending',
    }
    
    return photo


def compile_slideshow(slideshow_path: Path, adventure_path: Path) -> dict:
    """Compile a SLIDESHOW.yml into a registry entry.
    
    Slideshows are virtual objects - browseable photo collections
    linked to rooms but existing at top level for global access.
    
    Each photo is a subdirectory with images, metadata, and mining files.
    """
    data = load_yaml(slideshow_path)
    if not data:
        return None
    
    slideshow_dir = slideshow_path.parent
    rel_path = slideshow_dir.relative_to(adventure_path)
    
    # GitHub base URL for images
    github_base = data.get('compiled', {}).get('github_links', {}).get('base', 
        'https://raw.githubusercontent.com/SimHacker/moollm/don-adventure-4-run-1')
    github_base = f"{github_base}/examples/adventure-4"
    
    # ID is adventure-relative path (no type prefix)
    slideshow_id = '/'.join(rel_path.parts)
    
    # Find containing room - check explicit location first
    room_id = None
    if 'location' in data:
        # Explicit room specified
        loc = data['location']
        # Strip legacy room/ prefix if present
        room_id = loc[5:] if loc.startswith('room/') else loc
    elif 'subject' in data and 'location' in data['subject']:
        # Try to derive from subject.location description
        pass  # Keep room_id as None, will be linked globally
    
    # Try to find a room by walking up
    if not room_id:
        room_id = find_room_for_object(slideshow_path, adventure_path)
    
    # If still no room, try to find a sibling room (for slideshows that are siblings to rooms)
    if not room_id:
        parent = slideshow_dir.parent
        for sibling in parent.iterdir():
            if sibling.is_dir() and (sibling / 'ROOM.yml').exists():
                room_id = path_to_id(sibling / 'ROOM.yml', adventure_path)
                break
    
    # Scan photo subdirectories
    photos = []
    cover_photo = None
    for subdir in sorted(slideshow_dir.iterdir()):
        if subdir.is_dir() and (subdir / 'PHOTO.yml').exists():
            photo = compile_photo(subdir, slideshow_id, adventure_path, github_base)
            photos.append(photo)
            # Check for cover photo
            if 'contents' in data:
                for entry in data['contents']:
                    if entry.get('dir') == subdir.name and entry.get('role') == 'COVER_PHOTO':
                        cover_photo = photo
    
    # Build slideshow object
    slideshow = {
        'id': slideshow_id,
        'type': 'slideshow',
        'name': data.get('name', slideshow_id.split('/')[-1]),
        'tagline': data.get('tagline', ''),
        'description': data.get('nature', {}).get('philosophy', ''),
        'location': room_id,
        'subject': data.get('subject', {}),
        # Photos with full data
        'photos': photos,
        'photo_count': len(photos),
        'cover_photo': cover_photo['main_image'] if cover_photo else (photos[0]['main_image'] if photos else None),
        # Virtual object properties for LOD
        'glance': f"📷 {data.get('name', 'Photo slideshow')} ({len(photos)} photos)",
        'examine': f"A collection of {len(photos)} photos.\n" + 
                   (f"Cover: {cover_photo['name']}\n" if cover_photo else "") +
                   "Use BROWSE to view them.",
        # Keep raw data for future features
        'simulated_exif': data.get('simulated_exif', {}),
        'method': data.get('method', {}),
        'github_base': github_base,
        '_source': str(slideshow_path.relative_to(adventure_path)),
    }
    
    return slideshow


def find_slideshows(adventure_path: Path) -> list:
    """Find all SLIDESHOW.yml and SLIDESHOW.md files in the adventure.
    
    Stereo slideshows: YML is source of truth, MD is narrative view.
    When both exist in the same directory, only return the YML.
    """
    yml_files = list(adventure_path.rglob('SLIDESHOW.yml'))
    yml_dirs = {f.parent for f in yml_files}  # Directories that have YML
    
    # Only include MD files if no YML exists in that directory
    md_files = [f for f in adventure_path.rglob('SLIDESHOW.md') 
                if f.parent not in yml_dirs]
    
    return yml_files + md_files


def parse_slideshow_md(md_path: Path, adventure_path: Path, github_base: str) -> dict:
    """Parse a SLIDESHOW.md file into machine-readable format.
    
    SLIDESHOW.md files have:
    - YAML frontmatter (--- delimited)
    - Markdown content with image references ![alt](filename.png)
    - Optional prompt/mining file links
    
    Returns condensed metadata for the runtime.
    """
    import re
    
    content = md_path.read_text(encoding='utf-8')
    slideshow_dir = md_path.parent
    rel_path = slideshow_dir.relative_to(adventure_path)
    
    # Parse YAML frontmatter
    frontmatter = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
            except:
                pass
            content = parts[2]
    
    # Extract image references from markdown: ![alt](filename.png)
    image_pattern = r'!\[([^\]]*)\]\(([^)]+\.(?:png|jpg|jpeg|gif|webp))\)'
    images = []
    seen = set()
    
    for match in re.finditer(image_pattern, content, re.IGNORECASE):
        alt_text = match.group(1)
        filename = match.group(2)
        
        # Skip if already seen (some images may be referenced multiple times)
        if filename in seen:
            continue
        seen.add(filename)
        
        # Build image entry
        img_path = slideshow_dir / filename
        if img_path.exists():
            img_rel = img_path.relative_to(adventure_path)
            images.append({
                'filename': filename,
                'alt': alt_text,
                'url': f"{github_base}/{img_rel}",
            })
    
    # ID is adventure-relative path (no type prefix)
    slideshow_id = '/'.join(rel_path.parts)
    
    # Find room location - check frontmatter first, then fallback to directory search
    room_id = frontmatter.get('location')
    # Strip legacy room/ prefix if present
    if room_id and room_id.startswith('room/'):
        room_id = room_id[5:]
    if not room_id:
        room_id = find_room_for_object(md_path, adventure_path)
    if not room_id:
        parent = slideshow_dir.parent
        for sibling in parent.iterdir():
            if sibling.is_dir() and (sibling / 'ROOM.yml').exists():
                room_id = path_to_id(sibling / 'ROOM.yml', adventure_path)
                break
    
    # Build slideshow entry (condensed for runtime)
    return {
        'id': slideshow_id,
        'type': 'slideshow',
        'name': frontmatter.get('title', slideshow_dir.name),
        'style': frontmatter.get('style', ''),
        'created': frontmatter.get('created', ''),
        'location': room_id,
        # Only main/first image for now
        'main_image': images[0]['url'] if images else None,
        'main_image_alt': images[0]['alt'] if images else '',
        # Photo count (all images found)
        'photo_count': len(images),
        'image_count': frontmatter.get('images', len(images)),
        # LOD text
        'glance': f"📷 {frontmatter.get('title', slideshow_dir.name)}",
        'examine': f"A slideshow with {len(images)} images. Created {frontmatter.get('created', 'unknown')}.",
        # Source
        '_source': str(md_path.relative_to(adventure_path)),
        '_format': 'markdown',
    }


def generate_compound_examine(data: dict, obj_name: str) -> str:
    """Generate an examine string for compound objects like seating.yml.
    
    Summarizes nested structures (bar_stools, tables, booths, etc.) into
    a readable description.
    """
    lines = [f"═══ {obj_name} ═══", ""]
    
    # Get the object data
    obj = data.get('object', data.get('prototype', data))
    
    # Top-level description
    if 'description' in obj:
        lines.append(obj['description'].strip())
        lines.append("")
    
    # Scan for named collections (bar_stools, tables, booths, stools, items, etc.)
    collection_keys = ['bar_stools', 'stools', 'tables', 'named_tables', 'booths', 
                       'named_booths', 'items', 'seats', 'chairs', 'features', 'methods']
    
    for key in collection_keys:
        if key in obj and isinstance(obj[key], dict):
            coll = obj[key]
            # Collection description
            if 'description' in coll:
                lines.append(f"【{key.replace('_', ' ').title()}】")
                lines.append(coll['description'].strip())
                lines.append("")
            # Count items
            item_keys = [k for k in coll.keys() if not k.startswith('_') and k not in 
                        ['description', 'capacity', 'total', 'intimacy', 'service', 'features', 'layout', 'actions']]
            if item_keys:
                lines.append(f"  Contains {len(item_keys)} {key.replace('_', ' ')}")
                # List first few
                for item_key in item_keys[:5]:
                    item = coll.get(item_key, {})
                    if isinstance(item, dict):
                        desc = item.get('position', item.get('location', item.get('quirk', '')))
                        if desc:
                            lines.append(f"    • {item_key}: {desc[:50]}...")
                if len(item_keys) > 5:
                    lines.append(f"    ... and {len(item_keys) - 5} more")
                lines.append("")
    
    # Social dynamics or special sections
    for key in ['social_dynamics', 'lore', 'actions']:
        if key in obj:
            if isinstance(obj[key], str):
                lines.append(f"【{key.replace('_', ' ').title()}】")
                lines.append(obj[key].strip()[:200] + "..." if len(obj[key]) > 200 else obj[key].strip())
                lines.append("")
    
    return "\n".join(lines)


def compile_object(obj_path: Path, adventure_root: Path, room_id: str = None) -> dict:
    """Compile an object YAML to registry format.
    
    Objects can be:
    - Simple: { object: { id, name, description, examine, ... } }
    - Compound: Complex nested structures (seating, with bar_stools, tables, etc.)
    
    For compound objects, we generate a summary examine string.
    """
    data = load_yaml(obj_path)
    
    # Get object data (handle object: wrapper)
    obj_data = data.get('object', data.get('prototype', data))
    
    # Start with pass-through
    result = dict(obj_data)
    
    # Generate ID from path
    relative = obj_path.relative_to(adventure_root)
    stem = obj_path.stem  # filename without .yml
    
    # Build object ID: pub/seating, pub/arcade/pinball-machine
    path_parts = list(relative.parent.parts)
    obj_id = obj_data.get('id', stem)
    # Strip legacy object/ prefix if present
    if obj_id.startswith('object/'):
        obj_id = obj_id[7:]
    # Build full adventure-relative path
    obj_id = '/'.join(path_parts) + '/' + obj_id if path_parts else obj_id
    
    result['id'] = obj_id
    result['type'] = obj_data.get('type', 'object')
    result['_source'] = str(relative)
    
    # Derive room from path (parent directory with ROOM.yml)
    if room_id:
        result['location'] = room_id
    
    # Ensure name exists
    if 'name' not in result:
        result['name'] = stem.replace('-', ' ').title()
    
    # Generate synonyms from name if not present
    if 'synonyms' not in result:
        name = result['name'].lower()
        synonyms = [stem.lower(), name]
        # Add individual words
        for word in name.split():
            if len(word) > 2 and word not in synonyms:
                synonyms.append(word)
        result['synonyms'] = list(set(synonyms))
    
    # Check if this is a compound object (has nested collections)
    compound_keys = ['bar_stools', 'stools', 'tables', 'named_tables', 'booths', 'named_booths']
    is_compound = any(k in obj_data for k in compound_keys)
    
    # For compound objects without a simple examine, generate one
    if is_compound and 'examine' not in result:
        result['examine'] = generate_compound_examine(data, result['name'])
        result['_compound'] = True
    
    # Ensure description exists
    if 'description' not in result:
        result['description'] = f"A {result['name'].lower()}."
    
    # Extract value for economy (default 0)
    result['value'] = obj_data.get('value', 0)
    result['currency'] = obj_data.get('currency', 'gold')
    
    return result


def find_room_for_object(obj_path: Path, adventure_root: Path) -> str:
    """Find the room ID for an object based on its directory.
    
    Walk up directories until we find a ROOM.yml
    """
    current = obj_path.parent
    while current != adventure_root and current != current.parent:
        if (current / 'ROOM.yml').exists():
            return path_to_id(current / 'ROOM.yml', adventure_root)
        current = current.parent
    return None


def compile_adventure(adventure_path: Path) -> dict:
    """Compile entire adventure to world.json format with typed tables."""
    # Typed tables — each type gets its own dict with adventure-relative IDs
    room_table = {}
    character_table = {}
    slideshow_table = {}
    object_table = {}
    catalog_table = {}
    
    # Find all ROOM.yml files
    room_files = list(adventure_path.rglob('ROOM.yml'))
    print(f"📁 Found {len(room_files)} rooms")
    
    for room_file in room_files:
        try:
            r = compile_room(room_file, adventure_path)
            room_table[r['id']] = r
            print(f"  ✓ {r['id']}")
        except Exception as e:
            print(f"  ✗ {room_file}: {e}")
    
    # Find all CHARACTER.yml files
    char_files = list(adventure_path.rglob('CHARACTER.yml'))
    if char_files:
        print(f"🎭 Found {len(char_files)} characters")
        for char_file in char_files:
            try:
                char = compile_character(char_file, adventure_path)
                character_table[char['id']] = char
                print(f"  ✓ {char['id']} [{', '.join(char.get('tags', [])[:3])}...]")
            except Exception as e:
                print(f"  ✗ {char_file}: {e}")
    
    # Find catalog files (files containing type: catalog)
    # CATALOG ALLOWLIST — Set to None to export ALL catalogs, empty set to export none
    # Only export catalogs referenced by exported rooms
    CATALOG_ALLOWLIST = set()  # None of the NO AI TOWER rooms reference catalogs yet
    
    catalog_count = 0
    catalog_files = set()  # Track so we don't re-process as objects
    all_catalogs = {}  # Temp storage before filtering
    
    for yml_file in adventure_path.rglob('*catalog*.yml'):
        try:
            data = load_yaml(yml_file)
            obj = data.get('object', data.get('prototype', data))
            if obj.get('type') == 'catalog' or 'catalog' in obj.get('type', []):
                cat = compile_catalog(yml_file, adventure_path)
                all_catalogs[cat['id']] = cat
                catalog_files.add(yml_file)
        except Exception as e:
            # Not all *catalog*.yml are actual catalogs
            pass
    
    # Filter catalogs by allowlist
    if CATALOG_ALLOWLIST is None:
        # Export all
        catalog_table.update(all_catalogs)
        catalog_count = len(all_catalogs)
    else:
        # Export only allowed
        for cat_id, cat in all_catalogs.items():
            if cat_id in CATALOG_ALLOWLIST:
                catalog_table[cat_id] = cat
                catalog_count += 1
    
    if catalog_count > 0:
        print(f"📚 Found {catalog_count} catalogs")
    if len(all_catalogs) > catalog_count:
        print(f"   (skipped {len(all_catalogs) - catalog_count} catalogs not in allowlist)")
    
    # ═══════════════════════════════════════════════════════════════════════════
    # SLIDESHOWS — Virtual photo collections, linked to rooms
    # ═══════════════════════════════════════════════════════════════════════════
    slideshow_count = 0
    slideshow_files = set()
    # GitHub base URL for images
    github_base = 'https://raw.githubusercontent.com/SimHacker/moollm/don-adventure-4-run-1/examples/adventure-4'
    
    # Collect room IDs from the room table for filtering slideshows
    exported_room_ids = set(room_table.keys())
    
    # SLIDESHOW ALLOWLIST — Set to None to export ALL slideshows
    SLIDESHOW_ALLOWLIST = {
        'street/lane-neverending/slideshow',
    }
    
    print(f"📷 Scanning for slideshows...")
    skipped_orphan = 0
    skipped_not_allowed = 0
    for slideshow_file in find_slideshows(adventure_path):
        try:
            # Dispatch based on file type
            if slideshow_file.suffix == '.yml':
                ss = compile_slideshow(slideshow_file, adventure_path)
            elif slideshow_file.suffix == '.md':
                ss = parse_slideshow_md(slideshow_file, adventure_path, github_base)
            else:
                continue
                
            if ss:
                ss_id = ss.get('id', '')
                
                # Check allowlist (if set)
                if SLIDESHOW_ALLOWLIST is not None:
                    if ss_id not in SLIDESHOW_ALLOWLIST:
                        skipped_not_allowed += 1
                        continue  # Skip silently
                
                # Only export slideshows that are linked to exported rooms
                location = ss.get('location')
                if not location or location not in exported_room_ids:
                    skipped_orphan += 1
                    print(f"  ⊘ {ss['id']} (no room reference)")
                    continue
                    
                slideshow_table[ss['id']] = ss
                slideshow_files.add(slideshow_file)
                # Also track the slideshow directory to skip its contents from object scan
                slideshow_files.add(slideshow_file.parent)
                loc = f" @ {location}"
                img = f" [{ss.get('photo_count', 0)} imgs]"
                print(f"  ✓ {ss['id']}{img}{loc}")
                slideshow_count += 1
        except Exception as e:
            print(f"  ✗ {slideshow_file}: {e}")
    if slideshow_count > 0:
        print(f"📷 Found {slideshow_count} slideshows")
    if skipped_orphan > 0:
        print(f"   (skipped {skipped_orphan} orphan slideshows without room references)")
    if skipped_not_allowed > 0:
        print(f"   (skipped {skipped_not_allowed} slideshows not in allowlist)")
    
    # Find object files (*.yml that aren't ROOM.yml, CHARACTER.yml, or catalogs)
    object_count = 0
    skip_files = {'ROOM.yml', 'CHARACTER.yml', 'ADVENTURE.yml', 'INDEX.yml', 'README.yml', 'README.md', 
                  'SLIDESHOW.yml', 'SLIDESHOW.md', 'PHOTO.yml', 'SERIES.yml', 'PROTOTYPES.yml', 'LAYOUTS.yml'}
    # Skip file patterns (mined data, derived files, not source objects)
    skip_patterns = ['-mine.yml', '-mined.yml', '-flat.yml', 'IMAGE-MINE']
    # Skip non-object data directories and documentation
    skip_dirs = {
        'picnic-footage', 'footage', 'frames', 'images', 'assets',
        'dreams', 'selfies', 'slideshow', 'sessions', 'hazards'
    }
    
    print(f"🎁 Scanning for objects...")
    for yml_file in adventure_path.rglob('*.yml'):
        # Skip known non-object files
        if yml_file.name in skip_files:
            continue
        # Skip README files (any case/extension)
        if yml_file.name.upper().startswith('README'):
            continue
        # Skip mined/mining data files
        if any(pattern in yml_file.name for pattern in skip_patterns):
            continue
        if yml_file in catalog_files:
            continue
        # Skip data directories
        if any(skip_dir in yml_file.parts for skip_dir in skip_dirs):
            continue
        
        try:
            data = load_yaml(yml_file)
            if not data:
                continue
            
            # Check if this looks like an object
            if is_object_file(data):
                room_id = find_room_for_object(yml_file, adventure_path)
                obj = compile_object(yml_file, adventure_path, room_id)
                object_table[obj['id']] = obj
                
                # Shorter output for objects
                compound = " (compound)" if obj.get('_compound') else ""
                loc = f" @ {room_id}" if room_id else ""
                print(f"  ✓ {obj['id']}{compound}{loc}")
                object_count += 1
        except Exception as e:
            # Many .yml files won't be objects - that's fine
            pass
    
    if object_count > 0:
        print(f"🎁 Found {object_count} objects")
    
    # Load adventure config if present
    adventure_yml = adventure_path / 'ADVENTURE.yml'
    config_data = load_yaml(adventure_yml)
    
    starting_room = config_data.get('starting_room', 'pub')
    # Strip legacy room/ prefix if present
    if starting_room.startswith('room/'):
        starting_room = starting_room[5:]
    
    return {
        '_meta': {
            'version': '3.0.0',  # New typed-table format
            'compiled_at': datetime.now().isoformat(),
            'source': str(adventure_path),
            'counts': {
                'room': len(room_table),
                'character': len(character_table),
                'slideshow': len(slideshow_table),
                'object': len(object_table),
                'catalog': len(catalog_table)
            }
        },
        'config': {
            'starting_room': starting_room,
            'name': config_data.get('name', adventure_path.name),
            'features': {
                'pie_menus': True,
                'drag_drop': True,
                'speech': False,
                'images': False
            }
        },
        # Typed tables — each type has its own dict with adventure-relative IDs
        'room': room_table,
        'character': character_table,
        'slideshow': slideshow_table,
        'object': object_table,
        'catalog': catalog_table
    }


def main():
    parser = argparse.ArgumentParser(description='Compile MOOTAL DISTORTION adventure')
    parser.add_argument('adventure_path', type=Path, help='Path to adventure directory')
    parser.add_argument('--output', '-o', type=Path, default=Path('build/world.json'),
                       help='Output file or directory')
    parser.add_argument('--split', action='store_true',
                       help='Split into world.json, characters.json, presets.json')
    parser.add_argument('--pretty', action='store_true', default=True,
                       help='Pretty-print JSON output')
    
    args = parser.parse_args()
    
    if not args.adventure_path.exists():
        print(f"Error: Adventure path does not exist: {args.adventure_path}")
        return 1
    
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  compile.py — Adventure 4 Compiler                                            ║
║  "Compiling dreams into navigable worlds"                                     ║
╚═══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    print(f"📦 Compiling: {args.adventure_path}")
    
    world = compile_adventure(args.adventure_path)
    
    # Ensure output directory exists
    output_path = args.output
    if output_path.suffix == '':
        # It's a directory
        output_path.mkdir(parents=True, exist_ok=True)
        output_path = output_path / 'world.json'
    else:
        output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write output (use custom encoder for dates, etc.)
    indent = 2 if args.pretty else None
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(world, f, indent=indent, ensure_ascii=False, cls=YAMLJSONEncoder)
    
    print(f"\n✅ Compiled to: {output_path}")
    counts = world['_meta']['counts']
    print(f"   {counts['room']} rooms, {counts['character']} characters, {counts['object']} objects")
    print(f"   {counts['slideshow']} slideshows, {counts['catalog']} catalogs")
    print(f"   Starting room: {world['config']['starting_room']}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
