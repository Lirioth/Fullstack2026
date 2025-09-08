# Exercise 1, 2, 3: Birthdays
birthdays = {
    "Alice": "1995/06/12",
    "Bob": "1990/01/23",
    "Charlie": "1988/11/05",
    "Dana": "1993/04/17",
    "Eli": "2000/09/30"
}

print("Welcome! You can look up the birthdays of the people in the list.")

# show all names (Exercise 2)
print("Names:", ", ".join(birthdays.keys()))

# add a new birthday before lookup (Exercise 3)
new_name = input("Add a name (or press Enter to skip): ").strip()
if new_name != "":
    new_bday = input("Enter birthday (YYYY/MM/DD): ").strip()
    birthdays[new_name] = new_bday

# show names again so the new one is visible
print("Names:", ", ".join(birthdays.keys()))

# lookup
name = input("Who do you want to look up? ").strip()
if name in birthdays:
    print(name + "'s birthday is " + birthdays[name])
else:
    print("Sorry, we don't have the birthday information for " + name)

# Exercise 4: Fruit Shop
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for item, price in items.items():
    print(item + " costs " + str(price))

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
