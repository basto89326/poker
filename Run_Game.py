from Poker_Game import RunGame
from Player import Player

# Game setup
print("Welcome to Check's Poker House!")
num_players = int(input("How many players would you like in the game? "))
num_chips = int(input("How many chips do you want each player to start with? "))
players = []

for player in range(num_players):
    name = input(f"Enter the name of Player {player + 1}: ")
    players.append(Player(name, num_chips))

poker_game = RunGame(players)

# Simulating game
poker_game.start_game()
poker_game.flop()
poker_game.betting_round()
poker_game.turn()
poker_game.betting_round()
poker_game.river()
poker_game.betting_round()
poker_game.determine_winner()
