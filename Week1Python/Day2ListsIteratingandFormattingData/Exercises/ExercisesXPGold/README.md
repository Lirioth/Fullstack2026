# 🥈 Exercises XP Gold

A compact set of nine small exercises. 

---

## 📋 What's inside (quick tour)

### 1️⃣ Concatenate lists (without `+`)
- Make a **copy** with `list(a)` and **extend** it with `c.extend(b)`.
- This avoids using `a + b` and shows how `extend` mutates the list (shallow copy here, which is fine for numbers).

### 2️⃣ Range of numbers (multiples of 5 and 7)
- Loops from **1500 to 2500 inclusive** and prints numbers divisible by **both** 5 and 7 (i.e., by **35**).

### 3️⃣ Check the index
- Given a list of names (with duplicates), asks the user for a name.
- Prints the **first index** using `.index(...)` if found, else prints "name not found".

### 4️⃣ Greatest Number
- Reads three integers and prints the maximum using `max(x, y, z)`.

### 5️⃣ The Alphabet (vowel or consonant)
- Iterates the alphabet; if the letter is in `aeiou`, prints "vowel", otherwise "consonant".
- (Here, **`y`** is treated as a consonant; you can change that if you wish.)

### 6️⃣ Words and letters
- Collects **7 words** and then asks for **1 character** (only first char is used).
- For each word, prints the **index** of the first occurrence (`.find`), or a "not found" message.

### 7) Min, Max, Sum
- Builds a list of `1..1_000_000` and prints its min, max, and sum.
- **Note:** Creating a full list uses memory; a leaner option is to use `range` directly:
  - `min(range(1, 1_000_001))`, `max(range(1, 1_000_001))`, and `sum(range(1, 1_000_001))`.

### 8) List and Tuple
- Reads comma‑separated input, returns **list** and **tuple** of the values (as **strings**).
- Optional: cast to `int` with `[int(x) for x in data.split(",")]` if you want numbers.

### 9) Random number guessing
- Guess a number **1–9** or type **q** to quit.
- Counts wins/losses and prints the final score. Handles invalid or out‑of‑range input.

---

## ▶️ How to run

### Option A — Double click (if `.py` is associated to Python on your OS)
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

You’ll be prompted for input in several exercises (3–4, 6, 8–9).

---

## 🧪 Tiny sample (trimmed)
```
exercise1: [1, 2, 3, 4, 5, 6]
1505
1540
1575
...
index: 0
The greatest number is: 42
a - vowel
b - consonant
...
['12', '7', '33']
('12', '7', '33')
Guess 1-9 (or 'q' to quit): 5
better luck next time (number was 9 )
Guess 1-9 (or 'q' to quit): q
games won: 0 games lost: 1
```

---

## 🌟 Optional improvements (nice practice)
- **Input validation** for integer reads (wrap in `try/except ValueError`).
- **Normalize case** for the name search and for the single letter search (use `.lower()`).
- **Reduce memory** in Exercise 7 by using `range` directly instead of a full list.
- **Stats** in the guessing game: show **accuracy** and **streak**.
- **Type casting** in Exercise 8: convert the comma‑separated values to numbers if needed.

---

## Files
- `exercisesxpgold.py` — your script
- `README.md` — this file
