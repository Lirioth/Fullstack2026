# 🥉 Exercises XP — Lists, Sets, Tuples & Iteration

**Author:** Kevin Cusnir "Lirioth"  
**Course:** Fullstack Bootcamp 2026  
**Last Updated:** October 18, 2025

**Master Python collections through 10 comprehensive exercises covering sets, tuples, lists, loops, and interactive programs.**

## 📊 Quick Stats
- **⏰ Duration**: 60-90 minutes
- **🎯 Difficulty**: 🟢 Beginner
- **📝 Exercises**: 10
- **✅ Prerequisites**: Day 1 completion

## 🎯 Learning Objectives

By completing these exercises, you will:
- ✅ Master set operations for unique collections
- ✅ Understand tuple immutability and use cases
- ✅ Manipulate lists with various methods
- ✅ Build numeric sequences with conditionals
- ✅ Implement for and while loop patterns
- ✅ Process user input with validation
- ✅ Create practical calculators and pricing systems
- ✅ Handle order processing workflows

---

## 🗺️ Exercise Learning Map

Follow this progression to master Python collections:

```
📚 FOUNDATION (Exercises 1-4)
│
├─ 💖 Exercise 1: Sets → Unique collections & operations
│   └─ Learn: .add(), .discard(), .union()
│
├─ 📦 Exercise 2: Tuples → Immutable sequences
│   └─ Learn: Concatenation, immutability
│
├─ 📝 Exercise 3: Lists → Dynamic arrays
│   └─ Learn: .remove(), .append(), .insert(), .count(), .clear()
│
└─ 🔢 Exercise 4: Floats → Numeric sequences
    └─ Learn: .is_integer(), type checking

🔄 ITERATION (Exercises 5-6)
│
├─ Exercise 5: For Loops → Counted iteration
│   └─ Learn: range(), enumerate()
│
└─ Exercise 6: While Loops → Conditional iteration
    └─ Learn: Input validation, loop control

💼 APPLICATIONS (Exercises 7-10)
│
├─ 🍎 Exercise 7: Fruits → Membership testing
│   └─ Learn: .split(), 'in' operator
│
├─ 🍕 Exercise 8: Pizza → Price calculation
│   └─ Learn: Accumulator pattern, user loops
│
├─ 🎬 Exercise 9: Cinema → Age-based logic
│   └─ Learn: Conditional pricing, data collection
│
└─ 🥪 Exercise 10: Sandwiches → Order processing
    └─ Learn: List manipulation, FIFO processing
```

---

## ✅ What's inside (quick tour)

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
- Save as `exercisesxp.py` and double-click.

### Option B — Terminal / Command Prompt
```bash
# macOS / Linux
python3 exercisesxp.py

# Windows
python exercisesxp.py
# or
py exercisesxp.py
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

## 📁 Files
- `exercisesxp.py` — Complete implementation
- `README.md` — This documentation

---

## 🔧 Troubleshooting

### Common Issues & Solutions

**❌ Problem:** `ValueError: list.remove(x): x not in list`  
**✅ Solution:** Check if element exists before removing:
```python
if item in my_list:
    my_list.remove(item)
```

**❌ Problem:** Set order is unpredictable  
**✅ Solution:** Sets are unordered by design. Use lists if order matters.

**❌ Problem:** `TypeError: 'tuple' object does not support item assignment`  
**✅ Solution:** Tuples are immutable. Create a new tuple instead:
```python
t = (1, 2, 3)
t = t + (4, 5)  # Creates new tuple
```

**❌ Problem:** Pizza price calculation incorrect  
**✅ Solution:** Ensure base price + (topping count × topping price)

**❌ Problem:** Infinite while loop  
**✅ Solution:** Verify loop has proper exit condition and input validation

---

## 💡 Learning Tips

1. **Sets eliminate duplicates** - Perfect for finding unique values
2. **Tuples protect data** - Use for constants that shouldn't change
3. **enumerate() is powerful** - Get both index and value in loops
4. **Modular functions** - Break complex logic into helper functions
5. **Validate early** - Check user input before processing

---

## 👤 About the Author

**Kevin Cusnir "Lirioth"**  
- 🎓 Fullstack Developer Student  
- 💻 GitHub: [@Lirioth](https://github.com/Lirioth)  
- 📧 Repository: [Fullstack2026](https://github.com/Lirioth/Fullstack2026)

---

**Created with ❤️ for mastering Python collections**
