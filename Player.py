class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []

    def bet(self, amount):
        if amount > self.chips:
            raise ValueError("Not enough chips!")
        self.chips -= amount
        return amount

    def receive_cards(self, cards):
        self.hand.extend(cards)
    