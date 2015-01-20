from prime import sieve
from figurate_numbers import triangle
import sys

def is_prime(n):
    '''Checks if n is a prime number, caches results.'''
    return not n in non_primes

def in_triplet(i, n, t):
    '''Checks if integer i in row n of the pyramid is in a prime triplet.'''
    # Skip non-primes.
    if not is_prime(i):
        return False

    # On even line numbers, only one possible prime lines up below, and two above.
    # On odd line numbers it's vice versa.
    odd = n % 2

    # Check for directly adjacent primes.
    if odd:
        # Check number directly above.
        up = i - n + 1
        if is_prime(up):
            # Only two options: top left or top right (if they exist).
            tl = up - n + 1  # top left
            if is_prime(tl):
                return True
            tr = tl + 2  # top right
            if tr <= t[-2] and is_prime(tr):
                return True
        # Check the primes diagonally below.
        bl = i + n - 1
        if is_prime(bl):
            # Was up number prime?
            if is_prime(up):
                return True
            # Was previous i prime?
            if is_prime(i - 2):
                return True
            # Check directly below this one.
            ubl = bl + n + 1
            if is_prime(ubl):
                return True
        br = bl + 2
        if is_prime(br):
            # Were previously tested numbers prime?
            if is_prime(up) or is_prime(bl):
                return True
            # Will next i be prime?
            if is_prime(i + 2):
                return True
            # Check directly below this one.
            ubr = br + n + 1
            if is_prime(ubr):
                return True
    else:
        # Check number directly below.
        down = i + n
        if is_prime(down):
            # Only two options: bottom left+right (left only if exists).
            br = down + n + 2
            if is_prime(br):
                return True
            bl = br - 2
            if is_prime(bl):
                return True
        # Check diagonally above.
        tl = i - n
        if is_prime(tl):
            # Was straight down a prime?
            if is_prime(down):
                return True
            # Was previous i prime?
            if is_prime(i - 2):
                return True
            # Check directly above this one.
            atl = tl - n + 2
            if is_prime(atl):
                return True
        tr = tl + 2
        if is_prime(tr):
            # Were previously tested numbers prime?
            if is_prime(down) or is_prime(tl):
                return True
            # Will next i be prime?
            if is_prime(i + 2):
                return True
            # Check directly above this one.
            atr = tr - n + 2
            if is_prime(atr):
                return True
    # All options exhausted; i is not in a prime triplet.
    return False

# n accounts for the line number and the number of items per row.
args = sorted(int(i) for i in sys.argv[1:]) or [5678027, 7208785]
result = 0

primes = sieve(int(triangle(args[-1] + 2) ** 0.5) + 1)
primes.next()  # discard 2
primes = tuple(primes)

for n in args:
    # t[0] is the triangle number at the end of line n; -x for higher lines, +x for lower.
    t = dict((i, triangle(n+i)) for i in xrange(-3, 3))

    # Skip even numbers.
    istart = t[0] - n + 1
    if istart % 2 == 0:
        istart += 1

    # Performance: prefilter odd numbers that can easily be identified as non-primes.
    non_primes = set()
    for p in primes:
        # Find first "i" divisible by p.
        i = t[-3]
        mod = i % p
        if mod:
            i += p - mod
            if i % 2 == 0:
                i += p
        else:
            if i == p:
                i += 2*p
            elif i % 2 == 0:
                i += p
        non_primes.update(range(i, t[2], 2*p))

    # Test all numbers t[-1] < n < t[0]
    i = istart
    while i < t[0]:
        if in_triplet(i, n, t):
            result += i
        i += 2

print result

