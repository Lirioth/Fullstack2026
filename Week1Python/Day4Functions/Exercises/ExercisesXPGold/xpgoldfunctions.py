# XP Gold — Functions (short & simple)
# 🚀 Run: python3 xpgoldfunctions.py

import random

# --- Exercise 1: When will I retire? ---

# Hard-code today's date as required by the exercise
CURRENT_YEAR, CURRENT_MONTH, CURRENT_DAY = 2025, 9, 16

def get_age(year, month, day):
    """Return age in whole years based on the hard-coded 'today' above."""
    age = CURRENT_YEAR - year
    # if birthday hasn't happened yet this year -> subtract 1
    if (CURRENT_MONTH, CURRENT_DAY) < (month, day):
        age -= 1
    return age

def can_retire(gender, date_of_birth):
    """Return True if person can retire (men:67, women:62), else False.
    - gender: 'm' or 'f' (case-insensitive)
    - date_of_birth: 'yyyy/mm/dd'
    """
    gender = gender.strip().lower()
    y, m, d = map(int, date_of_birth.strip().split("/"))
    age = get_age(y, m, d)
    retirement_age = 67 if gender == "m" else 62
    return age >= retirement_age

# --- Exercise 2: Sum (X + XX + XXX + XXXX) ---

def series_sum(x):
    """Return X + XX + XXX + XXXX using string repetition."""
    return sum(int(str(x) * k) for k in range(1, 5))

# --- Exercise 3: Double Dice ---

def throw_dice():
    """Return a random die roll from 1..6."""
    return random.randint(1, 6)

def throw_until_doubles():
    """Throw two dice until both match; return number of throws."""
    throws = 0
    while True:
        throws += 1
        a, b = throw_dice(), throw_dice()
        if a == b:
            return throws

def main():
    """Run the doubles experiment 100 times; print total and average."""
    results = [throw_until_doubles() for _ in range(100)]
    total = sum(results)
    avg = total / len(results)
    print(f"Total throws: {total}")
    print(f"Average throws to reach doubles: {avg:.2f}")

if __name__ == "__main__":
    # Small interactive demo
    print("=== Exercise 1 ===")
    g = input("Gender (m/f): ")
    dob = input("DOB (yyyy/mm/dd): ")
    print("You can retire." if can_retire(g, dob) else "You cannot retire yet.")

    print("\n=== Exercise 2 ===")
    x = int(input("Enter a digit X: "))
    print("Result:", series_sum(x))

    print("\n=== Exercise 3 ===")
    # random.seed(0)  # uncomment for reproducible tests
    main()
