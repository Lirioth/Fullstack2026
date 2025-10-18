"""
🥇 Day 2 - Exercises XP Ninja
=============================
Advanced challenges covering:
1. Mathematical formula implementation (Q = sqrt((2*C*D)/H))
2. Comprehensive list analysis with manual statistics
3. Text paragraph analysis with frequency counting
4. Word frequency mapping with sorted output

Author: Kevin Cusnir "Lirioth"
GitHub: @Lirioth
Repository: https://github.com/Lirioth/Fullstack2026
Course: Fullstack Bootcamp 2026
Python Version: 3.8+
Last Updated: October 18, 2025
"""

# Exercises XP Ninja

from __future__ import annotations

from collections import Counter
from typing import Dict, Iterable, List

C = 50
H = 30


# ---------- Exercise 1: Formula ----------
def q_values(d_values: Iterable[int], *, c: int = C, h: int = H) -> List[int]:
    """
    Calculate Q values using the formula: Q = sqrt((2 * c * d) / h).
    
    Args:
        d_values: Iterable of D values to calculate Q for
        c: Constant C (default: 50)
        h: Constant H (default: 30)
        
    Returns:
        List of Q values rounded to nearest integer
        
    Example:
        >>> q_values([100, 150, 180])
        [18, 22, 24]
    """

    results: List[int] = []
    for d in d_values:
        q = int(round(((2 * c * d) / h) ** 0.5))
        results.append(q)
    return results


# ---------- Exercise 2: List of integers ----------
NUMS = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]


def number_report(numbers: Iterable[int]) -> Dict[str, object]:
    """Return a dictionary with the stats showcased in the original script."""

    numbers = list(numbers)
    unique: List[int] = []
    manual_sum = 0
    manual_max = numbers[0]
    manual_min = numbers[0]
    for n in numbers:
        manual_sum += n
        if n > manual_max:
            manual_max = n
        if n < manual_min:
            manual_min = n
        if n not in unique:
            unique.append(n)

    return {
        "list": " ".join(str(x) for x in numbers),
        "desc": " ".join(str(x) for x in sorted(numbers, reverse=True)),
        "sum": sum(numbers),
        "first_last": [numbers[0], numbers[-1]],
        ">50": [x for x in numbers if x > 50],
        "<10": [x for x in numbers if x < 10],
        "squares": " ".join(str(x * x) for x in numbers),
        "no_dups": unique,
        "no_dups_count": len(unique),
        "avg": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "manual_sum": manual_sum,
        "manual_avg": manual_sum / len(numbers),
        "manual_max": manual_max,
        "manual_min": manual_min,
    }


# ---------- Exercise 3: Working on a paragraph ----------
PARAGRAPH = (
    "Learning Python is fun. It helps you think clearly! "
    "Python has simple syntax, yet it is powerful. Keep practicing?"
)


def analyse_paragraph(text: str) -> Dict[str, object]:
    """Return stats for the supplied paragraph."""

    sentences = text.count(".") + text.count("!") + text.count("?")
    if sentences == 0:
        sentences = 1
    words = text.split()
    cleaned = [w.strip(".,!?;:").lower() for w in words]
    freq = Counter(cleaned)
    non_unique = sum(count for count in freq.values() if count > 1)

    return {
        "chars": len(text),
        "sentences": sentences,
        "words": len(words),
        "unique_words": len(set(cleaned)),
        "non_whitespace": sum(1 for ch in text if not ch.isspace()),
        "avg_words_per_sentence": round(len(words) / sentences, 2),
        "non_unique_word_total": non_unique,
    }


# ---------- Exercise 4: Frequency Of The Words ----------
def word_frequency(tokens: Iterable[str]) -> Dict[str, int]:
    """Return a frequency mapping like the original script."""

    return dict(sorted(Counter(tokens).items()))


def _cli() -> None:
    """Run the original console interaction for the exercises."""

    raw = input("Enter D values (comma-separated): ")
    parsed = [int(part.strip()) for part in raw.split(",") if part.strip()]
    print(",".join(str(v) for v in q_values(parsed)))

    report = number_report(NUMS)
    print("list:", report["list"])
    print("desc:", report["desc"])
    print("sum:", report["sum"])
    print("first+last:", report["first_last"])
    print(">50:", report[">50"])
    print("<10:", report["<10"])
    print("squares:", report["squares"])
    print("no_dups:", report["no_dups"], "count:", report["no_dups_count"])
    print("avg:", report["avg"])
    print("max:", report["max"])
    print("min:", report["min"])
    print(
        "manual sum:",
        report["manual_sum"],
        "manual avg:",
        report["manual_avg"],
        "manual max:",
        report["manual_max"],
        "manual min:",
        report["manual_min"],
    )

    stats = analyse_paragraph(PARAGRAPH)
    print("chars:", stats["chars"])
    print("sentences:", stats["sentences"])
    print("words:", stats["words"])
    print("unique words:", stats["unique_words"])
    print("non-whitespace chars:", stats["non_whitespace"])
    print("avg words/sentence:", stats["avg_words_per_sentence"])
    print("non-unique words total count:", stats["non_unique_word_total"])

    text = input("Enter a line for word frequency: ")
    frequencies = word_frequency(text.split())
    for token, count in frequencies.items():
        print(f"{token}:{count}")


if __name__ == "__main__":
    _cli()
