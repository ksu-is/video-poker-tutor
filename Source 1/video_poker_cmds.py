import random
import os
import sys
from card import Card
from deck import Deck
from hand import Hand
from score import score_hand

'''
counts = dict()
for iter in range(1000000):
    deck = Deck()
    hand = Hand(deck, 5)
    #print(hand)
    score = score_hand(hand)
    #print(iter, score)
    counts[score] = counts.get(score, 0) + 1

print(counts)
'''

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

os.system('clear')
print('''
Welcome to Python Video Poker!
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
    num_cards = 5

    while (command.lower() != 'q') and (total_credits>0):
        os.system('clear')

        total_credits -= bet * credit_value
        print('Total credits: ${0:0.2f}'.format(total_credits))
        print('')

        deck = Deck()
        hand = Hand()
        for _ in range(num_cards):
            hand.draw_card(deck)

        print("Select cards to hold separated by a space")
        print('Hit return to discard all')
        print(hand)
        print('[1] [2] [3] [4] [5]')
        print('')
        hold_cards = input('> ')
        if len(hold_cards) == 0:
            hold_cards = []
        else:
            hold_cards = hold_cards.split(" ")
            hold_cards = [int(val)-1 for val in hold_cards]

        for index in range(5):
            pos = 4 - index
            if pos not in hold_cards:
                hand.discard(pos)
        for _ in range(5 - len(hold_cards)):
            hand.draw_card(deck)

        print(hand)
        score = score_hand(hand)
        print(score)
        total_credits += pay_table[score] * bet * credit_value
        print('Total credits: ${0:0.2f}'.format(total_credits))
        print("Press enter to play again, q to quit:")
        command = input('> ')

mode = 0
# 0: round start
# 1: cards dealt for round 1
# 2: cards dealt for round 2, 
def round_start ():
    deck = Deck()
    hand = Hand()
    for _ in range(num_cards):
        hand.draw_card(deck)
    hold_cards = [True, True, True, True, True]
    mode = 1
    
def hold(num):
    num = int(num)
    if (num>= 0 & num<=4):
        hold_cards[num] = not hold_cards[num]
def judge():
    for index in range(5):
        if not hold_cards[index]:
            hand.discard(index)
    #update hand GUI
    score = score_hand(hand)
    #to do: convert change score_hand into an array output in the format [score_name,score]
    
