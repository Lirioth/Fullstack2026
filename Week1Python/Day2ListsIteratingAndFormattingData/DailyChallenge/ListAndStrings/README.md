# 🌟 Daily Challenge — Lists & Strings (Python)

A short practice file with two tiny problems: generating multiples and cleaning repeated letters. The code is kept simple with small comments.

> Run with **Python 3.10+** (any recent Python 3 works). No extra packages needed.

---

## How to run

```bash
python dailychallengelistandstrings.py
```
Run the command from the `ListAndStrings` folder. A small `_cli()` wrapper now collects input so importing the module elsewhere stays side-effect free.

The prompt sequence matches the original exercise: two numbers for Challenge 1 (base and length) and a single word for Challenge 2.

---

## Challenge 1 — Multiples of a Number

**Goal:** Read an integer `number` and a positive integer `length`, then print a list containing the first `length` multiples of `number`.

**Example 1**
```
Enter a number: 7
Enter length: 5
Output: [7, 14, 21, 28, 35]
```

**Example 2**
```
Enter a number: -3
Enter length: 4
Output: [-3, -6, -9, -12]
```

**How it works (step by step):**
1. Convert the two inputs into integers.
2. Call `multiples(number, length)` which returns the list of requested multiples.
3. Print the resulting list.

**Helper function:**
```python
from dailychallengelistandstrings import multiples

multiples(7, 5)
# -> [7, 14, 21, 28, 35]
```

**Notes:**
- If `length` is `0` or negative, the current script will produce `[]` or nothing useful. You can add a guard if you want to enforce `length > 0`.
- Works fine with negative `number`; the sign is kept in all multiples.
- Time complexity: **O(length)**; Space: **O(length)**.

---

## Challenge 2 — Remove Consecutive Duplicate Letters

**Goal:** Read a word and print a new string where **consecutive** duplicate letters are collapsed to a single letter.

**Example 1**
```
Enter a word: ppoollee
Output: pole
```

**Example 2**
```
Enter a word: bookkeeper
Output: bokeper
```

**Example 3**
```
Enter a word: AaAa
Output: AaAa   # case-sensitive: 'A' and 'a' are different
```

**How it works (step by step):**
1. Read the string from the user.
2. Pass it into `collapse_duplicates(word)` to obtain the cleaned version.
3. Print the return value.

**Helper function:**
```python
from dailychallengelistandstrings import collapse_duplicates

collapse_duplicates("ppoollee")
# -> "pole"
```

**Notes:**
- This collapses only **neighboring** duplicates. Non-consecutive repeats stay (e.g., `abca` -> `abca`).
- Works with spaces and punctuation as well (the check is character-by-character).
- Time complexity: **O(n)**; Space: up to **O(n)** in worst case.

---

## Quick tips for future me

- Keep the `multiples` and `collapse_duplicates` helpers pure so they stay easy to unit test.
- Add small guards for input validation if you want stricter behavior (e.g., ensure `length >= 1`).
- Replace the CLI with your own prompts by calling `_cli()` or wiring the helpers into a separate UI.

---

## License
MIT — free to use, copy, and modify.
