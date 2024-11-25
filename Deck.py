import random
import Card

class Deck:
    def __init__(self):
        # initialising the 52-card deck
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.cards = []

        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))
        
    def shuffle(self):
        # Shuffle the deck
        random.shuffle(self.cards)

    def deal(self, num_cards):
        # Deal the desired number of cards from the deck
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards
    