# 🏋️ ## 📋 What's inside (quick tour)xercises XP — Sequence / List / Set / Tuple 

A small, single-file collection that practices **sets, tuples, lists, loops, and user input**.

---

## ✅ What’s inside (quick tour)

### 1) 💖 Favorite Numbers — *sets*
- Start with a set, add items, remove the temporary one with `.discard(...)`.
- Merge with friend’s favorites using `.union(...)` → `our_fav_numbers`.
- *🔍 Reminder:* sets are **unordered** and only keep **unique** elements.

### 2) 📦 Tuple — *immutability*
- `t = (1, 2, 3)` then `t = t + (4, 5)`.
- Tuples **cannot** be changed in place; concatenation returns a **new** tuple.

### 3) 📝 List Manipulation
- Remove items, append `"Kiwi"`, insert `"Apples"` at index `0`, count `Apples`, then `.clear()`.
- `.remove(x)` deletes the **first** match; lists keep **order**.

### 4) 🔢 Floats
- Build values from **1.5** to **5** stepping by **0.5**.
- If a step is whole (like `2.0`), cast to `int` so it prints `2` instead of `2.0`.
- Result: `[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]`.

### 5) 🔄 For Loop
- Print numbers **1..20**.
- Then, with `enumerate(range(1, 21))`, print numbers where the **index is even** (`0,2,4,...`).  
  👉 Because `0` is the first index, this ends up printing the **odd numbers** `1,3,5,...,19`.

### 6) While Loop — Ask name until it matches
- Continues asking until input equals `"Kevin"` (case-insensitive, trims spaces).

### 7) Favorite Fruits
- Collect favorites as a **space-separated** string, split to a list, then check if a single fruit is in the list.
- Note: membership is **case-sensitive** as written.

### 8) Pizza Toppings
- Keep adding toppings until the user types `quit`.
- Price = **$10** base + **$2.5** per topping.

### 9) Cinemax Tickets
- Gather ages until `done`.
- Price rules: `<3 → $0`, `<=12 → $10`, `>12 → $15`.
- Bonus: build a list of **restricted** ages **16–21**.

### 10) Sandwich Orders
- Remove all `"Pastrami"` (sold out!), then prepare the rest FIFO, collecting them in `finished_sandwiches`.

---

## ▶️ How to run
### Option A — Double-click (if `.py` is associated with Python)
- Save as `exercises_xp_sequences.py` and double-click.

### Option B — Terminal / Command Prompt
```bash
# macOS / Linux
python3 exercises_xp_sequences.py

# Windows
python exercises_xp_sequences.py
# or
py exercises_xp_sequences.py
```
You’ll be prompted for input in several parts (Exercises **6–9**).

---

## 🧪 Tiny sample (trimmed)
```
our_fav_numbers: {1, 3, 7, 13, 27, 42}
tuple: (1, 2, 3, 4, 5)
apples count: 2
final basket: []
sequence: [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
...
Sorry, no Pastrami today.
I made your Tuna sandwich.
I made your Avocado sandwich.
I made your Egg sandwich.
I made your Chicken sandwich.
Finished sandwiches: ['Tuna', 'Avocado', 'Egg', 'Chicken']
```
*(Set order may vary.)*

---

## 🌟 Optional improvements
- **Input validation** with `try/except` for numbers; re-ask on invalid input.
- **Case-insensitive** comparisons for fruits: compare both sides with `.lower()`.
- **Avoid duplicate toppings**: switch `toppings` to a `set`.
- **Use constants**: `BASE_PRICE = 10`, `TOPPING_PRICE = 2.5`.
- **Refactor** into small functions per exercise for cleaner structure.

---

## Files
- `exercisesxp.py` — your script
- `README.md` — this file
