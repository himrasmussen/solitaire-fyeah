"""The game of solitaire."""
from collections import OrderedDict

from deck import Deck

class Stack():
    """A model representing the stack."""

    def __init__(self):
        """Initialize the stack."""
        self.cards = []

    def topcard(self):
        """Returns the top card of the stack."""
        try:
            return self.cards[-1]
        except IndexError:
            print("Empty stack.")
            return None


class Table():
    """A class modelling the table."""

    def __init__(self, deck):
        """Initialize the rows and stacks."""
        self.stack = Stack()
        self.columns = {i: [] for i in range(7)} #?
        self.acestacks = OrderedDict()
        for suit in "hearts diamonds spades clubs".split():
            self.acestacks[suit] = []

        """Cast the solitaire."""
        for column in range(6, 0, -1):
            for row in range(column):
                self.columns[column].append(deck.cards.pop())
                self.columns[column][-1].orientation = 'down'
        for column in range(7):
            self.columns[column].append(deck.cards.pop())
            self.columns[column][-1].orientation = 'up'

    def view(self):
        """
        The string representation of the table.
        A nicely formatted table.
        """

        for suit, stack in self.acestacks.items():
            try:
                print('|' + stack[-1] + '|', end='')
            except:
                print('|' + suit.center(13) + '|', end='')
        print()
        max_column_len = max([len(column) for column in self.columns.values()])
        for column in range(6, -1, -1):
            for row in range(max_column_len):
                try:
                    print(self.columns[column][row], end='')
                except IndexError:
                    print(''.center(15), end='')
            print()
        print()
        try:
            print('|' + self.stack.cards[-1] + '|')
        except IndexError:
            print('|' + 'The Stack'.center(13) + '|')

deck = Deck(); deck.shuffle()
table = Table(deck)
table.view()
