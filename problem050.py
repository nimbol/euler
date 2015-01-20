import prime

# no prime testing method; generate 'em all up front :(
limit = 10 ** 6
primes = sorted(set(prime.sieve(limit)))

# find the longest imaginable streak
L = 1
while sum(primes[:L]) < limit:
    L += 1

i = 0

while True:
    # sum up the longest streak that we haven't checked yet
    s = sum(primes[i:i+L])
    
    if s > limit:  # result is too high, try a smaller streak
        i = 0
        L -= 1
        continue

    if s in primes:
        break

    i += 1

print s, primes[i:i+L]

