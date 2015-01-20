'''
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2 * 1**2
15 = 7 + 2 * 2**2
21 = 3 + 2 * 3**2
25 = 7 + 2 * 3**2
27 = 19 + 2 * 2**2
33 = 31 + 2 * 1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
'''

import prime

def generate_and_store_squares(squares):
    n = 1
    while True:
        x = n ** 2
        squares.append(x)
        yield x
        n += 1

n = 7
primes = []
squares = []
pgen = prime.generate_and_store(primes)
sgen = generate_and_store_squares(squares)

pgen.next()
sgen.next()

while True:
    n += 2

    # generate primes up to n
    while primes[-1] < n:
        pgen.next()

    # skip if n is not a composite number (n is prime)
    if n == primes[-1]:
        continue

    # generate squares up to the square root of half n
    while squares[-1] < (n / 2):
        sgen.next()

    # now try to express n as the sum of a prime and twice a square
    for sq in squares:
        if (n - 2 * sq) in primes:
            # try next n
            break
    else:
        break

print n
