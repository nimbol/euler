result = 0
P = 0

for p in xrange(1, 1001):
    found = 0
    for a in xrange(1, p / 4):
        for b in xrange(a, (p - a) / 2):
            if a**2 + b**2 == (p - a - b)**2:
                found += 1
    if found > result:
        result, P = found, p

print P