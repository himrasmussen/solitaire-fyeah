import unittest


from deck import Deck, Card
from game import Stack, Choice, Table


class TestStack(unittest.TestCase):
    """Test the stack class."""

    def setUp(self):
        """Create a stack with a single card, and a stack with multiple cards."""
        self.card = Card('A', 'hearts')
        self.singlestack = Stack()
        self.bigstack = Stack()
        self.singlestack.cards.append(self.card)
        for i in range(10):
            self.bigstack.cards.append(self.card)

    def test_topcard_single(self):
        """ Test whether the topcard is in fact a card."""
        self.assertEqual(self.singlestack.topcard, self.card)

    def test_topcard_bigstack(self):
        """ Test whether the topcard is in fact a card."""
        self.assertEqual(self.bigstack.topcard, self.card)


class TestGame(unittest.TestCase):
    """Test the game clas."""

    def setUp(self):
        """Set up the test."""
        self.deck = Deck()
        self.table = Table(self.deck)
        self.choice = Choice()


    def test_get_movable_cards_new_game(self):
        """Test if get_moveable_cards gets all movable cards on a new game."""
        self.assertEqual(len(self.choice.get_moveable_cards(self.table)), 7)

    def test_get_movable_cards_with_stack(self):
        """Test if the function works with the stack."""
        self.table.stack.cards.append(Card('A', 'hearts'))
        self.assertEqual(len(self.choice.get_moveable_cards(self.table)), 8)

    def test_get_movable_cards_with_acestacks(self):
        """
        Test whether the function works with multiple cards in the acestacks.
        """
        for i in range(4):
            for acestack in self.table.acestacks.keys():
                self.table.acestacks[acestack].append(Card('A', 'hearts'))

        self.assertEqual(len(self.choice.get_moveable_cards(self.table)), 11)

    def test_get_movable_cards_with_multiple_cards_on_the_table(self):
        """Test if multiple face up cards on the table works."""
        for column in self.table.columns.values():
            column.append(Card('A', 'hearts'))
            print("1")
        self.assertEqual(len(self.choice.get_moveable_cards(self.table)), 19)
unittest.main()
