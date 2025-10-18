# 🏋️ Python Practice — Dictionaries

Compact notes for four small dictionary exercises. Clear steps and tiny code snippets with comments.

> ▶️ Run with **Python 3.10+**. No external packages required.

---

## 🚀 How to run

```bash
python exercisesxp.py
```
The CLI lives in a `_cli()` helper so importing the module exposes the reusable functions without printing anything. Only the optional bonus prompt still asks for live input.

---

## 1️⃣ Exercise 1 — Converting Lists into Dictionaries

**🎯 Goal:** build a dictionary from two parallel lists.

```python
from exercisesxp import build_dict

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
build_dict(keys, values)
# -> {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
```

**Notes:**
- `zip` stops at the shortest list if lengths differ.
- Dicts keep insertion order in modern Python.

---

## Exercise 2 — Cinemax #2

**Goal:** compute ticket price per family member based on age and sum the total.  
**Rules:** `<3 → $0`, `3–12 → $10`, `>12 → $15`.

```python
from exercisesxp import cinemax_report

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
summary = cinemax_report(family)
summary.lines  # ['rick pays 15', 'beth pays 15', 'morty pays 10', 'summer pays 10']
summary.total  # 50
```
Returns a `FamilyTicketSummary` dataclass so the calling code can access `lines` and `total` with dot notation.

The `_bonus_prompt()` helper keeps the original interactive add-on. Leave it untouched if you still want the input loop.

**Tips:**
- `ticket_price(age)` underpins the logic; reuse it for other reports.
- Keep ages as integers to avoid surprises when parsing input.

---

## Exercise 3 — Zara (dictionary practice)

**Goal:** practice updates, insertions, deletions, reading nested data, counting keys, and merging another dict.

```python
from exercisesxp import brand_summary

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
}

stats = brand_summary(brand)
stats["clients"]        # 'men, women, children, home'
stats["last_competitor"] # 'Desigual'
stats["merged_brand"]   # full updated dictionary
```

**Notes:**
- The helper returns a shallow copy so your original `brand` stays untouched.
- `update_brand()` is factored out if you only need the transformed dictionary.

---

## Exercise 4 — Disney Characters

**Goal:** build three mappings from the same list of names.

```python
from exercisesxp import disney_mappings

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
char_to_index, index_to_char, sorted_mapping = disney_mappings(users)
```

**Notes:**
- All three dictionaries come back at once as a tuple.
- Sorting changes indices; that’s why the third mapping rebuilds positions from scratch.

---

## Quick tips for future me
- `dict(zip(a, b))` is still a handy pattern, now encapsulated in `build_dict`.
- For nested dicts, print small parts to confirm shapes before deep access.
- Plug the helpers straight into tests; the CLI only exists for parity with the original exercise outputs.

---

## License
MIT — free to use, copy, and modify.
