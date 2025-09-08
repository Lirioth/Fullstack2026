# Daily challenge: Build up a string

s = input("Enter a string (must be exactly 10 characters): ")

# 1-2) Length checks
if len(s) < 10:
    print("String not long enough.")
elif len(s) > 10:
    print("String too long.")
else:
    print("Perfect string")

    # 3) First and last characters
    print("First character:", s[0])
    print("Last character:", s[-1])

    # 4) Build the string character by character
    built = ""
    for ch in s:
        built += ch
        print(built)

    # 5) Bonus: jumble (shuffle) the string
    import random
    chars = list(s)
    random.shuffle(chars)
    jumbled = "".join(chars)
    print("Jumbled string:", jumbled)
