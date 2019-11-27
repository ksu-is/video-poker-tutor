def score_royal_flush(hand):
    # must be flush and a straight with a low card of 10
    rank_list = [card.rank for card in hand]
    is_flush = score_flush(hand)
    is_straight = score_straight(hand)
    if is_flush and is_straight:
        if min(rank_list) == 10:
            return True
    return False

def score_straight_flush(hand):
    # must be a straight and flush
    return score_straight(hand) and score_flush(hand)

def score_four_of_a_kind(hand):
    #must have four cards with the same rank
    rank_list = [card.rank for card in hand]
    rank_set = set(rank_list)
    counts = [rank_list.count(rank) for rank in rank_set]
    if 4 in counts:
        return True
    else:
        return False

def score_full_house(hand):
    rank_list = [card.rank for card in hand]
    rank_set = set(rank_list)
    counts = [rank_list.count(rank) for rank in rank_set]
    if (3 in counts) and (2 in counts):
        return True
    else:
        return False

def score_flush(hand):
    suit_list = [card.suit for card in hand]
    if len(set(suit_list)) == 1:
        return True

    return False

def score_straight(hand):
    # must contain 5 unique ranks with a difference of 4 between
    # max and min ranks. If one card is an ace, you must also check
    # the case where the ace is a 1
    rank_list = [card.rank for card in hand]
    rank_list.sort()

    unique_rank = len(set(rank_list))
    if unique_rank == 5:
        diff = max(rank_list) - min(rank_list)
        if diff == 4:
            return True
        elif 14 in rank_list:
            rank_list = [1 if rank == 14 else rank for rank in rank_list]
            diff = diff = max(rank_list) - min(rank_list)
            if diff == 4:
                return True

    return False

def score_three_of_a_kind(hand):
    rank_list = [card.rank for card in hand]
    rank_set = set(rank_list)
    counts = [rank_list.count(rank) for rank in rank_set]
    if 3 in counts:
        return True
    else:
        return False

def score_two_pair(hand):
    # must have three unique rank_sets
    # count of one rank set must equal 1, and then the other two must be two each

    rank_list = [card.rank for card in hand]
    rank_set = set(rank_list)
    if len(rank_set) == 3:
        counts = [rank_list.count(rank) for rank in rank_set]
        if 1 in counts:
            return True

    return False

def score_jacks_or_better(hand):
    # must be at least two high cards with the same rank
    high_cards = [card for card in hand if card.is_high]
    if len(high_cards) > 1:
        rank_list = [card.rank for card in high_cards]
        rank_set = set(rank_list)
        counts = [rank_list.count(rank) for rank in rank_set]
        if 2 in counts:
            return True

    return False

def score_hand(hand):
    if score_royal_flush(hand):
        return "Royal Flush"
    elif score_straight_flush(hand):
        return "Straight Flush"
    elif score_four_of_a_kind(hand):
        return "4 of a Kind"
    elif score_full_house(hand):
        return "Full House"
    elif score_flush(hand):
        return "Flush"
    elif score_straight(hand):
        return "Straight"
    elif score_three_of_a_kind(hand):
        return "3 of a Kind"
    elif score_two_pair(hand):
        return "2 Pair"
    elif score_jacks_or_better(hand):
        return "Jacks or Better"
    else:
        return "Not a Winning Hand"
