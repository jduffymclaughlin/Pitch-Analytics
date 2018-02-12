import random
from collections import deque

class Card:

    gamePointValues = {'A': 4, 
                'K': 3, 
                'Q': 2, 
                'J': 1,
                '10': 10
                }

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.gamePoints = self.gamePointValues[self.rank] if self.rank in self.gamePointValues else 0

    def __repr__(self):
        return self.rank + "_" + self.suit


class PitchDeck:

    suits = ('spades', 'diamonds', 'hearts', 'clubs')
    ranks = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')

    def __init__(self, printing=False):

        self.deck = deque([Card(r, s) for r in self.ranks for s in self.suits])
        self.trump = random.choice(self.suits)
        self.printing = printing

    def shuffle(self):
        random.shuffle(self.deck)

    def print_hands(self, hands):
        if self.printing:
            for player, hand in hands.items():
                print('Player ' + str(player) + "  " + str(hand))

    def deal(self):
        self.origHands = {n: [self.deck.popleft() for _ in range(6)] for n in range(4)}
        self.print_hands(self.origHands)

    def bid(self):
        self.trump = random.choice(self.suits)

    def exchange(self):

        self.finalHands = dict()
        for i, hand in self.origHands.items():
            self.finalHands[i] = []
            for card in hand:
                if card.suit == self.trump:
                    self.finalHands[i].append(card)
            if self.printing:
                print(i, self.finalHands[i])
            while len(self.finalHands[i]) < 6:
                self.finalHands[i].append(self.deck.popleft())
        
        self.print_hands(self.finalHands)
        


