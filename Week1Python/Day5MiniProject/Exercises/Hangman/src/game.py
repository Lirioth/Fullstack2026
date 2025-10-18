"""
Hangman Game - Core Logic Module
=================================
Complete game state machine for Hangman.
Tracks guesses, wrong attempts, and masked representation.
Only letters are maskable ('*'); spaces/punctuation show as-is.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 5 - Mini Project
Python Version: 3.8+
"""
from typing import Set
from .art import HANGMAN, MAX_WRONG

def _is_letter(ch: str) -> bool:
    """Return True if ch is an ASCII letter (a-z)."""
    return len(ch) == 1 and ch.isalpha()

class HangmanGame:
    """
    Hangman game state machine.
    Attributes:
        secret (str): The target word/phrase (kept lowercase internally).
        guessed (Set[str]): Letters guessed so far (lowercase).
        wrong (int): Number of incorrect guesses.
    """
    def __init__(self, secret: str):
        self.secret = secret.lower()
        self.guessed: Set[str] = set()
        self.wrong = 0

    @property
    def max_wrong(self) -> int:
        return MAX_WRONG

    def masked(self) -> str:
        """
        Return a view of the secret with letters replaced by '*'
        unless they've been guessed. Non-letters (spaces, hyphens, etc.)
        are shown as-is.
        """
        out_chars = []
        for ch in self.secret:
            if ch.isalpha():
                out_chars.append(ch if ch in self.guessed else '*')
            else:
                out_chars.append(ch)  # keep spaces/punctuation visible
        return ''.join(out_chars)

    def already_complete(self) -> bool:
        """Return True if there are no '*' remaining (win state)."""
        return '*' not in self.masked()

    def guess(self, ch: str) -> str:
        """
        Process a single-letter guess.
        Returns a status string: 'repeat', 'hit', or 'miss'.
        Raises ValueError for invalid inputs (not a single A–Z letter).
        """
        ch = ch.lower().strip()
        if not _is_letter(ch):
            raise ValueError("Please enter a single letter (A–Z).")
        if ch in self.guessed:
            return 'repeat'
        self.guessed.add(ch)
        if ch in self.secret:
            return 'hit'
        self.wrong += 1
        return 'miss'

    def is_won(self) -> bool:
        return self.already_complete()

    def is_lost(self) -> bool:
        return self.wrong >= self.max_wrong

    def is_over(self) -> bool:
        return self.is_won() or self.is_lost()

    def gallows(self) -> str:
        """Return ASCII gallows for current wrong count."""
        idx = min(self.wrong, self.max_wrong)
        return HANGMAN[idx]

    def guessed_letters(self) -> str:
        """Return a sorted string of guessed letters (for display)."""
        return ' '.join(sorted(self.guessed))

    def __repr__(self) -> str:
        """Return developer-friendly representation for debugging."""
        return (
            f"HangmanGame(secret={'*' * len(self.secret)}, "
            f"wrong={self.wrong}/{self.max_wrong}, "
            f"guessed={len(self.guessed)} letters)"
        )
