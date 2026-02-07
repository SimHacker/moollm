#!/usr/bin/env python3
"""
adventure.py: Lint and compile MOOLLM adventures.

Sniff the end of this file for the tribute stash and lineage notes.

Usage:
  python adventure.py lint <adventure-path> [options]
  python adventure.py compile <adventure-path> [options]
  python adventure.py merge <adventure-path> <state.json> [options]
  python adventure.py serve <adventure-path>

Examples:
  python adventure.py lint examples/adventure-4/ --format yaml --dump
  python adventure.py compile examples/adventure-4/ --output build/
"""

from __future__ import annotations

import argparse
import sys
import os
import re
import json
import yaml
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Any, Optional, Union
from datetime import datetime
from enum import Enum, auto


def main() -> int:
    """Main entry point — CLI structure only."""
    parser = argparse.ArgumentParser(
        description=__doc__.splitlines()[0],
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    lint_parser = subparsers.add_parser("lint", help="Validate an adventure, emit events")
    lint_parser.add_argument("path", help="Adventure directory path")
    lint_parser.add_argument("--format", choices=["yaml", "json", "md", "html"], default="yaml")
    lint_parser.add_argument("--dump", action="store_true", help="Include full world state")
    lint_parser.add_argument("--dump-only", action="store_true", help="Only dump world state")
    lint_parser.add_argument("--summary", action="store_true", help="Only show summary counts")
    lint_parser.add_argument("--output", help="Write report to file")
    lint_parser.add_argument("--album", help="Generate Sims-style HTML album")

    compile_parser = subparsers.add_parser("compile", help="Generate web application")
    compile_parser.add_argument("path", help="Adventure directory path")
    compile_parser.add_argument("--output", help="Output directory")
    compile_parser.add_argument("--standalone", action="store_true", help="Embed runtime in HTML")

    merge_parser = subparsers.add_parser("merge", help="Merge runtime state back to YAML")
    merge_parser.add_argument("path", help="Adventure directory path")
    merge_parser.add_argument("state", help="State JSON path")
    merge_parser.add_argument("--dry-run", action="store_true", help="Show changes without writing")
    merge_parser.add_argument("--output", help="Write merge instructions to file")

    serve_parser = subparsers.add_parser("serve", help="Development server (coming soon)")
    serve_parser.add_argument("path", help="Adventure directory path")

    args = parser.parse_args()
    return _dispatch(args)


def _dispatch(args: argparse.Namespace) -> int:
    """Route to appropriate handler."""
    if args.command == "lint":
        lint_args = [args.path]
        if args.format:
            lint_args += ["--format", args.format]
        if args.dump:
            lint_args.append("--dump")
        if args.dump_only:
            lint_args.append("--dump-only")
        if args.summary:
            lint_args.append("--summary")
        if args.output:
            lint_args += ["--output", args.output]
        if args.album:
            lint_args += ["--album", args.album]
        return cmd_lint(lint_args)
    if args.command == "compile":
        compile_args = [args.path]
        if args.output:
            compile_args += ["--output", args.output]
        if args.standalone:
            compile_args.append("--standalone")
        return cmd_compile(compile_args)
    if args.command == "merge":
        merge_args = [args.path, args.state]
        if args.dry_run:
            merge_args.append("--dry-run")
        if args.output:
            merge_args += ["--output", args.output]
        return cmd_merge(merge_args)
    if args.command == "serve":
        return cmd_serve([args.path])
    print(f"Unknown command: {args.command}")
    return 1


# PART 1: EVENT SYSTEM
#
# Events are messages to the LLM. The linter DESCRIBES what it found.
# The LLM INTERPRETS the findings and generates code or fixes.
#
# "Let a million message schemas bloom and a gazillion messages flow!"
#     — Chuck Shotton, on message-based architecture
#

class EventSeverity(Enum):
    """
    Severity levels for linting events.
    
    INSIGHT from Marvin Minsky on Society of Mind:
    "Not every agent needs to shout. Some whisper. Some suggest.
     The severity is a volume knob on the agent's voice."
    """
    DEBUG = auto()      # Whisper — only when you really want to know
    INFO = auto()       # Normal voice — "I noticed this"
    WARNING = auto()    # Raised voice — "You should probably know this"
    ERROR = auto()      # Shout — "This is broken"
    FATAL = auto()      # Alarm — "I cannot continue"


class EventType(Enum):
    """
    Categories of events the linter can emit.
    
    DESIGN INSIGHT from Gary Drescher's Schema Mechanism:
    Each event is a RESULT in the Context → Action → Result loop.
    The LLM learns what to DO about each event type.
    """
    # === Discovery Events ===
    # "I found something!"
    FOUND_ADVENTURE = auto()    # Located ADVENTURE.yml
    FOUND_ROOM = auto()         # Located a ROOM.yml
    FOUND_OBJECT = auto()       # Located an object file
    FOUND_CHARACTER = auto()    # Located a CHARACTER.yml
    FOUND_CARD = auto()         # Located a CARD.yml
    FOUND_EXIT = auto()         # Found a navigation link
    
    # === Validation Events ===
    # "I checked this and..."
    VALID_SCHEMA = auto()       # Schema validates correctly
    INVALID_SCHEMA = auto()     # Schema has problems
    MISSING_REQUIRED = auto()   # Required field is absent
    TYPE_MISMATCH = auto()      # Field has wrong type
    
    # === Reference Events ===
    # "This points to that..."
    VALID_REFERENCE = auto()    # Reference resolves
    BROKEN_REFERENCE = auto()   # Reference doesn't resolve
    CIRCULAR_REFERENCE = auto() # A references B references A
    
    # === Compilation Requests ===
    # "I need the LLM to generate code for this!"
    #
    # DESIGN from the Pie Table Symposium:
    # The linter finds expressions in natural language and asks
    # the LLM to compile them into executable JavaScript/Python.
    #
    COMPILE_EXPRESSION = auto()     # "player has the key" → JS/PY
    COMPILE_SCORE = auto()          # Score calculation needed
    COMPILE_GUARD = auto()          # Condition check needed
    COMPILE_ACTION = auto()         # Action handler needed
    COMPILE_DIALOGUE = auto()       # Dialogue tree needed
    
    # === Style Events ===
    # "This works but could be better..."
    STYLE_SUGGESTION = auto()   # Naming, formatting, convention
    MISSING_DOCUMENTATION = auto()  # No README or description
    
    # === Connection Events ===
    # "Here's how things link together..."
    ROOM_TOPOLOGY = auto()      # Map of room connections
    OBJECT_HIERARCHY = auto()   # Parent/child relationships
    CHARACTER_LOCATIONS = auto()# Where everyone is
    
    # === Directory Structure Events ===
    # "Every directory must declare what it is..."
    MISSING_TYPE_DECLARATION = auto()  # Directory without ROOM.yml, CHARACTER.yml, etc.
    ORPHAN_DIRECTORY = auto()          # Directory with children but no declaration
    
    # === File Type Detection Events ===
    # "I found a file but I'm not sure what it is..."
    UNKNOWN_FILE_TYPE = auto()         # YML file with unrecognized structure
    INFERRED_FILE_TYPE = auto()        # YML file type was inferred from content
    FOUND_NARRATIVE = auto()           # MD file recognized as narrative/documentation
    IGNORED_FILE = auto()              # File has lint_ignore: true


@dataclass
class LintEvent:
    """
    A single event from the linter.
    
    DESIGN: Events are YAML Jazz — human-readable messages that
    carry semantic meaning. The LLM reads these and decides what to do.
    
    "The event is a letter to your future self (or your AI partner)
     explaining what you discovered and what might need attention."
        — Don Hopkins, on YAML Jazz
    
    DUAL RUNTIME RULE: We ALWAYS generate BOTH _js AND _py code.
    Python for server/testing, JavaScript for browser. Never one without the other.
    
    "Test in Python, deploy to browser. Same semantics, both targets."
        — Vanessa Freudenberg (memorial voice)
    
    Fields with `_js` or `_py` suffix are for COMPILED expressions:
    The natural language lives in the base field, the code in the suffix.
    
    Example:
        condition: "player has visited the kitchen"
        condition_js: "(world) => world.player.rooms_visited.includes('kitchen/')"
        condition_py: "lambda world: 'kitchen/' in world.player.rooms_visited"
    """
    type: EventType
    severity: EventSeverity
    path: str                   # File path where this was found
    message: str                # Human-readable description
    
    # Location within file (optional)
    line: Optional[int] = None
    column: Optional[int] = None
    
    # The data that triggered this event
    data: Optional[dict] = None
    
    # For COMPILE_* events: the source expression
    source_expression: Optional[str] = None
    source_field: Optional[str] = None      # e.g., "guard.allows_entry"
    target_field_js: Optional[str] = None   # e.g., "guard.allows_entry_js"
    target_field_py: Optional[str] = None   # e.g., "guard.allows_entry_py"
    expected_type: Optional[str] = None     # e.g., "boolean", "number", "action"
    
    # Context for the LLM
    context: Optional[str] = None           # Surrounding YAML for understanding
    
    # Runtime context: tells LLM what code to generate
    # Points to the execution engines and available functions
    runtime_context: Optional[dict] = None
    # Example:
    # {
    #   'closure_param': 'world',
    #   'subject': 'object',  # Who is "I"? object, player, npc
    #   'available_functions': {
    #     'subjective': ['i_have', 'i_am', 'i_get', 'i_set', 'i_emit', ...],
    #     'global': ['emit', 'flag', 'set_flag', 'trigger_event', ...],
    #     'effective': ['reset_effective', 'get_effective', 'modify_effective'],
    #   },
    #   'state_path_js': 'world.object.state',
    #   'state_path_py': 'world.object.state',
    #   'skill_refs': ['skills/subjective/', 'skills/runtime/', 'skills/context/'],
    # }
    
    # Suggestion (if any)
    suggestion: Optional[str] = None
    
    def to_dict(self) -> dict:
        """Convert to dictionary, filtering None values."""
        result = {
            'type': self.type.name,
            'severity': self.severity.name,
            'path': self.path,
            'message': self.message,
        }
        for key in ['line', 'column', 'data', 'source_expression', 
                    'source_field', 'target_field_js', 'target_field_py',
                    'expected_type', 'context', 'suggestion', 'runtime_context']:
            val = getattr(self, key)
            if val is not None:
                result[key] = val
        return result
    
    def to_yaml(self) -> str:
        """
        Render as YAML for human reading and LLM consumption.
        
        "YAML is semantic prose. The comments are data.
         The whitespace is meaning. The structure is thought."
            — Don Hopkins, YAML Jazz manifesto
        """
        return yaml.dump(self.to_dict(), default_flow_style=False, sort_keys=False)


@dataclass
class LintReport:
    """
    Complete report from a linting session.
    
    DESIGN from Ben Shneiderman's Golden Rules:
    "Offer informative feedback."
    
    The report tells you what happened and what to do next.
    """
    adventure_path: Path
    timestamp: str
    events: list[LintEvent] = field(default_factory=list)
    
    # Summaries
    rooms_found: int = 0
    objects_found: int = 0
    characters_found: int = 0
    errors: int = 0
    warnings: int = 0
    compile_requests: int = 0
    
    def add_event(self, event: LintEvent):
        """Add an event and update counters."""
        self.events.append(event)
        if event.severity == EventSeverity.ERROR:
            self.errors += 1
        elif event.severity == EventSeverity.WARNING:
            self.warnings += 1
        if event.type.name.startswith('COMPILE_'):
            self.compile_requests += 1
    
    def to_dict(self) -> dict:
        return {
            'adventure_path': str(self.adventure_path),
            'timestamp': self.timestamp,
            'summary': {
                'rooms_found': self.rooms_found,
                'objects_found': self.objects_found,
                'characters_found': self.characters_found,
                'errors': self.errors,
                'warnings': self.warnings,
                'compile_requests': self.compile_requests,
            },
            'events': [e.to_dict() for e in self.events]
        }
    
    def to_yaml(self) -> str:
        return yaml.dump(self.to_dict(), default_flow_style=False, sort_keys=False)


# PART 2: DATA MODEL
#
# Dataclasses that preserve unknown fields for round-trip safety.
#
# "The YAML is the single source of truth. The Python is just a view."
#     — Symposium consensus
#
# DESIGN from Barbara Liskov on abstraction barriers:
# "A good abstraction tells you what you need to know,
#  and hides what you don't need to know — but doesn't LOSE it."
#
# We preserve ALL fields, even ones we don't understand, so the YAML
# round-trips perfectly. Unknown fields are stored in `_extra`.
#

@dataclass
class YAMLObject:
    """
    Base class for all YAML-backed objects.
    
    CRITICAL DESIGN: Preserves unknown fields in `_extra`.
    
    This follows the Postel Principle:
    "Be liberal in what you accept, conservative in what you emit."
        — Jon Postel, RFC 761 (1980)
    
    Extended for YAML Jazz:
    "Accept unknown fields gracefully. Emit them unchanged.
     The future might understand what you don't."
        — MOOLLM Protocol
    """
    _source_path: Optional[Path] = field(default=None, repr=False)
    _extra: dict = field(default_factory=dict, repr=False)
    _raw_yaml: Optional[str] = field(default=None, repr=False)
    
    @classmethod
    def from_yaml(cls, data: dict, source_path: Optional[Path] = None):
        """
        Create from YAML dict, preserving unknown fields.
        
        Unknown fields go into _extra, not discarded.
        This is CRITICAL for round-trip safety.
        """
        known_fields = {f.name for f in cls.__dataclass_fields__.values()
                       if not f.name.startswith('_')}
        
        kwargs = {}
        extra = {}
        
        for key, value in data.items():
            if key in known_fields:
                kwargs[key] = value
            else:
                extra[key] = value
        
        kwargs['_source_path'] = source_path
        kwargs['_extra'] = extra
        
        return cls(**kwargs)
    
    def to_dict(self) -> dict:
        """
        Convert back to dict, INCLUDING unknown fields.
        
        Round-trip safety: what came in, goes out.
        """
        result = {}
        for f in self.__dataclass_fields__.values():
            if f.name.startswith('_'):
                continue
            val = getattr(self, f.name)
            if val is not None:
                result[f.name] = val
        
        # Merge back the unknown fields
        result.update(self._extra)
        return result


@dataclass 
class Exit(YAMLObject):
    """
    A navigation link between rooms.
    
    PIE MENU TOPOLOGY (Don Hopkins):
    - N/S/E/W are "highway" links to major rooms
    - NW/NE/SW/SE are "grid" links to expandable sub-rooms
    - UP/DOWN/IN/OUT for special transitions
    
    "Every exit is a promise of adventure."
    """
    destination: str = ""           # Path to target room
    description: str = ""           # What the player sees
    direction: str = ""             # N, S, E, W, NE, NW, SE, SW, UP, DOWN, etc.
    
    # Guards (optional conditions)
    guard: Optional[str] = None     # Natural language: "player has key"
    guard_js: Optional[str] = None  # Compiled: "(ctx) => ctx.inventory.has('key')"
    guard_py: Optional[str] = None  # Compiled: "lambda ctx: 'key' in ctx.inventory"
    
    locked: bool = False
    hidden: bool = False
    
    # Flavor
    note: Optional[str] = None
    hint: Optional[str] = None


@dataclass
class Advertisement(YAMLObject):
    """
    An action that an object offers.
    
    THE SIMS ARCHITECTURE (Will Wright / SimAntics):
    Objects advertise what they can do. Characters choose the best option.
    This inverts traditional AI: the environment IS the intelligence.
    
    "In The Sims, the toilet is smarter than the person.
     The toilet knows when it needs to be flushed.
     The person just wanders around waiting to be told."
        — Will Wright, GDC talk
    
    SCORE SYSTEM:
    - Base score: How good is this action in general? (0-100)
    - score_if: Natural language condition for when to boost score
    - score_if_js: Compiled condition
    - The highest-scoring available action wins
    """
    name: str = ""                  # Action name (verb)
    description: str = ""           # What this action does
    
    # Scoring (SimAntics-style)
    score: int = 50                 # Base attractiveness (0-100)
    score_if: Optional[str] = None  # "player is tired" → boost score
    score_if_js: Optional[str] = None
    score_if_py: Optional[str] = None
    
    # Guard (can you do this?)
    guard: Optional[str] = None     # "player has coins"
    guard_js: Optional[str] = None
    guard_py: Optional[str] = None
    
    # Effect (what happens)
    effect: Optional[str] = None    # Natural language effect description
    effect_js: Optional[str] = None # Compiled effect handler
    effect_py: Optional[str] = None
    
    # Params
    params: dict = field(default_factory=dict)


@dataclass
class Room(YAMLObject):
    """
    A navigable location in the adventure.
    
    MEMORY PALACE (Ancient Greece → Frances Yates → Don Hopkins):
    Rooms are locations in a memory palace. Spatial memory is powerful.
    Adventure games are mnemonic systems disguised as entertainment.
    
    "The method of loci... places items to be remembered at specific
     locations along an imagined journey through a building."
        — Frances Yates, "The Art of Memory" (1966)
    
    PIE MENU TOPOLOGY:
    - Each room is an 8-direction hub
    - Cardinal directions (N/S/E/W) link to major rooms
    - Diagonal directions (NW/NE/SW/SE) link to grid sub-rooms
    - grids can be CONTINUOUS (connected) or PRIVATE (isolated)
    """
    name: str = ""
    type: str = "room"
    description: str = ""
    examine: str = ""
    
    # Navigation
    exits: dict[str, Union[Exit, dict, str]] = field(default_factory=dict)
    
    # Contents
    objects: list[str] = field(default_factory=list)  # Paths to object files
    sub_rooms: list[str] = field(default_factory=list)
    
    # Atmosphere (for LLM narration)
    atmosphere: str = ""
    lighting: str = "normal"
    
    # Working set (for MOOLLM context)
    working_set: list[str] = field(default_factory=list)
    context: list[str] = field(default_factory=list)
    
    # Framing (from representation-ethics)
    framing: Optional[dict] = None
    
    # Grid topology (for pie menu grids)
    grid_mode: str = "private"  # "continuous" or "private"
    grid_rules: Optional[dict] = None
    
    # Theme (for themeable rooms like the pub)
    theme: Optional[dict] = None


@dataclass
class Object(YAMLObject):
    """
    An interactable thing in the world.
    
    THE SIMS OBJECT MODEL:
    Objects are NOT dumb scenery. They are SMART agents that:
    - Advertise actions they can perform
    - Calculate scores for each action
    - Execute effects when chosen
    
    "The intelligence is in the environment, not the actor."
        — SimAntics design philosophy
    
    PROTOTYPE INHERITANCE (Dave Ungar, Self):
    Objects can inherit from prototypes in skills/.
    An "object: torch" might inherit from skills/objects/light-source.yml.
    """
    id: str = ""
    name: str = ""
    type: str = "object"
    emoji: str = "📦"
    
    description: str = ""
    examine: str = ""
    
    # Properties
    takeable: bool = False      # Can player pick this up?
    container: bool = False     # Can hold other objects?
    locked: bool = False
    
    # Contents (if container)
    contains: list[str] = field(default_factory=list)
    
    # Actions this object advertises
    advertisements: dict[str, Union[Advertisement, dict]] = field(default_factory=dict)
    
    # Prototype (inheritance)
    inherits: list[str] = field(default_factory=list)
    
    # State
    state: dict = field(default_factory=dict)


@dataclass
class Character(YAMLObject):
    """
    A being in the world — player, NPC, or creature.
    
    THE SIMS (Maxis, 2000):
    Full Sims 1 personality block: traits (6), skills (7), needs (8),
    career, identity. Simple parameters → complex emergent behavior.
    
    MIND MIRROR (Timothy Leary, 1985):
    32 properties across 4 planes (Bio-Energy, Emotional Insight,
    Mental Abilities, Social Interaction). Flat structure in YAML,
    plane categories are for pedagogy and UI only.
    
    DIALOGUE TREES:
    Characters can have conversation trees with branches.
    Leaves contain expressions that affect world state.
    """
    id: str = ""
    name: str = ""
    type: str = "character"
    species: str = "human"
    
    description: str = ""
    subtitle: str = ""
    
    # Location
    location: str = ""
    
    # Personality — full Sims 1 block
    sims: Optional[dict] = None
    
    # Deeper personality — Leary Mind Mirror (flat, 32 properties)
    mind_mirror: Optional[dict] = None
    
    # Relationships
    relationships: dict = field(default_factory=dict)
    
    # Inventory
    inventory: list[str] = field(default_factory=list)
    
    # Dialogue
    dialogue: Optional[dict] = None
    
    # Voice (for LLM narration)
    voice: Optional[dict] = None
    
    # Buffs
    active_buffs: list[dict] = field(default_factory=list)
    
    # Standard Leary 32 property names
    LEARY_32 = frozenset({
        'energetic','calm','enthusiastic','restrained','cheerful','serious','easy_going','cautious',
        'forceful','docile','confident','insecure','friendly','hostile','assertive','timid',
        'well_informed','uninformed','logical','intuitive','imaginative','practical','uninhibited','inhibited',
        'moralistic','pragmatic','conventional','unconventional','trusting','suspicious','dominant','submissive',
    })
    
    # Standard sims sub-block keys
    SIMS_TRAITS = frozenset({'neat','outgoing','active','playful','nice','generous'})
    SIMS_SKILLS = frozenset({'cooking','mechanical','charisma','logic','body','creativity','cleaning'})
    SIMS_NEEDS = frozenset({'hunger','comfort','hygiene','bladder','energy','fun','social','room'})
    SIMS_CAREER = frozenset({'track','level','experience','performance'})
    SIMS_IDENTITY = frozenset({'age','gender','zodiac','aspiration'})
    SIMS_SECTIONS = frozenset({'traits','skills','needs','career','identity'})
    
    # Deprecated key names that should be renamed
    DEPRECATED_KEYS = {
        'sims_traits': 'sims.traits',
        'physical_description': 'physical',
        'nicknames': 'nickname',
        'object': 'character',
    }
    
    # Required companion files
    REQUIRED_FILES = ['CHARACTER.yml', 'CARD.yml', 'GLANCE.yml', 'README.md']


@dataclass
class Adventure(YAMLObject):
    """
    The root state of an adventure.
    
    This file IS the simulation. Reading it = loading the world.
    
    "The YAML is the save game. The YAML is the level editor.
     The YAML is the source code. The YAML is the documentation.
     Source is destination."
        — MOOLLM YAML Jazz philosophy
    """
    # Simulation state
    simulation: dict = field(default_factory=dict)
    parameters: dict = field(default_factory=dict)
    
    # Player & Party
    player: dict = field(default_factory=dict)
    party: dict = field(default_factory=dict)
    selection: dict = field(default_factory=dict)
    
    # World state
    active_buffs: list = field(default_factory=list)
    world_state: dict = field(default_factory=dict)
    flags: dict = field(default_factory=dict)
    
    # Adventure metadata
    adventure: dict = field(default_factory=dict)
    navigation: dict = field(default_factory=dict)
    evidence: dict = field(default_factory=dict)
    quest_log: list = field(default_factory=list)
    statistics: dict = field(default_factory=dict)
    
    # Theming
    seed: Optional[dict] = None


# PART 3: THE LINTER
#
# "The linter is dumb and anal-retentive. It doesn't interpret.
#  It describes what it finds and asks the LLM for help."
#     — Symposium consensus
#
# DESIGN PHILOSOPHY:
# - Walk the directory tree
# - Recognize file types by name patterns (ROOM.yml, CHARACTER.yml, etc.)
# - Parse YAML into dataclasses
# - Validate required fields
# - Find natural language expressions that need compilation
# - Emit events for everything
#
# The LLM can then:
# - Fix errors
# - Generate missing code
# - Suggest improvements
#

class AdventureLinter:
    """
    Walk an adventure directory and emit events about what we find.
    
    POSTEL PRINCIPLE IN ACTION:
    Be liberal in what you accept (any YAML, any structure).
    Be conservative in what you emit (precise, actionable events).
    """
    
    # File patterns we recognize
    PATTERNS = {
        'ADVENTURE.yml': Adventure,
        'ROOM.yml': Room,
        'CHARACTER.yml': Character,
        'CARD.yml': None,  # Generic card
    }
    
    # Fields that contain natural language expressions needing compilation
    EXPRESSION_FIELDS = [
        ('guard', 'boolean'),
        ('score_if', 'boolean'),
        ('effect', 'action'),
        ('allows_entry', 'boolean'),
        ('condition', 'boolean'),
        ('complete_when', 'boolean'),
        ('fail_when', 'boolean'),
        ('simulate', 'closure'),      # Object simulation tick
    ]
    
    # Fields that contain method maps (name → natural language)
    METHOD_MAP_FIELDS = [
        'methods',  # Object methods that simulate/advertisements can call
    ]
    
    # RUNTIME CONTEXT: Tells the LLM what code to generate
    #
    # "The linter points the LLM toward the execution engines and libraries
    #  the generated code will use, so it knows EXACTLY what to generate!"
    #     — Don Hopkins
    
    @staticmethod
    def _make_runtime_context(subject: str = 'object', expected_type: str = 'closure') -> dict:
        """
        Create runtime context that tells the LLM what code to generate.
        
        Args:
            subject: Who is "I"? 'object', 'player', 'npc', 'room'
            expected_type: What kind of expression? 'boolean', 'action', 'closure', 'method'
        
        Returns:
            dict with all the info LLM needs to generate correct code
        """
        return {
            # Closure signature
            'closure_param': 'world',
            'js_arrow': f"(world) => {'{ ... }' if expected_type in ('action', 'closure', 'method') else '...'}",
            'py_lambda': f"lambda world: ..." if expected_type == 'boolean' else "def fn(world): ...",
            
            # Who is "I"? (Subjective-oriented programming)
            'subject': subject,
            'subject_path_js': f'world.{subject}' if subject != 'player' else 'world.player',
            'subject_path_py': f'world.{subject}' if subject != 'player' else 'world.player',
            
            # Available functions by category
            'available_functions': {
                'subjective_inventory': [
                    'i_have(item_id) -> bool',
                    'i_has_tag(tag) -> bool', 
                    'i_give(item_id)',
                    'i_take(item_id)',
                    'i_drop(item_id)',
                ],
                'subjective_state': [
                    'i_am(state_key) -> bool',
                    'i_am_not(state_key) -> bool',
                    'i_get(key) -> any',
                    'i_set(key, value)',
                ],
                'subjective_communication': [
                    'i_say(message)',
                    'i_emit(message)',
                    'i_think(thought)',
                ],
                'effective_values': [
                    'reset_effective(obj)',
                    'get_effective(obj, prop) -> any',
                    'modify_effective(obj, prop, delta)',
                    'multiply_effective(obj, prop, factor)',
                ],
                'global_state': [
                    'emit(message)',
                    'flag(name) -> bool',
                    'set_flag(name, value)',
                    'trigger_event(name, data)',
                ],
                'navigation': [
                    'go(direction)',
                    'can_go(direction) -> bool',
                ],
                'buffs': [
                    'i_have_buff(buff_id) -> bool',
                    'i_add_buff(buff)',
                    'i_remove_buff(buff_id)',
                ],
            },
            
            # State access paths
            'state': {
                'object_state_js': 'world.object.state',
                'object_state_py': 'world.object.state',
                'player_state_js': 'world.player.state',
                'player_state_py': 'world.player.state',
                'adventure_flags_js': 'world.adventure.flags',
                'adventure_flags_py': 'world.adventure.flags',
            },
            
            # JS/PY naming conventions
            'naming': {
                'js_camelCase': True,  # iHave, iAm, resetEffective
                'py_snake_case': True,  # i_have, i_am, reset_effective
            },
            
            # Skill references for full documentation
            'skill_refs': [
                'skills/subjective/SKILL.md',
                'skills/runtime/SKILL.md', 
                'skills/context/CONTEXT.yml.tmpl',
                'skills/buff/EFFECTIVE-VALUES.md',
            ],
        }
    
    def __init__(self, adventure_path: Path):
        """
        Initialize the linter.
        
        adventure_path: Path to the adventure directory (e.g., examples/adventure-4/)
        """
        self.adventure_path = Path(adventure_path)
        self.report = LintReport(
            adventure_path=self.adventure_path,
            timestamp=datetime.now().isoformat()
        )
        
        # Caches
        self.rooms: dict[Path, Room] = {}
        self.objects: dict[Path, Object] = {}
        self.characters: dict[Path, Character] = {}
        self.adventure: Optional[Adventure] = None
        
    def lint(self) -> LintReport:
        """
        Main entry point: lint the entire adventure.
        
        Returns a LintReport with all findings.
        """
        print(f"🔍 Linting adventure at: {self.adventure_path}")
        print("=" * 60)
        
        # Phase 1: Discovery
        self._discover_files()
        
        # Phase 2: Validation
        self._validate_schemas()
        
        # Phase 3: Reference checking
        self._check_references()
        
        # Phase 4: Find expressions needing compilation
        self._find_expressions()
        
        # Phase 5: Map topology
        self._map_topology()
        
        # Phase 6: Check directory declarations
        self._check_directory_declarations()
        
        print("=" * 60)
        print(f"✅ Linting complete: {self.report.errors} errors, "
              f"{self.report.warnings} warnings, "
              f"{self.report.compile_requests} compile requests")
        
        return self.report
    
    # Known file types by filename
    KNOWN_FILES = {
        'ADVENTURE.yml': 'adventure',
        'ROOM.yml': 'room',
        'CHARACTER.yml': 'character',
        'CARD.yml': 'card',
        'CONTAINER.yml': 'container',   # Intermediate scope (like OpenLaszlo <node>)
        '.meta.yml': 'meta',
        # NOTE: MECHANICS.yml is DEPRECATED — mechanics are now SKILLS!
        # Old adventure-3 had MECHANICS.yml for scoring, curses, party, etc.
        # Now those live in skills/scoring/, skills/curse/, skills/party/, etc.
        # Skills can have simulate functions too!
    }
    
    # Type inference by top-level key
    TYPE_BY_KEY = {
        'room': 'room',
        'character': 'character',
        'object': 'object',
        'buff': 'buff',
        'exit': 'exit',
        'goal': 'goal',
        'card': 'card',
        'adventure': 'adventure',
        'message': 'message',
        'letter': 'letter',
        'meta': 'meta',
        'advertisement': 'advertisement',
        'container': 'container',   # OpenLaszlo-style intermediate scope
    }
    
    def _discover_files(self):
        """
        Walk the directory tree and discover all files.
        
        MEMORY PALACE METAPHOR (Frances Yates):
        We're walking through a building, noting what's in each room.
        Each file is an object placed at a locus.
        
        FILE TYPE DETECTION:
        1. Known filenames (ROOM.yml, CHARACTER.yml, etc.)
        2. Top-level key sniffing (room:, object:, buff:)
        3. MD files as narratives
        4. lint_ignore: true to suppress
        """
        print("\n📂 Phase 1: Discovery")
        
        # Counters
        narratives_found = 0
        unknown_files = 0
        ignored_files = 0
        
        # Find ADVENTURE.yml first
        adventure_file = self.adventure_path / 'ADVENTURE.yml'
        if adventure_file.exists():
            self._process_adventure(adventure_file)
        else:
            self.report.add_event(LintEvent(
                type=EventType.MISSING_REQUIRED,
                severity=EventSeverity.ERROR,
                path=str(self.adventure_path),
                message="No ADVENTURE.yml found in adventure root",
                suggestion="Create ADVENTURE.yml from the adventure template"
            ))
        
        # Walk for rooms
        for yml_file in self.adventure_path.rglob('ROOM.yml'):
            self._process_room(yml_file)
        
        # Walk for characters
        for yml_file in self.adventure_path.rglob('CHARACTER.yml'):
            self._process_character(yml_file)
        
        # Walk for personas (character subsets with blending rules)
        personas_dir = self.adventure_path / 'personas'
        if personas_dir.is_dir():
            for yml_file in personas_dir.glob('*.yml'):
                self._process_persona(yml_file)
        
        # Walk for other YAML files (objects, etc.)
        for yml_file in self.adventure_path.rglob('*.yml'):
            if yml_file.name in ['ADVENTURE.yml', 'ROOM.yml', 'CHARACTER.yml']:
                continue
            
            # Check for lint_ignore
            if self._should_ignore(yml_file):
                ignored_files += 1
                self.report.add_event(LintEvent(
                    type=EventType.IGNORED_FILE,
                    severity=EventSeverity.INFO,
                    path=str(yml_file.relative_to(self.adventure_path)),
                    message="File has lint_ignore: true"
                ))
                continue
            
            # Try to infer type
            inferred_type = self._infer_yml_type(yml_file)
            
            if inferred_type == 'yaml-error':
                # Already reported as INVALID_SCHEMA
                unknown_files += 1
                continue
            elif inferred_type:
                if inferred_type == 'object':
                    self._process_object(yml_file)
                elif inferred_type in ['buff', 'exit', 'goal', 'message', 'letter']:
                    # These are known types, process as objects with type info
                    self._process_object(yml_file, inferred_type=inferred_type)
                elif inferred_type in ['card', 'meta', 'mechanics']:
                    # Known metadata types, just note them
                    pass
                else:
                    self._process_object(yml_file)
            else:
                # Unknown type - emit warning
                unknown_files += 1
                self.report.add_event(LintEvent(
                    type=EventType.UNKNOWN_FILE_TYPE,
                    severity=EventSeverity.WARNING,
                    path=str(yml_file.relative_to(self.adventure_path)),
                    message=f"Unknown YML file type: {yml_file.name}",
                    suggestion="Add a top-level key (object:, buff:, etc.) or lint_ignore: true"
                ))
        
        # Walk for MD files (narratives, documentation)
        for md_file in self.adventure_path.rglob('*.md'):
            if self._should_ignore_md(md_file):
                continue
            
            narrative_type = self._sniff_md_type(md_file)
            narratives_found += 1
            
            self.report.add_event(LintEvent(
                type=EventType.FOUND_NARRATIVE,
                severity=EventSeverity.INFO,
                path=str(md_file.relative_to(self.adventure_path)),
                message=f"Found {narrative_type}: {md_file.name}",
                data={'narrative_type': narrative_type}
            ))
        
        print(f"   Found: {self.report.rooms_found} rooms, "
              f"{self.report.objects_found} objects, "
              f"{self.report.characters_found} characters")
        if narratives_found > 0:
            print(f"   Found: {narratives_found} narrative/doc files")
        if unknown_files > 0:
            print(f"   ⚠️ Unknown: {unknown_files} unrecognized YML files")
        if ignored_files > 0:
            print(f"   ⏭️ Ignored: {ignored_files} files with lint_ignore")
    
    def _should_ignore(self, path: Path) -> bool:
        """
        Check if a file should be ignored.
        
        Looks for lint_ignore: true in the YAML.
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                # Quick check first few lines for lint_ignore
                for i, line in enumerate(f):
                    if i > 10:  # Only check first 10 lines
                        break
                    if 'lint_ignore:' in line and 'true' in line.lower():
                        return True
                
                # Full parse check
                f.seek(0)
                data = yaml.safe_load(f)
                if isinstance(data, dict):
                    return data.get('lint_ignore', False) == True
        except:
            pass
        return False
    
    def _should_ignore_md(self, path: Path) -> bool:
        """Check if an MD file should be ignored."""
        # Skip hidden files and common non-content files
        if path.name.startswith('.'):
            return True
        if path.name in ['LICENSE.md', 'CONTRIBUTING.md', 'CHANGELOG.md']:
            return True
        return False
    
    def _infer_yml_type(self, path: Path) -> Optional[str]:
        """
        Infer the type of a YML file from its content.
        
        THE SIMS APPROACH:
        Objects declare what they are. We sniff the top-level key
        to figure out what type of thing we're looking at.
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if not isinstance(data, dict):
                return None
            
            # Check for known filename patterns
            if path.name in self.KNOWN_FILES:
                return self.KNOWN_FILES[path.name]
            
            # Check top-level keys for type hints
            for key in data.keys():
                key_lower = key.lower()
                if key_lower in self.TYPE_BY_KEY:
                    # Emit info about inferred type
                    self.report.add_event(LintEvent(
                        type=EventType.INFERRED_FILE_TYPE,
                        severity=EventSeverity.INFO,
                        path=str(path.relative_to(self.adventure_path)),
                        message=f"Inferred type '{self.TYPE_BY_KEY[key_lower]}' from key '{key}'",
                        data={'inferred_from': key}
                    ))
                    return self.TYPE_BY_KEY[key_lower]
            
            # Check if it looks like an object (has common object fields)
            object_hints = ['name', 'description', 'emoji', 'advertisements', 'state']
            if any(hint in data for hint in object_hints):
                return 'object'
            
            return None
            
        except yaml.YAMLError as e:
            # YAML syntax error - report it!
            self.report.add_event(LintEvent(
                type=EventType.INVALID_SCHEMA,
                severity=EventSeverity.ERROR,
                path=str(path.relative_to(self.adventure_path)),
                message=f"YAML syntax error: {str(e)[:100]}",
                suggestion="Fix the YAML syntax error"
            ))
            return 'yaml-error'  # Special marker
            
        except Exception as e:
            return None
    
    def _sniff_md_type(self, path: Path) -> str:
        """
        Sniff an MD file to determine what kind of narrative it is.
        
        Types:
        - README: Standard documentation
        - SESSION: Session log
        - TRANSCRIPT: Conversation transcript
        - ESSAY: Long-form writing
        - STORY: Narrative fiction
        - LOG: Event log
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                # Read first 500 chars for sniffing
                content = f.read(500).lower()
            
            name = path.name.lower()
            
            # Check filename patterns
            if 'readme' in name:
                return 'readme'
            if 'session' in name:
                return 'session-log'
            if 'transcript' in name:
                return 'transcript'
            if 'log' in name:
                return 'log'
            
            # Check content patterns
            if 'session log' in content or 'session:' in content:
                return 'session-log'
            if '**don hopkins:**' in content or '**will wright:**' in content:
                return 'dialogue'
            if '```yaml' in content or '```javascript' in content:
                return 'technical-doc'
            if '## summary' in content or '| metric |' in content:
                return 'report'
            if 'once upon' in content or 'chapter' in content:
                return 'story'
            
            # Default to generic narrative
            return 'narrative'
            
        except:
            return 'unknown'
    
    def _process_adventure(self, path: Path):
        """Process the main ADVENTURE.yml file."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                raw = f.read()
                data = yaml.safe_load(raw)
            
            self.adventure = Adventure.from_yaml(data, path)
            self.adventure._raw_yaml = raw
            
            self.report.add_event(LintEvent(
                type=EventType.FOUND_ADVENTURE,
                severity=EventSeverity.INFO,
                path=str(path.relative_to(self.adventure_path)),
                message=f"Found adventure: {data.get('adventure', {}).get('name', 'Unnamed')}",
                data={'turn': data.get('simulation', {}).get('turn', 0)}
            ))
            
        except Exception as e:
            self.report.add_event(LintEvent(
                type=EventType.INVALID_SCHEMA,
                severity=EventSeverity.ERROR,
                path=str(path),
                message=f"Failed to parse ADVENTURE.yml: {e}"
            ))
    
    def _process_room(self, path: Path):
        """Process a ROOM.yml file."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                raw = f.read()
                data = yaml.safe_load(raw)
            
            # Rooms can have 'room:' wrapper or be flat
            room_data = data.get('room', data)
            room = Room.from_yaml(room_data, path)
            room._raw_yaml = raw
            
            self.rooms[path] = room
            self.report.rooms_found += 1
            
            rel_path = path.relative_to(self.adventure_path)
            room_name = room.name or str(rel_path.parent)
            
            self.report.add_event(LintEvent(
                type=EventType.FOUND_ROOM,
                severity=EventSeverity.INFO,
                path=str(rel_path),
                message=f"Found room: {room_name}",
                data={
                    'exits': list(room.exits.keys()) if room.exits else [],
                    'objects': len(room.objects),
                    'sub_rooms': len(room.sub_rooms)
                }
            ))
            
            # Check for exits
            for direction, exit_data in (room.exits or {}).items():
                self._process_exit(path, direction, exit_data)
            
        except Exception as e:
            self.report.add_event(LintEvent(
                type=EventType.INVALID_SCHEMA,
                severity=EventSeverity.ERROR,
                path=str(path),
                message=f"Failed to parse ROOM.yml: {e}"
            ))
    
    def _process_exit(self, room_path: Path, direction: str, exit_data):
        """Process an exit definition."""
        if isinstance(exit_data, str):
            # Simple string destination
            destination = exit_data
            description = ""
        elif isinstance(exit_data, dict):
            destination = exit_data.get('destination', '')
            description = exit_data.get('description', '')
        else:
            return
        
        self.report.add_event(LintEvent(
            type=EventType.FOUND_EXIT,
            severity=EventSeverity.DEBUG,
            path=str(room_path.relative_to(self.adventure_path)),
            message=f"Exit {direction} → {destination}",
            data={'direction': direction, 'destination': destination}
        ))
    
    def _process_character(self, path: Path):
        """Process a CHARACTER.yml file with deep schema validation."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                raw = f.read()
                data = yaml.safe_load(raw)
            
            # Accept character: or object: as container, prefer character:
            char_data = data.get('character') or data.get('object') or data
            character = Character.from_yaml(char_data, path)
            character._raw_yaml = raw
            
            self.characters[path] = character
            self.report.characters_found += 1
            
            rel_path = path.relative_to(self.adventure_path)
            
            self.report.add_event(LintEvent(
                type=EventType.FOUND_CHARACTER,
                severity=EventSeverity.INFO,
                path=str(rel_path),
                message=f"Found character: {character.name or 'Unnamed'}",
                data={'species': character.species, 'location': character.location}
            ))
            
            # Deep validation
            self._validate_character(path, data, char_data, character)
            
        except Exception as e:
            self.report.add_event(LintEvent(
                type=EventType.INVALID_SCHEMA,
                severity=EventSeverity.ERROR,
                path=str(path),
                message=f"Failed to parse CHARACTER.yml: {e}"
            ))
    
    def _validate_character(self, path: Path, data: dict, char_data: dict, character: Character):
        """Deep validation of character schema, sims, mind_mirror, and companion files."""
        rel = str(path.relative_to(self.adventure_path))
        char_dir = path.parent
        
        # Check deprecated top-level key: object: should be character:
        if 'object' in data and 'character' not in data:
            self.report.add_event(LintEvent(
                type=EventType.STYLE_SUGGESTION,
                severity=EventSeverity.WARNING,
                path=rel,
                message="Uses 'object:' as container — prefer 'character:' for characters"
            ))
        
        # Check deprecated keys inside character block
        for old_key, new_key in Character.DEPRECATED_KEYS.items():
            if old_key in char_data:
                self.report.add_event(LintEvent(
                    type=EventType.STYLE_SUGGESTION,
                    severity=EventSeverity.WARNING,
                    path=rel,
                    message=f"Deprecated key '{old_key}' — rename to '{new_key}'"
                ))
        
        # Check required companion files
        for fname in Character.REQUIRED_FILES:
            if not (char_dir / fname).exists():
                self.report.add_event(LintEvent(
                    type=EventType.MISSING_REQUIRED,
                    severity=EventSeverity.WARNING,
                    path=rel,
                    message=f"Missing companion file: {fname}"
                ))
        
        # Validate sims block
        sims = char_data.get('sims') or data.get('sims')
        if not sims:
            self.report.add_event(LintEvent(
                type=EventType.MISSING_REQUIRED,
                severity=EventSeverity.WARNING,
                path=rel,
                message="Missing 'sims:' block"
            ))
        elif isinstance(sims, dict):
            character.sims = sims
            for section in Character.SIMS_SECTIONS:
                if section not in sims:
                    self.report.add_event(LintEvent(
                        type=EventType.MISSING_REQUIRED,
                        severity=EventSeverity.WARNING,
                        path=rel,
                        message=f"Missing sims.{section}"
                    ))
            # Validate trait keys
            if 'traits' in sims and isinstance(sims['traits'], dict):
                for k in sims['traits']:
                    if k not in Character.SIMS_TRAITS:
                        self.report.add_event(LintEvent(
                            type=EventType.INVALID_SCHEMA,
                            severity=EventSeverity.ERROR,
                            path=rel,
                            message=f"Unknown sims trait: '{k}' — expected {sorted(Character.SIMS_TRAITS)}"
                        ))
            # Validate skill keys
            if 'skills' in sims and isinstance(sims['skills'], dict):
                for k in sims['skills']:
                    if k not in Character.SIMS_SKILLS:
                        self.report.add_event(LintEvent(
                            type=EventType.INVALID_SCHEMA,
                            severity=EventSeverity.ERROR,
                            path=rel,
                            message=f"Unknown sims skill: '{k}'"
                        ))
            # Validate need keys
            if 'needs' in sims and isinstance(sims['needs'], dict):
                for k in sims['needs']:
                    if k not in Character.SIMS_NEEDS:
                        self.report.add_event(LintEvent(
                            type=EventType.INVALID_SCHEMA,
                            severity=EventSeverity.ERROR,
                            path=rel,
                            message=f"Unknown sims need: '{k}'"
                        ))
        
        # Validate mind_mirror
        mm = char_data.get('mind_mirror') or data.get('mind_mirror')
        if not mm:
            self.report.add_event(LintEvent(
                type=EventType.MISSING_REQUIRED,
                severity=EventSeverity.WARNING,
                path=rel,
                message="Missing 'mind_mirror:' block"
            ))
        elif isinstance(mm, dict):
            character.mind_mirror = mm
            for k in mm:
                if k not in Character.LEARY_32:
                    self.report.add_event(LintEvent(
                        type=EventType.INVALID_SCHEMA,
                        severity=EventSeverity.ERROR,
                        path=rel,
                        message=f"Non-standard mind_mirror property: '{k}' — not in Leary 32"
                    ))
            # Check values are in range 0-7
            for k, v in mm.items():
                if isinstance(v, (int, float)) and (v < 0 or v > 7):
                    self.report.add_event(LintEvent(
                        type=EventType.INVALID_SCHEMA,
                        severity=EventSeverity.WARNING,
                        path=rel,
                        message=f"mind_mirror.{k} = {v} — expected 0-7"
                    ))
    
    def _process_persona(self, path: Path):
        """Process a persona YAML file (character subset + blending rules)."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                raw = f.read()
                data = yaml.safe_load(raw)
            
            if not data or not isinstance(data, dict):
                return
            
            rel = str(path.relative_to(self.adventure_path))
            persona_data = data.get('object') or data.get('character') or data
            name = persona_data.get('name', path.stem)
            
            self.report.add_event(LintEvent(
                type=EventType.FOUND_CHARACTER,
                severity=EventSeverity.INFO,
                path=rel,
                message=f"Found persona: {name}"
            ))
            
            # Validate mind_mirror_modifiers if present
            mm_mods = persona_data.get('mind_mirror_modifiers')
            if mm_mods and isinstance(mm_mods, dict):
                for k in mm_mods:
                    if k not in Character.LEARY_32:
                        self.report.add_event(LintEvent(
                            type=EventType.INVALID_SCHEMA,
                            severity=EventSeverity.ERROR,
                            path=rel,
                            message=f"Non-standard mind_mirror_modifier: '{k}' — not in Leary 32"
                        ))
            
            # Validate sims_trait_modifiers if present
            sims_mods = persona_data.get('sims_trait_modifiers')
            if sims_mods and isinstance(sims_mods, dict):
                for k in sims_mods:
                    if k not in Character.SIMS_TRAITS:
                        self.report.add_event(LintEvent(
                            type=EventType.INVALID_SCHEMA,
                            severity=EventSeverity.ERROR,
                            path=rel,
                            message=f"Non-standard sims_trait_modifier: '{k}'"
                        ))
            
        except Exception as e:
            self.report.add_event(LintEvent(
                type=EventType.INVALID_SCHEMA,
                severity=EventSeverity.WARNING,
                path=str(path),
                message=f"Failed to parse persona: {e}"
            ))
    
    def _process_object(self, path: Path, inferred_type: Optional[str] = None):
        """
        Process a generic object YAML file.
        
        inferred_type: Optional type hint from file sniffing
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                raw = f.read()
                data = yaml.safe_load(raw)
            
            if data is None:
                return
            
            # Detect object type from top-level key
            obj_type = inferred_type  # Use inferred if provided
            obj_data = data
            
            # Check for wrapped structure
            for key in ['object', 'kitten', 'item', 'furniture', 'npc', 'card', 
                        'buff', 'exit', 'goal', 'message', 'letter']:
                if key in data:
                    obj_type = key
                    obj_data = data[key]
                    break
            
            if obj_type is None:
                # No recognized structure - still process as generic object
                obj_type = 'unknown'
                obj_data = data
            
            obj = Object.from_yaml(obj_data, path)
            obj._raw_yaml = raw
            obj.type = obj_type
            
            self.objects[path] = obj
            self.report.objects_found += 1
            
            rel_path = path.relative_to(self.adventure_path)
            
            self.report.add_event(LintEvent(
                type=EventType.FOUND_OBJECT,
                severity=EventSeverity.DEBUG,
                path=str(rel_path),
                message=f"Found {obj_type}: {obj.name or obj.id or path.stem}",
                data={
                    'type': obj_type,
                    'takeable': obj.takeable,
                    'advertisements': list(obj.advertisements.keys()) if obj.advertisements else []
                }
            ))
            
            # Check advertisements for expressions
            for action_name, action_data in (obj.advertisements or {}).items():
                self._check_advertisement(path, action_name, action_data)
            
            # Check for simulate field
            self._check_simulate(path, obj_data)
            
            # Check for methods field
            self._check_methods(path, obj_data)
            
        except Exception as e:
            # Not all YAML files are objects — silently skip parse failures
            pass
    
    def _check_advertisement(self, obj_path: Path, action_name: str, action_data):
        """Check an advertisement for expressions needing compilation."""
        if not isinstance(action_data, dict):
            return
        
        rel_path = str(obj_path.relative_to(self.adventure_path))
        
        # Check for natural language expressions that need JS/PY compilation
        for field, expected_type in self.EXPRESSION_FIELDS:
            if field in action_data:
                value = action_data[field]
                # If it's a string that looks like natural language (not already code)
                if isinstance(value, str) and not value.strip().startswith('('):
                    # Check if we already have compiled versions
                    has_js = f"{field}_js" in action_data
                    has_py = f"{field}_py" in action_data
                    
                    if not has_js or not has_py:
                        self.report.add_event(LintEvent(
                            type=EventType.COMPILE_EXPRESSION,
                            severity=EventSeverity.INFO,
                            path=rel_path,
                            message=f"Expression needs compilation: {action_name}.{field}",
                            source_expression=value,
                            source_field=f"advertisements.{action_name}.{field}",
                            target_field_js=f"advertisements.{action_name}.{field}_js",
                            target_field_py=f"advertisements.{action_name}.{field}_py",
                            expected_type=expected_type,
                            context=f"Action: {action_name}, Object: {obj_path.stem}",
                            runtime_context=self._make_runtime_context(
                                subject='object', 
                                expected_type=expected_type
                            )
                        ))
    
    def _check_simulate(self, obj_path: Path, obj_data: dict):
        """
        Check for simulate field — object's per-turn update loop.
        
        THE SIMS INSIGHT: Objects manage their own simulation!
        A lamp consumes fuel. Food spoils. The grue advances.
        """
        if 'simulate' not in obj_data:
            return
        
        rel_path = str(obj_path.relative_to(self.adventure_path))
        simulate = obj_data['simulate']
        
        if isinstance(simulate, str) and simulate.strip():
            has_js = 'simulate_js' in obj_data
            has_py = 'simulate_py' in obj_data
            
            if not has_js or not has_py:
                self.report.add_event(LintEvent(
                    type=EventType.COMPILE_EXPRESSION,
                    severity=EventSeverity.INFO,
                    path=rel_path,
                    message=f"Simulate needs compilation: {obj_path.stem}.simulate",
                    source_expression=simulate,
                    source_field="simulate",
                    target_field_js="simulate_js",
                    target_field_py="simulate_py",
                    expected_type="closure",
                    context=f"Object: {obj_path.stem} — per-turn simulation tick",
                    runtime_context=self._make_runtime_context(
                        subject='object',
                        expected_type='closure'
                    )
                ))
    
    def _check_methods(self, obj_path: Path, obj_data: dict):
        """
        Check for methods field — named behaviors that simulate can call.
        
        1:1 MAPPING: Method name in YAML = method name in JS/PY.
        consume_fuel(1) in natural language → ctx.consume_fuel(1) in code.
        """
        if 'methods' not in obj_data:
            return
        
        methods = obj_data['methods']
        if not isinstance(methods, dict):
            return
        
        rel_path = str(obj_path.relative_to(self.adventure_path))
        methods_js = obj_data.get('methods_js', {})
        methods_py = obj_data.get('methods_py', {})
        
        for method_name, method_desc in methods.items():
            if not isinstance(method_desc, str):
                continue
            
            has_js = method_name in methods_js
            has_py = method_name in methods_py
            
            if not has_js or not has_py:
                self.report.add_event(LintEvent(
                    type=EventType.COMPILE_EXPRESSION,
                    severity=EventSeverity.INFO,
                    path=rel_path,
                    message=f"Method needs compilation: {obj_path.stem}.methods.{method_name}",
                    source_expression=method_desc,
                    source_field=f"methods.{method_name}",
                    target_field_js=f"methods_js.{method_name}",
                    target_field_py=f"methods_py.{method_name}",
                    expected_type="method",
                    context=f"Object: {obj_path.stem}, Method: {method_name}",
                    runtime_context=self._make_runtime_context(
                        subject='object',
                        expected_type='method'
                    )
                ))
    
    def _validate_schemas(self):
        """
        Validate parsed objects against schema expectations.
        
        EMPATHIC TEMPLATES philosophy:
        Templates define what's REQUIRED, OPTIONAL, COMPUTED, INHERITED, ABSTRACT.
        We check for REQUIRED fields and note missing ones.
        """
        print("\n✓ Phase 2: Validation")
        
        # Check rooms have required fields
        for path, room in self.rooms.items():
            if not room.name:
                self.report.add_event(LintEvent(
                    type=EventType.MISSING_REQUIRED,
                    severity=EventSeverity.WARNING,
                    path=str(path.relative_to(self.adventure_path)),
                    message="Room missing 'name' field",
                    suggestion="Add a name to identify this room"
                ))
            if not room.description:
                self.report.add_event(LintEvent(
                    type=EventType.STYLE_SUGGESTION,
                    severity=EventSeverity.WARNING,
                    path=str(path.relative_to(self.adventure_path)),
                    message="Room missing 'description' field",
                    suggestion="Add a description for player immersion"
                ))
        
        # Check adventure has starting room
        if self.adventure:
            nav = self.adventure.navigation or {}
            starting_room = nav.get('starting_room')
            if not starting_room:
                self.report.add_event(LintEvent(
                    type=EventType.MISSING_REQUIRED,
                    severity=EventSeverity.ERROR,
                    path='ADVENTURE.yml',
                    message="Adventure missing navigation.starting_room",
                    suggestion="Set navigation.starting_room to the entry point"
                ))
    
    def _check_references(self):
        """
        Verify that references (paths) resolve to real files.
        
        "A reference is a promise. We check if promises are kept."
        """
        print("\n🔗 Phase 3: Reference checking")
        
        # Check exit destinations
        for room_path, room in self.rooms.items():
            room_dir = room_path.parent
            
            for direction, exit_data in (room.exits or {}).items():
                if isinstance(exit_data, str):
                    dest = exit_data
                elif isinstance(exit_data, dict):
                    dest = exit_data.get('destination', '')
                else:
                    continue
                
                if not dest or dest == '???':
                    continue  # Intentionally undefined
                
                # Check for external: true flag (skip validation)
                if isinstance(exit_data, dict) and exit_data.get('external'):
                    continue  # Intentional external link
                
                # Resolve path variables ($SKILLS, $KERNEL, etc.)
                if dest.startswith('$'):
                    # Path variables are external references — validated elsewhere
                    # Common: $SKILLS/ → moollm/skills/
                    var_name = dest.split('/')[0]
                    self.report.add_event(LintEvent(
                        type=EventType.INFERRED_FILE_TYPE,
                        severity=EventSeverity.DEBUG,
                        path=str(room_path.relative_to(self.adventure_path)),
                        message=f"Exit {direction} uses path variable {var_name}",
                        data={'direction': direction, 'variable': var_name}
                    ))
                    continue
                
                # Resolve relative path
                if dest.startswith('../'):
                    target = (room_dir / dest).resolve()
                elif dest.startswith('./'):
                    target = (room_dir / dest[2:]).resolve()
                else:
                    target = (room_dir / dest).resolve()
                
                if not target.exists():
                    self.report.add_event(LintEvent(
                        type=EventType.BROKEN_REFERENCE,
                        severity=EventSeverity.WARNING,
                        path=str(room_path.relative_to(self.adventure_path)),
                        message=f"Exit {direction} points to non-existent: {dest}",
                        data={'direction': direction, 'destination': dest},
                        suggestion=f"Create {dest} or update the exit"
                    ))
    
    def _find_expressions(self):
        """
        Find all natural language expressions that need compilation.
        
        THE BIG IDEA:
        Players write: guard: "player has the key"
        We compile to: guard_js: "(ctx) => ctx.inventory.includes('key')"
        
        The natural language is the specification.
        The generated code is the implementation.
        Both live side-by-side for debugging and learning.
        """
        print("\n⚙️ Phase 4: Finding expressions")
        
        # Already handled in _check_advertisement
        # This is where we'd do a deeper scan
        pass
    
    def _map_topology(self):
        """
        Build a map of room connections.
        
        PIE MENU TOPOLOGY:
        - Cardinal directions form a "web" of major locations
        - Diagonal directions form expandable "grids"
        - The map is a pie menu network!
        """
        print("\n🗺️ Phase 5: Mapping topology")
        
        connections = []
        for room_path, room in self.rooms.items():
            rel_path = str(room_path.parent.relative_to(self.adventure_path))
            
            for direction, exit_data in (room.exits or {}).items():
                if isinstance(exit_data, str):
                    dest = exit_data
                elif isinstance(exit_data, dict):
                    dest = exit_data.get('destination', '')
                else:
                    continue
                
                if dest and dest != '???':
                    connections.append({
                        'from': rel_path,
                        'direction': direction,
                        'to': dest
                    })
        
        if connections:
            self.report.add_event(LintEvent(
                type=EventType.ROOM_TOPOLOGY,
                severity=EventSeverity.INFO,
                path='',
                message=f"Room topology: {len(connections)} connections found",
                data={'connections': connections}
            ))
    
    def _check_directory_declarations(self):
        """
        Ensure every directory declares what it is.
        
        THE RULE (from Room skill):
        Every directory in an adventure MUST declare what it is:
        - Rooms/regions: ROOM.yml
        - Characters: CHARACTER.yml
        - Adventure root: ADVENTURE.yml
        - System dirs: .meta.yml or known names (inbox, outbox, messages, sessions, images)
        
        This catches orphan directories that might be intended as rooms
        but were never properly declared.
        
        REGIONS VS ROOMS:
        A region is a sub-area of a parent room (type: region in ROOM.yml).
        A sub-room is a full room that happens to be nested.
        Both need ROOM.yml!
        """
        print("\n📁 Phase 6: Checking directory declarations")
        
        # Known system directory names that don't need ROOM.yml
        SYSTEM_DIRS = {
            'inbox', 'outbox', 'messages', 'sessions', 'images', 
            'assets', 'logs', 'temp', '.git', '__pycache__',
            'node_modules', 'build', 'dist'
        }
        
        # Type declaration files we recognize
        # These files declare "this directory is a ___"
        TYPE_FILES = {
            'ROOM.yml',        # Navigable room or region
            'CHARACTER.yml',   # Character definition
            'ADVENTURE.yml',   # Adventure root
            'OBJECT.yml',      # Object container (rare at dir level)
            'MECHANICS.yml',   # Game mechanics definition
            '.meta.yml',       # Meta declaration (system, container, etc.)
        }
        
        undeclared = []
        
        # Walk all directories under adventure
        for dirpath in self.adventure_path.rglob('*'):
            if not dirpath.is_dir():
                continue
            
            # Skip hidden directories
            if any(part.startswith('.') for part in dirpath.parts):
                continue
                
            # Skip system directories
            if dirpath.name in SYSTEM_DIRS:
                continue
                
            # Skip if it's a known character directory (has CHARACTER.yml in parent hierarchy)
            # This handles characters/real-people/don-hopkins/ pattern
            relative = dirpath.relative_to(self.adventure_path)
            parts = relative.parts
            
            # Check if this directory or any parent has a type declaration
            has_declaration = False
            
            # Check for type file in this directory
            for type_file in TYPE_FILES:
                if (dirpath / type_file).exists():
                    has_declaration = True
                    break
            
            # Check if it's a leaf directory with only .yml files (object collections)
            if not has_declaration:
                children = list(dirpath.iterdir())
                # If all children are .yml files or there are no children, might be ok
                yml_children = [c for c in children if c.suffix == '.yml' and c.is_file()]
                dir_children = [c for c in children if c.is_dir()]
                
                # If this dir has subdirs with potential rooms, we need a declaration
                if dir_children:
                    # Check if any child has a ROOM.yml
                    has_room_children = False
                    room_children = []
                    for child_dir in dir_children:
                        if (child_dir / 'ROOM.yml').exists():
                            has_room_children = True
                            room_children.append(child_dir.name)
                    
                    if has_room_children:
                        # Check if parent has CONTAINER.yml (OpenLaszlo-style scope)
                        # CONTAINER.yml suppresses this warning — it's a valid scope declaration
                        if not (dirpath / 'CONTAINER.yml').exists():
                            undeclared.append({
                                'path': str(relative),
                                'has_room_children': True,
                                'child_rooms': room_children
                            })
        
        # Report findings
        for item in undeclared:
            self.report.add_event(LintEvent(
                type=EventType.MISSING_TYPE_DECLARATION,
                severity=EventSeverity.WARNING,
                path=item['path'],
                message=f"Directory has room children but no ROOM.yml or CONTAINER.yml: {item.get('child_rooms', [])}",
                data=item,
                suggestion="Add CONTAINER.yml (for inheritance) or ROOM.yml (if navigable)"
            ))
        
        if undeclared:
            print(f"   ⚠️ Found {len(undeclared)} directories without type declarations")
        else:
            print("   ✅ All directories properly declared")


# PART 4: CLI
#
# "Make it easy. Make it obvious. Make it delightful."
#     — Ben Shneiderman, paraphrased
#
# Commands:
#   adventure.py lint <path>     — Check an adventure, emit events
#   adventure.py compile <path>  — Generate web app (future)
#   adventure.py serve <path>    — Serve for development (future)
#

def cmd_lint(args):
    """
    Lint an adventure directory.
    
    Walks the directory, parses YAML, validates schemas,
    checks references, finds expressions needing compilation.
    
    THE SIMS 1 INSPIRATION:
    The Sims 1 save files would dump out everything PLUS generate
    HTML family albums you could browse! We do the same.
    
    Output formats:
      --format yaml    YAML report (default) — LLM can generate HTML from this!
      --format json    JSON for machine consumption
      --format md      Markdown summary
      --format html    Basic HTML (hint: let LLM generate beautiful HTML from YAML!)
      
    Dump options:
      --dump           Include full world state (rooms, objects, characters)
      --dump-only      Just dump world state, no events
      --summary        Just show summary counts
      
    Output destination:
      --output FILE    Write to file instead of stdout
      --album DIR      Generate Sims-style HTML album in directory
    """
    if len(args) < 1:
        print("Usage: adventure.py lint <adventure-path> [options]")
        print()
        print("Options:")
        print("  --format yaml|json|md|html  Output format (default: yaml)")
        print("  --dump                      Include full world state")
        print("  --dump-only                 Just dump world state, no lint events")
        print("  --summary                   Just show summary counts")
        print("  --output FILE               Write to file")
        print("  --album DIR                 Generate Sims-style HTML album")
        print()
        print("Example:")
        print("  adventure.py lint examples/adventure-4/")
        print("  adventure.py lint examples/adventure-4/ --format json --dump")
        print("  adventure.py lint examples/adventure-4/ --album ./album/")
        return 1
    
    adventure_path = Path(args[0])
    if not adventure_path.exists():
        print(f"Error: Path does not exist: {adventure_path}")
        return 1
    
    # Parse options
    output_format = 'yaml'
    if '--format' in args:
        idx = args.index('--format')
        if idx + 1 < len(args):
            output_format = args[idx + 1]
    
    include_dump = '--dump' in args or '--dump-only' in args
    dump_only = '--dump-only' in args
    summary_only = '--summary' in args
    
    output_path = None
    if '--output' in args:
        idx = args.index('--output')
        if idx + 1 < len(args):
            output_path = args[idx + 1]
    
    album_path = None
    if '--album' in args:
        idx = args.index('--album')
        if idx + 1 < len(args):
            album_path = Path(args[idx + 1])
    
    # Run the linter
    linter = AdventureLinter(adventure_path)
    report = linter.lint()
    
    # Build output based on options
    if album_path:
        # Generate Sims-style HTML album
        generate_album(linter, report, album_path)
        print(f"\n📸 Album generated at: {album_path}")
        return 0
    
    if output_format == 'json':
        output = generate_json_output(linter, report, include_dump, dump_only, summary_only)
    elif output_format == 'md':
        output = generate_markdown_output(linter, report, include_dump, dump_only, summary_only)
    elif output_format == 'html':
        output = generate_html_output(linter, report, include_dump)
    else:  # yaml
        output = generate_yaml_output(linter, report, include_dump, dump_only, summary_only)
    
    # Write output
    if output_path:
        with open(output_path, 'w') as f:
            f.write(output)
        print(f"\n📄 Report written to: {output_path}")
    else:
        if output_format != 'html':  # HTML is too verbose for stdout
            print("\n" + "=" * 60)
            print(f"LINT REPORT ({output_format.upper()})")
            print("=" * 60)
            print(output)
        else:
            print("\n⚠️  HTML output is large. Use --output FILE or --album DIR")
    
    return 0 if report.errors == 0 else 1


def generate_yaml_output(linter, report, include_dump, dump_only, summary_only):
    """Generate YAML output with optional world state dump."""
    if summary_only:
        return yaml.dump({
            'adventure': str(linter.adventure_path),
            'summary': {
                'rooms': report.rooms_found,
                'objects': report.objects_found,
                'characters': report.characters_found,
                'errors': report.errors,
                'warnings': report.warnings,
                'compile_requests': report.compile_requests
            }
        }, default_flow_style=False)
    
    data = report.to_dict() if not dump_only else {}
    
    if include_dump or dump_only:
        data['world_state'] = build_world_state(linter)
    
    return yaml.dump(data, default_flow_style=False, sort_keys=False)


def generate_json_output(linter, report, include_dump, dump_only, summary_only):
    """Generate JSON output with optional world state dump."""
    import json
    
    if summary_only:
        data = {
            'adventure': str(linter.adventure_path),
            'summary': {
                'rooms': report.rooms_found,
                'objects': report.objects_found,
                'characters': report.characters_found,
                'errors': report.errors,
                'warnings': report.warnings,
                'compile_requests': report.compile_requests
            }
        }
    elif dump_only:
        data = {'world_state': build_world_state(linter)}
    else:
        data = report.to_dict()
        if include_dump:
            data['world_state'] = build_world_state(linter)
    
    return json.dumps(data, indent=2, default=str)


def generate_markdown_output(linter, report, include_dump, dump_only, summary_only):
    """
    Generate Markdown output — human-friendly summary.
    
    WILL WRIGHT: "The Sims had Simlish for dialogue.
                  Markdown is our Simlish for documentation."
    """
    lines = []
    
    # Header
    # Get adventure name from the 'adventure' dict field
    if linter.adventure and linter.adventure.adventure:
        adv_name = linter.adventure.adventure.get('name', str(linter.adventure_path.name))
    else:
        adv_name = str(linter.adventure_path.name) if linter.adventure_path else 'Unknown'
    lines.append(f"# Adventure Report: {adv_name}")
    lines.append(f"")
    lines.append(f"> Generated: {report.timestamp}")
    lines.append(f"> Path: `{linter.adventure_path}`")
    lines.append(f"")
    
    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|--------|-------|")
    lines.append(f"| 🚪 Rooms | {report.rooms_found} |")
    lines.append(f"| 📦 Objects | {report.objects_found} |")
    lines.append(f"| 🧑 Characters | {report.characters_found} |")
    lines.append(f"| ❌ Errors | {report.errors} |")
    lines.append(f"| ⚠️ Warnings | {report.warnings} |")
    lines.append(f"| ⚙️ Compile Requests | {report.compile_requests} |")
    lines.append("")
    
    if summary_only:
        return '\n'.join(lines)
    
    if not dump_only:
        # Events by type
        events_by_type = {}
        for event in report.events:
            event_type = event.type.name
            if event_type not in events_by_type:
                events_by_type[event_type] = []
            events_by_type[event_type].append(event)
        
        if events_by_type:
            lines.append("## Events")
            lines.append("")
            for event_type, events in events_by_type.items():
                lines.append(f"### {event_type} ({len(events)})")
                lines.append("")
                for event in events[:5]:  # Show first 5
                    lines.append(f"- **{event.path}**: {event.message}")
                if len(events) > 5:
                    lines.append(f"- ... and {len(events) - 5} more")
                lines.append("")
    
    if include_dump or dump_only:
        lines.append("## World State")
        lines.append("")
        world = build_world_state(linter)
        
        # Rooms
        lines.append("### Rooms")
        lines.append("")
        for room_path, room_data in world.get('rooms', {}).items():
            lines.append(f"<details>")
            lines.append(f"<summary>🚪 <strong>{room_data.get('name', room_path)}</strong></summary>")
            lines.append("")
            lines.append(f"- **Path**: `{room_path}`")
            if room_data.get('description'):
                lines.append(f"- **Description**: {room_data['description']}")
            if room_data.get('exits'):
                exits_str = ', '.join(f"{d}: {p}" for d, p in room_data['exits'].items())
                lines.append(f"- **Exits**: {exits_str}")
            lines.append("")
            lines.append("</details>")
            lines.append("")
        
        # Characters
        lines.append("### Characters")
        lines.append("")
        for char_path, char_data in world.get('characters', {}).items():
            lines.append(f"- 🧑 **{char_data.get('name', char_path)}** (`{char_path}`)")
        lines.append("")
        
        # Objects
        lines.append("### Objects")
        lines.append("")
        for obj_path, obj_data in world.get('objects', {}).items():
            emoji = obj_data.get('emoji', '📦')
            lines.append(f"- {emoji} **{obj_data.get('name', obj_path)}** (`{obj_path}`)")
        lines.append("")
    
    return '\n'.join(lines)


def generate_html_output(linter, report, include_dump):
    """
    Generate BASIC HTML output — a starting point.
    
    PHILOSOPHY (from Don):
    "Let the LLM generate beautiful HTML from the YAML we produce!"
    
    This function generates a simple, functional HTML page.
    For BEAUTIFUL output, pipe the YAML/JSON to an LLM and ask it
    to generate a stunning Sims-style family album!
    
    THE BETTER WORKFLOW:
    1. adventure.py lint ... --format yaml --dump > world.yml
    2. Ask LLM: "Generate a beautiful HTML album from this YAML"
    3. LLM creates stunning, creative, context-aware HTML
    
    This basic HTML is a fallback / hint / scaffold.
    """
    world = build_world_state(linter) if include_dump else {}
    # Get adventure name from the 'adventure' dict field, or fall back to path
    if linter.adventure and linter.adventure.adventure:
        adventure_name = linter.adventure.adventure.get('name', str(linter.adventure_path.name))
    else:
        adventure_name = str(linter.adventure_path.name) if linter.adventure_path else 'Adventure'
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{adventure_name} — Adventure Album</title>
    <style>
        :root {{
            --bg: #1a1a2e;
            --surface: #16213e;
            --primary: #e94560;
            --secondary: #0f3460;
            --text: #eee;
            --muted: #888;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            padding: 2rem;
        }}
        h1 {{ color: var(--primary); margin-bottom: 0.5rem; }}
        h2 {{ color: var(--secondary); border-bottom: 2px solid var(--primary); padding-bottom: 0.5rem; margin: 2rem 0 1rem; }}
        h3 {{ color: var(--text); margin: 1rem 0 0.5rem; }}
        .header {{
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, var(--secondary), var(--bg));
            border-radius: 1rem;
            margin-bottom: 2rem;
        }}
        .stats {{
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            margin: 1rem 0;
        }}
        .stat {{
            background: var(--surface);
            padding: 1rem 2rem;
            border-radius: 0.5rem;
            text-align: center;
        }}
        .stat-value {{ font-size: 2rem; font-weight: bold; color: var(--primary); }}
        .stat-label {{ color: var(--muted); font-size: 0.9rem; }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
        }}
        .card {{
            background: var(--surface);
            border-radius: 0.5rem;
            padding: 1rem;
            border-left: 4px solid var(--primary);
        }}
        .card h4 {{ margin-bottom: 0.5rem; }}
        .card p {{ color: var(--muted); font-size: 0.9rem; }}
        .tag {{
            display: inline-block;
            background: var(--secondary);
            padding: 0.2rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 0.8rem;
            margin: 0.2rem;
        }}
        details {{ margin: 0.5rem 0; }}
        summary {{ cursor: pointer; padding: 0.5rem; background: var(--surface); border-radius: 0.25rem; }}
        details[open] summary {{ border-radius: 0.25rem 0.25rem 0 0; }}
        pre {{ background: #0d0d1a; padding: 1rem; overflow-x: auto; border-radius: 0.25rem; font-size: 0.85rem; }}
        .emoji {{ font-size: 1.5rem; margin-right: 0.5rem; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📜 {adventure_name}</h1>
        <p>Adventure Album — Generated {report.timestamp}</p>
        <div class="stats">
            <div class="stat">
                <div class="stat-value">{report.rooms_found}</div>
                <div class="stat-label">🚪 Rooms</div>
            </div>
            <div class="stat">
                <div class="stat-value">{report.objects_found}</div>
                <div class="stat-label">📦 Objects</div>
            </div>
            <div class="stat">
                <div class="stat-value">{report.characters_found}</div>
                <div class="stat-label">🧑 Characters</div>
            </div>
            <div class="stat">
                <div class="stat-value">{report.errors}</div>
                <div class="stat-label">❌ Errors</div>
            </div>
        </div>
    </div>
"""
    
    # Rooms section
    html += "    <h2>🚪 Rooms</h2>\n    <div class=\"grid\">\n"
    for room_path, room in (world.get('rooms', {}) or linter.rooms).items():
        if isinstance(room, dict):
            name = room.get('name', str(room_path))
            desc = room.get('description', '')[:100] or 'No description'
            exits = room.get('exits', {})
        else:
            name = room.name or str(room_path)
            desc = room.description[:100] if room.description else 'No description'
            exits = room.exits or {}
        
        exit_tags = ' '.join(f'<span class="tag">{d}</span>' for d in exits.keys())
        html += f"""        <div class="card">
            <h4><span class="emoji">🚪</span>{name}</h4>
            <p>{desc}</p>
            <div>{exit_tags or '<span class="tag">No exits</span>'}</div>
        </div>
"""
    html += "    </div>\n"
    
    # Characters section
    html += "\n    <h2>🧑 Characters</h2>\n    <div class=\"grid\">\n"
    for char_path, char in (world.get('characters', {}) or linter.characters).items():
        if isinstance(char, dict):
            name = char.get('name', str(char_path))
            desc = char.get('description', '')[:100] or 'No description'
        else:
            name = char.name or str(char_path)
            desc = char.description[:100] if char.description else 'No description'
        
        html += f"""        <div class="card">
            <h4><span class="emoji">🧑</span>{name}</h4>
            <p>{desc}</p>
        </div>
"""
    html += "    </div>\n"
    
    # Objects section
    html += "\n    <h2>📦 Objects</h2>\n    <div class=\"grid\">\n"
    for obj_path, obj in (world.get('objects', {}) or linter.objects).items():
        if isinstance(obj, dict):
            name = obj.get('name', str(obj_path))
            emoji = obj.get('emoji', '📦')
            desc = obj.get('description', '')[:100] or 'No description'
            tags = obj.get('tags', [])
        else:
            name = getattr(obj, 'name', str(obj_path)) or str(obj_path)
            emoji = getattr(obj, 'emoji', '📦') or '📦'
            desc = (getattr(obj, 'description', '') or '')[:100] or 'No description'
            tags = getattr(obj, 'tags', []) or []
        
        tag_html = ' '.join(f'<span class="tag">{t}</span>' for t in tags)
        html += f"""        <div class="card">
            <h4><span class="emoji">{emoji}</span>{name}</h4>
            <p>{desc}</p>
            <div>{tag_html}</div>
        </div>
"""
    html += "    </div>\n"
    
    # Events section
    html += "\n    <h2>📋 Lint Events</h2>\n"
    events_by_severity = {'ERROR': [], 'WARNING': [], 'INFO': []}
    for event in report.events:
        sev = event.severity.name if hasattr(event.severity, 'name') else str(event.severity)
        if sev in events_by_severity:
            events_by_severity[sev].append(event)
    
    for severity, events in events_by_severity.items():
        if events:
            emoji = '❌' if severity == 'ERROR' else '⚠️' if severity == 'WARNING' else 'ℹ️'
            html += f"    <details>\n        <summary>{emoji} {severity} ({len(events)})</summary>\n        <pre>"
            for event in events[:20]:
                html += f"{event.path}: {event.message}\n"
            if len(events) > 20:
                html += f"... and {len(events) - 20} more\n"
            html += "</pre>\n    </details>\n"
    
    html += """
    <footer style="margin-top: 3rem; text-align: center; color: var(--muted);">
        <p>Generated by adventure.py — The MOOLLM Adventure Compiler</p>
        <p>🥧 Inspired by The Sims 1 Family Album</p>
    </footer>
</body>
</html>
"""
    
    return html


def build_world_state(linter):
    """
    Build a complete world state dump.
    
    THE SIMS 1 SAVE FORMAT:
    The Sims saved everything — lot state, character memories,
    relationship scores, career progress, inventory.
    
    We do the same: dump EVERYTHING so you can restore or inspect.
    """
    world = {
        'adventure': None,
        'rooms': {},
        'characters': {},
        'objects': {}
    }
    
    # Adventure
    if linter.adventure:
        adv = linter.adventure
        # The adventure metadata is in the 'adventure' dict field
        adv_meta = adv.adventure or {}
        world['adventure'] = {
            'name': adv_meta.get('name', str(linter.adventure_path.name)),
            'objective': adv_meta.get('objective', ''),
            'status': adv_meta.get('status', 'active'),
            'flags': adv.flags or {},
            'world_state': adv.world_state or {},
            'player': adv.player or {},
            'party': adv.party or {},
            'simulation': adv.simulation or {},
            'quest_log': adv.quest_log or []
        }
    
    # Rooms
    for path, room in linter.rooms.items():
        rel_path = str(path.parent.relative_to(linter.adventure_path))
        world['rooms'][rel_path] = {
            'name': room.name,
            'description': room.description,
            'exits': room.exits,
            'type': room.type,
            'extra': room._extra
        }
    
    # Characters
    for path, char in linter.characters.items():
        rel_path = str(path.parent.relative_to(linter.adventure_path))
        world['characters'][rel_path] = {
            'name': char.name,
            'description': char.description,
            'species': char.species,
            'sims': char.sims,
            'mind_mirror': char.mind_mirror,
            'inventory': char.inventory,
            'location': char.location,
            'relationships': char.relationships,
            'active_buffs': char.active_buffs,
            'extra': char._extra
        }
    
    # Objects
    for path, obj in linter.objects.items():
        rel_path = str(path.relative_to(linter.adventure_path))
        world['objects'][rel_path] = {
            'name': getattr(obj, 'name', None),
            'emoji': getattr(obj, 'emoji', None),
            'description': getattr(obj, 'description', None),
            'tags': getattr(obj, 'tags', []),
            'state': getattr(obj, 'state', {}),
            'simulate': getattr(obj, 'simulate', None),
            'methods': getattr(obj, 'methods', {}),
            'advertisements': getattr(obj, 'advertisements', [])
        }
    
    return world


def generate_album(linter, report, album_path):
    """
    Generate a full Sims-style HTML album in a directory.
    
    THE SIMS 1 ALBUM:
    - Family photo page
    - Individual Sim pages
    - House tour
    - Scrapbook memories
    
    We generate:
    - index.html — Overview dashboard
    - rooms/ — Room pages
    - characters/ — Character pages
    - map.html — Topology visualization
    - objects.html — Object catalog
    """
    album_path.mkdir(parents=True, exist_ok=True)
    
    # Generate main index
    index_html = generate_html_output(linter, report, include_dump=True)
    (album_path / 'index.html').write_text(index_html)
    
    # Generate world state dumps
    world = build_world_state(linter)
    
    # YAML dump
    (album_path / 'world-state.yml').write_text(
        yaml.dump(world, default_flow_style=False, sort_keys=False)
    )
    
    # JSON dump (for loading into other tools)
    import json
    (album_path / 'world-state.json').write_text(
        json.dumps(world, indent=2, default=str)
    )
    
    # Markdown summary
    md = generate_markdown_output(linter, report, include_dump=True, dump_only=False, summary_only=False)
    (album_path / 'README.md').write_text(md)
    
    print(f"   📄 index.html — Main album page")
    print(f"   📄 world-state.yml — Full YAML dump")
    print(f"   📄 world-state.json — JSON for tools")
    print(f"   📄 README.md — Markdown summary")


def cmd_compile(args):
    """
    Compile an adventure to a web application.
    
    Generates:
    - adventure.json — Compact runtime JSON for browser/Node
    - index.html — Standalone playable page
    - Copies adventure.js runtime
    
    The JSON contains ONLY what the runtime needs:
    - Rooms with exits and progressive descriptions (glance/look/example/examine)
    - Objects with advertisements, compiled JS/PY
    - Characters with inventory, location
    - Initial flags and starting room
    
    Rooms synthesize from ROOM.yml + README.md. Objects and characters
    describe themselves; rooms do not duplicate artifact descriptions.
    All extra YAML Jazz (comments, metadata, design docs) stays in YAML.
    The runtime gets a lean, fast, stripped-down view.
    """
    if len(args) < 1:
        print("Usage: adventure.py compile <adventure-path> [options]")
        print()
        print("Options:")
        print("  --output DIR    Output directory (default: <adventure>/build/)")
        print("  --standalone    Include runtime in output (no external deps)")
        print()
        print("Example:")
        print("  adventure.py compile examples/adventure-4/")
        print("  adventure.py compile examples/adventure-4/ --output ./build/")
        return 1
    
    adventure_path = Path(args[0])
    if not adventure_path.exists():
        print(f"Error: Path does not exist: {adventure_path}")
        return 1
    
    # Parse options
    output_dir = adventure_path / 'build'
    if '--output' in args:
        idx = args.index('--output')
        if idx + 1 < len(args):
            output_dir = Path(args[idx + 1])
    
    standalone = '--standalone' in args
    
    print(f"📦 Compiling adventure: {adventure_path}")
    
    # First, lint to load and validate
    linter = AdventureLinter(adventure_path)
    linter.lint()
    
    # Check for errors
    errors = [e for e in linter.report.events if e.severity == EventSeverity.ERROR]
    if errors:
        print(f"❌ Cannot compile: {len(errors)} errors found")
        print("   Run 'lint' command to see details")
        return 1
    
    # Export to JSON
    runtime_json = export_runtime_json(linter)
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Write adventure.json
    json_path = output_dir / 'adventure.json'
    with open(json_path, 'w') as f:
        json.dump(runtime_json, f, indent=2)
    print(f"   📄 {json_path}")
    
    # Copy or generate index.html
    html_path = output_dir / 'index.html'
    runtime_dir = Path(__file__).parent
    
    if standalone:
        # Embed everything in one file
        with open(runtime_dir / 'adventure.js') as f:
            js_code = f.read()
        
        html_content = generate_standalone_html(runtime_json, js_code)
    else:
        # Reference external files
        import shutil
        shutil.copy(runtime_dir / 'adventure.js', output_dir / 'adventure.js')
        print(f"   📄 {output_dir / 'adventure.js'}")
        
        html_content = generate_index_html(runtime_json)
    
    with open(html_path, 'w') as f:
        f.write(html_content)
    print(f"   📄 {html_path}")
    
    print()
    print(f"✅ Compiled to: {output_dir}")
    print(f"   Open index.html in a browser to play!")
    
    return 0


def export_runtime_json(linter: 'AdventureLinter') -> dict:
    """
    Export adventure to compact runtime JSON.
    
    This is the bridge between rich YAML and lean runtime:
    - YAML has comments, documentation, design rationale
    - JSON has only what the runtime needs to execute
    
    The LLM reads YAML Jazz.
    The runtime eats JSON fast food.
    """
    # Get adventure name from the adventure metadata dict
    adventure_name = 'Unknown'
    if linter.adventure:
        # adventure.adventure is the metadata dict
        adventure_meta = linter.adventure.adventure or {}
        adventure_name = adventure_meta.get('name', linter.adventure_path.name)
    
    result = {
        'name': adventure_name,
        'version': '1.0',
        'generated': __import__('datetime').datetime.now().isoformat(),
        'starting_room': None,
        'initial_flags': {},
        'rooms': [],
        'objects': [],
        'characters': []
    }
    
    # Get starting room from navigation config
    if linter.adventure and linter.adventure.navigation:
        starting = linter.adventure.navigation.get('starting_room', '')
        # Normalize: remove trailing slash to match room IDs
        result['starting_room'] = starting.rstrip('/')
        result['initial_flags'] = linter.adventure.flags or {}
    
    # Export rooms
    for room_path, room in linter.rooms.items():
        room_id = str(room_path.parent.relative_to(linter.adventure_path))
        
        room_data = {
            'id': room_id,
            'name': room.name or room_id,
            'description': room.description or '',
            'exits': {},
            'atmosphere': room._extra.get('atmosphere', {})
        }
        
        # Export exits
        for direction, exit_data in (room.exits or {}).items():
            if isinstance(exit_data, str):
                room_data['exits'][direction] = {
                    'destination': exit_data
                }
            elif isinstance(exit_data, dict):
                room_data['exits'][direction] = {
                    'destination': exit_data.get('destination', ''),
                    'description': exit_data.get('description', ''),
                    'aliases': exit_data.get('aliases', []),
                    'locked': exit_data.get('locked', False),
                    'guard': exit_data.get('guard', ''),
                    'guard_js': exit_data.get('guard_js', ''),
                    'guard_py': exit_data.get('guard_py', ''),
                    'guard_fail': exit_data.get('guard_fail', '')
                }
        
        result['rooms'].append(room_data)
    
    # Export objects
    for obj_path, obj in linter.objects.items():
        obj_data = {
            'id': obj.id or str(obj_path.stem),
            'name': obj.name or obj.id or str(obj_path.stem),
            'description': obj.description or '',
            'emoji': obj._extra.get('emoji', '📦'),
            'portable': obj._extra.get('portable', True),
            'hidden': obj._extra.get('hidden', False),
            'location': str(obj_path.parent.relative_to(linter.adventure_path)),
            'advertisements': {}
        }
        
        # Export advertisements (could be dict or list)
        ads = obj.advertisements or {}
        if isinstance(ads, dict):
            for ad_name, ad_data in ads.items():
                if isinstance(ad_data, dict):
                    obj_data['advertisements'][ad_name] = {
                        'description': ad_data.get('description', ''),
                        'score': ad_data.get('score', 50),
                        'effect': ad_data.get('effect', ''),
                        'guard': ad_data.get('guard', ''),
                        'guard_js': ad_data.get('guard_js', ''),
                        'guard_py': ad_data.get('guard_py', ''),
                        'guard_fail': ad_data.get('guard_fail', ''),
                        'score_if': ad_data.get('score_if', ''),
                        'score_if_js': ad_data.get('score_if_js', ''),
                        'score_if_py': ad_data.get('score_if_py', ''),
                        'effect_js': ad_data.get('effect_js', ''),
                        'effect_py': ad_data.get('effect_py', '')
                    }
        # Handle list-style advertisements if present
        elif isinstance(ads, list):
            for i, ad_data in enumerate(ads):
                if isinstance(ad_data, dict):
                    ad_name = ad_data.get('name', f'ACTION_{i}')
                    obj_data['advertisements'][ad_name] = {
                        'description': ad_data.get('description', ''),
                        'score': ad_data.get('score', 50),
                        'effect': ad_data.get('effect', '')
                    }
        
        result['objects'].append(obj_data)
    
    # Export characters
    for char_path, char in linter.characters.items():
        char_data = {
            'id': char.id or str(char_path.stem),
            'name': char.name or char.id or str(char_path.stem),
            'description': char.description or '',
            'emoji': char._extra.get('emoji', '👤'),
            'is_player': char._extra.get('is_player', False),
            'mood': char._extra.get('mood', 'neutral'),
            'location': str(char_path.parent.relative_to(linter.adventure_path))
        }
        
        result['characters'].append(char_data)
    
    return result


def generate_index_html(adventure_data: dict) -> str:
    """Generate index.html that loads adventure.json."""
    name = adventure_data.get('name', 'Adventure')
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} — MOOLLM Adventure</title>
    <style>
        :root {{
            --bg: #0a0a0f;
            --surface: #12121a;
            --text: #e8e6e3;
            --accent: #ff6b35;
            --muted: #6b7280;
        }}
        
        * {{ box-sizing: border-box; }}
        
        body {{
            margin: 0;
            background: var(--bg);
            color: var(--text);
            font-family: 'Berkeley Mono', 'JetBrains Mono', monospace;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        
        .header {{
            background: var(--surface);
            padding: 1rem 2rem;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        
        .header h1 {{
            margin: 0;
            font-size: 1.25rem;
            color: var(--accent);
        }}
        
        #adventure {{
            flex: 1;
            display: flex;
            flex-direction: column;
            max-width: 900px;
            width: 100%;
            margin: 0 auto;
            padding: 1rem 2rem;
        }}
        
        .adventure-output {{
            flex: 1;
            overflow-y: auto;
        }}
        
        .adventure-line {{
            margin-bottom: 0.5rem;
            white-space: pre-wrap;
        }}
        
        .adventure-line.command {{ color: var(--accent); }}
        .adventure-line.room {{ 
            border-left: 3px solid var(--accent);
            padding-left: 1rem;
            margin: 1rem 0;
        }}
        .adventure-line.error {{ color: #ef4444; }}
        
        .adventure-input-row {{
            display: flex;
            gap: 0.5rem;
            padding: 1rem;
            background: var(--surface);
            border-radius: 8px;
        }}
        
        .prompt {{ color: var(--accent); font-weight: bold; }}
        
        #adventure-input {{
            flex: 1;
            background: transparent;
            border: none;
            color: var(--text);
            font-family: inherit;
            font-size: 1rem;
            outline: none;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🎮 {name}</h1>
    </div>
    <div id="adventure"></div>
    
    <script type="module">
        import {{ AdventureEngine, AdventureUI }} from './adventure.js';
        
        const response = await fetch('./adventure.json');
        const data = await response.json();
        
        const engine = new AdventureEngine();
        engine.load(data);
        new AdventureUI(engine, 'adventure');
    </script>
</body>
</html>
'''


def generate_standalone_html(adventure_data: dict, js_code: str) -> str:
    """Generate standalone HTML with embedded JS and data."""
    name = adventure_data.get('name', 'Adventure')
    json_str = json.dumps(adventure_data)
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} — MOOLLM Adventure</title>
    <style>
        :root {{
            --bg: #0a0a0f;
            --surface: #12121a;
            --text: #e8e6e3;
            --accent: #ff6b35;
            --muted: #6b7280;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            margin: 0;
            background: var(--bg);
            color: var(--text);
            font-family: monospace;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        .header {{
            background: var(--surface);
            padding: 1rem 2rem;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        .header h1 {{ margin: 0; font-size: 1.25rem; color: var(--accent); }}
        #adventure {{
            flex: 1;
            display: flex;
            flex-direction: column;
            max-width: 900px;
            width: 100%;
            margin: 0 auto;
            padding: 1rem 2rem;
        }}
        .adventure-output {{ flex: 1; overflow-y: auto; }}
        .adventure-line {{ margin-bottom: 0.5rem; white-space: pre-wrap; }}
        .adventure-line.command {{ color: var(--accent); }}
        .adventure-line.room {{ border-left: 3px solid var(--accent); padding-left: 1rem; margin: 1rem 0; }}
        .adventure-line.error {{ color: #ef4444; }}
        .adventure-input-row {{
            display: flex; gap: 0.5rem; padding: 1rem;
            background: var(--surface); border-radius: 8px;
        }}
        .prompt {{ color: var(--accent); font-weight: bold; }}
        #adventure-input {{
            flex: 1; background: transparent; border: none;
            color: var(--text); font-family: inherit; font-size: 1rem; outline: none;
        }}
    </style>
</head>
<body>
    <div class="header"><h1>🎮 {name}</h1></div>
    <div id="adventure"></div>
    
    <script type="module">
{js_code}

const adventureData = {json_str};
const engine = new AdventureEngine();
engine.load(adventureData);
new AdventureUI(engine, 'adventure');
    </script>
</body>
</html>
'''


def cmd_serve(args):
    """
    Serve an adventure for development.
    
    (Future implementation)
    """
    print("🚧 serve command not yet implemented")
    print("   Coming soon: Local development server with hot reload")
    return 0


def cmd_merge(args):
    """
    Merge a runtime state JSON back into the source YAML.
    
    This is where the LLM shines! Given:
    - The original YAML files (with all extra properties, comments, etc.)
    - A state JSON from the runtime
    
    The merge process:
    1. Reads the state JSON
    2. Identifies what changed (player location, inventory, flags, etc.)
    3. Generates YAML patches that preserve extra keys
    4. Outputs merge instructions for the LLM (or applies them)
    
    THE ROUND-TRIP:
    YAML → JSON (compile) → Runtime → State JSON (export) → YAML (merge)
    
    This enables:
    - Save games that update the source world
    - Simulation results written back to source
    - LLM can read state and intelligently update YAML
    """
    if len(args) < 2:
        print("Usage: adventure.py merge <adventure-path> <state.json> [options]")
        print()
        print("Options:")
        print("  --dry-run       Show what would be changed without writing")
        print("  --output FILE   Write merge instructions instead of applying")
        print()
        print("Example:")
        print("  adventure.py merge examples/adventure-4/ save.json --dry-run")
        return 1
    
    adventure_path = Path(args[0])
    state_path = Path(args[1])
    
    if not adventure_path.exists():
        print(f"Error: Adventure path does not exist: {adventure_path}")
        return 1
    
    if not state_path.exists():
        print(f"Error: State file does not exist: {state_path}")
        return 1
    
    dry_run = '--dry-run' in args
    
    print(f"🔄 Merging state into adventure")
    print(f"   Adventure: {adventure_path}")
    print(f"   State: {state_path}")
    
    # Load state
    with open(state_path) as f:
        state = json.load(f)
    
    if state.get('_meta', {}).get('type') != 'adventure-state':
        print("Error: Invalid state file format")
        return 1
    
    print(f"   Turn: {state['_meta'].get('turn', 0)}")
    print(f"   Exported: {state['_meta'].get('exported', 'unknown')}")
    
    # Generate merge instructions
    merge_ops = generate_merge_operations(adventure_path, state)
    
    print()
    print(f"📋 Merge operations ({len(merge_ops)} changes):")
    print()
    
    for op in merge_ops:
        icon = {'update': '✏️', 'create': '➕', 'delete': '➖'}.get(op['type'], '•')
        print(f"   {icon} {op['type'].upper()}: {op['target']}")
        if op.get('field'):
            print(f"      Field: {op['field']}")
        if op.get('value'):
            value_str = str(op['value'])[:60]
            if len(str(op['value'])) > 60:
                value_str += '...'
            print(f"      Value: {value_str}")
        print()
    
    if dry_run:
        print("🔍 Dry run — no changes made")
        print()
        print("To apply these changes, run without --dry-run")
        print("Or let the LLM read this output and intelligently update the YAML files!")
    else:
        print("📝 Applying changes...")
        apply_merge_operations(adventure_path, merge_ops)
        print("✅ Merge complete")
    
    return 0


def generate_merge_operations(adventure_path: Path, state: Dict) -> List[Dict]:
    """
    Generate merge operations from a state snapshot.
    
    Returns a list of operations like:
    - { type: 'update', target: 'ADVENTURE.yml', field: 'flags', value: {...} }
    - { type: 'update', target: 'start/ROOM.yml', field: 'contents', value: [...] }
    """
    ops = []
    
    # Update flags in ADVENTURE.yml
    if state.get('flags'):
        ops.append({
            'type': 'update',
            'target': 'ADVENTURE.yml',
            'field': 'flags',
            'value': state['flags'],
            'reason': 'Sync runtime flags'
        })
    
    # Update variables
    if state.get('variables'):
        ops.append({
            'type': 'update',
            'target': 'ADVENTURE.yml',
            'field': 'world_state.variables',
            'value': state['variables'],
            'reason': 'Sync runtime variables'
        })
    
    # Update player state
    if state.get('player'):
        player = state['player']
        ops.append({
            'type': 'update',
            'target': 'ADVENTURE.yml',
            'field': 'player',
            'value': {
                'location': player.get('location'),
                'inventory': [i['id'] for i in player.get('inventory', [])],
                'mood': player.get('mood')
            },
            'reason': 'Sync player state'
        })
    
    # Update room contents
    for room_id, room_state in state.get('rooms', {}).items():
        if room_state.get('contents'):
            # Find the ROOM.yml for this room
            room_path = f"{room_id}/ROOM.yml"
            ops.append({
                'type': 'update',
                'target': room_path,
                'field': 'contents',
                'value': room_state['contents'],
                'reason': f'Objects in {room_id}'
            })
    
    # Note character locations
    for char_id, char_state in state.get('characters', {}).items():
        ops.append({
            'type': 'update',
            'target': f'characters/{char_id}/CHARACTER.yml',
            'field': 'location',
            'value': char_state.get('location'),
            'reason': f'Character {char_id} moved'
        })
    
    return ops


def apply_merge_operations(adventure_path: Path, ops: List[Dict]):
    """
    Apply merge operations to YAML files.
    
    This is a simple implementation. The LLM can do better
    by reading the ops and intelligently merging!
    """
    for op in ops:
        target_path = adventure_path / op['target']
        
        if not target_path.exists():
            print(f"   ⚠️ Target not found: {op['target']}")
            continue
        
        try:
            with open(target_path) as f:
                data = yaml.safe_load(f)
            
            # Navigate to field and update
            field_parts = op['field'].split('.')
            target = data
            for part in field_parts[:-1]:
                if part not in target:
                    target[part] = {}
                target = target[part]
            
            target[field_parts[-1]] = op['value']
            
            with open(target_path, 'w') as f:
                yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
            
            print(f"   ✓ Updated {op['target']}")
            
        except Exception as e:
            print(f"   ✗ Failed to update {op['target']}: {e}")


# CLOSING THOUGHTS
#
# "Every line of code is a decision.
#  Every comment is a story.
#  Every program is a collaboration across time."
#     — The Pie Table Symposium, January 2026
#
# This code was written with love, caffeine, and the collected wisdom
# of decades of human-computer interaction research.
#
# May it serve you well.
#
# 🥧 — The Pie Table
#

'''
INSPIRATIONS & PHILOSOPHICAL GROUNDING

CONSTRUCTIONISM (Seymour Papert, 1980s)
    Learning happens when you build things you can inspect and share.
    This compiler embodies that: you learn programming by editing YAML,
    seeing the generated code, and watching the world come alive.
    
    "The role of the teacher is to create the conditions for invention
     rather than provide ready-made knowledge."
        — Seymour Papert, "Mindstorms: Children, Computers, and Powerful Ideas"
        https://en.wikipedia.org/wiki/Mindstorms_(book)

SCHEMA MECHANISM (Gary Drescher, 1991)
    Every interaction follows: Context → Action → Result
    The adventure world is a laboratory for causal learning.
    Players build schemas of how the world works through exploration.
    
    "Made-Up Minds: A Constructivist Approach to Artificial Intelligence"
        — Gary Drescher, 1991, MIT Press
        https://mitpress.mit.edu/9780262517089/made-up-minds/

SOCIETY OF MIND (Marvin Minsky, 1986)
    Intelligence emerges from communities of simple agents.
    Each object in the adventure "advertises" what it can do.
    Behavior is distributed, not centralized.
    
    K-LINES: When you activate one concept, you activate its friends.
    CENSORS: Negative K-lines that suppress bad ideas (humor, metaphor).
    
    "The society of mind is built from communities of simple agents
     that work together to produce our complex thoughts."
        — Marvin Minsky, "The Society of Mind"
        https://en.wikipedia.org/wiki/Society_of_Mind

PIE MENUS (Don Hopkins, 1988)
    Radial selection reduces Fitts' Law overhead.
    Navigation is spatial memory. Rooms are memory palaces.
    
    "Pie menus are a beautiful example of how understanding human
     cognition leads to better interface design."
        — Don Hopkins, Pie Menu Research
        https://donhopkins.medium.com/
    
    See also: "The Design and Evaluation of Pie Menus"
        — Jack Callahan, Don Hopkins, Mark Weiser, Ben Shneiderman
        ACM CHI 1988

SELF LANGUAGE (Dave Ungar & Randy Smith, 1987)
    Everything is an object. Objects delegate to prototypes.
    No classes — just examples that others can copy.
    
    "Self: The Power of Simplicity"
        — Ungar & Smith, OOPSLA 1987
        https://bibliography.selflanguage.org/

DIRECT MANIPULATION (Ben Shneiderman, 1982)
    "See and Point" beats "Remember and Type"
    The best interface has no modes. (Larry Tesler: "No modes!")
    
    "Direct Manipulation: A Step Beyond Programming Languages"
        — Ben Shneiderman, IEEE Computer, August 1983
        https://www.cs.umd.edu/~ben/papers/Shneiderman1983Direct.pdf

AUGMENTATION (Doug Engelbart, 1962)
    Computers augment human intellect, not replace it.
    Git IS the undo/redo tree. Git IS the collaboration layer.
    
    "Augmenting Human Intellect: A Conceptual Framework"
        — Doug Engelbart, SRI, 1962
        https://www.dougengelbart.org/content/view/138/

JAVASCRIPT RUNTIME (Vanessa Freudenberg, 2025)
    Target JavaScript, not WebAssembly for dynamic languages.
    The JIT is your friend. Self's insights live in V8.
    
    "V8 IS a Self implementation. Chrome IS a Squeak."
        — Vanessa Freudenberg, RIP 2025 ❤️
        https://codefrau.github.io/
        
THE SIMS (Will Wright, 2000)
    AI lives in the OBJECTS, not the characters.
    Objects advertise actions with scores.
    Behavior emerges from the environment.
    
    "SimAntics: The Virtual Machine that Powers The Sims"
        — Jamie Doornbos, EA/Maxis
        
ToonTalk (Ken Kahn, 1995)
    Programming by demonstration with tangible metaphors.
    Birds, robots, notebooks — all concrete manipulation.
    
    "ToonTalk — An Animated Programming Environment for Children"
        — Ken Kahn, Journal of Visual Languages & Computing, 1996
        https://toontalk.github.io/

HYPERCARD (Bill Atkinson, 1987)
    Anyone can author. Links connect ideas. Buttons do things.
    "Empowerment Epistemology" — tools that make you feel capable.
    
    "HyperCard's greatest contribution was not technical,
     it was social: it gave ordinary people permission to create."
        — Bill Atkinson

MARKDOWN (John Gruber & Aaron Swartz, 2004)
    Readable raw AND rendered. Write for humans first.
    "Source is destination" — the source IS the document.
    
    "The overriding design goal for Markdown's formatting syntax
     is to make it as readable as possible."
        — John Gruber, Daring Fireball
        https://daringfireball.net/projects/markdown/

THE HACKING PARTY CONTRIBUTORS (Adventure Uplift Session, January 2026)

This code was designed at The Gezelligheid Grotto pub, around the Pie Table,
with the following luminaries (invoked as tribute performances):

    Don Hopkins ......... Pie menus, spatial memory, YAML Jazz
    Dave Ungar .......... Prototypes, morphic directness
    Marvin Minsky ....... K-lines, censors, adversary skills
    Seymour Papert ...... Constructionism, low floor/high ceiling
    Gary Drescher ....... Schema mechanism, causal learning
    Doug Hofstadter ..... Strange loops, living measurements
    Doug Engelbart ...... Augmentation, collaboration, NLS
    Ben Shneiderman ..... Direct manipulation, golden rules
    Ted Nelson .......... Branching history, hypertext, Xanadu
    Vanessa Freudenberg . JavaScript optimization, Squeak spirit
    Craig Latta ......... Live programming, Caffeine, tethered mode
    Dan Ingalls ......... Morphic, Squeak, "make it live"
    Bill Atkinson ....... HyperCard, empowerment epistemology
    Ken Kahn ............ ToonTalk, tangible programming
    Amy Ko .............. CS education, Wordplay, learner-centered
    Adele Goldberg ...... Documentation as co-design, Smalltalk-80
    Barbara Liskov ...... Abstraction barriers, CLU
    Bret Victor ......... Learnable programming, explorable explanations
    Larry Tesler ........ Modeless interfaces, cut/copy/paste
    Randy Pausch ........ Alice, drama managers, last lecture
    John McCarthy ....... Executable comments, LISP
    Mitchel Resnick ..... Scratch, creative learning, low floor
    Brad Myers .......... GUI history, natural programming
    Henry Lieberman ..... Programming by demonstration
    Alan Cypher ......... Watch What I Do, PBD
    Arthur van Hoff ..... HotJava, applets
    James Gosling ....... Java, Emacs, NeWS
    Joe Armstrong ....... Erlang, supervision trees
    John Conway ......... Life, cellular automata, emergence
    Timothy Leary ....... Set and setting, expanded consciousness
    Pee Wee Herman ...... "I KNOW you are but what am I?" (chairy approved)
    Chuck Shotton ....... MacHTTP, message schemas, web servers

Plus the memorial avatars of those we've lost but who inspire us still:
    Marvin Minsky (1927-2016)
    Seymour Papert (1928-2016)
    Doug Engelbart (1925-2013)
    Larry Tesler (1945-2020)
    Randy Pausch (1960-2008)
    John McCarthy (1927-2011)
    Joe Armstrong (1950-2019)
    John Conway (1937-2020)
    Vanessa Freudenberg (1972-2025)
'''


if __name__ == "__main__":
    sys.exit(main())

