from prime import factors
from mymath import mul

limit = 10**6 + 1

print sum(
    mul(
#        x**y - x**(y-1) for x, y in factors(d).iteritems()
        x**(y-1) * (x-1) for x, y in factors(d).iteritems()
    ) for d in xrange(2, limit)
)
