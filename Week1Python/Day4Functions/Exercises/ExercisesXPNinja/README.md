# 🥷 Exercises XP Ninja — Functions (Single-File Edition) ✨

Welcome! This package contains a **single Python file** with clean, commented solutions to the four function exercises, plus a tiny demo runner. Everything is **English-only** as requested ✅

## 📂 Files
- `xp_ninja_functions_single.py` — all solutions + comments + demo
- `README.md` — this guide with emojis

## 🚀 Run
```bash
python3 xp_ninja_functions_single.py
```
You’ll see demos for all tasks printed to the console.

---

## 🧑‍🤝‍🧑 Exercise 1 — `get_full_name()`
Builds a full name where `middle_name` is optional. Includes **smart capitalization** for hyphens and apostrophes (e.g., `o'connor-smith` → `O'Connor-Smith`).  
**Examples:**
```python
get_full_name(first_name="john", middle_name="hooker", last_name="lee")  # -> "John Hooker Lee"
get_full_name(first_name="bruce", last_name="lee")                       # -> "Bruce Lee"
```

---

## 📻 Exercise 2 — English ⇄ Morse
- Letters separated by **spaces**, words separated by **' / '**.
- Strict validation: unsupported characters raise `ValueError` so errors don’t hide. 🧯  
**Examples:**
```python
text_to_morse("SOS HELP 123")
# -> '... --- ... / .... . .-.. .--. / .---- ..--- ...--'

morse_to_text("... --- ... / .... . .-.. .--. / .---- ..--- ...--")
# -> 'SOS HELP 123'
```

---

## ⭐ Exercise 3 — `box_printer(*strings)`
Prints a star-framed rectangle with each string on its own line. Also **returns** the framed string for reuse or testing.  
**Example output:**
```
******************
* Hello          *
* World          *
* in             *
* reallylongword *
* a              *
* frame          *
******************
```

---

## 🧠 Exercise 4 — Insertion Sort
Implements **Insertion Sort**: in-place, stable, best **O(n)** when nearly sorted, average/worst **O(n²)**. Think “sorting playing cards in your hand.”

**Snippet:**
```python
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(arr)
print(arr)  # -> [17, 20, 26, 31, 44, 54, 55, 77, 93]
```

---

## ✅ Notes
- Functions are small and pure when possible for easy testing.
- Inputs are trimmed and validated where it matters.
- The demo lives under `if __name__ == "__main__":` for easy local runs.

## 🎯 Have fun!
Code boldly, refactor kindly, and enjoy the craft ✨🐍
