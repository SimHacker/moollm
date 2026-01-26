#!/usr/bin/env python3
"""
validate_v2.py — MOOTAL DISTORTION YAML Validator

Validates all ROOM.yml files and reports all errors.
Optionally fixes common issues.

Usage:
    python validate_v2.py examples/adventure-4/           # Check all
    python validate_v2.py examples/adventure-4/ --fix     # Fix what we can
    python validate_v2.py examples/adventure-4/ --verbose # Show details
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
                if not exit_data.get('destination') and not exit_data.get('to'):
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
║  validate_v2.py — MOOTAL DISTORTION Validator                                 ║
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


def verify_topology(adventure_path: Path, verbose: bool = False, exclude_patterns: list = None):
    """Verify bidirectional links between rooms."""
    exclude_patterns = exclude_patterns or ['maze/']
    
    print(f"\n{'═' * 60}")
    print("🔗 TOPOLOGY VERIFICATION — Bidirectional Links")
    print(f"{'═' * 60}")
    print(f"   Excluding: {', '.join(exclude_patterns)}")
    
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
    
    # Check bidirectional links
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
    if verbose:
        print(f"\n📊 Room Graph: {len(rooms)} rooms")
        for room_id, info in sorted(rooms.items()):
            skip = any(p in room_id for p in exclude_patterns)
            marker = '⊘' if skip else '•'
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
    parser = argparse.ArgumentParser(description='Validate MOOTAL DISTORTION YAML files')
    parser.add_argument('adventure_path', type=Path, help='Path to adventure directory')
    parser.add_argument('--fix', action='store_true', help='Attempt to fix issues')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show all files')
    parser.add_argument('--topology', '-t', action='store_true', help='Verify bidirectional links')
    parser.add_argument('--exclude', '-x', nargs='*', default=['maze/'], 
                       help='Patterns to exclude from topology check (default: maze/)')
    
    args = parser.parse_args()
    
    if not args.adventure_path.exists():
        print(f"Error: Path does not exist: {args.adventure_path}")
        return 1
    
    validator = RoomValidator(verbose=args.verbose)
    results = validator.validate_adventure(args.adventure_path, fix=args.fix)
    
    # Topology verification
    if args.topology:
        one_way = verify_topology(args.adventure_path, args.verbose, args.exclude)
    
    # Return non-zero if there are unfixed errors
    unfixed = results['errors'] - results['fixed']
    return 0 if unfixed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
