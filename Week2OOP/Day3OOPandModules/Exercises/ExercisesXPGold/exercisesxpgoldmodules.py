"""
File: exercisesxpgoldmodules.py
Purpose: Single-file solutions for "Exercises XP Gold — Modules". 🧠📦
Author: Kevin "Lirioth" Cusnir
Date: 2025-10-11 | TZ: Asia/Jerusalem
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, date, time, timedelta
from typing import Dict, Iterable, List, Optional, Tuple

try:
    import holidays  # type: ignore
except Exception:
    holidays = None

import math
import re
import secrets
import string
import random

DEFAULT_FALLBACK_HOLIDAYS = [
    (1, 1, "New Year's Day"),
    (2, 14, "Valentine's Day"),
    (5, 1, "Labor Day"),
    (7, 4, "Independence Day"),
    (10, 31, "Halloween"),
    (12, 25, "Christmas Day"),
    (12, 31, "New Year's Eve"),
]

def today_and_next_holiday(*, country: str = "US") -> Tuple[datetime, date, str, timedelta]:
    now = datetime.now()
    today_date = now.date()

    if holidays is not None:
        try:
            try:
                cal = holidays.country_holidays(country)  # type: ignore[attr-defined]
            except Exception:
                cal = holidays.country_holidays("US")  # type: ignore[attr-defined]
            for offset in range(0, 370):
                d = today_date + timedelta(days=offset)
                name = cal.get(d)
                if name:
                    delta = datetime.combine(d, time.min) - now
                    if delta.total_seconds() < 0 and offset == 0:
                        continue
                    return now, d, str(name), delta if offset == 0 else (datetime.combine(d, time.min) - now)
        except Exception:
            pass

    for _ in range(2):
        candidates = []
        y = today_date.year
        for m, day, nm in DEFAULT_FALLBACK_HOLIDAYS:
            try:
                d = date(y, m, day)
            except ValueError:
                continue
            if d >= today_date:
                candidates.append((d, nm))
        if candidates:
            candidates.sort(key=lambda t: t[0])
            next_date, name = candidates[0]
            delta = datetime.combine(next_date, time.min) - now
            if delta.total_seconds() < 0 and next_date == today_date:
                if len(candidates) > 1:
                    next_date, name = candidates[1]
                    delta = datetime.combine(next_date, time.min) - now
            return now, next_date, name, delta
        today_date = date(y + 1, 1, 1)

    next_date = date(datetime.now().year + 1, 1, 1)
    return now, next_date, "New Year's Day", datetime.combine(next_date, time.min) - now

EARTH_SECONDS = 31_557_600
ORBITAL_PERIODS = {
    "Mercury": 0.2408467,
    "Venus": 0.61519726,
    "Earth": 1.0,
    "Mars": 1.8808158,
    "Jupiter": 11.862615,
    "Saturn": 29.447498,
    "Uranus": 84.016846,
    "Neptune": 164.79132,
}
def space_age(seconds: int | float) -> Dict[str, float]:
    if seconds < 0:
        raise ValueError("seconds must be non-negative")
    return {planet: (seconds / (EARTH_SECONDS * period)) for planet, period in ORBITAL_PERIODS.items()}

def return_numbers(s: str) -> str:
    return "".join(re.findall(r"\d", s))

NAME_PATTERN = re.compile(r"^[A-Z][a-z]+ [A-Z][a-z]+$")
def is_valid_full_name(name: str) -> bool:
    return bool(NAME_PATTERN.fullmatch(name))

DIGITS = string.digits
LOWERS = string.ascii_lowercase
UPPERS = string.ascii_uppercase
SPECIALS = "!@#$%^&*()-_=+[]{};:,.?/\\|`~"
ALL_CHARS = DIGITS + LOWERS + UPPERS + SPECIALS
_SEC = secrets.SystemRandom()

def generate_password(length: int) -> str:
    if not (6 <= length <= 30):
        raise ValueError("length must be between 6 and 30")
    parts = [
        _SEC.choice(DIGITS),
        _SEC.choice(LOWERS),
        _SEC.choice(UPPERS),
        _SEC.choice(SPECIALS),
    ]
    for _ in range(length - len(parts)):
        parts.append(_SEC.choice(ALL_CHARS))
    _SEC.shuffle(parts)
    return "".join(parts)

def is_valid_password(pwd: str, length: Optional[int] = None) -> bool:
    if length is not None and len(pwd) != length:
        return False
    has_digit = any(c in DIGITS for c in pwd)
    has_lower = any(c in LOWERS for c in pwd)
    has_upper = any(c in UPPERS for c in pwd)
    has_special = any(c in SPECIALS for c in pwd)
    allowed = set(ALL_CHARS)
    only_allowed = all(c in allowed for c in pwd)
    return has_digit and has_lower and has_upper and has_special and only_allowed

def password_cli() -> None:
    while True:
        raw = input("Desired password length (6–30): ").strip()
        if not raw.isdigit():
            print("Please type a number between 6 and 30.")
            continue
        n = int(raw)
        if 6 <= n <= 30:
            break
        print("Please choose a number between 6 and 30.")
    pwd = generate_password(n)
    print(f"Your new password: {pwd}")
    print("Keep it safe and never reuse passwords. 🔐")

def password_self_test(rounds: int = 100) -> None:
    for _ in range(rounds):
        n = random.randint(6, 30)
        pwd = generate_password(n)
        assert is_valid_password(pwd, n), f"Password failed validation: {pwd!r}"
    print(f"Self-test passed: {rounds} generated passwords validated. ✅")

if __name__ == "__main__":
    now, d, nm, delta = today_and_next_holiday(country="US")
    days = delta.days if delta.days >= 0 else 0
    print(f"Today: {now:%Y-%m-%d %H:%M}")
    print(f"Next holiday: {nm} on {d.isoformat()} (in ~{days} days) 🎉")

    example_seconds = 1_000_000_000
    ages = space_age(example_seconds)
    print("\nSpace age for 1,000,000,000 seconds:")
    for planet in ["Earth","Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptune"]:
        print(f"  {planet:8s}: {ages[planet]:.2f} years")

    print("\nDigits extracted:", return_numbers("k5k3q2g5z6x9bn"))

    demo_names = ["John Doe", "john doe", "John  Doe", "JohnDoe", "John D"]
    print("\nName validation:")
    for n in demo_names:
        print(f"  {n!r} -> {is_valid_full_name(n)}")

    password_self_test(100)
    # password_cli()
