"""The Game."""

from deck import Deck
from game import Table, Choice

# Initialize deck and table
deck = Deck()
table = Table(deck)


# The main loop
while True:
    choice = game.get_choice()
    if choice == 'draw':
        game.draw()
    else:
        game.move(choice.from_card, choice.to_card)
        game.turn_cards()

    game.check_win_loss()
