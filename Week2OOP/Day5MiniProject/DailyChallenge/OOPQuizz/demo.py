
"""Tiny demo script to showcase the Deck API with friendly output."""
from deck import Deck

def main():
    deck = Deck()
    deck.shuffle()
    hand = deck.deal_many(5)
    print("🃏 Shuffled a fresh deck of 52 cards!")
    print("🖐️ Dealt a 5-card hand:")
    for c in hand:
        print(" -", c)
    print(f"📦 Cards left in deck: {len(deck)}")


if __name__ == "__main__":
    main()
