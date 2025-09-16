# Python Practice — Functions, Defaults & Simple Logic (Exercises XP)

A compact set of small function exercises: printing messages, default parameters, basic conditionals, list mutation, and random-based branches. Clear and simple with tiny comments.

> Run with **Python 3.10+** (any recent Python 3 works). Uses only the standard library (`random`).

---

## How to run

```bash
python3 exercisesxp.py
```
Replace `exercisesxp.py` with your filename if different.  
The script **runs each exercise once** in order and prints to the console.

---

## What’s inside

### ✅ Exercise 1 — `display_message()`
**Goal:** define a function and call it.  
**Idea:** keep side effects obvious with a single `print`.
```python
def display_message():
    print("I am learning about functions in Python.")
display_message()
```

---

### ✅ Exercise 2 — `favorite_book(title)`
**Goal:** pass an argument into a function and format a message.  
**Key:** f-strings keep it short and readable.
```python
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Alice in Wonderland")
```

---

### ✅ Exercise 3 — `describe_city(city, country="Unknown")`
**Goal:** practice **default parameters** and multiple calls.  
**Note:** calling without `country` uses `"Unknown"`.
```python
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")
describe_city("Reykjavik", "Iceland")
describe_city("Paris")  # uses the default
```

---

### ✅ Exercise 4 — `compare_number(n)`
**Goal:** generate a random number and compare with the user’s number.  
**Range:** 1..100 inclusive via `random.randint(1, 100)`.
```python
import random

def compare_number(n):
    r = random.randint(1, 100)
    if n == r:
        print("Success!")
    else:
        print(f"Fail! Your number: {n}, Random number: {r}")
compare_number(50)
```
**Tip:** for reproducible tests, set a seed first: `random.seed(0)`.

---

### ✅ Exercise 5 — `make_shirt(size="large", text="I love Python")`
**Goal:** combine **defaults**, **positional**, and **keyword args**.  
**Calls included:** default, one-arg override, and full override.
```python
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()                      # large + default text
make_shirt("medium")              # medium + default text
make_shirt("small", "Custom message")
make_shirt(size="small", text="Hello!")
```

---

### ✅ Exercise 6 — Magicians (mutate list + print)
**Goal:** work with lists and in‑place mutation.  
**Pattern:** modify a list, then display it.
```python
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for n in names:
        print(n)

def make_great(names):
    for i in range(len(names)):
        names[i] = names[i] + " the Great"

make_great(magician_names)  # mutate in place
show_magicians(magician_names)
```
**Note:** if you want to **keep the original** list, pass a copy: `make_great(magician_names[:])`.

---

### ✅ Exercise 7 — Random temperature + advice
**Goal:** return a random temperature and branch on ranges to print advice.
```python
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
```
**Ideas to extend:**
- Add seasons or city names to the message.
- Let the user input a temperature instead of using random.

---

## Tips for my future self
- Prefer small, single‑purpose functions.  
- Use keyword args when readability matters.  
- For deterministic tests around randomness, use `random.seed(...)` and fixed inputs.

---

## License
MIT — free to use, copy, and modify.
