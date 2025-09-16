# Exercises XP Gold

A tiny pair of beginner-friendly exercises.

## ✅ Exercise 1: Hello World — I love Python (one line)
**Goal:** print multiple lines using **string multiplication** and `\n` newlines in a single statement.

What happens:
- `"Hello world\n"*4` → repeats `Hello world` 4 times, each with a newline.
- `"I love python\n"*3 + "I love python"` → prints the sentence 3 times with newlines, then once more without a trailing `\n` (so the output ends cleanly).

> Tip: This avoids writing many `print(...)` calls. Great for learning how strings combine.

## ✅ Exercise 2: What is the Season?
**Goal:** read a **month number** (1–12) and print the **season**.

How it works (simple membership checks):
```python
if m in (3, 4, 5):      # Spring
elif m in (6, 7, 8):    # Summer
elif m in (9, 10, 11):  # Autumn
elif m in (12, 1, 2):   # Winter
else:                   # Anything not 1..12
    print("Invalid month")
```

### Examples
```
Enter month (1-12): 4
Spring

Enter month (1-12): 8
Summer

Enter month (1-12): 12
Winter

Enter month (1-12): 0
Invalid month
```

## ▶️ How to run
### Option A — Double click (if `.py` files run with Python on your OS)
- Save as `exercises_xp_gold.py` and double click.

### Option B — Terminal / Command Prompt
```bash
# macOS / Linux
python3 exercises_xp_gold.py

# Windows
python exercises_xp_gold.py
# or
py exercises_xp_gold.py
```

## 🌟 Optional improvements (nice practice)
- **Validate input**: wrap `int(input(...))` in `try/except ValueError` to handle non-numbers.
- **Loop until valid month**: keep asking while `m` not in `1..12`.
- **Use a dict** mapping instead of `if/elif` (another style):
  ```python
  seasons = {
      "Spring": (3,4,5),
      "Summer": (6,7,8),
      "Autumn": (9,10,11),
      "Winter": (12,1,2)
  }
  ```
- **Localization**: print season names in Spanish/Hebrew if you want to practice i18n.
- **Unit tests**: write a tiny `def month_to_season(m): ...` and test it.

## Files
- `exercises_xp_gold.py` — the script.
- `README.md` — this file.
