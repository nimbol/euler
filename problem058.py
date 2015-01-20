import prime
import sys

primes = []
primegen = prime.generate()
primegen.next()  # discard 2
primes.append(primegen.next())  # primes list can't be empty

hits = 3
side = 3
ratio = 60

while ratio >= 10:
    side += 2
    while primes[-1] < side - 2:
        primes.append(primegen.next())
    for corner in ((side**2 - i*(side - 1)) for i in (1,2,3)):
        for p in primes:
            if not corner % p:
                break
        else:
            hits += 1
    ratio = 100 * float(hits) / (2 * (side - 1) + 1)

print side

