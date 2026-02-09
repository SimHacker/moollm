#!/usr/bin/env python3
"""
validate.py — Adventure 4 YAML Validator

Validates all ROOM.yml files and reports all errors.
Optionally fixes common issues.

Usage:
    python validate.py examples/adventure-4/           # Check all
    python validate.py examples/adventure-4/ --fix     # Fix what we can
    python validate.py examples/adventure-4/ --verbose # Show details
"""

import yaml
import argparse
import sys
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class ValidationError:
    file: Path
    line: Optional[int]
    error_type: str
    message: str
    fixable: bool = False
    fix_description: str = ""


class RoomValidator:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []
        self.fixed: List[str] = []
        
    def validate_yaml_syntax(self, path: Path) -> Tuple[bool, Optional[dict], Optional[str]]:
        """Check if file is valid YAML. Returns (valid, data, error_message)."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            data = yaml.safe_load(content)
            return True, data, None
        except yaml.YAMLError as e:
            # Extract line number if available
            line = None
            if hasattr(e, 'problem_mark') and e.problem_mark:
                line = e.problem_mark.line + 1
            return False, None, str(e)
    
    def validate_room_schema(self, path: Path, data: dict) -> List[ValidationError]:
        """Validate room data against expected schema."""
        errors = []
        
        # Handle both nested (room:) and flat format
        room_data = data.get('room', data)
        
        # Check required fields
        if not room_data.get('name') and not room_data.get('id'):
            errors.append(ValidationError(
                file=path,
                line=None,
                error_type="MISSING_FIELD",
                message="Room has no 'name' or 'id'",
                fixable=True,
                fix_description="Derive name from directory"
            ))
        
        # Validate exits
        exits = room_data.get('exits', {})
        for direction, exit_data in exits.items():
            # Check if direction is a string (not int)
            if not isinstance(direction, str):
                errors.append(ValidationError(
                    file=path,
                    line=None,
                    error_type="EXIT_KEY_TYPE",
                    message=f"Exit key '{direction}' is {type(direction).__name__}, should be string (quote it!)",
                    fixable=True,
                    fix_description=f"Quote exit key: '{direction}' -> '\"{direction}\"'"
                ))
            
            # Check exit has destination
            if isinstance(exit_data, dict):
                has_destination = (
                    exit_data.get('to') or
                    exit_data.get('condition', {}).get('pass', {}).get('to')
                )
                if not has_destination:
                    errors.append(ValidationError(
                        file=path,
                        line=None,
                        error_type="EXIT_NO_DEST",
                        message=f"Exit '{direction}' has no destination",
                        fixable=False
                    ))
        
        return errors
    
    def check_unquoted_special_chars(self, path: Path) -> List[ValidationError]:
        """Check for common YAML gotchas that might cause issues."""
        # Disabled - too many false positives from comments
        # These aren't real errors, just style warnings
        return []
    
    def validate_file(self, path: Path) -> List[ValidationError]:
        """Validate a single ROOM.yml file."""
        errors = []
        
        # Check YAML syntax first
        valid, data, error_msg = self.validate_yaml_syntax(path)
        
        if not valid:
            errors.append(ValidationError(
                file=path,
                line=None,
                error_type="YAML_SYNTAX",
                message=error_msg,
                fixable=False
            ))
            return errors
        
        # If valid YAML, check schema
        if data:
            errors.extend(self.validate_room_schema(path, data))
        
        # Check for common issues even in valid YAML
        errors.extend(self.check_unquoted_special_chars(path))
        
        return errors
    
    def fix_integer_keys(self, path: Path) -> bool:
        """Fix integer exit keys by quoting them."""
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern: line starting with spaces, then a number, then colon
        # e.g., "    13:" -> "    \"13\":"
        pattern = r'^(\s+)(\d+)(:)$'
        
        def replacer(m):
            return f'{m.group(1)}"{m.group(2)}"{m.group(3)}'
        
        new_content, count = re.subn(pattern, replacer, content, flags=re.MULTILINE)
        
        if count > 0:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        return False
    
    def validate_adventure(self, adventure_path: Path, fix: bool = False) -> dict:
        """Validate all ROOM.yml files in an adventure."""
        room_files = list(adventure_path.rglob('ROOM.yml'))
        
        results = {
            'total': len(room_files),
            'valid': 0,
            'errors': 0,
            'warnings': 0,
            'fixed': 0,
            'error_list': [],
            'warning_list': [],
            'fixed_list': []
        }
        
        print(f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  validate.py — Adventure 4 Validator                                          ║
║  "Trust, but verify"                                                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
        """)
        print(f"📁 Scanning: {adventure_path}")
        print(f"📄 Found {len(room_files)} ROOM.yml files\n")
        
        for room_file in sorted(room_files):
            rel_path = room_file.relative_to(adventure_path)
            errors = self.validate_file(room_file)
            
            if errors:
                results['errors'] += len(errors)
                results['error_list'].extend(errors)
                
                # Try to fix if requested
                if fix:
                    for error in errors:
                        if error.error_type == "EXIT_KEY_TYPE":
                            if self.fix_integer_keys(room_file):
                                results['fixed'] += 1
                                results['fixed_list'].append(f"{rel_path}: Fixed integer exit keys")
                                print(f"  🔧 {rel_path}: Fixed integer keys")
                
                if self.verbose or not fix:
                    print(f"  ✗ {rel_path}")
                    for error in errors:
                        print(f"      {error.error_type}: {error.message}")
                        if error.fixable:
                            print(f"        💡 Fix: {error.fix_description}")
            else:
                results['valid'] += 1
                if self.verbose:
                    print(f"  ✓ {rel_path}")
        
        # Summary
        print(f"\n{'═' * 60}")
        print(f"📊 VALIDATION SUMMARY")
        print(f"{'═' * 60}")
        print(f"  Total files:    {results['total']}")
        print(f"  Valid:          {results['valid']} ✓")
        print(f"  With errors:    {results['total'] - results['valid']} ✗")
        print(f"  Total issues:   {results['errors']}")
        if fix:
            print(f"  Fixed:          {results['fixed']} 🔧")
        
        # Group errors by type
        if results['error_list']:
            print(f"\n{'─' * 60}")
            print("📋 ERRORS BY TYPE:")
            
            by_type = {}
            for error in results['error_list']:
                by_type.setdefault(error.error_type, []).append(error)
            
            for error_type, errors in sorted(by_type.items()):
                print(f"\n  {error_type} ({len(errors)} files):")
                for error in errors[:5]:  # Show first 5
                    rel = error.file.relative_to(adventure_path)
                    print(f"    • {rel}")
                if len(errors) > 5:
                    print(f"    ... and {len(errors) - 5} more")
        
        return results


