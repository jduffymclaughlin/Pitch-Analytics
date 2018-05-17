from CardDeck import PitchDeck
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import time
from multiprocessing import Pool

start = time.time()
num_sims = 5

games = list()

for _ in range(num_sims):

    print('------- New Sim -------')
    deck = PitchDeck(printing=True)
    deck.shuffle()
    deck.deal()
    deck.bid()
    deck.exchange()

    gamePointsInPlay = 0
    for hand in deck.finalHands.values():
        for card in hand:
            gamePointsInPlay += card.gamePoints
    games.append(gamePointsInPlay)
    deck.done()
    

print("TOTAL TIME {}".format(time.time() - start))

df = pd.DataFrame(games, columns=['GamePointsInPlay'])
print(df.describe())
#df.plot(kind='hist', bins=30)
#plt.show()

