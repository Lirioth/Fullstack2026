"""Module: happybirthday
Purpose: Interactive Day 2 Gold challenge for celebrating birthdays with ASCII art.
Author: Kevin Cusnir "Lirioth"
Created: 2025-10-18
Last Updated: 2025-10-19

Features:
    - Date parsing and validation
    - Age calculation
    - Candle count based on last digit of age
    - Leap year detection (double cake bonus!)
    - ASCII art generation
"""

from __future__ import annotations

import calendar
from datetime import date, datetime


def print_cake(candles: int) -> None:
    """
    Print ASCII art birthday cake with specified number of candles.
    
    Args:
        c: Number of candles to display (0-10 recommended)
        
    Example:
    >>> print_cake(3)
               ___iii___
              |:H:a:p:p:y:|
            __|___________|__
           |^^^^^^^^^^^^^^^^^|
           |:B:i:r:t:h:d:a:y:|
           |                 |
           ~~~~~~~~~~~~~~~~~~~
    """
    top = "       ___" + ("i" * candles) + "___"
    print(top)
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

def main() -> None:
    """
    Main interactive birthday cake program.
    
    Prompts for birthdate, calculates age, displays cake with candles.
    Shows double cake if born in a leap year.
    """
    s = input("Enter your birthdate (DD/MM/YYYY): ").strip()

    try:
        bday = datetime.strptime(s, "%d/%m/%Y").date()
    except ValueError:
        print("Please use DD/MM/YYYY and ensure the date is valid.")
        return

    today = date.today()
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))

    candles = age % 10  # ✅ Only print the last digit worth of candles.

    if calendar.isleap(bday.year):
        # 🎉 Leap babies deserve a double celebration!
        print_cake(candles)
        print_cake(candles)
    else:
        print_cake(candles)


if __name__ == "__main__":
    main()
