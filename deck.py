import random

class CardDeck:
    def __init__(self):
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["♦", "♠", "♣", "♥"]
        self.cards = [(rank, suit) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards
    
if __name__ == "__main__":
    deck = CardDeck().shuffle()
    print(deck)



