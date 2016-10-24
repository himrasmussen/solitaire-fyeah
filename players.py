"""This is the players module and everything player related is here."""

from ai_strategy import Strategy

class Player():
    """The player class."""

    def __init__(self, id=None):
        """Initialize player attributes."""
        if id is None:
            raise ValueError("Player doesn't have id.")

        self.hand = []
        self.id = id

    def draw(self, deck):
        """Simulate drawing a card."""

        print("Player {0} draws a card.".format(self.id))


class  AI(Player):
    """The AI class."""

    def __init__(self, id):
        """Initialize the ai."""
        super().__init__(id)
        self.strategy = Strategy()


if __name__ == '__main__':
    ai = AI(1)
    print(ai.id)
