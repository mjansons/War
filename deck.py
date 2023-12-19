import random

class CardDeck:
    def __init__(self):
        self.suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
        self.cards = [(rank, suit) for suit in self.suits for rank in range(2,15)]

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards
    
if __name__ == "__main__":
    deck = CardDeck().shuffle()
    print(deck)



