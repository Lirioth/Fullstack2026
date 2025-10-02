# 💪 Solve The Matrix — Column‑Wise Decoder (Python)

A tiny script that reads a block of text **column by column** and reconstructs a clean English sentence by:
1) concatenating all **🔤 letters** in reading order, and  
2) replacing any **run of non‑letters** (digits, punctuation, spaces) that appears *between* letters with a **single space**.  
Leading and trailing non‑letters are ignored.

---

## 🔍 What it does (at a glance)

Given this matrix (rows can be jagged in length):

```
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%
```

The script first reads it **🔽 column‑wise** (top → bottom, left → right), then cleans it, and finally prints:

```
This is Matrix
```

---

## How to run

```bash
python3 solvethematrix.py
```

- Requires **Python 3.8+** (any recent Python 3 is fine).  
- No external packages needed.  
- Output is printed to standard output.

---

## How it works

1. **Split** the multiline string into `rows` and compute `cols = max(len(row))` so we know how many columns to scan.
2. **Column read:** for each column index `c` in `0..cols-1`, append `rows[r][c]` if that row is long enough.
3. **Clean up noise:** walk the concatenated text once:
   - If the character is a **letter**, append it to the result.
   - If it is **not** a letter:
     - **Before** the first letter has been seen → skip it.
     - **After** at least one letter → skip the whole run of non‑letters and insert **one single space** (but only if the previous output isn’t already a space).
4. **Stop** if the end contains only non‑letters (they’re ignored).

This preserves natural word spacing while removing junk symbols between words.

---

## Customizing

- Edit the `MATRIX_STR` triple‑quoted string and paste your own block.  
- Rows may have different lengths; the scan safely checks bounds per row.  
- If you want to **keep digits** as valid characters, change the `isalpha()` checks to accept digits too (e.g., `ch.isalnum()`).

---

## Complexity

- **Time:** `O(R × C)` to read the grid + `O(R × C)` to clean → overall linear in the number of characters.  
- **Space:** `O(R × C)` for the intermediate concatenation (can be streamed if needed).

---

## Example (quick test)

Try replacing `MATRIX_STR` with a small custom block like:
```python
MATRIX_STR = """
A0!
 b?
  c
"""
```
Expected: `A b c`

---

## Notes

- Uses only built‑in Python features.
- Safe on ragged matrices (rows of unequal length).
- Easy to adapt if you’d like to keep punctuation marks selectively.
