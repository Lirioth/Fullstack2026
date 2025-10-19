"""Module: test_day3_modules
Purpose: Regression coverage for Day 3 dictionary-focused helpers.
Author: Kevin Cusnir "Lirioth"
Created: 2025-10-19
Last Updated: 2025-10-19
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_module(module_name: str, relative_path: Path) -> object:
    """Load a module from file without polluting sys.modules."""
    spec = importlib.util.spec_from_file_location(module_name, str(relative_path))
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {module_name} from {relative_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


XP_PATH = PROJECT_ROOT / "Exercises" / "ExercisesXP" / "exercisesxp.py"
XP_GOLD_PATH = PROJECT_ROOT / "Exercises" / "ExercisesXPGold" / "exercisesxpgold.py"
XP_PLUS_PATH = PROJECT_ROOT / "Exercises" / "ExercisesXP+" / "exercisesxpplus.py"
XPNINJA_PATH = PROJECT_ROOT / "Exercises" / "ExercisesXPNinja" / "xpninjacars.py"
DAILY_DICT_PATH = PROJECT_ROOT / "DailyChallenge" / "Dictionaries" / "dictionaries.py"
CAESAR_PATH = PROJECT_ROOT / "DailyChallenge" / "CaesarCypher" / "caesarcipher.py"

exercisesxp = load_module("day3_exercisesxp", XP_PATH)
exercisesxpgold = load_module("day3_exercisesxpgold", XP_GOLD_PATH)
exercisesxpplus = load_module("day3_exercisesxpplus", XP_PLUS_PATH)
xpninjacars = load_module("day3_xpninjacars", XPNINJA_PATH)
daily_dicts = load_module("day3_daily_dicts", DAILY_DICT_PATH)
caesarcipher = load_module("day3_caesarcipher", CAESAR_PATH)


class ExercisesXpTests(unittest.TestCase):
    """Tests for the Day 3 XP practice helpers."""

    def test_build_dict_pairs(self) -> None:
        """Ensure build_dict zips keys and values in order."""
        result = exercisesxp.build_dict(["One", "Two"], [1, 2])
        self.assertEqual(result, {"One": 1, "Two": 2})

    def test_ticket_price_tiers(self) -> None:
        """Ticket pricing should match infant, child, and adult tiers."""
        self.assertEqual(exercisesxp.ticket_price(2), 0)
        self.assertEqual(exercisesxp.ticket_price(10), exercisesxp.TICKET_CHILD_PRICE)
        self.assertEqual(exercisesxp.ticket_price(42), exercisesxp.TICKET_ADULT_PRICE)

    def test_cinemax_report_totals(self) -> None:
        """Cinema report should sum prices across family members."""
        family = {"rick": 43, "beth": 13, "morty": 5}
        summary = exercisesxp.cinemax_report(family)
        self.assertEqual(summary.lines, ["rick pays 15", "beth pays 15", "morty pays 10"])
        self.assertEqual(summary.total, 40)

    def test_brand_summary_competitors(self) -> None:
        """Brand summary should append the Desigual competitor and count keys."""
        brand = {
            "name": "Zara",
            "creation_date": 1975,
            "creator_name": "Amancio Ortega Gaona",
            "type_of_clothes": ["men", "women"],
            "international_competitors": ["Gap"],
            "number_stores": 7000,
            "major_color": {"US": ["pink", "green"]},
        }
        summary = exercisesxp.brand_summary(brand)
        self.assertIn("Desigual", summary["merged_brand"]["international_competitors"])
        self.assertEqual(summary["last_competitor"], "Desigual")
        self.assertIsNotNone(summary["us_colors"])

    def test_disney_mappings(self) -> None:
        """Check that all three Disney dictionaries align with expectations."""
        names = ["Mickey", "Donald", "Ariel"]
        forward, inverse, sorted_map = exercisesxp.disney_mappings(names)
        self.assertEqual(forward["Donald"], 1)
        self.assertEqual(inverse[2], "Ariel")
        self.assertEqual(list(sorted_map.keys()), ["Ariel", "Donald", "Mickey"])


class DailyChallengeTests(unittest.TestCase):
    """Coverage for Day 3 daily challenge helpers."""

    def test_letter_indices_positions(self) -> None:
        """Ensure duplicate characters store multiple indices."""
        indices = daily_dicts.letter_indices("banana")
        self.assertEqual(indices["a"], [1, 3, 5])

    def test_affordable_items_filter(self) -> None:
        """Affordable items should be sorted alphabetically within budget."""
        items = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
        self.assertEqual(daily_dicts.affordable_items(items, "$20"), ["Bread", "Fertilizer", "Water"])


class CaesarCipherTests(unittest.TestCase):
    """Validation for Caesar cipher helpers."""

    def test_encrypt_decrypt_roundtrip(self) -> None:
        """Decrypting an encrypted message should return the original text."""
        message = "Hello, World!"
        cipher = caesarcipher.encrypt(message, 5)
        self.assertEqual(caesarcipher.decrypt(cipher, 5), message)

    def test_bruteforce_contains_plaintext(self) -> None:
        """Brute force should list the original plaintext in its options."""
        options = list(caesarcipher.brute_force("Khoor"))
        matches = [line for line in options if "Hello" in line]
        self.assertTrue(matches)


class ExercisesXpGoldTests(unittest.TestCase):
    """Validation for Day 3 gold helpers."""

    def test_add_and_lookup_birthday(self) -> None:
        """Birthdays should be stored and retrieved correctly."""
        book = exercisesxpgold.add_birthday(exercisesxpgold.DEFAULT_BIRTHDAYS, "Frank", "1985/02/14")
        self.assertEqual(exercisesxpgold.lookup_birthday(book, "Frank"), "1985/02/14")

    def test_stock_value_totals(self) -> None:
        """Stock valuation should multiply price by stock."""
        inventory = {
            "banana": {"price": 4, "stock": 10},
            "apple": {"price": 2, "stock": 5},
        }
        self.assertEqual(exercisesxpgold.stock_value(inventory), 4 * 10 + 2 * 5)


class ExercisesXpPlusTests(unittest.TestCase):
    """Regression tests for XP+ analytical helpers."""

    def test_calculate_student_grades(self) -> None:
        """Student grade report should compute averages and letters."""
        grades = {"Student": [100, 90]}
        report = exercisesxpplus.calculate_student_grades(grades)
        self.assertAlmostEqual(report.class_average, 95.0)
        self.assertEqual(report.letter_grades["Student"], "A")

    def test_analyse_sales_data(self) -> None:
        """Sales analysis should flag high-value transactions and loyalty."""
        transactions = [
            {"customer_id": 1, "product": "Phone", "price": 600, "quantity": 1, "date": "2024-01-01"},
            {"customer_id": 1, "product": "Case", "price": 25, "quantity": 2, "date": "2024-01-02"},
            {"customer_id": 2, "product": "Tablet", "price": 300, "quantity": 3, "date": "2024-01-03"},
        ]
        report = exercisesxpplus.analyse_sales_data(transactions)
        self.assertIn(1, report.loyal_customers)
        self.assertTrue(any(txn["product"] == "Tablet" for txn in report.high_value_transactions))
        self.assertIn("Phone", report.product_totals)


class XpNinjaCarsTests(unittest.TestCase):
    """Validation for ninja manufacturer helpers."""

    def test_parse_and_deduplicate(self) -> None:
        """Parsing should trim whitespace and deduplicate correctly."""
        raw = "Ford, Toyota, Ford"
        manufacturers = xpninjacars.parse_manufacturers(raw)
        self.assertEqual(manufacturers, ["Ford", "Toyota", "Ford"])
        self.assertEqual(xpninjacars.deduplicate_preserve_order(manufacturers), ["Ford", "Toyota"])

    def test_sort_and_letter_counts(self) -> None:
        """Sorting and letter counting should be case insensitive."""
        names = ["Audi", "BMW", "chevrolet"]
        self.assertEqual(xpninjacars.sort_descending(names), ["chevrolet", "BMW", "Audi"])
        self.assertEqual(xpninjacars.count_with_letter(names, "a"), 1)
        self.assertEqual(xpninjacars.count_without_letter(names, "a"), 2)
        self.assertEqual(xpninjacars.ascending_reversed(names), ["iduA", "WMB", "telorvehc"])


if __name__ == "__main__":
    unittest.main()
