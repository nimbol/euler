from mymath import mul

result = 0

for n in xrange(23, 101):
    for r in xrange(1, n):
        if 10 ** 6 < mul(range(1,n+1)) / (mul(range(1,r+1)) * mul(range(1,n-r+1))):
            # subsequent values of r will also lead to million+
            # until you get too close to n again
            result += n - 2 * (r - 1) - 1
            break

print result
