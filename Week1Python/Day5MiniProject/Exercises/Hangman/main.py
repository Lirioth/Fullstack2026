"""
Hangman Game - CLI Runner
=========================
Interactive word guessing game with ASCII art visualization.
Picks a random word and loops for user guesses until win/lose.
Prevents repeating guesses and displays gallows status each turn.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 5 - Mini Project
Python Version: 3.8+
"""
from src.words import random_word
from src.game import HangmanGame

def prompt_guess() -> str:
    """Prompt for a single-letter guess (stripped)."""
    return input("Enter a letter: ").strip()

def main():
    print("=== HANGMAN 🪢 — Guess the word! ===\n")
    while True:
        secret = random_word()
        game = HangmanGame(secret)
        # Show initial masked word
        print(game.gallows())
        print("Word:", game.masked())
        print("Lives:", game.max_wrong - game.wrong)
        print()

        while not game.is_over():
            try:
                g = prompt_guess()
                status = game.guess(g)
                if status == 'repeat':
                    print(f"You already guessed '{g.lower()}'. Try a different letter.")
                elif status == 'hit':
                    print("✅ Hit!")
                else:
                    print("❌ Miss!")
            except ValueError as e:
                print("Input error:", e)

            print(game.gallows())
            print("Word: ", game.masked())
            print("Guessed:", game.guessed_letters() or "(none)")
            print("Lives:", game.max_wrong - game.wrong)
            print()

        if game.is_won():
            print("🎉 You win! The word/phrase was:", secret)
        else:
            print("💀 You lost! The word/phrase was:", secret)

        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing. Bye!")
            break

if __name__ == "__main__":
    main()
