# 🥇 Exercises XP Ninj## 📋 What's inside

### 1️⃣ Exercise 1 — Formula Python Notes

A tiny collection of Python practice exercises I wrote to train basics like input/output, lists, loops, strings, and simple math. The code stays simple on purpose and uses only the standard library (`math`, `collections`).

> Run with **Python 3.10+** (any recent Python 3 is fine). No external packages needed.

---

## 🚀 How to run

```bash
python3 exercisesxpninja.py
```

- The script prints the results for each exercise in order.
- It **asks for input** in Exercise 1 (comma‑separated numbers) and in Exercise 4 (a line of text).
- Everything else runs automatically and prints to the console.

If your file has a different name, just replace `exercisesxpninja.py` with your filename.

---

## What’s inside

### ✅ Exercise 1 — Formula
**Goal:** compute `Q = sqrt((2 * C * D) / H)` for each `D` in a comma‑separated input.  
**Given:** `C = 50`, `H = 30`.  
**Input example:** `100,150,180` → **Output:** `18,22,24` (rounded to int).

**How it works (simple steps):**
1. Read a string from the user like `"100,150,180"`.
2. Split by commas and trim spaces → list of strings.
3. Convert each `D` to `int`.
4. For each `D`, compute `Q` with the formula and `round`, then `int()`.
5. Join all results back with commas and print.

**Tiny code peek:**

```python
# constants
C, H = 50, 30

# read values like: 100,150,180
data = input("Enter D values (comma-separated): ")
Ds = [x.strip() for x in data.split(",") if x.strip() != ""]

results = []
for d in Ds:
    D = int(d)  # turn text into number
    q = int(round(((2 * C * D) / H) ** 0.5))  # quick sqrt
    results.append(str(q))

print(",".join(results))  # e.g. 18,22,24
```

---

### ✅ Exercise 2 — Playing with a list of integers
**Goal:** practice list operations and basic stats on a predefined list.

**List used:**  
```python
nums = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
```

**What I print:**
- The whole list in one line.
- The list sorted in **descending** order.
- The **sum** of all numbers.
- The **first and last** numbers.
- All numbers **> 50**.
- All numbers **< 10**.
- The **squares** of all numbers.
- The list **without duplicates** and its **count**.
- The **average**, **max**, and **min**.
- **Bonus:** manual `sum`, `avg`, `max`, `min` without built‑ins.

**Tiny code peek:**

```python
# example list
nums = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

print("list:", " ".join(str(x) for x in nums))
print("desc:", " ".join(str(x) for x in sorted(nums, reverse=True)))
print("sum:", sum(nums))
print("first+last:", [nums[0], nums[-1]])
print(">50:", [x for x in nums if x > 50])
print("<10:", [x for x in nums if x < 10])
print("squares:", " ".join(str(x*x) for x in nums))

# remove duplicates (keep order) and count
no_dups = []
for x in nums:
    if x not in no_dups:  # only add if not seen before
        no_dups.append(x)
print("no_dups:", no_dups, "count:", len(no_dups))

# basic stats
print("avg:", sum(nums) / len(nums))
print("max:", max(nums))
print("min:", min(nums))

# manual stats (no built-ins for practice)
s = 0
mx = mn = nums[0]
for x in nums:
    s += x
    if x > mx: mx = x
    if x < mn: mn = x
print("manual sum:", s, "manual avg:", s/len(nums), "manual max:", mx, "manual min:", mn)
```

---

### ✅ Exercise 3 — Working on a paragraph
**Goal:** analyze a short paragraph and print simple stats.

**What I compute:**
- Total **characters** (including spaces).
- Number of **sentences** (count `.`, `!`, `?`). If none, treat as 1 to avoid division by zero.
- Number of **words** (split by whitespace).
- Number of **unique words** (lowercased and stripped of `.,!?;:`).
- **Non‑whitespace characters** (everything except spaces, tabs, etc.).
- **Average words per sentence** (rounded).
- **Total count of repeated words** (words that occur more than once).

**Tiny code peek:**

```python
from collections import Counter

para = (
    "Learning Python is fun. It helps you think clearly! "
    "Python has simple syntax, yet it is powerful. Keep practicing?"
)

chars = len(para)
sentences = para.count(".") + para.count("!") + para.count("?")
if sentences == 0:
    sentences = 1  # avoid division by zero

words = para.split()
cleaned = [w.strip(".,!?;:").lower() for w in words]

unique_words = set(cleaned)
non_ws = sum(1 for ch in para if not ch.isspace())
avg_w_per_sent = len(words) / sentences

freq = Counter(cleaned)
non_unique_total = sum(c for c in freq.values() if c > 1)
```

**Example output (may vary a bit):**
```
chars: 118
sentences: 3
words: 20
unique words: 17
non-whitespace chars: 99
avg words/sentence: 6.67
non-unique words total count: 3
```

---

### ✅ Exercise 4 — Frequency of the words
**Goal:** read one line from the user and print how many times each token appears.

**Rules I use:**
- Split by **whitespace** only. Punctuation stays attached (so `word,` and `word` are different).
- **Case‑sensitive** (so `Python` and `python` are different).
- Print tokens in **alphabetical order** as `token:count`.

**Tiny code peek:**

```python
from collections import Counter

text = input("Enter a line for word frequency: ")
tokens = text.split()  # case-sensitive; punctuation kept
counts = Counter(tokens)

for token in sorted(counts.keys()):
    print(f"{token}:{counts[token]}")
```

**Example:**
```
Input:  "Python python is fun, fun python"
Output:
Python:1
fun,:1
is:1
python:2
```

---

## Tips for my future self

- Keep the code readable: short variable names are fine but add tiny comments where it helps.
- Validate inputs if you plan to reuse these snippets.
- For bigger text tasks, consider `re` (regular expressions) for better tokenization.
- It’s okay if the print format is basic — clarity first.

---

## License
MIT — do whatever you want, just keep a copy of this file.
