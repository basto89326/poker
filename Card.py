class Card:
    def __init__(self, rank, suit):
        # Each card is defined with a rank and a suit
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        # How each card is represented
        return f"{self.rank} of {self.suit}"
    