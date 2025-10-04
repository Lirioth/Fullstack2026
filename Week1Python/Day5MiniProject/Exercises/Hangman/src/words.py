"""
Word source for Hangman.
Feel free to expand WORDS. Phrases can include spaces/punctuations; letters get masked with '*', others remain visible.
"""
import random

WORDS = [
    'correction', 'childish', 'beach', 'python', 'assertive',
    'interference', 'complete', 'share', 'credit card', 'rush', 'south'
]

def random_word() -> str:
    """Return a random word/phrase from WORDS."""
    return random.choice(WORDS)
