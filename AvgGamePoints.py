from CardDeck import PitchDeck
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
import time
from multiprocessing import Pool

start = time.time()
cards_seen = []
num_sims = 100000000
chunks = [(0, num_sims // 4), 
          (1 + num_sims // 4, num_sims // 2), 
          (1 + num_sims // 2, 3 * num_sims // 4), 
          (1 + 3 * num_sims // 4, num_sims-1)]

game_results = list()

def sim(chunk):
    start, end = chunk
    game = list()

    for _ in range(start, end + 1):

        deck = PitchDeck(printing=False)
        deck.shuffle()
        deck.deal()
        deck.bid()
        deck.exchange()
        hands = deck.finalHands

        gamePointsInPlay = 0
        for player, hand in hands.items():
            for card in hand:
                gamePointsInPlay += card.gamePoints
        game.append(gamePointsInPlay)
    return game

with Pool(4) as p:
    game_results = p.map(sim, chunks)

game_results = [i for o in game_results for i in o]
print("TOTAL TIME {}".format(time.time() - start))


df = pd.DataFrame(game_results, columns=['GamePointsInPlay'])
print(df.describe())

df.plot(kind='hist', bins=30)
plt.show()