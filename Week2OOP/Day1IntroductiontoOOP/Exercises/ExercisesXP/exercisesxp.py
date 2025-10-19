"""
OOP exercises for Day 1: Introduction to Object-Oriented Programming.

This module contains implementations for basic OOP concepts including:
- Cat class with age management
- Dog class with behavior methods
- Song class for lyrics display
- Zoo class for animal management

Author: Kevin "Lirioth" Cusnir
Date: 2025-10-19
"""

from typing import List, Optional, Any, Union
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@dataclass
class Cat:
    """
    Represents a domestic cat with basic attributes and behaviors.
    
    Attributes:
        name: The cat's name
        age: The cat's age in years
        
    Raises:
        ValueError: If name is empty or age is negative
        TypeError: If parameters are not of expected types
        
    Examples:
        >>> cat = Cat("Mimi", 4)
        >>> print(cat.name)
        Mimi
        >>> print(cat.is_senior)
        False
    """
    name: str
    age: int
    
    def __post_init__(self) -> None:
        """Validates cat data after initialization."""
        if not isinstance(self.name, str):
            raise TypeError(f"Name must be a string, got {type(self.name).__name__}")
        if not isinstance(self.age, int):
            raise TypeError(f"Age must be an integer, got {type(self.age).__name__}")
        if not self.name.strip():
            raise ValueError("Cat name cannot be empty or whitespace")
        if self.age < 0:
            raise ValueError(f"Cat age cannot be negative, got {self.age}")
        
        self.name = self.name.strip()
        logger.debug(f"Created cat: {self.name}, age {self.age}")
    
    def __str__(self) -> str:
        """Returns a human-readable string representation."""
        return f"Cat(name='{self.name}', age={self.age})"
    
    def __repr__(self) -> str:
        """Returns a debug string representation."""
        return f"Cat('{self.name}', {self.age})"
    
    def __eq__(self, other: Any) -> bool:
        """Compares two cats for equality by name and age."""
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name == other.name and self.age == other.age
    
    def __lt__(self, other: 'Cat') -> bool:
        """Compares cats by age for sorting."""
        if not isinstance(other, Cat):
            return NotImplemented
        return self.age < other.age
    
    def __hash__(self) -> int:
        """Makes Cat hashable for use in sets and dicts."""
        return hash((self.name, self.age))
    
    @property
    def is_senior(self) -> bool:
        """Returns True if the cat is senior (>= 7 years old)."""
        return self.age >= 7
    
    @property
    def is_kitten(self) -> bool:
        """Returns True if the cat is a kitten (< 1 year old)."""
        return self.age < 1
    
    @property
    def life_stage(self) -> str:
        """Returns the cat's life stage as a string."""
        if self.is_kitten:
            return "Kitten"
        elif self.is_senior:
            return "Senior"
        else:
            return "Adult"
    
    def celebrate_birthday(self) -> None:
        """Increments the cat's age by 1 year."""
        old_age = self.age
        self.age += 1
        logger.info(f"{self.name} celebrated birthday! {old_age} → {self.age} years old")
    
    def meow(self) -> str:
        """Returns the sound a cat makes."""
        return f"{self.name} says: Meow!"


def find_oldest_cat(*cats: Cat) -> Cat:
    """
    Finds the oldest cat among the provided cats.
    
    Args:
        *cats: One or more Cat objects to compare
        
    Returns:
        The Cat object with the highest age
        
    Raises:
        ValueError: If no cats are provided
        TypeError: If any argument is not a Cat object
        
    Examples:
        >>> cat1 = Cat("Young", 2)
        >>> cat2 = Cat("Old", 8)
        >>> oldest = find_oldest_cat(cat1, cat2)
        >>> print(oldest.name)
        Old
    """
    if not cats:
        raise ValueError("At least one cat must be provided")
    
    # Validate all arguments are Cat objects
    for i, cat in enumerate(cats, 1):
        if not isinstance(cat, Cat):
            raise TypeError(f"Argument {i} must be a Cat object, got {type(cat).__name__}")
    
    oldest = max(cats, key=lambda cat: cat.age)
    logger.info(f"Oldest cat is {oldest.name} with {oldest.age} years")
    return oldest


