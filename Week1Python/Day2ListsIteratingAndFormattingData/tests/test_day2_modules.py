"""Module: test_day2_modules
Purpose: Regression coverage for Day 2 collection and string utilities.
Author: Kevin Cusnir "Lirioth"
Created: 2025-10-19
Last Updated: 2025-10-19
"""

from __future__ import annotations

import importlib.util
import io
from contextlib import redirect_stdout
from pathlib import Path
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(module_name: str, relative_path: Path) -> object:
    """Dynamically load a module by file path for ad-hoc testing."""
    spec = importlib.util.spec_from_file_location(module_name, str(relative_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {module_name} from {relative_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


XP_PATH = PROJECT_ROOT / "Exercises" / "ExercisesXP" / "exercisesxp.py"
NINJA_PATH = PROJECT_ROOT / "Exercises" / "ExercisesXPNinja" / "exercisesxpninja.py"
LIST_CHALLENGE_PATH = PROJECT_ROOT / "DailyChallenge" / "ListAndStrings" / "dailychallengelistandstrings.py"
BIRTHDAY_PATH = PROJECT_ROOT / "DailyChallenge" / "GoldHappyBirthday" / "happybirthday.py"

exercisesxp = load_module("day2_exercisesxp", XP_PATH)
exercisesxpninja = load_module("day2_exercisesxpninja", NINJA_PATH)
list_challenge = load_module("day2_listchallenge", LIST_CHALLENGE_PATH)
happybirthday = load_module("day2_happybirthday", BIRTHDAY_PATH)


class ExercisesXpTests(unittest.TestCase):
    """Unit coverage for common helper functions in Exercises XP."""

    def test_calculate_pizza_price(self) -> None:
        """Ensure topping counts scale price correctly."""
        toppings = ["cheese", "mushroom", "pepperoni"]
        expected = exercisesxp.BASE_PIZZA_PRICE + exercisesxp.TOPPING_PRICE * len(toppings)
        self.assertAlmostEqual(exercisesxp.calculate_pizza_price(toppings), expected)

    def test_calculate_ticket_price_branches(self) -> None:
        """Validate ticket prices for infant, child, and adult ranges."""
        self.assertEqual(exercisesxp.calculate_ticket_price(2), exercisesxp.TICKET_PRICE_INFANT)
        self.assertEqual(exercisesxp.calculate_ticket_price(10), exercisesxp.TICKET_PRICE_CHILD)
        self.assertEqual(exercisesxp.calculate_ticket_price(35), exercisesxp.TICKET_PRICE_ADULT)


class DailyChallengeListTests(unittest.TestCase):
    """Coverage for list and string focused daily challenge helpers."""

    def test_multiples_generation(self) -> None:
        """Multiples should scale linearly and handle zeros."""
        self.assertEqual(list_challenge.multiples(3, 4), [3, 6, 9, 12])
        self.assertEqual(list_challenge.multiples(5, 0), [])

    def test_multiples_negative_length_guard(self) -> None:
        """Negative lengths should raise ValueError to protect learners."""
        with self.assertRaises(ValueError):
            list_challenge.multiples(1, -1)

    def test_collapse_duplicates_behavior(self) -> None:
        """Ensure consecutive duplicates collapse while separated ones remain."""
        self.assertEqual(list_challenge.collapse_duplicates("ppoollee"), "pole")
        self.assertEqual(list_challenge.collapse_duplicates("AaAa"), "AaAa")
        self.assertEqual(list_challenge.collapse_duplicates(""), "")


class ExercisesGoldTests(unittest.TestCase):
    """Regression coverage for Gold-level utilities."""

    def test_q_values_reference_example(self) -> None:
        """Confirm Q values match the documented worked example."""
        self.assertEqual(exercisesxpninja.q_values([100, 150, 180]), [18, 22, 24])

    def test_number_report_consistency(self) -> None:
        """Manual stats should align with Python's built-ins."""
        report = exercisesxpninja.number_report(exercisesxpninja.NUMS)
        self.assertEqual(report["manual_sum"], report["sum"])
        self.assertEqual(report["manual_avg"], report["avg"])
        self.assertEqual(report["manual_max"], report["max"])
        self.assertEqual(report["manual_min"], report["min"])

    def test_analyse_paragraph_sentence_count(self) -> None:
        """Verify paragraph stats include sentence tally and word count."""
        stats = exercisesxpninja.analyse_paragraph(exercisesxpninja.PARAGRAPH)
        self.assertEqual(stats["sentences"], 4)
        self.assertEqual(stats["words"], 19)

    def test_word_frequency_sorted(self) -> None:
        """Frequencies should be alphabetically ordered in output."""
        mapping = exercisesxpninja.word_frequency(["banana", "apple", "banana"])
        self.assertEqual(list(mapping.items()), [("apple", 1), ("banana", 2)])


class HappyBirthdayTests(unittest.TestCase):
    """Regression coverage for the Happy Birthday ASCII helper."""

    def test_print_cake_candles_rendering(self) -> None:
        """Validate that the candle count appears on the first cake row."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            happybirthday.print_cake(4)
        first_line = buffer.getvalue().splitlines()[0]
        self.assertIn("iiii", first_line)
        self.assertTrue(first_line.startswith("       ___"))


if __name__ == "__main__":
    unittest.main()
