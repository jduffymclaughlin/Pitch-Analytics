from CardDeck import PitchDeck
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import time
import itertools
import multiprocessing 


start = time.time()

num_sims, pools = 100000, multiprocessing.cpu_count()
chunks = [(start, start + num_sims // pools) for start in range(pools)]

def sim(chunk):

    start, end = chunk
    game = list()

    for _ in range(start, end):

        deck = PitchDeck(printing=False)
        deck.shuffle()
        deck.deal()
        deck.bid()
        deck.exchange()

        gamePointsInPlay = 0
        for hand in deck.finalHands.values():
            for card in hand:
                gamePointsInPlay += card.gamePoints
        game.append(gamePointsInPlay)
        deck.done()

    return game

with multiprocessing.Pool(pools) as p:
    game_results = p.map(sim, chunks)

game_results = [inner for outer in game_results for inner in outer]

print("TOTAL TIME {}".format(time.time() - start))

df = pd.DataFrame(game_results, columns=['GamePointsInPlay'])
print(df.describe())
df.plot(kind='hist', bins=df.GamePointsInPlay.max() - df.GamePointsInPlay.min())
plt.show()

