# 🌟 Exercise 3 : What is the output?
# Expected (Python 3):
# 5 < 3            -> False
# 3 == 3           -> True
# 3 == "3"         -> False
# "3" > 3          -> TypeError (can't compare str and int)
# "Hello" == "hello" -> False

print(5 < 3)           # False
print(3 == 3)          # True
print(3 == "3")        # False
try:
    print("3" > 3)     # TypeError in Python 3
except TypeError as e:
    print(f"TypeError: {e}")
print("Hello" == "hello")  # False
