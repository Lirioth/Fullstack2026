"""
🎉 Daily Challenge GOLD: Happy Birthday
========================================
Interactive birthday cake generator with ASCII art.

Features:
- Date parsing and validation
- Age calculation
- Candle count based on last digit of age
- Leap year detection (double cake bonus!)
- ASCII art generation

Author: Kevin Cusnir "Lirioth"
GitHub: @Lirioth
Repository: https://github.com/Lirioth/Fullstack2026
Course: Fullstack Bootcamp 2026
Python Version: 3.8+
Last Updated: October 18, 2025
"""

# 🎉 Daily Challenge GOLD : Happy birthday (beginner)

from datetime import date, datetime
import calendar

def print_cake(c):
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
    top = "       ___" + ("i" * c) + "___"
    print(top)
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

def main():
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

    candles = age % 10  # If age ends with 0, this will be 0 🎂

    if calendar.isleap(bday.year):
        print_cake(candles)
        print_cake(candles)
    else:
        print_cake(candles)


if __name__ == "__main__":
    main()
