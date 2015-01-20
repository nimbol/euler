import prime

limit = 5 * 10**7
primes = tuple(prime.sieve(int(limit**0.5) + 1))
squares = tuple(p**2 for p in primes)
trips = tuple(p**3 for p in primes if p**3 < limit)
quads = tuple(p**4 for p in primes if p**4 < limit)

result = set()

for a in squares:
    for b in trips:
        ab = a + b
        if ab > limit - quads[0]:
            break
        for c in quads:
            n = ab + c
            if n > limit:
                break
            result.add(n)

print len(result)
