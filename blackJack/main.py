from deck import Deck
from player import Player


def start(player, deck):
    for i in range(2):
        player.drawCard(deck)
    return


def main():
    player = Player(False)
    dealer = Player(True)
    deck = Deck()
    start(player, deck)
    start(dealer, deck)
    playerTotal = player.getTotal()
    print(playerTotal)


main()
