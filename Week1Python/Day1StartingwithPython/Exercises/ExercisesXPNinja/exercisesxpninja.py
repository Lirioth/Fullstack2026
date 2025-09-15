# Exercises XP Ninja

# Exercise 1 : Use the terminal (short notes)
print("Exercise 1: In terminal run: python3")
print("PATH = list of folders the OS searches for programs; if python is in PATH, you can run 'python3' from anywhere.")

# Exercise 2 : Alias (short notes)
print("Exercise 2: 'py' can be an alias/launcher. On Windows, 'py' starts Python. On Linux/mac, you can define alias py='python3'.")

# Exercise 3 : Outputs (predict and show)
print(3 <= 3 < 9)                  # True
print(3 == 3 == 3)                 # True
print(bool(0))                     # False
print(bool(5 == "5"))              # False
print(bool(4 == 4) == bool("4" == "4"))  # True
print(bool(bool(None)))            # False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10
print("x is", x)   # True
print("y is", y)   # False
print("a:", a)     # 5
print("b:", b)     # 10

# Exercise 4 : How many characters in a sentence ?
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco 
laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit 
esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, 
sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(len(my_text))  # single line after my_text

# Exercise 5 : Longest sentence without 'A'
best = ""
while True:
    s = input("Type a sentence without the letter 'A' (or 'quit' to stop): ")
    if s.lower() == "quit":
        break
    if "a" in s.lower():
        print("Contains 'A'. Try again.")
        continue
    if len(s) > len(best):
        best = s
        print("Congrats, new record:", len(best))
    else:
        print("No new record. Current record:", len(best))

print("Best sentence:", best)