import random


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
def get_random_temp():
    return random.randint(-10, 40)
def report_weather() -> None:
    t = get_random_temp()
    print(f"The temperature right now is {t} degrees Celsius.")
    if t < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif t < 16:
        print("Quite chilly! Don't forget your coat.")
    elif t < 24:
        print("Nice weather.")
    elif t < 33:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")


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
