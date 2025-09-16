from random import choice

# =========================
# EXERCISE 1: Pets (Cats)
# =========================
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"

class Bengal(Cat):
    def sing(self, sounds):
        return sounds

class Chartreux(Cat):
    def sing(self, sounds):
        return sounds

class Siamese(Cat):  # Step 1
    pass

# Run EX1
all_cats = [Bengal("Nala", 2), Chartreux("Milo", 5), Siamese("Luna", 3)]  # Step 2
sara_pets = Pets(all_cats)  # Step 3
print("EX1 - Cats walk:")
sara_pets.walk()  # Step 4
print("-" * 30)

# =========================
# EXERCISE 2: Dogs
# =========================
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} wins!"
        elif other_power > my_power:
            return f"{other_dog.name} wins!"
        else:
            return "It's a tie!"

# Run EX2
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Max", 3, 15)
dog3 = Dog("LunaDog", 7, 25)

print("EX2 - Dogs:")
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog3.fight(dog1))
print("-" * 30)

# =========================
# EXERCISE 3: PetDog (inherits Dog)
# =========================
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # args pueden ser nombres (str) o instancias Dog
        names = [self.name]
        for d in args:
            names.append(d if isinstance(d, str) else d.name)
        print(", ".join(names) + " all play together")

    def do_a_trick(self):
        if not self.trained:
            print(f"{self.name} is not trained yet")
            return
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        print(f"{self.name} {choice(tricks)}")

# Run EX3
pet1 = PetDog("Fido", 2, 10)
pet2 = PetDog("Buddy", 4, 18)

print("EX3 - PetDog:")
pet1.train()
pet1.play(pet2, "Max")
pet1.do_a_trick()
pet2.do_a_trick()  # aún no entrenado
print("-" * 30)

# =========================
# EXERCISE 4: Family & Person
# =========================
class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        p = Person(first_name, age, self.last_name)
        self.members.append(p)

    def check_majority(self, first_name):
        for m in self.members:
            if m.first_name == first_name:
                if m.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("This person is not in the family.")

    def family_presentation(self):
        print(f"Family: {self.last_name}")
        for m in self.members:
            print(f"- {m.first_name}, {m.age}")

# Run EX4
fam = Family("Cusnir")
fam.born("Kevin", 30)
fam.born("Janeth", 64)
fam.born("Leon", 67)
fam.born("Liri", 12)

print("EX4 - Family:")
fam.family_presentation()
fam.check_majority("Kevin")
fam.check_majority("Liri")
