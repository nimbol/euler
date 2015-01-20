'''
x2 - Dy2 = 1
'''

import icf

limit = 1000
squares = set(i ** 2 for i in xrange(int(limit ** 0.5) + 1))
record = dict(x=0, D=0)

for D in xrange(limit + 1):
    if D in squares:
        continue

    period_len = len(icf.repr(D)[1])
    if period_len % 2:
        # If D's period has an odd number of digits, x can apparently be found
        # in the continued fraction of sqrt(D).
        #for i in xrange(2, 100):#period_len + 2):
        i = 1
        while True:
            frac = icf.icf(D, i)
            x, y = frac.numerator, frac.denominator
            if x**2 - D * y**2 == 1:
#                print D, x, int(y)
                if x > record['x']:
                    record['x'] = x
                    record['D'] = D
                    record['i'] = i
                break
            else:
                i += 1
    else:
        pass

print record