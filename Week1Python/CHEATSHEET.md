# 📚 Week 1 Python - Quick Reference Cheat Sheet

> **Print this page** or keep it open while coding! 🖨️

---

## 🎯 Variables & Data Types

```python
# Creating variables (no type declaration needed!)
name = "Alice"          # String (text)
age = 25                # Integer (whole number)
price = 19.99           # Float (decimal)
is_active = True        # Boolean (True/False)

# Type conversion
age_str = str(25)       # "25"
age_int = int("25")     # 25
price_float = float("19.99")  # 19.99

# Check type
type(name)              # <class 'str'>
```

---

## 🔢 Operators

```python
# Arithmetic
10 + 5    # 15 (addition)
10 - 5    # 5  (subtraction)
10 * 5    # 50 (multiplication)
10 / 5    # 2.0 (division - always returns float)
10 // 3   # 3  (floor division - no remainder)
10 % 3    # 1  (modulo - remainder)
2 ** 3    # 8  (exponentiation - power)

# Comparison (returns True/False)
x == y    # Equal to
x != y    # Not equal to
x > y     # Greater than
x < y     # Less than
x >= y    # Greater than or equal to
x <= y    # Less than or equal to

# Logical
and       # Both must be True
or        # At least one must be True
not       # Reverse the boolean
```

---

## 🎨 Strings

```python
# Creation
text = "Hello"          # Double quotes
text = 'Hello'          # Single quotes (same)
multiline = """Line 1
Line 2"""               # Triple quotes for multiple lines

# Concatenation
"Hello" + " " + "World" # "Hello World"
f"{name} is {age}"      # F-string (modern, recommended!)

# Common methods
text.lower()            # "hello"
text.upper()            # "HELLO"
text.strip()            # Remove leading/trailing whitespace
text.split()            # Split into list by spaces
len(text)               # Length of string
text[0]                 # First character
text[-1]                # Last character
text[0:3]               # Slice: characters 0,1,2
```

---

## 📝 Lists (Mutable, Ordered)

```python
# Creation
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "text", True, 3.14]

# Access
fruits[0]               # "apple" (first item)
fruits[-1]              # "cherry" (last item)
fruits[1:3]             # ["banana", "cherry"] (slice)

# Common methods
fruits.append("orange")    # Add to end
fruits.insert(1, "kiwi")   # Insert at index 1
fruits.remove("apple")     # Remove first occurrence
fruits.pop()               # Remove and return last item
fruits.pop(0)              # Remove and return item at index 0
fruits.clear()             # Remove all items
len(fruits)                # Number of items
fruits.count("apple")      # Count occurrences
fruits.sort()              # Sort in place
fruits.reverse()           # Reverse in place

# Checking membership
"apple" in fruits       # True or False
```

---

## 🗂️ Dictionaries (Key-Value Pairs)

```python
# Creation
person = {
    "name": "Alice",
    "age": 25,
    "city": "Paris"
}

# Access
person["name"]          # "Alice"
person.get("age")       # 25 (safe - no error if missing)
person.get("email", "N/A")  # "N/A" if key doesn't exist

# Modify
person["age"] = 26      # Update existing
person["email"] = "alice@example.com"  # Add new
del person["city"]      # Remove key
person.pop("age")       # Remove and return value

# Common methods
person.keys()           # All keys
person.values()         # All values
person.items()          # All key-value pairs
person.update({"job": "Developer"})  # Merge/add items

# Checking membership
"name" in person        # True or False

# Iteration
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 🎯 Sets (Unique Items, Unordered)

```python
# Creation
numbers = {1, 2, 3, 4, 5}
colors = set(["red", "blue", "red"])  # {""red", "blue"}

# Operations
numbers.add(6)          # Add item
numbers.discard(3)      # Remove item (no error if missing)
numbers.remove(3)       # Remove item (error if missing)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
a | b                   # Union: {1, 2, 3, 4, 5}
a & b                   # Intersection: {3}
a - b                   # Difference: {1, 2}
```

---

## 📦 Tuples (Immutable, Ordered)

```python
# Creation
point = (10, 20)
rgb = (255, 128, 0)

