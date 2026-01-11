#!/usr/bin/env python3
"""
test_adventure.py — Test suite for MOOLLM Adventure Runtime
═══════════════════════════════════════════════════════════════════════════════

Run with: python test_adventure.py
Or: python -m pytest test_adventure.py -v

═══════════════════════════════════════════════════════════════════════════════
"""

import sys
import json
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from adventure_runtime import (
    AdventureEngine, WorldState, Room, Exit, GameObject, Character,
    setup_logging, LogLevel, logger
)


# ═══════════════════════════════════════════════════════════════════════════════
# TEST DATA
# ═══════════════════════════════════════════════════════════════════════════════

MINIMAL_ADVENTURE = {
    "name": "Test Adventure",
    "version": "1.0",
    "starting_room": "start",
    "initial_flags": {"test_flag": True},
    "rooms": [
        {
            "id": "start",
            "name": "Starting Room",
            "description": "You are in a small room.",
            "exits": {
                "north": {"destination": "north-room", "description": "A door to the north"},
                "south": {"destination": "south-room", "description": "A door to the south"}
            }
        },
        {
            "id": "north-room",
            "name": "North Room",
            "description": "You are in the north room.",
            "exits": {
                "south": {"destination": "start", "description": "Back to start"}
            }
        },
        {
            "id": "south-room",
            "name": "South Room", 
            "description": "You are in the south room.",
            "exits": {
                "north": {"destination": "start", "description": "Back to start"}
            }
        }
    ],
    "objects": [
        {
            "id": "key",
            "name": "Brass Key",
            "description": "A shiny brass key.",
            "emoji": "🔑",
            "location": "start",
            "portable": True,
            "advertisements": {
                "EXAMINE": {
                    "description": "Look at the key",
                    "score": 50,
                    "effect": "It's a small brass key."
                }
            }
        },
        {
            "id": "table",
            "name": "Wooden Table",
            "description": "A sturdy wooden table.",
            "location": "start",
            "portable": False
        }
    ],
    "characters": []
}


# ═══════════════════════════════════════════════════════════════════════════════
# TEST FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def test_load_adventure():
    """Test loading an adventure."""
    print("\n=== test_load_adventure ===")
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    assert engine.ready, "Engine should be ready after load"
    assert len(engine.world.rooms) == 3, f"Expected 3 rooms, got {len(engine.world.rooms)}"
    assert len(engine.world.objects) == 2, f"Expected 2 objects, got {len(engine.world.objects)}"
    assert engine.world.player is not None, "Player should be created"
    assert engine.world.current_room is not None, "Current room should be set"
    assert engine.world.current_room.id == "start", f"Should start in 'start', not '{engine.world.current_room.id}'"
    
    print("✓ Adventure loaded successfully")
    return True


def test_navigation():
    """Test movement between rooms."""
    print("\n=== test_navigation ===")
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    # Check starting position
    assert engine.world.current_room.id == "start"
    
    # Go north
    result = engine.command("north")
    assert result['success'], f"Go north failed: {result['message']}"
    assert engine.world.current_room.id == "north-room", f"Should be in north-room, not {engine.world.current_room.id}"
    
    # Go back south
    result = engine.command("south")
    assert result['success'], f"Go south failed: {result['message']}"
    assert engine.world.current_room.id == "start"
    
    # Try invalid direction
    result = engine.command("west")
    assert not result['success'], "West should fail"
    
    print("✓ Navigation works correctly")
    return True


def test_inventory():
    """Test picking up and dropping items."""
    print("\n=== test_inventory ===")
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    # Check inventory is empty
    result = engine.command("inventory")
    assert "nothing" in result['message'].lower(), "Inventory should be empty"
    
    # Take the key
    result = engine.command("take key")
    assert result['success'], f"Take key failed: {result['message']}"
    
    # Check inventory has key
    result = engine.command("inventory")
    assert "key" in result['message'].lower(), "Key should be in inventory"
    
    # Try to take non-portable table
    result = engine.command("take table")
    assert not result['success'], "Should not be able to take table"
    
    # Drop key
    result = engine.command("drop key")
    assert result['success'], f"Drop key failed: {result['message']}"
    
    # Check inventory empty again
    result = engine.command("inventory")
    assert "nothing" in result['message'].lower(), "Inventory should be empty after drop"
    
    print("✓ Inventory works correctly")
    return True


def test_examine():
    """Test examining objects."""
    print("\n=== test_examine ===")
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    # Examine key
    result = engine.command("examine key")
    assert result['success'], f"Examine key failed: {result['message']}"
    assert "brass" in result['message'].lower(), "Should describe the key"
    
    # Examine non-existent thing
    result = engine.command("examine unicorn")
    assert not result['success'], "Should fail to examine unicorn"
    
    print("✓ Examine works correctly")
    return True


