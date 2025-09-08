# Exercises XP Gold - one file (beginner)

# Exercise 1 : Hello World - I love Python (one line of code)
print("Hello world\n"*4 + "I love python\n"*3 + "I love python")

# Exercise 2 : What is the Season ?
m = int(input("Enter month (1-12): "))
if m in (3, 4, 5):
    print("Spring")
elif m in (6, 7, 8):
    print("Summer")
elif m in (9, 10, 11):
    print("Autumn")
elif m in (12, 1, 2):
    print("Winter")
else:
    print("Invalid month")
