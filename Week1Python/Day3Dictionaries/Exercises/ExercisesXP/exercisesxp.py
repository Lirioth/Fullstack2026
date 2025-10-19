"""Module: exercisesxp
Purpose: Day 3 XP dictionary exercises with reusable helpers for reports and mappings.
Author: Kevin Cusnir 'Lirioth'
Created: 2025-10-18
Last Updated: 2025-10-19

Overview:
    - Pair lists using ``zip``
    - Ticket pricing logic for Cinemax
    - Zara brand manipulation and summaries
    - Disney character dictionary mappings
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple


# 🎯 Constants for Cinemax pricing
TICKET_FREE_AGE = 3
TICKET_CHILD_AGE = 12
TICKET_CHILD_PRICE = 10
TICKET_ADULT_PRICE = 15


def build_dict(keys: Iterable[str], values: Iterable[int]) -> Dict[str, int]:
    """Return a dictionary by zipping the supplied keys and values."""

    return dict(zip(keys, values))


def ticket_price(age: int) -> int:
    """Return ticket price for a single age."""

    if age < TICKET_FREE_AGE:
        return 0
    if age <= TICKET_CHILD_AGE:
        return TICKET_CHILD_PRICE
    return TICKET_ADULT_PRICE


@dataclass
class FamilyTicketSummary:
    lines: List[str]
    total: int


def cinemax_report(family: Dict[str, int]) -> FamilyTicketSummary:
    """Return the printable lines and total cost for a family dictionary."""

    lines: List[str] = []
    total = 0
    for name, age in family.items():
        price = ticket_price(age)
        total += price
        lines.append(f"{name} pays {price}")
    return FamilyTicketSummary(lines=lines, total=total)


def update_brand(brand: Dict[str, object]) -> Dict[str, object]:
    """Apply the sequence of transformations from the exercise and return the new dict."""

    brand = dict(brand)  # shallow copy to avoid mutating input
    brand["number_stores"] = 2
    brand["country_creation"] = "Spain"
    competitors = brand.setdefault("international_competitors", [])
    if "Desigual" not in competitors:
        competitors.append("Desigual")
    brand.pop("creation_date", None)
    more_on_zara = {"creation_date": 1975, "number_stores": 10000}
    brand.update(more_on_zara)
    return brand


def brand_summary(brand: Dict[str, object]) -> Dict[str, object]:
    """Create the summary values printed in the exercise."""

    updated = update_brand(brand)
    return {
        "clients": ", ".join(updated.get("type_of_clothes", [])),
        "last_competitor": updated.get("international_competitors", [])[-1],
        "us_colors": updated.get("major_color", {}).get("US"),
        "num_keys": len(updated),
        "keys": list(updated.keys()),
        "merged_brand": updated,
    }


def disney_mappings(users: Iterable[str]) -> Tuple[Dict[str, int], Dict[int, str], Dict[str, int]]:
    """Return the three dictionaries created in the exercise."""

    users = list(users)
    char_to_index = {name: idx for idx, name in enumerate(users)}
    index_to_char = {idx: name for idx, name in enumerate(users)}
    sorted_mapping = {name: idx for idx, name in enumerate(sorted(users))}
    return char_to_index, index_to_char, sorted_mapping


def _bonus_prompt() -> None:
    """Handle the interactive bonus prompt for additional family members."""

    extra_total = 0
    ans = input("Add extra family? (y/n): ").strip().lower()
    while ans == "y":
        nm = input("name: ").strip()
        age_input = input("age: ").strip()
        try:
            ag = int(age_input)
            if ag < 0:
                print("⚠️ Age cannot be negative. Skipping...")
                ans = input("Add extra family? (y/n): ").strip().lower()
                continue
        except ValueError:
            print("❌ Invalid age! Please enter a number. Skipping...")
            ans = input("Add extra family? (y/n): ").strip().lower()
            continue

        price = ticket_price(ag)
        print(nm, "pays", price)
        extra_total += price
        ans = input("Add extra family? (y/n): ").strip().lower()
    if extra_total:
        print("extra total:", extra_total)


def _cli() -> None:
    """Reproduce the original console output for the exercises."""

    keys = ["Ten", "Twenty", "Thirty"]
    values = [10, 20, 30]
    print(build_dict(keys, values))

    family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
    summary = cinemax_report(family)
    for line in summary.lines:
        print(line)
    print("total:", summary.total)
    _bonus_prompt()

    brand = {
        "name": "Zara",
        "creation_date": 1975,
        "creator_name": "Amancio Ortega Gaona",
        "type_of_clothes": ["men", "women", "children", "home"],
        "international_competitors": ["Gap", "H&M", "Benetton"],
        "number_stores": 7000,
        "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
    }
    brand_stats = brand_summary(brand)
    print("Zara clients:", brand_stats["clients"])
    print("last competitor:", brand_stats["last_competitor"])
    print("US colors:", brand_stats["us_colors"])
    print("num keys:", brand_stats["num_keys"])
    print("keys:", brand_stats["keys"])
    print("merged brand:", brand_stats["merged_brand"])

    users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
    d1, d2, d3 = disney_mappings(users)
    print(d1)
    print(d2)
    print(d3)


if __name__ == "__main__":
    _cli()