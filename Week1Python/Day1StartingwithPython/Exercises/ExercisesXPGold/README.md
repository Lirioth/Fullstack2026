# 🥈 Exercises XP Gold

A tiny pair of beginner-friendly exercises.

## 1️⃣ Exercise 1: Hello World — I love Python (one line)
**🎯 Goal:** print multiple lines using **string multiplication** and `\n` newlines in a single statement.

What happens:
- `"Hello world\n"*4` → repeats `Hello world` 4 times, each with a newline.
- `"I love python\n"*3 + "I love python"` → prints the sentence 3 times with newlines, then once more without a trailing `\n` (so the output ends cleanly).

> 💡 Tip: This avoids writing many `print(...)` calls. Great for learning how strings combine.

## 2️⃣ Exercise 2: What is the Season?
**🎯 Goal:** read a **month number** (1–12) and print the **season**.

How it works (simple membership checks):
```python
if m in (3, 4, 5):      # 🌸 Spring
elif m in (6, 7, 8):    # ☀️ Summer
elif m in (9, 10, 11):  # 🍂 Autumn
elif m in (12, 1, 2):   # ❄️ Winter
else:                   # Anything not 1..12
    print("Invalid month")
```

### 📸 Examples
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
- Save as `exercisesxpgold.py` and double click.

### Option B — Terminal / Command Prompt
```bash
# macOS / Linux
python3 exercisesxpgold.py

# Windows
python exercisesxpgold.py
# or
py exercisesxpgold.py
```

## Files
- `exercisesxpgold.py` — the script.
- `README.md` — this file.
