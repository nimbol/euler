'''Infinite continued fractions.'''

from fractions import Fraction
from itertools import repeat

def e(n):
    '''
    Returns step n in the infinite continued fraction of e.
    '''
    def iter_e(step):
        while step > 1:
            if step % 3:
                yield 1
            else:
                yield 2 * step / 3
            step -= 1
        yield 2
        
    if n < 1:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 3
        
    i = iter_e(n-1)
    r = 1
    step = n
    for a in i:
        step -= 1
        r = a + Fraction(1, r)

    return r

def icf(x, n):
    '''
    Approximate the square root of x by using (infinite) continued fractions.
    Returns step n in the approximation.
    Optionally you can provide an iterator i with the values for a.
    '''
    # TODO: solve this using recursion

    step = n
    if step < 1:
        return 0
    if step == 1:
        return x - 1
    
    r = Fraction(x - 1, x) #return value
    while step > 2:
        step -= 1
        r = Fraction(x - 1, 2 + r)
        
    return 1 + r


