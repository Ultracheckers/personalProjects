from deck import Deck


class Player:
    def __init__(self, isDealer):
        self.isDealer = isDealer
        self.deck = []
        self.points = 0

    def drawCard(self, deck):
        card = deck.drawCard()
        self.deck.append(card)
        return

    def getTotal(self):
        total = 0
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                  '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        for i in self.deck:
            total += values[i]
        return total
