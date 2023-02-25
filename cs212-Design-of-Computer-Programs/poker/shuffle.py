"""
Compare shuffle algorithms
"""
import random
from collections import defaultdict
from math import factorial


def swap(deck, i, j):
    """
    Swap cards at position i and j in the deck.
    """
    deck[i], deck[j] = deck[j], deck[i]


def shuffle(deck):
    """
    Good shuffle algorithm: linear time complexity and shuffle result has uniform distribution..
    """
    n = len(deck)
    for i in range(n-1):
        swap(deck, i, random.randrange(i, n))


def shuffle1(deck):
    """
    Bad shuffle algorithm: randomly swap 2 cards until all cards have been swapped at least once.
    The shuffle can continue forever and the shuffle result does not have uniform distribution.
    """
    n = len(deck)
    swapped = [False] * len(deck)
    while not all(swapped):
        i, j = random.randrange(n), random.randrange(n)
        swapped[i] = swapped[j] = True
        swap(deck, i, j)


def shuffle2(deck):
    """
    Modified shuffle from shuffle 1. Time complexity O(n^2), correct result.
    """
    n = len(deck)
    swapped = [False] * len(deck)
    while not all(swapped):
        i, j = random.randrange(n), random.randrange(n)
        swapped[i] = True
        swap(deck, i, j)


def shuffle3(deck):
    """
    Modified from the Good shuffle algorithm: linear time complexity, but wrong shuffle result.
    What is wrong:
    When shuffling 3 item, there will be 3*3*3 shuffle orders with equal probability, producing 6 patterns.
    So each pattern will not appear with equal probability.
    """
    n = len(deck)
    for i in range(n):
        swap(deck, i, random.randrange(n))


def test_shuffler(shuffler, deck='abc', n=10*1000):
    """
    Test shuffler to see if they give equal distribution of all possible shuffle results.
    """
    counts = defaultdict(int)
    for _ in range(n):
        input_deck = list(deck)
        shuffler(input_deck)
        counts[''.join(input_deck)] += 1
    e = 1 / factorial(len(deck)) * n  # expected counts of each result
    okay = all((e * .9 < count < e * 1.1 for count in counts.values()))
    name = shuffler.__name__
    print('{name}({deck}) {okay}'.format(name=name, deck=deck, okay='ok' if okay else '*** BAD ***'))
    for item, count in sorted(counts.items()):
        print('{item}: {prob:4.3}%'.format(item=item, prob=count/n*100), end='  ')
    print('')


def test_shufflers(shufflers=[shuffle, shuffle1, shuffle2, shuffle3], decks=['ab', 'abc']):
    for deck in decks:
        for shuffler in shufflers:
            test_shuffler(shuffler, deck=deck)


test_shufflers()

