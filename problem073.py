from fractions import gcd

limit = 12000
result = 0

for d in xrange(limit, 4, -1):

    minimum = d / 3 + 1
    maximum = (d + 1) / 2

    if d % 2 == 0:
        step = 2
        if minimum % 2 == 0:
            minimum += 1
    else:
        step = 1

    for n in xrange(minimum, maximum, step):
        if gcd(n, d) == 1:
            result += 1

print (result)
