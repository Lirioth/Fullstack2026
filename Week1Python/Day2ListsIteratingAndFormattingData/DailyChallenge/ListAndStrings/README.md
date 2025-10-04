# 🌟 Daily Challenge — Lists & Strings (Python)

A short practice file with two tiny problems: generating multiples and cleaning repeated letters. The code is kept simple with small comments.

> Run with **Python 3.10+** (any recent Python 3 works). No extra packages needed.

---

## How to run

```bash
python3 dailychallengelistandstrings.py
```
Run the command from the `ListAndStrings` folder so Python can find the script easily.

The program asks for input twice in Challenge 1 (a number, then a length) and once in Challenge 2 (a word).

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
1. Read `number` with `int(input(...))`.
2. Read `length` with `int(input(...))`.
3. Build a list using a simple `for` loop from `1` to `length` (inclusive) and append `number * i`.
4. Print the resulting list.

**Tiny code peek:**
```python
number = int(input("Enter a number: "))
length = int(input("Enter length: "))

multiples = []
for i in range(1, length + 1):  # go from 1..length
    multiples.append(number * i) # make each multiple
print(multiples)                 # show the list
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
2. If it is empty, print an empty string.
3. Otherwise, start the `result` with the first character.
4. Walk over the rest of the characters; only append a character if it is **different** from the last character already in `result`.
5. Print `result`.

**Tiny code peek:**
```python
word = input("Enter a word: ")

if word == "":
    print("")               # nothing to do
else:
    result = word[0]        # start with first char
    for ch in word[1:]:     # scan the rest
        if ch != result[-1]:# add only if not same as last
            result += ch
    print(result)
```

**Notes:**
- This collapses only **neighboring** duplicates. Non-consecutive repeats stay (e.g., `abca` -> `abca`).
- Works with spaces and punctuation as well (the check is character-by-character).
- Time complexity: **O(n)**; Space: up to **O(n)** in worst case.

---

## Quick tips for future me

- Keep `print()` outputs clear so it’s easy to compare expected vs actual.
- Add small guards for input validation if you want stricter behavior (e.g., ensure `length >= 1`).
- For unit tests later, you can wrap each challenge in a function and test with sample inputs.

---

## License
MIT — free to use, copy, and modify.
