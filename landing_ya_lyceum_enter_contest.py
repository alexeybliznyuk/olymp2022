from sys import stdin
from itertools import chain
from collections import Counter


def getrep2(s):
    return (w for w, c in Counter(s.rstrip().split()).items() if c == 2)


a = set(chain.from_iterable(map(getrep2, stdin)))
print(*a, sep="; ")
