"""
Exercises XP Gold - Advanced Dictionary Manipulation
===================================================
Complex dictionary scenarios for intermediate practice.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 3 - Dictionaries
Python Version: 3.8+
"""

from __future__ import annotations

from typing import Dict, Iterable, Tuple


DEFAULT_BIRTHDAYS = {
    "Alice": "1995/06/12",
    "Bob": "1990/01/23",
    "Charlie": "1988/11/05",
    "Dana": "1993/04/17",
    "Eli": "2000/09/30",
}


def add_birthday(birthdays: Dict[str, str], name: str, date: str) -> Dict[str, str]:
    """Return a copy of ``birthdays`` that includes the supplied ``name``."""

    updated = dict(birthdays)
    updated[name] = date
    return updated


def lookup_birthday(birthdays: Dict[str, str], name: str) -> str | None:
    """Return the birthday for ``name`` if present."""

    return birthdays.get(name)


def stock_value(items: Dict[str, Dict[str, float]]) -> float:
    """Return the total cost to purchase all stock for the provided items."""

    return sum(info["price"] * info["stock"] for info in items.values())


def _cli() -> None:
    """Reproduce the original interactive behaviour for the gold exercises."""

    birthdays = dict(DEFAULT_BIRTHDAYS)
    print("Welcome! You can look up the birthdays of the people in the list.")
    print("Names:", ", ".join(birthdays.keys()))

    new_name = input("Add a name (or press Enter to skip): ").strip()
    if new_name:
        new_bday = input("Enter birthday (YYYY/MM/DD): ").strip()
        birthdays = add_birthday(birthdays, new_name, new_bday)

    print("Names:", ", ".join(birthdays.keys()))
    name = input("Who do you want to look up? ").strip()
    match = lookup_birthday(birthdays, name)
    if match:
        print(f"{name}'s birthday is {match}")
    else:
        print(f"Sorry, we don't have the birthday information for {name}")

    prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
    for item, price in prices.items():
        print(f"{item} costs {price}")

    inventory = {
        "banana": {"price": 4, "stock": 10},
        "apple": {"price": 2, "stock": 5},
        "orange": {"price": 1.5, "stock": 24},
        "pear": {"price": 3, "stock": 1},
    }
    print("Total cost to buy everything:", stock_value(inventory))


if __name__ == "__main__":
    _cli()
