import score
from deck import Deck

def get_rank_count(hand):
    '''
    Helper function for getting counts of each rank present in
    a hand. Returns a dictionary of counts.
    '''
    ranks = [card.rank for card in hand]
    rank_count = dict()
    for rank in ranks:
        rank_count[rank] = rank_count.get(rank, 0) + 1

    return rank_count

def get_suit_count(hand):
    '''
    Helper function for getting counts of each suit present in
    a hand. Returns a dictionary of counts.
    '''
    suits = [card.suit for card in hand]
    suit_count = dict()
    for suit in suits:
        suit_count[suit] = suit_count.get(suit, 0) + 1

    return suit_count

def choose_iter(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next

def choose(l, k):
    return list(choose_iter(l, k))

def get_plays(num_cards):
    '''
    Helper function for getting a list of possible cards to hold. For now,
    this assumes a hand contains 5 cards, but this could be updated in the
    future to work with hands of arbitrary sizes.

    Returns a list of lists. Each inner list is a number indicating which card position
    in the hand should be held. Card positions are labeled 0 through 4. An empty list
    means discard all cards in the hand.
    '''

    # Create the list of possible choices from the number of cards
    choice_list = [num for num in range(num_cards)]

    # Create the initial list of possible plays. Add the option of keeping none
    list_of_plays = [(),]

    # Loop over all the options for holding n number of cards and append the
    # plays to the list of plays options

    for n in range(num_cards+1):
        plays = choose(choice_list, n)
        for play in plays:
            list_of_plays.append(play)

    return list_of_plays

def cards_have_same_suit(cards_list):
    '''
    Helper function to determine if a list of cards all have the
    same suit
    '''
    suit_set = set([card.suit for card in cards_list])
    # If suit set has length 1 or less, the set is either empty or has cards
    # of all the same suit.

    if len(suit_set) <= 1:
        return True
    else:
        return False

def get_royal_flush_prob(held_cards, deck):
    '''
    Calculate the probability of getting royal flush based on the current
    cards in a hand along with the cards remaining in the deck.
    '''
    rank_list = [card.rank for card in held_cards]

    if len(held_cards)==5:
        # if all cards are held, check if the hand is a royal. If it is, return 1
        # otherwise return 0
        if score.score_royal_flush(held_cards):
            return 1
        else:
            return 0
    elif len(held_cards)==0:
        # if no cards are held, get the probability of a royal flush from
        # the remaining deck

        #get the suits that still have a full complement of high cards
        suit_list = []
        for suit in ['C', 'D', 'H', 'S']:
            if deck.get_num_cards_above_rank_with_suit(10, suit) == 5:
                suit_list.append(suit)

        if len(suit_list)==0:
            return 0
        else:
            cards_in_deck = deck.get_num_cards()
            return len(suit_list) * 5/cards_in_deck * 4/(cards_in_deck-1) * 3/(cards_in_deck-2) * 2/(cards_in_deck-3) * 1/(cards_in_deck-4)

    elif not cards_have_same_suit(held_cards):
        # All cards in a roayl flush must be of the same suit
        # Check if all held cards have the same suit. If not, return 0.
        return 0
    elif min(rank_list) < 10:
        # All cards in a royal flush must have rank 10 or above
        # Check if any held cards have a rank below 10. If not, return 0.
        return 0
    else:
        cards_needed = 5 - len(held_cards)
        # get number of high cards left with current suit. If number of high cards left
        # is less than number of cards needed, return 0. Otherwise compute the probability
        # of completing the hand
        cards_available = deck.get_num_cards_above_rank_with_suit(10, held_cards[0].suit)
        if cards_available < cards_needed:
            return 0
        else:
            cards_in_deck = deck.get_num_cards()
            prob = 1
            for num in range(cards_needed):
                prob *= (cards_needed - num) / (cards_in_deck - num)

            return prob

def get_straight_flush_prob(held_cards, deck):
    '''
    Calculate the probability of getting straight flush based on the current
    cards in a hand along with the cards remaining in the deck.
    '''
    if len(held_cards)==5:
        # if all cards are held, check if the hand is a straight flush. If it is,
        # return 1 otherwise return 0
        if score.score_straight_flush(held_cards) and not score.score_royal_flush(held_cards):
            return 1
        else:
            return 0
    else:
        return 0

def get_ev(held_cards, deck):
    payout_dict = {
        "royal_flush":800,
        "straight_flush":50,
        "four_of_a_kind":25,
        "full_house":9,
        "flush":6,
        "stright":4,
        "three_of_a_kind":3,
        "two_pair":2,
        "jacks_or_better":1,
    }

    probability_dict = dict()
    probability_dict["royal_flush"] = get_royal_flush_prob(held_cards, deck)
    probability_dict["straight_flush"] = get_straight_flush_prob(held_cards, deck)
    probability_dict["four_of_a_kind"] = 0
    probability_dict["full_house"] = 0
    probability_dict["flush"] = 0
    probability_dict["stright"] = 0
    probability_dict["three_of_a_kind"] = 0
    probability_dict["two_pair"] = 0
    probability_dict["jacks_or_better"] = 0

    ev = 0
    for key, value in probability_dict.items():
        ev += value * payout_dict[key]

    return ev

def analyze_hand(hand):
    '''
    This function takes a list of cards in a hand, and analyzes all of the
    possible plays. It returns a sorted list of plays from highest expected
    value to lowest expected value.
    '''

    #get possible plays for a five card hand
    plays = get_plays(5)

    # Create a deck, removing the cards from the initial hand that can
    # no longer be drawn from the deck
    exclude_cards = [str(card) for card in hand]
    deck = Deck(exclude=exclude_cards)

    ev_list = []
    # Loop over all the possible plays and get the expected value for each play
    for play in plays:
        # Create a list of held cards based on play
        held_cards = [hand[index] for index in play]

        # get the total expected value for the hand given the cards being held
        # and the cards remaining in the deck
        ev = get_ev(held_cards, deck)

        # add the ev for the hand to a list or dataframe.
        cards_str = [str(card) for card in held_cards]
        ev_list.append([cards_str, ev])

    return sorted(ev_list,key=lambda l:l[1], reverse=True)



'''
    if score.score_royal_flush(hand):
        return hand

    elif score.score_straight_flush(hand):
        return hand

    elif score.score_four_of_a_kind(hand):
        rank_count = get_rank_count(hand)

        for key, count in rank_count.items():
            if count == 4:
                rank_to_keep = key

        return [card for card in hand if card.rank == rank_to_keep]

    elif four_to_royal(hand):
        suit_count = get_suit_count(hand)
        suit_to_keep = None
        for key, count in suit_count.items():
            if count >= 4:
                suit_to_keep = key

        card_list = [card for card in hand if card.suit == suit_to_keep]
        return [card for card in card_list if (card.is_high or card.rank==10)]

    elif score.score_full_house(hand):
        return hand

    elif score.score_flush(hand):
        return hand

    elif score.score_three_of_a_kind(hand):
        rank_count = get_rank_count(hand)

        for key, count in rank_count.items():
            if count == 3:
                rank_to_keep = key

        return [card for card in hand if card.rank == rank_to_keep]

    elif score.score_straight(hand):
        return hand

    else:
        return []
'''




'''
def four_to_royal(hand):
    # must have at least four cards of the same suit
    # if there are four cards of the same suit, they must all be high cards
    suit_count = get_suit_count(hand)
    suit_to_keep = None
    for key, count in suit_count.items():
        if count >= 4:
            suit_to_keep = key

    cards_to_royal = []
    if suit_to_keep != None:
        card_list = [card for card in hand if card.suit == suit_to_keep]
        cards_to_royal = [card for card in card_list if (card.is_high or card.rank==10)]

    if len(cards_to_royal) == 4:
        return True
    else:
        return False
'''
