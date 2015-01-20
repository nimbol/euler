'''Infinite continued fractions.'''

from fractions import Fraction

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
    for a in i:
        r = a + Fraction(1, r)

    return r

def icf(x, n):
    '''
    Approximate the square root of x by using (infinite) continued fractions.
    Returns step n in the approximation (1-based).
    '''
    a = repr(x)
    a0 = a[0]
    a = a[1]
    period_len = len(a)

    step = n - 1  # remove the -1 to make it 0-based, it will still work (with changed input)
    if step < 0:
        return 0
    
    result = 0
    while step > 0:
        step -= 1
        pos = step % period_len  # position of a in the period
        result = Fraction(1, a[pos] + result)
        
    return Fraction(a0) + result

def repr(S):
    '''Return a representation of the continued fraction of sqrt(S).'''
    a = _geta(S)
    return [a[0], tuple(a[1:-1])]

def _geta(S):
    '''Get a[0..r] of sqrt(S).'''
    m = [0]
    d = [1]
    a = [int(S**.5)]
    n = 0
    while n < 2 or (m[n], d[n], a[n]) != (m[1], d[1], a[1]):
#        print m[n], d[n], a[n]
        m.append( d[n]*a[n] - m[n] )
        d.append( (S - m[n+1]**2)/d[n] )
        if d[-1] == 0:
            break
        a.append( int((S**.5 + m[n+1])/d[n+1]) )
        n += 1
    return a
