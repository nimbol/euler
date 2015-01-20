'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2 ** 2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct primes factors.
What is the first of these numbers?
'''

import prime

n = 1
streak = 0
target = 4

while True:
    if len(prime.factors(n)) == target:
        streak += 1
        if streak == target:
            break
    else:
        streak = 0
    n += 1

print n - target + 1