def find_youngest_cat(*cats: Cat) -> Cat:
    """
    Finds the youngest cat among the provided cats.
    
    Args:
        *cats: One or more Cat objects to compare
        
    Returns:
        The Cat object with the lowest age
    """
    if not cats:
        raise ValueError("At least one cat must be provided")
    
    youngest = min(cats, key=lambda cat: cat.age)
    logger.info(f"Youngest cat is {youngest.name} with {youngest.age} years")
    return youngest


def get_average_age(cats: List[Cat]) -> float:
    """
    Calculates the average age of a list of cats.
    
    Args:
        cats: List of Cat objects
        
    Returns:
        Average age as a float, or 0.0 if list is empty
    """
    if not cats:
        return 0.0
    
    total_age = sum(cat.age for cat in cats)
    average = total_age / len(cats)
    logger.debug(f"Average age of {len(cats)} cats: {average:.1f} years")
    return average

@dataclass
class Dog:
    """
    Represents a dog with physical attributes and behaviors.
    
    Attributes:
        name: The dog's name
        height: The dog's height in centimeters
        
    Raises:
        ValueError: If name is empty or height is not positive
        TypeError: If parameters are not of expected types
    """
    name: str
    height: Union[int, float]
    
    def __post_init__(self) -> None:
        """Validates dog data after initialization."""
        if not isinstance(self.name, str):
            raise TypeError(f"Name must be a string, got {type(self.name).__name__}")
        if not isinstance(self.height, (int, float)):
            raise TypeError(f"Height must be a number, got {type(self.height).__name__}")
        if not self.name.strip():
            raise ValueError("Dog name cannot be empty or whitespace")
        if self.height <= 0:
            raise ValueError(f"Dog height must be positive, got {self.height}")
        
        self.name = self.name.strip()
        self.height = float(self.height)
        logger.debug(f"Created dog: {self.name}, height {self.height}cm")
    
    def __str__(self) -> str:
        """Returns a human-readable string representation."""
        return f"Dog(name='{self.name}', height={self.height}cm)"
    
    def __repr__(self) -> str:
        """Returns a debug string representation."""
        return f"Dog('{self.name}', {self.height})"
    
    @property
    def size_category(self) -> str:
        """Returns the dog's size category based on height."""
        if self.height < 25:
            return "Toy"
        elif self.height < 40:
            return "Small"
        elif self.height < 60:
            return "Medium"
        elif self.height < 70:
            return "Large"
        else:
            return "Giant"
    
    def bark(self) -> str:
        """
        Makes the dog bark with size-appropriate sound.
        
        Returns:
            A string describing the dog's bark
        """
        size = self.size_category
        if size in ["Toy", "Small"]:
            sound = "yip yip!"
        elif size == "Medium":
            sound = "woof!"
        else:
            sound = "WOOF!"
        
        bark_msg = f"{self.name} goes {sound}"
        logger.info(f"Dog bark: {bark_msg}")
        print(bark_msg)
        return bark_msg
    
    def jump(self) -> str:
        """
        Makes the dog jump with height proportional to size.
        
        Returns:
            A string describing the jump height
        """
        jump_height = self.height * 2
        jump_msg = f"{self.name} jumps {jump_height:.1f} cm high!"
        logger.info(f"Dog jump: {jump_msg}")
        print(jump_msg)
        return jump_msg
    
    def compare_size(self, other: 'Dog') -> str:
        """
        Compares this dog's size with another dog.
        
        Args:
            other: Another Dog object to compare with
            
        Returns:
            A string describing the size comparison
            
        Raises:
            TypeError: If other is not a Dog object
        """
        if not isinstance(other, Dog):
            raise TypeError(f"Can only compare with another Dog, got {type(other).__name__}")
        
        if self.height > other.height:
            result = f"{self.name} is bigger than {other.name}"
        elif self.height < other.height:
            result = f"{other.name} is bigger than {self.name}"
        else:
            result = f"{self.name} and {other.name} are the same size"
        
        logger.info(f"Size comparison: {result}")
        return result

