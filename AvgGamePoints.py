from CardDeck import PitchDeck
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
from tqdm import tqdm


gameResults = []

<<<<<<< HEAD
for i in tqdm(range(10000000)):
=======
for i in tqdm(range(1000000)):
>>>>>>> 6c374f7c76654a88fde61e8429bfad08968547bc

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
    gameResults.append(gamePointsInPlay)
    #print(gamePointsInPlay)

df = pd.DataFrame(gameResults, columns=['GamePointsInPlay'])
print(df.describe())

df.plot(kind='hist', bins=30)
plt.show()