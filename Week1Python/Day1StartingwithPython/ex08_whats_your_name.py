# 🌟 Exercise 8 : What's your name?
my_name = "Kevin"
user_name = input("What's your name? / ¿Cómo te llamas? ").strip()

if user_name.lower() == my_name.lower():
    print("Wow, we have the same name! 🤝 That's an instant friendship buff! ✨")
else:
    print(f"Nice to meet you, {user_name}! Great name, but Kevin is still top tier 😉")
