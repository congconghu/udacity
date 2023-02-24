"""
Poker game implementation
"""


def poker(hands):
    """Return a list of the winning hands: poker([hand,...]) => [hand, ...]"""
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable."""
    maxval, result = None, []
    key = key or (lambda x: x)
    for x in iterable:
        val = key(x)
        if not maxval or val > maxval:
            maxval, result = val, [x]
        elif val == maxval:
            result.append(x)
    return result


def hand_rank(hand):
    """Return a value indicating the ranking of a hand."""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):
        return 5, ranks
    elif straight(ranks):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, kind(3, ranks), ranks
    elif two_pair(ranks):
        return 2, two_pair(ranks), ranks
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks


def card_ranks(cards):
    """
    returns an ORDERED list of the ranks in a hand (where the order goes from highest to lowest rank).
    """
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks


def straight(ranks):
    """
    Return True if the ordered ranks form a 5-card straight.
    ranks is the ordered ranks of the hand from the highest rank to the lowest
    """
    for i in range(len(ranks) - 1):
        if ranks[i] - ranks[i + 1] != 1:
            return False
    return True


def flush(hand):
    """Return True if all the cards have the same suit."""
    suit = [s for r, s in hand]
    return len(set(suit)) == 1


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    highest = kind(2, ranks)
    lowest = kind(2, ranks[::-1])
    if highest and highest != lowest:
        return highest, lowest
    else:
        return None


def test():
    """Test cases for the functions in poker program"""
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    tp = "5S 5D 9H 9C 6S".split()  # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    # test straight and flush
    assert straight([9, 8, 7, 6, 5])
    assert not straight([9, 8, 8, 6, 5])
    assert flush(sf)
    assert not flush(fk)

    # test card_ranks
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    # test kind
    assert kind(4, fkranks) == 9
    assert not kind(3, fkranks)
    assert not kind(2, fkranks)
    assert kind(1, fkranks) == 7
    # test 2 pair
    assert not two_pair(fkranks)
    assert two_pair(tpranks) == (9, 5)

    # test that hand_rank works
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    assert poker([sf, fk, fh]) == [sf]
    # four of a kind (fk) vs. full house (fh) returns fk.
    assert poker([fk, fh]) == [fk]
    # full house (fh) vs. full house (fh) returns fh.
    assert poker([fh, fh]) == [fh, fh]
    # single hand
    assert poker([fk]) == [fk]
    # 100 hands
    assert poker([sf] + [fk] * 99) == [sf]

    print('All test cases passed!')


test()
