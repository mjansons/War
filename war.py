ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["D", "S", "C", "H"]
deck = []

for rank in ranks:
    for suit in suits:
        card = (rank, suit)
        deck.append(card)

print(deck)