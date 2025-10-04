# 🧩 Challenges #2 — Loops • Conditionals • Functions (Python) ✨

This mini‑package delivers:
- Clean, **commented code** for all requested patterns (Exercise 1).  
- A clear **analysis** of the given program (Exercise 2) with an annotated version, a step‑by‑step trace (values of `i`, `j`, `minimum`, and the list after swaps), and the **final output**.  
- A friendly README with emojis. ✅

## 📂 Structure
```
challenges2_project/
├─ src/
│  ├─ patterns.py   # Exercise 1 — draw three patterns using for-loops
│  └─ ex2_analysis.py  # Exercise 2 — annotated code + step-by-step trace
└─ main.py          # Demo runner
```

## 🚀 Run
```bash
python3 main.py
```
You’ll see:
1) The **three patterns** printed exactly as shown.  
2) The **annotated code** for Exercise 2.  
3) A **trace log** with `i`, `j`, `minimum`, list snapshots, and the **final sorted list**.

---

## 🧠 Exercise 1 — Patterns
We render the following shapes with `for` loops (spaces are meaningful):

**Pattern A**
```
  *
 ***
*****
```

**Pattern B**
```
    *
   **
  ***
 ****
*****
```

**Pattern C**
```
*
**
***
****
*****
*****
 ****
  ***
   **
    *
```

---

## 🔍 Exercise 2 — Program Analysis (Selection‑like Sort)
The given code performs an **in‑place ascending sort** using a selection‑sort‑like method that **swaps immediately** whenever a new smaller element is found in the inner loop (this can lead to multiple swaps per outer iteration, but the smallest element still ends up at position `i`).  
We include:
- An **annotated** version with comments on each line.
- A **trace** printing changing values of `i`, `j`, `minimum`, and the list after each swap.
- The **final output** list.

Have fun — and tweak inputs to explore behavior! ✨🐍
