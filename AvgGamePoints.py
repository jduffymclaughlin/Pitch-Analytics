from CardDeck import PitchDeck
import pandas as pd
import matplotlib.pyplot as plt

gameResults = []


for i in range(1000000):
    deck = PitchDeck(printing=False)
    deck.shuffle()
    hands = deck.bid_exchange()

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