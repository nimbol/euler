import prime
import itertools

def mul(args):
    """
    Multiply all elements of iterable args.
    -> int / float
    """
    n = 1
    for arg in args:
        n *= arg
    return n

def precise_div(n, d, p):
    """
    Return the division of n by d, with decimal precision p.
    This gets around the limitation of floats having 15 points of precision.
    -> str
    """
    result = ''
    prec = -1
    while n and p > prec:
        r, n = divmod(n, d)
        n *= 10
        result += str(r)
        prec += 1
    try:
        return '%s.%s' % (result[0], result[1:])
    except IndexError:
        return '0'

def divisors(n):
    """
    Return all the divisors of n (unordered).
    -> iter(int)
    """
    for i in xrange(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if not mod:
            yield i
            if div != i:
                yield div

def n_divisors(n):
    """
    Return the number of divisors of n.
    -> int
    """
    return len(tuple(divisors(n)))

def factorial(n):
    """
    -> n!
    Don't try this for n > 25 or so. :)
    """
    return mul(xrange(1, n + 1))

def factorial_large(n):
    """
    Should work for any n.
    -> str(n!)
    """
    i = 0
    total = 1
    zeroes = 0
    while i != n:
        i += 1
        total *= i
        while not total % 10:
            total /= 10
            zeroes += 1
    return str(total) + zeroes * '0'

def smallest_divisible(*args):
    """
    Returns the smallest number that's evenly divisible by all args.
    """
    factors = {}
    for div in args:
        for (pri, pow) in prime.factors(div).iteritems():
            if factors.get(pri) < pow:
                factors[pri] = pow

    # multiply all primes, multiplied by their powers
    total = 1
    for (pri, pow) in factors.iteritems():
        total *= pri ** pow

    return total
