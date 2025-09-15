# Daily Challenge : Lists & Strings

# --- Challenge 1: Multiples of a Number ---
number = int(input("Enter a number: "))
length = int(input("Enter length: "))

multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)

# --- Challenge 2: Remove Consecutive Duplicate Letters ---
word = input("Enter a word: ")

if word == "":
    print("")
else:
    result = word[0]
    for ch in word[1:]:
        if ch != result[-1]:
            result += ch
    print(result)
