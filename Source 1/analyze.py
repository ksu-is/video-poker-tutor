import score
from hand import Hand

def get_rank_count(hand):
    ranks = [card.rank for card in hand.cards]
    rank_count = dict()
    for rank in ranks:
        rank_count[rank] = rank_count.get(rank, 0) + 1

    return rank_count

def get_suit_count(hand):
    suits = [card.suit for card in hand.cards]
    suit_count = dict()
    for suit in suits:
        suit_count[suit] = suit_count.get(suit, 0) + 1

    return suit_count

def analyze_hand(hand):
    if score.score_royal_flush(hand):
        return hand

    elif score.score_straight_flush(hand):
        return hand

    elif score.score_four_of_a_kind(hand):
        rank_count = get_rank_count(hand)

        for key, count in rank_count.items():
            if count == 4:
                rank_to_keep = key

        return Hand([card for card in hand.cards if card.rank == rank_to_keep])

    elif four_to_royal(hand):
        suit_count = get_suit_count(hand)
        suit_to_keep = None
        for key, count in suit_count.items():
            if count == 4:
                suit_to_keep = key

        card_list = [card for card in hand.cards if card.suit == suit_to_keep]
        return Hand([card for card in card_list if (card.is_high or card.rank==10)])

    elif score.score_full_house(hand):
        return hand

    elif score.score_flush(hand):
        return hand

    elif score.score_three_of_a_kind(hand):
        rank_count = get_rank_count(hand)

        for key, count in rank_count.items():
            if count == 3:
                rank_to_keep = key

        return Hand([card for card in hand.cards if card.rank == rank_to_keep])

    elif score.score_straight(hand):
        return hand

    else:
        return Hand()

def four_to_royal(hand):
    # must have at least four cards of the same suit
    # if there are four cards of the same suit, they must all be high cards

    suit_count = get_suit_count(hand)
    suit_to_keep = None
    for key, count in suit_count.items():
        if count == 4:
            suit_to_keep = key

    cards_to_royal = []
    if suit_to_keep != None:
        card_list = [card for card in hand.cards if card.suit == suit_to_keep]
        cards_to_royal = [card for card in card_list if (card.is_high or card.rank==10)]

    print(len(cards_to_royal))

    if len(cards_to_royal) == 4:
        return True
    else:
        return False
