"""
File: charactersgame.py
Role: Dungeons & Dragons quick character generator (4d6 drop lowest) with exports. 🎲🧙
Design: Character handles stat creation; Game manages N players and exporting (txt/json). 🧩
"""

from __future__ import annotations

import json, random
from dataclasses import dataclass, asdict
from typing import Dict, List


ABILITIES = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]  # 🧠💪


def roll_4d6_drop_lowest() -> int:
    """Roll four d6, drop the lowest, sum the rest. 🎲"""
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.sort(reverse=True)
    return sum(rolls[:3])


@dataclass
class Character:
    """A D&D character with six ability scores. 🧝‍♀️"""
    name: str
    age: int
    stats: Dict[str, int]

    @classmethod
    def create(cls, name: str, age: int) -> "Character":
        """Factory: roll six stats. 🏭"""
        stats = {ability: roll_4d6_drop_lowest() for ability in ABILITIES}
        return cls(name=name, age=age, stats=stats)

    def to_lines(self) -> List[str]:
        """Pretty lines for TXT export. 📝"""
        lines = [f"Name: {self.name}", f"Age: {self.age}"]
        for key in ABILITIES:
            lines.append(f"{key:13s}: {self.stats[key]}")
        return lines


@dataclass
class Game:
    """Game orchestrates player count, character creation, and exports. 🎮"""
    characters: List[Character]

    @classmethod
    def setup(cls) -> "Game":
        """Prompt for number of players, then create each character. 🙋"""
        try:
            n = int(input("How many players? ").strip())
        except Exception:
            print("⚠️ Invalid number. Defaulting to 1.")
            n = 1
        chars: List[Character] = []
        for i in range(1, max(1, n) + 1):
            name = input(f"Player {i} name: ").strip() or f"Player{i}"
            try:
                age = int(input(f"{name}'s age: ").strip())
            except Exception:
                print("⚠️ Invalid age. Using 18.")
                age = 18
            chars.append(Character.create(name, age))
        return cls(characters=chars)

    # ---------- Exports ----------
    def export_json(self, path: str = "characters.json") -> None:
        data = [asdict(ch) for ch in self.characters]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved JSON to {path}")

    def export_txt(self, path: str = "characters.txt") -> None:
        with open(path, "w", encoding="utf-8") as f:
            for i, ch in enumerate(self.characters, start=1):
                f.write(f"=== Character {i} ===\n")
                f.write("\n".join(ch.to_lines()))
                f.write("\n\n")
        print(f"✅ Saved TXT to {path}")


def main() -> None:
    try:
        game = Game.setup()
        game.export_json()
        game.export_txt()
    except (EOFError, KeyboardInterrupt):
        # Non-interactive fallback: create 2 sample characters
        print("\nNo interactive input detected. Creating sample characters. 🧪")
        game = Game(characters=[Character.create("Aria", 22), Character.create("Borin", 35)])
        game.export_json()
        game.export_txt()


if __name__ == "__main__":
    main()
