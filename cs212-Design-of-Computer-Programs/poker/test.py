
from poker import group, hand_rank, poker


class PokerTests:
    def __init__(self):
        self.sf = "6C 7C 8C 9C TC".split()  # straight flush
        self.k4 = "9D 9H 9S 9C 7D".split()  # four kind
        self.fh = "TD TC TH 7C 7D".split()  # full house
        self.tp = "5S 5D 9H 9C 6S".split()  # two pairs
        self.s1 = "AS 2S 3S 4S 5C".split()  # straight from ace
        self.s2 = "2C 3S 4S 5S 6S".split()  # simple straight
        self.ah = "AS 2S 3S 4S 6C".split()  # ace high
        self.sh = "2S 3S 4S 6C 7D".split()  # seven high

    def test_group(self):
        assert group(self.sf) == [(1, 10), (1, 9), (1, 8), (1, 7), (1, 6)]
        assert group(self.k4) == [(4, 9), (1, 7)]
        assert group(self.fh) == [(3, 10), (2, 7)]
        assert group(self.tp) == [(2, 9), (2, 5), (1, 6)]
        assert group(self.s1) == [(1, 14), (1, 5), (1, 4), (1, 3), (1, 2)]
        assert group(self.s2) == [(1, 6), (1, 5), (1, 4), (1, 3), (1, 2)]
        assert group(self.ah) == [(1, 14), (1, 6), (1, 4), (1, 3), (1, 2)]
        assert group(self.sh) == [(1, 7), (1, 6), (1, 4), (1, 3), (1, 2)]

    def test_hand_rank(self):
        assert hand_rank(self.sf) == (9, (10, 9, 8, 7, 6))
        assert hand_rank(self.k4) == (7, (9, 7))
        assert hand_rank(self.fh) == (6, (10, 7))
        assert hand_rank(self.tp) == (2, (9, 5, 6))
        assert hand_rank(self.s1) == (4, (5, 4, 3, 2, 1))
        assert hand_rank(self.s2) == (4, (6, 5, 4, 3, 2))
        assert hand_rank(self.ah) == (0, (14, 6, 4, 3, 2))
        assert hand_rank(self.sh) == (0, (7, 6, 4, 3, 2))

    def test_poker(self):
        sf, fk, fh = self.sf, self.k4, self.fh
        assert poker([sf, fk, fh]) == [sf]
        # four of a kind (fk) vs. full house (fh) returns fk.
        assert poker([fk, fh]) == [fk]
        # full house (fh) vs. full house (fh) returns fh.
        assert poker([fh, fh]) == [fh, fh]
        # single hand
        assert poker([fk]) == [fk]
        # 100 hands
        assert poker([sf] + [fk] * 99) == [sf]


test = PokerTests()
test.test_group()
test.test_hand_rank()
test.test_poker()
print('All test cases passed!')
