# 🌟 Exercise 7 : Odd or Even
try:
    n = int(input("Enter a number / Ingresa un número: "))
    if n % 2 == 0:
        print("Even / Par")
    else:
        print("Odd / Impar")
except ValueError:
    print("Please enter a valid integer / Por favor ingresa un entero válido")
