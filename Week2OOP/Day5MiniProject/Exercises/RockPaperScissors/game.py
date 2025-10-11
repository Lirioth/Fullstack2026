"""
File: game.py
Role: Core game logic for Rock–Paper–Scissors. 🎮🪨📄✂️
Note: This module prints minimal, user-facing info in play(); other methods are pure. ✅
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Literal


Item = Literal["rock", "paper", "scissors"]  # 🎯 precise type for clarity


EMOJI = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
}


def _normalize_choice(s: str) -> Item | None:
    """Normalize user text to an item or None if invalid. 🧼"""
    s = s.strip().lower()
    alias = {
        "r": "rock", "rock": "rock",
        "p": "paper", "paper": "paper",
        "s": "scissors", "scissor": "scissors", "scissors": "scissors",
    }
    value = alias.get(s)
    return value if value in {"rock", "paper", "scissors"} else None


@dataclass
class Game:
    """Single round of Rock–Paper–Scissors. One instance per play is fine. 🎲"""

    rng: random.Random = random.Random()  # inject for testability 🔁

    def get_user_item(self) -> Item:
        """Ask the user for their choice until valid. ⌨️"""
        while True:
            raw = input("Choose [r]ock, [p]aper, or [s]cissors: ")
            norm = _normalize_choice(raw)
            if norm:
                return norm
            print("Invalid choice. Please type r/p/s or rock/paper/scissors. ⚠️")

    def get_computer_item(self) -> Item:
        """Randomly select an item for the computer. 🎰"""
        return self.rng.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item: Item, computer_item: Item) -> Literal["win", "loss", "draw"]:
        """Decide outcome according to classic rules. ⚖️"""
        if user_item == computer_item:
            return "draw"
        wins_against = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }
        return "win" if wins_against[user_item] == computer_item else "loss"

    def play(self) -> Literal["win", "loss", "draw"]:
        """Run a round: ask user, roll computer, decide, print, and return result. ▶️"""
        user = self.get_user_item()
        comp = self.get_computer_item()
        result = self.get_game_result(user, comp)
        # Friendly output with emojis 🌈
        print(f"You chose {EMOJI[user]}  {user} | Computer chose {EMOJI[comp]}  {comp}")
        if result == "win":
            print("Result: You WIN! 🎉")
        elif result == "loss":
            print("Result: You LOSE. 😿")
        else:
            print("Result: It's a DRAW. 🤝")
        return result
