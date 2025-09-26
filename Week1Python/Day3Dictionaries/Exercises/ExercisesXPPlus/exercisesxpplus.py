# --- Exercise 1 : Student Grade Summary ---
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}

for name, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    student_averages[name] = avg
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
    student_letter_grades[name] = letter

class_average = sum(student_averages.values()) / len(student_averages)
print("class average:", round(class_average, 2))
for name in student_grades:
    print(name, "-", round(student_averages[name], 2), student_letter_grades[name])

# --- Exercise 2 : Advanced Data Manipulation and Analysis ---
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# add total_price and compute totals
product_totals = {}
customer_totals = {}
for t in sales_data:
    t["total_price"] = t["price"] * t["quantity"]
    product_totals[t["product"]] = product_totals.get(t["product"], 0) + t["total_price"]
    customer_totals[t["customer_id"]] = customer_totals.get(t["customer_id"], 0) + t["total_price"]

print("product totals:", product_totals)
print("customer totals:", customer_totals)

# high-value transactions (> 500), sorted desc
high_value = [t for t in sales_data if t["total_price"] > 500]
high_value.sort(key=lambda x: x["total_price"], reverse=True)
print("high value:", high_value)

# loyalty: customers with more than one purchase
counts = {}
for t in sales_data:
    cid = t["customer_id"]
    counts[cid] = counts.get(cid, 0) + 1
loyal = [cid for cid, c in counts.items() if c > 1]
print("loyal customers:", loyal)

# bonus: average transaction value per product
prod_sum = {}
prod_cnt = {}
for t in sales_data:
    p = t["product"]
    prod_sum[p] = prod_sum.get(p, 0) + t["total_price"]
    prod_cnt[p] = prod_cnt.get(p, 0) + 1
prod_avg = {}
for p in prod_sum:
    prod_avg[p] = prod_sum[p] / prod_cnt[p]
print("avg transaction by product:", prod_avg)

# bonus: most popular product by quantity sold
qty_sum = {}
for t in sales_data:
    p = t["product"]
    qty_sum[p] = qty_sum.get(p, 0) + t["quantity"]
max_qty = max(qty_sum.values())
popular = [p for p, q in qty_sum.items() if q == max_qty]
print("most popular:", popular)
