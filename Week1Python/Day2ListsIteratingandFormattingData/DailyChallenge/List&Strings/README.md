# Exercises XP — Sequence / List / Set / Tuple (Beginner)

A single Python script with small tasks about **sets, tuples, lists, loops, and input**.
Kept **very simple** and **beginner‑friendly**.

---

## ✅ What’s inside (by exercise)

### 1) Favorite Numbers (sets)
- Start with `my_fav_numbers = {7, 13, 27}`.
- Add a number (`42`), add a temp `last_added = 99`, then remove that last one with `.discard(last_added)`.
- Combine with a friend’s set using `.union(...)` → `our_fav_numbers`.
- **Note:** sets are **unordered** and store **unique** values.

### 2) Tuple (immutability)
- `t = (1, 2, 3)` then `t = t + (4, 5)`.
- Tuples **cannot** be changed in place; you create a **new** tuple when “adding”.

### 3) List manipulation
- Start: `["Banana", "Apples", "Oranges", "Blueberries"]`.
- Remove `"Banana"` and `"Blueberries"`, add `"Kiwi"`, insert `"Apples"` at index `0`.
- Count apples with `.count("Apples")`, then `.clear()` the list.
- **Note:** `.remove(x)` deletes the **first** match. Lists keep **order**.

### 4) Floats
- Build a sequence from **1.5** to **5** stepping by **0.5**.
- If a value is a whole number (e.g. `2.0`), cast it to `int` so it prints as `2` instead of `2.0`.
- Result: `[1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]`

### 5) For loop
- Print **1..20**.
- Then, with `enumerate(range(1, 21))`, print numbers where the **index** is even (`0,2,4,...`).  
  👉 Because the first index is `0`, this prints the **odd** numbers: `1, 3, 5, ..., 19`.

### 6) While loop — ask for your name until it matches
- Loops until the input equals `"Kevin"` (case‑insensitive, trims spaces).

### 7) Favorite Fruits
- Ask for favorite fruits in **one line** (space‑separated), then ask for **one fruit** and check membership.
- **Note:** this check is **case‑sensitive** as written (e.g., `"apple"` vs `"Apple"`).

### 8) Pizza Toppings
- Keep asking toppings until the user types `quit`. Base price **$10** + **$2.5** per topping.
- Prints the toppings list and the final price with 2 decimals.

### 9) Cinemax Tickets
- Collect ages until `done`. Prices: `<3 → $0`, `<=12 → $10`, `>12 → $15`.
- Bonus: collect **restricted** movie ages `16–21` into a list.

### 10) Sandwich Orders
- Remove all `"Pastrami"` (sold out!).
- Make the remaining sandwiches and move them to `finished_sandwiches`.

---

## ▶️ How to run
### Option A — Double click (if `.py` is associated with Python)
- Save as `exercises_xp_sequences.py` and double click.

### Option B — Terminal / Command Prompt
```bash
# macOS / Linux
python3 exercises_xp_sequences.py

# Windows
python exercises_xp_sequences.py
# or
py exercises_xp_sequences.py
```

You’ll be prompted for input in several exercises (6–9).

---

## 🧪 Mini example (trimmed)
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

*(Your exact set order may differ, because sets are unordered.)*

---

## 🌟 Optional improvements (practice ideas)
- **Input validation**: for numbers use `try/except ValueError` and re‑ask on bad input.
- **Case‑insensitive fruits**: compare `.lower()` on both sides.
- **Unique toppings**: use a `set` to avoid duplicates.
- **Constants**: define `BASE_PRICE = 10` and `TOPPING_PRICE = 2.5` at the top.
- **Functions**: wrap each exercise in a small function to organize the file.

---

## Files
- `exercises_xp_sequences.py` — the script
- `README.md` — this file
