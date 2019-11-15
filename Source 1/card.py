class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
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
