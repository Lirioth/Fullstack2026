# 🌟 Exercise 9 : Tall enough to ride a roller coaster
try:
    height_cm = float(input("Enter your height in cm / Ingresa tu altura en cm: "))
    if height_cm >= 145:
        print("You're tall enough to ride! 🎢")
    else:
        print("You need to grow some more to ride. Keep going! 💪")
except ValueError:
    print("Please enter a valid number / Por favor ingresa un número válido")
