# simple solutions for OOP & Modules XP

from datetime import datetime, date
import string
import random

# -------------------------
# EX1: Currency class
# -------------------------
class Currency:
    # store label and amount
    def __init__(self, currency, amount):
        self.currency = str(currency)
        self.amount = int(amount)

    # pretty text
    def __str__(self):
        label = self.currency if self.amount == 1 else self.currency + "s"
        return f"{self.amount} {label}"

    # debug text (keep same here)
    def __repr__(self):
        return str(self)

    # convert to int
    def __int__(self):
        return int(self.amount)

    # c1 + 5  or  c1 + c2 (same currency)
    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        raise TypeError("Can only add int or Currency")

    # c1 += 5  or  c1 += c2 (same currency)
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
            return self
        raise TypeError("Can only add int or Currency")


# quick demo for EX1 (matches prompt)
def run_ex1():
    print("EX1:")
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)
    c4 = Currency('shekel', 10)

    print(c1)            # '5 dollars'
    print(int(c1))       # 5
    print(repr(c1))      # '5 dollars'
    print(c1 + 5)        # 10
    print(c1 + c2)       # 15
    print(c1)            # 5 dollars
    c1 += 5
    print(c1)            # 10 dollars
    c1 += c2
    print(c1)            # 20 dollars
    try:
        print(c1 + c3)   # should raise
    except TypeError as e:
        print(f"TypeError: {e}")


# -------------------------
# EX2: Import (single-file mock)
# -------------------------
# pretend this is func.py
def sum_two(a, b):
    # very basic add + print
    print(a + b)

# pretend this is exercise_one.py using the import
def run_ex2():
    print("\nEX2:")
    sum_two(3, 7)


# -------------------------
# EX3: Random 5-letter string (letters only)
# -------------------------
def run_ex3():
    print("\nEX3:")
    # take only letters
    letters = string.ascii_letters  # A-Z + a-z
    # build with a simple loop (noob style)
    s = ""
    for _ in range(5):
        s += random.choice(letters)
    print(s)


# -------------------------
# EX4: Current date
# -------------------------
def show_today():
    # print YYYY-MM-DD
    today = date.today()
    print(today.strftime("%Y-%m-%d"))

def run_ex4():
    print("\nEX4:")
    show_today()


# -------------------------
# EX5: Time until Jan 1
# -------------------------
def time_until_jan1():
    # now
    now = datetime.now()
    # next Jan 1 (always the next one)
    next_new_year = datetime(year=now.year + 1, month=1, day=1)
    diff = next_new_year - now
    # print days/hours/minutes/seconds
    days = diff.days
    secs = diff.seconds
    hours = secs // 3600
    minutes = (secs % 3600) // 60
    seconds = secs % 60
    print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

def run_ex5():
    print("\nEX5:")
    time_until_jan1()


# -------------------------
# EX6: Birthday -> minutes lived
# -------------------------
def minutes_lived(birth_str):
    # expect YYYY-MM-DD
    birth = datetime.strptime(birth_str, "%Y-%m-%d")
    now = datetime.now()
    diff = now - birth
    mins = int(diff.total_seconds() // 60)
    print(f"Minutes lived: {mins}")

def run_ex6():
    print("\nEX6:")
    # example: change to your birthday
    minutes_lived("1994-06-16")


# -------------------------
# EX7: Faker users
# -------------------------
def run_ex7():
    print("\nEX7:")
    try:
        from faker import Faker
    except ImportError:
        # simple message if faker not installed
        print("faker is not installed. run: pip install faker")
        return

    fake = Faker()
    users = []

    # simple function to add users
    def add_users(n):
        for _ in range(int(n)):
            user = {
                "name": fake.name(),
                "address": fake.address(),
                "language_code": fake.language_code()
            }
            users.append(user)

    add_users(3)  # make 3 users
    for u in users:
        # print each user dict in a simple way
        print("---")
        print("name:", u["name"])
        print("address:", u["address"])
        print("language_code:", u["language_code"])


# -------------------------
# run all
# -------------------------
if __name__ == "__main__":
    run_ex1()
    run_ex2()
    run_ex3()
    run_ex4()
    run_ex5()
    run_ex6()
    run_ex7()
