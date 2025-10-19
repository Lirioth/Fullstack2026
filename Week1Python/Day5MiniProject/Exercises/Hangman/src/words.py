"""Module: words
Purpose: Provide Hangman word bank and random selection helper.
Author: Kevin Cusnir 'Lirioth'
Created: 2025-10-18
Last Updated: 2025-10-19

Overview:
    - ``WORDS`` constant storing candidate words and phrases
    - ``random_word`` helper returning one entry at random
"""

from __future__ import annotations

import random

WORDS = [
    'correction', 'childish', 'beach', 'python', 'assertive',
    'interference', 'complete', 'share', 'credit card', 'rush', 'south'
]

def random_word() -> str:
    """Return a random word/phrase from WORDS."""
    return random.choice(WORDS)
