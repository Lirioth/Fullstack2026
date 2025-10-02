# 🏋️ Python Practice — Dictionaries

Compact notes for four small dictionary exercises. Clear steps and tiny code snippets with comments.

> ▶️ Run with **Python 3.10+**. No external packages required.

---

## 🚀 How to run

```bash
python3 main.py
```
Replace `main.py` with your filename if different.  
Parts of the script read input (bonus in Exercise 2), the rest just print.

---

## 1️⃣ Exercise 1 — Converting Lists into Dictionaries

**🎯 Goal:** build a dictionary from two parallel lists.

```python
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# pair up: ('Ten', 10), ('Twenty', 20), ...
pairs = zip(keys, values)

# dict from pairs
d = dict(pairs)
print(d)  # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
```

**Notes:**
- `zip` stops at the shortest list if lengths differ.
- Dicts keep insertion order in modern Python.

---

## Exercise 2 — Cinemax #2

**Goal:** compute ticket price per family member based on age and sum the total.  
**Rules:** `<3 → $0`, `3–12 → $10`, `>12 → $15`.

```python
family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
total = 0

for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(name, "pays", price)  # show each person's price
    total += price              # add to total

print("total:", total)
```

**Bonus (optional):** interactively add more people and keep a separate `more_total`.

```python
more_total = 0
ans = input("Add extra family? (y/n): ").strip().lower()

while ans == "y":
    nm = input("name: ").strip()
    ag = int(input("age: ").strip())

    if ag < 3:
        p = 0
    elif ag <= 12:
        p = 10
    else:
        p = 15

    print(nm, "pays", p)
    more_total += p
    ans = input("Add extra family? (y/n): ").strip().lower()

if more_total:
    print("extra total:", more_total)
```

**Tips:**
- Always convert the `age` input with `int(...)`.
- You can merge totals if you prefer a single final number.

---

## Exercise 3 — Zara (dictionary practice)

**Goal:** practice updates, insertions, deletions, reading nested data, counting keys, and merging another dict.

```python
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
}

# update a value
brand["number_stores"] = 2

# format a list into a string
print("Zara clients:", ", ".join(brand["type_of_clothes"]))

# add a new key
brand["country_creation"] = "Spain"

# append to a list if present
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# remove a key safely (ignore if missing)
brand.pop("creation_date", None)

# read nested values
print("last competitor:", brand["international_competitors"][-1])
print("US colors:", brand["major_color"]["US"])

# count + list keys
print("num keys:", len(brand))
print("keys:", list(brand.keys()))

# merge another dict (overwrites on collisions)
more_on_zara = {"creation_date": 1975, "number_stores": 10000}
brand.update(more_on_zara)
print("merged brand:", brand)
```

**Notes:**
- After `update`, `number_stores` is `10000` again.
- `pop("creation_date", None)` prevents `KeyError`.

---

## Exercise 4 — Disney Characters

**Goal:** build three mappings from the same list of names.

```python
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
```

1) **character → index** (original positions):
```python
d1 = {}
for i, u in enumerate(users):
    d1[u] = i
print(d1)
```

2) **index → character** (reverse mapping):
```python
d2 = {}
for i, u in enumerate(users):
    d2[i] = u
print(d2)
```

3) **sorted characters → new indices** (alphabetical order):
```python
sorted_users = sorted(users)
d3 = {}
for i, u in enumerate(sorted_users):
    d3[u] = i
print(d3)
```

**Notes:**
- `enumerate(seq)` yields `(index, value)`.
- Sorting changes indices; that’s why we rebuild the mapping.

---

## Quick tips for future me
- `dict(zip(a, b))` is a handy pattern for parallel lists.
- For nested dicts, print small parts to confirm shapes before deep access.
- Keep prints consistent so it’s easy to compare with expected outputs.

---

## License
MIT — free to use, copy, and modify.
