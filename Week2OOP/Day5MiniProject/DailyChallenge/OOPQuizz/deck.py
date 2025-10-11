
"""
Module: deck_of_cards
Purpose: Simple Card and Deck classes with shuffle & deal, suitable for OOP practice.
Author: Kevin "Lirioth" Cusnir
Date: 2025-10-11 | TZ: Asia/Jerusalem
Notes: Minimal deps; comments in ENGLISH; emojis sparingly.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List
import random
import logging

# Configure basic logging (INFO by default). Use --log-level DEBUG in your scripts if you add argparse later.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Canonical suits/values as required by the exercise.
SUITS: tuple[str, ...] = ("Hearts", "Diamonds", "Clubs", "Spades")
VALUES: tuple[str, ...] = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")


@dataclass(frozen=True, slots=True)
class Card:
    """A single playing card.

    Args:
        suit: One of "Hearts", "Diamonds", "Clubs", "Spades".
        value: One of "A,2,3,4,5,6,7,8,9,10,J,Q,K".

    Example:
        >>> Card("Spades", "A")
        Card(suit='Spades', value='A')
    """
    suit: str
    value: str

    def __post_init__(self) -> None:
        # Validate inputs early to avoid invalid cards creeping in.
        if self.suit not in SUITS:
            raise ValueError(f"Invalid suit: {self.suit!r}. Allowed: {SUITS}")
        if self.value not in VALUES:
            raise ValueError(f"Invalid value: {self.value!r}. Allowed: {VALUES}")

    def __str__(self) -> str:
        # Human-friendly display like "A of Spades".
        return f"{self.value} of {self.suit}"


class Deck:
    """A standard 52-card deck with shuffle and deal operations.

    The deck does NOT inherit from Card (by design of the exercise).

    Public API:
        - shuffle(): rebuilds a full 52-card deck and shuffles it.
        - deal(): deals (removes) one card from the top of the deck.
        - deal_many(n): deals n cards safely.
        - __len__(): number of remaining cards.
        - __iter__(): iterate remaining cards.

    Example:
        >>> deck = Deck()
        >>> deck.shuffle()
        >>> len(deck)
        52
        >>> c = deck.deal()
        >>> isinstance(c, Card)
        True
        >>> len(deck)
        51
    """

    _cards: List[Card]

    def __init__(self) -> None:
        # Start with a fresh full deck.
        self._cards = self._build_full_deck()
        logger.debug("Initialized new deck with 52 cards.")

    @staticmethod
    def _build_full_deck() -> List[Card]:
        """Create a sorted list of all 52 unique cards."""
        return [Card(s, v) for s in SUITS for v in VALUES]

    def shuffle(self) -> None:
        """Reset to a full deck of 52 cards and shuffle randomly.

        This matches the requirement: "makes sure the deck of cards has all 52 cards
        and then rearranges them randomly."
        """
        self._cards = self._build_full_deck()
        random.shuffle(self._cards)
        logger.info("Deck reset and shuffled ✅")

    def deal(self) -> Card:
        """Deal a single card from the top of the deck.

        Returns:
            The dealt Card instance.

        Raises:
            IndexError: If the deck is empty.

        Example:
            >>> d = Deck(); d.shuffle()
            >>> card = d.deal()
            >>> isinstance(card, Card)
            True
        """
        if not self._cards:
            # Fail softly with a clear message.
            raise IndexError("Cannot deal from an empty deck ❌")
        card = self._cards.pop()
        logger.debug("Dealt %s", card)
        return card

    def deal_many(self, n: int) -> List[Card]:
        """Deal n cards safely.

        Args:
            n: Number of cards to deal (>= 0).

        Returns:
            A list of dealt cards, length exactly n.

        Raises:
            ValueError: If n is negative.
            IndexError: If there aren't enough cards to fulfill the request.

        Example:
            >>> d = Deck(); d.shuffle()
            >>> hand = d.deal_many(5)
            >>> len(hand)
            5
        """
        if n < 0:
            raise ValueError("n must be >= 0")
        if n > len(self._cards):
            raise IndexError(f"Not enough cards left: requested {n}, have {len(self._cards)}")
        # Pop from the end for efficiency.
        return [self._cards.pop() for _ in range(n)]

    def __len__(self) -> int:  # Allows len(deck)
        return len(self._cards)

    def __iter__(self) -> Iterable[Card]:
        # Iterate remaining cards without exposing internals.
        return iter(list(self._cards))  # shallow copy to avoid accidental mutation


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    print(f"Cards in deck: {len(deck)}")
    first_five = deck.deal_many(5)
    print("Your hand:", ", ".join(map(str, first_five)))
    print(f"Cards left: {len(deck)}")
