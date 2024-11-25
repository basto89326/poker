class Player:
    def __init__(self, name, chips):
        # Each player has a name, chip count and hand
        self.name = name
        self.chips = chips
        self.hand = []

    def bet(self, amount):
        # Function for when a player bets
        if amount > self.chips:
            raise ValueError("Not enough chips!")
        self.chips -= amount
        return amount

    def receive_cards(self, cards):
        # Player receives 2 hole cards
        self.hand.extend(cards)
    