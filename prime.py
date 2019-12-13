# Copyright (c) 2012 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)?action=history&offset=20110413052045
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Retrieved from: http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)?oldid=17104

import random
import math
from collections import defaultdict

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def miller_rabin(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    for repeat in xrange(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

class MillerRabin(object):
    def __init__(self, a):
        self.a = sorted(a)
        
    def __call__(self, n):
        d = n - 1
        s = 0
        while d % 2 == 0:
            d >>= 1
            s += 1
            
        limit = 2 * math.log(n)**2
        for a in self.a:
            if a > limit:
                break
            if not miller_rabin_pass(a, s, d, n):
                return False
        return True
        
    @classmethod
    def factory(cls, n):
        """
        Returns a MillerRabin instance optimized to handle numbers up to n.
        """
        if n < 1373653:
            a = (2, 3)
        elif n < 9080191:
            a = (31, 73)
        elif n < 4759123141:
            a = (2, 7, 61)
        elif n < 2152302898747:
            a = (2, 3, 5, 7, 11)
        elif n < 3474749660383:
            a = (2, 3, 5, 7, 11, 13)
        elif n < 341550071728321:
            a = (2, 3, 5, 7, 11, 13, 17)
        else:
            return miller_rabin
        
        inst = MillerRabin(a)
        return inst

def sieve(limit):
    """
    Generate prime numbers below n.
    Uses a boolean array to attempt to save memory vs using ints.
    """
    yield 2  # special case
    sq_limit = int(limit ** 0.5)   # smart limit
    listlen = limit / 2 - 1
    lot = [True] * listlen # list represents 3, 5, 7, 9, etc
    n, i = 3, 0  # number and its position in the lot
    # Start sifting!
    while n <= sq_limit:
        if lot[i]:
            yield n  # n is prime, sift out multiples of n
            for pos in xrange(i + (i+1)*n, listlen, n):
                lot[pos] = False
        n += 2
        i += 1
    while i < listlen:
        if lot[i]:
            yield n
        n += 2
        i += 1

def smart_sieve(limit):
    """
    Generate a list of prime numbers below n.
    Employs a smart sieving algoritm. ;)
    Takes memory upfront, not recommended for high numbers!
    -> iter(int)
    """
    yield 2  # special case
    n = 3
    sq_limit = int(limit ** 0.5)   # smart limit
    lot = set(range(3, limit + 1, 2))  # to be sifted through
    # Sift out the table of current prime.
    while n <= sq_limit:
        if n in lot:
            yield n
            lot.remove(n)
            lot.difference_update(set(n * p * i for p in lot if p < n**2 and p >= n for i in xrange(1, limit/n)))
        n += 2
    # What's left in the lot is a bunch of primes.
    for n in sorted(lot):
        yield n

def generate():
    """
    Generate prime numbers till infinity (but probably till memory runs out).
    This method is much slower than sieving, but it doesn't use a limit.
    Useful when limit is uncertain or possibly very high.
    -> iter(int)
    """
    yield 2  # special case
    primes = []  # primes to test against, 2 excluded on purpose
    n = 3
    # test prime candidate against known primes
#    while n < 17500:
    while True:
        for prime in primes:
            if not n % prime:
                break
        else:
            yield n
            primes.append(n)
        n += 2
    # test prime candidate against known primes below sqrt(n)
    # currently I don't know from what number this starts making a difference
    while True:
        for prime in (p for p in primes if p <= int(n**0.5)):  # doesn't seem to make a difference for the first 2000 primes
            if not n % prime:
                break
        else:
            yield n
            primes.append(n)
        n += 2

def generate_and_store(primes, generator=generate()):
    """
    Stores generated primes in the supplied list before yielding them.
    Useful if you need to iterate over an unknown number of primes
    multiple times:
    >>> primes = []
    >>> pgen = generate_and_store(primes)
    >>> for n in iterable:
    ...     gen = itertools.chain(primes, pgen)
    ...     #etc
    """
    # Iterate over pregenerated primes.
    for p in primes:
        yield p

    # Figure out store method for the primes collection.
    if isinstance(primes, list):
        store = primes.append
    elif isinstance(primes, set):
        store = primes.add
    else:
        raise TypeError('No store method implemented for type: ' + str(type(primes)))

    # Iterate over newly generated primes and store them.
    for p in generator:
        store(p)
        yield p

def factors(n):
    """
    Break number n up into its prime factors.
    -> dict(prime=power)
    """
    res = defaultdict(int)
    # special-case 2
    p = 2
    while not n % p:
        n /= p
        res[p] += 1
    # start from 3, forget about generating primes; this is faster!
    p = 3
    while n > 1 and p <= n ** 0.5:
        while not n % p:
            n /= p
            res[p] += 1
        p += 2
    if n > 1:
        res[n] += 1
    return dict(res)

