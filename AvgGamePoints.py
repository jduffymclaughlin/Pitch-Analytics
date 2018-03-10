from CardDeck import PitchDeck
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import time
from multiprocessing import Pool

start = time.time()
cards_seen = []
num_sims, pools = 1000000, 4
chunks = [(start, start + num_sims // pools) for start in range(0, num_sims, num_sims // pools)]

def sim(chunk):
    start, end = chunk
    game = list()

    for _ in range(start, end):
        deck = PitchDeck(printing=False)
        deck.shuffle()
        deck.deal()
        deck.bid()
        deck.exchange()
        hands = deck.finalHands

        gamePointsInPlay = 0
        for hand in hands.values():
            for card in hand:
                gamePointsInPlay += card.gamePoints
        game.append(gamePointsInPlay)
    return game

with Pool(pools) as p:
    game_results = p.map(sim, chunks)

game_results = [i for o in game_results for i in o]
print("TOTAL TIME {}".format(time.time() - start))

df = pd.DataFrame(game_results, columns=['GamePointsInPlay'])
print(df.describe())

df.plot(kind='hist', bins=30)
plt.show()

