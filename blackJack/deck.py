import random


class Deck:
    def __init__(self):
        self.deck = []
        self.createDeck()

    def createDeck(self):
        values = ['2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K', 'A']
        suites = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        for suite in suites:
            for card in values:
                self.deck.append(card)
        random.shuffle(self.deck)

    def drawCard(self):
        rCard = self.deck.pop()
        return rCard
