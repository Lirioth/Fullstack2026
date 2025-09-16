# Full-Stack Coding Bootcamp - Python Dictionaries Exercises XP+
# Simple solution with small comments in English. Run with: python3 dictionaries_xp_plus.py

# ------------------------------
# 🌟 Exercise 1 : Student Grade Summary
# ------------------------------

# initial data
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# empty dicts to store results
student_averages = {}
student_letter_grades = {}

# compute average per student + letter grade
for name, grades in student_grades.items():
    avg = sum(grades) / len(grades)           # mean of this student's grades
    student_averages[name] = avg              # save the numeric average

    # simple letter scale
    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    else:
        letter = "F"

    student_letter_grades[name] = letter      # save the letter grade

# class average = average of student averages
class_average = sum(student_averages.values()) / len(student_averages)

# show results
print("=== Exercise 1: Student Grade Summary ===")
print("class average:", round(class_average, 2))
for name in student_grades:
    print(name, "-", round(student_averages[name], 2), student_letter_grades[name])
print()  # empty line


# ------------------------------
# 🌟 Exercise 2 : Advanced Data Manipulation and Analysis
# ------------------------------

# dataset: list of purchases
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# 2.1 add total_price and compute totals per product and per customer
product_totals = {}   # product -> total revenue
customer_totals = {}  # customer_id -> total spend

for t in sales_data:
    # total for this transaction
    t["total_price"] = t["price"] * t["quantity"]

    # accumulate revenue by product
    p = t["product"]
    product_totals[p] = product_totals.get(p, 0) + t["total_price"]

    # accumulate spend by customer
    cid = t["customer_id"]
    customer_totals[cid] = customer_totals.get(cid, 0) + t["total_price"]

print("=== Exercise 2: Sales Analysis ===")
print("product totals:", product_totals)
print("customer totals:", customer_totals)

# 2.2 high-value transactions (> 500), sorted descending by total_price
high_value = [t for t in sales_data if t["total_price"] > 500]
high_value.sort(key=lambda x: x["total_price"], reverse=True)
print("high value transactions:", high_value)

# 2.3 loyalty: customers with more than one purchase
purchase_counts = {}  # customer_id -> count of purchases
for t in sales_data:
    cid = t["customer_id"]
    purchase_counts[cid] = purchase_counts.get(cid, 0) + 1
loyal_customers = [cid for cid, count in purchase_counts.items() if count > 1]
print("loyal customers:", loyal_customers)

# 2.4 bonus: average transaction value per product (average of total_price for that product)
sum_by_prod = {}   # sum of transaction totals per product
cnt_by_prod = {}   # number of transactions per product
for t in sales_data:
    p = t["product"]
    sum_by_prod[p] = sum_by_prod.get(p, 0) + t["total_price"]
    cnt_by_prod[p] = cnt_by_prod.get(p, 0) + 1

avg_txn_by_product = {}
for p in sum_by_prod:
    avg_txn_by_product[p] = sum_by_prod[p] / cnt_by_prod[p]
print("avg transaction by product:", avg_txn_by_product)

# 2.5 bonus: most popular product by quantity sold
qty_sum = {}  # product -> total quantity sold
for t in sales_data:
    p = t["product"]
    qty_sum[p] = qty_sum.get(p, 0) + t["quantity"]

max_qty = max(qty_sum.values())
most_popular = [p for p, q in qty_sum.items() if q == max_qty]  # list in case of ties
print("most popular product(s):", most_popular)
