import prime
from mymath import mul
from itertools import combinations

# Phi of a prime = p - 1.
# Phi of p ** k = p ** k - p ** (k - 1) = p ** (k - 1) * (p - 1)
# Phi of a composite: multiply the above components.

def phi(n):
    return mul(p**(k - 1)*(p - 1) for p, k in prime.factors(n).iteritems())

record = {'n': None, 'ratio': 1}

# The more composite a number is, the lower the ratio: pregenerate composites!
primes = tuple(prime.sieve(3200))
np = 7  # number of primes in each combination
maxp = 10 ** 7 / mul(primes[:np-1])

for n in (mul(c) for c in combinations([p for p in primes if p < maxp], np)):
    print n
        # Ironically checking the rate vs the record is faster than checking whether
        # phi and n are permutations of eachother. So do that first.
#        ratio = float(phi) / n
#        if ratio < record['ratio'] and sorted(str(phi)) == sorted(str(n)):
#            record['ratio'] = ratio
#            record['n'] = n
#            print n, 'new ratio:', ratio,

#        n += 1

print record
