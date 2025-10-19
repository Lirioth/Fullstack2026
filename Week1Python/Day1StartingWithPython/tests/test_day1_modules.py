"""Module: test_day1_modules
Purpose: Basic regression tests for Day 1 Python exercises without third-party dependencies.
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


BUILD_UP_PATH = PROJECT_ROOT / "DailyChallenge" / "BuildUpAString" / "buildupastring.py"
GOLD_PATH = PROJECT_ROOT / "Exercises" / "ExercisesXPGold" / "exercisesxpgold.py"

buildupastring = load_module("buildupastring", BUILD_UP_PATH)
exercisesxpgold = load_module("exercisesxpgold", GOLD_PATH)


class BuildUpStringTests(unittest.TestCase):
    """Regression coverage for Day 1 Daily Challenge helpers."""

    def test_validate_length_feedback(self) -> None:
        """Ensure validate_length flags short, long, and valid strings correctly."""
        self.assertEqual(
            buildupastring.validate_length("short"),
            (False, "String not long enough."),
        )
        self.assertEqual(
            buildupastring.validate_length("abcdefghij"),
            (True, "Perfect string"),
        )
        self.assertEqual(
            buildupastring.validate_length("too_long_text"),
            (False, "String too long."),
        )

    def test_build_up_text_sequence(self) -> None:
        """Verify build_up_text emits incremental substrings in order."""
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            buildupastring.build_up_text("abc")
        self.assertEqual(buffer.getvalue().splitlines(), ["a", "ab", "abc"])

    def test_jumble_text_preserves_characters(self) -> None:
        """Check that jumble_text returns a permutation with identical characters."""
        original = "abcdefghij"
        shuffled = buildupastring.jumble_text(original)
        self.assertEqual(sorted(shuffled), sorted(original))
        self.assertEqual(len(shuffled), len(original))
        self.assertEqual(set(shuffled), set(original))


class ExercisesGoldTests(unittest.TestCase):
    """Regression coverage for Exercises XP Gold helpers."""

    def test_get_season_mapping(self) -> None:
        """Confirm that month numbers map to the expected seasons with emojis."""
        self.assertEqual(exercisesxpgold.get_season(3), "Spring 🌸")
        self.assertEqual(exercisesxpgold.get_season(7), "Summer ☀️")
        self.assertEqual(exercisesxpgold.get_season(10), "Autumn 🍂")
        self.assertEqual(exercisesxpgold.get_season(1), "Winter ❄️")


if __name__ == "__main__":
    unittest.main()