def test_state_export_import():
    """Test exporting and importing state."""
    print("\n=== test_state_export_import ===")
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    # Make some changes
    engine.command("north")
    engine.command("take key")  # This will fail since key is in start
    engine.world.set_flag("custom_flag", True)
    
    # Export state
    state = engine.export_state()
    
    assert state['_meta']['type'] == 'adventure-state'
    assert state['player']['location'] == 'north-room'
    assert state['flags']['custom_flag'] == True
    
    # Create new engine and import
    engine2 = AdventureEngine()
    engine2.load(MINIMAL_ADVENTURE)
    engine2.import_state(state)
    
    assert engine2.world.current_room.id == 'north-room', "Should be in north-room after import"
    assert engine2.world.get_flag('custom_flag') == True, "Custom flag should be restored"
    
    print("✓ State export/import works correctly")
    return True


def test_look():
    """Test look command."""
    print("\n=== test_look ===")
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    # Look at room
    result = engine.command("look")
    assert result['success']
    assert "small room" in result['message'].lower()
    
    # Look should show objects
    assert "key" in result['message'].lower() or "table" in result['message'].lower()
    
    print("✓ Look works correctly")
    return True


def test_aliases():
    """Test command aliases."""
    print("\n=== test_aliases ===")
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    # Test 'l' for look
    result = engine.command("l")
    assert result['success'], "'l' should work as look"
    
    # Test 'i' for inventory  
    result = engine.command("i")
    assert result['success'], "'i' should work as inventory"
    
    # Test 'n' for north
    result = engine.command("n")
    assert result['success'], "'n' should work as north"
    
    print("✓ Aliases work correctly")
    return True


def test_debug_logging():
    """Test debug logging."""
    print("\n=== test_debug_logging ===")
    
    # Enable debug logging
    setup_logging(LogLevel.DEBUG)
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    # This should produce debug output
    engine.command("north")
    engine.command("south")
    
    # Reset to info
    setup_logging(LogLevel.INFO)
    
    print("✓ Debug logging works")
    return True


def test_error_handling():
    """Test error handling."""
    print("\n=== test_error_handling ===")
    
    engine = AdventureEngine()
    
    # Try commands before loading
    result = engine.command("look")
    assert not result['success'], "Should fail before loading"
    
    # Load empty adventure
    engine.load({"name": "Empty", "rooms": [], "objects": [], "characters": []})
    
    # Try look with no room
    result = engine.command("look")
    # Should not crash
    
    print("✓ Error handling works")
    return True


def test_exits_command():
    """Test exits command."""
    print("\n=== test_exits_command ===")
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    result = engine.command("exits")
    assert result['success']
    assert "north" in result['message'].lower()
    assert "south" in result['message'].lower()
    
    print("✓ Exits command works")
    return True


def test_stats_command():
    """Test stats command."""
    print("\n=== test_stats_command ===")
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    result = engine.command("stats")
    assert result['success']
    assert "Turn:" in result['message']
    assert "Rooms: 3" in result['message']
    
    print("✓ Stats command works")
    return True


def test_save_load_commands():
    """Test save and load commands."""
    print("\n=== test_save_load_commands ===")
    
    import tempfile
    import os
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    # Move and make changes
    engine.command("north")
    engine.world.set_flag("test_save", True)
    
    # Save
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        save_path = f.name
    
    result = engine.command(f"save {save_path}")
    assert result['success'], f"Save failed: {result['message']}"
    
    # Create new engine and load
    engine2 = AdventureEngine()
    engine2.load(MINIMAL_ADVENTURE)
    
    result = engine2.command(f"load {save_path}")
    assert result['success'], f"Load failed: {result['message']}"
    
    # Verify state was restored
    assert engine2.world.current_room.id == 'north-room'
    assert engine2.world.get_flag('test_save') == True
    
    # Cleanup
    os.unlink(save_path)
    
    print("✓ Save/Load commands work")
    return True


def test_empty_command():
    """Test empty command handling."""
    print("\n=== test_empty_command ===")
    
    engine = AdventureEngine()
    engine.load(MINIMAL_ADVENTURE)
    
    result = engine.command("")
    assert not result['success']
    assert "What?" in result['message']
    
    result = engine.command("   ")
    assert not result['success']
    
    print("✓ Empty command handled")
    return True


# ═══════════════════════════════════════════════════════════════════════════════
# TEST RUNNER
# ═══════════════════════════════════════════════════════════════════════════════

def run_all_tests():
    """Run all tests."""
    print("=" * 60)
    print("MOOLLM Adventure Runtime Test Suite")
    print("=" * 60)
    
    tests = [
        test_load_adventure,
        test_navigation,
        test_inventory,
        test_examine,
        test_state_export_import,
        test_look,
        test_aliases,
        test_debug_logging,
        test_error_handling,
        test_exits_command,
        test_stats_command,
        test_save_load_commands,
        test_empty_command,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
                print(f"✗ {test.__name__} returned False")
        except Exception as e:
            failed += 1
            print(f"✗ {test.__name__} raised exception: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


if __name__ == '__main__':
    # Suppress normal output during tests
    setup_logging(LogLevel.WARN)
    
    success = run_all_tests()
    sys.exit(0 if success else 1)
