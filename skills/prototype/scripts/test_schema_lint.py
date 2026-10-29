#!/usr/bin/env python3
"""Tests for schema_lint.py on fixture schemas in a temp dir. Run: python3 test_schema_lint.py"""

from __future__ import annotations

import io
import sys
import tempfile
import textwrap
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import schema_lint  # noqa: E402

SCHEMAS = {
    "skills/advertisement/ADVERTISEMENT.yml": """
        schema:
          id: advertisement
          conventions:
            list_of_one: "a bare string where a list is expected is a list of one"
          keys:
            score: {shape: number, range: [0, 100], default: 50, aliases: [score_hint]}
            score_if: {shape: prose, compiles: true}
            guard: {shape: prose, aliases: [condition]}
            satisfies: {shape: list, of: string}
        """,
    "skills/object/OBJECT.yml": """
        name: object
        schema:
          id: method
          keys:
            description: {shape: prose, aliases: [does]}
            parameters: {shape: map, of: prose, aliases: [params]}
            invoked_by: {shape: enum, values: [player, npc, self, any]}
        """,
    "skills/card/CARD.yml": """
        id: card
        schema:
          id: card
          extends: [dublin]
          keys:
            type: {shape: ref}
            tier: {shape: enum, values: [0, 1, 2, 3]}
            k_lines: {shape: list, of: string}
            advertisements: {shape: map, of: advertisement}
            methods: {shape: map, of: method}
        """,
    "skills/dublin/DUBLIN.yml": """
        schema:
          id: dublin
          keys:
            tags: {shape: list, of: string}
            see_also: {shape: list, aliases: [references]}
        """,
    "skills/character/CHARACTER.yml": """
        schema:
          id: character
          keys:
            name: string
            representation: {shape: map, of: representation}
        """,
    "skills/representation-ethics/REPRESENTATION.yml": """
        schema:
          id: representation
          keys:
            consent: {shape: enum, values: [given, none, public-record]}
        """,
}


class Fixture:
    def __init__(self, schemas: dict[str, str] | None = None) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / ".git").mkdir()
        for path, text in (SCHEMAS if schemas is None else schemas).items():
            self.write(path, text)

    def write(self, path: str, text: str) -> Path:
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(textwrap.dedent(text).lstrip("\n"), encoding="utf-8")
        return p

    def lint(self, *paths: str, cards: bool = False) -> list[schema_lint.Finding]:
        schemas, _ = schema_lint.load_schemas(self.root)
        linter = schema_lint.Linter(self.root, schemas, cards_only=cards)
        targets = [self.root / p for p in paths] or [self.root / "w"]
        for f in schema_lint.iter_files(targets, self.root, cards):
            linter.lint_file(f)
        return linter.findings

    def cli(self, *argv: str) -> tuple[int, str]:
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = schema_lint.main(["--root", str(self.root), *argv])
        return code, buf.getvalue()

    def close(self) -> None:
        self.tmp.cleanup()


def rules(findings: list[schema_lint.Finding]) -> dict[tuple[str, str], schema_lint.Finding]:
    return {(f.path, f.rule): f for f in findings}


