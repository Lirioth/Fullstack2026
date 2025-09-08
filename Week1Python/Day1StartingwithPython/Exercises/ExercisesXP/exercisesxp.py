# Exercises XP

# Exercise 1 : Hello World
print("Hello world\nHello world\nHello world\nHello world")

# Exercise 2 : Some Math
print((99**3) * 8)

# Exercise 3 : What is the output ?
print(5 < 3)            # False
print(3 == 3)           # True
print(3 == "3")         # False
try:
    print("3" > 3)      # TypeError in Python
except TypeError:
    print("TypeError")
print("Hello" == "hello")  # False

# Exercise 4 : Your computer brand
computer_brand = "ASUS"
print("I have a " + computer_brand + " computer.")

# Exercise 5 : Your information
name = "Kevin"
age = 30
shoe_size = 400
info = "My name is " + name + ", I'm " + str(age) + " years old and my shoe size is " + str(shoe_size) + "."
print(info)

# Exercise 6 : A & B
a = 10
b = 5
if a > b:
    print("Hello World")

# Exercise 7 : Odd or Even
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 8 : What’s your name ?
my_name = "Kevin"
user_name = input("What is your name? ")
if user_name.strip().lower() == my_name.lower():
    print("Hey, we have the same name! :)")
else:
    print("Nice to meet you, " + user_name + "!")

# Exercise 9 : Tall enough to ride a roller coaster
height = int(input("Enter your height in cm: "))
if height > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.")
