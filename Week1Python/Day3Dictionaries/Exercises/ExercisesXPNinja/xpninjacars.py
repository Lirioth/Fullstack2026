#!/usr/bin/env python3
"""
Exercises XP Ninja — Exercise 1: Cars
=====================================
Reusable helpers for the manufacturer analysis plus a CLI reproducing the
original outputs. Import this module elsewhere to reuse the pure functions.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 3 - Dictionaries
Python Version: 3.8+
"""

from __future__ import annotations

from typing import Iterable, List


def parse_manufacturers(names: str) -> List[str]:
    """Return a cleaned list of manufacturer names from a comma-separated string."""

    return [name.strip() for name in names.split(",") if name.strip()]


def sort_descending(names: Iterable[str]) -> List[str]:
    """Return manufacturer names sorted Z-A, case-insensitive."""

    return sorted(names, key=lambda value: value.lower(), reverse=True)


def count_with_letter(names: Iterable[str], letter: str) -> int:
    """Count names containing ``letter`` (case-insensitive)."""

    letter = letter.lower()
    return sum(1 for name in names if letter in name.lower())


def count_without_letter(names: Iterable[str], letter: str) -> int:
    """Count names missing ``letter`` (case-insensitive)."""

    letter = letter.lower()
    return sum(1 for name in names if letter not in name.lower())


def deduplicate_preserve_order(names: Iterable[str]) -> List[str]:
    """Return the first occurrence of each name, preserving input order."""

    seen: set[str] = set()
    unique: List[str] = []
    for name in names:
        if name not in seen:
            unique.append(name)
            seen.add(name)
    return unique


def ascending_reversed(names: Iterable[str]) -> List[str]:
    """Return A-Z sorted names with each entry reversed character-wise."""

    return [name[::-1] for name in sorted(names, key=lambda value: value.lower())]


def _cli() -> None:
    """Recreate the original console output for the ninja exercise."""

    base = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
    manufacturers = parse_manufacturers(base)
    print(f"Total manufacturers: {len(manufacturers)}")
    print("Descending (Z-A):", sort_descending(manufacturers))
    print("Manufacturers with letter 'o':", count_with_letter(manufacturers, "o"))
    print(
        "Manufacturers without letter 'i':",
        count_without_letter(manufacturers, "i"),
    )

    dupes = [
        "Honda",
        "Volkswagen",
        "Toyota",
        "Ford Motor",
        "Honda",
        "Chevrolet",
        "Toyota",
    ]
    unique = deduplicate_preserve_order(dupes)
    print("No-duplicate list:", ", ".join(unique))
    print("New total (no duplicates):", len(unique))
    print("Ascending A-Z with reversed names:", ascending_reversed(manufacturers))


if __name__ == "__main__":
    _cli()
