# Python Dictionaries — Exercises XP+ (Student Grades & Sales Analysis)

This repo contains a **simple, well‑commented** Python script that solves two exercises:
1) **Student Grade Summary** — averages + letter grades per student and class average.  
2) **Sales Data Analysis** — totals by product/customer, high‑value transactions, loyalty, averages, and popularity.

> Tested with **Python 3.10+**. Only the standard library is used.

---

## Files

- `dictionaries_xp_plus.py` — the full working solution with small English comments.
- `README_Dictionaries_XP_Plus.md` — this guide.

---

## How to run

```bash
python3 dictionaries_xp_plus.py
```
It prints all results to the console in the order of the tasks.

---

## Exercise 1 — Student Grade Summary

**Input (hard‑coded example):**
```python
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
```

**What the script does:**
- Computes each student’s **numeric average** → `student_averages`.
- Assigns a **letter grade** using this scale:

  - A: 90+  
  - B: 80–89  
  - C: 70–79  
  - D: 60–69  
  - F: < 60

- Computes **class average** (average of all student averages).
- Prints: class average, then each student with `avg` and letter.

**Why it’s written this way:**
- Clear loops and dicts keep the logic easy to follow.
- `round(x, 2)` improves readability when printing averages.

---

## Exercise 2 — Advanced Data Manipulation & Analysis

**Dataset (hard‑coded list of dicts):**
```python
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop",     "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop",     "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500,  "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150,  "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550,  "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100,  "quantity": 2, "date": "2023-04-09"},
]
```

**Steps implemented:**
1. **Enhance data** — add `total_price = price * quantity` to every transaction.
2. **Totals by product** — build `product_totals[product] += total_price`.
3. **Totals by customer** — build `customer_totals[cid] += total_price`.
4. **High‑value transactions** — `total_price > 500`, sorted **desc**.
5. **Loyal customers** — customers with **> 1** purchase.
6. **Bonus A:** **Average transaction value** by product
   - average of `total_price` per product (sum / count of transactions).
7. **Bonus B:** **Most popular product** by **quantity** sold (returns a list to handle ties).

**Outputs printed:**
- `product totals:` dictionary
- `customer totals:` dictionary
- `high value transactions:` list (sorted)
- `loyal customers:` list
- `avg transaction by product:` dictionary
- `most popular product(s):` list

---

## Complexity (quick view)

- Each pass is linear in the number of transactions **O(n)**.  
- Sorting high‑value transactions is **O(k log k)** for `k` matching rows.  
- Memory use is small dictionaries for aggregation.

---

## Tips / Extensions

- Turn each block into a **function** and add unit tests.
- Parse `date` with `datetime.strptime` if you need date‑based grouping.
- Use `collections.Counter/defaultdict` to simplify counting.
- Replace the hard‑coded lists with **CSV** input when scaling up.

---

## License

MIT — do whatever you want, just keep a copy of this file.
