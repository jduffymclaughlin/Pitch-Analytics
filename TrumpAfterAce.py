from CardDeck import PitchDeck
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm


allResults = list()
soloAce = list()


for _ in tqdm(range(10)):

    deck = PitchDeck(printing=True)

    deck.shuffle()
    deck.deal()
    deck.bid()
    hands = deck.origHands

       
    deck.exchange()
    hands = deck.finalHands

    if len(deck.cardsKept[deck.winning_player]) == 1 and deck.cardsKept[deck.winning_player][0].rank == 'A':
        allResults.append(1)
        
        ace = deck.cardsKept[deck.winning_player][0]
        numNewTrump = 0

        for card in hands[deck.winning_player]:
            if card.suit == ace.suit and card != ace:
                numNewTrump += 1
        soloAce.append(numNewTrump)
    else:
        allResults.append(0)


print('Solo-Ace bid {}% of the time'.format(sum(allResults) / len(allResults)))
print('Liklihood of at least one new trump {}'.format(sum([1 for i in soloAce if i > 0]) / len(soloAce)))

df = pd.DataFrame(soloAce, columns=['TrumpAfterSoloAce'])
print(df.describe())

df.plot(kind='hist', bins=5)
plt.show()
