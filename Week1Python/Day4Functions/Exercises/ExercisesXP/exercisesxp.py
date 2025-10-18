"""
⚙️ Day 4 - Exercises XP
=======================
Function practice covering:
- Basic definition and calling
- Default parameters
- Random number generation
- List manipulation in-place
- Multi-function systems with composition

Author: Week1Python Course
Python Version: 3.8+
"""

import random

# 🌡️ Temperature thresholds for weather advice
TEMP_FREEZING = 0  # Below this: freezing
TEMP_CHILLY = 16   # 0-16: chilly
TEMP_NICE = 24     # 16-24: nice weather
TEMP_WARM = 33     # 24-33: warm
TEMP_MIN = -10     # Minimum temperature
TEMP_MAX = 40      # Maximum temperature


# Exercise 1 🎯
def display_message():
    print("I am learning about functions in Python.")

# Exercise 2 🎯
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# Exercise 3 🎯
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Exercise 4 🎯
def compare_number(n):
    r = random.randint(1, 100)
    if n == r:
        print("Success!")
    else:
        print(f"Fail! Your number: {n}, Random number: {r}")

# Exercise 5 🎯
def make_shirt(size="large", text="I love Python"):
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
