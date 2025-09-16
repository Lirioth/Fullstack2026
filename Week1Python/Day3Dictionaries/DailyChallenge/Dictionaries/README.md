# Daily Challenge — Letter Index Dictionary & Affordable Items (Python)

Two small problems written in a clean, readable way with tiny comments.

> Run with **Python 3.10+**. No extra packages needed.

---

## How to run

```bash
python3 main.py
```
Replace `main.py` with your filename if it’s different.

---

## Challenge 1 — Letter Index Dictionary

**Goal:** read a word and build a dictionary where each key is a character and each value is a list of positions (indexes) where that character appears.

**Example**
```
Input:  "mississippi"
Output: {'m': [0], 'i': [1, 4, 7, 10], 's': [2, 3, 5, 6], 'p': [8, 9]}
```

**How it works (simple steps):**
1. Read the string from the user.
2. Create an empty dict `d = {}`.
3. Loop over the characters using `enumerate` to get `(index, char)`.
4. If the char is not in the dict, create a new list with the current index.
5. Otherwise, append the current index to the existing list.
6. Print the dictionary.

**Tiny code peek:**
```python
word = input("Enter a word: ")
d = {}

for i, ch in enumerate(word):          # i = index, ch = character
    if ch not in d:                    # first time we see this character
        d[ch] = [i]                    # start a new list with this index
    else:
        d[ch].append(i)                # add another index
print(d)                               # show the result
```

**Notes:**
- Empty input prints `{}`.
- Time complexity: **O(n)** where `n` is the word length.
- The dictionary order follows insertion order in modern Python, which usually matches first sightings.

---

## Challenge 2 — Affordable Items

**Goal:** given a dictionary of items with string prices like `"$1,200"` and a wallet amount like `"$300"`, print a sorted list of item names you can afford. If none, print `"Nothing"`.

**Helper:**
```python
def to_int(s):
    return int(s.replace("$", "").replace(",", "").strip())
```
This removes the dollar sign and commas, then converts to `int`.

**How it works (simple steps):**
1. Define `to_int` to parse prices like `"$1,000"` into `1000`.
2. For each `(name, price)` in the dictionary:
   - Convert `price` and `wallet` to integers.
   - If `price <= wallet`, push the `name` to a list.
3. Sort the list alphabetically.
4. Print the list or `"Nothing"` if it’s empty.

**Tiny code peek (pattern used in the script):**
```python
affordable = []
for name, price in items_purchase.items():
    if to_int(price) <= to_int(wallet):  # compare ints, not strings
        affordable.append(name)
affordable.sort()
print(affordable if affordable else "Nothing")
```

**Examples**

Example 1
```python
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
# Output: ['Bread', 'Fertilizer', 'Water']
```

Example 2
```python
items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"
# Output: ['Apple', 'Bananas', 'Fan', 'Honey', 'Pan', 'Spoon']
```

Example 3
```python
items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"
# Output: "Nothing"
```

**Notes:**
- Works with any currency string formatted like `"$1,234"` (only `$` and `,` are stripped).
- If you want stricter validation, add checks for negative numbers or invalid strings.
- Time complexity: **O(n log n)** due to sorting; the scan itself is **O(n)**.

---

## Tips for my future self
- Keep outputs clear so they’re easy to compare against the expected results.
- Consider wrapping each challenge in a function and unit‑testing with sample cases.
- If you later support other formats (like `"€1.234"`), extend the parser carefully.

---

## License
MIT — free to use, copy, and modify.
