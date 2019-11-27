class Card():
    def __init__(self, card_str):
        rank_dict = {
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'T':10,
            'J':11,
            'Q':12,
            'K':13,
            'A':14,
        }

        self.suit = card_str[1]
        self.rank = rank_dict[card_str[0]]
        if self.rank > 10:
            self.is_high = True
        else:
            self.is_high = False

    def __str__(self):
        if self.rank < 10:
            rank_str = str(self.rank)
        else:
            rank_dict = {
                10:'T',
                11:'J',
                12:'Q',
                13:'K',
                14:'A'
            }
            rank_str = rank_dict[self.rank]

        return rank_str + self.suit

    def get_name(self):
        return __str__(self)