@dataclass
class Song:
    """
    Represents a song with lyrics that can be sung line by line.
    
    Attributes:
        lyrics: List of strings representing song lines
        title: Optional title for the song
        
    Raises:
        ValueError: If lyrics is empty or contains non-strings
        TypeError: If lyrics is not a list
    """
    lyrics: List[str]
    title: Optional[str] = None
    
    def __post_init__(self) -> None:
        """Validates song data after initialization."""
        if not isinstance(self.lyrics, list):
            raise TypeError(f"Lyrics must be a list, got {type(self.lyrics).__name__}")
        if not self.lyrics:
            raise ValueError("Song must have at least one line of lyrics")
        
        # Validate all lyrics are strings
        for i, line in enumerate(self.lyrics):
            if not isinstance(line, str):
                raise ValueError(f"Lyric line {i+1} must be a string, got {type(line).__name__}")
        
        # Clean up lyrics (strip whitespace but preserve empty lines)
        self.lyrics = [line.rstrip() for line in self.lyrics]
        
        if self.title:
            self.title = self.title.strip()
        
        logger.debug(f"Created song: {len(self.lyrics)} lines" + 
                    (f" - '{self.title}'" if self.title else ""))
    
    def __str__(self) -> str:
        """Returns a human-readable string representation."""
        title_part = f"'{self.title}'" if self.title else "Untitled"
        return f"Song({title_part}, {len(self.lyrics)} lines)"
    
    def __len__(self) -> int:
        """Returns the number of lines in the song."""
        return len(self.lyrics)
    
    def __getitem__(self, index: int) -> str:
        """Allows indexing to get specific lyrics lines."""
        return self.lyrics[index]
    
    def sing_me_a_song(self) -> None:
        """
        Prints the song lyrics line by line.
        
        If the song has a title, it's displayed first.
        """
        if self.title:
            print(f"🎵 {self.title} 🎵")
            print("-" * (len(self.title) + 6))
        
        for i, line in enumerate(self.lyrics, 1):
            print(f"{line}")
            logger.debug(f"Sang line {i}: {line[:30]}{'...' if len(line) > 30 else ''}")
        
        if self.title:
            print("-" * (len(self.title) + 6))
        
        logger.info(f"Finished singing song with {len(self.lyrics)} lines")
    
    def get_lyrics_preview(self, max_lines: int = 3) -> str:
        """
        Returns a preview of the song lyrics.
        
        Args:
            max_lines: Maximum number of lines to include in preview
            
        Returns:
            A string with the first few lines of the song
        """
        preview_lines = self.lyrics[:max_lines]
        preview = "\n".join(preview_lines)
        if len(self.lyrics) > max_lines:
            preview += f"\n... ({len(self.lyrics) - max_lines} more lines)"
        return preview
    
    def add_line(self, line: str) -> None:
        """
        Adds a new line to the song.
        
        Args:
            line: The lyric line to add
            
        Raises:
            TypeError: If line is not a string
        """
        if not isinstance(line, str):
            raise TypeError(f"Lyric line must be a string, got {type(line).__name__}")
        
        self.lyrics.append(line.rstrip())
        logger.info(f"Added line to song: {line[:30]}{'...' if len(line) > 30 else ''}")

