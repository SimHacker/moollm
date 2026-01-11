#!/usr/bin/env python3
"""
adventure_runtime.py — The MOOLLM Adventure Python Runtime
═══════════════════════════════════════════════════════════════════════════════

"Every program is a game. Every game is a world."
    — Will Wright

This is the Python-side runtime for MOOLLM adventures.
Parallel implementation to adventure.js for:
- Headless simulations
- API-based interaction
- Testing and validation
- Server-side game state

═══════════════════════════════════════════════════════════════════════════════
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Callable, Tuple
from enum import Enum, auto
import json
import time
import re
import logging
import traceback

# ═══════════════════════════════════════════════════════════════════════════════
# LOGGING CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

# Create module logger
logger = logging.getLogger('adventure')

class LogLevel(Enum):
    """Log levels for adventure runtime."""
    SILENT = 0      # No output
    ERROR = 1       # Errors only
    WARN = 2        # Warnings and errors
    INFO = 3        # Normal operation
    DEBUG = 4       # Detailed debugging
    TRACE = 5       # Everything (very verbose)


def setup_logging(level: LogLevel = LogLevel.INFO, log_file: Optional[str] = None):
    """Configure logging for the adventure runtime."""
    log_level = {
        LogLevel.SILENT: logging.CRITICAL + 1,
        LogLevel.ERROR: logging.ERROR,
        LogLevel.WARN: logging.WARNING,
        LogLevel.INFO: logging.INFO,
        LogLevel.DEBUG: logging.DEBUG,
        LogLevel.TRACE: logging.DEBUG - 5
    }.get(level, logging.INFO)
    
    # Add TRACE level
    logging.addLevelName(5, 'TRACE')
    
    # Configure formatter
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%H:%M:%S'
    )
    
    # Console handler
    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(formatter)
    
    logger.setLevel(log_level)
    logger.handlers = [console]
    
    # File handler if specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


# ═══════════════════════════════════════════════════════════════════════════════
# ERROR TYPES
# ═══════════════════════════════════════════════════════════════════════════════

class AdventureError(Exception):
    """Base exception for adventure runtime errors."""
    pass

class LoadError(AdventureError):
    """Error loading adventure data."""
    pass

class NavigationError(AdventureError):
    """Error during navigation."""
    pass

class CommandError(AdventureError):
    """Error processing a command."""
    pass

class StateError(AdventureError):
    """Error with world state."""
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# WORLD STATE
# ═══════════════════════════════════════════════════════════════════════════════

class WorldState:
    """
    The complete state of an adventure world.
    """
    
    def __init__(self):
        self.rooms: Dict[str, 'Room'] = {}
        self.objects: Dict[str, 'GameObject'] = {}
        self.characters: Dict[str, 'Character'] = {}
        self.player: Optional['Character'] = None
        self.current_room: Optional['Room'] = None
        self.flags: Dict[str, bool] = {}
        self.variables: Dict[str, Any] = {}
        self.turn: int = 0
        self.history: List[Dict] = []
        self.event_log: List[Dict] = []
        self._event_handlers: Dict[str, List[Callable]] = {}
    
    @property
    def room(self) -> Optional['Room']:
        """Get the current room."""
        return self.current_room
    
    @property
    def inventory(self) -> List['GameObject']:
        """Get player inventory."""
        return self.player.inventory if self.player else []
    
    def set_flag(self, name: str, value: bool = True):
        """Set a flag."""
        self.flags[name] = value
        self.emit('flag_changed', {'name': name, 'value': value})
    
    def get_flag(self, name: str) -> bool:
        """Get a flag."""
        return self.flags.get(name, False)
    
    def emit(self, event_type: str, data: Dict = None):
        """Emit an event."""
        event = {
            'type': event_type,
            'data': data or {},
            'turn': self.turn,
            'time': time.time()
        }
        self.event_log.append(event)
        
        # Call registered handlers
        for handler in self._event_handlers.get(event_type, []):
            handler(event)
    
    def on(self, event_type: str, handler: Callable):
        """Register an event handler."""
        if event_type not in self._event_handlers:
            self._event_handlers[event_type] = []
        self._event_handlers[event_type].append(handler)


# ═══════════════════════════════════════════════════════════════════════════════
# RUNTIME CLASSES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Entity:
    """Base class for all adventure entities."""
    id: str
    name: str
    description: str = ""
    data: Dict = field(default_factory=dict)
    world: Optional[WorldState] = None
    
    def describe(self) -> str:
        """Get description."""
        return self.description or f"A {self.name}."


@dataclass
class Exit:
    """Connection between rooms."""
    direction: str
    destination: str
    description: str = ""
    aliases: List[str] = field(default_factory=list)
    locked: bool = False
    guard: str = ""  # Natural language guard
    guard_py: Optional[Callable] = None  # Compiled Python guard
    guard_fail: str = ""
    world: Optional[WorldState] = None
    
    def can_use(self, world: WorldState) -> Tuple[bool, str]:
        """Check if player can use this exit."""
        if self.locked:
            return False, "The way is locked."
        
        if self.guard_py:
            try:
                if not self.guard_py(world):
                    return False, self.guard_fail or "You cannot go that way."
            except Exception as e:
                print(f"Guard failed for {self.direction}: {e}")
                return False, "Something prevents you."
        
        return True, ""


@dataclass 
class Room(Entity):
    """A navigable location."""
    exits: Dict[str, Exit] = field(default_factory=dict)
    contents: List['GameObject'] = field(default_factory=list)
    characters: List['Character'] = field(default_factory=list)
    atmosphere: Dict = field(default_factory=dict)
    
    def get_exits(self) -> List[Dict]:
        """Get available exits as list."""
        return [
            {
                'direction': d,
                'description': e.description,
                'aliases': e.aliases
            }
            for d, e in self.exits.items()
        ]
    
    def get_objects(self) -> List['GameObject']:
        """Get visible objects."""
        return [o for o in self.contents if not o.hidden]
    
    def get_characters(self) -> List['Character']:
        """Get present characters."""
        return self.characters
    
    def look(self) -> str:
        """Full room description with contents."""
        parts = [self.describe()]
        
        objects = self.get_objects()
        if objects:
            parts.append('\nYou see: ' + ', '.join(o.name for o in objects))
        
        chars = self.get_characters()
        if chars:
            parts.append('\nPresent: ' + ', '.join(c.name for c in chars))
        
        exits = self.get_exits()
        if exits:
            parts.append('\nExits: ' + ', '.join(e['direction'] for e in exits))
        
        return ''.join(parts)


@dataclass
class Advertisement:
    """An action available on an object."""
    name: str
    description: str = ""
    base_score: int = 50
    effect: str = ""
    guard: str = ""
    guard_py: Optional[Callable] = None
    guard_fail: str = ""
    score_if: str = ""
    score_if_py: Optional[Callable] = None
    effect_py: Optional[Callable] = None
    parent: Optional['GameObject'] = None
    world: Optional[WorldState] = None
    
    def is_available(self, world: WorldState) -> bool:
        """Check if action is currently available."""
        if self.guard_py:
            try:
                return self.guard_py(world)
            except Exception as e:
                print(f"Guard failed for {self.name}: {e}")
                return False
        return True
    
    def score(self, world: WorldState) -> int:
        """Calculate current score."""
        s = self.base_score
        if self.score_if_py:
            try:
                if self.score_if_py(world):
                    s += 20  # Bonus if condition met
            except Exception as e:
                print(f"Score calculation failed for {self.name}: {e}")
        return s
    
    def execute(self, world: WorldState) -> str:
        """Execute the action."""
        world.emit('action_start', {'action': self.name, 'object': self.parent.name if self.parent else ''})
        
        result = self.effect or f"You {self.name.lower()} the {self.parent.name if self.parent else 'thing'}."
        
        if self.effect_py:
            try:
                fn_result = self.effect_py(world)
                if fn_result:
                    result = fn_result
            except Exception as e:
                print(f"Effect failed for {self.name}: {e}")
        
        world.emit('action_complete', {
            'action': self.name, 
            'object': self.parent.name if self.parent else '',
            'result': result
        })
        return result


@dataclass
class GameObject(Entity):
    """Interactive object in the world."""
    emoji: str = "📦"
    portable: bool = True
    hidden: bool = False
    container: Any = None  # Room or Character that holds this
    contents: List['GameObject'] = field(default_factory=list)
    advertisements: Dict[str, Advertisement] = field(default_factory=dict)
    
    def get_actions(self) -> List[Advertisement]:
        """Get available actions sorted by score."""
        return sorted(
            [a for a in self.advertisements.values() if a.is_available(self.world)],
            key=lambda a: a.score(self.world),
            reverse=True
        )
    
    @property
    def display_name(self) -> str:
        """Short display name with emoji."""
        return f"{self.emoji} {self.name}"


@dataclass
class Character(Entity):
    """NPC or player."""
    emoji: str = "👤"
    inventory: List[GameObject] = field(default_factory=list)
    location: Optional[Room] = None
    mood: str = "neutral"
    is_player: bool = False
    
    def move_to(self, room: Optional[Room]):
        """Move to a room."""
        if self.location:
            if self in self.location.characters:
                self.location.characters.remove(self)
        
        self.location = room
        if room:
            room.characters.append(self)
        
        if self.world:
            self.world.emit('character_moved', {
                'character': self.name,
                'room': room.name if room else None
            })
    
    def take(self, obj: GameObject) -> Dict:
        """Add item to inventory."""
        if not obj.portable:
            return {'success': False, 'message': f"You can't take the {obj.name}."}
        
        # Remove from container
        if isinstance(obj.container, Room):
            if obj in obj.container.contents:
                obj.container.contents.remove(obj)
        elif isinstance(obj.container, Character):
            if obj in obj.container.inventory:
                obj.container.inventory.remove(obj)
        
        self.inventory.append(obj)
        obj.container = self
        
        if self.world:
            self.world.emit('item_taken', {'character': self.name, 'object': obj.name})
        
        return {'success': True, 'message': f"You take the {obj.name}."}
    
    def drop(self, obj: GameObject) -> Dict:
        """Drop item from inventory."""
        if obj not in self.inventory:
            return {'success': False, 'message': f"You don't have the {obj.name}."}
        
        self.inventory.remove(obj)
        if self.location:
            self.location.contents.append(obj)
            obj.container = self.location
        
        if self.world:
            self.world.emit('item_dropped', {'character': self.name, 'object': obj.name})
        
        return {'success': True, 'message': f"You drop the {obj.name}."}
    
    def has(self, object_id: str) -> bool:
        """Check if character has an item."""
        return any(obj.id == object_id for obj in self.inventory)


# ═══════════════════════════════════════════════════════════════════════════════
# ADVENTURE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class AdventureEngine:
    """
    Main game controller for Python runtime.
    """
    
    # Direction mappings
    # Maps input to normalized short form
    DIR_MAP = {
        'n': 'n', 'north': 'n',
        's': 's', 'south': 's',
        'e': 'e', 'east': 'e',
        'w': 'w', 'west': 'w',
        'ne': 'ne', 'northeast': 'ne',
        'nw': 'nw', 'northwest': 'nw',
        'se': 'se', 'southeast': 'se',
        'sw': 'sw', 'southwest': 'sw',
        'u': 'up', 'up': 'up',
        'd': 'down', 'down': 'down',
        'in': 'in', 'out': 'out'
    }
    
    # Reverse map: short form to full name for exit lookup
    DIR_EXPAND = {
        'n': 'north', 's': 'south', 'e': 'east', 'w': 'west',
        'ne': 'northeast', 'nw': 'northwest', 'se': 'southeast', 'sw': 'southwest',
        'u': 'up', 'd': 'down'
    }
    
    def __init__(self):
        self.world = WorldState()
        self.ready = False
    
    def load(self, data: Dict) -> 'AdventureEngine':
        """Load compiled adventure JSON/dict."""
        adventure_name = data.get('name', 'Unknown')
        logger.info(f"Loading adventure: {adventure_name}")
        print(f"🎮 Loading adventure: {adventure_name}")
        
        # Validate required fields
        if not isinstance(data, dict):
            raise LoadError("Adventure data must be a dictionary")
        
        if 'rooms' not in data:
            logger.warning("Adventure has no rooms defined")
        
        if 'starting_room' not in data:
            logger.warning("No starting_room specified")
        
        # Create rooms
        for room_data in data.get('rooms', []):
            room = Room(
                id=room_data['id'],
                name=room_data.get('name', room_data['id']),
                description=room_data.get('description', ''),
                data=room_data,
                world=self.world,
                atmosphere=room_data.get('atmosphere', {})
            )
            
            # Build exits
            for direction, exit_data in room_data.get('exits', {}).items():
                if isinstance(exit_data, str):
                    exit_data = {'destination': exit_data}
                
                exit_obj = Exit(
                    direction=direction,
                    destination=exit_data.get('destination', ''),
                    description=exit_data.get('description', ''),
                    aliases=exit_data.get('aliases', []),
                    locked=exit_data.get('locked', False),
                    guard=exit_data.get('guard', ''),
                    guard_fail=exit_data.get('guard_fail', ''),
                    world=self.world
                )
                
                # Compile guard if provided
                if exit_data.get('guard_py'):
                    try:
                        exit_obj.guard_py = eval(exit_data['guard_py'])
                    except Exception as e:
                        print(f"Failed to compile guard: {e}")
                
                room.exits[direction] = exit_obj
            
            self.world.rooms[room.id] = room
        
        # Create objects
        for obj_data in data.get('objects', []):
            obj = GameObject(
                id=obj_data['id'],
                name=obj_data.get('name', obj_data['id']),
                description=obj_data.get('description', ''),
                data=obj_data,
                world=self.world,
                emoji=obj_data.get('emoji', '📦'),
                portable=obj_data.get('portable', True),
                hidden=obj_data.get('hidden', False)
            )
            
            # Build advertisements
            for ad_name, ad_data in obj_data.get('advertisements', {}).items():
                ad = Advertisement(
                    name=ad_name,
                    description=ad_data.get('description', ''),
                    base_score=ad_data.get('score', 50),
                    effect=ad_data.get('effect', ''),
                    guard=ad_data.get('guard', ''),
                    guard_fail=ad_data.get('guard_fail', ''),
                    score_if=ad_data.get('score_if', ''),
                    parent=obj,
                    world=self.world
                )
                
                # Compile Python functions if provided
                if ad_data.get('guard_py'):
                    try:
                        ad.guard_py = eval(ad_data['guard_py'])
                    except Exception as e:
                        print(f"Failed to compile guard: {e}")
                
                if ad_data.get('score_if_py'):
                    try:
                        ad.score_if_py = eval(ad_data['score_if_py'])
                    except Exception as e:
                        print(f"Failed to compile score_if: {e}")
                
                if ad_data.get('effect_py'):
                    try:
                        ad.effect_py = eval(ad_data['effect_py'])
                    except Exception as e:
                        print(f"Failed to compile effect: {e}")
                
                obj.advertisements[ad_name] = ad
            
            self.world.objects[obj.id] = obj
            
            # Place in room
            if obj_data.get('location'):
                room = self.world.rooms.get(obj_data['location'])
                if room:
                    room.contents.append(obj)
                    obj.container = room
        
        # Create characters
        for char_data in data.get('characters', []):
            char = Character(
                id=char_data['id'],
                name=char_data.get('name', char_data['id']),
                description=char_data.get('description', ''),
                data=char_data,
                world=self.world,
                emoji=char_data.get('emoji', '👤'),
                mood=char_data.get('mood', 'neutral'),
                is_player=char_data.get('is_player', False)
            )
            
            self.world.characters[char.id] = char
            
            if char.is_player:
                self.world.player = char
            
            # Place in room
            if char_data.get('location'):
                room = self.world.rooms.get(char_data['location'])
                if room:
                    char.move_to(room)
        
        # Create default player if none was marked
        if not self.world.player:
            player = Character(
                id='player',
                name='You',
                description='A curious adventurer.',
                world=self.world,
                is_player=True
            )
            self.world.characters['player'] = player
            self.world.player = player
        
        # Set starting room
        if data.get('starting_room'):
            start_room = self.world.rooms.get(data['starting_room'])
            if start_room and self.world.player:
                self.world.player.move_to(start_room)
                self.world.current_room = start_room
        
        # Initialize flags
        if data.get('initial_flags'):
            self.world.flags.update(data['initial_flags'])
        
        self.ready = True
        self.world.emit('adventure_loaded', {'name': data.get('name', 'Unknown')})
        
        # Log statistics
        stats = {
            'rooms': len(self.world.rooms),
            'objects': len(self.world.objects),
            'characters': len(self.world.characters),
            'starting_room': data.get('starting_room'),
            'player': self.world.player.id if self.world.player else None,
            'current_room': self.world.current_room.id if self.world.current_room else None
        }
        logger.info(f"Adventure loaded: {stats}")
        
        # Validate state
        if not self.world.current_room:
            logger.error(f"No current room set! starting_room='{data.get('starting_room')}', available rooms: {list(self.world.rooms.keys())[:10]}")
        
        print(f"✅ Adventure loaded: {stats['rooms']} rooms, "
              f"{stats['objects']} objects, {stats['characters']} characters")
        
        return self
    
    def command(self, input_str: str) -> Dict:
        """Process a player command."""
        if not self.ready:
            logger.warning("Command issued before adventure loaded")
            return {'success': False, 'message': 'Adventure not loaded.'}
        
        cmd = input_str.strip().lower()
        if not cmd:
            return {'success': False, 'message': 'What?'}
        
        words = cmd.split()
        verb = words[0] if words else ''
        args = ' '.join(words[1:])
        
        self.world.turn += 1
        self.world.history.append({'turn': self.world.turn, 'input': cmd})
        
        logger.debug(f"Command (turn {self.world.turn}): '{cmd}' -> verb='{verb}', args='{args}'")
        
        # Built-in commands
        if verb in ('look', 'l'):
            return self.look(args)
        
        if verb in ('go', 'n', 'north', 's', 'south', 'e', 'east', 'w', 'west',
                    'ne', 'northeast', 'nw', 'northwest', 'se', 'southeast', 
                    'sw', 'southwest', 'u', 'up', 'd', 'down', 'in', 'out'):
            return self.go(args if verb == 'go' else verb)
        
        if verb in ('take', 'get', 'grab'):
            return self.take(args)
        
        if verb in ('drop', 'put'):
            return self.drop(args)
        
        if verb in ('inventory', 'inv', 'i'):
            return self.show_inventory()
        
        if verb in ('examine', 'x', 'inspect'):
            return self.examine(args)
        
        if verb in ('talk', 'speak'):
            return self.talk(args)
        
        if verb in ('help', '?'):
            return self.help()
        
        if verb == 'exits':
            return self.exits()
        
        if verb == 'stats':
            return self.stats()
        
        if verb == 'debug':
            return self.debug_mode(args)
        
        if verb == 'save':
            if not args:
                return {'success': False, 'message': 'Usage: save <filename>'}
            try:
                self.save_to_file(args)
                return {'success': True, 'message': f'Game saved to {args}'}
            except Exception as e:
                return {'success': False, 'message': f'Save failed: {e}'}
        
        if verb == 'load':
            if not args:
                return {'success': False, 'message': 'Usage: load <filename>'}
            try:
                self.load_from_file(args)
                return {'success': True, 'message': f'Game loaded from {args}'}
            except Exception as e:
                return {'success': False, 'message': f'Load failed: {e}'}
        
        # Try to match an object action
        return self.try_action(verb, args)
    
    def look(self, target: str = '') -> Dict:
        """Look at current room or specific thing."""
        if not target:
            if not self.world.room:
                return {'success': False, 'message': "You are nowhere. (This is a bug!)"}
            return {'success': True, 'message': self.world.room.look()}
        return self.examine(target)
    
    def go(self, direction: str) -> Dict:
        """Move in a direction."""
        logger.debug(f"go command: direction='{direction}'")
        
        if not self.world.room:
            logger.error("Cannot move: no current room")
            return {'success': False, 'message': "You're nowhere! (This is a bug)"}
        
        d = self.DIR_MAP.get(direction, direction)
        d_full = self.DIR_EXPAND.get(d, d)  # Expand short form to full name
        logger.debug(f"  normalized to '{d}' (full: '{d_full}'), room has exits: {list(self.world.room.exits.keys())}")
        
        # Find exit - try multiple variations (case-insensitive, short and long forms)
        exit_obj = None
        tried = []
        for try_dir in [d, d_full, direction, d.upper(), d_full.upper(), direction.upper(), d.lower(), d_full.lower(), direction.lower()]:
            tried.append(try_dir)
            exit_obj = self.world.room.exits.get(try_dir)
            if exit_obj:
                logger.debug(f"  found exit with key '{try_dir}'")
                break
        
        if not exit_obj:
            # Check aliases
            for exit_key, e in self.world.room.exits.items():
                if direction in e.aliases or d in e.aliases:
                    exit_obj = e
                    logger.debug(f"  found exit via alias in '{exit_key}'")
                    break
            
            # Check numeric shortcuts
            if not exit_obj and direction.isdigit():
                num = int(direction)
                for exit_key, e in self.world.room.exits.items():
                    if num in e.aliases:
                        exit_obj = e
                        logger.debug(f"  found exit via numeric alias {num} in '{exit_key}'")
                        break
        
        if not exit_obj:
            logger.debug(f"  no exit found. Tried: {tried}")
            return {'success': False, 'message': f"You can't go {direction}."}
        
        allowed, reason = exit_obj.can_use(self.world)
        if not allowed:
            logger.debug(f"  exit blocked: {reason}")
            return {'success': False, 'message': reason}
        
        # Resolve destination - handle relative paths
        dest = exit_obj.destination
        current_id = self.world.room.id
        logger.debug(f"  destination: '{dest}' (from room '{current_id}')")
        
        # Normalize: strip trailing slashes
        dest_clean = dest.rstrip('/')
        
        # Try various ways to resolve the destination
        candidates = []
        
        # 1. Exact match as given
        candidates.append(dest_clean)
        
        # 2. Resolve relative paths based on current room
        if dest.startswith('./') or not dest.startswith('../'):
            # Relative to current room's directory
            if '/' in current_id:
                parent = '/'.join(current_id.split('/')[:-1])
                candidates.append(f"{parent}/{dest_clean.lstrip('./')}")
            # Also try current_id/dest for sub-rooms
            candidates.append(f"{current_id}/{dest_clean.lstrip('./')}")
        
        # 3. Handle ../ by going up from current room
        if dest.startswith('../'):
            parts = current_id.split('/')
            dest_parts = dest_clean.split('/')
            up_count = sum(1 for p in dest_parts if p == '..')
            remaining = '/'.join(p for p in dest_parts if p != '..')
            base = '/'.join(parts[:-up_count]) if up_count < len(parts) else ''
            if base:
                candidates.append(f"{base}/{remaining}".strip('/'))
            else:
                candidates.append(remaining)
        
        # 4. Strip all ../ and ./ and try raw
        stripped = dest_clean
        while stripped.startswith('../') or stripped.startswith('./'):
            stripped = stripped.lstrip('./').lstrip('../')
        candidates.append(stripped)
        
        # 5. Just the last component
        candidates.append(dest_clean.split('/')[-1])
        
        logger.debug(f"  trying candidates: {candidates}")
        
        dest_room = None
        for candidate in candidates:
            if not candidate:
                continue
            dest_room = self.world.rooms.get(candidate)
            if dest_room:
                logger.debug(f"  found room with id '{candidate}'")
                break
        
        if not dest_room:
            logger.warning(f"  destination room not found: '{dest}' (tried '{dest_normalized}')")
            logger.debug(f"  available rooms: {list(self.world.rooms.keys())[:20]}")
            return {'success': False, 'message': 'That way leads nowhere.'}
        
        logger.debug(f"  moving to room: {dest_room.id}")
        self.world.player.move_to(dest_room)
        self.world.current_room = dest_room
        
        return {'success': True, 'message': dest_room.look()}
    
    def take(self, name: str) -> Dict:
        """Pick up an object."""
        obj = self._find_object(name)
        if not obj:
            return {'success': False, 'message': f"You don't see a {name} here."}
        return self.world.player.take(obj)
    
    def drop(self, name: str) -> Dict:
        """Drop an object."""
        obj = self._find_in_inventory(name)
        if not obj:
            return {'success': False, 'message': f"You don't have a {name}."}
        return self.world.player.drop(obj)
    
    def show_inventory(self) -> Dict:
        """Show inventory."""
        inv = self.world.player.inventory
        if not inv:
            return {'success': True, 'message': 'You are carrying nothing.'}
        items = '\n  '.join(o.display_name for o in inv)
        return {'success': True, 'message': f'You are carrying:\n  {items}'}
    
    def examine(self, name: str) -> Dict:
        """Examine something."""
        # Check room objects
        target = self._find_object(name)
        if target:
            actions = target.get_actions()
            msg = target.describe()
            if actions:
                msg += '\n\nActions: ' + ', '.join(a.name for a in actions)
            return {'success': True, 'message': msg}
        
        # Check inventory
        target = self._find_in_inventory(name)
        if target:
            return {'success': True, 'message': target.describe()}
        
        # Check characters
        target = self._find_character(name)
        if target:
            return {'success': True, 'message': target.describe()}
        
        return {'success': False, 'message': f"You don't see a {name} here."}
    
    def talk(self, name: str) -> Dict:
        """Talk to someone."""
        char = self._find_character(name)
        if not char:
            return {'success': False, 'message': f"You don't see {name} here."}
        
        # TODO: Full dialogue system
        return {'success': True, 'message': f"{char.name} nods at you."}
    
    def try_action(self, verb: str, target: str) -> Dict:
        """Try to match an action on an object."""
        obj = self._find_object(target) or self._find_in_inventory(target)
        if not obj:
            return {'success': False, 'message': f'I don\'t understand "{verb}".'}
        
        action = obj.advertisements.get(verb.upper())
        if not action:
            return {'success': False, 'message': f"You can't {verb} the {obj.name}."}
        
        if not action.is_available(self.world):
            return {'success': False, 'message': action.guard_fail or "You can't do that right now."}
        
        result = action.execute(self.world)
        return {'success': True, 'message': result}
    
    def help(self) -> Dict:
        """Show help."""
        return {
            'success': True,
            'message': """Commands:
  look (l)          - Describe current room
  go <direction>    - Move (n/s/e/w/ne/nw/se/sw/up/down/in/out)
  take <item>       - Pick up an item
  drop <item>       - Drop an item
  inventory (i)     - Show what you're carrying
  examine <thing>   - Look at something closely
  talk <person>     - Talk to someone
  <action> <item>   - Do an action on an item
  exits             - List exits from current room
  stats             - Show game statistics
  debug [on|off]    - Toggle debug mode
  save <file>       - Save game state
  load <file>       - Load game state
  help              - Show this help"""
        }
    
    def exits(self) -> Dict:
        """List all exits from current room."""
        if not self.world.room:
            return {'success': False, 'message': "You're nowhere!"}
        
        exits = self.world.room.exits
        if not exits:
            return {'success': True, 'message': "There are no obvious exits."}
        
        lines = ["Exits:"]
        for direction, exit_obj in sorted(exits.items()):
            # Get first line of description, or destination
            desc = exit_obj.description.split('\n')[0][:50] if exit_obj.description else f"→ {exit_obj.destination}"
            aliases = f" ({', '.join(str(a) for a in exit_obj.aliases)})" if exit_obj.aliases else ''
            lines.append(f"  {direction}{aliases}: {desc}")
        
        return {'success': True, 'message': '\n'.join(lines)}
    
    def stats(self) -> Dict:
        """Show game statistics."""
        lines = [
            "Game Statistics:",
            f"  Turn: {self.world.turn}",
            f"  Rooms: {len(self.world.rooms)}",
            f"  Objects: {len(self.world.objects)}",
            f"  Characters: {len(self.world.characters)}",
            f"  Current room: {self.world.room.id if self.world.room else 'None'}",
            f"  Inventory items: {len(self.world.player.inventory) if self.world.player else 0}",
            f"  Flags set: {sum(1 for v in self.world.flags.values() if v)}",
        ]
        return {'success': True, 'message': '\n'.join(lines)}
    
    def debug_mode(self, args: str) -> Dict:
        """Toggle or set debug mode."""
        if args == 'on':
            setup_logging(LogLevel.DEBUG)
            return {'success': True, 'message': 'Debug mode ON'}
        elif args == 'off':
            setup_logging(LogLevel.WARN)
            return {'success': True, 'message': 'Debug mode OFF'}
        else:
            # Toggle
            if logger.level <= logging.DEBUG:
                setup_logging(LogLevel.WARN)
                return {'success': True, 'message': 'Debug mode OFF'}
            else:
                setup_logging(LogLevel.DEBUG)
                return {'success': True, 'message': 'Debug mode ON'}
    
    # ─────────────────────────────────────────────────────────────────────────
    # Helper methods
    # ─────────────────────────────────────────────────────────────────────────
    
    def _find_object(self, name: str) -> Optional[GameObject]:
        """Find object in current room."""
        if not name or not self.world.room:
            return None
        name = name.lower()
        for obj in self.world.room.contents:
            if name in obj.name.lower() or obj.id.lower() == name:
                return obj
        return None
    
    def _find_in_inventory(self, name: str) -> Optional[GameObject]:
        """Find object in player inventory."""
        if not name or not self.world.player:
            return None
        name = name.lower()
        for obj in self.world.player.inventory:
            if name in obj.name.lower() or obj.id.lower() == name:
                return obj
        return None
    
    def _find_character(self, name: str) -> Optional[Character]:
        """Find character in current room."""
        if not name or not self.world.room:
            return None
        name = name.lower()
        for char in self.world.room.characters:
            if name in char.name.lower() or char.id.lower() == name:
                return char
        return None
    
    # ─────────────────────────────────────────────────────────────────────────
    # STATE EXPORT/IMPORT
    # ─────────────────────────────────────────────────────────────────────────
    
    def export_state(self) -> Dict:
        """
        Export current world state to a dict.
        
        This creates a snapshot that can be:
        1. Saved to file for later
        2. Sent to LLM for intelligent merging back to YAML
        3. Used for debugging/replay
        
        The LLM can read this and apply changes to the source YAML,
        retaining extra keys and using intelligence to merge!
        """
        import datetime
        
        state = {
            '_meta': {
                'type': 'adventure-state',
                'version': '1.0',
                'exported': datetime.datetime.now().isoformat(),
                'turn': self.world.turn
            },
            
            # Player state
            'player': None,
            
            # Global state
            'flags': dict(self.world.flags),
            'variables': dict(self.world.variables),
            
            # Modified states
            'rooms': {},
            'objects': {},
            'characters': {},
            
            # History
            'history': self.world.history[-100:],
            'eventLog': self.world.event_log[-50:]
        }
        
        # Export player
        if self.world.player:
            state['player'] = {
                'id': self.world.player.id,
                'location': self.world.player.location.id if self.world.player.location else None,
                'inventory': [{'id': o.id, 'name': o.name} for o in self.world.player.inventory],
                'mood': self.world.player.mood
            }
        
        # Export room states
        for room_id, room in self.world.rooms.items():
            room_state = {
                'contents': [o.id for o in room.contents],
                'characters': [c.id for c in room.characters]
            }
            if room_state['contents'] or room_state['characters']:
                state['rooms'][room_id] = room_state
        
        # Export object states
        for obj_id, obj in self.world.objects.items():
            obj_state = {}
            if obj.container:
                if isinstance(obj.container, Room):
                    obj_state['location'] = obj.container.id
                    obj_state['locationType'] = 'room'
                elif isinstance(obj.container, Character):
                    obj_state['location'] = obj.container.id
                    obj_state['locationType'] = 'character'
            
            if obj_state:
                state['objects'][obj_id] = obj_state
        
        # Export character states (non-player)
        for char_id, char in self.world.characters.items():
            if char.is_player:
                continue
            state['characters'][char_id] = {
                'location': char.location.id if char.location else None,
                'mood': char.mood,
                'inventory': [o.id for o in char.inventory]
            }
        
        return state
    
    def export_state_json(self, pretty: bool = True) -> str:
        """Export state as JSON string."""
        import json
        return json.dumps(self.export_state(), indent=2 if pretty else None)
    
    def import_state(self, state: Dict):
        """
        Import state from a saved snapshot.
        
        Restores:
        - Player location and inventory
        - Flags and variables
        - Object locations
        - Character states
        """
        if state.get('_meta', {}).get('type') != 'adventure-state':
            raise ValueError('Invalid state format')
        
        # Restore flags and variables
        self.world.flags = dict(state.get('flags', {}))
        self.world.variables = dict(state.get('variables', {}))
        self.world.turn = state.get('_meta', {}).get('turn', 0)
        
        # Restore player
        player_state = state.get('player')
        if player_state and self.world.player:
            if player_state.get('location'):
                room = self.world.rooms.get(player_state['location'])
                if room:
                    self.world.player.move_to(room)
                    self.world.current_room = room
            
            # Restore inventory
            self.world.player.inventory = []
            for item in player_state.get('inventory', []):
                obj = self.world.objects.get(item['id'])
                if obj:
                    self.world.player.inventory.append(obj)
                    obj.container = self.world.player
        
        # Restore object locations
        for obj_id, obj_state in state.get('objects', {}).items():
            obj = self.world.objects.get(obj_id)
            if not obj:
                continue
            
            if obj_state.get('locationType') == 'room':
                room = self.world.rooms.get(obj_state.get('location'))
                if room and obj not in room.contents:
                    room.contents.append(obj)
                    obj.container = room
        
        # Restore character states
        for char_id, char_state in state.get('characters', {}).items():
            char = self.world.characters.get(char_id)
            if not char:
                continue
            
            if char_state.get('location'):
                room = self.world.rooms.get(char_state['location'])
                if room:
                    char.move_to(room)
            char.mood = char_state.get('mood', 'neutral')
        
        self.world.emit('state_imported', {'turn': self.world.turn})
    
    def save_to_file(self, path: str):
        """Save state to a JSON file."""
        with open(path, 'w') as f:
            f.write(self.export_state_json())
    
    def load_from_file(self, path: str):
        """Load state from a JSON file."""
        import json
        with open(path) as f:
            self.import_state(json.load(f))


# ═══════════════════════════════════════════════════════════════════════════════
# CLI INTERFACE (for testing)
# ═══════════════════════════════════════════════════════════════════════════════

def play_cli(adventure_json: str):
    """
    Play an adventure from the command line.
    """
    import json
    
    with open(adventure_json) as f:
        data = json.load(f)
    
    engine = AdventureEngine()
    engine.load(data)
    
    print("\n" + "═" * 60)
    print(engine.world.room.look())
    print("═" * 60 + "\n")
    
    while True:
        try:
            cmd = input("> ").strip()
            if cmd.lower() in ('quit', 'exit', 'q'):
                print("Goodbye!")
                break
            
            result = engine.command(cmd)
            print(result['message'])
            print()
            
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


# ═══════════════════════════════════════════════════════════════════════════════
# API FOR SIMULATIONS
# ═══════════════════════════════════════════════════════════════════════════════

class SimulationRunner:
    """
    Run automated simulations for testing or AI play.
    """
    
    def __init__(self, engine: AdventureEngine):
        self.engine = engine
        self.transcript: List[Dict] = []
    
    def run_script(self, commands: List[str]) -> List[Dict]:
        """Run a sequence of commands."""
        results = []
        for cmd in commands:
            result = self.engine.command(cmd)
            entry = {
                'turn': self.engine.world.turn,
                'command': cmd,
                'success': result['success'],
                'message': result['message']
            }
            results.append(entry)
            self.transcript.append(entry)
        return results
    
    def explore(self, max_steps: int = 100) -> Dict:
        """
        Automated exploration - visit all reachable rooms.
        """
        visited = set()
        queue = [self.engine.world.current_room.id]
        path = []
        
        while queue and len(path) < max_steps:
            current = self.engine.world.current_room
            visited.add(current.id)
            
            # Find an unvisited exit
            for direction, exit_obj in current.exits.items():
                dest_id = exit_obj.destination
                if dest_id not in visited:
                    result = self.engine.command(f"go {direction}")
                    if result['success']:
                        path.append({
                            'from': current.id,
                            'direction': direction,
                            'to': dest_id
                        })
                        queue.append(dest_id)
                    break
            else:
                # All exits visited, backtrack
                if path:
                    # Simple backtrack - go back
                    last = path.pop()
                    # Find reverse direction
                    reverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e',
                              'ne': 'sw', 'sw': 'ne', 'nw': 'se', 'se': 'nw',
                              'up': 'down', 'down': 'up', 'in': 'out', 'out': 'in'}
                    rev_dir = reverse.get(last['direction'], 'out')
                    self.engine.command(f"go {rev_dir}")
                else:
                    break
        
        return {
            'rooms_visited': len(visited),
            'total_rooms': len(self.engine.world.rooms),
            'path_length': len(path),
            'visited': list(visited)
        }
    
    def get_state_snapshot(self) -> Dict:
        """Get a serializable snapshot of current state."""
        return self.engine.export_state()


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        play_cli(sys.argv[1])
    else:
        print("Usage: python adventure_runtime.py <adventure.json>")
        print("\nOr import and use programmatically:")
        print("  from adventure_runtime import AdventureEngine, SimulationRunner")
        print("  engine = AdventureEngine()")
        print("  engine.load(data)")
        print("  result = engine.command('look')")
