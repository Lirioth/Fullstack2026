
import unittest
from deck import Deck, Card, SUITS, VALUES

class TestDeck(unittest.TestCase):
    def test_full_deck_has_52(self):
        d = Deck()
        self.assertEqual(len(d), 52)

    def test_shuffle_resets_and_randomizes(self):
        d = Deck()
        original = list(iter(d))
        d.deal()  # remove one
        d.shuffle()
        self.assertEqual(len(d), 52)
        self.assertNotEqual(original, list(iter(d)))  # highly likely to differ

    def test_deal_and_remove(self):
        d = Deck()
        d.shuffle()
        seen = set()
        for _ in range(52):
            c = d.deal()
            self.assertIsInstance(c, Card)
            seen.add((c.suit, c.value))
        self.assertEqual(len(seen), 52)
        with self.assertRaises(IndexError):
            d.deal()

    def test_deal_many(self):
        d = Deck()
        d.shuffle()
        hand = d.deal_many(5)
        self.assertEqual(len(hand), 5)
        self.assertEqual(len(d), 47)
        with self.assertRaises(IndexError):
            d.deal_many(100)

    def test_card_values(self):
        # Quick sanity: all cards in a new deck are valid
        d = Deck()
        for c in d:
            self.assertIn(c.suit, SUITS)
            self.assertIn(c.value, VALUES)

if __name__ == '__main__':
    unittest.main()
