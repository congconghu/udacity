"""
Simulate hand of poker games
"""
import random
from poker import hand_rank

hand_names = ['',
              'Straight Flush',
              '',
              '4 Kind',
              'Full House',
              'Flush',
              'Straight',
              '3 Kind',
              '2 Pair',
              'Pair',
              'High Card']


def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[i * n: (i + 1) * n] for i in range(numhands)]


def hand_percentages(n=700*1000):
    counts = [0] * 11
    for _ in range(n // 10):
        for hand in deal(10):
            rank = hand_rank(hand)
            counts[rank[0]] += 1
    for i, count in enumerate(counts[::-1]):
        print('{:14s}: {:6.4f}%'.format(hand_names[i], 100 * count / n))


hand_percentages()