# YAML CLASSIFICATION — Identify file types, warn on unrecognized

# Known file types (don't warn about these)
KNOWN_FILES = {
    'ROOM.yml', 'CHARACTER.yml', 'ADVENTURE.yml', 'INDEX.yml', 
    'README.yml', 'README.md', 'CARD.yml', 'SKILL.yml'
}

# Ignore patterns (data files, not objects)
IGNORE_PATTERNS = [
    # Directories
    'picnic-footage',   # Image frame data
    'footage',          # Video/image data
    'frames',           # Animation frames
    'images',           # Image assets
    'assets',           # General assets
    'dreams',           # Dream narratives
    'selfies',          # Image metadata
    'slideshow',        # Slideshow data
    'sessions',         # Session logs
    'hazards',          # Hazard definitions
    # File patterns
    '-mine.yml',        # User-annotated versions
    'IMAGE-PROMPTS.yml',# Image generation prompts
    'IMAGE-MINE',       # Image inventory
    'ENEMIES.yml',      # Character relationships
    'LINTER.yml',       # Linter output
    'demo.yml',         # Demo/test files
    'README',           # Documentation (README.md, README.yml, etc.)
]

# Files with these keys are data, not objects (auto-ignore)
DATA_MARKERS = {
    # Linter/system
    'lint_ignore', 'probe', 'boot_sequence', 'session',
    # Character data
    'dream', 'incarnation', 'enemies_list', 'selfies', 'selfie', 
    'inherits', 'defaults', 'generate', 'also_called', 'style_guide',
    # Image/media
    'image_prompts', 'inventory', 'resources', 'mining_notes',
    'generation', 'prompt', 'sources', 'provider', 'model',
    'art_style', 'game_style', 'style_reference', 'tribute',
    'exhausted', 'visible_elements', 'extracted_text', 'mined',
    # Game data
    'game', 'hazard', 'dodecahedron', 'rooms', 'arrows', 'deck',
    'layouts', 'prototypes', 'aisle',
    # Artifacts
    'artifact', 'advertisement', 'conversation_hooks', 'sample_quotes',
    # Content
    'series', 'frame', 'context_synthesis', 'container',
    'scene', 'guest_book', 'entries', 'templates',
    # Cards
    'card', 'secret_word',
}

