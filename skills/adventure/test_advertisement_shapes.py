#!/usr/bin/env python3
"""
test_advertisement_shapes.py — advertisement normalization in the adventure compiler.

Run with: python3 test_advertisement_shapes.py
Or: python3 -m unittest test_advertisement_shapes -v
"""

import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from adventure import (
    AdventureLinter, EventType, advertisement_name, export_advertisement,
    export_runtime_json, iter_advertisements, normalize_advertisements,
)
from adventure_runtime import AdventureEngine


class NormalizeListForm(unittest.TestCase):

    def test_name_wins(self):
        ads = normalize_advertisements([{'name': 'RING', 'action': 'hit gong', 'score': 70}])
        self.assertEqual(list(ads), ['RING'])
        self.assertEqual(ads['RING']['action'], 'hit gong')

    def test_action_uppercased_hyphenated(self):
        ads = normalize_advertisements([{'action': 'speak to', 'score': 60, 'result': 'Silence.'}])
        self.assertEqual(list(ads), ['SPEAK-TO'])
        self.assertEqual(ads['SPEAK-TO']['result'], 'Silence.')

    def test_trigger_becomes_on_slug(self):
        ads = normalize_advertisements([
            {'trigger': 'feed me', 'score': 0.8, 'response': 'Nom.'},
            {'trigger': ['sing', 'hungry'], 'response': 'La.'},
        ])
        self.assertEqual(list(ads), ['ON-FEED-ME', 'ON-SING'])
        self.assertEqual(ads['ON-FEED-ME']['score'], 0.8)

    def test_neither_falls_back_to_index(self):
        ads = normalize_advertisements([{'action': 'LOOK'}, {'description': 'mystery'}])
        self.assertEqual(list(ads), ['LOOK', 'ACTION_1'])

    def test_duplicate_names_get_suffix(self):
        ads = normalize_advertisements([{'action': 'LOOK'}, {'action': 'look'}])
        self.assertEqual(list(ads), ['LOOK', 'LOOK-2'])

    def test_bare_string_entry(self):
        self.assertEqual(normalize_advertisements(['wave']), {'ACTION_0': {'description': 'wave'}})

    def test_yaml_path_is_list_index(self):
        paths = [p for _, p, _ in iter_advertisements([{'action': 'A'}, {'action': 'B'}])]
        self.assertEqual(paths, ['advertisements[0]', 'advertisements[1]'])

    def test_advertisement_name_non_dict(self):
        self.assertEqual(advertisement_name('x', 3), 'ACTION_3')


class NormalizeMapForm(unittest.TestCase):

    def test_map_passthrough(self):
        src = {'RING': {'score': 90, 'effect': 'BONG', 'satisfies': ['fun'], 'note': 'loud'}}
        self.assertEqual(normalize_advertisements(src), src)
        self.assertEqual(list(iter_advertisements(src))[0][1], 'advertisements.RING')

    def test_none_and_empty(self):
        self.assertEqual(normalize_advertisements(None), {})
        self.assertEqual(normalize_advertisements({}), {})
        self.assertEqual(normalize_advertisements([]), {})


class ExportAdvertisement(unittest.TestCase):

    def test_unknown_keys_pass_through_with_defaults(self):
        out = export_advertisement({'trigger': 'hi', 'response': 'Hello.', 'cooldown': 3})
        self.assertEqual(out['trigger'], 'hi')
        self.assertEqual(out['response'], 'Hello.')
        self.assertEqual(out['cooldown'], 3)
        self.assertEqual(out['score'], 50)
        self.assertEqual(out['guard_js'], '')

    def test_given_values_override_defaults(self):
        out = export_advertisement({'score': 0, 'effect': 'x', 'guard_js': 'w => true'})
        self.assertEqual((out['score'], out['effect'], out['guard_js']), (0, 'x', 'w => true'))

    def test_condition_fills_guard(self):
        out = export_advertisement({'condition': 'player has feather_token'})
        self.assertEqual(out['guard'], 'player has feather_token')
        self.assertEqual(out['condition'], 'player has feather_token')

    def test_condition_does_not_override_guard(self):
        out = export_advertisement({'condition': 'c', 'guard': 'g'})
        self.assertEqual((out['guard'], out['condition']), ('g', 'c'))


