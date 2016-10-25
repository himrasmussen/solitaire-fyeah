"""The models for representing dekcs and cards."""

import random


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
        """The string representation of the card. Hides unturned cards."""
        if self.orientation == 'up':
            return '|' + (self.rank + " " + self.suit).center(13) + '|'
        else:
            return '|' + ''.center(13, '-') + '|'


class Deck():
    """This is a deck."""

    def __init__(self, ranks=None, shuffle=True):
        """Make the deck."""

        if not ranks:
            self.ranks = ['A'] + [str(x) for x in range(2, 11)] + list('JQK')
        else:
            self.ranks = ranks

        self.suits = "hearts diamonds spades clubs".split()
        self.cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
        if shuffle:
            random.shuffle(self.cards)

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
        self.piquet_ranks = ['A'] + [str(x) for x in range(6, 11)] + list('JQK')
        super().__init__(self.piquet_ranks)


if __name__ == "__main__":
    pass
