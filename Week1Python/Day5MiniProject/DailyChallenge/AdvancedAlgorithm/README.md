# 🧠 Daily Challenge — Advanced Algorithm (Two-Sum Pairs) ✨

Find **all pairs** of numbers in a list of **20,000 random integers** that sum to a given **target** — efficiently and without double-counting.  
This package includes clean Python code (English-only), comments, and a tiny CLI.

## 📂 Structure
```
daily_advanced_pairs/
├─ src/
│  ├─ pairs.py      # Core algorithms: hash-map (O(n)) and two-pointer (O(n log n))
│  └─ demodata.py   # Starter data generation (matches the prompt) + optional seeding
└─ main.py          # CLI: run the finder, print stats & sample pairs
└─ README.md        # This guide
```

## 🚀 Quick Start
```bash
python3 main.py
```
Defaults:
- 20,000 numbers from 0..10,000
- `target=3728` (as in the prompt)
- Prints unique **value pairs** `(a, b)` with `a ≤ b` and the **total number of index-pairs** implied by duplicates.
- Shows a small sample of pairs like: `1000 and 2728 sum to 3728`.

### CLI Options
```bash
python3 main.py --target 3728 --seed 1337 --sample 10
```
- `--target`: target sum (default `3728`)
- `--seed`: fix random seed for reproducibility (default: none)
- `--sample`: how many sample pairs to display (default `10`)
- `--algo`: `hash` (default) or `two-pointer`

## 🧩 What’s included
- **Unique value pairs** only (no `(b, a)` duplicates).  
- Correct handling of the **`a == b`** case (e.g., `1864 + 1864 = 3728`) using combinations `nC2` for counts.  
- A **total index-pair count** (how many `(i, j)` pairs exist in the list) **without enumerating them** — avoids huge memory/time.

## ⏱ Complexity
- **Hash-map approach:** time `O(n)`, space `O(u)` where `u` is the number of distinct values.  
- **Two-pointer approach:** time `O(n log n)` due to sorting, space `O(1)` beyond the sort.

## 🧪 Example Output (abridged)
```
Target: 3728
Numbers: 20000 (range 0..10000)
Algorithm: hash
Unique value pairs found: 142
Total index-pairs (with multiplicities): 367
Sample pairs:
- 1000 and 2728 sum to 3728
- 1864 and 1864 sum to 3728
...
```

## 💡 Notes
- We avoid double-counting by iterating values `a` and computing `b = target - a` with `a ≤ b`.
- For `a == b`, we require at least **two** occurrences and add `nC2` to the index-pair count.
- If you truly need **all index pairs** (positions), that set can be massive; it’s easy to add a small sampler.

Happy hunting for sums! ✨🐍