class SchemaLintTest(unittest.TestCase):
    def setUp(self) -> None:
        self.fx = Fixture()

    def tearDown(self) -> None:
        self.fx.close()

    def test_discovers_schemas_and_merges_extends(self) -> None:
        schemas, problems = schema_lint.load_schemas(self.fx.root)
        self.assertEqual(set(schemas), {"advertisement", "method", "card", "dublin", "character", "representation"})
        self.assertEqual(problems, [])
        self.assertIn("tags", schemas["card"].keys)
        self.assertEqual(schemas["card"].aliases["references"], "see_also")
        self.assertEqual(schemas["advertisement"].keys["score"].default, 50)

    def test_plain_schema_key_without_id_is_not_a_schema(self) -> None:
        self.fx.write("skills/goal/CARD.yml", "schema:\n  required: [id]\n")
        schemas, _ = schema_lint.load_schemas(self.fx.root)
        self.assertNotIn("goal", schemas)

    def test_duplicate_id_prefers_the_file_named_for_it(self) -> None:
        self.fx.write("skills/advertisement/CARD.yml", "schema:\n  id: advertisement\n  keys: {}\n")
        schemas, problems = schema_lint.load_schemas(self.fx.root)
        self.assertEqual(schemas["advertisement"].source, "skills/advertisement/ADVERTISEMENT.yml")
        self.assertEqual(len(problems), 1)

    def test_unparseable_schema_file_is_a_problem_not_a_crash(self) -> None:
        self.fx.write("skills/representation-ethics/REPRESENTATION.yml", 'schema:\n  id: representation\n  - "x" y\n')
        schemas, problems = schema_lint.load_schemas(self.fx.root)
        self.assertNotIn("representation", schemas)
        self.assertTrue(any("REPRESENTATION.yml" in p for p in problems))

    def test_unparseable_file(self) -> None:
        self.fx.write("w/a/CARD.yml", 'principles:\n  - "I think..." (they KNOW)\n')
        f = self.fx.lint()
        self.assertEqual([(x.rule, x.severity) for x in f], [("unparseable", "error")])
        self.assertIn("line 2", f[0].message)

    def test_list_form_advertisements_and_entries_still_checked(self) -> None:
        self.fx.write("w/a/CARD.yml", """
            advertisements:
              - action: LOOK
                score: 150
              - action: SIT
              - just a string
            """)
        r = rules(self.fx.lint())
        self.assertEqual(r[("advertisements", "shape.advertisements-list")].severity, "error")
        self.assertEqual(r[("advertisements[0].score", "range")].severity, "error")
        self.assertEqual(r[("advertisements[1]", "advertisement-no-score")].severity, "info")
        self.assertIn("default 50", r[("advertisements[1]", "advertisement-no-score")].message)
        self.assertEqual(r[("advertisements[2]", "shape")].severity, "error")
        self.assertNotIn(("advertisements", "shape"), r)

    def test_score_without_default_is_a_warning(self) -> None:
        fx = Fixture(schemas={})
        try:
            fx.write("w/a/CARD.yml", "advertisements:\n  LOOK: {condition: here}\n")
            r = rules(fx.lint())
            self.assertEqual(r[("advertisements.LOOK", "advertisement-no-score")].severity, "warning")
        finally:
            fx.close()

    def test_alias_default_and_non_numeric_score(self) -> None:
        self.fx.write("w/room/ROOM.yml", """
            advertisements:
              SIT: {score_hint: high, condition: "player is tired"}
              LOOK: {score: 50, score-if: "always"}
              WAVE: {score: "=50+x"}
            """)
        r = rules(self.fx.lint())
        self.assertIn("score", r[("advertisements.SIT.score_hint", "alias")].message)
        self.assertIn("guard", r[("advertisements.SIT.condition", "alias")].message)
        self.assertEqual(r[("advertisements.SIT.score_hint", "advertisement-no-score")].severity, "warning")
        self.assertEqual(r[("advertisements.LOOK.score", "default")].severity, "info")
        self.assertIn("score_if", r[("advertisements.LOOK.score-if", "hyphenated-key")].message)
        self.assertEqual(r[("advertisements.WAVE.score", "advertisement-no-score")].severity, "warning")
        self.assertNotIn(("advertisements.WAVE.score", "shape"), r)

    def test_methods_list_string_entries_alias_and_enum(self) -> None:
        self.fx.write("w/a/CARD.yml", """
            methods:
              LOOK: "describe the room"
              SIT:
                params: {where: "a seat"}
                invoked_by: wizard
            """)
        self.fx.write("w/b/thing.yml", "methods:\n  - LOOK: {description: look}\n  - SIT\n")
        r = rules(self.fx.lint())
        self.assertEqual(r[("methods.LOOK", "shape.method-string")].severity, "error")
        self.assertNotIn(("methods.LOOK", "shape"), r)
        self.assertIn("parameters", r[("methods.SIT.params", "alias")].message)
        self.assertEqual(r[("methods.SIT.invoked_by", "enum")].severity, "error")
        self.assertIn(("methods", "shape.methods-list"), r)

    def test_wrong_shape_for_schema_key(self) -> None:
        self.fx.write("w/o/thing.yml", "methods:\n  LOOK: {parameters: [a, b]}\n")
        r = rules(self.fx.lint())
        self.assertIn("expected map, got list", r[("methods.LOOK.parameters", "shape")].message)

    def test_list_of_one_convention(self) -> None:
        self.fx.write("w/o/thing.yml", "advertisements:\n  SIT: {score: 60, satisfies: comfort}\n")
        self.assertEqual(self.fx.lint(), [])

    def test_card_rules_type_list_invoke_when_hyphens(self) -> None:
        self.fx.write("w/a/CARD.yml", """
            type: [skill, protocol]
            tier: 7
            invoke_when: ["giving voice"]
            k-lines: [VOICE]
            allowed-tools: [read]
            the-insight: "x"
            advertisements:
              VOICE: {score: 80}
            """)
        r = rules(self.fx.lint())
        self.assertEqual(r[("type", "type-list")].severity, "warning")
        self.assertNotIn(("type", "shape"), r)
        self.assertEqual(r[("tier", "enum")].severity, "error")
        self.assertEqual(r[("invoke_when", "invoke-when-beside-advertisements")].severity, "warning")
        self.assertIn("schema key k_lines", r[("k-lines", "hyphenated-key")].message)
        self.assertIn(("the-insight", "hyphenated-key"), r)
        self.assertNotIn(("allowed-tools", "hyphenated-key"), r)

    def test_character_and_representation(self) -> None:
        self.fx.write("w/c/CHARACTER.yml", """
            name: Don
            representation: {consent: maybe}
            """)
        self.fx.write("w/d/CHARACTER.yml", "character:\n  name: Ann\n  representation: not a map\n")
        r = rules(self.fx.lint())
        self.assertEqual(r[("representation.consent", "enum")].severity, "error")
        self.assertEqual(r[("character.representation", "shape")].severity, "error")

    def test_schema_descriptions_are_not_objects(self) -> None:
        self.fx.write("w/a/CARD.yml", """
            schema:
              keys:
                advertisements: {shape: map}
            advertisement_schema:
              advertisements: [a, b]
            """)
        self.assertEqual(self.fx.lint(), [])

    def test_cards_mode_restricts_to_projection_rules(self) -> None:
        self.fx.write("w/a/CARD.yml", """
            tier: 9
            references: [x]
            type: [a, b]
            advertisements: [{score: 80}]
            """)
        self.fx.write("w/a/ROOM.yml", "advertisements: [{score: 80}]\n")
        got = {(f.file, f.rule) for f in self.fx.lint(cards=True)}
        self.assertEqual(got, {("w/a/CARD.yml", "type-list"), ("w/a/CARD.yml", "shape.advertisements-list")})

    def test_missing_schemas_degrade(self) -> None:
        fx = Fixture(schemas={})
        try:
            fx.write("w/a/CARD.yml", "type: [a]\ntier: 9\nmethods: [x]\nadvertisements:\n  A: {score: 500}\n")
            got = {f.rule for f in fx.lint()}
            self.assertEqual(got, {"type-list", "shape.methods-list"})
        finally:
            fx.close()

    def test_recursive_anchor_does_not_crash(self) -> None:
        self.fx.write("w/o/loop.yml", "a: &x\n  methods: {LOOK: {invoked_by: nobody}}\n  b: *x\n")
        f = self.fx.lint()
        self.assertTrue(all(x.rule != "internal" for x in f))

    def test_cli_exit_codes_formats_and_summary(self) -> None:
        self.fx.write("w/a/CARD.yml", "type: [a, b]\n")
        code, out = self.fx.cli(str(self.fx.root / "w"))
        self.assertEqual(code, 0)
        self.assertIn("[type-list]", out)
        self.fx.write("w/b/CARD.yml", "methods: [x]\n")
        code, out = self.fx.cli(str(self.fx.root / "w"), "--format", "yaml")
        self.assertEqual(code, 1)
        self.assertEqual({d["rule"] for d in yaml.safe_load(out)}, {"type-list", "shape.methods-list"})
        code, out = self.fx.cli(str(self.fx.root / "w"), "--summary", "--format", "yaml")
        s = yaml.safe_load(out)
        self.assertEqual(s["totals"], {"error": 1, "warning": 1, "info": 0})
        self.assertEqual(s["schemas_missing"], [])
        code, out = self.fx.cli(str(self.fx.root / "w"), "--cards", "--summary")
        self.assertIn("type-list", out)
        self.assertIn("files scanned:   2", out)


if __name__ == "__main__":
    unittest.main()
