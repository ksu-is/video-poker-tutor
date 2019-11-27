import random
import os
import sys
from card import Card
from deck import Deck
from hand import Hand
from score import score_hand


mode = 0
win_hand = 0
# 0: round start, valid bet             # place_bet()
# 1: cards dealt for round 1            # round_start()
# 2: cards dealt for round 2            # judge()
# 3: round end, everything finalized    # payout()

# default variables
total_credits = 20.00
bet = 5
credit_value = 0.25
hold_cards = [False, False, False, False, False]
deck = Deck()
hand = Hand()


def place_bet():
    global total_credits
    if (bet <= total_credits):
        total_credits -= bet
        bet = bet
    # else:
        # throw error?


def round_start():
    global deck
    global hand
    deck = Deck()
    hand = Hand()
    for _ in range(5):
        hand.draw_card(deck)
    hold_cards = [False, False, False, False, False]


def hold(num):
    num = int(num)
    if (num >= 1 & num <= 5):
        hold_cards[num-1] = not hold_cards[num-1]


def judge():
    global hand
    global hold_cards
    for index in range(5):
        if not hold_cards[index]:
            hand.discard(index)
    for _ in range(5 - len(hold_cards)):
        hand.draw_card(deck)
    # update hand GUI
    score = score_hand(hand)
    # to do: convert change score_hand into an array output in the format [score_name,score])
    mode = 3
    return score


def test_class():
    #Def
    global total_credits
    global bet
    global credit_value
    global hold_cards
    global deck
    global hand
    
    os.system('clear')
    print('''
    Testing Video Poker Terminal Version!
    ==============================

    Please enter a command:
    q - quit
    n - new game
    ''')
    command = input('> ')
    if command.lower() == 'q':
        sys.exit()
    else:
        total_credits = 20.00
        bet = 5
        credit_value = 0.25
        while (command.lower() != 'q') and (total_credits > 0):
            os.system('clear')
            round_start()
            total_credits -= bet * credit_value
            print('Total credits: ${0:0.2f}'.format(total_credits))
            print('')
            round_start()
            print("Select cards to hold separated by a space")
            print('Hit return to discard all')
            print(hand)
            print('[1] [2] [3] [4] [5]')
            print('')
            # Using original implementation of hold command for this test
            temp_cards = input('> ')
            hold_cards = [False, False, False, False, False]

            if len(temp_cards) == 0:
                hold_cards = [False, False, False, False, False]
            else:
                temp_cards = temp_cards.split(" ")
                temp_cards = [int(val)-1 for val in hold_cards]
                for i in range(5):
                    if temp_cards.count(i) > 0:
                        hold_cards[i-1] = True
            #End original implementation
            result = judge()
            print(hand)
            pay_table = {
                "Royal Flush": 800,
                "Straight Flush": 50,
                "4 of a Kind": 25,
                "Full House": 9,
                "Flush": 6,
                "Straight": 4,
                "3 of a Kind": 3,
                "2 Pair": 2,
                "Jacks or Better": 1,
                "Not a Winning Hand": 0,
            }
            total_credits += pay_table[result] * bet * credit_value
            print('Total credits: ${0:0.2f}'.format(total_credits))
            print("Press enter to play again, q to quit:")
            command = input('> ')
test_class()