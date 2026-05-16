import random 
# called upon random to be used in later functions

def activate_spade_ability(card, winner, round_state):
  # helps identify the winning card to which ability will be played
  # Helps to continue the game if the winning card is not a spade
  if card.suite != "♠":
        return
    
    # Simplifies the card identification through numbers
    rank = card.orderID

    # attaches an ability to each card or rank
    if rank == 14:
      ace_ability(winner, round_state)
    elif rank == 13:
      king_ability(winner, round_state)
    elif rank == 12:
      queen_abilty(winner, round_state)
    elif rank == 11:
      jack_ability(winner, round_state)
    elif rank == 10:
      ten_ability(winner, round_state)
    elif rank == 9:
      nine_ability(winner, round_state)
    elif rank == 8:
      eight_ability(winner, round_state)
    elif rank == 7:
      seven_ability(winner, round_state)
    elif rank == 6:
      six_ability(winner, round_state)
    elif rank == 5:
      five_ability(winner, round_state)
    elif rank == 4:
      four_ability(winner, round_state)
    elif rank == 3:
      three_ability(winner, round_state)
    elif rank == 2:
      two_ability(winner, round_state)

# -----------------------------------------------------------------------------
# Helper code functions
# -----------------------------------------------------------------------------

def get_partner(player):
    """
    Returns the partner of a player.
    Example:
    A1 <-> A2
    B1 <-> B2
    This is a helper function to be utilized when determining the following:
      - Whose deck are you going to view
      - Whose book are you going to take
      - Whose card are you going to trade
    """
    team = player[0]
    player_number = player[1]

    if player_number == "1":
        return team + "2"
    else:
        return team + "1"
      
def get_left_opponent(player):
    """
    Returns the left opponent according to the table order.
    This helper function is utilized in:
      - seven of spades
      
    Table order:
    A1 -> B1 -> A2 -> B2 -> A1
    """

    left_map = {
        "A1": "B1",
        "B1": "A2",
        "A2": "B2",
        "B2": "A1"
    }
    return left_map[player]
  
def get_right_opponent(player):
    """
    Returns the right opponent based on table order.
    This helper function is utilized in:
      - eight of spades
      
    Table order:
    A1 -> B1 -> A2 -> B2 -> A1
    """

    right_map = {
        "A1": "B2",
        "B1": "A1",
        "A2": "B1",
        "B2": "A2"
    }
    return right_map[player]
  
def get_opponents(player):
    """
    Returns both opponents.
    This helper function is utilized in:
      - king of spades
      - jack of spades
      - ten of spades
      - five of spades
      - three of spades
    """
    if player[0] == "A":
        return ["B1", "B2"]
    else:
        return ["A1", "A2"]

def choose_player_from_list(players, prompt):
    """
    Lets the user choose a player from a list.
    This helper function is utilized in:
      - king of spades
    """
    print(prompt)

    for i, player in enumerate(players):
        print(f"{i + 1}. {player}")

    while True:
        choice = input("Enter choice number: ")

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(players):
                return players[choice - 1]

        print("Invalid choice. Try again.")
      
def choose_card_from_hand(hand, prompt):
    """
    Let the player choose a card from a hand.
    This helper function is utilized in:
      - king of spades
    """

    print(prompt)

    for i, card in enumerate(hand):
        print(f"{i + 1}. {card}")

    while True:
        choice = input("Enter choice number: ")

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(hand):
                return hand[choice - 1]

        print("Invalid choice. Try again.")
      
# -----------------------------------------------------------------------------
# Abilities code functions
# -----------------------------------------------------------------------------

