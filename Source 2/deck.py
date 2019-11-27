import random
from card import Card

class Deck():
    def __init__(self, exclude=None):
        self.cards = []
        cards_list = []
        for suit in ['H', 'D', 'S', 'C']:
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']:
                cards_list.append(rank+suit)
        if exclude != None:
            for card in exclude:
                cards_list.remove(card)

        for card in cards_list:
            self.cards.append(Card(card))

    def get_num_cards(self):
        return len(self.cards)

    def get_num_cards_above_rank_with_suit(self, rank, suit):
        return len([card for card in self.cards if card.rank >= rank and card.suit==suit])

    def get_cards_with_suit(self, suit):
        return [card for card in self.cards if card.suit == suit]

    def get_cards_with_rank(self, rank):
        return [card for card in self.cards if card.rank == rank]

    def draw_card(self):
        random.shuffle(self.cards)
        return self.cards.pop()

    def __str__(self):
        deck_str = ""
        for card in self.cards:
            deck_str = deck_str + str(card)+" "

        return deck_str
