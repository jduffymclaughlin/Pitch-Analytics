from CardDeck import PitchDeck
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from multiprocessing import Pool
import time

start = time.time()
num_sims, pools = 1000000, 4
chunks = [(start, start + num_sims // pools) for start in range(0, num_sims, num_sims // pools)]

def sim(chunk):
    start, end = chunk

    allResults, soloAce = list(), list()
    for _ in range(start, end):

        deck = PitchDeck(printing=False)
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
    return allResults, soloAce

with Pool(pools) as p:
    results = p.map(sim, chunks)

all_results = [i for o in results for i in o[0]]
solo_ace = [i for o in results for i in o[1]]
print('TOTAL TIME {} SECONDS'.format(time.time() - start))

print('Solo-Ace bid {}% of the time'.format(sum(all_results) / len(all_results)))
print('Liklihood of at least one new trump {}'.format(sum([1 for i in solo_ace if i > 0]) / len(solo_ace)))

df = pd.DataFrame(solo_ace, columns=['TrumpAfterSoloAce'])
print(df.describe())

df.plot(kind='hist', bins=5)
plt.show()
