#!/usr/bin/env python3
"""
compile_v2.py — MOOTAL DISTORTION Compiler V2

Compiles YAML adventure sources to world.json with flat registry format.

Usage:
    python compile_v2.py examples/adventure-4/ --output build/world.json
    python compile_v2.py examples/adventure-4/ --output build/ --split
"""

import yaml
import json
import argparse
import sys
from pathlib import Path
from datetime import datetime


def load_yaml(path: Path) -> dict:
    """Load YAML file, return empty dict if not found."""
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def path_to_room_id(room_path: Path, adventure_root: Path) -> str:
    """Convert file path to registry ID: room/pub, room/pub/basement, etc."""
    relative = room_path.parent.relative_to(adventure_root)
    parts = str(relative).replace('\\', '/').split('/')
    # Filter out empty parts
    parts = [p for p in parts if p and p != '.']
    return 'room/' + '/'.join(parts) if parts else 'room/root'


def normalize_destination(dest: str, current_room_id: str) -> str:
    """Normalize exit destination to registry format.
    
    Handles:
    - Absolute: room/pub/basement -> room/pub/basement
    - Relative: ../street/ -> resolve relative to current
    - Simple: basement/ -> room/current/basement
    """
    if not dest:
        return None
    
    # Already in registry format
    if dest.startswith('room/'):
        return dest.rstrip('/')
    
    # Parse current room path
    current_parts = current_room_id.replace('room/', '').split('/')
    
    # Handle relative paths
    dest_parts = dest.rstrip('/').split('/')
    result_parts = list(current_parts)
    
    for part in dest_parts:
        if part == '..':
            if result_parts:
                result_parts.pop()
        elif part and part != '.':
            result_parts.append(part)
    
    return 'room/' + '/'.join(result_parts)


def compile_exit(direction: str, exit_data: dict, current_room_id: str) -> dict:
    """Compile an exit definition."""
    # Handle both old format (destination) and new format (to)
    dest = exit_data.get('to') or exit_data.get('destination')
    
    exit_obj = {
        'to': normalize_destination(dest, current_room_id),
        'description': exit_data.get('description', f'Exit {direction}'),
    }
    
    # Aliases
    if 'aliases' in exit_data:
        exit_obj['aliases'] = exit_data['aliases']
    
    # _js hooks (guard, fail_message, dynamic description)
    if '_js' in exit_data:
        js = exit_data['_js']
        if 'guard' in js:
            exit_obj['guard'] = js['guard']
        if 'fail_message' in js:
            exit_obj['fail_message'] = js['fail_message']
        if 'description' in js:
            exit_obj['description_js'] = js['description']
    
    # Legacy guard_js support
    if 'guard_js' in exit_data:
        exit_obj['guard'] = exit_data['guard_js']
    
    # Locked flag
    if exit_data.get('locked'):
        exit_obj['locked'] = True
    
    # Notes (for display)
    if 'note' in exit_data:
        exit_obj['note'] = exit_data['note']
    
    return exit_obj


def compile_room(room_path: Path, adventure_root: Path) -> dict:
    """Compile a ROOM.yml to registry format."""
    data = load_yaml(room_path)
    
    # Handle both nested (room:) and flat format
    room_data = data.get('room', data)
    
    # Derive ID from path
    room_id = path_to_room_id(room_path, adventure_root)
    
    # Use explicit ID if provided
    if 'id' in room_data:
        room_id = 'room/' + room_data['id']
    
    # Compile exits
    exits = {}
    for direction, exit_data in room_data.get('exits', {}).items():
        if isinstance(exit_data, str):
            # Simple format: "north: room/street"
            exit_data = {'to': exit_data}
        exits[direction.lower()] = compile_exit(direction, exit_data, room_id)
    
    result = {
        'type': 'room',
        'id': room_id,
        'name': room_data.get('name', room_id.split('/')[-1].replace('-', ' ').title()),
        'description': room_data.get('description', ''),
        'exits': exits
    }
    
    # Optional fields
    if 'examine' in room_data:
        result['examine'] = room_data['examine']
    if 'atmosphere' in room_data:
        result['atmosphere'] = room_data['atmosphere']
    if 'lighting' in room_data:
        result['lighting'] = room_data['lighting']
    
    # Contents (object references for later)
    if 'objects' in room_data:
        result['contents'] = room_data['objects']
    if 'contents' in room_data:
        result['contents'] = room_data['contents']
    
    return result


def compile_adventure(adventure_path: Path) -> dict:
    """Compile entire adventure to world.json format."""
    registry = {}
    
    # Find all ROOM.yml files
    room_files = list(adventure_path.rglob('ROOM.yml'))
    print(f"📁 Found {len(room_files)} rooms")
    
    for room_file in room_files:
        try:
            room = compile_room(room_file, adventure_path)
            registry[room['id']] = room
            print(f"  ✓ {room['id']}")
        except Exception as e:
            print(f"  ✗ {room_file}: {e}")
    
    # Load adventure config if present
    adventure_yml = adventure_path / 'ADVENTURE.yml'
    config_data = load_yaml(adventure_yml)
    
    starting_room = config_data.get('starting_room', 'room/pub')
    if not starting_room.startswith('room/'):
        starting_room = 'room/' + starting_room
    
    return {
        '_meta': {
            'version': '2.0.0',
            'compiled_at': datetime.now().isoformat(),
            'source': str(adventure_path),
            'room_count': len(registry)
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
        'registry': registry
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
║  compile_v2.py — MOOTAL DISTORTION Compiler                                   ║
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
    
    # Write output
    indent = 2 if args.pretty else None
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(world, f, indent=indent, ensure_ascii=False)
    
    print(f"\n✅ Compiled to: {output_path}")
    print(f"   {world['_meta']['room_count']} rooms")
    print(f"   Starting room: {world['config']['starting_room']}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
