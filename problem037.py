import prime
import re

# don't allow even numbers and five anywhere other than at the start of the prime
#regex = re.compile(r'0|\d2|\d4|\d5|\d6|\d8|^3$|^7$')
#primes = set(str(p) for p in prime.sieve(10**6) if not regex.findall(str(p)))

primes = set(prime.sieve(10 ** 6))
collect = set()

for p in primes:
    s = set(int(str(p)[i:]) for i in range(1, len(str(p)))).union(
        set(int(str(p)[:i]) for i in range(1, len(str(p))))
    )
    if s.intersection(primes) == s and p > 10:
        collect.add(p)
        if len(collect) == 11:
            break

print sum(collect)#, collect