def ace_ability(winner, round_state):
    """
    Ace of Spades Ability:
    Choose any other spade ability to activate.
    """
    # identifies the winner of the round and what ability is now in place
    print("\nAce of Spades Ability Activated!")
    print(f"{winner} may choose any other spade ability.")

    # Through the use of a dictionary, the winner can select which ability they would like to take effect
    ability_options = {
        "2": ("2 - Give 1 book to partner", two_ability),
        "3": ("3 - Give 1 book to opponent", three_ability),
        "4": ("4 - Steal 1 book from partner", four_ability),
        "5": ("5 - Steal 1 book from opponent", five_ability),
        "6": ("6 - See partner's hand", six_ability),
        "7": ("7 - See left opponent's hand", seven_ability),
        "8": ("8 - See right opponent's hand", eight_ability),
        "9": ("9 - Trade random card with partner", nine_ability),
        "X": ("10 - Trade random card with opponent", ten_ability),
        "J": ("J - See both opponents' hands", jack_ability),
        "Q": ("Q - See everyone's hand", queen_ability),
        "K": ("K - See opponent's hand and trade chosen card", king_ability),
    }

    print("\nChoose an ability:")

    # The winner will be able to select the ability of their choosing through the use of keys on their laptop
    for key, value in ability_options.items():
        description = value[0]
        print(f"{key}. {description}")

    while True:
        choice = input("Enter ability choice: ").upper()

        #determines if the key that was pressed is valid
        if choice in ability_options:
            selected_description, selected_function = ability_options[choice]

            print(f"\nAce selected: {selected_description}")
            selected_function(winner, round_state)
            break
        
        # if they do not select a key that corresponds with the options above, then this is what will be sent
        print("Invalid choice. Try again.")

def king_ability(winner, round_state):
    """
    K♠ Ability:
    See an opponent's hand and trade one chosen card.
    """

  # Identifies the opponents of the winner
    opponents = get_opponents(winner)

    print("\nK of Spades Ability Activated!")
    print(f"{winner} may inspect an opponent's hand and trade one card.")

    # Choose an opponent between your left and right
    target = choose_player_from_list(
        opponents,
        "Choose an opponent:"
    )

    # identifies who the winner has selected as the opponent that they would like to view into their hand and trade a card 
    winner_hand = round_state.hands[winner]
    target_hand = round_state.hands[target]

    # The winner is now able to see the hand of the person they selected
    print(f"\n{target}'s hand:")
    for card in target_hand:
        print(card)

    # The winner selects the card that they would like to get rid of
    winner_card = choose_card_from_hand(
        winner_hand,
        f"\nChoose one of your cards to trade:"
    )
  
    # The winner selects the card that they would like to get
    target_card = choose_card_from_hand(
        target_hand,
        f"\nChoose one of {target}'s cards to take:"
    )

    # The exchange is complete
    winner_hand.remove(winner_card)
    target_hand.remove(target_card)

    winner_hand.append(target_card)
    target_hand.append(winner_card)

    print(f"\n{winner} traded away: {winner_card}")
    print(f"{winner} received: {target_card}")

    input("\nPress Enter to continue...")

def queen_ability(winner, round_state):
    """
    Q of Spades Ability:
    Winner sees everyone's hand.
    """
    
    print("\nQ♠ Ability Activated!")
    print(f"{winner} gets to see everyone's hand.")

    for player, hand in round_state.hands.items():
        print(f"\n{player}'s hand:")
        for card in hand:
            print(card)

    input("\nPress Enter to continue...")
def jack_ability(winner, round_state):
    """
    J of Spades Ability:
    Winner sees both opponents' hands.
    """

    opponents = get_opponents(winner)

    print("\nJ♠ Ability Activated!")
    print(f"{winner} gets to see both opponents' hands.")

    for opponent in opponents:
        print(f"\n{opponent}'s hand:")
        for card in round_state.hands[opponent]:
            print(card)

    input("\nPress Enter to continue...")
  
  
def ten_ability(winner, round_state):
    """
    10 of Spades Ability:
    Trade a random card with an opponent.
    """

    opponents = get_opponents(winner)

    print("\n10♠ Ability Activated!")
    print(f"{winner} must trade a random card with an opponent.")

    target = choose_player_from_list(opponents, "Choose an opponent to trade with:")

    winner_hand = round_state.hands[winner]
    target_hand = round_state.hands[target]

    if len(winner_hand) == 0 or len(target_hand) == 0:
        print("Trade could not occur because one player has no cards left.")
        input("\nPress Enter to continue...")
        return

    winner_card = random.choice(winner_hand)
    target_card = random.choice(target_hand)

    winner_hand.remove(winner_card)
    target_hand.remove(target_card)

    winner_hand.append(target_card)
    target_hand.append(winner_card)

    print(f"{winner} gave away: {winner_card}")
    print(f"{target} gave away: {target_card}")

    input("\nPress Enter to continue...")
  
