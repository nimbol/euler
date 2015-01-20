import mymath

n = 10 ** 6

nchars = sum(10 ** i * (i + 1) for i in range(len(str(n)) - 1))
limit = n + (n - nchars) / len(str(n))

s = ''.join(str(i) for i in xrange(limit))
print mymath.mul(int(s[10 ** i]) for i in range(len(str(n))))