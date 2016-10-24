"""Helper functions to make cards."""

def get_color(suit):
    """Return the color of a suit."""
    if suit in "hearts diamonds":
        color = 'red'
    elif suit in "spades clubs":
        color = 'black'
    return color

def get_value(rank):
    """Returns the value of a rank."""
    values = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
    if rank in values:
        value = values[rank]
    else:
        value = int(rank)
    return value
