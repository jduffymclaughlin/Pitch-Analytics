from CardDeck import PitchDeck
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

cards_seen = []

for _ in tqdm(range(1000000)):
    deck = PitchDeck(printing=False)

    deck.shuffle()
    deck.deal()
    deck.bid()
    deck.exchange()

    cards_seen.append(52 - len(deck.deck))


df = pd.DataFrame(cards_seen, columns=['CardsSeen'])
print(df.describe())
df.plot(kind='hist', bins=5)
plt.show()


