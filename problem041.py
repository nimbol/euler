import prime
#print max(p for p in prime.sieve(7654321) if ''.join(sorted(str(p))) == '1234567')

from itertools import permutations as pmt

limit = 7654321  # greatest pandigital not divisible by 3...
primes = set(p for p in prime.sieve(limit))
for n in (int(''.join(i)) for i in pmt(str(limit))):
    if n in primes:
        print n
        break