# Filename patterns that are data (not objects)
DATA_FILE_PATTERNS = [
    '-mine.yml',      # Mining analysis files
    '-mined.yml',     # Mined image metadata
    'IMAGE-MINE',     # Image inventory
    'PROTOTYPES.yml', # Prototype data
    'LAYOUTS.yml',    # Layout data
    'SERIES.yml',     # Series data
]

# Filename patterns that are data
DATA_FILENAMES = {
    'PALM-LANGUAGE.yml', 'DODECAHEDRON.yml', 'GAME.yml', 'SUPERBATS.yml',
    'SLIDESHOW.yml', 'PHOTO.yml'
}

# Object detection: files with these top-level keys are objects
OBJECT_MARKERS = {'object', 'prototype', 'item'}

# Object-like: has these fields = probably should be an object
OBJECT_FIELDS = {'name', 'description', 'examine', 'type', 'glance'}


def classify_yaml(path: Path, data: dict) -> dict:
    """Classify a YAML file by its content.
    
    Returns: {
        'type': 'room'|'character'|'catalog'|'object'|'data'|'unknown',
        'confidence': 'high'|'medium'|'low',
        'reason': str,
        'should_be_object': bool,  # Suggest promotion to object
        'missing_fields': list,    # Fields needed for objecthood
    }
    """
    filename = path.name
    
    # Known special files
    if filename == 'ROOM.yml':
        return {'type': 'room', 'confidence': 'high', 'reason': 'ROOM.yml', 
                'should_be_object': False, 'missing_fields': []}
    if filename == 'CHARACTER.yml':
        return {'type': 'character', 'confidence': 'high', 'reason': 'CHARACTER.yml',
                'should_be_object': False, 'missing_fields': []}
    if filename in KNOWN_FILES:
        return {'type': 'known', 'confidence': 'high', 'reason': f'{filename}',
                'should_be_object': False, 'missing_fields': []}
    if filename in DATA_FILENAMES:
        return {'type': 'data', 'confidence': 'high', 'reason': f'data file: {filename}',
                'should_be_object': False, 'missing_fields': []}
    
    # Check ignore patterns
    # Convert to string for pattern matching
    path_str = str(path)
    abs_path_str = str(path.resolve())
    
    for pattern in IGNORE_PATTERNS:
        # Check if pattern is in path (either relative or absolute)
        if pattern in path_str or pattern in abs_path_str:
            return {'type': 'ignored', 'confidence': 'high', 'reason': f'matches {pattern}',
                    'should_be_object': False, 'missing_fields': []}
        # Check path components (handle /dreams/ style directories)
        if f'/{pattern}/' in path_str or f'/{pattern}/' in abs_path_str:
            return {'type': 'ignored', 'confidence': 'high', 'reason': f'in {pattern}/',
                    'should_be_object': False, 'missing_fields': []}
    
    if not data:
        return {'type': 'empty', 'confidence': 'high', 'reason': 'empty file',
                'should_be_object': False, 'missing_fields': []}
    
    # Must be a dict to continue
    if not isinstance(data, dict):
        return {'type': 'data', 'confidence': 'high', 'reason': f'non-dict content ({type(data).__name__})',
                'should_be_object': False, 'missing_fields': []}
    
    # Check for data markers (lint_ignore, dream, etc.)
    if any(marker in data for marker in DATA_MARKERS):
        matched = [m for m in DATA_MARKERS if m in data]
        return {'type': 'data', 'confidence': 'high', 'reason': f'has {matched[0]}',
                'should_be_object': False, 'missing_fields': []}
    
    # Catalog detection
    obj = data.get('object', data.get('prototype', data))
    if not isinstance(obj, dict):
        obj = data
    if obj.get('type') == 'catalog' or 'catalog' in filename.lower():
        return {'type': 'catalog', 'confidence': 'high', 'reason': 'type: catalog',
                'should_be_object': False, 'missing_fields': []}
    
    # Explicit object marker
    if any(marker in data for marker in OBJECT_MARKERS):
        return {'type': 'object', 'confidence': 'high', 'reason': 'has object: wrapper',
                'should_be_object': False, 'missing_fields': []}
    
    # Object-like detection (has some object fields)
    found_fields = [f for f in OBJECT_FIELDS if f in data]
    if len(found_fields) >= 2:
        # Has enough fields to be an object, but missing wrapper
        missing = []
        if 'name' not in data:
            missing.append('name')
        if 'description' not in data and 'examine' not in data:
            missing.append('description or examine')
        
        return {
            'type': 'object-like',
            'confidence': 'medium',
            'reason': f'has {", ".join(found_fields)}',
            'should_be_object': True,
            'missing_fields': missing
        }
    
    # Check if it's just data (has structure but not object-like)
    if isinstance(data, dict) and len(data) > 0:
        # Has content but doesn't match patterns
        return {
            'type': 'unknown',
            'confidence': 'low',
            'reason': f'unrecognized structure (keys: {", ".join(list(data.keys())[:5])})',
            'should_be_object': False,
            'missing_fields': list(OBJECT_FIELDS)
        }
    
    return {'type': 'unknown', 'confidence': 'low', 'reason': 'no matching pattern',
            'should_be_object': False, 'missing_fields': []}


