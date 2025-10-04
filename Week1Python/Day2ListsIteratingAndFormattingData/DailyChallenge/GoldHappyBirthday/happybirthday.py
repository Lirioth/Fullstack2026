# 🎉 Daily Challenge GOLD : Happy birthday (beginner)

from datetime import date, datetime
import calendar

def print_cake(c):
    top = "       ___" + ("i" * c) + "___"
    print(top)
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

def main():
    s = input("Enter your birthdate (DD/MM/YYYY): ").strip()

    try:
        bday = datetime.strptime(s, "%d/%m/%Y").date()
    except ValueError:
        print("Please use DD/MM/YYYY and ensure the date is valid.")
        return

    today = date.today()
    age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))

    candles = age % 10  # If age ends with 0, this will be 0 🎂

    if calendar.isleap(bday.year):
        print_cake(candles)
        print_cake(candles)
    else:
        print_cake(candles)


if __name__ == "__main__":
    main()
