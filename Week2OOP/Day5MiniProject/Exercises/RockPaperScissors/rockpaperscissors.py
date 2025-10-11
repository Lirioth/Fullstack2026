"""
File: rockpaperscissors.py
Role: Menu/UI for Rock–Paper–Scissors. Handles loop, input, and score summary. 🖥️
"""

from __future__ import annotations

from typing import Dict
from game import Game


def get_user_menu_choice() -> str:
    """Show the menu and return 'p' (play), 's' (show scores), or 'q' (quit). 🧭"""
    print("\n=== Rock–Paper–Scissors ===")
    print("1) Play a new game 🎮")
    print("2) Show scores 📊")
    print("3) Quit 🚪")
    choice = input("Choose 1/2/3 (or p/s/q): ").strip().lower()
    mapping = {"1": "p", "2": "s", "3": "q", "p": "p", "s": "s", "q": "q"}
    picked = mapping.get(choice)
    if not picked:
        print("Invalid selection. Please choose 1, 2, or 3. ⚠️")
        return get_user_menu_choice()  # tail recursion is fine for small depth 🔁
    return picked


def print_results(results: Dict[str, int]) -> None:
    """Pretty-print the score dictionary. 🧾"""
    wins = results.get("win", 0)
    losses = results.get("loss", 0)
    draws = results.get("draw", 0)
    print("\n=== Final Results ===")
    print(f"Wins: {wins}  |  Losses: {losses}  |  Draws: {draws}")
    print("Thanks for playing! 🙏")


def main() -> None:
    results: Dict[str, int] = {"win": 0, "loss": 0, "draw": 0}
    while True:
        choice = get_user_menu_choice()
        if choice == "p":
            game = Game()
            outcome = game.play()
            results[outcome] += 1
        elif choice == "s":
            print_results(results)
        elif choice == "q":
            print_results(results)
            break


if __name__ == "__main__":
    main()
