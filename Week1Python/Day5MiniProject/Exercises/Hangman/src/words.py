"""
Hangman Game - Word Source Module
==================================
Word and phrase source for Hangman game.
Includes random word selection function.
Phrases can include spaces/punctuations; letters get masked with '*', others remain visible.

Author: Kevin Cusnir 'Lirioth'
Repository: Fullstack2026
Week 1 Day 5 - Mini Project
Python Version: 3.8+
"""
import random

WORDS = [
    'correction', 'childish', 'beach', 'python', 'assertive',
    'interference', 'complete', 'share', 'credit card', 'rush', 'south'
]

def random_word() -> str:
    """Return a random word/phrase from WORDS."""
    return random.choice(WORDS)
