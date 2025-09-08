# Exercises XP - Sequence / List / Set / Tuple (beginner, one file)

# -------- Exercise 1: Favorite Numbers (sets) --------
my_fav_numbers = {7, 13, 27}
last_added = 99
my_fav_numbers.add(42)
my_fav_numbers.add(last_added)
my_fav_numbers.discard(last_added)  # "remove the last one you added"
friend_fav_numbers = {1, 3, 7}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("our_fav_numbers:", our_fav_numbers)

# -------- Exercise 2: Tuple (immutability) --------
t = (1, 2, 3)
# tuples can't be changed in place; create a new one instead
t = t + (4, 5)
print("tuple:", t)

# -------- Exercise 3: List Manipulation --------
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
print("apples count:", basket.count("Apples"))
basket.clear()
print("final basket:", basket)

# -------- Exercise 4: Floats --------
# float has decimals; int is whole number
seq = []
x = 1.5
while x <= 5:
    seq.append(int(x) if x.is_integer() else x)
    x += 0.5
print("sequence:", seq)  # [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

# -------- Exercise 5: For Loop --------
for i in range(1, 21):
    print(i)
for idx, num in enumerate(range(1, 21)):  # print numbers where index is even (0,2,4,...)
    if idx % 2 == 0:
        print(num)

# -------- Exercise 6: While Loop (ask name until it's mine) --------
my_name = "Kevin"
name = ""
while name.strip().lower() != my_name.lower():
    name = input("Enter your name: ")
print("Hi", name)

# -------- Exercise 7: Favorite Fruits --------
favorites = input("Enter your favorite fruits (space separated): ")
fav_list = favorites.split()
fruit = input("Enter a fruit: ")
if fruit in fav_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# -------- Exercise 8: Pizza Toppings --------
toppings = []
while True:
    t = input("Enter a topping (or 'quit' to finish): ")
    if t.lower() == "quit":
        break
    toppings.append(t)
    print("Adding " + t + " to your pizza.")
total_price = 10 + 2.5 * len(toppings)
print("Toppings:", toppings)
print("Total price: $" + format(total_price, ".2f"))

# -------- Exercise 9: Cinemax Tickets --------
ages = []
while True:
    a = input("Enter age (or 'done'): ")
    if a.lower() == "done":
        break
    if a.isdigit():
        ages.append(int(a))
total = 0
for age in ages:
    if age < 3:
        total += 0
    elif age <= 12:
        total += 10
    else:
        total += 15
print("Total ticket cost:", total)

# Bonus: restricted movie ages 16–21
allowed = []
while True:
    a = input("Enter age for restricted movie (or 'done'): ")
    if a.lower() == "done":
        break
    if a.isdigit():
        n = int(a)
        if 16 <= n <= 21:
            allowed.append(n)
print("Allowed attendees ages:", allowed)

# -------- Exercise 10: Sandwich Orders --------
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
print("Sorry, no Pastrami today.")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

finished_sandwiches = []
while sandwich_orders:
    s = sandwich_orders.pop(0)
    print("I made your " + s + " sandwich.")
    finished_sandwiches.append(s)

print("Finished sandwiches:", finished_sandwiches)
