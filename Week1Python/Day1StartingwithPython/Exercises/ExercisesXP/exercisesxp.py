"""Interactive exercises for Day 1."""


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


def read_int(prompt: str) -> int:
    """Prompt the user until a valid integer is provided."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer 🤖")


def exercise_7() -> None:
    """Determine whether a number is odd or even."""
    n = read_int("Enter a number: ")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


def exercise_8() -> None:
    """Check if the user shares the same name."""
    my_name = "Kevin"
    user_name = input("What is your name? ")
    if user_name.strip().lower() == my_name.lower():
        print("Hey, we have the same name! :)")
    else:
        print("Nice to meet you, " + user_name + "!")


def exercise_9() -> None:
    """Check whether the user is tall enough to ride."""
    height = read_int("Enter your height in cm: ")
    # ✅ Fixed: Use >= to include exactly 145cm as tall enough
    if height >= 145:
        print("You are tall enough to ride.")
    else:
        print("You need to grow some more to ride.")


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
