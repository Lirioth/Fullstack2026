# Challenge 1: Letter Index Dictionary
word = input("Enter a word: ")
d = {}
for i, ch in enumerate(word):
    if ch in d:
        d[ch].append(i)
    else:
        d[ch] = [i]
print(d)

# Challenge 2: Affordable Items
def to_int(s):
    return int(s.replace("$", "").replace(",", "").strip())

# Example 1
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
affordable = []
for name, price in items_purchase.items():
    if to_int(price) <= to_int(wallet):
        affordable.append(name)
affordable.sort()
print(affordable if affordable else "Nothing")

# Example 2
items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"
affordable = []
for name, price in items_purchase.items():
    if to_int(price) <= to_int(wallet):
        affordable.append(name)
affordable.sort()
print(affordable if affordable else "Nothing")

# Example 3
items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"
affordable = []
for name, price in items_purchase.items():
    if to_int(price) <= to_int(wallet):
        affordable.append(name)
affordable.sort()
print(affordable if affordable else "Nothing")
