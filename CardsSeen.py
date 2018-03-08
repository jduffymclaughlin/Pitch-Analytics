from CardDeck import PitchDeck
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
from multiprocessing import Pool
import numpy as np
import time

start = time.time()
cards_seen = []
num_sims = 1000000
chunks = [(0, num_sims // 4), 
          (1 + num_sims // 4, num_sims // 2), 
          (1 + num_sims // 2, 3 * num_sims // 4), 
          (1 + 3 * num_sims // 4, num_sims)]

def sim(chunk):
    start, end = chunk

    results = list()
    for _ in range(start, end + 1):
        deck = PitchDeck(printing=False)

        deck.shuffle()
        deck.deal()
        deck.bid()
        deck.exchange()

        results.append(52 - len(deck.deck))
    print(results)
    return results


with Pool(4) as p:
    cards_seen = p.map(sim, chunks)

cards_seen = [s for c in cards_seen for s in c]
print("TOTAL TIME {}".format(time.time() - start))

df = pd.DataFrame(cards_seen, columns=['CardsSeen'])
print(df.describe())
df.plot(kind='hist', bins=5)
plt.show()

