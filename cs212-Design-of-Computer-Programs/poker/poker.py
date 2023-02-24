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
    """
    Return a value indicating the ranking of a hand and the ranks to break a tie
    Examples:
    Straight Flush: "6C 7C 8C 9C TC" => (9, (10, 9, 8, 7, 6))
    4 of a kind: "9D 9H 9S 9C 7D" => (7, (9, 7))
    Full House: "TD TC TH 7C 7D" => (6, (10, 7))
    """
    counts, ranks = unzip(group(hand))
    if ranks == (14, 5, 4, 3, 2): ranks = (5, 4, 3, 2, 1)  # when straight, A is seen as 1
    straight = ranks[0] - ranks[-1] == 4 and len(ranks) == 5
    flush = len(set([s for r, s in hand])) == 1
    return max(count_rankings[counts], straight * 4 + 5 * flush), ranks


count_rankings = {(5, ): 10, (4, 1): 7, (3, 2): 6, (3, 1, 1): 3,
                  (2, 2, 1): 2, (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 0}


def group(cards):
    """
    returns a list of ordered pairs of counts and ranks. Highest count first, then highest rank first.
    e.g. '7 T 7 9 7' => [(count, rank), ...]: [(3, 7), (1, 10), (1, 9)]
    """
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    groups = [(ranks.count(x), x) for x in set(ranks)]
    return sorted(groups, reverse=True)


def unzip(pairs): return zip(*pairs)


