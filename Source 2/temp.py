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

print(get_plays(5))
print(len(get_plays(5)))