# Access (same as lists)
point[0]                # 10
point[-1]               # 20

# Cannot modify! (immutable)
# point[0] = 15  # ❌ ERROR!

# Use case: Coordinates, RGB colors, function returns
```

---

## 🔀 Conditionals

```python
# If statement
if age >= 18:
    print("Adult")

# If-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# If-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary operator (one-liner)
status = "adult" if age >= 18 else "minor"
```

---

## 🔄 Loops

```python
# For loop - iterate over sequence
for item in [1, 2, 3]:
    print(item)

# For loop with range
for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):   # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step by 2)
    print(i)

# For loop with enumerate (index + value)
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
break       # Exit loop immediately
continue    # Skip to next iteration
```

---

## ⚙️ Functions

```python
# Basic function
def greet():
    print("Hello!")

greet()  # Call the function

# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)  # 8

# Default parameters
def greet(name="World"):
    print(f"Hello, {name}!")

greet()         # "Hello, World!"
greet("Alice")  # "Hello, Alice!"

# Type hints (optional but recommended)
def add(a: int, b: int) -> int:
    """Add two integers and return result."""
    return a + b

# Multiple return values (returns tuple)
def get_stats():
    return 10, 20, 30

min_val, max_val, avg = get_stats()
```

---

## 💬 Input/Output

```python
# Output
print("Hello")              # Basic print
print("Hello", "World")     # Multiple items
print(f"Name: {name}")      # F-string formatting

# Input (always returns string!)
name = input("Enter name: ")
age = int(input("Enter age: "))  # Convert to integer

# Input validation
while True:
    try:
        age = int(input("Age: "))
        break
    except ValueError:
        print("Please enter a number!")
```

---

## 🐛 Error Handling

```python
# Try-except
try:
    number = int(input("Enter number: "))
    result = 10 / number
except ValueError:
    print("Not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("This always runs")
```

---

## 💡 Common Patterns

### Swap values
```python
a, b = b, a
```

### List comprehension
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

### Dictionary comprehension
```python
squares = {x: x**2 for x in range(5)}
```

### Check if list is empty
```python
if not my_list:
    print("List is empty")
```

### Find min/max
```python
numbers = [1, 5, 3, 9, 2]
min(numbers)    # 1
max(numbers)    # 9
sum(numbers)    # 20
```

### String checking
```python
text.isdigit()      # All characters are digits
text.isalpha()      # All characters are letters
text.isalnum()      # All alphanumeric
text.startswith("Hello")
text.endswith(".py")
```

---

## 🎯 Quick Tips

1. **Indentation matters!** Use 4 spaces (not tabs)
2. **Variables are case-sensitive**: `name` ≠ `Name`
3. **Lists are 0-indexed**: first item is `[0]`, not `[1]`
4. **Use f-strings** for formatting: `f"{name} is {age}"`
5. **Type hints help readability**: `def add(a: int, b: int) -> int:`
6. **Always validate user input** with try-except
7. **Use meaningful variable names**: `user_age` not `x`

---

## 🆘 Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `SyntaxError` | Missing `:` or wrong indentation | Check colons and indentation |
| `NameError` | Using undefined variable | Define variable first |
| `TypeError` | Wrong type operation | Convert types: `int()`, `str()` |
| `IndexError` | List index out of range | Check `if i < len(list)` |
| `KeyError` | Dictionary key missing | Use `.get()` method |
| `ValueError` | Invalid conversion | Use try-except block |

---

## 📌 Remember

```python
# Good practices
✅ Use descriptive variable names
✅ Add comments for complex logic
✅ Use functions for repeated code
✅ Validate user input
✅ Handle errors with try-except
✅ Test your code with different inputs

# Avoid
❌ Global variables
❌ Single-letter variables (except i, j in loops)
❌ Functions that do too much
❌ Ignoring errors
❌ Copy-pasting code
```

---

**🚀 Now you're ready to code! Keep this cheat sheet handy while working on exercises!**
