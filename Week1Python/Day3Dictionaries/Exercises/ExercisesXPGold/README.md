# 🥈 Python Practice — Birthdays & Fruit Shop

Two tiny console exercises: a birthday lookup (with optional insert) and a fruit shop inventory cost calculator. Code is kept simple with small comments.

> ▶️ Run with **Python 3.10+**. No extra packages required.

---

## 🚀 How to run

```bash
python3 exercisesxpgold.py
```
Execute the exercises via `exercisesxpgold.py`.

This script **📝 asks for input** a few times in the Birthdays section (adding a contact and doing a lookup). The Fruit Shop section just prints results.

---

## 🎂 Exercise 1–3 — Birthdays

**🎯 Goal:** store some birthdays, optionally add a new person, show the names list, and look up one birthday.

**📊 Data shape:**
```python
birthdays = {
    "Alice": "1995/06/12",
    "Bob": "1990/01/23",
    # ...
}
```

**Steps performed:**
1. Print a welcome message.
2. Print all names with `", ".join(birthdays.keys())`.
3. Ask the user to add a new name (press Enter to skip).
4. If provided, ask for a date in `YYYY/MM/DD` and insert into the dict.
5. Show the names again (so the new one is visible).
6. Ask **who** to look up; print the birthday if found, otherwise a friendly message.

**Tiny code peek:**
```python
# show all names
print("Names:", ", ".join(birthdays.keys()))

# optional insert
new_name = input("Add a name (or press Enter to skip): ").strip()
if new_name != "":
    new_bday = input("Enter birthday (YYYY/MM/DD): ").strip()
    birthdays[new_name] = new_bday

# show names again
print("Names:", ", ".join(birthdays.keys()))

# lookup
name = input("Who do you want to look up? ").strip()
if name in birthdays:
    print(name + "'s birthday is " + birthdays[name])
else:
    print("Sorry, we don't have the birthday information for " + name)
```

**Example run (one possible flow):**
```
Welcome! You can look up the birthdays of the people in the list.
Names: Alice, Bob, Charlie, Dana, Eli
Add a name (or press Enter to skip): Kevin
Enter birthday (YYYY/MM/DD): 1994/06/16
Names: Alice, Bob, Charlie, Dana, Eli, Kevin
Who do you want to look up? Kevin
Kevin's birthday is 1994/06/16
```

**Notes:**
- Date format is treated as plain text (no validation here).
- Keys are case‑sensitive (`"alice"` ≠ `"Alice"`).
- To avoid duplicates, you can check `if new_name in birthdays` before inserting.
- Time complexity: all operations shown are **O(n)** or better for these tiny tasks.

---

## Exercise 4 — Fruit Shop

**Goal:** print item prices and compute the **total cost** to buy all stock from a nested dictionary.

**Phase 1:** simple dict `item → price`
```python
items = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
for item, price in items.items():
    print(item + " costs " + str(price))
```

**Phase 2:** nested dict with `price` and `stock`, then compute total cost
```python
items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_cost = 0
for item, info in items.items():
    total_cost += info["price"] * info["stock"]
print("Total cost to buy everything:", total_cost)
```

**Notes:**
- Multiplying `price * stock` gives the cost to clear that item.
- The code assumes `price` and `stock` exist for each item.
- If you need currency formatting later, use `format` or `locale` libraries.

---

## Tips for my future self
- For the birthdays dict, consider validating dates with `datetime.strptime`.
- Normalize names (e.g., `.title()`) to reduce case mismatches.
- For the fruit shop, guard against missing keys with `dict.get` or `try/except`.
- Wrap each exercise into a function if you plan to unit test.

---

## License
MIT — free to use, copy, and modify.
