# 🏋️ Exercises XP
A small collection of Python exercises.

## � Quick Reference Table

| Exercise | Concept | Difficulty | Output Type | Key Learning |
|----------|---------|------------|-------------|--------------|
| 1 | Strings & newlines | 🟢 Easy | Text | `print()` and `\n` |
| 2 | Operators | 🟢 Easy | Number | Exponentiation `**` |
| 3 | Comparisons | 🟡 Medium | Booleans | Type comparisons |
| 4 | Variables | 🟢 Easy | Text | String concatenation |
| 5 | Type casting | 🟡 Medium | Text | `str()` conversion |
| 6 | Conditionals | 🟢 Easy | Text | `if` statements |
| 7 | Input + modulo | 🟡 Medium | Interactive | User input, `%` operator |
| 8 | String methods | 🟡 Medium | Interactive | `.lower()`, `.strip()` |
| 9 | Validation | 🟡 Medium | Interactive | Input validation |

---

## �📋 What this script covers

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

## 📋 **Exercise-by-Exercise Expected Outputs**

<details>
<summary>📋 Click to expand detailed outputs for each exercise</summary>

### Exercise 1 - Hello World
```
Hello world
Hello world
Hello world
Hello world
```

### Exercise 2 - Arithmetic
```
768032
```
(Result of `(99³) × 8`)

### Exercise 3 - Comparisons
```
False
True  
False
TypeError
False
```

### Exercise 4 - Computer Brand
```
I have a ASUS computer.
```

### Exercise 5 - Personal Info
```
My name is Kevin, I'm 31 years old and my shoe size is 40.
```

### Exercise 6 - Comparison
```
Hello World
```
(Only prints if `a > b`)

### Exercise 7 - Odd/Even
```
Enter a number: 7
Odd
```
or
```
Enter a number: 10
Even
```

### Exercise 8 - Name Match
```
What is your name? Alice
Nice to meet you, Alice!
```
or
```
What is your name? Kevin
Hey, we have the same name! :)
```

### Exercise 9 - Height Check
```
Enter your height in cm: 150
You are tall enough to ride.
```
or
```
Enter your height in cm: 140
You need to grow some more to ride.
```

</details>

---

---

## 🐛 Troubleshooting

### Common Issues & Solutions

**❌ Problem:** `TypeError: '>' not supported between instances of 'str' and 'int'`  
**✅ Solution:** Use `int(input("..."))` to convert user input to integer
```python
# Wrong:
age = input("Enter age: ")  # This is a string!
if age > 18:  # Error!

# Correct:
age = int(input("Enter age: "))  # Convert to integer
if age > 18:  # Works!
```

**❌ Problem:** `ValueError: invalid literal for int() with base 10: 'abc'`  
**✅ Solution:** User entered non-numeric text. Add validation:
```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("❌ Please enter a valid number")
```

**❌ Problem:** Height of 145cm not accepted  
**✅ Solution:** Code uses `>=` for inclusive comparison (145 is tall enough)

**❌ Problem:** Exercise 3 crashes on `"3" > 3`  
**✅ Solution:** The code includes `try/except` to catch this TypeError safely

**❌ Problem:** Name comparison doesn't work  
**✅ Solution:** Use `.lower()` and `.strip()` for case-insensitive comparison:
```python
if user_input.strip().lower() == my_name.lower():
    print("Same name!")
```

---

## 🎨 Customization tips (optional)

- Change `computer_brand`, `name`, `age`, `shoe_size` to your values.  
- Make Exercise 6 dynamic by asking the user for `a` and `b` with `input()` and `int(...)`.  
- Exercise 8: use `f-strings` to format:  
  ```python
  print(f"Nice to meet you, {user_name}!")
  ```
- Exercise 9: Already handles non-integer input with `try/except ValueError` around `int(...)`.

---

## 💡 Learning Tips

1. **Run each exercise separately** to understand what it does
2. **Try breaking the code** to see error messages
3. **Experiment with different inputs** to test edge cases
4. **Add your own print statements** to debug
5. **Read error messages carefully** - they tell you what's wrong!

---

## 📁 Files

- `exercisesxp.py` — the script
- `README.md` — this file
