"""The models for representing dekcs and cards."""

from random import shuffle

from card_funcs import get_color, get_value

class Card():
    """This is a card."""
    def __init__(self, rank, suit):
        """Initialize values for the card."""
        self.rank = rank
        self.suit = suit
        self.color = get_color(self.suit)
        self.value = get_value(self.rank)
        self.orientation = "up"

    def __str__(self):
        """The string representation of the card."""
        return self.rank + " " + self.suit


class Deck():
    """This is a deck."""



    def __init__(self):
        """Make the deck."""
        self.ranks = ['A'] + [str(x) for x in range(2, 11)] + list("JQK")
        self.suits = "hearts diamonds spades clubs".split())
        self.cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        """The length representation of the deck."""
        return len(self.cards)


    def shuffle(self):
        """Shuffles the deck."""
        shuffle(self.cards)

class PiquetDeck(Deck):
    """A piquet deck."""

    def __init__(self):
        """Initialize the deck. Cards 2 through 6 are removed."""

        self.ranks = ['A'] + [str(x) for x in range(7, 11)] + list('JQK')
        super().__init__()



deck = Deck().cards
piquetdeck = PiquetDeck().cards
for card in piquetdeck:
    print(card)
