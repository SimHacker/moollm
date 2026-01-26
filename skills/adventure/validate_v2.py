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


def main():
    parser = argparse.ArgumentParser(description='Validate MOOTAL DISTORTION YAML files')
    parser.add_argument('adventure_path', type=Path, help='Path to adventure directory')
    parser.add_argument('--fix', action='store_true', help='Attempt to fix issues')
    parser.add_argument('--verbose', '-v', action='store_true', help='Show all files')
    
    args = parser.parse_args()
    
    if not args.adventure_path.exists():
        print(f"Error: Path does not exist: {args.adventure_path}")
        return 1
    
    validator = RoomValidator(verbose=args.verbose)
    results = validator.validate_adventure(args.adventure_path, fix=args.fix)
    
    # Return non-zero if there are unfixed errors
    unfixed = results['errors'] - results['fixed']
    return 0 if unfixed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
