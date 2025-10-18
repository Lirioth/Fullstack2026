# Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d = dict(zip(keys, values))
print(d)  # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# Exercise 2: Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total = 0
for name, age in family.items():
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15
    print(name, "pays", price)
    total += price
print("total:", total)

# Bonus (optional)
more_total = 0
ans = input("Add extra family? (y/n): ").strip().lower()
while ans == "y":
    nm = input("name: ").strip()
    age_input = input("age: ").strip()
    
    # ✅ IMPROVED: Add try/except for input validation
    try:
        ag = int(age_input)
        if ag < 0:
            print("⚠️ Age cannot be negative. Skipping...")
            ans = input("Add extra family? (y/n): ").strip().lower()
            continue
    except ValueError:
        print("❌ Invalid age! Please enter a number. Skipping...")
        ans = input("Add extra family? (y/n): ").strip().lower()
        continue
    
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

# Exercise 3: Zara
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
}

brand["number_stores"] = 2
print("Zara clients:", ", ".join(brand["type_of_clothes"]))
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
brand.pop("creation_date", None)
print("last competitor:", brand["international_competitors"][-1])
print("US colors:", brand["major_color"]["US"])
print("num keys:", len(brand))
print("keys:", list(brand.keys()))

more_on_zara = {"creation_date": 1975, "number_stores": 10000}
brand.update(more_on_zara)
print("merged brand:", brand)

# Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1) character -> index
d1 = {}
for i, u in enumerate(users):
    d1[u] = i
print(d1)

# 2) index -> character
d2 = {}
for i, u in enumerate(users):
    d2[i] = u
print(d2)

# 3) sorted characters -> new indices
sorted_users = sorted(users)
d3 = {}
for i, u in enumerate(sorted_users):
    d3[u] = i
print(d3)