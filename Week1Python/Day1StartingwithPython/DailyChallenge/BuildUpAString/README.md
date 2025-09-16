# Daily Challenge — Build up a string

A tiny Python script that checks an input string and prints info step by step.

## What it does (step by step)
1. **Ask for input**: the script reads a string from the user.
2. **Length check (exactly 10)**  
   - If length `< 10` ⇒ prints **"String not long enough."**  
   - If length `> 10` ⇒ prints **"String too long."**  
   - If length `== 10` ⇒ prints **"Perfect string"** and continues.
3. **Show first & last characters** of the string.
4. **Build the string gradually**: prints the string character by character, growing one char per line.
5. **Bonus**: creates a **jumbled (shuffled)** version of the string and prints it.

> Falsy/Truthiness are not used here. This is basic string + loops + indexing.
> The shuffle is random, so the jumbled output will be different each run.

## How to run
### Option A — Double click (if you have Python associated to `.py` files)
- Save the code as `build_up_string.py`
- Double click to run (on some systems it opens a console automatically).

### Option B — Terminal
```bash
# macOS / Linux
python3 build_up_string.py

# Windows (sometimes python or py)
python build_up_string.py
# or
py build_up_string.py
```

When prompted, type a string of **exactly 10 characters** and press Enter.

## Example runs
### 1) Too short
```
Enter a string (must be exactly 10 characters): hello
String not long enough.
```

### 2) Too long
```
Enter a string (must be exactly 10 characters): hellothere!
String too long.
```

### 3) Perfect (length 10)
```
Enter a string (must be exactly 10 characters): abcdefghij
Perfect string
First character: a
Last character: j
a
ab
abc
abcd
abcde
abcdef
abcdefg
abcdefgh
abcdefghi
abcdefghij
Jumbled string: fdgijbaech   <-- (your result will vary each time)
```

## Notes / tweaks (optional)
- If you want a **repeatable** jumbled result for testing, add this line before shuffling:
  ```python
  random.seed(0)
  ```
- You can replace `print` lines with formatted strings if you like:
  ```python
  print(f"First character: {s[0]}")
  ```
- If you want to **loop until correct length**, wrap the input logic in a `while True` and `break` when `len(s) == 10`.

## File list
- `buildupastring.py` — the script
- `README.md` — this file
