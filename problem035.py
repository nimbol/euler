import prime
import re

regex = re.compile(r'0|2|4|5|6|8')
primes = set(str(p) for p in prime.sieve(10**6) if not regex.findall(str(p)))
collect = set([2, 5])

for p in primes:
    for i in xrange(1, len(p)):
        if p[i:] + p[:i] not in primes:
            break
    else:
        collect.add(p)

print len(collect)