def nine_ability(winner, round_state):
    """
    9 of Spades Ability:
    Trade a random card with your partner.
    """

    partner = get_partner(winner)

    print("\n9♠ Ability Activated!")
    print(f"{winner} trades a random card with partner {partner}.")

    winner_hand = round_state.hands[winner]
    partner_hand = round_state.hands[partner]

    # Safety check
    if len(winner_hand) == 0 or len(partner_hand) == 0:
        print("Trade could not occur because one player has no cards left.")
        input("\nPress Enter to continue...")
        return

    # Randomly select cards
    winner_card = random.choice(winner_hand)
    partner_card = random.choice(partner_hand)

    # Swap cards
    winner_hand.remove(winner_card)
    partner_hand.remove(partner_card)

    winner_hand.append(partner_card)
    partner_hand.append(winner_card)

    print(f"{winner} gave away: {winner_card}")
    print(f"{partner} gave away: {partner_card}")

    input("\nPress Enter to continue...")
  
def eight_ability(winner, round_state):
    """
    8 of Spades Ability:
    Winner sees their right opponent's hand.
    """

    right_opponent = get_right_opponent(winner)

    print("\n8♠ Ability Activated!")
    print(f"{winner} gets to see their right opponent's hand: {right_opponent}")

    print(f"\n{right_opponent}'s hand:")
    for card in round_state.hands[right_opponent]:
        print(card)

    input("\nPress Enter to continue...")
  
def seven_ability(winner, round_state):
    """
    7 of Spades Ability:
    Winner sees their left opponent's hand.
    """

    left_opponent = get_left_opponent(winner)

    print("\n7♠ Ability Activated!")
    print(f"{winner} gets to see their left opponent's hand: {left_opponent}")

    print(f"\n{left_opponent}'s hand:")
    for card in round_state.hands[left_opponent]:
        print(card)

    input("\nPress Enter to continue...")
  
def six_ability(winner, round_state):
    """
    6 of Spades Ability:
    Winner sees their partner's hand.
    """

    partner = get_partner(winner)

    print("\n6♠ Ability Activated!")
    print(f"{winner} gets to see their partner's hand: {partner}")

    print(f"\n{partner}'s hand:")
    for card in round_state.hands[partner]:
        print(card)

    input("\nPress Enter to continue...")
  
def five_ability(winner, round_state):
    """
    5 of Spades Ability:
    Steal 1 book from an opponent.
    """

    opponents = get_opponents(winner)

    print("\n5♠ Ability Activated!")
    print(f"{winner} steals 1 book from an opponent.")

    target = choose_player_from_list(opponents, "Choose an opponent to steal from:")

    if round_state.winnings[target] > 0:
        round_state.winnings[target] -= 1
        round_state.winnings[winner] += 1

        print(f"1 book transferred from {target} to {winner}.")
    else:
        print(f"{target} has no books to steal.")

    input("\nPress Enter to continue...")
  
def four_ability(winner, round_state):
    """
    4 of Spades Ability:
    Steal 1 book from partner.
    """

    partner = get_partner(winner)

    print("\n4♠ Ability Activated!")
    print(f"{winner} steals 1 book from their partner: {partner}")

    if round_state.winnings[partner] > 0:
        round_state.winnings[partner] -= 1
        round_state.winnings[winner] += 1

        print(f"1 book transferred from {partner} to {winner}.")
    else:
        print(f"{partner} has no books to steal.")

    input("\nPress Enter to continue...")

def three_ability(winner, round_state):
    """
    3 of Spades Ability:
    Give 1 book to an opponent.
    """

    opponents = get_opponents(winner)

    print("\n3♠ Ability Activated!")
    print(f"{winner} must give 1 book to an opponent.")

    target = choose_player_from_list(opponents, "Choose an opponent to receive the book:")

    if round_state.winnings[winner] > 0:
        round_state.winnings[winner] -= 1
        round_state.winnings[target] += 1

        print(f"1 book transferred from {winner} to {target}.")
    else:
        print(f"{winner} has no books to transfer.")

    input("\nPress Enter to continue...")

def two_ability(winner, round_state):
    """
    2 of Spades Ability:
    Give 1 book to partner.
    """

    partner = get_partner(winner)

    print("\n 2 of Spades Ability Activated!")
    print(f"{winner} gives 1 book to their partner: {partner}")

    # Transfer one book to partner
    if round_state.winnings[winner] > 0:
        round_state.winnings[winner] -= 1
        round_state.winnings[partner] += 1

        print(f"1 book transferred from {winner} to {partner}.")
    else:
        print(f"{winner} has no books to transfer.")

    input("\nPress Enter to continue...")

activate_spade_ability()
