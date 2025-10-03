# 🥇 Exercises XP Ninja

A single Python script with five quick exercises.

## 📋 What's inside

### 1️⃣ Exercise 1 — Use the terminal (short notes)
- Prints tiny notes about running Python from the terminal: `python3` and the **PATH** concept.
- **🛤️ PATH** = list of folders your OS searches for programs. If Python is in PATH, you can run `python3` anywhere.

### 2️⃣ Exercise 2 — Alias (short notes)
- On **🪟 Windows**, `py` is the official Python **launcher** (it chooses the right Python version).
- On **🐧 Linux/macOS**, you can create a shell alias like `alias py='python3'` in your shell config.

### 3️⃣ Exercise 3 — Outputs (predict and show)
The script prints and demonstrates:
- `3 <= 3 < 9` → **✅ True** (chained comparisons)
- `3 == 3 == 3` → **✅ True** (all equal)
- `bool(0)` → **❌ False** (`0` is falsy)
- `bool(5 == "5")` → **❌ False** (`5 == "5"` is `False` → `bool(False)` → `False`)
- `bool(4 == 4) == bool("4" == "4")` → **✅ True** (`True == True`)
- `bool(bool(None))` → **❌ False** (`None` is falsy, so `bool(None)` is `False`)

And some boolean ↔ integer tricks:
- `x = (1 == True)` → **✅ True**; `y = (1 == False)` → **❌ False**
- `a = True + 4` → **5️⃣** (because `True` behaves like `1`)
- `b = False + 10` → **🔟** (because `False` behaves like `0`)

### 4️⃣ Exercise 4 — How many characters?
- Uses a triple-quoted string with multiple lines and prints its length.
- With the provided text **exactly as written**, `len(my_text)` is **452** (newlines and spaces count!).

### Exercise 5 — Longest sentence **without 'A'**
- Repeatedly asks you to type a sentence **without the letter 'A'** (case-insensitive).
- Type `quit` to stop.
- If your sentence is valid and longer than the current record, it updates the record and prints the new length.

> Note: The check only looks for `'a'`/`'A'`. Accented letters like **á/à** are **not** blocked by default.

---

## ▶️ How to run
### Option A — Double click (if `.py` is associated with Python)
- Save as `exercisesxpninja.py` and double click to run.

### Option B — Terminal
```bash
# macOS / Linux
python3 exercisesxpninja.py

# Windows
python exercisesxpninja.py
# or
py exercisesxpninja.py
```

You will be prompted for input during **Exercise 5**.

---

## 🧪 Example (short, trimmed)
```
True
True
False
False
True
False
x is True
y is False
a: 5
b: 10
452
Type a sentence without the letter 'A' (or 'quit' to stop): hello there
Congrats, new record: 11
Type a sentence without the letter 'A' (or 'quit' to stop): a bad try
Contains 'A'. Try again.
Type a sentence without the letter 'A' (or 'quit' to stop): this is longer
Congrats, new record: 15
Type a sentence without the letter 'A' (or 'quit' to stop): quit
Best sentence: this is longer
```

---

## 🌟 Optional improvements (nice practice)
- **Robust input loop**: In Exercise 5, allow `QUIT`, `Quit`, etc. (already handled via `.lower()`).
- **Accents**: If you want to reject `á/à/â/ä`, normalize the string or use a regex that covers them.
- **Refactor**: Move the "no 'A'" check to a function like `def has_a(s): ...` and unit-test it.
- **Counting**: Show how many attempts the user made before quitting.
- **Save record**: Write the best sentence to a file for later sessions.

---

## Files
- `exercisesxpninja.py` — the script.
- `README.md` — this file.
