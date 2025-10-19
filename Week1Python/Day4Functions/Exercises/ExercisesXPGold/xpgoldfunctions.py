"""Module: xpgoldfunctions
Purpose: Day 4 gold exercises for retirement checks, summations, and dice stats.
Author: Kevin Cusnir 'Lirioth'
Created: 2025-10-18
Last Updated: 2025-10-19

Overview:
    - Age calculation with retirement eligibility
    - Series sum via string repetition
    - Dice simulation with doubles tracking
"""

# XP Gold — Functions (short & simple)
# 🚀 Run: python3 xpgoldfunctions.py

from __future__ import annotations

import datetime
import random

# --- Exercise 1: When will I retire? ---

# Allow overriding today's date for deterministic tests 📆
TODAY_OVERRIDE = None


def get_today():
    """Return today's date, using an override when provided."""
    return TODAY_OVERRIDE or datetime.date.today()

def get_age(year, month, day):
    """Return age in whole years based on the current date."""
    today = get_today()
    age = today.year - year
    # If birthday hasn't happened yet this year -> subtract 1 🎂
    if (today.month, today.day) < (month, day):
        age -= 1
    return age

def can_retire(gender, date_of_birth):
    """Return True if person can retire (men:67, women:62), else False.
    - gender: 'm' or 'f' (case-insensitive)
    - date_of_birth: 'yyyy/mm/dd'
    - Raises ValueError for invalid gender inputs.
    """
    gender = gender.strip().lower()
    if gender not in {"m", "f"}:
        raise ValueError("Invalid gender 🚫: expected 'm' or 'f'.")
    y, m, d = map(int, date_of_birth.strip().split("/"))
    age = get_age(y, m, d)
    retirement_age = 67 if gender == "m" else 62
    return age >= retirement_age

# --- Exercise 2: Sum (X + XX + XXX + XXXX) ---

def series_sum(x):
    """Return X + XX + XXX + XXXX using string repetition."""
    return sum(int(str(x) * k) for k in range(1, 5))

# --- Exercise 3: Double Dice ---

def throw_dice():
    """Return a random die roll from 1..6."""
    return random.randint(1, 6)

def throw_until_doubles():
    """Throw two dice until both match; return number of throws."""
    throws = 0
    while True:
        throws += 1
        a, b = throw_dice(), throw_dice()
        if a == b:
            return throws

def main():
    """Run the doubles experiment 100 times; print total and average."""
    results = [throw_until_doubles() for _ in range(100)]
    total = sum(results)
    avg = total / len(results)
    print(f"Total throws: {total}")
    print(f"Average throws to reach doubles: {avg:.2f}")

if __name__ == "__main__":
    # Small interactive demo
    print("=== Exercise 1 ===")
    g = input("Gender (m/f): ")
    dob = input("DOB (yyyy/mm/dd): ")
    print("You can retire." if can_retire(g, dob) else "You cannot retire yet.")

    print("\n=== Exercise 2 ===")
    x = int(input("Enter a digit X: "))
    print("Result:", series_sum(x))

    print("\n=== Exercise 3 ===")
    # random.seed(0)  # uncomment for reproducible tests
    main()
