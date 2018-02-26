import random
from collections import deque
import numpy as np

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
        self.gamePoints = Card.gamePointValues[self.rank] if self.rank in Card.gamePointValues else 0

    def __repr__(self):
        return self.rank + "_" + self.suit


class PitchDeck:

    suits = ('spades', 'diamonds', 'hearts', 'clubs')
    ranks = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')

    def __init__(self, printing=False):

        self.deck = deque([Card(r, s) for r in PitchDeck.ranks for s in PitchDeck.suits])
        self.printing = printing

    def shuffle(self):
        random.shuffle(self.deck)

    def print_hands(self, hands):
        if self.printing:
            for player, hand in hands.items():
                print('Player ' + str(player) + " -  " + str(hand))
            print()

    def deal(self):
        self.origHands = {n: [self.deck.popleft() for _ in range(6)] for n in range(4)}
        self.print_hands(self.origHands)

    def hand_score(self):
        hand_scores = [0] * 4
        score_total = 0

        for player, hand in self.origHands.items():
            for card in hand:
                hand_scores[player] += card.gamePoints if card.rank != '10' else 0
            score_total += hand_scores[player]

        if score_total == 0:
            return [.25] * 4
        for i in range(len(hand_scores)):
            hand_scores[i] /= score_total
        return hand_scores

    def bid(self):
        
        self.winning_player = np.random.choice([0, 1, 2, 3], p=self.hand_score())

        best_card = self.origHands[self.winning_player][0]
        for card in self.origHands[self.winning_player]:
            if card.gamePoints > best_card.gamePoints and card.rank != '10':
                best_card = card
        self.trump = best_card.suit

        if self.printing:
            print("player " + str(self.winning_player) + " bids with best card " + str(best_card))
        

    def exchange(self):

        self.finalHands = dict()
        self.cardsKept = dict()

        for i, hand in self.origHands.items():
            self.finalHands[i] = list()
            for card in hand:
                if card.suit == self.trump:
                    self.finalHands[i].append(card)
            self.cardsKept[i] = list(self.finalHands[i])


            if self.printing:
                print(i, self.finalHands[i])
            while len(self.finalHands[i]) < 6:
                self.finalHands[i].append(self.deck.popleft())
        
        self.print_hands(self.finalHands)
        
