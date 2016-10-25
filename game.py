"""The game of solitaire."""

from collections import OrderedDict

from deck import Deck, Card

class Stack():
    """A model representing the stack."""

    def __init__(self):
        """Initialize the stack."""
        self.cards = []

    @property
    def topcard(self):
        """This is the stack's top card.."""
        try:
            return self.cards[-1]
        except IndexError:
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
            except IndexError:
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

class Game():
    """Representing the game."""

    def __init__(self):
        """This does nothing. Comment anyway"""
        self.fuck = 0

    def get_choice(self, draw=True):
        """
        Get choice from player. Either 'draw'  or a [move_card]
        and [destination_card].
        """

        self.choice = ''
        while not self.choice in self.get_moveable_cards():
            self.choice = input("Draw or select card to move: ").lower().strip() ## REFACTOR
            if self.choice not 'draw':
                temp_card = self.choice.split()
                self.move_from = Card(temp_card[0], temp_card[1])

                self.move_to = ''
                while self.move_to not in self.get_movable_cards(): ## REFACTOR
                    self.move_to = input("Enter destination: ")
                    self.temp_card = self.move_to.split()
                    try:
                        self.move_to = Card(temp_card[0], temp_card[1])
                    except IndexError:
                        print("Index error.")
                        continue



    def get_moveable_cards(self, table):
        """Generate all movable cards (all open cards in the columns and
        all the stack's top cards.
        """

        self.movable_cards = []
        for stack in table.acestacks.values():
            try:
                self.movable_cards.append(stack[-1])
            except IndexError:
                pass
        if table.stack.topcard:
            self.movable_cards.append(table.stack.topcard)

        for column in table.columns.values():
            for card in column:
                if card.orientation == 'up':
                    self.movable_cards.append(card)

        return self.movable_cards
