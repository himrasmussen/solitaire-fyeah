import unittest

from players import Player, AI
from deck import Deck, Card
from game import Stack

class  TestPlayer(unittest.TestCase):
    """Test the Player class."""

    def setUp(self):
        """Create a player with id 0."""
        self.player = Player(0)

    def test_id(self):
        self.assertEqual(self.player.id, 0)


class TestAI(unittest.TestCase):
    """Test the AI class."""

    def setUp(self):
        """Create an AI with id 1."""
        self.ai = AI(1)

    def test_ai_id(self):
        self.assertEqual(self.ai.id, 1)

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
        self.assertEqual(self.singlestack.topcard(), self.card)

    def test_topcard_bigstack(self):
        """ Test whether the topcard is in fact a card."""
        self.assertEqual(self.bigstack.topcard(), self.card)

unittest.main()
