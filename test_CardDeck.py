import unittest
from CardDeck_np import PitchDeck, Card


class test_PitchDeck(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(test_PitchDeck, self).__init__(*args, **kwargs)

        obj = PitchDeck(printing=False)
        self.orig_deck = list(obj.deck.copy())

        obj.shuffle()
        self.deck_after_shuffle = list(obj.deck.copy())

        obj.deal()
        self.orig_hands = obj.origHands.copy()

        obj.bid()
        self.bidding_trump = obj.trump

        obj.exchange()
        self.final_hands = obj.finalHands.copy()

        obj.done()
        self.deck_after_game = list(obj.deck.copy())

        self.known_cards = (
            Card('5', 'hearts'),
            Card('10', 'diamonds'),
            Card('Q', 'spades'),
            Card('A', 'spades'), 
            Card('2', 'clubs'),
        )
        self.suits = ('hearts', 'spades', 'diamonds', 'clubs')

    def test_shuffle(self):
        self.assertNotEqual(self.orig_deck, self.deck_after_shuffle)

    def test_known_cards(self):

        for card in self.known_cards:
            self.assertIn(card, self.orig_deck)
            self.assertIn(card, self.deck_after_shuffle)
            self.assertIn(card, self.deck_after_game) 
            

    def test_deck_size(self):

        self.assertEqual(len(self.orig_deck), 52)
        self.assertEqual(len(self.deck_after_shuffle), 52)
        self.assertEqual(len(self.deck_after_game), 52)

    def test_deck_uniqueness(self):

        self.assertEqual(len(set(self.orig_deck)), 52)
        self.assertEqual(len(set(self.deck_after_shuffle)), 52)
        self.assertEqual(len(set(self.deck_after_game)), 52)

    def test_deal(self):

        self.assertEqual(len(self.orig_hands.keys()), 4)

        for hand in self.orig_hands.values():
            self.assertEqual(len(hand), 6)

    def test_bid(self):

        self.assertIn(self.bidding_trump, self.suits)

    def test_exchange(self):

        self.assertEqual(len(self.final_hands.keys()), 4)

        for hand in self.final_hands.values():
            self.assertEqual(len(hand), 6)
    
    def test_gamePoints(self):

        total = 0
        for card in self.orig_deck:
            total += card.gamePoints
        self.assertEqual(total, 80)

        for card in self.deck_after_game:
            total += card.gamePoints
        self.assertEqual(total, 160)


if __name__ == '__main__':
    unittest.main()
