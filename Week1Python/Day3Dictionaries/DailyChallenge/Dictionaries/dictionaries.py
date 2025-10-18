"""
Daily Challenge - Dictionaries
==============================
Comprehensive dictionary manipulation challenges.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 3 - Dictionaries
Python Version: 3.8+
"""

from __future__ import annotations

from typing import Dict, List


# Challenge 1: Letter Index Dictionary
def letter_indices(word: str) -> Dict[str, List[int]]:
    """Return a dictionary mapping characters to the indices they occupy."""

    positions: Dict[str, List[int]] = {}
    for idx, ch in enumerate(word):
        positions.setdefault(ch, []).append(idx)
    return positions


# Challenge 2: Affordable Items
def to_int(value: str) -> int:
    """Convert a currency string like "$1,000" into an integer value."""

    return int(value.replace("$", "").replace(",", "").strip())


def affordable_items(items: Dict[str, str], wallet: str) -> List[str]:
    """Return a sorted list of item names that fit within the wallet amount."""

    limit = to_int(wallet)
    return sorted(name for name, price in items.items() if to_int(price) <= limit)


def _cli() -> None:
    """Run the original examples and prompt for the first challenge."""

    word = input("Enter a word: ")
    print(letter_indices(word))

    examples = [
        ({"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}, "$300"),
        (
            {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"},
            "$100",
        ),
        ({"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}, "$1"),
    ]

    for items, wallet in examples:
        choices = affordable_items(items, wallet)
        print(choices if choices else "Nothing")


if __name__ == "__main__":
    _cli()
