from CardDeck import PitchDeck
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
from multiprocessing import Pool
import numpy as np
import time

start = time.time()
cards_seen = []
num_sims, pools = 100000, 4
chunks = [(start, start + num_sims // pools) for start in range(0, num_sims, num_sims // pools)]

def sim(chunk):
    start, end = chunk

    results = list()
    for _ in range(start, end):
        deck = PitchDeck(printing=False)
        deck.shuffle()
        deck.deal()
        deck.bid()
        deck.exchange()

        results.append(52 - len(deck.deck))
    return results


with Pool(pools) as p:
    cards_seen = p.map(sim, chunks)

cards_seen = [s for c in cards_seen for s in c]
print("TOTAL TIME {}".format(time.time() - start))

df = pd.DataFrame(cards_seen, columns=['CardsSeen'])
print(df.describe())
df.plot(kind='hist', bins=5)
plt.show()

