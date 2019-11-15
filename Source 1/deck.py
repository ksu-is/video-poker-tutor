import random

from card import Card

class Deck():
    def __init__(self):
        self.cards = []
        for suit in ["H", "D", "S", "C"]:
            for rank in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
                self.cards.append(Card(suit, rank))

    def get_num_cards(self):
        return len(self.cards)

    def draw_card(self):
        random.shuffle(self.cards)
        return self.cards.pop()
