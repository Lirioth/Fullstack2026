
"""
Exercises XP — All-In-One (single file) 🐍

How to run
- Optional: install Faker for Exercise 7 →  pip install faker
- Run everything:  python Exercises_XP_All_in_One.py

What's inside
1) Currency class with dunder methods (__str__, __repr__, __int__, __add__, __iadd__)
2) "Import" demo (single-file version): simple function add_and_print(a, b)
3) Random 5-letter string using string + random
4) Current date (datetime.date.today)
5) Time left until next January 1st (datetime)
6) Birthday → minutes lived (strptime + total_seconds)
7) Faker users list (name, address, language_code)
All code is short and commented in English.
"""

# ------------------ 1) Currency (dunder methods) ------------------
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def _label(self):
        # add 's' when amount != 1 (simple pluralization)
        return self.currency if self.amount == 1 else self.currency + "s"

    def __str__(self):
        # human-friendly representation
        return f"{self.amount} {self._label()}"

    def __repr__(self):
        # developer-friendly (kept same for simplicity)
        return self.__str__()

    def __int__(self):
        # allow int(Currency(...))
        return int(self.amount)

    def __add__(self, other):
        # Currency + int/float → return a number
        if isinstance(other, (int, float)):
            return self.amount + other
        # Currency + Currency (same label only)
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        return NotImplemented

    def __iadd__(self, other):
        # in-place addition: modify self.amount
        if isinstance(other, (int, float)):
            self.amount += other
            return self
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
            return self
        return NotImplemented


# ------------------ 2) "Import" (single-file simplification) ------------------
def add_and_print(a, b):
    """Print the sum of two numbers (simulating a function from another module)."""
    print(a + b)


# ------------------ 3) Random 5-letter string ------------------
def random_5_letters():
    import string, random
    letters = string.ascii_letters  # A-Z + a-z
    return "".join(random.choice(letters) for _ in range(5))


# ------------------ 4) Current date ------------------
def show_today():
    from datetime import date
    print(date.today())  # YYYY-MM-DD


# ------------------ 5) Time left until Jan 1 ------------------
def time_to_next_jan1():
    from datetime import datetime
    now = datetime.now()
    jan1_next = datetime(year=now.year + 1, month=1, day=1)
    delta = jan1_next - now
    # print days/hours/minutes (simple breakdown)
    print(f"Time until Jan 1: {delta.days} days, {delta.seconds//3600} hours, {(delta.seconds%3600)//60} minutes")


# ------------------ 6) Birthday → minutes lived ------------------
def minutes_lived(birth_str, fmt="%Y-%m-%d"):
    from datetime import datetime
    birth = datetime.strptime(birth_str, fmt)
    now = datetime.now()
    minutes = int((now - birth).total_seconds() // 60)
    print(f"You lived ~{minutes:,} minutes.")


# ------------------ 7) Faker users ------------------
def demo_faker_users(n=5):
    """Generate n fake users. Needs 'faker' package."""
    try:
        from faker import Faker
    except Exception:
        print("Faker not installed. Run: pip install faker")
        return
    fake = Faker()
    users = []
    for _ in range(n):
        users.append({
            "name": fake.name(),
            "address": fake.address().replace("\\n", ", "),
            "language_code": fake.language_code(),
        })
    # print simple list
    for u in users:
        print(u)


# ------------------ Demo runner ------------------
if __name__ == "__main__":
    print("== Exercise 1: Currency ==")
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)
    c4 = Currency('shekel', 10)  # not used, just for reference

    print(c1)            # 5 dollars
    print(int(c1))       # 5
    print(repr(c1))      # 5 dollars
    print(c1 + 5)        # 10
    print(c1 + c2)       # 15
    print(c1)            # 5 dollars
    c1 += 5
    print(c1)            # 10 dollars
    c1 += c2
    print(c1)            # 20 dollars
    try:
        print(c1 + c3)   # TypeError ...
    except TypeError as e:
        print(f"TypeError: {e}")

    print("\n== Exercise 2: Import (single-file) ==")
    add_and_print(2, 3)  # -> 5

    print("\n== Exercise 3: Random 5-letter string ==")
    print(random_5_letters())

    print("\n== Exercise 4: Current date ==")
    show_today()

    print("\n== Exercise 5: Time to next Jan 1 ==")
    time_to_next_jan1()

    print("\n== Exercise 6: Birthday minutes ==")
    minutes_lived("1994-06-16")  # change to your birthdate if you want

    print("\n== Exercise 7: Faker users ==")
    demo_faker_users(5)
