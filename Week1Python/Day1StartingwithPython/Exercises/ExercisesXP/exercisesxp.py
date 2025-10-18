"""
📝 Day 1 - Exercises XP
=======================
Fundamental Python exercises covering:
- Variables and data types
- Input/output operations
- Conditional logic and comparisons
- String manipulation and formatting
- Boolean operations
- Type conversions

Author: Week1Python Course
Python Version: 3.8+
"""

# 🎯 Constants
HEIGHT_REQUIREMENT_CM = 145  # Minimum height to ride in centimeters
MY_NAME = "Kevin"  # Used in exercise 8 for name comparison


def exercise_1() -> None:
    """Display the classic Hello World message."""
    print("Hello world\nHello world\nHello world\nHello world")


def exercise_2() -> None:
    """Compute a simple arithmetic expression."""
    print((99**3) * 8)


def exercise_3() -> None:
    """Show boolean comparisons and exception handling."""
    print(5 < 3)            # ❗ False
    print(3 == 3)           # ❗ True
    print(3 == "3")         # ❗ False
    try:
        print("3" > 3)      # ❗ TypeError in Python
    except TypeError:
        print("TypeError")
    print("Hello" == "hello")  # ❗ False


def exercise_4() -> None:
    """Display the computer brand information."""
    computer_brand = "ASUS"
    print("I have a " + computer_brand + " computer.")


def exercise_5() -> None:
    """Present personal information."""
    name = "Kevin"
    age = 31
    shoe_size = 40
    info = (
        "My name is "
        + name
        + ", I'm "
        + str(age)
        + " years old and my shoe size is "
        + str(shoe_size)
        + "."
    )
    print(info)


def exercise_6() -> None:
    """Compare two numbers and greet the world if appropriate."""
    a = 10
    b = 5
    if a > b:
        print("Hello World")


def read_int(prompt: str, min_val: int | None = None, max_val: int | None = None) -> int:
    """
    Prompt the user until a valid integer is provided.
    
    Args:
        prompt: Message to display to user
        min_val: Minimum acceptable value (inclusive), optional
        max_val: Maximum acceptable value (inclusive), optional
        
    Returns:
        Valid integer within specified range (if provided)
        
    Example:
        >>> age = read_int("Enter age: ", min_val=0, max_val=120)
        >>> number = read_int("Enter any number: ")
    """
    while True:
        try:
            value = int(input(prompt))
            
            # Validate range if specified
            if min_val is not None and value < min_val:
                print(f"❌ Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ Value must be at most {max_val}")
                continue
                
            return value
        except ValueError:
            print("❌ Please enter a valid integer")


def exercise_7() -> None:
    """Determine whether a number is odd or even."""
    n = read_int("Enter a number: ")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


def exercise_8() -> None:
    """Check if the user shares the same name."""
    user_name = input("What is your name? ")
    if user_name.strip().lower() == MY_NAME.lower():
        print("Hey, we have the same name! :)")
    else:
        print(f"Nice to meet you, {user_name}!")


def exercise_9() -> None:
    """Check whether the user is tall enough to ride (>= 145cm)."""
    height = read_int("Enter your height in cm: ", min_val=0, max_val=300)
    # ✅ Uses >= to include exactly 145cm as tall enough
    if height >= HEIGHT_REQUIREMENT_CM:
        print(f"✅ You are tall enough to ride! ({height}cm)")
    else:
        needed = HEIGHT_REQUIREMENT_CM - height
        print(f"❌ You need to grow {needed}cm more to ride.")


def main() -> None:
    """Run all Day 1 exercises in sequence."""
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()
    exercise_6()
    exercise_7()
    exercise_8()
    exercise_9()


if __name__ == "__main__":
    main()
