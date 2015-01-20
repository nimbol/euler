import time
_t = time.time()

for a in xrange(1, 1000):
    for b in xrange(a, 1000):
        cc = (a**2 + b**2) ** 0.5
        c = int(cc)
        if c != cc:
            continue
        s = sum([a, b, c])
        if s > 1000:
            break
        if s == 1000:
            print a * b * c, (a, b, c)

print time.time() - _t
