from deck import CardDeck

# get the deck
deck = CardDeck()
deck.shuffle()
clean_deck = deck.cards

player_list = {}
table = []
temporary_stack = []

# get player count
# player_count = input("Player count: ")

while True:
    try:
        player_count = int(input("How many players? "))
        if player_count not in range(1,10):
            print("Invalid input. Please select no more than 9 players")
            continue
        else:
            break
    except (TypeError, ValueError):
        print("Invalid input. Please enter an integer.")
        continue

# how many cards per player?
cards_per_player = len(clean_deck) // player_count

# divide cards amongst players
for player in range(player_count):
    player_list[f"player_{player + 1}"] = clean_deck[:cards_per_player]
    clean_deck = clean_deck[cards_per_player:]

# print(player_list)


# draw a card for each player and put them in the table list




# # rather
# while len(player_list) != 1:
#     # run the program
# # announce winner:
# for key, value in player_list:
#     print(f"{key} wins!")
    
              

# Each player draws a card if he has, if not, he is removed.
def draw_cards():
    for player_key, player_cards in player_list.items():
        if player_cards:
            removed_card = player_cards.pop(0)
            table.append(removed_card)
        else:
            player_list.pop(player_key)
            print(f"{player_key} is out of cards")

   
# Evaluate cards on the table:
            



def evaulate_table():
    for index, card in table:
        max_value = max(table)
        max_count = table.count(max_value)


while max_count != 1: ??
    if max_count > 1: ???
        # temporarily store the current cards in a stack
        temp_stack = temp_stack + table
        table = []
        # draw 2 cards from each player, and evaluate their last drawn cards between each other.
        draw_cards()
        temp_stack = temp_stack + table
        table = []
        draw_cards()
    # no war
    else:
        ...
        #add all the cards from the table to the player who had the highest card.
    



#compare the cards on the table



