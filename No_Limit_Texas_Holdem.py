import random

# Determine player positions for next hand
def determine_positions(no_of_players, hands_played, positions):
    if hands_played == 0:
        if no_of_players == 2:
            Small_Blind = 0
            Big_Blind = 1

            positions[0] = "BB"
            positions[1] = "SB"
        else:
            Dealer = 0
            Small_Blind = 1
            Big_Blind = 2

            positions[0] = "D"
            positions[1] = "SB"
            positions[2] = "BB"

    else:
        Small_Blind = (hands_played + 1) % no_of_players
        Big_Blind = (hands_played + 2) % no_of_players

        positions[Small_Blind] = "SB"
        positions[Big_Blind] = "BB"

        if no_of_players > 2:
            Dealer = hands_played % no_of_players
            positions[Dealer] = "D"

        if no_of_players > 3:
            positions[(hands_played - 1) % no_of_players] = None

    return [Small_Blind, Big_Blind]

# Deal out the cards
def deal_cards(no_of_players, hands_played, deck_of_cards):
    hands = [["", ""] for _ in range(no_of_players)]
    for i in range(2):
        for j in range(no_of_players):
            card_chosen = random.choice(deck_of_cards)

            # Dealing out cards, in order of SB, BB, ..., D
            hands[(hands_played + j + 1) % no_of_players][i] = card_chosen
            deck_of_cards.remove(card_chosen)
    
    return hands

def player_to_act_preflop(no_of_players, key_positions):
    # Players make decisions in order of UTG to BB
    if no_of_players == 2:
        player_to_act = key_positions[0]

    elif no_of_players == 3:
        player_to_act = key_positions[0] - 1
            
    else:
        player_to_act = key_positions[1] + 1

    return player_to_act

def make_decision(hands, player_to_act, no_of_players, highest_bet, preflop, folded, chips):
    # Find player to act if players have folded
    while folded[player_to_act]:
        player_to_act = (player_to_act + 1) % no_of_players

    print(f"Player {player_to_act}, your hand is {hands[player_to_act]} and you have {chips[player_to_act]} chips")

    if preflop or highest_bet > 0:
        action = input("Would you like to fold, call or raise? ")
    else:
        action = input("Would you like to bet or check? ")
    
    while action not in ["fold", "call", "raise", "check", "bet"]:
        print("That is an invalid action, try again")
        action = make_decision(hands, player_to_act, no_of_players, highest_bet, preflop, folded, chips)

    return action

def preflop_action(no_of_players, hands, player_to_act, highest_bet, preflop, folded, chips, money_in_pot):
    extra_chips = 0
    
    for i in range(no_of_players):
        player_to_act = (player_to_act + i) % no_of_players
        action = make_decision(hands, player_to_act, no_of_players, highest_bet, preflop, folded, chips)

        if action == "fold":
            folded[player_to_act] = True
            
        elif action == "call":
            call_amount = highest_bet - money_in_pot[player_to_act]

            if call_amount > chips[player_to_act]:
                call_amount = chips[player_to_act]

            extra_chips += call_amount
            money_in_pot[player_to_act] = highest_bet
            
        elif action == "raise":
            raise_amount = int(input("How much would you like to raise to? "))

            if raise_amount > chips[player_to_act]:
                print("Cannot raise to more than you have, assumed all in")
                raise_amount = chips[player_to_act]

            highest_bet = raise_amount
            money_in_pot[player_to_act] += raise_amount

        else:
            print("Cannot do that action preflop")
            preflop_action(no_of_players, hands, player_to_act, highest_bet, preflop, folded, chips, money_in_pot)
            break

    return extra_chips

def main():
    # Welcome player
    print("Welcome to Check's Pokerhouse!")

    hands_played = 0

    # Keep playing hands until one player left
    while True:
        no_of_players = int(input("Please type in how many players you want in your poker game: "))

        # Must be at least 2 players
        if no_of_players <= 1:
            print("Not a valid number of players, try again")
        else:
            break
    
    starting_stack = int(input("How many chips do you want everyone to start with? "))
    chips = [starting_stack for _ in range(no_of_players)]

    print("Ok gentlemen, the game is No Limit Texas Holdem, the blinds are 1/2, good luck everyone!")

    while True:
        deck_of_cards = ["Ac", "Ad", "Ah", "As", "Kc", "Kd", "Kh", "Ks", "Qc", "Qd", "Qh", "Qs", 
                        "Jc", "Jd", "Jh", "Js", "10c", "10d", "10h", "10s", "9c", "9d", "9h", "9s",
                        "8c", "8d", "8h", "8s", "7c", "7d", "7h", "7s", "6c", "6d", "6h", "6s",
                        "5c", "5d", "5h", "5s", "4c", "4d", "4h", "4s", "3c", "3d", "3h", "3s",
                        "2c", "2d", "2h", "2s"]
        
        positions = [None for _ in range(no_of_players)]
        folded = [False for _ in range(no_of_players)]
        money_in_pot = [0 for _ in range(no_of_players)]
        preflop = True

        # key_positions = [SB, BB] - Dealer = SB - 1, and UTG = BB + 1
        key_positions = determine_positions(no_of_players, hands_played, positions)
        Small_Blind = key_positions[0]
        Big_Blind = key_positions[1]
        hands = deal_cards(no_of_players, hands_played, deck_of_cards)

        # Taking blinds
        money_in_pot[Small_Blind] += 1
        money_in_pot[Big_Blind] += 2

        highest_bet = 2
        pot = 3

        # Start with preflop action
        player_to_act = player_to_act_preflop(no_of_players, key_positions) 
        extra_chips = preflop_action(no_of_players, hands, player_to_act, highest_bet, preflop, folded, chips, money_in_pot)

        pot += extra_chips

        # For testing purposes
        print("Finished the hand!")

        hands_played += 1
    
if __name__ == "__main__":
    main()