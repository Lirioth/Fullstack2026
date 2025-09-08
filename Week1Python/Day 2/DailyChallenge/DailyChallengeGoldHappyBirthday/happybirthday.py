# Daily Challenge GOLD : Happy birthday (beginner)

from datetime import date, datetime
import calendar

# ask for birthdate
s = input("Enter your birthdate (DD/MM/YYYY): ").strip()

# parse and compute age
bday = datetime.strptime(s, "%d/%m/%Y").date()
today = date.today()
age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))

# candles = last digit of age
candles = age % 10  # if age ends with 0, this will be 0

def print_cake(c):
    top = "       ___" + ("i" * c) + "___"
    print(top)
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

# print one or two cakes (bonus: leap year)
if calendar.isleap(bday.year):
    print_cake(candles)
    print_cake(candles)
else:
    print_cake(candles)
