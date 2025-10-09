"""OOP exercises for Day 1."""


class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(a, b, c):
    oldest = a
    if b.age > oldest.age:
        oldest = b
    if c.age > oldest.age:
        oldest = c
    return oldest

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
        self._groups = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        groups = {}
        for animal in self.animals:
            key = animal[0].upper()
            if key not in groups:
                groups[key] = []
            groups[key].append(animal)
        self._groups = groups
        return groups

    def get_groups(self):
        for key in sorted(self._groups):
            print(f"{key}: {self._groups[key]}")


def exercise_1():
    """Find and display the oldest cat."""
    print("=== Exercise 1: Cats ===")
    cat1 = Cat("Mimi", 4)
    cat2 = Cat("Nala", 7)
    cat3 = Cat("Loki", 2)
    oldest = find_oldest_cat(cat1, cat2, cat3)
    print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.\n")


def exercise_2():
    """Create dogs, show their tricks, and compare sizes."""
    print("=== Exercise 2: Dogs ===")
    davids_dog = Dog("Rex", 50)
    sarahs_dog = Dog("Teacup", 20)
    print(f"{davids_dog.name} is {davids_dog.height} cm")
    davids_dog.bark()
    davids_dog.jump()
    print(f"{sarahs_dog.name} is {sarahs_dog.height} cm")
    sarahs_dog.bark()
    sarahs_dog.jump()
    bigger = davids_dog if davids_dog.height > sarahs_dog.height else sarahs_dog
    print(f"The bigger dog is {bigger.name}.\n")


def exercise_3():
    """Instantiate a song and sing it line by line."""
    print("=== Exercise 3: Song ===")
    stairway = Song([
        "There's a lady who's sure",
        "all that glitters is gold",
        "and she's buying a stairway to heaven",
    ])
    stairway.sing_me_a_song()
    print()


def exercise_4():
    """Manage zoo animals and display grouped listings."""
    print("=== Exercise 4: Zoo ===")
    brooklyn_safari = Zoo("Brooklyn Safari")
    brooklyn_safari.add_animal("Giraffe")
    brooklyn_safari.add_animal("Bear")
    brooklyn_safari.add_animal("Baboon")
    brooklyn_safari.get_animals()
    brooklyn_safari.sell_animal("Bear")
    brooklyn_safari.get_animals()
    brooklyn_safari.sort_animals()
    brooklyn_safari.get_groups()


def main():
    """Run all OOP Day 1 exercises sequentially."""
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()


if __name__ == "__main__":
    main()
