# Daily Challenge — Letter Index Dictionary & Affordable Items (Dictionaries)

Two small problems written in a clean, readable way with tiny comments.

> Run with **Python 3.10+**. No extra packages needed.

---

## How to run

```bash
python dictionaries.py
```
Run the provided `dictionaries.py` script. The CLI wrapper now lives behind `if __name__ == "__main__"` so importing the helpers leaves your code quiet.

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
2. Pass it to `letter_indices(word)` which builds the dictionary using `enumerate`.
3. Print the dictionary returned by the helper.

**Helper function:**
```python
from dictionaries import letter_indices

letter_indices("mississippi")
# -> {'m': [0], 'i': [1, 4, 7, 10], 's': [2, 3, 5, 6], 'p': [8, 9]}
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

affordable = []
affordable.sort()
**How it works (simple steps):**
1. Call `affordable_items(items, wallet)` to get a sorted list of names that fit the budget.
2. The helper handles currency parsing, comparisons, and empty results.
3. Print the resulting list or `"Nothing"` if it’s empty.

**Helper function:**
```python
from dictionaries import affordable_items

items = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
affordable_items(items, "$300")
# -> ['Bread', 'Fertilizer', 'Water']
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
- The helpers are already pure functions—drop them straight into unit tests or other projects.
- If you later support other formats (like `"€1.234"`), extend the parser carefully.

---

## License
MIT — free to use, copy, and modify.
