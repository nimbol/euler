'''
By replacing the 1st digit of *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime
with this property.

Find the smallest prime which, by replacing part of the number (not necessarily
adjacent digits) with the same digit, is part of an eight prime value family.
'''

import sys
from prime import sieve
from itertools import combinations
from collections import defaultdict as ddict

# The number of digits the primes will have that we're applying our patterns to.
digits = 6

# Make patterns by indicating which digits will be replaced.
patterns = []
for i in range(digits - 1, 0, -1):
    patterns.extend(combinations(range(digits), i))

# Pregenerate a list of primes cast to strings - for pattern replacement.
limit = 10 ** digits
primes = list(str(p) for p in sieve(limit) if p > (limit / 10))
map = ddict(int)


# map primes to each pattern
for pattern in patterns:
    for p in primes:
        # compare the digits from the positions specified in pattern
        d = p[pattern[0]]
        hash = ''
#        hash = p[:pattern[0]] + '.'
        for pos in pattern:
            if p[pos] != d:
                break
            hash += p[len(hash):pos] + '.'
        else:
            # all digits in pattern are equal, score it
            hash += p[pos+1:]
            map[hash] += 1

# find highest value in map
record = (0, '')
for hash, value in map.iteritems():
    if value > record[0]:
        record = (value, hash)
    elif value == record[0] and hash < record[1]:
        record = (value, hash)

# find smallest prime that matches pattern
hash = record[1]
for i in range(10):
    p = hash.replace('.', str(i))
    if p in primes:
        print p,
