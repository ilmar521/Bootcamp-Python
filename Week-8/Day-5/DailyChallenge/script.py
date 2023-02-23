
import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    def __init__(self):
        self.cards_in_deck = []

    def shuffle(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards_in_deck.clear()
        for x in suits:
            for y in values:
                self.cards_in_deck.append(Card(x, y))

    def deal(self):
        self.cards_in_deck.remove(random.choice(self.cards_in_deck))


new_deck = Deck()
new_deck.shuffle()
print(len(new_deck.cards_in_deck))
new_deck.deal()
print(len(new_deck.cards_in_deck))
