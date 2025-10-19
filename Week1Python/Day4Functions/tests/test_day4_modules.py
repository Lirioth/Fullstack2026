"""Module: test_day4_modules
Purpose: Regression tests for Day 4 function exercises and challenges.
Author: Kevin Cusnir "Lirioth"
Created: 2025-10-19
Last Updated: 2025-10-19
"""

from __future__ import annotations

import importlib.util
from contextlib import contextmanager, redirect_stdout
from datetime import date
from pathlib import Path
import sys
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(module_name: str, relative_path: Path) -> object:
    """Load a module from file while registering it in sys.modules."""
    spec = importlib.util.spec_from_file_location(module_name, str(relative_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {module_name} from {relative_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


XP_PATH = PROJECT_ROOT / "Exercises" / "ExercisesXP" / "exercisesxp.py"
GOLD_PATH = PROJECT_ROOT / "Exercises" / "ExercisesXPGold" / "xpgoldfunctions.py"
NINJA_PATH = PROJECT_ROOT / "Exercises" / "ExercisesXPNinja" / "xpninjafunctionssingle.py"
MATRIX_PATH = PROJECT_ROOT / "DailyChallenge" / "SolveTheMatrix" / "solvethematrix.py"

exercisesxp = load_module("day4_exercisesxp", XP_PATH)
xpgoldfunctions = load_module("day4_xpgoldfunctions", GOLD_PATH)
xpninjafunctionssingle = load_module("day4_xpninjafunctions", NINJA_PATH)
solvethematrix = load_module("day4_solvethematrix", MATRIX_PATH)


@contextmanager
def override_throw_dice(*values: int):
    """Temporarily replace throw_dice with deterministic outputs."""
    original = xpgoldfunctions.throw_dice
    sequence = iter(values)

    def _mock() -> int:
        return next(sequence)

    xpgoldfunctions.throw_dice = _mock  # type: ignore[assignment]
    try:
        yield
    finally:
        xpgoldfunctions.throw_dice = original  # type: ignore[assignment]


class ExercisesXpTests(unittest.TestCase):
    """Tests for the core XP helper functions."""

    def test_make_great_mutation(self) -> None:
        """make_great should append the honorific in-place."""
        names = ["Alice", "Bob"]
        exercisesxp.make_great(names)
        self.assertEqual(names, ["Alice the Great", "Bob the Great"])

    def test_get_temp_advice_thresholds(self) -> None:
        """Advice strings should reflect temperature bands."""
        self.assertIn("freezing", exercisesxp.get_temp_advice(-5))
        self.assertIn("chilly", exercisesxp.get_temp_advice(10))
        self.assertIn("Nice", exercisesxp.get_temp_advice(20))
        self.assertIn("warm", exercisesxp.get_temp_advice(28))
        self.assertIn("hot", exercisesxp.get_temp_advice(40))

    def test_get_random_temp_bounds(self) -> None:
        """Random temperature respects provided bounds."""
        for _ in range(10):
            temp = exercisesxp.get_random_temp(min_temp=-2, max_temp=2)
            self.assertGreaterEqual(temp, -2)
            self.assertLessEqual(temp, 2)


class XpGoldFunctionsTests(unittest.TestCase):
    """Regression coverage for gold-level functions."""

    def tearDown(self) -> None:
        xpgoldfunctions.TODAY_OVERRIDE = None

    def test_can_retire_logic(self) -> None:
        """Retirement eligibility depends on gender and computed age."""
        xpgoldfunctions.TODAY_OVERRIDE = date(2025, 10, 19)
        self.assertTrue(xpgoldfunctions.can_retire("m", "1950/10/19"))
        self.assertFalse(xpgoldfunctions.can_retire("f", "1970/10/19"))

    def test_series_sum_pattern(self) -> None:
        """Series sum mirrors the X + XX + XXX + XXXX pattern."""
        self.assertEqual(xpgoldfunctions.series_sum(3), 3702)

    def test_throw_until_doubles_deterministic(self) -> None:
        """Deterministic throw_dice should lead to predictable loop count."""
        with override_throw_dice(3, 4, 5, 5):
            self.assertEqual(xpgoldfunctions.throw_until_doubles(), 2)


class XpNinjaFunctionTests(unittest.TestCase):
    """Validation for ninja-level helpers."""

    def test_get_full_name_variations(self) -> None:
        """Names should be capitalized correctly with optional middle name."""
        self.assertEqual(
            xpninjafunctionssingle.get_full_name(
                first_name="john", middle_name="hooker", last_name="lee"
            ),
            "John Hooker Lee",
        )
        self.assertEqual(
            xpninjafunctionssingle.get_full_name(first_name="bruce", last_name="lee"),
            "Bruce Lee",
        )

    def test_text_to_morse_roundtrip(self) -> None:
        """Translating to Morse and back should yield the original text."""
        message = "SOS HELP 123"
        morse = xpninjafunctionssingle.text_to_morse(message)
        self.assertEqual(xpninjafunctionssingle.morse_to_text(morse), message)

    def test_box_printer_dimensions(self) -> None:
        """Box printer should produce consistent top and bottom borders."""
        from io import StringIO

        buffer = StringIO()
        with redirect_stdout(buffer):
            frame = xpninjafunctionssingle.box_printer("Hi", "Team")
        lines = frame.splitlines()
        self.assertTrue(lines[0].startswith("****"))
        self.assertEqual(lines[0], lines[-1])

    def test_insertion_sort(self) -> None:
        """Insertion sort should order the list in ascending order."""
        data = [5, 2, 4, 6, 1, 3]
        xpninjafunctionssingle.insertion_sort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5, 6])


class SolveTheMatrixTests(unittest.TestCase):
    """Regression coverage for the matrix decoder."""

    def test_decode_matrix_sentence(self) -> None:
        """Decoder should remove punctuation and preserve words."""
        matrix = """7ir\nTsi\nh%x\ni ?\nsM# \n$a \n#t%"""
        self.assertEqual(solvethematrix.decode_matrix(matrix), "This is Matrix")


if __name__ == "__main__":
    unittest.main()
