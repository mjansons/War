from deck import CardDeck

# get the deck
deck = CardDeck()
deck.shuffle()
clean_deck = deck.cards

# get player count
# player_count = input("Player count: ")
player_count = 2

# get cards per player amount
cards_per_player = len(clean_deck) // player_count

player_list = {}

# divide cards
for player in range(player_count):
    player_list[f"player_{player + 1}"] = clean_deck[:cards_per_player]
    clean_deck = clean_deck[cards_per_player:]


print(player_list)






# result = 10 / /3
# print(result)