class Zoo:
    """
    Manages a zoo with animals and provides organization capabilities.
    
    Attributes:
        name: The zoo's name
        animals: List of animal names
        
    The zoo can group animals alphabetically and manage the collection
    through add/remove operations.
    """
    
    def __init__(self, zoo_name: str) -> None:
        """
        Initializes a zoo with a name.
        
        Args:
            zoo_name: The name of the zoo
            
        Raises:
            ValueError: If zoo_name is empty
            TypeError: If zoo_name is not a string
        """
        if not isinstance(zoo_name, str):
            raise TypeError(f"Zoo name must be a string, got {type(zoo_name).__name__}")
        if not zoo_name.strip():
            raise ValueError("Zoo name cannot be empty or whitespace")
        
        self.name = zoo_name.strip()
        self.animals: List[str] = []
        self._groups: dict[str, List[str]] = {}
        logger.info(f"Created zoo: {self.name}")
    
    def __str__(self) -> str:
        """Returns a human-readable string representation."""
        return f"Zoo('{self.name}', {len(self.animals)} animals)"
    
    def __len__(self) -> int:
        """Returns the number of animals in the zoo."""
        return len(self.animals)
    
    def __contains__(self, animal: str) -> bool:
        """Checks if an animal is in the zoo."""
        return animal in self.animals
    
    def add_animal(self, new_animal: str) -> bool:
        """
        Adds a new animal to the zoo if not already present.
        
        Args:
            new_animal: Name of the animal to add
            
        Returns:
            True if animal was added, False if already present
            
        Raises:
            TypeError: If new_animal is not a string
            ValueError: If new_animal is empty
        """
        if not isinstance(new_animal, str):
            raise TypeError(f"Animal name must be a string, got {type(new_animal).__name__}")
        
        clean_animal = new_animal.strip().capitalize()
        if not clean_animal:
            raise ValueError("Animal name cannot be empty or whitespace")
        
        if clean_animal not in self.animals:
            self.animals.append(clean_animal)
            logger.info(f"Added animal to {self.name}: {clean_animal}")
            # Clear cached groups since animals list changed
            self._groups.clear()
            return True
        else:
            logger.warning(f"Animal {clean_animal} already exists in {self.name}")
            return False
    
    def get_animals(self) -> List[str]:
        """
        Returns a copy of the animals list and prints it.
        
        Returns:
            A copy of the current animals list
        """
        animals_copy = self.animals.copy()
        print(f"Animals in {self.name}: {animals_copy}")
        logger.debug(f"Retrieved {len(animals_copy)} animals from {self.name}")
        return animals_copy
    
    def sell_animal(self, animal_sold: str) -> bool:
        """
        Removes an animal from the zoo.
        
        Args:
            animal_sold: Name of the animal to remove
            
        Returns:
            True if animal was removed, False if not found
            
        Raises:
            TypeError: If animal_sold is not a string
        """
        if not isinstance(animal_sold, str):
            raise TypeError(f"Animal name must be a string, got {type(animal_sold).__name__}")
        
        clean_animal = animal_sold.strip().capitalize()
        if clean_animal in self.animals:
            self.animals.remove(clean_animal)
            logger.info(f"Sold animal from {self.name}: {clean_animal}")
            # Clear cached groups since animals list changed
            self._groups.clear()
            return True
        else:
            logger.warning(f"Animal {clean_animal} not found in {self.name}")
            return False
    
    def sort_animals(self) -> dict[str, List[str]]:
        """
        Sorts animals alphabetically and groups them by first letter.
        
        Returns:
            Dictionary mapping first letters to lists of animals
        """
        # Sort animals alphabetically (case-insensitive)
        sorted_animals = sorted(self.animals, key=str.lower)
        self.animals = sorted_animals
        
        # Group by first letter
        groups: dict[str, List[str]] = {}
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        
        self._groups = groups
        logger.info(f"Sorted and grouped {len(sorted_animals)} animals into {len(groups)} groups")
        return groups.copy()
    
    def get_groups(self) -> dict[str, List[str]]:
        """
        Returns the current groupings and prints them.
        
        Returns:
            Dictionary of current animal groupings
            
        Note:
            If animals haven't been sorted yet, this will sort them first.
        """
        if not self._groups and self.animals:
            self.sort_animals()
        
        print(f"\nAnimal groups in {self.name}:")
        print("=" * (len(self.name) + 20))
        
        for letter in sorted(self._groups.keys()):
            animals_in_group = self._groups[letter]
            print(f"{letter}: {animals_in_group}")
        
        if not self._groups:
            print("No animals to group.")
        
        logger.debug(f"Retrieved {len(self._groups)} animal groups")
        return self._groups.copy()
    
    def get_animals_by_letter(self, letter: str) -> List[str]:
        """
        Gets all animals starting with a specific letter.
        
        Args:
            letter: The letter to search for
            
        Returns:
            List of animals starting with the given letter
        """
        if not self._groups and self.animals:
            self.sort_animals()
        
        letter_upper = letter.upper()
        return self._groups.get(letter_upper, []).copy()
    
    def get_zoo_statistics(self) -> dict[str, Any]:
        """
        Returns statistics about the zoo.
        
        Returns:
            Dictionary with various zoo statistics
        """
        if not self._groups and self.animals:
            self.sort_animals()
        
        stats = {
            "name": self.name,
            "total_animals": len(self.animals),
            "animal_types": len(set(self.animals)),  # Unique animals
            "letter_groups": len(self._groups),
            "animals_by_letter": {k: len(v) for k, v in self._groups.items()},
            "most_common_letter": max(self._groups.keys(), key=lambda k: len(self._groups[k])) if self._groups else None
        }
        
        return stats


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
