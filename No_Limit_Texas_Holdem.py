import random
import Deck, Player

class RunGame:
    def __init__(self, players):
        # Initialise the deck, list of players, pot and community cards
        self.deck = Deck()
        self.players = players
        self.pot = 0
        self.community_cards = []

    def start_game(self):
        # Shuffle the deck and deal each player their 2 hole cards
        self.deck.shuffle()
        for player in self.players:
            player.receive_cards(self.deck.deal(2))
        
        print("Starting Hands:")
        for player in self.players:
            print(f"{player.name}: {player.show_hand()}")

    def flop(self):
        # Deal 3 cards for the flop
        self.community_cards.extend(self.deck.deal(3))
        print(f"Flop: {self.community_cards}")

    def turn(self):
        # Deal 1 card for the turn
        self.community_cards.extend(self.deck.deal(1))
        print(f"Turn: {self.community_cards[-1]}")

    def river(self):
        # Deal 1 card for the ruver
        self.community_cards.extend(self.deck.deal(1))
        print(f"River: {self.community_cards[-1]}")

    def betting_round(self):
        # Simplified betting logic
        for player in self.players:
            bet_amount = min(player.chips, 10)  # Example bet logic
            self.pot += player.bet(bet_amount)
            print(f"{player.name} bets {bet_amount}. Remaining chips: {player.chips}")

    def determine_winner(self):
        # Placeholder logic: can implement actual hand rankings
        winner = random.choice(self.players)
        winner.chips += self.pot
        print(f"{winner.name} wins the pot of {self.pot} chips!")
        self.pot = 0
