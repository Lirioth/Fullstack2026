# Exercise 1
def display_message():
    print("I am learning about functions in Python.")
display_message()

# Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Alice in Wonderland")

# Exercise 3
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")
describe_city("Reykjavik", "Iceland")
describe_city("Paris")

# Exercise 4
import random
def compare_number(n):
    r = random.randint(1, 100)
    if n == r:
        print("Success!")
    else:
        print(f"Fail! Your number: {n}, Random number: {r}")
compare_number(50)

# Exercise 5
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")
make_shirt()                      # large + default text
make_shirt("medium")              # medium + default text
make_shirt("small", "Custom message")
make_shirt(size="small", text="Hello!")  # keyword args

# Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(names):
    for n in names:
        print(n)
def make_great(names):
    for i in range(len(names)):
        names[i] = names[i] + " the Great"
make_great(magician_names)
show_magicians(magician_names)

# Exercise 7
def get_random_temp():
    return random.randint(-10, 40)
def main():
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
main()
