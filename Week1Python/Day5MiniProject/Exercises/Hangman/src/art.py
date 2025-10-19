"""Module: art
Purpose: Provide ASCII gallows and constants for Hangman feedback.
Author: Kevin Cusnir 'Lirioth'
Created: 2025-10-18
Last Updated: 2025-10-19

Overview:
     - ``HANGMAN`` list of 7 art frames
     - ``MAX_WRONG`` constant indicating the last index (game over)
"""

from __future__ import annotations
HANGMAN = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========="""
]
MAX_WRONG = len(HANGMAN) - 1  # 6
