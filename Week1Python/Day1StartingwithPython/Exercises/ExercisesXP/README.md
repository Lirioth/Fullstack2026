# 🏋️ Exercises XP
A small collection of Python exercises.

## 📋 What this script covers

1) **👋 Hello World (strings + newlines)**  
   Prints "Hello world" four times, using `\n` for new lines.

2) **🧮 Some Math (operators & precedence)**  
   Calculates `(99**3) * 8` (power then multiply).

3) **❓ What is the output? (comparisons & types)**  
   - `5 < 3` → `False`  
   - `3 == 3` → `True`  
   - `3 == "3"` → `False` (different types)  
   - `"3" > 3` → **⚠️ TypeError** in Python (you cannot compare `str` and `int`)  
   - `"Hello" == "hello"` → `False` (string comparison is case-sensitive)

4) **💻 Your computer brand (variables + string concatenation)**  
   Uses `computer_brand = "ASUS"` and prints a sentence.

5) **👤 Your information (variables + casting)**  
   Builds a sentence with `name`, `age`, `shoe_size`. Uses `str(...)` to cast numbers when concatenating.

6) **🔀 A & B (conditionals)**  
   If `a > b`, prints `"Hello World"`.

7) **🔢 Odd or Even (input + modulo)**  
   Asks for a number and prints `Even` if `n % 2 == 0`, otherwise `Odd`.

8) **🤝 What's your name? (input + normalization)**  
   Compares the user’s input (lowercased and stripped) to `my_name`. If equal, prints a friendly message.

9) **🎢 Tall enough to ride? (input + numeric compare)**  
   Asks for height in cm and prints if you’re tall enough.  
   > ⚠️ Note: This code uses `height > 145`. If you want `145` to count as tall enough, change to `>=`.

---

## 🚀 How to run

### Option A — 🖱️ Double click (if `.py` is associated to Python)
- Save the script as `exercisesxp.py`
- Double click to run (your OS may open a console window).

### Option B — 💻 Terminal
```bash
# macOS / Linux
python3 exercisesxp.py

# Windows
python exercisesxp.py
# or
py exercisesxp.py
```

You will be prompted for input in **📝 Exercises 7–9**.

---

## 📸 Example session (short)

```
Hello world
Hello world
Hello world
Hello world
768032
False
True
False
TypeError
False
I have a ASUS computer.
My name is Kevin, I'm 31 years old and my shoe size is 40.
Hello World
Enter a number: 4
Even
What is your name? Kevin
Hey, we have the same name! :)
Enter your height in cm: 150
You are tall enough to ride.
```

> 💡 Your inputs may differ; this is only a quick sample.

---

## 🎨 Customization tips (optional)

- Change `computer_brand`, `name`, `age`, `shoe_size` to your values.  
- Make Exercise 6 dynamic by asking the user for `a` and `b` with `input()` and `int(...)`.  
- Exercise 8: use `f-strings` to format:  
  ```python
  print(f"Nice to meet you, {user_name}!")
  ```
- Exercise 9: handle non-integer input with a `try/except ValueError` around `int(...)`.

---

## 📁 Files

- `exercisesxp.py` — the script
- `README.md` — this file
