import random
import os
import sys
from card import Card
from deck import Deck
from hand import Hand
from score import score_hand

class Game():
    def __init__(self, cards_list = None):
        self.mode = 0
        self.win_hand = 0
        # 0: round start, valid bet             # place_bet()
        # 1: cards dealt for round 1            # round_start()
        # 2: cards dealt for round 2            # judge()
        # 3: round end, everything finalized    # payout()

        # default variables
        self.total_credits = 20.00
        self.bet = 5
        self.credit_value = 0.25
        self.hold_cards = [False, False, False, False, False]
        self.deck = Deck()
        self.hand = Hand()


    def place_bet(self):
        if (self.bet <= self.total_credits):
            self.total_credits -= self.bet
            return True
        else:
            return False
            
    def set_bet(self, new_bet):
        if (new_bet <= self.total_credits):
            self.bet = self.bet

    def round_start(self):
        self.deck = Deck()
        self.hand = Hand()
        for _ in range(5):
            self.hand.draw_card(self.deck)
        self.hold_cards = [False, False, False, False, False]


    def hold(self, num):
        num = int(num)
        if (num >= 1 & num <= 5):
            self.hold_cards[num-1] = not self.hold_cards[num-1]


    def judge(self):
        #print(self.hold_cards)
        for index in range(4, -1, -1):
            #print(index, self.hold_cards[index])
            if self.hold_cards[index] == False:
                #print("Attempting to discard #", str(index))
                #print(self.hand)
                self.hand.discard(index)
                #print("Success:\t", self.hand)
            #else:
                #print("Not attempting to discard #", str(index))
        print("Length:\t", (5 - self.hand.length()))
        for _ in range(5 - self.hand.length()):
            self.hand.draw_card(self.deck)
        # update hand GUI
        score = score_hand(self.hand)
        # to do: convert change score_hand into an array output in the format [score_name,score])
        return score


    def test_class(self):
        #Def
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
            if (self.set_bet(5)):
                #nothing
                i = True
            else:
                self.total_credits = 20
                self.set_bet(5)
            self.credit_value = 0.25
            while (command.lower() != 'q') and (self.total_credits > 0):
                os.system('clear')
                self.round_start()
                self.total_credits -= self.bet * self.credit_value
                print('Total credits: ${0:0.2f}'.format(self.total_credits))
                print('')
                self.round_start()
                print("Select cards to hold separated by a space")
                print('Hit return to discard all')
                print(self.hand)
                print('[1] [2] [3] [4] [5]')
                print('')
                # Using original implementation of hold command for this test
                temp_cards = input('> ')
                self.hold_cards = [False, False, False, False, False]

                #Debug
                

                if len(temp_cards) == 0:
                    self.hold_cards = [False, False, False, False, False]
                else:
                    temp_cards = temp_cards.split(" ")
                    print(temp_cards, len(temp_cards))
                    for i in range(5,0,-1):
                        print("Test:\t", temp_cards, "\t", i)
                        if temp_cards.count(str(i)) > 0:
                            self.hold_cards[i-1] = True
                #End original implementation
                result = self.judge()
                print("Cards:", self.hand)
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
                self.total_credits += pay_table[result] * self.bet * self.credit_value
                print('Total credits: ${0:0.2f}'.format(self.total_credits))
                print("Press enter to play again, q to quit:")
                command = input('> ')