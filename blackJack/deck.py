import random
from card import Card


class Deck:
    def __init__(self):
        self.deck = []

    def createDeck(self):
        values = ['2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K', 'A']
        suites = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        for suite in suites:
            for value in values:
                card = Card(value)
                self.deck.append(card)
        random.shuffle(self.deck)
