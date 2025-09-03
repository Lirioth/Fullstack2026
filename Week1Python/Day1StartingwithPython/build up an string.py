# Daily challenge: Build up a string

user_str = input("Enter a string of exactly 10 characters: ")

if len(user_str) < 10:
    print("String not long enough.")
elif len(user_str) > 10:
    print("String too long.")
else:
    print("Perfect string")

    # 3) First and last characters
    print("First character:", user_str[0])
    print("Last character:", user_str[-1])

    # 4) Build the string character by character
    partial = ""
    for ch in user_str:
        partial += ch
        print(partial)
