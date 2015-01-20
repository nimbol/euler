import sys

from prime import sieve
from collections import defaultdict as ddict
from itertools import combinations

# group primes by permutation
pmts = ddict(list)
for p in sieve(10000):
    if p > 1000:
        key = ''.join(sorted(str(p)))
        pmts[key].append(p)

# iterate over the groups
for group in pmts.itervalues():
    # skip too small groups
    if len(group) < 3:
        continue

    # find the combination of 3 equally spaced primes
    for x, y, z in combinations(group, 3):
        if (z - y == y - x) and x != 1487:
            print x, y, z
            sys.exit()