class LinterAndExport(unittest.TestCase):
    """A list-form object still gets its method and advertisement checks, and exports by name."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / 'ADVENTURE.yml').write_text('adventure:\n  name: T\nnavigation:\n  starting_room: hall\n')
        (root / 'hall').mkdir()
        (root / 'hall' / 'ROOM.yml').write_text('room:\n  name: Hall\n  description: A hall.\n')
        (root / 'hall' / 'face.yml').write_text(textwrap.dedent('''\
            object:
              id: face
              name: Carved Face
              advertisements:
                - action: speak to
                  score: 60
                  score_if: "player is lonely"
                  result: "Silence."
                - trigger: hello
                  score: 0.9
                  response: "The face smiles."
                  condition: "player has feather_token"
              methods:
                BLINK:
                  description: "The face blinks"
                  effect: "set blinked to true"
                STARE: "look at the player"
            '''))
        self.root = root
        self.linter = AdventureLinter(root)
        self.linter.lint()

    def tearDown(self):
        self.tmp.cleanup()

    def compile_fields(self):
        return {e.source_field: e for e in self.linter.report.events
                if e.type == EventType.COMPILE_EXPRESSION}

    def test_found_object_lists_names(self):
        found = [e for e in self.linter.report.events if e.type == EventType.FOUND_OBJECT]
        self.assertEqual(found[0].data['advertisements'], ['SPEAK-TO', 'ON-HELLO'])

    def test_list_advertisement_checked(self):
        fields = self.compile_fields()
        self.assertIn('advertisements[0].score_if', fields)
        self.assertEqual(fields['advertisements[0].score_if'].target_field_js,
                         'advertisements[0].score_if_js')
        self.assertIn('advertisements[1].condition', fields)

    def test_map_method_checked(self):
        fields = self.compile_fields()
        self.assertIn('methods.BLINK.effect', fields)
        self.assertEqual(fields['methods.BLINK.effect'].target_field_js, 'methods.BLINK.effect_js')
        self.assertEqual(fields['methods.BLINK.effect'].target_field_py, 'methods.BLINK.effect_py')

    def test_string_method_checked(self):
        fields = self.compile_fields()
        self.assertEqual(fields['methods.STARE'].target_field_js, 'methods_js.STARE')

    def test_compiled_method_not_reported(self):
        (self.root / 'hall' / 'face.yml').write_text(textwrap.dedent('''\
            object:
              id: face
              methods:
                BLINK:
                  effect: "set blinked to true"
                  effect_js: "(world) => world.setFlag('blinked', true)"
                  effect_py: "lambda world: world.set_flag('blinked', True)"
            '''))
        linter = AdventureLinter(self.root)
        linter.lint()
        self.assertFalse([e for e in linter.report.events
                          if e.type == EventType.COMPILE_EXPRESSION
                          and (e.source_field or '').startswith('methods.')])

    def test_export_and_runtime_load(self):
        world = export_runtime_json(self.linter)
        face = [o for o in world['objects'] if o['id'] == 'face'][0]
        ads = face['advertisements']
        self.assertEqual(list(ads), ['SPEAK-TO', 'ON-HELLO'])
        self.assertEqual(ads['SPEAK-TO']['action'], 'speak to')
        self.assertEqual(ads['SPEAK-TO']['result'], 'Silence.')
        self.assertEqual(ads['ON-HELLO']['trigger'], 'hello')
        self.assertEqual(ads['ON-HELLO']['guard'], 'player has feather_token')
        engine = AdventureEngine()
        engine.load(world)
        self.assertIn('ON-HELLO', engine.world.objects['face'].advertisements)


if __name__ == '__main__':
    unittest.main(verbosity=2)
