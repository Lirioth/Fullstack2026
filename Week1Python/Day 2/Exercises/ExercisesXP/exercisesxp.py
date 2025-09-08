# Exercises XP - Lists, Iterating, Formatting (beginner, one file)

# -------- Exercise 1: Favorite Numbers (sets) --------
my_fav_numbers = {7, 13, 27}
my_fav_numbers.add(42)
my_fav_numbers.add(99)
my_fav_numbers.remove(99)  # sets are unordered; just remove one we added
friend_fav_numbers = {1, 3, 7}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("our_fav_numbers:", our_fav_numbers)

# -------- Exercise 2: Tuple (immutability) --------
t = (1, 2, 3)
# Tuples are immutable; you can't change in place, but you can create a new one
t = t + (4, 5)
print("tuple:", t)

# -------- Exercise 3: List Manipulation --------
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
count_apples = basket.count("Apples")
print("apples count:", count_apples)
basket.clear()
print("final basket:", basket)

# -------- Exercise 4: Floats --------
# float: number with decimal part; int: whole number
# generate: 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (without hard-coding each)
seq = [i / 2 for i in range(3, 11)]  # 3/2=1.5 up to 10/2=5.0
print("sequence:", seq)

# -------- Exercise 5: For Loop --------
for i in range(1, 21):
  print(i)
for i in range(1, 21):
  if i % 2 == 0:
    print(i)

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
