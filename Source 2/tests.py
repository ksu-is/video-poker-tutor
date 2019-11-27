import unittest
from card import Card
from score import score_hand


class TestScore(unittest.TestCase):
    def setUp(self):
        self.royal_flush_hand = [Card('AS'), Card('KS'), Card('TS'), Card('QS'), Card('JS')]
        self.straight_flush_hand = [Card('9S'), Card('KS'), Card('TS'), Card('QS'), Card('JS')]
        self.flush_hand = [Card('2C'), Card('3C'), Card('KC'), Card('5C'), Card('8C')]
        self.straight_hand = [Card('AC'), Card('2S'), Card('3C'), Card('4H'), Card('5C')]
        self.full_house_hand = [Card('3C'), Card('3S'), Card('3D'), Card('8D'), Card('8H')]
        self.four_of_a_kind_hand = [Card('4S'), Card('4C'), Card('4H'), Card('4D'), Card('JC')]
        self.three_of_a_kind_hand = [Card('5D'), Card('5H'), Card('9S'), Card('5C'), Card('AS')]
        self.two_pair_hand = [Card('5D'), Card('5H'), Card('9S'), Card('9C'), Card('AS')]
        self.jacks_or_better_hand = [Card('QH'), Card('QC'), Card('5C'), Card('3S'), Card('8H')]
        self.non_winning_hand = [Card('3D'), Card('4C'), Card('6C'), Card('KC'), Card('8H')]

    def test_royal_flush(self):
        self.assertEqual(score_hand(self.royal_flush_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.straight_flush_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.flush_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.straight_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.full_house_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.two_pair_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), 'Royal Flush')
        self.assertNotEqual(score_hand(self.non_winning_hand), 'Royal Flush')

    def test_straight_flush(self):
        self.assertNotEqual(score_hand(self.royal_flush_hand), 'Straight Flush')
        self.assertEqual(score_hand(self.straight_flush_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.flush_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.straight_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.full_house_hand), 'Straight Flushh')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.two_pair_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), 'Straight Flush')
        self.assertNotEqual(score_hand(self.non_winning_hand), 'Straight Flush')

    def test_flush(self):
        self.assertNotEqual(score_hand(self.royal_flush_hand), 'Flush')
        self.assertNotEqual(score_hand(self.straight_flush_hand), 'Flush')
        self.assertEqual(score_hand(self.flush_hand), 'Flush')
        self.assertNotEqual(score_hand(self.straight_hand), 'Flush')
        self.assertNotEqual(score_hand(self.full_house_hand), 'Flush')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), 'Flush')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), 'Flush')
        self.assertNotEqual(score_hand(self.two_pair_hand), 'Flush')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), 'Flush')
        self.assertNotEqual(score_hand(self.non_winning_hand), 'Flush')

    def test_straight(self):
        self.assertNotEqual(score_hand(self.royal_flush_hand), 'Straight')
        self.assertNotEqual(score_hand(self.straight_flush_hand), 'Straight')
        self.assertNotEqual(score_hand(self.flush_hand), 'Straight')
        self.assertEqual(score_hand(self.straight_hand), 'Straight')
        self.assertNotEqual(score_hand(self.full_house_hand), 'Straight')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), 'Straight')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), 'Straight')
        self.assertNotEqual(score_hand(self.two_pair_hand), 'Straight')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), 'Straight')
        self.assertNotEqual(score_hand(self.non_winning_hand), 'Straight')

    def test_full_house(self):
        self.assertNotEqual(score_hand(self.royal_flush_hand), 'Full House')
        self.assertNotEqual(score_hand(self.straight_flush_hand), 'Full House')
        self.assertNotEqual(score_hand(self.flush_hand), 'Full House')
        self.assertNotEqual(score_hand(self.straight_hand), 'Full House')
        self.assertEqual(score_hand(self.full_house_hand), 'Full House')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), 'Full House')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), 'Full House')
        self.assertNotEqual(score_hand(self.two_pair_hand), 'Full House')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), 'Full House')
        self.assertNotEqual(score_hand(self.non_winning_hand), 'Full House')

    def test_four_of_a_kind(self):
        self.assertNotEqual(score_hand(self.royal_flush_hand), '4 of a Kind')
        self.assertNotEqual(score_hand(self.straight_flush_hand), '4 of a Kind')
        self.assertNotEqual(score_hand(self.flush_hand), '4 of a Kind')
        self.assertNotEqual(score_hand(self.straight_hand), '4 of a Kind')
        self.assertNotEqual(score_hand(self.full_house_hand), '4 of a Kind')
        self.assertEqual(score_hand(self.four_of_a_kind_hand), '4 of a Kind')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), '4 of a Kind')
        self.assertNotEqual(score_hand(self.two_pair_hand), '4 of a Kind')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), '4 of a Kind')
        self.assertNotEqual(score_hand(self.non_winning_hand), '4 of a Kind')

    def test_three_of_a_kind(self):
        self.assertNotEqual(score_hand(self.royal_flush_hand), '3 of a Kind')
        self.assertNotEqual(score_hand(self.straight_flush_hand), '3 of a Kind')
        self.assertNotEqual(score_hand(self.flush_hand), '3 of a Kind')
        self.assertNotEqual(score_hand(self.straight_hand), '3 of a Kind')
        self.assertNotEqual(score_hand(self.full_house_hand), '3 of a Kind')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), '3 of a Kind')
        self.assertEqual(score_hand(self.three_of_a_kind_hand), '3 of a Kind')
        self.assertNotEqual(score_hand(self.two_pair_hand), '3 of a Kind')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), '3 of a Kind')
        self.assertNotEqual(score_hand(self.non_winning_hand), '3 of a Kind')

    def test_two_pair(self):
        self.assertNotEqual(score_hand(self.royal_flush_hand), '2 Pair')
        self.assertNotEqual(score_hand(self.straight_flush_hand), '2 Pair')
        self.assertNotEqual(score_hand(self.flush_hand), '2 Pair')
        self.assertNotEqual(score_hand(self.straight_hand), '2 Pair')
        self.assertNotEqual(score_hand(self.full_house_hand), '2 Pair')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), '2 Pair')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), '2 Pair')
        self.assertEqual(score_hand(self.two_pair_hand), '2 Pair')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), '2 Pair')
        self.assertNotEqual(score_hand(self.non_winning_hand), '2 Pair')

    def test_jacks_or_better(self):
        self.assertNotEqual(score_hand(self.royal_flush_hand), 'Jacks or Better')
        self.assertNotEqual(score_hand(self.straight_flush_hand), 'Jacks or Better')
        self.assertNotEqual(score_hand(self.flush_hand), 'Jacks or Better')
        self.assertNotEqual(score_hand(self.straight_hand), 'Jacks or Better')
        self.assertNotEqual(score_hand(self.full_house_hand), 'Jacks or Better')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), 'Jacks or Better')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), 'Jacks or Better')
        self.assertNotEqual(score_hand(self.two_pair_hand), 'Jacks or Better')
        self.assertEqual(score_hand(self.jacks_or_better_hand), 'Jacks or Better')
        self.assertNotEqual(score_hand(self.non_winning_hand), 'Jacks or Better')

    def test_non_winning_hand(self):
        self.assertNotEqual(score_hand(self.royal_flush_hand), 'Not a Winning Hand')
        self.assertNotEqual(score_hand(self.straight_flush_hand), 'Not a Winning Hand')
        self.assertNotEqual(score_hand(self.flush_hand), 'Not a Winning Hand')
        self.assertNotEqual(score_hand(self.straight_hand), 'Not a Winning Hand')
        self.assertNotEqual(score_hand(self.full_house_hand), 'Not a Winning Hand')
        self.assertNotEqual(score_hand(self.four_of_a_kind_hand), 'Not a Winning Hand')
        self.assertNotEqual(score_hand(self.three_of_a_kind_hand), 'Not a Winning Hand')
        self.assertNotEqual(score_hand(self.two_pair_hand), 'Not a Winning Hand')
        self.assertNotEqual(score_hand(self.jacks_or_better_hand), 'Not a Winning Hand')
        self.assertEqual(score_hand(self.non_winning_hand), 'Not a Winning Hand')

if __name__ == '__main__':
    unittest.main()
