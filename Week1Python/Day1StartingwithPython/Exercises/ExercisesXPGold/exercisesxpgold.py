"""
🥈 Day 1 - Exercises XP Gold
============================
Enhanced practice with:
1. String multiplication techniques
2. Month-to-season mapping with membership testing

Author: Week1Python Course
Python Version: 3.8+
"""

# 🌸 Season mappings
SPRING_MONTHS = (3, 4, 5)
SUMMER_MONTHS = (6, 7, 8)
AUTUMN_MONTHS = (9, 10, 11)
WINTER_MONTHS = (12, 1, 2)


def exercise_1_hello_world() -> None:
    """Print Hello World and I love Python using string multiplication."""
    print("Hello world\n" * 4 + "I love python\n" * 3 + "I love python")


def get_valid_month() -> int:
    """Get valid month input (1-12) from user with validation."""
    while True:
        try:
            month = int(input("Enter month (1-12): "))
            if 1 <= month <= 12:
                return month
            print("⚠️ Month must be between 1 and 12")
        except ValueError:
            print("⚠️ Please enter a valid number")


def get_season(month: int) -> str:
    """
    Return season name for given month number.
    
    Args:
        month: Month number (1-12)
        
    Returns:
        Season name string with emoji
        
    Example:
        >>> get_season(4)
        'Spring 🌸'
    """
    if month in SPRING_MONTHS:
        return "Spring 🌸"
    elif month in SUMMER_MONTHS:
        return "Summer ☀️"
    elif month in AUTUMN_MONTHS:
        return "Autumn 🍂"
    else:  # WINTER_MONTHS
        return "Winter ❄️"


def exercise_2_season() -> None:
    """Interactive season finder based on month with input validation."""
    month = get_valid_month()
    season = get_season(month)
    print(season)


def main() -> None:
    """Run all Gold exercises in sequence."""
    print("🥈 Exercise 1: Hello World Variations")
    exercise_1_hello_world()
    print("\n🥈 Exercise 2: Season Finder")
    exercise_2_season()


if __name__ == "__main__":
    main()
