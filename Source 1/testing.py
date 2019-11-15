import random
import os
import sys
from card import Card
from hand import Hand
from score import score_hand
from analyze import analyze_hand

card_list = [Card("H",10), Card("H",11), Card("H",12), Card("H",13), Card("H",14)]
print("==========")
print("Testing Royal Flush")
hand = Hand(card_list)
print("Hand: {}".format(hand))
print("Score Output: {}".format(score_hand(hand)))
print("Cards to Hold: {}".format(analyze_hand(hand)))
print("")

card_list = [Card("H",10), Card("H",11), Card("H",12), Card("H",13), Card("H",9)]
print("==========")
print("Testing Straight Flush")
hand = Hand(card_list)
print("Hand: {}".format(hand))
print("Score Output: {}".format(score_hand(hand)))
print("Cards to Hold: {}".format(analyze_hand(hand)))
print("")

card_list = [Card("H",10), Card("C",10), Card("D",10), Card("S",10), Card("H",9)]
print("==========")
print("Testing Four of a Kind")
hand = Hand(card_list)
print("Hand: {}".format(hand))
print("Score Output: {}".format(score_hand(hand)))
print("Cards to Hold: {}".format(analyze_hand(hand)))
print("")

card_list = [Card("H",10), Card("H",11), Card("H",13), Card("H",14), Card("D",3)]
print("==========")
print("Testing Four Card to a Royal")
hand = Hand(card_list)
print("Hand: {}".format(hand))
print("Score Output: {}".format(score_hand(hand)))
print("Cards to Hold: {}".format(analyze_hand(hand)))
print("")

'''
print("Analyze custom hand or quit?")
print("q: quit")
print("a: analyze hand")
command = input("> ")

while command.lower() != "q":
    hand = Hand()
    for count in range(5):
        print("Card {}:".format(count+1))
        suit = input("Enter suit (H, C, S, D): ")
        rank = input("Enter rank (2 - 14): ")
        rank = int(rank)
        hand.add_card(Card(suit, rank))

    print("")
    print("Hand: {}".format(hand))
    print("Score: {}".format(score_hand(hand)))
    print("Cards to Hold: {}".format(analyze_hand(hand)))
    print("")

    print("Analyze another hand or quit?")
    print("q: quit")
    print("a: analyze hand")
    command = input("> ")
'''