def scan_yaml_files(adventure_path: Path, verbose: bool = False) -> dict:
    """Scan all YAML files and classify them.
    
    Returns summary with warnings for unrecognized files.
    """
    print(f"\n{'═' * 60}")
    print("📂 YAML FILE CLASSIFICATION")
    print(f"{'═' * 60}")
    
    results = {
        'total': 0,
        'by_type': {},
        'warnings': [],
        'promotable': [],  # Files that should be objects
    }
    
    for yml_file in sorted(adventure_path.rglob('*.yml')):
        results['total'] += 1
        
        try:
            with open(yml_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
        except Exception as e:
            results['warnings'].append({
                'file': yml_file,
                'type': 'parse_error',
                'message': str(e)
            })
            continue
        
        classification = classify_yaml(yml_file, data)
        file_type = classification['type']
        
        # Count by type
        results['by_type'][file_type] = results['by_type'].get(file_type, 0) + 1
        
        # Track warnings
        if file_type == 'unknown':
            rel_path = yml_file.relative_to(adventure_path)
            results['warnings'].append({
                'file': rel_path,
                'type': 'unrecognized',
                'message': classification['reason'],
                'keys': list(data.keys())[:5] if isinstance(data, dict) else []
            })
        
        # Track promotable files
        if classification['should_be_object']:
            rel_path = yml_file.relative_to(adventure_path)
            results['promotable'].append({
                'file': rel_path,
                'reason': classification['reason'],
                'missing': classification['missing_fields']
            })
        
        if verbose and file_type not in ('room', 'character', 'object', 'catalog', 'known', 'ignored'):
            rel_path = yml_file.relative_to(adventure_path)
            print(f"  ⚠️  {rel_path}: {file_type} ({classification['reason']})")
    
    # Summary
    print(f"\n📊 Classification Summary ({results['total']} files):")
    for ftype, count in sorted(results['by_type'].items(), key=lambda x: -x[1]):
        emoji = {'room': '🏠', 'character': '🎭', 'object': '📦', 'catalog': '📚',
                 'known': '📄', 'ignored': '⊘', 'object-like': '📦?', 'unknown': '❓'}.get(ftype, '•')
        print(f"   {emoji} {ftype}: {count}")
    
    # Separate parse errors from unrecognized
    parse_errors = [w for w in results['warnings'] if w.get('type') == 'parse_error']
    unrecognized = [w for w in results['warnings'] if w.get('type') == 'unrecognized']
    
    # Parse errors
    if parse_errors:
        print(f"\n❌ PARSE ERRORS ({len(parse_errors)}):")
        for w in parse_errors[:5]:
            print(f"   • {w['file']}")
        if len(parse_errors) > 5:
            print(f"   ... and {len(parse_errors) - 5} more")
    
    # Unrecognized
    if unrecognized:
        print(f"\n⚠️  UNRECOGNIZED FILES ({len(unrecognized)}):")
        print("   (Consider adding to IGNORE_PATTERNS or promoting to objects)")
        for w in unrecognized[:10]:
            print(f"   • {w['file']}")
            if w.get('keys'):
                print(f"     keys: {', '.join(w['keys'])}")
        if len(unrecognized) > 10:
            print(f"   ... and {len(unrecognized) - 10} more")
    
    # Promotable
    if results['promotable']:
        print(f"\n📦 SHOULD BE OBJECTS ({len(results['promotable'])}):")
        print("   (Add 'object:' wrapper or missing fields)")
        for p in results['promotable'][:10]:
            print(f"   • {p['file']}")
            if p['missing']:
                print(f"     missing: {', '.join(p['missing'])}")
        if len(results['promotable']) > 10:
            print(f"   ... and {len(results['promotable']) - 10} more")
    
    return results


def verify_topology(adventure_path: Path, verbose: bool = False, exclude_patterns: list = None, starting_room: str = 'room/pub'):
    """Verify bidirectional links, disconnected rooms, and unbound exits."""
    exclude_patterns = exclude_patterns or ['maze/']
    
    print(f"\n{'═' * 60}")
    print("🔗 TOPOLOGY VERIFICATION")
    print(f"{'═' * 60}")
    print(f"   Starting room: {starting_room}")
    print(f"   Excluding from bidirectional check: {', '.join(exclude_patterns)}")
    
    # Build room graph
    rooms = {}  # room_id -> {exits: {direction: destination_id}}
    room_files = list(adventure_path.rglob('ROOM.yml'))
    
    for room_file in room_files:
        try:
            with open(room_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            if not data:
                continue
                
            room_data = data.get('room', data)
            
            # Derive room ID from path
            relative = room_file.parent.relative_to(adventure_path)
            parts = str(relative).replace('\\', '/').split('/')
            parts = [p for p in parts if p and p != '.']
            room_id = 'room/' + '/'.join(parts) if parts else 'room/root'
            
            # Get exits
            exits = {}
            for direction, exit_data in room_data.get('exits', {}).items():
                if isinstance(exit_data, str):
                    dest = exit_data
                else:
                    dest = exit_data.get('to') or exit_data.get('destination')
                
                if dest:
                    # Normalize destination
                    if not dest.startswith('room/'):
                        # Resolve relative path
                        current_parts = room_id.replace('room/', '').split('/')
                        dest_parts = dest.rstrip('/').split('/')
                        result_parts = list(current_parts)
                        for part in dest_parts:
                            if part == '..':
                                if result_parts:
                                    result_parts.pop()
                            elif part and part != '.':
                                result_parts.append(part)
                        dest = 'room/' + '/'.join(result_parts)
                    else:
                        dest = dest.rstrip('/')
                    
                    exits[str(direction).lower()] = dest
            
            rooms[room_id] = {'exits': exits, 'file': str(room_file.relative_to(adventure_path))}
            
        except Exception as e:
            pass  # Skip files with errors
    
    # CHECK 1: Unbound Exits (point to non-existent rooms)
    unbound_exits = []
    global_exits = []  # $SKILLS, $CHARACTERS, etc — valid but external
    todo_exits = []    # TODO, ???, TBD — marked as work-in-progress (warnings)
    
    # TODO markers — intentional placeholders
    TODO_MARKERS = {'TODO', '???', 'TBD', 'FIXME', 'WIP', 'PLANNED', 'STUB'}
    
    for room_id, room_info in rooms.items():
        for direction, dest_id in room_info['exits'].items():
            if not dest_id:
                continue
            
            dest_str = str(dest_id).strip()
            dest_upper = dest_str.upper()
            
            # TODO markers — intentional placeholders (warning, not error)
            is_todo = (dest_upper in TODO_MARKERS or 
                       any(dest_upper.startswith(m + ':') for m in TODO_MARKERS) or
                       any(dest_upper.startswith(m + ' ') for m in TODO_MARKERS) or
                       '???' in dest_str)
            if is_todo:
                todo_exits.append({
                    'from': room_id,
                    'direction': direction,
                    'to': dest_id
                })
                continue
                
            # Global/external references (valid, just not in this adventure)
            if dest_id.startswith('$') or '/$' in dest_id:
                global_exits.append({
                    'from': room_id,
                    'direction': direction,
                    'to': dest_id
                })
                continue
                
            # Check if destination exists
            if dest_id not in rooms:
                unbound_exits.append({
                    'from': room_id,
                    'direction': direction,
                    'to': dest_id
                })
    
    # CHECK 2: Disconnected Rooms (not reachable from starting room)
    # BFS from starting room to find all reachable rooms
    # Note: Global exits ($SKILLS etc) don't count for connectivity
    reachable = set()
    queue = [starting_room] if starting_room in rooms else []
    
    while queue:
        current = queue.pop(0)
        if current in reachable:
            continue
        reachable.add(current)
        
        # Add all destinations from this room (skip global refs)
        if current in rooms:
            for dest in rooms[current]['exits'].values():
                if dest and dest in rooms and dest not in reachable:
                    if not dest.startswith('$') and '/$' not in dest:
                        queue.append(dest)
    
    disconnected = []
    for room_id in rooms:
        if room_id not in reachable:
            disconnected.append(room_id)
    
    # CHECK 3: Bidirectional links
    one_way_links = []
    checked = set()
    
    # Direction opposites
    opposites = {
        'north': 'south', 'south': 'north',
        'east': 'west', 'west': 'east',
        'up': 'down', 'down': 'up',
        'northeast': 'southwest', 'southwest': 'northeast',
        'northwest': 'southeast', 'southeast': 'northwest',
        'in': 'out', 'out': 'in',
    }
    
    for room_id, room_info in rooms.items():
        # Skip excluded patterns
        skip = False
        for pattern in exclude_patterns:
            if pattern in room_id:
                skip = True
                break
        if skip:
            continue
        
        for direction, dest_id in room_info['exits'].items():
            # Create unique key for this link
            link_key = tuple(sorted([room_id, dest_id]))
            if link_key in checked:
                continue
            checked.add(link_key)
            
            # Skip if destination doesn't exist
            if dest_id not in rooms:
                continue
            
            # Skip excluded destinations
            skip_dest = False
            for pattern in exclude_patterns:
                if pattern in dest_id:
                    skip_dest = True
                    break
            if skip_dest:
                continue
            
            # Check for return link
            dest_exits = rooms[dest_id]['exits']
            opposite = opposites.get(direction)
            
            # Look for any exit back to this room
            has_return = False
            return_dir = None
            for d, target in dest_exits.items():
                if target == room_id:
                    has_return = True
                    return_dir = d
                    break
            
            if not has_return:
                one_way_links.append({
                    'from': room_id,
                    'to': dest_id,
                    'direction': direction,
                    'expected_return': opposite
                })
    
    # Report results
    print(f"\n📊 Room Graph: {len(rooms)} rooms, {len(reachable)} reachable from {starting_room}")
    
    # Report global exits (informational)
    if global_exits:
        print(f"\n🌐 GLOBAL EXITS: {len(global_exits)}")
        print("   (External references — valid, handled at runtime)")
        if verbose:
            for ge in global_exits:
                short_from = '/'.join(ge['from'].split('/')[-2:])
                print(f"      {short_from} →{ge['direction']}→ {ge['to']}")
    
    # Report unbound exits
    if unbound_exits:
        print(f"\n❌ UNBOUND EXITS: {len(unbound_exits)}")
        print("   (Exit points to non-existent room)")
        for ub in unbound_exits[:10] if not verbose else unbound_exits:
            short_from = '/'.join(ub['from'].split('/')[-2:])
            print(f"      {short_from} →{ub['direction']}→ {ub['to']} ✗")
        if len(unbound_exits) > 10 and not verbose:
            print(f"      ... and {len(unbound_exits) - 10} more")
    else:
        print(f"\n✅ All local exits point to existing rooms")
    
    # Report disconnected rooms
    if disconnected:
        print(f"\n🏝️  DISCONNECTED ROOMS: {len(disconnected)}")
        print(f"   (Not reachable from {starting_room})")
        for d in sorted(disconnected)[:15] if not verbose else sorted(disconnected):
            print(f"      • {d}")
        if len(disconnected) > 15 and not verbose:
            print(f"      ... and {len(disconnected) - 15} more")
        
        # Find potential entry points (rooms that COULD connect to main graph)
        potential_entries = []
        for disc_room in disconnected:
            for direction, dest in rooms[disc_room]['exits'].items():
                if dest in reachable:
                    potential_entries.append((disc_room, direction, dest))
        
        if potential_entries:
            print(f"\n   💡 These disconnected rooms have exits TO the main graph:")
            for entry in potential_entries[:5]:
                short = '/'.join(entry[0].split('/')[-2:])
                short_dest = '/'.join(entry[2].split('/')[-2:])
                print(f"      {short} →{entry[1]}→ {short_dest}")
                print(f"         ↳ Add exit from {short_dest} back to {short}")
    else:
        print(f"\n✅ All rooms reachable from {starting_room}")
    
    if verbose:
        print(f"\n📋 Full Room Graph:")
        for room_id, info in sorted(rooms.items()):
            skip = any(p in room_id for p in exclude_patterns)
            is_reachable = room_id in reachable
            if not is_reachable:
                marker = '🏝️'  # disconnected
            elif skip:
                marker = '⊘'   # excluded from bidirectional
            else:
                marker = '•'
            exits_str = ', '.join(f"{d}→{t.split('/')[-1]}" for d, t in info['exits'].items())
            print(f"   {marker} {room_id}")
            if exits_str:
                print(f"      exits: {exits_str}")
    
    if one_way_links:
        print(f"\n⚠️  ONE-WAY LINKS FOUND: {len(one_way_links)}")
        print("   (Room A → Room B, but no return path)")
        
        # Categorize by type
        cardinal = []      # north/south/east/west
        vertical = []      # up/down
        in_out = []        # in/out
        named = []         # lobby, storage, etc
        
        for link in one_way_links:
            d = link['direction']
            if d in ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest']:
                cardinal.append(link)
            elif d in ['up', 'down']:
                vertical.append(link)
            elif d in ['in', 'out']:
                in_out.append(link)
            else:
                named.append(link)
        
        def show_category(title, links, show_all=False):
            if not links:
                return
            print(f"\n   {title} ({len(links)}):")
            show = links if show_all else links[:5]
            for link in show:
                short_from = '/'.join(link['from'].split('/')[-2:])
                short_to = '/'.join(link['to'].split('/')[-2:])
                print(f"      {short_from} →{link['direction']}→ {short_to}")
            if len(links) > 5 and not show_all:
                print(f"      ... and {len(links) - 5} more")
        
        show_category("🧭 CARDINAL (N/S/E/W) — likely bugs", cardinal, verbose)
        show_category("⬆️  VERTICAL (up/down) — check stairs/ladders", vertical, verbose)
        show_category("🚪 IN/OUT — check door symmetry", in_out, verbose)
        show_category("🏷️  NAMED EXITS — intentional or needs return", named, verbose)
        
        print(f"\n   💡 To add return exit, add to destination room:")
        print(f"      exits:")
        print(f"        <return_direction>:")
        print(f"          to: <source_room>")
        print(f"          description: \"Back to ...\"")
        
    else:
        print(f"\n✅ All links are bidirectional!")
    
    return one_way_links


def main():
    parser = argparse.ArgumentParser(description='Validate Adventure 4 YAML files')
    parser.add_argument('adventure_path', type=Path, help='Path to adventure directory')
    parser.add_argument('--fix', action='store_true', help='Attempt to fix issues')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show all files')
    parser.add_argument('--topology', '-t', action='store_true', help='Verify bidirectional links')
    parser.add_argument('--scan', '-s', action='store_true', help='Scan and classify all YAML files')
    parser.add_argument('--exclude', '-x', nargs='*', default=['maze/'], 
                       help='Patterns to exclude from topology check (default: maze/)')
    
    args = parser.parse_args()
    
    if not args.adventure_path.exists():
        print(f"Error: Path does not exist: {args.adventure_path}")
        return 1
    
    validator = RoomValidator(verbose=args.verbose)
    results = validator.validate_adventure(args.adventure_path, fix=args.fix)
    
    # YAML file classification scan
    if args.scan:
        scan_results = scan_yaml_files(args.adventure_path, args.verbose)
    
    # Topology verification
    if args.topology:
        one_way = verify_topology(args.adventure_path, args.verbose, args.exclude)
    
    # Return non-zero if there are unfixed errors
    unfixed = results['errors'] - results['fixed']
    return 0 if unfixed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
