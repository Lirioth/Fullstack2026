"""Module: exercisesxp
Purpose: Day 4 XP function practice helpers for demonstrations and weather advice.
Author: Kevin Cusnir 'Lirioth'
Created: 2025-10-18
Last Updated: 2025-10-19

Overview:
    - Basic definition and calling patterns
    - Default parameters and string formatting
    - Random number utilities for games and weather
    - List mutation helpers for magician names
"""

from __future__ import annotations

import random

# 🌡️ Temperature thresholds for weather advice
TEMP_FREEZING = 0  # Below this: freezing
TEMP_CHILLY = 16   # 0-16: chilly
TEMP_NICE = 24     # 16-24: nice weather
TEMP_WARM = 33     # 24-33: warm
TEMP_MIN = -10     # Minimum temperature
TEMP_MAX = 40      # Maximum temperature


# Exercise 1 🎯
def display_message() -> None:
    """Print the short reminder used to kick off the warm-up."""
    print("I am learning about functions in Python.")

# Exercise 2 🎯
def favorite_book(title: str) -> None:
    """Display a formatted message containing the reader's favorite book.

    Args:
        title: Book title to highlight in the output sentence.
    """
    print(f"One of my favorite books is {title}.")

# Exercise 3 🎯
def describe_city(city: str, country: str = "Unknown") -> None:
    """Print the relationship between a city and its host country.

    Args:
        city: City name to feature in the message.
        country: Optional country name; defaults to "Unknown".
    """
    print(f"{city} is in {country}.")

# Exercise 4 🎯
def compare_number(n: int) -> None:
    """Compare the supplied number with a random value between 1 and 100.

    Args:
        n: Player-selected number to check against the random draw.
    """
    r = random.randint(1, 100)
    if n == r:
        print("Success!")
    else:
        print(f"Fail! Your number: {n}, Random number: {r}")

# Exercise 5 🎯
def make_shirt(size: str = "large", text: str = "I love Python") -> None:
    """Summarize a shirt order using the requested size and slogan.

    Args:
        size: Requested shirt size, such as "small", "medium", or "large".
        text: Message to print on the shirt front.
    """
    print(f"The size of the shirt is {size} and the text is {text}.")

# Exercise 6 🎯
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names: list[str]) -> None:
    """Display each magician's name."""
    for n in names:
        print(n)

def make_great(names: list[str]) -> None:
    """
    Modify list in-place by adding 'the Great' to each name.
    
    Note: This function mutates the input list. For a functional approach
    (no side effects), use: return [name + " the Great" for name in names]
    """
    for i in range(len(names)):
        # ✅ Append the honorific while keeping existing order stable.
        names[i] = names[i] + " the Great"

# Exercise 7 🎯
def get_random_temp(min_temp: int = TEMP_MIN, max_temp: int = TEMP_MAX) -> int:
    """
    Generate random temperature in Celsius.
    
    Args:
        min_temp: Minimum temperature (default: -10)
        max_temp: Maximum temperature (default: 40)
        
    Returns:
        Random integer temperature
    """
    return random.randint(min_temp, max_temp)


def get_temp_advice(temp: int) -> str:
    """
    Get appropriate advice message for given temperature.
    
    Args:
        temp: Temperature in Celsius
        
    Returns:
        Advice string with emoji
    """
    if temp < TEMP_FREEZING:
        return "🥶 Brrr, that's freezing! Wear some extra layers today."
    elif temp < TEMP_CHILLY:
        return "🧥 Quite chilly! Don't forget your coat."
    elif temp < TEMP_NICE:
        return "😊 Nice weather."
    elif temp < TEMP_WARM:
        return "☀️ A bit warm, stay hydrated."
    else:
        return "🔥 It's really hot! Stay cool."


def report_weather() -> None:
    """Display current random temperature with appropriate advice."""
    temp = get_random_temp()
    advice = get_temp_advice(temp)
    print(f"🌡️ The temperature right now is {temp} degrees Celsius.")
    print(advice)


def main() -> None:
    """Sequence all exercise demonstrations. ✨"""
    display_message()
    favorite_book("Alice in Wonderland")
    describe_city("Reykjavik", "Iceland")
    describe_city("Paris")
    compare_number(50)
    make_shirt()                      # Large + default text 😊
    make_shirt("medium")              # Medium + default text 😊
    make_shirt("small", "Custom message")
    make_shirt(size="small", text="Hello!")  # Keyword args 😊
    magicians = magician_names.copy()
    make_great(magicians)
    show_magicians(magicians)
    report_weather()


if __name__ == "__main__":
    main()
