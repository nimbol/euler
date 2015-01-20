from prime import sieve
from prime import miller_rabin_pass as MRP
from collections import defaultdict as ddict
import math

limit = 10 ** 4
pgen = sieve(limit)

# Remove 2 and 5 from the primes list. They won't generate any concatenated
# primes and none of the concatenated primes will be equally divisible by them.
pgen.next()  # 2
pgen.next()  # 3
pgen.next()  # 5
primes = [3]

def int_concat(x, y):
    '''Concatenate integers x and y to make a new integer.'''
    return 10 ** (int(math.log10(y)) + 1) * x + y

def is_prime(n):
    # for 32-bit numbers only!
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    return MRP(2, s, d, n) and MRP(7, s, d, n) and MRP(61, s, d, n)

def pair_gen():
    # (0,1), (0,2), (1,2), (0,3), (1,3), (2,3), (0,4), ...
    i = 0
    for hi in pgen:
        i += 1
        for lo in (primes[j] for j in xrange(0, i)):
            if pair_filter(lo, hi):
                yield (lo, hi)
        primes.append(hi)

def pair_filter(lo, hi):
    return is_prime(int_concat(lo, hi)) and is_prime(int_concat(hi, lo))

def chain(key, restriction=None):
    '''
    Finds the longest path through d, with the smallest sum.
    Uses key as starting point.
    '''
    if key and key not in d:
        return [key]
        
    if restriction is None:
        allowed = d[key]
    else:
        allowed = d[key].intersection(restriction)

    if not allowed:
        return [key]

    coll = dict()
    for value in d[key]:
        if value not in allowed:
            continue
        result = chain(value, allowed)
        coll[(-len(result), sum(result))] = result
    return [key] + coll[min(coll)]

d = ddict(set)
for lo, hi in pair_gen():
    d[lo].add(hi)
#for k in sorted(d):
#    print k, sorted(d[k])

coll = dict()
for key in d:
    result = chain(key)
    coll[(-len(result), sum(result))] = result
best = coll[min(coll)]
print sum(best), best
