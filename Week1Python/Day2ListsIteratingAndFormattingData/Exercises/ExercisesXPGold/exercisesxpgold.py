# Exercises XP Gold

# Exercise 1: Concatenate lists (without +)
a = [1, 2, 3]
b = [4, 5, 6]
c = list(a)          # make a copy
c.extend(b)          # concatenate using extend
print("exercise1:", c)

# Exercise 2: Range of numbers (multiples of 5 and 7)
for n in range(1500, 2501):
    if n % 5 == 0 and n % 7 == 0:
        print(n)

# Exercise 3: Check the index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user = input("Enter a name: ")
if user in names:
    print("index:", names.index(user))
else:
    print("name not found")

# Exercise 4: Greatest Number
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))
print("The greatest number is:", max(x, y, z))

# Exercise 5: The Alphabet (vowel or consonant)
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
for ch in alphabet:
    if ch in vowels:
        print(ch, "- vowel")
    else:
        print(ch, "- consonant")

# Exercise 6: Words and letters
words = []
for _ in range(7):
    words.append(input("Enter a word: "))
letter = input("Enter a single character: ")[:1]
for w in words:
    idx = w.find(letter)
    if idx != -1:
        print(w, "-> index", idx)
    else:
        print("'", letter, "' not found in '", w, "'", sep="")

# Exercise 7: Min, Max, Sum
# ✅ OPTIMIZED: Use mathematical formula instead of creating 1 million items
# Old approach: nums = list(range(1, 1_000_001))  # ❌ ~8MB memory, slow!
# New approach: Calculate directly with formulas ⚡
n = 1_000_000
min_val = 1
max_val = n
sum_val = n * (n + 1) // 2  # 💡 Gauss formula: sum of 1 to n
print(f"min: {min_val}, max: {max_val}, sum: {sum_val}")

# Exercise 8: List and Tuple
data = input("Enter comma-separated numbers: ")
lst = [x.strip() for x in data.split(",")]
tup = tuple(lst)
print(lst)
print(tup)

# Exercise 9: Random number guessing
import random
wins = 0
losses = 0
while True:
    guess = input("Guess 1-9 (or 'q' to quit): ").strip().lower()
    if guess == 'q':
        break
    if not guess.isdigit():
        print("invalid")
        continue
    guess = int(guess)
    if guess < 1 or guess > 9:
        print("out of range")
        continue
    num = random.randint(1, 9)
    if guess == num:
        print("Winner")
        wins += 1
    else:
        print("better luck next time (number was", num, ")")
        losses += 1
print("games won:", wins, "games lost:", losses)
